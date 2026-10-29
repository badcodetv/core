---
title: The Magic Money Tree — rough-cut build kit
status: phase 1 (prepare everything) in progress, 2026-09-30
owner: Kai (rulings) · Claude (build)
---

# Rough-cut build kit

**What this is.** Everything needed to put the first rough cut of *The Future He Never Saw* on a
Premiere timeline in one run, written as data so the run is mechanical. Ruled by Kai on 30
September 2026 as two phases:

- **Phase 1 (this folder): prepare everything.** Every shot pinned to the frame, every card
  rendered, every document fetched, the edit written as a cut list a script can check and a
  preview can be rendered from.
- **Phase 2: execute with full autonomy.** Suno narration generated and recorded from preview,
  the cut list re-timed to the real voice, and the whole thing placed on the Premiere timeline.

The paper edit this is built from is [`../edit-plan.md`](../edit-plan.md). Where the paper edit and
the [storyboard](../storyboard.md) disagree, **the storyboard wins** (it is canon) and the
difference is recorded in the scene's `notes`.

## What is in the folder

| Path | What |
| --- | --- |
| `lines.json` | Every spoken line, keyed `P<part>.<nn>` (the Suno part and line number in [`../songs/narration.md`](../songs/narration.md)), with its scene and **planned** clock in seconds. Rebuilt by `scripts/lines.py` whenever the words change |
| `shotlogs/<film>.tsv` | Every shot in every film: shot number, in, out, duration, one-line description. Cuts found by ffmpeg's scene score (`scripts/shotlog.py`); the contact sheets it drew are on D: in `clips/_shotlogs/<film>/sheet-NN.jpg` |
| `cutlist/<scene>.json` | **The edit.** One file per scene, the format below |
| `cards/cards.json` | The text and style of every rendered card; `scripts/cards.py` renders them to `clips/cards/*.png` on D: |
| `data/` | The numbers behind the chart, with sources |
| `facts.md` | Every checkable claim and every quotation card, with a verdict and a source |
| `documents.md` | Receipts for the fetched documents and screenshots |
| `scripts/` | `shotlog.py`, `lines.py`, `cards.py`, `validate.py` (checks the cut list), `preview.py` (renders a low-resolution preview from it) |

Media never lives in git: films, stills, cards, contact sheets and previews stay under
`D:\badcode-videos\magic-money-tree\` (`/mnt/d/...`), per the clips-folder convention.

## The cut-list format

One JSON file per scene, `cutlist/<scene>.json`:

```json
{
  "scene": "01",
  "title": "Get them off the beach",
  "notes": ["storyboard vs plan differences, judgement calls, anything a human should check"],
  "clips": [
    {
      "id": "01-03",
      "line": "P1.03",
      "offset": 0.0,
      "dur": 1.6,
      "track": "V1",
      "kind": "film",
      "file": "s01-dunkirk/gov.fdr.25.4.picture-only.mov",
      "src_in": 292.10,
      "src_max": 295.40,
      "treatment": "FILM-43",
      "desc": "small vessel from above, packed with troops",
      "shot": "gov.fdr.25.4#41",
      "check": null
    }
  ]
}
```

| Field | Meaning |
| --- | --- |
| `id` | `<scene>-<nn>`, in timeline order within the scene |
| `line` | The `lines.json` id this picture sits under. A picture that runs across several lines names the **first** |
| `offset` | Seconds after that line starts. Keeps the cut attached to the words when the real voice moves them |
| `dur` | Planned seconds on the timeline |
| `track` | `V1` archive picture · `V2` overlays (documents, headlines, chart) · `V3` cards · `V4` labels that must stay with their shot |
| `kind` | `film` · `still` · `card` · `doc` · `chart` · `illustration` (made in Flow; a placeholder card until Kai approves the plate) · `black` |
| `file` | Relative to `clips/` on D:. Cards are `cards/<name>.png` |
| `src_in` | Films only: the source second the shot starts at, in the **picture-only** file |
| `src_max` | Films only: the last usable second of that shot (the next cut, or where it goes bad). `src_in + dur` must not pass it; the gap is the handle the real voice can use |
| `treatment` | A house treatment from the edit plan §0.3 (`FILM-43`, `PUSH`, `DRIFT`, `INSET`, `DOC`, `HOLD`, `XD`, `DIP`, `GRADE-BW`) — several joined with `+`. A still may add `"move": {"from": [cx, cy, scale], "to": [cx, cy, scale]}` in 0–1 frame fractions |
| `desc` | What is in the frame, in plain words, so a human can check it without opening the file |
| `shot` | `<film>#<n>` in the shot log, so the choice can be traced and swapped |
| `check` | `null`, or the thing a human must confirm before this clip ships (actuality vs staged, a label, a legal note) |

