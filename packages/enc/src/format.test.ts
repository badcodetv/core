/**
 * Printing numbers that a `Number` cannot hold.
 *
 * The supply is around 2.2e16 base units, which is past 2^53 — so the test that
 * matters most here is the one where the naive implementation is off by a few
 * units and nothing else notices.
 */
import { describe, expect, it } from 'vitest'
import { formatBps, formatDuration, formatEnc, formatM2, formatShare, formatUnits } from './format.js'

describe('base units', () => {
  it('splits on the string, so nothing rounds at scale', () => {
    // The supply at today's M2: 22,176,100,000 ENC, exactly.
    const supply = 22_176_100_000_000_000n
    expect(formatEnc(supply)).toBe('22,176,100,000')
    // One base unit off, which a float would swallow entirely.
    expect(formatEnc(supply + 1n)).toBe('22,176,100,000.000001')
    expect(formatEnc(supply - 1n)).toBe('22,176,099,999.999999')
  })

  it('truncates rather than rounding up', () => {
    // Rounding up would show a balance nobody has.
    expect(formatEnc(1_999_999n, { fractionDigits: 2 })).toBe('1.99')
  })

  it('keeps the sign on a negative drift', () => {
    expect(formatEnc(-1_500_000n)).toBe('-1.5')
  })

  it('pads or trims the fraction on request', () => {
    expect(formatEnc(1_500_000n)).toBe('1.5')
    expect(formatEnc(1_500_000n, { fractionDigits: 2, padFraction: true })).toBe('1.50')
    expect(formatEnc(1_000_000n)).toBe('1')
    expect(formatUnits(1_000_000n, 6, { grouped: false, fractionDigits: 0 })).toBe('1')
  })

  it('shows a sub-unit amount without pretending it is zero', () => {
    expect(formatEnc(1n)).toBe('0.000001')
  })
})

describe('M2', () => {
  it('reads in billions, which is the factor of a thousand that kills you', () => {
    // 22_176_100_000 is $22,176.1bn, not $22.1bn and not $22,176,100bn.
    expect(formatM2(22_176_100_000n)).toBe('$22,176.1bn')
    expect(formatM2(22_176_100_000n, 3)).toBe('$22,176.100bn')
  })
})

describe('basis points', () => {
  it('reads as the percentage it is', () => {
    expect(formatBps(5_000)).toBe('50%')
    expect(formatBps(1_000)).toBe('10%')
    // The cheapest slot: one basis point of all the money there is.
    expect(formatBps(1)).toBe('0.01%')
  })
})

describe('a share of the money supply', () => {
  it('keeps the small end visible', () => {
    // The cheapest column is a hundredth of a percent of everything. Two
    // decimal places would print that as 0% and delete the joke.
    expect(formatShare(1n, 10_000n)).toBe('0.01%')
    expect(formatShare(72n, 1_000_000n)).toBe('0.0072%')
    expect(formatShare(1n, 1_000_000n)).toBe('0.0001%')
  })

  it('handles the large end and the empty one', () => {
    expect(formatShare(7_200n, 1_000_000n)).toBe('0.72%')
    expect(formatShare(1n, 1n)).toBe('100%')
    expect(formatShare(1n, 0n)).toBe('0%')
  })
})

describe('countdowns', () => {
  it('leads with the largest unit that is not zero', () => {
    expect(formatDuration(12 * 86_400 + 3_600 + 61)).toBe('12d 01h 01m')
    expect(formatDuration(3_661)).toBe('1h 01m 01s')
    expect(formatDuration(61)).toBe('1m 01s')
    expect(formatDuration(9)).toBe('9s')
  })

  it('says now rather than counting backwards', () => {
    // A term that ended an hour ago is a slot waiting to be settled, not "-1h".
    expect(formatDuration(0)).toBe('now')
    expect(formatDuration(-3_600)).toBe('now')
    expect(formatDuration(Number.NaN)).toBe('now')
  })
})
