# docs/brand — the BadCode logo

**The red triangle in the ring, and a solid red o in the name. Kai, 2026-10-19: "I'm just going to say
that's our logo."** Bench save `2f6bogo164mzzi4lzz00` ("Saved version 5"). Kai kept the ring thickness,
the triangle, the name beside the ring, the solid o and the drawn letters ("it's very important that
we use the same font"). It replaces the 2026-10-15 save `b0dhojp15efdyw7rboj6` (ring 8%, o = ring +
triangle), which was canonical "for a minute". Files are in [`logo/`](./logo/). It replaces "The Look" of 2026-09-29 (the
same ring with a red **dot**), kept in [`archive/2026-09-29-dot/`](./archive/2026-09-29-dot/README.md);
the curly brace before that is in [`archive/2026-09-13-brace/`](./archive/2026-09-13-brace/README.md).

![BadCode lock-up](./logo/badcode-lockup-reversed.svg)

> **Answered, 15 October 2026:** the meeting's "red circle to a red triangle" ([`docs/misc/2026-10-15-meeting.md`](../misc/2026-10-15-meeting.md))
> turned out to be both: this mark (the triangle above) **and** the balaclava presenter's eyepatch.
> **Potential triangle designs (Jack, 2026-10-15):** twelve concepts in six versions, none picked,
> in [`design/research/2026-09-29-logo/triangle-round.md`](../../design/research/2026-09-29-logo/triangle-round.md)
> (images in its `sketches/triangle/`).

## What it is

**The icon:** a thin ring with one small red triangle inside it, off centre toward 2 o'clock, rounded
at the corners. It is the same character as the dot — something that has already seen how this ends
and is sizing you up — with an edge to it. It is also **the red-triangle eyepatch** worn by the
balaclava host of Money For Something (Kai, 2026-10-15), so the logo and BadCode-in-person are one sign.

**The name:** `badcode` in round lowercase, drawn from circles and straight stems (no font — the
"drawn letters" on the bench, and Kai wants this exact lettering everywhere), where **the o is a solid
red circle** the full size of the letters. A bare triangle as the o "reads as an A" (*badcade*, Kai
2026-10-15). The ring-with-triangle o of 2026-10-15 to 2026-10-19 is superseded by save 5.

## The rules

- **The triangle is never dead centre.** Off centre, it is a glance.
- **The o is always the solid red circle**, never a bare triangle (it reads as an a) and never a ring
  (a ring-with-a-dot o is close to Badoo's 2006–17 logo).
- **Always the drawn letters.** Never set `badcode` in a typeface; use the files.
- **Red is only ever the triangle and the o.** One small red thing per mark; never a red field.
- **Below 48px use the favicon files** — they carry a heavier line floor and a bigger triangle, or at
  16px it shrinks to a speck.

## The settings (the source of truth)

Everything in `logo/` is generated from these by
[`scripts/brand/build-logo.mjs`](../../scripts/brand/build-logo.mjs) (`node scripts/brand/build-logo.mjs`,
uses the repo's `sharp`). Change them, re-run, never hand-edit an SVG. They are Kai's bench save
`2f6bogo164mzzi4lzz00` of 2026-10-19 14:40 ("Saved version 5") — on the bench it reads *"triangle ·
ring 15% · size 36% · 2 o'clock · round 55% · drawn letters · solid o"*. The bench is
[`design/research/2026-09-29-logo/tuner/`](../../design/research/2026-09-29-logo/tuner/index.html)
(live: https://claude.ai/artifact/4Tf8nXY8RmRokTevDQ7cWe — it has a Triangle / Dot switch; old dot
saves still load as the dot).

| Setting | Value | Meaning |
| --- | --- | --- |
| ring | `0.15` | ring line thickness, as a fraction of the ring's radius (0.08 on 2026-10-15; the dot logo's was 0.17) |
| tSize | `0.36` | triangle size: centre to corner, as a fraction of the ring's radius |
| tPush | `0.61` | how far off centre: 0 = centre, 1 = touching the rim |
| tAngle | `55°` | which way it sits, clockwise from 12 o'clock (about 2 o'clock) |
| tRot | `55°` | which way it points, clockwise from 12 o'clock |
| tRound | `0.55` | corner rounding, as a share of the most possible |
| red | `#cc2b37` | the triangle in the icon, and the o |
| lw | `0.30` | letter line weight, as a fraction of letter radius |
| tr | `0.26` | letter spacing, as a fraction of letter radius |
| ck | `0.35` | the c pulled toward the red o (was 0.42 on the dot logo) |
| the o | solid red circle | the bench's "Solid red o" style |
| letters | drawn | the bench's "drawn letters" — circles and stems, no typeface |

Ink is `#0a0a0a` on light grounds and cold off-white `#eef3f6` on dark; the ground is `#050607`.
The red never changes with the ground.

## Files

| File | Use |
| --- | --- |
| `badcode-mark.svg` / `-reversed.svg` | the icon alone, dark ring / light ring, transparent |
| `badcode-wordmark.svg` / `-reversed.svg` (+ `-2400.png`) | the name alone |
| `badcode-lockup.svg` / `-reversed.svg` | icon + name side by side — the everyday lock-up |
| `badcode-stacked.svg` / `-reversed.svg` (+ reversed `-2400.png`) | icon over name — sleeves, posters |
| `favicon.svg`, `favicon-16/32/48/180.png`, `favicon.ico` | the icon on its own near-black disc, so it reads on light and dark tab bars |
| `avatar.svg` / `avatar-1024.png` | profile picture on a near-black square, safe for a circle crop |

## Open

- **Jack's say** — the pick is Kai's (2026-10-19, no longer provisional); Jack (lead creative designer) has not seen it yet.
- **Checks before it goes public:** a UK IPO trade-mark search for ring-with-triangle device marks (and the old ring-with-dot)
  (classes 9, 41, 42); a look at Big Brother UK's 2001–2025 geometric eyes (the one near-miss the
  research could not see). Research and the clash checks: [`design/research/2026-09-29-logo/`](../../design/research/2026-09-29-logo/README.md).
- **Not yet on the website** (`apps/web` still has no favicon or logo).
- **Red for colour-blind viewers:** `#cc2b37` is darker than the brief's `#e6291c`, so red-blind
  viewers see it closer to the black ground. Logos are exempt from contrast rules; noted, not ruled.
