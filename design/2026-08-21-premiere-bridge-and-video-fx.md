# Premiere bridge + video-fx toolkit — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

**Date:** 2026-08-21 · **Status:** approved (2026-08-21, Kai) — T16 research launched, T1 in progress
**Relates:** `packages/flow-mcp` (the pattern being cloned) ·
`.claude/skills/flow-automation/SKILL.md` (the skill being mirrored) ·
`docs/flow/post-production.md` (the ffmpeg half this extends) ·
`design/research/2026-08-12-enc-tokenomics/` (the research-brief convention being reused)

---

## Context

BadCode's video pipeline today is two tools joined by a conversation: **Google Flow** (driven by
`@badcode/flow-mcp` over CDP, invents the footage) and **ffmpeg** (recipe book in
`docs/flow/post-production.md`, does everything exact). Every scene ends the same way: the
approved clips sit in `/mnt/c/Users/kai/Desktop/<scene>/final/` and Kai assembles them **by
hand in Adobe Premiere Pro 2026** on the Windows host — narration from Suno, cuts, transitions,
colour, titles, render. The session that generated the footage cannot see, touch, or verify any of
that step.

This plan adds Premiere as the **third tool in the same conversation**: a session in WSL can
import clips, build and re-cut a sequence, apply and keyframe any installed effect (third-party
plugins included), insert motion-graphics templates, export a frame to *look at* and a render to
*check*, all from natural language — the loop that already works for Flow, extended to the edit.

It also adds the knowledge that makes the loop useful: **a video-effects toolkit** (`docs/video-fx/`)
built from a ~20-agent research sweep across Premiere built-ins, the plugin ecosystem (free and
paid, price-tagged), and ffmpeg, fronted by a skill that answers "we need a fire effect / a map
zoom / a film look — what's the tool, what does it cost, how do we apply it from here?" by
consulting the toolkit first, searching the web on a miss, and recording what it finds.

### Why now, and why UXP

- Premiere 2026 (installed: **26.3.2**, `C:\Program Files\Adobe\Adobe Premiere Pro 2026`) runs
  extensions on **UXP**. CEP panels are no longer loaded natively; ExtendScript support ends
  ~September 2026. `pymiere` and every CEP-based "Premiere MCP" on GitHub are dead ends.
- The UXP API at 26.3 (types: npm `@adobe/premierepro@26.3.0`, file `src/premierepro.d.ts`,
  4,675 lines — **install it as a devDependency and read it; it is the ground truth**) covers the
  whole surface this plan needs: `SequenceEditor` insert/overwrite/clone/remove,
  `VideoClipTrackItem` move/trim/transitions, `VideoFilterFactory` (any installed effect by match
  name), `ComponentParam` values + keyframes + interpolation, `TransitionFactory`,
  `SequenceEditor.insertMogrtFromPath`, `Exporter.exportSequenceFrame`,
  `EncoderManager.exportSequence`, `Markers`. Adobe's own sample
  (`github.com/AdobeDocs/uxp-premiere-pro-samples`, `sample-panels/premiere-api/src/*.ts`) shows
  every one of these being called and is the worked reference for the panel code.
- A UXP plugin **cannot listen on a socket** — it can only dial out (`WebSocket` client, with the
  target declared in the manifest). Windows→WSL `localhost:<port>` forwarding is on by default in
  WSL2 NAT mode. Together those two facts mean the bridge server lives **inside the MCP server
  process in WSL**, and nothing but the panel is installed on Windows.

### Host facts (verified 2026-08-21)

| Fact | Value |
| --- | --- |
| Windows | 11 **25H2** (build 26200) — mirrored networking available as a fallback |
| WSL | 2.7.12, distro `Ubuntu-22.04`, `.wslconfig` = `guiApplications=true`, `memory=24GB` (NAT mode, localhost forwarding default-on) |
| WSL → host IP | `ip route | grep default` → `172.24.176.1` (changes per boot; only the fallback path needs it) |
| Node (WSL) | v22.14.0 (root `engines: >=22`) · Node (Windows) v18 — **not used** |
| Premiere | 26.3.2, Media Encoder 2026 installed, no After Effects |
| UXP Developer Tool | **not installed** (no `C:\Program Files\Common Files\Adobe\UXP\Developer\settings.json`) — manual prerequisite, see T1 |
| H.264 system preset | `C:\Program Files\Adobe\Adobe Premiere Pro 2026\MediaIO\systempresets\4E49434B_48323634\01 - Match Source - High bitrate.epr` |
| ffmpeg (WSL) | 4.4.2 |
| **Media root (ruled 2026-08-21)** | **`D:\badcode-videos`** — 5.5 TB free, vs 87 GB on C:. The pre-existing `karen-music\` folder there is left alone; it predates the convention |
| esbuild | 0.21.5 already in `node_modules` (transitive) — add as an explicit devDependency |

---

## Architecture

```
 WSL (Ubuntu-22.04)                                   Windows 11 host
┌────────────────────────────────────────┐          ┌──────────────────────────────────────┐
│ Claude Code session                    │          │ Premiere Pro 2026                    │
│   │ stdio (MCP)                        │          │ ┌──────────────────────────────────┐ │
│   ▼                                    │          │ │ UXP panel  "BadCode Bridge"      │ │
│ @badcode/premiere-mcp                  │          │ │  • WebSocket CLIENT (dials out)  │ │
│  ┌ server.ts   MCP tools ─────────────┐│  ws://   │ │  • command dispatcher            │ │
│  │ bridge.ts   WS SERVER :7890        ││◀─────────│ │  • require('premierepro') calls  │ │
│  │ paths.ts    /mnt/c ↔ C:\           ││ localhost│ │  • status light + scrolling log  │ │
│  │ config.ts   badcode.local.json     ││  (WSL    │ └──────────────────────────────────┘ │
│  └────────────────────────────────────┘│  localhost│ Media Encoder 2026 (renders)        │
│ ffmpeg · @badcode/flow-mcp (unchanged) │  forward) │ <MEDIA_ROOT>\<story>\…  (all media) │
└────────────────────────────────────────┘          └──────────────────────────────────────┘
```

**Decisions (all approved 2026-08-21):**

1. **Server in WSL, panel dials out.** `bridge.ts` opens a `ws` server on `127.0.0.1:7890`
   (and `0.0.0.0` only if `PREMIERE_BRIDGE_BIND=all`, for the direct-IP fallback). The panel
   connects to `ws://localhost:7890`. No Windows-side proxy. Fallbacks, documented in
   `docs/premiere/setup.md`, in order: (a) `wsl --shutdown` (forwarding breaks after host
   sleep), (b) `networkingMode=mirrored` in `%USERPROFILE%\.wslconfig`, (c) the panel's URL
   field pointed at WSL's `172.24.x.x` IP with `PREMIERE_BRIDGE_BIND=all`.
2. **One configurable root, one fixed tree.** `badcode.local.json` at the repo root (gitignored,
   per machine) names `mediaRoot`. Everything under it is convention:

   ```
   <MEDIA_ROOT>\
     _bridge\panel\                     ← built UXP panel, mirrored here so UDT loads a local path
     <story>\                           ← story slug = its docs/stories/<story>/ folder name
       <story>.prproj                   ← ONE project per story
       renders\                         ← premiere_export_sequence outputs
       frames\                          ← premiere_export_frame PNGs (the session's eyes)
       <scene>\                         ← Flow takes (today's Desktop\<scene>\, relocated in T14)
         final\                         ← keepers — the only thing that gets imported
   ```

   One **sequence per scene** named by scene id (`s00`, `s01`, …) plus `MASTER` nesting them.
   Bins mirror `<scene>\final\`. Tools default to the active project/sequence and can open or
   create by story slug.

   **AMENDED 2026-08-21 (Kai, during T6): the media root is a default, not a cage.**
   `premiere_open_project` takes **either** `story` (resolved under the media root, as above) **or**
   `path` — any absolute `.prproj` anywhere on disk, in WSL or Windows form, needing no media root
   at all. Kai's case is the ordinary one: a project downloaded to a folder of its own that he wants
   to point us at by pasting its path. Consequences, all deliberate:
   - **`frames\` and `renders\` always sit beside the project file**, whichever way it was opened.
     Exports follow the project rather than being pinned to the root, and
     `premiere_open_project` returns both paths so the session never has to guess.
   - Only `story` mode raises `NO_MEDIA_ROOT`. `premiere_save`, `premiere_import` and
     `premiere_list_items` never needed the root and no longer ask for it — they work on explicit
     paths and the open project.
   - The story convention is untouched and remains what `make-comic` and the ledgers use.
3. **Every mutation is one transaction** (sole exception: `premiere_insert_mogrt`, whose API is not an Action — see the tool table). Panel commands wrap
   `project.lockedAccess(() => project.executeTransaction(ca => {...}, 'BadCode: <label>'))`
   — atomic, one undo step. Every mutating tool returns the **refreshed `SequenceState`** so the
   session never needs a second call and clip refs never go stale.
4. **Clips are addressed as `v<track>:<item>`** (0-based API indices, e.g. `v0:2` = third clip
   on V1) from the most recent state; `a<track>:<item>` for audio. The state carries human
   labels (`V1`, `A2`).
5. **Paths are translated at the server boundary only.** The panel sees Windows paths
   exclusively. Inputs accept `/mnt/c/…`, `C:\…`, and `/home/kai/…` (→
   `\\wsl.localhost\Ubuntu-22.04\…`, accepted with a warning — media belongs under the root).
   Outputs are always written under the root and returned in WSL form.
6. **Strictly serial.** One panel connection, one in-flight command — the same law as Flow's one
   browser.
7. **`premiere_eval` is the escape hatch, not the product.** It runs JS in the panel with
   `ppro` + helpers in scope so a new plugin's API can be tried from the conversation the day it
   is installed. Anything used twice gets promoted to a typed tool.
8. **Research and build run in parallel.** The research sweep (T16) needs no code and starts the
   moment the plan is approved; the toolkit distillation (T17) follows it.

**Rejected:** generate FCP7 XML and import (no live control, no effects, no read-back, a hand-off
not a loop) · CEP / pymiere (unloaded by Premiere 2026) · a Windows-side Node proxy à la
`mikechambers/adb-mcp` (extra process, old Windows Node, no benefit once localhost forwarding
works) · any of the "285 / 1,027-tool" Premiere MCPs (unverified, mostly CEP) · CDP (Premiere is
not a browser).

### Data flow

```
"put the s00 keepers on V1 in ledger order, dissolve between, blur the last one"
        │
        ▼ MCP tool call                     ┌──────────── panel ────────────┐
server.ts ── zod validate ──▶ bridge.ts ──▶ │ dispatch(cmd)                  │
  paths.ts: /mnt/c/… → C:\…   {id,cmd,args} │  withTransaction(project, …,   │
                                            │    ca => { ca.addAction(…) })  │  ← atomic, one undo
                               {id,ok,result}│  dumpSequence() → result      │
server.ts ◀── normalise.ts ◀── bridge.ts ◀──└────────────────────────────────┘
  returns SequenceState (+ Windows paths back in WSL form)
        │
        ▼
premiere_export_frame({time: 12}) → <root>\gitpush-origin-master\frames\s00-12.000.png
        → session Reads it → adjusts → repeats
