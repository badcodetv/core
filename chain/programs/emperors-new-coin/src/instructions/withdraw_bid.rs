//! Take an escrowed bid back.
//!
//! **Every route out of escrow is reachable by the bidder alone.** That is the
//! property the whole auction is checked against: escrowed ENC must never be
//! strandable. A bid is locked in exactly one situation — while it is the
//! standing high bid *of the current term* — and even that lock has a
//! permissionless exit, because anyone may call `settle_auction` once the term
//! ends, and settlement either spends the bid or releases it.
//!
//! In particular a bid that beat the reserve when placed but sits under it at
//! term end is released by settlement rather than rolled forward, so the sole
//! bidder in a quiet market cannot be locked in term after term while the
//! reserve climbs away from them.
use anchor_lang::prelude::*;
use anchor_spl::token::{transfer, Mint, Token, TokenAccount, Transfer};

use crate::errors::EncError;
use crate::state::*;

pub fn handler(ctx: Context<WithdrawBid>, index: u8) -> Result<()> {
    let asset = &ctx.accounts.asset;
    let bid = &ctx.accounts.bid;

    // Locked only while it is *both* the standing high bid and from the live
    // term. Once the term rolls over the bid is dead regardless of what it once
    // was, which is what makes a stale high bid recoverable.
    let is_standing =
        bid.term_number == asset.term_number && asset.high_bidder == ctx.accounts.bidder.key();
    require!(!is_standing, EncError::BidIsStanding);

    let amount = bid.amount;
    if amount > 0 {
        let escrow_seeds: &[&[u8]] = &[ESCROW_SEED, &[ctx.bumps.escrow]];
        transfer(
            CpiContext::new_with_signer(
                ctx.accounts.token_program.key(),
                Transfer {
                    from: ctx.accounts.escrow_token_account.to_account_info(),
                    to: ctx.accounts.bidder_token_account.to_account_info(),
                    authority: ctx.accounts.escrow.to_account_info(),
                },
                &[escrow_seeds],
            ),
            amount,
        )?;
    }

    // The pool's own token account is deliberately never closed, even when it
    // empties. Closing it would hand one bidder rent another paid, and would
    // let anyone force the next bidder to fund a fresh one — a small toll on
    // participation in exchange for recovering a fraction of a cent, once.
    msg!("asset {index}: {} withdrew {amount}", ctx.accounts.bidder.key());
    Ok(())
}

#[derive(Accounts)]
#[instruction(index: u8)]
pub struct WithdrawBid<'info> {
    #[account(mut)]
    pub bidder: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Account<'info, Asset>,

    /// Closed on the way out, rent back to the bidder who paid it.
    #[account(
        mut,
        close = bidder,
        seeds = [BID_SEED, &[index], bidder.key().as_ref()],
        bump = bid.bump,
        constraint = bid.bidder == bidder.key() @ EncError::WrongBidAccount,
    )]
    pub bid: Account<'info, Bid>,

    #[account(address = config.mint)]
    pub mint: Account<'info, Mint>,

    #[account(
        mut,
        associated_token::mint = mint,
        associated_token::authority = bidder,
    )]
    pub bidder_token_account: Account<'info, TokenAccount>,

    /// CHECK: signer-only PDA; the escrow pool's authority.
    #[account(seeds = [ESCROW_SEED], bump)]
    pub escrow: UncheckedAccount<'info>,

    #[account(
        mut,
        associated_token::mint = mint,
        associated_token::authority = escrow,
    )]
    pub escrow_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
}
