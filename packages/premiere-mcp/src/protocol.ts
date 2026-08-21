/**
 * The wire protocol between `bridge.ts` (WSL) and the UXP panel (Windows) — zod schemas plus
 * their inferred TS types, shared by both sides. Times at the tool boundary are seconds
 * (number); the panel converts with `ppro.TickTime`. Track indices are the API's 0-based
 * indices. `clip` refs are `v<track>:<item>` / `a<track>:<item>` (Decision 4 in the plan).
 */
import { z } from 'zod'

// ---- Error codes ----------------------------------------------------------------------------

export const ErrorCodeSchema = z.enum([
  'NO_MEDIA_ROOT', 'PANEL_NOT_CONNECTED', 'TIMEOUT', 'NO_PROJECT', 'NO_SEQUENCE',
  'ITEM_NOT_FOUND', 'CLIP_NOT_FOUND', 'EFFECT_NOT_FOUND', 'TRANSITION_NOT_FOUND',
  'PARAM_NOT_FOUND', 'TRANSACTION_FAILED', 'IMPORT_FAILED', 'EXPORT_FAILED',
  'INVALID_ARGS', 'EVAL_ERROR', 'PANEL_ERROR', 'BAD_CONFIG',
])
export type ErrorCode = z.infer<typeof ErrorCodeSchema>

// ---- Command names ------------------------------------------------------------------------

/** Every `premiere_*` tool name with the prefix dropped, plus `ping` (panel-only liveness
 * check — there is no `premiere_ping` tool). */
export const CMD_NAMES = [
  'status', 'open_project', 'save', 'import', 'list_items',
  'create_sequence', 'list_sequences', 'set_active', 'get_sequence',
  'insert_clip', 'move_clip', 'trim_clip', 'remove_clip', 'clone_clip',
  'list_transitions', 'add_transition', 'remove_transition',
  'list_effects', 'describe_effect', 'apply_effect', 'set_param', 'remove_effect',
  'insert_mogrt',
  'add_marker', 'set_playhead',
  'export_frame', 'export_sequence',
  'eval',
  'ping',
] as const
export const CmdNameSchema = z.enum(CMD_NAMES)
export type CmdName = (typeof CMD_NAMES)[number]

// ---- Envelope ---------------------------------------------------------------------------------

export const HelloSchema = z.object({
  type: z.literal('hello'),
  appVersion: z.string(),
  panelVersion: z.string(),
  protocol: z.literal(1),
})
export type Hello = z.infer<typeof HelloSchema>

export const CmdSchema = z.object({
  type: z.literal('cmd'),
  id: z.string(),
  cmd: CmdNameSchema,
  args: z.unknown(),
})
export type Cmd = z.infer<typeof CmdSchema>

const ResultOkSchema = z.object({ type: z.literal('result'), id: z.string(), ok: z.literal(true), result: z.unknown() })
const ResultErrSchema = z.object({
  type: z.literal('result'),
  id: z.string(),
  ok: z.literal(false),
  code: ErrorCodeSchema,
  message: z.string(),
  detail: z.unknown().optional(),
})
export const ResultSchema = z.union([ResultOkSchema, ResultErrSchema])
export type Result = z.infer<typeof ResultSchema>

export const LogSchema = z.object({
  type: z.literal('log'),
  level: z.enum(['info', 'warn', 'error']),
  message: z.string(),
})
export type Log = z.infer<typeof LogSchema>

/**
 * Frames the bridge can receive FROM the panel (never `cmd` — that direction is server -> panel
 * only). A plain `z.union`, not `discriminatedUnion`, because the `result` branch is itself a
 * union on `ok` and zod's discriminated union requires every member to be a bare object with
 * the discriminant key at the top level.
 */
export const IncomingFrameSchema = z.union([HelloSchema, ResultOkSchema, ResultErrSchema, LogSchema])
export type IncomingFrame = z.infer<typeof IncomingFrameSchema>

// ---- Value coercion (premiere_apply_effect / premiere_set_param) --------------------------

