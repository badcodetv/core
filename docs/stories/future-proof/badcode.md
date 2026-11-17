# Future Proof

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
The good branch: redesigning politics with three software-engineering tenets: **composition over inheritance** (vote
issue by issue, not one party bundle), **continuous integration** (laws changed small, checked, with an undo) and
**data-driven decisions** (no policy without its experiment). This folder holds the media; the written canon is
[the canon file](../gitpush-origin-master/future-proof.md).

## Parts
- Front door — three giant questions ("Why can I only vote red or blue?", "Why is it only once every five years?",
  "Why don't we ask the experts?"), each a three.js scene of how it is and how it could be — live at badcode.tv
  `/future-proof/` (GOVT programme 2).
- Launch talk — [slideshows/launch-talk/](./slideshows/launch-talk/) — deck v3 (17 slides + 6 appendix, ~3:17), on the
  website; content rework next.

Don't carry one part's look into another.

## Look
**Launch talk slides: LOCKED — "Update Available".** Britain is an old computer that has clicked "remind me later"
since 1872. Every slide is a desktop with system windows: error boxes whose buttons are both bad, installers stuck at
3%, release notes, bug tickets, notification stacks, an image viewer for pictures, a blue crash screen for the big
turn. The taskbar clock reads 1872.
- Palette: desktop teal `#3b7f86`, window grey `#d4d3cc`, title bar navy `#1f3070` → `#3c55a8`, progress green
  `#2d9a4c`, alert yellow `#ffd43b`, error red `#d22d2d`, ink `#141618`.
- Type: Silkscreen (title bars, pixel labels), Atkinson Hyperlegible (window text, captions), VT323 (lists, receipts).
- 3D diagrams: flat, chunky, low-poly, in the palette, HTML pixel tags for labels.
- Source of truth for the frame: `slideshows/launch-talk/theme/` (theme.css, layouts.js, LAYOUTS.md).

**Pictures inside the slides (Mel, scenes):** Not decided — run story-style.
**Front door:** Unclear: look.md does not say whether "Update Available" covers it.

## Sound
Not decided — run story-style. Known: the launch talk is spoken by the narrator from the future, voiced as the AI,
and Kai can also give it live on stage. Voice, score and sound effects not chosen.

## Story-only rules
- Pop-up text blames whoever designed or decided, never "the computer" and never the voter.
- Generic old-OS grammar only: no real operating system's logo, no GOV.UK crown, typeface or colours.
- **Mel**, the recurring ordinary UK voter (character sheet: deck.md §2), is not cast. Casting needs Kai's approval
  before any picture is made.
- The talk is meme-laden: a meme after every diagram, simplest possible way to make each point, funnier rather than longer.

## Flow project
None recorded yet. Create one with `flow_create_project` before the first Flow call, and write its id here.

## Library pieces in use
- none yet

## Where the detail is
- [README.md](./README.md), [look.md](./look.md), [sound.md](./sound.md)
- Launch talk: [deck.md](./slideshows/launch-talk/deck.md) (script), [slides.json](./slideshows/launch-talk/slides.json),
  [trail.md](./slideshows/launch-talk/trail.md) (rounds and links), [theme/LAYOUTS.md](./slideshows/launch-talk/theme/LAYOUTS.md)
- Look page (the four options): https://claude.ai/artifact/Xzq6Xt8Ueujrvymth72ryN
- Talk preview: https://claude.ai/artifact/LNreQcESnsdmBZD1HVEaCB · script page: https://claude.ai/artifact/H3SLnrtgVraXpLvput1Axw
