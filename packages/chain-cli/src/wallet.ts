import { existsSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'
import { chainDir } from './paths.js'
import { chosenRunner } from './docker.js'
import { captureInChain, runInChain } from './runner.js'

/**
 * The deploy wallet's keypair, on the host filesystem.
 *
 * Anchor.toml points at `~/.config/solana/id.json`. Under Docker that `~` is the
 * container's, which is bind-mounted from chain/.solana — so the keypair is a
 * real file you can back up, rather than something trapped in a volume.
 */
export function walletPath(root?: string): string {
  return chosenRunner(process.env, root) === 'docker'
    ? join(chainDir(root), '.solana', 'id.json')
    : join(homedir(), '.config', 'solana', 'id.json')
}

/** Where solana-keygen must write, as seen by whoever is running it. */
const CONTAINER_WALLET = '/home/dev/.config/solana/id.json'

/** Create the deploy wallet if it does not exist yet. Returns true if created. */
export function ensureWallet(root?: string): boolean {
  if (existsSync(walletPath(root))) return false
  const docker = chosenRunner(process.env, root) === 'docker'
  runInChain(
    'solana-keygen',
    ['new', '--no-bip39-passphrase', '--force', '--outfile', docker ? CONTAINER_WALLET : walletPath(root)],
    root,
  )
  return true
}

export function walletAddress(root?: string): string | null {
  const out = captureInChain('solana', ['address'], root)
  return out === null ? null : out.trim()
}

/** Balance in SOL, or null if the cluster is unreachable. */
export function walletBalance(url: string, root?: string): number | null {
  const out = captureInChain('solana', ['balance', '--url', url], root)
  if (out === null) return null
  const n = Number.parseFloat(out.trim().split(/\s+/)[0] ?? '')
  return Number.isFinite(n) ? n : null
}
