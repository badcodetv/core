---
name: scene-images
description: Use for the IMAGE IDEATION of one BadCode scene — a mood board of cheap image options per beat in Flow, published as a voting page, run in rounds on Kai's notes until every beat has a pick, then turned into a storyboard of picked stills in rough shot order. Stage 2 of new-scene. Triggers on "mood board for <scene>", "image options for…", "show me looks for this beat", "another round of stills", "storyboard <scene>", "put the picks in order".
---

# Scene images: mood board → storyboard (BadCode)

**Stage 2 of a scene.** Cheap first looks, then the picked stills in order. Before it: **`scene-beats`**
(the brief). After it: **`scene-animation`**. The whole loop is **`new-scene`**, which also holds the scene
folder layout and `scene.json`.

## Read first

- The scene's `brief.md` and `scene.json`.
- **`shot-craft`**: what each shot should *be*, and any gate the story's `look.md` adds.
- **`flow-prompt`**: how Nano Banana behaves, and the policy blocks.
- **`flow-automation`**: driving the browser and recovering from failures.
- **The story's `look.md`** (`docs/stories/STYLE.md`): the only source of a look. LOCKED → every option sits inside it, plus at least one deliberate break. EMPTY → run `story-style` first (the story's look is found once, for the whole story). EXPLORING → the board is how the look gets settled: run the options as a `variations` round (`kind` = `flow`), and write the pick back into `look.md`.
- **`new-image`**: variety mode, casting, and the plan → critique → generate loop.
- **The scene's real-photo references** (`reference/`, `refs.json`; picked in `scene-beats` from `scripts/scene/unsplash-refs.py`, or pasted by Kai or Jack). No reference yet and the look is not LOCKED → offer the Unsplash picks page first (Kai, 2026-11-13: "give me some sentences, I'll search Unsplash and stick some examples on the artifact for you to pick from"). Hand the picked photo's path to every clean-room writer.

## The mood board

Cheap first looks: many options per beat, not finished frames. **Stills cost no credits** (Kai,
2026-10-20), so make options freely.

- Per beat, 3–6 prompts across different ideas *and* the styles from the brief. Write them with `flow-prompt`. Put every reference character in through its canonical image or Flow Character.
- Generate with `flow_generate_image` (new) or `flow_edit_image` (variations of an existing still: "Using the provided image, change only…"). Save to `<media>/moodboard/<id>.jpg`, using ids like `ST4-a`/`-b`/`-c` (beat letters + round number + candidate).
- Stage references in `~/.cache/…` and **never upload from `/mnt`**. Check candidates with md5; Flow sometimes returns duplicates.
- A **silent block looks like a vanished tile or a timeout**. Rewrite, don't retry. Known refusals:
  - any image with a child in it (mask the child out locally with ffmpeg `drawbox`, then edit-fill)
  - an open-mouth singing face
  - "sing"/"note" in video prompts
- Record every row in `moodboard.json` (`[beat, id, look, prompt, style?]`), blocked ones included. The Flow tools write each still's recipe card themselves (docs/provenance).
- Build the page with `python3 scripts/scene/build-moodboard.py <scene-dir> <out.html>` and publish it with `capabilities: {db:{}, user:{}}`. Republish to the **same file path** each round so the URL never changes. After each publish: `python3 scripts/provenance/prov.py trail <scene-dir> --stage moodboard --round N --url <url> --what "…" --rebuild "python3 scripts/scene/build-moodboard.py <scene-dir> <out.html>"` (this also records the URL in `scene.json`).
- Read votes and notes by **dumping them into the repo first**: `ArtifactData list` on `votes` and on `notes`, each with `out_dir` = `$(python3 scripts/provenance/prov.py feedback-dir <scene-dir> --stage moodboard --round N)`, then read the files. Kai often clicks his picks himself, so read them before writing any. Log it: `prov.py trail … --feedback --decided "<each pick or ruling, Kai's words>"`. The page is only the UI; the repo is the record (docs/provenance).
- **A few stills to choose between outside a mood board round** (a fix, a missing shot): a picks page, `scripts/scene/build-picks.py` from the scene's `picks.json`. Every image enlarges on click. Never hand-make a page.
- **Rounds:** a round answers Kai's notes, with new rows tagged by round. Keep going until every beat has a "This".
- **One round clears the whole board** (Jack, 2026-11-17). Dump every vote and note first, then answer ALL of them in
  the same round (every beat at once), never one note per round. Don't ask Kai or Jack to vote: read the page.
