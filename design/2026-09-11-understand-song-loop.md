# music-session — the guided Suno listening loop — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: approved (Kai, 2026-09-11)
Relates: [`2026-09-11-listen-mcp.md`](./2026-09-11-listen-mcp.md) (the describe-audio tool this
calls — **must be built first**; this plan extends its package with one module),
[`2026-09-11-suno-playback-recording-findings.md`](./2026-09-11-suno-playback-recording-findings.md)
(the proven recording method), `docs/suno-gpt/session-method.md`, `docs/suno-gpt/automation.md`,
`scripts/suno/suno.mts`.

## Context

BadCode develops drum & bass tracks in Suno with Claude writing the prompts. The humans are not
trained in sound-design vocabulary, so the feedback loop ("what did you hear?") is weak. The
listen-mcp plan gives Claude a way to describe an audio file. The recording findings prove Claude can
get that file from Suno **without spending the monthly download allowance**, by recording the
browser's playback into a silent virtual speaker (Kai ruled 2026-09-11: preview copies only, releases
still go through the official download).

Kai's workflow, in his words: *"generate one generation, three songs, oh I like that one… I can point
you at an exact title of one Suno song and then you can… listen to it using our tool, then… give the
thread back, here is the textual description… then we can have a skill that kind of refines that
text based on what we want… and hone in on the prompt… we start in a place, we try some stuff out, we
pick one… based on that, let's try another… keep going."*

So the loop is:

```
EXPLORE (4 takes, deliberately spread) → YOU PICK → UNDERSTAND (record + describe + "as a prompt")
   → REFINE (conversation, one change) → NARROW (4 covers of the pick) → YOU PICK → UNDERSTAND → …
```

Facts from the code that shape it (read 2026-09-11):

- `listTakes` (`scripts/suno/suno.mts:1130-1148`) returns only `{ title, dur }`. There's no song ID,
  and **both takes of one Create share a title**, told apart only by duration (`attachCover` picks by
  `wantDuration` for that reason, `suno.mts:968-979`). It reads only rows already in the create
  page's right-hand list and never scrolls.
- **Nothing in `scripts/suno/` presses Play** or touches the player. The create page's row Play
  control has never been mapped (`docs/suno-gpt/automation.md:126` maps only `Select clip`,
  `Like clip`, `More options`).
- **Navigating away from the create page wipes the whole form** (Trap 4/6,
  `automation.md:187-216`). Kai: **one Suno tab, ever.**
- **Suno auto-plays the next song** when one ends (seen live 2026-09-11).
- `gridCells` (`suno.mts:1209-1235`) applies one `styleInfluence` to every cell (`suno.mts:1327`),
  so a spread with a different Style Influence per Create needs a per-cell value.
- Cover rounds: the lyrics come **with the source**, not the sheet. That cost a whole 20-take run on
  2026-08-25 (`scripts/suno/cover-ab.mts:11-15`). `attachCover` exists (`suno.mts:968`), and so do
  `detachCover` (`:1060`) and `formMode` (`:636`). `load` refuses a form in the wrong mode but does
  not switch it (`suno.mts:698-716`).

Research on 2026-09-11 (a capped web sweep, 13 searches):

- **Two takes per Create is fixed.** Suno's v6 FAQ (help.suno.com/en/articles/13924481): "Each time
  you generate, you make two songs with a total cost of 10 credits." So 4 takes means 2 Creates,
  which is 20 credits.
- **Variety rewrites the Style box.** Same FAQ: Variety works by "adjusting and updating your style
  prompts… reduce the Variety slider to 0" to keep control. That breaks our rule that each song is
  its boxes plus its settings, so **Variety is Off** in every round of this loop.
- Remaster levels (help.suno.com/en/articles/8105281): Subtle is "very close to the original",
  Normal is "slight variations", High is "possible changes to musical elements and vocals".
- **No published slider test has a sample size.** All knob values here are starting hypotheses, ours
  included.

## Architecture

```
 YOU ── "explore", "I like X", "understand X", "make the bass dirtier"
  │
  ▼
┌─ skill: music-session (.claude/skills/music-session/SKILL.md) ──────────────────────┐
│ runs the loop; listening mode per session: both | you-first | claude-only               │
│ nothing that spends credits runs without the human's explicit yes                      │
│ writes every round into the song's round log                                            │
└──────┬───────────────────────────┬──────────────────────────────┬─────────────────────────┘
       │ mechanics                 │ ears                         │ craft
       ▼                           ▼                              ▼
 scripts/suno/suno.mts        listen-mcp: listen_describe     suno-prompt skill
  takes  (+ songId)            (built by the other plan)      description → "as a prompt"
  record <songId|title>                                        refine → the next boxes
  explore <spec> --round N [--yes]
  narrow <spec> <songId> --round N [--yes]
       │ imports
       ▼
 @badcode/listen-mcp/capture   (packages/listen-mcp/src/capture.ts, unit-tested)
 scripts/suno/take-row.mts     (pure Suno helpers, unit-tested)
```

Decisions (all ruled by Kai, 2026-09-11):

0. **`music-session` is the front door and a guided walkthrough.** It triggers on broad requests:
   "I want to make some music", "let's work on some Suno audio", "I want to work with some sound",
   "how do we run a music session", "understand that song", "listen to <title>". It opens by
   offering to walk the user through the session, explaining the five steps in plain words. It runs
   **every step as an `AskUserQuestion` with concrete options**: which sheet (or a new song, handed
   to `new-story`/`suno-prompt`), which listening mode, go or no-go on each 20-credit round, which
   take was liked, and which one thing to change next. Each question is written for someone who
   has never done this before (Jack as much as Kai): what happens next and what it costs. It calls
   `suno-prompt` whenever prompt-writing is needed. `suno-prompt` keeps its specific triggers
   ("write a style prompt", "fix this vocal") and gains a one-line pointer sending broad "make
   music" requests to `music-session`. *Rejected:* the walkthrough inside `suno-prompt` (it would mix
   prompt craft with session flow in an already large skill), and the name `understand-song` (it
   reads as "analyse one song" to a newcomer).

