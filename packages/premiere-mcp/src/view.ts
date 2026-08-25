/**
 * `SequenceState` → something a language model can actually read.
 *
 * ## Why this file exists
 *
 * The first hand-cut project the bridge ever opened — Jack's camping edit, 149 video and 135
 * audio clips — produced a `SequenceState` of **573,065 bytes**. The MCP transport refuses a
 * result that large, so *every one of the thirteen tools that returns a state* was unusable on
 * it. Trimming was measured and does not save you: dropping every intrinsic component still
 * leaves 64 KB, because 284 clips of scaffolding is 58 KB on its own.
 *
 * **Only summarising works.** The same timeline as a digest is **1,154 bytes** — a 500× cut — and
 * the size is governed by the number of *tracks*, not the number of clips, so it does not grow
 * with the edit.
 *
 * ## The contract
 *
 * 1. **The full state is never thrown away.** It is written to disk beside the project and the
 *    path comes back as `statePath`. A session that needs everything runs `jq` over that file,
 *    which costs it no context at all. This file only decides what is worth *saying*.
 * 2. **Say what changed.** After an edit, the useful signal is not the whole timeline — it is the
 *    clips that moved. `diffStates` finds them by comparing against the previous state, so
 *    `insert_clip` can report the ref of the clip it just created without anyone having to guess.
 * 3. **Never exceed the budget.** `fitToBudget` degrades through a fixed ladder until the result
 *    fits, and says in `notes` what it dropped and how to get it back. A caller can always trust
 *    that a state-returning tool returns.
 *
 * That last point is a correctness fix, not an ergonomic one. When the transport refuses an
 * oversized result, the refusal happens *after* the panel has committed the edit — so the caller
 * sees an error for work that actually succeeded. Making the result always fit removes the trap.
 */
import type { AudioClip, Component, SequenceState, VideoClip } from './protocol'

type AnyClip = VideoClip | AudioClip

/**
 * Character budget for a tool result. The transport's real cap is expressed in tokens; dense
 * JSON runs around 2.5 characters per token, and a 63,543-character result was refused, which
 * puts the ceiling near 25k tokens. 30,000 characters (~12k tokens) leaves generous headroom and
 * is still large enough to hold a whole track's clips.
 */
export const DEFAULT_BUDGET = 30_000

/** How many clips a `changed` report will name in full before it starts counting instead. */
const MAX_CHANGED_DETAIL = 40

// ---- the view shape ----------------------------------------------------------------------------

export interface ClipSummary {
  ref: string
  name: string
  start: number
  end: number
  duration: number
  inPoint: number
  outPoint: number
  mediaPath: string | null
  disabled: boolean
  speed: number
  /** Present only when components survived the budget. */
  components?: ComponentSummary[]
  /** Set when components were dropped to fit — says how many there were. */
  componentCount?: number
}

export interface ComponentSummary {
  index: number
  matchName: string
  displayName: string
  params?: { index: number; name: string; value: unknown; timeVarying?: true; unreadable?: true }[]
  paramCount?: number
  /** Blank-named duplicate slots folded away — see `foldNoiseParams`. */
  omittedParams?: number
}

export interface TrackView {
  index: number
  label: string
  name: string
  muted: boolean
  /** Number of clips on the track. */
  clipCount: number
  transitionCount: number
  /** First start and last end, or null on an empty track. */
  span: [number, number] | null
  /** Present only for tracks the caller selected. */
  clips?: ClipSummary[]
}

export interface SequenceView {
  project: SequenceState['project']
  sequence: SequenceState['sequence']
  videoTracks: TrackView[]
  audioTracks: TrackView[]
  markers: { count: number; items?: SequenceState['markers'] }
  totals: { videoClips: number; audioClips: number; components: number; params: number }
  /** Where the complete, untrimmed `SequenceState` was written. `jq` over this for anything
   * the view does not carry. Absent if the write failed (a `note` says so). */
  statePath?: string
  /** What this edit changed, when a previous state was available to compare against. */
  changed?: ChangeReport
  /** Anything the caller should know: what was dropped, and how to get it. */
  notes?: string[]
}

