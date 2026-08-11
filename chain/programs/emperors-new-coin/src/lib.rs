//! Emperor's New Coin.
//!
//! Supply is pegged to the Fed's M2 money supply: when they print, we print.
//! See design/2026-08-06-solana-toolchain-and-emperors-new-coin.md.
//!
//! Scaffold only at this stage — the real instructions land in later tickets.
use anchor_lang::prelude::*;

declare_id!("5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT");

#[program]
pub mod emperors_new_coin {
    use super::*;

    /// Proves the build/deploy/test loop works end to end. Removed once
    /// `initialize` lands.
    pub fn ping(_ctx: Context<Ping>) -> Result<()> {
        msg!("the cloth was always invisible");
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Ping {}
