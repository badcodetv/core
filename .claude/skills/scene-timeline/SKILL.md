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
and builds it into Premiere as a **new sequence with a new name** (`<story>-<order>-<part>-r<N>`, below) the first time Kai asks.
**From then on, every round lands on the page and in Premiere together** ("No split brain", below).
Never place clips on, or rebuild, a timeline Kai is hand-cutting, and never rebuild a rough sequence after
he has edited it by hand (add your changes around his).

## Talk first

Agree the words (`script.json`: `{beats:[{id, title, see, lines:[{who, text, by: kai|claude, how?}], music, sfx}], voices:[{id, name, profile…}]}`,
every line tagged `by: kai` or `by: claude` so drafts are visible), the music cues and the spend (Suno
credits, any new Flow shots). The words have **one home**; every page and script reads them from there.
A whole dialogue that needs rewriting (too long, lecturing, not landing) goes through **`scene-dialogue`**
first: options ranked on a dialogue page, Kai picks, the picks land here to be voiced.

## Produce

Independent, so they can run side by side; one owner per tool:

| Layer | How | Rules |
| --- | --- | --- |
| **Picking takes** | a picks page: write the options into the scene's `picks.json` and build it with `scripts/scene/build-picks.py` (never hand-made; images enlarge on click, audio and video play in place, Suno takes link out) | dump `picks` into `feedback/` before reading |
| **Voices** | Gemini TTS (`scripts/aistudio-tts.py`, docs/ai-studio): one voice per call, Google's four-part prompt, a TOWN for the accent. **Who each character sounds like is the story's `sound.md` §Narration / voices**; a new role's pick is written back there | Casting test of 2–3 voices for any new role. Re-run a take that is too short for its words **or** has a dead-air gap over 2 s. Keep dry takes; filtered versions (`-fx`) for speakers, tannoys, walls. Lips to match: **`lip-sync-dub`** |
| **Music** | `suno-automation`, inside the story's `sound.md` (no house genre or settings; empty → a `variations` round): workspace set, duration set | Covers ignore Duration (trim in the mix). **Record only the picks**, never download. Kai's credits. Add the sheet to the take's card (`prov.py card <wav> --merge --setting sheet=…`) |
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
`python3 scripts/provenance/prov.py trail <scene-dir> --stage timeline --round N --url <url> --what "…" --rebuild "python3 scripts/scene/build-timeline.py <scene-dir> <out-dir>"` (records the URL as `boards.timeline`).

- What Kai gets: the cut playing, a beat row, V1 with thumbnails, every audio track A1…, a playhead, and underneath the beat under the playhead with every line, shot and sound in it, each with a note slip; plus notes pinned to an exact frame.
- Before showing a cut: `prov.py check <scene-dir>`, and card anything it lists.

## Rounds

- **Dump the notes into the repo before reading them** (the page is only the UI; the repo is the record): `ArtifactData list` on `notes` with `out_dir` = `$(python3 scripts/provenance/prov.py feedback-dir <scene-dir> --stage timeline --round N)`, then read the files (keys documented in `timeline.py`). Log it with `prov.py trail … --feedback`, adding `--decided "<Kai's words>"` for each ruling once he gives his go.
- Turn them into **one fix list** sorted into words / voices / music / picture / timing, with the cost of each, and get Kai's go before re-assembling. Fixes knock on (a new line changes its length, which moves the picture), so batch them per round.
- 🔑 **Answer ON the page, then talk** (Kai, 2026-10-20: *"a weird Premiere feedback engine"*). Write the round into `<scene>/cut-notes.json` (`round`, `plan` = your read as a few short groups ending in a *You decide* group, `replies` = one answer per note key, and a `kai_round<N>` snapshot of the notes themselves), pass `round`/`plan`/`replies` into the timeline data, and republish to the same link: each note then shows *Claude's read* under it, and the plan sits at the top. Kai notes further or replies; the next round re-reads and adds. Worked example: GPOM `scenes/second-half-cut2-notes.json`.
- Worked example page: https://claude.ai/artifact/C3cZffUkuRUSMWQvHtKsXq (built by `scripts/gpom/second-half-video/build-timeline-page.py`, an adapter onto the same tool).

## Keep the film's board current

Every time a timeline page is made, changes state, or is replaced, update the scene's row in the story's
overview board (`docs/stories/<story>/timelines.json`), rebuild and republish (the **`overview-board`** skill).

## Done

**When Kai says a cut is done:** `python3 scripts/provenance/prov.py freeze <scene-dir> --note "<his words>"`, mark the row done on the overview board, and commit.

## Premiere sync: the page drives a sequence (Kai, 2026-10-26)

