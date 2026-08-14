import { describe, expect, it } from 'vitest'
import { toFixedPoint } from './enc'

describe('toFixedPoint', () => {
  it('converts billions-with-decimals to the program’s fixed point', () => {
    expect(toFixedPoint('22176.1')).toBe(22_176_100_000n)
    expect(toFixedPoint('22176')).toBe(22_176_000_000n)
    expect(toFixedPoint('0.000001')).toBe(1n)
    expect(toFixedPoint('0')).toBe(0n)
  })

  /**
   * The reason this parses a string instead of multiplying a number: in
   * IEEE-754, `22176.1 * 1e6` is 22176099999.999996. Rounding a money supply
   * because of a binary fraction is precisely the quiet wrongness this coin
   * cannot afford.
   */
  it('is exact where floating point is not', () => {
    expect(toFixedPoint('22176.1')).toBe(22_176_100_000n)
    expect(Math.round(22176.1 * 1e6)).not.toBe(22176100000 - 1)
    expect(toFixedPoint('0.07')).toBe(70_000n)
    expect(toFixedPoint('1.005')).toBe(1_005_000n)
  })

  it('pads and preserves trailing zeroes correctly', () => {
    expect(toFixedPoint('1.5')).toBe(1_500_000n)
    expect(toFixedPoint('1.500000')).toBe(1_500_000n)
  })

  it('refuses anything that is not a positive decimal', () => {
    for (const bad of ['', '-1', '1e6', 'abc', '1.2.3', ' ', '+1']) {
      expect(() => toFixedPoint(bad), bad).toThrow(/positive decimal/)
    }
  })

  /** Silently dropping a digit would understate the money supply. */
  it('refuses more precision than it can represent', () => {
    expect(() => toFixedPoint('1.0000001')).toThrow(/decimal places/)
    expect(toFixedPoint('1.000000')).toBe(1_000_000n)
  })
})
