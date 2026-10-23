---
name: scene-timeline
description: Use to CUT a BadCode scene or sequence and get it noted — voices, music and sound effects assembled with the picture outside Premiere, shown as a playable Premiere-style TIMELINE PAGE with a note slip on every beat, shot, line and sound, iterated round by round on Kai's notes (answered on the page), frozen when done, and built into Premiere as a new sequence when asked. Works on any cut with an edl, including ones assembled by their own script. Stage 4 of new-scene. Triggers on "timeline page", "give me the timeline to note", "cut it together", "rough cut", "voice it and score it", "read my notes on the timeline", "next round", "answer my notes", "put this cut on a timeline", "build it into Premiere", "this cut is done".
---

# Scene timeline: rough cut → notes → rounds (BadCode)

**Stage 4 of a scene, and usable on its own.** Before it: **`scene-animation`** (the clips). The whole
loop is **`new-scene`**; the film these timelines string together is the **`overview-board`**.

Kai, 2026-10-20: *"before we've even got to Premiere, we're actually cutting the timeline together with
speech, sound effects and video… it's really saving a huge amount of time."* The point is to **taste the
scene** with real voices and real sound, noted beat by beat, before any hand-cutting starts.

**Kai cuts the film himself.** This cuts a rough version *outside* Premiere (ffmpeg) so it can be noted,
and only builds it into Premiere as a **new sequence with a new name** (`<scene>-rough<N>`) when Kai asks.
Never place clips on, or rebuild, a timeline Kai is hand-cutting, and never rebuild a rough sequence after
he has edited it by hand (add your changes around his).

## Talk first

Agree the words (`script.json`: `{beats:[{id, title, see, lines:[{who, text, by: kai|claude, how?}], music, sfx}], voices:[{id, name, profile…}]}`,
every line tagged `by: kai` or `by: claude` so drafts are visible), the music cues and the spend (Suno
credits, any new Flow shots). The words have **one home**; every page and script reads them from there.

## Produce

Independent, so they can run side by side; one owner per tool:

| Layer | How | Rules |
| --- | --- | --- |
| **Voices** | Gemini TTS (`scripts/aistudio-tts.py`, docs/ai-studio): one voice per call, Google's four-part prompt, a TOWN for the accent | Casting test of 2–3 voices for any new role. Re-run a take that is too short for its words **or** has a dead-air gap over 2 s. Keep dry takes; filtered versions (`-fx`) for speakers, tannoys, walls. Lips to match: **`lip-sync-dub`** |
| **Music** | `suno-automation`: pairs at weirdness 30/60, workspace set, duration set | Covers ignore Duration (trim in the mix). **Record only the picks**, never download. Kai's credits. Add the sheet to the take's card (`prov.py card <wav> --merge --setting sheet=…`) |
| **Effects** | free and licence-checked by us (Freesound CC0 first, CC-BY with the credit recorded; no BBC, no NC, no ShareAlike), plus ffmpeg synths for pings, tones, ringing | `sfx/CREDITS.md` + `sfx/index.json` + a `prov.py card` each. Previews are fine for a rough; originals for the final |
| **New shots** | `scene-images` → `scene-animation` in miniature for any beat with no picture | contact-sheet every clip |

## Assemble (ffmpeg, no Premiere)

- **Picture is timed to the real voice lengths:** a lead-in before the first line (0.4 s), a gap between lines (0.35 s) and a tail after (0.6 s). Never slow speech. A shot too short for its words is chained, or played forward-then-back (`looped: true` in the edl, which the page stripes so Kai can see where it happens).
- **One stem per track**: each voice, each music cue, each effects group, all running from t=0. Ducks and drops are written into the stems, and each cue is measured at its moment, because nobody listens until Kai does.
- Write `<media>/cut/edl.json` in the **timeline format** (documented in `scripts/scene/timeline.py`), a reference mix and `preview.mp4`. Run `scripts/delivery-qc.sh` on anything rendered.
- **A cut made by its own script** (like GPOM's `scripts/gpom/second-half-video/cut3.py` and `ending/cut_end*.py`) only needs to write an edl in the same format; point `scene.json` `cut` at it and the rest of this skill applies unchanged.
- Worked example: GPOM second half cut 2 (`scripts/gpom/second-half-video/cut2.py`, `--cut2` on timing / extend / rough_audio / rough_place).

## The timeline page

`python3 scripts/scene/build-timeline.py <scene-dir> <out-dir>`, then publish `<out-dir>/index.html` with
every file in `<out-dir>/media/` and `capabilities: {db:{}, user:{}}`. Republish to the **same file path**
each round so the URL and the notes stay. After each publish:
`python3 scripts/provenance/prov.py trail <scene-dir> --stage timeline --round N --url <url> --what "…"` (records the URL as `boards.timeline`).

- What Kai gets: the cut playing, a beat row, V1 with thumbnails, every audio track A1…, a playhead, and underneath the beat under the playhead with every line, shot and sound in it, each with a note slip; plus notes pinned to an exact frame.
- Before showing a cut: `prov.py check <scene-dir>`, and card anything it lists.

## Rounds

- Read the notes with `ArtifactData` (collection `notes`, keys documented in `timeline.py`). Save them and pass `--notes` on that round's trail line.
- Turn them into **one fix list** sorted into words / voices / music / picture / timing, with the cost of each, and get Kai's go before re-assembling. Fixes knock on (a new line changes its length, which moves the picture), so batch them per round.
- 🔑 **Answer ON the page, then talk** (Kai, 2026-10-20: *"a weird Premiere feedback engine"*). Write the round into `<scene>/cut-notes.json` (`round`, `plan` = your read as a few short groups ending in a *You decide* group, `replies` = one answer per note key, and a `kai_round<N>` snapshot of the notes themselves), pass `round`/`plan`/`replies` into the timeline data, and republish to the same link: each note then shows *Claude's read* under it, and the plan sits at the top. Kai notes further or replies; the next round re-reads and adds. Worked example: GPOM `scenes/second-half-cut2-notes.json`.
- Worked example page: https://claude.ai/artifact/C3cZffUkuRUSMWQvHtKsXq (built by `scripts/gpom/second-half-video/build-timeline-page.py`, an adapter onto the same tool).

## Keep the film's board current

Every time a timeline page is made, changes state, or is replaced, update the scene's row in the story's
overview board (`docs/stories/<story>/timelines.json`), rebuild and republish (the **`overview-board`** skill).

## Done, and into Premiere

- **When Kai says a cut is done:** `python3 scripts/provenance/prov.py freeze <scene-dir> --note "<his words>"`, mark the row done on the overview board, and commit.
- **Into Premiere, when Kai asks:** a **new** sequence (`<scene>-rough<N>`), media imported to its own bin, picture on V1, each stem on its own audio track, every call checked against the sequence name (premiere-automation law 8). Kai's open sequences are never touched. Plan the build with `python3 scripts/scene/premiere-plan.py <edl.json> <plan.json> [--skip <stem>]`: picture with in/out, one track per stem, each voice line as its own clip (with the stem's gain, filters and lip-sync stretches baked in), and silent copies of clips that carry their own audio. Worked example: GPOM `gpom-sh-{B,C,D,E}-rough1`.

## Replies

House output style: the outcome first, plain words, file paths written out in full (`D:\badcode-videos\…`),
what is on the timeline versus in a bin, and one clear next move.
