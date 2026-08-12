/**
 * Every number the ENC program derives, mirrored in TypeScript.
 *
 * **This is a mirror, not an implementation.** `chain/programs/emperors-new-coin/src/math.rs`
 * is the source of truth; if the two disagree, the Rust is right and this is a
 * bug. `math.test.ts` asserts the same fixed vectors the Rust unit tests use,
 * so the two fail together or not at all.
 *
 * Everything is `bigint`, because every quantity here is a `u64` in base units
 * and `Number` silently loses precision above 2^53 — which the money supply
 * passed a long time ago (~2.2e16 base units today). A mirror that quietly
 * rounded would be worse than no mirror, because the simulation it feeds is
 * what picks the parameters that ship.
 */

/** Basis points denominator. 10,000 bps = 100%. */
export const BPS = 10_000n

/** The ceiling every value here has to fit under. */
export const U64_MAX = 2n ** 64n - 1n

/** The Rust `EncError` a mirrored function would have returned. */
export class EncMathError extends Error {
  constructor(readonly code: 'MathOverflow' | 'NoBaselineM2') {
    super(code)
    this.name = 'EncMathError'
  }
}

/** Narrow back to `u64`, throwing instead of truncating. */
function narrow(value: bigint): bigint {
  if (value < 0n || value > U64_MAX) throw new EncMathError('MathOverflow')
  return value
}

// ── Supply targeting ────────────────────────────────────────────────────────

export type SupplyMove =
  | { kind: 'mint'; amount: bigint }
  | { kind: 'burn'; amount: bigint }
  | { kind: 'hold' }

/** `supply = k × m2_value`. */
export function targetSupply(m2Value: bigint, k: bigint): bigint {
  return narrow(m2Value * k)
}

/**
 * Compare current supply with the target.
 *
 * Level-targeting, not a ratchet: a downward M2 revision and genuine
 * quantitative tightening take the identical path, and nothing records a burn
 * the vault could not cover.
 */
export function supplyMove(currentSupply: bigint, target: bigint): SupplyMove {
  if (currentSupply < target) return { kind: 'mint', amount: target - currentSupply }
  if (currentSupply > target) return { kind: 'burn', amount: currentSupply - target }
  return { kind: 'hold' }
}

/**
 * One step of a catch-up walk: move `from` toward `to` by at most `capBps`.
 *
 * The cap is a speed limit, not a veto. A move beyond it is absorbed over
 * several calls rather than refused, because refusing was permanent — see
 * `math.rs` for the full reasoning and the two floors that stop the walk
 * inventing new deadlocks of its own.
 */
export function cappedStep(from: bigint, to: bigint, capBps: number): bigint {
  if (from === 0n) throw new EncMathError('NoBaselineM2')
  const proportional = (from * BigInt(capBps)) / BPS
  const cap = proportional > 1n ? proportional : 1n
  if (to >= from) {
    const raw = from + cap
    const ceiling = raw > U64_MAX ? U64_MAX : raw
    return to < ceiling ? to : ceiling
  }
  const dropped = from > cap ? from - cap : 0n
  const floor = dropped > 1n ? dropped : 1n
  return to > floor ? to : floor
}

/** Scale `value` by `to / from`. */
export function rescale(value: bigint, from: bigint, to: bigint): bigint {
  if (from === 0n) throw new EncMathError('MathOverflow')
  return narrow((value * to) / from)
}

// ── Price interpolation ─────────────────────────────────────────────────────

export interface PriceCurve {
  from: bigint
  to: bigint
  start: number
  end: number
}

export function flatCurve(price: bigint, at: number): PriceCurve {
  return { from: price, to: price, start: at, end: at }
}

/**
 * The price at a moment. Flat at `from` before `start`, flat at `to` after
 * `end`, a straight line between — which is also why retirement needs no code:
 * after the final sync the curve simply arrives and holds.
 */
export function priceAt(curve: PriceCurve, now: number): bigint {
  const end = Math.max(curve.end, curve.start)
  if (now >= end) return curve.to
  if (now <= curve.start) return curve.from
  const span = BigInt(end - curve.start)
  const elapsed = BigInt(now - curve.start)
  const price = curve.from + ((curve.to - curve.from) * elapsed) / span
  const lo = curve.from < curve.to ? curve.from : curve.to
  const hi = curve.from < curve.to ? curve.to : curve.from
  return price < lo ? lo : price > hi ? hi : price
}

// ── The faucet ──────────────────────────────────────────────────────────────

/** The vault's floor: `floorBps` of total supply. */
export function floorAmount(totalSupply: bigint, floorBps: number): bigint {
  return narrow((totalSupply * BigInt(floorBps)) / BPS)
}

/** What one epoch may pay out: `α × max(0, vault − floor × supply)`. */
export function faucetPot(
  vaultBalance: bigint,
  totalSupply: bigint,
  floorBps: number,
  alphaBps: number,
): bigint {
  const floor = floorAmount(totalSupply, floorBps)
  const surplus = vaultBalance > floor ? vaultBalance - floor : 0n
  return narrow((surplus * BigInt(alphaBps)) / BPS)
}

/** One registrant's share of a settled pot. Truncation stays in the vault. */
export function faucetShare(pot: bigint, registrants: number): bigint {
  if (registrants === 0) return 0n
  return pot / BigInt(registrants)
}

/** Below the floor **nothing** pays out — not a share, and not a grant. */
export function aboveFloor(
  vaultBalance: bigint,
  totalSupply: bigint,
  floorBps: number,
): boolean {
  return vaultBalance > floorAmount(totalSupply, floorBps)
}

/** Which epoch a timestamp falls in. */
export function epochOf(unixTimestamp: number, secondsPerEpoch: number): number {
  if (unixTimestamp <= 0 || secondsPerEpoch <= 0) return 0
  return Math.floor(unixTimestamp / secondsPerEpoch)
}