const PointFSchema = z.object({ x: z.number(), y: z.number() })
const ColorSchema = z.object({ r: z.number(), g: z.number(), b: z.number(), a: z.number().optional() })

/** A component param value as it crosses the wire — a plain {x,y} or {r,g,b,a?} object, never
 * a constructed ppro `PointF`/`Color`. The panel wraps the validated plain data into the real
 * ppro type; this module cannot (it has no `ppro` to import). */
export const ParamValueSchema = z.union([z.number(), z.string(), z.boolean(), PointFSchema, ColorSchema])
export type ParamValue = z.infer<typeof ParamValueSchema>

export function coerceParamValue(v: unknown): ParamValue {
  return ParamValueSchema.parse(v)
}

// ---- SequenceState ---------------------------------------------------------------------------

const ParamSchema = z.object({
  index: z.number(),
  name: z.string(),
  value: z.unknown(),
  timeVarying: z.boolean(),
  keyframes: z.array(z.object({ t: z.number(), value: z.unknown() })).optional(),
  /** True when Premiere refuses to hand over this param's value by any route — 33 of Lumetri
   * Color's 130 params behave this way. `value` is null; the param can still be WRITTEN. */
  unreadable: z.boolean().optional(),
})
export type Param = z.infer<typeof ParamSchema>

const ComponentSchema = z.object({
  index: z.number(),
  matchName: z.string(),
  displayName: z.string(),
  params: z.array(ParamSchema),
})
export type Component = z.infer<typeof ComponentSchema>

const TransitionInfoSchema = z.object({ matchName: z.string(), duration: z.number() })
export type TransitionInfo = z.infer<typeof TransitionInfoSchema>

const ClipBaseShape = {
  ref: z.string(), // 'v0:2' | 'a1:0'
  name: z.string(),
  start: z.number(),
  end: z.number(),
  duration: z.number(),
  inPoint: z.number(),
  outPoint: z.number(),
  mediaPath: z.string().nullable(), // WSL form; null for generated/synthetic items
  disabled: z.boolean(),
  speed: z.number(),
}

const VideoClipSchema = z.object({
  ...ClipBaseShape,
  components: z.array(ComponentSchema),
  transitions: z.object({ start: TransitionInfoSchema.optional(), end: TransitionInfoSchema.optional() }),
})
export type VideoClip = z.infer<typeof VideoClipSchema>

const AudioClipSchema = z.object({
  ...ClipBaseShape,
  components: z.array(ComponentSchema),
})
export type AudioClip = z.infer<typeof AudioClipSchema>

function trackSchema<C extends z.ZodTypeAny>(clip: C) {
  return z.object({
    index: z.number(),
    label: z.string(), // 'V1' | 'A1'
    name: z.string(),
    muted: z.boolean(),
    items: z.array(clip),
    // How many transitions sit on this track. A COUNT and nothing more: Premiere hands back a
    // null for every transition track item, so their match names and positions are unreadable
    // (see docs/premiere/api-notes.md, T9). The per-clip `transitions` field below is therefore
    // always empty today — it is kept because the shape is right the day Premiere fixes this.
    transitionCount: z.number(),
  })
}

export const SequenceStateSchema = z.object({
  project: z.object({ name: z.string(), path: z.string() }), // path: WSL form
  sequence: z.object({
    name: z.string(),
    guid: z.string(),
    timebase: z.string(), // ticks per frame, as Premiere reports it
    frameRate: z.number(), // frames per second, derived from timebase — 0 if it could not be worked out
    frameSize: z.object({ w: z.number(), h: z.number() }),
    end: z.number(),
    playhead: z.number(),
  }),
  videoTracks: z.array(trackSchema(VideoClipSchema)),
  audioTracks: z.array(trackSchema(AudioClipSchema)),
  markers: z.array(z.object({ name: z.string(), start: z.number(), duration: z.number(), comments: z.string() })),
})
export type SequenceState = z.infer<typeof SequenceStateSchema>

