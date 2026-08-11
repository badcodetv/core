//! One module per instruction. `lib.rs` stays a table of contents.
pub mod init_asset;
pub mod initialize;

pub use init_asset::*;
pub use initialize::*;
