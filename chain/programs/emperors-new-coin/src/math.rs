//! Every number this program derives, as pure functions.
//!
//! Nothing here touches an account, a clock or a signer, so all of it is unit
//! tested directly and the same vectors can be mirrored in TypeScript for the
//! economic simulation (T14).
//!
//! **Two rules hold throughout.** Every intermediate is computed in `u128` and
//! narrowed back to `u64` with a checked conversion that *errors* rather than
//! wraps; and every subtraction is checked. A wrapped supply target would mint
//! an arbitrary number of tokens against a coin whose entire claim is that its
//! supply is not ours to choose — it is the one bug this program cannot
//! survive, so it is made unrepresentable rather than merely avoided.
use anchor_lang::prelude::*;

use crate::errors::EncError;

/// Basis points denominator. 10,000 bps = 100%.
pub const BPS: u128 = 10_000;

/// Parts-per-million denominator. The genesis price ladder is measured in these
/// rather than in basis points: the cheapest slot is one basis point of the
/// money supply, and a ladder that started at "1" would have no room underneath
/// it to be finer than the masthead ever needs.
pub const PPM: u128 = 1_000_000;

/// Narrow a `u128` back to `u64`, erroring instead of truncating.
#[inline]
fn narrow(value: u128) -> Result<u64> {
    u64::try_from(value).map_err(|_| error!(EncError::MathOverflow))
}

// ── Supply targeting ────────────────────────────────────────────────────────

/// What a sync must do to reach the target.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SupplyMove {
    /// Mint this many base units to the vault.
    Mint(u64),
    /// Burn this many base units from the vault.
    Burn(u64),
    /// Already on target.
    Hold,
}

/// `supply = k × m2_value`.
///
/// M2 is in billions of USD at 6 decimals (`22176.1` → `22_176_100_000`) and
/// `k` is base units of ENC per unit of that, so at the real M2 and `k = 1e6`
/// this lands near `2.2e16` — comfortably inside `u64`, with roughly 830× of
/// headroom. That headroom is why 6 decimals was chosen over 9, and why this
/// function errors rather than saturating: if the product ever *doesn't* fit,
/// the oracle is lying, and minting a saturated supply would be far worse than
/// refusing to sync.
pub fn target_supply(m2_value: u64, k: u64) -> Result<u64> {
    narrow((m2_value as u128) * (k as u128))
}

/// Compare current supply with the target.
///
/// Level-targeting, not a ratchet: every release simply retargets, so a
/// downward M2 revision and genuine quantitative tightening take the identical
/// code path. There is deliberately no record of a burn the vault couldn't
/// cover — the next sync's target is absolute, so the excess corrects itself,
/// and tracking it as well would apply the correction twice.
pub fn supply_move(current_supply: u64, target: u64) -> SupplyMove {
    match current_supply.cmp(&target) {
        std::cmp::Ordering::Less => SupplyMove::Mint(target - current_supply),
        std::cmp::Ordering::Greater => SupplyMove::Burn(current_supply - target),
        std::cmp::Ordering::Equal => SupplyMove::Hold,
    }
}

