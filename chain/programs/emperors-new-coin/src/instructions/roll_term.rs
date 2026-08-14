//! End a tenancy nobody won.
//!
//! **Dormancy is an expected outcome, not a failure.** The artwork does not
//! need players; if no bid clears the reserve the incumbent simply keeps the
//! asset for another term, and the Emperor keeps the ones nobody ever wanted.
//!
//! This is also where a **stale high bid** is released. A bid that beat the
//! reserve when it was placed can sit under it by term end, because prices rise
//! with M2 during the term. Rolling the term clears `high_bid`, which makes
//! that escrow withdrawable exactly as if it had been outbid. Without the
//! release, the sole bidder in a quiet market would be locked in term after
//! term while the reserve climbed away from them — stranded escrow, reached
//! through the design's *expected* state rather than an exotic one.
//!
//! Split from `settle_auction` because the two outcomes need genuinely
//! different accounts — there is no bid, no winner and no payment here — and
//! because an explorer then says which of the two happened without decoding a
//! thing.
use anchor_lang::prelude::*;

use crate::errors::EncError;
use crate::math::PriceCurve;
use crate::state::*;

pub fn handler(ctx: Context<RollTerm>, index: u8) -> Result<()> {
    let now = Clock::get()?.unix_timestamp;
    let asset = &mut ctx.accounts.asset;

    require!(now >= asset.term_ends_at, EncError::TermNotEnded);

    let curve = PriceCurve {
        from: asset.price_from,
        to: asset.price_to,
        start: asset.interp_start,
        end: asset.interp_end,
    };
    let reserve = curve.price_at(now);

    // The exact complement of `settle_auction`'s guard, so every ended term is
    // handled by precisely one of the two and neither can be used to deny the
    // other's outcome.
    require!(
        !(asset.high_bid > 0 && asset.high_bid >= reserve),
        EncError::QualifyingBidExists
    );

    let released = asset.high_bid;
    asset.high_bid = 0;
    asset.high_bidder = Pubkey::default();
    asset.term_number = asset
        .term_number
        .checked_add(1)
        .ok_or(error!(EncError::MathOverflow))?;
    asset.term_ends_at = now
        .checked_add(ctx.accounts.config.term_seconds)
        .ok_or(error!(EncError::MathOverflow))?;
    // Same new edition as a settlement: the incumbent gets another filing, a
    // spiked column is unstruck, and the copy on the page is left exactly where
    // it was. A dormant slot simply keeps running last month's words.
    asset.open_a_new_edition();

    msg!(
        "asset {index}: nobody cleared {reserve}, {} keeps it for term {} ({released} released)",
        asset.holder,
        asset.term_number
    );
    Ok(())
}

/// No signer at all. The fee payer signs the transaction; this instruction asks
/// nothing of anyone, which is what "the clock is published" has to mean.
#[derive(Accounts)]
#[instruction(index: u8)]
pub struct RollTerm<'info> {
    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    /// Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack
    /// frame. See the note in `place_bid.rs`.
    #[account(mut, seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Box<Account<'info, Asset>>,
}
