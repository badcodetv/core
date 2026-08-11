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
pub mod instructions;
pub mod math;
pub mod oracle;
pub mod state;

pub use errors::EncError;
pub use instructions::*;
pub use math::{PriceCurve, SupplyMove};
pub use oracle::Quote;
pub use state::*;

declare_id!("5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT");

#[program]
pub mod emperors_new_coin {
    use super::*;

    /// Create the mint, the vault, the rules and the printer. Once, ever, and
    /// only by the program's upgrade authority.
    pub fn initialize(ctx: Context<Initialize>, params: InitializeParams) -> Result<()> {
        instructions::initialize::handler(ctx, params)
    }

    /// Create one parody asset and its NFT. Called ten times, in order.
    pub fn init_asset(
        ctx: Context<InitAsset>,
        index: u8,
        name: String,
        symbol: String,
        uri: String,
        genesis_price: u64,
    ) -> Result<()> {
        instructions::init_asset::handler(ctx, index, name, symbol, uri, genesis_price)
    }

    /// Read the oracle and move the supply to `k × M2`. **Anyone may call
    /// this.** The ten Asset PDAs go in `remaining_accounts`, writable, in
    /// index order.
    pub fn sync_m2(ctx: Context<SyncM2>) -> Result<()> {
        instructions::sync_m2::handler(ctx)
    }

    /// Set M2 by hand. **Compiled only under `--features mock`** — a default
    /// build has no such instruction at all.
    #[cfg(feature = "mock")]
    pub fn set_mock_m2(ctx: Context<SetMockM2>, m2_value: u64, release_date: i64) -> Result<()> {
        instructions::set_mock_m2::handler(ctx, m2_value, release_date)
    }
}
