/**
 * The release calendar, and the hour that moves.
 *
 * The acceptance criterion this file exists for: **the countdown is correct
 * across a DST boundary.** A release is a wall-clock time in a zone that
 * changes offset twice a year, so the failure mode is not a crash — it is a
 * countdown that is quietly an hour out for five months and looks fine.
 */
import { describe, expect, it } from 'vitest'
import { H6_TIME_ZONE, fourthTuesday, h6ReleaseFor, nextH6Release } from './h6.js'

/** What the wall clock in New York reads at an instant. */
function easternWallClock(unix: number): string {
  return new Intl.DateTimeFormat('en-US', {
    timeZone: H6_TIME_ZONE,
    hourCycle: 'h23',
    weekday: 'short',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  }).format(new Date(unix * 1000))
}

const unixOf = (iso: string) => Math.floor(Date.parse(iso) / 1000)

describe('the fourth Tuesday', () => {
  it('finds it whatever day the month starts on', () => {
    // A month starting on the Tuesday itself: the first Tuesday is the 1st.
    expect(fourthTuesday(2026, 8)).toBe(22) // September 2026 starts on a Tuesday
    // A month starting the day after: the first Tuesday is a whole week later.
    expect(fourthTuesday(2026, 11)).toBe(22) // December 2026 starts on a Tuesday
    expect(fourthTuesday(2026, 0)).toBe(27) // January 2026 starts on a Thursday
    expect(fourthTuesday(2026, 1)).toBe(24) // February 2026 starts on a Sunday
  })

  it('is always the fourth one, never the last one', () => {
    // March 2026 has five Tuesdays (3, 10, 17, 24, 31). The Fed publishes on
    // the fourth, so a "last Tuesday" rule would be a week late once a quarter.
    expect(fourthTuesday(2026, 2)).toBe(24)
  })
})

describe('the release instant', () => {
  it('is 1pm Eastern Standard Time in winter', () => {
    // EST is UTC-5, so 13:00 there is 18:00 UTC.
    expect(h6ReleaseFor(2026, 1)).toBe(unixOf('2026-02-24T18:00:00Z'))
  })

  it('is 1pm Eastern Daylight Time in summer', () => {
    // EDT is UTC-4, so the same wall clock is 17:00 UTC — an hour earlier in
    // absolute time than the February release, which is the whole trap.
    expect(h6ReleaseFor(2026, 2)).toBe(unixOf('2026-03-24T17:00:00Z'))
    expect(h6ReleaseFor(2026, 6)).toBe(unixOf('2026-07-28T17:00:00Z'))
  })

  it('crosses the spring boundary without drifting an hour', () => {
    // DST 2026 begins on 8 March. The February and March releases sit either
    // side of it, and their gap is 28 days minus one hour, not 28 days.
    const february = h6ReleaseFor(2026, 1)
    const march = h6ReleaseFor(2026, 2)
    expect(march - february).toBe(28 * 86_400 - 3_600)
  })

  it('crosses the autumn boundary the other way', () => {
    // DST 2026 ends on 1 November, before that month's fourth Tuesday.
    const october = h6ReleaseFor(2026, 9)
    const november = h6ReleaseFor(2026, 10)
    expect(november).toBe(unixOf('2026-11-24T18:00:00Z'))
    expect(november - october).toBe(28 * 86_400 + 3_600)
  })

  /**
   * The property, rather than a handful of vectors: whatever the offset is
   * doing that month, the answer always reads 13:00 on a Tuesday in New York.
   * Five years is twenty DST transitions, so an off-by-one-hour bug cannot hide
   * in the months nobody wrote a vector for.
   */
  it('always lands at 1pm on a Tuesday in New York, for five years', () => {
    for (let year = 2026; year < 2031; year++) {
      for (let month = 0; month < 12; month++) {
        const clock = easternWallClock(h6ReleaseFor(year, month))
        expect(clock).toMatch(/^Tue,/)
        expect(clock).toMatch(/13:00$/)
        const day = Number(clock.match(/\/(\d{2})\//)?.[1])
        expect(day).toBeGreaterThanOrEqual(22)
        expect(day).toBeLessThanOrEqual(28)
      }
    }
  })
})

describe('the countdown', () => {
  it('finds this month while the release is still ahead', () => {
    const now = unixOf('2026-03-02T12:00:00Z')
    expect(nextH6Release(now)).toBe(unixOf('2026-03-24T17:00:00Z'))
  })

  it('rolls to next month the moment the release lands', () => {
    const march = h6ReleaseFor(2026, 2)
    expect(nextH6Release(march - 1)).toBe(march)
    // At exactly 1pm the number is out; the next one due is April's.
    expect(nextH6Release(march)).toBe(h6ReleaseFor(2026, 3))
  })

  it('rolls over the end of the year', () => {
    const now = unixOf('2026-12-30T00:00:00Z')
    expect(nextH6Release(now)).toBe(h6ReleaseFor(2027, 0))
  })

  it('never returns a release in the past, at any hour of five years', () => {
    // Every six hours across five years: a search window off by a month, or a
    // boundary handled with >= instead of >, shows up here and nowhere else.
    const start = unixOf('2026-01-01T00:00:00Z')
    const end = unixOf('2031-01-01T00:00:00Z')
    for (let now = start; now < end; now += 6 * 3_600) {
      const next = nextH6Release(now)
      expect(next).toBeGreaterThan(now)
      // And it is the *next* one, not a later one. The widest possible wait is
      // the instant after a release on the 22nd of a 31-day month, with the
      // following month's landing on the 28th: 37 days and an hour.
      expect(next - now).toBeLessThanOrEqual(38 * 86_400)
    }
  })
})
