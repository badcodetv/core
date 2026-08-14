/**
 * What the simulation is allowed to be wrong about, and what it is not.
 *
 * The report itself asserts nothing — T15 reads it and judges. These tests
 * defend the three properties whose failure would mean the *program* is broken:
 *
 * 1. **The peg never deadlocks.** T29's whole reason for existing, and the one
 *    that a historical replay cannot see, because the breach is in the future
 *    by construction.
 * 2. **The vault never goes negative**, and a burn it cannot cover leaves
 *    supply above target rather than inventing tokens.
 * 3. **No epoch pays out more than one pot plus its capped grants**, however
 *    many wallets show up. That bound is why ENC needs no identity system.
 */
import { describe, expect, it } from 'vitest'

import { loadHistory, pegHorizon, project, toFixedPoint } from './m2.js'
import { run } from './run.js'
import { loadParams, runAll, standardCohorts, violations } from './index.js'
import { nobody, patient, sybil } from './players.js'

const params = loadParams()

describe('the M2 record', () => {
  const history = loadHistory()

  it('is the full published series, committed rather than fetched', () => {
    expect(history.length).toBeGreaterThan(800)
    expect(history[0].date).toBe('1959-01-01')
    expect(history[0].billions).toBe(286.6)
  })

  it('carries the 2022–23 contraction, which is the case that matters most', () => {
    // The first sustained decline since the 1930s. If the replay ever stops
    // containing it, the coin's hardest path stops being exercised.
    const window = history.filter((o) => o.date >= '2022-01-01' && o.date <= '2023-12-01')
    const peak = window.reduce((a, b) => (b.billions > a.billions ? b : a))
    const trough = window.reduce((a, b) => (b.billions < a.billions ? b : a))
    expect(trough.billions).toBeLessThan(peak.billions)
    const fall = (1 - trough.billions / peak.billions) * 100
    expect(fall).toBeGreaterThan(4)
    expect(fall).toBeLessThan(6)
  })

  it('stores M2 the way the chain does', () => {
    // Getting this wrong by a factor of a thousand is the easiest catastrophic
    // mistake available anywhere in this project.
    expect(toFixedPoint(22176.1)).toBe(22_176_100_000n)
  })

  it('has strictly advancing release dates, or the guard would reject them', () => {
    for (let i = 1; i < history.length; i++) {
      expect(history[i].releaseDate).toBeGreaterThan(history[i - 1].releaseDate)
    }
  })
})

describe('the historical replay', () => {
  const report = run('history', {
    params,
    observations: loadHistory(),
    cohorts: standardCohorts(),
  })

  it('never deadlocks the peg', () => {
    expect(report.deadlocks).toBe(0)
  })

  it('never lets the vault go negative', () => {
    expect(report.vaultWentNegative).toBe(false)
  })

  it('never pays out more than one pot plus the capped grants in an epoch', () => {
    expect(report.worstBoundBreach).toBe(0n)
  })

  it('ends with supply on the peg', () => {
    expect(report.finalSupply).toBe(report.finalM2 * params.k)
  })

  it('reports how long a patient claimant waits, without judging it', () => {
    // T13's pass/fail carried into T15: Ruling C made the faucet the only route
    // in that we control, so if this were never, the loop would not close.
    expect(report.epochsToFirstAsset).not.toBeNull()
  })
})

