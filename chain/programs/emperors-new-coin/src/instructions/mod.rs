//! One module per instruction. `lib.rs` stays a table of contents.
pub mod init_asset;
pub mod initialize;
/// Localnet only — see the module docs for why this is a compile-time choice.
#[cfg(feature = "mock")]
pub mod set_mock_m2;

pub use init_asset::*;
pub use initialize::*;
#[cfg(feature = "mock")]
pub use set_mock_m2::*;
