//! End a tenancy that somebody won, and start the next one.
//!
//! **Permissionless**, because a tenancy that only ends when the person losing
//! it cooperates is not a tenancy. The transaction's fee payer signs; this
//! instruction asks nothing of either party.
//!
//! Three rules here exist because of the 2026-08-12 adversarial review, and
//! each closes a hole the first spec left open:
//!
//! 1. **The reserve is re-checked now, not at bid time.** Prices move during a
//!    term (upward in ~94% of months), so a bid that cleared the reserve when
//!    placed can sit under it at term end. Such a bid does not win — it is
//!    released by `roll_term` and its owner can take it back.
//! 2. **Settlement never needs the outgoing holder's cooperation.** If their
//!    ENC account is missing — closed deliberately or not — it is created here
//!    at the caller's expense. Otherwise an incumbent could veto their own
//!    eviction, and freeze the winner's escrow with it, by closing one account.
//! 3. **A self-bid settles cleanly.** The incumbent may bid on their own asset,
//!    and a winning self-bid simply renews the term with payer and payee the
//!    same wallet.
//!
//! What the outgoing holder is paid is the winning bid: **the current price,
//! whatever M2 says it is.** Never "the new, higher price" — M2 falls in about
//! 6% of months, thirteen in a row in 2022–23, and the reserve falls with it.
use anchor_lang::prelude::*;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::{transfer, Mint, Token, TokenAccount, Transfer};

use crate::errors::EncError;
use crate::math::PriceCurve;
use crate::state::*;

pub fn handler(ctx: Context<SettleAuction>, index: u8) -> Result<()> {
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

    // Rule 1: the reserve as it stands *now*.
    require!(
        asset.high_bid > 0 && asset.high_bid >= reserve,
        EncError::NoQualifyingBid
    );

    // The bid account must be the standing one, on every axis. Checking the
    // amount as well as the bidder means a bid that was topped up or replaced
    // cannot be settled at a figure the asset no longer records.
    let bid = &ctx.accounts.winning_bid;
    require!(
        bid.bidder == asset.high_bidder
            && bid.term_number == asset.term_number
            && bid.amount == asset.high_bid,
        EncError::WrongBidAccount
    );

    let price = asset.high_bid;
    let escrow_seeds: &[&[u8]] = &[ESCROW_SEED, &[ctx.bumps.escrow]];
    transfer(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            Transfer {
                from: ctx.accounts.escrow_token_account.to_account_info(),
                to: ctx.accounts.outgoing_holder_token_account.to_account_info(),
                authority: ctx.accounts.escrow.to_account_info(),
            },
            &[escrow_seeds],
        ),
        price,
    )?;

    let winner = bid.bidder;
    let outgoing = asset.holder;

    asset.holder = winner;
    asset.high_bid = 0;
    asset.high_bidder = Pubkey::default();
    asset.term_number = asset
        .term_number
        .checked_add(1)
        .ok_or(error!(EncError::MathOverflow))?;
    asset.term_ends_at = now
        .checked_add(ctx.accounts.config.term_seconds)
        .ok_or(error!(EncError::MathOverflow))?;
    // A new edition: the incoming tenant gets their one filing and the pen gets
    // its one strike back. The **copy itself is deliberately left standing** —
    // yesterday's news runs until today's is filed, so a column whose new
    // tenant never writes keeps saying whatever it said last month.
    asset.open_a_new_edition();

    msg!(
        "asset {index}: {outgoing} paid {price}, {winner} holds term {}",
        asset.term_number
    );
    Ok(())
}

#[derive(Accounts)]
#[instruction(index: u8)]
pub struct SettleAuction<'info> {
    /// Whoever bothered to run it. Pays for any account this has to create and
    /// is otherwise not consulted.
    #[account(mut)]
    pub caller: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    /// Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack
    /// frame. See the note in `place_bid.rs`.
    #[account(mut, seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Box<Account<'info, Asset>>,

    /// The winner's escrow record. Closed here; its rent returns to the winner,
    /// who paid it.
    #[account(
        mut,
        close = winner,
        seeds = [BID_SEED, &[index], winner.key().as_ref()],
        bump = winning_bid.bump,
    )]
    pub winning_bid: Account<'info, Bid>,

    /// CHECK: identified by the asset's own `high_bidder` field, which the
    /// handler checks against the bid account before anything moves.
    #[account(mut, address = asset.high_bidder)]
    pub winner: UncheckedAccount<'info>,

    /// CHECK: the wallet losing the tenancy, pinned to the asset's record. Can
    /// be the vault (the Emperor held it) or the winner (a self-bid renewal).
    #[account(address = asset.holder)]
    pub outgoing_holder: UncheckedAccount<'info>,

    #[account(address = config.mint)]
    pub mint: Account<'info, Mint>,

    /// Created if absent, payer = caller. Rule 2: nobody gets to veto their own
    /// eviction by closing an account.
    #[account(
        init_if_needed,
        payer = caller,
        associated_token::mint = mint,
        associated_token::authority = outgoing_holder,
    )]
    pub outgoing_holder_token_account: Account<'info, TokenAccount>,

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
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
}