```

The conversational loop this enables: Flow generates → ffmpeg conforms → `premiere_import` +
`premiere_insert_clip` → `premiere_export_frame` / `premiere_export_sequence` →
`scripts/video-contact-sheet.sh` → the session looks → iterate. The scene ledger
(`docs/stories/<story>/scenes/<scene>.md`) gains a **Premiere** section (sequence name, what was
applied, render path) — it stays the record of the cut.

---

## File Structure

**Create**

| Path | Purpose |
| --- | --- |
| `packages/premiere-mcp/package.json` | `@badcode/premiere-mcp`, `type: module`, bin `badcode-premiere-mcp`, scripts `start` / `typecheck` (= `tsc --noEmit -p tsconfig.json && tsc --noEmit -p tsconfig.panel.json`) / `test` / `build:panel` (= `tsx scripts/build-panel.ts`) / `build:panel:watch`; deps `@modelcontextprotocol/sdk`, `ws`, `zod`; dev `@adobe/premierepro`, `@types/ws`, `esbuild`, `tsx`, `vitest`, `@types/node` |
| `packages/premiere-mcp/tsconfig.json` | extends `../../tsconfig.base.json`, `noEmit`, `types: ["node"]`, `include: ["src", "scripts"]` (same as flow-mcp plus the build script) |
| `packages/premiere-mcp/tsconfig.panel.json` | for `panel/src` only. **Does NOT extend the base** (base's `moduleResolution: "bundler"` + `verbatimModuleSyntax` are incompatible with a CJS bundle): `module: commonjs`, `moduleResolution: node`, `target: ES2020`, `lib: ["ES2020","DOM"]`, `strict: true`, `noEmit: true`, `types: []`, `paths: { "premierepro": ["../../node_modules/@adobe/premierepro/src/premierepro.d.ts"] }`, `include: ["panel/src", "src/protocol.ts"]` |
| `packages/premiere-mcp/src/result.ts` | `ok()` / `fail()` / `ToolResult` — copied from `packages/flow-mcp/src/result.ts` |
| `packages/premiere-mcp/README.md` | tool reference in flow-mcp's style: "ground truth is `src/server.ts`"; error table |
| `packages/premiere-mcp/src/index.ts` | `export { NAME, VERSION } from './version'` |
| `packages/premiere-mcp/src/version.ts` | `NAME = '@badcode/premiere-mcp'`, `VERSION` |
| `packages/premiere-mcp/src/server.ts` | MCP server over stdio; one `server.registerTool(...)` per tool; `toToolError()` exactly as `packages/flow-mcp/src/server.ts:40`, `ok()`/`fail()` from `src/result.ts` |
| `packages/premiere-mcp/src/bridge.ts` | `Bridge` class: `ws` server, hello handshake, id-correlated request/response, serial queue, per-command timeout, connect-wait |
| `packages/premiere-mcp/src/protocol.ts` | zod schemas + TS types for every command's args and result, the envelope, `ErrorCode`, `SequenceState` — **shared by server and panel** |
| `packages/premiere-mcp/src/paths.ts` | pure `toWindows()` / `toWsl()` / `isUnderRoot()` |
| `packages/premiere-mcp/src/config.ts` | `loadConfig()` from `badcode.local.json` + env; `storyLayout()` |
| `packages/premiere-mcp/src/normalise.ts` | raw panel dump → `SequenceState` (pure; fixtures from live captures) |
| `packages/premiere-mcp/src/*.test.ts` | vitest for bridge, protocol, paths, config, normalise |
| `packages/premiere-mcp/src/smoke-*.ts` | live scripts against real Premiere: `smoke-status`, `smoke-project`, `smoke-sequence`, `smoke-edit`, `smoke-transitions`, `smoke-effects`, `smoke-mogrt-eval`, `smoke-export`, `smoke-e2e` |
| `packages/premiere-mcp/panel/manifest.json` | UXP manifest v5 (see Interfaces) |
| `packages/premiere-mcp/panel/index.html` | status light, server URL field (default `ws://localhost:7890`), connect/disconnect button, scrolling log |
| `packages/premiere-mcp/panel/icons/{dark,light,plugin-icon}.png` | required by the manifest |
| `packages/premiere-mcp/panel/src/main.ts` | connect + reconnect with backoff, hello, dispatch, UI |
| `packages/premiere-mcp/panel/src/ppro.ts` | `const ppro = require('premierepro')` + `withTransaction`, `secondsToTick`, `tickToSeconds`, `resolveClip`, `resolveProjectItem`, `dumpSequence`, `PanelError` |
| `packages/premiere-mcp/panel/src/commands/{project,sequence,clips,transitions,effects,mogrt,markers,export,eval}.ts` | one handler per command, each returning a `protocol.ts` result shape |
| `packages/premiere-mcp/panel/dist/` | esbuild output (`main.js` + copied `manifest.json`, `index.html`, `icons/`); gitignored; mirrored to `<MEDIA_ROOT>\_bridge\panel\` |
| `packages/premiere-mcp/scripts/build-panel.ts` | run via `tsx`; esbuild bundle (`format: cjs`, `platform: neutral`, `external: ['premierepro','uxp','os','fs']`), copy statics; from T3 on, also mirrors `dist/` to `panelMirrorDir(cfg)` (imports `src/config.ts`) |
| `docs/premiere/README.md` | index of this folder; the two-jobs split (craft vs automation) like `docs/flow/README.md` |
| `docs/premiere/setup.md` | UDT install, developer mode, load panel, networking fallbacks, media root, export preset |
| `docs/premiere/bridge-protocol.md` | the wire protocol + error codes (generated-by-hand from `protocol.ts`, kept in sync) |
| `docs/premiere/api-notes.md` | live-discovered facts: intrinsic match names (Motion/Opacity), param indices for Lumetri/Gaussian Blur/Cross Dissolve, export completion behaviour, UXP quirks |
| `.claude/skills/premiere-automation/SKILL.md` | mechanics skill mirroring `flow-automation`: bring it up, `premiere_status` table, recovery, the laws |
| `.claude/skills/video-fx/SKILL.md` | judgement skill: lane choice (ffmpeg / built-in / plugin), toolkit-first → web-on-miss → record-back procedure, price/licence gate |
| `docs/video-fx/README.md` + category pages | the distilled toolkit (T17 defines the exact pages from the briefs) |
| `design/research/2026-08-21-video-fx-landscape/README.md` + `NN-<topic>.md` | raw research briefs (T16) |
| `badcode.local.json.example` | committed template for the local config |

**Modify**

| Path | Change |
| --- | --- |
| `.mcp.json` | add `"premiere": { "command": "npx", "args": ["tsx", "packages/premiere-mcp/src/server.ts"] }` |
| `.gitignore` | add `badcode.local.json` (the global `dist/` rule already covers `panel/dist/`) |
| `CLAUDE.md` | repo-map row for `packages/premiere-mcp`, `docs/premiere/`, `docs/video-fx/`; two bullets under "How to work in this repo" for the new skills |
| `docs/README.md` | index rows for `docs/premiere/` and `docs/video-fx/` |
| `.claude/skills/flow-automation/SKILL.md` (§"While you are working: nothing goes in the repo", lines 412–418) | scratch-folder convention → `<MEDIA_ROOT>\<story>\<scene>\` and `…\final\` |
| `docs/stories/gitpush-origin-master/scenes/s00-awakening.md` (lines 303, 476, 588) and `s01-the-push.md` (line 17) | update the `/mnt/c/Users/kai/Desktop/gpom-sNN/` paths to the new root after T14's move |
| `docs/flow/README.md` | one line pointing at `docs/premiere/` and `docs/video-fx/` as the downstream of `post-production.md` |

**Delete** — nothing.

---

## Interfaces

### Local config — `badcode.local.json` (repo root, gitignored)

```jsonc
{
  "mediaRoot": "D:\\badcode-videos",                     // REQUIRED. Windows path. RULED 2026-08-21.
  "premiere": {
    "port": 7890,                                            // optional, default 7890
    "exportPreset": "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2026\\MediaIO\\systempresets\\4E49434B_48323634\\01 - Match Source - High bitrate.epr"   // optional; this path IS the default
  }
}
```

Env overrides (win over the file): `BADCODE_MEDIA_ROOT`, `PREMIERE_BRIDGE_PORT`,
`PREMIERE_EXPORT_PRESET`, `PREMIERE_BRIDGE_BIND` (`local` default | `all`).

```ts
// src/config.ts
export interface Config { mediaRoot: string; premiere: { port: number; exportPreset: string; bind: 'local' | 'all' } }
export function loadConfig(repoRoot?: string): Config            // throws ConfigError { code: 'NO_MEDIA_ROOT' | 'BAD_CONFIG' } — both are ErrorCodes, surfaced as-is by toToolError
export function storyLayout(cfg: Config, story: string): {
  root: string; projectPath: string; rendersDir: string; framesDir: string;
  sceneDir(scene: string): string; finalDir(scene: string): string   // all Windows paths
}
export function panelMirrorDir(cfg: Config): string                 // <mediaRoot>\_bridge\panel
```

### Paths — `src/paths.ts` (pure, no shell-out)

```ts
export function toWindows(p: string, distro = process.env.WSL_DISTRO_NAME ?? 'Ubuntu-22.04'): { path: string; warning?: string }
//  '/mnt/c/Users/kai/x.mp4'  → 'C:\Users\kai\x.mp4'
//  'C:\Users\kai\x.mp4'      → unchanged
//  '/home/kai/x.mp4'         → '\\wsl.localhost\Ubuntu-22.04\home\kai\x.mp4' + warning 'outside media root'
//  relative                  → throws PathError('RELATIVE_PATH') — toToolError maps it to INVALID_ARGS
export function toWsl(p: string): string
//  'C:\Users\kai\x.mp4'                         → '/mnt/c/Users/kai/x.mp4'
//  '\\wsl.localhost\Ubuntu-22.04\home\kai\x'    → '/home/kai/x'
//  '/mnt/c/…'                                   → unchanged
export function isUnderRoot(windowsPath: string, mediaRoot: string): boolean   // case-insensitive, separator-normalised
```

### Wire protocol — `src/protocol.ts` (shared)

```ts
export type Hello  = { type: 'hello'; appVersion: string; panelVersion: string; protocol: 1 }
export type Cmd    = { type: 'cmd'; id: string; cmd: CmdName; args: unknown }
export type Result = { type: 'result'; id: string; ok: true; result: unknown }
                   | { type: 'result'; id: string; ok: false; code: ErrorCode; message: string; detail?: unknown }
export type Log    = { type: 'log'; level: 'info' | 'warn' | 'error'; message: string }

export type ErrorCode =
  | 'NO_MEDIA_ROOT' | 'PANEL_NOT_CONNECTED' | 'TIMEOUT' | 'NO_PROJECT' | 'NO_SEQUENCE'
  | 'ITEM_NOT_FOUND' | 'CLIP_NOT_FOUND' | 'EFFECT_NOT_FOUND' | 'TRANSITION_NOT_FOUND'
  | 'PARAM_NOT_FOUND' | 'TRANSACTION_FAILED' | 'IMPORT_FAILED' | 'EXPORT_FAILED'
  | 'INVALID_ARGS' | 'EVAL_ERROR' | 'PANEL_ERROR' | 'BAD_CONFIG'

// CmdName = the tool name without its `premiere_` prefix, PLUS `ping` (panel-only, used by smoke-status and
// the bridge's liveness check; there is no premiere_ping tool). CmdArgs / CmdResult are zod-derived maps.
```

Times at the tool boundary are **seconds (number)**; the panel converts with
`ppro.TickTime.createWithSeconds(s)` and reports back via `tickTime.seconds`. Track indices are the
API's 0-based indices.

### `SequenceState` (returned by `premiere_get_sequence` and every mutating tool)

```ts
export interface SequenceState {
  project: { name: string; path: string /* WSL form */ }
  sequence: { name: string; guid: string; timebase: string; frameSize: { w: number; h: number }; end: number; playhead: number }
  videoTracks: Track<VideoClip>[]
  audioTracks: Track<AudioClip>[]
  markers: { name: string; start: number; duration: number; comments: string }[]
}
interface Track<C> { index: number; label: string /* 'V1' | 'A1' */; name: string; muted: boolean; items: C[] }
interface ClipBase {
  ref: string            // 'v0:2' | 'a1:0'
  name: string; start: number; end: number; duration: number; inPoint: number; outPoint: number
  mediaPath: string | null   // WSL form; null for generated/synthetic items
  disabled: boolean; speed: number
}
interface VideoClip extends ClipBase {
  components: Component[]
  transitions: { start?: TransitionInfo; end?: TransitionInfo }
}
interface AudioClip extends ClipBase { components: Component[] }
interface Component { index: number; matchName: string; displayName: string; params: Param[] }
interface Param { index: number; name: string; value: unknown; timeVarying: boolean; keyframes?: { t: number; value: unknown }[] }
interface TransitionInfo { matchName: string; duration: number }
```

### Bridge — `src/bridge.ts`

```ts
export class Bridge {
  constructor(opts: { port: number; bind: 'local' | 'all'; connectWaitMs?: number /* 5000 */; defaultTimeoutMs?: number /* 30000 */ })
  listen(): Promise<void>
  close(): Promise<void>
  readonly connected: boolean
  readonly hello: Hello | null
  send<C extends CmdName>(cmd: C, args: CmdArgs[C], opts?: { timeoutMs?: number }): Promise<CmdResult[C]>
  // serial FIFO; waits connectWaitMs for a panel before rejecting PANEL_NOT_CONNECTED;
  // rejects BridgeError { code: ErrorCode, message, detail? }; a panel disconnect mid-command rejects PANEL_NOT_CONNECTED
}
```

### Tool surface — `src/server.ts` (args → result; all errors `{ error: true, code, message, hint? }`)

| Tool | Args | Result | Panel API (from `premierepro.d.ts`) |
| --- | --- | --- | --- |
| `premiere_status` | — | `{ connected, appVersion?, project?: {name,path}, activeSequence?: string, mediaRoot: string \| null, hint? }` | `Project.getActiveProject()`, `getActiveSequence()`, `ppro.Application.version`. **The only tool that runs without config** — reports `mediaRoot: null` + hint instead of `NO_MEDIA_ROOT` |
| `premiere_open_project` | `{ story }` | `{ project: {name,path}, created: boolean, sequences: string[] }` | `Project.isProject(p) ? Project.open(p, OpenProjectOptions().setShowLocateFileDialog(false)) : Project.createProject(p)` |
| `premiere_save` | — | `{ path }` | `project.save()` |
| `premiere_import` | `{ paths: string[], bin?: string }` | `{ items: { id, name, mediaPath }[], bin }` | bin: walk `getRootItem().getItems()` for a `FolderItem` named `bin`; if missing, `withTransaction(…, ca => ca.addAction(rootItem.createBinAction(bin, false)))` then **re-find it by name** (actions return nothing). Import: snapshot the bin's item ids, `await project.importFiles(winPaths, true, binItem)` (returns only `boolean`), re-list the bin and **diff ids** to build `items`; `false` → `IMPORT_FAILED` |
| `premiere_list_items` | `{ bin? }` | `{ items: { id, name, type: 'clip'|'bin'|'sequence', mediaPath? , bin }[] }` | `getRootItem().getItems()` recursive; `ClipProjectItem.cast(item).getMediaFilePath()` |
| `premiere_create_sequence` | `{ name, preset?: string, fromItems?: string[] }` | `SequenceState` | `createSequence(name, preset)` or `createSequenceFromMedia(name, clipItems)`; then `openSequence` + `setActiveSequence` |
| `premiere_list_sequences` | — | `{ sequences: { name, guid, active }[] }` | `getSequences()` |
| `premiere_set_active` | `{ name }` | `SequenceState` | `setActiveSequence` + `openSequence` |
| `premiere_get_sequence` | `{ name? }` | `SequenceState` | full walk: tracks → `getTrackItems(CLIP,false)` → `getComponentChain()` → params. Transitions: `getTrackItems(TRANSITION,false)` on the same track gives separate items; `normalise.ts` attaches each to the clip(s) whose `start`/`end` touch its time span (`end` of the outgoing clip, `start` of the incoming), `duration` from the transition item's `getDuration()`, `matchName` from its `getMatchName()` |
| `premiere_insert_clip` | `{ item, time, videoTrack=0, audioTrack=0, mode: 'insert'|'overwrite', limitShift=false }` | `SequenceState` | `SequenceEditor.getEditor(seq).createInsertProjectItemAction(pi, t, v, a, limitShift)` / `createOverwriteItemAction(pi, t, v, a)` |
| `premiere_move_clip` | `{ clip, deltaSeconds }` | `SequenceState` | `trackItem.createMoveAction(tick(delta))` |
| `premiere_trim_clip` | `{ clip, inPoint?, outPoint?, start?, end? }` | `SequenceState` | `createSetInPointAction` / `createSetOutPointAction` / `createSetStartAction` / `createSetEndAction` |
| `premiere_remove_clip` | `{ clips: string[], ripple=false }` | `SequenceState` | `TrackItemSelection.createEmptySelection(sel => sel.addItem(ti))` → `createRemoveItemsAction(sel, ripple, MediaType.ANY, false)` |
| `premiere_clone_clip` | `{ clip, deltaSeconds, videoTrackOffset=0, audioTrackOffset=0, mode='insert' }` | `SequenceState` | `createCloneTrackItemAction(ti, tick, vOff, aOff, true, mode==='insert')` |
| `premiere_list_transitions` | `{ query? }` | `{ transitions: { matchName }[] }` | `TransitionFactory.getVideoTransitionMatchNames()` |
| `premiere_add_transition` | `{ clip, matchName, at: 'start'|'end', duration?: number, alignment?: number }` | `SequenceState` | `createAddVideoTransitionAction(TransitionFactory.createVideoTransition(mn), AddTransitionOptions().setApplyToStart(at==='start').setDuration(tick(d)).setTransitionAlignment(a))` |
| `premiere_remove_transition` | `{ clip, at }` | `SequenceState` | `createRemoveVideoTransitionAction(TransitionPosition.START/END)` |
| `premiere_list_effects` | `{ query? }` | `{ effects: { matchName, displayName }[] }` | `VideoFilterFactory.getMatchNames()` zipped with `getDisplayNames()`; `query` is case-insensitive substring on either |
| `premiere_describe_effect` | `{ matchName, clip? }` | `{ matchName, displayName, params: { index, name, value?, keyframable }[] }` | `createComponent(mn)` returns `VideoFilterComponent`, typed `{}` — **cast to `Component`** before `getParamCount()` / `getParam(i).displayName` / `areKeyframesSupported()`. **If an un-inserted component cannot report params at runtime (T10 decides), `clip` becomes required and params are read from the applied instance** |
| `premiere_apply_effect` | `{ clip, matchName, params?: Record<string|number, unknown>, index? }` | `SequenceState` | `createComponent` → `chain.createAppendComponentAction` (or `createInsertComponentAction(c, index)`) + `createSetValueAction(param.createKeyframe(v), true)` per param, in ONE transaction |
| `premiere_set_param` | `{ clip, component: string|number, param: string|number, value, time?, interpolation?: 'linear'|'bezier'|'hold' }` | `SequenceState` | no `time` → `createSetValueAction`; with `time` → `createSetTimeVaryingAction(true)` (if needed) + `createAddKeyframeAction(kf at tick)` + `createSetInterpolationAtKeyframeAction(tick, InterpolationMode.X)` |
| `premiere_remove_effect` | `{ clip, component: string|number }` | `SequenceState` | `createRemoveComponentAction` |
| `premiere_insert_mogrt` | `{ path, time, videoTrack=0, audioTrack=0 }` | `SequenceState` | `SequenceEditor.insertMogrtFromPath(winPath, tick, v, a)` — **not an Action**: returns the inserted track items synchronously, so it runs inside `lockedAccess` but outside `executeTransaction`; the one exception to Decision 3 (no single `BadCode:` undo label; Premiere's own undo entry applies) |
| `premiere_add_marker` | `{ name, time, duration=0, comments? }` | `SequenceState` | `Markers.getMarkers(seq)` → `createAddMarkerAction(name, 'Comment', tick, tick(d), comments)` |
| `premiere_set_playhead` | `{ time }` | `{ playhead }` | `sequence.setPlayerPosition(tick)` |
| `premiere_export_frame` | `{ time, outPath?, width?, height? }` | `{ path /* WSL */, time }` | `Exporter.exportSequenceFrame(seq, tick, filename, dir, w, h)`; default `<root>\<story>\frames\<seq>-<time>.png`, default size = sequence frame size |
| `premiere_export_sequence` | `{ outPath?, preset?, inOutOnly=false }` | `{ path /* WSL */, durationSeconds, bytes }` | `EncoderManager.getManager().exportSequence(seq, ExportType.IMMEDIATELY, winOut, preset, !inOutOnly)`; await, then poll the file until size is stable 2s; timeout 600 s; default `<root>\<story>\renders\<seq>-<yyyymmdd-hhmm>.mp4` |
| `premiere_eval` | `{ code, timeoutMs? }` | `{ value: unknown, logs: string[] }` | `new Function('ppro','helpers','log', code)` inside the panel; `helpers` = `{ withTransaction, secondsToTick, tickToSeconds, resolveClip, resolveProjectItem, dumpSequence, activeProject(), activeSequence() }`; result JSON-serialised (non-serialisable → `String(value)`) |

`clip` everywhere is a `ref` (`v0:2`); `item` is a project-item **name or id** as returned by
`premiere_list_items`. Every mutating tool is one `executeTransaction`, labelled
`BadCode: <tool>` so it reads well in Edit ▸ Undo.

### UXP manifest — `panel/manifest.json`

```json
{
  "id": "com.badcode.premiere-bridge",
  "name": "BadCode Bridge",
  "version": "0.1.0",
  "main": "index.html",
  "host": { "app": "premierepro", "minVersion": "26.0.0" },
  "manifestVersion": 5,
  "requiredPermissions": {
    "network": { "domains": ["ws://localhost:7890", "ws://127.0.0.1:7890", "ws://*:7890"] },
    "localFileSystem": "request"
  },
  "entrypoints": [{
    "type": "panel", "id": "bridge",
    "label": { "default": "BadCode Bridge" },
    "minimumSize": { "width": 260, "height": 200 },
    "preferredDockedSize": { "width": 320, "height": 260 },
    "preferredFloatingSize": { "width": 420, "height": 320 },
    "icons": [
      { "width": 23, "height": 23, "path": "icons/dark.png",  "scale": [1, 2], "theme": ["darkest", "dark", "medium"] },
      { "width": 23, "height": 23, "path": "icons/light.png", "scale": [1, 2], "theme": ["lightest", "light"] }
    ]
  }],
  "icons": [{ "width": 48, "height": 48, "path": "icons/plugin-icon.png", "scale": [1, 2], "theme": ["all"], "species": ["pluginList"] }]
}
```

(Shape from Adobe's `sample-panels/premiere-api/public/manifest.json`; the `network` block from
the Premiere UXP network recipe. If `ws://*:7890` is rejected by the manifest validator, drop it and
keep the two explicit entries — T1 records which forms load.)

