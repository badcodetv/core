//! Where M2 comes from.
//!
//! One function, `read_quote`, with two implementations chosen at compile time.
//! Not a runtime switch and not a config field: a program that *could* be told
//! to read a different oracle has a backdoor, however well guarded. The mock
//! exists in mock builds and nowhere else.
//!
//! **The environment split is deliberate and absolute.** Localnet runs the mock
//! and never talks to Switchboard; devnet is where the real integration is
//! proven. There is no local Switchboard, because cloned oracle accounts are
//! frozen snapshots that no oracle ever re-signs — a local clone could only
//! prove we can decode a stale quote, which is not the failure that would hurt.
use anchor_lang::prelude::*;

use crate::errors::EncError;

/// What the Fed said, and when they said it.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Quote {
    /// M2SL in billions of USD, fixed-point with 6 decimals.
    pub m2_value: u64,
    /// Unix seconds of the **Fed's release**, not of the read. This is the only
    /// timestamp an attacker cannot advance simply by waiting, which is what
    /// makes it usable as the anti-double-mint guard.
    pub release_date: i64,
}

// ── The real thing ──────────────────────────────────────────────────────────

/// Read a Switchboard On-Demand quote.
///
/// **Stubbed until T18**, which lands the real read path and proves it against
/// devnet — including that a quote cranked days earlier is still readable,
/// which is our actual access pattern for a monthly feed. Until then a default
/// build simply cannot sync, which is the honest state of affairs rather than a
/// silent fallback to something weaker.
///
/// Two things T18 must get right, recorded here so they are not rediscovered:
/// the feed id has to be checked with an explicit `require!` (the canonical
/// address constraint only proves "this is the canonical account for whatever
/// feeds it holds", so a canonical BTC/USD account would pass it); and
/// staleness has to be bounded by *timestamp*, not with
/// `QuoteVerifier::verify_account`, which is hard-capped near 512 slots by the
/// `SlotHashes` sysvar and would reject every quote of a monthly series.
#[cfg(not(feature = "mock"))]
pub fn read_quote(_oracle: &AccountInfo<'_>, _expected_feed_id: &[u8; 32]) -> Result<Quote> {
    err!(EncError::OracleUnavailable)
}

// ── The mock ────────────────────────────────────────────────────────────────

/// A number somebody typed, for localnet.
///
/// Compiled only under `--features mock`. A default build contains neither this
/// account nor the instruction that writes it.
#[cfg(feature = "mock")]
#[account]
#[derive(InitSpace)]
pub struct MockOracle {
    pub m2_value: u64,
    pub release_date: i64,
    pub bump: u8,
}

#[cfg(feature = "mock")]
pub const MOCK_ORACLE_SEED: &[u8] = b"mock_oracle";

/// Read whatever was last set by `set_mock_m2`.
///
/// The feed id is accepted and ignored: on localnet there is no feed to be
/// wrong about, and taking the same argument keeps the two implementations
/// interchangeable so `sync_m2` has no idea which one it is talking to.
#[cfg(feature = "mock")]
pub fn read_quote(oracle: &AccountInfo<'_>, _expected_feed_id: &[u8; 32]) -> Result<Quote> {
    // Deserialized by hand rather than through `Account`, whose lifetime bound
    // (`&'info AccountInfo<'info>`) does not survive being called with a
    // borrow of the accounts struct. Nothing is lost: the owner check below is
    // the only thing `Account` would have added, and the discriminator check
    // comes free with `try_deserialize`.
    require_keys_eq!(*oracle.owner, crate::ID, EncError::WrongFeed);
    let data = oracle.try_borrow_data()?;
    let account = MockOracle::try_deserialize(&mut &data[..])?;
    Ok(Quote {
        m2_value: account.m2_value,
        release_date: account.release_date,
    })
}
