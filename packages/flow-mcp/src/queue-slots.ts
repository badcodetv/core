/**
 * Machine-wide bookkeeping for the Flow queue (2026-11-18): tab SLOTS and the projects tabs work in.
 *
 * - Slots: at most MAX_TABS (10) worker tabs at once across EVERY queue run and scripts/scene/pool.mts on
 *   this machine. A tab takes a slot before it opens and gives it back when it closes; when all ten are
 *   taken, the next tab waits. A slot whose owner process died is free again.
 * - Projects: a tab finds its own results by diffing its project's media grid, so two tabs must never
 *   work in the same project at once. Each project a tab works in is locked for the tab's life.
 * - Helper projects: the queue keeps a story's work in that story's projects only (docs/rules/flow.md,
 *   one project per story): its home project, plus helper projects named "<story> queue N", made the
 *   first time they are needed and reused after. Machine-local (each machine may be signed in to a
 *   different Google account), in .flow-queue/helpers.json.
 */
import { existsSync, readFileSync, writeFileSync, renameSync, mkdirSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { QUEUE_HOME, tryLock, unlock, withLock } from './lock'
import { MAX_TABS } from './queue-core'

export interface Held { dir: string; token: string }

const SLOTS = () => join(QUEUE_HOME, 'slots')
const PROJECT_LOCKS = () => join(QUEUE_HOME, 'locks', 'projects')
const REGISTRY = () => join(QUEUE_HOME, 'helpers.json')
const REGISTRY_LOCK = () => join(QUEUE_HOME, 'locks', 'registry')
const nap = (ms: number) => new Promise((r) => setTimeout(r, ms))

/** Take a free tab slot now, or null when all MAX_TABS are taken. */
export function trySlot(who: string): (Held & { n: number }) | null {
  for (let n = 0; n < MAX_TABS; n++) {
    const dir = join(SLOTS(), String(n))
    const token = tryLock(dir, who)
    if (token) return { dir, token, n }
  }
  return null
}

/** Wait for a free tab slot. `onWait` is called once, the first time it has to wait. */
export async function takeSlot(who: string, onWait?: () => void, shouldStop?: () => boolean): Promise<(Held & { n: number }) | null> {
  let told = false
  for (;;) {
    const s = trySlot(who)
    if (s) return s
    if (shouldStop?.()) return null
    if (!told) { told = true; onWait?.() }
    await nap(2_000 + Math.random() * 1_000)
  }
}

export const release = (h: Held | null | undefined): void => { if (h) unlock(h.dir, h.token) }

/** How many slots are taken right now (by anyone). */
export function slotsInUse(): number {
  let n = 0
  for (let i = 0; i < MAX_TABS; i++) if (existsSync(join(SLOTS(), String(i), 'owner.json'))) n++
  return n
}

export function tryProject(id: string, who: string): Held | null {
  const dir = join(PROJECT_LOCKS(), id)
  const token = tryLock(dir, who)
  return token ? { dir, token } : null
}

/** Wait until no other tab is working in project `id`, then hold it. */
export async function takeProject(id: string, who: string, shouldStop?: () => boolean): Promise<Held | null> {
  for (;;) {
    const h = tryProject(id, who)
    if (h) return h
    if (shouldStop?.()) return null
    await nap(2_000)
  }
}

type Registry = Record<string, { story: string; helpers: string[]; named?: number }>
const readRegistry = (): Registry => {
  try { return existsSync(REGISTRY()) ? JSON.parse(readFileSync(REGISTRY(), 'utf8')) : {} } catch { return {} }
}
const writeRegistry = (r: Registry) => {
  mkdirSync(dirname(REGISTRY()), { recursive: true })
  const tmp = `${REGISTRY()}.${process.pid}.tmp`
  writeFileSync(tmp, JSON.stringify(r, null, 1))
  renameSync(tmp, REGISTRY())
}

export function helpersOf(home: string): string[] {
  return readRegistry()[home]?.helpers ?? []
}

/**
 * Hold a helper project of the story whose home project is `home`: the first one no other tab is using,
 * or a new one from `make(name)` when every existing helper is busy.
 */
export async function takeHelper(
  home: string,
  story: string,
  who: string,
  make: (name: string) => Promise<string>,
): Promise<{ id: string; held: Held; made: boolean }> {
  for (const id of helpersOf(home)) {
    const held = tryProject(id, who)
    if (held) return { id, held, made: false }
  }
  // Number the new one under the registry lock so two tabs never pick the same name; make it outside the
  // lock (it drives a browser for a few seconds), then record it.
  const n = await withLock(REGISTRY_LOCK(), async () => {
    const r = readRegistry()
    const row = (r[home] ??= { story, helpers: [] })
    row.named = Math.max(row.named ?? 0, row.helpers.length) + 1
    writeRegistry(r)
    return row.named
  }, { who })
  const id = await make(`${story} queue ${n}`)
  const held = tryProject(id, who)
  if (!held) throw new Error(`PROJECT_LOCK_FAILED: new helper project ${id} is already locked`)
  await withLock(REGISTRY_LOCK(), async () => {
    const r = readRegistry()
    const row = (r[home] ??= { story, helpers: [] })
    if (!row.helpers.includes(id)) row.helpers.push(id)
    writeRegistry(r)
  }, { who })
  return { id, held, made: true }
}
