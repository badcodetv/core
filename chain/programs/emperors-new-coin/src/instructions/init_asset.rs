//! Create one of the ten parody assets.
//!
//! Called ten times, once per transaction. **Split deliberately:** doing all ten
//! in one instruction is roughly forty accounts, past both the 200k compute
//! limit and the 1232-byte transaction limit — it cannot be made to fit, so
//! there is no point trying.
//!
//! Each asset is a Token-2022 NFT with **metadata pointer** aimed at the mint
//! itself, plus **embedded metadata** — so a wallet renders a name and a
//! picture rather than an anonymous token.
//!
//! **There is deliberately no permanent delegate.** It was here to make a
//! forced sale possible, which Ruling A (2026-08-12) removed: the ten NFTs
//! never leave this program's custody, so no wallet exists to reach into and
//! the power would have been dead weight — while costing the heaviest flag a
//! risk scanner issues (`"Permanent Control Enabled"`, danger, weight 50000).
//! Dropping it is what makes "no token leaves any wallet without its owner's
//! signature" structurally true rather than merely intended.
//!
//! After minting the single unit, the mint authority is set to `None`, which is
//! what makes it permanently a *non*-fungible token.
use anchor_lang::prelude::*;
use anchor_lang::system_program::{transfer, Transfer};
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token_2022::spl_token_2022::instruction::AuthorityType;
use anchor_spl::token_2022::Token2022;
use anchor_spl::token_interface::{
    mint_to, set_authority, spl_pod::optional_keys::OptionalNonZeroPubkey,
    spl_token_metadata_interface::state::TokenMetadata, token_metadata_initialize, Mint, MintTo,
    SetAuthority, TokenAccount, TokenMetadataInitialize,
};
// Brought in only for `get_packed_len` on TokenMetadata: the metadata is
// variable length, so its size can only be known from the actual strings.
use spl_type_length_value::variable_len_pack::VariableLenPack;

use crate::errors::EncError;
use crate::state::*;

