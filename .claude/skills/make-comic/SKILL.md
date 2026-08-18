---
name: make-comic
description: Use to take a BadCode comic from idea to a rendered comic in the browser as a gated, staged workflow — discuss & approve each stage, then produce. Triggers on "make a comic", "let's build the <x> comic", "turn this idea into a comic", "ideate a comic", "new comic from scratch", or any request to generate comic images / a storyboard via Google Flow. Composes new-story (canon) + Google Flow (images) + @badcode/comic (assembly).
---

# Make Comic (BadCode)

Take a comic from **idea → rendered comic in the browser**, run as a gated
workflow: each stage is *discuss → approve → produce*. Nothing is produced before
its stage is approved. This skill **composes** existing tools — it does not
duplicate them.

## Read first

- `CLAUDE.md` — what BadCode is and the repo map.
- `docs/voice.md` — load-bearing tone (sarcastic, dark, total authority; politics
  & economics first; story over sermon). All prose and captions match it.
- `docs/storytelling.md` — the method: one load-bearing idea, real grounding,
  beats. Don't reinvent it.
- The **`new-story`** skill — captures the `docs/stories/<story>/` canon. Stages 1, 2, 4
  delegate to its method.
- `packages/flow-mcp/README.md` — the `flow` MCP server (tools, prerequisites).
- `badcode-art-direction` skill — prompt craft + critique loop; invoked for every image.
- `packages/comic/AUTHORING.md` — **mandatory** before writing any comic `.tsx`
  in Stage 6.

## The six stages (each: discuss → approve → produce)

| # | Stage | Produces | Tool |
|---|---|---|---|
| 1 | Idea | `docs/stories/<story>/story.md` + `README.md` | new-story method |
| 2 | Characters | `docs/stories/<story>/characters/<name>.md` (+ visual `sheet` desc) | new-story method |
| 3 | Character images | a portrait + record per character | flow MCP + art-direction |
| 4 | Storyboard | `docs/stories/<story>/storyboard/index.md` + `pNN.md` (planned) | new-story method |
| 5 | Storyboard images | one image + record per panel | flow MCP + art-direction |
| 6 | Assemble | comic `.tsx` + manifest + route, verified rendering | @badcode/comic |

`docs/stories/<story>/` is the **source of truth**; the comic in `apps/web` is *derived*
(Stage 6). Worked reference: `docs/stories/magic-money-tree/` and
`apps/web/src/comics/magic-money-tree/`.

## Gating principle

Never run a *produce* step before the user approves that stage's *discuss*
output. After each stage, summarise what was produced and ask before proceeding.
This mirrors how `superpowers:brainstorming` gates its sections.

## Resume

Progress **is** the artifacts. On invocation, inspect `docs/stories/<story>/` and
continue at the first incomplete stage/panel:

- `story.md` / `characters/*` present → stages 1–2 done.
- a character whose `.md` has a recorded portrait → stage 3 done for it.
- `storyboard/pNN.md` with `status: done` → that panel done.

Resume; don't restart.

---

## Stage 1 — Idea

Discuss the concept and the single load-bearing political/economic idea, in the
BadCode voice. Take a fragment, reference, or existing material — **don't demand a
brief.** Using `new-story`'s method, write `docs/stories/<story>/story.md` (key concept,
background, high-level beats, the twist) and `docs/stories/<story>/README.md` (the
tracker).

**Gate:** present the spine; get approval before Stage 2.

## Stage 2 — Characters

Discuss each character. Using `new-story`, write `docs/stories/<story>/characters/<name>.md`
for **every named character** — each one becomes a Flow Character in Stage 3. Each
file must include a specific, class-coded **visual `sheet` description** in house
style (see `docs/voice.md` image direction; `docs/stories/camping/characters/` and
`docs/stories/magic-money-tree/characters/dawn.md` are worked examples).

**Gate:** approve the character descriptions before Stage 3.

---

## Stage 3 — Character images

Image generation is now deterministic via the `flow` MCP server, and prompt craft +
critique live in the **`badcode-art-direction`** skill — invoke it for every image.
Per image: the art-direction skill plans + critiques the prompt, calls
`flow_generate_image({ prompt, outPath })` (or `flow_refine` to correct in-session),
and records the prompt + revision in `docs/stories/<story>/storyboard/pNN.md`.

Prerequisite: the Flow browser up and logged in — see
[`docs/flow/operating.md`](../../../docs/flow/operating.md) §1. Do NOT puppeteer Flow via the
Playwright MCP by hand.

