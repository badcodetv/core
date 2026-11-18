---
name: gpom-timelines-index
description: GPOM timelines index page AXJqmgAWTRhxK7fzMkKukp lists every timeline notes page in story order; keep it current
metadata:
  type: project
---

On 2026-10-23 Kai asked for a record of which timeline page (the browser feedback editor from new-scene stage 4) covers each section of GPOM, and which one to look at right now. That record is https://claude.ai/artifact/AXJqmgAWTRhxK7fzMkKukp. **Since 2026-10-23 its source is `docs/stories/gitpush-origin-master/timelines.json`** (the running order, start to end, earlier pages kept as history), built by `scripts/provenance/build-timelines.py` into `timelines/index.html`. The old hand-written `scenes/timelines-index/` is gone. Every story gets the same file (docs/provenance/README.md).

**Why:** Kai works mostly from the timeline pages. He lost track of where the middle of the film was: scene B existed but had never been noted, and the debate/vote scene had not been made.

**How to apply:** whenever a timeline page is made, signed off, or rebuilt, or the "open now" focus changes, edit timelines.json, rebuild, republish to the same URL, and point Kai to it. Story order: Kai's Premiere cut (music video, then the bot), then A kill bots, B at the door, the debate/vote (not made as of 23 Oct), then the ending reel (C, D, E). Related: [[timeline-page-stage-4]], [[gpom-second-half-clips]].