pub fn handler(
    ctx: Context<InitAsset>,
    index: u8,
    name: String,
    symbol: String,
    uri: String,
    genesis_price: u64,
) -> Result<()> {
    require!(index < ASSET_COUNT, EncError::InvalidAssetIndex);
    // Sequential rather than any-order. `init` on the Asset PDA already makes a
    // repeat impossible; requiring order on top of it means `initialized_assets`
    // is exactly "how many exist", which `sync_m2` relies on rather than having
    // to go and count.
    require!(
        ctx.accounts.config.initialized_assets == index,
        EncError::AssetOutOfOrder
    );

    let now = Clock::get()?.unix_timestamp;
    let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];

    // ── Metadata, embedded in the mint ──────────────────────────────────────
    // The metadata extension is variable length and is appended to the mint
    // account, so the account has to be able to pay rent for the extra bytes
    // *before* the token program writes them. Anchor's `init` sized the account
    // for the fixed extensions only, so top it up here or the CPI fails with a
    // rent error that names nothing useful.
    let metadata = TokenMetadata {
        update_authority: OptionalNonZeroPubkey::try_from(Some(ctx.accounts.vault.key()))?,
        mint: ctx.accounts.asset_mint.key(),
        name: name.clone(),
        symbol: symbol.clone(),
        uri: uri.clone(),
        ..Default::default()
    };
    // Four bytes of extension header (type + length) plus the payload.
    let extra = 4 + metadata.get_packed_len()?;
    let mint_info = ctx.accounts.asset_mint.to_account_info();
    let needed = Rent::get()?.minimum_balance(mint_info.data_len() + extra);
    let held = mint_info.lamports();
    if needed > held {
        transfer(
            CpiContext::new(
                ctx.accounts.system_program.key(),
                Transfer {
                    from: ctx.accounts.authority.to_account_info(),
                    to: mint_info.clone(),
                },
            ),
            needed - held,
        )?;
    }

    token_metadata_initialize(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            TokenMetadataInitialize {
                program_id: ctx.accounts.token_program.to_account_info(),
                metadata: mint_info.clone(),
                update_authority: ctx.accounts.vault.to_account_info(),
                mint: mint_info.clone(),
                mint_authority: ctx.accounts.vault.to_account_info(),
            },
            &[vault_seeds],
        ),
        name.clone(),
        symbol,
        uri,
    )?;

    // ── The single unit ─────────────────────────────────────────────────────
    mint_to(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            MintTo {
                mint: mint_info.clone(),
                to: ctx.accounts.vault_nft_account.to_account_info(),
                authority: ctx.accounts.vault.to_account_info(),
            },
            &[vault_seeds],
        ),
        1,
    )?;

    // Supply is now fixed at one, forever. Without this the "NFT" is just a
    // token the program could print more of, and every wallet would render it
    // as a balance rather than as a thing.
    set_authority(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            SetAuthority {
                current_authority: ctx.accounts.vault.to_account_info(),
                account_or_mint: mint_info.clone(),
            },
            &[vault_seeds],
        ),
        AuthorityType::MintTokens,
        None,
    )?;

    // ── The asset's own state ───────────────────────────────────────────────
    let asset = &mut ctx.accounts.asset;
    asset.index = index;
    // The Emperor holds it until somebody buys it.
    asset.holder = ctx.accounts.vault.key();
    asset.price_from = genesis_price;
    asset.price_to = genesis_price;
    asset.interp_start = now;
    asset.interp_end = now;
    // Term 0 is the Emperor's own, and it starts ticking immediately — so the
    // first auction can be settled a term after the coin exists, with no
    // separate "open the market" instruction to forget to call.
    asset.term_number = 0;
    asset.term_ends_at = now
        .checked_add(ctx.accounts.config.term_seconds)
        .ok_or(error!(EncError::MathOverflow))?;
    asset.high_bid = 0;
    asset.high_bidder = Pubkey::default();
    asset.bump = ctx.bumps.asset;

    ctx.accounts.config.initialized_assets = index + 1;

    msg!("asset {index} \"{name}\" minted to the vault at {genesis_price}");
    Ok(())
}

#[derive(Accounts)]
#[instruction(index: u8)]
pub struct InitAsset<'info> {
    #[account(mut)]
    pub authority: Signer<'info>,

    /// CHECK: paired with `program_data` to prove `authority` may upgrade this
    /// program — the same gate as `initialize`.
    #[account(constraint = program.programdata_address()? == Some(program_data.key()))]
    pub program: Program<'info, crate::program::EmperorsNewCoin>,

    #[account(constraint = program_data.upgrade_authority_address == Some(authority.key()) @ EncError::NotUpgradeAuthority)]
    pub program_data: Account<'info, ProgramData>,

    #[account(mut, seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    /// CHECK: signer-only PDA; mint authority and custodian of every asset.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    #[account(
        init,
        payer = authority,
        space = 8 + Asset::INIT_SPACE,
        seeds = [ASSET_SEED, &[index]],
        bump,
    )]
    pub asset: Account<'info, Asset>,

    /// The NFT.
    ///
    /// `metadata_address` points at the mint itself, which is what "embedded
    /// metadata" means: there is no separate metadata account to lose.
    #[account(
        init,
        payer = authority,
        mint::decimals = 0,
        mint::authority = vault,
        mint::token_program = token_program,
        extensions::metadata_pointer::authority = vault,
        extensions::metadata_pointer::metadata_address = asset_mint,
        seeds = [ASSET_MINT_SEED, &[index]],
        bump,
    )]
    pub asset_mint: InterfaceAccount<'info, Mint>,

    #[account(
        init,
        payer = authority,
        associated_token::mint = asset_mint,
        associated_token::authority = vault,
        associated_token::token_program = token_program,
    )]
    pub vault_nft_account: InterfaceAccount<'info, TokenAccount>,

    pub token_program: Program<'info, Token2022>,
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
}