For **every named character**: invoke **`badcode-art-direction`** with the character's
`sheet` description; harvest the portrait to `docs/stories/<story>/characters/img/<name>.jpg`,
set the character file's `sheet:` frontmatter to that path, and append the **character
record** below.

**Gate:** show the portraits; reroll any the user rejects before Stage 4.

### Character record (appended to `characters/<name>.md`)

```markdown
**Flow Character:** id `<flow-character-id>` · model `nano-banana-2`

**Portrait prompt (exact):**
> <the description sent to Flow>

**Revisions:**
- v1 (<date>) — initial
```

---

## Stage 4 — Storyboard

Discuss the panel sequence (beats → panels). Write `docs/stories/<story>/storyboard/index.md`
(an overview: numbered panels, each with a one-line intent and which characters
appear) and one `docs/stories/<story>/storyboard/pNN.md` per panel with `status: planned`,
the planned scene, the narration/speech copy (BadCode voice), and the characters
in it.

**Gate:** approve the board before any image is generated.

### Panel record — `docs/stories/<story>/storyboard/pNN.md`

```markdown
---
panel: 3
characters: [dawn]
flow_media_id:                 # filled when generated
model: nano-banana-2
status: planned                # planned | done
asset_key: img/i03.jpg         # comic asset this panel renders as (badcode panel resolves via it)
---
![panel 3](img/p03.jpg)        # added when generated

**Prompt (exact, sent to Flow):**
> <exact prompt: house style + scene + cast every character by name>

**Narration:** "<caption / speech>"

**Revisions:**
- v1 (<date>) — initial
```

## Stage 5 — Storyboard images

Image generation is now deterministic via the `flow` MCP server, and prompt craft +
critique live in the **`badcode-art-direction`** skill — invoke it for every image.
Per image: the art-direction skill plans + critiques the prompt, calls
`flow_generate_image({ prompt, outPath })` (or `flow_refine` to correct in-session),
and records the prompt + revision in `docs/stories/<story>/storyboard/pNN.md`.

Prerequisite: the Flow browser up and logged in — see
[`docs/flow/operating.md`](../../../docs/flow/operating.md) §1. Do NOT puppeteer Flow via the
Playwright MCP by hand.

**Budget this stage for policy blocks.** Flow's usage filter silently blocks a large
share of prompts, and over CDP a block is indistinguishable from a timeout — on the
camping recut it was over half of all generations. Two no-candidate failures on a
healthy session means **rewrite the prompt, never retry**. Better: avoid the triggers
when *writing the storyboard*, not when generating — real brand names and legible
wordmarks, likeness phrasing, stacked destitution, institutional text. If a sign or
headline is load-bearing for a beat, plan it as a comic text overlay rather than baked
into the image. Rules + rewrite table: **`badcode-art-direction`** → "Usage-policy
blocks".

For each `pNN.md` with `status: planned`: invoke **`badcode-art-direction`**, casting
**every** character listed in `characters:` by name; generate, judge, and harvest to
`docs/stories/<story>/storyboard/img/pNN.jpg`. Then fill `flow_media_id`, set
`status: done`, embed the image, record the **exact prompt** used, and add a
revision line.

**Gate:** present a contact sheet of all panels; reroll weak ones before Stage 6.

---

## Fast slide loop: plan → batch → iterate

Work in batches, not one image at a time. `flow_generate_batch` opens the project once and
fires the whole list sequentially in one Flow session — roughly **12s an image** on the cheap
tier (measured 2026-08-12), so twenty slides is minutes, not an afternoon.

1. **Plan every prompt first.** Write the full prompt for every slide in the batch before
   generating anything, and get them agreed. This is the gate; everything after it is machinery.
2. **Batch-generate.** `flow_generate_batch({ prompts, outDir, resume: true })`. Always pass
   `resume: true` — see the loop below.
3. **Review all N frames together**, not one by one.
4. **Iterate only the weak ones.** A single slide is a cheap same-session follow-up:
   `flow_refine` with the correction, or `edit-panel` once it is a finished panel. Don't
   regenerate the batch.

### The unattended loop (how to actually leave it running)

A batch does not fail all-or-nothing. It returns `{ items, failed, partial }`, and the two
failure kinds mean opposite things:

- **`POLICY_BLOCKED` is about that one prompt.** The batch records it and carries on. It leaves
  a hole, and the hole is a prompt that needs **rewriting, never retrying** — the same prompt
  will be blocked forever.
- **Anything else** (`TIMEOUT`, `SUBMIT_FAILED`, a raw Playwright error) is about the
  **session**. The batch stops there deliberately, because a wedged page will fail the next
  prompt too.

So the loop is:

