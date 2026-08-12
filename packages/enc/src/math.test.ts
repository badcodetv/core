/**
 * The mirror, checked against the original.
 *
 * **Every vector here is copied from the Rust unit tests in
 * `chain/programs/emperors-new-coin/src/math.rs`.** That is the whole point:
 * the simulation that picks the shipped parameters runs on this file, so if it
 * drifts from the program by one truncation the parameters are chosen against a
 * coin that does not exist. Two languages, one set of numbers, failing together.
 *
 * When a Rust vector changes, change it here in the same commit.
 */
import { describe, expect, it } from 'vitest'
import {
  BPS,
  U64_MAX,
  aboveFloor,
  cappedStep,
  epochOf,
  faucetPot,
  faucetShare,
  flatCurve,
  floorAmount,
  priceAt,
  rescale,
  supplyMove,
  targetSupply,
  type PriceCurve,
} from './math.js'

/** M2SL at the time of writing: $22,176.1bn, 6dp fixed point. */
const M2_REAL = 22_176_100_000n
const K = 1_000_000n
/** `DEFAULT_SECONDS_PER_EPOCH` in state.rs. */
const DAY = 86_400

describe('supply targeting', () => {
  it('targets the real money supply without going near u64', () => {
    const supply = targetSupply(M2_REAL, K)
    expect(supply).toBe(22_176_100_000_000_000n)
    expect(supply < U64_MAX / 800n).toBe(true)
  })

  it('errors rather than wrapping on a target that would not fit', () => {
    expect(() => targetSupply(U64_MAX, K)).toThrow()
    expect(() => targetSupply(U64_MAX, U64_MAX)).toThrow()
    expect(() => targetSupply(U64_MAX / 2n, 3n)).toThrow()
    expect(targetSupply(U64_MAX, 1n)).toBe(U64_MAX)
    expect(() => targetSupply(U64_MAX / 2n + 1n, 2n)).toThrow()
  })

  it('treats a zero target as representable and burns everything', () => {
    expect(targetSupply(0n, K)).toBe(0n)
    expect(supplyMove(500n, 0n)).toEqual({ kind: 'burn', amount: 500n })
    expect(targetSupply(M2_REAL, 0n)).toBe(0n)
  })

  it('moves toward the target in both directions', () => {
    expect(supplyMove(100n, 150n)).toEqual({ kind: 'mint', amount: 50n })
    expect(supplyMove(150n, 100n)).toEqual({ kind: 'burn', amount: 50n })
    expect(supplyMove(100n, 100n)).toEqual({ kind: 'hold' })
    expect(supplyMove(0n, U64_MAX)).toEqual({ kind: 'mint', amount: U64_MAX })
    expect(supplyMove(U64_MAX, 0n)).toEqual({ kind: 'burn', amount: U64_MAX })
  })

  it('treats a revised-down release as an ordinary burn', () => {
    const before = targetSupply(M2_REAL, K)
    // The observed ~0.16% downward restatement between vintages.
    const revised = targetSupply(M2_REAL - M2_REAL / 625n, K)
    expect(supplyMove(before, revised).kind).toBe('burn')
  })
})

