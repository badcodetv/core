//! Type a number and pretend the Fed said it. Localnet only.
//!
//! The whole file is behind `--features mock`, so a default build contains no
//! instruction that can influence M2 — not a gated one, none. That is the
//! difference between "we promise not to" and "there is nothing to promise
//! about", and it is the only version worth shipping for a coin whose entire
//! claim is that its supply is not ours to choose.
//!
//! Deliberately callable by anyone. On a throwaway local chain an authority
//! check would only be theatre, and the moment this compiles into a build that
//! reaches devnet the mistake is the *feature flag*, not the missing signer.
use anchor_lang::prelude::*;

use crate::oracle::{MockOracle, MOCK_ORACLE_SEED};

pub fn handler(ctx: Context<SetMockM2>, m2_value: u64, release_date: i64) -> Result<()> {
    let oracle = &mut ctx.accounts.mock_oracle;
    oracle.m2_value = m2_value;
    oracle.release_date = release_date;
    oracle.bump = ctx.bumps.mock_oracle;
    msg!("mock M2 = {m2_value} released at {release_date}");
    Ok(())
}

#[derive(Accounts)]
pub struct SetMockM2<'info> {
    #[account(mut)]
    pub payer: Signer<'info>,

    /// `init_if_needed` so the first call creates it and later calls overwrite
    /// it — which is exactly the reinitialisation pattern Anchor warns about,
    /// and exactly what a mock wants. The feature is enabled by `mock` alone
    /// (see Cargo.toml), so a default build cannot use it anywhere.
    #[account(
        init_if_needed,
        payer = payer,
        space = 8 + MockOracle::INIT_SPACE,
        seeds = [MOCK_ORACLE_SEED],
        bump,
    )]
    pub mock_oracle: Account<'info, MockOracle>,

    pub system_program: Program<'info, System>,
}
