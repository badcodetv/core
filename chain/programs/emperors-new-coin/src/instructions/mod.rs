//! One module per instruction. `lib.rs` stays a table of contents.
pub mod init_asset;
pub mod foreclose;
pub mod initialize;
pub mod settle_rent;
pub mod sync_m2;
/// Localnet only — see the module docs for why this is a compile-time choice.
#[cfg(feature = "mock")]
pub mod set_mock_m2;

pub use init_asset::*;
pub use foreclose::*;
pub use initialize::*;
pub use settle_rent::*;
pub use sync_m2::*;
#[cfg(feature = "mock")]
pub use set_mock_m2::*;
