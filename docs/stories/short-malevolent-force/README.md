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

**Project:** `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\shorts\malevolent-force\malevolent force.prproj` · **Sequence:** `short-malevolent-force-1-malevolent-force-r2`, 720×1280 @ 24, 20.8 s · built 2026-11-16 from `cut/r2/edl.json`

| Track | What |
| --- | --- |
| V1 | shot 1 `mf-01-w2-FO2-c-treated` 0→2 · 2 `mf-02-PR2-e-treated` 2→4.21 · 3 `mf-03-w2-PR2-c-noaudio` 4.21→6.21 · 4 `mf-04-b-PR2-b-treated` 6.21→10 · 5 `mf-05-b-FO2-d-noaudio` 10→12 · 6 `mf-06-f4b-swap` 12→15.58 · card `v6-card` 15.58→18.21 · logo `v7-logo` 18.21→20.79 (card and logo Motion Scale 66.67) |
| A1 | `mus-track.wav` (vibes1) 0→20.79, silent after 15 s |

**Needs a human:** the export (from Premiere, never ffmpeg), then `scripts/delivery-qc.sh`; a thunder hit under the logo flash if wanted.