/// One step of a catch-up walk: move `from` toward `to` by at most `cap_bps`.
///
/// **This is what stops the sanity cap from being a doomsday device.** As first
/// built, a release beyond `max_change_bps` was simply refused — and because
/// `previous_m2` only advances on success, the refusal was *permanent*: the gap
/// never closed, every later sync failed too, and `retire` ended the coin a year
/// later. A single genuine hyperinflation-scale month would have killed the
/// artwork at the exact moment its thesis was most vindicated.
///
/// So an oversized move is absorbed instead of refused. Each call moves by one
/// capped step and does **not** commit the release date; repeated
/// permissionless calls walk to the target over several transactions, and the
/// final step — the one that lands exactly on `to` — commits it. The steps
/// telescope, so prices end up rescaled by the same total ratio a single-step
/// sync would have applied, up to truncation.
///
/// The honest trade, because it is permanent after T22: a bad oracle print is no
/// longer refused outright, it is merely slow and expensive — anyone willing to
/// send enough transactions can walk supply all the way to a wrong number. What
/// makes that survivable is that level-targeting self-heals: the next genuine
/// release retargets absolutely, exactly as it already does for an uncovered
/// burn. A permanent deadlock does not self-heal, which is why this is the
/// better of the two failure modes rather than a free lunch.
///
/// Two floors keep the walk from inventing new deadlocks of its own:
///
/// - **A step is never zero.** With a small `from` and a small cap the
///   proportional step truncates to nothing, and a walk that cannot move is the
///   same permanent refusal in a friendlier costume.
/// - **A downward walk never reaches zero.** From zero there is no ratio to
///   walk along and every later sync divides by nothing, so a program that
///   could reach `m2 = 0` could never leave it. A real M2 of zero is not a
///   reading, it is the end of money.
pub fn capped_step(from: u64, to: u64, cap_bps: u16) -> Result<u64> {
    if from == 0 {
        return err!(EncError::NoBaselineM2);
    }
    // At least one unit, so the walk always advances.
    let cap = (((from as u128) * (cap_bps as u128)) / BPS).max(1);
    if to >= from {
        // Saturating, not checked: `to` is a `u64`, so a ceiling above `u64::MAX`
        // is simply "no ceiling in range". Erroring here would refuse a step
        // that is perfectly representable, which is the deadlock again.
        let ceiling = u64::try_from((from as u128) + cap).unwrap_or(u64::MAX);
        Ok(to.min(ceiling))
    } else {
        // `from` is at least 1 and `cap_bps` cannot exceed 100%, so this floors
        // at 1 rather than wrapping.
        let floor = ((from as u128).saturating_sub(cap)).max(1);
        Ok(to.max(narrow(floor)?))
    }
}

/// One rung of the genesis price ladder, in base units.
///
/// The ladder is chosen as a fraction of the money supply rather than as a
/// number of tokens (see `GENESIS_PRICE_PPM`), so the only place the absolute
/// figure exists is here — computed from the same genesis supply `initialize`
/// mints, by the program that is going to enforce it.
///
/// **It refuses to produce zero.** A zero price is an absorbing state: `rescale`
/// multiplies it by every later ratio and gets zero back, so the slot would
/// stay at zero through every sync the coin ever performs and be winnable for
/// one base unit forever. On a non-upgradeable program that is permanent, so it
/// is made unreachable here rather than caught downstream.
pub fn genesis_price(m2_value: u64, k: u64, ppm: u32) -> Result<u64> {
    let supply = target_supply(m2_value, k)? as u128;
    let price = narrow(supply * (ppm as u128) / PPM)?;
    if price == 0 {
        msg!("a genesis rung of {ppm} ppm of {supply} base units rounds to zero");
        return err!(EncError::WrongGenesisPrice);
    }
    Ok(price)
}

/// Scale `value` by `to / from`, in `u128` throughout.
///
/// This is how asset prices follow the money supply: when M2 rises 1%, every
/// price target rises 1%, so an asset costs the same share of the money supply
/// as it did before. A zero `from` would be a division by zero, and there is no
/// meaningful ratio from nothing, so it errors.
pub fn rescale(value: u64, from: u64, to: u64) -> Result<u64> {
    if from == 0 {
        return err!(EncError::MathOverflow);
    }
    narrow((value as u128) * (to as u128) / (from as u128))
}

// ── Price interpolation ─────────────────────────────────────────────────────

/// A price on its way from one level to another.
///
/// Flat at `from` before `start`, flat at `to` after `end`, a straight line
/// between. Every supply change rescales both endpoints and restarts the
/// window, which is what makes prices tick every slot instead of jumping once a
/// month when the Fed publishes.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct PriceCurve {
    pub from: u64,
    pub to: u64,
    pub start: i64,
    pub end: i64,
}

impl PriceCurve {
    /// A price that is not going anywhere.
    pub fn flat(price: u64, at: i64) -> Self {
        Self { from: price, to: price, start: at, end: at }
    }