1. **Listening modes, chosen by the user**, and changeable any round:
   - `both`: Claude always prepares its read and asks "my read now, or after you listen?"
   - `you-first`: Claude holds its read until the human has reacted.
   - `claude-only`: the human doesn't listen; Claude listens, judges and proposes.
   In **every** mode, nothing that spends credits runs without the human's yes.
2. **Suno only.** Other audio reaches the listening tool as a file. *Rejected:* a generic "record any
   URL" input (Kai: not now).
3. **Play from the create page's take list**, never navigating (it wipes the form). Mapping that
   control is the first live ticket and a **stop gate**. *Rejected:* song-page playback plus `load`
   to refill the form, which stays only as the fallback Kai rules on if the gate is hit.
4. **A take is identified by its Suno song ID** (the UUID in `suno.com/song/<uuid>`), read from its
   row, and round logs record it. Titles alone are ambiguous across a pair.
5. **The hand-back from "understand":** (a) the plain description from `listen_describe`, and (b) a
   draft "as a prompt" (Style box, plus exclude notes) written by the `suno-prompt` skill from that
   description, using our v6 rules, nobody else's. REFINE edits (b) rather than starting over.
6. **Explore spread ("safe end + wild end"),** with the prompt boxes unchanged within a round:
   - Create 1: `model 'v6'`, Weirdness 30, Style Influence 75, Variety `off`
   - Create 2: `model 'v6-wild'`, Weirdness 60, Style Influence 60, Variety `off`
   - Titles carry a **round id** so a later round never matches an earlier round's takes (`create()`
     returns once any 2 rows contain the title, `suno.mts:1086-1087`; the trap `cover-ab.mts:117-119`
     works around): `<title>-r<N>-v6-w30`, `<title>-r<N>-wild-w60`. The base title is capped at 30
     chars because `listTakes` truncates titles at 48 (`suno.mts:1140`).
7. **Narrow = cover the pick with the refined boxes.** Cover mode, source = the picked take (matched
   by title and duration), Variety `off`, the pick's model:
   - Create 1: Audio Influence 75, Weirdness 30
   - Create 2: Audio Influence 40, Weirdness 30
   - Style Influence 75 in both; Max Mode off.
   - Titles: `<title>-r<N>-<modelTag>-ai75-w30`, `<title>-r<N>-<modelTag>-ai40-w30`.
   Lyrics on the page must equal the sheet's before any Create (the `cover-ab.mts` lesson).
   Afterwards: `detachCover` and back to Custom mode.
8. **Recording goes through a virtual speaker per channel.** `flow-chrome.sh` creates a PulseAudio
   null sink `badcode_ch<N>` (N = channel = port − 9221) plus a `module-loopback` from its monitor
   to the default sink, so **live listening in the WSL Chrome is unchanged**, and launches Chrome
   with `PULSE_SINK=badcode_ch<N>`. The recorder reads `badcode_ch<N>.monitor`. Running browsers
   need one relaunch to pick this up.
9. **Two files per recording**, both outside the repo under `LISTEN_MEDIA_ROOT` (default
   `/mnt/c/Users/kai/Desktop/suno-recordings`):
   - `<slug>-<id8>.wav`: raw, for Claude.
   - `<slug>-<id8>.preview.mp3`: Kai's filter `lowpass=f=8000:poles=2,lowpass=f=8000:poles=2`, for
     the human.
   🔴 The filter never touches the raw file (it would falsify the measurements).
10. **Credit-spending commands need `--yes`.** Without it, `explore` and `narrow` print the plan and
    the 20-credit cost and spend nothing. The balance is read before and after every Create
    (existing rule, `suno.mts:1337-1341`).
11. **Research folded into the docs:** the docs say explore/narrow run with Variety Off, and that
    `pair`/`grid` still default to Normal in code (`suno.mts:431, 457, 1213`), with a note that
    Normal lets Suno rewrite the Style box. Changing the pair/grid code default stays out of scope.
    "Variety rewrites the Style box" and "two takes per Create" are now sourced (`suno-v6.md:99, 107, 356`).

## File Structure

| Path | Action | Purpose |
|---|---|---|
| `docs/suno-gpt/files/suno-v6.md` | Modify | fold in the research: `:99` Variety mechanism, `:101` Max Mode source, `:107` two takes sourced, `:356` "rewrites" now sourced; add the Remaster levels and the sources |
| `docs/suno-gpt/automation.md` | Modify | grid baseline → Variety Off (`:548-549`); new §10 "Playback, recording and the listening loop" (Play control + song-id selectors from T4, `record`/`explore`/`narrow`, traps) |
| `docs/suno-gpt/files/suno-controls-and-workflows.md` | Modify | `:39-40`: mark the Weirdness claims unsourced; Suno calls 50 the "normal" midpoint |
| `docs/suno-gpt/session-method.md` | Modify | a section on the explore → pick → understand → refine → narrow loop; round logs record song IDs |
| `packages/listen-mcp/src/capture.ts` (+ `capture.test.ts`) | Create | virtual speaker, record, pin volume, silence check, trim, preview |
| `packages/listen-mcp/package.json` | Modify | add export `./capture` → `./src/capture.ts` |
| `scripts/flow-chrome.sh` | Modify | ensure `badcode_ch<N>` + loopback; launch Chrome with `PULSE_SINK` |
| `scripts/suno/take-row.mts` (+ `take-row.test.mts`) | Create | pure helpers: song-ID parsing, take matching, explore/narrow cell builders, titles, preview slug |
| `package.json` (root) | Modify | `"test"` also runs `vitest run --dir scripts` so `scripts/**/*.test.mts` are gated; `vitest` added to root devDependencies |
| `scripts/suno/suno.mts` | Modify | `listTakes` + songId; `findTake`; `record`; `explore`; `narrow`; usage text |
| `.claude/skills/music-session/SKILL.md` | Create | the loop, modes, hand-back format, credit rule, round-log template |
| `.claude/skills/suno-prompt/SKILL.md` | Modify | refinement loop (`:293-314`): new first step, "from a listen_describe description → as-a-prompt draft" |
| `.claude/skills/suno-automation/SKILL.md` | Modify | document `record`, `explore`, `narrow`, the `--yes` rule and the channel relaunch |
| `CLAUDE.md` | Modify | add `music-session` to the skills row; one bullet under "How to work in this repo" |

