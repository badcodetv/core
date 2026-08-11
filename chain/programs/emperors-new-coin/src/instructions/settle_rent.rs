//! Collect the rent. Anyone may do it, including nobody.
//!
//! Rent accrues lazily — there is no crank and nothing iterates over accounts.
//! An asset's debt is `rent_accrued` (banked at the last price rescale) plus
//! whatever has run up against the current curve since `last_touched`.
//!
//! ## How a permissionless pull is possible at all
//!
//! ENC is a classic SPL token, so this program cannot move a holder's balance
//! on its own say-so. It can only do it as a **delegate**, and the holder
//! grants that when they buy: `buy_asset` sets the vault as delegate over the
//! buyer's ENC account for an unlimited amount, and the buyer signs that
//! transaction.
//!
//! So the bargain is explicit and on the nose: **to hold one of the Emperor's
//! flags you sign away control of your money.** A holder can revoke the
//! delegation at any time with a standard SPL `revoke` — at which point rent
//! can no longer be collected, the debt keeps climbing, and `foreclose` takes
//! the asset back. Revoking is allowed; keeping the asset afterwards is not.
//!
//! Rent only ever *moves* tokens between a holder and the vault. Total supply
//! is untouched by everything in this file — only the oracle changes that.
use anchor_lang::prelude::*;
use anchor_spl::token::{transfer, Mint, Token, TokenAccount, Transfer};

use crate::errors::EncError;
use crate::math::{rent_owed, PriceCurve};
use crate::state::*;

/// Emitted whenever rent actually moves, so the site can show the drip.
#[event]
pub struct RentSettled {
    pub index: u8,
    pub holder: Pubkey,
    pub paid: u64,
    /// What remains owed because the holder could not cover it.
    pub outstanding: u64,
}

/// The full debt: banked plus accrued-since.
pub fn rent_due(asset: &Asset, rate_bps: u16, now: i64) -> Result<u64> {
    let curve = PriceCurve {
        from: asset.price_from,
        to: asset.price_to,
        start: asset.interp_start,
        end: asset.interp_end,
    };
    asset
        .rent_accrued
        .checked_add(rent_owed(&curve, rate_bps, asset.last_touched, now)?)
        .ok_or(error!(EncError::MathOverflow))
}

pub fn handler(ctx: Context<SettleRent>, _index: u8) -> Result<()> {
    let now = Clock::get()?.unix_timestamp;
    let vault = ctx.accounts.vault.key();

    // The Emperor does not pay rent to the Emperor. Charging it would move
    // nothing while inflating the vault's books.
    require_keys_neq!(ctx.accounts.asset.holder, vault, EncError::VaultHoldsAsset);
    require_keys_eq!(
        ctx.accounts.holder_token_account.owner,
        ctx.accounts.asset.holder,
        EncError::WrongHolderAccount
    );

    let due = rent_due(&ctx.accounts.asset, ctx.accounts.config.rent_rate_per_day_bps, now)?;
    // Pay what they can. A holder who cannot cover the debt is not in error —
    // they are a foreclosure candidate, which is a different instruction.
    let paid = due.min(ctx.accounts.holder_token_account.amount);

    if paid > 0 {
        let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];
        transfer(
            CpiContext::new_with_signer(
                ctx.accounts.token_program.key(),
                Transfer {
                    from: ctx.accounts.holder_token_account.to_account_info(),
                    to: ctx.accounts.vault_token_account.to_account_info(),
                    // As delegate, not as owner. This is the only reason a
                    // stranger can trigger this at all.
                    authority: ctx.accounts.vault.to_account_info(),
                },
                &[vault_seeds],
            ),
            paid,
        )?;
    }

    let asset = &mut ctx.accounts.asset;
    asset.rent_accrued = due - paid;
    asset.last_touched = now;

    emit!(RentSettled {
        index: asset.index,
        holder: asset.holder,
        paid,
        outstanding: asset.rent_accrued,
    });
    Ok(())
}

#[derive(Accounts)]
#[instruction(index: u8)]
pub struct SettleRent<'info> {
    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(mut, seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Account<'info, Asset>,

    /// CHECK: signer-only PDA; here it signs as the delegate over the holder's
    /// token account.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    #[account(address = config.mint)]
    pub mint: Account<'info, Mint>,

    /// The holder's ENC account. Checked against `asset.holder` in the handler
    /// rather than by constraint, so the error names the actual problem.
    #[account(mut, token::mint = mint)]
    pub holder_token_account: Account<'info, TokenAccount>,

    #[account(
        mut,
        associated_token::mint = mint,
        associated_token::authority = vault,
    )]
    pub vault_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
}

#[cfg(test)]
mod tests {
    use super::*;

    fn asset_at(price: u64, banked: u64, last_touched: i64) -> Asset {
        Asset {
            index: 0,
            holder: Pubkey::new_unique(),
            price_from: price,
            price_to: price,
            interp_start: 0,
            interp_end: 0,
            rent_accrued: banked,
            last_touched,
            bump: 255,
        }
    }

    #[test]
    fn adds_what_was_banked_to_what_has_accrued_since() {
        // 5%/day of 1_000_000 for one day, on top of 7 already owed.
        let asset = asset_at(1_000_000, 7, 0);
        assert_eq!(rent_due(&asset, 500, SECONDS_PER_EPOCH).unwrap(), 50_007);
    }

    #[test]
    fn owes_only_what_was_banked_when_no_time_has_passed() {
        assert_eq!(rent_due(&asset_at(1_000_000, 42, 100), 500, 100).unwrap(), 42);
        // A clock that appears to run backwards must not refund anyone.
        assert_eq!(rent_due(&asset_at(1_000_000, 42, 100), 500, 50).unwrap(), 42);
    }

    #[test]
    fn a_banked_debt_at_the_ceiling_errors_rather_than_wrapping() {
        let asset = asset_at(u64::MAX, u64::MAX, 0);
        assert!(rent_due(&asset, 10_000, SECONDS_PER_EPOCH).is_err());
    }
}
