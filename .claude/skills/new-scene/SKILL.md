---
name: new-scene
description: Use to take one scene of a BadCode film from an idea all the way to a noted cut by running its four stage skills in order — scene-beats (talk out what the scene is), scene-images (mood board → storyboard), scene-animation (animate the picks into clips), scene-timeline (rough cut on a timeline page, noted in rounds). Holds the scene folder layout, scene.json and the tools all four share, and the gates between them. Triggers on "new scene", "let's do a new scene", "make a scene for…", "take <scene> from scratch", "the whole scene loop". For one stage on its own, the stage skill's own triggers apply.
---

# New scene (BadCode)

Take **one scene** of a film from a conversation to a noted cut. This is the loop that made the GPOM
opening recut, the second half, the gaze sequence and the ending. It is a conductor: each stage is its
own skill, and this one runs them in order and holds what they share.

```
overview-board  ── the film: this scene is one row, its beat is the starting sentence
     │
1 scene-beats      talk ──► brief.md + scene.json                     │ Kai approves the brief
2 scene-images     mood board ──► votes ──► rounds ──► storyboard     │ Kai picks the stills
3 scene-animation  options per frame ──► picks ──► Flow clips ──► bin │ Kai's go on the words and the spend
4 scene-timeline   voices + music + effects ──► timeline page ──► notes ──► rounds ──► frozen
  scene-dialogue   (beside 4, when the words need rewriting) ten writers ──► ranked ──► 3 drafts ──► dialogue page ──► picks ──► script
                   ──► (when Kai asks) a NEW Premiere sequence, which the page then DRIVES:
                       every later round of notes lands as <story>-<order>-<part>-r<N+1> (scene-timeline, "Premiere sync")
```

**Gated.** Each stage is *talk → approve → produce*, and nothing is generated past a stage before its
picks are in. Never spend video credits on a still Kai has not picked. **Kai cuts the film himself:**
stage 3 ends at clips in a Premiere **bin**, and stage 4 only builds into Premiere as a new sequence when he asks.
After that the timeline page is still where he notes, and **every round lands on the page and in Premiere
together**, as a new sequence. If he has cut the current one by hand, his edit is pulled back onto the page
instead of built over: no split brain (Kai, 2026-10-27; scene-timeline, "No split brain").

Any stage can be run on its own: a new round of stills is `scene-images`, re-rolls are `scene-animation`,
putting an existing cut on a timeline page is `scene-timeline`, rewriting a dialogue by options is `scene-dialogue`.

## Read first

- `CLAUDE.md`: what BadCode is.
- `docs/marketing/the-reader.md`: who the work is for.
- The story's canon (`docs/stories/<story>/README.md`) and its overview board (`timelines.json`).
- Then the stage skill you are in. Each lists the craft skills it leans on (`story-craft`, `shot-craft`, `flow-prompt`, `flow-automation`, `suno-automation`, `premiere-automation`, `lip-sync-dub`).

## Where things live

The words live in the repo and the media lives outside it (the clips/ convention).

