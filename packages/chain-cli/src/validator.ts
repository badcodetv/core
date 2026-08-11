import { existsSync, readFileSync, rmSync, unlinkSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { chainDir } from './paths.js'
import { runDetached, sleep } from './exec.js'
import { chosenRunner, composeDown, composeUpValidator } from './docker.js'
import { captureInChain } from './runner.js'

const RPC_URL = 'http://127.0.0.1:8899'

export const ledgerDir = (root?: string): string => join(chainDir(root), 'test-ledger')
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

async function waitForRpc(timeoutSeconds: number, isDead?: () => boolean): Promise<boolean> {
  for (let i = 0; i < timeoutSeconds * 2; i++) {
    await sleep(500)
    if (await isUp()) return true
    if (isDead?.()) throw new Error('Validator exited during startup. Try: chain up --reset')
  }
  return false
}

export interface UpOptions {
  /** Wipe the ledger first, so tests start from a known-empty chain. */
  reset?: boolean
  /** Seconds to wait for RPC before giving up. */
  timeoutSeconds?: number
  root?: string
}

/**
 * Start the local validator and wait until it answers.
 *
 * Under Docker the validator is a compose service with 8899/8900 published to
 * the host, so a browser wallet and the container hit the same chain. On the
 * host it is a detached solana-test-validator. Either way the ledger lives in
 * chain/test-ledger (gitignored), so `--reset` means the same thing in both.
 */
export async function up(opts: UpOptions = {}): Promise<{ started: boolean; pid: number | null }> {
  const { reset = false, timeoutSeconds = 90, root } = opts
  const docker = chosenRunner(process.env, root) === 'docker'

  if (await isUp()) {
    if (!reset) return { started: false, pid: readPid(root) }
    await down(root)
  }

  const ledger = ledgerDir(root)
  if (reset && existsSync(ledger)) rmSync(ledger, { recursive: true, force: true })

  if (docker) {
    composeUpValidator(root)
    if (!(await waitForRpc(timeoutSeconds))) {
      throw new Error(`Validator did not answer RPC within ${timeoutSeconds}s. Try: docker compose -f chain/docker-compose.yml logs validator`)
    }
    return { started: true, pid: null }
  }

  const pid = runDetached('solana-test-validator', [
    '--ledger', ledger,
    '--rpc-port', '8899',
    '--quiet',
    ...(reset ? ['--reset'] : []),
  ], { cwd: chainDir(root) })

  if (await waitForRpc(timeoutSeconds, () => !alive(pid))) {
    writeFileSync(pidFile(root), String(pid))
    return { started: true, pid }
  }
  throw new Error(`Validator did not answer RPC within ${timeoutSeconds}s`)
}

/** Stop the validator. */
export async function down(root?: string): Promise<boolean> {
  const wasUp = await isUp()

  if (chosenRunner(process.env, root) === 'docker') {
    composeDown(root)
    return wasUp
  }

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
export function airdrop(address: string, sol: number, url: string, root?: string): void {
  const out = captureInChain('solana', ['airdrop', String(sol), address, '--url', url], root)
  if (out === null) throw new Error(`Airdrop failed. Is the cluster at ${url} reachable?`)
}