    /// `end`, but never before `start`. A window stored backwards would make
    /// the interpolation run in reverse; treating it as instantaneous means a
    /// corrupt window reads as "already arrived" rather than as nonsense.
    fn effective_end(&self) -> i64 {
        self.end.max(self.start)
    }

    /// The price at a moment.
    pub fn price_at(&self, now: i64) -> u64 {
        let end = self.effective_end();
        // Arrival is tested first so that a degenerate window (end <= start)
        // reads as "already arrived" at its own instant rather than as never
        // having started. For a normal window the two orders agree.
        if now >= end {
            return self.to;
        }
        if now <= self.start {
            return self.from;
        }
        let span = (end - self.start) as i128;
        let elapsed = (now - self.start) as i128;
        let delta = self.to as i128 - self.from as i128;
        let price = self.from as i128 + delta * elapsed / span;
        // Between the endpoints by construction; the clamp is belt and braces
        // against a rounding surprise at the boundaries.
        price.clamp(self.from.min(self.to) as i128, self.from.max(self.to) as i128) as u64
    }

}

// ── The faucet ──────────────────────────────────────────────────────────────

/// The vault's floor: `floor_bps` of total supply.
pub fn floor_amount(total_supply: u64, floor_bps: u16) -> Result<u64> {
    narrow((total_supply as u128) * (floor_bps as u128) / BPS)
}

/// What one epoch may pay out: `α × max(0, vault − floor × supply)`.
///
/// The floor governs the *faucet*, not the burn. Burning from the vault lowers
/// the vault's share of supply, so a floor enforced by refusing to burn would
/// break the peg — the burn must always happen. Instead the pot goes to zero
/// below the floor and stays there until the vault refills, which it does two
/// ways: M2 rises and the new supply mints into it, or a flag the Emperor
/// still holds is won at auction and the bid lands in his pocket. The story
/// that falls out of the arithmetic: the Fed tightens, and your pocket money
/// stops entirely until the Emperor's coffers rebuild.
pub fn faucet_pot(
    vault_balance: u64,
    total_supply: u64,
    floor_bps: u16,
    alpha_bps: u16,
) -> Result<u64> {
    let floor = floor_amount(total_supply, floor_bps)?;
    let surplus = vault_balance.saturating_sub(floor);
    narrow((surplus as u128) * (alpha_bps as u128) / BPS)
}

/// One registrant's share of a settled pot.
///
/// Epoch zero has nothing registered before it, so it pays nothing and does not
/// divide by zero.
pub fn faucet_share(pot: u64, registrants: u32) -> u64 {
    if registrants == 0 {
        return 0;
    }
    pot / registrants as u64
}

/// Is the vault above the floor? Below it **nothing** pays out — not a share,
/// and not a welcome grant.
///
/// Gating only the pot would let fresh wallets keep drawing
/// `grants_per_epoch × welcome_grant` out of a depleted vault every epoch
/// forever, which defeats the floor's whole purpose. "Arrive during the
/// tightening and there is nothing for you" is the intended beat, not a gap.
pub fn above_floor(vault_balance: u64, total_supply: u64, floor_bps: u16) -> Result<bool> {
    Ok(vault_balance > floor_amount(total_supply, floor_bps)?)
}

/// Which epoch a timestamp falls in.
///
/// `seconds_per_epoch` comes from `Config`, not from a constant: the shipped
/// day is what the coin runs on, but a test ledger cannot wait one out. A
/// non-positive length is impossible (`initialize` refuses it) and clamps to
/// epoch zero rather than dividing by it. Pre-1970 timestamps cannot occur on a
/// live chain, and clamping beats panicking on a negative division.
pub fn epoch_of(unix_timestamp: i64, seconds_per_epoch: i64) -> u64 {
    if unix_timestamp <= 0 || seconds_per_epoch <= 0 {
        return 0;
    }
    (unix_timestamp / seconds_per_epoch) as u64
}

#[cfg(test)]
mod tests {
    use super::*;

    /// M2SL at the time of writing: $22,176.1bn, 6dp fixed point.
    const M2_REAL: u64 = 22_176_100_000;
    const K: u64 = 1_000_000;

