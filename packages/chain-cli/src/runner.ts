import { capture, run } from './exec.js'
import { chosenRunner, composeCapture, composeRun } from './docker.js'
import { chainDir } from './paths.js'

/**
 * Run a toolchain command (anchor, solana, cargo) against the Anchor workspace.
 *
 * The point of routing everything through here is that the container is an
 * implementation detail: `anchor build` means the same thing whether it runs in
 * Docker or on the host, and callers never branch on it. CHAIN_RUNNER=host opts
 * out for anyone who already has the toolchain installed.
 */
export function runInChain(cmd: string, args: string[], root?: string): void {
  if (chosenRunner(process.env, root) === 'docker') composeRun(cmd, args, root)
  else run(cmd, args, { cwd: chainDir(root) })
}

export function captureInChain(cmd: string, args: string[], root?: string): string | null {
  if (chosenRunner(process.env, root) === 'docker') return composeCapture(cmd, args, root)
  return capture(cmd, args, { cwd: chainDir(root) })
}
