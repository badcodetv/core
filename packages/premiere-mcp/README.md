# @badcode/premiere-mcp

MCP server that drives **Adobe Premiere Pro 2026** on the Windows host from a session running in
WSL — import, arrange, trim, transitions, any installed effect, keyframes, motion-graphics
templates, export a frame to look at and a render to check.

**Setting this up for the first time? → [`docs/premiere/setup.md`](../../docs/premiere/setup.md).**

## How it is wired

```
  WSL                                        Windows
  ┌──────────────────────────┐               ┌──────────────────────────┐
  │ Claude session           │               │ Premiere Pro 2026        │
  │   │ stdio (MCP)          │               │  ┌────────────────────┐  │
  │   ▼                      │   ws://       │  │ "BadCode Bridge"   │  │
  │ src/server.ts            │  localhost    │  │  UXP panel         │  │
  │ src/bridge.ts  (WS SERVER)│◀─────────────│  │  (WS CLIENT)       │  │
  └──────────────────────────┘               │  └────────────────────┘  │
                                             └──────────────────────────┘
```

A UXP plugin **cannot listen on a socket** — it can only dial out. That single fact decides the
whole topology: the server lives here in WSL, the panel is the client, and nothing is installed
on Windows except the panel itself.

## Prerequisites

1. `badcode.local.json` at the repo root with a `mediaRoot` (copy `badcode.local.json.example`).
   Every tool but `premiere_status` refuses to run without it.
2. The **BadCode Bridge** panel loaded in Premiere via UXP Developer Tool and open
   (Window ▸ Extensions (UXP) ▸ BadCode Bridge). Green light = connected.

## Building the panel

```bash
npm run build:panel --workspace @badcode/premiere-mcp          # once
npm run build:panel:watch --workspace @badcode/premiere-mcp    # while working on it
```