    // ── Supply targeting ────────────────────────────────────────────────────

    #[test]
    fn targets_the_real_money_supply_without_going_near_u64() {
        let supply = target_supply(M2_REAL, K).unwrap();
        // $22.18tn of M2 → ~22.18 billion ENC, i.e. 1 ENC per $1,000 of M2.
        assert_eq!(supply, 22_176_100_000_000_000);
        // ~2.2e16 against a u64 ceiling of ~1.8e19.
        assert!(supply < u64::MAX / 800, "less headroom than the design assumes");
    }

    /// The acceptance criterion: `k × m2` must not be able to wrap.
    #[test]
    fn a_supply_target_that_would_not_fit_errors_rather_than_wrapping() {
        assert!(target_supply(u64::MAX, K).is_err());
        assert!(target_supply(u64::MAX, u64::MAX).is_err());
        assert!(target_supply(u64::MAX / 2, 3).is_err());
        // The exact boundary: the largest product that still fits, and one past.
        assert!(target_supply(u64::MAX, 1).is_ok());
        assert!(target_supply(u64::MAX / 2 + 1, 2).is_err());
    }

    #[test]
    fn a_zero_target_is_representable_and_burns_everything() {
        assert_eq!(target_supply(0, K).unwrap(), 0);
        assert_eq!(supply_move(500, 0), SupplyMove::Burn(500));
        assert_eq!(target_supply(M2_REAL, 0).unwrap(), 0);
    }

    #[test]
    fn moves_toward_the_target_in_both_directions() {
        assert_eq!(supply_move(100, 150), SupplyMove::Mint(50));
        assert_eq!(supply_move(150, 100), SupplyMove::Burn(50));
        assert_eq!(supply_move(100, 100), SupplyMove::Hold);
        // Extremes must not wrap either.
        assert_eq!(supply_move(0, u64::MAX), SupplyMove::Mint(u64::MAX));
        assert_eq!(supply_move(u64::MAX, 0), SupplyMove::Burn(u64::MAX));
    }

    /// A downward M2 revision and quantitative tightening are the same path.
    #[test]
    fn a_revised_down_release_burns_rather_than_holding() {
        let before = target_supply(M2_REAL, K).unwrap();
        // The observed ~0.16% downward restatement between vintages.
        let revised = target_supply(M2_REAL - M2_REAL / 625, K).unwrap();
        assert!(matches!(supply_move(before, revised), SupplyMove::Burn(_)));
    }

    // ── The catch-up walk ───────────────────────────────────────────────────

    #[test]
    fn an_in_cap_move_lands_in_one_step() {
        // The ordinary case: the whole move is inside the cap, so the step *is*
        // the quote and the caller commits the release date.
        assert_eq!(capped_step(10_000, 10_500, 1_000).unwrap(), 10_500);
        assert_eq!(capped_step(10_000, 9_500, 1_000).unwrap(), 9_500);
        assert_eq!(capped_step(10_000, 10_000, 1_000).unwrap(), 10_000);
        // Exactly at the cap still lands in one.
        assert_eq!(capped_step(10_000, 11_000, 1_000).unwrap(), 11_000);
        assert_eq!(capped_step(10_000, 9_000, 1_000).unwrap(), 9_000);
    }

    #[test]
    fn an_oversized_move_is_walked_rather_than_refused() {
        // Five times the cap, up: five steps and a landing, never a refusal.
        let target = 15_000u64;
        let mut m2 = 10_000u64;
        let mut steps = 0;
        while m2 != target {
            m2 = capped_step(m2, target, 1_000).unwrap();
            steps += 1;
            assert!(steps < 50, "the walk did not converge");
        }
        assert_eq!(steps, 5);

        // And down, which is the direction that used to be able to reach zero.
        let mut m2 = 10_000u64;
        let mut steps = 0;
        while m2 != 1_000 {
            m2 = capped_step(m2, 1_000, 1_000).unwrap();
            steps += 1;
            assert!(steps < 100, "the downward walk did not converge");
        }
        assert!(steps > 1, "a 90% fall should not have landed in one step");
    }

