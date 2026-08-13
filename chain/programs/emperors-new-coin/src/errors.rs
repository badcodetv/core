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

    /// There is no previous M2 to measure a move against.
    ///
    /// Replaces `ChangeTooLarge` and `MintTooLarge`, both of which T29 deleted.
    /// A move beyond the sanity cap is no longer *refused* — refusing it was
    /// permanent, because the baseline only advances on success, so one
    /// oversized release killed the peg forever. It is walked instead. The only
    /// thing left to refuse is a walk that has no ratio to walk along, which
    /// needs a baseline of zero and cannot be reached from a live program.
    #[msg("This program has no previous M2 to measure a move against")]
    NoBaselineM2,

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

    // ── Assets ──────────────────────────────────────────────────────────────
    /// A token account was supplied that does not belong to the asset's holder,
    /// or is for the wrong mint.
    ///
    /// Checked explicitly rather than by silent mismatch: the auction pays out
    /// to whatever account is passed, so getting this wrong would pay the
    /// wrong person.
    #[msg("That token account does not belong to the holder")]
    WrongHolderAccount,

    /// A price interpolation window that ends before it starts.
    #[msg("Invalid price interpolation window")]
    InvalidInterpolationWindow,

    // ── The auction ─────────────────────────────────────────────────────────
    /// A bid below the reserve — the asset's current interpolated price.
    ///
    /// The reserve is what M2 says the asset is worth, so a flag can never
    /// change hands below it. It moves during a term, which is why settlement
    /// checks it again rather than trusting the check made at bid time.
    #[msg("That bid is below what M2 says this asset is worth")]
    BidBelowReserve,

    /// A bid that did not beat the standing high bid.
    #[msg("That bid does not beat the standing high bid")]
    BidNotHighEnough,

    /// A bid arrived after the term had already ended.
    ///
    /// Settlement is permissionless but nobody is obliged to run it, so a term
    /// can sit expired for a while. Accepting bids in that window would mean
    /// bidding against a reserve that is about to be re-checked.
    #[msg("This term has ended; it must be settled before bidding reopens")]
    TermEnded,

    /// `settle_auction` before the term's published end.
    #[msg("This term has not ended yet")]
    TermNotEnded,

    /// A bid from an earlier term is still in escrow.
    ///
    /// Withdraw it first. Rolling it forward automatically would mean money
    /// re-entering an auction its owner never chose to join.
    #[msg("Withdraw your bid from the previous term first")]
    StaleBidOutstanding,

    /// `withdraw_bid` by the standing high bidder of the live term.
    ///
    /// The only locked escrow in the program, and only until settlement — at
    /// which point it either buys the tenancy or is released.
    #[msg("The standing high bid cannot be withdrawn until the term settles")]
    BidIsStanding,

    /// The winning bid account passed to `settle_auction` was not the standing
    /// high bidder's.
    #[msg("That is not the standing high bid for this asset")]
    WrongBidAccount,

    /// `settle_auction` on a term no bid won. Roll it over instead.
    ///
    /// The two outcomes are separate instructions on purpose: their account
    /// lists genuinely differ, and an explorer showing `settle_auction` versus
    /// `roll_term` says which of the two things happened without decoding
    /// anything.
    #[msg("No bid cleared the reserve for this term")]
    NoQualifyingBid,

    /// `roll_term` on a term that has a winner. Settle it instead.
    #[msg("A bid did clear the reserve; this term must be settled")]
    QualifyingBidExists,

    /// A certificate for a term the asset has already moved past, or for a
    /// tenancy the Emperor holds.
    ///
    /// The vault gets no receipt: it never won anything.
    #[msg("No certificate is issuable for that tenancy")]
    NoCertificateDue,

    // ── The Gazette ─────────────────────────────────────────────────────────
    /// `file_copy` by somebody who does not hold the tenancy.
    ///
    /// The column is rented, not owned, and only its current tenant writes in
    /// it. The Emperor's own slots are held by the vault, which is a PDA nobody
    /// can sign for — so they can never be filed at all, and the page renders
    /// their default copy forever.
    #[msg("Only the current tenant of this column may file copy")]
    NotTheTenant,

    /// A second `file_copy` in the same term.
    ///
    /// Write-once per term is the design, not a rate limit: unlimited rewrites
    /// would make moderation a war of attrition that only a bot BadCode ran
    /// forever could win, which puts us back in the loop.
    #[msg("This column has already been filed this term")]
    AlreadyFiled,

    /// The editor struck this column this term. Refuses a second spike and a
    /// re-file alike, because those are the same fact: the column is spiked
    /// until the term rolls.
    #[msg("This column has been spiked; the next term gets a fresh page")]
    ColumnSpiked,

    /// Copy longer than `COPY_BYTES`. Bytes, not characters.
    #[msg("That copy is longer than a column")]
    CopyTooLong,

    /// `spike`, `pass_the_pen` or `break_the_pen` by somebody who is not the
    /// editor.
    #[msg("Only the editor may do that")]
    NotTheEditor,

    /// The pen was broken. There is no way back — `pass_the_pen` needs a
    /// current editor to sign, and nothing else writes the field.
    #[msg("The pen is broken; this paper has no editor and never will again")]
    PenBroken,

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

    /// The epoch a `claim` named is not the one the chain is in.
    ///
    /// The caller has to name it, because a PDA seed cannot read the clock —
    /// so the program checks the name against `Clock::get()` rather than
    /// trusting it. In practice this means a transaction that sat in the
    /// mempool across an epoch boundary; resubmit it with the new number.
    #[msg("That is not the epoch this chain is currently in")]
    WrongEpoch,

    // ── The ending ──────────────────────────────────────────────────────────
    /// `retire` while the program has heard from the Fed recently enough.
    ///
    /// Nobody can end this early. The condition is elapsed time since the last
    /// successful sync, which is true or false whether or not anyone is
    /// watching — no key, no discretion, no announcement.
    #[msg("This coin has heard about money too recently to be retired")]
    NotSilentEnough,

    /// `sync_m2` after retirement. There is no way back.
    #[msg("This coin has retired; the peg has stopped")]
    Retired,
}