// ---- Per-command args / results ------------------------------------------------------------

const ClipRefSchema = z.string().regex(/^[va]\d+:\d+$/, 'expected a clip ref like "v0:2" or "a1:0"')
const ProjectRefSchema = z.object({ name: z.string(), path: z.string() })
const EmptyArgsSchema = z.object({})

/**
 * **These schemas describe the WIRE, not the tool boundary.** `Bridge.send()` is typed against
 * them, so they must match exactly what the panel receives and sends back. Where a tool's public
 * arguments differ from what the panel needs, `server.ts` declares its own `inputSchema` and
 * translates between the two. Two places that diverge today:
 *
 * - `open_project` — the tool takes `{ story }`; the panel has no idea what the media root is,
 *   so the wire carries the resolved **Windows** project path instead.
 * - `status` — never crosses the wire at all. `premiere_status` is composed server-side from a
 *   `ping` plus what only the server knows (is a panel connected, what is the media root). Its
 *   entry below is kept as the *tool result* shape, which is what `server.ts` types against.
 *
 * Paths on the wire are always **Windows** form in both directions; `server.ts` converts at the
 * boundary so the panel never sees a `/mnt/…` path and the session never sees a `D:\…` one.
 */

export const CmdArgsSchemas = {
  status: EmptyArgsSchema,
  // Windows path + an explicit create/open decision. The panel does NOT decide which: Premiere's
  // `Project.isProject()` answers "could a project live at this path", NOT "does one" — it returns
  // true for files that do not exist (found live 2026-08-21). Only the server can actually check
  // the filesystem, so it does, and the panel obeys.
  open_project: z.object({ path: z.string(), create: z.boolean() }),
  save: EmptyArgsSchema,
  import: z.object({ paths: z.array(z.string()), bin: z.string().optional() }),
  list_items: z.object({ bin: z.string().optional() }),
  create_sequence: z.object({ name: z.string(), preset: z.string().optional(), fromItems: z.array(z.string()).optional() }),
  list_sequences: EmptyArgsSchema,
  set_active: z.object({ name: z.string() }),
  get_sequence: z.object({ name: z.string().optional(), params: z.boolean().optional() }),
  insert_clip: z.object({
    item: z.string(),
    time: z.number(),
    videoTrack: z.number().default(0),
    audioTrack: z.number().default(0),
    mode: z.enum(['insert', 'overwrite']),
    limitShift: z.boolean().default(false),
  }),
  move_clip: z.object({ clip: ClipRefSchema, deltaSeconds: z.number() }),
  trim_clip: z.object({
    clip: ClipRefSchema,
    inPoint: z.number().optional(),
    outPoint: z.number().optional(),
    start: z.number().optional(),
    end: z.number().optional(),
  }),
  remove_clip: z.object({ clips: z.array(ClipRefSchema), ripple: z.boolean().default(false) }),
  clone_clip: z.object({
    clip: ClipRefSchema,
    deltaSeconds: z.number(),
    videoTrackOffset: z.number().default(0),
    audioTrackOffset: z.number().default(0),
    mode: z.enum(['insert', 'overwrite']).default('insert'),
  }),
  list_transitions: z.object({ query: z.string().optional() }),
  add_transition: z.object({
    clip: ClipRefSchema,
    matchName: z.string(),
    at: z.enum(['start', 'end']),
    duration: z.number().optional(),
    alignment: z.number().optional(),
  }),
  remove_transition: z.object({ clip: ClipRefSchema, at: z.enum(['start', 'end']) }),
  list_effects: z.object({ query: z.string().optional() }),
  // `clip` is REQUIRED, not optional as first planned: an un-inserted `VideoFilterComponent`
  // has no methods at all (its prototype is a bare `constructor`), so params can only ever be
  // read off an APPLIED instance. Ruled by live probe, T10 — see docs/premiere/api-notes.md.
  describe_effect: z.object({ clip: ClipRefSchema, component: z.union([z.string(), z.number()]) }),
  apply_effect: z.object({
    clip: ClipRefSchema,
    matchName: z.string(),
    params: z.record(ParamValueSchema).optional(),
    index: z.number().optional(),
  }),
  set_param: z.object({
    clip: ClipRefSchema,
    component: z.union([z.string(), z.number()]),
    param: z.union([z.string(), z.number()]),
    value: ParamValueSchema,
    time: z.number().optional(),
    interpolation: z.enum(['linear', 'bezier', 'hold']).optional(),
  }),
  remove_effect: z.object({ clip: ClipRefSchema, component: z.union([z.string(), z.number()]) }),
  insert_mogrt: z.object({ path: z.string(), time: z.number(), videoTrack: z.number().default(0), audioTrack: z.number().default(0) }),
  add_marker: z.object({ name: z.string(), time: z.number(), duration: z.number().default(0), comments: z.string().optional() }),
  set_playhead: z.object({ time: z.number() }),
  // Resolved Windows dir + filename, not the tool's `outPath`: only the server can decide where
  // a file goes (it is the side with a filesystem) and only it can create the directory first.
  export_frame: z.object({
    time: z.number(),
    dir: z.string(),
    filename: z.string(),
    width: z.number().optional(),
    height: z.number().optional(),
    sequence: z.string().optional(),
  }),
  export_sequence: z.object({
    outputFile: z.string(),
    preset: z.string(),
    exportFull: z.boolean(),
    sequence: z.string().optional(),
  }),
  eval: z.object({ code: z.string(), timeoutMs: z.number().optional() }),
  ping: EmptyArgsSchema,
} satisfies Record<CmdName, z.ZodTypeAny>