    /// The bug the walk could have introduced: a step that truncates to nothing
    /// is the same permanent refusal wearing a friendlier hat.
    #[test]
    fn a_step_is_never_zero_however_small_the_numbers() {
        // 10% of 5 truncates to 0. It must still move.
        assert_eq!(capped_step(5, 1_000_000, 1_000).unwrap(), 6);
        assert_eq!(capped_step(1, 1_000_000, 1).unwrap(), 2);
        assert_eq!(capped_step(5, 1, 1_000).unwrap(), 4);
    }

    /// From zero there is no ratio to walk along, so a program that could reach
    /// `m2 = 0` could never leave it — the exact deadlock class this replaces.
    #[test]
    fn a_downward_walk_never_reaches_zero_and_zero_is_refused_outright() {
        let mut m2 = 1_000u64;
        for _ in 0..500 {
            m2 = capped_step(m2, 0, 1_000).unwrap();
            assert!(m2 > 0, "the walk reached a value it could never leave");
        }
        assert_eq!(m2, 1);
        // And if one ever arrived there anyway, it refuses rather than walking.
        assert!(capped_step(0, 1_000, 1_000).is_err());
    }

    /// The property that lets the walk stand in for a single sync: the steps
    /// telescope, so prices land where one big rescale would have put them.
    #[test]
    fn the_steps_telescope_to_the_same_total_ratio() {
        let (from, to) = (10_000u64, 15_000u64);
        let price = 1_000_000_000u64;

        let one_step = rescale(price, from, to).unwrap();

        let mut m2 = from;
        let mut walked = price;
        while m2 != to {
            let next = capped_step(m2, to, 1_000).unwrap();
            walked = rescale(walked, m2, next).unwrap();
            m2 = next;
        }

        // Equal up to truncation, which loses at most one unit per step.
        let drift = one_step.abs_diff(walked);
        assert!(drift <= 10, "walking drifted {drift} from a single rescale");
    }

    /// A ceiling past `u64::MAX` means "no ceiling in range", not "refuse".
    /// Erroring there would be the deadlock again, wearing a different hat.
    #[test]
    fn a_walk_at_the_top_of_the_range_saturates_rather_than_refusing() {
        assert_eq!(capped_step(u64::MAX, u64::MAX, 1_000).unwrap(), u64::MAX);
        assert_eq!(capped_step(u64::MAX - 1, u64::MAX, 1_000).unwrap(), u64::MAX);
        assert_eq!(capped_step(u64::MAX, 0, 10_000).unwrap(), 1);
    }

    // ── Rescaling ───────────────────────────────────────────────────────────

    #[test]
    fn rescales_prices_by_the_supply_ratio() {
        assert_eq!(rescale(1_000, 100, 101).unwrap(), 1_010);
        assert_eq!(rescale(1_000, 100, 99).unwrap(), 990);
        assert_eq!(rescale(0, 100, 200).unwrap(), 0);
    }

    #[test]
    fn rescaling_refuses_impossible_inputs_instead_of_panicking() {
        assert!(rescale(1_000, 0, 100).is_err());
        assert!(rescale(u64::MAX, 1, 2).is_err());
        assert!(rescale(u64::MAX, 2, 2).is_ok());
    }

    // ── The genesis ladder ──────────────────────────────────────────────────

    #[test]
    fn the_cheapest_rung_is_one_basis_point_of_all_the_money_there_is() {
        let supply = target_supply(M2_REAL, K).unwrap();
        // 100 ppm = 1bp. 22,176,100,000,000,000 ÷ 10,000.
        assert_eq!(genesis_price(M2_REAL, K, 100).unwrap(), supply / 10_000);
        assert_eq!(genesis_price(M2_REAL, K, 100).unwrap(), 2_217_610_000_000);
        // …and the dearest is 1%, a hundred times more.
        assert_eq!(genesis_price(M2_REAL, K, 10_000).unwrap(), supply / 100);
        assert_eq!(genesis_price(M2_REAL, K, 10_000).unwrap(), 221_761_000_000_000);
    }

