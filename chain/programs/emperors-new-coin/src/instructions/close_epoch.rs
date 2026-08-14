//! Sweep up an epoch nobody can collect against any more.
//!
//! A `FaucetEpoch` is a rent-exempt account, so left alone they accumulate one
//! per day forever against a program that is meant to run forever. This hands
//! the rent to whoever bothers to close one — permissionless, no signer
//! consulted beyond the fee payer, and worth doing purely for the lamports.
//!
//! **Only `N−2` and earlier.** Epoch `N−1` is what today's claims are paid
//! from, so closing it would delete a pot people are still owed. Epoch `N` is
//! still being registered for. Two behind is the first one that can never
//! matter again.
use anchor_lang::prelude::*;

use crate::errors::EncError;
use crate::math::epoch_of;
use crate::state::*;

pub fn handler(ctx: Context<CloseEpoch>, epoch: u64) -> Result<()> {
    let now = Clock::get()?.unix_timestamp;
    let current = epoch_of(now, ctx.accounts.config.epoch_seconds);

    require!(
        epoch.checked_add(2).ok_or(error!(EncError::MathOverflow))? <= current,
        EncError::EpochNotSettled
    );

    msg!("epoch {epoch} closed, rent to {}", ctx.accounts.closer.key());
    Ok(())
}

/// No authority anywhere. The fee payer signs and is paid for it.
#[derive(Accounts)]
#[instruction(epoch: u64)]
pub struct CloseEpoch<'info> {
    #[account(mut)]
    pub closer: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(
        mut,
        close = closer,
        seeds = [EPOCH_SEED, &epoch.to_le_bytes()],
        bump = epoch_account.bump,
    )]
    pub epoch_account: Account<'info, FaucetEpoch>,
}