/**
 * What the panel actually sends back for every command that "returns a SequenceState": a
 * `RawSequenceDump`. The server runs it through `normalise.ts` before the caller sees it.
 *
 * Deliberately `z.unknown()` rather than a mirror of the dump's shape. `normaliseSequence()` is
 * total by contract — it takes `unknown` and degrades missing fields to nulls — so validating
 * here would add a second, stricter gate that could reject a dump the normaliser handles
 * perfectly well. The strict schema is `SequenceStateSchema`, and it applies at the tool
 * boundary where it belongs.
 */
const RawDumpWireSchema = z.unknown()

export const CmdResultSchemas = {
  status: z.object({
    connected: z.boolean(),
    appVersion: z.string().optional(),
    project: ProjectRefSchema.optional(),
    activeSequence: z.string().optional(),
    mediaRoot: z.string().nullable(),
    hint: z.string().optional(),
  }),
  open_project: z.object({ project: ProjectRefSchema, created: z.boolean(), sequences: z.array(z.string()) }),
  save: z.object({ path: z.string() }),
  import: z.object({ items: z.array(z.object({ id: z.string(), name: z.string(), mediaPath: z.string() })), bin: z.string().optional() }),
  list_items: z.object({
    items: z.array(z.object({
      id: z.string(),
      name: z.string(),
      type: z.enum(['clip', 'bin', 'sequence']),
      mediaPath: z.string().optional(),
      bin: z.string().optional(),
    })),
  }),
  create_sequence: RawDumpWireSchema,
  list_sequences: z.object({ sequences: z.array(z.object({ name: z.string(), guid: z.string(), active: z.boolean() })) }),
  set_active: RawDumpWireSchema,
  get_sequence: RawDumpWireSchema,
  insert_clip: RawDumpWireSchema,
  move_clip: RawDumpWireSchema,
  trim_clip: RawDumpWireSchema,
  remove_clip: RawDumpWireSchema,
  clone_clip: RawDumpWireSchema,
  list_transitions: z.object({ transitions: z.array(z.object({ matchName: z.string() })) }),
  add_transition: RawDumpWireSchema,
  remove_transition: RawDumpWireSchema,
  list_effects: z.object({ effects: z.array(z.object({ matchName: z.string(), displayName: z.string() })) }),
  describe_effect: z.object({
    matchName: z.string(),
    displayName: z.string(),
    componentIndex: z.number(),
    params: z.array(
      z.object({
        index: z.number(),
        name: z.string(),
        value: z.unknown().optional(),
        keyframable: z.boolean(),
        timeVarying: z.boolean(),
        unreadable: z.boolean().optional(),
      })
    ),
  }),
  apply_effect: RawDumpWireSchema,
  set_param: RawDumpWireSchema,
  remove_effect: RawDumpWireSchema,
  insert_mogrt: RawDumpWireSchema,
  add_marker: RawDumpWireSchema,
  set_playhead: z.object({ playhead: z.number() }),
  // `path` is still WINDOWS form here — this is the wire. `server.ts` converts before returning.
  export_frame: z.object({
    path: z.string(),
    time: z.number(),
    width: z.number(),
    height: z.number(),
    sequence: z.string(),
  }),
  export_sequence: z.object({ path: z.string(), sequence: z.string(), exportFull: z.boolean() }),
  eval: z.object({ value: z.unknown(), logs: z.array(z.string()) }),
  ping: z.object({ appVersion: z.string(), project: ProjectRefSchema.optional(), sequence: z.string().optional() }),
} satisfies Record<CmdName, z.ZodTypeAny>

