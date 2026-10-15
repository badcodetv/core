# The triangle round — 2026-10-15

> **Asked by Jack, 2026-10-15**, after the meeting the same day
> ([`docs/misc/2026-10-15-meeting.md`](../../../docs/misc/2026-10-15-meeting.md)): Kai wants the
> red circle swapped for a **red triangle** ("triangles feel more threatening"). Jack: *"make a
> similar logo, where it is a triangle instead of a circle… multiple versions that vary from each
> other… avoid elements of AI slop."*
>
> **These are pictures of logos, not logos.** As in [`concepts.md`](./concepts.md), the image
> model sketches the idea; a picked one gets built properly in `scripts/brand/build-logo.mjs`.
> The official logo in [`docs/brand/`](../../../docs/brand/README.md) is unchanged until Kai and
> Jack rule.

## The design, before the words (shot-craft)

A logo is not a shot, but the same three questions apply.

- **What is it for?** Keep what Kai ruled on 29 September: one off-centre red mark that reads as
  a **glance**, and a round lowercase name whose o is the red. Make it **harder**: the circle's
  calm goes, a point comes in.
- **Where does the eye land?** On the red. Everything else is off-white on near-black, flat. The
  red is the only small, warm, high-contrast thing (`frame.md` §2).
- **Tension, not balance.** The red is never in the middle (`frame.md` §3: off-centre and
  asymmetric reads as tense; centred reads as resolved). Centred, the dot was a record button.
  **In a triangle, centred is worse: it is the all-seeing eye** on the dollar bill, which is
  conspiracy iconography, and our reader is being pulled toward conspiracy content
  ([brief 05](./05-threat-perception-science.md), [brief 06](./06-warning-symbols.md)).
- **The cliché to dodge.** Triangle + dot is also a hazard sign, and at small sizes a play
  button or an error icon (brief 06; [`direction.md`](./direction.md)). Sheet 07 of round 1 was a
  warning triangle and was held in reserve for exactly that reason. Each version below moves away
  from it a different way.
- **Gate 2 (a visible cost) does not apply.** It is a flat mark, not a monumental shot.
- **Light.** None. Flat colour. The one exception is the last version, which puts the mark in
  the world with one named source.

## The versions

Each moves **one** thing, so the pictures can be compared.

| # | Name | What changes |
| --- | --- | --- |
| T1 | The straight swap | The ring becomes an upward triangle outline; the dot stays, pushed up and right |
| T2 | Upside down | A downward-pointing triangle (the angry-brow V of brief 05); the dot pushed into the top right corner |
| T3 | Two triangles | The red is a small solid triangle too, pointing out at the top right; the o in the name becomes a red triangle |
| T4 | Off level | The triangle is tipped about 12 degrees, not quite level; the dot off-centre |
| T5 | The gap | One corner of the triangle is open; the dot sits just outside it, as if it got out |
| T6 | In the world | T1 as a red-and-white enamel sign screwed to a wet brick wall, photographed (breaks the register on purpose) |

## What the research changed (web pass, 2026-10-15)

Read on top of [`docs/google-flow/nano-banana-2.md`](../../../docs/google-flow/nano-banana-2.md)
and [`2026-10-08-anti-slop-sweep.md`](../../../docs/google-flow/2026-10-08-anti-slop-sweep.md).
Tags: **[G]** Google's own docs · **[P]** several practitioners · **[A]** one source.

- **Name the shape first, style second** ("silhouette-first") [A, morphed.app]. Vague words like
  "abstract shape" give mush; named primitives (triangles) render reliably [A].
- **Google's logo template:** *Create a [type] for [brand] with the text "[text]" in a [font
  style]. The design should be [style], with a [colour scheme].* Describe the font in words [G,
  ai.google.dev]. Sentences, not tag lists [G].
