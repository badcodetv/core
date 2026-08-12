//! Issue the tenancy certificate — the only thing a holder ever actually owns.
//!
//! You never really owned the asset. All you keep is the receipt. That is the
//! Emperor's New Clothes exactly: the magnificent thing was never yours, and
//! what you are left with is documentation that you were there.
//!
//! **Immutable at issue, structurally rather than by restraint.** The mint
//! authority is dropped after the single unit, there is no freeze authority,
//! and the metadata's update authority is set to `None` in this same
//! instruction. Its "stub" state is *derived* — the certificate's term number
//! stops matching the asset's — so no later instruction has to leave it alone;
//! none exists that could touch it.
//!
//! Seeds are `(asset, term)`, so a term issues exactly one certificate, ever,
//! and it can never be reissued. Anyone may pay to mint it; it always lands in
//! the current holder's wallet, never the caller's.
use anchor_lang::prelude::*;
use anchor_lang::system_program::{transfer, Transfer};
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token_2022::spl_token_2022::instruction::AuthorityType;
use anchor_spl::token_2022::Token2022;
use anchor_spl::token_interface::{
    mint_to, set_authority, spl_pod::optional_keys::OptionalNonZeroPubkey,
    spl_token_metadata_interface::state::TokenMetadata, token_metadata_initialize,
    token_metadata_update_authority, Mint, MintTo, SetAuthority, TokenAccount,
    TokenMetadataInitialize, TokenMetadataUpdateAuthority,
};
use spl_type_length_value::variable_len_pack::VariableLenPack;

use crate::errors::EncError;
use crate::state::*;

pub fn handler(ctx: Context<MintCertificate>, index: u8, term: u64) -> Result<()> {
    let asset = &ctx.accounts.asset;

    // Only the tenancy that is actually running, and only for a real tenant.
    // The Emperor gets no receipt: he never won anything.
    require!(term == asset.term_number, EncError::NoCertificateDue);
    require!(
        asset.holder != ctx.accounts.vault.key(),
        EncError::NoCertificateDue
    );
    require!(
        ctx.accounts.holder.key() == asset.holder,
        EncError::WrongHolderAccount
    );

    let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];
    let name = format!("ENC Tenancy {index} — Term {term}");
    let symbol = String::from("ENCTEN");
    let uri = String::new();

    let metadata = TokenMetadata {
        update_authority: OptionalNonZeroPubkey::try_from(Some(ctx.accounts.vault.key()))?,
        mint: ctx.accounts.cert_mint.key(),
        name: name.clone(),
        symbol: symbol.clone(),
        uri: uri.clone(),
        ..Default::default()
    };
    // Same rent top-up as `init_asset`: Anchor sized the account for the fixed
    // extensions only, and the metadata is appended afterwards.
    let extra = 4 + metadata.get_packed_len()?;
    let mint_info = ctx.accounts.cert_mint.to_account_info();
    let needed = Rent::get()?.minimum_balance(mint_info.data_len() + extra);
    let held = mint_info.lamports();
    if needed > held {
        transfer(
            CpiContext::new(
                ctx.accounts.system_program.key(),
                Transfer {
                    from: ctx.accounts.payer.to_account_info(),
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

    mint_to(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            MintTo {
                mint: mint_info.clone(),
                to: ctx.accounts.holder_cert_account.to_account_info(),
                authority: ctx.accounts.vault.to_account_info(),
            },
            &[vault_seeds],
        ),
        1,
    )?;

    // Supply fixed at one, forever.
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

    // And the words are fixed too. Unlike `init_asset`, which keeps the vault
    // as metadata update authority, a certificate is a record of something that
    // happened — a record that could be rewritten later is not a record.
    token_metadata_update_authority(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            TokenMetadataUpdateAuthority {
                program_id: ctx.accounts.token_program.to_account_info(),
                metadata: mint_info.clone(),
                current_authority: ctx.accounts.vault.to_account_info(),
                new_authority: ctx.accounts.none_authority.to_account_info(),
            },
            &[vault_seeds],
        ),
        OptionalNonZeroPubkey::default(),
    )?;

    msg!("asset {index} term {term}: certificate issued to {}", asset.holder);
    Ok(())
}

#[derive(Accounts)]
#[instruction(index: u8, term: u64)]
pub struct MintCertificate<'info> {
    /// Anyone. The certificate lands in the holder's wallet regardless.
    #[account(mut)]
    pub payer: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Account<'info, Asset>,

    /// CHECK: pinned to the asset's recorded holder by the handler.
    pub holder: UncheckedAccount<'info>,

    /// CHECK: signer-only PDA; mint authority for the certificate.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    /// CHECK: the all-zero key, which is how the token metadata interface
    /// encodes "no update authority". The System Program's id *is* that key.
    #[account(address = Pubkey::default())]
    pub none_authority: UncheckedAccount<'info>,

    /// Seeded by (asset, term), so one term issues one certificate, ever.
    #[account(
        init,
        payer = payer,
        mint::decimals = 0,
        mint::authority = vault,
        mint::token_program = token_program,
        extensions::metadata_pointer::authority = vault,
        extensions::metadata_pointer::metadata_address = cert_mint,
        seeds = [CERT_SEED, &[index], &term.to_le_bytes()],
        bump,
    )]
    pub cert_mint: InterfaceAccount<'info, Mint>,

    #[account(
        init,
        payer = payer,
        associated_token::mint = cert_mint,
        associated_token::authority = holder,
        associated_token::token_program = token_program,
    )]
    pub holder_cert_account: InterfaceAccount<'info, TokenAccount>,

    pub token_program: Program<'info, Token2022>,
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
}
