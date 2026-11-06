# Camping music video: the balaclava rappers — picks and state

Jack 2026-11-05 (verbatim in `cleanroom/jack.md`): every shot where Bob or Tarquin raps to camera becomes a BadCode
balaclava man (one rough sleeper, one posh); action shots stay. Clean room.

- **Premiere project:** `songs\camping vid\camping vid Copy-test_1.prproj` (created 25.6, last saved 26.5.2; open in Premiere 2026).
- **Rap-to-camera clips** (`clips\bob rapping` 1, 1.1, 2, 3, 4, 5.5; `clips\Tarquin rapping` 1, 2, 2.1, 3, 4.3, 4.4, 5, 6).
  Maybes, unruled: loose clips 12, 13 (Bob), 19, 23 (Tarquin). In the project but missing from disk: bob 1.5, Tarquin 4.1, 4.2.
- **Round 1 (designs), 2026-11-05:** web research `cleanroom/research.md`; sealed writers w1–w4 → 12 designs (r1–r6, p1–p6),
  NB2 16:9 x2, all 24 made. r4 rewritten twice (too close to r1, then same blue as r3). Faults: r3 triangle outside the ring
  + fingers; r4 reads New York; p1 maybe a bare hand; p6-b red mark at the mouth.
  Board: https://claude.ai/artifact/Tc95mWsa81QThUnHFv4Dbc — awaiting Jack's picks.
- **Next:** read votes (ArtifactData `votes`, `notes`) → shoot each rap shot in the picked design (picked still as reference,
  same place and framing as the original clip) → clips (Omni) → overwrite only the rap slots in a cloned sequence.
- **Round 2 (2026-11-05 evening):** Jack: "more designs, massively different", fixed only balaclava + ring + red triangle over the
  left eye. Fresh material research (`cleanroom/r2/research.md`), a sealed ideas writer (`r2/ideas.md`, 16 concepts, each a
  different material family), 4 sealed writers → `prompts-r2.json`; 32 stills (ids `<a|b><n>r2-<a|b>`), 0 failures. Rough: boro,
  foil, sleeping-bag nylon, carrier-bag crochet, hi-vis, hessian, duct tape, moquette. Posh: tweed, gold chainmail, velvet,
  black crystal, Fair Isle, luggage canvas, toile, houndstooth. Faults: a1 fingerless gloves; triangle near centre on a2 a4 a6
  b2 b4 b6; a8-b triangle outside ring; a5 ring weak. Board version 2, same link. Awaiting picks.
- **Picks on round 2 (2026-11-05):** rough sleeper **a7r2-a Duct Tape Armour**, posh **b1r2-b Estate Tweed Squire**. Jack: "make sure they never show skin".
  References saved to `<media>/reference/rough-duct-tape.jpg` and `posh-tweed.jpg`.
- **Round 3 (per-shot stills):** 3 sealed writers (`cleanroom/r3/`), each saw the original frames + the pick; 18 shots
  (s01–s06 Bob, t01–t08 Tarquin, maybes m12 m13 m19 m23), NB2 with the pick attached. ⚠ Flow trap: with 2 prompts per project,
  the SECOND prompt's take a came back as a copy of the reference (7 times); one prompt per project (`PER_PROJECT=1`) never did.
  Copies kept as `*.refcopy.jpg`; those 7 shots have takes a/b (redo) + c (old b). Every kept take eye-checked for skin.
  Board version 3. Awaiting Jack's take picks, then Omni clips.

## (done 2026-11-06) take picks (Jack, 2026-11-05 night: "those please but dont do anything now, just save them for next time")

Jack's take picks (board round 3, votes in `feedback/moodboard-r3/`), one still per shot to animate:

| Shot | Replaces clip | Take to animate |
| --- | --- | --- |
| s01 | bob rapping/1.mp4 | s01r3-a (my pick 2026-11-06: closest to the original close-up; Jack said just get on with it) |
| s02 | bob rapping/1.1.mp4 | s02r3-a |
| s03 | bob rapping/2.mp4 | s03r3-b |
| s04 | bob rapping/3.mov | s04r3-b |
| s05 | bob rapping/4.mp4 | s05r3-b |
| s06 | bob rapping/5.5.mp4 | s06r3-b |
| m12 | 12.mp4 | m12r3-b |
| m13 | 13.mp4 | m13r3-a |
| t01 | Tarquin rapping/1.mp4 | t01r3-a |
| t02 | Tarquin rapping/2.mp4 | t02r3-b |
| t03 | Tarquin rapping/2.1.mp4 | t03r3-a |
| t04 | Tarquin rapping/3.mp4 | t04r3-b |
| t05 | Tarquin rapping/4.3.mp4 | t05r3-b |
| t06 | Tarquin rapping/4.4.mp4 | t06r3-a |
| t07 | Tarquin rapping/5.mp4 | t07r3-b |
| t08 | Tarquin rapping/6.mp4 | t08r3-a |
| m19 | 19.mp4 | m19r3-a |
| m23 | 23.mp4 | m23r3-b |

