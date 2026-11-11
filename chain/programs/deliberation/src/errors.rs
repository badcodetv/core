//! Every way this program refuses.
//!
//! Error names are part of the public interface: they surface in wallets and
//! in the explorer. Name them for what the caller did, not for the line of code
//! that noticed.
use anchor_lang::prelude::*;

#[error_code]
pub enum DeliberationError {
    // ── Input ───────────────────────────────────────────────────────────────
    /// A URI was empty, too long, or held a byte outside printable ASCII.
    ///
    /// Printable ASCII only (0x21–0x7E, so no spaces and no control bytes):
    /// a pointer is for machines, and a homoglyph in a pointer is a trap.
    #[msg("A URI must be 1-200 bytes of printable ASCII with no spaces")]
    InvalidUri,

    /// An optional URI (a label's note) was too long or not printable ASCII.
    #[msg("An optional URI must be at most 200 bytes of printable ASCII with no spaces")]
    InvalidOptionalUri,

    /// A label tag was empty, longer than 32 bytes, or used a character
    /// outside `a-z`, `0-9` and `-`.
    #[msg("A label tag must be 1-32 characters of a-z, 0-9 and -")]
    InvalidTag,

    /// A content hash of all zeroes: almost certainly a client that forgot to
    /// hash, and never a real digest of anything.
    #[msg("A hash of all zeroes is not a hash")]
    EmptyHash,

    /// A prior outside 1..=9999 basis points. 0 and 10,000 are certainties,
    /// and a certainty is not a prediction.
    #[msg("A prior must be between 1 and 9999 basis points")]
    InvalidPrior,

    /// The default (all-zero) public key was named as the resolver. Nobody
    /// holds its private key, so the prediction could never be resolved.
    #[msg("The resolver must be a real key")]
    InvalidResolver,

    /// The check time is not in the future, or is further out than the
    /// horizon (a timestamp in milliseconds instead of seconds lands here).
    #[msg("The check time must be in the future and within the horizon")]
    InvalidCheckTime,

    // ── Targets ─────────────────────────────────────────────────────────────
    /// The account given as a target is not a record this program wrote, or
    /// is a kind of record that cannot be targeted by this instruction.
    #[msg("That account is not a record this instruction can target")]
    InvalidTarget,

    // ── Resolution ──────────────────────────────────────────────────────────
    /// Somebody other than the resolver named in the prediction tried to
    /// resolve it. The asker chose who marks it; nobody can repoint that.
    #[msg("Only the resolver named in the prediction may resolve it")]
    NotTheResolver,

    /// The prediction's check time has not arrived.
    #[msg("This prediction cannot be resolved before its check time")]
    TooEarly,

    // ── Rate limit ──────────────────────────────────────────────────────────
    /// This key has posted its allowance for the current window.
    ///
    /// The limit bounds one key. It does nothing against someone with many
    /// keys, and is not claimed to; see the design doc's Sybil section.
    #[msg("This key has reached its posting limit for this window; try again later")]
    RateLimited,

    /// A counter would have overflowed.
    #[msg("Arithmetic overflow")]
    MathOverflow,
}
