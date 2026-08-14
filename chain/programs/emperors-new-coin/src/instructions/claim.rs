//! The faucet: register now, collect next epoch.
//!
//! **This is the only way into the economy.** Ruling C (2026-08-12) is that
//! BadCode seeds no liquidity and sells no ENC, ever, so unless a stranger
//! makes a pool of their own there is no route to the coin except this
//! instruction. Which is also the joke: the only place money comes from is the
//! Emperor, and he hands it out in slices of what he happens to be holding.
//!
//! One call does three things, in this order:
//!
//! 1. **Opens the epoch, if nobody has yet** — which is what snapshots
//!    `pot(N) = α × max(0, V − floor·S)`, computed from the vault balance
//!    *before* this same caller is paid anything.
//! 2. **Pays your share of the previous epoch's pot**, `pot(N−1)` divided by
//!    everyone who registered in `N−1`, plus a one-off welcome grant if you
//!    have never taken one.
//! 3. **Registers you for this epoch**, so you can come back tomorrow.
//!
//! **Why the pot is a snapshot, and why it is yesterday's.** A pot cannot be
//! divided fairly among a set that is still growing, so the divisor has to be a
//! headcount that has stopped moving — which only yesterday's is. Dividing
//! *today's* pot by *yesterday's* headcount would be the disaster: ten
//! registrants one day and a thousand the next would draw a hundred pots out of
//! the vault. As built, outflow during any epoch is at most one pot plus the
//! capped grants, however many wallets show up, so a sybil farm dilutes itself
//! and everybody else equally and cannot increase what leaves the vault. That
//! bound is the entire reason this program needs no identity system.
//!
//! **Nothing here mints.** The mint account is not writable, so the faucet is
//! structurally incapable of changing the supply — it can only move tokens the
//! Fed's number already brought into existence.
use anchor_lang::prelude::*;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::{transfer, Mint, Token, TokenAccount, Transfer};

use crate::errors::EncError;
use crate::math::{above_floor, epoch_of, faucet_pot, faucet_share};
use crate::state::*;

/// What one claim actually paid, so the page can say which of the three things
/// happened — yesterday's share, a welcome grant, or nothing and why.
#[event]
pub struct Claimed {
    pub wallet: Pubkey,
    pub epoch: u64,
    pub share: u64,
    pub grant: u64,
    /// The pot this claim just registered for, collectable next epoch.
    pub pot: u64,
    pub registrants: u32,
    /// False when the vault sits at or below its floor, where nothing pays out.
    pub above_floor: bool,
}

