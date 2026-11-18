/**
 * Cross-process locks for everything that shares one Flow browser: the MCP server, the queue runner
 * (queue-runner.ts) and the scene runners (scripts/scene/run.mts, pool.mts). mkdir is atomic, so whoever
 * creates the directory holds the lock. A lock whose owner process is dead, or that is older than
 * `staleMs`, is broken.
 *
 * Why a lock at all (2026-11-18, the Flow queue): Chrome has ONE download folder per browser context, and
 * every Playwright `connectOverCDP` points it at that connection's own temp folder. With several tabs
 * driven at once, whoever connected last got everyone's downloads and the rest failed with ENOENT (pool
 * run 1, 2026-11-17; the 2026-10-23 lost hour was the same thing). So connecting, detaching and
 * downloading all happen under DOWNLOAD_LOCK, one at a time across every process on this machine.
 */
import { existsSync, mkdirSync, readFileSync, rmSync, statSync, writeFileSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

/** Repo root: src/ -> package -> packages/ -> root. */
export const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..', '..')
/** Machine-local queue state (gitignored): runs, tab slots, project locks, helper projects. */
export const QUEUE_HOME = process.env.BADCODE_FLOW_QUEUE_HOME ?? join(REPO_ROOT, '.flow-queue')
/** The one lock every Flow connect, detach and download takes. */
export const DOWNLOAD_LOCK = join(QUEUE_HOME, 'locks', 'download')

export function pidAlive(pid: unknown): boolean {
  if (typeof pid !== 'number' || !Number.isInteger(pid) || pid <= 0) return false
  try {
    process.kill(pid, 0)
    return true
  } catch (err) {
    return (err as NodeJS.ErrnoException).code === 'EPERM'
  }
}

function ownerOf(dir: string): { pid?: number; at?: number; who?: string; token?: string } {
  try {
    return JSON.parse(readFileSync(join(dir, 'owner.json'), 'utf8'))
  } catch {
    return {}
  }
}

/**
 * Try once to take `dir`. Breaks it first when its owner is dead or it is older than `staleMs`
 * (a lock with no owner file yet is only judged by age: its owner may be writing it right now).
 */
export function tryLock(dir: string, who = '', staleMs = Infinity): string | null {
  mkdirSync(dirname(dir), { recursive: true })
  try {
    mkdirSync(dir)
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== 'EEXIST') throw err
    let age = 0
    try {
      age = Date.now() - statSync(dir).mtimeMs
    } catch {
      return null // vanished between the two calls: try again next round
    }
    const o = ownerOf(dir)
    const dead = o.pid !== undefined ? !pidAlive(o.pid) : age > 5_000 && !existsSync(join(dir, 'owner.json'))
    if (!dead && age <= staleMs) return null
    rmSync(dir, { recursive: true, force: true })
    try {
      mkdirSync(dir)
    } catch {
      return null
    }
  }
  // A token, not just the pid: several tabs in ONE process (the queue runner) each take locks.
  const token = `${process.pid}-${Date.now()}-${Math.random().toString(36).slice(2)}`
  writeFileSync(join(dir, 'owner.json'), JSON.stringify({ pid: process.pid, at: Date.now(), who, token }))
  return token
}

/** Release `dir` if `token` still holds it (a lock broken as stale may already belong to someone else). */
export function unlock(dir: string, token: string): void {
  if (ownerOf(dir).token === token) rmSync(dir, { recursive: true, force: true })
}

const nap = (ms: number) => new Promise((r) => setTimeout(r, ms))

/** Wait for `dir`, run `fn`, release. `staleMs` must exceed the longest hold. */
export async function withLock<T>(
  dir: string,
  fn: () => Promise<T>,
  opts: { timeoutMs?: number; staleMs?: number; who?: string } = {},
): Promise<T> {
  const end = Date.now() + (opts.timeoutMs ?? 300_000)
  let token: string | null
  while (!(token = tryLock(dir, opts.who, opts.staleMs ?? 150_000))) {
    if (Date.now() > end) throw new Error(`LOCK_TIMEOUT ${dir}`)
    await nap(150 + Math.random() * 100)
  }
  try {
    return await fn()
  } finally {
    unlock(dir, token)
  }
}
