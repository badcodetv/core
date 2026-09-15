---
story: gitpush-origin-master
scene: ghosts
cut: 5
supersedes_cuts: empty-street (old 5), vantage (old 6), robots (old 9, unfired), ghosts (old 7)
status: BEAT LIST RULED · 48s ffmpeg preview · timeline build OWED
updated: 2026-09-13
---

# Cut 5 — `ghosts`, merged

**Ledger for the merged cut.** Why it exists and what each beat carries:
[`../critique-pass-7.md`](../critique-pass-7.md). Canon lines stay in [`../story.md`](../story.md)
scenes 8, 9, 10 and 12. Media stays on `D:` under `clips/empty-street/`, `clips/vantage/` and
`clips/ghosts/` — nothing was moved.

## Preview

`CUT5-MERGED-PREVIEW.mp4`, 48.0s, 960×540, silent — built with ffmpeg for the Cutting Room board.
**Preview only** (ruling 2026-08-24): the deliverable is the per-beat clips on a Premiere timeline.
Ghost beats are held stills with a 4% linear push; no ghost video has been fired.

## Premiere

**Project:** `/mnt/d/badcode-videos/gitpush-origin-master/gpom-story.prproj`
**Sequence:** *not built* — planned name `gpom-short-05-ghosts` (a new sequence, so the cut-2
session's work on `gpom-s01` is untouched).

🔴 **Blocked 2026-09-13:** `premiere_status` reported the bridge port held by another live Claude
session (the cut-2 rework thread). Not killed, per `premiere-automation` §1d. Run the build from
whichever session holds the bridge, once nobody is hand-editing.

### Build spec — replayable

All clips are already imported (bins `05-empty-street`, `06-vantage`); the six ghost stills
need importing into a new bin `07-ghosts`.

| t (s) | Track | Item | Source in → out | Notes |
| --- | --- | --- | --- | --- |
| 0.0 | V1 | `C5-street.mp4` | 2.0 → 5.0 | |
| 3.0 | V1 | `C5-screen.mp4` | 2.0 → 5.0 | |
| 6.0 | V1 | `C5-robot.mp4` | 2.0 → 5.5 | |
| 9.5 | V1 | `C6-b1-stadium.mp4` | 2.0 → 5.0 | |
| 12.5 | V1 | `C6-b6-pub.mp4` | 2.0 → 5.5 | |
| 16.0 | V1 | `C6-b7-piano2.mp4` | 1.0 → 6.0 | |
| 21.0 | V1 | `C7-b1-street.jpg` | still, 3.0s | Motion Scale push 100→104 |
| 24.0 | V1 | `C7-b2-kitchen-START.jpg` | still, 6.0s | push 100→104 |
| 30.0 | V1 | `C7-b3-face.jpg` | still, 5.0s | push 100→104 |
| 35.0 | V1 | `C7-b2-kitchen-END.jpg` | still, 3.0s | no move — the check is a repeat |
| 38.0 | V1 | `C7-b5-hall.jpg` | still, 6.0s | push 100→104 |
| 44.0 | V1 | `C7-b6-hall-empty.jpg` | still, 4.0s | hard cut in, no move |

Strip Veo audio from the C5/C6 clips. Markers at 6.0 (*It worked. Nobody was there to see it.*),
16.0 (*I could compute everything…*), 21.0 (*So I brought you back.*), 44.0 (silence).

## Needs a human

- The line *handed over, not seized* needs a home (default M2, or in the bulletins).
- Narration GEN E + cut-6 drafts to be re-cut to ~48s together with the ghosts' lines.
