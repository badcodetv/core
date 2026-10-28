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
- **`shot-craft`**: what each shot should *be*, the visible-cost gate on monumental shots, darkness that reads as depth.
- **`flow-prompt`**: how Nano Banana behaves, and the policy blocks.
- **`flow-automation`**: driving the browser and recovering from failures.
- **`new-image`**: the house look (near-black, one thin light), and how to break it on purpose.

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

## The storyboard

Put the picked stills into a rough order of frames. One frame is one shot, and a frame may hold two or
three candidate stills when Kai hasn't chosen yet. Write `storyboard.json`
(`{acts:[{id,title,beats}], frames:[{n, act, title, look, line?, stills:[ids], anim:n}]}`). The order is
rough; Kai re-cuts in Premiere anyway. The storyboard page is shown together with the animation
options, in `scene-animation`.

**Before showing anything, critique it** (shot-craft): does each frame step the argument, do the monumental shots carry a visible cost, does the sequence vary its scale (wide, close, insert)?

Log every pick and ruling in `picks.md` as it happens.
