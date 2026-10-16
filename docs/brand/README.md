# docs/brand — the BadCode logo

**The red triangle in the ring. Kai, 2026-10-15: "record this as the canonical logo for a minute"**
— so it is the logo now, and it may still move. Tuned on the logo bench and saved as
`b0dhojp15efdyw7rboj6`. Files are in [`logo/`](./logo/). It replaces "The Look" of 2026-09-29 (the
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

**The name:** `badcode` in round lowercase, drawn from circles and straight stems (no font), where
**the o is the icon itself**: a ring at the letters' line weight with the red triangle inside it. Kai,
2026-10-15: a bare triangle as the o "reads as an A" (*badcade*), so "we just use the circle with the
triangle inside it". It replaced the solid red dot o the same day.

## The rules

- **The triangle is never dead centre.** Off centre, it is a glance.
- **The o is always the ring with the triangle**, never a bare triangle (it reads as an a) and no
  longer a solid dot. Noted, not ruled: the dot logo banned a ring-in-the-word o because
  ring-with-a-*dot* is close to Badoo's 2006–17 logo; a triangle is a different mark, but it's worth
  a look in the trade-mark search below.
- **Red is only ever the triangle**, in the icon and in the o. One small red thing per mark; never a red field.
- **Below 48px use the favicon files** — they carry a heavier line floor and a bigger triangle, or at
  16px it shrinks to a speck.

## The settings (the source of truth)

Everything in `logo/` is generated from these by
[`scripts/brand/build-logo.mjs`](../../scripts/brand/build-logo.mjs) (`node scripts/brand/build-logo.mjs`,
uses the repo's `sharp`). Change them, re-run, never hand-edit an SVG. They are Kai's bench save
`b0dhojp15efdyw7rboj6` of 2026-10-15 14:06 — on the bench it reads *"triangle · ring 8% · size 36% ·
55° · toward 2 o'clock · round 55%"*. The bench is
[`design/research/2026-09-29-logo/tuner/`](../../design/research/2026-09-29-logo/tuner/index.html)
(live: https://claude.ai/artifact/4Tf8nXY8RmRokTevDQ7cWe — it has a Triangle / Dot switch; old dot
saves still load as the dot).

| Setting | Value | Meaning |
| --- | --- | --- |
| ring | `0.08` | ring line thickness, as a fraction of the ring's radius (the dot logo's was 0.17) |
| tSize | `0.36` | triangle size: centre to corner, as a fraction of the ring's radius |
| tPush | `0.61` | how far off centre: 0 = centre, 1 = touching the rim |
| tAngle | `55°` | which way it sits, clockwise from 12 o'clock (about 2 o'clock) |
| tRot | `55°` | which way it points, clockwise from 12 o'clock |
| tRound | `0.55` | corner rounding, as a share of the most possible |
| red | `#cc2b37` | the triangle, in the icon and in the o |
| lw | `0.30` | letter line weight, as a fraction of letter radius |
| tr | `0.26` | letter spacing, as a fraction of letter radius |
| ck | `0.35` | the c pulled toward the o (was 0.42 on the dot logo) |
| the o | ring + triangle | the icon at the letters' line weight; the bench's "Ring + red triangle" o style |

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

- **"For a minute"** — Kai ruled it canonical provisionally on 2026-10-15; expect another bench save.
- **Jack's say** — the pick is Kai's; Jack (lead creative designer) has not seen the triangle yet.
- **Checks before it goes public:** a UK IPO trade-mark search for ring-with-triangle device marks (and the old ring-with-dot)
  (classes 9, 41, 42); a look at Big Brother UK's 2001–2025 geometric eyes (the one near-miss the
  research could not see). Research and the clash checks: [`design/research/2026-09-29-logo/`](../../design/research/2026-09-29-logo/README.md).
- **Not yet on the website** (`apps/web` still has no favicon or logo).
- **Red for colour-blind viewers:** `#cc2b37` is darker than the brief's `#e6291c`, so red-blind
  viewers see it closer to the black ground. Logos are exempt from contrast rules; noted, not ruled.
