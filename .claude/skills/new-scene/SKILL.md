---
name: new-scene
description: Use to take one scene of a BadCode film from an idea to a cut, in four gated stages — (1) an interview that decides what the scene is and makes it interesting, (2) a mood board of image options turned into a storyboard of picked stills, (3) animation options per frame turned into Flow video clips, (4) a rough cut with voices, music and sound effects shown as a playable Premiere-style TIMELINE PAGE with a note slip on every beat, shot, line and sound, iterated on Kai's notes before anything goes into Premiere. Each stage ends on a shared page where Kai and Jack pick or note, and nothing is generated past a stage before its picks are in. Triggers on "new scene", "let's do a new scene", "make a scene for…", "mood board for <scene>", "storyboard <scene>", "animate the storyboard", "turn the picks into videos", "recut <scene> with new shots", "cut it together", "rough cut", "timeline page", "give me the timeline to note", "voice it and score it". Composes story-craft, shot-craft, flow-prompt, flow-automation, suno-automation and premiere-automation.
---

# New scene (BadCode)

Take **one scene** of a film from a conversation to a noted rough cut. This is the loop that made the
GPOM opening recut, the second half and the gaze sequence, and (stage 4) GPOM second half cut 2:

```
1 INTERVIEW  ──►  brief.md
                   │  Kai approves the brief
2 MOOD BOARD ──►  image options per beat ──► board page ──► Kai votes ──► rounds
  STORYBOARD ──►  picked stills in rough order ──► (shown with stage 3)
                   │  Kai picks the stills
3 ANIMATION  ──►  2–3 ways to animate each frame ──► storyboard page ──► Kai picks
  VIDEO      ──►  Flow clips ──► checked ──► imported to a Premiere bin ──► re-roll notes
                   │  Kai's go on the words and the spend
4 ROUGH CUT  ──►  voices + music + effects, picture timed to the real voices ──► edl.json + preview.mp4
  TIMELINE   ──►  timeline page ──► Kai notes beats, shots, lines, sounds, frames ──► rounds
                   ──► (when Kai asks) a NEW Premiere sequence built from the edl
```

**Gated.** Each stage is *talk → approve → produce*. Never spend video credits on a still Kai has
not picked (the still-approval gate). The one exception is when Kai says to proceed without him
("I'm on a call, just make it"): then make the call yourself, animate the best two so he still
chooses, and say so.

**Kai cuts the film himself.** Stage 3 ends at clips in a Premiere **bin**. Stage 4 cuts a rough
version *outside* Premiere (ffmpeg) so it can be noted on the timeline page, and only builds it into
Premiere as a **new sequence with a new name** (`<scene>-rough<N>`) when Kai asks. Never place clips on,
or rebuild, a timeline Kai is hand-cutting, and never rebuild a rough sequence after he has edited it by
hand (add your changes around his).

## Read first

- `CLAUDE.md`: what BadCode is.
- `docs/marketing/the-reader.md`: who the work is for. In particular, name the beneficiary and never raise automation fear unaimed.
- The story's canon: `docs/stories/<story>/README.md` and any scene files near this one.
- **`story-craft`** (stage 1): the sentence, but/therefore, every beat a step.
- **`shot-craft`** (stages 2 and 3): what each shot should *be*, the visible-cost gate on monumental shots, and darkness that reads as depth.
- **`flow-prompt`** (stages 2 and 3): how Nano Banana and Omni actually behave, and the policy blocks.
- **`flow-automation`** (stages 2 and 3): driving the browser and recovering from failures.
- **`premiere-automation`** (the end of stage 3): importing to a bin.
- `docs/video-fx/hybrid-method.md`: Veo animates with the camera locked, Premiere moves the camera, ffmpeg draws every word.

## Where things live

The words live in the repo and the media lives outside it (the clips/ convention).

