import { spawn, spawnSync, type SpawnOptions } from 'node:child_process'
import { existsSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'

/**
 * PATH with the Solana and Cargo bin directories added.
 *
 * The Anza installer appends these to ~/.profile, which a non-login shell never
 * reads — so `solana` is on PATH in the user's terminal and missing here. Rather
 * than telling everyone to fix their shell, find the standard locations.
 */
export function toolPath(env: NodeJS.ProcessEnv = process.env): string {
  const extras = [
    join(homedir(), '.local', 'share', 'solana', 'install', 'active_release', 'bin'),
    join(homedir(), '.cargo', 'bin'),
    join(homedir(), '.avm', 'bin'),
  ].filter((p) => existsSync(p))
  const current = env.PATH ?? ''
  const missing = extras.filter((p) => !current.split(':').includes(p))
  return missing.length > 0 ? [...missing, current].join(':') : current
}

export function envWithTools(env: NodeJS.ProcessEnv = process.env): NodeJS.ProcessEnv {
  return { ...env, PATH: toolPath(env) }
}

/** Run a command to completion, inheriting stdio. Throws on non-zero exit. */
export function run(cmd: string, args: string[], opts: SpawnOptions = {}): void {
  const res = spawnSync(cmd, args, { stdio: 'inherit', env: envWithTools(), ...opts })
  if (res.error) {
    const hint = (res.error as NodeJS.ErrnoException).code === 'ENOENT'
      ? ` — is it installed? try: npx tsx packages/cli/src/bin.ts chain doctor`
      : ''
    throw new Error(`Failed to run ${cmd}${hint}`)
  }
  if (res.status !== 0) throw new Error(`${cmd} ${args.join(' ')} exited with ${res.status}`)
}

/** Run a command and capture stdout. Returns null if it fails. */
export function capture(cmd: string, args: string[], opts: SpawnOptions = {}): string | null {
  const res = spawnSync(cmd, args, { encoding: 'utf8', env: envWithTools(), ...opts })
  return res.status === 0 && typeof res.stdout === 'string' ? res.stdout : null
}

/** Start a detached background process, fully unhooked from this one. */
export function runDetached(cmd: string, args: string[], opts: SpawnOptions = {}): number {
  const child = spawn(cmd, args, {
    detached: true,
    stdio: 'ignore',
    env: envWithTools(),
    ...opts,
  })
  child.unref()
  if (child.pid === undefined) throw new Error(`Failed to start ${cmd}`)
  return child.pid
}

export const sleep = (ms: number): Promise<void> => new Promise((r) => setTimeout(r, ms))
