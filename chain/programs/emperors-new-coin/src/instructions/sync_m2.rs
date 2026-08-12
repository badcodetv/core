//! When they print, we print.
//!
//! The permissionless core: read what the Fed published, and move the supply to
//! `k × M2`. Anyone may call it and it costs a fraction of a cent, which is the
//! point — a peg that only BadCode could advance would be a peg BadCode
//! controls.
//!
//! **Level-targeting, not a ratchet.** Every release retargets absolutely, so a
//! downward M2 revision and genuine quantitative tightening travel the identical
//! code path. Nothing records a burn the vault could not cover: the next
//! target is absolute, so the excess corrects itself, and remembering it as well
//! would apply the correction twice and undershoot permanently. The honest
//! invariant is therefore `supply ≥ k × M2`, with equality whenever the vault
//! was solvent enough to absorb the last burn.
use anchor_lang::prelude::*;
use anchor_spl::token::{burn, mint_to, Burn, Mint, MintTo, Token, TokenAccount};

use crate::errors::EncError;
use crate::math::{change_bps, rescale, supply_move, target_supply, PriceCurve, SupplyMove};
use crate::oracle::read_quote;
use crate::state::*;

/// Emitted on every successful sync, so the website and any indexer can show
/// what the printer did without replaying the whole chain.
#[event]
pub struct Synced {
    pub m2_value: u64,
    pub m2_release_date: i64,
    pub target_supply: u64,
    /// Positive when minted, negative when burned.
    pub supply_delta: i128,
    /// How much of a burn the vault could not cover. Non-zero means supply is
    /// left above target on purpose.
    pub uncovered_burn: u64,
    pub slot: u64,
}

pub fn handler(ctx: Context<SyncM2>) -> Result<()> {
    // Prices are rescaled as part of a sync, so syncing before the assets exist
    // would set a ratio the missing assets never see.
    require!(
        ctx.accounts.config.initialized_assets == ASSET_COUNT,
        EncError::NotFullyInitialized
    );

    let clock = Clock::get()?;
    let now = clock.unix_timestamp;
    let config = &ctx.accounts.config;
    let oracle_info = ctx.accounts.oracle.to_account_info();
    let quote = read_quote(&oracle_info, &config.expected_feed_id)?;

    let previous_m2 = ctx.accounts.printer.m2_value;

    // Anti-double-mint. The release date is the Fed's, not ours, so it is the
    // one timestamp a caller cannot advance simply by waiting — which is what
    // makes it usable as a replay guard where a block time would not be.
    require!(
        quote.release_date > ctx.accounts.printer.m2_release_date,
        EncError::StaleRelease
    );

    // A real monthly M2 move is a fraction of a percent. A large jump means the
    // oracle is wrong, not that the economy changed.
    require!(
        change_bps(previous_m2, quote.m2_value) <= config.max_change_bps as u64,
        EncError::ChangeTooLarge
    );

    let target = target_supply(quote.m2_value, config.k)?;
    let supply = ctx.accounts.mint.supply;
    let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];

    let mut uncovered_burn: u64 = 0;
    let supply_delta: i128 = match supply_move(supply, target) {
        SupplyMove::Hold => 0,
        SupplyMove::Mint(amount) => {
            require!(amount <= config.max_single_mint, EncError::MintTooLarge);
            mint_to(
                CpiContext::new_with_signer(
                    ctx.accounts.token_program.key(),
                    MintTo {
                        mint: ctx.accounts.mint.to_account_info(),
                        to: ctx.accounts.vault_token_account.to_account_info(),
                        authority: ctx.accounts.vault.to_account_info(),
                    },
                    &[vault_seeds],
                ),
                amount,
            )?;
            amount as i128
        }
        SupplyMove::Burn(amount) => {
            // Only the vault's own tokens can be burned. Reaching into holders'
            // balances to hit the target is exactly the power this coin claims
            // not to have, so a burn the vault cannot cover simply burns
            // everything it has and leaves supply above target.
            let available = ctx.accounts.vault_token_account.amount;
            let burning = amount.min(available);
            uncovered_burn = amount - burning;
            if burning > 0 {
                burn(
                    CpiContext::new_with_signer(
                        ctx.accounts.token_program.key(),
                        Burn {
                            mint: ctx.accounts.mint.to_account_info(),
                            from: ctx.accounts.vault_token_account.to_account_info(),
                            authority: ctx.accounts.vault.to_account_info(),
                        },
                        &[vault_seeds],
                    ),
                    burning,
                )?;
            }
            -(burning as i128)
        }
    };

    rescale_assets(&ctx, previous_m2, quote.m2_value, now)?;

    let printer = &mut ctx.accounts.printer;
    printer.m2_value = quote.m2_value;
    printer.m2_release_date = quote.release_date;
    printer.last_sync_slot = clock.slot;
    printer.target_supply = target;

    emit!(Synced {
        m2_value: quote.m2_value,
        m2_release_date: quote.release_date,
        target_supply: target,
        supply_delta,
        uncovered_burn,
        slot: clock.slot,
    });

    msg!("M2 {previous_m2} -> {}, supply delta {supply_delta}", quote.m2_value);
    Ok(())
}

