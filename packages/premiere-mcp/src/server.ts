/**
 * The MCP server: one `registerTool` per `premiere_*` tool, over stdio.
 *
 * Everything here is the WSL half of the bridge. Its jobs are narrow and worth stating, because
 * the panel deliberately cannot do any of them:
 *
 *   - **Own the config.** The media root is established at setup, never guessed. Every tool but
 *     `premiere_status` refuses to run without it.
 *   - **Translate paths.** Callers speak `/mnt/d/…`; Premiere speaks `D:\…`. The conversion
 *     happens here and only here, in both directions.
 *   - **Make directories.** The panel has no filesystem access worth the name, so the server
 *     creates `<root>\<story>\{renders,frames}\` through `/mnt` before asking Premiere to put a
 *     project there.
 *   - **Serialise.** One Premiere, one panel, one command in flight — enforced by `bridge.ts`.
 */
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { execFile } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import os from 'node:os'
import { promisify } from 'node:util'
import { z } from 'zod'
import { Bridge, BridgeError } from './bridge'
import { ConfigError, loadConfig, storyLayout, type Config } from './config'
import { normaliseSequence } from './normalise'
import { PathError, stripExtendedPrefix, toWindows, toWsl } from './paths'
import { ParamValueSchema, type ErrorCode, type SequenceState } from './protocol'
import { fail, ok, type ToolResult } from './result'
import { buildView, diffStates, fitToBudget, type Selection, type SequenceView } from './view'
import { NAME, VERSION } from './version'

/* ---- config ------------------------------------------------------------------------------------ */

/** Re-read per call rather than cached: editing `badcode.local.json` should take effect without
 * restarting the MCP server, and the read is a single small file. */
function readConfig(): { cfg: Config | null; err: ConfigError | null } {
  try {
    return { cfg: loadConfig(process.cwd()), err: null }
  } catch (err) {
    if (err instanceof ConfigError) return { cfg: null, err }
    throw err
  }
}

function requireConfig(): Config {
  const { cfg, err } = readConfig()
  if (cfg) return cfg
  throw err ?? new ConfigError('NO_MEDIA_ROOT', 'No media root is configured.')
}

/* ---- bridge lifecycle -------------------------------------------------------------------------- */

let bridge: Bridge | null = null

/**
 * Started lazily and kept for the life of the process. The port comes from config when there is
 * one, so that `premiere_status` can still answer on a machine that has not been set up yet.
 */
async function getBridge(): Promise<Bridge> {
  if (bridge) return bridge
  const { cfg } = readConfig()
  const port = cfg?.premiere.port ?? Number(process.env.PREMIERE_BRIDGE_PORT ?? 7890)
  const bind = cfg?.premiere.bind ?? (process.env.PREMIERE_BRIDGE_BIND === 'all' ? 'all' : 'local')
  // 15s, not the 5s default: after a server restart the panel is reconnecting on its own
  // exponential backoff, which is capped at 10s. A shorter wait reports "not connected" for a
  // panel that is about to dial in a second later.
  const b = new Bridge({ port, bind, connectWaitMs: 15_000 })
  try {
    await b.listen()
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err)
    if (/EADDRINUSE/.test(message)) {
      // Almost always another Claude session that touched Premiere first. Say that, rather than
      // leaving someone to decode a socket error — and never suggest killing it, because the
      // other session may be mid-edit and only the user knows.
      throw new BridgeError(
        'PANEL_NOT_CONNECTED',
        `Another process already holds the Premiere bridge on port ${port}. ` +
          'Almost always a second Claude session that used Premiere first — only one session can drive it ' +
          '(one Premiere, one panel, strictly serial).'
      )
    }
    throw err
  }
  console.error(`[premiere-mcp] bridge listening on ws://${bind === 'all' ? '0.0.0.0' : '127.0.0.1'}:${port}`)
  bridge = b
  return b
}

/* ---- errors -------------------------------------------------------------------------------------- */

const HINTS: Partial<Record<ErrorCode, string>> = {
  PANEL_NOT_CONNECTED:
    'Open the panel in Premiere: Window ▸ Extensions (UXP) ▸ BadCode Bridge, and check the light is green. ' +
    'If it was rebuilt since Premiere started, press ⋯ → Load in UXP Developer Tool. ' +
    'If the message mentions the port being held, another Claude session is driving Premiere: work in that ' +
    'one, or close it and retry here. Run `ss -ltnp | grep 7890` to see which. Setup: docs/premiere/setup.md.',
  TIMEOUT:
    'Almost always a modal dialog waiting in Premiere — switch to it and dismiss it, then retry. ' +
    'If the machine slept, WSL localhost forwarding may have broken: `wsl --shutdown` in PowerShell.',
  NO_PROJECT: 'Open one with premiere_open_project({ story }).',
  NO_SEQUENCE: 'Create one with premiere_create_sequence, or pick one with premiere_set_active.',
  ITEM_NOT_FOUND: 'Re-read the project with premiere_list_items — names and ids both work.',
  CLIP_NOT_FOUND: 'Clip refs go stale after every edit. Use the state the last call returned, not an older one.',
  IMPORT_FAILED: 'Check the file exists on the Windows side and that Premiere can read the codec.',
  TRANSACTION_FAILED: 'Usually a locked track or a read-only project.',
  INVALID_ARGS: 'If the arguments look right, the panel may be an older build — rebuild it and press ⋯ → Load in UDT.',
  EFFECT_NOT_FOUND: 'Match names are never guessable — list them with premiere_list_effects and copy one.',
  EXPORT_FAILED:
    'Check the output directory exists and is writable, and that the preset path is right. A render can also ' +
    'fail on missing media — premiere_get_sequence reports each clip\'s mediaPath.',
  PARAM_NOT_FOUND:
    'Params are addressed by INDEX first, name second: display names repeat and some are blank. ' +
    'premiere_describe_effect reports every index.',
}

