/**
 * Turning a run into something a person can read and a ticket can cite.
 *
 * Amounts print as whole ENC (6 decimals) because base units are unreadable at
 * this scale, and the whole point of the report is that a human looks at it and
 * decides. The exact base-unit figures stay in the `RunReport` object.
 */
import type { RunReport } from './run.js'

const DECIMALS = 1_000_000n

export function enc(baseUnits: bigint): string {
  const whole = baseUnits / DECIMALS
  return whole.toLocaleString('en-US')
}

export function pct(bps: number): string {
  return `${(bps / 100).toFixed(2)}%`
}

/** Epochs are days in the shipped parameters, so say both. */
export function epochsAsTime(epochs: number | null, epochSeconds: number): string {
  if (epochs === null) return 'never'
  const days = (epochs * epochSeconds) / 86_400
  if (days < 90) return `${epochs} epochs (${days.toFixed(0)} days)`
  return `${epochs} epochs (${(days / 365).toFixed(1)} years)`
}

export function format(report: RunReport, epochSeconds: number): string {
  const rows: [string, string][] = [
    ['releases replayed', String(report.releases)],
    ['epochs simulated', String(report.epochs)],
    ['releases needing a catch-up walk', String(report.walkedReleases)],
    ['longest walk', `${report.maxWalkSteps} sync${report.maxWalkSteps === 1 ? '' : 's'}`],
    ['DEADLOCKED releases', String(report.deadlocks)],
    ['vault share min / max / final',
      `${pct(report.minVaultShareBps)} / ${pct(report.maxVaultShareBps)} / ${pct(report.finalVaultShareBps)}`],
    ['vault ever negative', report.vaultWentNegative ? 'YES — broken' : 'no'],
    ['burn the vault could not cover', `${enc(report.uncoveredBurn)} ENC`],
    ['paid out by the faucet', `${enc(report.faucetOutflow)} ENC`],
    ['worst breach of the payout bound', `${enc(report.worstBoundBreach)} ENC`],
    ['a patient claimant affords the cheapest tenancy after',
      epochsAsTime(report.epochsToFirstAsset, epochSeconds)],
    ['tenancies bought', String(report.purchases)],
    ['final M2 (billions, 6dp)', report.finalM2.toString()],
    ['final supply', `${enc(report.finalSupply)} ENC`],
    ['final cheapest reserve', `${enc(report.finalCheapestReserve)} ENC`],
  ]
  const width = Math.max(...rows.map(([k]) => k.length))
  const body = rows.map(([k, v]) => `  ${k.padEnd(width)}   ${v}`).join('\n')
  return `── ${report.label} ${'─'.repeat(Math.max(0, 60 - report.label.length))}\n${body}`
}
