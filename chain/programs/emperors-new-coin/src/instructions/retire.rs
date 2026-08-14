//! The coin notices its own end.
//!
//! ENC runs **forever** (Ruling B, 2026-08-12) — with one exception it can
//! prove for itself. If a full `retirement_silence_seconds` passes in which no
//! new M2 figure reaches this program, anyone may call `retire`: no key is
//! consulted, no announcement is made, and a passer-by can simply observe that
//! it is over. Nobody can end it early; nobody can prevent it once the
//! condition is true.
//!
//! **Why elapsed time, and not "the value stopped changing".** The program has
//! no clock of its own and only runs when somebody sends it a transaction. A
//! staleness *counter* would need someone to keep poking it. An elapsed-time
//! test is true whether or not anyone is watching, so the first visitor years
//! later can flip the bit.
//!
//! **What a year of silence actually means — and the copy must not overclaim.**
//! The trigger measures exactly one thing: *no new M2 figure reached this
//! program for a year.* The program cannot know why. Over a forever horizon the
//! likely causes, roughly in order: the oracle stack rotted (Switchboard
//! sunsets the feed's runtime, against a pinned feed hash on a non-upgradeable
//! program — near-certain eventually); nobody left who cared to crank; FRED
//! stopped serving; the Fed went dark. Oracle silence is **not** Fed silence.
//! What is true is also the better joke: **the coin ends when nobody has told
//! it about money for a year — whether because the dollar ended or because
//! everyone stopped looking, and from where it sits those are the same event.**
//!
//! **What retirement does, and does not, stop.** It stops `sync_m2`, and that
//! is all. The auctions keep running forever at the last prices the Fed ever
//! reported — the machine grinding on, trading flags at the valuations of a
//! vanished world, because nobody noticed the numbers stopped meaning anything.
//! That is free: `PriceCurve` already flattens at `price_to`, so after the
//! final sync the machine simply holds. It is also the *safe* ending — a freeze
//! would have had to keep `withdraw_bid` and every other escrow exit alive
//! anyway, or it would strand live bids permanently, which is the exact harm
//! the auction's criteria forbid.
use anchor_lang::prelude::*;

use crate::errors::EncError;
use crate::state::*;

/// Emitted once, ever. The receipt for the end of the artwork.
#[event]
pub struct Retired {
    /// When the bit was flipped.
    pub at: i64,
    /// The last time anyone told this program what money was.
    pub last_sync_at: i64,
    /// What the Fed last said, and when they said it — the numbers the
    /// auctions go on trading at forever.
    pub final_m2_value: u64,
    pub final_m2_release_date: i64,
}

pub fn handler(ctx: Context<Retire>) -> Result<()> {
    let now = Clock::get()?.unix_timestamp;
    let config = &mut ctx.accounts.config;
    let printer = &ctx.accounts.printer;

    let silent_since = now
        .checked_sub(printer.last_sync_at)
        .ok_or(error!(EncError::MathOverflow))?;
    require!(
        silent_since >= config.retirement_silence_seconds,
        EncError::NotSilentEnough
    );

    // Deliberately not guarded against a repeat. Calling it twice is harmless —
    // the condition is still true, the bit is already set, and refusing would
    // make "anyone can walk up and observe that it ended" throw an error at the
    // second person who looks.
    config.retired = true;

    emit!(Retired {
        at: now,
        last_sync_at: printer.last_sync_at,
        final_m2_value: printer.m2_value,
        final_m2_release_date: printer.m2_release_date,
    });

    msg!(
        "retired after {silent_since}s of silence; the last word on money was {} on {}",
        printer.m2_value,
        printer.m2_release_date
    );
    Ok(())
}

/// No signer at all, and no authority anywhere. The fee payer signs the
/// transaction; this instruction asks nothing of anyone, which is the whole
/// point of an ending nobody has to be trusted to declare.
#[derive(Accounts)]
pub struct Retire<'info> {
    #[account(mut, seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(seeds = [PRINTER_SEED], bump = printer.bump)]
    pub printer: Account<'info, Printer>,
}
