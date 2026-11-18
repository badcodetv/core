import { describe, expect, it } from 'vitest'
import { COPY_THRESHOLD, isCopyOfAny, meanAbsDiff } from './ref-copy'

const flat = (v: number) => new Uint8Array(256).fill(v)

describe('meanAbsDiff', () => {
  it('is 0 for identical prints', () => expect(meanAbsDiff(flat(100), flat(100))).toBe(0))
  it('averages the per-pixel difference', () => expect(meanAbsDiff(flat(100), flat(110))).toBe(10))
  it('treats mismatched lengths as unrelated', () => expect(meanAbsDiff(flat(1), new Uint8Array(4))).toBe(255))
})

describe('isCopyOfAny', () => {
  it('flags a re-encoded copy (tiny noise)', () => {
    const noisy = flat(120).map((v, i) => v + (i % 8 === 0 ? 1 : 0)) // ~0.125, like the measured 0.06-0.1 copies
    expect(isCopyOfAny(noisy, [flat(120)])).toBe(true)
  })
  it('passes a genuinely new image', () => expect(isCopyOfAny(flat(40), [flat(120)])).toBe(false))
  it('checks every reference', () => expect(isCopyOfAny(flat(60), [flat(200), flat(60)])).toBe(true))
  it('never flags when the print is unreadable', () => expect(isCopyOfAny(null, [flat(1)])).toBe(false))
  it('ignores unreadable references', () => expect(isCopyOfAny(flat(1), [null])).toBe(false))
  it('uses a threshold well below real-result scores', () => expect(COPY_THRESHOLD).toBeLessThan(38))
  it('keeps a small edit (a figure added: 1.5-2.0 on 2026-11-18)', () => expect(COPY_THRESHOLD).toBeLessThan(1.5))
  it('still catches a true copy (0.06-0.1)', () => expect(COPY_THRESHOLD).toBeGreaterThan(0.1))
})
