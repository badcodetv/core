/**
 * When the Fed next says how much money there is.
 *
 * The H.6 *Money Stock Measures* release — the publication M2SL arrives in — is
 * put out on the **fourth Tuesday of each month at 1:00pm Eastern**. That is a
 * wall-clock time in a zone that changes its offset twice a year, so this is
 * calendar arithmetic and not a fixed interval: the gap between two consecutive
 * releases is 28 days minus an hour in March and 28 days plus an hour in
 * November, and a countdown built on `28 * 86400` is wrong for half the year.
 *
 * Nothing here touches the chain. The program does not know or care when the
 * Fed publishes — `sync_m2` is permissionless and runs whenever someone calls
 * it — so this is the page telling a visitor when the next number is due, which
 * is the one piece of the machine that lives on a calendar rather than a clock.
 *
 * No timezone library: `Intl.DateTimeFormat` already carries the IANA database
 * in every browser and in Node, and asking it what the wall clock reads at an
 * instant is enough to invert.
 */

/** The zone the Fed publishes on. Not "EST" — that is only half the year. */
export const H6_TIME_ZONE = 'America/New_York'

/** 1:00pm Eastern, the published release time. */
export const H6_HOUR_ET = 13

/** Tuesday, as `Date` counts days of the week. */
const TUESDAY = 2

/**
 * Which day of the month the fourth Tuesday falls on.
 *
 * Pure calendar arithmetic, so it is done in UTC deliberately — a date has no
 * timezone until a time is attached to it, and doing this in local time would
 * make the answer depend on where the visitor is sitting.
 */
export function fourthTuesday(year: number, month: number): number {
  const firstDayOfWeek = new Date(Date.UTC(year, month, 1)).getUTCDay()
  return 1 + ((TUESDAY - firstDayOfWeek + 7) % 7) + 21
}

/** What a zone's UTC offset is at an instant, in milliseconds. */
function zoneOffsetMs(instantMs: number, timeZone: string): number {
  const parts = new Intl.DateTimeFormat('en-US', {
    timeZone,
    hourCycle: 'h23',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  }).formatToParts(new Date(instantMs))

  const field = (type: Intl.DateTimeFormatPartTypes) =>
    Number(parts.find((p) => p.type === type)?.value)

  const asIfUtc = Date.UTC(
    field('year'),
    field('month') - 1,
    field('day'),
    field('hour'),
    field('minute'),
    field('second'),
  )
  return asIfUtc - instantMs
}

/**
 * A wall-clock time in a zone, as a unix timestamp.
 *
 * Two passes, because the offset we need depends on the instant we are trying
 * to find. Guess with the offset at the naive instant, then re-read the offset
 * where that lands and correct once — which converges for any time that is not
 * inside a DST gap, and 1:00pm never is: the transitions happen at 2am.
 */
function wallTimeToUnix(
  year: number,
  month: number,
  day: number,
  hour: number,
  timeZone: string,
): number {
  const naive = Date.UTC(year, month, day, hour)
  const firstPass = naive - zoneOffsetMs(naive, timeZone)
  const corrected = naive - zoneOffsetMs(firstPass, timeZone)
  return Math.floor(corrected / 1000)
}

/** The H.6 release instant for one month, in unix seconds. */
export function h6ReleaseFor(year: number, month: number): number {
  return wallTimeToUnix(
    year,
    month,
    fourthTuesday(year, month),
    H6_HOUR_ET,
    H6_TIME_ZONE,
  )
}

/**
 * The next H.6 release strictly after `now`, in unix seconds.
 *
 * Starts a month behind the current UTC month because a UTC date can be a day
 * ahead of the Eastern one, and ends two ahead so that December's search does
 * not fall off the end of the year — `Date.UTC` normalises out-of-range months,
 * so month 12 is simply next January.
 */
export function nextH6Release(now: number): number {
  const at = new Date(now * 1000)
  const year = at.getUTCFullYear()
  const month = at.getUTCMonth()

  for (let offset = -1; offset <= 2; offset++) {
    // Normalise through Date so a negative or >11 month rolls the year with it.
    const probe = new Date(Date.UTC(year, month + offset, 1))
    const release = h6ReleaseFor(probe.getUTCFullYear(), probe.getUTCMonth())
    if (release > now) return release
  }

  // Unreachable: the +2 probe is always at least four weeks out.
  throw new Error(`no H.6 release found after ${now}`)
}