export interface ChangeReport {
  added: ClipSummary[]
  removed: { ref: string; name: string; start: number }[]
  modified: { ref: string; name: string; was: ClipDelta; now: ClipDelta }[]
  /** Set when there were more changes than were listed in full. */
  more?: { added: number; removed: number; modified: number }
}

interface ClipDelta {
  start: number
  end: number
  inPoint: number
  outPoint: number
}

export interface Selection {
  /** Track labels or refs: `['v2']`, `['V3', 'A1']`. Case-insensitive. */
  tracks?: string[]
  /** Specific clips by ref: `['v2:3', 'v2:4']`. Implies their tracks. */
  clips?: string[]
  /** Seconds. Only clips overlapping this window are listed. */
  range?: [number, number]
  /** Include effect parameters on selected clips. Default true when a selection narrows things. */
  params?: boolean
}

// ---- building the view -------------------------------------------------------------------------

/**
 * Summarise a state, expanding only what `selection` asks for.
 *
 * With no selection this is the digest: every track described, no clip listed. That is the right
 * default because it answers the question a session actually has after an edit — *what does the
 * timeline look like now* — in a kilobyte, whatever the size of the edit.
 */
export function buildView(state: SequenceState, selection: Selection = {}): SequenceView {
  const wantedTracks = resolveTrackSelection(state, selection)
  const clipRefs = selection.clips?.length ? new Set(selection.clips.map((r) => r.toLowerCase())) : null
  const includeParams = selection.params !== false

  const view: SequenceView = {
    project: state.project,
    sequence: state.sequence,
    videoTracks: state.videoTracks.map((t) =>
      trackView(t, 'v', wantedTracks, clipRefs, selection.range, includeParams)
    ),
    audioTracks: state.audioTracks.map((t) =>
      trackView(t, 'a', wantedTracks, clipRefs, selection.range, includeParams)
    ),
    markers: state.markers.length ? { count: state.markers.length, items: state.markers } : { count: 0 },
    totals: totalsOf(state),
  }
  return view
}

function trackView(
  track: SequenceState['videoTracks'][number] | SequenceState['audioTracks'][number],
  kind: 'v' | 'a',
  wantedTracks: Set<string> | null,
  clipRefs: Set<string> | null,
  range: [number, number] | undefined,
  includeParams: boolean
): TrackView {
  const key = `${kind}${track.index}`
  const base: TrackView = {
    index: track.index,
    label: track.label,
    name: track.name,
    muted: track.muted,
    clipCount: track.items.length,
    transitionCount: track.transitionCount,
    span: spanOf(track.items),
  }

  // No selection at all → digest only. This is the common case and the one that must stay small.
  if (!wantedTracks && !clipRefs && !range) return base
  if (wantedTracks && !wantedTracks.has(key)) return base

  const clips = (track.items as AnyClip[]).filter((c) => {
    if (clipRefs && !clipRefs.has(c.ref.toLowerCase())) return false
    if (range && !overlaps(c.start, c.end, range[0], range[1])) return false
    return true
  })
  // A track the caller narrowed to nothing is still reported as a summary, not as `clips: []`,
  // so "no clips here" and "you did not ask about this track" stay distinguishable.
  if (!clips.length) return base

  return { ...base, clips: clips.map((c) => clipSummary(c, includeParams)) }
}

function clipSummary(clip: AnyClip, includeParams: boolean): ClipSummary {
  const out: ClipSummary = {
    ref: clip.ref,
    name: clip.name,
    start: clip.start,
    end: clip.end,
    duration: clip.duration,
    inPoint: clip.inPoint,
    outPoint: clip.outPoint,
    mediaPath: clip.mediaPath,
    disabled: clip.disabled,
    speed: clip.speed,
  }
  if (clip.components.length) {
    out.components = clip.components.map((c) => componentSummary(c, includeParams))
  }
  return out
}

