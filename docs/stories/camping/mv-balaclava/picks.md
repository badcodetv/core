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

## Round 5: stage rap, not a geography teacher (2026-11-07)

Jack: *"i asked for the balaclava guy to rap and gesture like eminem on stage, he kind of raps and gestures like a geography
teacher, so fix that, is there something in the prompt or in the repo that is affecting it"* (full words: `../mv-song2/cleanroom/jack.md`).
- **Cause found** (`docs/google-flow/same-clip-traps.md`): the r4 clip briefs pasted in Bank Robbery's recycled action-clip research
  (subtle, one primary motion, small gesture vocabulary, count then stop), quoted Jack's "make it simple" note from another video,
  told writers to match the talking originals, and the stills were chest-up, two seated, no mic. Fixed in the repo: the old research
  file is fenced off, `fresh.py` now lists DAMPERS, the trap doc is linked from CLAUDE.md, the scene-animation skill and memory.
- Fresh web research (sealed): `../mv-song2/cleanroom/research-stage-rap.md`. Sealed still writers w1–w3 (`cleanroom/r5/brief-w*.md`)
  → `prompts-r5.json`: medium-wide/full-body performance stills from low angles, mid-move, a mic in most. NB2 with the design
  reference, one prompt per project, 26 stills. Mask check at full size (`cleanroom/r5/mask-check.md`): s04 and t05 failed both takes
  (bowed head; centred triangle), re-rolled as s04x/t05x and passed. Picks: `cleanroom/r5/picks.json`.
- Motion: sealed writers c1–c3 (picked still + fresh research, no old prompts or strips, damper words banned) → jobs `<shot>p` in
  `video-jobs.json` (old clips kept). fresh.py: no copies, no dampers. Omni Flash, Frames, 8 s, rolling queue.
- Then: swapped into the rap slots of `camping song 2 beat 1` (`../mv-song2/cut/swap_rap.py`).

## Round 6: grounded, Venom-style (2026-11-07)

Jack: *"he seems to float in the air, ai slop is present when he does anything ... watch this [Eminem, Venom] ... to see how he
does this, as in gesturing and rapping at the camera ... clean room it all and research the internet"* (verbatim: `cleanroom/r6/jack.md`).
- **Why r5 floated:** its writers had him prowl or stride at a locked camera, jump, lunge and squat-and-spring, framed full-body small in
  the frame. The feet slid, the body glided forward, and the mask swelled near the lens (`cleanroom/r6/failures.md`). The r5 brief was an
  over-correction of the "geography teacher" note ("continue that energy", banned every calm word).
