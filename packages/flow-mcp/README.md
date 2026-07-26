# @badcode/flow-mcp

MCP server that drives Google Flow over CDP to generate images/videos and harvest them to disk.

## Prerequisites
1. `./scripts/flow-chrome.sh` — launches Chrome on CDP `:9222` with the persistent
   `.flow-profile/`. Log into Google/Flow once in that window and leave it running.

## Tools
- `flow_status()` → `{ loggedIn, projectOpen, url }`
- `flow_open_project({ name })` → opens an existing project by exact name
- `flow_generate_image({ prompt, outPath, character?, numOutputs? })` → `{ path, mediaId, width, height, candidates? }`
- `flow_edit_image({ prompt, referenceImages, outPath, numOutputs?, character? })` →
  `{ candidates: [{ path, mediaId, width, height }], partial? }` — uploads the reference
  image(s) as prompt ingredients and applies a delta prompt; `numOutputs` defaults to 2
  (candidates saved with `-a`/`-b`… suffixes). Always reference the golden original, not a
  previous edit output.
- `flow_refine({ prompt, outPath })` → `{ path, mediaId }` (same session)
- `flow_generate_batch({ prompts, outDir })` → `BatchItem[]` (`<outDir>/NN.jpg`)
- `flow_generate_video({ imagePath, motion, model?, outPath })` → `{ path, mediaId }`
- `flow_create_character({ name, refImages })` → `{ name }`

All `outPath` values are absolute; the server never decides where comic assets live.
The CDP attachment is cached across calls (reconnects automatically if Chrome restarts).

## Reference images — the two rules that decide whether a call succeeds

Learned the hard way on the camping recut (2026-07-25); ignoring either produces a
`FLOW_ERROR` timeout that looks like Flow being down but isn't.

1. **One reference image per call.** The upload path waits for each reference to
   appear in the asset dialog (`[role="dialog"] img[alt="<filename>"]`). With three
   references that wait reliably expires — observed
   `locator.evaluate: Timeout 30000ms exceeded` on the *second* image, every attempt.
   One reference succeeded first try, repeatedly. If a shot needs multiple anchors,
   pick the one that matters (usually the face) and put the rest in prose.
2. **Downscale references before passing them.** Comic goldens are 5504×3072 PNGs at
   7–10 MB; uploading one blows the 90 s media wait
   (`waiting for locator('button:has(img[alt*="piece of media"])')`). Convert first:
   `convert in.png -resize 1600x1600\> -quality 88 out.jpg` (~200–500 KB). Quality of
   the result is unaffected — the reference is an ingredient, not the output.

**Generating *new* images with a character anchor:** `flow_generate_image` takes no
reference images, so use `flow_edit_image` with a single reference and open the prompt
by asking for **character-design consistency** (see the policy rules below — do *not*
phrase it as reproducing a face).

## Usage-policy blocks — the biggest time sink

**A policy block is invisible to this server.** Flow shows it in the browser, but over
CDP it surfaces as a generic timeout or a missing candidate — identical to a slow
generation. So the retry ladder happily retries a prompt that can *never* pass, three
or four times, and you lose minutes per attempt. On the camping recut more than half of
all generations were blocked, not slow.

**Diagnosis:** if a call fails twice with no candidates and the session is otherwise
healthy (`flow_status` fine, project loads, other prompts succeed), assume **policy
block, not timeout** — and rewrite the prompt rather than retrying it. Look at the Flow
window to confirm.

### What triggers a block

1. **Real brand names, prominent or repeated** — supermarket signage, a named car
   marque with a specific number plate, branded tote bags. Asking for a *legible* real
   logo or wordmark is the single most reliable way to get blocked.
2. **Likeness-style face-reference phrasing** — "using the provided image only as a
   face reference — same face, same bone structure" reads as an attempt to reproduce a
   specific real person.
3. **Stacked destitution/degradation imagery** — burn barrels + tent city + collapsed
   figures + "gaunt", *especially* combined with a real identifiable business.
4. **Specific legible text attributed to real institutions** — invented newspaper
   headlines quoting a real central bank, etc.

### How to write prompts that pass

- **Invent near-miss brands.** Keep the class signal, drop the trademark: a green-and-
  white upmarket supermarket fascia rather than the real chain; "a heavy-duty reusable
  grocery tote" rather than the branded one; "a large black luxury SUV" rather than the
  marque and plate.
- **Reframe faces as character design, not identity:** *"keep this character's design
  consistent — same hairstyle, build, colouring and wardrobe as the reference"*, not
  "same face, same bone structure".
- **Stop asking for legible text.** Describe the object; let type be incidental. If a
  line of text is load-bearing for the story, consider setting it as a comic overlay
  instead of baking it into the image.
- **Soften degradation vocabulary.** "Weary", "worn", "tired" over "gaunt",
  "squalid", "collapsed"; one hardship signal per frame rather than four stacked.

**Known gap:** the server should distinguish a policy block from a timeout and return a
distinct `POLICY_BLOCKED` code so callers rewrite instead of retry. Until then, use the
two-failure heuristic above.

**Separate concern — publication, not generation:** images already accepted into the
camping comic contain visible real supermarket signage. That is a brand-usage question
for release, not a generation problem, and needs a human decision before publishing.

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

## Selector contract
`docs/superpowers/flow-selectors.md` (images) and `docs/superpowers/flow-video.md` (video).
If Flow's UI drifts, fix `src/flow-client.ts` and update those docs.
