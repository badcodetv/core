/**
 * The panel's thin layer over Premiere's UXP API: one place that knows how to reach `ppro`,
 * how to wrap a mutation in a single undoable transaction, how to turn a `v0:2` ref into a real
 * track item, and how to dump a sequence into the raw shape `src/normalise.ts` consumes.
 *
 * Nothing in `panel/src/commands/` should touch `require()` or `TickTime` directly — it all
 * comes through here, so the awkward parts of the API are wrong in at most one place.
 */
import type Premierepro from 'premierepro'
import type {
  Action,
  AudioClipTrackItem,
  AudioComponentChain,
  Component,
  CompoundAction,
  Project,
  Sequence,
  TickTime,
  TrackItemSelection,
  VideoClipTrackItem,
  VideoComponentChain,
} from 'premierepro'
import type {
  ErrorCode,
  RawComponentDump,
  RawParamDump,
  RawSequenceDump,
  RawTrackDump,
  RawTrackItemDump,
  RawTransitionDump,
} from '../../src/protocol'

/* ---- reaching the UXP runtime ------------------------------------------------------------- */

declare const require: ((id: string) => unknown) | undefined

/**
 * UXP supplies `require` to a panel's scripts, but whether it lands as a true global or as a
 * scope-local of the script wrapper differs between hosts — so try both rather than assume.
 * Written as a bare identifier reference, never a `require(...)` call expression, so esbuild
 * leaves it alone instead of trying to bundle the module.
 */
export function uxpRequire<T>(id: string): T {
  const fn =
    typeof require === 'function'
      ? require
      : ((globalThis as Record<string, unknown>).require as ((id: string) => unknown) | undefined)
  if (!fn) throw new PanelError('PANEL_ERROR', `UXP require() is unavailable — cannot load "${id}".`)
  return fn(id) as T
}

export const ppro: Premierepro = uxpRequire<Premierepro>('premierepro')

/**
 * The host version. **Not** `ppro.Application.version` — that returns `null` at runtime even
 * though the type declarations promise a string (found live in the T1 spike, 2026-08-21).
 */
export function appVersion(): string {
  try {
    const uxp = uxpRequire<{ host?: { version?: string } }>('uxp')
    return uxp.host?.version ?? 'unknown'
  } catch {
    return 'unknown'
  }
}

/* ---- errors -------------------------------------------------------------------------------- */

export class PanelError extends Error {
  constructor(public code: ErrorCode, message: string, public detail?: unknown) {
    super(message)
    this.name = 'PanelError'
  }
}

/* ---- time ---------------------------------------------------------------------------------- */

export const secondsToTick = (s: number): TickTime => ppro.TickTime.createWithSeconds(s)
export const tickToSeconds = (t: TickTime | null | undefined): number => (t ? t.seconds : 0)

/* ---- transactions -------------------------------------------------------------------------- */

/**
 * Every mutation is one transaction, labelled so it reads as a single `BadCode: …` entry in
 * Edit ▸ Undo (Decision 3 in the plan). `executeTransaction` is synchronous, so `build` must be
 * too — resolve every promise you need BEFORE calling this.
 */
export function withTransaction(project: Project, label: string, build: (ca: CompoundAction) => void): void {
  let committed = false
  project.lockedAccess(() => {
    committed = project.executeTransaction(build, `BadCode: ${label}`)
  })
  if (!committed) throw new PanelError('TRANSACTION_FAILED', `Transaction "${label}" was not committed.`)
}

/**
 * The workhorse the command modules use: build N Actions, commit them as one labelled
 * transaction.
 *
 * The builders are **thunks** rather than ready-made Actions because `executeTransaction` is
 * synchronous and Premiere wants its Actions constructed inside the callback. Resolve every
 * promise you need BEFORE calling this; construct Actions inside.
 */
export function withActions(project: Project, label: string, builders: (() => Action)[]): void {
  let committed = false
  project.lockedAccess(() => {
    committed = project.executeTransaction((ca) => {
      for (const build of builders) ca.addAction(build())
    }, `BadCode: ${label}`)
  })
  if (!committed) throw new PanelError('TRANSACTION_FAILED', `Premiere rejected the edit: ${label}`)
}

