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

### C1 · Spike — two questions, then map ✅ DONE 2026-08-12

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

**Answers, all by clicking:**

- **Q1 — Animate is neither tab.** It runs in the compose bar's **Agent mode**, which has no
  config popover at all; the Frames/Ingredients tabs belong to direct-generation mode. So the
  merge was not free, but it was clean: start-only keeps the Animate path, everything else goes
  through Frames.
- **Q2 — first+last works on EVERY Veo 3.1 tier**, not just Lite. The "coming soon" on Fast and
  Quality is stale documentation. Omni Flash rejects a last frame (End slot fills, then shows an
  error badge, which clears the instant you switch tier). **A last frame with no first frame is
  not a mode at all** — Flow flags it invalid on Fast and on Lite. `platform-controls.md`'s
  clip-length and first+last columns are now marked verified with the date.
- **The slots**: `[Start] [swap_horiz Swap first and last frames] [End]`, filled through Flow's
  media picker. Three silent traps (empty-vs-filled label, upload-does-not-select, and
  select-is-not-confirm) are written up in `flow-video.md` "Frames mode".

### C2 · Fold both source modes into `flow_generate_video` ✅ DONE 2026-08-12

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

**Shipped.** `generateVideo(req)` now takes one options object; `chooseVideoMode` picks the
path and `videoRequestError` holds every "Flow will refuse this" rule, both pure and tested
(`video-mode.ts`, 9 tests). End-only is refused up front rather than uploaded and rejected.

**Live proof, all four modes:** start-only 6.000s in a clean project (unchanged path,
regression-checked after the refactor); start+end 4.000s on Veo 3.1 Fast with its first frame
verified as the start still and its **last frame** as the end still; text-to-video a genuinely
new 4s clip; end-only correctly refused.

**Two bugs this found, both of which returned success:**

1. A text-to-video call came back with a healthy mp4 that was **byte-for-byte an older
   generation** — the media grid hydrates after page load, so the "before" snapshot was
   incomplete and an existing clip looked new. Caught by md5, not by reading the result.
   Fixed with `stableMediaNames` (wait for the count to settle).
2. A project load can render a **completely black page**, after which every later call fails
   with an unrelated-looking timeout. `reloadProject` now loads twice, which is the documented
   Flow workaround applied where it belongs.

**Worth knowing:** the start-only Animate path identifies its upload by diffing the tile grid,
and that **degrades in a cluttered project** — `ANIMATE_NOT_FOUND` at ~30 media items, working
immediately in a fresh one. The Frames path never touches the tile grid and has no such
weakness, which is an argument for eventually routing start-only through Frames too. Not done:
Animate is the path with the most live proof, and the ruling was to keep it byte-for-byte.

### C3 · Rewrite `animate-slide` onto the tools ✅ DONE 2026-08-12

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

**Shipped.** `## Flow engine` is now `flow_status` plus the launch fallback (and a warning to
work in an uncluttered project, per the tile-diff finding above); `### Step 4` is one
`flow_generate_video` call, with the start+end variant and its prompt-craft rule; co-viewing
step 2 uses `flow_status`. Kept exactly as they were: the scope guard, the motion-prompt craft,
the `[GATE]`, judging the clip, the `.tsx` swap, and `## Out of scope`. The gate now also
carries clip length, since that is a creative call made with the prompt.

### C4 · Clip duration — the control nobody knew existed ✅ DONE 2026-08-12

Wave B found duration tabs (`4s` / `6s` / `8s` / `10s`) in the compose-bar popover's Video
mode. Nothing in the repo knew clip length was controllable, and there is no duration
control in the Agent Settings panel at all, which is why it was missed. `animate-slide`
has been taking Flow's 8s default by accident on every clip it has ever made.

- Add `durationSeconds` to `flow_generate_video`, driven through the popover.
- ⚠️ Per `platform-controls.md`, **10s is Gemini Omni Flash only**; the Veo 3.1 tiers cap
  at 8s. Asking for 10s on Veo must fail loudly, not silently deliver 8s.
- Expose it at `animate-slide`'s approval gate: clip length is a creative decision made
  with the motion prompt, and it is the one parameter that changes both cost and cut.

