/**
 * Replay a series of Fed releases through the economy and report what happened.
 *
 * **The report asserts nothing.** T14 builds the instrument; T15 reads it and
 * picks the parameters. The only things this file treats as failures are the
 * two that would mean the *program* is broken rather than the parameters badly
 * chosen: a sync that never lands (T29's deadlock) and a vault that goes
 * negative.
 */
import type { Cohort } from './players.js'
import type { Observation } from './m2.js'
import { Economy, type SimParams } from './economy.js'

export interface RunOptions {
  params: SimParams
  observations: Observation[]
  cohorts: Cohort[]
  /** M2 publishes monthly; the faucet runs on epochs. Thirty is a month. */
  epochsPerRelease?: number
  /** Where the coin's own M2 starts. Defaults to the first observation. */
  genesisM2?: bigint
  startedAt?: number
  /**
   * The release date the coin is deployed carrying. Defaults to just before
   * the first observation, i.e. "deployed the month before the replay starts".
   *
   * The program hardcodes zero, which is right for a coin deployed in 2026 and
   * wrong for a replay beginning in 1959 — see `Economy`'s constructor.
   */
  genesisReleaseDate?: number
}

export interface RunReport {
  label: string
  releases: number
  epochs: number
  /** Releases that took more than one `sync_m2` — T29's walk engaging. */
  walkedReleases: number
  maxWalkSteps: number
  /** Releases that never landed. Non-zero means the peg deadlocked. */
  deadlocks: number
  /** How much of a burn the vault could not cover, over the whole run. */
  uncoveredBurn: bigint
  minVaultShareBps: number
  maxVaultShareBps: number
  finalVaultShareBps: number
  /** Negative at any point means the model or the program is wrong. */
  vaultWentNegative: boolean
  finalSupply: bigint
  finalM2: bigint
  /** Total ENC that left the vault through the faucet. */
  faucetOutflow: bigint
  /**
   * The worst any single epoch exceeded its bound, in base units. Anything
   * above zero breaks the property the no-identity design rests on.
   */
  worstBoundBreach: bigint
  /** Epochs before the patient claimant could afford the cheapest reserve. */
  epochsToFirstAsset: number | null
  /**
   * Epochs before the vault first settled within 10bps of its floor.
   *
   * How long the Emperor's genesis hoard takes to distribute. After it, the
   * faucet pays out **half** of what the Fed prints: the floor is half of a
   * supply that is itself growing, so the vault has to retain half of every
   * release just to stay level with its own floor, and only the other half is
   * ever above the floor for the pot to be a fraction of.
   */
  epochsToVaultFloor: number | null
  purchases: number
  finalCheapestReserve: bigint
}

export function run(label: string, options: RunOptions): RunReport {
  const { params, observations, cohorts } = options
  const epochsPerRelease = options.epochsPerRelease ?? 30
  const genesisM2 = options.genesisM2 ?? observations[0].m2Value
  const startedAt = options.startedAt ?? observations[0].releaseDate

  const genesisReleaseDate = options.genesisReleaseDate ?? observations[0].releaseDate - 1
  const economy = new Economy(params, genesisM2, startedAt, genesisReleaseDate)
  const grantCeiling = BigInt(params.grantsPerEpoch) * params.welcomeGrant

  let epochs = 0
  let walkedReleases = 0
  let maxWalkSteps = 0
  let deadlocks = 0
  let uncoveredBurn = 0n
  let minShare = economy.vaultShareBps()
  let maxShare = minShare
  let vaultWentNegative = false
  let faucetOutflow = 0n
  let worstBoundBreach = 0n
  let epochsToFirstAsset: number | null = null
  let epochsToVaultFloor: number | null = null
  let purchases = 0

  const patientWallet = cohorts.find((c) => c.name.startsWith('patient'))?.wallets[0]

  for (const observation of observations) {
    for (let e = 0; e < epochsPerRelease; e++) {
      economy.advance(params.epochSeconds)
      const epoch = economy.epoch()
      const vaultBefore = economy.vault

      for (const cohort of cohorts) {
        for (const wallet of cohort.wallets) {
          // Run-relative, not the chain's absolute epoch index — see `Cohort`.
          if (!cohort.claimsIn(epochs, wallet)) continue
          economy.claim(wallet)
          if (cohort.buys && economy.buyCheapest(wallet) !== null) purchases += 1
        }
      }

      const outflow = vaultBefore - economy.vault
      if (outflow > 0n) faucetOutflow += outflow
      // The headline bound: at most one pot plus the capped grants, however
      // many wallets showed up. Purchases pay *into* the vault, so a cohort
      // that buys can only make this smaller.
      const bound = economy.potOf(epoch - 1) + grantCeiling
      const breach = outflow - bound
      if (breach > worstBoundBreach) worstBoundBreach = breach

      if (economy.vault < 0n) vaultWentNegative = true
      const share = economy.vaultShareBps()
      if (share < minShare) minShare = share
      if (share > maxShare) maxShare = share

      epochs += 1
      if (epochsToVaultFloor === null && share <= params.floorBps + 10) {
        epochsToVaultFloor = epochs
      }
      if (
        epochsToFirstAsset === null &&
        patientWallet !== undefined &&
        economy.balanceOf(patientWallet) >= economy.cheapestReserve()
      ) {
        epochsToFirstAsset = epochs
      }
    }

    const result = economy.sync(observation.m2Value, observation.releaseDate)
    if (result.steps > 1) walkedReleases += 1
    if (result.steps > maxWalkSteps) maxWalkSteps = result.steps
    if (!result.committed) deadlocks += 1
    uncoveredBurn += result.uncovered
  }

  return {
    label,
    releases: observations.length,
    epochs,
    walkedReleases,
    maxWalkSteps,
    deadlocks,
    uncoveredBurn,
    minVaultShareBps: minShare,
    maxVaultShareBps: maxShare,
    finalVaultShareBps: economy.vaultShareBps(),
    vaultWentNegative,
    finalSupply: economy.supply,
    finalM2: economy.m2,
    faucetOutflow,
    worstBoundBreach,
    epochsToFirstAsset,
    epochsToVaultFloor,
    purchases,
    finalCheapestReserve: economy.cheapestReserve(),
  }
}
