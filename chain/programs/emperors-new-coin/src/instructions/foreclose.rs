//! Take the flag back.
//!
//! Permissionless, and paid: the caller collects a bounty from the vault, so
//! nobody has to run a bot out of civic duty. Foreclosure is the other half of
//! the rent engine — without it, an unpayable debt would simply sit there and
//! the asset would never return to circulation.
//!
//! The condition is deliberately narrow. Debt has to exceed what the holder
//! could pay *and* grace has to have elapsed, so an ordinary holder who is
//! merely late is safe, and a holder who can cover the debt cannot be
//! foreclosed at all — anyone wanting them out can call `settle_rent` instead,
//! which is what the debt is for.
use anchor_lang::prelude::*;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::{transfer, Mint, Token, TokenAccount, Transfer};
use anchor_spl::token_2022::Token2022;
use anchor_spl::token_interface::{
    transfer_checked, Mint as MintInterface, TokenAccount as TokenAccountInterface, TransferChecked,
};

use crate::errors::EncError;
use crate::instructions::settle_rent::rent_due;
use crate::state::*;

#[event]
pub struct Foreclosed {
    pub index: u8,
    pub former_holder: Pubkey,
    pub caller: Pubkey,
    /// The debt written off when the asset went back to the vault.
    pub debt: u64,
    pub bounty: u64,
}

pub fn handler(ctx: Context<Foreclose>, _index: u8) -> Result<()> {
    let now = Clock::get()?.unix_timestamp;
    let vault = ctx.accounts.vault.key();
    let config = &ctx.accounts.config;

    require_keys_neq!(ctx.accounts.asset.holder, vault, EncError::VaultHoldsAsset);

    let debt = rent_due(&ctx.accounts.asset, config.rent_rate_per_day_bps, now)?;
    let balance = ctx.accounts.holder_token_account.amount;

    // Two conditions, both required. Either alone would be wrong: without the
    // balance test a solvent holder could be evicted by anyone willing to wait,
    // and without grace a holder would lose the asset the instant they dipped
    // below the running total.
    require!(debt > balance, EncError::NotForeclosable);
    require!(
        now.saturating_sub(ctx.accounts.asset.last_touched) >= config.grace_seconds,
        EncError::NotForeclosable
    );

    // Move the NFT back with the permanent delegate. No signature from the
    // holder, which is the whole point of the extension — and the reason the
    // asset is "always for sale" rather than "for sale if they feel like it".
    let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];
    transfer_checked(
        CpiContext::new_with_signer(
            ctx.accounts.token_2022_program.key(),
            TransferChecked {
                from: ctx.accounts.holder_nft_account.to_account_info(),
                mint: ctx.accounts.asset_mint.to_account_info(),
                to: ctx.accounts.vault_nft_account.to_account_info(),
                authority: ctx.accounts.vault.to_account_info(),
            },
            &[vault_seeds],
        ),
        1,
        0,
    )?;

    // The bounty comes out of the vault, capped at what it actually holds so a
    // depleted vault cannot make foreclosure impossible — the asset must come
    // home either way.
    let bounty = config.foreclose_bounty.min(ctx.accounts.vault_token_account.amount);
    if bounty > 0 {
        transfer(
            CpiContext::new_with_signer(
                ctx.accounts.token_program.key(),
                Transfer {
                    from: ctx.accounts.vault_token_account.to_account_info(),
                    to: ctx.accounts.caller_token_account.to_account_info(),
                    authority: ctx.accounts.vault.to_account_info(),
                },
                &[vault_seeds],
            ),
            bounty,
        )?;
    }

    let former_holder = ctx.accounts.asset.holder;
    let asset = &mut ctx.accounts.asset;
    asset.holder = vault;
    // The debt dies with the tenancy. Carrying it forward would mean the next
    // holder inherits a stranger's arrears, and keeping a ledger of it would
    // mean tracking a receivable against a wallet that has already walked away.
    asset.rent_accrued = 0;
    asset.last_touched = now;

    emit!(Foreclosed {
        index: asset.index,
        former_holder,
        caller: ctx.accounts.caller.key(),
        debt,
        bounty,
    });
    msg!("asset {} foreclosed, {debt} written off", asset.index);
    Ok(())
}

#[derive(Accounts)]
#[instruction(index: u8)]
pub struct Foreclose<'info> {
    /// Anyone. They pay the fees and collect the bounty.
    #[account(mut)]
    pub caller: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(mut, seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Account<'info, Asset>,

    /// CHECK: signer-only PDA; permanent delegate over the NFT and owner of the
    /// vault's token accounts.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    #[account(address = config.mint)]
    pub mint: Account<'info, Mint>,

    #[account(mut, seeds = [ASSET_MINT_SEED, &[index]], bump)]
    pub asset_mint: InterfaceAccount<'info, MintInterface>,

    #[account(
        mut,
        constraint = holder_nft_account.owner == asset.holder @ EncError::WrongHolderAccount,
        constraint = holder_nft_account.mint == asset_mint.key() @ EncError::WrongHolderAccount,
    )]
    pub holder_nft_account: InterfaceAccount<'info, TokenAccountInterface>,

    #[account(
        mut,
        associated_token::mint = asset_mint,
        associated_token::authority = vault,
        associated_token::token_program = token_2022_program,
    )]
    pub vault_nft_account: InterfaceAccount<'info, TokenAccountInterface>,

    /// The holder's ENC account — read to decide whether they could have paid.
    #[account(
        token::mint = mint,
        constraint = holder_token_account.owner == asset.holder @ EncError::WrongHolderAccount,
    )]
    pub holder_token_account: Account<'info, TokenAccount>,

    #[account(
        mut,
        associated_token::mint = mint,
        associated_token::authority = vault,
    )]
    pub vault_token_account: Account<'info, TokenAccount>,

    /// Created if absent so a first-time forecloser still gets paid.
    #[account(
        init_if_needed,
        payer = caller,
        associated_token::mint = mint,
        associated_token::authority = caller,
    )]
    pub caller_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
    pub token_2022_program: Program<'info, Token2022>,
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
}