**Shipped.** `flow_generate_video({ durationSeconds })`, the `maxDurationForModel` /
`parseVideoDuration` helpers in `compose.ts` with tests, `ensureVideoDuration` +
`assertVideoDuration` in the client, and the gate wording in `animate-slide`. Live proof: an
explicit `4` returned a 4.011s / 96-frame mp4 of the correct source still; a call omitting the
parameter, made in a project left sitting at 4s, returned exactly 8.000s.

Three findings, two of which change later tickets:

1. **⚠️ The Animate flow leaves the compose bar in AGENT mode, which has no config popover at
   all.** `ensureVideoSettings` goes through the Agent panel immediately before, so by the time
   Animate attaches the source chip there is no `crop_` trigger on the page — the first
   implementation timed out for 90s waiting on a control that cannot exist in that mode.
   Toggling the `Agent` pill fixes it, the source chip survives the toggle, and the trigger
   returns already in Video mode. **This matters for C2:** the Frames/Ingredients source tabs
   also live in that popover, so the merged tool works in direct-generation mode, and the
   Agent-mode toggle is a step every source mode will need. `flow-video.md`'s claim that
   "Animate switches the bar to Video mode … Agent toggle off" is only true when the bar was in
   direct mode to begin with; it is now corrected in place.
2. **10s is Omni Flash only, and the tab is ABSENT from the DOM on Veo — not disabled.** So a
   `click-if-present` would be a silent no-op billing for an 8s clip; the model rule is in code
   and throws before uploading anything. The duration column of `platform-controls.md`'s matrix
   is now marked verified (that column only — the first+last row is still C1's to settle).
3. **Duration persists on the project**, so an omitted `durationSeconds` asserts 8s rather than
   leaving the control alone. Otherwise one 4s clip would quietly make every later clip 4s.

**Deliberately not done:** the Video-mode popover also carries model, aspect and count, so
`ensureVideoSettings`' whole Settings-panel path could collapse into it. Tempting, out of
scope, and the Settings path is the one with live proof behind it. Revisit only if C2 needs it.

### Ordering

**C4 → C1 → C2 → C3**, and C3 last on purpose. C4 is small, self-contained and improves
every clip we make from now on. C1 is cheap and may end the Frames line entirely. C3 is
written once, against whatever video tool shape C1/C2 settle on, rather than rewritten
when Frames lands.

---

## What is left (L1–L4 worked through 2026-08-12; see each entry)

Waves A, B and C are done. Batch is proven, resumable and reports honest dimensions, and
`make-comic`'s "unattended loop" section documents the rewrite-and-retry cycle.

**L1–L4 are now all closed** — three built, one answered by testing:

| | | |
| --- | --- | --- |
| **L1** Video refine | ✅ built | `flow_refine_video`, live-proven |
| **L2** Extend / video Edit | ✅ answered | neither exists in this account's UI, on any tier |
| **L3** Unmapped failure states | ⏳ still unseen | but a timeout now records the page, so the next one is mappable |
| **L4** Animate's cluttered-project weakness | ✅ built | falls back to Frames, visibly (`via`) |

The one cell in `platform-controls.md` still transcribed rather than tested is
**Ingredients→Video**. Everything below is the detail, most valuable first.

### L1 · Video refine — "like that clip, but slower" — ✅ DONE 2026-08-12

Shipped as **`flow_refine_video`** (`refineVideo` + `openClipMenu` + `refineRequestError`).

What the probe settled, and it is more than was expected: **`Reuse prompt` restores the whole
turn** — the original prompt text, the **source still re-attached**, and the compose bar flipped
into Frames mode. So refine needs **nothing but the clip's mediaId**: the caller never has to
still hold the source image. Live-proven with one clip — a 6s corridor clip re-prompted from
"slow push in, light holds steady" to "slow pull back, light fades down"; the refined clip's
first frame is the original source still and its last frame follows the new prompt.

**`Add to prompt`** was also driven: it attaches the clip itself as a compose-bar ingredient,
landing as an `img` with the generic *"A piece of media generated or uploaded by you…"* alt —
which `scrapeReferenceChips` cannot see. Mapped, deliberately unused: Reuse restores a
known-good turn, an ingredient asks the model to interpret a video, and nothing we make needs
the latter. **No video *edit* was built**, so we stayed off the Omni-Flash pin.

Write-up: `docs/superpowers/flow-video.md` § "What an EXISTING clip offers" (incl. the clip
card's hover-swaps-the-thumbnail DOM trap, which breaks any code copied from `openAnimateMenu`).

### L2 · The two matrix rows still transcribed, not tested — ✅ TESTED 2026-08-12

Answer: **neither exists in this account's UI.** Two clips generated for the purpose (Veo 3.1
Lite, Omni Flash — the exact tiers the matrix claims them for), and the clip's hover menu came
back as the **identical eleven items** it shows on Veo 3.1 Fast. Nor are they on the clip's own
page: clicking a clip opens the **scene editor** (`/edit/<sceneId>` — a timeline with `Add
Clip`), whose controls include no Extend and no video Edit, and hovering the timeline reveals
none. `smoke-tier-menus.ts`, `smoke-clip-detail.ts`.

Recorded in `platform-controls.md` as "not present (2026-08-12)" rather than "false" — Google
gates features per account and per rollout, and this is one account on one day. But nothing
should be planned around either.

What Flow offers *instead* of Extend is that scene editor's `Add Clip` — chaining footage on a
timeline. A much larger surface than a per-clip action, and nothing we make has needed it, so it
is not proposed here. `Ingredients→Video` is now the only cell in the matrix still transcribed
rather than tested.

### L3 · Failure states we have never seen — ⏳ still unseen, but now self-recording

**Credit exhaustion** and **rate-limiting / recaptcha** still have no mapped card text, so
`classifyCard` cannot name them and they still surface as `TIMEOUT`. The strings are not
invented, per the ruling — but a timeout no longer throws away the evidence.

Every timeout now **writes down what was on screen**: `dumpLines` (pure, tested) filters Flow's
own chrome out of the page's leaf text, and the client saves it plus a screenshot to
`$TMPDIR/flow-timeout-<stamp>.txt/.png`, naming the path in the error message and in the MCP
hint. On a healthy page that is 13 readable lines, so a real failure message will be the obvious
one. Verified live without waiting eight minutes for a real timeout (`smoke-timeout-dump.ts`).

**What to do when one lands:** read the dump, add the exact wording to `failure-card.ts`, and the
state aborts in seconds from then on instead of burning the full timeout.

### L4 · Route start-only video through Frames — ✅ DONE 2026-08-12, as a fallback

Not switched — **fallen back to**, which keeps both properties. `generateVideo` catches exactly
`ANIMATE_NOT_FOUND` and re-runs the request through `framesToVideo`, so the happy path stays
byte-for-byte the code with all the live proof behind it (the ruling) and the one known failure
stops being fatal. The result carries `via: 'frames-fallback'` so the degradation is visible
rather than silent. It costs a stray uploaded tile from the attempt that failed.

⚠️ The weakness is **intermittent, not a size threshold** — the same ~30-item project completed
a start-only Animate call normally when re-tested. So the fallback was proven by *forcing*
`animateToVideo` to throw (`smoke-animate-fallback.ts`), not by waiting for a flaky project:
4.000s clip, opening on the still that was passed in. A test that just runs in a busy project
and passes proves nothing about the fallback.

### After the review (2026-08-12, prompted by "would this be fast in a new thread?")

An adversarial pass over the *iterate on images and videos together* workflow found four real
faults that L1–L4 had not touched. All fixed and live-proven:

| | What was wrong | Now |
| --- | --- | --- |
| **Asset picker** | Unreachable in video mode (`add_2 Create` does not exist there) — 90s timeouts on `flow_list_media`, character creation and every reference attach after any clip | `@` fallback, which works in every mode |
| **Media listing** | Showed only what the current mode can USE: zero clips in video mode | `listMedia` asserts image mode first |
| **`count`** | A lie: the tab was never clicked and the harvest took the first clip only | Popover tab + asserted + all candidates harvested |
| **Characters** | Assumed impossible in video; the two helpers that would have proved otherwise both hung on stale waits | `flow_generate_video({ character })`, mechanism proven |

The one thing that did NOT change: for a character who must look right, animate an art-directed
still. A text mention does not pin a likeness.

### Explicitly NOT on this list

Batch video (ruling 2), audio and voice (ruling 3), and a second video tool name (ruling 1).

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