export type CmdArgs = { [K in CmdName]: z.infer<(typeof CmdArgsSchemas)[K]> }
export type CmdResult = { [K in CmdName]: z.infer<(typeof CmdResultSchemas)[K]> }

// ---- Raw panel dump (panel -> server, before normalise.ts) ----------------------------------

/**
 * What `dumpSequence()` in the panel produces and `normalise.ts` consumes. It is the same
 * information as `SequenceState` before the server-side conversions: paths are still **Windows**
 * form, clips have no `ref` yet (the panel emits plain indices), tracks have no `V1`/`A1` label,
 * and transitions are still separate track items rather than being attached to their clips.
 *
 * Times are already **seconds** — only the panel has `TickTime` to convert with.
 *
 * `normalise.ts` must be total (never throw on a partial dump), so it takes `unknown` and reads
 * defensively; these types describe the shape the panel *intends* to send, not a guarantee.
 */
export interface RawParamDump {
  index: number
  name: string
  value: unknown
  timeVarying: boolean
  keyframes?: { t: number; value: unknown }[]
  /** Premiere would not part with the value. See `SequenceState`'s `Param.unreadable`. */
  unreadable?: boolean
}

export interface RawComponentDump {
  index: number
  matchName: string
  displayName: string
  params: RawParamDump[]
}

export interface RawTrackItemDump {
  index: number
  name: string
  start: number
  end: number
  duration: number
  inPoint: number
  outPoint: number
  mediaPath: string | null // Windows form; null for generated/synthetic items
  disabled: boolean
  speed: number
  components: RawComponentDump[]
}

/** A transition is its own track item in the API — `normalise.ts` attaches it to the clip(s)
 * whose start/end touch its time span. 🔴 Premiere never actually hands one over (every
 * transition track item marshals to `null`), so this shape is currently aspirational. */
export interface RawTransitionDump {
  matchName: string
  start: number
  end: number
  duration: number
}

export interface RawTrackDump {
  index: number
  name: string
  muted: boolean
  items: RawTrackItemDump[]
  /** Always empty in practice — see `transitionCount`. */
  transitions: RawTransitionDump[]
  /** The length of `getTrackItems(TRANSITION, …)`, which is exact even though every element
   * of it is `null`. The only transition information the API will part with. */
  transitionCount: number
}

export interface RawSequenceDump {
  project: { name: string; path: string } // path: Windows form
  sequence: {
    name: string
    guid: string
    timebase: string
    frameSize: { w: number; h: number }
    end: number
    playhead: number
  }
  videoTracks: RawTrackDump[]
  audioTracks: RawTrackDump[]
  markers: { name: string; start: number; duration: number; comments: string }[]
}
