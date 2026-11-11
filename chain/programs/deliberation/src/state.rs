//! The accounts. Every record is written once, by `init`, and never again:
//! no instruction in this program takes a Policy, Argument, Prediction,
//! Resolution or Label as writable after creation, and none closes one. The
//! only account that changes is an `Author`, and only its own counters.
use anchor_lang::prelude::*;
use anchor_lang::Discriminator;

use crate::errors::DeliberationError;

/// Longest pointer to off-chain text. Fits an `ar://` id, an IPFS CID, and an
/// HTTPS link to a file at a pinned commit.
pub const MAX_URI_LEN: usize = 200;
/// Longest advisory label tag, e.g. `unsourced`, `unmeasurable`, `disputed`.
pub const MAX_TAG_LEN: usize = 32;

/// Posts one key may make per window. Bounds one key, not one person.
pub const MAX_POSTS_PER_WINDOW: u16 = 24;
/// The rate-limit window, in seconds.
pub const WINDOW_SECS: i64 = 3_600;
/// The furthest a check time may sit in the future: thirty years. Catches a
/// timestamp sent in milliseconds, which would otherwise never come due.
pub const MAX_HORIZON_SECS: i64 = 30 * 365 * 24 * 3_600;

pub const AUTHOR_SEED: &[u8] = b"author";
pub const POLICY_SEED: &[u8] = b"policy";
pub const ARGUMENT_SEED: &[u8] = b"argument";
pub const PREDICTION_SEED: &[u8] = b"prediction";
pub const RESOLUTION_SEED: &[u8] = b"resolution";
pub const LABEL_SEED: &[u8] = b"label";

/// One per key that posts. Holds the key's sequence number (so every record's
/// address is derivable without the client inventing ids) and its rate-limit
/// window. Created by `register`; changed only by that key's own posts.
#[account]
#[derive(InitSpace)]
pub struct Author {
    pub key: Pubkey,
    /// The seq the next record by this key will take. Also its total posts.
    pub next_seq: u64,
    pub window_start: i64,
    pub posts_in_window: u16,
    pub bump: u8,
}

impl Author {
    /// Take the next sequence number, charging one post against the window.
    pub fn spend(&mut self, now: i64) -> Result<u64> {
        if now >= self.window_start.saturating_add(WINDOW_SECS) {
            self.window_start = now;
            self.posts_in_window = 0;
        }
        require!(
            self.posts_in_window < MAX_POSTS_PER_WINDOW,
            DeliberationError::RateLimited
        );
        self.posts_in_window += 1;
        let seq = self.next_seq;
        self.next_seq = seq.checked_add(1).ok_or(DeliberationError::MathOverflow)?;
        Ok(seq)
    }
}

/// A proposal: its text lives off-chain at `uri`; `content_hash` proves what
/// the text said. `parent` makes revisions and forks a visible lineage: a
/// parent by the same author reads as a revision, by another author as a fork.
#[account]
#[derive(InitSpace)]
pub struct Policy {
    pub author: Pubkey,
    pub seq: u64,
    pub content_hash: [u8; 32],
    #[max_len(MAX_URI_LEN)]
    pub uri: String,
    pub parent: Option<Pubkey>,
    pub created_at: i64,
    pub created_slot: u64,
    pub bump: u8,
}

#[derive(AnchorSerialize, AnchorDeserialize, Clone, Copy, PartialEq, Eq, InitSpace, Debug)]
pub enum Stance {
    For,
    Against,
    Amend,
    /// Context, a question, or a record of both sides (e.g. a debate log).
    Neutral,
}

/// One node of the debate tree: a reasoned position on a policy, a prediction,
/// a resolution, or another argument.
#[account]
#[derive(InitSpace)]
pub struct Argument {
    pub author: Pubkey,
    pub seq: u64,
    pub target: Pubkey,
    pub target_kind: RecordKind,
    pub stance: Stance,
    pub content_hash: [u8; 32],
    #[max_len(MAX_URI_LEN)]
    pub uri: String,
    pub created_at: i64,
    pub bump: u8,
}

/// A dated, falsifiable claim about the world, attached to a policy. Frozen at
/// creation: the rule (metric, comparator, threshold, revision handling) is
/// `rule_hash` of the text at `rule_uri`; the source is `source_uri`; who
/// marks it is `resolver`. None of it can be changed afterwards by anyone.
#[account]
#[derive(InitSpace)]
pub struct Prediction {
    pub author: Pubkey,
    pub seq: u64,
    pub policy: Pubkey,
    pub resolver: Pubkey,
    /// Unix seconds. The resolver may act at or after this, never before.
    pub check_at: i64,
    /// The author's stated probability that it holds, in basis points.
    /// Stored so calibration can be scored from the chain alone.
    pub prior_bps: u16,
    pub rule_hash: [u8; 32],
    #[max_len(MAX_URI_LEN)]
    pub rule_uri: String,
    #[max_len(MAX_URI_LEN)]
    pub source_uri: String,
    pub created_at: i64,
    pub bump: u8,
}

#[derive(AnchorSerialize, AnchorDeserialize, Clone, Copy, PartialEq, Eq, InitSpace, Debug)]
pub enum Outcome {
    Held,
    Failed,
    /// The rule could not be applied: the source vanished, the series was
    /// discontinued. Scored as neither right nor wrong.
    Void,
}

