# @badcode/flow-mcp

MCP server that drives Google Flow over CDP to generate images/videos and harvest them to disk.

## Prerequisites
1. `./scripts/flow-chrome.sh` — launches Chrome on CDP `:9222` with the persistent
   `.flow-profile/`. Log into Google/Flow once in that window and leave it running.

## Tools

Ground truth is `src/server.ts` (each `server.registerTool(...)` call) — if this list and
the code ever disagree, the code wins; fix this file. Count them there rather than
trusting a number here — this list is being actively extended.

### Status & projects
- `flow_status()` → `{ loggedIn, projectOpen, url }`
- `flow_open_project({ name })` → opens an existing project by **exact name** (case-
  sensitive match against the projects grid). Errors `PROJECT_NOT_FOUND` if nothing
  matches. Returns `{ loggedIn, projectOpen, url }`.

- `flow_list_media({ query?, limit? })` → `{ title, kind, mediaId?, index }[]` for the open
  project's gallery, in gallery order. **This is how you get the `mediaTitle` that
  `flow_create_character_from_media` requires** — the gallery legitimately repeats titles
  (Flow auto-captions), so titles are never de-duplicated or suffixed; use `index` to
  disambiguate rather than editing the title text, which must match what the UI shows.

### Images
- `flow_generate_image({ prompt, outPath, character?, numOutputs? })` — `character` casts
  a project Character (make one first with `flow_create_character`) for cross-slide
  consistency without a reference-image upload. `numOutputs` (1–4, default 1) generates
  variants in one turn, saved with `-a`/`-b`… suffixes. Returns
  `{ path, mediaId, width, height }`; when `numOutputs > 1` the result also carries
  `candidates: [...]` and `partial: true` if fewer candidates landed than requested.
- `flow_edit_image({ prompt, referenceImages, outPath, numOutputs?, character? })` —
  uploads `referenceImages` (1–3 absolute paths, schema max) as prompt ingredients and
  applies a delta prompt. `numOutputs` defaults to 2. Always reference the golden
  original, not a previous edit output — chained edits accumulate artifacts. See
  "Reference images" below for why the schema allows 3 but practice uses 1. Returns
  `{ candidates: [{ path, mediaId, width, height }], partial? }`.
- `flow_refine({ prompt, outPath })` → `{ path, mediaId }` — a follow-up correction in the
  SAME Flow session. It does not assert a project or image mode of its own (no
  `ensureProjectRoot`/`ensureImageMode` call) — it trusts whatever state the prior call in
  this process left behind, so it only makes sense immediately after a
  `flow_generate_image`/`flow_edit_image` in the same session.
- `flow_generate_batch({ prompts, outDir, character?, numOutputs?, model?, aspect? })` —
  generates up to **20** images sequentially in ONE session (raised from 8 — a schema
  choice, not a Flow limit; batch is serial so a longer list is a longer call, not a
  heavier one, but there's no per-item timeout budget, so don't push past what one
  unattended call should reasonably run). Saves `<outDir>/00.jpg`, `01.jpg`, … (`-a`/`-b`…
  suffixes per prompt when `numOutputs > 1`, same convention as `flow_generate_image`).
  `character` casts one project Character into every prompt in the batch, via the same
  path `flow_generate_image` uses. Returns `{ items: BatchItem[], failed: BatchFailure[],
  partial: boolean }` — **not** a bare array, and **not** all-or-nothing. `items` is every
  prompt that completed (`{ index, prompt, path, mediaId, width, height, candidates?,
  partial? }`); `failed` is every prompt that didn't (`{ index, prompt, code, error }`).
  A `POLICY_BLOCKED` prompt is recorded in `failed` and the batch **keeps going** — that
  verdict is about the one prompt, not the session, and skipping it is what makes a batch
  useful for a mixed scene list. Any other failure (`TIMEOUT`, `SUBMIT_FAILED`, …) is
  recorded and the batch **stops there**, on the theory that it signals the page itself
  needs recovering, not that prompt-by-prompt retries would help. Either way nothing
  already harvested is thrown away; resume with `prompts.slice(items.length +
  failed.length)` once the cause is fixed. Never retry a `POLICY_BLOCKED` entry
  unmodified — rewrite it per `docs/flow/failure-modes.md`.

### Video
- `flow_generate_video({ imagePath, motion, model?, aspect?, count?, outPath })` — uploads
  `imagePath`, attaches it via the tile's Animate menu, applies the motion prompt, saves the
  `.mp4` to `outPath`. Returns `{ path, mediaId }`.
  **Tier and aspect are asserted per call** through Flow's `tune Settings` panel, because
  those defaults reset per project (a fresh project comes up as Omni Flash), so without the
  assertion a caller asking for Quality could silently get an Omni Flash clip.
  **`model` defaults to `Veo 3.1 Fast` (20 credits).** Lite is 10, **Quality is 100** — the
  spread is steep enough that defaulting to the top tier would risk a 5× spend nobody asked
  for, so Quality is opt-in. Override the default globally with `FLOW_VIDEO_MODEL`.

