/**
 * The ENC economic simulation.
 *
 *   npx tsx chain/sim/index.ts --report
 *   npx tsx chain/sim/index.ts --report --params chain/params.genesis.json
 *   npx tsx chain/sim/index.ts --report --forward 50
 *
 * Two legs, and the second is not optional.
 *
 * **The history** replays the full FRED M2SL record, 1959–2026, including the
 * 2022–23 contraction — the first sustained fall since the 1930s, and the one
 * stretch that proves the coin handles a Fed that tightens.
 *
 * **The forward projection** runs decades at the historical median month.
 * It exists because the failure T29 fixed is in the future *by construction*:
 * every observation in the record is small enough for any cap, so a historical
 * replay alone would have waved a doomsday constant straight through.
 *
 * Exits non-zero if the peg ever deadlocks, the vault ever goes negative, or an
 * epoch pays out more than one pot plus its capped grants. Everything else is
 * reported, not judged — T15 does the judging.
 */
import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'

import { loadHistory, project } from './m2.js'
import { run, type RunReport } from './run.js'
import { format } from './report.js'
import { casual, collector, nobody, patient, sybil } from './players.js'
import type { SimParams } from './economy.js'

interface GenesisParams {
  peg: { k: number }
  vault: { floorBps: number }
  faucet: {
    epochSeconds: number
    alphaBps: number
    welcomeGrant: number
    grantsPerEpoch: number
  }
  sanity: { maxChangeBps: number }
  prices: { interpolationSeconds: number }
  assets: { count: number; genesisPrices?: number[] }
}

export function loadParams(path?: string): SimParams {
  const url = path
    ? resolve(process.cwd(), path)
    : new URL('../params.genesis.json', import.meta.url)
  const raw = JSON.parse(readFileSync(url as never, 'utf8')) as GenesisParams
  const count = raw.assets.count
  // Until T15 writes a ladder, use the placeholder the test harness uses: ten
  // prices from one million ENC to ten million, cheapest first.
  const ladder = raw.assets.genesisPrices ?? Array.from({ length: count }, (_, i) => 1e12 * (i + 1))
  return {
    k: BigInt(raw.peg.k),
    floorBps: raw.vault.floorBps,
    alphaBps: raw.faucet.alphaBps,
    welcomeGrant: BigInt(raw.faucet.welcomeGrant),
    grantsPerEpoch: raw.faucet.grantsPerEpoch,
    epochSeconds: raw.faucet.epochSeconds,
    maxChangeBps: raw.sanity.maxChangeBps,
    interpolationSeconds: raw.prices.interpolationSeconds,
    genesisPrices: ladder.map((p) => BigInt(Math.round(p))),
  }
}

/** The standard population: one measuring instrument and a lot of noise. */
export function standardCohorts() {
  return [patient(), collector(), casual(20), sybil(100)]
}

export function runAll(params: SimParams, forwardYears: number): RunReport[] {
  const history = loadHistory()
  const historical = run('the record, 1959–2026', {
    params,
    observations: history,
    cohorts: standardCohorts(),
  })

  const last = history[history.length - 1]
  const forward = run(`${forwardYears} years at the median month (+0.522%)`, {
    params,
    observations: project(last, forwardYears),
    cohorts: standardCohorts(),
    genesisM2: last.m2Value,
    startedAt: last.releaseDate,
  })

  const dead = run('the dead state — nobody ever shows up', {
    params,
    observations: history,
    cohorts: [nobody()],
  })

  return [historical, forward, dead]
}

/** The three things that would mean the program is wrong, not the parameters. */
export function violations(reports: RunReport[]): string[] {
  const problems: string[] = []
  for (const r of reports) {
    if (r.deadlocks > 0) problems.push(`${r.label}: ${r.deadlocks} release(s) deadlocked the peg`)
    if (r.vaultWentNegative) problems.push(`${r.label}: the vault went negative`)
    if (r.worstBoundBreach > 0n) {
      problems.push(`${r.label}: an epoch paid out ${r.worstBoundBreach} base units over its bound`)
    }
  }
  return problems
}

function main() {
  const argv = process.argv.slice(2)
  const paramsPath = argv[argv.indexOf('--params') + 1]
  const forwardArg = argv.indexOf('--forward')
  const forwardYears = forwardArg === -1 ? 50 : Number(argv[forwardArg + 1] ?? 50)

  const params = loadParams(argv.includes('--params') ? paramsPath : undefined)
  const reports = runAll(params, forwardYears)

  if (argv.includes('--json')) {
    console.log(
      JSON.stringify(reports, (_k, v) => (typeof v === 'bigint' ? v.toString() : v), 2),
    )
  } else {
    for (const r of reports) console.log(`${format(r, params.epochSeconds)}\n`)
  }

  const problems = violations(reports)
  if (problems.length > 0) {
    console.error('\nINVARIANTS BROKEN:')
    for (const p of problems) console.error(`  - ${p}`)
    process.exit(1)
  }
  console.log('All invariants hold. What the numbers MEAN is T15\'s call.')
}

// Only when run directly, so the tests can import the pieces.
if (process.argv[1] && import.meta.url.endsWith(process.argv[1].replace(/^.*\/chain/, 'chain'))) {
  main()
}