| What | Where |
| --- | --- |
| Scene folder (words) | `docs/stories/<story>/scenes/<scene>/` |
| `scene.json` | config: titles, media root, Flow project, beats, board URLs |
| `brief.md` | stage 1's outcome |
| `moodboard.json` | rows `[beat, id, look, prompt, style?]`, one per still made, **including blocked ones** |
| `storyboard.json` | `{acts:[{id,title,beats}], frames:[{n, act, title, look, line?, stills:[ids], anim:n}]}` |
| `animation-options.json` | `{sequence_notes:[{rule,why,source}], frames:[{n, job, options:[{id, label, idea, lanes, veo_prompt, cut, seconds, risk}]}]}` |
| `video-jobs.json` | picks turned into Flow jobs (format in `scripts/scene/shots.py`) |
| `script.json` | stage 4: the words per beat `{beats:[{id, title, see, lines:[{who, text, by: kai\|claude, how?}], music, sfx}], voices:[{id, name, profile…}]}` |
| `picks.md` | append-only record of every pick, note and ruling, dated, Kai's words kept |
| `trail.json` + `notes/` | **provenance**: one line per page published (`prov.py trail`), with the notes snapshotted each round |
| `final.json` + `final-edl.json` | **provenance**: the finished cut, every shot and sound traced to its recipe (`prov.py freeze`) |
| Media | `/mnt/d/badcode-videos/<story>/clips/<scene>/` with `moodboard/<id>.jpg`, `video/<prefix>-<key>-<still>.mp4`, and stage 4's `voice/`, `sfx/`, `cut/` (`edl.json`, `preview.mp4`, `stems/`) |

`scene.json`:

```json
{
  "story": "gitpush-origin-master", "scene": "the-vault", "prefix": "vt",
  "title": "GPOM The Vault",
  "heading": "GitPush Origin Master <span class=\"tri\">▲</span> the vault",
  "moodboard_intro": "What this board is for, in plain words. Tap This, Maybe or No; leave a note per beat.",
  "storyboard_intro": "Frames in story order. Pick one still and one way to animate each.",
  "media": "/mnt/d/badcode-videos/gitpush-origin-master/clips/the-vault",
  "flow_project": "<Flow project id>",
  "beats": [{"key": "door", "at": "0:00", "name": "The door", "blurb": "What this beat must do."}],
  "existing": {"door": [["NOW-door", "On the timeline now (replace)", "moodboard/current/NOW-door.jpg"]]},
  "styles": {"threads": "1980s BBC 16mm"},
  "looks": {"news": "Bulletin realism"},
  "boards": {"moodboard": "<artifact url>", "storyboard": "<artifact url>", "timeline": "<artifact url>"},
  "cut": {"edl": "<media>/cut/edl.json", "preview": "<media>/cut/preview.mp4"}
}
```

Tools in `scripts/scene/`, all taking the scene folder:

| Tool | Does |
| --- | --- |
| `build-moodboard.py <dir> <out.html>` | the mood board page (votes and notes per beat) |
| `build-storyboard.py <dir> <out.html>` | the storyboard page (still and animation pick per frame, and a flip-through reel) |
| `shots.py <dir>` | the video job list (JSON) from the storyboard, the options and `video-jobs.json` |
| `run.mts <dir> [keys…]` | animates jobs in Flow in waves, harvests them, names them |
| `match.py <dir> [--apply]` | names harvested clips by matching their first frame to the plates |
| `build-timeline.py <dir> <out-dir>` | stage 4's timeline page from `cut.edl` + `cut.preview` (the format is documented in `timeline.py`) |

Worked examples, built before the tools were generalised: the GPOM opening recut
(`scripts/gpom/build-opening-*.py`, `scripts/gpom/opening-video/`,
`docs/stories/gitpush-origin-master/scenes/opening-recut-*`) and the second half
(`scripts/gpom/second-half-video/`).

## Provenance (every stage)