### Characters
- `flow_create_character({ name, refImages, body?, info?, bodyOutPath?, model? })` —
  creates a reusable, castable Character from one or more reference image paths. `body`
  runs Flow's native "Create Body" pass in the SAME call (describe build, posture,
  outfit) — a Character with both Portrait and Body binds identity noticeably better than
  a Portrait alone. `info` fills the free-text note Flow's own scene agent reads on cast,
  so it doesn't have to be repeated in every prompt. `bodyOutPath` saves the body render
  locally (meaningful only alongside `body`). `model` picks the generation tier. Cast the
  result later via `character` on the image tools above. Returns
  `{ name, bodyMediaId?, bodyPath? }`.
- `flow_create_character_from_media({ name, mediaTitle, body?, info?, bodyOutPath?, model? })`
  — same as `flow_create_character`, but the reference is a media item already IN the
  project gallery (e.g. a prior generation) instead of a fresh upload. Use this when the
  reference came from Flow itself — re-uploading a harvested image can 400.
  `mediaTitle` is the option's accessible name shown in the gallery (Flow's
  auto-caption, e.g. `"Man sitting with open book"`), **not** a file path or media id.
  Errors `MEDIA_NOT_FOUND` if nothing in the gallery matches. Returns the same shape as
  `flow_create_character`.
- `flow_character_body({ name, description, outPath?, model? })` — adds the full-figure
  Body view to an existing Character that only has a Portrait, via Flow's native "Create
  Body" pass. `description` should cover build, posture, outfit and setting. Errors
  `BODY_EXISTS` if the character already has one — use `flow_edit_character` instead.
  Returns `{ path, mediaId }`.
- `flow_edit_character({ name, prompt, target?, outPath?, model? })` — iterates on an
  EXISTING character's Portrait (default, `target: 'portrait'`) or Body
  (`target: 'body'`) view with a delta prompt, through the character editor — cheaper
  and more faithful than re-creating from a new reference, and each round is recoverable
  via the editor's own "Show history". Errors `NO_BODY` if `target: 'body'` is requested
  but no Body view exists yet. Returns `{ path, mediaId, target }`.
- `flow_character_info({ name, info })` — sets or replaces a Character's free-text note.
  Returns `{ name }`.

There is no `flow_list_characters` or a read/get-character tool yet — the Characters tab
in the Flow UI is the only way to enumerate what a project already has.

All `outPath` values are absolute; the server never decides where comic assets live.
The CDP attachment is cached across calls (reconnects automatically if Chrome restarts).

## Errors

Every failed call returns `{ error: true, code, message, hint? }` (built by `toToolError`
in `server.ts`). Codes a caller can branch on today:

| Code | Meaning | Hint |
| --- | --- | --- |
| `NOT_RUNNING` | Could not attach to Chrome on the CDP port. | Run `./scripts/flow-chrome.sh` and log into Google/Flow, then retry. |
| `TIMEOUT` | Flow did not finish generating in time. | A genuine slow/stuck generation. Policy blocks now return `POLICY_BLOCKED` instead, so this no longer means "probably blocked". |
| `PROJECT_NOT_FOUND` | No Flow project with that exact name. | Check the name in the Flow projects list. |
| `CHARACTER_NOT_FOUND` | No Character with that name in the open project. | Check the Characters tab; names are case-sensitive. |
| `BODY_EXISTS` | That character already has a Body view. | Use `flow_edit_character` with `target: 'body'` to change it. |
| `NO_BODY` | That character has no Body view yet. | Create one with `flow_character_body` first. |
| `MEDIA_NOT_FOUND` | No project media matches that title. | Use the exact accessible name shown in the project gallery, not a file path or media id. |
| `ANIMATE_NOT_FOUND` | No project media tile offered the Animate action. | The source still may not have finished uploading, or the tile is a video (its menu has no Animate). |
| `SUBMIT_FAILED` | The prompt was typed but Flow never accepted the submit. | Usually a wedged compose bar — reload the project URL (twice; the first load can throw a client-side exception) and retry. |
| `NOT_IN_PROJECT` | The page is not inside a Flow project. | Open one with `flow_open_project`, or pass a project id. |
| `POLICY_BLOCKED` | Flow flagged the generation as a possible policy violation. | **Never retry** — it can never pass. Rewrite per `docs/flow/failure-modes.md`, checking the Character name/info and reference image too, not just the prompt. |
| `FLOW_ERROR` | Fallback for anything not mapped above. | Read `message` — it carries the raw underlying error text. |

⚠️ `flow_edit_character` can also throw `NO_PORTRAIT` internally (`target: 'portrait'`
requested on a character with no Portrait view) — as of this writing that string has no
entry in `toToolError`, so it currently surfaces as `FLOW_ERROR` rather than a distinct
code. Treat any `FLOW_ERROR` whose message looks like a missing-view sentinel the same
way you'd treat `NO_BODY`.

