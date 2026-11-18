import { afterEach, beforeEach, describe, expect, it } from 'vitest'
import { mkdtempSync, rmSync, writeFileSync, mkdirSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'

// Point the queue's machine-local state at a temp folder BEFORE the modules read it.
const home = mkdtempSync(join(tmpdir(), 'flowq-test-'))
process.env.BADCODE_FLOW_QUEUE_HOME = home
const { tryLock, unlock } = await import('./lock')
const { trySlot, release, slotsInUse, tryProject, takeHelper, helpersOf } = await import('./queue-slots')
const { MAX_TABS } = await import('./queue-core')

beforeEach(() => rmSync(home, { recursive: true, force: true }))
afterEach(() => rmSync(home, { recursive: true, force: true }))

describe('locks', () => {
  it('one holder at a time; released by its own token only', () => {
    const d = join(home, 'l')
    const t = tryLock(d)!
    expect(t).toBeTruthy()
    expect(tryLock(d)).toBeNull()
    unlock(d, 'someone-else')
    expect(tryLock(d)).toBeNull()
    unlock(d, t)
    expect(tryLock(d)).toBeTruthy()
  })
  it('breaks a lock whose owner process is dead', () => {
    const d = join(home, 'dead')
    mkdirSync(d, { recursive: true })
    writeFileSync(join(d, 'owner.json'), JSON.stringify({ pid: 2 ** 22 + 12345, token: 'x' }))
    expect(tryLock(d)).toBeTruthy()
  })
})

describe('tab slots', () => {
  it(`gives out exactly ${MAX_TABS}, then waits`, () => {
    const held = Array.from({ length: MAX_TABS }, () => trySlot('t'))
    expect(held.every(Boolean)).toBe(true)
    expect(trySlot('t')).toBeNull()
    expect(slotsInUse()).toBe(MAX_TABS)
    release(held[3])
    expect(trySlot('t')?.n).toBe(3)
  })
})

describe('helper projects', () => {
  it('makes one when none is free, reuses a free one, never shares a busy one', async () => {
    let made = 0
    const make = async (name: string) => { made++; expect(name).toBe(`karen queue ${made}`); return `p${made}` }
    const a = await takeHelper('HOME', 'karen', 't0', make)
    expect(a).toMatchObject({ id: 'p1', made: true })
    const b = await takeHelper('HOME', 'karen', 't1', make) // p1 is busy
    expect(b).toMatchObject({ id: 'p2', made: true })
    release(a.held)
    const c = await takeHelper('HOME', 'karen', 't2', make)
    expect(c).toMatchObject({ id: 'p1', made: false })
    expect(helpersOf('HOME')).toEqual(['p1', 'p2'])
    expect(helpersOf('OTHER-STORY')).toEqual([])
    expect(tryProject('p2', 'x')).toBeNull()
  })
})
