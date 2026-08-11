//! Emperor's New Coin.
//!
//! Supply is pegged to the Fed's M2 money supply: when they print, we print.
//! Nobody, including us, can change that — the oracle feed is the hash of its
//! own fetch job, so no key exists that could repoint it, and this program
//! ships non-upgradeable.
//!
//! The machine, in one paragraph. A permissionless `sync_m2` reads the feed and
//! mints or burns against the vault so that `supply = k × M2`. Everything else
//! only moves tokens that already exist: ten parody assets are always for sale
//! at a published price with no right of refusal, their holders pay rent to the
//! vault, and the vault pays a daily faucet back out to anyone who shows up.
//! The Fed decides how much money there is; the game decides who holds it.
//!
//! See design/2026-08-06-solana-toolchain-and-emperors-new-coin.md.
use anchor_lang::prelude::*;

pub mod errors;
pub mod math;
pub mod state;

pub use errors::EncError;
pub use math::{PriceCurve, SupplyMove};
pub use state::*;

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
