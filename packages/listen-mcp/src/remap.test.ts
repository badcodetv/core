import { describe, it, expect } from 'vitest'
import { formatTime, remapTimestamps } from './remap'

describe('formatTime', () => {
  it('formats minutes and hours', () => {
    expect(formatTime(85)).toBe('1:25')
    expect(formatTime(5)).toBe('0:05')
    expect(formatTime(3725)).toBe('1:02:05')
    expect(formatTime(3600)).toBe('1:00:00')
  })
})

describe('remapTimestamps', () => {
  it('shifts M:SS', () => {
    expect(remapTimestamps('Drop at 0:05', 80)).toEqual({ text: 'Drop at 1:25', count: 1 })
  })
  it('crosses into hours', () => {
    expect(remapTimestamps('0:59', 3600).text).toBe('1:00:59')
  })
  it('shifts H:MM:SS', () => {
    expect(remapTimestamps('at 1:02:05', 60).text).toBe('at 1:03:05')
  })
  it('shifts both ends of a range', () => {
    expect(remapTimestamps('0:05–0:12', 80)).toEqual({ text: '1:25–1:32', count: 2 })
    expect(remapTimestamps('0:05-0:12', 80).text).toBe('1:25-1:32')
  })
  it.each(['4:4', '3:75', '12:3'])('leaves %s alone', (t) => {
    expect(remapTimestamps(`ratio ${t} here`, 80)).toEqual({ text: `ratio ${t} here`, count: 0 })
  })
  it('keeps the text identical at offset 0 but still counts tokens', () => {
    const t = 'intro 0:00, drop **0:32**, outro 1:10'
    expect(remapTimestamps(t, 0)).toEqual({ text: t, count: 3 })
  })
  it('preserves markdown around tokens', () => {
    expect(remapTimestamps('- **0:05** — the kick (`0:10`)', 20).text).toBe('- **0:25** — the kick (`0:30`)')
  })
  it('keeps a fraction when the answer gave one', () => {
    expect(remapTimestamps('0:05.5', 80).text).toBe('1:25.5')
  })
  it('handles a fractional offset', () => {
    expect(remapTimestamps('0:05', 80.4).text).toBe('1:25')
  })
})
