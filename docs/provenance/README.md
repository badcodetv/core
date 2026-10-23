# Provenance — how every piece of a film was made

Ruled by Kai, 2026-10-23. **Going forward only**: nothing made before this date is backfilled.

The goal: **when a better video model comes out, rerun a whole story's exact prompts through it.**
To do that we keep a recipe for everything we generate, a log of every page we published, and a
frozen recipe for every finished cut.

**Where things live.** The repo (GitHub) holds every word: prompts, picks, notes and recipes. The
D: drive (`D:\badcode-videos\`, backed up to Google Drive) holds every piece of media. Neither is
complete alone; the two together are everything. Nothing in this folder needs the media to make sense.

## The three things we keep (plus the running order)

| What | Where | Written by |
| --- | --- | --- |
| 🧾 **Recipe card**: one per generated file (engine, model, exact prompt, inputs, settings, the file it came from, why it was asked for) | beside the file as `<file>.prov.json` **and** in the repo at `docs/provenance/cards/<path under D:\badcode-videos>.prov.json` | the tools, automatically (list below). `prov.py card` for anything else |
| 📜 **Scene trail**: one line per page published (mood board, storyboard, clips board, timeline round), with its link, round, what it was, and a snapshot of the notes left on it | `docs/stories/<story>/scenes/<scene>/trail.json` + `notes/<stage>-r<N>.json` | `prov.py trail`, run straight after every publish |
| 🔒 **Final recipe**: when Kai says a cut is done, every shot and sound in it traced back through its cards to the first prompt, plus the script and voice casting | `<scene>/final.json` + `final-edl.json` (an earlier freeze is renamed, never overwritten) | `prov.py freeze` |

## The overview board: the film's running order (one per story)

Run by the **`overview-board`** skill (`.claude/skills/overview-board/`): skeleton, status, reshaping, keeping it current.

Kai, 2026-10-23: *"stitch together the list of timelines that, from beginning to end, are the entire story."*

`docs/stories/<story>/timelines.json` is the film in order. Each section (a scene or sequence) has its
state, where it lives (a timeline page, Premiere, or not made yet), its current timeline, and every earlier
page under `history`. A section can hold `parts` (a reel and the scenes in it). Parts that only exist in Premiere,
or don't exist yet, still get a row, so the gaps are visible.

```bash
python3 scripts/provenance/build-timelines.py docs/stories/<story>   # → docs/stories/<story>/timelines/index.html
```

The builder also reads each section's scene folder (`"scene": "scenes/<scene>"`). It picks up the pages in
`scene.json` `boards`, every round in `trail.json`, and a "recipe frozen" badge when `final.json` exists. So a
scene made the new-scene way joins the running order with one line, and its history fills in by itself.
Publish the page to the `url` in `timelines.json` every time it changes, so the link never moves.
**Whenever a timeline page is made, changes state or is replaced:** edit `timelines.json` (state, `open_now`,
move the old link into `history`), rebuild, republish. Link the board at the top of the story's `README.md` too. GPOM's board: https://claude.ai/artifact/AXJqmgAWTRhxK7fzMkKukp

## Which tools write cards on their own

| Tool | Cards it writes |
| --- | --- |
| Flow MCP (`flow_generate_image`, `flow_edit_image`, `flow_refine`, `flow_generate_video`, `flow_refine_video`, `flow_generate_batch`) | every file saved, candidates included. An edit's `parent` is its first reference image; a video's is its start frame |
| `scripts/scene/run.mts` (via `match.py`, when a clip is named) | every clip, with its plate as `parent`, its motion prompt and the job's `why` |
| `scripts/aistudio-tts.py` | every voice take, with the full audio profile and transcript |
| `scripts/suno/suno.mts record` | the recorded take and its preview, with the Suno song id. **Add the sheet by hand**: `prov.py card <wav> --merge --setting sheet=<path to the sheet>` |

Anything else, write the card yourself straight after making the file. That covers ffmpeg composites and
text, Premiere renders, Freesound effects, and archive footage (with its licence and credit string):

```bash
python3 scripts/provenance/prov.py card <file> --kind sfx --engine freesound --tool manual \
  --prompt "heavy door slam" --input url=https://freesound.org/s/123 --input licence=CC0 --why "Kai 23 Oct: the door must slam"
```

`--kind` is one of image, video, voice, music, sfx, cut, other. `--parent <file>` links the card to
the file it was made from, and that link is what lets a freeze walk back to the first prompt.

## The loop (new-scene and anything like it)

1. **Make media with the tools above.** Cards appear by themselves.
2. **Publish a page** (mood board, storyboard, timeline). Straight after, run:
   ```bash
   python3 scripts/provenance/prov.py trail <scene-dir> --stage timeline --round 2 --url <artifact url> --what "cut 2: door slam in"
   ```
   It also writes the link into `scene.json`'s `boards`, so the link can't get lost.
3. **When Kai's notes come in**, read them with `ArtifactData`, save them to a JSON file, and pass `--notes <file>` on that
   round's trail line. The notes then live in the repo, not only on claude.ai.
4. **Before showing a cut**, run `python3 scripts/provenance/prov.py check <scene-dir>`. It lists every file in the cut that has no
   card. Write the missing ones then, while you still know how each file was made.
5. **When Kai says it's done**, run `python3 scripts/provenance/prov.py freeze <scene-dir> --note "<his words>"` and commit.

## Rerunning on a better model (later)

`final.json` already holds what a replay needs. For every shot, its chain runs clip → still → golden,
each step with its exact prompt, model and settings. A replay script would read that chain and
resubmit each prompt to the new engine, oldest step first. **It isn't built yet**, on purpose: write it
when a model worth switching to actually arrives, against that model's real controls.

## Card format (`badcode.prov/1`)

```json
{
 "schema": "badcode.prov/1",
 "file": "/mnt/d/badcode-videos/<story>/clips/<scene>/video/vt-03-DR2-a.mp4",
 "made": "2026-10-23T15:39:16+00:00",
 "by": "claude",
 "kind": "video",
 "engine": "google-flow",
 "tool": "scripts/scene/run.mts",
 "model": "Omni 1.1 Flash",
 "prompt": "The camera does not move. …",
 "parent": "/mnt/d/…/moodboard/DR2-a.jpg",
 "inputs": {"start": "…", "character": null, "scene": "…", "key": "03"},
 "settings": {"mode": "Frames", "aspect": "16:9", "durationSeconds": 8, "count": 1},
 "source_id": "<Flow mediaId or Suno song id>",
 "why": "Kai 23 Oct: the door must slam"
}
```

There are two writers and both must write the same shape:
[`scripts/provenance/prov.py`](../../scripts/provenance/prov.py) (Python, plus the command line) and
[`packages/flow-mcp/src/prov.ts`](../../packages/flow-mcp/src/prov.ts) (TypeScript). The test environment can point both elsewhere
with `BADCODE_MEDIA_ROOT` and `BADCODE_PROV_MIRROR`.