- **The reference, watched frame by frame** (`cleanroom/r6/venom-observed.md`; frame sheets in `<media>/reference/venom/`, local only):
  rooted on one spot, wide stance, knees bent, weight low; mostly chest-up, handheld close, short elbow/wrist gestures cut off hard
  (temple tap, a claw thrown down, a fist pumped down, a palm chop, a boxer's guard), no mic, no travel.
- Fresh sealed web research `cleanroom/r6/research.md`; 3 sealed writers each wrote still + clip (`r6/brief-w*.md` → `w*.md` →
  `prompts-r6.json`, `r6/clips-r6.json`). fresh.py: no copies; the counts and "subtle handheld" dampers kept on purpose (the research
  and the reference call for tight gestures; this time stiffness is not the fault).
- Stills: NB2 + design reference, one per project. t04 and t06 were blocked by Flow twice and rewritten by their writers (no rail or
  height cues; no "clawed"). Mask check `r6/mask-check.md`; picks `r6/picks.json`.
- Clips: jobs `<shot>v` in `video-jobs.json` (Omni Flash, Frames, 8 s). All checked on 2 fps strips: on the spot, feet planted on the
  wides, masks hold. 1080p silent copies at the clip's own 24 fps in `<media>/video/premiere/`.
- Premiere: `cut/swap_venom.py` (in `../mv-song2/`) overwrites every `cb-<shot>p-` piece in a clone **`camping song 2 beat 2`**,
  same slots; `beat 1` untouched.

## Round 7: five gesture patterns, picked on a page (2026-11-07)

Jack: *"the new sequence has terrible gesturing ... maybe show the 5 examples ... I will choose them from the link"*, then *"dont do 65
clips just do a few ... like 5"* (verbatim: `cleanroom/r7/jack.md`). Round 6's hands hover at the chest in tiny repeated pumps
(`r7/failures-r6.md`).
- Fresh web research `r7/research-prompts.md` (no proven Omni rap prompt exists online; 5 best-bet patterns T1-T5). Five sealed
  writers, one per pattern, wrote all 13 shots (`r7/t1..t5.md` → `r7/clips-r7.json`; 65 jobs `<shot><t>` in `video-jobs.json`).
- Only 6 clips made (the 65-clip run was stopped): **m12 in all five patterns** + s01 T1, from the r6 start frames.
- ⚠ **Runner trap:** `run.mts` names clips by FIRST FRAME, so five jobs on one still all came back as "m12t1" (four went to dupes) and
  the next wave re-downloaded them. The m12 labels were fixed by hand from Flow's grid order (newest first: T5 T4 T3 T2 T1), checked
  against what each clip does (T4 shows a phone and zooms; T1's camera moves). Never put two jobs on one still in one run.
- Page: https://claude.ai/artifact/Ybta5HtYWYvW5RVFBHP88Y (`r7/build_page.py`, picks in db `picks`). Next: dump picks into
  `feedback/`, write the winning pattern for all 13 (prompts already in `r7/t<n>.md`), one clip per shot, swap into a new sequence.
- My read before Jack's: all five still keep the hands near the chest; the start frame (chest-up, hands at the chest) seems to pin
  the gesture more than the prompt does [inference, untested]. T4 drew a phone into the frame.
- **Jack picked T3** (locked, understated) for all. 12 T3 clips made (`cb-<shot>t3-*`; spares `t3b`/`t3c`). ⚠ The runner trap struck
  again inside the T3 run (the unmade T1/T2 jobs on the same stills took the names): ~20 extra T3 takes were made. Fixed in the repo:
  `scripts/scene/run.mts` now refuses to run while two unmade jobs share a start frame; the 47 unmade r7 jobs were dropped from
  `video-jobs.json` (prompts kept in `r7/clips-r7.json`). Built into `camping song 2 beat 3` and the beat re-cut `beat 4`
  (`../mv-song2/README.md`, Round 7).

## Round 8: eight rappers, clean room (2026-11-07 evening)

Jack: *"it still looks strange and boring and ai slop like ... gesture like action bronson, eminem, rza, wu tang, kendrick lamar,
50 cent, and so on, make like 8 versions"* (verbatim: `cleanroom/r8/jack.md`). T3's failure (`r8/failures-t3.md`): every clip
repeated its start pose (finger to the temple, other hand on the lapel), centred, dead in the last seconds.
- Fresh web engine research `r8/research-engine.md` (no tested Veo/Omni rap source; motion transfer from a real clip reported
  strongest; a mid-gesture blurred start still primes motion).
- Eight sealed writers, one per rapper, each watched his videos frame by frame (`r8/<key>-observed.md`) and wrote a NEW start still +
  clip (`r8/<key>.md` → `prompts-r8.json`, `r8/clips-r8.json`). Bob at s02 (flyover): Eminem, 50 Cent, Method Man, Kendrick.
  Tarquin at t06 (beach): Action Bronson, RZA, Ghostface, Rick Ross (Rick Ross is my "and so on" pick).
- Stills NB2 + reference, `ROUND=-r8 run_stills.mts`; mask check `r8/mask-check.md`. Clips jobs `s02em`… in `video-jobs.json`,
  `cb-<key>-<still>.mp4`. fresh.py: no repeats bar the required mask sentence.
- Page: https://claude.ai/artifact/QTyxei2Ae3cZuWDuBA24hK (`r8/build_page.py`, picks in db `picks`). Next: dump picks into `feedback/`,
  write the picked style for all 13 shots (new stills + clips), swap into a new sequence cloned from `camping song 2 beat 4`.

## Round 9: Ghostface for every rap clip (2026-11-07 night) — DONE 2026-11-09, built into beat 5

Jack picked **Ghostface Killah** on the round-8 page: *"do Ghostface Killah for all clips and redo them all, and make a new sequence"*
(verbatim: `cleanroom/r9/jack.md`).
- Two sealed writers (`r9/brief-g1.md` Bob's 7 shots, `r9/brief-g2.md` Tarquin's 5) from the round-8 Ghostface observation, the
  round-8 engine research and the picked t06gf prompt as the target → `r9/g1.md`, `r9/g2.md` → `prompts-r9.json`, `r9/clips-r9.json`
  (`r9/parse.py`). t06 keeps its round-8 clip `cb-t06gf-t06gfr8-a`.
- Stills (ids `<shot>g`, files `<shot>gr9-a/b.jpg`), mask check `r9/mask-check.md`, picks `r9/picks.json`.
  - **s01 trap:** the alley shot came back three times with FINGERLESS gloves (bare fingertips) although the reference has full
    gloves; failed takes kept as `s01gr9-*-fingerless*.jpg`. Writer rewrote it with closed fists: **not yet run**.
  - s05 was blocked by Flow twice (silent "Failed"); rewritten without the tents, passed.
- Clips: jobs `<shot>g` in `video-jobs.json` (11, s01 missing), run started 2026-11-07 20:58 → `r9/run.out`.
- **2026-11-09:** s01 retry 3 PASS (take a), clip PASS, all 12 strip-checked (`r9/mask-check.md`), 1080p done, built into
  `camping song 2 beat 5` (`../mv-song2/README.md` Round 9). Was: run s01g still (`ROUND=-r9 REF=<local rough-duct-tape.jpg> PER_PROJECT=1 npx tsx run_stills.mts s01g`), check gloves, add its
  job (`python3 r9/parse.py jobs s01=<take>`), make its clip; strip-check all 12 clips; `r9/to1080.sh`; then beat 5 (`../mv-song2/README.md`).