/** One Action, one transaction. */
export function withAction(project: Project, label: string, build: () => Action): void {
  withActions(project, label, [build])
}

/* ---- argument reading ------------------------------------------------------------------------ */

/** Commands receive `Record<string, unknown>` off the wire — the server validated it against
 * zod, but the panel cannot see that schema, so it re-reads defensively rather than casting. */
export function numArg(v: unknown, name: string): number {
  if (typeof v !== 'number' || !Number.isFinite(v)) {
    throw new PanelError('INVALID_ARGS', `${name} must be a number (seconds).`)
  }
  return v
}

export function intArg(v: unknown, fallback: number): number {
  return typeof v === 'number' && Number.isFinite(v) ? Math.trunc(v) : fallback
}

export function strArg(v: unknown, name: string): string {
  if (typeof v !== 'string' || !v) throw new PanelError('INVALID_ARGS', `${name} must be a non-empty string.`)
  return v
}

/* ---- path comparison ------------------------------------------------------------------------ */

/**
 * Are these the same Windows path? Premiere reports paths in **extended-length** form
 * (`\\?\D:\…`) while callers pass the ordinary form, so a raw `===` never matches.
 * Case-insensitive and separator-normalised, as Windows is.
 */
export function samePath(a: string | null | undefined, b: string | null | undefined): boolean {
  if (!a || !b) return false
  const norm = (p: string): string =>
    p
      .replace(/^\\\\\?\\UNC\\/i, '\\\\')
      .replace(/^\\\\\?\\/, '')
      .replace(/\//g, '\\')
      .replace(/\\+$/, '')
      .toLowerCase()
  return norm(a) === norm(b)
}

/* ---- resolving things ---------------------------------------------------------------------- */

export async function activeProject(): Promise<Project> {
  const project = await ppro.Project.getActiveProject()
  if (!project) throw new PanelError('NO_PROJECT', 'No project is open in Premiere.')
  return project
}

export async function activeSequence(project: Project, name?: string): Promise<Sequence> {
  if (name) {
    const all = await project.getSequences()
    const found = all.find((s) => s.name === name)
    if (!found) {
      const names = all.map((s) => s.name).join(', ') || '(none)'
      throw new PanelError('NO_SEQUENCE', `No sequence named "${name}". Open sequences: ${names}`)
    }
    return found
  }
  const seq = await project.getActiveSequence()
  if (!seq) throw new PanelError('NO_SEQUENCE', 'No sequence is active in Premiere.')
  return seq
}

const CLIP_REF = /^([va])(\d+):(\d+)$/

/** `v0:2` → third CLIP item on video track 0. Refs come from the most recent `SequenceState`
 * and go stale the moment the timeline changes — that is why every mutating tool returns a
 * fresh state. */
export async function resolveClip(
  seq: Sequence,
  ref: string
): Promise<VideoClipTrackItem | AudioClipTrackItem> {
  const m = CLIP_REF.exec(ref)
  if (!m) throw new PanelError('INVALID_ARGS', `"${ref}" is not a clip ref (expected e.g. "v0:2").`)
  const [, kind, trackStr, itemStr] = m
  const trackIndex = Number(trackStr)
  const itemIndex = Number(itemStr)

  const track =
    kind === 'v' ? await seq.getVideoTrack(trackIndex) : await seq.getAudioTrack(trackIndex)
  if (!track) throw new PanelError('CLIP_NOT_FOUND', `No ${kind === 'v' ? 'video' : 'audio'} track ${trackIndex}.`)

  const items = track.getTrackItems(ppro.Constants.TrackItemType.CLIP, false)
  const item = items[itemIndex]
  if (!item) {
    throw new PanelError(
      'CLIP_NOT_FOUND',
      `No clip at ${ref} — that track has ${items.length} clip${items.length === 1 ? '' : 's'}. ` +
        'Re-read the sequence: refs go stale after any edit.'
    )
  }
  return item
}

export async function resolveProjectItem(project: Project, nameOrId: string): Promise<import('premierepro').ProjectItem> {
  const root = await project.getRootItem()
  const found = await findItem(root, nameOrId)
  if (!found) throw new PanelError('ITEM_NOT_FOUND', `No project item named or with id "${nameOrId}".`)
  return found
}

async function findItem(
  folder: import('premierepro').FolderItem,
  nameOrId: string
): Promise<import('premierepro').ProjectItem | null> {
  const items = await folder.getItems()
  for (const item of items) {
    if (item.name === nameOrId || safeId(item) === nameOrId) return item
  }
  // Depth-second: an exact match higher in the tree wins over a nested one.
  for (const item of items) {
    if (item.type !== ppro.ProjectItem.TYPE_BIN) continue
    const nested = await findItem(ppro.FolderItem.cast(item), nameOrId)
    if (nested) return nested
  }
  return null
}

function safeId(item: import('premierepro').ProjectItem): string | null {
  try {
    return item.getId()
  } catch {
    return null
  }
}

/** A component by 0-based index, or by matchName / displayName (case-insensitive). */
export async function resolveComponent(
  chain: VideoComponentChain | AudioComponentChain,
  key: string | number
): Promise<Component> {
  const count = chain.getComponentCount()
  if (typeof key === 'number') {
    if (key < 0 || key >= count) {
      throw new PanelError('PARAM_NOT_FOUND', `No component at index ${key} — the chain has ${count}.`)
    }
    return chain.getComponentAtIndex(key)
  }

  const wanted = key.toLowerCase()
  const seen: string[] = []
  for (let i = 0; i < count; i += 1) {
    const component = chain.getComponentAtIndex(i)
    const [matchName, displayName] = await Promise.all([
      component.getMatchName(),
      component.getDisplayName(),
    ])
    seen.push(displayName)
    if (matchName.toLowerCase() === wanted || displayName.toLowerCase() === wanted) return component
  }
  throw new PanelError('PARAM_NOT_FOUND', `No component "${key}" on this clip. Present: ${seen.join(', ') || '(none)'}`)
}

/* ---- selections ------------------------------------------------------------------------------ */

/**
 * A `TrackItemSelection` holding exactly the given items.
 *
 * 🔴 **NOT via `TrackItemSelection.createEmptySelection()`.** That hands back an object with all
 * the right methods on it, and every native call against it throws *"The script object is no
 * longer valid."* — including synchronously inside its own callback. It is unusable (measured
 * live 2026-08-21).
 *
 * The route that works is the sequence's own selection: clear it, take it, fill it. The visible
 * side effect is that the user's timeline selection is replaced, which is a fair trade for being
 * able to remove a clip at all.
 */
export async function selectionFor(
  sequence: Sequence,
  items: (VideoClipTrackItem | AudioClipTrackItem)[]
): Promise<TrackItemSelection> {
  await sequence.clearSelection()
  const selection = await sequence.getSelection()
  if (!selection) throw new PanelError('PANEL_ERROR', 'Premiere would not hand over the sequence selection.')
  for (const item of items) selection.addItem(item, true)
  return selection
}

/* ---- value serialisation -------------------------------------------------------------------- */

/**
 * Component param values come back as numbers, strings, booleans, or ppro `PointF` / `Color`
 * objects whose fields are native getters — `JSON.stringify` on those yields `{}`, so unwrap
 * them into the plain shapes `protocol.ts` describes.
 */
export function plainValue(v: unknown): unknown {
  if (v === null || v === undefined) return null
  const t = typeof v
  if (t === 'number' || t === 'string' || t === 'boolean') return v
  if (Array.isArray(v)) return v.map(plainValue)

  if (t === 'object') {
    const o = v as Record<string, unknown>

    // 🔴 `ComponentParam.getValueAtTime()` does NOT return the value its type declaration
    // promises (`number | string | boolean | PointF | Color`). It returns a plain wrapper object
    // with a single `value` key — `{ value: 100 }`, `{ value: [0.5, 0.5] }` — so every parameter
    // read has to be unwrapped or the whole timeline comes back full of `{"value":…}` noise.
    // Found live 2026-08-21 reading Motion's params.
    const keys = Object.getOwnPropertyNames(o)
    if (keys.length === 1 && keys[0] === 'value') return plainValue(o.value)

    if (typeof o.red === 'number') return { r: o.red, g: o.green, b: o.blue, a: o.alpha }
    if (typeof o.x === 'number' && typeof o.y === 'number') return { x: o.x, y: o.y }
    if (typeof o.width === 'number' && typeof o.height === 'number') return { w: o.width, h: o.height }
  }

  try {
    return JSON.parse(JSON.stringify(v))
  } catch {
    return String(v)
  }
}


/* ---- writing param values -------------------------------------------------------------------- */

/**
 * Turn a plain wire value into what `ComponentParam.createKeyframe` wants. `protocol.ts`
 * validates the shape but cannot build these — it has no `ppro` to import.
 *
 * Point values are **normalised 0–1 fractions of the frame**, not pixels: `{x: 0.5, y: 0.5}` is
 * dead centre (measured on Motion's Position and Anchor Point, T7).
 */
export function toPproValue(v: unknown): number | string | boolean | import('premierepro').PointF | import('premierepro').Color {
  if (typeof v === 'number' || typeof v === 'string' || typeof v === 'boolean') return v
  if (v && typeof v === 'object') {
    const o = v as Record<string, unknown>
    if (typeof o.x === 'number' && typeof o.y === 'number') return new ppro.PointF(o.x, o.y)
    if (typeof o.r === 'number' && typeof o.g === 'number' && typeof o.b === 'number') {
      return new ppro.Color(o.r, o.g, o.b, typeof o.a === 'number' ? o.a : 1)
    }
    // A two-number array is how a point reads BACK, so accept it going in as well.
    if (Array.isArray(v) && v.length === 2 && v.every((n) => typeof n === 'number')) {
      return new ppro.PointF(v[0] as number, v[1] as number)
    }
  }
  throw new PanelError(
    'INVALID_ARGS',
    `Cannot use ${JSON.stringify(v)} as a param value. Allowed: number, string, boolean, ` +
      '{x,y} (0–1 fractions of the frame), or {r,g,b,a?}.'
  )
}

/**
 * A param by 0-based index, or by display name (case-insensitive, first match).
 *
 * 🔴 **The index is the authoritative address.** Display names are neither unique nor always
 * present: `AE.ADBE Opacity` has two params called "Blend Mode", `AE.ADBE Motion` param 3 is
 * named `" "`, and Lumetri Color has several blank names and repeats "Saturation", "Intensity",
 * "Look" and "Input LUT". Name lookup is a convenience for the obvious cases and nothing more —
 * always report indices so a caller can be exact.
 */
export function resolveParam(component: Component, key: string | number): { param: import('premierepro').ComponentParam; index: number } {
  const count = component.getParamCount()
  if (typeof key === 'number') {
    if (!Number.isInteger(key) || key < 0 || key >= count) {
      throw new PanelError('PARAM_NOT_FOUND', `No param at index ${key} — this component has ${count} (0–${count - 1}).`)
    }
    return { param: component.getParam(key), index: key }
  }

  const wanted = key.trim().toLowerCase()
  const names: string[] = []
  const matches: number[] = []
  for (let i = 0; i < count; i += 1) {
    const name = component.getParam(i).displayName
    names.push(`${i} "${name}"`)
    if (name.trim().toLowerCase() === wanted) matches.push(i)
  }
  if (matches.length === 0) {
    throw new PanelError('PARAM_NOT_FOUND', `No param named "${key}". This component has: ${names.join(', ')}`)
  }
  if (matches.length > 1) {
    throw new PanelError(
      'PARAM_NOT_FOUND',
      `"${key}" is ambiguous — indices ${matches.join(', ')} all carry that name. Address it by index.`
    )
  }
  return { param: component.getParam(matches[0]), index: matches[0] }
}

/** `'linear' | 'bezier' | 'hold'` → Premiere's InterpolationMode. */
export function interpolationMode(name: string): number {
  const modes: Record<string, number> = {
    linear: ppro.Constants.InterpolationMode.LINEAR,
    bezier: ppro.Constants.InterpolationMode.BEZIER,
    hold: ppro.Constants.InterpolationMode.HOLD,
  }
  const mode = modes[name.toLowerCase()]
  if (mode === undefined) throw new PanelError('INVALID_ARGS', `Unknown interpolation "${name}" — use linear, bezier or hold.`)
  return mode
}

/* ---- dumping the sequence ---------------------------------------------------------------------- */

export interface DumpOptions {
  /** Read every component param of every clip. Costly on Lumetri-heavy sequences; the only
   * reason to turn it off is a measured stall. */
  params?: boolean
}

export async function dumpSequence(
  project: Project,
  seq: Sequence,
  opts: DumpOptions = {}
): Promise<RawSequenceDump> {
  const withParams = opts.params !== false

  const [videoCount, audioCount, frameSize, timebase, end, playhead] = await Promise.all([
    seq.getVideoTrackCount(),
    seq.getAudioTrackCount(),
    seq.getFrameSize(),
    seq.getTimebase(),
    seq.getEndTime(),
    seq.getPlayerPosition(),
  ])

  const videoTracks: RawTrackDump[] = []
  for (let i = 0; i < videoCount; i += 1) {
    videoTracks.push(await dumpTrack(await seq.getVideoTrack(i), i, withParams))
  }
  const audioTracks: RawTrackDump[] = []
  for (let i = 0; i < audioCount; i += 1) {
    audioTracks.push(await dumpTrack(await seq.getAudioTrack(i), i, withParams))
  }

  return {
    project: { name: project.name, path: project.path },
    sequence: {
      name: seq.name,
      guid: String(seq.guid),
      timebase: String(timebase),
      frameSize: { w: frameSize?.width ?? 0, h: frameSize?.height ?? 0 },
      end: tickToSeconds(end),
      playhead: tickToSeconds(playhead),
    },
    videoTracks,
    audioTracks,
    markers: await dumpMarkers(seq),
  }
}

type AnyTrack = import('premierepro').VideoTrack | import('premierepro').AudioTrack

/**
 * 🔴 `getTrackItems()` yields `null` for every item that is not a CLIP.
 *
 * Measured live 2026-08-21: on a track carrying two clips and two real transitions,
 * `getTrackItems(TRANSITION, false)` returned `[null, null]`. The **length is exact and
 * meaningful** — it went 0 → 1 → 2 as transitions were added — but not one element could be
 * marshalled into JS. The same is true of EMPTY items when `includeEmpty` is set.
 *
 * So: count them, never read them, and filter the nulls out of the clip list too rather than
 * trusting that CLIP is always safe.
 */
function liveItems<T>(items: (T | null | undefined)[]): T[] {
  return items.filter((x): x is T => Boolean(x))
}

export function countTransitions(track: AnyTrack): number {
  return track.getTrackItems(ppro.Constants.TrackItemType.TRANSITION, false).length
}

async function dumpTrack(track: AnyTrack, index: number, withParams: boolean): Promise<RawTrackDump> {
  const clips = liveItems(track.getTrackItems(ppro.Constants.TrackItemType.CLIP, false))
  const items: RawTrackItemDump[] = []
  for (let i = 0; i < clips.length; i += 1) {
    items.push(await dumpTrackItem(clips[i], i, withParams))
  }

  // Always empty, and deliberately kept: the day Premiere marshals a transition track item,
  // this fills itself in and `normalise.ts` attaches them to their clips with no other change.
  const transitions: RawTransitionDump[] = []

  return {
    index,
    name: track.name,
    muted: await track.isMuted(),
    items,
    transitions,
    transitionCount: countTransitions(track),
  }
}

async function dumpTrackItem(
  item: VideoClipTrackItem | AudioClipTrackItem,
  index: number,
  withParams: boolean
): Promise<RawTrackItemDump> {
  const [name, start, end, duration, inPoint, outPoint, disabled, speed] = await Promise.all([
    item.getName(),
    item.getStartTime(),
    item.getEndTime(),
    item.getDuration(),
    item.getInPoint(),
    item.getOutPoint(),
    item.isDisabled(),
    item.getSpeed(),
  ])

  return {
    index,
    name,
    start: tickToSeconds(start),
    end: tickToSeconds(end),
    duration: tickToSeconds(duration),
    inPoint: tickToSeconds(inPoint),
    outPoint: tickToSeconds(outPoint),
    mediaPath: await mediaPathOf(item),
    disabled,
    speed,
    components: withParams ? await dumpComponents(item) : [],
  }
}

async function mediaPathOf(item: VideoClipTrackItem | AudioClipTrackItem): Promise<string | null> {
  try {
    const projectItem = await item.getProjectItem()
    if (!projectItem) return null
    return (await ppro.ClipProjectItem.cast(projectItem).getMediaFilePath()) || null
  } catch {
    // Synthetic items (titles, colour mattes, adjustment layers) have no media file.
    return null
  }
}

async function dumpComponents(item: VideoClipTrackItem | AudioClipTrackItem): Promise<RawComponentDump[]> {
  let chain: VideoComponentChain | AudioComponentChain
  try {
    chain = await item.getComponentChain()
  } catch {
    return []
  }
  if (!chain) return []

  const out: RawComponentDump[] = []
  const count = chain.getComponentCount()
  for (let i = 0; i < count; i += 1) {
    const component = chain.getComponentAtIndex(i)
    const [matchName, displayName] = await Promise.all([component.getMatchName(), component.getDisplayName()])
    out.push({ index: i, matchName, displayName, params: await dumpParams(component) })
  }
  return out
}

async function dumpParams(component: Component): Promise<RawParamDump[]> {
  const out: RawParamDump[] = []
  const count = component.getParamCount()
  for (let i = 0; i < count; i += 1) {
    try {
      out.push(await dumpParam(component, i))
    } catch (err) {
      // A param that refuses even to identify itself must not take the whole dump down.
      out.push({ index: i, name: `(unreadable #${i})`, value: null, timeVarying: false, unreadable: true })
    }
  }
  return out
}

/**
 * 🔴 **Some params have no readable value by any route.** 33 of Lumetri Color's 130 throw
 * *"getValueAtTime is not supported for these value types. Use GetKeyframeAtTime…"* — and the
 * `getKeyframePtr` that message recommends returns `null` or throws *"Illegal Parameter type"*,
 * and `getStartValue()` returns `null` too. Measured live 2026-08-21. They are the structural
 * ones: colour wheels, curves, group headers.
 *
 * The **display name still reads fine**, so keep it and flag the value rather than throwing the
 * name away with it — `unreadable: true`, `value: null`. A caller can still address the param by
 * index and write to it; only reading is lost.
 */
async function readValue(param: import('premierepro').ComponentParam): Promise<{ value: unknown; unreadable: boolean }> {
  try {
    return { value: plainValue(await param.getValueAtTime(ppro.TickTime.TIME_ZERO)), unreadable: false }
  } catch {
    // The documented fallback, tried anyway in case a future Premiere honours it.
    try {
      const kf = param.getKeyframePtr(ppro.TickTime.TIME_ZERO)
      if (kf) return { value: plainValue(kf.value), unreadable: false }
    } catch {
      /* "Illegal Parameter type" — expected; fall through */
    }
    return { value: null, unreadable: true }
  }
}

async function dumpParam(component: Component, index: number): Promise<RawParamDump> {
  const param = component.getParam(index)
  const timeVarying = param.isTimeVarying()
  const read = await readValue(param)
  const dump: RawParamDump = {
    index,
    name: param.displayName,
    value: read.value,
    timeVarying,
    ...(read.unreadable ? { unreadable: true } : {}),
  }

  if (timeVarying) {
    const times = param.getKeyframeListAsTickTimes() ?? []
    const keyframes: { t: number; value: unknown }[] = []
    for (const t of times) {
      let value: unknown = null
      try {
        value = plainValue(await param.getValueAtTime(t))
      } catch {
        /* same unreadable-value families as above */
      }
      keyframes.push({ t: tickToSeconds(t), value })
    }
    dump.keyframes = keyframes
  }
  return dump
}

async function dumpMarkers(seq: Sequence): Promise<RawSequenceDump['markers']> {
  try {
    const markers = await ppro.Markers.getMarkers(seq)
    return markers.getMarkers().map((m) => ({
      name: m.getName(),
      start: tickToSeconds(m.getStart()),
      duration: tickToSeconds(m.getDuration()),
      comments: m.getComments(),
    }))
  } catch {
    return []
  }
}