function componentSummary(component: Component, includeParams: boolean): ComponentSummary {
  const out: ComponentSummary = {
    index: component.index,
    matchName: component.matchName,
    displayName: component.displayName,
  }
  if (!includeParams) {
    out.paramCount = component.params.length
    return out
  }
  const { params, omitted } = foldNoiseParams(component.params)
  out.params = params.map((p) => ({
    index: p.index,
    name: p.name,
    value: p.value,
    ...(p.timeVarying ? { timeVarying: true as const } : {}),
    ...(p.unreadable ? { unreadable: true as const } : {}),
  }))
  if (omitted) out.omittedParams = omitted
  return out
}

/**
 * Fold away blank-named params that merely repeat a value already shown.
 *
 * `Internal Channel Volume Stereo` reports **33 params per audio clip**: `Bypass`, `Left`,
 * `Right`, and then thirty more with **no name at all**, every one carrying the same number —
 * Premiere exposing 32 channel slots on a clip that has two. On camping that single component
 * accounted for 4,455 of the timeline's 6,819 parameters: **65% of every param in the dump was
 * that padding.**
 *
 * Only genuinely redundant entries go: the name must be empty (a single-space name like Motion's
 * Uniform Scale is a real param and is kept) *and* the value must already appear on a named param
 * of the same component. The count of what was folded is reported, and the complete list is in
 * the state file on disk, so nothing is actually lost — a caller can still write to those indices.
 */
export function foldNoiseParams<P extends { index: number; name: string; value?: unknown }>(
  params: P[]
): { params: P[]; omitted: number } {
  const namedValues = new Set(params.filter((p) => p.name !== '').map((p) => stableKey(p.value)))
  const kept = params.filter((p) => p.name !== '' || !namedValues.has(stableKey(p.value)))
  return { params: kept, omitted: params.length - kept.length }
}

function stableKey(value: unknown): string {
  try {
    return JSON.stringify(value) ?? 'undefined'
  } catch {
    return String(value)
  }
}

function spanOf(items: { start: number; end: number }[]): [number, number] | null {
  if (!items.length) return null
  let lo = Infinity
  let hi = -Infinity
  for (const i of items) {
    if (i.start < lo) lo = i.start
    if (i.end > hi) hi = i.end
  }
  return [lo, hi]
}

function overlaps(aStart: number, aEnd: number, bStart: number, bEnd: number): boolean {
  return aStart < bEnd && aEnd > bStart
}

function totalsOf(state: SequenceState): SequenceView['totals'] {
  let components = 0
  let params = 0
  for (const track of [...state.videoTracks, ...state.audioTracks]) {
    for (const item of track.items as AnyClip[]) {
      for (const c of item.components) {
        components++
        params += c.params.length
      }
    }
  }
  return {
    videoClips: state.videoTracks.reduce((n, t) => n + t.items.length, 0),
    audioClips: state.audioTracks.reduce((n, t) => n + t.items.length, 0),
    components,
    params,
  }
}

/**
 * `'v2'`, `'V3'`, `'a0'`, `'A1'` all name a track; a clip ref like `'v2:3'` names its track too.
 *
 * The two numbering systems are the trap: Premiere's UI counts tracks from 1 (`V1`) and its API
 * counts from 0 (`v0`). Both are accepted, distinguished by case — an uppercase `V3` is the UI
 * label and means API index 2, a lowercase `v3` is the API index. That mirrors how the rest of
 * the bridge prints them, so whichever a caller copies from a previous result works.
 */
