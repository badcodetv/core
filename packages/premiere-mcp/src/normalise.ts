/**
 * Raw panel dump → `SequenceState`.
 *
 * The panel sends what Premiere gave it: Windows paths, plain indices, and transitions as
 * separate track items. This turns that into what a session wants: WSL paths, `v0:2` refs,
 * `V1`/`A1` labels, and transitions attached to the clips they sit between.
 *
 * 🔴 **This function is total. It must never throw.** It runs on the return path of every
 * mutating tool, so a dump that is missing a field — because a Premiere API misbehaved, or a
 * newer panel sent something older code does not know — must degrade to nulls and zeroes rather
 * than take the whole call down with it. Every read here is defensive on purpose.
 */
import { toWsl } from './paths'
import type { AudioClip, Component, Param, SequenceState, TransitionInfo, VideoClip } from './protocol'

/** Times are seconds; a frame at 24fps is ~0.0417s, so this is comfortably sub-frame. */
const EPSILON = 1e-6

/**
 * Premiere counts time in ticks, and there are exactly this many per second. A sequence's
 * `timebase` is ticks-per-FRAME, so dividing gives the frame rate.
 *
 * Callers need that number: **Premiere snaps every edit to a frame boundary.** Ask for a clip at
 * 4.0s in a 23.976 sequence and it lands at 4.004 — not a bug, and not something a caller can
 * predict without knowing the rate. Surfacing it here means nobody has to guess or hard-code it.
 */
const TICKS_PER_SECOND = 254_016_000_000

function frameRateFrom(timebase: string): number {
  const ticksPerFrame = Number(timebase)
  if (!Number.isFinite(ticksPerFrame) || ticksPerFrame <= 0) return 0
  return TICKS_PER_SECOND / ticksPerFrame
}

export function normaliseSequence(raw: unknown): SequenceState {
  const dump = obj(raw)
  const sequence = obj(dump.sequence)
  const frameSize = obj(sequence.frameSize)
  const project = obj(dump.project)
  const timebase = str(sequence.timebase)

  return {
    project: {
      name: str(project.name),
      path: wslPath(project.path),
    },
    sequence: {
      name: str(sequence.name),
      guid: str(sequence.guid),
      timebase,
      frameRate: frameRateFrom(timebase),
      frameSize: { w: num(frameSize.w), h: num(frameSize.h) },
      end: num(sequence.end),
      playhead: num(sequence.playhead),
    },
    videoTracks: arr(dump.videoTracks).map((track, i) => normaliseTrack(track, i, 'v')) as SequenceState['videoTracks'],
    audioTracks: arr(dump.audioTracks).map((track, i) => normaliseTrack(track, i, 'a')) as SequenceState['audioTracks'],
    markers: arr(dump.markers).map((m) => {
      const marker = obj(m)
      return {
        name: str(marker.name),
        start: num(marker.start),
        duration: num(marker.duration),
        comments: str(marker.comments),
      }
    }),
  }
}

function normaliseTrack(rawTrack: unknown, fallbackIndex: number, kind: 'v' | 'a'): {
  index: number
  label: string
  name: string
  muted: boolean
  items: (VideoClip | AudioClip)[]
  transitionCount: number
} {
  const track = obj(rawTrack)
  const index = Number.isFinite(track.index) ? (track.index as number) : fallbackIndex
  const transitions = arr(track.transitions).map(obj)

  const items = arr(track.items).map((rawItem, itemIndex) => {
    const item = obj(rawItem)
    const start = num(item.start)
    const end = num(item.end)

    const base = {
      ref: `${kind}${index}:${itemIndex}`,
      name: str(item.name),
      start,
      end,
      duration: num(item.duration),
      inPoint: num(item.inPoint),
      outPoint: num(item.outPoint),
      mediaPath: item.mediaPath == null ? null : wslPath(item.mediaPath),
      disabled: bool(item.disabled),
      speed: Number.isFinite(item.speed) ? (item.speed as number) : 1,
      components: arr(item.components).map(normaliseComponent),
    }

    if (kind === 'a') return base as AudioClip
    return { ...base, transitions: attachTransitions(transitions, start, end) } as VideoClip
  })

  return {
    index,
    // Premiere's UI is 1-based ("V1"), its API is 0-based. Carry both so nobody has to remember.
    label: `${kind === 'v' ? 'V' : 'A'}${index + 1}`,
    name: str(track.name),
    muted: bool(track.muted),
    items,
    // Defaults to 0 for a dump from an older panel, which is the honest answer: it did not say.
    transitionCount: num(track.transitionCount),
  }
}

/**
 * A transition is its own track item, with no back-reference to the clips it joins — so match it
 * by time. A cross dissolve at a cut sits across the boundary, meaning the outgoing clip's `end`
 * and the incoming clip's `start` both fall inside its span.
 *
 * Best-effort by nature: alignment can be centred, start-at-cut or end-at-cut, so containment is
 * tested inclusively at both edges. A clip shorter than the transition it sits under can pick up
 * both — which is the honest answer, since it is genuinely under both halves.
 */
function attachTransitions(
  transitions: Record<string, unknown>[],
  clipStart: number,
  clipEnd: number
): { start?: TransitionInfo; end?: TransitionInfo } {
  const out: { start?: TransitionInfo; end?: TransitionInfo } = {}

  for (const t of transitions) {
    const tStart = num(t.start)
    const tEnd = num(t.end)
    const info: TransitionInfo = { matchName: str(t.matchName), duration: num(t.duration) }

    if (!out.start && covers(tStart, tEnd, clipStart)) out.start = info
    if (!out.end && covers(tStart, tEnd, clipEnd)) out.end = info
  }
  return out
}

function covers(spanStart: number, spanEnd: number, t: number): boolean {
  return t >= spanStart - EPSILON && t <= spanEnd + EPSILON
}

function normaliseComponent(rawComponent: unknown, index: number): Component {
  const component = obj(rawComponent)
  return {
    index: Number.isFinite(component.index) ? (component.index as number) : index,
    matchName: str(component.matchName),
    displayName: str(component.displayName),
    params: arr(component.params).map(normaliseParam),
  }
}

function normaliseParam(rawParam: unknown, index: number): Param {
  const param = obj(rawParam)
  const out: Param = {
    index: Number.isFinite(param.index) ? (param.index as number) : index,
    name: str(param.name),
    value: param.value ?? null,
    timeVarying: bool(param.timeVarying),
  }
  if (Array.isArray(param.keyframes)) {
    out.keyframes = param.keyframes.map((k) => {
      const kf = obj(k)
      return { t: num(kf.t), value: kf.value ?? null }
    })
  }
  // Carried, not inferred: `value: null` is a legitimate value for a readable param, so the only
  // way to know Premiere refused is for the panel to say so.
  if (param.unreadable === true) out.unreadable = true
  return out
}

/* ---- defensive readers ------------------------------------------------------------------------ */

function obj(v: unknown): Record<string, unknown> {
  return typeof v === 'object' && v !== null && !Array.isArray(v) ? (v as Record<string, unknown>) : {}
}

function arr(v: unknown): unknown[] {
  return Array.isArray(v) ? v : []
}

function str(v: unknown): string {
  return typeof v === 'string' ? v : ''
}

function num(v: unknown): number {
  return typeof v === 'number' && Number.isFinite(v) ? v : 0
}

function bool(v: unknown): boolean {
  return v === true
}

/** Empty rather than a bogus path: `''` reads as "no path", a half-translated string does not. */
function wslPath(v: unknown): string {
  const s = str(v)
  return s ? toWsl(s) : ''
}
