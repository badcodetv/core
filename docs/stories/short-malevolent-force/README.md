# The Malevolent Force (a BadCode short)

> **A short is a project** (Kai, 2026-11-10): ID `short-malevolent-force`, Drive `Shorts/The Malevolent Force` (row in `scripts/drive/folders.json`),
> each machine points the ID at its own folder. Made with `new-short`, which runs `new-scene` on the one scene in
> `scenes/malevolent-force/`. The list: [`docs/marketing/badcode-shorts.md`](../../marketing/badcode-shorts.md) (#83).

## The idea

Kai and Jack, 2026-11-13 meeting (docs/misc/2026-11-13-meeting.md): "make going to buy bread really scary." Buying bread made terrifying with horror-film music, at 50p → £1 → £5 → £50. The ghost is inflation, and the money printer is in the hands of whoever decides that day. From the #36 Magic Money Tree talk: The Conjuring 2, where you fear the old man, then find he is trapped by the nun. Jack: "the system is the nun, the mouthpiece is the old man." Kai: blaming one person makes it about money again; the evil should be a force you can't see. The Fredo is a running joke here too. Jack wants to do one horror short.

**Point:** Inflation is not weather: someone decides who gets the new money first, and you meet it last, at the till. The evil is a force you can't see, never one person.

## Checks owed
- 🔴 The lines on every short (`docs/marketing/badcode-shorts.md`): no AI people in real footage, no AI likeness of a real politician, the reader rules.
- 🔴 Any balaclava (`docs/brand/README.md`): reference + zoomed check of the triangle in every still and clip.
- ⬜ `marketing-gatekeeper` before posting.

## State

| Stage | State |
| --- | --- |
| Set up | ✅ 2026-11-15 (Jack: "make all those stills for each and put them on the new scene skill… use your best judgement, don't ask questions") |
| Mood board round 1 | ✅ 9 stills, no votes (Jack moved on to his reference photo) |
| Mood board round 2 | ✅ https://claude.ai/artifact/K5CptJtk7JHuW8KCHeHvrY (clean room from Jack's night-shop photo, 15 stills); Jack picked PR2-b/c/e, FO2-c/d/e |
| Beats | ✅ 2026-11-16 `scenes/malevolent-force/brief.md`: one bread trip, 6 stills + end card, no voice; end card "Based on true events. Coming to a shop near you." + chocolate 10p→£12 (Jack) |
| Clips + music | ✅ 2026-11-16: shots 1 a2, 2 a, 3 a2, 4 b, 5 b, 6 FL4-b swap; music vibes1 |
| Rough cut 2 | 🟡 2026-11-16 https://claude.ai/artifact/2xC772Jtzb5LNK5qWYYFFX (20.8 s, lightning + logo ending added); in Premiere (`short-malevolent-force-1-malevolent-force-r2`), saved, agreed cut on Drive |

## Premiere

**Project:** `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\shorts\malevolent-force\malevolent force.prproj`
**Current sequence:** `short-malevolent-force-1-malevolent-force-r5`, 1080×1920 @ 24, 21.5 s · built 2026-11-18 from `cut/r5/edl-premiere.json`
(rough cut 2, `…-r2`, is kept beside it, untouched).

| Track | What |
| --- | --- |
| V1 | `r5-01` shop 0→1.58 · `r5-02` door 1.58→3 · `r5-03` figure behind the door 3→3.5 · `r5-04` aisle 3.5→4.21 · `r5-05` peek 4.21→5.21 · `r5-06` shelf drop 5.21→6.5 · `r5-07` shelf hand, 50p → £5 6.5→11.08 · `r5-08` mirror 11.08→12.71 · `r5-09` freezer swoop, £5/10p → £50/£12 12.71→16.29 · `v-card` 16.29→18.92 · `v-logo` 18.92→21.5 |
| A1 | `mus-track.wav`: suspense strings (basses take 2, 0.92x) with a stab at 7.95 and 14.0 s (the hand), silent under the card and logo |

Shots are cut from the finished picture (`cut/r5/shots-vhs.mp4`), so the subtle VHS, the blurs and the drawn prices are baked
in and there are **no handles**: a re-trim beyond a shot's edges means a rebuild from `scripts/shorts/malevolent_force_cut_r4.py`.
`v0:7` (mirror) and `v0:9` (card) were each lengthened one frame to close two rounding gaps. Frames 10.6 s and 15.8 s exported and checked.

**Needs a human:** the export (from Premiere, never ffmpeg), then `scripts/delivery-qc.sh`.
