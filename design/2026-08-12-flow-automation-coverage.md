# Flow automation coverage — closing the gaps

**Date:** 2026-08-12 · **Status:** planned
**Branch:** `worktree-flow-automation` (worktree, based on `feat/enc-program` @ `e00f648`)
**Goal:** stop hand-driving Google Flow. Wrap every remaining capability we actually
use as a `flow_*` MCP tool, so a session spends its time on prompts and judgement
rather than DOM round-trips.

## Context

Two sessions of Flow work (GPOM + MMT casting, 2026-08-11/12) established that **~90% of
elapsed time went on browser navigation, not generation.** Building the character tools
fixed that for casting. An audit then found ~29 Flow capabilities with no wrapper and
three known-broken paths. Two of them cost us a session on 2026-08-12 alone:

- A policy block is indistinguishable from a timeout, so the recovery ladder burned
  ~90s a go on a prompt that could never pass.
- `flow_create_character_from_media` shipped needing an exact `mediaTitle` with **no tool
  that can list media** — the title was only knowable from a DOM snapshot.

This plan closes those, plus the video path, which today calls **zero** `flow_*` tools.

## The hard constraint that shapes everything

**There is one logged-in browser and it is strictly serial.** Coding agents can write
code and unit tests in parallel; they **cannot validate against Flow**. So:

- Wave A is written blind, against selectors already recorded in
  `docs/superpowers/flow-selectors.md` and `flow-video.md`. Its correctness bar is
  *typecheck + unit tests + selector fidelity to the maps*.
- Live validation is a **separate serial phase** (Wave B), run by one session with the
  browser, batching all of Wave A into one pass.
- Anything with **no recorded selectors cannot be written blind at all** — it needs a
  mapping spike first. That is exactly Frames-to-Video (§Wave C).

Do not let an agent "verify" its work by driving the browser. It will collide with
every other agent.

---

## Wave A — parallel, no browser

Ten tasks. Each is one agent. Grouped by file to avoid collisions: **A1–A5 touch
`flow-client.ts` + `server.ts`**, so they must be integrated in sequence even though
they are written in parallel — each agent returns a patch against `e00f648` and I
resolve. A6–A10 are independent.

### A1 · `flow_list_media` — the missing discovery tool

**Why:** `flow_create_character_from_media` and every "use that image" workflow need a
title, and nothing can produce one.

Add `listMedia(opts?: { query?: string; limit?: number })` to `FlowClient`. Open the
asset picker (`openAssetPicker()` already exists, `flow-client.ts:472`), read the
`role="option"` tiles, return `{ title, kind, mediaId? }[]`. Use the existing search box
(`getByRole('textbox', { name: 'Search assets' })`) when `query` is given. Close the
picker via `closeAssetPicker()`.