He picked all four maybes, so clips 12, 13, 19 and 23 count as rap shots (confirm in passing). Stills are in
`<media>/moodboard/<id>.jpg` (media = `songs\camping vid\balaclava`).


**2026-11-06, Jack:** "basically just anything with them talking to the camera is rapping, just replace those ones."
Checked every clip visible on the `camping` sequence (contact sheet of all 53 sources; timeline page
https://claude.ai/artifact/WVScfLPy242nXzuExhH2y9): the talking-to-camera shots are exactly these **13**, so only these get animated:
s01 s02 s03 s04 s05 s06 m12 · t03 t04 t05 t06 t07 t08. **Dropped** (not on screen in the cut): t01, t02 (Tarquin 1, 2 not on the timeline),
m13 (always under a higher track), m19, m23 (not on the timeline). Not to camera, so kept: clip 22 (beach phone call), `last verse/*`
(Bob and Tarquin talk to each other), `badcode guy/*`.

**Next session, in order:**
1. Ask about s01.
2. Animate each pick (scene-animation; Omni Flash, Frames, 16:9, 720p, 8 s): rap to camera, big gestures, head still so
   the triangle holds, no mouth (there isn't one), no skin. Clean room the motion prompts (sealed writers).
3. Clip-check every mask frame by frame (the triangle drifts in motion; see Bank Robbery's `mask-clip-check.md`).
4. Premiere 2026 (bridge on): clone the sequence, then overwrite ONLY the rap slots, keeping each slot's in/out length.
   Read the timeline first (which slots use which rap clip). Bob 1.5 and Tarquin 4.1 / 4.2 are in the project but missing
   from disk: check if they sit on the timeline.

## Round 4: clips (2026-11-06)

- 13 shots to animate (list above). Motion prompts from 4 sealed writers (`cleanroom/r4-clips/brief-w1..w4.md` → `w1..w4.md`
  → `clips.json` → `video-jobs.json`), each shown the picked still + a 2 fps strip of the original clip (`<media>/originals/strip-<id>.jpg`),
  web research reused from the Bank Robbery gang clean room (`mv-gang/cleanroom/research-clips.md`, web only).
- Settings in scene.json `video`: Omni 1.1 Flash, Frames, 16:9, 8 s, 720p, count 1. Runner: `scripts/scene/run.mts`.
- fresh.py: only matches are this round against itself, plus the shared camera-lock line ("Locked-off camera, framing holds; the editor
  adds any camera move"), kept on purpose.
- ⚠ Two slots run longer than 8 s: s05 (8.8 s) and t08 (10.0 s). Fill in Premiere (repeat a beat of the clip, or 0.9× on a held gesture).

## ▶ RESUME HERE — `camping balaclava 1` BUILT (2026-11-06), awaiting Jack

- 13 clips made (Omni Flash, one take each; the first five also have a spare take in `<media>/video/inbox/dupes/`), every one
  checked on a contact sheet: masks hold, gloves on, no skin, nothing morphs. Small flag: m12's triangle goes ragged mid-clip (the cut
  shows ~1 s).
- Premiere: `camping` cloned to **`camping balaclava 1`** (original untouched); bin `balaclava clips` holds 1080p silent copies
  (`<media>/video/premiere/`, lanczos up from 720p, so no scaling). 26 overwrites (`premiere/swap.py`, `swap-plan.json`): same track, span
  and in point as each original (pulled back to fit the 8 s clip). s05 (8.8 s) and t08 (10 s) are two pieces each, jumping back to 2 s in.
  Checked: no original rap clip left visible (only 12.mp4 at 57.60 on V3, under V4 as before), no slivers, frames exported and looked at. Saved.
- Timeline page (plays the new cut, NEW = balaclava clip): https://claude.ai/artifact/WVScfLPy242nXzuExhH2y9 (page round 2 · camping balaclava 1 · in sync)
- Left as is: the original rap clips' sound on the muted tracks, and Bob's `3.mov` clip sound on A6 (unmuted, 47.20-48.48) — ask Jack
  whether that one should go now Bob is gone from the picture.
- Runner fix: `scripts/scene/run.mts` now waits for the tiles after its reload (it saved nothing on the first run); `scripts/scene/harvest.mts`
  pulls every finished tile from the open project when a run misses them.
