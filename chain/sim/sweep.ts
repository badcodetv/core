/**
 * The T15 parameter sweep.
 *
 *   npx tsx chain/sim/sweep.ts
 *   npx tsx chain/sim/sweep.ts --csv
 *
 * Every number in `chain/params.genesis.json` that is not fixed by arithmetic
 * gets chosen here, from output, rather than typed in because it looked
 * plausible. `chain/sim/RESULTS.md` records what was chosen and what was
 * rejected.
 *
 * **What may and may not justify a choice.** Ruling A is absolute: no economic
 * parameter may be justified or tuned by engagement, retention or turnover —
 * that is precisely how rent came to invert the thesis. What a parameter may be
 * chosen for is **legibility**: whether the sentence it produces is true, short,
 * and says something about money. The one thing that is a genuine pass/fail is
 * whether a patient claimant can ever reach the cheapest tenancy, because Ruling
 * C made the faucet the only route in that BadCode controls — if that fails the
 * loop does not close and the piece is a shop window.
 *
 * The sweep runs from the **real deployment case**: today's M2, forward at the
 * historical median month. The 1959 replay is a different question (does the
 * machine survive the record) and is answered by `index.ts`.
 */
import { loadHistory, project } from './m2.js'
import { run } from './run.js'
import { patients, patientsWithLatecomer } from './players.js'
import { genesisPrices, loadParams } from './index.js'
import type { SimParams } from './economy.js'

const history = loadHistory()
const genesis = history[history.length - 1]
const base = loadParams()

/**
 * Ten slots, cheapest to dearest, as a geometric ladder in **parts per million
 * of the money supply** — never in tokens.
 *
 * A price fixed in base units would be a constant measured against an
 * exponentially growing M2, which is exactly the shape T29 had to delete from
 * the sanity caps. As a fraction it holds forever: every sync rescales all ten
 * by the same factor, so the masthead is always the masthead.
 */
export function ladderPpm(cheapestBps: number, spread: number): number[] {
  const step = Math.pow(spread, 1 / 9)
  return Array.from({ length: 10 }, (_, i) => {
    const ppm = cheapestBps * 100 * Math.pow(step, i)
    // Two significant figures, so the published ladder reads as a decision
    // rather than as the output of a `Math.pow`.
    const magnitude = Math.pow(10, Math.floor(Math.log10(ppm)) - 1)
    return Math.round(ppm / magnitude) * magnitude
  })
}

interface Row {
  floorBps: number
  alphaBps: number
  cheapestBps: number
  claimants: number
  epochsToCheapest: number | null
  epochsToFloor: number | null
  equilibriumShareBps: number
  minShareBps: number
  deadlocks: number
  breach: boolean
}

function trial(params: SimParams, claimants: number, years = 50): Row {
  const report = run('sweep', {
    params,
    observations: project(genesis, years),
    cohorts: [patients(claimants)],
    genesisM2: genesis.m2Value,
    startedAt: genesis.releaseDate,
  })
  return {
    floorBps: params.floorBps,
    alphaBps: params.alphaBps,
    cheapestBps: 0,
    claimants,
    epochsToCheapest: report.epochsToFirstAsset,
    epochsToFloor: report.epochsToVaultFloor,
    equilibriumShareBps: report.finalVaultShareBps,
    minShareBps: report.minVaultShareBps,
    deadlocks: report.deadlocks,
    breach: report.worstBoundBreach > 0n,
  }
}

/**
 * The cheapest slot, as basis points of the money supply. **One basis point.**
 *
 * Chosen on legibility, which is the only thing Ruling A permits a parameter to
 * be chosen on. It gives an exact sentence — *the cheapest column costs one
 * basis point of all the money there is* — and, through the ceiling law in leg
 * 3, an exact second one: **five thousand diligent claimants can each eventually
 * afford it, and the five thousand and first cannot.**
 */
const CHOSEN_CHEAPEST_BPS = 1

/**
 * How much dearer the masthead is than the classified: **a hundred times.**
 *
 * Which puts the dearest slot at 1% of the money supply, so a lone claimant can
 * reach it and fifty competing for it cannot. Ratios freeze at genesis —
 * every sync rescales all ten by the same factor — so the masthead is always
 * the masthead.
 */
const CHOSEN_SPREAD = 100

const FLOORS = [2_500, 4_000, 5_000, 6_000]
const ALPHAS = [100, 250, 500, 1_000, 2_000]
const CHEAPEST_BPS = [1, 5, 10, 25, 50]
const CROWDS = [1, 10, 100, 1_000]

