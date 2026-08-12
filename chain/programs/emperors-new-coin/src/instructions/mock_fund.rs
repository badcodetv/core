//! Hand a wallet some ENC from the vault. Localnet only.
//!
//! **Why this has to exist.** The vault holds every token at genesis and its
//! authority is a PDA, so the only way ENC ever reaches a wallet is an
//! instruction that says so. That instruction is the faucet — which is T13, and
//! T13 depends on T12. Without a stand-in, the auction could not be tested
//! against a real bidder at all: every acceptance case here needs somebody who
//! actually owns some money.
//!
//! Behind `--features mock` with the same reasoning as `set_mock_m2`: a default
//! build contains no instruction that can move vault ENC to a chosen wallet,
//! and `initialize.ts` proves the shipped IDL does not carry this one.
//!
//! It **moves** tokens rather than minting them, so `supply = k × M2` holds
//! across every test — which is exactly what the faucet will do, making this a
//! smaller lie than it looks.
use anchor_lang::prelude::*;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::{transfer, Mint, Token, TokenAccount, Transfer};

use crate::state::*;

pub fn handler(ctx: Context<MockFund>, amount: u64) -> Result<()> {
    let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];
    transfer(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            Transfer {
                from: ctx.accounts.vault_token_account.to_account_info(),
                to: ctx.accounts.recipient_token_account.to_account_info(),
                authority: ctx.accounts.vault.to_account_info(),
            },
            &[vault_seeds],
        ),
        amount,
    )?;
    msg!("mock: {amount} to {}", ctx.accounts.recipient.key());
    Ok(())
}

#[derive(Accounts)]
pub struct MockFund<'info> {
    #[account(mut)]
    pub payer: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    /// CHECK: whoever the test wants funded.
    pub recipient: UncheckedAccount<'info>,

    /// CHECK: signer-only PDA; the vault's authority.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    #[account(address = config.mint)]
    pub mint: Account<'info, Mint>,

    #[account(
        mut,
        associated_token::mint = mint,
        associated_token::authority = vault,
    )]
    pub vault_token_account: Account<'info, TokenAccount>,

    #[account(
        init_if_needed,
        payer = payer,
        associated_token::mint = mint,
        associated_token::authority = recipient,
    )]
    pub recipient_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
}