```
round 1: flow_generate_batch({ prompts, outDir, resume: true })
         │
         ├─ failed is empty ────────────────────────────────► done
         │
         ├─ POLICY_BLOCKED entries ──► rewrite those prompts in place
         │                             (badcode-art-direction → "Usage-policy blocks")
         │                             then re-run the SAME list, resume: true
         │
         └─ any other code ──────────► the session is hurt, not the prompt.
                                       flow_status, re-open the project, re-run
                                       the SAME list, resume: true
```

**`resume: true` is what makes re-running free.** It skips any prompt whose output file is
already on disk, so round 2 only pays for the holes. Same prompts, same `outDir`, every time.
Deleting one bad image and re-running regenerates exactly that one.

**Stop after three rounds** and report what is still missing. A prompt that survives two
rewrites is a storyboard problem, not a prompting problem — take it back to the human.

⚠️ **Never re-run a `POLICY_BLOCKED` prompt unchanged**, even in a later round. It cannot pass,
and it costs a full turn-timeout to learn that again.

⚠️ **Twenty prompts per call.** Longer lists get chunked; each chunk is its own loop.

⚠️ **Credits do not roll over and there are no top-ups** (`docs/flow/platform-controls.md` §2).
A long run can hard-stall until the billing cycle turns. We have never mapped what Flow's UI
does at zero credits, so expect it to look like a `TIMEOUT` — if a run starts failing at the
session level and `flow_status` is healthy, check the credit balance by eye before retrying.

**Budget this stage for policy blocks.** Flow's usage filter silently blocks a large share of
prompts, and over CDP a block is indistinguishable from a timeout — on the camping recut it was
over half of all generations. Better than any retry loop: avoid the triggers when *writing the
storyboard*. Real brand names and legible wordmarks, likeness phrasing, stacked destitution,
institutional text. If a sign or headline is load-bearing for a beat, plan it as a comic text
overlay rather than baked into the image. Rules + rewrite table: **`badcode-art-direction`**.

Precondition: the Flow browser is up and logged in (see
[`docs/flow/operating.md`](../../../docs/flow/operating.md) §1) and the project is opened with
`flow_open_project`. Prefer a
project that is not already full of test media.

---

## Stage 6 — Assemble

Derive the comic from the storyboard (`docs/stories/<story>/` stays the source). Read
`packages/comic/AUTHORING.md` first.

1. Copy storyboard images to `apps/web/public/comics/<slug>/img/iNN.jpg` (the
   source of truth stays in `docs/stories/<story>/storyboard/img/`). *[v1 path; migrating
   to the `badcode assets-build` bucket pipeline is a later follow-up.]*
2. Write `apps/web/src/comics/<slug>/assets.manifest.json`: `basePath`
   `"comics/<slug>"`, one asset per frame
   (`{ "thumbhash": "", "low": "img/iNN.jpg", "high": "img/iNN.jpg", "width", "height" }`).
3. Write `apps/web/src/comics/<slug>/<Name>Comic.tsx` with `@badcode/comic`:
   `createComic(manifest, { baseUrl: '' })`, one `<Page>` per panel, narration via
   `<NarrationBox>` (speech via `<SpeechBubble>`), and tasteful built-in
   effects/transitions (see `AUTHORING.md`).
4. Register in `apps/web/src/home/comics.ts`: import the component and add
   `'<slug>': <Name>Comic` to `liveComics` (route `/comics/<slug>`).
5. **Verify:** `npm run typecheck`; `npm run dev`; navigate the Flow browser to
   `http://localhost:5173/comics/<slug>` and screenshot the opener + one mid
   panel to confirm it renders.

**Gate:** show the rendered comic; the story is done when the user is happy.

---

## Iterating on an image

Editing an existing panel — *"take page 4 and change X"* — is the **`edit-panel`**
skill's job: it resolves the page to its record + golden image (`badcode panel`),
generates reference-anchored candidates with `flow_edit_image`, and maintains the
revision log. Invoke it instead of hand-rolling refine calls. (Character-sheet
records under `characters/` still iterate via `badcode-art-direction` + `flow_refine`.)

## Out of scope

- **Music.** Songs are the `suno-prompt` skill's job; only offer it as an optional
  follow-on after Stage 6.
- **Animating a panel.** make-comic produces static panels. Turning a finished
  panel into a Flow-generated scroll-scrubbed video is the **`animate-slide`**
  skill's job — reach for it after Stage 6, on a comic that has been migrated to
  the bucket pipeline (`basePath "comics-v2/<comic>"`).
- **Bucket-pipeline migration** for derived assets (a noted follow-up).
- **Fully-unattended runs.** The gates assume a human approving each stage.