Extract the option-row parsing into `media-list.ts` as a pure function over scraped
`{ name, alt, src }` records + a `media-list.test.ts`. That is the testable half:
dedupe by title, strip the doubled accessible-name text ("Man in suit holding papers Man
in suit holding papers Image"), classify kind from the trailing label.

Register `flow_list_media({ query?, limit? })`.

### A2 · `POLICY_BLOCKED` — stop retrying prompts that can never pass

**Why:** documented as the single biggest time sink; `packages/flow-mcp/README.md:89`
already flags it as a known gap.

Flow renders a warning card. Confirmed strings (see `docs/flow/failure-modes.md` §A1):

- `This generation might violate our policies`
- `This Prompt Might Violate Our Policies About Generating Prominent People`

Add a `detectFailureCard()` probe polled **inside the existing generation waits**
(`waitForNewCanvas`, `waitForNewCanvases`, `waitForVideoClip`) so a block aborts fast
instead of running out the 90s clock. Throw `POLICY_BLOCKED`; map it in `toToolError`
with a hint pointing at the rewrite table.

Also distinguish the two *other* card states already documented in `flow-video.md:41-49`:
`scheduled … waiting in the queue` (benign — keep waiting) and `Oops, something went
wrong` (transient — retry path already exists).

Pure + tested: `failure-card.ts` — `classifyCard(text): 'blocked' | 'queued' | 'error' |
null`. This is the whole point of the task; get the classifier right and the wiring is
trivial.

### A3 · Projects — create, list, open by id

**Why:** no tool creates or enumerates projects, so it is a manual step in every plan,
and `flow-operator`'s documented recovery path is raw `curl` against the CDP endpoint.

- `flow_create_project({ name? })` — the `add_2 New project` button is already clicked
  internally by `ensureProject()` (`flow-client.ts:64`). ⚠️ **Renaming is documented as
  un-automatable** (`flow-selectors.md:275` — fill and keystrokes both revert on blur).
  So `name` is best-effort: attempt it, return the actual name and id, and say plainly in
  the tool description that the caller must accept what came back.
- `flow_list_projects()` — `SCRAPE_PROJECTS` in `project.ts` already returns every tile;
  it is currently consumed only for name matching. Just expose it.
- `flow_open_project` gains an optional `id`, navigating straight to
  `/project/<id>`. ⚠️ Known issue (`flow-selectors.md:269`): project tiles sometimes
  render without `<a href>`, breaking name matching entirely — id is the reliable path
  and this task is what makes it available.

### A4 · `model` and `aspect` on image calls

**Why:** `ensureModel` already takes a model argument; only the character tools can reach
it. And the research says iterate-cheap-then-spend-on-Quality, which needs per-call tier
control. Aspect has tabs mapped (`flow-selectors.md:174`) and no code path at all.

Add optional `model` and `aspect` to `flow_generate_image`, `flow_edit_image`,
`flow_generate_batch`, `flow_refine`. Thread through to `ensureImageMode(count, model,
aspect)`. Aspect tabs follow the same Radix `tabClick` pattern as the count tabs.

Reuse `modelAlreadySelected` for the short-circuit. Add `aspectAlreadySelected` to
`compose.ts` with tests — **and mind the same prefix trap**: `crop_16_9` vs `crop_9_16`
are not substrings of each other but `1:1` vs `21:9` style labels may be. Test it.

Note `refine()` currently calls neither `ensureProjectRoot()` nor `ensureImageMode()`
(`flow-client.ts:561`) — it relies entirely on prior session state. Adding parameters
means it must now assert them.

### A5 · Character reads

**Why:** we can write character info but not read it; cannot list characters; cannot
reach "Show history", which our own plan doc calls the undo mechanism. "Show Kai the
current portrait" has no tool behind it.

- `flow_list_characters()` — character cards carry the name as `img[alt]`
  (`flow-client.ts:204`).
- `flow_get_character({ name })` — returns `{ name, info, portraitMediaId, bodyMediaId? }`,
  optionally harvesting either view to a path. `openCharacterPage()` already exists.

### A6 · Video — honour `model`, and assert video settings

**Why:** `flow_generate_video` advertises a `model` parameter and **silently discards
it** (`flow-client.ts:748`, `_model` never referenced). Combined with the documented
"defaults RESET per project — a fresh project comes up as Omni Flash", the tool can
quietly produce an Omni Flash clip at the wrong aspect while the caller believes it
asked for Veo 3.1 Quality.

Add `ensureVideoSettings({ model?, aspect?, count? })` driving the `tune Settings` panel,
fully mapped at `flow-video.md:12-23`:

| Control | Selector |
| --- | --- |
| Open | `button "tune Settings"` (agent panel footer) |
| Model | `button "<model> arrow_drop_down"` under **Video generation default** |
| Aspect | `tab "crop_16_9 16:9"` / `tab "crop_9_16 9:16"` |
| Count | tabs `1x｜x2｜x3｜x4` |
| Confirm gate | `Always` (default) / `Never` |
| Save | `button "Save"` |

Model options as recorded: `Omni Flash`, `Veo 3.1 Lite`, `Veo 3.1 Fast`,
`Veo 3.1 Quality`, `Veo 3.1 Lite[Lower Priority]`.

⚠️ **`Veo 3.1 Lite` is a strict prefix of `Veo 3.1 Lite[Lower Priority]`** — the exact
bug `modelAlreadySelected` already guards for the Nano Banana tiers. Extract
`videoModelAlreadySelected` into `compose.ts` **with a test for this case**. Do not
hand-roll a substring check.

Assert settings at the top of `generateVideo`. Default to `Veo 3.1 Quality` only if the
caller passes nothing *and* we decide that is right — flag the credit implication (100
credits/clip) in the tool description.

### A7 · Video — hardened clicks and tile targeting

**Why:** the video path uses **zero** hardened click helpers for its three interactive
steps, in a file that declares "a bare click with default actionability is banned in this
file" (`flow-client.ts:117`).

Fix the three violations:

| Line | Call | Should be |
| --- | --- | --- |
| 792 | `more.click({ force: true })` — Radix menu trigger | `pointerClick` |
| 795 | `animate.click({ force: true })` — menu item | `forceClick` |
| 824 | `approve.click({ force: true })` — plain button | `forceClick` |

Also `tiles.nth(i).hover()` (`:787`) is coordinate-based, on a rig where coordinate input
is documented as untrustworthy.

Then fix the targeting itself — the standing "open rough edge" (`flow-video.md:166`):
`openAnimateMenu` hovers **every** tile and takes the first menu exposing Animate, which
"timed out on re-runs once the project filled with test media." **Target the
just-uploaded still specifically**: snapshot media names before upload (the pattern
`generateVideo` already uses at `:762`), and drive the menu for that one new tile rather
than scanning.

Map `ANIMATE_NOT_FOUND` in `toToolError` while here.

### A8 · Batch — `character`, and raise the cap

**Why:** `flow_generate_batch` has no `character` param and caps at 8, which will bite
during Phase 2 scene generation for GPOM/MMT.

Add `character` (reuse `submitWithCharacter`), `model`, `aspect`, `numOutputs`. Revisit
the cap of 8 — it is a schema choice, not a Flow limit; keep a cap but justify it in the
description. Batch is serial by nature so a higher cap is a longer call, not a heavier
one; make sure a mid-batch failure returns the items already harvested rather than
throwing everything away.

### A9 · Unmapped error codes

Three client sentinels fall through to generic `FLOW_ERROR`, so callers cannot branch:
`ANIMATE_NOT_FOUND` (`:800`), `SUBMIT_FAILED` (`:298`), `NOT_IN_PROJECT` (`:81`). Map all
three in `toToolError` with actionable hints. Trivial task; good first integration.

### A10 · Documentation sync

`packages/flow-mcp/README.md` lists **8 tools; there are 12** (soon ~20), and
`flow_create_character` is documented without `body`/`info`/`model`/`bodyOutPath`. It also
duplicates the policy-block guidance now owned by `docs/flow/failure-modes.md` — replace
the duplicate with a pointer.

`docs/superpowers/flow-selectors.md:88-105` still carries a superseded section claiming
"character panels need the reference attached via the UI (Playwright) for now", already
contradicted by the `character` param and by its own `:107` "SUPERSEDES the flow above".
Delete the dead section rather than leaving two truths.

---

## Wave B — live validation (serial, one browser, human-paced)

**Runs after Wave A is integrated.** One session, the real browser, working through a
checklist. This is where the code meets Flow for the first time.

1. `flow_status` green, project open.
2. Each Wave A tool once, against `magic-money-tree-story`, recording pass/fail and
   wall-clock.
3. **The two that matter most:** force a policy block (a prompt naming a real person)
   and confirm `POLICY_BLOCKED` returns fast rather than timing out; run
   `flow_list_media` and confirm its titles actually feed
   `flow_create_character_from_media`.
4. One video clip end-to-end with an explicit `model`, confirming the Settings panel was
   asserted and the clip came back at the requested tier. **Costs 100 credits** on
   Quality — do it once, deliberately.

Fix-ups from Wave B are small serial commits, not new agent work.

## Wave C — one video tool, several source modes

> **Revised 2026-08-12 (evening), after Wave B shipped and Kai ruled on scope.** The
> original Wave C is preserved in git history; this supersedes it. Three things changed:
> Wave B accidentally mapped the Frames entry point, Kai ruled that Frames and Animate are
> one feature and should be one tool, and batch generation is off the table.

### Rulings (Kai, 2026-08-12) — decided, not open

1. **Frames-to-Video and Animate are ONE tool, not two.** They are two tabs of the same
   popover and two ways of saying "make me a video from these stills". The tool takes an
   optional start image and an optional end image; **the mode follows from which are
   supplied**, and neither is required. No `flow_generate_video_frames`. If a second tool
   name ever seems necessary, it is a sign the modes were not genuinely unified.
2. **No batch animation, and no batch image generation for now.** Effort goes into making
   *single-image iteration* excellent, not into automating volume. `animate-slide` stays
   per-slide and human-paced; that line in its `## Out of scope` **stands** and is no
   longer an open policy question.
3. **Audio and voice are permanently out of scope.** Flow is a visuals tool for us. Do not
   re-scope voice selection, dialogue or audio track work into this plan.

### What Wave B changed about the spike

The original C1 opened "an exhaustive search found **zero selector knowledge** of Frames to
Video anywhere in the repo". That is no longer true. `smoke-compose-popover.ts` mapped the
compose-bar popover on 2026-08-12, and in **Video** mode it leads with two source tabs:

| Tab | Ligature + label |
| --- | --- |
| Frames | `crop_freeFrames` |
| Ingredients | `chrome_extensionIngredients` (**active by default**) |

So the entry point is known. What is still unmapped: the **first-frame and last-frame
slots** behind the Frames tab, and the submit path once both are filled.

### C1 · Spike — two questions, then map (live, timeboxed)

**Q1 — which mode is our existing `generateVideo` actually using?** It uploads a still and
fires the tile's `motion_blur Animate` menuitem, which attaches the image as a "source
frame" chip. Whether Flow treats that as **Ingredients** or as **Frames with only a first
frame** is genuinely unknown, and it decides the shape of the merged tool: if Animate is
already Frames-first-frame, the merge is nearly free and `startImage` is just the argument
we already pass. Settle this before writing anything.

**Q2 — is first+last frame really unavailable at our tier?**
`docs/flow/platform-controls.md` records first+last as ✅ on Veo 3.1 Lite and **"coming
soon" on Fast and Quality**. ⚠️ **That row is transcribed from Google's own documentation
and has never been tested by us** — it is not evidence, and it must not be "corrected" in
either direction until someone has opened the Frames tab on each tier and looked. Checking
it is minutes of work and it gates everything below, so do it first.

- If first+last works on Fast/Quality → the docs row is stale; fix it, note the date and
  that it was verified live, and build the full tool.
- If it is genuinely Lite-only → say so in `platform-controls.md` with the verification
  date, and decide whether a Lite-tier-only start+end mode is worth having at all. **"Not
  usable at our tier yet" remains a good outcome** — it stops us building on sand.

Then map the slots and write the selectors into `flow-video.md`, per the usual rule: every
resolved guess goes into the selector maps, or the next session re-learns it.

### C2 · Fold both source modes into `flow_generate_video`

Only after C1. One tool, one name, mode inferred from arguments:

```
flow_generate_video({
  motion, outPath,
  startImage?, endImage?,     // neither, either, or both — this selects the mode
  model?, aspect?, count?, durationSeconds?,
})
```

- **Neither image** — text-to-video.
- **Start only** — today's behaviour, and the one path that is already proven.
- **Start + end** — the panel-to-panel technique
  (`docs/flow/video-prompting.md` §4): art-direct page N and page N+1 as clean stills and
  let the video prompt carry only the connective camera move.
- **End only** — accept it if Flow supports it; do not invent a workaround if it does not.

**Backwards compatibility:** today's callers pass a positional `imagePath`. That becomes
`startImage`. Keep the existing behaviour byte-for-byte when only a start image is given —
`animate-slide` depends on it and it is the one video path with live proof behind it.

**⚠️ The prompt craft genuinely differs per mode, even though the tool does not.** An
Ingredients/start-only prompt describes *what moves*; a start+end prompt should name *only
the camera move connecting the two frames*, because the stills already carry the content
(`video-prompting.md` §4 is explicit, and adding scene description there makes drift
worse). The tool description must say this — descriptions are the agent-facing docs.

### C3 · Rewrite `animate-slide` onto the tools

The skill still drives the browser by hand throughout, so none of Wave A/B reaches it.
Replace:

- `## Flow engine` (:53-80) — the CDP curl checks, `flow-chrome.sh` launch, OAuth race
  workaround, signed-in screenshot → one `flow_status` call plus its existing
  `NOT_RUNNING` hint.
- `### Step 4: Drive Flow` (:178-187) — the whole step → one `flow_generate_video` call.
  Aspect pinning and polling become parameters and internal behaviour.
- `## Co-viewing` steps 1-3 (:90-98) — mechanical browser steps.

**Keep, explicitly** — these are judgement, not plumbing, and automation must not eat
them: `## Scope guard` (:26), `## Writing motion prompts` (:115, the only motion
prompt-craft we have), **`### Step 3 [GATE]`** (:173 — "do not proceed until the prompt is
explicitly approved"; this is the credit-spend gate), `### Step 5: Judge the clip` (:189),
`### Step 7` the `.tsx` swap (:233).

**`## Out of scope` (:331) stays as written.** Per ruling 2, batch animating a comic is not
becoming viable-and-therefore-default. Do not touch that line.

### C4 · Clip duration — the control nobody knew existed

Wave B found duration tabs (`4s` / `6s` / `8s` / `10s`) in the compose-bar popover's Video
mode. Nothing in the repo knew clip length was controllable, and there is no duration
control in the Agent Settings panel at all, which is why it was missed. `animate-slide`
has been taking Flow's 8s default by accident on every clip it has ever made.

- Add `durationSeconds` to `flow_generate_video`, driven through the popover.
- ⚠️ Per `platform-controls.md`, **10s is Gemini Omni Flash only**; the Veo 3.1 tiers cap
  at 8s. Asking for 10s on Veo must fail loudly, not silently deliver 8s.
- Expose it at `animate-slide`'s approval gate: clip length is a creative decision made
  with the motion prompt, and it is the one parameter that changes both cost and cut.

### Ordering

**C4 → C1 → C2 → C3**, and C3 last on purpose. C4 is small, self-contained and improves
every clip we make from now on. C1 is cheap and may end the Frames line entirely. C3 is
written once, against whatever video tool shape C1/C2 settle on, rather than rewritten
when Frames lands.

---

## Conventions every agent must follow

- **Never write a bare `.click()` or `.click({ force: true })`.** Use `forceClick`
  (plain React buttons), `pointerClick` (Radix menu/dialog triggers), `tabClick` (Radix
  tabs). The reasoning is at `flow-client.ts:115-126`.
- **Never use `waitForEvent('filechooser')`.** Use `uploadFiles(paths, reveal?)`.
- **Extract the fiddly logic and test it.** `flow-client.ts` has no test file by design —
  browser I/O is untestable here. Every label-parsing, classification or path-building
  decision goes in a small pure module beside it with a colocated `.test.ts`. Precedent:
  `compose.ts`, `canvas.ts`, `project.ts`, `harvest.ts`.
- **Watch for prefix traps in every label match.** "Nano Banana 2" ⊂ "Nano Banana 2 Lite";
  "Veo 3.1 Lite" ⊂ "Veo 3.1 Lite[Lower Priority]". Regex with a negative lookahead, and a
  test that proves it.
- **Tool registration shape is invariant** — see `flow_generate_video`
  (`server.ts:165-185`). `inputSchema` is a plain object of zod schemas, not
  `z.object({})`. Optional args spread conditionally. Descriptions are the agent-facing
  docs: write them long and instructional.
- **Run `npx tsc --noEmit` and `npx vitest run` before returning.** Both must be clean.
- **Do not drive the browser.** One logged-in browser, strictly serial; validation is
  Wave B.

## Verification

- Per agent: `npx tsc --noEmit` clean, `npx vitest run` green (39 tests today, each task
  adds its own).
- Per integration: same two, plus a read of the diff against the selector maps — the one
  thing unit tests cannot catch is a selector that is merely *plausible*.
- End to end: Wave B checklist above.
- Regression risk to watch: A4 changes `refine()` to assert mode where it previously
  assumed session state; A7 changes tile targeting on a path whose end-to-end flow is
  proven but whose targeting is not. Both want a deliberate look in Wave B.
