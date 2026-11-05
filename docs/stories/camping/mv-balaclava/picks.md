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

## ▶ RESUME HERE (Jack, 2026-11-05 night: "those please but dont do anything now, just save them for next time")

Jack's take picks (board round 3, votes in `feedback/moodboard-r3/`), one still per shot to animate:

| Shot | Replaces clip | Take to animate |
| --- | --- | --- |
| s01 | bob rapping/1.mp4 | ⬜ **no pick** — ask Jack (takes s01r3-a / -b) |
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

**Next session, in order:**
1. Ask about s01.
2. Animate each pick (scene-animation; Omni Flash, Frames, 16:9, 720p, 8 s): rap to camera, big gestures, head still so
   the triangle holds, no mouth (there isn't one), no skin. Clean room the motion prompts (sealed writers).
3. Clip-check every mask frame by frame (the triangle drifts in motion; see Bank Robbery's `mask-clip-check.md`).
4. Premiere 2026 (bridge on): clone the sequence, then overwrite ONLY the rap slots, keeping each slot's in/out length.
   Read the timeline first (which slots use which rap clip). Bob 1.5 and Tarquin 4.1 / 4.2 are in the project but missing
   from disk: check if they sit on the timeline.
