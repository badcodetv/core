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

## Phase-2 run (Premiere)

Written out in full at the end of phase 1. In outline: generate and record the narration, re-time
`lines.json` from it, `validate.py`, then per scene import, place, trim, treat, label, and
`premiere_export_frame` to look.