Bundles `panel/src/main.ts` → `panel/dist/main.js` (esbuild, CJS, with `premierepro` and `uxp`
left to UXP's own `require`), copies the statics, and mirrors the result to
`<mediaRoot>\_bridge\panel\` — the Windows path UDT loads from.

🔴 **A rebuild does not reload the panel.** Press **⋯ → Load** in UXP Developer Tool afterwards,
or Premiere keeps running the previous bundle. The symptom of forgetting is a panel that
connects happily and then answers `INVALID_ARGS` to commands it should know.

## Checking it end to end

```bash
npx tsx packages/premiere-mcp/src/smoke-status.ts
```

Brings the bridge up, waits for the panel, sends `ping`, prints the host version and what is
open. Every subsequent ticket adds its own `src/smoke-*.ts` alongside it.

## Tools

Ground truth is `src/server.ts` (each `server.registerTool(...)` call) — if this list and the
code disagree, the code wins; fix this file.

### All 27 tools

**27 `registerTool` calls in `src/server.ts`.** Args in `**bold**` are required.

#### Status & project

| Tool | Args | Returns |
| --- | --- | --- |
| `premiere_status` | — | `{ connected, appVersion?, project?, activeSequence?, mediaRoot, hint? }`. **The only tool that runs without config** — reports `mediaRoot: null` plus a hint rather than failing, so it is always the right first call |
| `premiere_open_project` | **`path`** *or* **`story`** | `{ project, created, sequences, framesDir, rendersDir }`. `path` = any `.prproj` anywhere, WSL or Windows form, no media root needed. `story` = `<mediaRoot>\<story>\<story>.prproj`. `frames/` and `renders/` always sit **beside the project file** |
| `premiere_save` | — | `{ path }` |
| `premiere_import` | **`paths[]`**, `bin?` | `{ items, bin? }`. Premiere's import API reports only success/failure, so the bin is diffed before and after to work out what arrived |
| `premiere_list_items` | `bin?` | `{ items }` — clips, bins and sequences, walked recursively. Media paths in WSL form |

#### Sequences

| Tool | Args | Returns |
| --- | --- | --- |
| `premiere_create_sequence` | **`name`**, `preset?`, `fromItems?` | View. `fromItems` matches the footage; `preset` takes a `.sqpreset`; **neither uses the project default, which is rarely what you want** |
| `premiere_list_sequences` | — | `{ sequences: [{name, guid, active}] }`. Cheap — walks no timelines |
| `premiere_set_active` | **`name`** | View |
| `premiere_get_sequence` | `name?`, `tracks?`, `clips?`, `range?`, `params?` | View. **Summary by default**; the selectors expand what you ask for. See below |

#### Editing

All take refs from the most recent view. `v0:2` = third clip on video track 0 (`V1` in the UI).

| Tool | Args | Notes |
| --- | --- | --- |
| `premiere_insert_clip` | **`item`**, **`time`**, **`mode`**, `videoTrack=0`, `audioTrack=0`, `limitShift=false` | `mode: "overwrite"` replaces what is under it; `"insert"` splices and pushes. A track index past the last track **creates** one |
| `premiere_move_clip` | **`clip`**, **`deltaSeconds`** | An **offset**, not a destination. Subtract the current `start` yourself to land absolute |
| `premiere_trim_clip` | **`clip`**, `inPoint?`, `outPoint?`, `start?`, `end?` | 🔴 **`inPoint` and `start` must not go in one call** — Actions in a transaction all compute against the pre-transaction state, so they fight. Trim, then move |
| `premiere_remove_clip` | **`clips[]`**, `ripple=false` | |
| `premiere_clone_clip` | **`clip`**, **`deltaSeconds`**, `videoTrackOffset=0`, `audioTrackOffset=0`, `mode="insert"` | |

#### Transitions, markers, playhead

| Tool | Args | Notes |
| --- | --- | --- |
| `premiere_list_transitions` | `query?` | Match names **only** — the transition API has no display names at all |
| `premiere_add_transition` | **`clip`**, **`matchName`**, **`at`**, `duration?`, `alignment?` | Video only; **there is no audio transition API**. A transition belongs to a clip *edge*, so add it once from either side. No handles is **not** a refusal — you get a single-sided frame-hold |
| `premiere_remove_transition` | **`clip`**, **`at`** | |
| `premiere_insert_mogrt` | `path`, `time`, `videoTrack?`, `audioTrack?` | Place a `.mogrt` on the timeline. **Places it; cannot type in it** — the text is not writable through the API. Not an Action, so no undo entry |
| `premiere_add_marker` | **`name`**, **`time`**, `duration=0`, `comments?` | How to leave a human a note at a timecode |
| `premiere_set_playhead` | **`time`** | Not an Action, not undoable. Read the result back — it snaps to a frame |

#### Effects and parameters

| Tool | Args | Notes |
| --- | --- | --- |
| `premiere_list_effects` | `query?` | Match name + display name. **Always call this before applying** |
| `premiere_describe_effect` | **`clip`**, **`component`** | 🔴 **`clip` is required** — an un-inserted effect object has no methods at all. Params flagged `unreadable` can still be written |
| `premiere_apply_effect` | **`clip`**, **`matchName`**, `params?`, `index?` | ⚠️ **Two undo entries, not one** — Premiere cannot address an effect's params until the effect has committed |
| `premiere_set_param` | **`clip`**, **`component`**, **`param`**, **`value`**, `time?`, `interpolation?` | With `time` it adds a keyframe. Points are `{x,y}` as **0–1 fractions of the frame**; colours `{r,g,b,a?}`. **Prefer numeric indices** — display names are ambiguous |
| `premiere_remove_effect` | **`clip`**, **`component`** | Refuses the Motion and Opacity intrinsics; reset their params instead |

#### Export and escape hatch

| Tool | Args | Notes |
| --- | --- | --- |
| `premiere_export_frame` | **`time`**, `outPath?`, `width?`, `height?`, `sequence?` | **This is how to SEE the timeline** — export, then read the PNG |
| `premiere_export_sequence` | `outPath?`, `preset?`, `inOutOnly=false`, `sequence?` | Renders **inside Premiere**, so it blocks. `durationSeconds` is measured with `ffprobe` on the finished file, never assumed |
| `premiere_eval` | **`code`**, `timeoutMs?` | Diagnostic tool, not the product. `ppro`, `helpers`, `log()` in scope; `await` works; `return` a value |

### 🔴 Not yet built

`premiere_insert_mogrt` (T11). Until a tool exists the panel answers `INVALID_ARGS` — **which is
also what a stale panel says**, so reload the panel before concluding a tool is missing.

### Reading a timeline — the one thing to understand before using any of this

**No tool returns a whole timeline.** Jack's hand-cut camping project normalises to 573,065 bytes
and the MCP transport refuses anything near that — worse, it refuses it *after* the panel has
committed the edit, so a caller would see a failure for work that succeeded. So every tool that
produces a sequence goes through the same three-part contract (T21):

- **You get a summary.** The project, the sequence settings, and one line per track: clip count,
  transition count, time span, mute state. About 1.8 KB on camping, and it does not grow with the
  edit — it is bounded by the number of tracks, not the number of clips.
- **The complete state is on disk**, untrimmed, at the returned `statePath`
  (`<project dir>/.bridge/state-<sequence>.json`). **`jq` over that file for anything bulk** —
  counting, searching, auditing a whole cut. It costs no context and it is the full article: every
  clip, every effect, every parameter and keyframe.
- **Ask for the detail you want.** `premiere_get_sequence({ tracks: ["v2"] })` lists that track's
  clips in full; `clips: ["v2:3"]` expands named clips with their parameters; `range: [10, 30]`
  lists whatever plays in that window. Uppercase is the UI label (`V3`), lowercase the API index
  (`v2`) — both work, so whichever form you copied from a previous result is fine.

If a response would still be too big it degrades one rung at a time — parameter values, then
effect chains, then markers, then change detail, then clip lists — and `notes` says what went and
which narrower call would have kept it. The bottom rung always fits.

Mutating tools additionally return **`changed`**: the clips added, removed or modified by that
call. That is how you learn the ref of a clip `premiere_insert_clip` just created — the panel
returns a timeline, never a receipt, so the server diffs against the previous state. Note it
compares clip **times**, so a `premiere_set_param` correctly reports no change.

### 🔴 Every edit tool acts on the ACTIVE sequence

None of the editing tools take a sequence argument. They act on whatever Premiere considers active
when the panel runs them — and **a human clicking a different timeline tab changes that silently**.
Re-assert `premiere_set_active` before a run of edits, and **read `sequence.name` on every response**
to confirm the work landed where you meant.

## Errors

Every failure comes back as `{ error: true, code, message, hint? }`. The codes:

| Code | Means | Usual fix |
| --- | --- | --- |
| `NO_MEDIA_ROOT` | No `mediaRoot` configured | Write `badcode.local.json` (see setup.md) |
| `BAD_CONFIG` | `badcode.local.json` is malformed | Fix the JSON; check the env overrides |
| `PANEL_NOT_CONNECTED` | No panel on the socket | Open the panel in Premiere; if it was rebuilt, ⋯ → Load in UDT |
| `TIMEOUT` | The panel took too long | Almost always a modal dialog open in Premiere — dismiss it |
| `NO_PROJECT` | No project open | `premiere_open_project({ story })` |
| `NO_SEQUENCE` | No active sequence | `premiere_create_sequence` or `premiere_set_active` |
| `ITEM_NOT_FOUND` | No such project item | Re-read with `premiere_list_items` |
| `CLIP_NOT_FOUND` | No clip at that ref | Refs go stale after every edit — use the state the last call returned |
| `EFFECT_NOT_FOUND` | No effect by that match name | `premiere_list_effects({ query })`; never guess a match name |
| `TRANSITION_NOT_FOUND` | No transition by that match name | `premiere_list_transitions({ query })` |
| `PARAM_NOT_FOUND` | No such component or param | `premiere_describe_effect` |
| `TRANSACTION_FAILED` | Premiere refused the mutation | Often a locked track or a read-only project |
| `IMPORT_FAILED` | Premiere could not import the file | Check the path exists and the codec is supported |
| `EXPORT_FAILED` | The render did not produce a file | Check the preset path and disk space |
| `INVALID_ARGS` | Bad arguments — **or a stale panel** | Check the call; then rebuild the panel and ⋯ → Load |
| `EVAL_ERROR` | `premiere_eval` code threw | The stack comes back in `detail` |
| `PANEL_ERROR` | Something unexpected inside the panel | Read the panel's own log |

## Layout

| Path | What |
| --- | --- |
| `src/server.ts` | MCP tools over stdio (T6) |
| `src/bridge.ts` | The WebSocket server; strictly serial, one command in flight |
| `src/protocol.ts` | zod schemas + types shared by server and panel |
| `src/config.ts` · `src/paths.ts` | The media root, and `/mnt/d` ⇄ `D:\` translation |
| `src/normalise.ts` | Raw panel dump → `SequenceState` (T7) |
| `src/view.ts` | `SequenceState` → what a session can actually read: digest, drill-down, change diff, budget ladder (T21) |
| `src/smoke-*.ts` | Live scripts against real Premiere, one per ticket |
| `panel/src/` | The UXP panel: `main.ts` (socket + dispatch), `ppro.ts` (API helpers), `commands/` |
| `panel/dist/` | Build output, gitignored, mirrored to `<mediaRoot>\_bridge\panel\` |
| `scripts/build-panel.ts` | The esbuild bundle + mirror |

Hard-won API facts live in [`docs/premiere/api-notes.md`](../../docs/premiere/api-notes.md).
Read it before guessing at a Premiere API — Adobe's web docs lag the npm type declarations, and
the declarations themselves are wrong in at least one place.
