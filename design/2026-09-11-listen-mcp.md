# listen-mcp — give Claude ears — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: approved (Kai, 2026-09-11)
Relates: `packages/flow-mcp` (the pattern this copies), `scripts/suno/suno.mts` (tab-marking
pattern), `docs/ai-studio/README.md` (AI Studio account, quota and data terms),
`scripts/beat-grid.py` (tempo measurement reused), session "claude-can-hear" 2026-09-11.

## Context

BadCode makes drum & bass in Suno. The loop today is: Claude writes a Suno prompt, Suno makes a
take, a human listens and tries to *describe* what they hear so Claude can revise the prompt. The
humans are not trained in sound design vocabulary, so the feedback is the weakest link. Claude can
see images but cannot hear audio.

Gemini models accept audio and return text. Research on 2026-09-11 established:

- **Gemini 3.1 Pro** (newest Pro, Feb 2026) lists `Text, Image, Video, Audio, and PDF` as inputs
  (`ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview`).
- Pro is **not on the free API tier** (`ai.google.dev/gemini-api/docs/pricing` — "Not available").
  The free key reaches Flash models only (newest: Gemini 3.8 Flash).
- **AI Studio's web page is free to use and Jack's Ultra account raises its quota**
  (`docs/ai-studio/README.md:110-111` — "web UI only, not API keys"). So Pro is reachable at £0
  only through the browser. Kai ruled: browser, Pro, no API route in v1.
- 🔴 **Gemini hears a degraded copy.** `ai.google.dev/gemini-api/docs/audio`: audio is
  "Downsampled to 16 Kbps" and "Multi-channel audio combined to single channel"; 32 tokens per
  second; `MM:SS` timestamps. Therefore Gemini cannot judge stereo width and will miss fine top-end
  detail. We measure those locally instead and never ask Gemini about stereo.

The lesson from Flow automation (Kai, this session): an MCP server whose browser steps are **fixed
Playwright routines against a known DOM map** is fast and reliable; a model that reads the DOM to
decide each click is slow. This tool follows the fixed-routine pattern. No part of it asks a model
to inspect the page.

The existing AI Studio doc maps only the **speech** page (`aistudio.google.com/generate-speech`,
`docs/ai-studio/README.md:152-229`). The **chat** page this tool drives has never been mapped,
so T3 maps it live before any browser code is written.

## Architecture

```
 Claude Code
    │  listen_describe({ path, lens, start?, end?, question?, model? })
    ▼
┌──────────────── packages/listen-mcp ("listen" in .mcp.json) ─────────────────┐
│ prepare.ts → ffmpeg decode/trim → seg.wav ─┬─► measure.ts → scripts/audio-measure.py
│                                            └─► ffmpeg → seg.mp3 (upload copy)
│ lens.ts (docs/listening/lenses/<lens>.md) ─► prompt.ts (lens + measured facts + question)
│ studio-client.ts (fixed routines, selectors from studio-dom.ts)
│     new chat → pick model → Search grounding off → attach mp3 → prompt → Run → read reply
│ remap.ts (shift MM:SS by range start) ─► ledger.ts → docs/listening/log/<stamp>-<slug>.md
│ describe.ts orchestrates the above; server.ts exposes it as MCP tools
└───────────────────────────────┬───────────────────────────────────────────────┘
                                │ CDP
                                ▼
       its OWN browser channel (owner "listen"), profile signed into Jack's Ultra account
```

Decisions (all ruled by Kai, 2026-09-11):

1. **Shape: MCP server**, sibling of `packages/flow-mcp` and `packages/premiere-mcp`, registered in
   `.mcp.json` as `npx tsx packages/listen-mcp/src/server.ts`.
2. **Engine: AI Studio chat page, browser only, default model "Gemini 3.1 Pro".** The model is
   chosen by visible name in the model menu; `model` arg or `LISTEN_MODEL` env overrides; the
   result reports the model name the page actually displayed. *Rejected:* free-key Flash fallback
   (Kai: out of v1).
