# docs/brand — the BadCode logo

**"The Look." Picked by Kai, 2026-09-29**, after a 16-agent research sweep, a Flow concept-sheet
round and a tuning session on the logo bench. Files are in [`logo/`](./logo/). It replaces the
curly-brace logo of 2026-09-13, which Kai found "very obvious and very cliché" — kept in
[`archive/2026-09-13-brace/`](./archive/2026-09-13-brace/README.md).

![BadCode lock-up](./logo/badcode-lockup-reversed.svg)

## What it is

**The icon:** a ring with one red dot inside it, off centre, glancing up and to the right. Kai: *"it
looks a bit like a Death Star, it looks like an eyeball."* It is BadCode as a character — not
friendly, not a mascot: something that has already seen how this ends and is sizing you up.

**The name:** `badcode` in round lowercase, drawn from circles and straight stems (no font), where
**the o is a solid red dot** — the same red as the icon's.

## The rules

- **The dot is never dead centre.** Centred, it is a record button. Off centre, it is a glance.
- **The icon and the name stand apart.** Never put the ring-with-dot inside the word as the o —
  that is almost exactly Badoo's 2006–17 logo (dating app). In the name the o is always a plain
  solid dot.
- **Red is only ever the dot.** One small red thing per mark; never a red field.
- **Below 48px use the favicon files** — they carry a heavier line floor and a bigger dot, or at
  16px the dot shrinks to a speck.

## The settings (the source of truth)

Everything in `logo/` is generated from these by
[`scripts/brand/build-logo.mjs`](../../scripts/brand/build-logo.mjs) (`node scripts/brand/build-logo.mjs`,
uses the repo's `sharp`). Change them, re-run, never hand-edit an SVG. They are Kai's bench save of
2026-09-29 18:30; the bench is [`design/research/2026-09-29-logo/tuner/`](../../design/research/2026-09-29-logo/tuner/index.html)
(live: https://claude.ai/artifact/4Tf8nXY8RmRokTevDQ7cWe).

| Setting | Value | Meaning |
| --- | --- | --- |
| ring | `0.17` | ring line thickness, as a fraction of the ring's radius |
| dot | `0.245` | red dot radius, as a fraction of the ring's radius |
| push | `0.51` | how far off centre: 0 = centre, 1 = touching the rim |
| angle | `55°` | which way it looks, clockwise from 12 o'clock (about 2 o'clock) |
| red | `#cc2b37` | the dot, and the o — carried over from the brace logo |
| lw | `0.30` | letter line weight, as a fraction of letter radius |
| tr | `0.26` | letter spacing, as a fraction of letter radius |
| ck | `0.42` | the c pulled toward the red o — the c's open side makes that gap look bigger than it is |

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

- **Jack's say** — the pick is Kai's; Jack (lead creative designer) has not seen it yet.
- **Checks before it goes public:** a UK IPO trade-mark search for ring-with-dot device marks
  (classes 9, 41, 42); a look at Big Brother UK's 2001–2025 geometric eyes (the one near-miss the
  research could not see). Research and the clash checks: [`design/research/2026-09-29-logo/`](../../design/research/2026-09-29-logo/README.md).
- **Not yet on the website** (`apps/web` still has no favicon or logo).
- **Red for colour-blind viewers:** `#cc2b37` is darker than the brief's `#e6291c`, so red-blind
  viewers see it closer to the black ground. Logos are exempt from contrast rules; noted, not ruled.