function toToolError(err: unknown): ToolResult {
  if (err instanceof ConfigError) return fail(err.code, err.message, err.hint)
  if (err instanceof PathError) {
    return fail('INVALID_ARGS', err.message, 'Paths must be absolute — `/mnt/d/…`, `D:\\…` or `/home/…`.')
  }
  if (err instanceof BridgeError) return fail(err.code, err.message, HINTS[err.code])
  return fail('PANEL_ERROR', err instanceof Error ? err.message : String(err))
}

/* ---- path helpers -------------------------------------------------------------------------------- */

/** Windows in, WSL out — every path the session sees comes back through here. */
function outPath(windowsPath: string | null | undefined): string {
  return windowsPath ? toWsl(windowsPath) : ''
}

function inPath(p: string): { path: string; warning?: string } {
  return toWindows(p)
}

/** Create a Windows directory from WSL. The panel cannot, and Premiere will not make one for us. */
function ensureDir(windowsDir: string): void {
  fs.mkdirSync(toWsl(windowsDir), { recursive: true })
}

/* Windows-path string surgery. `node:path` is posix here, so it would mangle backslashes. */
function winDirname(windowsPath: string): string {
  const cut = Math.max(windowsPath.lastIndexOf('\\'), windowsPath.lastIndexOf('/'))
  return cut <= 0 ? windowsPath : windowsPath.slice(0, cut)
}

function winJoin(...parts: string[]): string {
  return parts
    .map((part, i) => (i === 0 ? part.replace(/[\\/]+$/, '') : part.replace(/^[\\/]+|[\\/]+$/g, '')))
    .join('\\')
}

/**
 * Every tool that returns a timeline sends the panel's raw dump through `normalise.ts` — WSL
 * paths, `v0:2` refs, `V1`/`A1` labels, transitions attached to their clips. One door, so the
 * shape a session sees can never drift between tools.
 */
async function sendAndNormalise(
  cmd:
    | 'create_sequence' | 'set_active' | 'get_sequence'
    | 'insert_clip' | 'move_clip' | 'trim_clip' | 'remove_clip' | 'clone_clip'
    | 'add_transition' | 'remove_transition' | 'add_marker'
    | 'apply_effect' | 'set_param' | 'remove_effect',
  args: Record<string, unknown>,
  timeoutMs = 60_000
): Promise<SequenceState> {
  const b = await getBridge()
  const raw = await b.send(cmd, args as never, { timeoutMs })
  return normaliseSequence(raw)
}


/* ---- state views --------------------------------------------------------------------------------- */

/**
 * The last state seen per sequence, so the next one can be diffed against it.
 *
 * This is what lets `insert_clip` report the ref of the clip it just made. The panel hands back a
 * whole timeline, never a receipt, so the only way to know what an edit produced is to compare.
 * Keyed by sequence GUID; bounded because a session works on a handful of sequences, and a stale
 * entry costs nothing worse than a diff that reports more than it needs to.
 */
const lastStates = new Map<string, SequenceState>()

/**
 * Write the complete state beside the project, in `.bridge/`.
 *
 * **This is the half of the fix that keeps nothing from being lost.** The view that goes back to
 * the caller is a summary by necessity — a real timeline does not fit through the transport — but
 * the full article lands here, where a session can `jq` it for free. Dotted so it stays out of
 * the way of the media folders a human browses.
 *
 * Failure is never fatal: a read-only drive or a project opened from somewhere unwritable costs
 * the caller a note, not the tool call.
 */
function writeStateFile(state: SequenceState): { path?: string; note?: string } {
  const projectPath = state.project.path
  const dir = projectPath
    ? path.join(path.dirname(projectPath), '.bridge')
    : path.join(os.tmpdir(), 'badcode-premiere-bridge')
  try {
    fs.mkdirSync(dir, { recursive: true })
    const file = path.join(dir, `state-${safeFilename(state.sequence.name)}.json`)
    fs.writeFileSync(file, JSON.stringify(state))
    return { path: file }
  } catch (err) {
    return { note: `The full state could not be written to ${dir} (${String(err)}), so only this summary is available.` }
  }
}

/**
 * The return path for every tool that produces a timeline.
 *
 * 🔴 **Never return a raw `SequenceState` to a caller.** Jack's camping cut normalises to 573,065
 * bytes and the transport refuses anything near that — and it refuses it *after* the panel has
 * committed the edit, so the caller sees a failure for work that succeeded. Everything goes
 * through here instead: full state to disk, summary to the caller, guaranteed to fit.
 */
async function sendAndView(
  cmd: Parameters<typeof sendAndNormalise>[0],
  args: Record<string, unknown>,
  opts: { timeoutMs?: number; selection?: Selection } = {}
): Promise<SequenceView> {
  const state = await sendAndNormalise(cmd, args, opts.timeoutMs)

  const key = state.sequence.guid || state.sequence.name
  const previous = lastStates.get(key) ?? null
  lastStates.set(key, state)

  const written = writeStateFile(state)
  const view = buildView(state, opts.selection ?? {})
  if (written.path) view.statePath = written.path
  if (written.note) view.notes = [...(view.notes ?? []), written.note]

  // `get_sequence` is a read: reporting "what changed" there would describe someone else's edit.
  if (cmd !== 'get_sequence') {
    const changed = diffStates(previous, state)
    if (changed) view.changed = changed
  }
  return fitToBudget(view)
}


/* ---- export helpers ------------------------------------------------------------------------------ */

const execFileAsync = promisify(execFile)