### Panel helpers — `panel/src/ppro.ts`

```ts
export const ppro: typeof import('premierepro')           // const ppro = require('premierepro')
export class PanelError extends Error { constructor(public code: ErrorCode, message: string, public detail?: unknown) }
export function withTransaction(project: Project, label: string, build: (ca: CompoundAction) => void): void
//   project.lockedAccess(() => { ok = project.executeTransaction(build, `BadCode: ${label}`) }); if (!ok) throw new PanelError('TRANSACTION_FAILED', label)
export const secondsToTick: (s: number) => TickTime       // ppro.TickTime.createWithSeconds
export const tickToSeconds: (t: TickTime) => number       // t.seconds
export async function activeProject(): Promise<Project>   // throws NO_PROJECT
export async function activeSequence(project: Project, name?: string): Promise<Sequence>   // throws NO_SEQUENCE
export async function resolveClip(seq: Sequence, ref: string): Promise<VideoClipTrackItem | AudioClipTrackItem>  // throws CLIP_NOT_FOUND
export async function resolveProjectItem(project: Project, nameOrId: string): Promise<ProjectItem>            // throws ITEM_NOT_FOUND
export async function resolveComponent(chain: VideoComponentChain | AudioComponentChain, key: string | number): Promise<Component>  // by index or matchName/displayName
export async function dumpSequence(project: Project, seq: Sequence): Promise<RawSequenceDump>   // what normalise.ts consumes
```

---

## Out of Scope

- **Any Windows-side service** beyond the UXP panel. No Windows Node, no proxy, no scheduled task.
- **Buying, downloading or installing plugins / templates.** The `video-fx` skill finds, prices and
  documents; a human installs. The bridge then drives whatever is installed.
- **After Effects / Dynamic Link automation** (AE is not installed). The research *describes* the
  AE crossover so the toolkit can say "this one needs AE".
- **Audio mixing beyond insert + component params.** Narration/music placement is in scope via
  `premiere_insert_clip` on audio tracks and `premiere_set_param` on the audio chain; Essential
  Sound panel automation is not.
- **Captions/transcription, Productions, Team Projects, proxies, C2PA.**
- **A `scene-prompt` skill** or any change to Flow prompt craft.
- **Packaging the panel as a signed `.ccx` / Marketplace listing.** UDT-loaded is the supported
  mode for this repo; packaging notes go in `api-notes.md` only if discovered for free.
- **Moving `.prproj` or media into git.** The repo tracks prompts, ledgers, stills and code only.

---

## Tickets

