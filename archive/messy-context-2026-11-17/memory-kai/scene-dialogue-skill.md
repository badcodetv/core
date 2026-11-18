---
name: scene-dialogue-skill
description: 2026-10-27 Kai — dialogue rewrites are a skill beside scene-timeline; options page must be one tab per dialogue with rankings linked to the versions they rank
metadata:
  node_type: memory
  type: feedback
  originSessionId: d0d90f9d-ddbf-43a5-ae1b-16968b1f6d47
  modified: 2026-10-27T08:28:21.384Z
---

Kai, 2026-10-27: "ranking and reflowing dialogue into something else could be a skill that we put alongside the rest of the timeline editor skills." It is now `.claude/skills/scene-dialogue`: a workflow of ten shape writers plus one synthesis (`scripts/scene/dialogue-workflow.js`) produces `options.json`, which `scripts/scene/build-dialogue.py` turns into a dialogue page with picks and notes.

**Why:** the first options page was one long markdown document. Kai couldn't link the rankings table to the dialogue it ranked, or tell which options belonged to which scene.

Kai on the tabbed page (2026-10-27): "That is so much better… this is brilliant." Confirmed approach.

**How to apply:** one tab per dialogue, showing Now, the three drafts and the ranked writers. Every ranking row and line chip opens that writer's version. Never publish dialogue options as one flat document. First page: https://claude.ai/artifact/QtMCweEvwqFz6M8CUUdBiN.

Related: [[timeline-page-stage-4]], [[provenance-trail]].
