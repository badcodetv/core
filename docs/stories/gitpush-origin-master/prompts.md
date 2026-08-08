---
story: gitpush-origin-master
flow_project: TBD — set by T12
flow_project_id: TBD — set by T11b
updated: 2026-08-08
---

# GitPush Origin Master — prompt ledger

Read `.claude/skills/badcode-art-direction/SKILL.md` first (Layer 0 — the global
BadCode register; never copied into this file).

> **Status: partial, hand-seeded 2026-08-08.** This file front-runs T2/T7/T10 of
> [`design/2026-08-08-story-covers-and-prompt-ledger.md`](../../../design/2026-08-08-story-covers-and-prompt-ledger.md)
> for the cover only, so Kai could test it manually in Flow. The cast table and
> the remaining assets are still owed. An executor picking up T2 should **extend**
> this file, not recreate it.

## 1. Style prompt

_TBD — T7._ Working basis is the register anchor
([`docs/images/register-anchor.md`](../../images/register-anchor.md)): near-black
exposure, deep unlifted shadows, a single motivated light source, monumental
machine architecture receding into darkness, muted cool-neutral with tiny points
of status-LED light, fine 35mm grain, no lens flares, vast still composition.

## 2. Cast

_TBD — T2/T11b._ Known so far:

| Tag | Character file | Sheet | Flow Character id | Status |
| --- | --- | --- | --- | --- |
| @TheAI | characters/the-ai.md | — | — | none-by-design |
| @Carrier | characters/the-carrier.md | — (recoverable at `7dd36c7^`) | — | not-cast |
| @TheHundred | characters/the-hundred.md | — | — | not-cast |

The AI is **never rendered** pre-revert. That is canon, not an omission.

## 3. Assets

### cover → `docs/images/covers/gitpush-origin-master.jpg`

- **Cast:** — (no people in this image)
- **Light source:** earthlight down the aisle — the planet is the only
  illumination in the hall
- **Prompt (variant A — primary):**
  > Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted
  > cool-neutral palette, no lens flares, calm observational tone, landscape
  > orientation. The interior of a monumental server hall in orbit: two facing
  > rows of tall dark equipment racks recede down a central aisle into deep clean
  > black, their faces carrying tiny points of blue-white and amber status light.
  > The far end of the aisle opens directly onto space — no window frame, no
  > glass — and the Earth hangs there, the whole planet visible as a complete disc
  > occupying roughly a quarter of the frame, its own soft blue light the only
  > illumination in the hall, catching the nearest rack edges and falling away to
  > nothing. Machine-precise geometry, vast still symmetrical composition, deep
  > unlifted shadows. No people, no text, no fantasy effects.

- **Variant B — less symmetrical, more photographic:** replace *"vast still
  symmetrical composition"* with *"the aisle running off-axis so the planet sits
  low and right of centre"*.
- **Variant C — Earth larger, racks as silhouette:** replace *"roughly a quarter
  of the frame"* with *"roughly a third of the frame"*, and add *"the nearest
  racks reduced to black silhouetted rails at the frame edges"*.

- **Lint:** ✅ 2026-08-08 — no brand names or wordmarks · no likeness phrasing ·
  no stacked destitution · no institutional text. **Never name SpaceX or
  Starlink in the prompt** — it adds nothing the image can show and a real brand
  name is block trigger #1.
- **Flow media id:** _pending_
- **Revisions:**
  - _none yet — awaiting Kai's manual test run._

#### Why this image, and what not to "fix"

The concept is Kai's (2026-08-08): a terrestrial-looking server hall in orbit,
seen the way the AI would see us. It is grounded in SpaceX's real January 2026
FCC filing for a constellation of up to one million satellites as the foundation
of an orbital AI data centre — but the brief is explicitly **not** to reconstruct
that hardware.

**The deliberate departure:** the real filing puts those satellites at 310–1,240
miles, where Earth would fill most of the sky. A whole disc at a quarter of the
frame reads as far higher orbit. This is chosen, not an error — the target is the
Apollo 8 / *Pale Blue Dot* emotional register, the first time humans saw the
whole planet at once. **Do not "correct" it toward LEO accuracy.**

**Why it isn't the anchor.** `docs/images/register-anchor.jpg` *is* GPOM Short
panel 1 and doubles as the site-wide OG fallback, so a plain server-hall cover
would make BC-000 and the brand the same picture. This keeps the anchor's
grammar — one motivated light, deep unlifted black, monumental machine
architecture — and swaps the blade of light for the planet.
