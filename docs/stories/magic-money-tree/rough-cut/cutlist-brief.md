# Brief: writing a scene's cut list

For whoever writes `cutlist/<scene>.json` (an agent or a person). The format is in
[`README.md`](./README.md); this is **how to choose what goes in it**.

## Read first

1. [`README.md`](./README.md) — the cut-list format and the timing rule.
2. [`../edit-plan.md`](../edit-plan.md) — your scene's table: the **picture intent** for each line.
3. [`../storyboard.md`](../storyboard.md) — your scene's section. **Canon: where it disagrees with the
   edit plan, the storyboard wins.** Record each difference in the scene's `notes`.
4. [`lines.json`](./lines.json) — the line ids (`P1.03`…), the words, and the planned `start`/`end`
   in seconds. Your clips must tile your scene's lines exactly.
5. [`facts.md`](./facts.md) — verdicts and wording; [`documents.md`](./documents.md) — fetched documents.
6. [`cards/cards.json`](./cards/cards.json) — every card by name; the PNG is `clips/cards/<NAME>.png`
   (a `column` card is `NAME-1`, `NAME-2`…; a quote with `lit` also has `NAME-LIT`). The review
   sheet of all of them is `clips/cards/_contact.jpg`.
7. [`../footage.md`](../footage.md) §11–12 — what each film and still is, and why we may use it.

Media root: `/mnt/d/badcode-videos/magic-money-tree/clips/` (`file` paths are relative to it).
Charts and diagrams: `charts/CHART-10B-A.mp4` (5.0 s), `-B.mp4` (5.5 s), `-C.mp4` (6.0 s), each with a
`.png` of its last frame; `charts/DIAGRAM-10A-1.png`, `-2`, `-3`. Treat a chart `.mp4` as `kind: chart`
with `src_in` 0 and `src_max` its length; hold its `.png` after it if the line runs longer.

## How to choose

- **Look before you write.** For films: open the contact sheets in `clips/_shotlogs/<film>/` and the
  shot log `shotlogs/<film>.tsv`, pick the shot, then confirm it with
  `python3 scripts/grab.py <film> <seconds>` (one frame) or `<from>-<to>` (a 10-frame strip) and
  **read the image**. For stills: read the image before choosing its move.
- **Stay inside the shot.** `src_in` at least 0.2 s after the shot's `in_s`; `src_max` = the shot's
  `out_s` − 0.1. Never let a clip run across a cut in the source.
- **Tile the time.** From your first line's `start` to your last line's `end`, something is on V1, V2
  or V3 at every moment. `offset` + `dur` of consecutive clips on the main picture must meet. Aim for
  2–6 s per picture; hold longer only where the edit plan says HOLD.
- **Cards are opaque** (V3) and replace the picture while they are up. **Labels** (V4:
  `cards/LABEL-*.png`) sit over the shot they belong to, with the same `line`/`offset`/`dur`.
- **Stills get a move.** `PUSH` (1.00→1.12) by default for big stills; for a push toward something in
  particular give `"move": {"from": [cx, cy, scale], "to": [cx, cy, scale]}` in 0–1 fractions of the
  image (centre x, centre y, zoom). A still under 1920 px wide is `INSET` (never pushed past 1.05).
- **Illustrations not yet made** are `kind: illustration` with `file: cards/PH-<name>.png` (the grey
  placeholder), plus `LABEL-ILLUSTRATION` on V4.
- **Every `check`** is something a human must confirm before this ships (staged vs actuality, a
  label, a legal line). Better an honest `check` than a confident guess.
- **Credits:** add a `credit` field with the exact string wherever `footage.md` or `documents.md` gives one.

## House rules that bind the picture

1. No photograph of Baroness Mone, ever. Headlines are the `press/*--headline-only.png` crops only.
2. American footage under a British line carries `LABEL-AMERICAN-*` on V4, or does not go there.
3. No printing-press imagery under anything before 2009.
4. Never a `_masters` file (they carry sound we may not use): only `*.picture-only.mov`, stills,
   cards, charts and documents.
5. Scene 11a: follow `facts.md` §18 to the letter (what may and may not be said or shown).

## Finish

Run `python3 scripts/validate.py <your scenes>` until it reports **0 errors**; warnings are fine if
each is intended. Then render a preview of one scene, `python3 scripts/preview.py <scene>`, grab
three frames from it with ffmpeg, and look at them. Do not commit, and do not edit files outside
`cutlist/`. Report in under 250 words: scenes done, total clips, every `check`, and any line where
nothing we have fits.
