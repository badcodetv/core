# docs/brand — the BadCode logo

**Picked by Kai, 2026-09-13**, after four rounds in a design session (tuning fork → the fork turned
into a C → the curly brace → tuned by hand). Files are in [`logo/`](./logo/).

![BadCode wordmark](./logo/badcode-wordmark.svg)

## What it is

A curly brace `{` standing in for the C of Code. Its left point is the fork where history splits;
its two ends are the two branches. **Red end on top: the timeline that went wrong. Blue end
underneath: the one being sent back to fix it.** Turned on its side, it is also the tuning fork
from GitPush Origin Master, with the handle as the brace's point.

- Anyone sees a C with two coloured tips — one line, two endings.
- A coder sees the `{` that opens every block of code.

## The settings (the source of truth)

These came out of the round-4 tuner. Everything in `logo/` is generated from them by
[`scripts/brand/build-logo.mjs`](../../scripts/brand/build-logo.mjs) — change these, re-run, never
hand-edit an SVG.

| Setting | Value | Meaning |
| --- | --- | --- |
| depth | `0.59` | how far the brace reaches right, as a fraction of its height |
| point | `0.54` | where the spine sits across that depth — high is a sharp brace, low is a soft C |
| dot | `0.50` | end circle radius as a fraction of line width — 0.5 means the tips are *dipped* in colour, not blobs |
| red | `#cc2b37` | top end |
| blue | `#2696d4` | bottom end |
| type | IBM Plex Mono SemiBold | the site's own face, outlined into the wordmark so it needs no font |

Ink is pure black on light grounds and pure white on dark. The colours never change with the ground.

## Files

| File | Use |
| --- | --- |
| `badcode-wordmark.svg` / `-reversed.svg` | the name, black / white lettering (+ 2400px PNGs) |
| `badcode-mark.svg` / `-reversed.svg` | the brace alone |
| `favicon.svg` | heavier line for small sizes; flips black/white with the browser's theme |
| `favicon-16/32/48/180.png`, `favicon.ico` | PNG/ICO fallbacks — **black ink on transparent**, so they vanish on a dark tab bar; use the SVG where possible |
| `avatar-1024.png` / `avatar-reversed-1024.png` | profile pictures, safe for a circle crop |

**Below 32px use the favicon, not the mark** — the mark's line is too thin to survive.

## Open

- 🔴 **Red and blue are the UK's two main party colours** (Labour red, Conservative blue). A logo with a
  "bad" red end and a "good" blue end can read as partisan to the reader in
  [`the-reader.md`](../marketing/the-reader.md). Raised during the session; Kai chose red and blue
  anyway and has not ruled on the risk. The site's amber/cyan was offered as the fallback.
- Not yet applied to the website (`apps/web` still has no favicon or logo).
