/**
 * A tiny cross-process lock for files the pool's workers share (video/inbox/settings.json). mkdir is atomic, so
 * whoever creates the directory holds the lock; a lock older than STALE_MS belongs to a crashed worker and is broken.
 */
import { mkdirSync, rmSync, statSync } from 'node:fs'

const STALE_MS = 30_000
const nap = (ms: number) => Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms)

export function withLock<T>(dir: string, fn: () => T, timeoutMs = 60_000): T {
  const end = Date.now() + timeoutMs
  for (;;) {
    try { mkdirSync(dir); break } catch (err) {
      if ((err as NodeJS.ErrnoException).code !== 'EEXIST') throw err
      try {
        if (Date.now() - statSync(dir).mtimeMs > STALE_MS) { rmSync(dir, { recursive: true, force: true }); continue }
      } catch { continue }
      if (Date.now() > end) throw new Error(`LOCK_TIMEOUT ${dir}`)
      nap(50)
    }
  }
  try { return fn() } finally { rmSync(dir, { recursive: true, force: true }) }
}

/** The same lock around async work (a pool worker's download). `staleMs` must exceed the longest hold. */
export async function withLockAsync<T>(dir: string, fn: () => Promise<T>, timeoutMs = 300_000, staleMs = 150_000): Promise<T> {
  const end = Date.now() + timeoutMs
  for (;;) {
    try { mkdirSync(dir); break } catch (err) {
      if ((err as NodeJS.ErrnoException).code !== 'EEXIST') throw err
      try {
        if (Date.now() - statSync(dir).mtimeMs > staleMs) { rmSync(dir, { recursive: true, force: true }); continue }
      } catch { continue }
      if (Date.now() > end) throw new Error(`LOCK_TIMEOUT ${dir}`)
      await new Promise((r) => setTimeout(r, 200))
    }
  }
  try { return await fn() } finally { rmSync(dir, { recursive: true, force: true }) }
}
