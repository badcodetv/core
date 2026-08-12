//! Bid on a tenancy.
//!
//! The bidder moves their own ENC into escrow, **signed by them**. That is the
//! whole reason the auction replaced the forced sale: no delegate over anyone's
//! balance is ever required, so no path in this program can take a token from a
//! wallet that did not sign for it.
//!
//! Two floors a bid has to clear:
//!
//! - **The reserve** — the asset's current interpolated price, i.e. what M2
//!   says it is worth right now. A flag never changes hands below that.
//! - **The standing high bid** — strictly. Ties lose, so the earlier bidder
//!   keeps the position they paid the fee for.
//!
//! Raising your own bid is a top-up: only the difference moves. The incumbent
//! holder may bid on their own asset like anyone else — to take a flag from
//! someone defending it, outbid them. That is an auction working, not a hole.
use anchor_lang::prelude::*;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::{transfer, Mint, Token, TokenAccount, Transfer};

use crate::errors::EncError;
use crate::math::PriceCurve;
use crate::state::*;

pub fn handler(ctx: Context<PlaceBid>, index: u8, amount: u64) -> Result<()> {
    require!(index < ASSET_COUNT, EncError::InvalidAssetIndex);
    require!(
        ctx.accounts.config.initialized_assets == ASSET_COUNT,
        EncError::NotFullyInitialized
    );

    let now = Clock::get()?.unix_timestamp;
    let asset = &mut ctx.accounts.asset;

    // Bidding closes at the published term end and does not reopen until
    // somebody settles. Taking bids in that gap would mean bidding against a
    // reserve that settlement is about to re-check.
    require!(now < asset.term_ends_at, EncError::TermEnded);

    let curve = PriceCurve {
        from: asset.price_from,
        to: asset.price_to,
        start: asset.interp_start,
        end: asset.interp_end,
    };
    require!(amount >= curve.price_at(now), EncError::BidBelowReserve);
    require!(amount > asset.high_bid, EncError::BidNotHighEnough);

    let bid = &mut ctx.accounts.bid;
    let already = if bid.amount == 0 {
        // Fresh account: `init_if_needed` zeroed it.
        bid.asset_index = index;
        bid.bidder = ctx.accounts.bidder.key();
        bid.term_number = asset.term_number;
        bid.bump = ctx.bumps.bid;
        0
    } else {
        // Money from a term that has already settled is not automatically
        // re-entered into a new auction — its owner decides that, by taking it
        // back and choosing to bid again.
        require!(
            bid.term_number == asset.term_number,
            EncError::StaleBidOutstanding
        );
        bid.amount
    };

    // Only the difference moves, so raising a bid costs what the raise costs.
    let owed = amount
        .checked_sub(already)
        .ok_or(error!(EncError::MathOverflow))?;
    if owed > 0 {
        transfer(
            CpiContext::new(
                ctx.accounts.token_program.key(),
                Transfer {
                    from: ctx.accounts.bidder_token_account.to_account_info(),
                    to: ctx.accounts.escrow_token_account.to_account_info(),
                    authority: ctx.accounts.bidder.to_account_info(),
                },
            ),
            owed,
        )?;
    }

    bid.amount = amount;
    asset.high_bid = amount;
    asset.high_bidder = ctx.accounts.bidder.key();

    msg!(
        "asset {index}: {} bids {amount} for term {}",
        ctx.accounts.bidder.key(),
        asset.term_number
    );
    Ok(())
}

#[derive(Accounts)]
#[instruction(index: u8)]
pub struct PlaceBid<'info> {
    #[account(mut)]
    pub bidder: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(mut, seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Account<'info, Asset>,

    #[account(
        init_if_needed,
        payer = bidder,
        space = 8 + Bid::INIT_SPACE,
        seeds = [BID_SEED, &[index], bidder.key().as_ref()],
        bump,
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

    /// CHECK: signer-only PDA. Holds nothing itself; it is the authority over
    /// the escrow token account and the only thing that can sign a release.
    #[account(seeds = [ESCROW_SEED], bump)]
    pub escrow: UncheckedAccount<'info>,

    /// Every bidder's ENC, pooled. Created on the first bid ever placed.
    #[account(
        init_if_needed,
        payer = bidder,
        associated_token::mint = mint,
        associated_token::authority = escrow,
    )]
    pub escrow_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
}
