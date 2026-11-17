---
name: always-run-shot-craft-then-flow-prompt
description: MANDATORY — load the shot-craft skill and docs/cinematography/ before ANY image or video prompt, including rewrites; then flow-prompt for phrasing.
metadata:
  type: feedback
---

**Before writing or rewriting any image or video prompt — every time, no exceptions, including a
small revision to a prompt that already exists — load the `shot-craft` skill and read the
matching file in `docs/cinematography/`.** Then, and only then, `flow-prompt` for phrasing.

Jack calls these "the cinematography skills". Two skills, strict order:

1. **`shot-craft`** → `docs/cinematography/` — what the shot should **be**. Gates, then a shot
   spec a human can argue with. `symptoms.md` when something is wrong, `principles.md` for the
   gates, `frame.md` for composition, **`stills.md` for any held image under narration**, `registers.md` for anything monumental.
2. **`flow-prompt`** → `docs/flow/` — how to **phrase** it so the generator obeys.

**Never do design and phrasing in one breath.** The skill says outright that the design step is
the one that gets skipped and it is the one that decides whether the shot is interesting.

**Why:** camping 8b(i) burned four generations and two rewrites on a face that kept reading sad.
Each layer caught a different fault, and none of them was reachable from the layer above:
`flow-prompt` found that the prompt *named the emotion* (Nano Banana has no negative-prompt
field, so "not sad, not troubled" is sad in the scene). `principles.md` found gate 1 and gate 2
failing — a still face asked to carry a change of inner state, in a monumental frame with the
cost blurred out. **`stills.md` §1 found the real one:** every draft described a *finished*
action, and a resting pose dies no matter how well composed. The fix was to move the moment
earlier, not to describe the face harder.

**The gates are not all universal** (2026-10-29 audit): gate 1 (a still needs an unresolved question) and gate 3 (name the light source) are craft. **Gate 2, a visible cost in any monumental frame, is a gate only where the story's `look.md` makes it one** — GPOM's does; for another story, read its `look.md`. Whether it should hold everywhere is Kai's to rule.

**The three that catch the most:** a still needs an **unresolved question**; **geometry and event
must arrive together**; and **when a shot is not landing, delete a clause — never add one**.
Related: [[every-flow-prompt-ends-with-thanks]], [[always-new-prompt-never-edit-an-image]],
[[one-shot-at-a-time-still-then-video]].
