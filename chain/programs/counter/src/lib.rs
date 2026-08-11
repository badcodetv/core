//! A counter.
//!
//! This program has no product purpose. It exists to exercise the toolchain end
//! to end — build, deploy, generated types, wallet, live account subscription —
//! with the smallest possible amount of program to be wrong about. When you copy
//! `chain/` into another project, this is what you run first to prove the copy
//! works, and the first thing you delete once your own program does.
//!
//! It is also the loop you develop against: change STEP below, `chain build &&
//! chain deploy`, and watch the number in the browser go up by a different
//! amount without touching a line of TypeScript.
use anchor_lang::prelude::*;

declare_id!("F1t91u9XG9WbXPPQVj6mzmgVXPTVx6PZLo5kYaB76u9Q");

/// How much `increment` adds. Change it and redeploy — that is the demo.
pub const STEP: u64 = 1;

/// PDA seed prefix. One counter per wallet, so two browsers do not fight.
pub const COUNTER_SEED: &[u8] = b"counter";

#[program]
pub mod counter {
    use super::*;

    /// Create the caller's counter. Fails if they already have one.
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let counter = &mut ctx.accounts.counter;
        counter.authority = ctx.accounts.authority.key();
        counter.count = 0;
        counter.updated_at = Clock::get()?.unix_timestamp;
        counter.bump = ctx.bumps.counter;
        msg!("counter created for {}", counter.authority);
        Ok(())
    }

    /// Add STEP to the caller's counter.
    pub fn increment(ctx: Context<Update>) -> Result<()> {
        let counter = &mut ctx.accounts.counter;
        // Saturating, not checked: a demo counter running out of u64 should not
        // be an error path anyone has to think about.
        counter.count = counter.count.saturating_add(STEP);
        counter.updated_at = Clock::get()?.unix_timestamp;
        msg!("count = {}", counter.count);
        Ok(())
    }

    /// Back to zero. The second button.
    pub fn reset(ctx: Context<Update>) -> Result<()> {
        ctx.accounts.counter.count = 0;
        ctx.accounts.counter.updated_at = Clock::get()?.unix_timestamp;
        Ok(())
    }
}

#[account]
#[derive(InitSpace)]
pub struct Counter {
    /// Who may change it. Also the PDA seed, so it is one-per-wallet.
    pub authority: Pubkey,
    pub count: u64,
    /// Unix seconds of the last change. Here to prove the type flows through:
    /// add a field, rebuild, and the browser knows about it.
    pub updated_at: i64,
    pub bump: u8,
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(
        init,
        payer = authority,
        // 8 for Anchor's account discriminator; INIT_SPACE covers the fields.
        space = 8 + Counter::INIT_SPACE,
        seeds = [COUNTER_SEED, authority.key().as_ref()],
        bump,
    )]
    pub counter: Account<'info, Counter>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(
        mut,
        seeds = [COUNTER_SEED, authority.key().as_ref()],
        bump = counter.bump,
        has_one = authority,
    )]
    pub counter: Account<'info, Counter>,
    pub authority: Signer<'info>,
}