/// Move every asset's price target by the same ratio the money supply moved.
///
/// An asset should cost the same *share* of the money supply as it did before,
/// so when M2 rises one percent every price target rises one percent. The new
/// curve starts from the price the asset is showing right now, so nothing
/// jumps: the visible price walks to its new target over thirty days and ticks
/// every slot on the way.
///
/// The ten assets arrive as `remaining_accounts` in index order. Naming them
/// individually would put them past the transaction size limit alongside
/// everything else this instruction needs.
fn rescale_assets(ctx: &Context<SyncM2>, m2_old: u64, m2_new: u64, now: i64) -> Result<()> {
    require!(
        ctx.remaining_accounts.len() == ASSET_COUNT as usize,
        EncError::NotFullyInitialized
    );

    for (index, info) in ctx.remaining_accounts.iter().enumerate() {
        let index = index as u8;
        // Derived, not trusted. Without this a caller could pass ten copies of
        // asset 0 and rescale it ten times.
        let seeds = asset_seeds(index);
        let refs: Vec<&[u8]> = seeds.iter().map(|s| s.as_slice()).collect();
        let (expected, _) = Pubkey::find_program_address(&refs, &crate::ID);
        require_keys_eq!(info.key(), expected, EncError::InvalidAssetIndex);

        let mut asset: Account<Asset> = Account::try_from(info)?;
        let curve = PriceCurve {
            from: asset.price_from,
            to: asset.price_to,
            start: asset.interp_start,
            end: asset.interp_end,
        };

        asset.last_touched = now;

        asset.price_from = curve.price_at(now);
        asset.price_to = rescale(asset.price_to, m2_old, m2_new)?;
        asset.interp_start = now;
        asset.interp_end = now
            .checked_add(PRICE_INTERPOLATION_SECONDS)
            .ok_or(error!(EncError::MathOverflow))?;

        asset.exit(&crate::ID)?;
    }
    Ok(())
}

/// No signer. Anyone may advance the peg, which is the whole idea — the fee
/// payer signs the transaction, but this instruction asks nothing of them.
#[derive(Accounts)]
pub struct SyncM2<'info> {
    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    #[account(mut, seeds = [PRINTER_SEED], bump = printer.bump)]
    pub printer: Account<'info, Printer>,

    /// CHECK: interpreted by `oracle::read_quote`, which is the only thing that
    /// knows what shape this account has — a Switchboard feed in a real build,
    /// a mock in a mock one.
    pub oracle: UncheckedAccount<'info>,

    #[account(mut, address = config.mint)]
    pub mint: Account<'info, Mint>,

    /// CHECK: signer-only PDA; the mint authority and the only account whose
    /// tokens this instruction may burn.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    #[account(
        mut,
        associated_token::mint = mint,
        associated_token::authority = vault,
    )]
    pub vault_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
    // remaining_accounts: the ten Asset PDAs, writable, in index order.
}