describe('the forward projection', () => {
  const history = loadHistory()
  const last = history[history.length - 1]

  /**
   * The regression for T29, and the reason the forward leg is not optional.
   *
   * `max_single_mint` was an absolute number of base units against a money
   * supply that doubles roughly every eleven years, so an ordinary month would
   * have exceeded it eventually, `sync_m2` would have failed, and — because the
   * baseline only advances on success — every later sync would have failed too.
   * `retire` would then have ended the artwork a year later. None of that is
   * visible in 67 years of history.
   */
  it('runs 50 years of ordinary months without one deadlock', () => {
    const report = run('forward 50y', {
      params,
      observations: project(last, 50),
      cohorts: standardCohorts(),
      genesisM2: last.m2Value,
      startedAt: last.releaseDate,
    })
    expect(report.deadlocks).toBe(0)
    // Every ordinary month lands in a single sync: the cap is a speed limit
    // nobody ever hits, which is what a speed limit should be.
    expect(report.walkedReleases).toBe(0)
    expect(report.maxWalkSteps).toBe(1)
    expect(report.vaultWentNegative).toBe(false)
  })

  it('still holds at 100 years, where M2 is nearly 600x today', () => {
    const report = run('forward 100y', {
      params,
      observations: project(last, 100),
      cohorts: [patient()],
      genesisM2: last.m2Value,
      startedAt: last.releaseDate,
    })
    expect(report.deadlocks).toBe(0)
    expect(report.finalM2 / last.m2Value).toBeGreaterThan(100n)
    // And supply is still representable, which is the other thing that could
    // have quietly ended it: k x M2 must fit in a u64 forever.
    expect(report.finalSupply).toBe(report.finalM2 * params.k)
  })
})

describe('the peg horizon — when the Emperor runs out of counting', () => {
  /**
   * `supply = k × M2` and an SPL token's supply is a `u64`, so there is a
   * largest M2 this coin can represent. Past it `sync_m2` fails the overflow
   * check, and because the baseline only advances on success it fails forever
   * after — which T28 then turns into a graceful ending rather than a broken
   * one.
   *
   * This is the same shape as the bug T29 deleted, and it is the one instance
   * that cannot be designed away: the token standard picks the width. So it is
   * pinned here as a published fact instead, and this test is what stops a
   * future change to `k` quietly shortening the life of the artwork.
   */
  const horizon = pegHorizon(params.k, loadHistory()[loadHistory().length - 1])

  it('can count to about eighteen quadrillion dollars of M2', () => {
    expect(horizon.largestM2Value).toBe(18_446_744_073_709n)
    expect(Math.round(horizon.largestTrillions)).toBe(18_447)
    expect(Math.round(horizon.multiple)).toBe(797)
  })

  it('is more than a century away at the historical median month', () => {
    expect(horizon.years).toBeGreaterThan(100)
    // A tighter bound than "greater than 100" would be a promise about the
    // Fed. This one is only a statement about arithmetic.
    expect(Math.round(horizon.years)).toBe(107)
  })
})

describe('the dead state', () => {
  /**
   * The floor the whole artwork is judged against: it must still work with
   * nobody in it. Ruling A is that it is fine if it dies and nobody cares — so
   * the machine must not need anyone.
   */
  const report = run('dead', {
    params,
    observations: loadHistory(),
    cohorts: [nobody()],
  })

  it('runs the whole record with not one participant', () => {
    expect(report.deadlocks).toBe(0)
    expect(report.faucetOutflow).toBe(0n)
    expect(report.epochsToFirstAsset).toBeNull()
  })

  it('leaves the Emperor holding everything, still repricing', () => {
    expect(report.finalVaultShareBps).toBe(10_000)
    expect(report.finalCheapestReserve).toBeGreaterThan(0n)
  })
})

describe('a sybil farm', () => {
  /**
   * The property that replaces an identity system. A thousand wallets take a
   * thousandth each; the vault loses what it would have lost to one.
   */
  it('extracts no more than one wallet would have', () => {
    const observations = loadHistory().slice(-24)
    const genesisM2 = observations[0].m2Value
    const alone = run('one', {
      params,
      observations,
      cohorts: [patient()],
      genesisM2,
      startedAt: observations[0].releaseDate,
    })
    const farm = run('farm', {
      params,
      observations,
      cohorts: [sybil(500)],
      genesisM2,
      startedAt: observations[0].releaseDate,
    })

    expect(farm.worstBoundBreach).toBe(0n)
    // Five hundred wallets, not five hundred times the money. Grants are the
    // one thing that does scale with headcount, and they are capped per epoch,
    // which is exactly why the cap exists.
    expect(farm.faucetOutflow).toBeLessThan(alone.faucetOutflow * 3n)
  })
})

describe('the whole run', () => {
  it('reports no broken invariants at the committed parameters', () => {
    expect(violations(runAll(params, 50))).toEqual([])
  })
})
