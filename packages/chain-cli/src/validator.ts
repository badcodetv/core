import { existsSync, readFileSync, rmSync, unlinkSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { chainDir } from './paths.js'
import { capture, runDetached, sleep } from './exec.js'

const RPC_URL = 'http://127.0.0.1:8899'

const ledgerDir = (root?: string): string => join(chainDir(root), 'test-ledger')
const pidFile = (root?: string): string => join(ledgerDir(root), 'validator.pid')

/** Is a local validator answering RPC? */
export async function isUp(url = RPC_URL): Promise<boolean> {
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'getHealth' }),
      signal: AbortSignal.timeout(1500),
    })
    if (!res.ok) return false
    const body = (await res.json()) as { result?: string }
    return body.result === 'ok'
  } catch {
    return false
  }
}

export function readPid(root?: string): number | null {
  const f = pidFile(root)
  if (!existsSync(f)) return null
  const pid = Number.parseInt(readFileSync(f, 'utf8').trim(), 10)
  return Number.isFinite(pid) ? pid : null
}

function alive(pid: number): boolean {
  try {
    // Signal 0 tests for existence without actually signalling.
    process.kill(pid, 0)
    return true
  } catch {
    return false
  }
}

export interface UpOptions {
  /** Wipe the ledger first, so tests start from a known-empty chain. */
  reset?: boolean
  /** Seconds to wait for RPC before giving up. */
  timeoutSeconds?: number
  root?: string
}

/**
 * Start solana-test-validator in the background and wait until it answers.
 *
 * The ledger lives under chain/test-ledger (gitignored) rather than the CWD,
 * which is where the validator would otherwise scatter it.
 */
export async function up(opts: UpOptions = {}): Promise<{ started: boolean; pid: number | null }> {
  const { reset = false, timeoutSeconds = 45, root } = opts

  if (await isUp()) return { started: false, pid: readPid(root) }

  const ledger = ledgerDir(root)
  if (reset && existsSync(ledger)) rmSync(ledger, { recursive: true, force: true })

  const pid = runDetached('solana-test-validator', [
    '--ledger', ledger,
    '--rpc-port', '8899',
    '--quiet',
    ...(reset ? ['--reset'] : []),
  ], { cwd: chainDir(root) })

  for (let i = 0; i < timeoutSeconds * 2; i++) {
    await sleep(500)
    if (await isUp()) {
      writeFileSync(pidFile(root), String(pid))
      return { started: true, pid }
    }
    if (!alive(pid)) throw new Error('Validator exited during startup. Try: chain up --reset')
  }
  throw new Error(`Validator did not answer RPC within ${timeoutSeconds}s`)
}

/** Stop the validator we started. */
export async function down(root?: string): Promise<boolean> {
  const pid = readPid(root)
  if (pid !== null && alive(pid)) {
    process.kill(pid, 'SIGTERM')
    for (let i = 0; i < 20 && alive(pid); i++) await sleep(200)
    if (alive(pid)) process.kill(pid, 'SIGKILL')
  }
  const f = pidFile(root)
  if (existsSync(f)) unlinkSync(f)
  return pid !== null
}

/** Airdrop SOL on a non-mainnet cluster. */
export function airdrop(address: string, sol: number, url: string): void {
  const out = capture('solana', ['airdrop', String(sol), address, '--url', url])
  if (out === null) throw new Error(`Airdrop failed. Is the cluster at ${url} reachable?`)
}
