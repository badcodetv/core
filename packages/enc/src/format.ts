/**
 * Numbers, printed without lying about them.
 *
 * Every quantity on this coin is a `u64` of base units, and the obvious way to
 * print one — divide by `10 ** decimals` and call `toFixed` — is wrong here
 * rather than merely imprecise: the supply is around 2.2e16 base units, well
 * past the 2^53 where a `Number` starts skipping integers. So the split happens
 * on the decimal string, in `bigint`, and no float is involved anywhere.
 *
 * The countdown formatter lives here too, because "how long until the Fed
 * speaks" and "how long is left in this term" are the same shape and were
 * otherwise going to be written twice.
 */

/** Group a run of digits into thousands. */
function group(digits: string): string {
  return digits.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}

export interface FormatOptions {
  /** How many decimal places to show. Defaults to all of them. */
  fractionDigits?: number
  /** Thousands separators on the integer part. On by default. */
  grouped?: boolean
  /** Keep trailing zeros in the fraction. Off by default. */
  padFraction?: boolean
}

/**
 * Base units as a decimal string. Truncating, never rounding.
 *
 * Rounding up would show a balance nobody has, which on a coin whose whole
 * subject is the honesty of a number is the wrong direction to be wrong in.
 */
export function formatUnits(value: bigint, decimals: number, options: FormatOptions = {}): string {
  const { fractionDigits = decimals, grouped = true, padFraction = false } = options
  const negative = value < 0n
  const magnitude = negative ? -value : value
  const scale = 10n ** BigInt(decimals)

  const whole = (magnitude / scale).toString()
  let fraction = (magnitude % scale).toString().padStart(decimals, '0').slice(0, fractionDigits)
  if (!padFraction) fraction = fraction.replace(/0+$/, '')

  const sign = negative ? '-' : ''
  const integer = grouped ? group(whole) : whole
  return fraction ? `${sign}${integer}.${fraction}` : `${sign}${integer}`
}

/** ENC, at the mint's six decimals. */
export function formatEnc(value: bigint, options: FormatOptions = {}): string {
  return formatUnits(value, 6, options)
}

/**
 * M2 as the Fed says it: billions of dollars.
 *
 * The program stores it as billions at six decimal places, so `22_176_100_000`
 * is $22,176.1bn — and getting that by a factor of a thousand is the easiest
 * catastrophic mistake available on this page.
 */
export function formatM2(value: bigint, fractionDigits = 1): string {
  return `$${formatUnits(value, 6, { fractionDigits, padFraction: true })}bn`
}

/** Basis points as a percentage: `5000` → `50%`. */
export function formatBps(bps: number, fractionDigits = 2): string {
  return `${formatUnits(BigInt(bps), 2, { fractionDigits })}%`
}

/**
 * One quantity as a percentage of another, both in base units.
 *
 * Four decimal places, because the interesting end of this page is very small:
 * the cheapest column is **one basis point** of all the money there is, and a
 * percentage rounded to two places renders that as `0%` — which is not a
 * rounding, it is the opposite of the point being made.
 */
export function formatShare(part: bigint, whole: bigint, fractionDigits = 4): string {
  if (whole === 0n) return '0%'
  // Millionths of the whole, then read as a percentage with four places.
  const millionths = (part * 1_000_000n) / whole
  return `${formatUnits(millionths, 4, { fractionDigits })}%`
}

/**
 * A countdown, largest unit first.
 *
 * Zero and past-zero both render as `now`: a term that ended an hour ago is not
 * "-1h", it is a slot waiting for someone to settle it, and the page says that
 * in words beside this.
 */
export function formatDuration(totalSeconds: number): string {
  if (!Number.isFinite(totalSeconds) || totalSeconds <= 0) return 'now'

  const s = Math.floor(totalSeconds)
  const days = Math.floor(s / 86_400)
  const hours = Math.floor((s % 86_400) / 3_600)
  const minutes = Math.floor((s % 3_600) / 60)
  const secs = s % 60
  const pad = (n: number) => String(n).padStart(2, '0')

  if (days > 0) return `${days}d ${pad(hours)}h ${pad(minutes)}m`
  if (hours > 0) return `${hours}h ${pad(minutes)}m ${pad(secs)}s`
  if (minutes > 0) return `${minutes}m ${pad(secs)}s`
  return `${secs}s`
}