describe('the catch-up walk', () => {
  it('lands an in-cap move in one step', () => {
    expect(cappedStep(10_000n, 10_500n, 1_000)).toBe(10_500n)
    expect(cappedStep(10_000n, 9_500n, 1_000)).toBe(9_500n)
    expect(cappedStep(10_000n, 10_000n, 1_000)).toBe(10_000n)
    expect(cappedStep(10_000n, 11_000n, 1_000)).toBe(11_000n)
    expect(cappedStep(10_000n, 9_000n, 1_000)).toBe(9_000n)
  })

  it('walks an oversized move rather than refusing it', () => {
    let m2 = 10_000n
    let steps = 0
    while (m2 !== 15_000n) {
      m2 = cappedStep(m2, 15_000n, 1_000)
      steps += 1
      expect(steps).toBeLessThan(50)
    }
    expect(steps).toBe(5)
  })

  it('never takes a step of zero, however small the numbers', () => {
    expect(cappedStep(5n, 1_000_000n, 1_000)).toBe(6n)
    expect(cappedStep(1n, 1_000_000n, 1)).toBe(2n)
    expect(cappedStep(5n, 1n, 1_000)).toBe(4n)
  })

  it('never walks down to zero, and refuses to walk from it', () => {
    let m2 = 1_000n
    for (let i = 0; i < 500; i++) {
      m2 = cappedStep(m2, 0n, 1_000)
      expect(m2 > 0n).toBe(true)
    }
    expect(m2).toBe(1n)
    expect(() => cappedStep(0n, 1_000n, 1_000)).toThrow()
  })

  it('telescopes to the same total ratio a single rescale would give', () => {
    const price = 1_000_000_000n
    const oneStep = rescale(price, 10_000n, 15_000n)
    let m2 = 10_000n
    let walked = price
    while (m2 !== 15_000n) {
      const next = cappedStep(m2, 15_000n, 1_000)
      walked = rescale(walked, m2, next)
      m2 = next
    }
    const drift = oneStep > walked ? oneStep - walked : walked - oneStep
    expect(drift <= 10n).toBe(true)
  })

  it('saturates at the top of the range rather than refusing', () => {
    expect(cappedStep(U64_MAX, U64_MAX, 1_000)).toBe(U64_MAX)
    expect(cappedStep(U64_MAX - 1n, U64_MAX, 1_000)).toBe(U64_MAX)
    expect(cappedStep(U64_MAX, 0n, 10_000)).toBe(1n)
  })
})

describe('rescaling', () => {
  it('rescales prices by the supply ratio', () => {
    expect(rescale(1_000n, 100n, 101n)).toBe(1_010n)
    expect(rescale(1_000n, 100n, 99n)).toBe(990n)
    expect(rescale(0n, 100n, 200n)).toBe(0n)
  })

  it('refuses impossible inputs instead of returning nonsense', () => {
    expect(() => rescale(1_000n, 0n, 100n)).toThrow()
    expect(() => rescale(U64_MAX, 1n, 2n)).toThrow()
    expect(rescale(U64_MAX, 2n, 2n)).toBe(U64_MAX)
  })
})

describe('price interpolation', () => {
  const curve: PriceCurve = { from: 1_000n, to: 2_000n, start: 0, end: 100 }

  it('interpolates between the endpoints and holds outside them', () => {
    expect(priceAt(curve, -50)).toBe(1_000n)
    expect(priceAt(curve, 0)).toBe(1_000n)
    expect(priceAt(curve, 25)).toBe(1_250n)
    expect(priceAt(curve, 50)).toBe(1_500n)
    expect(priceAt(curve, 100)).toBe(2_000n)
    expect(priceAt(curve, 10_000)).toBe(2_000n)
  })

  it('interpolates downward too', () => {
    const down: PriceCurve = { from: 2_000n, to: 1_000n, start: 0, end: 100 }
    expect(priceAt(down, 25)).toBe(1_750n)
    expect(priceAt(down, 100)).toBe(1_000n)
  })

  it('reads a backwards window as already arrived', () => {
    const bad: PriceCurve = { from: 1_000n, to: 2_000n, start: 100, end: 50 }
    expect(priceAt(bad, 99)).toBe(1_000n)
    expect(priceAt(bad, 100)).toBe(2_000n)
    expect(priceAt(bad, 101)).toBe(2_000n)
  })

  it('never moves a flat curve', () => {
    const flat = flatCurve(1_234n, 500)
    expect(priceAt(flat, 0)).toBe(1_234n)
    expect(priceAt(flat, 500)).toBe(1_234n)
    expect(priceAt(flat, Number.MAX_SAFE_INTEGER)).toBe(1_234n)
  })

  it('survives prices at the top of the range', () => {
    const huge: PriceCurve = { from: 0n, to: U64_MAX, start: 0, end: 1_000 }
    expect(priceAt(huge, 0)).toBe(0n)
    expect(priceAt(huge, 1_000)).toBe(U64_MAX)
    expect(priceAt(huge, 500)).toBe(U64_MAX / 2n)
  })
})

