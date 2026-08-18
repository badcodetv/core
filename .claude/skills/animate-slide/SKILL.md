---
name: animate-slide
description: Use to turn a single comic slide into a scroll-scrubbed video clip via Google Flow (image→video / Veo), then weave it into the comic. Triggers on "turn this slide into a video", "animate panel N", "animate this slide", "add motion to <panel>". Points at an existing bucket-pipeline comic; reuses the Flow video recipe (docs/superpowers/flow-video.md) + assets-build + @badcode/comic AnimationWidget.
---

# Animate Slide (BadCode)

Take a static comic panel and turn it into a **scroll-scrubbed video clip**, run as a gated
loop: *discuss the motion prompt → approve → produce*. Nothing is generated before the prompt
is approved. This skill operates on a **finished comic** one panel at a time; it does not
rebuild the whole thing.

Worked path: `docs/stories/<story>/storyboard/pNN.md` + `comics-v2/<comic>/anim/<key>/video.mp4` in
the bucket → `badcode assets-build` (renditions/poster/manifest) →
`<AnimationWidget animation={comic.resolveAnimation('anim/<key>')} />`.

## Read first

| File | Why |
|---|---|
| `CLAUDE.md` | What BadCode is; repo map |
| `docs/voice.md` | Load-bearing tone — applies to motion prompts too |
| `docs/superpowers/flow-video.md` | How the Flow video tools work underneath — selectors, the frame slots, the completion signal, the mp4 harvest. Reference material for when a call fails; not needed to run this skill. |
| `packages/comic/AUTHORING.md` | Mandatory before the `.tsx` widget swap |

## Scope guard — bucket pipeline only

**Before doing anything else**, open the target comic's manifest:

```
apps/web/src/comics/<comic>/assets.manifest.json
```

Check its `basePath`:

| `basePath` value | Status |
|---|---|
| `"comics-v2/<comic>"` | **In scope.** Continue. |
| `"comics/<slug>"` or `""` | **Out of scope. Stop.** |

If the manifest has `basePath: "comics/<slug>"` (or `baseUrl: ""`, images in `apps/web/public/`),
this is a **local/v1 comic**. Video requires the bucket pipeline — renditions, poster, and
`frameCount` come only from `assets-build`/`buildAnimation`. Explain to the user that the comic
must be migrated to the bucket pipeline first (a pre-existing make-comic follow-up) and stop.

**No `comic.meta.ts` is touched.** The source of truth for an animated panel is the storyboard
record (`docs/stories/<story>/storyboard/pNN.md`) and the generated `assets.manifest.json`. The runtime
does not read `comic.meta.ts` for animations; Karen's 9 working animations aren't declared there.
(Decided: YAGNI.)

---

## Flow engine (required before generating)

Video generation runs through the **`flow` MCP server**, not by driving the browser by hand.
Call `flow_status` once before producing:

- `{ loggedIn: true }` → you are ready.
- `NOT_RUNNING` → bring the browser up yourself; the recipe is
  [`docs/flow/operating.md`](../../../docs/flow/operating.md) §1. It renders via WSLg, so the
  user sees the window.
- `loggedIn: false` → ask the user to sign in; nothing else here will work.

Then open the working project once with `flow_open_project`. **Prefer a project that is not
full of test media**: the animate path identifies the still you just uploaded by diffing the
tile grid, and that diff degrades in a project holding dozens of items (observed failing with
`ANIMATE_NOT_FOUND` at ~30 items, 2026-08-12, and working immediately in a fresh project).
`flow_create_project` gives you a clean one.

For what the tools do underneath — the compose bar, the frame slots, the completion signal,
the mp4 harvest — see **`docs/superpowers/flow-video.md`**. You should not need it to run this
skill; read it when something fails.

---

## Co-viewing the comic (interactive mode)

When the user wants to **work on a slide together** — browse the comic, pick one, and iterate
on its motion — run this co-view setup first. The whole thing is automatable; don't make the
user start things by hand.

1. **Start the dev server yourself**, backgrounded: `npm run dev` (from repo root). Read the
   port from its output (`http://localhost:<port>/comics/<comic>`) — it's `5173` unless taken.
   **Print the URL** so the user can open it on their side too if they like.
2. **Ensure the shared browser** is up (`flow_status`; on `NOT_RUNNING` follow
   [`docs/flow/operating.md`](../../../docs/flow/operating.md) §1).
