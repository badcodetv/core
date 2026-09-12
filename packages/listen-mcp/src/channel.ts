/**
 * Which browser the listen server talks to.
 *
 * 🔴 It cannot reuse Flow's `resolveChannel`. That one claims the LOWEST up-and-unclaimed
 * browser, so whichever server resolved first would take channel 1 — Flow's signed-in browser,
 * which the Playwright MCP also attaches to on 9222 — and silently push the other onto a channel
 * with no login. So listen has its own order, and **never takes channel 1 unless pinned**.
 *
 * 🔴 A Flow tab is a veto, not a tiebreak: `flow.google.com` (Flow moved there from
 * `labs.google/fx/tools/flow` — found 2026-09-11) means that browser belongs to Flow.
 */
import {
  endpointFor,
  heldChannel,
  portForChannel,
  probe,
  surveyChannels,
  writeLock,
  MAX_CHANNELS,
  channelForPort,
  type Resolution,
} from '@badcode/flow-mcp/channel'

export const FLOW_TAB_HOSTS = ['flow.google.com', 'labs.google/fx/tools/flow']
export const STUDIO_TAB_HOST = 'aistudio.google.com'
/** Channel 1 is Flow's and Suno's. Listen starts at 2. */
export const LISTEN_MIN_CHANNEL = 2

export function isListenCandidate(tabUrls: string[]): boolean {
  if (tabUrls.some((u) => FLOW_TAB_HOSTS.some((h) => u.includes(h)))) return false
  return tabUrls.some((u) => u.includes(STUDIO_TAB_HOST))
}

/** Tab URLs from CDP's own listing. Empty on any failure — a browser we cannot read is not a candidate. */
export async function tabUrls(port: number, timeoutMs = 1500): Promise<string[]> {
  try {
    const res = await fetch(`http://localhost:${port}/json/list`, {
      signal: AbortSignal.timeout(timeoutMs),
    })
    if (!res.ok) return []
    const list = (await res.json()) as Array<{ type?: string; url?: string }>
    // Only real pages: the `accounts.google.com/RotateCookiesPage` IFRAME target is what made
    // browser-channel.sh misread a signed-in Flow browser as signed out.
    return list.filter((t) => t.type === 'page').map((t) => t.url ?? '')
  } catch {
    return []
  }
}

export async function resolveListenChannel(
  root: string,
  owner: string,
  env: NodeJS.ProcessEnv = process.env,
  max = MAX_CHANNELS,
): Promise<Resolution> {
  // (1) An explicit pin is the user's instruction — honoured even for channel 1, and never locked.
  const pinned = env.LISTEN_CDP_PORT ? Number(env.LISTEN_CDP_PORT) : null
  if (pinned && Number.isInteger(pinned)) {
    return {
      channel: channelForPort(pinned),
      port: pinned,
      endpoint: endpointFor(pinned),
      how: 'pinned',
      needsLaunch: !(await probe(pinned)),
    }
  }

  // (2) A lock this process already holds.
  const held = heldChannel(root)
  if (held !== null) {
    const port = portForChannel(held)
    return { channel: held, port, endpoint: endpointFor(port), how: 'held', needsLaunch: !(await probe(port)) }
  }

  const survey = (await surveyChannels(root, max)).filter((c) => c.channel >= LISTEN_MIN_CHANNEL)

  // (3) A running, unclaimed browser that already has AI Studio open and is not Flow's.
  for (const c of survey) {
    if (!c.up || c.claimedBy !== null) continue
    if (isListenCandidate(await tabUrls(c.port))) {
      writeLock(root, c.channel, owner)
      return { channel: c.channel, port: c.port, endpoint: c.endpoint, how: 'claimed', needsLaunch: false }
    }
  }

  // (4) The lowest channel with no browser at all — the caller launches it.
  const empty = survey.find((c) => !c.up && c.claimedBy === null)
  if (empty) {
    writeLock(root, empty.channel, owner)
    return { channel: empty.channel, port: empty.port, endpoint: empty.endpoint, how: 'needs-launch', needsLaunch: true }
  }

  throw new Error(
    `ALL_CHANNELS_BUSY: no channel ≥ ${LISTEN_MIN_CHANNEL} is free for listening. ` +
      `Release one (./scripts/browser-channel.sh release <n>) or pin with LISTEN_CDP_PORT.`,
  )
}

/** The exact command a human must run when a channel needs launching. */
export const launchCommand = (channel: number): string => `./scripts/browser-channel.sh up ${channel}`
