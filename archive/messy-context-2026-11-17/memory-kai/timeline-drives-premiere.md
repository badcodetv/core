---
name: timeline-drives-premiere
description: "2026-10-26 Kai — once built into Premiere, the timeline page stays the noting surface and each round lands as a new sequence; board carries the Premiere map; open tabs = film in order"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d0d90f9d-ddbf-43a5-ae1b-16968b1f6d47
  modified: 2026-10-26T16:05:10.279Z
---

Kai, 2026-10-26: keep noting on the timeline artifact even after a scene is in Premiere ("I can just play the video in the timeline and feed back to you in situ"); every round of notes should also reach Premiere. For a story, there must always be a coherent map of which timeline page drives which Premiere sequence. He asked for the sequences not in use to be closed, so the open tabs are the whole film, one sequence per part.

**Why:** He had many sequences open and couldn't tell which was current or which page each belonged to.

**How to apply:** the procedure is in the scene-timeline skill, "Premiere sync".
- `scene.json` `premiere.current` points to the current build.
- Check with `scripts/scene/premiere-check.py --write` before every Premiere step. If it says "edited in Pr", stop.
- Sequence names follow the board: `<story>-<order>-<part>-r<N>`, e.g. `gpom-2-A-killbots-r1` (renamed 2026-10-26; `gpom-s01` is now `gpom-1-track-and-off-switch`, and it runs straight into A). gaze-cut-46 and gpom-second-half are retired to the `_not-in-film` bin.
- Each round becomes a NEW `…-r<N+1>`, built with `premiere-plan.py --seq`, which writes `place.js`.
- The overview board opens with the Premiere map; every sequence not on it goes in `timelines.json` `premiere.other`.
- Tabs: close all, then open in film order (`closeSequence`/`openSequence` via eval).

Related: [[timeline-page-stage-4]], [[gpom-timelines-index]], [[overview-board-skill]].
