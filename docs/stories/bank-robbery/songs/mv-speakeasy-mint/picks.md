# The Speakeasy Mint: picks and rulings (animation stage)

The stills record is `script.md` (one section per scene) and `storyboard.md` → Resume. This file logs the video stage.

## 2026-10-26: Jack, "please make the video"

- **Scene folder:** this folder is now a `new-scene` scene (`scene.json`, `storyboard.json`, `animation-options.json`,
  `video-jobs.json`). Media root = Jack's folder `Youtube Vids\animation\songs\bank robbery` (`moodboard/` = the 38 picked
  stills as `<scene>-<id>.jpg`; `video/` = the clips).
- **38 clips:** one per pick, plus the pairs (13 + 13b, 22a + 22, 24 + 24b, 28a + 28b, 31 + 31b, 32 + 32b). Scene 29 is 9:16
  and post-only (a Premiere ride up the tall still), so it has no clip.
- **Motion prompts:** house lock line at both ends; one or two movers; one ambient motion; "Shot at 24fps with a 180-degree
  shutter" (the sharp-motion tell); "No dialogue"; ~40 words of motion. Nothing rendered falling in flight (3: the moth flies up
  out of frame; 7: the envelope slides through the grate; 26: coins slide, they don't fall). One flash only in 14 (photosensitivity).
- **Settings:** Omni 1.1 Flash, Frames (start frame = the still), 16:9, 720p, 8 s, ×1 (runner defaults; Jack's standing ruling).
- 🟡 **Scene 2's still is a best guess:** Jack's pick ("2b round 2 + side flames") was never matched to a media id; I used
  2b-r2-b `c98067ae` (no side flames). Swap if Jack has the other one.
- Cost estimate: 38 × 12 credits (Omni 720p 8 s, per `2026-10-09-crowd-vault-accent-sweep.md`) ≈ 456 credits.

## Clips: results (2026-10-26 evening)

All 38 rows ran (Omni 1.1 Flash, Frames, 720p, 8s). Each was checked with a 2fps contact sheet and `photosensitivity-check.py`.

| Row | Result | What I did |
|---|---|---|
| 14 · 13b firebox | r1 failed the flash check (9 flashes/s at 4.5s) | `14-r2` (steady rolling flames) still failed at 6.75s. **The first 6.0s pass**, so it is trimmed to 6s on the timeline |
| 15 · 14 bandstand flash | No candidate in 4 waves; the rewrite `15-r2` (no "burst of flash", no "gangsters") also gave none | Treated as a silent block. **Used as an 8s still hold** (`sm-15-14-6d5f89ab-hold.mp4`). Owed: a new still or a very different motion |
| 17 · 16 pockets | r1 painted BAKERY on the blank sign | `17-r2` with "the sign stays a plain blank board" is clean |
| 29 | Post-only (9:16) | 8s pillarboxed hold (`sm-29b-29-ae848e6f-hold.mp4`); the full-size still was re-fetched from Flow into `moodboard/` |
| everything else | Pass | — |

## Premiere

- Project: `songs\bank robbery\bank robbery.prproj`. Bin **`speakeasy-mint clips`** holds every take, including the failed r1s.
- Sequence **`Speakeasy Mint rough 1`** (1280x720, 24fps): 39 pieces on V1 and their own audio on A1, laid end to end in film order, 0:00–5:10.
  Order: 01–13, 13b (r2, 6s), 14 (hold), 15, 16 (r2), 17–21, 22a, 22, 23, 24, 24b, 25, 26, 27, 28a, 28b, 29 (hold), 30, 31, 31b, 32, 32b, 33.
- No song, no trims (except the 13b flash trim), no camera moves, no text yet. Next: lay the song on A2 and cut to it.
- Undo: delete the sequence. The bin can stay.