**Timing rule.** In phase 1 a line starts at its planned clock. In phase 2 each line starts where
the real narration says it does, and every clip keeps its `offset` from its line; durations
stretch or shrink within `src_max`. The voice sets the cut.

## Phase-2 run: narration, then Premiere

Granted by Kai on 30 September 2026: Suno generation, recording Suno previews, and placing
everything on the Premiere timeline, all without asking per step. Still true: **no Suno download
by script** (a human spends that allowance), **P8 (scene 11a) is not generated before its legal
read**, and **no Flow video credit without Kai's yes on the plate**.

### A. Narration (Suno)

1. **Preflight:** `npx tsx scripts/suno/suno.mts status`. One Suno tab, Custom mode, no Cover
   source attached, Personalize off. **Never let a Playwright MCP navigate that tab** (it drives
   the same Chrome; it cost a Suno form on 30 September).
2. **Round 1:** `python3 scripts/narration-spec.py --round1` writes six P1 specs (palettes A, B,
   C × with and without `badcode newsreader` — GPOM's Voice, borrowed from GPOM, a candidate, not inherited; Kai to rule, 2026-10-29 audit) to `/tmp/mmt-specs/`. Run each with
   `npx tsx scripts/suno/suno.mts pair <spec>` (one Create, two takes, 10 credits each; 60 in all).
3. **Record** each take from preview (null-sink capture, `docs/suno-gpt/` playback-recording
   method) into `narration/takes/`. **Pick** by listening (Gemini listen tool) for: every line
   said, no singing, Keynes said right, the voice on top of the score. Write the pick and why into
   `../songs/narration.md` §7 and tell Kai; he can overrule by ear.
4. **P2–P7, P9, P10** with the winning palette and voice: `narration-spec.py P<n> <palette>
   <voice|novoice>`, then `pair`. A take 20 s or more shorter than its twin has skipped lines.
5. **Align:** for each chosen take, `npx tsx scripts/suno/.tmp/align.mts <clip-id>
   narration/P<n>.aligned.json` (Suno's per-word times).
6. **Re-time:** write `narration/parts.json` (film order; P8 as `{"part": "P8", "seconds": 80}`
   until it exists), then `python3 scripts/retime.py narration/parts.json`. Every clip now follows
   the real voice through the time map; the scene files are not edited.
7. `python3 scripts/validate.py` (0 errors), `python3 scripts/preview.py --audio <mix.wav>` to
   watch it once, and `python3 scripts/premiere-plan.py` to write `cutlist/_premiere.json`.

### B. Premiere

1. `premiere_status`; nobody else driving Premiere. Create `D:\badcode-videos\magic-money-tree\magic-money-tree.prproj`.
2. Sequence **`mmt-rough-cut-v1`** from the `HD 1080p 25 fps` preset (never the project default,
   which is 23.976). `premiere_set_active` it and read `sequence.name` on every response.
3. Import per bin (`1 Pride` … `5 Statement`, `cards`, `charts`, `docs`, `narration`), one path per
   file, never `_masters/`.
4. **Lay the picture** with the recipe *lay down a whole cut from a plan* (`docs/premiere/recipes.md`):
   one `premiere_eval` per batch of about ten entries from `_premiere.json`, in time order, per
   track: set the item's in/out to `[in, in + dur]`, `createOverwriteItemAction` at `start` on
   `videoTrack = track`, clear in/out. Stills and cards: check once that an in/out range sets a
   still's length; if not, trim the end after placing.
5. **Motion and opacity:** for each placed clip, `premiere_set_param` component 1 (param 1 Scale,
   param 0 Position) and component 0 (Opacity) from its `motion`/`opacity` keys. Check on the
   first clip whether a keyframe `time` is clip-relative or sequence time, with `export_frame`.
   `dim_under_doc` spans set V1 opacity to 35 %.
6. **Narration:** each part's audio at its `_placement.json` `timeline_start` on its track (A1/A2).
7. **Transitions:** `xd_out` → `AE.ADBE Cross Dissolve New`, 0.4 s, at the clip's end (only where
   both sides have handles); movement seams → `AE.ADBE Dip To Black`, 0.5 s.
8. **Markers:** one per line at its start, named with its first four words; plus one per `check`,
   with the check in the comment, so Kai can find every open question on the timeline.
9. **Look:** `premiere_export_frame` at three points per scene; read each. Save. Export a
   low-resolution review render. Nothing goes through `delivery-qc.sh` until the grade and mix are real.
