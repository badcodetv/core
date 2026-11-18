---
name: story-covers-and-prompt-ledger
description: "2026-08-08 initiative — per-story prompts.md ledger as canonical image memory, full character roster, four EP cover images"
metadata: 
  node_type: memory
  type: project
  originSessionId: 22a2afc1-be0d-4b26-8b06-8d9df2abef71
  modified: 2026-08-08T18:15:06.889Z
---

Plan at `design/2026-08-08-story-covers-and-prompt-ledger.md` (status: proposed,
24 tickets, 4 phases). Scope is the **four EP stories only** — GPOM (BC-000),
Camping (BC-001), Karen (BC-002), Magic Money Tree (BC-003). Galileo, Storyverse
and Future Proof stay file-ready but **unlinked from the home page** (Kai's call).

**The core artifact is `docs/stories/<story>/prompts.md`** — a per-story prompt
ledger that is the canonical memory of how a story looks, so Kai and Jack can
both pick a story up mid-flight instead of Jack typing prompts into the Flow
browser with nothing surviving the session. Four layers: Layer 0 global register
(stays in the `badcode-art-direction` skill, never copied), Layer 1 per-story
style prompt, Layer 2 asset prompt, Layer 3 cast as a *list of Flow Character
tags* — never prose, because a tag typed as text does not bind a face.
Chosen over prompts-in-`story.md` (Kai's original ask) mainly because story.md
files are 400–700 lines and mix the why with the how.

**Cover art direction:** shared grammar, story-native subject — each cover shows
its own story's location and palette, but all four obey a single motivated light
source, deep unlifted blacks, and one subject held small in a large frame. No
text baked in. **GPOM's cover is Kai's specific vision:** an orbital server hall,
terrestrial-looking racks receding down an aisle open to space, Earth a whole
disc at ~¼ frame as the only light source — Apollo 8 / Pale Blue Dot register,
deliberately not LEO-accurate. Grounded in SpaceX's real Jan 2026 FCC filing for
~1M orbital-AI-datacentre satellites.

**Why it isn't just "generate four images":** Karen and Ari have no `## Visual`
sections at all; Keynes and the tree are uncast; MMT's Dawn is dead canon.
See [[flow-policy-blocks]] — there is no prompt pre-check API, so the plan lints
prompts on paper in Phase 1 before spending credits.

Related: [[website-reset-initiative]] (consumes the covers), [[flow-mcp-and-art-direction-initiative]],
[[stories-consolidation-2026-08]], [[magic-money-tree-refounding]].
