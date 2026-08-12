//! One module per instruction. `lib.rs` stays a table of contents.
pub mod claim;
pub mod close_epoch;
pub mod init_asset;
pub mod initialize;
pub mod mint_certificate;
pub mod place_bid;
pub mod retire;
pub mod roll_term;
pub mod settle_auction;
pub mod sync_m2;
pub mod withdraw_bid;
/// Localnet only — see the module docs for why these are a compile-time choice.
#[cfg(feature = "mock")]
pub mod mock_fund;
#[cfg(feature = "mock")]
pub mod set_mock_m2;

pub use claim::*;
pub use close_epoch::*;
pub use init_asset::*;
pub use initialize::*;
pub use mint_certificate::*;
pub use place_bid::*;
pub use retire::*;
pub use roll_term::*;
pub use settle_auction::*;
pub use sync_m2::*;
pub use withdraw_bid::*;
#[cfg(feature = "mock")]
pub use mock_fund::*;
#[cfg(feature = "mock")]
pub use set_mock_m2::*;