- **Clean room for new shots; quick rewrites for small fixes** (Jack, 2026-11-17). A new shot or a new idea gets a
  sealed writer. A small fix to an existing prompt ("make the poster bigger", "move the ambulance to the near lane")
  is a direct edit of that prompt, logged in the round's folder, no new writer.
- **The shared clean-room brief carries the look as ONE line** taken from `look.md`, never a paragraph; each shot's own
  facts (geometry, the face, the slogan) come first.

## Real photos first, sealed writers always (Jack, 2026-11-17)

- **Lean on Unsplash.** For anything real-world (a street, a junction, a vehicle interior, a building, a shelter),
  start from real photos: `python3 scripts/scene/unsplash-refs.py <scene-dir> "<query>" ...` and the picks page. A real
  photo carries correct physics, proportions and traffic for free; the generator only has to restyle it. Jack: "the
  Unsplash fix does seem to solve a lot of these problems".
- **Writers must not see the repo.** A `general-purpose` subagent loads the whole CLAUDE.md and the memory index
  (tested 2026-11-17), so a "sealed" writer is not sealed. Run every clean-room writer with
  `scripts/variations/sealed-writer.sh <round-dir> <brief files...> -- <output.json>` (an empty temp folder,
  CLAUDE.md and auto memory switched off; tested blank), or the `clean-room-writer` agent
  (`.claude/agents/clean-room-writer.md`, `omitClaudeMd: true`, loads after a session restart).
- **Brief from raw inputs only.** The shared brief is the human's words, the geometry map and ONE look line; never a
  paragraph of look wording copied from earlier prompts or briefs, and never earlier prompts as "evidence".

## Before a still reaches the board (Jack, 2026-11-17)

Priority Lane rounds 8-17 lost a round to every one of these. Each is a check, not a style rule.

- **One world map per scene.** Any scene with roads, traffic, rooms or a vehicle interior gets a `geometry.md`
  in its clean-room folder: every vehicle's lane, direction and which side it drives on (the UK keeps LEFT, the driver
  sits on the RIGHT), where each camera stands and which way it looks. Every writer of every shot in the scene gets the
  same map, so neighbouring shots agree. A writer who sees only their own shot invents the junction.
- **The physics check.** Before publishing, look at each still and answer: which way is every vehicle pointing, which
  lane is it in, is that the correct side, does it match the map and the shots either side, could the camera really be
  there (a van cab sits high; a bus stop is on the near kerb)? A still that fails is redone or labelled, never shown as
  if fine. Kai and Jack are not the physics checker.
- **A pick must pass the check before it becomes a reference.** A reference image's mistakes are copied into every
  shot made from it (HD14-c inherited CD8-b's wrong-way convoy).
- **Describe only what should be there.** Never name the thing to remove ("the cars coming toward us are gone"):
  naming summons it (same rule as Suno, memory "a ban loses to a positive instruction").
- **Keep the story's look to one short line.** The look belongs in `look.md`; in a prompt it is a few words, not a
  paragraph copied into every writer's brief. In rounds 8-17 one look sentence sat in ~55 of 69 prompts (avg 272 words)
  and buried the facts that mattered. Put the shot's own facts (geometry, the face, the slogan) first. Treat the
  same-prompt check's NEAR COPY / HABIT warnings as real: rewrite, don't wave them through.
- **A lookalike stays invented** only if the face is big and the prompt does not stack the real person's cues; a small
  face (a poster in a street) is made big first, then used as a reference. See `docs/google-flow/nano-banana-2.md`
  ("A small reference face on a poster…").
- **Reference results are checked automatically** by flow-mcp (`REFERENCE_COPY_ONLY`), but still look at each one.

## The storyboard

Put the picked stills into a rough order of frames. One frame is one shot, and a frame may hold two or
three candidate stills when Kai hasn't chosen yet. Write `storyboard.json`
(`{acts:[{id,title,beats}], frames:[{n, act, title, look, line?, stills:[ids], anim:n}]}`). The order is
rough; Kai re-cuts in Premiere anyway. The storyboard page is shown together with the animation
options, in `scene-animation`.

**Before showing anything, critique it** (shot-craft): does each frame step the argument, does every frame pass the gates in the story's `look.md`, does the sequence vary its scale (wide, close, insert)?

Log every pick and ruling in `picks.md` as it happens.