/// The named resolver's signed verdict on one prediction. At most one per
/// prediction, ever: its address is derived from the prediction's.
#[account]
#[derive(InitSpace)]
pub struct Resolution {
    pub prediction: Pubkey,
    pub resolver: Pubkey,
    pub outcome: Outcome,
    pub evidence_hash: [u8; 32],
    #[max_len(MAX_URI_LEN)]
    pub evidence_uri: String,
    pub resolved_at: i64,
    pub bump: u8,
}

/// An advisory tag from any key on any record. Carries no power: no
/// instruction in this program reads a label.
#[account]
#[derive(InitSpace)]
pub struct Label {
    pub author: Pubkey,
    pub seq: u64,
    pub target: Pubkey,
    pub target_kind: RecordKind,
    #[max_len(MAX_TAG_LEN)]
    pub tag: String,
    /// Optional reasoning; all zeroes and an empty URI when there is none.
    pub note_hash: [u8; 32],
    #[max_len(MAX_URI_LEN)]
    pub note_uri: String,
    pub created_at: i64,
    pub bump: u8,
}

#[derive(AnchorSerialize, AnchorDeserialize, Clone, Copy, PartialEq, Eq, InitSpace, Debug)]
pub enum RecordKind {
    Policy,
    Argument,
    Prediction,
    Resolution,
    Label,
}

/// What kind of record this program wrote at `info`, if any. Checks the owner
/// first: an account owned by any other program is never a record, whatever
/// its first eight bytes say.
pub fn record_kind(info: &AccountInfo) -> Option<RecordKind> {
    if info.owner != &crate::ID {
        return None;
    }
    let data = info.try_borrow_data().ok()?;
    if data.len() < 8 {
        return None;
    }
    let d = &data[..8];
    if d == Policy::DISCRIMINATOR {
        Some(RecordKind::Policy)
    } else if d == Argument::DISCRIMINATOR {
        Some(RecordKind::Argument)
    } else if d == Prediction::DISCRIMINATOR {
        Some(RecordKind::Prediction)
    } else if d == Resolution::DISCRIMINATOR {
        Some(RecordKind::Resolution)
    } else if d == Label::DISCRIMINATOR {
        Some(RecordKind::Label)
    } else {
        None
    }
}

pub fn check_uri(uri: &str) -> Result<()> {
    require!(
        !uri.is_empty() && uri.len() <= MAX_URI_LEN && uri.bytes().all(|b| (0x21..=0x7e).contains(&b)),
        DeliberationError::InvalidUri
    );
    Ok(())
}

pub fn check_optional_uri(uri: &str) -> Result<()> {
    require!(
        uri.len() <= MAX_URI_LEN && uri.bytes().all(|b| (0x21..=0x7e).contains(&b)),
        DeliberationError::InvalidOptionalUri
    );
    Ok(())
}

pub fn check_hash(hash: &[u8; 32]) -> Result<()> {
    require!(hash.iter().any(|&b| b != 0), DeliberationError::EmptyHash);
    Ok(())
}

pub fn check_tag(tag: &str) -> Result<()> {
    require!(
        !tag.is_empty()
            && tag.len() <= MAX_TAG_LEN
            && tag.bytes().all(|b| b.is_ascii_lowercase() || b.is_ascii_digit() || b == b'-'),
        DeliberationError::InvalidTag
    );
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    fn author() -> Author {
        Author { key: Pubkey::default(), next_seq: 0, window_start: 1_000, posts_in_window: 0, bump: 0 }
    }

    #[test]
    fn spends_up_to_the_limit_then_refuses() {
        let mut a = author();
        for i in 0..MAX_POSTS_PER_WINDOW {
            assert_eq!(a.spend(1_000).unwrap(), i as u64);
        }
        assert!(a.spend(1_000 + WINDOW_SECS - 1).is_err());
        assert_eq!(a.next_seq, MAX_POSTS_PER_WINDOW as u64);
    }

    #[test]
    fn a_new_window_resets_the_allowance_but_not_the_seq() {
        let mut a = author();
        for _ in 0..MAX_POSTS_PER_WINDOW {
            a.spend(1_000).unwrap();
        }
        let seq = a.spend(1_000 + WINDOW_SECS).unwrap();
        assert_eq!(seq, MAX_POSTS_PER_WINDOW as u64);
        assert_eq!(a.posts_in_window, 1);
    }

    #[test]
    fn uris_are_printable_ascii_without_spaces() {
        assert!(check_uri("ar://abc").is_ok());
        assert!(check_uri("").is_err());
        assert!(check_uri("has space").is_err());
        assert!(check_uri("caf\u{e9}").is_err());
        assert!(check_uri(&"a".repeat(MAX_URI_LEN + 1)).is_err());
        assert!(check_optional_uri("").is_ok());
    }

    #[test]
    fn tags_are_lowercase_slugs() {
        assert!(check_tag("unsourced").is_ok());
        assert!(check_tag("not-measurable-2").is_ok());
        assert!(check_tag("Unsourced").is_err());
        assert!(check_tag("").is_err());
        assert!(check_tag(&"a".repeat(MAX_TAG_LEN + 1)).is_err());
    }

    #[test]
    fn a_zero_hash_is_refused() {
        assert!(check_hash(&[0; 32]).is_err());
        assert!(check_hash(&[1; 32]).is_ok());
    }
}