## Reference images — schema ceiling vs. what actually works

Learned the hard way on the camping recut (2026-07-25); ignoring either produces a
`FLOW_ERROR` timeout that looks like Flow being down but isn't.

`flow_edit_image`'s schema allows up to **3** `referenceImages` — that's a ceiling picked
because it costs nothing to leave open, not a claim that 3 is reliable. In practice:

1. **Pass one reference image per call.** The upload path waits for each reference to
   appear in the asset dialog (`[role="dialog"] img[alt="<filename>"]`). With three
   references that wait reliably expires — observed
   `locator.evaluate: Timeout 30000ms exceeded` on the *second* image, every attempt.
   One reference succeeded first try, repeatedly. If a shot needs multiple anchors,
   pick the one that matters (usually the face) and put the rest in prose. Treat the
   schema max as "allowed, not validated" and the working number as 1.
2. **Downscale references before passing them.** Comic goldens are 5504×3072 PNGs at
   7–10 MB; uploading one blows the 90 s media wait
   (`waiting for locator('button:has(img[alt*="piece of media"])')`). Convert first:
   `convert in.png -resize 1600x1600\> -quality 88 out.jpg` (~200–500 KB). Quality of
   the result is unaffected — the reference is an ingredient, not the output.

**Generating *new* images with a character anchor:** cast a project Character via the
`character` parameter on `flow_generate_image` (create one first with
`flow_create_character`) rather than reaching for `flow_edit_image` — it drives Flow's
own Characters asset-picker internally and doesn't count against the reference-image
limits above. Reserve `flow_edit_image` + a single reference for editing an existing
image, not for casting a recurring character into a new one.

## Usage-policy blocks

**Triggers, the rewrite table, and the debugging procedure now live in
[`docs/flow/failure-modes.md`](../../docs/flow/failure-modes.md)** — that's the single
source of truth (also what the `flow-prompt` skill reads) and is more complete than what
used to be duplicated here. Read it before writing a prompt that might trip a filter.

What's genuinely specific to this server:

- **A policy block returns `POLICY_BLOCKED`, not `TIMEOUT`.** The generation waits poll
  Flow's status card every tick and classify it (`failure-card.ts`), so a block aborts in
  seconds instead of running out the 90s (or 8-minute video) clock. **Never retry a
  `POLICY_BLOCKED` call** — it can never pass. Rewrite per `docs/flow/failure-modes.md`,
  and check the Character name/info fields and the reference image, not just the prompt
  text: every field Flow reads is scanned.
- **The other two card states are handled, not confused with it.** `queued` ("waiting in
  the queue due to high demand") is benign and keeps waiting — note a `warning Failed`-looking
  icon can render while queued. `error` ("Oops, something went wrong") is transient; Flow
  re-posts the credit gate and the video path re-approves to retry.
- **Two-failure heuristic, still useful as a backstop:** if a call fails twice with no
  candidates and no `POLICY_BLOCKED`, and the session is otherwise healthy, glance at the
  Flow window — the card wording may have changed and `failure-card.ts` may need a new
  pattern.

**Separate concern — publication, not generation:** an image can pass generation and
still carry a brand-usage risk once it's in a comic (visible real signage, etc.). That's
a release decision for Kai, not something this server can catch.

## Recovering a wedged session

- **Client-side exception on project load** — Flow's project page intermittently dies
  with `TypeError: Cannot read properties of undefined (reading 'service')` and renders
  "Application error". A second navigation to the same URL fixes it. Always reload
  twice before concluding anything is actually broken.
- **Stale-tab drift** — calls can target a tab left on a *different* project, plus
  dangling `signin?error=OAuthCallback` tabs accumulate. Recover by opening a fresh tab
  straight at the project URL via the CDP HTTP endpoint (`PUT /json/new?<url>`),
  closing the stale ones, then confirming `flow_status` reports `projectOpen` at the
  URL you expect *before* retrying.
- **A wedged asset picker** (half-uploaded ingredients from a failed call) survives
  retries and poisons the next one. Reload the project page to clear it.
- `flow_open_project` matches on **exact name only**. A project you opened by URL is
  not addressable by a guessed name — that returns `PROJECT_NOT_FOUND` even though the
  project is open and healthy. Prefer navigating to the URL.

## Smoke test
`npx tsx packages/flow-mcp/src/smoke.ts` (needs a logged-in Flow window).
`npx tsx packages/flow-mcp/src/smoke-edit.ts [referenceImage]` proves the edit/ingredients path
(needs a project named `edit-smoke`).

Narrower, single-surface smoke scripts also live in `src/`: `smoke-status.ts`,
`smoke-core.ts` (generate + refine), `smoke-batch.ts`, `smoke-character.ts`,
`smoke-video.ts` — read each file's header comment for what it exercises and what
project/args it expects.

## Selector contract
`docs/flow/automation-images.md` (images) and `docs/flow/automation-video.md` (video).
If Flow's UI drifts, fix `src/flow-client.ts` and update those docs.
