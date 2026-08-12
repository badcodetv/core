/**
 * Where the simulation's M2 comes from: the real record, and a plausible future.
 *
 * The history is **committed** (`m2-history.csv`, the full FRED M2SL series,
 * 1959-01 to 2026-06) rather than fetched, so the simulation is deterministic
 * and runs offline. `design/research/2026-08-12-enc-tokenomics/m2-backtest.mjs`
 * is the re-fetchable version and the two must agree; that script is what every
 * published number about M2 is derived from.
 */
import { readFileSync } from 'node:fs'

export interface Observation {
  /** The Fed's own observation date, `YYYY-MM-DD`. */
  date: string
  /** Billions of USD, as published (e.g. `23155.2`). */
  billions: number
  /** The same figure as the chain stores it: billions at 6dp fixed point. */
  m2Value: bigint
  /** Unix seconds of the observation date, which stands in for the release. */
  releaseDate: number
}

/** `22176.1` → `22_176_100_000`. Six decimals, and the rounding is deliberate. */
export function toFixedPoint(billions: number): bigint {
  return BigInt(Math.round(billions * 1e6))
}

export function loadHistory(path = new URL('./m2-history.csv', import.meta.url)): Observation[] {
  const rows = readFileSync(path, 'utf8').trim().split('\n').slice(1)
  return rows
    .map((line) => {
      const [date, value] = line.split(',')
      return { date, billions: Number(value) }
    })
    .filter((r) => Number.isFinite(r.billions))
    .map((r) => ({
      date: r.date,
      billions: r.billions,
      m2Value: toFixedPoint(r.billions),
      // The Fed publishes about a month after the observation. The exact lag
      // does not matter here — the guard only needs the date to advance — but
      // using the observation date keeps the series monotone by construction.
      releaseDate: Math.floor(Date.parse(`${r.date}T00:00:00Z`) / 1000),
    }))
}

/**
 * A future, at the historical median month.
 *
 * **This leg exists because the failure T29 fixed is in the future by
 * construction.** A historical replay alone would have waved it through: every
 * observation in the record is small enough for any cap, and the deadlock only
 * arrives once M2 has outgrown a constant chosen in 2026. Fifty years at the
 * median is the cheapest way to make that arrive inside a test.
 *
 * The median month-on-month move is **+0.522%** over 809 observations, computed
 * by `m2-backtest.mjs`. It is a median rather than a mean on purpose: the mean
 * is dragged by April 2020 (+6.42%), which is exactly the kind of month a
 * forward projection should not assume repeats.
 */
export function project(
  from: Observation,
  years: number,
  monthlyGrowthBps = 52,
): Observation[] {
  const out: Observation[] = []
  let m2 = from.m2Value
  let release = from.releaseDate
  const months = Math.round(years * 12)
  for (let i = 1; i <= months; i++) {
    m2 = m2 + (m2 * BigInt(monthlyGrowthBps)) / 10_000n
    // Thirty days is close enough to a month for a guard that only checks
    // "later than last time".
    release += 30 * 86_400
    const year = Math.floor(i / 12)
    out.push({
      date: `+${year}y${String(i % 12).padStart(2, '0')}m`,
      billions: Number(m2) / 1e6,
      m2Value: m2,
      releaseDate: release,
    })
  }
  return out
}