## Interfaces

```ts
// packages/listen-mcp/src/capture.ts
export const PREVIEW_FILTER = 'lowpass=f=8000:poles=2,lowpass=f=8000:poles=2'
export const sinkName = (channel: number): string => `badcode_ch${channel}`
export async function ensureSink(name: string, opts?: { loopback?: boolean }): Promise<{ sink: string; created: boolean; moduleIds: number[] }>
  // idempotent: `pactl list short sinks` → if absent, load module-null-sink sink_name=<name> and
  // (unless loopback === false) module-loopback source=<name>.monitor sink=@DEFAULT_SINK@ latency_msec=60
export async function removeSink(moduleIds: number[]): Promise<void>   // pactl unload-module each
export async function pinVolume(sink: string): Promise<void>
  // pactl set-sink-volume <sink> 100%; every sink-input on <sink> → 100%; unmute.
  // 🔴 Call AFTER the stream exists (Chrome creates its sink-input on Play); stream-restore may re-apply an old volume
export async function moveChromeStreams(sink: string, chromePid: number): Promise<number>
  // no-relaunch recovery: move every sink-input whose application.process.id is chromePid or a descendant → returns count
export interface Recording { stop(): Promise<{ path: string; seconds: number }> }
export async function startRecording(sink: string, outWav: string): Promise<Recording>
  // spawns `ffmpeg -v error -y -f pulse -i <sink>.monitor -ac 2 -ar 44100 <outWav>`; resolves only once
  // <outWav> has grown past its header (poll ≤ 3 s, else throw CAPTURE_NOT_STARTED); stop() sends SIGINT and awaits exit
export async function firstSoundAt(wav: string, thresholdDb = -60): Promise<number>
  // seconds of leading silence via `silencedetect=n=<thr>dB:d=0.05`; 0 when there is no leading silence
  // (a silence_start within 0.01 s of 0 counts as leading). All-silent is isSilent's job, not this one's
export async function isSilent(wav: string): Promise<boolean>    // max_volume <= -80 dB via volumedetect
export async function trim(inWav: string, startSec: number, durSec: number, outWav: string): Promise<void>
export async function makePreview(inWav: string, outMp3: string): Promise<void>  // PREVIEW_FILTER + libmp3lame 320k
export function parseSinks(pactlShort: string): string[]         // pure, tested
export function parseMaxVolume(ffmpegStderr: string): number | null   // pure, tested
export function parseSilenceEnd(ffmpegStderr: string): number | null  // pure: first silence_end when silence_start: 0

// scripts/suno/take-row.mts
export interface Take { title: string; dur: string | null; songId: string | null }
export function parseSongId(hrefOrHtml: string): string | null   // first /song/<uuid> (8-4-4-4-12 hex)
export function durToSeconds(dur: string): number                 // '3:20' → 200
export function matchTakes(takes: Take[], key: string): Take[]
  // order: a 36-char uuid → exact songId; else /^[0-9a-f]{8}$/ → songId prefix, falling back to a
  // title substring only if no id matches; else a case-insensitive title substring
export const modelTag = (m: string) => string                     // MOVED here from suno.mts:140-141; suno.mts re-exports it
export interface Cell { model: string; weirdness: number; styleInfluence: number; variety: 'off'; maxMode: false; audioInfluence?: number; title: string }
export const MAX_BASE_TITLE = 30                                   // listTakes truncates titles at 48 chars (suno.mts:1140)
export function exploreCells(baseTitle: string, round: number): Cell[]   // decision 6, exactly two cells; throws if baseTitle > MAX_BASE_TITLE
export function narrowCells(baseTitle: string, round: number, model: string): Cell[]   // decision 7, exactly two cells, styleInfluence 75
export function mediaSlug(title: string, songId: string): string  // '<slug(title)>-<first 8 of id>'
```

**`suno.mts` CLI additions** (all print JSON on the last line):