### T1: Spike — the panel reaches WSL   [Status: DONE 2026-08-21 | Model: opus]
- **Scope:** Prove the one thing everything depends on: a UXP panel loaded into Premiere 26.3 via
  UXP Developer Tool can open a `WebSocket` to a `ws` server running in WSL and exchange a
  message. Minimal panel (`manifest.json`, `index.html`, hand-written `main.js` — no build step
  yet), minimal server (`src/spike-server.ts`: `ws` on 7890, logs hello, echoes). Records which
  manifest `network.domains` forms load, whether `ws://localhost` connects under default NAT,
  where the panel appears in Premiere's menus, whether UDT will load the plugin from a
  `\\wsl.localhost\…` path or needs the `<MEDIA_ROOT>\_bridge\panel\` mirror, and two runtime
  checks T11 depends on: `typeof WebSocket === 'function'` and `new Function('return 1')()`
  both work inside the panel. **Manual steps for
  Kai, stated in the ticket's Notes as a checklist:** install UXP Developer Tools from the Creative
  Cloud desktop app (All apps → UXP Developer Tools; admin rights), enable Developer Mode when UDT
  prompts, in Premiere enable Settings ▸ Plugins ▸ *Enable developer mode* and restart, choose the
  media root and write `badcode.local.json`.
- **Files:** create `packages/premiere-mcp/panel/manifest.json`, `panel/index.html`,
  `panel/main.js` (spike version), `packages/premiere-mcp/src/spike-server.ts`,
  `packages/premiere-mcp/package.json` (minimal: `ws`, `tsx`), `badcode.local.json.example`;
  modify `.gitignore`.
- **Acceptance criteria:** `npx tsx packages/premiere-mcp/src/spike-server.ts` prints
  `hello from panel appVersion=26.3.2` within 10 s of clicking Connect in the panel; an echo
  round-trip completes; Notes record: manifest forms accepted, connection URL that worked,
  menu path, UDT load path that worked, any fallback needed.
- **TDD:** no (spike)
- **Validation:** `npx tsx packages/premiere-mcp/src/spike-server.ts` → the two log lines above.
- **Depends on:** —
- [x] done
- Notes: **PASSED live 2026-08-21.** Panel connected from Premiere 26.3.2; all four checks green
  (echo round-trip, ping, and both eval probes). Full findings in
  [`docs/premiere/api-notes.md`](../docs/premiere/api-notes.md). Headlines:
  · **Plain `ws://localhost:7890` worked on default WSL2 NAT** — no mirrored networking, no
    direct-IP fallback, no firewall rule. Both `ws://localhost:7890` and `ws://127.0.0.1:7890`
    were accepted by the manifest validator.
  · **`new Function` runs in the UXP runtime**, async form included → T11's `premiere_eval` is
    viable as designed.
  · **`VideoFilterFactory.getMatchNames()` returned 106 effects** — the automation premise is
    proven end to end: we enumerated Premiere's effects from WSL.
  · 🔴 **`ppro.Application.version` returns `null`** (the plan's tool table specified it). Use
    `require('uxp').host.version` instead — verified returning `26.3.2`. **Fix in T5/T6 before
    `premiere_status` ships.**
  · `require('premierepro')` exposes 70 keys; `VideoFilterFactory`, `SequenceEditor`,
    `EncoderManager`, `Exporter`, `TickTime` all present.
  · Manual steps are written up for Jack in [`docs/premiere/setup.md`](../docs/premiere/setup.md).

### T2: Package scaffold + panel build   [Status: DONE 2026-08-21 — panel half landed with T5 | Model: sonnet]
- **Scope:** Turn the spike into the real package layout. Full `package.json` (scripts
  `start`, `typecheck`, `test`, `build:panel`, `build:panel:watch`; deps per File Structure),
  `tsconfig.json`, `tsconfig.panel.json`, `src/index.ts`, `src/version.ts`, `src/result.ts`, `README.md` stub,
  `scripts/build-panel.ts` (esbuild `panel/src/main.ts` → `panel/dist/main.js`, cjs, externals
  `premierepro`/`uxp`/`os`/`fs`; copy `manifest.json`, `index.html`, `icons/`; **no mirror step yet** —
  T3 adds it once `config.ts` exists; until then UDT loads `panel/dist/` by whatever path T1 proved),
  `.mcp.json` entry, workspace wiring. Move the spike's `main.js` logic into `panel/src/main.ts`
  unchanged in behaviour and delete `panel/main.js` and `src/spike-server.ts`.
- **Files:** create/modify as listed; `panel/icons/*.png` (plain 23/46/48 px placeholders).
- **Acceptance criteria:** `npm install` at root succeeds; `npm run typecheck --workspace
  @badcode/premiere-mcp` passes; `npm run build:panel --workspace @badcode/premiere-mcp` produces
  `panel/dist/{main.js,manifest.json,index.html,icons/}`; UDT loads the built panel and the T1
  round-trip still works; `npm run typecheck` at root still passes.
- **TDD:** no (wiring)
- **Validation:** `npm run typecheck --workspace @badcode/premiere-mcp && npm run build:panel --workspace @badcode/premiere-mcp && ls packages/premiere-mcp/panel/dist`
- **Depends on:** T1
- [x] done
- Notes: **Split deliberately, both halves now landed.** The non-panel half was done 2026-08-21:
  full `package.json`, `tsconfig.json`, `src/{index,version,result}.ts`, root `npm install`
  (`@adobe/premierepro` 26.3.0 resolved).
  **The panel half was deferred on purpose** — the T1 spike panel was staged at
  `D:\badcode-videos\_bridge\panel\` and Kai was about to load that exact copy into Premiere,
  so rebuilding it mid-setup would have broken his install. It landed with T5:
  `panel/src/main.ts`, `scripts/build-panel.ts`, `tsconfig.panel.json`, `panel/dist/` + its
  mirror, the `.mcp.json` `premiere` entry, `packages/premiere-mcp/README.md`; `panel/main.js`
  and `src/spike-server.ts` deleted, and `docs/premiere/setup.md` repointed off the spike.
  Findings recorded in `docs/premiere/api-notes.md` (§Building the panel) — the short version is
  that the plan's `format: 'cjs'` works **only because `main.ts` exports nothing**, and that a
  rebuilt panel does not reload itself.

### T3: `config.ts` + `paths.ts`   [Status: DONE 2026-08-21 | Model: sonnet]
- **Scope:** Implement the Interfaces exactly: `loadConfig` (file + env, `NO_MEDIA_ROOT` /
  `BAD_CONFIG`), `storyLayout`, `panelMirrorDir`, `toWindows`, `toWsl`, `isUnderRoot`. Pure
  string logic; no `wslpath` shell-out. Then extend `scripts/build-panel.ts` to mirror `panel/dist/`
  to `panelMirrorDir(cfg)` when config loads (skip with a notice when it doesn't).
- **Files:** `src/config.ts`, `src/config.test.ts`, `src/paths.ts`, `src/paths.test.ts`, `scripts/build-panel.ts`.
- **Acceptance criteria:** the example table in Interfaces → Paths is the test table, plus:
  mixed-case drive letters, trailing separators, spaces in paths, UNC round-trip, env override
  precedence, missing file → `NO_MEDIA_ROOT` with a hint naming `badcode.local.json.example`.
- **TDD:** yes
- **Validation:** `npm test --workspace @badcode/premiere-mcp -- paths config` → all green.
- **Depends on:** T2
- [x] done
- Notes: 37 tests (25 paths + 12 config), green; typecheck green; both re-run by the orchestrator.
  Live-checked against the real root: `/mnt/d/badcode-videos/…` ⇄ `D:\badcode-videos\…`
  round-trips exactly, `/home/kai/…` gets the UNC form + "outside media root" warning, and the
  sibling-prefix trap (`D:\badcode-videos-old`) correctly reads as NOT under the root.
  **Deferred from this ticket:** the `scripts/build-panel.ts` mirror step (T3's scope per the plan)
  moves with the rest of the panel work — see T2's note.

### T4: `protocol.ts` + `bridge.ts`   [Status: DONE 2026-08-21 | Model: sonnet]
- **Scope:** The envelope types and zod schemas for every command in the tool table (args and
  results, including `SequenceState`); the `Bridge` class per Interfaces: hello handshake,
  id correlation, FIFO serialisation, per-command timeout, connect-wait, disconnect-mid-command
  rejection, `log` frames forwarded to stderr. Tests use a real `ws` client in-process as a fake
  panel.
- **Files:** `src/protocol.ts`, `src/protocol.test.ts`, `src/bridge.ts`, `src/bridge.test.ts`.
- **Acceptance criteria:** two concurrent `send()`s are delivered strictly one after the other;
  a slow command times out with `TIMEOUT` and the next command still runs; `send()` before any
  panel connects waits `connectWaitMs` then rejects `PANEL_NOT_CONNECTED`; a second panel
  connecting replaces the first (old socket closed with reason `superseded`); malformed frames
  are logged and ignored; every schema round-trips a fixture.
- **TDD:** yes
- **Validation:** `npm test --workspace @badcode/premiere-mcp -- protocol bridge`
- **Depends on:** T3
- [x] done
- Notes: 56 tests (42 protocol + 14 bridge, real `ws` client as the fake panel), green.
  **Real bug found and fixed during implementation, worth keeping:** on supersede, a command in
  flight on the OLD socket never settled. The naive `if (this.socket !== ws) return` guard in the
  close handler ignores it, because by the time `close` fires `this.socket` already points at the
  NEW connection — so the caller hung until its own timeout. Fixed by failing the pending command
  explicitly in `onConnection()` before swapping the socket reference (`bridge.ts:115–121`).
  Judgement calls accepted: timeout/connectWait defaults implemented as real runtime defaults
  (the plan documented them as comments); no `.strict()`/`discriminatedUnion` on the zod schemas,
  matching flow-mcp's house style.

### T5: Panel runtime   [Status: DONE 2026-08-21 | Model: sonnet]
- **Scope:** `panel/src/main.ts` (connect/reconnect with exponential backoff capped at 10 s,
  hello, dispatch table, per-command try/catch → `Result` with `PanelError` codes or
  `PANEL_ERROR`, UI: light, URL field persisted in `localStorage`, log) and
  `panel/src/ppro.ts` (all helpers in Interfaces, including `dumpSequence` producing the raw
  shape `normalise.ts` will consume). Register a `ping` command returning
  `{ appVersion, project?: name, sequence?: name }`.
- **Files:** `panel/src/main.ts`, `panel/src/ppro.ts`, `panel/src/commands/index.ts` (the table), `src/smoke-status.ts`.
- **Acceptance criteria:** with the server up, the panel auto-connects on load and after a
  server restart; `Bridge.send('ping')` from a tsx script returns within 1 s; killing the server
  flips the light and the panel reconnects when it returns; unknown command → `INVALID_ARGS`.
- **TDD:** no (cannot unit-test inside UXP; `smoke-status.ts` is the check)
- **Validation:** `npm run build:panel --workspace @badcode/premiere-mcp && npx tsx packages/premiere-mcp/src/smoke-status.ts` → prints the ping result.
- **Depends on:** T4
- [x] done
- Notes: **PASSED live 2026-08-21.** Panel 0.2.0 connected, `ping` answered, an unregistered
  command came back `INVALID_ARGS` as designed. T2's deferred panel half landed here (see T2).
  Findings in `docs/premiere/api-notes.md` §Building the panel.
  **One acceptance criterion missed by design, not by accident:** "ping returns within 1s" was
  measured at 51s. That is the *connect wait* — the panel had to be reloaded first — not the
  round trip. Once connected, calls answer in milliseconds. The criterion should have said
  "within 1s of the panel being connected".
  Judgement call: `dumpSequence` takes an optional `{ params: false }` so a Lumetri-heavy
  sequence can skip the expensive walk. Cost not yet measured — do that in T7.

### T6: Status + project tools   [Status: DONE 2026-08-21 | Model: sonnet]
- **Scope:** `server.ts` skeleton (stdio MCP, `ok/fail/toToolError` as flow-mcp, config + bridge
  lifecycle) and the tools `premiere_status`, `premiere_open_project`, `premiere_save`,
  `premiere_import`, `premiere_list_items`, with their panel handlers in
  `panel/src/commands/project.ts`. `open_project` creates `<root>\<story>\` (+ `renders\`,
  `frames\`) via `importFiles`-independent means — the panel has no fs for that, so **the server
  creates the directories through `/mnt/c`** before asking the panel to create/open the project.
- **Files:** `src/server.ts`, `panel/src/commands/project.ts`, `src/smoke-project.ts`.
- **Acceptance criteria:** `premiere_open_project({story:'gitpush-origin-master'})` creates the
  project on first call (`created: true`) and opens it on the second (`created: false`);
  `premiere_import` with a `/mnt/c/...` path and a bin name puts the clip in that bin and
  returns its id; `premiere_list_items` shows it with a WSL `mediaPath`; a missing config →
  `NO_MEDIA_ROOT` with hint from every tool except `premiere_status`, which reports `mediaRoot: null`;
  panel closed → `PANEL_NOT_CONNECTED` with the menu-path hint from T1.
- **TDD:** no (live-only); server helpers that are pure (`toToolError` mapping) get a test.
- **Validation:** `npx tsx packages/premiere-mcp/src/smoke-project.ts` → prints created/opened, item list.
- **Depends on:** T5
- [x] done
- Notes: **PASSED live 2026-08-21 — 22/22 checks.** The smoke drives the REAL MCP server over
  stdio rather than the bridge directly, so config gating and path translation are exercised too.
  **Scope added at Kai's request mid-ticket:** `premiere_open_project` now takes `path` (any
  `.prproj` anywhere) as well as `story`, and `frames\`/`renders\` follow the project rather than
  the media root. See the AMENDED block in Decision 2. `premiere_save` / `premiere_import` /
  `premiere_list_items` no longer require a media root — they never used it.
  **Two Premiere bugs cost this ticket a full run each**, both now in `api-notes.md`:
  `Project.isProject()` is not an existence check, and `Project.open()` rejects with a bare
  string *even when it succeeds*. `premiere_eval` was pulled forward from T11 to diagnose them.
  Known wart: re-running the smoke re-imports the same clip, so the test project accumulates
  duplicates. Harmless; the project is a scratch artifact.

### T7: Sequence tools + `normalise.ts`   [Status: DONE 2026-08-21 | Model: sonnet]
- **Scope:** `premiere_create_sequence`, `premiere_list_sequences`, `premiere_set_active`,
  `premiere_get_sequence`; `panel/src/commands/sequence.ts`; `dumpSequence` completed (tracks,
  items, component chains with params and keyframes, transitions, markers);
  `src/normalise.ts` turning the raw dump into `SequenceState` (seconds, refs, labels, WSL paths).
  Capture two real dumps (empty sequence; sequence with two clips + Motion/Opacity intrinsics)
  as fixtures for the tests.
- **Files:** `panel/src/commands/sequence.ts`, `src/normalise.ts`, `src/normalise.test.ts`,
  `src/fixtures/dump-*.json`, `src/smoke-sequence.ts`; **creates** `docs/premiere/api-notes.md`
  (T9–T12 append; T13 consolidates).
- **Acceptance criteria:** `get_sequence` on a sequence with two clips returns refs `v0:0`,
  `v0:1`, correct start/end/in/out in seconds, the intrinsic components (record their
  matchNames in `docs/premiere/api-notes.md`), and `mediaPath` in `/mnt/c/…` form; `normalise`
  is total (never throws on a partial dump; missing fields → nulls).
- **TDD:** yes for `normalise.ts`
- **Validation:** `npm test --workspace @badcode/premiere-mcp -- normalise && npx tsx packages/premiere-mcp/src/smoke-sequence.ts`
- **Depends on:** T6
- [x] done
- Notes: **PASSED live 2026-08-21 — smoke green, 129 unit tests green.**
  **The fixtures are REAL captured Premiere output, not hand-written.** `SMOKE_CAPTURE=1` makes
  `smoke-sequence.ts` pull the raw dump straight out of Premiere via `premiere_eval` and overwrite
  `src/fixtures/`. The first pass of `normalise.test.ts` was written against hand-made fixtures and
  ten of its assertions failed the moment real data replaced them — which is precisely the point.
  Anything Premiere did not hand us on that run (transitions, keyframes, markers, malformed dumps)
  is exercised with inline objects instead; **do not hand-edit the fixtures to add them.**
  `dump-two-clips.json` → `dump-one-clip.json`: the plan assumed two clips, and
  `createSequenceFromMedia` on a single video-only source lays down one.
  **Three findings that change T10**, all in `api-notes.md`: `getValueAtTime()` returns a
  `{ value: … }` **wrapper**, not the value its declaration promises (fixed in `plainValue`);
  `PointF` params are **normalised 0–1 arrays**, not `{x,y}` pixels; and display names are
  **neither unique nor always present** (`AE.ADBE Opacity` has two params called "Blend Mode";
  `AE.ADBE Motion` param 3 is named `" "`) — **the index is the authoritative address.**
  Param-walk cost measured at 13ms vs 15ms, i.e. noise on a one-clip sequence: `params: false`
  is kept but is not a performance need. Re-measure on a Lumetri-graded cut before trusting it.
  A smoke assertion — not the code — was wrong about audio: the test clip is a Flow render with
  no audio stream at all. `src/smoke-client.ts` was extracted here so T8–T12 do not each re-grow
  the harness.

### T8: Edit tools   [Status: DONE 2026-08-21 | Model: sonnet]
- **Scope:** `premiere_insert_clip`, `premiere_move_clip`, `premiere_trim_clip`,
  `premiere_remove_clip`, `premiere_clone_clip`; `panel/src/commands/clips.ts`. Each is one
  transaction and returns the refreshed state.
- **Files:** `panel/src/commands/clips.ts`, `src/smoke-edit.ts`.
- **Acceptance criteria:** on a fresh sequence: overwrite clip A at 0, insert clip B at 0
  (A shifts), move B by +2 s, trim A's out point by −1 s, clone A at +10 s, remove the clone
  with ripple — after each call the returned state matches what Premiere's timeline shows
  (verified by eye once, then by the state's numbers); a stale ref → `CLIP_NOT_FOUND`; each
  step is one entry in Edit ▸ Undo labelled `BadCode: …`.
- **TDD:** no (live-only)
- **Validation:** `npx tsx packages/premiere-mcp/src/smoke-edit.ts` → prints the state after each step and asserts the expected start times.
- **Depends on:** T7
- [x] done
- Notes: **PASSED live 2026-08-21 — 24/24 checks.**
  **Two Premiere behaviours found here, both in `api-notes.md`, both load-bearing:**
  · 🔴 **`TrackItemSelection.createEmptySelection()` — the API this ticket specified for
    `remove_clip` — is unusable.** Every native call against the object it yields throws "The
    script object is no longer valid", including synchronously inside its own callback. Isolated
    before concluding (the clip handles alongside it were fine). Replaced with
    `sequence.clearSelection()` + `sequence.getSelection()`, verified removing a real clip.
  · 🔴 **Every edit snaps to a frame boundary** — 4.0s becomes 4.004 at 23.976 fps. The ticket's
    acceptance criteria ("asserts the expected start times") were written assuming exact times,
    which makes exact-equality assertions *wrong* rather than strict. **`frameRate` added to
    `SequenceState.sequence`**, derived from `timebase`, because no caller can predict where a
    clip lands without it; the smoke compares within half a frame.
  Also recorded: a zod violation surfaces as an MCP protocol error (`-32602`), not as our
  `{ error, code, message, hint }` shape — anything parsing tool results must handle both.
  **One acceptance criterion is NOT machine-verified and cannot be:** "each step is one entry in
  Edit ▸ Undo labelled `BadCode: …`". Premiere exposes no undo-history API. The code does it (one
  `executeTransaction` per call, labelled); confirming it needs a human looking at the Edit menu.
  The smoke says so rather than quietly skipping it.

### T9: Transitions, markers, playhead   [Status: done | Model: sonnet]
- **Scope:** `premiere_list_transitions`, `premiere_add_transition`,
  `premiere_remove_transition`, `premiere_add_marker`, `premiere_set_playhead`;
  `panel/src/commands/transitions.ts`, `panel/src/commands/markers.ts`. Record the Cross
  Dissolve / Dip to Black match names in `api-notes.md`.
- **Files:** as above + `src/smoke-transitions.ts`.
- **Acceptance criteria:** a 1 s cross dissolve lands at the cut between `v0:0` and `v0:1` and
  shows in `get_sequence` under both clips' `transitions`; unknown matchName →
  `TRANSITION_NOT_FOUND` with three nearest names; a marker at 3 s with a comment appears in
  state; `set_playhead` moves the program monitor.
- **TDD:** no
- **Validation:** `npx tsx packages/premiere-mcp/src/smoke-transitions.ts`
- **Depends on:** T8
- [x] done
- Notes:
  - **Acceptance criteria amended mid-ticket, with cause.** "…and shows in `get_sequence` under
    both clips' `transitions`" is **not achievable**: `getTrackItems()` hands back `null` for
    every item that is not a CLIP, so a transition can be counted and never read. Proven three
    ways — the array length tracks additions exactly (0 → 1 → 2) while every element is null;
    and the transition itself was read out of the saved `.prproj` (gzipped XML) with its match
    name, its 3.545–4.505s span and `HasOutgoingClip/HasIncomingClip`. **The write half works;
    only the read is gone.** Full detail in `api-notes.md`.
  - **`SequenceState` gained `transitionCount` per track** — the only transition information the
    API will part with. Per-clip `transitions` is kept in the schema, always empty, so it lights
    up for free if Adobe ever fixes the marshalling.
  - **`add_transition` verifies itself by comparing that count before and after**, because
    `executeTransaction` returning `true` is not proof (see `Project.open`, T6).
  - **A latent T8 crash fixed:** one unfiltered null broke `dumpSequence` and therefore *every*
    tool returning a state, `move_clip` included. It only surfaced once a transition existed.
  - **No handles is NOT a refusal** — Premiere writes a single-sided transition (frame-hold),
    and will happily add one across a gap. The smoke asserts this; the original assumption in
    this ticket was wrong.
  - **There is no audio transition API whatsoever.** `premiere_add_transition` is video-only,
    enforced at the schema. Audio crossfades stay manual.
  - **`inPoint` and `start` cannot go in one `trim_clip` call** — Actions in a CompoundAction all
    compute against the pre-transaction state, so they fight. Trim, then move.
  - `alignment` is a **fraction** (0.5 = centred), not an enum.
  - Match names recorded: Cross Dissolve = `AE.ADBE Cross Dissolve New`, Dip to Black =
    `AE.ADBE Dip To Black`. 118 video transitions on this install; the catalogue mixes `AE.ADBE`
    and bare `ADBE` prefixes, so always resolve via `premiere_list_transitions`.
  - New shared `src/nearest.ts` (+17 unit tests) powers the "did you mean" tail on
    `TRANSITION_NOT_FOUND`; T10 gets `EFFECT_NOT_FOUND` from it free.
  - Panel helpers `withAction`/`withActions`/`numArg`/`intArg`/`strArg` hoisted out of `clips.ts`
    into `ppro.ts` — one copy, used by all command modules.
  - **Smoke: 26/26 green.** Gates: root typecheck clean, 152 unit tests green.
  - 🔴 **Panel rebuilt after the smoke** (one error message reworded once its stated cause was
    disproved). Needs ⋯ → Load before T10's smoke — which rebuilds anyway.

### T10: Effects tools   [Status: done | Model: opus]
- **Scope:** `premiere_list_effects`, `premiere_describe_effect`, `premiere_apply_effect`,
  `premiere_set_param`, `premiere_remove_effect`; `panel/src/commands/effects.ts`. Resolve the
  open question in the tool table: can an un-inserted `VideoFilterComponent` report its params?
  If not, `describe_effect` requires `clip` and reads the applied instance — document the ruling
  in `api-notes.md`. Params addressable by index or display name; values typed per
  `ComponentParam.createKeyframe` (`number | string | boolean | PointF | Color`). `protocol.ts` validates
  plain `{x,y}` / `{r,g,b,a?}` objects (it cannot construct ppro types); the panel wraps them into
  `PointF` / `Color`. Record Lumetri Color and Gaussian
  Blur match names and their param indices in `api-notes.md`.
- **Files:** `panel/src/commands/effects.ts`, `src/smoke-effects.ts`.
- **Acceptance criteria:** `list_effects({query:'blur'})` includes Gaussian Blur;
  `apply_effect(v0:0, <GaussianBlur>, {Blurriness: 20})` shows in state with value 20;
  `set_param(v0:0, <GaussianBlur>, 'Blurriness', 0, time: 0)` then `(…, 40, time: 2,
  interpolation:'bezier')` yields two keyframes in state; Motion → Scale 120 via the intrinsic
  works through the same tools; `remove_effect` removes it; unknown effect →
  `EFFECT_NOT_FOUND` with nearest display names.
- **TDD:** no (live); value-coercion helper in `protocol.ts` gets a unit test.
- **Validation:** `npm test --workspace @badcode/premiere-mcp -- protocol && npx tsx packages/premiere-mcp/src/smoke-effects.ts`
- **Depends on:** T8
- [x] done
- Notes:
  - **Open question answered: an un-inserted `VideoFilterComponent` has NO METHODS AT ALL** — its
    prototype is a bare `constructor`, so `getParamCount`/`getParam`/`getMatchName` are all "not a
    function". It is an opaque token for `createAppendComponentAction` and nothing else.
    **`describe_effect` therefore requires `clip`**, and its signature became
    `{ clip, component }` (`component` for consistency with `set_param` / `remove_effect`).
  - **Forced deviation: `apply_effect` is TWO transactions, not one.** Issue #7 again — a param
    cannot be addressed until the append has committed, and the token has no params to address.
    Same for keyframing: `createSetTimeVaryingAction` must commit before `createAddKeyframeAction`.
    Two `BadCode:` undo entries; the tool description says so.
  - 🔴 **33 of Lumetri Color's 130 params are unreadable by every available route.**
    `getValueAtTime` throws and recommends `getKeyframePtr`, which returns null or throws
    "Illegal Parameter type"; `getStartValue()` returns null. Stable across re-reads and edits.
    They can still be **written**. `Param` now carries `unreadable: true` with `value: null`, and
    keeps the real display name.
  - **The T7 cost caution is retired.** Measured on a Lumetri-graded clip: 181 params in 49ms
    versus 3ms with `params: false`. Cheap. `params: false` matters only on a large graded cut.
  - **Display names collide across effect generations:** "Gaussian Blur" is `AE.Impact_Blur_FX`
    (20 params, mostly internal, real control at index 5 "Amount"); "Gaussian Blur (Legacy)" is
    `AE.ADBE Gaussian Blur 2` (3 clean params, Blurriness defaults to 25). **Prefer the legacy
    effect for automation.** Both accepted — `apply_effect` resolves match name or display name.
  - **Lumetri's useful param indices recorded in `api-notes.md`.** Saturation, Intensity, Look
    and Input LUT each appear TWICE at different indices; `resolveParam` refuses an ambiguous
    name rather than guessing.
  - **Point values write the way they read** — `{x,y}` 0–1 fractions of the frame, back as
    `[x, y]`. Keyframes behave exactly as declared (`Keyframe.position` is settable).
  - **The intrinsics are protected** — `remove_effect` refuses Opacity and Motion with an
    explanation rather than a failing action.
  - **A bug caught by fixing a vacuous test:** `normaliseParam` silently dropped `unreadable`,
    and three `every()`-on-empty-array checks all passed, reporting "0 unreadable". The checks
    now assert non-emptiness first. Worth remembering across the remaining tickets.
  - **Smoke: 41/41 green.** Gates: root typecheck clean, 155 unit tests green.

### T11: MOGRT + `premiere_eval`   [Status: pending | Model: sonnet]
- **Scope:** `premiere_insert_mogrt` (`panel/src/commands/mogrt.ts`; runs under `lockedAccess`
  only — see the tool table) and `premiere_eval`
  (`panel/src/commands/eval.ts`): `new Function('ppro','helpers','log', code)`, async-aware
  (`await` allowed by wrapping in `(async () => { ${code} })()`), captured logs, JSON-safe
  result, `EVAL_ERROR` with stack. Server-side `timeoutMs` default 60 s.
- **Files:** as above + `src/smoke-mogrt-eval.ts`.
- **Acceptance criteria:** a `.mogrt` from `SequenceEditor.getInstalledMogrtPath()` inserts at
  5 s on V2 and appears in state; `eval` returning `await (await helpers.activeSequence()).name`
  yields the name; a throwing snippet yields `EVAL_ERROR` with the message.
- **TDD:** no
- **Validation:** `npx tsx packages/premiere-mcp/src/smoke-mogrt-eval.ts`
- **Depends on:** T7
- [ ] done
- Notes:

### T12: Export frame + export sequence   [Status: done | Model: sonnet]
- **Scope:** `premiere_export_frame`, `premiere_export_sequence`;
  `panel/src/commands/export.ts`. Server creates `frames\` / `renders\` if missing, computes
  default output names, runs the export with a 600 s timeout, polls the output file through
  `/mnt/c` until its size is stable for 2 s, then `ffprobe`s it for `durationSeconds`. Record
  in `api-notes.md` whether `exportSequence(IMMEDIATELY)` resolves on completion or on queueing.
- **Files:** as above + `src/smoke-export.ts`.
- **Acceptance criteria:** `export_frame({time: 1.5})` returns a PNG path that `Read` opens and
  that matches the program monitor at 1.5 s; `export_sequence()` on a 6 s sequence returns an
  `.mp4` whose `ffprobe` duration is 6.0 ± 0.05 s; outputs are under `<root>\<story>\…`; an
  `outPath` outside the root → `INVALID_ARGS`.
- **TDD:** no
- **Validation:** `npx tsx packages/premiere-mcp/src/smoke-export.ts && scripts/video-contact-sheet.sh <printed render path>`
- **Depends on:** T8
- [x] done
- Notes:
  - **Open question answered: `exportSequence(IMMEDIATELY)` resolves on COMPLETION**, not on
    queueing. 6s of video rendered in 1.3s with the finished MP4 behind the promise. No job to
    poll, no queue to watch.
  - 🔴 **But both exports resolve BEFORE the file finishes being written.** Measured: the frame
    promise resolved at 8394ms, the file appeared at 8498ms holding 672KB, and settled at 8704ms
    at 831KB. Reading on resolution yields ENOENT or — worse — a truncated file that still opens.
    `waitForStableFile()` waits for existence then for a steady size (1.5s frame / 2s render);
    both tools report `bytes`. **The plan's instinct to poll was right for the wrong reason.**
  - **Acceptance criterion amended:** "an `outPath` outside the root → `INVALID_ARGS`" was
    dropped. It contradicts the amended Decision 2 (media root is a default, not a cage) and
    Kai's ruling that projects live anywhere. An explicit `outPath` is the caller being specific
    and is honoured wherever it points. Format and preset existence ARE still validated.
  - **`exportSequenceFrame` takes directory and filename separately** — a full path in
    `filename` does not work. The directory must pre-exist; failure is a bare `false`.
  - **Neither export is an Action** — no transaction, no `BadCode:` undo entry. Correct: they
    write files, they do not change the project.
  - **Visual proof of the `createSequence` trap:** the first exported frame showed the picture
    inset in black, because the source is 1280x720@25 and the default sequence is 1920x1080@23.976.
    Confirms the T8 note with pixels. **Use `create_sequence({ fromItems })` to match footage.**
  - **Premiere adds a silent AAC track** to a render even when the source is video-only.
  - **Duration is measured with ffprobe on the finished file**, never assumed. A 6s timeline
    reported 6.037s — 6s plus one frame at 23.976, exactly right.
  - **Smoke: 30/30 green**, and the exported PNG was opened and looked at, closing the "matches
    the program monitor" criterion. Gates: root typecheck clean, 155 unit tests green.

### T13: Docs — setup, protocol, api-notes, README   [Status: DONE 2026-08-21 | Model: opus]
- **Scope:** Write `docs/premiere/README.md`, `docs/premiere/setup.md` (UDT install from the
  Creative Cloud app, developer mode in UDT and Premiere, loading `<MEDIA_ROOT>\_bridge\panel\
  manifest.json`, the exact menu path recorded in T1, the three networking fallbacks with the
  PowerShell/`.wslconfig` lines, choosing the media root and writing `badcode.local.json`, the
  export preset), `docs/premiere/bridge-protocol.md`, consolidate `docs/premiere/api-notes.md`
  from T7–T12 Notes, and finish `packages/premiere-mcp/README.md` (tool table mirrors
  `server.ts`; error table).
- **Files:** as listed.
- **Acceptance criteria:** a reader with a fresh Windows + WSL machine can follow `setup.md` to a
  green `premiere_status` without asking a question; every tool in `server.ts` appears in the
  README; every `ErrorCode` appears in the error table with a hint.
- **TDD:** no
- **Validation:** `test "$(grep -c 'registerTool(' packages/premiere-mcp/src/server.ts)" = "$(grep -c '^| `premiere_' packages/premiere-mcp/README.md)" && echo COUNTS-MATCH`; `npm run typecheck` at root passes.
- **Depends on:** T9, T10, T11, T12
- [x] done
- Notes: **Done 2026-08-21, and scoped wider than the ticket** at Kai's request — he asked for
  "every trick documented so it's easy when I mention in a thread, let's apply this clip to
  Premiere project", which is a cookbook, not just a reference.
  - `packages/premiere-mcp/README.md` — **all 27 tools** with arguments, grouped, with the traps
    inline. Validation passes: 27 `registerTool` calls, 27 table rows.
  - **`docs/premiere/recipes.md` (NEW, not in the plan)** — the cookbook. Build a cut, fill the
    frame, push in / pan / fade, dissolves, grade, the near-black look, Flow atmospherics, text
    without a MOGRT, markers, export and look, audit someone else's project, `jq` snippets for the
    state file, plus **"things that do not work, so you stop looking"** and the error table.
  - **`docs/premiere/effects-catalogue.md` (NEW, not in the plan)** — **106 effects and 118
    transitions harvested live from this install**, grouped by what a person would ask for, with
    the BadCode register (near-black, glitch, decay) called out and the absorbed Film Impact set
    mapped. An inventory, not research: if a name is in it, it is on the machine.
  - `docs/premiere/bridge-protocol.md` — frames, the five bridge rules, every error code, the
    tick/seconds and path conventions, and why the server is in WSL.
  - `docs/premiere/README.md` — reindexed, and the "two facts" section became four (the state-size
    contract and the active-sequence footgun).
  - `docs/premiere/api-notes.md` — three new sections this session: the camping hand-cut findings,
    the T21 fix, and the live-validation findings including the EADDRINUSE orphan.
  - **T11's MOGRT tool is still unbuilt**, and every doc says so rather than implying otherwise.

### T14: Media-root migration   [Status: pending | Model: sonnet]
- **Scope:** Move the existing scene folders under the root and update every reference.
  `mv /mnt/c/Users/kai/Desktop/gpom-s00 "<root wsl>/gitpush-origin-master/s00"` and `gpom-s01 →
  …/s01` (**ask Kai before moving; `final/` contents are irreplaceable renders**). Update
  `docs/stories/gitpush-origin-master/scenes/s00-awakening.md` (lines 303, 476, 588) and
  `s01-the-push.md` (line 17), and the scratch-folder convention in
  `.claude/skills/flow-automation/SKILL.md` (§"While you are working") to the new tree.
- **Files:** the two ledgers, the flow-automation skill.
- **Acceptance criteria:** `ls "<root wsl>/gitpush-origin-master/s00/final"` lists
  `s00v3-SEQUENCE.mp4`; `grep -rn "Desktop/gpom" docs .claude/skills` returns nothing; the
  flow-automation skill names `<MEDIA_ROOT>\<story>\<scene>\` and `…\final\`.
- **TDD:** no
- **Validation:** the two commands above.
- **Depends on:** T6 (root established)
- [ ] done
- Notes:

### T15: `premiere-automation` skill   [Status: DONE 2026-08-21 | Model: opus]
- **Scope:** `.claude/skills/premiere-automation/SKILL.md` mirroring `flow-automation`'s
  structure: what this is not (mechanics only — *what* to apply is `video-fx`), §1 get a working
  bridge (`premiere_status` result table → do), §2 the laws (serial; refs from the latest state;
  one transaction per call; exports under the root; look before you claim — `export_frame` /
  contact sheet after every visual change), §3 the loop (import → insert → frame → iterate), §4
  recovery (`PANEL_NOT_CONNECTED`, `TIMEOUT` = a modal in Premiere, forwarding broke after
  sleep), §5 the ledger's Premiere section template, §6 when to reach for `premiere_eval`.
- **Files:** the skill file.
- **Acceptance criteria:** frontmatter `description` lists the triggers ("import this into
  Premiere", "build the sequence", "the panel isn't connecting", "add a Premiere tool"); every
  tool named exists in `server.ts`; the skill tells the agent to bring the bridge up itself and
  only bounce to the user on the manual UDT step.
- **TDD:** no
- **Validation:** `comm -23 <(grep -o "premiere_[a-z_]*" .claude/skills/premiere-automation/SKILL.md | sort -u) <(grep -o "'premiere_[a-z_]*'" packages/premiere-mcp/src/server.ts | tr -d "'" | sort -u)` → empty output.
- **Depends on:** T13
- [x] done
- Notes: **Final pass done 2026-08-21.** §4 was stale (it still said T7–T12 were "landing") and now
  carries all 27 tools grouped, the summary-by-default reading contract, and pointers to the new
  `recipes.md` and `effects-catalogue.md`. Two laws added from live experience: **law 8** — every
  edit tool acts on the ACTIVE sequence and a human clicking another tab silently redirects your
  next call; **law 9** — do not drive Premiere while a human is using it. The error table gained
  the `EADDRINUSE` orphaned-server row. Validation passes: every `premiere_*` named in the skill
  exists in `server.ts` (`insert_mogrt` is named unprefixed, as not-yet-built).
  **Originally drafted 2026-08-21 at Kai's explicit request**, ahead of its T13
  dependency. His ask, in his words: when Premiere automation is not running, the skill should
  *detect the state and guide you through fixing it* — including the from-scratch UXP install —
  so Jack (or a future Kai who has forgotten) is walked through it rather than stuck.
  Delivered as §1: `premiere_status` first, always, mapping to **four distinct states**
  (connected / panel not answering / no media root / not installed), each with its own fix, plus
  which steps a session can do itself versus which need a human in Adobe's GUI.
  **Stays open** until T13, when the tool surface is complete — §4 currently says which tools
  exist today and which are still landing, and that has to be trued up.

### T16: Video-fx research sweep (Workflow, 20 Sonnet agents)   [Status: DONE 2026-08-21 | Model: sonnet]
- **Scope:** Run by the **orchestrating Claude Code session itself** (not a worker) using its
  `Workflow` tool — multi-agent orchestration Kai explicitly requested on 2026-08-21 ("a workflow
  with 20 Sonnet agents"). The script uses `agent(prompt, { model: 'sonnet', schema })` for the
  scouts/critic and `pipeline()` for the briefs. If `Workflow` is unavailable in the executing
  session, fall back to `Agent`-tool fan-out in batches of five with the same prompts and
  schemas. Briefs land in `design/research/2026-08-21-video-fx-landscape/`. Shape:
  - **Phase A — 2 scouts** (parallel): *Premiere & plugin ecosystem taxonomy* and *ffmpeg & CLI
    post taxonomy*. Each returns `{ categories: [{ key, title, why, suggestedQueries[] }] }`
    (schema-forced). The script merges them into exactly **18** brief assignments: the default
    list below, amended by the scouts' findings (a scout may split or merge categories, never
    exceed 18).
  - **Phase B — 18 brief writers** (pipeline, each independent). Default split **11 Premiere :
    7 ffmpeg**: `01-premiere-builtin-video-effects` · `02-transitions-essential-graphics-mogrt-titles`
    · `03-lumetri-colour-luts-film-looks` · `04-particles-fire-smoke-weather-vfx` ·
    `05-maps-motion-graphics-kinetic-text` · `06-premiere-ai-features-captions` ·
    `07-paid-suites-boris-redgiant-maxon-filmconvert-dehancer` · `08-free-plugins-and-template-ecosystem`
    · `09-after-effects-crossover-dynamic-link` · `10-speed-retime-stabilise-warp` ·
    `11-audio-ducking-denoise-narration-mix` · `12-ffmpeg-filter-map` · `13-ffmpeg-colour-lut-grain`
    · `14-ffmpeg-xfade-overlay-blend-chroma` · `15-ffmpeg-drawtext-subtitles-ass` ·
    `16-ffmpeg-zoompan-vidstab-minterpolate` · `17-ffmpeg-audio-filters` ·
    `18-ffmpeg-adjacent-frei0r-vapoursynth-mlt-gl-transition`.
    **Brief template (mandatory sections):** *What this covers* · *What's possible* (table:
    need → tool → how) · *Named tools* (each: what it is, **price/licence**, platform, install
    route, maturity) · *Automation hook* (Premiere: UXP match name if known or how to find it via
    `premiere_list_effects`; ffmpeg: command skeleton, tested flag or "untested") · *BadCode
    fit* (near-black register, 1376×768 Flow stills, 8 s clips) · *Traps* · *Sources* (≥5
    primary URLs, dated).
  - **Phase C — 1 critic**: reads all 18, returns `{ gaps: [{ topic, why, suggestedBrief }],
    contradictions: [] }` → logged to the README; the orchestrator decides whether to run a
    second small round.
  - The script `log()`s any brief that fails and never silently drops one; `README.md` lists
    every brief with a one-line summary and the critic's gaps.
- **Files:** `design/research/2026-08-21-video-fx-landscape/README.md`, `NN-<topic>.md` × 18.
- **Acceptance criteria:** 18 briefs present, each with all mandatory sections and ≥5 sources;
  every named paid tool carries a price; every Premiere-side entry carries a match name or the
  discovery instruction; README index + critic gaps written.
- **TDD:** no
- **Validation:** `ls design/research/2026-08-21-video-fx-landscape/*.md | wc -l` → 19; `grep -L "## Sources" design/research/2026-08-21-video-fx-landscape/[0-9]*.md` → empty.
- **Depends on:** — (starts immediately on approval, in parallel with T1)
- [x] done
- Notes: Ran as one Workflow, 21 agents, ~22 min, 2.24M subagent tokens. Validation re-run by the
  orchestrator: 19 files ✅ · all 18 briefs carry all 7 mandatory sections ✅ · none missing
  `## Sources` ✅. **Accepted deviation:** brief 15 has 4 source *URLs* plus 3 non-URL sources
  (`ffmpeg -h filter=drawtext` and `fc-list` run on this box) against a "≥5 primary URLs" bar —
  the local-execution sources are stronger evidence than a URL would be, so it passes.
  **False failure:** the workflow reported `17-ffmpeg-audio-filters` as failed; the agent hit the
  structured-output retry cap *after* writing a complete, 7-section, 7-source file. The critic
  caught this independently and corrected the README. Lesson for future sweeps: a schema-validation
  failure is not evidence the work wasn't done — check the artifact before re-running.
  Critic output (4 gaps, 4 price contradictions, 5 weak briefs) is in the Discovered Issues Log
  below and is **required input to T17**.

### T17: Distil `docs/video-fx/` + `video-fx` skill   [Status: PARTIAL 2026-08-21 — index shipped, per-lane pages and skill still pending | Model: opus]
- **Scope:** The orchestrating session (not a worker) reads the 18 briefs and writes the toolkit:
  `docs/video-fx/README.md` (the index: *need → lane → page*, the price-tier legend, the
  "toolkit-first → web-on-miss → record-back" rule), one page per lane group (`premiere-builtins.md`,
  `premiere-plugins.md` with price tags, `ffmpeg-recipes.md` extending but not duplicating
  `docs/flow/post-production.md`, `lane-choice.md` — the decision table: exactness → ffmpeg,
  real-time/plugin-only → Premiere, AE-only → flag), and `.claude/skills/video-fx/SKILL.md`
  (triggers: "add a fire effect", "zoom into the map", "make it black and white", "what plugin
  does X", "is there a tool for…"; procedure; the gate: it prices and documents, a human installs;
  how it hands off to `premiere-automation` / `premiere_eval` / ffmpeg; how it appends a new
  finding to the right page with a date).
- **Files:** as listed; modify `docs/flow/README.md` (one pointer line).
- **Acceptance criteria:** three dry-run requests resolved from the toolkit alone, with lane, tool,
  price and the first command/tool call named: (1) "fire in the server hall", (2) "push into a map
  of Tokyo", (3) "make s01 black and white with grain"; the skill's procedure never says
  "install"; each toolkit page cites its source briefs.
- **TDD:** no
- **Validation:** `ls docs/video-fx/` shows the five files; `grep -c "design/research/2026-08-21-video-fx-landscape" docs/video-fx/*.md` ≥ 1 per page.
- **Depends on:** T16
- [ ] done
- Notes: **`docs/video-fx/README.md` shipped 2026-08-21** — the highest-value slice: the
  **lane-choice table** (Flow invents / ffmpeg is exact / Premiere is the edit / AE is not
  installed), the no-paid-plugins ruling stated at the top as standing policy, the house answer for
  atmospherics (Flow on black → Luma Key), the index of all **20** briefs flagged as *raw research
  superseded by the ruling*, the toolkit-first→web-on-miss→record-back procedure, and the
  "what we deliberately don't own + the free route" table.
  **Still pending, and the file says so:** the four per-lane pages, and the `video-fx` skill.
  Two of them are arguably moot — the Premiere "which effect" question is answered better by the
  live `docs/premiere/effects-catalogue.md` than a distilled page would be, and ffmpeg recipes
  already live in `docs/flow/post-production.md` plus briefs 12–18. Reconsider the shape before
  writing them.

### T18: CLAUDE.md, docs index, flow docs pointers   [Status: DONE 2026-08-21 | Model: opus]
- **Scope:** Repo-map rows and two "How to work" bullets in `CLAUDE.md` (Premiere bridge;
  video-fx), index rows in `docs/README.md`, pointer line in `docs/flow/README.md` (if T17 did
  not already add it). Keep the voice and length of neighbouring bullets.
- **Files:** `CLAUDE.md`, `docs/README.md`, `docs/flow/README.md`.
- **Acceptance criteria:** every new path in File Structure that is user-facing
  (`packages/premiere-mcp`, `docs/premiere/`, `docs/video-fx/`, both skills) is reachable from
  `CLAUDE.md` in one hop.
- **TDD:** no
- **Validation:** `grep -n "premiere-mcp\|docs/premiere\|docs/video-fx\|premiere-automation\|video-fx" CLAUDE.md docs/README.md` shows all five.
- **Depends on:** T15, T17
- [x] done
- Notes: Done 2026-08-21. `CLAUDE.md` gained two repo-map rows (`docs/premiere/`,
  `packages/premiere-mcp`) plus one for `docs/video-fx/`, `premiere-automation` added to the skills
  row, and a full "Put something on a Premiere timeline" bullet under How to work — which names the
  27 tools, the cookbook, the live effects catalogue, and **the two facts that save the most time**
  (no tool returns a whole timeline; every edit tool acts on the active sequence).
  `docs/README.md` already carried its rows. Validation: all five names present in `CLAUDE.md`, and
  a link check across every touched doc shows **zero broken relative links**.

### T19: `smoke-e2e.ts`   [Status: pending | Model: sonnet]
- **Scope:** One live script composing every tool: open `gitpush-origin-master` → import
  `<root>\gitpush-origin-master\s00\final\*.mp4` into bin `s00` → create sequence `s00-e2e` →
  overwrite clips in name order → 1 s Cross Dissolve at each cut → Lumetri on `v0:0` (exposure
  −0.5) → Gaussian Blur keyframed 0→40 over the last clip → marker at 1 s → `export_frame` at
  the midpoint → `export_sequence` → `ffprobe` duration equals the sum of clip durations ±0.05 s
  → delete sequence `s00-e2e` via `premiere_eval` (`project.deleteSequence`) → save.
- **Files:** `src/smoke-e2e.ts`.
- **Acceptance criteria:** runs green end to end in under 5 minutes on the real project; leaves
  the project as it found it bar the imported bin.
- **TDD:** no
- **Validation:** `npx tsx packages/premiere-mcp/src/smoke-e2e.ts` → `E2E OK` + the render path; `scripts/video-contact-sheet.sh <render>` shows the dissolves and the blur.
- **Depends on:** T9, T10, T11, T12, T14
- [ ] done
- Notes:

### T20: End-to-end verification — a live GPOM scene-0 session   [Status: pending | Model: opus]
- **Scope:** Prove the feature as the user will use it. In a fresh session, invoke
  `premiere-automation` and, by conversation only: bring the bridge up from cold (Premiere
  running, panel loaded), build `s00` from the ledger's approved beats, place the narration
  stem on A1, add the cuts/dissolves the ledger calls for, ask `video-fx` for one effect the
  ledger implies (the near-black grain/vignette), apply it, export a frame and a render, look at
  both, write the ledger's **Premiere** section. Then run the repo gates.
- **Files:** `docs/stories/gitpush-origin-master/scenes/s00-awakening.md` (Premiere section).
- **Acceptance criteria:** the session completes without the human touching Premiere except to
  watch; the render exists under `<root>\gitpush-origin-master\renders\`; the ledger section is
  written; all gates pass.
- **TDD:** no
- **Validation:** `npm run typecheck && npm test --workspace @badcode/premiere-mcp && ./stack check` all green; `premiere_status` green; the render path opens.
- **Depends on:** T18, T19
- [ ] done
- Notes:

### T21: Make the state fit — digest, drill-down, state file   [Status: DONE 2026-08-21 | Model: opus]
- **Scope:** Approved by Kai on 2026-08-21 after issue #11, in his words: *"is it not a case of us
  writing scripts that can process that data before we dump it into the language model… reduce the
  data down to the essential signal?"* — plus the observation that **camping is the worst case we
  own**, so anything that copes with it copes with everything. Stop every state-returning tool
  handing a raw `SequenceState` to the caller. Instead: summarise by default, write the complete
  state to disk beside the project, let the caller drill into what it actually cares about, and
  make exceeding the transport cap structurally impossible.
  - `src/view.ts` (new): `buildView(state, selection)` → `SequenceView` (project, sequence, one
    line per track, totals); `Selection` = `{ tracks, clips, range, params }`; `diffStates` →
    `changed` (added / removed / modified, so `insert_clip` can report the ref it just made);
    `fitToBudget` → a five-rung degradation ladder that always fits and always says what it gave up
    and where to get it; `foldNoiseParams` → drops the blank-named duplicate channel slots.
  - `src/server.ts`: `sendAndView()` replaces `sendAndNormalise()` at all 13 call sites;
    `writeStateFile()` puts the untrimmed state in `<project dir>/.bridge/state-<sequence>.json`
    (Kai's ruling: beside the project, so it follows the project like `frames\` and `renders\`);
    `lastStates` caches the previous state per sequence GUID for the diff.
  - `premiere_get_sequence` gains `tracks` / `clips` / `range`; its description tells the caller
    that `statePath` exists and that `jq` over it is free.
- **Files:** `src/view.ts`, `src/view.test.ts`, `src/smoke-view.ts`,
  `src/fixtures/state-camping.json.gz` (the real 573KB camping state, gzipped to 12.5KB),
  `src/server.ts`; docs: `packages/premiere-mcp/README.md`, `docs/premiere/api-notes.md`.
- **Acceptance criteria:** the camping digest is under 2.5 KB against a 573 KB raw state; every
  selection a caller could plausibly make fits `DEFAULT_BUDGET`; a drill-down into the busiest
  track lists **all** its clips (not a truncated slice); the state file on disk holds every clip;
  a degraded response names `statePath` and the narrower call that would have kept the detail;
  `changed` reports the ref of an inserted clip.
- **TDD:** yes — `view.ts` is pure. **The fixture is real captured output, not hand-written**, per
  T7's lesson.
- **Validation:** `npm test --workspace @badcode/premiere-mcp && npm run typecheck` (both re-run,
  green: **189 tests**, up from 155); then `npx tsx packages/premiere-mcp/src/smoke-view.ts` live.
- **Depends on:** T7 (the state it summarises)
- [x] done
- Notes:
  - **PASSED live 2026-08-21** on a real cut built through the bridge end to end: imported 4 clips,
    created `gpom-s01` from the `HD 1080p 25 fps` preset, laid three clips on V1 and the narration
    on A1, scaled the 720p opener to fill, exported two frames and **looked at both**. Every
    response came back in the new shape, and the largest was a few kilobytes.
  - **The feature that mattered most works:** `insert_clip` returned
    `changed.added = [{ ref: "v0:0", … }]` — the ref of the clip it had just made, which the panel
    cannot report and which previously had to be guessed from a whole-timeline dump.
  - **Drill-down verified live:** `get_sequence({ tracks: ["V1"] })` expanded that track's three
    clips with every parameter, resolved the **uppercase UI label** to API index 0, and left the
    other five tracks as one-line summaries.
  - **Measured, not guessed.** Every trimming approach was sized against the real camping state
    before the design was chosen: dropping blank param slots → 289,633 bytes; dropping every
    intrinsic component → 64,281; `params: false` at the panel → 60,371. **All still over the
    cap.** Only summarising works, because 284 clips of bare scaffolding is 58 KB on its own.
    The digest is **1,772 bytes** and, crucially, is bounded by *track* count rather than clip
    count — so it does not grow with the edit.
  - **The ladder was instrumented rather than assumed.** For `tracks: ['v2']` (84 clips): 82,813
    bytes whole → 32,833 without params → 19,645 without effect chains. It lands on rung 2, keeps
    all 84 clips with their `componentCount`, and says so in `notes`. Rung 1 missing the budget by
    2,833 bytes is the kind of thing a guessed design gets wrong silently.
  - **The blank-slot fold moved out of `normalise.ts` on purpose.** Doing it upstream would have
    made the on-disk state lossy, and that file is meant to be ground truth. It happens in the
    view only, so a caller can still write to those param indices.
  - **This is a correctness fix, not just ergonomics.** An oversized result is refused *after* the
    panel commits, so the caller sees a failure for work that succeeded — exactly what happened
    with `set_active` on camping. With the ladder in place that cannot recur.
  - **Not yet live-validated:** the session's own MCP server holds the bridge port and was started
    before this code existed, so it is still running the old `server.ts`. Needs an MCP reconnect
    (or a smoke run with the port free) before this ticket can be checked off.
  - Judgement calls: uppercase track names are read as UI labels (`V3` → index 2) and lowercase as
    API indices (`v2`), so whichever form a caller copies from a previous result works;
    `MAX_CHANGED_DETAIL = 40` caps a ripple report; `DEFAULT_BUDGET = 30_000` characters
    (~12k tokens) against an observed refusal at 63,543.


---

## Discovered Issues Log


### 2026-08-21 · T5 · A rebuilt panel does not reload itself
Premiere keeps running the previously loaded bundle until someone presses **⋯ → Load** in UXP
Developer Tool. The symptom is not an error you would connect to the cause: the stale panel opens
the socket normally, so the port looks healthy, but its `hello` fails validation and the caller
gets `PANEL_NOT_CONNECTED`. (A stale panel that *does* handshake instead answers `INVALID_ARGS` to
commands it ought to know.) `bridge.ts` now detects "socket attached, handshake never completed"
and names the real fix; there is a regression test for it. **Every ticket from here on rebuilds
the panel, so every ticket needs the reload.**

### 2026-08-21 · T6 · `Project.isProject()` is not an existence check — cost one full run
It returns `true` for paths that do not exist, so the panel chose `Project.open` for a file that
was not there and Premiere threw a stackless `Failed to open the project`. Fixed by moving the
create-vs-open decision to the server, which can actually check the filesystem. Full write-up in
[`docs/premiere/api-notes.md`](../docs/premiere/api-notes.md).

### 2026-08-21 · T6 · Premiere returns extended-length paths
`project.path` is `\\?\D:\…`, which defeated every drive-letter match in `paths.ts` and passed
through translation untouched. `stripExtendedPrefix()` added, with tests.

### 2026-08-21 · T6 · `premiere_eval` pulled forward from T11
Diagnosing the above through the panel alone meant one guess per manual reload. `premiere_eval`
has no real dependency on T7–T10, so its panel handler and tool shipped early and turned the loop
into free live probing. T11 keeps `premiere_insert_mogrt` and the acceptance criteria for both.

### 2026-08-21 · T6 · Smoke scripts must not spawn servers via `npx`
`npx tsx …` adds two wrapper processes, and killing the wrapper leaves the node process holding
the bridge port — an `EADDRINUSE` landmine for the next run. Spawn `node_modules/.bin/tsx`
directly and close the transport explicitly.


(appended by executors during implementation)

### 2026-08-21 · T16 critic findings — must be resolved during T17

**Gaps (no brief covers these):**
1. **Delivery specs + QC scopes** — nothing covers what YouTube Shorts / TikTok / Instagram want
   (aspect, codec, bitrate) or how to check levels on a waveform/vectorscope before shipping.
   Brief 12 explicitly forward-references this content to briefs 13–18, which never deliver it.
   → T17 must either commission `19-delivery-specs-and-qc-scopes.md` or correct 12's promise.
2. **Beat-synced cutting** — BadCode shorts are cut to drum & bass, so "cut this to the beat" is a
   natural ask, and no brief covers onset/tempo detection or audio-reactive cutting. **Judged the
   most BadCode-relevant gap of the four.**
3. **MOGRT parameter automation via UXP** — briefs 02, 05 and 08 each independently raise, and each
   leave unresolved, whether the bridge can read/set a MOGRT's exposed Essential Graphics
   parameters. This blocks template-driven maps/charts/kinetic type specifically (plain-effect
   match-name automation is confirmed fine). **Answerable by us:** it is a live-introspection
   question — resolve it in T11 with `premiere_eval` and write the answer into `api-notes.md`.
4. **3D/extruded text without After Effects** — brief 09 correctly flags true 3D text as AE-only but
   never checks whether a bought MOGRT fakes it acceptably. Owner would be brief 05.

**Price contradictions (T17 must resolve or mark unresolved — never launder into the toolkit):**
- Dehancer Lite: brief 03 flags the vendor's own site as self-contradictory ($199 perpetual vs
  subscription-only); briefs 07 and 13 then each assert opposite licence models at the same price.
- Boris FX Sapphire: brief 04 gives figures ($545–985/yr, $1,865–3,075 perpetual); brief 07, same
  day, says the price is unpublished.
- Mocha Pro perpetual ceiling: $1,645 (brief 07) vs $1,095 (brief 09), same product, same day.
- CoreMelt tiers: brief 02's "V2 plugin pack" vs brief 07's "Lock & Load / Everything Bundle" —
  never reconciled as the same or different product lines.

**Weak briefs (re-verify before their claims reach `docs/video-fx/`):** 04 (ActionVFX +
ProductionCrate pricing pages both 403'd — prices rest on snippets), 06 (a "40%+ efficiency gain"
for Scene Edit Detection stated as fact but sourced to a vendor blog), 09 (UK After Effects price
from a search cache only), 10 (Mercalli and ReelSteady prices self-conflicting on the vendors' own
pages), 16 (lowest source count, sole citation for Topaz pricing).

**Standing rule this establishes for T17:** a price without a live vendor page is quoted as
"unconfirmed", never as a number. The toolkit's whole value is that Kai can trust the figure.

### 2026-08-21 · Kai's ruling after reading the sweep — NO PAID PLUGINS

> "We don't really need any paid plugins because they all sound far too advanced, and for smoke
> and fire we could use Flow anyway."

**Consequences, which T17 must implement:**
- `docs/video-fx/` is a toolkit for **the free stack**: Premiere built-ins (incl. the ex-Film
  Impact transitions Adobe absorbed into 25.5), Lumetri, MOGRTs, and ffmpeg. Paid tools are
  demoted to a single reference page — *what we deliberately don't own, and the free route we
  take instead* — not a priced catalogue threaded through every page.
- **This dissolves the price-contradiction problem entirely.** Every contradiction the critic
  found (Dehancer, Sapphire, Mocha Pro, CoreMelt) and every weak-brief price finding was about a
  paid tool. None of them now gate the toolkit. The "no unverified price" rule still stands for
  the one reference page, where the numbers are indicative only and labelled as such.
- **The named free route for atmospherics is Flow.** Fire, smoke, sparks: prompt the element on a
  black background in Flow, composite with a Screen blend (Premiere blend mode, or ffmpeg
  `blend=screen`). This is the house answer; `video-fx` must give it before it mentions buying
  anything. Stock-element libraries (Mixkit, Pexels, Videvo — free tiers) are the fallback.
- The gaps the critic found that are NOT about paid tools still stand and still need work:
  delivery specs/QC, beat-synced cutting, and MOGRT parameter automation.

### 6. `getTrackItems()` marshals only CLIP items — transitions are write-only (T9, 2026-08-21)

Every non-CLIP track item comes back as `null`. The array **length** is exact, the **contents**
are unreachable. Consequences: `SequenceState` reports a per-track `transitionCount` instead of
per-clip transition detail; `add_transition` verifies by count; `dumpSequence` filters nulls
(this was crashing every state-returning tool the moment a transition existed).

**Workaround exists and is proven, deliberately not built:** a `.prproj` is gzipped XML and
carries every transition in full. Costs a forced save on read. Revisit only if a real project
needs it — likely trigger is opening a hand-cut edit such as camping.

### 7. Actions in a CompoundAction do not compose (T9, 2026-08-21)

They are all computed against the state at the start of the transaction, not against each
other's results. `trim_clip({ inPoint: 1, start: 4 })` lands the clip at 5. Any pair of edits
where one's correct argument depends on the other must be **separate calls**. Worth re-reading
before T10 batches several `createSetValueAction`s into one transaction.

### 8. Adobe's own recommended fallback for unreadable params does not work (T10, 2026-08-21)

`getValueAtTime` on 33 of Lumetri's 130 params throws *"…Use GetKeyframeAtTime to get a keyframe
object at time"* — and `getKeyframePtr` returns `null` or throws "Illegal Parameter type", and
`getStartValue()` returns `null`. There is no route to those values. They remain writable.
Treat any Premiere error message that names an alternative API as a lead, not an instruction.

### 9. An `every()` assertion over an empty array passes (T10, 2026-08-21)

Three green checks were reporting on a list that was empty because a field had been dropped in
`normaliseParam`. The count check beside them caught it. **Any `every()`/`all` assertion in a
smoke must assert the collection is non-empty first** — the remaining tickets should be read
with this in mind.

### 10. Export promises resolve before the file is written (T12, 2026-08-21)

Both `exportSequenceFrame` and `exportSequence` resolve while the file is still being flushed —
around 300ms early for a still. The dangerous case is not the missing file but the **truncated
one that still opens**. Any future tool that produces a file through Premiere must wait for a
stable size, not for the promise.

### 11. `SequenceState` does not fit through MCP on a real project (camping, 2026-08-21)

**The first hand-cut project the bridge opened broke thirteen tools at once.**

`D:\badcode-videos\camping\camping vid Copy-test_1.prproj` — Jack's camping cut, 149 video and 135
audio clips across 12 tracks, 3m35s. Measured:

| Mode | Bytes |
| --- | --- |
| `params: true` (default) | **573,065** |
| `params: false` | **60,371** |

The MCP result cap is ~25k tokens. **Both modes exceed it.** `premiere_get_sequence` was refused
at 63,543 chars; `premiere_set_active` at 576,237. Because all thirteen state-returning tools go
through the one `sendAndNormalise()` door in `src/server.ts`, **none of them can be used on this
project** — `move_clip`, `insert_clip`, `apply_effect` and the rest included. Decision 3's promise
("every mutating tool returns the refreshed `SequenceState` so the session never needs a second
call") does not survive contact with a real timeline.

Worse, the refusal happens at the transport **after** the panel has committed the work: `set_active`
really did switch the sequence and the caller still saw an error. **A failed state-returning call is
not evidence the mutation failed.**

**Where the bytes are:** params are 81% of the payload, and `Internal Channel Volume Stereo` alone
is 4,455 of the 6,819 params — 33 per audio clip, indices 3–32 blank-named duplicates of the same
value (32 channel slots on a stereo clip). That single component is 65% of all params in the dump.

**Not fixed in this session — it needs a ticket and Kai's call on shape.** The candidates, cheapest
first: drop blank-named duplicate channel slots in `normalise.ts` (free, ~65% of params, no
information lost); make `params: false` the default; add a `tracks` / `range` filter so a caller
asks for the part of the timeline it is working on; and stop mutating tools returning a full state
by default (return the touched clips plus a summary, with the full state on request). Full
measurements in [`docs/premiere/api-notes.md`](../docs/premiere/api-notes.md) §"A real hand-cut
project".

### 12. Findings from the camping project that are NOT the size problem (2026-08-21)

All measured live, all written up in `api-notes.md`:

- **Audio effect match names are bare GUIDs.** Jack's Hard Limiter is
  `e0b23f05-f1a7-4ef7-9b50-7ec3e3002058`. This kills the `PR.ADBE.*` / `AE.ADBE.*` prefix rule
  recorded during planning — never pattern-match a match name.
- **The audio intrinsics, documented for the first time:** `Internal Volume Stereo` (Volume) and
  `Internal Channel Volume Stereo` (Channel Volume). `Level` is a **linear multiplier, not dB**.
- **`mediaPath` is reported for offline media.** 8 clips point at Jack's OneDrive on Jack's PC;
  Premiere reports the path regardless. Stat before trusting it; those clips will render Media
  Offline.
- 🟢 **The transitions wall did not bite.** Every track reported `transitionCount: 0` and the
  project XML agrees — Jack cut the whole thing with hard cuts. **The `.prproj`-XML workaround
  stays unbuilt**, as Kai ruled; camping did not need it after all.
- **`getSequences()` reports 1 sequence where the XML has 3 `<Sequence` nodes** — the API is right,
  the extra nodes are structural. Do not count XML nodes to predict the API.
- **Opening a project leaves no active sequence** (`active: false`). Name the sequence explicitly
  or `set_active` first.

### 13. An MCP reconnect orphans the old server on the bridge port (T21, 2026-08-21)

Reconnecting `premiere` from `/mcp` spawns a new server and **leaves the old one running**, still
holding `127.0.0.1:7890`. Every tool then fails with
`PANEL_ERROR: listen EADDRINUSE: address already in use`. Three generations were alive at once
here. Fix from WSL: `ss -lptn 'sport = :7890'` to find the holder,
`ps -eo pid,ppid,etime,cmd | grep premiere-mcp/src/server.ts` to see every generation, `kill -TERM`
all but the newest. The next call binds and the panel reconnects on its own backoff.

Recorded because **this is now the most likely reason a working bridge suddenly stops working**,
and the error names a port rather than the cause. Same hazard as the T6 note about `npx`; a
reconnect is just another route to it. Worth `premiere_status` detecting and naming one day.

### 14. Opening a project makes it Premiere's active project — and a human may then edit into it

Not a bug, but it cost a real hand cut. `premiere_set_active` on Jack's camping project during
T21's investigation left camping frontmost in Premiere; Kai then built the GPOM cut into it,
emptying the `camping` sequence in memory. The on-disk file was never saved and was byte-identical
throughout, and a 22:31 autosave (68KB against 108KB) is what exposed the divergence.

**The lesson for the skill:** a session that opens or activates a project has changed what the
human in front of Premiere is looking at. Say so, and prefer a scratch project over someone's real
one when only exercising tools. Camping was reopened read-only for measurement afterwards and the
`.prproj` is intact.

### 11. Binding the port at startup made every launched session fight for it (2026-08-22)

Tried, and reverted the next day. The bridge was made to `listen()` when the MCP server process
started, so the panel's light went green and stayed green through an idle session — fixing a real
complaint that a red light "looks broken".

The cost was much larger than the benefit. **Claude Code starts every server in `.mcp.json` at
session launch**, so four open sessions became four servers all grabbing port 7890, and three
collided before anybody had said the word "Premiere". Found live with four sessions open, the
holder seven minutes into an unrelated task.

**The bridge binds on first USE**, like Flow's browser. The panel's own wording carries the idle
state instead — `waiting for Claude…` rather than `disconnected` + a raw close code — which costs
nobody a port. `premiere_status` is what opens the bridge.

Second-order fix: the EADDRINUSE guidance in the skill, recipes and api-notes said *"kill all but
the newest tree"*, which is right for a self-orphaned server and **destructive when the holder is
another live session**. All three now require tracing the holder up to its `claude` process first,
and forbid killing a sibling session.