| What | Where | Stage |
| --- | --- | --- |
| Scene folder (words) | `docs/stories/<story>/scenes/<scene>/` | all |
| `scene.json` | config: titles, media root, Flow project, beats, board URLs | 1, kept current by all |
| `brief.md` | the interview's outcome | 1 |
| `moodboard.json` | rows `[beat, id, look, prompt, style?]`, one per still made, **including blocked ones** | 2 |
| `storyboard.json` | `{acts:[{id,title,beats}], frames:[{n, act, title, look, line?, stills:[ids], anim:n}]}` | 2 |
| `animation-options.json` | `{sequence_notes:[{rule,why,source}], frames:[{n, job, options:[{id, label, idea, lanes, veo_prompt, cut, seconds, risk}]}]}` | 3 |
| `video-jobs.json` | picks turned into Flow jobs (format in `scripts/scene/shots.py`) | 3 |
| `script.json` | the words per beat `{beats:[{id, title, see, lines:[{who, text, by: kai\|claude, how?}], music, sfx}], voices:[{id, name, profile…}]}` | 4 |
| `cut-notes.json` | each timeline round: Claude's plan, a reply per note, Kai's notes snapshotted | 4 |
| `picks.md` | append-only record of every pick, note and ruling, dated, Kai's words kept | all |
| `trail.json` + `feedback/` | **provenance**: one line per page published or read (`prov.py trail`): its link, rebuild command, decisions, and every vote, pick and note dumped raw | all |
| `final.json` + `final-edl.json` | **provenance**: the finished cut, every shot and sound traced to its recipe (`prov.py freeze`) | 4 |
| Media | `/mnt/d/badcode-videos/<story>/clips/<scene>/` with `moodboard/<id>.jpg`, `video/<prefix>-<key>-<still>.mp4`, and stage 4's `voice/`, `sfx/`, `cut/` (`edl.json`, `preview.mp4`, `stems/`) | all |

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

| Tool | Does | Stage |
| --- | --- | --- |
| `build-moodboard.py <dir> <out.html>` | the mood board page (votes and notes per beat) | 2 |
| `build-storyboard.py <dir> <out.html>` | the storyboard page (still and animation pick per frame, and a flip-through reel) | 3 |
| `shots.py <dir>` | the video job list (JSON) from the storyboard, the options and `video-jobs.json` | 3 |
| `run.mts <dir> [keys…]` | animates jobs in Flow in waves, harvests them, names them | 3 |
| `match.py <dir> [--apply]` | names harvested clips by matching their first frame to the plates, and writes each clip's recipe card | 3 |
| `build-timeline.py <dir> <out-dir>` | the timeline page from `cut.edl` + `cut.preview` (format in `timeline.py`) | 4 |
| `build-picks.py <picks.json> <out.html>` | a **picks page**: rows of options (stills, clips, voice takes, Suno links), Pick one per row, a note per row | 2, 3, 4 |

**Every page comes from a builder, and every image on it opens large on click** (Kai, 2026-10-23: a hand-made picks page had
thumbnails you couldn't enlarge). Never hand-write a page's HTML. If no builder fits, extend one of these (or add one
here) and keep its spec in the scene folder, so the page can be rebuilt from the repo.

Worked examples, built before the tools were generalised: the GPOM opening recut
(`scripts/gpom/build-opening-*.py`, `scripts/gpom/opening-video/`,
`docs/stories/gitpush-origin-master/scenes/opening-recut-*`) and the second half
(`scripts/gpom/second-half-video/`).

## Provenance (every stage)

Kai, 2026-10-23: keep a trail good enough to **rerun the whole scene on a better model**. Full rules:
[`docs/provenance/README.md`](../../../docs/provenance/README.md). Each stage skill carries its own part. In short:
- **Recipe cards are automatic** for Flow MCP stills and edits, `run.mts` clips, TTS voices and Suno `record`. Anything else you make gets `prov.py card` straight after.
- **The pages are only the UI; the repo is the record** (Kai, 2026-10-23). After every publish: `prov.py trail <scene-dir> --stage … --round N --url … --what "…" --rebuild "<builder command>"`.
  Every time you read a page's votes, picks or notes: dump them first (`ArtifactData list` with `out_dir` from `prov.py feedback-dir`), then `prov.py trail … --feedback --decided "<Kai's words>"`. A lost page is rebuilt from its `rebuild` command and refilled with `prov.py restore`.
- **Before showing a cut:** `prov.py check`. **When Kai says it's done:** `prov.py freeze`, and commit.
- **The overview board** row for the scene is kept current at every stage (the `overview-board` skill).

## Replies

Kai reads cold, often between calls. Every reply follows the house output style: the outcome first,
plain words, file paths written out in full (`D:\badcode-videos\…`), what is on the timeline versus in a bin, and one clear next move.