Kai, 2026-10-23: keep a trail good enough to **rerun the whole scene on a better model**. Full rules:
[`docs/provenance/README.md`](../../../docs/provenance/README.md). In this skill that means:
- **Cards are automatic** for Flow MCP stills and edits, `run.mts` clips, TTS voices and Suno `record`. Anything else you make
  (ffmpeg text or composites, effects, footage, a Suno take's sheet) gets `prov.py card` straight after.
- **After every publish** of a mood board, storyboard or timeline round, run `prov.py trail <scene-dir> --stage … --round N --url … --what "…"`.
  It also writes the link into `scene.json` `boards`. When you read Kai's notes, save them and pass `--notes`.
- **Before showing a cut**, run `prov.py check <scene-dir>` and card anything it lists.
- **When Kai says a cut is done**, run `prov.py freeze <scene-dir> --note "<his words>"` and commit it.
- **The story's overview board** (the **`overview-board`** skill, `docs/stories/<story>/timelines.json`). A scene usually starts as a row there, and its `beat` is stage 1's starting sentence.
  If the scene has no row yet, add one (with `"scene": "scenes/<scene>"`) by the time its first timeline
  page exists. Update its state whenever it changes, then rebuild with
  `scripts/provenance/build-timelines.py docs/stories/<story>` and republish to the URL in `timelines.json`.

## Stage 1: the interview

This works like planning a feature: a back-and-forth, **one or two questions at a time**, never a
questionnaire. Kai often talks in long voice notes, so pull the decisions out of them and play them back.

Settle these before anything is generated:

1. **Where it sits.** Which film, between which scenes, and how long? Is the music fixed? If so, cut points follow the track: note the drop timecodes and the BPM (174 BPM is 0.345s a beat).
2. **The one sentence.** What does this scene *argue*? Who benefits, by name or by role? (the-reader rules)
3. **The steps.** The rough sequence of what we see, each step changing something (but/therefore). Write the ending first.
4. **What makes it interesting.** Push past the first idea. For every beat, offer one bolder alternative: a different angle, a reveal, scale against a single human, a visible cost, a callback. Kai's best notes have come from contrast: "zoomed out, a vast parade ground", "a strobe, not a glow", "from outside, through the corner windows".
5. **Cast.** Which characters recur from elsewhere in the story? Find their canonical reference image and their Flow Character, if one exists (`flow_list_characters`). One reference per character, always the same one. The GPOM bot always refs `simulation/stills/s3/s3-bot-00b-a.jpg` and keeps the torn bunting.
6. **Look.** The register (house near-black, or a deliberate break such as 1980s BBC 16mm or advert-bright) and the styles worth trying as filters on the board.
7. **What exists.** Clips or stills already on the timeline that stay, or that must be beaten (they go in `existing` as dashed cards).

**Output:** `brief.md` (the sentence, the beats with timecodes, the cast with reference paths, the look,
and what is kept) plus `scene.json`. Play it back in plain words and get Kai's "yes" before stage 2.

## Stage 2: mood board → storyboard

**The mood board** is cheap first looks: many options per beat, not finished frames.

- Per beat, 3–6 prompts across different ideas *and* the styles from the brief. Write them with `flow-prompt`. Put every reference character in through its canonical image or Flow Character.
- Generate with `flow_generate_image` (new) or `flow_edit_image` (variations of an existing still: "Using the provided image, change only…"). Save to `<media>/moodboard/<id>.jpg`, using ids like `ST4-a`/`-b`/`-c` (beat letters + round number + candidate).
- Stage references in `~/.cache/…` and **never upload from `/mnt`**. Check candidates with md5; Flow sometimes returns duplicates.
- A **silent block looks like a vanished tile or a timeout**. Rewrite, don't retry. Known refusals:
  - any image with a child in it (mask the child out locally with ffmpeg `drawbox`, then edit-fill)
  - an open-mouth singing face
  - "sing"/"note" in video prompts
- Record every row in `moodboard.json`, blocked ones included. Build the page with `build-moodboard.py` and publish it as an artifact with `capabilities: {db:{}, user:{}}`. Republish to the **same file path** each round so the URL never changes, and record the URL in `scene.json`.
- Read votes and notes with `ArtifactData` (collections `votes`, `notes`). Kai often clicks his picks himself, so read them before writing any.
- **Rounds:** a round answers Kai's notes, with new rows tagged by round. Keep going until every beat has a "This".

**The storyboard** puts the picked stills into a rough order of frames. One frame is one shot, and a
frame may hold two or three candidate stills when Kai hasn't chosen yet. Write `storyboard.json`. The
order is rough; Kai re-cuts in Premiere anyway.

**Before showing anything, critique it** (shot-craft): does each frame step the argument, do the monumental shots carry a visible cost, does the sequence vary its scale (wide, close, insert)?

## Stage 3: animation → video

**Animation options.** For each frame, write 2–3 ways to animate it into `animation-options.json`. Each option gives:
- the *job* of the shot
- the lanes: what Veo does with the camera locked, what Premiere does to the camera, what ffmpeg draws
- the `veo_prompt`, or none if the option is post-only
- the cut in and out, the seconds, and the risk

Rules that have held:
- **Lock Veo's camera.** "The camera does not move." at the start and end. Premiere does every push, zoom and pan, eased (hybrid method).
- **Animate dramatically**: dive, storm, hard flashes. Not vague twinkle.
- **Few movers.** Omni struggles past about three moving figures. Give the motion to rain, haze, light and one actor.
- **Words are ffmpeg.** Never ask Veo for readable text.
- **Timed events** use timestamp brackets `[00:00-00:01]` in whole seconds. These place things roughly; Premiere puts them on the beat. Keep flashes at **3 a second or fewer** (photosensitivity).
- **6–8s clips.** Eight seconds is never a reason to cut a beat short: chain clips last frame to first instead. Long clips redraw the scene after a few seconds, so cut before that happens.

Build the storyboard page with `build-storyboard.py` and publish it the same way. Kai picks a still
and an option per frame (db `picks`, kinds `still`/`anim`). In the reply, **break each decision down
plainly**: the choice, what each option buys, and your recommendation. Kai has asked for this.

**Video.** Write `video-jobs.json` from the picks (`anim_picks`, `still_picks`, `skip` for kept or
post-only frames, `cast`). Then:

```bash
python3 scripts/scene/shots.py docs/stories/<story>/scenes/<scene>        # check the job list
FLOW_CDP_PORT=<port from flow_status> npx tsx scripts/scene/run.mts docs/stories/<story>/scenes/<scene> [keys…]
```

- Run it with `run_in_background` and wait for the notification. **One Flow user at a time**: never run the runner and a Flow MCP call together.
- Settings are fixed: Omni 1.1 Flash, Frames, 16:9, count 1 (`flow_generate_video` fails on Omni Frames; the runner is the route).
- **Check every clip before telling Kai.**
  - Make a contact sheet: `ffmpeg -i clip.mp4 -vf "fps=2,scale=480:-1,tile=4x4" -frames:v 1 sheet.jpg`.
  - Look at it for a redraw, a morph, extra people, or text slop.
  - Crop and enlarge the subject at the first, middle and last frames.
- Import the passing clips to the scene's Premiere bin (`premiere_import` with `bin`). Don't place them unless asked.
- **Re-rolls.** Kai's notes become `extra` rows in `video-jobs.json`, each with `key` like `12-r2`, the still, the duration, the new motion and `why` in his words. If a new still is needed, go back through a small stage-2 round first. Show all candidates and let him pick, unless he said to go ahead.

Log every pick and ruling in `picks.md` as it happens.

## Stage 4: rough cut → timeline page

Kai, 2026-10-20: *"before we've even got to Premiere, we're actually cutting the timeline together with
speech, sound effects and video… it's really saving a huge amount of time."* The point is to **taste the
scene** with real voices and real sound, noted beat by beat, before any hand-cutting starts.

**Talk first.** Agree the words (`script.json`, every line tagged `by: kai` or `by: claude` so drafts
are visible), the music cues and the spend (Suno credits, any new Flow shots). The words have **one home**;
every page and script reads them from there.

**Produce** (independent, so they can run side by side; one owner per tool):

| Layer | How | Rules |
| --- | --- | --- |
| **Voices** | Gemini TTS (`scripts/aistudio-tts.py`, docs/ai-studio): one voice per call, Google's four-part prompt, a TOWN for the accent | Casting test of 2–3 voices for any new role. Re-run a take that is too short for its words **or** has a dead-air gap over 2 s. Keep dry takes; filtered versions (`-fx`) for speakers, tannoys, walls |
| **Music** | `suno-automation`: pairs at weirdness 30/60, workspace set, duration set | Covers ignore Duration (trim in the mix). **Record only the picks**, never download. Kai's credits |
| **Effects** | free and licence-checked by us (Freesound CC0 first, CC-BY with the credit recorded; no BBC, no NC, no ShareAlike), plus ffmpeg synths for pings, tones, ringing | `sfx/CREDITS.md` + `sfx/index.json`. Previews are fine for a rough; originals for the final |
| **New shots** | stage 2–3 in miniature for any beat with no picture | contact-sheet every clip |

**Assemble** (ffmpeg, no Premiere):
- **Picture is timed to the real voice lengths:** a lead-in before the first line (0.4 s), a gap between lines (0.35 s) and a tail after (0.6 s). Never slow speech. A shot too short for its words is chained, or played forward-then-back (`looped: true` in the edl, which the page stripes so Kai can see where it happens).
- **One stem per track**: each voice, each music cue, each effects group, all running from t=0. Ducks and drops are written into the stems, and each cue is measured at its moment, because nobody listens until Kai does.
- Write `<media>/cut/edl.json` in the **timeline format** (`scripts/scene/timeline.py`), a reference mix and `preview.mp4`. Run `scripts/delivery-qc.sh` on anything rendered.
- Worked example: GPOM second half cut 2 (`scripts/gpom/second-half-video/cut2.py`, `--cut2` on timing / extend / rough_audio / rough_place).

**The timeline page.** `python3 scripts/scene/build-timeline.py <dir> <out-dir>`, then publish
`<out-dir>/index.html` with every file in `<out-dir>/media/` and `capabilities: {db:{}, user:{}}`, and record
the URL as `boards.timeline`. Republish to the **same file path** each round so the URL and the notes stay.
- What Kai gets: the cut playing, a beat row, V1 with thumbnails, every audio track A1…, a playhead, and underneath the beat under the playhead with every line, shot and sound in it, each with a note slip; plus notes pinned to an exact frame.
- Read the notes with `ArtifactData` (collection `notes`, keys documented in `timeline.py`). Turn them into **one fix list** sorted into words / voices / music / picture / timing, with the cost of each, and get Kai's go before re-assembling. Fixes knock on (a new line changes its length, which moves the picture), so batch them per round.
- 🔑 **Answer ON the page, then talk** (Kai, 2026-10-20: *"a weird Premiere feedback engine"*). Write the round into `<scene>/cut-notes.json` (`round`, `plan` = your read as a few short groups ending in a *You decide* group, `replies` = one answer per note key, and a `kai_round<N>` snapshot of the notes themselves), pass `round`/`plan`/`replies` into the timeline data, and republish to the same link: each note then shows *Claude's read* under it, and the plan sits at the top. Kai notes further or replies; the next round re-reads and adds. Worked example: GPOM `scenes/second-half-cut2-notes.json`.
- Worked example: https://claude.ai/artifact/C3cZffUkuRUSMWQvHtKsXq (built by `scripts/gpom/second-half-video/build-timeline-page.py`, an adapter onto the same tool).

**Into Premiere, when Kai asks:** a **new** sequence (`<scene>-rough<N>`), media imported to its own bin,
picture on V1, each stem on its own audio track, every call checked against the sequence name
(premiere-automation law 8). Kai's open sequences are never touched.

## Replies

Kai reads cold, often between calls. Every reply follows the house output style: the outcome first,
plain words, file paths written out in full (`D:\badcode-videos\…`), what is on the timeline versus in a bin, and one clear next move.