3. **Open the comic in the shared browser**: `browser_navigate` to
   `http://localhost:<port>/comics/<comic>`. This one Chromium is **both** what the user sees
   (WSLg) **and** what you screenshot (CDP) — so you're always looking at the same thing. When
   you scroll, it scrolls on their screen.
4. **Co-locate on a slide.** Scroll (`window.scrollTo` to a fraction of `scrollHeight`) and
   `browser_take_screenshot`; identify the slide by its bubble text. Discuss it in plain
   language until you agree on the target. Resolve it to `img/iNN` + page + new `anim/<key>`.
5. **Iterate the motion prompt in conversation** (see below) — gate before generating.
6. **Review in context** (loop step 7): after building in, switch to the comic tab, reload to
   pick up the new manifest, scroll to the slide, and screenshot **a few scroll positions** —
   the clip is scroll-scrubbed, so one screenshot is one frame; stepping the scroll gives a
   flip-book of the motion in the real comic. Then decide: accept, or iterate.

**Cheap-iteration rule:** judge the harvested clip (frames/scrub) **before** the upload+build
step — `assets-build` is the slow part. Only build in once the clip is right; refine weak ones
in the **same Flow session** first.

**Tabs:** keep the comic on one tab and Flow on another; `browser_tabs` to switch. Driving Flow
shows the user Flow; switching back to the comic shows them the result.

## Writing motion prompts

The motion prompt is **BadCode copy** — it must match `docs/voice.md`. The narrator is a
superintelligence from the future. Restraint is authority. Spectacle is weakness.

**The rule:** a motion prompt describes one deliberate camera or element move that *serves the
beat of the panel*. If the panel beats on silence, the prompt should be near-still. If it
beats on dread, a slow push-in. If it beats on collapse, a drift downward.

Where the beat allows, let the motion carry the **political/economic register** that drives
everything BadCode makes (`docs/voice.md`: inequality, automation, the machine's indifference,
the fiction of "we can't afford it"). The motion is an argument, not decoration — the slow
mechanical pan that doesn't care, the wealth piling while the room dims. Imply it; never
sermonise it.

| | Example | Why |
|---|---|---|
| **Good** | `"Slow push-in toward Karen's face; the fluorescent light flickers once, then holds. Everything else static."` | One move, serves the beat, restrained |
| **Good** | `"The screen text scrolls upward at a crawl; camera does not move."` | Zero camera spectacle; motion is in the world |
| **Good** | `"Embers drift upward from the left; the banner stirs once. Hold on the crowd."` | Atmosphere only; no hero moment |
| **Bad** | `"Dynamic zoom and spinning camera sweep across the office!"` | Spectacle for its own sake |
| **Bad** | `"Epic slow-mo explosion with lens flare and particle trails"` | Flashy; no political register |

A tween (`to` end-keyframe) is for a **deliberate visual argument** — the camera travels from
one position to another because the panel idea demands it. Not for motion variety.

Discuss the motion prompt with the user. Don't generate until it's approved.

---

## The gated per-slide loop

**Discuss → approve → produce.** Never generate before the motion prompt is confirmed.

### Step 1: Resolve the panel

Gather:

| Item | Where to find it |
|---|---|
| Comic id | given by the user (e.g. `karen`) |
| `basePath` | `assets.manifest.json` → `"basePath"` (must be `comics-v2/<comic>`) |
| Static image key | the `<ImageWidget src={comic.resolve('<imgKey>')} />` line for this page in `<Name>Comic.tsx` (e.g. `img/i05.png`) |
| Storyboard record | `docs/stories/<story>/storyboard/pNN.md` (may not exist yet — create it at step 8) |
| New animation key | choose `anim/<key>` not already in the manifest (e.g. `anim/a10` or `anim/i05` — any folder not present) |

If the user passes a `to` panel (end-keyframe tween), note its image key too.

### Step 2: Stage the source image

Download the source image locally so it can be uploaded to Flow:

```bash
gsutil cp gs://badcode-storage/comics-v2/<comic>/<imgKey> /tmp/animate-slide/src.<ext>
```

Confirm with `file /tmp/animate-slide/src.<ext>`. For a `to` tween, stage both images.

### Step 3: Discuss and approve the motion prompt [GATE]

Draft the motion prompt (see "Writing motion prompts" above). Present it to the user **with the
clip length**, and get both approved together. **Do not proceed to step 4 until the prompt is
explicitly approved.**

