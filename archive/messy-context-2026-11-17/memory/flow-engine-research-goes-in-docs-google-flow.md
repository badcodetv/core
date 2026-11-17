---
name: flow-engine-research-goes-in-docs-google-flow
description: "Standing instruction — any research about how a Flow/Gemini engine behaves must be written into docs/google-flow/, not left in a story file or the chat."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c83d503b-fe66-42cb-a482-f08a5cb93941
  modified: 2026-08-14T12:02:08.573Z
---

Kai's standing instruction (2026-08-14): **always** write engine research into
`docs/google-flow/` at the time it is found — `omni-flash.md` for Gemini Omni
Flash (video), `nano-banana-2.md` for the image model. Not into a story's prompt
file, not only into the conversation.

**Why:** research is worth nothing the second time somebody has to find it again.
The trigger was a Karen river-drop clip that kept failing; the cause (Omni
supports no negative prompts, and `no`/`don't` phrasing backfires) was in a blog
post three clicks away and nobody had recorded it the first time.

**How to apply:** the test is *"would this still be true for a different story?"*
Yes → `docs/google-flow/`. No → the story's own file. Tag every claim with the
folder's evidence tier (`[vendor]`, `[runware]`, `[community]`, `[yt]`,
`[untested]`, `[confirmed <date>]`), date the section, cite the URL. The rule is
also written into `docs/google-flow/README.md` and the CLAUDE.md repo map, so
prefer reading those — they may have moved on from this note.

**⚠ Contested since 2026-08-14.** Kai independently built a second Flow tree,
`docs/flow/` (7 files, paired with the `flow-prompt` skill), on the branch that
became `badcodetv/core` main. Both trees now exist. The merge left an interim
split written into the CLAUDE.md repo map — `docs/flow/` = prompt craft,
`docs/google-flow/` = engine behaviour — but **a real consolidation call is still
owed by Kai and Jack.** Check the repo map before trusting the "always" above.

Related: [[repo-records-intent-flow-holds-assets]].