function resolveTrackSelection(state: SequenceState, selection: Selection): Set<string> | null {
  const names = [...(selection.tracks ?? []), ...(selection.clips ?? []).map((r) => r.split(':')[0] ?? '')]
  if (!names.length) return null

  const out = new Set<string>()
  for (const raw of names) {
    const name = raw.trim()
    if (!name) continue
    const kind = name[0]?.toLowerCase() === 'a' ? 'a' : 'v'
    const digits = Number(name.slice(1).split(':')[0])
    if (!Number.isFinite(digits)) continue
    // Uppercase is the UI label (1-based); lowercase is the API index (0-based).
    const isUiLabel = name[0] === name[0]?.toUpperCase()
    const index = isUiLabel ? digits - 1 : digits
    const tracks = kind === 'v' ? state.videoTracks : state.audioTracks
    if (tracks.some((t) => t.index === index)) out.add(`${kind}${index}`)
  }
  return out.size ? out : null
}

// ---- what changed ------------------------------------------------------------------------------

/**
 * Compare two states and report the clips that differ.
 *
 * This is the signal an edit actually produces. `insert_clip` cannot tell you the ref of the clip
 * it made — the panel returns a whole timeline, not a receipt — but a diff against the state
 * before the call finds it exactly, and the same machinery covers moves, trims and removals for
 * free.
 *
 * Clips are matched by `ref`, which is positional, so a ripple that shifts every later clip on a
 * track reports them all as modified. That is the truth of what happened and is worth seeing;
 * `more` caps how much of it gets spelled out.
 */
export function diffStates(before: SequenceState | null, after: SequenceState): ChangeReport | undefined {
  if (!before) return undefined
  if (before.sequence.guid && after.sequence.guid && before.sequence.guid !== after.sequence.guid) return undefined

  const was = indexClips(before)
  const now = indexClips(after)

  const added: ClipSummary[] = []
  const removed: ChangeReport['removed'] = []
  const modified: ChangeReport['modified'] = []

  for (const [ref, clip] of now) {
    const prev = was.get(ref)
    if (!prev) {
      added.push(clipSummary(clip, false))
      continue
    }
    if (!sameDelta(prev, clip) || prev.name !== clip.name) {
      modified.push({ ref, name: clip.name, was: deltaOf(prev), now: deltaOf(clip) })
    }
  }
  for (const [ref, clip] of was) {
    if (!now.has(ref)) removed.push({ ref, name: clip.name, start: clip.start })
  }

  if (!added.length && !removed.length && !modified.length) return { added: [], removed: [], modified: [] }

  const report: ChangeReport = {
    added: added.slice(0, MAX_CHANGED_DETAIL),
    removed: removed.slice(0, MAX_CHANGED_DETAIL),
    modified: modified.slice(0, MAX_CHANGED_DETAIL),
  }
  if (added.length + removed.length + modified.length > MAX_CHANGED_DETAIL) {
    report.more = { added: added.length, removed: removed.length, modified: modified.length }
  }
  return report
}

function indexClips(state: SequenceState): Map<string, AnyClip> {
  const map = new Map<string, AnyClip>()
  for (const track of [...state.videoTracks, ...state.audioTracks]) {
    for (const item of track.items as AnyClip[]) map.set(item.ref, item)
  }
  return map
}

/** Half a frame at 240fps — far below any real edit, comfortably above float noise. */
const TIME_EPSILON = 1e-4

function sameDelta(a: AnyClip, b: AnyClip): boolean {
  return (
    Math.abs(a.start - b.start) < TIME_EPSILON &&
    Math.abs(a.end - b.end) < TIME_EPSILON &&
    Math.abs(a.inPoint - b.inPoint) < TIME_EPSILON &&
    Math.abs(a.outPoint - b.outPoint) < TIME_EPSILON
  )
}

function deltaOf(clip: AnyClip): ClipDelta {
  return { start: clip.start, end: clip.end, inPoint: clip.inPoint, outPoint: clip.outPoint }
}

// ---- the budget ladder -------------------------------------------------------------------------