3. **Own browser channel — and never Flow's.** Flow's `resolveChannel`
   (`packages/flow-mcp/src/channel.ts:160`) claims the *lowest* up-and-unclaimed browser, so if
   listen resolved first it would take channel 1 (Flow's signed-in browser, which the Playwright
   MCP also attaches to on 9222) and silently push Flow onto another channel. So listen has its
   own resolver, `resolveListenChannel` (in `src/channel.ts`, built from Flow's exported
   `surveyChannels`/`writeLock`/`heldChannel`/`probe`/`portForChannel`/`endpointFor`), in this order:
   (1) `LISTEN_CDP_PORT` pin (no lock; Flow's `FLOW_CDP_PORT` is **never** read);
   (2) a lock this PID already holds;
   (3) an up, unclaimed channel **≥ 2** that has an `aistudio.google.com` tab and **no**
   `labs.google/fx/tools/flow` tab (tab URLs from `http://localhost:<port>/json/list`);
   (4) the lowest down, unclaimed channel **≥ 2** → lock it, `needsLaunch: true`;
   (5) else throw `ALL_CHANNELS_BUSY`. Channel 1 is never claimed by listen unless pinned.
   Resolution is lazy (first tool call) and the lock is released on exit, as in
   `packages/flow-mcp/src/server.ts:32-45`. The server never launches Chrome; it returns the exact
   `./scripts/browser-channel.sh up <n>` command. *Rejected:* reusing `resolveChannel` as-is
   (the collision above).
4. **Reuse by export, not copy.** `@badcode/flow-mcp` gains sub-path exports `./channel`,
   `./page-dump`, `./result`. *Rejected:* extracting a shared package (churn inside Flow's server,
   no second consumer beyond this one).
5. **Ranges are cut with ffmpeg** (`start`/`end`), so Gemini hears only the range; timestamps in
   the answer are shifted back to source time and the shift is noted. *Rejected:* whole-song upload
   with a focus prompt.
6. **Lenses live in the repo** as markdown (`docs/listening/lenses/{music,voice,sfx}.md`). Changing
   the vocabulary is a doc edit. Lenses are written in plain production language, never Suno-tag
   vocabulary, so a Suno model change never breaks them.
7. **Measure and ground.** Every call measures the segment locally; tempo (when trustworthy) and
   loudness are given to Gemini as facts not to contradict. Stereo numbers are recorded but never
   sent (Gemini hears mono).
8. **Ledger in the repo.** Every call writes one markdown file under `docs/listening/log/` (house
   rule: media outside the repo, words inside it).
9. **One call at a time** — a promise-chain mutex in `server.ts`; one tab.
10. **No DOM reading by a model.** Selectors live in `studio-dom.ts`, evidence in
    `docs/listening/automation.md`. Error strings are matched only when seen live (Flow's ruling,
    `packages/flow-mcp/src/flow-client.ts:2586-2600`); anything unmapped becomes a `TIMEOUT` with a
    page-text + screenshot dump.

## File Structure

| Path | Action | Purpose |
|---|---|---|
| `packages/flow-mcp/package.json` | Modify | add `exports` `./channel` → `./src/channel.ts`, `./page-dump` → `./src/page-dump.ts`, `./result` → `./src/result.ts` |
| `packages/listen-mcp/package.json` | Create | `@badcode/listen-mcp`, type module, scripts `start`/`typecheck`/`test` identical to flow-mcp's; deps `@badcode/flow-mcp` (`*`), `@modelcontextprotocol/sdk`, `playwright`, `zod`; devDeps `@types/node`, `tsx`, `vitest` (same ranges as `packages/flow-mcp/package.json`) |
| `packages/listen-mcp/tsconfig.json` | Create | copy of `packages/flow-mcp/tsconfig.json` |
| `packages/listen-mcp/README.md` | Create | tool reference (args, returns, error codes), setup (channel + sign-in) |
| `packages/listen-mcp/src/version.ts` | Create | `NAME = 'badcode-listen'`, `VERSION = '0.0.0'` |
| `packages/listen-mcp/src/types.ts` | Create | shared types (`Range`, `Measurements`, `Lens`, `DescribeArgs`, `DescribeResult`) so tickets can be built in any order |
| `packages/listen-mcp/src/channel.ts` (+ `.test.ts`) | Create | `resolveListenChannel` — never claims channel 1 or a Flow browser |
| `packages/listen-mcp/src/prepare.ts` (+ `.test.ts`) | Create | path normalisation, sha256, ffprobe duration, range validation, trim → wav, wav → mp3, cleanup |
| `packages/listen-mcp/src/measure.ts` (+ `.test.ts`) | Create | spawn `scripts/audio-measure.py`, validate JSON with zod |
| `packages/listen-mcp/src/lens.ts` (+ `.test.ts`) | Create | load/list lens files, extract required headings, content hash |
| `packages/listen-mcp/src/prompt.ts` (+ `.test.ts`) | Create | build the exact instruction text sent to Gemini |
| `packages/listen-mcp/src/remap.ts` (+ `.test.ts`) | Create | shift `MM:SS` / `H:MM:SS` timestamps by an offset |
| `packages/listen-mcp/src/ledger.ts` (+ `.test.ts`) | Create | render + write the ledger record |
| `packages/listen-mcp/src/studio-dom.ts` (+ `.test.ts`) | Create | selector constants + pure classifiers for page states (signed out, rate limited, error, model list parsing) |
| `packages/listen-mcp/src/studio-client.ts` | Create | the only browser code: attach, marked tab, new chat, model, grounding off, attach, submit, wait, read, timeout dump |
| `packages/listen-mcp/src/describe.ts` (+ `.test.ts`) | Create | orchestrator; takes an injected `Studio` interface so it is testable with a fake |
| `packages/listen-mcp/src/server.ts` | Create | MCP wiring, channel, mutex, error → tool-result mapping |
| `packages/listen-mcp/src/smoke-map.ts` | Create | live DOM probe used by T3 (prints what it finds) |
| `packages/listen-mcp/src/smoke-describe.ts` | Create | live end-to-end of `studio-client` on a generated tone |
| `scripts/audio-measure.py` | Create | measurements → JSON on stdout |
| `scripts/test_audio_measure.py` | Create | unittest on synthetic signals |
| `scripts/browser-channel.sh` | Modify | `logged_in()` (`:50-57`): add `aistudio\.google\.com` to the "yes" pattern |
| `docs/listening/README.md` | Create | what the tool is, the 16 kbps mono caveat, how to call it, the verified-vs-read table, the Pro-vs-Flash result (T15) |
| `docs/listening/automation.md` | Create | the AI Studio chat-page DOM map, traps, verified table (format mirrors `docs/suno-gpt/automation.md`) |
| `docs/listening/lenses/music.md`, `voice.md`, `sfx.md` | Create | the checklists |
| `docs/listening/log/.gitkeep` | Create | ledger directory |
| `.claude/skills/listen/SKILL.md` | Create | when to use, preflight (channel + sign-in stop), caveats, where records go |
| `.mcp.json` | Modify | add `"listen": { "command": "npx", "args": ["tsx", "packages/listen-mcp/src/server.ts"] }` |
| `CLAUDE.md` | Modify | one repo-map row for `docs/listening/` + `packages/listen-mcp`; add `listen` to the skills list row |
| `docs/README.md` | Modify | one toolkit bullet for `listening/` |

## Interfaces

### MCP tools (server `listen`)

`listen_status()` → `ok({ channel: { channel, port, how, needsLaunch } | null, browserUp: boolean, signedIn: 'yes'|'no'|'unknown', lenses: string[], defaultModel: string })`
— `how` is `Resolution.how` verbatim; `browserUp` = `probe(port)` from `@badcode/flow-mcp/channel`;
`signedIn` = `studio.signedInState()` when the browser is up, else `'unknown'`. It never throws for
a missing browser — reporting that is its job.

`listen_describe(args)`:

```ts
{
  path: string            // Linux or Windows path (D:\x\y.mp3 or /mnt/d/x/y.mp3)
  lens?: string           // default 'music'; must match a file in docs/listening/lenses/
  start?: string | number // seconds or "M:SS" / "H:MM:SS", source time
  end?: string | number
  question?: string       // appended verbatim after the lens checklist
  model?: string          // visible model-menu name; default LISTEN_MODEL ?? 'Gemini 3.1 Pro'
}
```
→ `ok(DescribeResult)`:

```ts
// types.ts
export interface DescribeArgs { path: string; lens?: string; start?: string|number; end?: string|number; question?: string; model?: string }
export interface DescribeResult {
  description: string; measurements: Measurements; modelShown: string; lens: string
  range: Range | null; sha256: string; ledgerPath: string /* repo-relative */
  remapped: boolean   // true iff range !== null && range.start > 0 && remapTimestamps(...).count > 0
}
```

`classifyPage` → error code mapping (in `studio-client.ts`): `'signed-out'` → throw
`NOT_SIGNED_IN`; `'rate-limited'` → `RATE_LIMITED: <matched text>`; `'error'` →
`STUDIO_ERROR: <matched text>`; `'ok'` → continue.

Error codes (via `fail(code, message, hint)` from `@badcode/flow-mcp/result`):
`INVALID_ARGS`, `FILE_NOT_FOUND`, `RANGE_INVALID`, `LENS_NOT_FOUND`, `NOT_RUNNING`,
`NOT_SIGNED_IN`, `MODEL_NOT_FOUND`, `UPLOAD_FAILED`, `RATE_LIMITED`, `STUDIO_ERROR`, `TIMEOUT`,
`MEASURE_FAILED`, `LISTEN_ERROR` (catch-all). `RATE_LIMITED`/`STUDIO_ERROR` exist only once T3
has recorded their live wording; until then those states surface as `TIMEOUT`.

### Module signatures

```ts
// channel.ts
export async function resolveListenChannel(root: string, env?: NodeJS.ProcessEnv): Promise<Resolution>
  // Resolution type imported from '@badcode/flow-mcp/channel'; order per Architecture decision 3
export function isListenCandidate(tabUrls: string[]): boolean   // has aistudio.google.com AND no labs.google/fx/tools/flow

// prepare.ts   (Range lives in types.ts)
export interface Range { start: number; end: number }            // seconds, source time
export function toLinuxPath(p: string): string                     // 'D:\\a\\b.mp3' → '/mnt/d/a/b.mp3'; posix passthrough
export function parseTime(t: string | number): number             // 80 | '80' | '1:20' | '1:20.5' | '0:01:20' → seconds; throws 'RANGE_INVALID: …'
export function validateRange(durationSec: number, start?: number, end?: number): Range | null
  // null when neither given; start defaults 0, end defaults duration; throws 'RANGE_INVALID: …' if start<0, end>duration+0.05, start>=end
export interface Prepared {
  sourcePath: string; sourceName: string; sha256: string; durationSec: number
  range: Range | null; wavPath: string; mp3Path: string; cleanup(): Promise<void>
}
export async function prepare(path: string, opts?: { start?: string|number; end?: string|number; tmpRoot?: string }): Promise<Prepared>
  // throws 'FILE_NOT_FOUND: …'; wav = pcm_s16le 44.1k stereo-preserving; mp3 = libmp3lame 192k

// measure.ts
export const MeasurementsSchema: z.ZodType<Measurements>
export interface Measurements {
  durationSec: number
  integratedLufs: number | null; truePeakDbtp: number | null; loudnessRangeLu: number | null
  channels: number
  stereoCorrelation: number | null   // null when channels === 1 OR either channel has zero variance
  sideToMidDb: number | null         // null when channels === 1 or both M and S are silent; else clamped to [-120, 120]
  spectralCentroidHz: number
  tempo: { bpm: number | null; confidence: 'high'|'fair'|'tempo-only'|'unverified'|'none' }
}
export async function measure(wavPath: string, opts: { script: string; python?: string }): Promise<Measurements>
  // script = absolute path to scripts/audio-measure.py (caller supplies it); python defaults 'python3'
  // throws 'MEASURE_FAILED: <stderr tail>'

// lens.ts
export interface Lens { name: string; description: string; body: string; headings: string[]; hash: string /* sha256 of file, first 12 hex */ }
export function parseLens(name: string, fileText: string): Lens   // frontmatter name/description; headings = every '## ' line in body, in order
export function listLenses(dir: string): string[]                 // '*.md' only, extension stripped, sorted
export function loadLens(dir: string, name: string): Lens        // throws 'LENS_NOT_FOUND: …' listing available names

// prompt.ts
export const TRUSTED_TEMPO: ReadonlySet<string>                  // {'high','fair','tempo-only'}
export function buildPrompt(input: { lens: Lens; measurements: Measurements; question?: string; rangeLabel?: string }): string

// remap.ts
export function formatTime(sec: number): string                  // 85 → '1:25'; 3725 → '1:02:05'
export function remapTimestamps(text: string, offsetSec: number): { text: string; count: number }
  // shifts every M:SS / MM:SS / H:MM:SS token; leaves ratios like '4:4' untouched only when the second field is not two digits

// ledger.ts
export interface LedgerRecord {
  at: Date; sourceName: string; sha256: string; range: Range | null; lens: Lens
  modelRequested: string; modelShown: string; measurements: Measurements
  instruction: string; description: string; remapped: boolean; question?: string
}
export function ledgerFileName(r: LedgerRecord): string          // 'YYYY-MM-DD-HHMMSS-<slug of sourceName>.md'
export function renderLedger(r: LedgerRecord): string
export async function writeLedger(dir: string, r: LedgerRecord): Promise<string>   // returns absolute path; never overwrites (suffix -2, -3)

// studio-client.ts
export interface Studio {
  signedInState(): Promise<'yes' | 'no' | 'unknown'>      // never throws; from classifyPage on the marked tab
  ensureSignedIn(): Promise<void>                         // throws 'NOT_SIGNED_IN'
  newChat(): Promise<void>
  selectModel(name: string): Promise<string>              // returns shown name; throws 'MODEL_NOT_FOUND: <available…>'
  disableSearchGrounding(): Promise<void>
  attachAudio(mp3Path: string): Promise<void>             // throws 'UPLOAD_FAILED' | 'TIMEOUT: …'
  submit(prompt: string): Promise<void>
  waitForReply(timeoutMs: number): Promise<string>        // reply text; throws classified codes or 'TIMEOUT: …(dump path)'
}
export class StudioClient implements Studio { static connect(endpoint: string): Promise<StudioClient>; isAlive(): boolean; close(): Promise<void> }

// describe.ts
export interface DescribeDeps {
  studio: Studio; defaultModel: string
  lensDir: string; logDir: string; repoRoot: string   // repoRoot only to make ledgerPath repo-relative
  measure: (wavPath: string) => Promise<Measurements> // server binds the real script path
  writeLedger?: typeof writeLedger                    // injectable so tests never write into docs/
  now?: () => Date
}
export async function describe(args: DescribeArgs, deps: DescribeDeps): Promise<DescribeResult>
```

### Ledger file format

Every string value in the frontmatter is JSON-quoted (`JSON.stringify`), so a file or model name
containing `: ` or `#` cannot break the YAML.

```markdown
---
at: "2026-09-11T14:03:22.000Z"
source: "camping-r17-a.mp3"
sha256: <64 hex>
range: "1:20–1:45"        # or "full"
lens: music@<hash12>
model_requested: Gemini 3.1 Pro
model_shown: <exact text from the page>
remapped: true
measurements: { durationSec: 25, integratedLufs: -9.8, … }   # one-line JSON
---

## Question
<only when given>

## Instruction sent
<verbatim prompt>

## Description
<Gemini's reply, after remapping>
```

### `scripts/audio-measure.py`

`python3 scripts/audio-measure.py SEG.wav` → one JSON object on stdout matching `Measurements`
(snake_case NOT used — keys exactly as the TS interface). Exit 1 with a message on stderr on
failure; always `json.dumps(..., allow_nan=False)` so NaN/Infinity can never reach the TS side.
Loudness via `ffmpeg -nostats -i SEG.wav -af ebur128=peak=true -f null -` parsing the `Summary:`
block. In ffmpeg 4.4 the block reads `Integrated loudness:` → `I: … LUFS`, `Loudness range:` →
`LRA: … LU`, and `True peak:` → `Peak: … dBFS` (the unit says dBFS, not dBTP; `Threshold:` appears
twice — ignore it). Key the parser on each header, then the next value line. Silence prints
`I: -70.0`, `LRA: 0.0`, `Peak: -inf`: map I ≤ −70 → null, and when I is null set LRA null too;
`-inf` peak → null. Correlation = Pearson of L and R; side-to-mid =
`20*log10(rms(S)/rms(M))` with M=(L+R)/2, S=(L−R)/2. Centroid = mean of
`librosa.feature.spectral_centroid`. Tempo by importing `analyse()` from `scripts/beat-grid.py`
via `importlib.util.spec_from_file_location` (the hyphenated name cannot be imported normally),
called as `analyse(path, 4, 8, None)`; `bpm` = its `bpm` key or null.

## Out of Scope

- Hooking this into Suno (`suno-prompt` / `suno-automation`) — next feature.
- Comparing two takes in one call.
- Musical key detection.
- The free API key / Gemini 3.8 Flash as an engine (Flash is used only by hand in T15, in the
  AI Studio page, for the comparison).
- Automating Claude Code's MCP restart; launching Chrome from the server.
- Changing Flow's server behaviour beyond the three `exports` entries.
- Automating Suno downloads — house rule: downloads are human-only (`docs/suno-gpt/automation.md:335`).

## Tickets

### T1: Scaffold `@badcode/listen-mcp` and expose Flow's helpers   [Status: done | Model: sonnet]
- **Scope:** add the three sub-path exports to `packages/flow-mcp/package.json`; create the package
  skeleton (`package.json`, `tsconfig.json`, `src/version.ts`, `src/version.test.ts` asserting
  `NAME === 'badcode-listen'`); write `src/types.ts` with every type in the Interfaces section
  that other modules share (`Range`, `Measurements`, `Lens`, `DescribeArgs`, `DescribeResult`);
  run `npm install` at the root so the workspace links.
- **Files:** `packages/flow-mcp/package.json`; `packages/listen-mcp/{package.json,tsconfig.json}`;
  `packages/listen-mcp/src/{version.ts,version.test.ts,types.ts}`.
- **Acceptance criteria:** `import { resolveChannel } from '@badcode/flow-mcp/channel'` typechecks
  from inside listen-mcp; flow-mcp's own tests still pass.
- **TDD:** no (wiring)
- **Validation:** `npm install` → exit 0; `npm run typecheck -w @badcode/listen-mcp` → exit 0;
  `npm test -w @badcode/listen-mcp` → 1 passing; `npm test -w @badcode/flow-mcp` → all pass.
- **Depends on:** —
- [x] done
- Notes: 2026-09-11 — done. The root tsconfig's `@badcode/*` path alias maps sub-paths wrongly (`packages/flow-mcp/channel/src`), so TS falls through to the package `exports`; typecheck and a tsx runtime import both confirmed.

### T2: Channel script recognises AI Studio as signed in   [Status: done | Model: sonnet]
- **Scope:** in `scripts/browser-channel.sh` `logged_in()` (`:50-57`) extend the "yes" regex to
  `labs\.google/fx/tools/flow|suno\.com|aistudio\.google\.com`. Keep the `accounts.google.com`
  "no" check first (a sign-in redirect must still win).
- **Files:** `scripts/browser-channel.sh`.
- **Acceptance criteria:** a channel whose only tab is `https://aistudio.google.com/...` reports
  `LOGGED_IN=yes`; a tab on `accounts.google.com` still reports `no`.
- **TDD:** no (one-line config)
- **Validation:** `bash -n scripts/browser-channel.sh` → exit 0;
  `grep -n 'aistudio\\.google\\.com' scripts/browser-channel.sh` → one hit inside `logged_in()`;
  `./scripts/browser-channel.sh list` runs without error. (A fresh channel opens on Flow and
  already reads `yes`, so `list` alone does not exercise the new pattern. If T3 finds AI Studio's
  signed-out state stays on `aistudio.google.com` rather than redirecting, record that in T3 — the
  script's `yes` for such a tab would then be wrong and `listen_status` is the authority.)
- **Depends on:** —
- [x] done
- Notes: 2026-09-11 — done. `bash -n` clean, one grep hit inside `logged_in()`, `list` runs (all 8 channels down at the time, so the new pattern is not exercised live; T3 records whether signed-out AI Studio redirects).

### T3: Live map of AI Studio's chat page   [Status: blocked — human sign-in needed | Model: opus]
- **Scope:** a HUMAN-GATED discovery ticket. (a) Bring up a channel **≥ 2** for listening with
  `./scripts/browser-channel.sh up 2` (or the lowest free channel ≥ 2 per `list`) — never channel 1,
  which is Flow's. If it is not signed in, STOP and ask Kai/Jack to sign that window into **Jack's
  Ultra account** (the Flow account, `docs/ai-studio/README.md:109`); then navigate that window to
  `https://aistudio.google.com` so later resolution recognises it. (b) Write `src/smoke-map.ts` that attaches over CDP
  (`chromium.connectOverCDP`, `contexts()[0]`, its own tab marked with sessionStorage key
  `__badcode_listen_tab` exactly as `scripts/suno/suno.mts:176-225` does), opens a new chat and
  prints candidate selectors and visible text for each control. (c) Drive the page once end to end
  with a 10-second generated tone (`ffmpeg -f lavfi -i "sine=frequency=440:duration=10" /tmp/tone.mp3`)
  on **Gemini 3.1 Pro** and record, with evidence, in `docs/listening/automation.md`:
  - the new-chat URL; the model menu trigger, how to read the current model's visible name, how
    to pick one by name, and the exact names offered (is 3.1 Pro there on this account?);
  - the Google Search grounding toggle (and its default state), temperature and thinking controls
    and their defaults;
  - the file-attach path: the hidden `input[type="file"]` (set it directly — never the OS chooser;
    reason at `packages/flow-mcp/src/flow-client.ts:467-481`) and the signal that an upload has
    finished processing;
  - the prompt box, the Run control, the "running" vs "done" signal, the selector for the last
    model turn, and whether its `innerText` preserves headings and bullets;
  - the signed-out state (URL/redirect) and any error/rate-limit wording seen (verbatim);
  - 🔴 whether AI Studio saves the chat and the uploaded file to the account's Google Drive, and
    if so the setting that stops it (record, do not change Jack's settings without asking).
  Then put the selectors into `src/studio-dom.ts` as named constants (no logic yet). Use the
  section layout of `docs/suno-gpt/automation.md` (Connecting / Selector table / Traps / Verified
  table / Revision log).
- **Files:** `packages/listen-mcp/src/{smoke-map.ts,studio-dom.ts}`, `docs/listening/automation.md`.
- **Acceptance criteria:** every control used by the `Studio` interface has a selector and a
  one-line evidence note (date, what was observed); the Drive question is answered; the tone
  produced a reply from a model whose shown name contains "Pro". **Two stop gates** — if either is
  hit, record the evidence and the orchestrator stops the plan for a Kai ruling: (1) no Pro model
  accepts the audio; (2) AI Studio saves uploads/chats to Jack's Drive with no per-chat or
  account-level off switch.
- **TDD:** no (discovery)
- **Validation:** `npm run typecheck -w @badcode/listen-mcp` → exit 0;
  `LISTEN_CDP_PORT=<port> npx tsx packages/listen-mcp/src/smoke-map.ts` prints a non-empty value
  for every selector constant in `studio-dom.ts`.
- **Depends on:** T1, T2
- [ ] done
- Notes: 2026-09-11 — (a) done: channel 2 is up (`./scripts/browser-channel.sh up 2`, fresh profile `.flow-profile-9223`) with a tab on AI Studio. It is **signed out**: AI Studio shows its marketing page at `https://aistudio.google.com/welcome` ("Get started") — it does NOT redirect to accounts.google.com. 🔴 **STOPPED at the gate:** someone must sign that window into Jack's Ultra account (`jacktttt330@…`). (b)–(c) not started.

### T4: `scripts/audio-measure.py`   [Status: done | Model: sonnet]
- **Scope:** implement per the Interfaces section. Mono input → `channels: 1`,
  `stereoCorrelation: null`, `sideToMidDb: null`. Digital silence → loudness fields null (ebur128
  prints `-inf`/`-70`; map `-inf` and values ≤ −70 to null), tempo confidence `none`.
- **Files:** `scripts/audio-measure.py`, `scripts/test_audio_measure.py`.
- **Acceptance criteria (tests generate their signals with numpy + the stdlib `wave` module into
  a temp dir — no new Python dependency):** identical L/R → correlation ≥ 0.999 and sideToMidDb
  ≤ −100; L = −R → correlation ≤ −0.999; a 1 kHz sine at −20 dBFS peak in both channels →
  integratedLufs within ±1.5 of −20 (BS.1770: per-channel −3 dB for a sine's RMS, +3 dB for
  summing two channels);
  10 s of 174 BPM clicks generated at **48 kHz** → bpm within ±3 of 174 or its octave, confidence
  not `none` (expect `unverified` — aubiotrack finds too few beats on a bare click train, so the
  trusted path is not exercised here; accepted); silence → integratedLufs, loudnessRangeLu,
  truePeakDbtp and stereoCorrelation all null; **the stdout of the silence case and of the L = −R
  case both parse with `json.loads`** (no NaN/Infinity). Output keys exactly match the TS interface.
- **TDD:** yes
- **Validation:** `python3 -m unittest scripts/test_audio_measure.py -v` → all pass;
  `python3 scripts/audio-measure.py <any wav>` prints valid JSON.
- **Depends on:** —
- [x] done
- Notes: 2026-09-11 — done, 6/6 tests. Deviation: a 10 ms windowed sine click is too faint for librosa's median onset envelope (fewer than four beats, confidence `none`), so the test uses a 20 ms decaying noise burst; on that, both detectors agree and confidence comes out `high`, not the `unverified` the plan expected — the trusted path IS exercised.

### T5: `prepare.ts`   [Status: done | Model: sonnet]
- **Scope:** implement per Interfaces. `toLinuxPath` handles `X:\…` and `X:/…` (lower-cases the
  drive) and passes posix paths through; do not spawn `wslpath`. sha256 is streamed. Duration from
  `ffprobe -v error -show_entries format=duration -of csv=p=0`. Trim with
  `ffmpeg -v error -ss <start> -to <end> -i <src> -c:a pcm_s16le -ar 44100 <tmp>/seg.wav`
  (input-side seek for speed); mp3 via `-c:a libmp3lame -b:a 192k`. Temp dir under
  `os.tmpdir()/listen-<random>`; `cleanup()` removes it.
- **Files:** `packages/listen-mcp/src/prepare.ts`, `prepare.test.ts`.
- **Acceptance criteria:** unit tests for `toLinuxPath`, `parseTime` (all formats + garbage →
  throws `RANGE_INVALID`), `validateRange` (every rule in its signature comment). One integration
  test generating a 5 s stereo tone with ffmpeg in a temp dir: `prepare(tone, {start: 1, end: 3})`
  yields a wav of 2.0 ± 0.05 s with 2 channels and an mp3 that ffprobe reads; missing file →
  `FILE_NOT_FOUND`.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass; `npm run typecheck -w @badcode/listen-mcp` → exit 0.
- **Depends on:** T1
- [x] done
- Notes: 2026-09-11 — done, 22 tests (unit + ffmpeg integration). ffprobe failing to read a duration also reports FILE_NOT_FOUND ("is it audio?"), and a range is validated before any cut.

### T6: `measure.ts`   [Status: done | Model: sonnet]
- **Scope:** spawn `<python> <opts.script> <wav>` (caller passes the absolute script path), parse
  stdout with `MeasurementsSchema`; non-zero exit or schema failure → `MEASURE_FAILED: …` with the
  last 500 chars of stderr. Integration tests set an explicit vitest timeout of 60 s (the librosa
  import alone takes 3–8 s here; the default is 5 s).
- **Files:** `packages/listen-mcp/src/measure.ts`, `measure.test.ts`.
- **Acceptance criteria:** schema accepts a valid fixture and rejects a missing key; a fake script
  (temp file printing fixed JSON) is parsed; a fake script exiting 1 throws `MEASURE_FAILED`; one
  integration test on a generated tone returns `channels: 2`.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass.
- **Depends on:** T4, T5
- [x] done
- Notes: 2026-09-11 — done, 8 tests; the real-script tone test takes ~1.1 s here (60 s timeout set).

### T7: Lenses and `lens.ts`   [Status: done | Model: sonnet]
- **Scope:** write the three lens files and the loader. Each file has frontmatter `name`,
  `description`, then a short instruction paragraph and `## ` headings that the answer must use.
  `music`: `## Overall impression`, `## Drums`, `## Bass`, `## Lead and vocals`,
  `## Pads, texture and effects`, `## Mix balance`, `## Energy and structure` (per section with
  `MM:SS` timestamps), `## What stands out` (best and worst moments). `voice`:
  `## Overall impression`, `## Voice` (age, accent, timbre, register), `## Delivery` (pace,
  emphasis, emotion), `## Recording quality`, `## Timeline` (MM:SS), `## What stands out`. `sfx`:
  `## Overall impression`, `## Sources`, `## Character` (texture, attack, decay, space),
  `## Timeline`, `## What stands out`. Every lens instructs: describe only what is heard; say
  "unsure" rather than guess; do not comment on stereo width (the model hears mono); plain
  producer language, no genre-tag lists. Lens text must follow `docs/voice.md` only where it
  addresses tone of instructions — the lenses are working documents, not public copy.
- **Files:** `docs/listening/lenses/{music,voice,sfx}.md`, `packages/listen-mcp/src/lens.ts`,
  `lens.test.ts`.
- **Acceptance criteria:** `parseLens` extracts name/description/headings in order; `hash` changes
  when a byte changes; `listLenses` ignores non-`.md` files and returns a sorted list; `loadLens`
  on an unknown name throws `LENS_NOT_FOUND` listing `music, sfx, voice`; a test loads each real lens file and asserts ≥ 5 headings.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass.
- **Depends on:** T1
- [x] done
- Notes: 2026-09-11 — done, 10 tests. Each lens heading carries a one-line guide under it (part of the body sent to Gemini). `loadLens` only accepts names from `listLenses`, so a name cannot walk out of the directory.

### T8: `prompt.ts`   [Status: done | Model: sonnet]
- **Scope:** `buildPrompt` returns, in order: the lens body; a `MEASURED FACTS — do not contradict
  these:` block containing duration, integrated loudness and true peak (when non-null) and tempo
  **only when** `tempo.confidence ∈ TRUSTED_TEMPO`; when a range was cut, one line "This clip is
  <rangeLabel> of a longer track; timestamps are relative to the clip start."; the question under
  `EXTRA QUESTION:` when given; a closing line "Answer using exactly these headings, in order:"
  followed by the lens headings. Stereo fields are never included.
- **Files:** `packages/listen-mcp/src/prompt.ts`, `prompt.test.ts`.
- **Acceptance criteria:** snapshot-free assertions: tempo present for `high`, absent for `none`
  and `unverified`; within the `MEASURED FACTS` block only, none of the stereo keys or their values
  (`stereoCorrelation`, `sideToMidDb`, and the fixture's numbers for them) appear — the lens body
  itself legitimately says "do not comment on stereo width"; question
  appears verbatim; headings listed in lens order; output is deterministic.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass.
- **Depends on:** T6, T7
- [x] done
- Notes: 2026-09-11 — done, 8 tests. Numbers are rounded for the prompt (1 dp; tempo to a whole BPM); the stereo check covers both raw and rounded forms of the fixture values.

### T9: `remap.ts`   [Status: done | Model: sonnet]
- **Scope:** implement `formatTime` and `remapTimestamps`. Match `\b(?:(\d+):)?(\d{1,2}):(\d{2})(?:\.\d+)?\b`
  semantics (H:MM:SS or M:SS/MM:SS with two-digit seconds < 60); ranges like `0:05–0:12` shift both
  ends. Tokens whose seconds field is not two digits or ≥ 60 are left alone.
- **Files:** `packages/listen-mcp/src/remap.ts`, `remap.test.ts`.
- **Acceptance criteria:** `0:05` + 80 → `1:25`; `0:59` + 3600 → `1:00:59`; `0:05–0:12` + 80 →
  `1:25–1:32`; `4:4`, `3:75`, `12:3` unchanged; offset 0 returns identical text (with `count`
  still equal to the number of timestamp tokens found); markdown around tokens preserved.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass.
- **Depends on:** T1
- [x] done
- Notes: 2026-09-11 — done, 12 tests. A token's own fraction is kept at its precision; otherwise shifted times round to whole seconds (so a fractional range start never prints a decimal the answer didn't have).

### T10: `ledger.ts`   [Status: done | Model: sonnet]
- **Scope:** implement per Interfaces and the Ledger file format. Slug: lower-case source name
  without extension, non-alphanumerics → `-`, collapsed, max 60 chars. Range label uses
  `formatTime` and an en dash. Never overwrite: append `-2`, `-3`… Use UTC in `at` and in the file
  name.
- **Files:** `packages/listen-mcp/src/ledger.ts`, `ledger.test.ts`, `docs/listening/log/.gitkeep`.
- **Acceptance criteria:** every frontmatter value round-trips through `JSON.parse` (strings are
  JSON-quoted, `measurements` is one-line JSON), including a source name containing `: ` and `#`;
  the three body sections in order, `## Question` only when a question exists; two writes with the
  same timestamp into a temp dir produce two files. Tests write only to a temp dir.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass.
- **Depends on:** T1 (types), T9
- [x] done
- Notes: 2026-09-11 — done, 6 tests. `sha256` is JSON-quoted too (the format example showed it bare, but the rule says every string value is quoted and every value must round-trip). Files are created with the `wx` flag, so two concurrent writers cannot clobber each other either.

### T11: `studio-dom.ts` classifiers   [Status: pending | Model: sonnet]
- **Scope:** add pure functions over data the client will scrape: `classifyPage({ url, texts })`
  → `'signed-out' | 'rate-limited' | 'error' | 'ok'` using ONLY URL rules and wording recorded
  verbatim in `docs/listening/automation.md` by T3 (if T3 recorded no rate-limit/error wording,
  those branches do not exist yet — say so in a comment pointing at the dump mechanism);
  `matchModel(available: string[], wanted: string)` → the first available name containing
  `wanted` case-insensitively, else null.
- **Files:** `packages/listen-mcp/src/studio-dom.ts`, `studio-dom.test.ts`.
- **Acceptance criteria:** tests use the exact strings from `automation.md`; `accounts.google.com`
  URL → `signed-out`; `matchModel(['Gemini 3.1 Pro Preview','Gemini 3.8 Flash'], 'gemini 3.1 pro')`
  → `'Gemini 3.1 Pro Preview'`; unknown → null.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass.
- **Depends on:** T3
- [ ] done
- Notes:

### T12: `studio-client.ts`   [Status: pending | Model: opus]
- **Scope:** implement `StudioClient implements Studio` using only selectors from
  `studio-dom.ts`. Attach like `packages/flow-mcp/src/flow-client.ts:171-186` but find/create its
  own tab marked with sessionStorage `__badcode_listen_tab` (never `goto` on another automation's
  tab — `scripts/suno/suno.mts:181-182`). Page code passed to `evaluate` as strings, not arrow
  functions (tsx `__name` trap, `docs/suno-gpt/automation.md:41-60`). Upload by `setInputFiles`
  on the hidden input (never the chooser). Upload wait 60 s; reply wait default 240 s. On timeout,
  write `${tmpdir()}/listen-timeout-<ISO>.txt/.png` using `dumpLines` from
  `@badcode/flow-mcp/page-dump`, mirroring `flow-client.ts:2586-2616`, and throw
  `TIMEOUT: … <dump path>`. Each poll tick runs `classifyPage` and throws its code immediately.
  `selectModel` reads the menu's options, uses `matchModel`, throws `MODEL_NOT_FOUND: <names>`,
  and returns the name read back from the trigger after selection.
  `signedInState()` never throws: it reads the marked tab's URL/texts through `classifyPage` and
  maps `signed-out` → `'no'`, `ok` → `'yes'`, anything unreadable → `'unknown'`.
- **Files:** `packages/listen-mcp/src/studio-client.ts`, `packages/listen-mcp/src/smoke-describe.ts`.
- **Acceptance criteria:** `smoke-describe.ts` generates its own 10 s tone into `os.tmpdir()` with
  ffmpeg (does not rely on T3's file), sends the generic prompt "Describe this audio.", and prints
  the shown model name and a non-empty reply; running it twice in a row works (new chat each time).
  HUMAN-GATED, manual: bring up an unused channel ≥ 2 that has never been signed in
  (`./scripts/browser-channel.sh up <n>`), pin it with `LISTEN_CDP_PORT`, and confirm
  `smoke-describe.ts` exits with `NOT_SIGNED_IN`; record the result in Notes.
- **TDD:** no (browser code; covered by smoke + T11's pure tests)
- **Validation:** `npm run typecheck -w @badcode/listen-mcp` → exit 0;
  `LISTEN_CDP_PORT=<port> npx tsx packages/listen-mcp/src/smoke-describe.ts` → exit 0 with reply.
- **Depends on:** T3, T11
- [ ] done
- Notes:

### T13: `describe.ts` orchestrator, `channel.ts` and `server.ts`   [Status: pending | Model: sonnet]
- **Scope:** `channel.ts`: `resolveListenChannel` and `isListenCandidate` per Architecture decision
  3 and Interfaces, with `channel.test.ts` covering each branch against a temp lock dir and stubbed
  tab lists (follow `packages/flow-mcp/src/channel.test.ts` for the temp-dir + lock pattern; stub
  the `/json/list` fetch by injecting a `tabsFor(port)` function with a real-fetch default).
  `describe()` runs: validate lens (before any work) → `prepare` → `deps.measure` →
  `buildPrompt` → `studio.ensureSignedIn/newChat/selectModel/disableSearchGrounding/attachAudio/
  submit/waitForReply` → `remapTimestamps` only when `range && range.start > 0` (offset =
  range.start) → prepend a line `_Timestamps shifted by +<formatTime(start)> to source time._` when
  `count > 0` → `(deps.writeLedger ?? writeLedger)(deps.logDir, …)` → `cleanup()` in `finally`.
  `server.ts` binds `lensDir = REPO_ROOT/docs/listening/lenses`, `logDir = REPO_ROOT/docs/listening/log`,
  `measure = (w) => measure(w, { script: REPO_ROOT/scripts/audio-measure.py })`; registers
  `listen_status` and `listen_describe` (zod input schemas per Interfaces), resolves the channel
  with `resolveListenChannel(REPO_ROOT)`,
  caches/reconnects the client like `packages/flow-mcp/src/server.ts:17-68`, serialises
  `listen_describe` calls through a promise-chain mutex, releases the lock on exit, and maps error
  prefixes to `fail()` codes with hints. The `NOT_RUNNING` hint names the exact
  `./scripts/browser-channel.sh up <n>` for the resolved channel and says the profile must be
  signed into Jack's Ultra account.
- **Files:** `packages/listen-mcp/src/{channel.ts,channel.test.ts,describe.ts,describe.test.ts,server.ts}`.
- **Acceptance criteria:** `resolveListenChannel` never returns channel 1 unless pinned, skips an
  up channel with a Flow tab, and prefers an up channel ≥ 2 with an AI Studio tab. `describe` tests
  use a fake `Studio`, a fake `measure` returning a fixture, the real lens dir, and a temp `logDir`
  (nothing is written into `docs/`): a full-file call writes one ledger file containing the fake
  reply and returns `remapped: false`; a ranged call (`start: 80, end: 90` on a generated 95 s tone)
  with fake reply `"Drop at 0:05"` returns a description that **contains** `"Drop at 1:25"` and
  `remapped: true`; `start: 0, end: 5` returns `remapped: false` and no shift line; unknown lens
  fails before `prepare` is called (spy); the temp dir is removed even when the fake throws; two
  concurrent calls through the mutex helper run sequentially. Tests that call ffmpeg set a 60 s
  vitest timeout.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass; `npm run typecheck` (root) → exit 0;
  `echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | npx tsx packages/listen-mcp/src/server.ts`
  prints both tool names (verified to work without `initialize` against flow-mcp's server).
- **Depends on:** T5, T6, T7, T8, T10, T12
- [ ] done
- Notes:

### T14: Register, document, skill   [Status: pending | Model: sonnet]
- **Scope:** add the `listen` entry to `.mcp.json`; write `packages/listen-mcp/README.md` (tools,
  args, returns, error codes, setup), `docs/listening/README.md` (purpose; 🔴 16 kbps mono caveat
  with the source URL; how measurements are used; where records go; a Verified-vs-read table
  seeded from T3's evidence), `.claude/skills/listen/SKILL.md` (frontmatter `name: listen`,
  description with triggers "describe this audio", "what does this take sound like", "listen to
  this", "describe the drop at 1:20"; preflight = `listen_status`, and if not signed in STOP and
  ask the human; never retry a `TIMEOUT` before reading its dump; records live in
  `docs/listening/log/`, audio stays outside the repo). Add one row to `CLAUDE.md`'s repo map and
  `listen` to its skills row, and one bullet to `docs/README.md`'s toolkit list.
- **Files:** `.mcp.json`, `packages/listen-mcp/README.md`, `docs/listening/README.md`,
  `.claude/skills/listen/SKILL.md`, `CLAUDE.md`, `docs/README.md`.
- **Acceptance criteria:** `.mcp.json` is valid JSON; every path mentioned in the new docs exists.
- **TDD:** no (docs/config)
- **Validation:** `node -e "JSON.parse(require('fs').readFileSync('.mcp.json','utf8'))"` → exit 0;
  `grep -ohE '\`[^\` ]*/[^\` ]*\`' docs/listening/README.md .claude/skills/listen/SKILL.md packages/listen-mcp/README.md | tr -d '\`' | grep -vE '^https?:|<' | sort -u | xargs -I{} ls -d {}`
  → every backticked repo path resolves (run from the repo root; URLs and `<placeholder>` paths excluded).
- **Depends on:** T13
- [ ] done
- Notes:

### T15: End-to-end verification + Pro vs Flash by ear   [Status: pending | Model: opus]
- **Scope:** HUMAN-GATED. Restart Claude Code so it loads the `listen` server. Kai/Jack supplies
  one downloaded Suno take (downloads are human-only). Run `listen_status`, then
  `listen_describe({ path, lens: 'music' })` and a ranged call (`start`/`end` around a drop).
  Then, by hand in the AI Studio page, run the **same instruction text** (copied from the ledger's
  "Instruction sent") on the same MP3 with **Gemini 3.8 Flash** and paste that reply into a
  second section of the same ledger file, `## Comparison — Gemini 3.8 Flash (manual)`. Kai listens
  and rules which is more accurate; record the ruling, date and reasons in
  `docs/listening/README.md` (Verified table).
- **Files:** `docs/listening/log/*` (generated), `docs/listening/README.md`.
- **Acceptance criteria:** two ledger files exist for the take (full + ranged); the ranged one's
  timestamps fall inside the requested range in source time; measurements present; Kai's Pro-vs-
  Flash ruling recorded (or recorded as "undecided" with reasons).
- **TDD:** no
- **Validation:** `npm run typecheck` → exit 0; `npm test` (root) → all pass;
  `ls docs/listening/log/*.md` shows the new records.
- **Depends on:** T14
- [ ] done
- Notes:

## Discovered Issues Log
(appended by executors during implementation)

- **2026-09-11 (T3, gate) — AI Studio's signed-out state stays on `aistudio.google.com`.** A fresh
  profile lands on `https://aistudio.google.com/welcome` (marketing page, "Get started"), not an
  accounts.google.com redirect. So `browser-channel.sh`'s T2 pattern reports `LOGGED_IN=yes` for a
  signed-out AI Studio tab (seen: channel 2 `yes` while signed out). As T2 anticipated,
  `listen_status` is the authority; T11's `classifyPage` must treat `/welcome` as `signed-out`
  (confirm once signed in that the signed-in app never uses `/welcome`).
- **2026-09-11 — Flow moved to `flow.google.com`.** Channel 1's tabs are `https://flow.google.com/`,
  not `labs.google/fx/tools/flow`. Two consequences: (1) Architecture decision 3 / `isListenCandidate`
  must also treat a `flow.google.com` tab as a Flow browser, or listen could claim Flow's browser
  (fix in T13, noted here as a scope-safety deviation); (2) `browser-channel.sh logged_in()` reads
  channel 1 as `no` although it is signed in — its `accounts\.google\.com` "no" check matches the
  `accounts.google.com/RotateCookiesPage` **iframe** that flow.google.com embeds, and the Flow "yes"
  pattern no longer matches. Out of this plan's scope; owed a small fix (match only `type: page`
  targets, add `flow\.google\.com`).
