import { describe, expect, it, beforeEach, afterEach, vi } from 'vitest'
import { mkdtempSync, rmSync, existsSync, writeFileSync, mkdirSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import {
  channelForPort,
  endpointFor,
  heldChannel,
  portForChannel,
  profileFor,
  readLock,
  releaseLock,
  resolveChannel,
  writeLock,
} from './channel'

let root: string
beforeEach(() => {
  root = mkdtempSync(join(tmpdir(), 'chan-'))
})
afterEach(() => {
  rmSync(root, { recursive: true, force: true })
  vi.unstubAllGlobals()
})

/** Make probe() answer for a named set of ports. */
function stubPorts(upPorts: number[]) {
  vi.stubGlobal('fetch', async (url: string) => {
    const port = Number(new URL(url).port)
    if (upPorts.includes(port)) return { ok: true } as Response
    throw new Error('ECONNREFUSED')
  })
}

describe('channel arithmetic', () => {
  it('maps channels to ports and back', () => {
    expect(portForChannel(1)).toBe(9222)
    expect(portForChannel(3)).toBe(9224)
    expect(channelForPort(9223)).toBe(2)
  })

  it('keeps channel 1 on the original profile path', () => {
    expect(profileFor(1)).toBe('.flow-profile')
    expect(profileFor(2)).toBe('.flow-profile-9223')
  })

  it('builds a localhost endpoint', () => {
    expect(endpointFor(9224)).toBe('http://localhost:9224')
  })
})

describe('locks', () => {
  it('round-trips a lock', () => {
    writeLock(root, 2, 'flow', process.pid)
    expect(readLock(root, 2)).toEqual({ pid: process.pid, owner: 'flow' })
    expect(heldChannel(root)).toBe(2)
  })

  it('treats a lock owned by a dead PID as stale and removes it', () => {
    mkdirSync(join(root, '.flow-channels'), { recursive: true })
    // PID 2^31-1 is not a running process on any sane box.
    writeFileSync(join(root, '.flow-channels', '4.lock'), '2147483647 flow\n')
    expect(readLock(root, 4)).toBeNull()
    expect(existsSync(join(root, '.flow-channels', '4.lock'))).toBe(false)
  })

  it('refuses to release a channel owned by someone else', () => {
    writeLock(root, 1, 'flow', process.pid)
    releaseLock(root, 1, process.pid + 1)
    expect(readLock(root, 1)).not.toBeNull()
    releaseLock(root, 1, process.pid)
    expect(readLock(root, 1)).toBeNull()
  })
})

describe('resolveChannel', () => {
  it('honours an explicit FLOW_CDP_PORT pin and claims nothing', async () => {
    stubPorts([9223])
    const r = await resolveChannel(root, 'flow', { FLOW_CDP_PORT: '9223' } as NodeJS.ProcessEnv)
    expect(r).toMatchObject({ channel: 2, port: 9223, how: 'pinned', needsLaunch: false })
    expect(heldChannel(root)).toBeNull()
  })

  it('reports needsLaunch when the pinned port is dead', async () => {
    stubPorts([])
    const r = await resolveChannel(root, 'flow', { FLOW_CDP_PORT: '9299' } as NodeJS.ProcessEnv)
    expect(r.needsLaunch).toBe(true)
  })

  it('claims the lowest running, unclaimed channel', async () => {
    stubPorts([9222, 9223])
    const r = await resolveChannel(root, 'flow', {} as NodeJS.ProcessEnv)
    expect(r).toMatchObject({ channel: 1, port: 9222, how: 'claimed', needsLaunch: false })
    expect(readLock(root, 1)?.owner).toBe('flow')
  })

  it('skips a channel another live process holds', async () => {
    stubPorts([9222, 9223])
    // pid 1 is alive but owned by root, so process.kill(1, 0) throws EPERM — the case that
    // must still read as ALIVE, or we would steal a channel another process holds.
    writeLock(root, 1, 'suno', 1)
    const r = await resolveChannel(root, 'flow', {} as NodeJS.ProcessEnv)
    expect(r.channel).toBe(2)
  })

  it('returns a channel it already holds without re-claiming', async () => {
    stubPorts([9224])
    writeLock(root, 3, 'flow', process.pid)
    const r = await resolveChannel(root, 'flow', {} as NodeJS.ProcessEnv)
    expect(r).toMatchObject({ channel: 3, how: 'held', needsLaunch: false })
  })

  it('falls through to an unlaunched channel and flags needsLaunch', async () => {
    stubPorts([]) // nothing running anywhere
    const r = await resolveChannel(root, 'flow', {} as NodeJS.ProcessEnv)
    expect(r).toMatchObject({ channel: 1, how: 'needs-launch', needsLaunch: true })
  })

  it('throws a directed error when every channel is claimed', async () => {
    stubPorts([])
    for (let c = 1; c <= 2; c++) writeLock(root, c, 'flow', 1)
    await expect(resolveChannel(root, 'flow', {} as NodeJS.ProcessEnv, 2)).rejects.toThrow(/ALL_CHANNELS_BUSY/)
  })
})
