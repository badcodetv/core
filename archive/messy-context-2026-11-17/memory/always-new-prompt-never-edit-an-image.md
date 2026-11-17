---
name: always-new-prompt-never-edit-an-image
description: Never hand over an image-edit prompt — always write a complete fresh generation prompt with the changes folded in.
metadata:
  type: feedback
---

When a generated image needs changing, write a **complete new prompt** with the
change folded in. Never produce an `flow_edit_image`-style edit prompt ("Using the
provided image, change only…"), and never hand over isolated replacement blocks for
the user to splice — give the whole prompt, ready to paste.

**Why:** Kai's repeated experience is that editing an existing generation does not
work — the edit either ignores the instruction or drags the rest of the frame with
it. Stated twice: 2026-08-24 ("editing existing ones never work") and again the same
day as a standing rule ("always make new prompts instead of editing images going
forward"). Regeneration from a reference image is reliable; editing is not.

**How to apply:** Keep the accepted image as the reference attachment, restate the
entire prompt with the revision inside it, and end it with "Thanks."
See [[every-flow-prompt-ends-with-thanks]] and [[flow-hand-driven-not-automated]].

Caveat worth remembering: `docs/flow/image-prompting.md` §6 and the `edit-panel`
skill still document the edit path. This preference overrides them in practice —
if that ever needs reconciling in the repo, raise it rather than silently following
the docs.