    /// Every rung, in the order `init_asset` will be called in. The ladder has
    /// to climb: the indexes are forced to arrive in sequence, so this is what
    /// makes "cheapest column first" true of the chain rather than of a
    /// convention. (The check that the *ladder itself* still matches
    /// `params.genesis.json` is `test-init`, which prices its ten assets
    /// straight from the JSON and is refused if the two ever disagree.)
    #[test]
    fn the_ladder_climbs_and_never_touches_zero() {
        let mut previous = 0u64;
        for (i, ppm) in crate::state::GENESIS_PRICE_PPM.iter().enumerate() {
            let price = genesis_price(M2_REAL, K, *ppm).unwrap();
            assert!(price > previous, "rung {i} does not climb: {price} after {previous}");
            previous = price;
        }
    }

    /// Zero is the failure this exists to prevent, and the reason is one line
    /// down: every later sync multiplies the price by a ratio, and zero times
    /// anything is zero — so a slot that starts at nothing is winnable for one
    /// base unit for the life of the coin.
    #[test]
    fn a_rung_that_rounds_to_zero_is_refused_rather_than_stored() {
        assert_eq!(rescale(0, 100, 10_000_000).unwrap(), 0);
        // A supply small enough that one ppm of it is nothing.
        assert!(genesis_price(1, 1, 1).is_err());
        assert!(genesis_price(0, K, 100).is_err());
        // And a rung that cannot be represented at all is refused, not wrapped.
        assert!(genesis_price(u64::MAX, K, 100).is_err());
    }

    // ── Price interpolation ─────────────────────────────────────────────────

    fn curve() -> PriceCurve {
        PriceCurve { from: 1_000, to: 2_000, start: 0, end: 100 }
    }

    #[test]
    fn interpolates_between_the_endpoints_and_holds_outside_them() {
        let c = curve();
        assert_eq!(c.price_at(-50), 1_000);
        assert_eq!(c.price_at(0), 1_000);
        assert_eq!(c.price_at(25), 1_250);
        assert_eq!(c.price_at(50), 1_500);
        assert_eq!(c.price_at(100), 2_000);
        assert_eq!(c.price_at(10_000), 2_000);
    }

    #[test]
    fn interpolates_downward_too() {
        let c = PriceCurve { from: 2_000, to: 1_000, start: 0, end: 100 };
        assert_eq!(c.price_at(25), 1_750);
        assert_eq!(c.price_at(100), 1_000);
    }

    #[test]
    fn a_backwards_window_reads_as_already_arrived_rather_than_as_nonsense() {
        let c = PriceCurve { from: 1_000, to: 2_000, start: 100, end: 50 };
        assert_eq!(c.price_at(99), 1_000);
        assert_eq!(c.price_at(100), 2_000);
        assert_eq!(c.price_at(101), 2_000);
    }

    #[test]
    fn a_flat_curve_never_moves() {
        let c = PriceCurve::flat(1_234, 500);
        assert_eq!(c.price_at(0), 1_234);
        assert_eq!(c.price_at(500), 1_234);
        assert_eq!(c.price_at(i64::MAX), 1_234);
    }

    #[test]
    fn interpolation_survives_prices_at_the_top_of_the_range() {
        let c = PriceCurve { from: 0, to: u64::MAX, start: 0, end: 1_000 };
        assert_eq!(c.price_at(0), 0);
        assert_eq!(c.price_at(1_000), u64::MAX);
        assert_eq!(c.price_at(500), u64::MAX / 2);
    }

    // ── The faucet ──────────────────────────────────────────────────────────

    #[test]
    fn pays_alpha_of_the_surplus_above_the_floor() {
        // Supply 1_000, floor 50% = 500, vault 800 → surplus 300, α 10% → 30.
        assert_eq!(faucet_pot(800, 1_000, 5_000, 1_000).unwrap(), 30);
    }

    #[test]
    fn pays_nothing_at_or_below_the_floor() {
        assert_eq!(faucet_pot(500, 1_000, 5_000, 1_000).unwrap(), 0);
        assert_eq!(faucet_pot(499, 1_000, 5_000, 1_000).unwrap(), 0);
        assert_eq!(faucet_pot(0, 1_000, 5_000, 1_000).unwrap(), 0);
        assert!(!above_floor(500, 1_000, 5_000).unwrap());
        assert!(above_floor(501, 1_000, 5_000).unwrap());
    }

