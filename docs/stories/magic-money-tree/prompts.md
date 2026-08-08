---
story: magic-money-tree
flow_project: TBD — set by T12
flow_project_id: TBD — set by T11b
updated: 2026-08-08
---

# The Magic Money Tree — prompt ledger

Read `.claude/skills/badcode-art-direction/SKILL.md` first (Layer 0 — the global
BadCode register; never copied into this file).

> **Status: partial, hand-seeded 2026-08-08.** This file front-runs T2/T7/T10 of
> [`design/2026-08-08-story-covers-and-prompt-ledger.md`](../../../design/2026-08-08-story-covers-and-prompt-ledger.md)
> for the cover only, so Kai could test it manually in Flow. The cast table and
> the remaining assets are still owed. An executor picking up T2 should **extend**
> this file, not recreate it.

## 1. Style prompt

_TBD — T7._ Working basis: documentary-historical rather than near-black. Low
raking winter daylight, desaturated winter greens and browns under a muted
cool-neutral grade, 35mm grain, observational distance, deep unlifted shade. The
bench and the young lime are recurring geometry across four decades — the same
place, re-photographed as the century changes around it.

## 2. Cast

_TBD — T2/T11b._ Known so far:

| Tag | Character file | Sheet | Flow Character id | Status |
| --- | --- | --- | --- | --- |
| @Keynes | characters/keynes.md | — | — | not-cast |
| @TheTree | characters/the-tree.md | — | — | none-by-design (object; referenced by sheet) |

`characters/dawn.md` is **deprecated canon** — the 2026-08-05/06 re-founding
replaced the Dawn spine with Keynes and the tree. Do not cast her.

## 3. Assets

### cover → `docs/images/covers/magic-money-tree.jpg`

**Metadata — none of this is pasted into Flow.**

- **Cast:** — (the figure is deliberately distant and faceless; no Flow Character
  needed, and none exists yet)
- **Light source:** low raking winter daylight from behind the trees. Recorded so
  a later revision never adds a second source.
- **Lint:** ✅ 2026-08-08 — no brand names or wordmarks · **no likeness phrasing**
  (the prompt must never name Keynes; a real historical person named as a
  likeness target is block trigger #2) · no stacked destitution · no institutional
  text or signage.
- **Flow media id:** _pending_
- **Revisions:**
  - _none yet — awaiting Kai's manual test run._

**Prompt (variant A — primary).** Everything inside the fence is the prompt and
nothing outside it is. Paste the whole block, unedited, into Flow.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette with desaturated winter greens and browns, no lens flares, calm observational tone, landscape orientation. A wide view of an empty London park on a cold overcast morning in the early 1940s: a single slatted wooden bench sits small in the lower third of the frame beside a young, unremarkable lime tree of perhaps thirty years, its bare branches thin and modest against a pale sky. One man in a heavy dark three-piece suit and long overcoat sits alone at one end of the bench, seen from a distance and slightly behind so his face is not readable, papers resting unread on his knee, his head angled very slightly toward the tree as though mid-conversation. Low raking winter daylight from behind the trees is the only illumination, throwing long soft shadows across wet grass and gravel into deep unlifted shade. Mist between distant plane trees, the edge of a lake just visible beyond. No other people, no text, no signage, no glow, no fantasy effects — it is an ordinary tree.
```

- **Variant B — the ending, not the premise:** replace *"his head angled very
  slightly toward the tree as though mid-conversation"* with *"sitting forward
  with his head in his hands"*, and add *"hard frost on the grass"*. This is the
  winter-bench image the story closes on; darker, and arguably a better poster
  than a cover.
- **Variant C — the empty seat:** delete the entire sentence beginning *"One man
  in a heavy dark three-piece suit"*. Bench and tree alone, nobody there. Purest
  expression of "presence carried by framing, wind and light", and it removes the
  figure-rendering risk entirely.

#### Why this image, and what not to "fix"

**The tree must stay boring.** Canon (revised 2026-08-07): it grew from a
Treasury £1 note planted in August 1914, so it is twenty-eight years old when
Keynes sits down — *young*, unremarkable, too small to be notable. **No glow, no
face, no anthropomorphism.** The sage is in the writing, not the rendering. If a
generation comes back with a mystical or glowing tree, that is a miss, not a
bonus.

**The man is never named in the prompt.** He is historically *inspired*, not a
likeness — naming a real person is a reliable policy-block trigger, and the
distant, face-not-readable framing means it costs the image nothing.

**Why it looks nothing like BC-000.** Cover grammar is shared, subject is
story-native: one motivated light source, deep unlifted blacks, one figure held
small in a large frame. Here that grammar produces cold daylight and wet grass
rather than a near-black machine hall — which is the point. The four covers must
be distinguishable at catalogue-thumb size.