function main() {

  const rows: Row[] = []

  // ── Leg 1: the vault. How the floor and alpha shape the Emperor's hoard ──
  // The ladder is held at the placeholder while this runs, because neither the
  // floor nor alpha depends on what the slots cost.
  console.log('\n## The vault: how long the hoard lasts, and where it settles\n')
  console.log('floor   alpha   hoard reaches floor      settles at   worst dip   deadlocks')
  for (const floorBps of FLOORS) {
    for (const alphaBps of ALPHAS) {
      const r = trial({ ...base, floorBps, alphaBps }, 100)
      rows.push({ ...r, cheapestBps: -1 })
      const reached =
        r.epochsToFloor === null ? 'never' : `${r.epochsToFloor} epochs (${(r.epochsToFloor / 30).toFixed(1)} mo)`
      console.log(
        `${(floorBps / 100).toFixed(0).padStart(4)}%  ` +
          `${(alphaBps / 100).toFixed(2).padStart(6)}%  ` +
          `${reached.padEnd(24)} ` +
          `${(r.equilibriumShareBps / 100).toFixed(2).padStart(8)}%   ` +
          `${(r.minShareBps / 100).toFixed(2).padStart(8)}%   ` +
          `${r.deadlocks}`,
      )
    }
  }

  // ── Leg 2: the ladder. What "anyone patient can afford a small ad" costs ──
  console.log('\n## The cheapest slot: epochs a patient claimant waits, by crowd\n')
  console.log('cheapest slot            ' + CROWDS.map((c) => `${c} claiming`.padStart(14)).join(''))
  for (const cheapestBps of CHEAPEST_BPS) {
    const ppm = ladderPpm(cheapestBps, 10)
    const label = `${(cheapestBps / 100).toFixed(2)}% of supply`
    const cells = CROWDS.map((claimants) => {
      const r = trial({ ...base, genesisPricePpm: ppm }, claimants)
      rows.push({ ...r, cheapestBps })
      return (r.epochsToCheapest === null ? 'never' : `${r.epochsToCheapest}`).padStart(14)
    })
    console.log(`${label.padEnd(24)} ${cells.join('')}`)
  }

  // ── Leg 3: the ceiling, which turned out to be exact ────────────────────
  //
  // The sweep above shows a slot going from "two epochs" to "never" as the
  // crowd grows, and the boundary is not fuzzy.
  //
  // **Corrected 2026-08-13: this prediction was out by a factor of two.** It
  // read the steady state as the faucet paying out everything the Fed printed.
  // It pays out HALF: the floor is half of a supply that is itself growing, so
  // the vault must retain half of every release just to stay level with its own
  // floor, and only the other half is ever above the floor to be paid from. The
  // 50 bps row below is what gives it away — the old formula predicted 200 could
  // get in and the harness had already measured that 200 never do.
  //
  // So: the slot price is a fixed fraction of supply, C diligent claimants split
  // each pot C ways, and each therefore accumulates in the limit a **1/2C share
  // of everything ever printed** — affording a slot costing up to **1/2C of the
  // total supply, and never more.** Inverted, which is how it is published: a
  // slot priced at a fraction p of supply is reachable by at most 1/2p people.
  //
  // That is a hard arithmetic ceiling on how many people can ever hold a
  // column, and it is the honest replacement for the rent-era "Invariant M".
  // Stated, it is the scarcity the piece is about. Unstated, it is a surprise.
  console.log('\n## The ceiling: a slot costing 1/2C of supply is exactly out of reach for C claimants\n')
  console.log('slot as bps of supply   predicted max crowd   200 claiming   500 claiming   2000 claiming')
  for (const cheapestBps of [10, 25, 50]) {
    const ppm = ladderPpm(cheapestBps, 100)
    // 1/2p, with p in basis points. The crowds that beat it in the cells to the
    // right are living off the genesis hoard, not off the steady state; leg 3b
    // is the measurement with the hoard gone.
    const predicted = Math.floor(5_000 / cheapestBps)
    const cells = [200, 500, 2_000].map((claimants) => {
      const r = trial({ ...base, genesisPricePpm: ppm }, claimants, 80)
      rows.push({ ...r, cheapestBps })
      return (r.epochsToCheapest === null ? 'never' : `${r.epochsToCheapest} epochs`).padStart(15)
    })
    console.log(`${String(cheapestBps).padStart(12)} bps ${String(predicted).padStart(21)}   ${cells.join('')}`)
  }

  // ── Leg 3b: the number that is still true in year five ──────────────────
  //
  // Everything above answers the *launch* question, and the answer is "almost
  // no time at all", because the Emperor's genesis hoard is half the money
  // supply and it goes out over the first couple of months. Publishing that as
  // "how long it takes to afford a column" would be a false claim for
  // everybody who arrives afterwards, which is the one bug class this project
  // treats as fatal. So: the measured claimant arrives once the hoard is gone,
  // and competes for a share of new printing like everyone else.
  console.log('\n## The steady state: a claimant who arrives after the hoard is gone\n')
  console.log('crowd      wait for the cheapest column (100 ppm)')
  const LATE = 400
  for (const claimants of [10, 100, 1_000, 4_000, 5_000]) {
    const r = run('late', {
      params: { ...base, genesisPricePpm: ladderPpm(CHOSEN_CHEAPEST_BPS, CHOSEN_SPREAD) },
      observations: project(genesis, 60),
      cohorts: [patientsWithLatecomer(claimants, LATE)],
      genesisM2: genesis.m2Value,
      startedAt: genesis.releaseDate,
    })
    const waited = r.epochsToFirstAsset === null ? null : r.epochsToFirstAsset - LATE
    const asText =
      waited === null
        ? 'never'
        : `${waited} epochs (${(waited / 30).toFixed(1)} months)`
    console.log(`${String(claimants).padStart(6)}     ${asText}`)
  }

  // ── Leg 4: the values that ship ─────────────────────────────────────────
  //
  // Printed rather than typed, so `params.genesis.json` is a transcript of this
  // run. The ladder is computed from `GENESIS_M2_VALUE` — the figure
  // `initialize` bootstraps with — because the ratio is what survives: the
  // first real sync corrects the supply and rescales every price by the same
  // factor, so a slot set at one basis point of the bootstrap supply is still
  // one basis point of the corrected one.
  const GENESIS_M2_VALUE = 22_176_100_000n // state.rs
  const bootstrapSupply = GENESIS_M2_VALUE * base.k
  const chosenPpm = ladderPpm(CHOSEN_CHEAPEST_BPS, CHOSEN_SPREAD)
  const chosen = genesisPrices(chosenPpm, bootstrapSupply)

  console.log('\n## The ladder that ships (parts per million of supply, cheapest first)\n')
  chosen.forEach((price, i) => {
    console.log(
      `  slot ${i}  ${String(chosenPpm[i]).padStart(6)} ppm  ` +
        `= ${(chosenPpm[i] / 100).toFixed(2).padStart(6)} bps  ` +
        `= ${(Number(price) / 1e6).toLocaleString('en-US', { maximumFractionDigits: 0 }).padStart(15)} ENC at genesis  ` +
        // 1/2p, not 1/p — half of every release never leaves the vault.
        `max crowd ${Math.floor(500_000 / chosenPpm[i]).toLocaleString('en-US')}`,
    )
  })
  console.log(`\n  genesisPricePpm: ${JSON.stringify(chosenPpm)}`)

  // The sanity cap, against the record it has to clear.
  let worst = 0
  let worstDate = ''
  for (let i = 1; i < history.length; i++) {
    const move = (Number(history[i].m2Value - history[i - 1].m2Value) * 10_000) / Number(history[i - 1].m2Value)
    if (Math.abs(move) > Math.abs(worst)) { worst = move; worstDate = history[i].date }
  }
  console.log(
    `\n  largest monthly move in the whole record: ${(worst / 100).toFixed(2)}% (${worstDate}) ` +
      `— the ${(base.maxChangeBps / 100).toFixed(0)}% speed limit clears it with room.`,
  )

  const broken = rows.filter((r) => r.deadlocks > 0 || r.breach)
  console.log(
    `\n${rows.length} trials. Deadlocks or bound breaches: ${broken.length}. ` +
      'Every combination above keeps the peg alive; what differs is only what it says.',
  )

  if (process.argv.includes('--csv')) {
    console.log('\nfloorBps,alphaBps,cheapestBps,claimants,epochsToCheapest,epochsToFloor,equilibriumShareBps')
    for (const r of rows) {
      console.log(
        [r.floorBps, r.alphaBps, r.cheapestBps, r.claimants, r.epochsToCheapest ?? '', r.epochsToFloor ?? '', r.equilibriumShareBps].join(','),
      )
    }
  }
}

main()
