/**
 * Printing numbers that a `Number` cannot hold.
 *
 * The supply is around 2.2e16 base units, which is past 2^53 — so the test that
 * matters most here is the one where the naive implementation is off by a few
 * units and nothing else notices.
 */
import { describe, expect, it } from 'vitest'
import {
  formatBps,
  formatDuration,
  formatEnc,
  formatM2,
  formatShare,
  formatUnits,
  parseEnc,
  parseUnits,
} from './format.js'

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

describe('reading a typed figure back', () => {
  it('round-trips what the page prints, separators and all', () => {
    // A bidder copies the reserve off the column and pastes it into the box.
    // Rejecting it for looking like the page would be its own small insult.
    expect(parseEnc('22,176,100,000')).toBe(22_176_100_000_000_000n)
    expect(parseEnc(formatEnc(1_234_567n))).toBe(1_234_567n)
  })

  it('keeps every base unit past 2^53', () => {
    // `parseFloat` loses the low digits here, and this is the number that
    // leaves somebody's wallet.
    expect(parseEnc('22176100000.000001')).toBe(22_176_100_000_000_001n)
  })

  it('truncates beyond the mint’s decimals rather than rounding up', () => {
    expect(parseEnc('1.9999999')).toBe(1_999_999n)
  })

  it('fills in the halves people actually type', () => {
    expect(parseEnc('5')).toBe(5_000_000n)
    expect(parseEnc('0.5')).toBe(500_000n)
    expect(parseEnc('.5')).toBe(500_000n)
    expect(parseEnc('5.')).toBe(5_000_000n)
    expect(parseUnits('1', 0)).toBe(1n)
  })

  it('refuses anything that is not a number', () => {
    for (const bad of ['', ' ', '.', 'lots', '1e9', '-1', '1.2.3', '0x10']) {
      expect(parseEnc(bad), bad).toBe(null)
    }
  })
})
