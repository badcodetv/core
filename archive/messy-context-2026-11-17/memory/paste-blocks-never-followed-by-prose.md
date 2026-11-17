---
name: paste-blocks-never-followed-by-prose
description: Put all commentary BEFORE a copy-paste block, never after it — Jack could not tell where the Suno style prompt ended.
metadata:
  type: feedback
---

When handing over anything the user copies and pastes verbatim — a Suno Style/Exclude/My Taste/Lyrics
box, a Flow prompt, a shell command — **all explanation goes above the fenced block. Nothing goes
between or immediately after the blocks.** End the message's paste section with the last block.

**Why:** 2026-09-01, camping narration. A Suno Style box was followed immediately by a paragraph
explaining why `Madchester` was chosen. Jack had to ask *"Is this part going in the style prompt?"* —
in a Suno box, prose after the prompt is indistinguishable from more prompt, and pasting it would
have silently ruined the round.

**How to apply:** rationale first, then the fence. If several boxes go together, stack the fences
back to back in paste order with only a short label line between them, and put every "what changed
and why" note above the first one or in a clearly separate section after a `---` rule. This also
applies to the repo sheets people paste from — see the paste boxes in
`docs/stories/camping/narration/suno-narration.md`. Related: [[every-flow-prompt-ends-with-thanks]].