/**
 * Shrink a view until it fits, and say what was given up.
 *
 * The ladder is ordered by how much a session is likely to miss each rung — parameters first,
 * because they are voluminous and rarely the point; the clip list last, because it is usually
 * why the caller narrowed the selection in the first place. The digest at the bottom always
 * fits: it is bounded by the track count, not the clip count.
 *
 * **This function never fails and never throws away access to anything** — every rung adds a note
 * naming `statePath` and the narrower call that would have kept the detail.
 */
export function fitToBudget(view: SequenceView, budget = DEFAULT_BUDGET): SequenceView {
  if (measure(view) <= budget) return view

  const notes: string[] = [...(view.notes ?? [])]
  let current = view

  // Rung 1: drop parameter values, keep the effect chain.
  current = mapClips(current, (clip) => {
    if (!clip.components) return clip
    return {
      ...clip,
      components: clip.components.map((c) => ({
        index: c.index,
        matchName: c.matchName,
        displayName: c.displayName,
        paramCount: c.params?.length ?? c.paramCount ?? 0,
      })),
    }
  })
  if (measure({ ...current, notes }) <= budget) {
    notes.push(note('effect parameter values', view.statePath, 'narrow with `clips` or `range`'))
    return { ...current, notes }
  }

  // Rung 2: drop the effect chains entirely, keep the clips.
  current = mapClips(current, (clip) => {
    const componentCount = clip.components?.length ?? clip.componentCount
    const { components: _dropped, ...rest } = clip
    return componentCount ? { ...rest, componentCount } : rest
  })
  if (measure({ ...current, notes }) <= budget) {
    notes.push(note('effect chains', view.statePath, 'narrow with `clips` or `range`'))
    return { ...current, notes }
  }

  // Rung 3: drop the marker list, keep the count.
  if (current.markers.items) {
    current = { ...current, markers: { count: current.markers.count } }
    if (measure({ ...current, notes }) <= budget) {
      notes.push(note('the marker list', view.statePath, 'read them from the state file'))
      return { ...current, notes }
    }
  }

  // Rung 4: drop the `changed` detail, keep the counts.
  if (current.changed && (current.changed.added.length || current.changed.modified.length)) {
    const c = current.changed
    current = {
      ...current,
      changed: {
        added: [],
        removed: c.removed,
        modified: [],
        more: c.more ?? { added: c.added.length, removed: c.removed.length, modified: c.modified.length },
      },
    }
    if (measure({ ...current, notes }) <= budget) {
      notes.push(note('the detail of what changed', view.statePath, 'compare against the previous state file'))
      return { ...current, notes }
    }
  }

  // Rung 5: the digest. Bounded by track count, so this always fits.
  current = stripClips(current)
  notes.push(
    note(
      'every clip list',
      view.statePath,
      'ask for one track at a time (`tracks: ["v2"]`) or a time window (`range`)'
    )
  )
  return { ...current, notes }
}

function note(what: string, statePath: string | undefined, how: string): string {
  const where = statePath ? ` The complete state is at ${statePath} — jq it.` : ''
  return `This result was too large, so ${what} could not be included.${where} To get it here instead, ${how}.`
}

function measure(view: SequenceView): number {
  try {
    return JSON.stringify(view)?.length ?? 0
  } catch {
    return Infinity
  }
}

function mapClips(view: SequenceView, fn: (clip: ClipSummary) => ClipSummary): SequenceView {
  const onTrack = (t: TrackView): TrackView => (t.clips ? { ...t, clips: t.clips.map(fn) } : t)
  return {
    ...view,
    videoTracks: view.videoTracks.map(onTrack),
    audioTracks: view.audioTracks.map(onTrack),
    ...(view.changed ? { changed: { ...view.changed, added: view.changed.added.map(fn) } } : {}),
  }
}

function stripClips(view: SequenceView): SequenceView {
  const onTrack = (t: TrackView): TrackView => {
    const { clips: _dropped, ...rest } = t
    return rest
  }
  return {
    ...view,
    videoTracks: view.videoTracks.map(onTrack),
    audioTracks: view.audioTracks.map(onTrack),
  }
}
