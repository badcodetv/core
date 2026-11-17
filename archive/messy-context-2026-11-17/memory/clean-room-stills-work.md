---
name: clean-room-stills-work
description: "Jack 2026-10-29 — the clean-room method for Flow stills (fresh web research + sealed writers who never see repo prompts) is what finally beat \"AI slop\"; use it for stills going forward"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ebc09e68-009b-4083-b375-c9ef6e7d703d
  modified: 2026-10-29T16:31:45.019Z
---

Jack, 2026-10-29, on the Bank Robbery MV ALT scene 1 round 2 stills: *"i love this new style, see this unlocks so much more stuff using this clean room approach, please remember this."*

The method that worked:
1. A web-only researcher (told not to read the repo) writes a fresh, tiered research note on the engine (here: Nano Banana 2.1 anti-slop).
2. Run the last round's prompts and write an honest "what came back" list of the slop tells (`baseline-r1.md`).
3. Sealed writers (one per staging/scene batch) read ONE brief file only: Jack's verbatim words + plain facts + the research + the failure list + the task. No repo prompts, no skill phrasing.
4. Run their prompts verbatim in Flow, put them on a picks page.

**Why:** repo/skill prompts carry habit wording that makes every image the same glossy AI look; the clean room broke it at once (dry streets, one motivated light, specific place, physical psychedelic layer).

**How to apply:** for Flow stills (and likely clips) when Jack wants new or better looks, default to this clean room; Kai's in-repo `variations` skill is the alternative [[suno-clean-room-for-exploring]]. Worked example: `docs/stories/bank-robbery/songs/mv-speakeasy-mint-alt/cleanroom/`. See [[rules-are-a-loose-guide]].


**Breach found 2026-11-07 (Camping rappers, "like a geography teacher"):** the clip briefs pasted in a RECYCLED research file (Bank Robbery's action-clip research) and quoted Jack's note about another video, so restraint wording leaked through the clean room. Step 1 means fresh web research every job; never paste an old research file or another video's notes into a brief. Traps: docs/google-flow/same-clip-traps.md.

**Update 2026-11-17:** the writers must be truly sealed: run them with `scripts/variations/sealed-writer.sh` or the `clean-room-writer` agent, never `general-purpose` (which loads CLAUDE.md + this memory). See [[sealed-writers-must-not-see-repo]].