pub fn handler(ctx: Context<Claim>, epoch: u64) -> Result<()> {
    let config = &ctx.accounts.config;

    // The same gate `place_bid` uses, and here it closes a real window: between
    // `initialize` and the tenth `init_asset` the vault holds every token, so a
    // stranger claiming in that gap would draw a full pot out of a machine that
    // is not built yet.
    require!(
        config.initialized_assets == ASSET_COUNT,
        EncError::NotFullyInitialized
    );

    // The caller names the epoch because a PDA seed cannot read the clock. It
    // is checked rather than trusted: naming a different epoch would otherwise
    // let someone pick which pot they are paid from.
    let now = Clock::get()?.unix_timestamp;
    require!(
        epoch_of(now, config.epoch_seconds) == epoch,
        EncError::WrongEpoch
    );

    let vault_balance = ctx.accounts.vault_token_account.amount;
    let supply = ctx.accounts.mint.supply;

    // Below the floor **nothing** is paid — not a share, not a grant. Gating
    // only the pot would let fresh wallets keep drawing grants out of a
    // depleted vault forever. Arrive during the tightening and there is nothing
    // for you, which is what austerity is.
    let above = above_floor(vault_balance, supply, config.floor_bps)?;

    // ── Open the epoch, which snapshots its pot ─────────────────────────────
    // Every successful claim registers, so an epoch account that exists has at
    // least one registrant: `registrants == 0` is an exact test for "created by
    // this transaction", with no ambiguous zero anywhere in it.
    let current = &mut ctx.accounts.epoch_account;
    if current.registrants == 0 {
        current.epoch = epoch;
        current.pot = faucet_pot(
            vault_balance,
            supply,
            config.floor_bps,
            config.faucet_alpha_bps,
        )?;
        current.grants_issued = 0;
        current.bump = ctx.bumps.epoch_account;
    }

    // ── Who is asking ───────────────────────────────────────────────────────
    let player = &mut ctx.accounts.player;
    let first_visit = player.wallet == Pubkey::default();
    if first_visit {
        player.wallet = ctx.accounts.claimer.key();
        player.welcome_grant_taken = false;
        player.bump = ctx.bumps.player;
    } else {
        require!(
            player.last_registered_epoch != epoch,
            EncError::AlreadyClaimedThisEpoch
        );
    }

    // ── Yesterday's share ───────────────────────────────────────────────────
    // Eligibility is "registered in exactly the previous epoch". Miss a day and
    // you miss that pot; the share you did not take stays in the vault, which is
    // why outflow is *at most* a pot rather than exactly one.
    let registered_yesterday =
        !first_visit && player.last_registered_epoch.checked_add(1) == Some(epoch);
    let previous_pot = match &ctx.accounts.previous_epoch {
        // The epoch field is written from the checked argument at creation and
        // the seed makes it unique, so a `FaucetEpoch` claiming to be `N−1`
        // is the one and only account for `N−1`.
        Some(prev) if prev.epoch.checked_add(1) == Some(epoch) => Some(prev),
        _ => None,
    };
    let share = match (above, registered_yesterday, previous_pot) {
        (true, true, Some(prev)) => faucet_share(prev.pot, prev.registrants),
        // Epoch zero, a missed day, an account nobody passed: all pay nothing,
        // and none of them divides by anything.
        _ => 0,
    }
    // A pot snapshotted while the vault was fuller than it is now can exceed
    // what is left. Pay what there is rather than underflowing.
    .min(vault_balance);

    // ── The welcome grant ───────────────────────────────────────────────────
    // Keyed on "has this wallet ever taken one", not on "is this wallet new":
    // somebody who first arrived below the floor, or after the day's allotment
    // ran out, is owed theirs when they come back rather than punished for
    // having turned up at the wrong minute.
    let grant_due =
        above && !player.welcome_grant_taken && current.grants_issued < config.grants_per_epoch;
    let grant = if grant_due {
        config
            .welcome_grant
            .min(vault_balance.saturating_sub(share))
    } else {
        0
    };

    // ── Pay, once ───────────────────────────────────────────────────────────
    // A single transfer, so the vault balance read above cannot go stale
    // between two CPIs and quietly overpay the second one.
    let total = share
        .checked_add(grant)
        .ok_or(error!(EncError::MathOverflow))?;
    if total > 0 {
        let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];
        transfer(
            CpiContext::new_with_signer(
                ctx.accounts.token_program.key(),
                Transfer {
                    from: ctx.accounts.vault_token_account.to_account_info(),
                    to: ctx.accounts.claimer_token_account.to_account_info(),
                    authority: ctx.accounts.vault.to_account_info(),
                },
                &[vault_seeds],
            ),
            total,
        )?;
    }

    // ── Register for this epoch ─────────────────────────────────────────────
    if grant_due {
        player.welcome_grant_taken = true;
        current.grants_issued = current
            .grants_issued
            .checked_add(1)
            .ok_or(error!(EncError::MathOverflow))?;
    }
    player.last_registered_epoch = epoch;
    current.registrants = current
        .registrants
        .checked_add(1)
        .ok_or(error!(EncError::MathOverflow))?;

    emit!(Claimed {
        wallet: ctx.accounts.claimer.key(),
        epoch,
        share,
        grant,
        pot: current.pot,
        registrants: current.registrants,
        above_floor: above,
    });

    msg!(
        "epoch {epoch}: {} took {share} + {grant}, registrant {} of a pot of {}",
        ctx.accounts.claimer.key(),
        current.registrants,
        current.pot
    );
    Ok(())
}

#[derive(Accounts)]
#[instruction(epoch: u64)]
pub struct Claim<'info> {
    #[account(mut)]
    pub claimer: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    /// Created on a wallet's first ever claim, at that wallet's expense.
    #[account(
        init_if_needed,
        payer = claimer,
        space = 8 + Player::INIT_SPACE,
        seeds = [PLAYER_SEED, claimer.key().as_ref()],
        bump,
    )]
    pub player: Account<'info, Player>,

    /// This epoch. Created by whoever claims first, which is what freezes the
    /// pot — everyone who registers today divides today's pot tomorrow.
    #[account(
        init_if_needed,
        payer = claimer,
        space = 8 + FaucetEpoch::INIT_SPACE,
        seeds = [EPOCH_SEED, &epoch.to_le_bytes()],
        bump,
    )]
    pub epoch_account: Account<'info, FaucetEpoch>,

    /// Last epoch, the one being paid out. **Optional**, and legitimately
    /// absent in three cases: the very first epoch anyone ever claimed in, an
    /// epoch nobody claimed in at all, and one already closed by `close_epoch`.
    /// Omitting it costs the caller their own share and nobody else anything,
    /// so it needs no defending beyond the handler's check that it really is
    /// the previous epoch.
    pub previous_epoch: Option<Account<'info, FaucetEpoch>>,

    /// Read-only on purpose: **the faucet cannot mint.** Only `sync_m2` may
    /// change the supply, and only against what the Fed published.
    #[account(address = config.mint)]
    pub mint: Account<'info, Mint>,

    /// CHECK: signer-only PDA; the Emperor's pocket, and the authority that
    /// signs the payout.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    #[account(
        mut,
        associated_token::mint = mint,
        associated_token::authority = vault,
    )]
    pub vault_token_account: Account<'info, TokenAccount>,

    #[account(
        init_if_needed,
        payer = claimer,
        associated_token::mint = mint,
        associated_token::authority = claimer,
    )]
    pub claimer_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
}