describe('the faucet', () => {
  it('pays alpha of the surplus above the floor', () => {
    expect(faucetPot(800n, 1_000n, 5_000, 1_000)).toBe(30n)
  })

  it('pays nothing at or below the floor', () => {
    expect(faucetPot(500n, 1_000n, 5_000, 1_000)).toBe(0n)
    expect(faucetPot(499n, 1_000n, 5_000, 1_000)).toBe(0n)
    expect(faucetPot(0n, 1_000n, 5_000, 1_000)).toBe(0n)
    expect(aboveFloor(500n, 1_000n, 5_000)).toBe(false)
    expect(aboveFloor(501n, 1_000n, 5_000)).toBe(true)
  })

  it('handles a vault holding the entire supply', () => {
    const supply = targetSupply(M2_REAL, K)
    expect(faucetPot(supply, supply, 5_000, 1_000)).toBe(supply / 20n)
  })

  it('has no floor and no pot at zero supply', () => {
    expect(floorAmount(0n, 5_000)).toBe(0n)
    expect(faucetPot(0n, 0n, 5_000, 1_000)).toBe(0n)
  })

  it('survives the largest representable supply', () => {
    expect(floorAmount(U64_MAX, 10_000)).toBe(U64_MAX)
    expect(floorAmount(U64_MAX, 5_000)).toBe(U64_MAX / 2n)
    expect(() => faucetPot(U64_MAX, U64_MAX, 0, 10_000)).not.toThrow()
  })

  it('divides a pot among its registrants', () => {
    expect(faucetShare(100n, 4)).toBe(25n)
    expect(faucetShare(100n, 3)).toBe(33n)
    expect(faucetShare(1n, 1_000)).toBe(0n)
  })

  it('pays nothing for an empty epoch and does not divide by zero', () => {
    expect(faucetShare(1_000_000n, 0)).toBe(0n)
    expect(faucetShare(0n, 0)).toBe(0n)
  })

  /** The property the whole no-identity design rests on: a farm dilutes itself. */
  it('cannot let a sybil farm extract more than the pot', () => {
    const pot = 1_000_000n
    for (const registrants of [1, 10, 1_000, 100_000, 4_294_967_295]) {
      const total = faucetShare(pot, registrants) * BigInt(registrants)
      expect(total <= pot).toBe(true)
    }
  })
})

describe('epochs', () => {
  it('makes one shipped epoch one day', () => {
    expect(epochOf(0, DAY)).toBe(0)
    expect(epochOf(DAY - 1, DAY)).toBe(0)
    expect(epochOf(DAY, DAY)).toBe(1)
    expect(epochOf(DAY * 20_000, DAY)).toBe(20_000)
    expect(epochOf(1_754_870_400, DAY)).toBe(20_311)
  })

  it('is the same arithmetic at a shorter epoch', () => {
    expect(epochOf(0, 10)).toBe(0)
    expect(epochOf(9, 10)).toBe(0)
    expect(epochOf(10, 10)).toBe(1)
    expect(epochOf(1_754_870_400, 10)).toBe(175_487_040)
  })

  it('clamps a nonsense timestamp or length instead of throwing', () => {
    expect(epochOf(-1, DAY)).toBe(0)
    expect(epochOf(Number.MIN_SAFE_INTEGER, DAY)).toBe(0)
    expect(epochOf(1_754_870_400, 0)).toBe(0)
    expect(epochOf(1_754_870_400, -1)).toBe(0)
  })
})

describe('the constants both languages share', () => {
  it('agrees on basis points', () => {
    expect(BPS).toBe(10_000n)
  })
})
