//! Every way this program refuses.
//!
//! Error names are part of the public interface: they surface in wallets and in
//! the explorer, and the website turns them into human sentences. Name them for
//! what the caller did, not for the line of code that noticed.
use anchor_lang::prelude::*;

#[error_code]
pub enum EncError {
    // ── Arithmetic ──────────────────────────────────────────────────────────
    /// A value did not fit, or a subtraction would have gone below zero.
    ///
    /// Every arithmetic path in this program is checked. Nothing wraps: a
    /// wrapped supply target would mint an arbitrary number of tokens, which is
    /// the one failure this coin cannot survive.
    #[msg("Arithmetic overflow or underflow")]
    MathOverflow,

    /// A basis-points parameter exceeded 10,000 (i.e. 100%).
    #[msg("A rate was given outside the range 0-10000 basis points")]
    InvalidRate,

    // ── Oracle / supply ─────────────────────────────────────────────────────
    /// This build has no working oracle.
    ///
    /// A default build cannot read M2 until T18 lands the real Switchboard
    /// path. Refusing loudly beats falling back to something weaker.
    #[msg("This build cannot read the oracle")]
    OracleUnavailable,

    /// The quote came from a feed other than the one `Config` pins.
    #[msg("The quote is for a different feed than this program accepts")]
    WrongFeed,

    /// The published release date did not strictly advance since the last sync.
    ///
    /// This is the anti-double-mint guard. M2 releases are monthly and the date
    /// is the Fed's, not ours, so a repeat is either a replay or a stalled feed.
    #[msg("That M2 release has already been applied")]
    StaleRelease,

    /// M2 moved further in one release than the sanity cap allows.
    ///
    /// A real monthly M2 move is a fraction of a percent. A large jump means the
    /// oracle is wrong, not that the economy changed, so we refuse rather than
    /// mint against it.
    #[msg("M2 changed more in one release than the sanity cap allows")]
    ChangeTooLarge,

    /// A single sync would have minted more than the per-sync cap.
    #[msg("That would mint more in one step than the cap allows")]
    MintTooLarge,

    // ── Lifecycle ───────────────────────────────────────────────────────────
    /// Bootstrap was attempted by someone other than the program's upgrade
    /// authority.
    ///
    /// Gating on the loader's own record rather than a hardcoded key means no
    /// new key exists, and the gate dies with the authority at T22.
    #[msg("Only the program's upgrade authority may do that")]
    NotUpgradeAuthority,

    /// Assets must be created in order, 0 through 9.
    #[msg("Assets must be initialised in order")]
    AssetOutOfOrder,

    /// An instruction ran before all ten assets existed.
    #[msg("The ten assets are not all initialised yet")]
    NotFullyInitialized,

    /// An asset index outside 0..ASSET_COUNT.
    #[msg("Asset index out of range")]
    InvalidAssetIndex,

    /// That asset has already been created.
    #[msg("That asset already exists")]
    AssetAlreadyInitialized,

    // ── Assets, rent, sales ─────────────────────────────────────────────────
    /// Rent was owed against an asset the vault itself holds.
    ///
    /// The Emperor does not pay rent to the Emperor. Charging it would inflate
    /// the vault out of thin air on paper while moving nothing.
    #[msg("The vault holds this asset, so no rent is owed")]
    VaultHoldsAsset,

    /// Foreclosure attempted while the holder could still pay, or before grace
    /// had elapsed.
    #[msg("This asset is not foreclosable yet")]
    NotForeclosable,

    /// A price interpolation window that ends before it starts.
    #[msg("Invalid price interpolation window")]
    InvalidInterpolationWindow,

    // ── Faucet ──────────────────────────────────────────────────────────────
    /// A second `claim` in the same epoch.
    #[msg("You have already claimed this epoch")]
    AlreadyClaimedThisEpoch,

    /// `close_epoch` on an epoch that may still be collected against.
    ///
    /// Epoch `N-1` is still payable during epoch `N`, so only `N-2` and earlier
    /// are settled.
    #[msg("That epoch is not settled yet")]
    EpochNotSettled,
}