/** Windows forbids these in a filename; sequence names do not care. */
function safeFilename(name: string): string {
  return name.replace(/[\\/:*?"<>|]/g, '-').replace(/\s+/g, ' ').trim() || 'sequence'
}

/** `2026-08-21T14:03:09` → `20260821-1403`, for a render name that sorts. */
function stamp(): string {
  const d = new Date()
  const p = (n: number): string => String(n).padStart(2, '0')
  return `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}`
}

/**
 * 🔴 Premiere's export promises resolve BEFORE the file is finished.
 *
 * Measured live 2026-08-21: `exportSequenceFrame` resolved at 8394ms, the file appeared at
 * 8498ms holding 672KB, and settled at 8704ms holding 831KB. Reading it on resolution gets a
 * truncated file — or none at all.
 *
 * So: wait for it to exist, then for its size to stop moving. `stableMs` is deliberately
 * generous relative to the ~300ms observed, because a long render writes in bursts and a brief
 * plateau mid-render must not read as finished.
 */
async function waitForStableFile(
  wslPath: string,
  { timeoutMs = 600_000, stableMs = 1500, pollMs = 200 } = {}
): Promise<number> {
  const deadline = Date.now() + timeoutMs
  let lastSize = -1
  let unchangedSince = 0

  while (Date.now() < deadline) {
    let size = -1
    try {
      size = fs.statSync(wslPath).size
    } catch {
      // Not there yet. Premiere creates it late; that is normal, not an error.
    }

    if (size > 0) {
      if (size === lastSize) {
        if (unchangedSince === 0) unchangedSince = Date.now()
        if (Date.now() - unchangedSince >= stableMs) return size
      } else {
        unchangedSince = 0
        lastSize = size
      }
    }
    await new Promise((r) => setTimeout(r, pollMs))
  }

  if (lastSize > 0) return lastSize // it exists and is still growing — report what we have
  throw new BridgeError(
    'EXPORT_FAILED',
    `Premiere reported success but nothing appeared at ${wslPath} within ${Math.round(timeoutMs / 1000)}s.`
  )
}

/** Duration in seconds, straight from the file rather than from what we asked for. */
async function probeDuration(wslPath: string): Promise<number | null> {
  try {
    const { stdout } = await execFileAsync('ffprobe', [
      '-v', 'error',
      '-show_entries', 'format=duration',
      '-of', 'default=noprint_wrappers=1:nokey=1',
      wslPath,
    ])
    const seconds = Number(stdout.trim())
    return Number.isFinite(seconds) ? seconds : null
  } catch {
    // ffprobe missing or the file is not media Premiere finished writing — not fatal.
    return null
  }
}

/** Where does the active project live, and what sequence is up? Both are needed to name a
 * default output, and only the panel knows. */
async function activeContext(): Promise<{ projectDir: string; sequence: string }> {
  const b = await getBridge()
  const pong = await b.send('ping', {})
  if (!pong.project) throw new BridgeError('NO_PROJECT', 'No project is open in Premiere.')
  if (!pong.sequence) throw new BridgeError('NO_SEQUENCE', 'No sequence is active in Premiere.')
  return { projectDir: winDirname(stripExtendedPrefix(pong.project.path)), sequence: pong.sequence }
}

/* ---- the server ------------------------------------------------------------------------------------ */

const server = new McpServer({ name: NAME, version: VERSION })

server.registerTool(
  'premiere_status',
  {
    title: 'Premiere status',
    description:
      'Is the bridge up, is the panel connected, what is open in Premiere, and where is the media root. ' +
      'This is the ONLY tool that always answers — no configured media root, no bridge, no panel, it still ' +
      'returns a result with a hint rather than an error, so it is always the right first call when something ' +
      'is not working. **Calling it OPENS the bridge**, which is why the panel goes green a few seconds after ' +
      'a session first touches Premiere and not before. ' +
      '`connected: false` means the panel is not answering: open it in Premiere (Window ▸ Extensions (UXP) ▸ ' +
      'BadCode Bridge), and if it was rebuilt since Premiere started, press ⋯ → Load in UXP Developer Tool.',
    inputSchema: {},
  },
  async () => {
    try {
      const { cfg, err } = readConfig()
      if (err && err.code === 'BAD_CONFIG') return toToolError(err)

      // Opening the bridge is itself a thing that can fail, and the commonest failure — another
      // Claude session already holding the port — is INFORMATION, not an error. `premiere_status`
      // exists to answer when nothing works; it must not be the tool that refuses to.
      let b: Bridge
      try {
        b = await getBridge()
      } catch (bridgeErr) {
        return ok({
          connected: false,
          mediaRoot: cfg?.mediaRoot ?? null,
          hint: `${bridgeErr instanceof BridgeError ? bridgeErr.message : String(bridgeErr)} ${HINTS.PANEL_NOT_CONNECTED}`,
        })
      }

      try {
        // Short window: status should answer quickly and say "no", not sit on the default wait.
        const pong = await b.send('ping', {}, { timeoutMs: 5000 })
        return ok({
          connected: true,
          appVersion: pong.appVersion,
          ...(pong.project ? { project: { name: pong.project.name, path: outPath(pong.project.path) } } : {}),
          ...(pong.sequence ? { activeSequence: pong.sequence } : {}),
          mediaRoot: cfg?.mediaRoot ?? null,
          ...(cfg ? {} : { hint: err?.hint }),
        })
      } catch (pingErr) {
        const message = pingErr instanceof BridgeError ? pingErr.message : String(pingErr)
        return ok({
          connected: false,
          mediaRoot: cfg?.mediaRoot ?? null,
          hint: `${message} ${HINTS.PANEL_NOT_CONNECTED}`,
        })
      }
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_open_project',
  {
    title: 'Open (or create) a Premiere project',
    description:
      'Open a Premiere project, creating it if it is not there. Two ways to say which, and exactly one is required:\n' +
      '  • `path` — ANY absolute path to a `.prproj`, WSL (`/mnt/d/…`) or Windows (`D:\\…`) form. Use this for a ' +
      'project that already exists anywhere on disk; no media root needed. The parent folder is created if missing.\n' +
      '  • `story` — the BadCode convention: `<mediaRoot>\\<story>\\<story>.prproj`, one project per story. ' +
      'Needs a configured media root.\n' +
      'Returns `{ project, created, sequences, framesDir, rendersDir }`. `created: true` means this call made the ' +
      'project; `false` means it already existed and was opened. **`framesDir` and `rendersDir` always sit beside ' +
      'the project file**, whichever way it was opened — so exports follow the project rather than being pinned to ' +
      'the media root.',
    inputSchema: {
      story: z.string().min(1).optional().describe('Story slug, e.g. "gitpush-origin-master" — resolved under the media root'),
      path: z.string().min(1).optional().describe('Absolute path to a .prproj, anywhere on disk. Wins if both are given.'),
    },
  },
  async ({ story, path: rawPath }) => {
    try {
      if (!story && !rawPath) {
        return fail('INVALID_ARGS', 'Provide `path` (any .prproj on disk) or `story` (resolved under the media root).')
      }

      // `path` wins: an explicit path is the caller being specific, and should never be overridden
      // by a convention.
      const projectPath = rawPath ? inPath(rawPath).path : storyLayout(requireConfig(), story!).projectPath

      if (!/\.prproj$/i.test(projectPath)) {
        return fail('INVALID_ARGS', `Not a Premiere project file: ${rawPath ?? projectPath}`, 'The path must end in .prproj.')
      }

      const projectDir = winDirname(projectPath)
      const framesDir = winJoin(projectDir, 'frames')
      const rendersDir = winJoin(projectDir, 'renders')

      // These must exist before Premiere is asked to write a project into them.
      ensureDir(projectDir)
      ensureDir(framesDir)
      ensureDir(rendersDir)

      // Only the server can answer this. Premiere's `Project.isProject()` reports whether a
      // project COULD live at a path, not whether one does — it returns true for files that do
      // not exist (live, 2026-08-21). So check the filesystem and tell the panel what to do.
      const create = !fs.existsSync(toWsl(projectPath))

      const b = await getBridge()
      const result = await b.send('open_project', { path: projectPath, create }, { timeoutMs: 120_000 })
      return ok({
        project: { name: result.project.name, path: outPath(result.project.path) },
        created: result.created,
        sequences: result.sequences,
        framesDir: outPath(framesDir),
        rendersDir: outPath(rendersDir),
      })
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_save',
  {
    title: 'Save the project',
    description: 'Save the open Premiere project in place. Returns its path.',
    inputSchema: {},
  },
  async () => {
    try {
      // No requireConfig(): saving the open project has nothing to do with the media root.
      const b = await getBridge()
      const result = await b.send('save', {}, { timeoutMs: 120_000 })
      return ok({ path: outPath(result.path) })
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_import',
  {
    title: 'Import media',
    description:
      'Import files into the open project, optionally into a named bin (created if missing). Paths may be ' +
      'WSL (`/mnt/d/…`) or Windows (`D:\\…`) — they are translated here. Media should live under the media ' +
      'root; a path outside it still imports but Premiere will be reading across a slower boundary. ' +
      'Returns the items that actually arrived — Premiere\'s import API reports only success/failure, so ' +
      'the bin is diffed before and after to work out what is new.',
    inputSchema: {
      paths: z.array(z.string().min(1)).min(1).describe('Absolute paths, WSL or Windows form'),
      bin: z.string().min(1).optional().describe('Bin name; created at the project root if it does not exist'),
    },
  },
  async ({ paths, bin }) => {
    try {
      // No requireConfig(): importing takes explicit paths, so the media root is irrelevant.
      const translated = paths.map(inPath)
      const warnings = translated.map((t) => t.warning).filter((w): w is string => Boolean(w))

      const b = await getBridge()
      const result = await b.send(
        'import',
        { paths: translated.map((t) => t.path), ...(bin ? { bin } : {}) },
        { timeoutMs: 300_000 }
      )

      return ok({
        items: result.items.map((item) => ({ ...item, mediaPath: outPath(item.mediaPath) })),
        ...(result.bin ? { bin: result.bin } : {}),
        ...(warnings.length > 0 ? { warnings: [...new Set(warnings)] } : {}),
      })
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_list_items',
  {
    title: 'List project items',
    description:
      'Every item in the open project — clips, bins and sequences — walked recursively from the root, or ' +
      'from `bin` if given. `id` and `name` are both accepted wherever a tool takes an item. Media paths ' +
      'come back in WSL form so they can be read directly.',
    inputSchema: { bin: z.string().min(1).optional().describe('Restrict the walk to this bin') },
  },
  async ({ bin }) => {
    try {
      const b = await getBridge()
      const result = await b.send('list_items', { ...(bin ? { bin } : {}) }, { timeoutMs: 60_000 })
      return ok({
        items: result.items.map((item) => ({
          ...item,
          ...(item.mediaPath ? { mediaPath: outPath(item.mediaPath) } : {}),
        })),
      })
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_create_sequence',
  {
    title: 'Create a sequence',
    description:
      'Create a sequence in the open project, then open it and make it active. The BadCode convention is one ' +
      'sequence per scene, named by scene id (`s00`, `s01`, ...), plus a `MASTER` that nests them. ' +
      'With `fromItems`, Premiere derives the settings from the media and lays those clips down — the fastest way ' +
      'to start a scene from its keepers. With `preset`, it uses that `.sqpreset` file. With neither, the project ' +
      'default. Returns the full sequence state.',
    inputSchema: {
      name: z.string().min(1).describe('Sequence name, e.g. "s00"'),
      preset: z.string().min(1).optional().describe('Absolute path to a .sqpreset file'),
      fromItems: z
        .array(z.string().min(1))
        .optional()
        .describe('Project item names or ids to build the sequence from — settings come from the first'),
    },
  },
  async ({ name, preset, fromItems }) => {
    try {
      return ok(
        await sendAndView(
          'create_sequence',
          { name, ...(preset ? { preset: inPath(preset).path } : {}), ...(fromItems ? { fromItems } : {}) },
          { timeoutMs: 120_000 }
        )
      )
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_list_sequences',
  {
    title: 'List sequences',
    description:
      'Every sequence in the open project: `{ name, guid, active }`. Cheap — it does not walk any timelines, so ' +
      'reach for it rather than premiere_get_sequence when you only need to know what exists.',
    inputSchema: {},
  },
  async () => {
    try {
      const b = await getBridge()
      return ok(await b.send('list_sequences', {}, { timeoutMs: 30_000 }))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_set_active',
  {
    title: 'Switch the active sequence',
    description:
      'Open a sequence by name and make it active — every later tool that does not name a sequence acts on this ' +
      'one. Returns its full state.',
    inputSchema: { name: z.string().min(1).describe('Sequence name, exactly as premiere_list_sequences reports it') },
  },
  async ({ name }) => {
    try {
      return ok(await sendAndView('set_active', { name }))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_get_sequence',
  {
    title: 'Read the timeline',
    description:
      'Read a sequence. BY DEFAULT THIS IS A SUMMARY, NOT A DUMP: the project, the sequence settings, and every ' +
      'track with its clip count, transition count, time span and mute state — about a kilobyte however big the ' +
      'edit is. ' +
      'ASK FOR DETAIL AND YOU GET IT: `tracks: ["v2"]` lists that track\'s clips in full, `range: [10, 30]` lists ' +
      'whatever is playing in those seconds, `clips: ["v2:3"]` expands named clips. Combine them freely. ' +
      'CLIPS ARE ADDRESSED BY `ref`: `v0:2` is the third clip on video track 0 (labelled `V1` in the UI), `a1:0` ' +
      'the first on audio track 1. Refs are ONLY valid for the state that produced them — every mutating tool ' +
      'returns a fresh view for exactly this reason, so use the newest one and never a cached one. ' +
      'THE COMPLETE STATE IS ALWAYS WRITTEN TO DISK at the returned `statePath` — every clip, every effect, every ' +
      'parameter and keyframe, untrimmed. Run `jq` over that file for anything this summary leaves out; it costs ' +
      'nothing to read and is the right tool for counting, searching or auditing a whole timeline. ' +
      'If a result would still be too large it degrades a rung at a time and `notes` says exactly what was dropped. ' +
      'Pass `params: false` to skip reading effect parameters from Premiere at all — faster on a colour-graded ' +
      'timeline, and enough when you only care about the arrangement.',
    inputSchema: {
      name: z.string().min(1).optional().describe('Sequence name; defaults to the active sequence'),
      params: z.boolean().optional().describe('Read effect parameter values from Premiere (default true)'),
      tracks: z
        .array(z.string().min(1))
        .optional()
        .describe('Expand these tracks\' clips: ["v2"] (API index) or ["V3"] (the UI label). Both work.'),
      clips: z.array(z.string().min(1)).optional().describe('Expand these clips by ref: ["v2:3", "a0:1"]'),
      range: z
        .tuple([z.number(), z.number()])
        .optional()
        .describe('[start, end] in seconds — expand whatever overlaps this window'),
    },
  },
  async ({ name, params, tracks, clips, range }) => {
    try {
      return ok(
        await sendAndView(
          'get_sequence',
          {
            ...(name ? { name } : {}),
            ...(params === undefined ? {} : { params }),
          },
          {
            selection: {
              ...(tracks ? { tracks } : {}),
              ...(clips ? { clips } : {}),
              ...(range ? { range } : {}),
              ...(params === undefined ? {} : { params }),
            },
          }
        )
      )
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_insert_clip',
  {
    title: 'Put a clip on the timeline',
    description:
      'Place a project item on the timeline at `time` (seconds). ' +
      '`mode: "overwrite"` drops it in place, replacing whatever is under it — use this when you are laying out ' +
      'shots at known positions. `mode: "insert"` splices it in and PUSHES everything after it later on that ' +
      'track — use this when you are adding a shot into an existing cut. ' +
      'Track indices are 0-based (`videoTrack: 0` is the track shown as V1). ' +
      'Passing a track index beyond the last existing track CREATES a new track. ' +
      'Returns the refreshed sequence state — read your next refs from it, never from an earlier one.',
    inputSchema: {
      item: z.string().min(1).describe('Project item name or id, from premiere_import / premiere_list_items'),
      time: z.number().describe('Where on the timeline, in seconds'),
      videoTrack: z.number().int().min(0).default(0).describe('0-based; 0 is V1'),
      audioTrack: z.number().int().min(0).default(0).describe('0-based; 0 is A1'),
      mode: z.enum(['insert', 'overwrite']).describe('"overwrite" replaces what is there; "insert" shifts it later'),
      limitShift: z
        .boolean()
        .default(false)
        .describe('insert mode only: keep the shift local rather than rippling the whole track'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('insert_clip', a, { timeoutMs: 120_000 }))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_move_clip',
  {
    title: 'Move a clip along the timeline',
    description:
      'Shift a clip by `deltaSeconds` — an OFFSET from where it is now, not a destination. Negative moves it ' +
      'earlier. Premiere expresses moves this way; to land on an absolute time, subtract the clip\'s current ' +
      '`start` (from the last state) yourself.',
    inputSchema: {
      clip: z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"'),
      deltaSeconds: z.number().describe('Offset in seconds; negative moves earlier'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('move_clip', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_trim_clip',
  {
    title: 'Trim a clip',
    description:
      'Change a clip\'s edges. TWO DIFFERENT PAIRS, and mixing them up is the usual mistake:\n' +
      '  • `inPoint` / `outPoint` — points INTO the source media: which part of the footage plays.\n' +
      '  • `start` / `end` — positions ON the timeline: where the clip sits.\n' +
      'All are seconds, all optional, at least one required. Given several, they apply in the order above.',
    inputSchema: {
      clip: z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"'),
      inPoint: z.number().optional().describe('Source in-point, seconds'),
      outPoint: z.number().optional().describe('Source out-point, seconds'),
      start: z.number().optional().describe('Timeline start, seconds'),
      end: z.number().optional().describe('Timeline end, seconds'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('trim_clip', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_remove_clip',
  {
    title: 'Remove clips',
    description:
      'Delete one or more clips. `ripple: false` (default) leaves a gap where they were; `ripple: true` closes ' +
      'the gap and pulls everything after them earlier. ' +
      'Every ref is resolved before anything is removed, so a multi-clip list means what you meant when you ' +
      'wrote it — removal renumbers the track it happens on.',
    inputSchema: {
      clips: z.array(z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"')).min(1).describe('Clip refs to remove'),
      ripple: z.boolean().default(false).describe('true closes the gap; false leaves it'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('remove_clip', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_clone_clip',
  {
    title: 'Duplicate a clip',
    description:
      'Copy a clip to another spot, keeping its trim and its effects. `deltaSeconds` offsets from the original; ' +
      '`videoTrackOffset` / `audioTrackOffset` move it up or down tracks (+1 = one track higher). ' +
      '`mode: "insert"` (default) splices the copy in and shifts what follows; `"overwrite"` drops it on top. ' +
      'This is the tool for a repeated beat or a stutter cut — it is cheaper and more faithful than re-inserting ' +
      'from the project item and reapplying everything.',
    inputSchema: {
      clip: z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"'),
      deltaSeconds: z.number().describe('Offset from the original, in seconds'),
      videoTrackOffset: z.number().int().default(0).describe('+1 puts the copy one video track higher'),
      audioTrackOffset: z.number().int().default(0),
      mode: z.enum(['insert', 'overwrite']).default('insert'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('clone_clip', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

/* ---- T9: transitions, markers, playhead ------------------------------------------------------- */

server.registerTool(
  'premiere_list_transitions',
  {
    title: 'List the video transitions this install has',
    description:
      'Every video transition match name Premiere can offer, sorted, optionally filtered by a case-insensitive ' +
      'substring. There are no friendly display names on the transition API — the match name (`AE.ADBE Cross Dissolve`) ' +
      'is all there is, so call this before premiere_add_transition rather than guessing. ' +
      'AUDIO IS NOT HERE: Premiere\'s UXP API exposes no audio transition at all.',
    inputSchema: {
      query: z.string().optional().describe('Case-insensitive substring, e.g. "dissolve"'),
    },
  },
  async ({ query }) => {
    try {
      const b = await getBridge()
      return ok(await b.send('list_transitions', query ? { query } : {}))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_add_transition',
  {
    title: 'Put a transition on a cut',
    description:
      'Add a video transition to one edge of one clip. A transition belongs to a CLIP, not to a cut: a dissolve ' +
      'between two adjacent clips is `at: "end"` on the outgoing one or `at: "start"` on the incoming one — the same ' +
      'transition described from either side, so add it once. Premiere needs media beyond the cut to dissolve into; ' +
      'a clip used to its full length has no handles and the transition will be shorter than asked for, or refused. ' +
      'Get `matchName` from premiere_list_transitions.',
    inputSchema: {
      clip: z.string().regex(/^v\d+:\d+$/, 'a VIDEO clip ref like "v0:2" — transitions are video-only'),
      matchName: z.string().describe('e.g. "AE.ADBE Cross Dissolve" — from premiere_list_transitions'),
      at: z.enum(['start', 'end']).describe('Which edge of this clip'),
      duration: z.number().positive().optional().describe('Seconds; Premiere\'s default (usually 1s) if omitted'),
      alignment: z
        .number()
        .optional()
        .describe('Raw Premiere alignment code — leave unset unless you know the mapping; the default centres on the cut'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('add_transition', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_remove_transition',
  {
    title: 'Take a transition off a cut',
    description: 'Remove the video transition from one edge of one clip. A no-op if there is none there.',
    inputSchema: {
      clip: z.string().regex(/^v\d+:\d+$/, 'a VIDEO clip ref like "v0:2" — transitions are video-only'),
      at: z.enum(['start', 'end']),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('remove_transition', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_add_marker',
  {
    title: 'Leave a marker on the sequence',
    description:
      'Add a comment marker at a time in the active sequence. This is how to hand a human a note inside Premiere — ' +
      '"beat lands here", "this cut is a frame late" — rather than only in chat. Markers come back in every ' +
      'SequenceState. `duration` > 0 makes it a span rather than a point.',
    inputSchema: {
      name: z.string().min(1).describe('Shown on the marker in the timeline'),
      time: z.number().describe('Seconds into the sequence'),
      duration: z.number().min(0).default(0).describe('Seconds; 0 (default) is a point marker'),
      comments: z.string().optional().describe('The body of the note'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('add_marker', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_set_playhead',
  {
    title: 'Move the playhead',
    description:
      'Move the program monitor to a time, so a human looking at Premiere sees the moment being discussed. ' +
      'Not an edit and not undoable. The returned `playhead` is where it actually landed — it snaps to a frame ' +
      'boundary, so it will rarely equal the time asked for exactly.',
    inputSchema: { time: z.number().describe('Seconds into the sequence') },
  },
  async ({ time }) => {
    try {
      const b = await getBridge()
      return ok(await b.send('set_playhead', { time }))
    } catch (err) {
      return toToolError(err)
    }
  }
)

/* ---- T10: effects ------------------------------------------------------------------------------ */

server.registerTool(
  'premiere_list_effects',
  {
    title: 'List the video effects this install has',
    description:
      'Every video effect Premiere can apply, as match name + display name, optionally filtered by a ' +
      'case-insensitive substring across both. ALWAYS call this before applying something — no vendor publishes ' +
      'their match names and guessing does not work. Beware near-duplicates: "Gaussian Blur" is ' +
      '`AE.Impact_Blur_FX` (20 params, most of them internal) while "Gaussian Blur (Legacy)" is ' +
      '`AE.ADBE Gaussian Blur 2` (3 clean params) — the legacy one is usually the better automation target.',
    inputSchema: { query: z.string().optional().describe('Case-insensitive substring, e.g. "blur" or "lumetri"') },
  },
  async ({ query }) => {
    try {
      const b = await getBridge()
      return ok(await b.send('list_effects', query ? { query } : {}))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_describe_effect',
  {
    title: 'List an applied effect\'s parameters',
    description:
      'Report every parameter of one effect ON A CLIP: index, display name, current value, whether it takes ' +
      'keyframes, and whether Premiere will part with its value at all. ' +
      'THE CLIP IS REQUIRED — an un-inserted effect has no readable parameters whatsoever (its object has no ' +
      'methods), so an effect must be applied before it can be described. ' +
      'ADDRESS PARAMS BY INDEX. Display names are neither unique nor always present: Lumetri Color repeats ' +
      '"Saturation", "Intensity" and "Look", and several of its params are named with a single space. ' +
      'Params flagged `unreadable` can still be WRITTEN — only reading is lost.',
    inputSchema: {
      clip: z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"'),
      component: z
        .union([z.string(), z.number().int().min(0)])
        .describe('Component index on the clip (0 = Opacity, 1 = Motion), or its match/display name'),
    },
  },
  async (a) => {
    try {
      const b = await getBridge()
      return ok(await b.send('describe_effect', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_apply_effect',
  {
    title: 'Put an effect on a clip',
    description:
      'Append (or insert) an effect on a clip and optionally set some of its parameters in the same call. ' +
      '`matchName` accepts either the match name or the display name. `params` is keyed by param index (as a ' +
      'string) or by display name — prefer indices, which are unambiguous; get them from premiere_describe_effect. ' +
      'Point values are `{x, y}` as 0–1 FRACTIONS OF THE FRAME ({x:0.5,y:0.5} is centre), colours are {r,g,b,a?}. ' +
      'NOTE this is two undo entries, not one: Premiere cannot address an effect\'s params until the effect ' +
      'itself has committed.',
    inputSchema: {
      clip: z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"'),
      matchName: z.string().describe('Match name or display name — from premiere_list_effects'),
      params: z.record(ParamValueSchema).optional().describe('{ "0": 20 } or { "Blurriness": 20 }'),
      index: z.number().int().min(0).optional().describe('Insert at this position in the chain instead of appending'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('apply_effect', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_set_param',
  {
    title: 'Set an effect parameter, or keyframe it',
    description:
      'Set one parameter on one component of one clip. Without `time` it sets a fixed value. WITH `time` it ' +
      'adds a keyframe at that moment — call it twice at two times to get a move (e.g. Scale 100 at 0s, 120 at ' +
      '2s is a slow push in). `interpolation` shapes the keyframe: "linear" for a constant rate, "bezier" for ' +
      'ease, "hold" to snap. ' +
      'This works on the intrinsics too — component "Motion" param "Scale" or "Position" is how you push, pan ' +
      'and reframe, and component "Opacity" param 0 is how you fade. ' +
      'Prefer numeric indices for `component` and `param`; names are ambiguous on Lumetri and on Opacity.',
    inputSchema: {
      clip: z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"'),
      component: z.union([z.string(), z.number().int().min(0)]).describe('Index, or match/display name'),
      param: z.union([z.string(), z.number().int().min(0)]).describe('Index (preferred), or display name'),
      value: ParamValueSchema.describe('number | string | boolean | {x,y} (0–1) | {r,g,b,a?}'),
      time: z.number().optional().describe('Seconds. Omit for a fixed value; give it to add a keyframe'),
      interpolation: z.enum(['linear', 'bezier', 'hold']).optional().describe('Only meaningful with `time`'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('set_param', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_remove_effect',
  {
    title: 'Take an effect off a clip',
    description:
      'Remove one component from a clip\'s chain. The two intrinsics (Opacity at index 0, Motion at index 1) ' +
      'cannot be removed — every clip has them and Premiere\'s own UI will not delete them either; reset their ' +
      'params instead. Indices shift after a removal, so re-read the state before removing a second one.',
    inputSchema: {
      clip: z.string().regex(/^[va]\d+:\d+$/, 'a clip ref like "v0:2" (video track 0, third clip) or "a1:0"'),
      component: z.union([z.string(), z.number().int().min(0)]).describe('Index, or match/display name'),
    },
  },
  async (a) => {
    try {
      return ok(await sendAndView('remove_effect', a))
    } catch (err) {
      return toToolError(err)
    }
  }
)

/* ---- T12: export ------------------------------------------------------------------------------ */

const FRAME_FORMATS = ['png', 'jpg', 'bmp', 'dpx', 'gif', 'exr', 'tga', 'tif']

server.registerTool(
  'premiere_export_frame',
  {
    title: 'Export a still frame',
    description:
      'Render one frame of the active sequence to an image file and return its path. This is how to SEE the ' +
      'timeline: export a frame, then Read the file to look at it. Defaults to `<project dir>/frames/<sequence>-<time>s.png` ' +
      'at the sequence frame size; `outPath` overrides it entirely and may be anywhere on disk. ' +
      'Formats: ' + FRAME_FORMATS.join(', ') + '. The returned path is a WSL path, ready to Read.',
    inputSchema: {
      time: z.number().min(0).describe('Seconds into the sequence'),
      outPath: z.string().optional().describe('Full path including extension; anywhere on disk'),
      width: z.number().int().positive().optional().describe('Defaults to the sequence width'),
      height: z.number().int().positive().optional().describe('Defaults to the sequence height'),
      sequence: z.string().optional().describe('Name; defaults to the active sequence'),
    },
  },
  async ({ time, outPath: rawOut, width, height, sequence }) => {
    try {
      let dir: string
      let filename: string

      if (rawOut) {
        const resolved = inPath(rawOut).path
        dir = winDirname(resolved)
        filename = resolved.slice(dir.length + 1)
      } else {
        const ctx = await activeContext()
        dir = winJoin(ctx.projectDir, 'frames')
        filename = `${safeFilename(sequence ?? ctx.sequence)}-${time}s.png`
      }

      const ext = (filename.split('.').pop() ?? '').toLowerCase()
      if (!FRAME_FORMATS.includes(ext)) {
        return fail(
          'INVALID_ARGS',
          `"${ext || filename}" is not a frame format Premiere exports.`,
          `Use one of: ${FRAME_FORMATS.join(', ')}.`
        )
      }

      ensureDir(dir)
      const b = await getBridge()
      const result = await b.send(
        'export_frame',
        { time, dir, filename, ...(width ? { width } : {}), ...(height ? { height } : {}), ...(sequence ? { sequence } : {}) },
        { timeoutMs: 300_000 }
      )

      // The promise resolving is not the file being finished — see waitForStableFile.
      const wsl = toWsl(result.path)
      const bytes = await waitForStableFile(wsl, { timeoutMs: 120_000 })
      return ok({ path: wsl, time: result.time, width: result.width, height: result.height, bytes, sequence: result.sequence })
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_export_sequence',
  {
    title: 'Render the sequence to a video file',
    description:
      'Render the active sequence and return the path, its real duration (measured with ffprobe, not assumed) ' +
      'and its size. Defaults to `<project dir>/renders/<sequence>-<yyyymmdd-hhmm>.mp4` using the Match Source ' +
      'high-bitrate preset; `outPath` and `preset` override those and may be anywhere on disk. ' +
      'Renders in Premiere itself rather than queueing to Media Encoder, so it blocks — allow up to 10 minutes ' +
      'and expect roughly real-time for a graded timeline. `inOutOnly: true` renders just the in/out range.',
    inputSchema: {
      outPath: z.string().optional().describe('Full path including extension; anywhere on disk'),
      preset: z.string().optional().describe('Path to an .epr; defaults to the configured export preset'),
      inOutOnly: z.boolean().default(false).describe('Render only the sequence in/out range instead of all of it'),
      sequence: z.string().optional().describe('Name; defaults to the active sequence'),
    },
  },
  async ({ outPath: rawOut, preset: rawPreset, inOutOnly, sequence }) => {
    try {
      const cfg = readConfig().cfg
      const preset = rawPreset ? inPath(rawPreset).path : cfg?.premiere.exportPreset
      if (!preset) {
        return fail(
          'NO_MEDIA_ROOT',
          'No export preset configured and none given.',
          'Set premiere.exportPreset in badcode.local.json, or pass `preset`.'
        )
      }
      if (!fs.existsSync(toWsl(preset))) {
        return fail('INVALID_ARGS', `No export preset at ${preset}.`, 'Premiere\'s presets live under MediaIO/systempresets/.')
      }

      let outputFile: string
      if (rawOut) {
        outputFile = inPath(rawOut).path
      } else {
        const ctx = await activeContext()
        outputFile = winJoin(ctx.projectDir, 'renders', `${safeFilename(sequence ?? ctx.sequence)}-${stamp()}.mp4`)
      }

      ensureDir(winDirname(outputFile))
      const b = await getBridge()
      const result = await b.send(
        'export_sequence',
        { outputFile, preset, exportFull: !inOutOnly, ...(sequence ? { sequence } : {}) },
        { timeoutMs: 600_000 }
      )

      const wsl = toWsl(result.path)
      const bytes = await waitForStableFile(wsl, { timeoutMs: 600_000, stableMs: 2000 })
      const durationSeconds = await probeDuration(wsl)
      return ok({
        path: wsl,
        bytes,
        durationSeconds,
        sequence: result.sequence,
        renderedWholeSequence: result.exportFull,
        ...(durationSeconds === null ? { note: 'ffprobe could not read a duration — the file may be incomplete.' } : {}),
      })
    } catch (err) {
      return toToolError(err)
    }
  }
)

server.registerTool(
  'premiere_eval',
  {
    title: 'Run JS inside the panel (escape hatch)',
    description:
      'Run arbitrary JavaScript inside the Premiere panel, with `ppro` (the premierepro module), `helpers` and ' +
      '`log()` in scope. `await` works at the top level of the snippet, and a value must be `return`ed — the ' +
      'code is a function body, not an expression. `helpers` carries `activeProject()`, `activeSequence(project)`, ' +
      '`resolveClip(seq, ref)`, `resolveProjectItem(project, nameOrId)`, `resolveComponent(chain, key)`, ' +
      '`dumpSequence(project, seq)`, `withTransaction(project, label, build)`, `secondsToTick`, `tickToSeconds`, ' +
      '`plainValue`, `require(id)`. ' +
      'THIS IS A DIAGNOSTIC TOOL, NOT THE PRODUCT: use it to find out what an unfamiliar API actually does, then ' +
      'promote anything you reach for twice into a typed tool. Values that will not serialise come back as ' +
      '`{ __opaque, members }` listing what the object offers, which is what makes it useful for probing.',
    inputSchema: {
      code: z.string().min(1).describe('Function body. Use `return` for a value; `await` is allowed.'),
      timeoutMs: z.number().int().positive().optional().describe('Default 60000'),
    },
  },
  async ({ code, timeoutMs }) => {
    try {
      const b = await getBridge()
      return ok(await b.send('eval', { code, ...(timeoutMs ? { timeoutMs } : {}) }, { timeoutMs: timeoutMs ?? 60_000 }))
    } catch (err) {
      if (err instanceof BridgeError && err.code === 'EVAL_ERROR') {
        return fail('EVAL_ERROR', err.message, typeof err.detail === 'string' ? err.detail : undefined)
      }
      return toToolError(err)
    }
  }
)

/* ---- go ---------------------------------------------------------------------------------------------- */

const transport = new StdioServerTransport()
await server.connect(transport)

/**
 * 🔴 **Nothing is opened here.** The bridge binds its port on the FIRST `premiere_*` call and not
 * a moment earlier — the same discipline as Flow, where the browser comes up when you start
 * working on Flow, not when you start Claude.
 *
 * This matters because Claude Code launches every server in `.mcp.json` at session startup. Four
 * open sessions means four of these processes, and if they each grabbed the port on launch, three
 * would collide before anybody had said the word "Premiere". An idle server is a few megabytes
 * doing nothing; an idle server holding the port is a session-wide outage for everyone else.
 *
 * (This was briefly the other way round, to keep the panel's light green while a session sat
 * idle. Wrong trade: the panel now says "waiting for Claude…" instead of looking broken, which
 * costs nothing and collides with nobody.)
 */