    /// At genesis the vault holds everything, which must not overflow.
    #[test]
    fn handles_a_vault_holding_the_entire_supply() {
        let supply = target_supply(M2_REAL, K).unwrap();
        let pot = faucet_pot(supply, supply, 5_000, 1_000).unwrap();
        // 10% of the half above the floor.
        assert_eq!(pot, supply / 20);
    }

    #[test]
    fn a_zero_supply_has_no_floor_and_no_pot() {
        assert_eq!(floor_amount(0, 5_000).unwrap(), 0);
        assert_eq!(faucet_pot(0, 0, 5_000, 1_000).unwrap(), 0);
    }

    #[test]
    fn the_floor_survives_the_largest_representable_supply() {
        assert_eq!(floor_amount(u64::MAX, 10_000).unwrap(), u64::MAX);
        assert_eq!(floor_amount(u64::MAX, 5_000).unwrap(), u64::MAX / 2);
        assert!(faucet_pot(u64::MAX, u64::MAX, 0, 10_000).is_ok());
    }

    #[test]
    fn divides_a_pot_among_its_registrants() {
        assert_eq!(faucet_share(100, 4), 25);
        // Truncation leaves the remainder in the vault, never overpays.
        assert_eq!(faucet_share(100, 3), 33);
        assert_eq!(faucet_share(1, 1_000), 0);
    }

    /// Epoch zero has nobody registered before it.
    #[test]
    fn an_empty_epoch_pays_nothing_and_does_not_divide_by_zero() {
        assert_eq!(faucet_share(1_000_000, 0), 0);
        assert_eq!(faucet_share(0, 0), 0);
    }

    /// The property the whole no-identity design rests on: a farm dilutes
    /// itself. Total outflow is bounded by the pot however many wallets show up.
    #[test]
    fn a_sybil_farm_cannot_extract_more_than_the_pot() {
        let pot = 1_000_000u64;
        for registrants in [1u32, 10, 1_000, 100_000, u32::MAX] {
            let total = faucet_share(pot, registrants) as u128 * registrants as u128;
            assert!(total <= pot as u128, "{registrants} wallets drew {total} from a pot of {pot}");
        }
    }

    // ── Epochs ──────────────────────────────────────────────────────────────

    #[test]
    fn one_shipped_epoch_is_one_day() {
        use crate::state::DEFAULT_SECONDS_PER_EPOCH as DAY;
        assert_eq!(epoch_of(0, DAY), 0);
        assert_eq!(epoch_of(DAY - 1, DAY), 0);
        assert_eq!(epoch_of(DAY, DAY), 1);
        assert_eq!(epoch_of(DAY * 20_000, DAY), 20_000);
        // A real timestamp, for scale.
        assert_eq!(epoch_of(1_754_870_400, DAY), 20_311);
    }

    /// The test ledger runs short epochs so the cross-epoch behaviour is
    /// reachable at all. Nothing about the faucet cares how long one is.
    #[test]
    fn a_shorter_epoch_is_the_same_arithmetic() {
        assert_eq!(epoch_of(0, 10), 0);
        assert_eq!(epoch_of(9, 10), 0);
        assert_eq!(epoch_of(10, 10), 1);
        assert_eq!(epoch_of(1_754_870_400, 10), 175_487_040);
    }

    #[test]
    fn a_nonsense_timestamp_or_length_clamps_instead_of_panicking() {
        use crate::state::DEFAULT_SECONDS_PER_EPOCH as DAY;
        assert_eq!(epoch_of(-1, DAY), 0);
        assert_eq!(epoch_of(i64::MIN, DAY), 0);
        // `initialize` refuses these, so this is the belt to that braces.
        assert_eq!(epoch_of(1_754_870_400, 0), 0);
        assert_eq!(epoch_of(1_754_870_400, -1), 0);
    }
}
