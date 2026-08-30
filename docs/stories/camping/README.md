# Camping

> ## 🖐 Visuals are developed externally — do not regenerate
>
> **As of 2026-08-08, Camping's imagery is Jack's, made by hand in Flow outside
> this repo.** Do not generate character sheets, panels or a cover for this
> story, and do not try to reconstruct or replicate what already exists. The
> prompt-ledger initiative
> ([`design/2026-08-08-story-covers-and-prompt-ledger.md`](../../../design/2026-08-08-story-covers-and-prompt-ledger.md))
> explicitly excludes Camping and Karen for this reason.
>
> The **written canon below is still ours and still authoritative** — story,
> beats, characters, songs. It is only the image pipeline that lives elsewhere.
> The two character sheets in `characters/img/` and the Flow Character IDs in
> `characters/{tarquin,bob}.md` are kept as a historical record, not as a
> pipeline to feed.

> **Source of truth** for the Camping story — the single canonical folder,
> consolidated 2026-08-05 from the Kai <-> Jack story conversation in
> [`./master-notes-2026-08-04.md`](./master-notes-2026-08-04.md) (2026-08-04). That
> transcript outranks everything that came before it; the previous `camping`
> and `camping-v2` folders are retired and live on in git history. Method:
> [`../../storytelling.md`](../../storytelling.md); tone:
> [`../../voice.md`](../../voice.md); house style: the `badcode-art-direction`
> skill.

EP1, track 1. The trader who caused 2008 and the man it ruined meet outside
Waitrose — and an ayahuasca trip drops the trader five years forward into the
tent, after the AI has taken even his job.

## Canon

- [`story.md`](./story.md) — the locked structure: concept, the twelve beats,
  devices, decisions log, salvage list — **plus the
  [scene-by-scene storyboard](./story.md#storyboard--scene-by-scene-video-guide)
  Jack records the story video from**: shots, draft narration/dialogue, asset
  checklist
- **[`shot-list.md`](./shot-list.md)** — **the edit order**: every shot in the film
  in the order it appears in the cut, one line each, plus the shot-depends-on-shot
  chains and the "start here next session" list. The assembly view of the
  storyboard; `story.md` still wins on canon.
- [`master-notes-2026-08-04.md`](./master-notes-2026-08-04.md) — the archived
  Kai <-> Jack session transcript this canon was distilled from
- [`characters/tarquin.md`](./characters/tarquin.md) — Tarquin (posh London,
  sneering; 2008 / 2026 / ruined variants) — Flow sheet + Character record
- [`characters/bob.md`](./characters/bob.md) — Bob (Scouse, weathered; 2008
  variant) — Flow sheet + Character record
- [`characters/tent.md`](./characters/tent.md) ·
  [`characters/wank-tank.md`](./characters/wank-tank.md) — load-bearing object refs
- [`style.md`](./style.md) — thin per-story style notes (locations, warmth
  rules, motifs)
- [`year-device.md`](./year-device.md) — **where the year is shown.** ✅ Ruled 2026-08-30: a
  two-instance device, and it lives on the **Thames foreshore** (`1y` 2008 / `4y` 2026), not on
  the skyline — the cloud-break version was run and failed. Both plates are shot
- [`songs/camping.md`](./songs/camping.md) — the "Camping" track (lyrics + Suno
  style/exclude; predates the restructure)

## What's committed vs open

The **scene structure is locked** — the twelve beats in `story.md` are the
agreement. The exact narrator words and per-scene details are deliberately
open ("there's a really funny way to say that thing" is allowed to arrive
later). Change the story here first, then the media.

## Production tracker

| Medium | Where | Status |
| --- | --- | --- |
| Story spine | [`story.md`](./story.md) | **locked structure** (2026-08-04 master notes) |
| Storyboard (video) | [`story.md`](./story.md#storyboard--scene-by-scene-video-guide) | drafted from the spine — Jack to shoot from |
| Shot list (video) | [`shot-list.md`](./shot-list.md) | cut order, 12 scenes / 38 shots — **scenes 1–7 and 8a shot (4c dropped), 6c locked; 8b in progress — next session starts there** |
| Flow prompt ledger | [`prompts.md`](./prompts.md) | verbatim **still** prompts as restore points (video prompts not recorded, ruled 2026-08-26). **complete through scene 4** — 1a, 1b, 1c, 2a, 4a all recovered 2026-08-26 |
| Song — "Camping" | [`songs/camping.md`](./songs/camping.md) | **accepted prompt** — duet re-cut, same words, rebuilt casting so Bob and Tarquin stop blending. Signed off at round 17, 2026-08-21 |
| Song — released take | [`songs/camping-released.md`](./songs/camping-released.md) | the published version, and the lyric-fidelity reference. Jack's video is cut to it |
| Song — prompt history | [`songs/camping-prompt-history.md`](./songs/camping-prompt-history.md) | archive: what failed in each of the 17 rounds and why, plus the previous cue sets as revert targets |
| Video | Jack, from the storyboard section of `story.md` | next up |
| Music video (Premiere cut) | [`music-video.md`](./music-video.md) · `/mnt/d/badcode-videos/camping-music/` | **in progress** — Kai cutting; picture to 43.56s of 236.4s, flicker runs built by hand |
| Comic | `apps/web/src/comics/camping/` | **tells the old spine** (v1 recut, 24 pages) — rebuild from this canon when the video has proven the telling |
| Social posts | — | not started |

## Notes on the retirement

- `camping-v2/` (the pipeline rework of the old spine) is deleted; its useful
  parts were carried in here: the character visual specs and Flow records, the
  object refs, the style notes, and the character sheets in
  [`characters/img/`](./characters/img/). Its storyboard told the old story and
  was not carried.
- The Flow cloud project is still named `camping-v2`
  (`9b729074-da88-4668-a442-458e9a0f15ac`) and holds the `@Tarquin` / `@Bob`
  Flow Characters — the name refers to the Flow project, not a docs folder.
- The choose-your-own-ending idea stays parked in
  [`docs/ideas/camping-bandersnatch.md`](../../ideas/camping-bandersnatch.md).