Once a page has been built into Premiere, **the page stays the place Kai notes** (*"I don't want to detach
from this timeline artifact… I can just play the video in the timeline and feed back to you in situ"*), and
every round of notes lands in Premiere as well. Each timeline page drives **exactly one current sequence**
(a reel page drives its parts' sequences), and the story's overview board shows that map.

### 🔑 No split brain (Kai, 2026-10-27)

*"What I don't want to do is create a split brain where the timeline artifact becomes stale and everything
now is just in Premiere… we should always be keeping the timeline and Premiere synced with the feedback so
that we don't diverge that much."* The page and the sequence are **two views of one cut**. So:

1. **A round is not finished until both match.** Once a scene is in Premiere, every round of notes ends with
   the page republished **and** the next `…-r<N+1>` built, and `premiere-check.py` saying **in sync**. Leave a
   scene **page ahead** only when Kai has said to hold Premiere (he's cutting in it, or wants to see the page
   first), and say so in the reply.
2. **Edits flow both ways.** When the check says **edited in Pr**, Kai has cut by hand. Never build over it,
   and never leave the page behind it either: list his changes, write them into the edl as the next round
   (marked `by: kai, in Premiere`), rebuild and republish the page so it plays his cut, and log the round.
   His Premiere edit is then the base the next round builds on. Never ask him to re-note on the page
   something he already did in Premiere.
   📎 There is no pull-back script yet: port his changes by hand from the state dump. `premiere-check.py`
   compares only the picture on V1, so ask him whether he moved any sound by hand as well.
3. **Words are a round like any other.** New lines from `scene-dialogue` go script → voices → edl → page →
   sequence in one round, not page now and Premiere later.
4. **Every round's reply ends with the sync line**, per scene: `page round N · <sequence> · in sync`.

### The record

`scene.json` `premiere` holds one record per build plus a pointer to the current one:

```json
"premiere": {
  "current": "rough2",
  "rough1": {"sequence": "gpom-sh-B-rough1", "guid": "…", "bin": "gpom-sh-B-rough1", "built": "2026-10-23",
             "project": "/mnt/d/…/gpom-story.prproj", "stale": "why it must not be used, if so"},
  "rough2": {"sequence": "gpom-sh-B-rough2", "guid": "…", "bin": "gpom-sh-B-rough2", "built": "2026-10-23",
             "edl": "/mnt/d/…/cut3/B/edl.json", "what": "Kai's picks in", "how": "premiere-plan.py --tag rough2",
             "check": {"at": "…", "state": "in sync", "why": ""}}
}
```

Write it the moment a sequence is built; the board reads it (`overview-board`, "Premiere map").

### The check: is Premiere still what the page says?

Before every Premiere step, read the sequence (`premiere_get_sequence({name, params:false})`, which never
switches Kai's tab) and run `python3 scripts/scene/premiere-check.py docs/stories/<story> --write`:

| State | Means | Do |
| --- | --- | --- |
| **in sync** | V1 shots, trims, starts and length match the edl | build the next round |
| **page ahead** | notes answered and the edl rebuilt, not yet in Premiere | build the next round |
| **edited in Pr** | Kai has worked on the sequence by hand | 🔴 **never build over his hands.** Show him the differences, then pull them back into the edl and the page ("No split brain", 2) |
| **no state** | the sequence hasn't been read | read it, run again |

Effects Kai adds are only seen in a dump read with `params` on; read that way when it matters.

### A round on a page that is already in Premiere

1. **Dump, read, answer on the page** exactly as in Rounds above.
2. **Sort every note** in the fix list into:
   - **edit only**: a trim, a move, a swapped take, a dropped or reordered shot, a line nudged or re-levelled, a stem's gain. Nothing is generated; it's a new edl.
   - **new material**: a new voice take, music cue, still or clip. The usual gates apply (stills before video, Suno credits are Kai's).
   Say which kind each one is in its reply, so Kai sees the cost.
3. **Re-assemble, rebuild the page, republish** to the same link, and log the round.
4. **Check** (above). In sync or page ahead: build **`…-r<N+1>`** from the new edl. Never edit the current sequence in place and never reuse a name; every round stays undoable.
5. **Move the pointer**: add the new record, set `current`, and give the old one `stale` if a later build overwrote its media. Close the old tab and open the new one in its film-order slot (below).
6. **Answer back**: each note that reached Premiere gets "→ in `<sequence>`" on its reply; republish the page, rebuild and republish the overview board.

### Names say where the part sits in the film (Kai, 2026-10-26)

`<story>-<order>-<part>-r<N>`: the part's position on the overview board, its letter and short name, and
the round, e.g. `gpom-2-A-killbots-r1`, `gpom-3-B-door-r2`. Its media bin has the same name. Kai's own cuts get
an order number and a name too (`gpom-1-track-and-off-switch`), so the Project panel sorts as the film.
When a part moves on the board, rename its sequences and bins (`projectItem.createSetNameAction` /
`folder.createRenameBinAction`), and record `renamed_from` on the build record.

### Building a sequence

```bash
python3 scripts/scene/premiere-plan.py <edl.json> <plan.json> --tag r<N> --seq <story>-<order>-<part>-r<N> [--skip <stem>]
```

It cuts each voice line out of its stem into `premiere/r<N>/lines/` (`--tag` keeps earlier sequences'
files intact; music and sfx stems are shared, so a rebuild that changes a stem makes the older sequence
`stale`), makes silent copies of clips that carry audio, and writes `<plan>.place.js`. Then, strictly in order:

1. `premiere_import` every file in `plan.files`, `bin: "<the sequence name>"`
2. `premiere_create_sequence({name, fromItems: [<the first V1 clip's item id>]})`, which makes it active
3. `premiere_eval` with the contents of `place.js`. It refuses to run unless the active sequence has the right name; it returns the clip counts per track. Compare them with the plan
4. `premiere_get_sequence` → `premiere-check.py --write` (it must say in sync), export two or three frames and look, `premiere_save`

Layout: picture on V1 with in/out, one audio track per stem (voices, then music, then effects), each voice
line its own clip. Kai's music track is left out with `--skip`. Worked example: GPOM `gpom-sh-B-rough2`.

### Tabs show the film

The open sequence tabs are **the film in order, one tab per part**: Kai's own cuts, then each page's current
sequence. Nothing else stays open. `project.closeSequence(seq)` and `project.openSequence(seq)` (via
`premiere_eval`) only close and open tabs. Neither changes a sequence, and tabs open in the order called, so
close all, then open the board's list in film order and set the active one back. Do it only when Kai isn't
working in Premiere.

## Replies

House output style: the outcome first, plain words, file paths written out in full (`D:\badcode-videos\…`),
what is on the timeline versus in a bin, and one clear next move.
