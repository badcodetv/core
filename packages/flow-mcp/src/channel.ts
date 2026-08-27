/**
 * Browser CHANNELS — a port + a Chrome profile, claimed by one process at a time.
 *
 * Ruled 2026-08-26 (Kai): *"I never have to mess around with what session or port."* A channel
 * merges the two things nobody should have to think about — which debug port is free and which
 * profile is logged in — into one number.
 *
 *   channel 1 -> CDP 9222, profile .flow-profile
 *   channel 2 -> CDP 9223, profile .flow-profile-9223
 *   channel N -> CDP 9221+N
 *
 * Resolution order, first hit wins:
 *   1. FLOW_CDP_PORT / SUNO_CDP_ENDPOINT — an explicit pin always beats discovery.
 *   2. A live lock this process already holds.
 *   3. The lowest-numbered channel that is UP and unclaimed — claim it.
 *   4. The lowest-numbered channel that is DOWN — report it so the caller can launch it.
 *
 * Locks are files under .flow-channels/ holding the owning PID. A lock whose PID is gone is
 * stale and is ignored, so a crashed session never wedges a channel — the failure mode that
 * would make this whole abstraction worse than typing a port by hand.
 */
import { existsSync, mkdirSync, readFileSync, readdirSync, unlinkSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'

export const FIRST_PORT = 9222
export const MAX_CHANNELS = 8

export const portForChannel = (channel: number): number => FIRST_PORT + channel - 1
export const channelForPort = (port: number): number => port - FIRST_PORT + 1
export const endpointFor = (port: number): string => `http://localhost:${port}`

/** Profile directory for a channel, relative to the repo root. Channel 1 keeps the original path. */
export const profileFor = (channel: number): string =>
  channel === 1 ? '.flow-profile' : `.flow-profile-${portForChannel(channel)}`

export interface ChannelState {
  channel: number
  port: number
  endpoint: string
  /** CDP answered on this port. */
  up: boolean
  /** A live process holds the lock. */
  claimedBy: number | null
  /** What that process said it was doing ("flow", "suno", …). */
  owner: string | null
}

const lockDir = (root: string): string => join(root, '.flow-channels')
const lockPath = (root: string, channel: number): string => join(lockDir(root), `${channel}.lock`)

/**
 * Signal 0 only asks "does this process exist and may I signal it?".
 * 🔴 EPERM means it EXISTS but belongs to another user — that is alive, not dead. Treating
 * EPERM as dead would let one session steal a channel another user's Chrome session holds.
 */
const pidAlive = (pid: number): boolean => {
  try {
    process.kill(pid, 0)
    return true
  } catch (e) {
    return (e as NodeJS.ErrnoException)?.code === 'EPERM'
  }
}

/** Read a lock, deleting it if the owning process is gone. */
export function readLock(root: string, channel: number): { pid: number; owner: string } | null {
  const p = lockPath(root, channel)
  if (!existsSync(p)) return null
  let raw: string
  try {
    raw = readFileSync(p, 'utf8')
  } catch {
    return null
  }
  const [pidRaw, owner = ''] = raw.trim().split(/\s+/, 2)
  const pid = Number(pidRaw)
  if (!Number.isInteger(pid) || pid <= 0 || !pidAlive(pid)) {
    try {
      unlinkSync(p)
    } catch {
      /* another process cleaned it first — fine */
    }
    return null
  }
  return { pid, owner }
}

export function writeLock(root: string, channel: number, owner: string, pid = process.pid): void {
  mkdirSync(lockDir(root), { recursive: true })
  writeFileSync(lockPath(root, channel), `${pid} ${owner}\n`, 'utf8')
}

export function releaseLock(root: string, channel: number, pid = process.pid): void {
  const held = readLock(root, channel)
  if (held && held.pid !== pid) return // never release someone else's channel
  try {
    unlinkSync(lockPath(root, channel))
  } catch {
    /* already gone */
  }
}

/** The channel this PID already holds, if any. */
export function heldChannel(root: string, pid = process.pid): number | null {
  const dir = lockDir(root)
  if (!existsSync(dir)) return null
  for (const f of readdirSync(dir)) {
    const m = /^(\d+)\.lock$/.exec(f)
    if (!m) continue
    const ch = Number(m[1])
    if (readLock(root, ch)?.pid === pid) return ch
  }
  return null
}

/** Does CDP answer here? Short timeout — a dead port must not stall a tool call. */
export async function probe(port: number, timeoutMs = 700): Promise<boolean> {
  const ctl = new AbortController()
  const t = setTimeout(() => ctl.abort(), timeoutMs)
  try {
    const res = await fetch(`${endpointFor(port)}/json/version`, { signal: ctl.signal })
    return res.ok
  } catch {
    return false
  } finally {
    clearTimeout(t)
  }
}

export async function surveyChannels(root: string, max = MAX_CHANNELS): Promise<ChannelState[]> {
  const channels = Array.from({ length: max }, (_, i) => i + 1)
  const up = await Promise.all(channels.map((c) => probe(portForChannel(c))))
  return channels.map((channel, i) => {
    const lock = readLock(root, channel)
    return {
      channel,
      port: portForChannel(channel),
      endpoint: endpointFor(portForChannel(channel)),
      up: up[i]!,
      claimedBy: lock?.pid ?? null,
      owner: lock?.owner ?? null,
    }
  })
}

export interface Resolution {
  channel: number
  port: number
  endpoint: string
  /** How we got here — worth surfacing, because "pinned" and "claimed" behave differently. */
  how: 'pinned' | 'held' | 'claimed' | 'needs-launch'
  /** True when nothing is listening yet and the caller must launch Chrome. */
  needsLaunch: boolean
}

/**
 * Decide which browser this process should talk to. Claims a lock as a side effect unless the
 * port was pinned by env (a pin is the user's explicit instruction and is not ours to own).
 */
export async function resolveChannel(
  root: string,
  owner: string,
  env: NodeJS.ProcessEnv = process.env,
  max = MAX_CHANNELS,
): Promise<Resolution> {
  const pinned = env.FLOW_CDP_PORT ? Number(env.FLOW_CDP_PORT) : null
  if (pinned && Number.isInteger(pinned)) {
    return {
      channel: channelForPort(pinned),
      port: pinned,
      endpoint: endpointFor(pinned),
      how: 'pinned',
      needsLaunch: !(await probe(pinned)),
    }
  }

  const held = heldChannel(root)
  if (held !== null) {
    const port = portForChannel(held)
    return { channel: held, port, endpoint: endpointFor(port), how: 'held', needsLaunch: !(await probe(port)) }
  }

  const survey = await surveyChannels(root, max)

  // Prefer a browser that is already running and nobody has claimed.
  const free = survey.find((c) => c.up && c.claimedBy === null)
  if (free) {
    writeLock(root, free.channel, owner)
    return { channel: free.channel, port: free.port, endpoint: free.endpoint, how: 'claimed', needsLaunch: false }
  }

  // Otherwise the lowest channel with no browser at all — the caller launches it.
  const empty = survey.find((c) => !c.up && c.claimedBy === null)
  if (empty) {
    writeLock(root, empty.channel, owner)
    return { channel: empty.channel, port: empty.port, endpoint: empty.endpoint, how: 'needs-launch', needsLaunch: true }
  }

  throw new Error(
    `ALL_CHANNELS_BUSY: ${max} channels are all claimed by live processes. ` +
      `Free one with: ./scripts/browser-channel.sh release <n>`,
  )
}
