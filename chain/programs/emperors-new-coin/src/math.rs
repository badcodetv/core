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

/// Absolute change from `old` to `new`, in basis points of `old`.
///
/// Used only as a sanity bound on the oracle. From a zero baseline any change
/// is infinite, so that case reports the maximum rather than dividing by zero —
/// which makes the very first sync after genesis fail the cap if genesis M2 was
/// left at zero, and that is the correct outcome.
pub fn change_bps(old: u64, new: u64) -> u64 {
    if old == 0 {
        return if new == 0 { 0 } else { u64::MAX };
    }
    let delta = if new > old { new - old } else { old - new };
    // (delta / old) × 10_000, in u128 so a large delta cannot wrap.
    u64::try_from((delta as u128) * BPS / (old as u128)).unwrap_or(u64::MAX)
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

    // ── Sanity bounds ───────────────────────────────────────────────────────

    #[test]
    fn measures_change_symmetrically_in_basis_points() {
        assert_eq!(change_bps(10_000, 10_100), 100); // +1%
        assert_eq!(change_bps(10_100, 10_000), 99); // −1% of a larger base
        assert_eq!(change_bps(100, 200), 10_000); // doubled
        assert_eq!(change_bps(M2_REAL, M2_REAL), 0);
    }

    #[test]
    fn treats_any_change_from_zero_as_unbounded_rather_than_dividing_by_zero() {
        assert_eq!(change_bps(0, 1), u64::MAX);
        assert_eq!(change_bps(0, 0), 0);
        // So a genesis M2 left at zero fails any finite cap, which is correct.
        assert!(change_bps(0, M2_REAL) > 10_000);
    }

    #[test]
    fn change_from_the_extremes_does_not_wrap() {
        assert_eq!(change_bps(1, u64::MAX), u64::MAX);
        assert_eq!(change_bps(u64::MAX, 0), BPS as u64);
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