- **The slop tells for logos:** gradients, bevels and gloss; the logo dropped onto a desk or
  marble mock-up; melted lettering; mixed styles and no breathing room [P]. Counters: "flat",
  "vector-style", "solid fills", "crisp edges", "uniform line thickness", and a **plain solid
  background** said positively, because there is no negative-prompt field [G: "semantic negative
  prompts"].
- **Hex codes are not documented** to work [G, by omission]. Colour words only; exact values live
  in `build-logo.mjs`.
- **Short, large text.** One word, in quotes, big [P]. Practitioners suggest capitals; ours is
  lowercase by ruling, so lowercase is the untested part.
- **Geometry is approximate.** No source measures it. These are concepts to redraw [P].
- **Pro is reported sharper on type and edges** [P]. The standing rule is Nano Banana 2 (free); if
  the name garbles, Pro is Jack's call.

## The prompts

Settings for all six: **Nano Banana 2 · 1:1 · 2 candidates each.** No reference attached (the
generator tool cannot attach one, and attaching the ring logo would pull it back to a circle).

Shared opening, `LOGO` (T1, T2, T4, T5 use it as written; T3 changes the last sentence):

```
Create a flat vector logo for a brand called badcode, shown straight on, on a plain solid near-black background that fills the whole square, with wide empty space around the logo. It uses only two colours on the black, a cold off-white and one deep signal red, both solid and unlit, with crisp edges and perfectly even line thickness. The symbol sits in the upper part of the square, large. Below it, centred, is the single word "badcode" in large lowercase letters drawn from perfect circles and straight vertical stems, a rounded geometric sans-serif with one uniform medium stroke, in off-white, where the letter o is a solid red disc the same red as the symbol.
```

**T1 — The straight swap**
```
LOGO + The symbol: a thick off-white outline of an equilateral triangle pointing up, its line about a tenth as thick as the triangle is wide, and inside it one solid red disc about a quarter of the triangle's width, placed above and to the right of the triangle's middle, close to its right-hand side, like an eye glancing sideways. Thanks.
```

**T2 — Upside down**
```
LOGO + The symbol: a thick off-white outline of an equilateral triangle pointing down, with its flat side at the top, its line about a tenth as thick as the triangle is wide, and inside it one solid red disc about a quarter of the triangle's width, pushed up into the top right corner so it nearly touches both sides of that corner. Thanks.
```

**T3 — Two triangles** *(the name changes: its o is a triangle)*
```
LOGO, with its last sentence changed to: ... where the letter o is replaced by a small solid red equilateral triangle pointing up, the same height as the round letters, the same red as the symbol. + The symbol: a thick off-white outline of an equilateral triangle pointing up, its line about a tenth as thick as the triangle is wide, and inside it one small solid red triangle about a quarter of its width, placed above and to the right of the middle and turned so its point aims at the upper right. Thanks.
```

**T4 — Off level**
```
LOGO + The symbol: a thick off-white outline of an equilateral triangle pointing up, tipped about twelve degrees clockwise so its base is not level, its line about a tenth as thick as the triangle is wide, and inside it one solid red disc about a quarter of the triangle's width, placed above and to the right of the middle. Thanks.
```

**T5 — The gap**
```
LOGO + The symbol: a thick off-white outline of an equilateral triangle pointing up, its line about a tenth as thick as the triangle is wide, where the two lines at the top corner stop short and never meet, leaving a small open gap at the very top. One solid red disc, about a quarter of the triangle's width, sits just above and to the right of that gap, outside the triangle, as if it has just got out. Thanks.
```

**T6 — In the world** *(replaces `LOGO`)*
```
Documentary photograph on 35mm film with fine natural grain. A small square vitreous enamel sign with a near-black face, chipped at one corner, held by four rusted screws to a wet red-brick wall beside a shuttered shop at dusk, lit by one sodium street lamp off to the left. Painted flat on the sign: a thick off-white outline of an upward-pointing triangle with one solid red dot inside it, above and to the right of the middle, and beneath it the word "badcode" in round lowercase off-white letters whose o is a solid red dot. Camera at chest height, a little to the right, the sign off-centre, a black drainpipe running down the left edge of the frame. Thanks.
```

The exact strings sent to Flow are the expansions (LOGO + the symbol sentence, as one paragraph).

## Run log
**2026-10-15, attempt 1: not run.** Flow on channel 2 redirected every project URL to
`flow.google.com/about` and listed no projects, so the browser is signed out of Flow (although
`flow_status` said logged in). Nothing generated, no credits spent. Prompts as sent are in the
session's `prompts.json`, identical to the expansions above.

**2026-10-15 14:44, attempt 2: ran.** Flow signed in by Jack; a cookie banner had to be accepted
before the settings button would click. New Flow project **"Oct 15 - 14:42"**
(`0558b1d5-094c-4102-b71f-21ba1d95e7c6`; the rename to "badcode triangle logo" did not take, as
usual). Nano Banana 2, 1:1, 2 each: **12/12 landed, no blocks.** Images stay in Flow; a contact
sheet was made in the session scratchpad only.

### First read (Claude, one look; Jack and Kai rule)

| # | Version | Read |
| --- | --- | --- |
| T1 a/b | Straight swap | Clean and closest to the current logo. In (a) the dot is near the middle, which tips toward the all-seeing eye; (b) presses it against the right side, and that keeps the glance |
| T2 a/b | Upside down | The most threatening, and the dot in the corner reads as watching from above. Risk: a downward triangle is also the UK give-way sign |
| T3 a/b | Two triangles | A triangle inside a triangle reads as a hazard or mountain icon. The triangle o turns the name into "badcAde". Weakest |
| T4 a/b | Off level | (a) is tipped hard and has energy, but its dot is central (eye risk). (b) is barely tipped and reads as a mistake |
| T5 a/b | The gap | The surprise: with the dot outside the gap, the triangle reads as the letters **"Ai"** or a little figure. A clear idea; whether it is the right one is a ruling |
| T6 a/b | In the world | Believable as a real enamel sign; (b) is the stronger photo. The dot came out small and near the middle |

The lettering came out right in all twelve, lowercase with the red o. No gradients, glow or
mock-up scenes; the flat backgrounds carry a faint vignette.

### Saved as potential designs (Jack, 2026-10-15)

All twelve are kept in [`sketches/triangle/`](./sketches/triangle/) at 768 px
(`t1-straight-swap-a.jpg` … `t6-in-the-world-b.jpg`, plus `contact.jpg`). **Potential designs,
none picked.** The full-size originals are in Flow project "Oct 15 - 14:42".
