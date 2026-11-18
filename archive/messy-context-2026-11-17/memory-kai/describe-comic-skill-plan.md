---
name: describe-comic-skill-plan
description: "Planned \"describe-comic\" skill + V1→V2 critical-rebuild workflow for camping/Karen"
metadata: 
  node_type: memory
  type: project
  originSessionId: 91018e61-ad6d-41ca-9a63-10121e422c83
---

Planned next initiative (queued after the Flow scripts/tools are reworked, merged to main, and documented — user is finishing that first as of 2026-06-30).

**Goal:** rebuild the camping (and later Karen) comic via the official make-comic pipeline, but informed by V1 instead of discarding it.

**New skill to document — "describe-comic" / "read-comic":**
- Load an existing rendered comic (e.g. camping V1 at `apps/web/src/comics/camping`) in the browser
- Step/scroll through it, screenshotting page by page
- Pair each screenshot with the existing storyline/script text
- Emit a per-panel **visual + narrative composition commentary** (what's in frame, blocking, mood, what the beat does) as a durable artifact

**Then the rebuild workflow:** take that V1 commentary and *critically merge* it into the camping-v2 storyboard (`docs/camping-v2/storyboard/`) — keep what works, deliberately edit/cut, regenerate panels with the new Flow tools. Recreate with judgment, not copy, not discard. Same playbook for Karen.

Bigger picture: a family of skills for working with EXISTING story/comic media (describe → critique → re-author), complementing make-comic which currently only goes idea→new. Relates to [[camping-karen-rework-initiative]] and [[flow-mcp-and-art-direction-initiative]].

Current camping-v2 state: canon + 20-panel storyboard written, only p02/p03 imaged, not yet assembled into `apps/web/src/comics/`.
