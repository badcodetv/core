---
name: no-split-brain
description: 2026-10-27 Kai — timeline page and Premiere sequence must never diverge; every round lands on both, and his hand edits in Premiere are pulled back onto the page
metadata:
  type: feedback
---

Kai, 2026-10-27: "What I don't want to do is create a split brain where the timeline artifact becomes stale and everything now is just in Premiere… we should always be keeping the timeline and Premiere synced with the feedback."

**Why:** after a scene went into Premiere, the work drifted back to the pages (dialogue rewrites) and he feared the two would split.

**How to apply:** scene-timeline "No split brain". A round isn't done until the page is republished AND the next `…-r<N+1>` is built and `premiere-check.py` says in sync. When it says "edited in Pr", don't build over him and don't leave the page behind: port his edits into the edl and the page. There's no pull-back script yet, and the check only compares V1 picture, so ask about any sound he moved by hand. Every round reply ends with a sync line per scene.

Related: [[timeline-drives-premiere]], [[scene-dialogue-skill]], [[timeline-page-stage-4]].