**Clip length is part of this gate, not a detail.** Flow offers **4 / 6 / 8 / 10 seconds** and
nothing between. Every clip made before 2026-08-12 was 8s because nobody knew the control
existed — do not inherit that by default. Propose a length with the prompt and say why: a
single held beat rarely needs more than 4s, and a scroll-scrubbed panel plays at the reader's
speed anyway, so longer mostly buys drift, not drama. It changes both the cut and the cost.

⚠️ **10s is Gemini Omni Flash only.** Every Veo 3.1 tier caps at 8s and asking for 10s there
fails outright (before spending credits) rather than quietly returning an 8s clip.

### Step 4: Generate the clip

One call:

```
flow_generate_video({
  startImage: "/tmp/animate-slide/src.jpg",   // the staged source frame
  motion:     "<the approved motion prompt>",
  outPath:    "/tmp/animate-slide/clip.mp4",
  aspect:     "16:9",              // match the comic page; "9:16" for portrait
  durationSeconds: 4,              // the approved length — 4/6/8, or 10 on Omni Flash only
})
```

It uploads the still, attaches it, applies the prompt, asserts the model/aspect/count/duration,
waits for the clip (no fixed sleeps) and saves the .mp4. Model defaults to Veo 3.1 Fast
(20 credits); pass `model` for a different tier and say so at the gate, since Quality is 100.

**For a tween, pass both frames instead of one.** `startImage` + `endImage` generates the
motion BETWEEN two stills — art-direct the two ends as clean panels and let the video carry only
the move between them. ⚠️ Then the prompt should name **only the connecting camera move**; the
two stills already carry the content, and describing the scene again makes drift worse. An
`endImage` needs a Veo 3.1 tier (Omni Flash rejects a last frame) and cannot be passed alone.

If it fails, read the error's `hint` — every failure mode here (policy block, wrong duration for
the tier, a frame Flow rejected) names its own fix. `POLICY_BLOCKED` in particular means
**rewrite, never retry**: see `docs/flow/failure-modes.md`.

### Step 5: Judge the clip

Read the poster or a sampled frame. Evaluate against:
- Does the motion serve the panel's beat?
- Does it match the BadCode voice (restrained, not flashy)?
- Technical: acceptable quality, correct aspect, no artefacts?

If weak, refine it rather than starting over:

```
flow_refine_video({
  mediaId: "<the mediaId the generate call returned>",
  motion:  "<the whole tightened prompt — not a delta>",
  outPath: "/tmp/animate-slide/clip-v2.mp4",
})
```

