import { describe, it, expect } from 'vitest'
import { durToSeconds } from './take-row.mts'

describe('durToSeconds', () => {
  it('parses M:SS', () => {
    expect(durToSeconds('3:20')).toBe(200)
    expect(durToSeconds('0:07')).toBe(7)
    expect(durToSeconds('0:00')).toBe(0)
  })

  it('parses MM:SS with more than one minute digit', () => {
    expect(durToSeconds('12:05')).toBe(725)
  })

  it('parses H:MM:SS', () => {
    expect(durToSeconds('1:02:03')).toBe(3723)
  })

  it('tolerates surrounding whitespace', () => {
    expect(durToSeconds(' 3:20\n')).toBe(200)
  })

  it.each([
    [''],
    ['abc'],
    ['200'],       // bare seconds: ambiguous, not a Suno duration
    ['3:2'],       // seconds must be two digits
    ['3:60'],      // seconds out of range
    ['1:60:00'],   // minutes out of range when hours are present
    ['-1:20'],
    ['3:20.5'],
    ['1:2:3:4'],
    [':20'],
  ])('throws on %j', (bad) => {
    expect(() => durToSeconds(bad)).toThrow(/durToSeconds/)
  })
})