- `takes [filter]` → `Take[]` (now with `songId`).
- `record <songId|id8|title>` → `{ songId, title, durationSec, raw, preview, channel }`. Errors are
  printed as `CODE: message`, with exit code 1 for all of them (the code in the text is what callers
  branch on):
  - `TAKE_NOT_FOUND` (lists the visible titles)
  - `TAKE_AMBIGUOUS` (lists ids + durs)
  - `TAKE_RENDERING` (dur null)
  - `PLAY_NOT_MAPPED`: the T4 Play selector matches nothing inside the take's row
  - `CAPTURE_SILENT`: the recording is silent. The fix text first tries the no-relaunch recovery
    (`pactl move-sink-input` of that Chrome's stream to `badcode_ch<N>`, done automatically once).
    Only then does it tell the human to relaunch the channel, warning that a relaunch **loses the
    loaded create form and the marked Suno tab**, and that they must wait until the port stops
    answering before `up`.
  - `WRONG_CHANNEL`: the resolved browser has no `suno.com/create` tab, e.g. because it resolved to
    the listen server's AI Studio browser
- `explore <spec.json> --round <N> [--yes]` → `--round` is required. Without `--yes`, the two cells, titles and "20 credits", then exit 0.
  With `--yes`, it runs them like `pair` (`suno.mts:1316-1343`) with a per-cell Style Influence and
  Variety `off`, then prints the takes with song IDs.
- `narrow <spec.json> <songId|id8> --round <N> [--yes]` → the same dry-run/`--yes` contract. The dry run resolves
  the pick and prints it, the cells and the cost, and touches nothing: no lyric check, because the
  pick's lyrics only reach the page on attach. With `--yes`, before any Create it:
  1. resolves the pick
  2. attaches it **by song ID** if T4b found IDs in the Remix picker. Otherwise it uses
     `attachCover(page, pick.title, 0, pick.dur)`, and stops with `TAKE_AMBIGUOUS` if both takes of
     the pick's Create show the same duration.
  3. asserts cover mode, using T4b's v6 detector (not the v5.5-era `formMode` tab check,
     `automation.md:517`), and asserts from `attachCover`'s returned title and duration that the
     attached source is the pick
  4. **loads the refined boxes:** Style and Exclude via `fillChecked`, and Lyrics via
     `setLyrics(spec.lyrics)` (the sheet's words overwrite the source's, as in `cover-ab.mts:129-153`).
     It then verifies the paragraph count and `shape()` equality: lines trimmed, blanks dropped.
     `load()` is NOT reused, because its Voice detector reads the Audio Influence slider, which Cover
     mode also shows (`suno.mts:752-762`).
  5. per cell: model, Variety `off`, Max Mode `false`, Style Influence, Audio Influence, Weirdness,
     title, `checkV6`, then a re-check that the source is still attached (cover-ab's rule), then Create
  Afterwards: `detachCover`, then T4b's detector must read custom with nothing attached, or it prints
  `🔴 FORM LEFT IN COVER MODE — fix by hand before the next load` and exits 1.

Channel number for `record`: from `resolveEndpoint()` (`suno.mts:30-55`), port → channel = port − 9221.

**Round-log entry** (written by the skill into the song's `## Round log`, following
`session-method.md`'s one-variable rule):

```markdown
### r3 — 2026-09-12, explore. Boxes = sheet §<section> (unchanged). Mode: you-first.
| take | songId | settings | preview | Claude's read | human |
|---|---|---|---|---|---|
| m3-A-r3-v6-w30 (3:18) | 44f46458-… | v6 W30 SI75 V-off | …/m3-a-r3-v6-w30-44f46458.preview.mp3 | docs/listening/log/<file>.md | — |
**Pick:** <id8> — Kai: *"…"*   **Next variable:** <one change>
```

## Out of Scope

- Listening to anything but Suno takes (files still work through `listen_describe` directly).
- Autonomous credit spending in any mode.
- Automated Suno downloads (still human-only, `automation.md:335`).
- Fixing Suno's hiss beyond the preview filter.
- Scrolling or paginating the take list (a take must be visible in the create page's list).
- Remaster, Extend, Replace Section (candidates for later narrowing moves).
- Changing `pair`/`grid` behaviour beyond the baseline doc edit.
- Anything in the listen-mcp plan's tickets. This plan only adds `capture.ts` and its export.

## Tickets

### T1: Fold the 2026-09-11 research into the Suno docs   [Status: done | Model: sonnet]
- **Scope:** edit the docs listed in the File Structure rows for `suno-v6.md`, `automation.md`
  (the grid baseline only; §10 comes in T12) and `suno-controls-and-workflows.md`, using the facts
  and URLs in Context. Grade each claim with the existing evidence vocabulary of those files (e.g.
  tested / reported / vendor copy). Add a dated line to each file's revision log if it has one.
- **Files:** `docs/suno-gpt/files/suno-v6.md`, `docs/suno-gpt/automation.md`,
  `docs/suno-gpt/files/suno-controls-and-workflows.md`.
- **Acceptance criteria:**
  - `suno-v6.md` no longer says Variety rewriting the Style box is unsourced, and cites the FAQ URL.
  - Two takes per Create is stated as vendor-sourced.
  - The grid baseline reads Variety Off.
  - No other behaviour claims change.
- **TDD:** no (docs)
- **Validation:** `grep -n "13924481" docs/suno-gpt/files/suno-v6.md` → ≥ 1 hit;
  `grep -n -iE 'variety \**off' docs/suno-gpt/automation.md` → ≥ 1 hit.
- **Depends on:** —
- [x] done
- Notes: 2026-09-11 — done. Both validation greps hit (suno-v6.md :99/:107/:361/:458; automation.md :549/:552/:568). Max Mode (:101) left alone — the plan gives it no source. `suno-controls-and-workflows.md` has no revision log, so the date sits in the note.

### T2: Root test script covers `scripts/`   [Status: done | Model: sonnet]
- **Scope:** root `package.json` `"test"` becomes
  `"npm run test --workspaces --if-present && vitest run --dir scripts"`. `--dir` matters: a bare
  `vitest run scripts` is a path *substring* filter and also runs every copy under
  `.claude/worktrees/` (863 test files there on 2026-09-11). Add `vitest` (same range as
  `packages/flow-mcp/package.json`) to the root `devDependencies`, since today it is only hoisted by
  accident. So the runner has a real target
  (no placeholder tests), create `scripts/suno/take-row.mts` containing only `durToSeconds`, with
  its test.
- **Files:** `package.json`, `scripts/suno/take-row.mts`, `scripts/suno/take-row.test.mts`.
- **Acceptance criteria:** `npx vitest run --dir scripts` finds and passes the take-row test and no
  file under `.claude/`. `npm test` still passes all workspaces.
- **TDD:** yes
- **Validation:** `npx vitest run --dir scripts` → exactly 1 file passing; `npm test` → exit 0.
- **Depends on:** —
- [x] done
- Notes: 2026-09-11 — done. `npx vitest run --dir scripts` → 1 file, 14 tests; root `npm test` exit 0 across all 14 workspaces. The lock gained only the root vitest devDependency. `durToSeconds` throws on anything not M:SS / H:MM:SS.

### T3: `capture.ts`   [Status: pending | Model: sonnet]
- **Scope:** implement per Interfaces. `pactl` and `ffmpeg` are spawned with `execFile` (no shell).
  The pure parsers are unit-tested against captured real outputs (paste real `pactl list short sinks`
  and ffmpeg stderr samples into the test as fixtures). Add the `./capture` export.
- **Integration test**, opt-in only via `it.skipIf(process.env.LISTEN_PULSE_IT !== '1')`.
  `PULSE_SERVER` is always set under WSLg, so gating on it would load PulseAudio modules and play a
  tone out loud on every `npm test`. It creates a uniquely named sink with
  `ensureSink('badcode_test_<pid>', { loopback: false })`, record 3 s while `paplay --device=<sink>` plays a generated 1 kHz tone, stop, and
  assert:
  - `isSilent` is false
  - `firstSoundAt` < 1.5
  - the preview MP3 exists
  - the sink is unloaded in `afterAll` via `removeSink(moduleIds)`
  60 s vitest timeout.
- **Files:** `packages/listen-mcp/src/capture.ts`, `packages/listen-mcp/src/capture.test.ts`,
  `packages/listen-mcp/package.json`.
- **Acceptance criteria:**
  - `ensureSink` twice creates one sink (asserted in the opt-in integration test; the unit tests
    cover the command builders and parsers).
  - `startRecording` resolves only after the WAV has grown past its header.
  - `firstSoundAt` returns 0 for a file with no leading silence.
  - `PREVIEW_FILTER` equals the string in decision 9.
  - Parsers handle the silence case (`max_volume: -91.0 dB` → silent).
  - `makePreview` never writes to its input path.
- **TDD:** yes
- **Validation:** `npm test -w @badcode/listen-mcp` → all pass; `npm run typecheck -w @badcode/listen-mcp` → exit 0;
  `LISTEN_PULSE_IT=1 npm test -w @badcode/listen-mcp` → the integration test passes too.
- **Depends on:** listen-mcp plan T1 (the package exists)
- [ ] done
- Notes:

### T4: Live map — Play control, song ID and player on the create page   [Status: pending | Model: opus]
- **Scope:** HUMAN-GATED if the Suno channel is signed out (stop and ask). Spends no credits. With
  the create page open in the one Suno tab (`npx tsx scripts/suno/suno.mts status` first; do NOT
  navigate), record in a scratch probe script (not committed):
  - the row's Play control (selector, whether a real `page.mouse.click` is needed — cf.
    `suno.mts:965-966`)
  - where the row exposes its song ID (an `href` containing `/song/<uuid>`, a data attribute, or
    the ⋯ → Copy link path)
  - whether clicking Play navigates (it must not)
  - the bottom player's `<audio>` element and how to read `duration`/`currentTime`/`ended` (in the
    2026-09-11 experiment it was the `<audio>` whose `src` is a `blob:` URL, not `sil-100.mp3`)
  - how to pause
  - whether playback auto-advances to the next row
  Write the evidence (date, what was observed) into `docs/suno-gpt/automation.md` §10, and the
  selectors as exported constants in `scripts/suno/take-row.mts`.
- **🔴 Stop gate:** if a row cannot be played without leaving the create page, record why and stop
  the plan for Kai's ruling (fallback in decision 3).
- **Files:** `docs/suno-gpt/automation.md`, `scripts/suno/take-row.mts`.
- **Acceptance criteria:** every selector the `record` command needs has a constant and an evidence
  line; the form (`status`) reads identically before and after the probe.
- **TDD:** no (discovery)
- **Validation:** `npx tsx scripts/suno/suno.mts status` before and after → identical `styleLen`,
  `lyricParas`, `title`.
- **Depends on:** T2
- [ ] done
- Notes:

### T4b: Live map — v6 Cover attach, detach and mode detection   [Status: pending | Model: opus]
- **Scope:** HUMAN-GATED like T4, and spends no credits (never click Create). v6 Cover has never been
  driven from code. `formMode` detects cover from a "Cover" tab calibrated on the v5.5 UI
  (`automation.md:517` warns it "may false-abort or, worse, false-pass"), `suno-v6.md:97` suggests
  Cover may now be a post-upload mode rather than a tab, and `attachCover`/`detachCover` match
  v5.5-era text. With the create page open (`status` first; do NOT navigate), record:
  - how `attachCover` behaves on v6
  - whether the Remix picker rows expose `/song/<uuid>`, which would allow attaching by song ID
  - a reliable v6 detector for "cover mode + which source is attached" and for "custom + nothing
    attached"
  - whether the Audio Influence, Variety and Style Influence controls are present in Cover mode
  - whether Cover can use `v6-wild` (open question, `suno-v6.md:434`)
  - that `detachCover` returns the form to Custom
  Write the evidence into `automation.md` §10, and the detector as exported selectors/constants in
  `scripts/suno/take-row.mts`.
- **🔴 Stop gate:** if cover state cannot be reliably detected, or the pick cannot be attached
  unambiguously, stop the plan before T10 for Kai's ruling.
- **Files:** `docs/suno-gpt/automation.md`, `scripts/suno/take-row.mts`.
- **Acceptance criteria:** the detector distinguishes the three states (custom-empty, cover-with-X,
  custom-with-leftover) on the live page; the form reads identically (`status`) before and after.
- **TDD:** no (discovery)
- **Validation:** `npx tsx scripts/suno/suno.mts status` before and after → identical `styleLen`,
  `lyricParas`, `title`.
- **Depends on:** T2, T4
- [ ] done
- Notes:

### T5: `take-row.mts` pure helpers   [Status: done | Model: sonnet]
- **Scope:** implement `parseSongId`, `matchTakes`, `exploreCells`, `narrowCells` and `mediaSlug`
  per Interfaces and decisions 6–7. **Move `modelTag` from `suno.mts:140-141` into `take-row.mts`**
  and re-export it from `suno.mts` (`export { modelTag } from './take-row.mts'`), so `take-row.mts`
  imports nothing from `suno.mts`. Otherwise the two import each other: a verified cycle that throws
  `Cannot access … before initialization` under tsx and silently yields `undefined` under vitest, and
  it would also make the "pure" module load Playwright.
- **Files:** `scripts/suno/take-row.mts`, `scripts/suno/take-row.test.mts`.
- **Acceptance criteria:**
  - `parseSongId('<a href="/song/44f46458-d0c2-40f6-a14a-2c331b805fa8">')` → the uuid; no uuid → null.
  - `matchTakes` with an id8 returns only that take; with a title shared by two takes it returns both.
  - `exploreCells('m3-A', 3)` deep-equals the two cells of decision 6, including titles
    `m3-A-r3-v6-w30` / `m3-A-r3-wild-w60`, and `maxMode: false`.
  - `narrowCells('m3-B', 4, 'v6-wild')` → titles `m3-B-r4-wild-ai75-w30` / `m3-B-r4-wild-ai40-w30`,
    both `styleInfluence: 75`.
  - `exploreCells` with a 31-char base title throws.
  - `modelTag` behaves exactly as before the move (`'v6'` → `v6`, `'v6-wild'` → `wild`).
  - `mediaSlug('M3 Lane: take 2', '44f46458-…')` → `m3-lane-take-2-44f46458`.
- **TDD:** yes
- **Validation:** `npx vitest run --dir scripts` → all pass; `npx tsx scripts/suno/suno.mts grid-plan <an existing spec>`
  → unchanged output (proves the `modelTag` move).
- **Depends on:** T2
- [x] done
- Notes: 2026-09-11 — done, 48 tests in scripts/. No grid spec is committed anywhere, so `grid-plan` was proven unchanged on a scratch spec exercising modelTag's edge cases (56 cells; before/after output identical). suno.mts keeps a local binding (`import { modelTag }` + `export { modelTag }`) because gridCells still uses it. narrowCells shares the 30-char cap and both reject a non-positive/non-integer round. No tsconfig covers scripts/; a scratch strict tsconfig typechecked all three files clean.

### T6: `flow-chrome.sh` routes each channel's sound through its own sink   [Status: done | Model: sonnet]
- **Scope:** before launching Chrome, compute `CH=$((PORT-9221))` and `SINK=badcode_ch$CH`. If
  `pactl` exists and `$SINK` is not in `pactl list short sinks`, load
  `module-null-sink sink_name=$SINK` and
  `module-loopback source=$SINK.monitor sink=@DEFAULT_SINK@ latency_msec=60`. Launch Chrome with
  `PULSE_SINK=$SINK` in its environment. The script runs under `set -euo pipefail`, so every
  PulseAudio step must be **non-fatal**: capture `pactl list short sinks` into a variable (no
  `| grep -q` under pipefail), match the sink name as an exact field, and wrap each `pactl` call so a
  failure (WSLg audio server not ready) only prints a warning. **Export `PULSE_SINK` only once the
  sink is confirmed present.** A missing sink must never be named, or Chrome may lose audio
  entirely. If `pactl` is missing or fails, launch exactly as before with one warning line.
- **Files:** `scripts/flow-chrome.sh`.
- **Acceptance criteria:**
  - Launching channel N leaves `badcode_chN` in `pactl list short sinks`.
  - A second launch attempt (which refuses because the port is up, `flow-chrome.sh:50-54`) creates
    no second sink.
  - Live audio is still audible through the loopback (human confirms once).
- **TDD:** no (shell wiring)
- **Validation:** `bash -n scripts/flow-chrome.sh` → exit 0.
  `./scripts/browser-channel.sh up 3 && pactl list short sinks | grep -c badcode_ch3` → `1`.
  `./scripts/browser-channel.sh down 3`.
- **Depends on:** —
- [x] done
- Notes: 2026-09-11 — done. `bash -n` clean; `up 3` → exactly one `badcode_ch3`; a repeat `up 3` refused and still one sink; `down 3` clean; modules 26/27 unloaded afterwards. The plan's idea of reading PULSE_SINK from `/proc/<pid>/environ` cannot work (Chrome blanks its environ for its process title), so routing was proven by playing a 4 s tone at 0.02 gain in a channel-3 tab: the stream landed on `badcode_ch3` and the loopback carried it to RDPSink. **Human confirmation:** Kai reported hearing "a noise in my headphone" at that moment — taken as the one-time audibility check. Known edge: if a sink exists but its loopback was unloaded by hand, the script does not restore the loopback.

### T7: `takes` returns song IDs; `findTake`   [Status: pending | Model: sonnet]
- **Scope:** extend `listTakes` (`suno.mts:1130-1148`) to read each row's song ID with the T4
  selector and return `Take` (`take-row.mts`). Add
  `export async function findTake(page, key): Promise<Take>` using `matchTakes`, which throws
  `TAKE_NOT_FOUND` / `TAKE_AMBIGUOUS` / `TAKE_RENDERING` with the message formats in Interfaces.
  Existing callers of `listTakes` (`create()` at `:1073-1090`, the CLI at `:1343`, and
  `camping.mts` / `cover-ab.mts` / `style-ab.mts`) must keep working. They read `title`/`dur` only.
  Also fix `resolveEndpoint` (`suno.mts:35-50`): when scanning `.flow-channels/*.lock`, skip locks
  whose owner isn't `flow`. Otherwise, once the listen server holds a lock (owner `listen`), Suno
  commands can attach to the AI Studio browser. Any command that needs the create page and finds no
  `suno.com/create` tab stops with `WRONG_CHANNEL`.
- **Files:** `scripts/suno/suno.mts`.
- **Acceptance criteria:** `takes` on the live page prints a song ID for every finished row, and each
  ID opens the right song when pasted into a browser by a human.
- **TDD:** no (browser code; logic is in T5)
- **Validation:** `npx tsx scripts/suno/suno.mts takes` → JSON rows with 36-char `songId`.
  `npx vitest run --dir scripts` still passes.
- **Depends on:** T4, T5
- [ ] done
- Notes:

### T8: `record` command   [Status: pending | Model: opus]
- **Scope:** `record <key>`. The capture module is loaded with a **dynamic `import()` inside this
  command**, so every other `suno.mts` command (and `cover-ab`, `camping`, `style-ab`) keeps working
  without listen-mcp installed. The steps:
  1. `findTake`; the channel from the endpoint (`WRONG_CHANNEL` if there's no create tab)
  2. `ensureSink(sinkName(channel))`
  3. install a page-side listener on the player `<audio>` (T4): on `ended` it sets a flag and pauses
     **immediately**, because a 500 ms poll can miss `ended` and Suno then auto-advances
  4. click the row's Play (T4 selector), then pause at once
  5. wait for Chrome's sink-input to appear on the sink (≤ 3 s); if it isn't there, run
     `moveChromeStreams` once, and if it's still missing, `CAPTURE_SILENT`
  6. `pinVolume(sink)` (the stream exists now); set `audio.volume = 1` and `muted = false` and assert
     both; seek `currentTime = 0`
  7. `startRecording(sink, tmp/raw.wav)` (resolves once audio is flowing), then resume playback
  8. wait for the flag, or `currentTime >= duration − 0.05`; timeout = duration + 30 s
  9. pause every `<audio>`; `stop()`
  10. `isSilent` → `CAPTURE_SILENT`
  11. `firstSoundAt` → `trim(raw, first, audio.duration)` → `<root>/<mediaSlug>.wav`. Trim to the
      player's exact `audio.duration`, not the row's whole-second m:ss
  12. `makePreview` → `<root>/<mediaSlug>.preview.mp3`
  13. delete tmp; print the JSON
  `root` = `LISTEN_MEDIA_ROOT` or the default in decision 9, created if missing. Never navigates;
  asserts `page.url()` still contains `/create` at the end.
- **Files:** `scripts/suno/suno.mts`.
- **Acceptance criteria (live, human-gated on a signed-in Suno channel that was relaunched after T6):**
  - Recording a visible take produces both files.
  - The WAV's duration is within ±0.3 s of the player's `audio.duration` (printed as `durationSec`).
  - `isSilent` is false.
  - `status` reads the form identically before and after.
  - The human opens the preview MP3 and confirms it's the right song with no audible tail of another.
- **TDD:** no (browser + capture wiring; parts tested in T3/T5)
- **Validation:** `npx tsx scripts/suno/suno.mts record <id8>` → exit 0 and JSON with both paths;
  `ffprobe -v error -show_entries format=duration -of csv=p=0 <raw>` → within 0.3 s of `durationSec`;
  `grep -n "@badcode/listen-mcp/capture" scripts/suno/suno.mts` → only a dynamic `import(` line, no
  top-level `import … from`.
- **Depends on:** T3, T6, T7
- [ ] done
- Notes:

### T9: `explore` command   [Status: pending | Model: sonnet]
- **Scope:** add a per-cell `styleInfluence` to the pair/grid run loop (`suno.mts:1316-1343`). Each
  cell sets `Style Influence` from the cell (existing grid cells keep `spec.styleInfluence ?? 75`).
  Then add `explore <spec.json> --round <N> [--yes]` using `exploreCells(spec.title, N)` (Variety
  `off`, Max Mode off). `--round` is required: without it the command refuses, because reused titles
  make `create()` report success on an earlier round's takes.
  - Without `--yes`: print cells, titles and `20 credits (2 Creates)`, then exit 0.
  - With `--yes`: run the loop, then print `listTakes` with song IDs.
  Update the usage banner (`suno.mts:1351-1368`).
- **Files:** `scripts/suno/suno.mts`.
- **Acceptance criteria:** the dry run spends nothing and prints both titles. `grid-plan` output for
  an existing spec is unchanged.
- **Live, human-gated (Kai says yes, 20 credits):** one `--yes` run yields 4 takes titled per
  decision 6, credits logged around each Create.
- **TDD:** no (loop wiring; cells tested in T5)
- **Validation:** `npx tsx scripts/suno/suno.mts explore <spec.json> --round 1` → two titles + cost,
  no Create; without `--round` → refuses with exit 1.
  `npx tsx scripts/suno/suno.mts grid-plan <an existing spec>` → same output as before the change.
- **Depends on:** T5
- [ ] done
- Notes:

### T10: `narrow` command   [Status: pending | Model: opus]
- **Scope:** `narrow <spec.json> <key> --round <N> [--yes]`, exactly per the Interfaces entry
  (dry run, then the five `--yes` steps, then detach and the final assert), using T4b's detector and
  attach-by-ID where T4b found it possible. The pick's model is read from its title tag (`-v6-` →
  `v6`, `-wild-` → `v6-wild`, else `spec.model`); if T4b found Cover can't use `v6-wild`, stop with
  `COVER_MODEL_UNSUPPORTED` instead of silently switching model.
- **Files:** `scripts/suno/suno.mts`.
- **Acceptance criteria:** the dry run prints the pick (title, dur, songId), both cells and the cost,
  and spends nothing; it refuses without `--round`.
- **Live, human-gated (Kai says yes, 20 credits):** 4 cover takes titled per decision 7; the form
  ends in Custom with nothing attached.
- **TDD:** no (browser wiring; cells tested in T5)
- **Validation:** `npx tsx scripts/suno/suno.mts narrow <spec.json> <id8> --round 2` (dry) → plan
  printed, exit 0; `npx tsx scripts/suno/suno.mts status` after a live run →
  mode custom, nothing attached.
- **Depends on:** T4b, T7, T9
- [ ] done
- Notes:

### T11: The `music-session` skill and the suno-prompt hand-off   [Status: pending | Model: opus]
- **Scope:** write `.claude/skills/music-session/SKILL.md`:
  - **Frontmatter:** `name: music-session`; a description that leads with the broad triggers from
    decision 0 ("I want to make some music", "let's work on some Suno audio", "I want to work with
    some sound", "how do we run a music session") and then the specific ones ("understand that
    song", "listen to <title>", "what does <title> sound like", "explore this prompt", "narrow on
    <title>").
  - **The walkthrough** (decision 0): the opening offer, the plain-words five-step explanation, and
    one `AskUserQuestion` per step, with the exact question and options written into the skill for:
    sheet choice, mode choice, each credit go/no-go, the pick, and the next variable. Each question
    must stand alone for a newcomer (what happens, what it costs).
  - **The loop** (Context diagram).
  - **Modes and how to ask** (decision 1).
  - **Preflight:**
    - `suno.mts status`
    - `listen_status`
    - the channel must have been launched after T6, else relaunch it once
    - signed-out → STOP and ask
  - **UNDERSTAND:**
    - `suno.mts record <key>`
    - `listen_describe({ path: raw, lens: 'music' })`
    - hand-back (a) the description
    - hand-back (b) "as a prompt", produced by following the suno-prompt skill's rules, clearly
      labelled as a draft
    - mode-dependent withholding
    - always give the human the preview path
  - **REFINE:** one variable per round (`session-method.md:12-34`), diagnose before rewording
    (`:65-78`), edit the draft rather than rewrite it, and write the new boxes into the sheet.
  - **EXPLORE / NARROW:** always dry run first, show the cost, and run with `--yes` only after the
    human's explicit yes.
  - **The round-log template** (Interfaces).
  - **Hard rules:**
    - one Suno tab
    - never navigate
    - never download
    - the filter only on previews
    - media outside the repo, words inside
  Then update `suno-prompt/SKILL.md`: its refinement loop gets a first step pointing here, and its
  description gets one line routing broad "make some music" requests to `music-session`, without
  removing any of its existing triggers. Add the
  commands to `suno-automation/SKILL.md`, add the loop section to `session-method.md`, and update
  `CLAUDE.md`.
- **Files:** `.claude/skills/music-session/SKILL.md`, `.claude/skills/suno-prompt/SKILL.md`,
  `.claude/skills/suno-automation/SKILL.md`, `docs/suno-gpt/session-method.md`, `CLAUDE.md`.
- **Acceptance criteria:** every command the skill names exists in `suno.mts`'s usage banner or the
  listen-mcp README; every file path it names exists; the description contains each broad trigger
  phrase from decision 0; the skill contains at least five `AskUserQuestion` step definitions (sheet,
  mode, credit go/no-go, pick, next variable).
- **TDD:** no (docs)
- **Validation:** `npx tsx scripts/suno/suno.mts` (no args) prints `record`, `explore`, `narrow`.
  `grep -ohE '\`[^\` ]*/[^\` ]*\`' .claude/skills/music-session/SKILL.md | tr -d '\`' | sed -E 's/:[0-9].*$//' | grep -vE '^https?:|<|^/mnt/|^@' | sort -u | xargs -I{} ls -d {}`
  → all resolve (path:line refs are stripped to the path; the media root and package specifiers are
  excluded).
- **Depends on:** T8, T9, T10
- [ ] done
- Notes:

### T12: `automation.md` §10 — the listening loop's mechanics   [Status: pending | Model: sonnet]
- **Scope:** extend the §10 started in T4 with `record` / `explore` / `narrow` usage, the error
  codes, the relaunch-after-T6 note, the no-navigation rule, auto-advance, the Verified table rows
  (from T8–T10 live results), and a revision-log line.
- **Files:** `docs/suno-gpt/automation.md`.
- **Acceptance criteria:** each command has a Verified-table row with its live date or ⬜.
- **TDD:** no (docs)
- **Validation:** `awk '/^## 10\./,/^## Revision log/' docs/suno-gpt/automation.md | grep -cE '`(record|explore|narrow)'`
  → ≥ 3, and the same section contains `CAPTURE_SILENT`, `WRONG_CHANNEL` and a Verified table.
- **Depends on:** T8, T9, T10
- [ ] done
- Notes:

### T13: End-to-end — one real session through the loop   [Status: pending | Model: opus]
- **Scope:** HUMAN-DRIVEN. **Requires the listen-mcp plan complete** (its T15). With Kai:
  1. Pick a song sheet and mode.
  2. `explore` (dry run, then yes).
  3. Kai listens to the previews and picks.
  4. "understand <id8>" → description + as-a-prompt.
  5. Refine one variable.
  6. `narrow` (dry run, then yes).
  7. Kai picks.
  8. Understand the new pick.
  Everything goes in the song's round log per the template.
- **Files:** the chosen song's sheet/round log; `docs/listening/log/*` (generated).
- **Acceptance criteria:**
  - Two rounds logged with song IDs, previews, ledger links, picks in Kai's words, and the one
    variable changed.
  - The credit spend is recorded.
  - Kai records a verdict on whether the loop helped (verbatim), which is added to
    `session-method.md`'s loop section.
- **TDD:** no
- **Validation:** `npm test` → exit 0; `npm run typecheck` → exit 0; the round log shows two
  complete round entries.
- **Depends on:** T11, T12, listen-mcp plan T15
- [ ] done
- Notes:

## Discovered Issues Log
(appended by executors during implementation)

- **2026-09-11 (T1):** `docs/suno-gpt/files/suno-v6.md` §6 (≈ lines 319–321) still says the
  credit cost per v6 generation is "unknown" and that "the old '10 credits per Create' may not
  hold". The FAQ quote now at §2 (Create row) says two songs cost 10 credits in total, so §6
  contradicts it. Left unchanged (T1 says no other behaviour claims change); owed a one-line fix
  or a ruling. Also: the "Suno calls 50 the normal midpoint" claim has no kept URL, and our live
  form captions 50 "Expected results" — both are written into the note rather than choosing.