That re-runs the clip's own turn against the **same source frame**, which Flow re-attaches
itself — no re-upload, and it works even if the still is long gone. It returns `originalPrompt`,
so you can show the user exactly what changed. Tighten one thing at a time ("slower" / "less
camera" / "hold longer on the face"): each call is one generation and one charge, so changing
three things at once tells you nothing about which one worked.

Only go back to `flow_generate_video` if the **source still** is what's wrong.

### Step 6: Upload and build

Upload the clip into the comic's bucket as an animation folder. `assets-build` groups any
folder containing a file named exactly `video.mp4` into an animation keyed by that folder:

```bash
gsutil cp /tmp/animate-slide/clip.mp4 \
  gs://badcode-storage/comics-v2/<comic>/anim/<key>/video.mp4
```

Then rebuild renditions, poster, and manifest. **⚠️ Use an ABSOLUTE `-m` path.**
`npm run --workspace @badcode/cli` runs with its CWD set to `packages/cli/`, so a *relative*
`-m apps/web/...` silently writes the manifest to `packages/cli/apps/web/...` (the wrong
place). Anchor it to the repo root:

```bash
npm run badcode --workspace @badcode/cli -- \
  assets-build -s comics-v2/<comic> \
  -m "$(pwd)/apps/web/src/comics/<comic>/assets.manifest.json"
```

(Run from the repo root so `$(pwd)` resolves correctly.) Confirm the new entry landed — note
the manifest keeps animations under a top-level **`animations`** map (images are under
`assets`):

```bash
node -e "const m=require('./apps/web/src/comics/<comic>/assets.manifest.json'); const a=m.animations['anim/<key>']; console.log(a ? {renditions:a.renditions.length, frameCount:a.frameCount, fps:a.fps, poster:a.poster} : 'MISSING')"
```

Expected: renditions/poster/frameCount/fps present (not `MISSING`). If a stray
`packages/cli/apps/` tree appeared, you used a relative path — move the manifest to the real
location and `rm -rf packages/cli/apps`.

### Step 7: Assemble — swap the page

Read `packages/comic/AUTHORING.md` before editing. In `apps/web/src/comics/<comic>/<Name>Comic.tsx`,
replace the static line for this page:

```tsx
<ImageWidget src={comic.resolve('<imgKey>')} />
```

with:

```tsx
<AnimationWidget animation={comic.resolveAnimation('anim/<key>')} />
```

Ensure `AnimationWidget` is in the `@badcode/comic` import (Karen already imports it — copy
that pattern). Follow `AUTHORING.md` for any page-level `hold` / `effect` / `transition`
props; keep the rest of the page unchanged.

Verify:

```bash
npm run typecheck
```

Expected: passes. Then `npm run dev`, navigate to the comic, scroll to the swapped page, and
screenshot. Expected: the slide plays as a scroll-scrubbed clip.

### Step 8: Record

Write (or update) `docs/stories/<story>/storyboard/pNN.md`. Create `docs/stories/<story>/storyboard/` if it
doesn't exist. See the record format below.

---

## Record format — `docs/stories/<story>/storyboard/pNN.md`

```markdown
---
panel: <N>
image_key: img/<iNN>.<ext>         # the static source image in the bucket
anim_key: anim/<key>               # e.g. anim/a10
flow_media_id: <uuid>              # the Flow media name from getMediaUrlRedirect
model: <as Flow reports it>        # the model name from flow-video.md / the Flow UI
status: done                       # planned | done
---

**Motion prompt (exact, sent to Flow):**
> <the full approved prompt>

**Tween to:** img/<iMM>.<ext>      # only if a 'to' end-keyframe was used; omit otherwise

**Revisions:**
- v1 (<date>) — initial
```

This loop writes the record at **step 8 — after step 7 has confirmed the clip renders** — so
it lands as `status: done`. Only use `status: planned` if you are recording a panel you intend
to animate later (e.g. pre-planning alongside `make-comic`); flip it to `done` once it renders.

For panels that already existed as storyboard image records (from `make-comic`), add the
video block below the existing image record — do not erase prior history.

---

## Resume

Progress is the artifacts. On invocation for an existing panel:

| Artifact | Meaning |
|---|---|
| `pNN.md` has `status: done` AND the page renders `AnimationWidget` | Complete. Nothing to do. |
| `pNN.md` has `status: planned` OR `anim/<key>` absent from manifest | Incomplete — continue from the first missing step. |
| No `pNN.md` yet | Start from step 1. |

Do not restart completed work. Do not re-generate a clip that already renders correctly.

---

## Iterating — "just like that but change X"

1. Open `docs/stories/<story>/storyboard/pNN.md` and read the recorded motion prompt.
2. Re-prompt Flow in the **same session** if it is still open — "just like that but
   `<change>`". If the session is closed, start fresh from **step 2 of the loop** (re-stage
   the source image and re-upload it to Flow per `flow-video.md`) before re-prompting — a new
   Flow session has no reference image until you re-stage it.
3. Re-harvest the clip (follow `flow-video.md`).
4. Re-upload and re-run `assets-build` (step 6 above) — the manifest entry updates in place.
5. **Append a revision line** to the `pNN.md` Revisions log:
   ```
   - v2 (<date>) — <change description>
   ```
6. No `.tsx` edit needed unless the `anim/<key>` itself changed.

Touch only that one panel's record/clip. Leave the rest of the comic untouched.

---

## Out of scope

- **Local/v1 (`public/`) comics.** Must be migrated to the bucket pipeline first; this skill stops if `basePath` is not `comics-v2/<comic>`.
- **New `@badcode/cli` code.** `gsutil` + existing `assets-build` cover upload and rendition/poster generation.
- **`comic.meta.ts` / `@badcode/comic-meta` changes.** Not needed; Karen's existing animations work without it.
- **Batch animating an entire comic.** This skill is per-slide and human-paced by design.
- **Music.** Songs are the `suno-prompt` skill's job.
- **Building a comic from scratch.** That is `make-comic`'s job. Once `make-comic` has produced a comic and it is on the bucket pipeline, `animate-slide` can add motion to individual panels.
