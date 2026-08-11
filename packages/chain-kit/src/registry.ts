import { PublicKey } from '@solana/web3.js'
import type { Cluster } from './clusters.js'
import programs from './programs.json' with { type: 'json' }

/**
 * Deployed program addresses, keyed by program name then cluster.
 *
 * Deliberately a plain data map with `string` keys: this package is meant to be
 * lifted into unrelated projects, so no program name may be hardcoded in the
 * types or the logic here. Add a program by editing programs.json, not this file.
 */
export type ProgramRegistry = Record<string, Partial<Record<Cluster, string>>>

export const registry: ProgramRegistry = programs as ProgramRegistry

export function knownPrograms(): string[] {
  return Object.keys(registry)
}

/**
 * Address of a program on a cluster.
 *
 * Throws rather than returning null — a missing address means a deploy step was
 * skipped, and failing at the call site with the name in the message beats
 * surfacing later as an inscrutable "account does not exist".
 */
export function programId(name: string, cluster: Cluster, reg: ProgramRegistry = registry): PublicKey {
  const entry = reg[name]
  if (!entry) {
    const known = Object.keys(reg).join(', ') || '(registry is empty)'
    throw new Error(`Unknown program "${name}". Known programs: ${known}`)
  }
  const address = entry[cluster]
  if (!address) {
    const deployed = Object.keys(entry).join(', ') || '(nowhere)'
    throw new Error(`Program "${name}" has no address for cluster "${cluster}". Deployed on: ${deployed}`)
  }
  return new PublicKey(address)
}

/** Whether a program has a recorded address, without throwing. */
export function isDeployed(name: string, cluster: Cluster, reg: ProgramRegistry = registry): boolean {
  return Boolean(reg[name]?.[cluster])
}
