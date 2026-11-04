# The balaclava gang: picks and rulings

## 2026-11-03: the brief

Jack's words: `cleanroom/jack.md`. Brief: `brief.md`. Rulings:

- Song: `Youtube Vids\animation\songs\bank robbery\the version.wav` (Suno 81953c32, Kai's lyrics). Transcribed with Whisper: `song-transcript.json`.
- More balaclavas; the jeweller's-shop gang (Colour Noir `mask1` b, `noir\moodboard\r2-mask1-3\00-b.jpg`; clip `noir\video\mask1-b.mp4`) and more like them rap to camera all through, gesturing hard.
- The picture shows each lyric literally ("grandma freezing" = a grandmother freezing).
- More action: hot rods, Tommy guns, robberies. Researched on the web.
- **The balaclava rule, every story** (saved in `docs/brand/README.md`): triangle over the right eye, no skin, gloves, no robot features. ⚠ "Right eye" taken as the wearer's right (left of picture); the Colour Noir masks had it the other side. Unconfirmed.
- Clean room.

## 2026-11-03: clean room, round 1: 48 shots, 96 stills

- Research (web only, a researcher told not to read the repo): `cleanroom/research.md` (32 set pieces, period cars, rap-to-camera gestures, Nano Banana 2 notes, literal economics pictures). Could not verify: an oil smoke screen from a car (boats only) and a 1920s armoured-car robbery, so those two shots were swapped for the frozen-river whiskey convoy and the mail-train job.
- Shot list (`cleanroom/shots.py`): my plain facts per lyric line from the transcript, plus 7 action shots; the six-man gang sheet (plum, bottle, crimson, marine, rust, silver), each colour and suit fixed.
- 12 sealed writers × 4 shots (`cleanroom/brief-wN.md` → `wN.md`, `make_briefs.py`), parsed by `parse.py` to `prompts.json` and `moodboard.json`. Run verbatim plus "Thanks.", Nano Banana 2, 16:9, 2 takes each, a fresh Flow project per 2 prompts (`run_stills.mts`, log `run_stills.log`).
- Same-prompt check against every past prompt: no identical or near copies. Repeats are framing phrases ("the left of the") and the gang sheet's mask wording, kept on purpose so the masks stay the same.
- Known by reading: c02's cop wears a "tall domed helmet" (US cops wore peaked caps); run verbatim, flag if it shows.
- Flow: 8 shots timed out once ("Failed, not charged"), and the runner's retry in a fresh project got 6 back. v07 (grandma) and v11 (the Fed) failed twice, so each had one phrase changed (in `prompts.json` → `departure`): "A robber called PLUM" → "A masked man called PLUM"; "central-bank building" → "stone building". Both then ran. 96 stills, recipe cards written.
- By eye on two contact sheets: the triangle still lands on the picture's right in many shots (the rule wants the left); c02 has a British helmet and a readable "BUTCHER" sign; in crowd shots some masks lose their ring.
- Mood board: https://claude.ai/artifact/5BjXvFxB36RYqijxRGGRQF (`moodboard.html`, `build-moodboard.py`), with the Colour Noir jeweller still as the reference card. Waiting on Jack's picks.

## 2026-11-03: Jack's ruling on round 1: the masks are wrong

Jack: *"Please do them all again but the masks are wrong they should be like the ones in [the jeweller's shop reference] with the triangle over the left eye and the white cirlce, maybe use it as a refernece image or make one thanks"*

- Rule corrected in `docs/brand/README.md`: white ring, triangle over the wearer's LEFT eye (right of picture), as the jeweller-shop masks. The "right eye" reading is withdrawn.
- Made a reference: the jeweller still attached, six-man line-up facing camera (`gang\reference\lineup-a.jpg`, picked by me: all six rings white and the triangle on the picture's right; take b lost the crimson ring). Staged at `~/.cache/badcode-refs/gang/gang-lineup.jpg`.
- Round 2: the same 12 writers kept their shots and changed only the masks, plus one sentence pointing to the reference (`correction-r2.md` → `wN-r2.md` → `prompts-r2.json`). Departures: v11's block fix re-applied; c02 "tall domed helmet" → "peaked cap" (US police).
- Run with the reference attached (`flow_edit_image` path), one prompt per Flow project: on a second prompt in one project Flow handed back the uploaded reference as the "result" (a02). Round 1 rows kept in `moodboard-r1.json`.
- Result: 95 stills (d10 one take). Refused twice and changed once: d07 (sawing a woman → a dove from a top hat), v07 (run without the reference, as in round 1). No still was a copy of the reference (`refdup.py`). By eye: rings white and the triangle on the picture's right throughout; c02 b and x01 print shop signs. Republished to the same board; waiting on Jack's picks.

## 2026-11-03: clips round 1, stopped for Jack's picks

- Jack: *"i like all of them, make videos out of them, clean room and research the internet to make them, then add it to premiere with uxp, and make another sequence in Bank Robbery with the new song"*. Research (web only): `cleanroom/research-clips.md`. 12 sealed clip writers (`brief-clip-wN.md` → `clip-wN.md` → `clips.json`, `video-jobs.json`), no copies of past prompts. Omni 1.1 Flash, Frames, 16:9, 6 s, one clip per still, via `scripts/scene/run.mts` (Flow project `9849e924`).
- Edit plan: `edit-plan.json` (`cleanroom/edit_plan.py`), 71 cuts on the Whisper line times.
- Jack then: *"95 clips seems like too much, so show me all the stills in the new scene link and ill pick which to make videos from"*. Runner stopped after 16 clips (a01–a03, c02–c04, d01, d02, both takes). Refused: c01-b and c02-b (POLICY_BLOCKED; c02-b later came through), c01-a silently failed 4 waves; c01's motion rewritten by me (`clips.json` → `departure`), not yet run. Wave 7 (c01-a, d03 a/b, d05 a/b) was in flight when stopped; not harvested.
- Board republished asking for This on each still to animate.

## 2026-11-03: Jack's picks for clips

Dump: `feedback/moodboard-r3/votes/`. Jack: *"use these picks and continue thanks"*.
- Picked (34): a01 a, a02 b, a03 b, c01 b, c02 b, c04 a, d02 b, d05 a, d06 a, d08 b, d10 a, d11 a, d12 b, e03 a, f01 a, f02 a, f03 b, f08 b, v01 b, v03 b, v05 b, v06 b, v07 b, v08 b, v11 b, v12 b, v13 b, v14 a, x01 a, x02 a, x03 b, x04 a, x06 a, x07 b.
- Already animated: 6 of them. New clips: 28 (c01-b d05-a d06-a d08-b d10-a d11-a d12-b e03-a f01-a f02-a f03-b f08-b v01-b v03-b v05-b v06-b v07-b v08-b v11-b v12-b v13-b v14-a x01-a x02-a x03-b x04-a x06-a x07-b).
- The cut uses only these 34 (plus the other takes already made for c03 and d01, since they exist); edit plan rebuilt.

## 2026-11-03: clips made and `Balaclava Gang 1` built

- 43 clips made (Omni 1.1 Flash, 6 s): Jack's 34 picks minus c01-b, plus the 16 made before he picked. c01-b refused three times (POLICY_BLOCKED, then twice silent, even after my rewrite): no clip. d08-b and d11-a refused once each, then passed (d11-a after a one-line rewrite: `clips.json` → `departure`).
- By eye on first/middle/last frames: masks hold, nothing morphs. Faults: x01-a prints a "BAKERY" sign, c02 a/b a "BUTCHER'S SHOP" sign (both from the stills).
- Premiere, `bank robbery.prproj`: bins `Balaclava Gang song` (the version.wav) and `Balaclava Gang clips` (43). Sequence **`Balaclava Gang 1`**: the song on A1 (0–209.6 s), 65 cuts on V1 from `edit-plan.json` (in-point 0, cut on the Whisper line starts), each clip's own sound on A2, **A2 muted**. No gaps; V1 ends 209.67. Placed by `cleanroom/premiere_place.py` evals in batches with saves.
- Substitutes: c01-b's two chorus slots (61.86, 123.74) got a02-b and a02-a (the doors bursting in). Lines whose still Jack didn't pick get the nearest picked clip (marked "not picked" in `edit_plan.py`).
- Checked against the lyrics: a mid-cut frame per shot labelled with the words Whisper hears ±1.2 s, two sheets; every picture sits on its line (e.g. 36 s grandma on "grandma freezing", 46 s the Fed finger on "the Fed is not your friend", 113 s the vault wheelbarrow on "stack up the vaults like a wheelbarrow"). Whisper times are loose by ~0.3 s; cuts are not yet on the beat.
- Unwatched by Jack. Next: his notes on the timeline.
- Timeline page (scene-timeline): https://claude.ai/artifact/8jVNcLhe45pFMDwXoodHH1, built from `cleanroom/assemble_cut.py` (ffmpeg proxy of the same 65 cuts) + `scripts/scene/build-timeline.py`. Page round 1 · Balaclava Gang 1 · in sync.

## 2026-11-03: cut 2 (`Balaclava Gang 2`), from Jack's timeline notes

Jack: *"please pay attention to the notes i left on the timeline page. also bring back some of the action clips from the last cut into the new one, there were cool action scenes. also please listen and watch the video, so you can cut it to the beat."* Notes dump: `feedback/timeline-r1/notes/`.
- 0:05 *"same scene twice"* → rods3-b (Colour Noir) after the gang walk.
- 0:36 *"his triangle on his balaclava should always be on the left eye, on anyone wearing a badcode balaclava"* → v07-b mirrored (`bg-v07f-b-…-mirrored.mp4`, ffmpeg hflip). Audited every gang clip by eye: all others already left eye. Rule unchanged (it already said left eye).
- 1:00 *"there is no one in the drivers seat"* → x01-a dropped at all three places.
- Colour Noir action back (10): rods3-b, safe2-c, pov2-a, pov1-b, chase1-a, chase3-a, safe1-b, safe4-b, rods4-a, rods2-b. Left out: mask3-a (black rings, triangle on the right eye), mask1-b (the green robber's triangle on his right eye).
- To the beat: listened (`docs/listening/log/2026-11-03-170503-the-version.md`: drop 0:07.5, chorus 1:02, 2:04, final 3:07.5; drums out 2:55–3:07) and tracked (~92.3 BPM, kick on 1 and 3). The beat tracker drifted up to ~0.35 s, so each cut snaps to the strongest percussive hit from 0.33 s before to 0.2 s after its line (`hits.json`, `cleanroom/plan_r2.py` → `edit-plan-r2.json`); 64 of 65 moved, max 0.33 s.
- Built: `cut2/preview.mp4` (no black or frozen frames), Premiere `Balaclava Gang 2` (65 on V1, song A1, A2 muted, no gaps), page republished with replies (`cut-notes.json`). Page round 2 · Balaclava Gang 2 · in sync.

## 2026-11-04: round 3 asked for: the singer, action parodies, sarcastic stage gestures, faster cut

Jack on `Balaclava Gang 2`, verbatim: `cleanroom/r3/jack.md` (not enough action or Prohibition gloss; action-movie parodies with the balaclava men; the singer, a woman, raps throughout as "a harley quinn type character with a bat" in the balaclava style, stills of her to pick; the rappers gesture like a stage rapper, sarcastically; clean room; cut on the beat and much faster; timeline page once cut).
- Research (web only, sealed): `cleanroom/r3/research.md` (30 action tropes moved to the 1920s, glossy period glamour vs AI slop, the bat-woman signature elements to avoid, stage-rap gesture vocabulary, fast cutting at 92 BPM, Nano Banana tips).
- Shot list `cleanroom/r3/shots.py`: 10 singer designs (h), 16 action parodies (k), 12 gesture shots (g); briefs `make_briefs.py` → `brief-wN.md`.
- Jack: *"smaller first"*: only the singer this round. The singer is ORIGINAL: no name of any existing character, none of its signature elements (diamond pattern, red/black split, jester hood, pigtails, face paint, mallet).
- 5 sealed writers (w1–w5) → `cleanroom/prompts-r3.json`, run verbatim plus "Thanks.", Nano Banana 2, 16:9, 2 takes, no reference. Same-prompt check: no copies of past prompts; the shared mask sentence kept on purpose. 20 stills, two timeouts passed on retry. Round-2 board rows kept in `moodboard-r2.json`.
- By eye: h03 triangle top-centre, h09a low-centre; h01, h03, h05, h07 legs read as skin or sheer stockings (rule: no skin); h02's background gang have plain masks.
- Board republished (same link), singer only. Waiting on Jack's pick.

## 2026-11-04: the singer dropped; action stills next

Jack: *"maybe we forget her and focus on the action stills, then show me in the next scene link thanks"*. The singer is out (her 20 stills stay on disk, rows in `prompts-r3.json`, nothing picked). Writers w6–w9 run the 16 action parodies (k01–k16), with the six-man line-up reference attached, one prompt per Flow project. The gesture shots (g01–g12) are briefed but not run.
- 2026-11-04: action round run. 4 sealed writers (w6–w9) → `prompts-r3.json` k01–k16; same-prompt check: only the mask wording repeats (10–22 words, kept on purpose). Nano Banana 2 with the line-up reference, one prompt per project; k13 timed out once, then passed. 32 stills, none a copy of the reference (`refdup.py`, now checks r2 and r3).
- By eye: masks hold (white rings, triangle on the picture's right). Faults: k08a 1960s cars and police cars, k08b a 1940s car (wrong period); readable words on k06b (plate), k12 a/b ("THEATRE"), k13b ("GIN" crates); k11 the man on the ladder reads as unmasked at this size.
- Board republished (same link), action only. Waiting on Jack's picks.

## 2026-11-04: Jack's 13 action picks animated; 20 more parodies stilled

Jack: *"please come up with more parodied action scenes that fit this please research the internet and do more stills in next scene. clean room the ones i liked and make the videos thanks"*. Dump: `feedback/moodboard-r5/`.
- Picked (13): k01 a, k02 b, k03 a, k04 a, k06 b, k07 a, k09 a, k10 a, k11 a, k12 a, k13 b, k14 a, k16 a. Not picked: k05, k08, k15.
- Clips: 3 sealed clip writers (`r3/make_clip_briefs.py` → `brief-clip-cwN.md` → `clip-cwN.md`, `r3/parse_clips.py` → `r3/clips.json`, appended to `video-jobs.json`); research = `research-clips.md` + `r3/research.md`. No repeats of past prompts. Omni 1.1 Flash, Frames, 16:9, 6 s via `scripts/scene/run.mts`. **12 made** (`gang\video\bg-k…-k…r3-….mp4`); **k14-a stalled** three waves (no clip came back), retried once more.
- By eye on the clips (first/middle/last frames): masks hold, nothing morphs. Faults: k12-a marquees print garbled words mid-clip; k13-b "GIN" crates (from the still); k11-a ladder man reads unmasked when small.
- More parodies: sealed web research `r3/research-more-action.md` (40 new set pieces, period facts graded; two real robberies with deaths to avoid: the 1927 armoured-car and 1922 Denver Mint). I picked 20 → `shots.py` MORE (k17–k36), 5 sealed writers w13–w17. 40 stills, none a copy of the reference; same-prompt check: only mask wording repeats.
- By eye: k31 a/b masks show eye holes; k32 triangle big and centred; k33b mask looks holed.
- Board republished (same link) with k17–k36. Waiting on Jack's picks.

## 2026-11-04: cut 3 (`Balaclava Gang 3`), from Jack's cut-3 brief

- Second clip run: 12 of 13 made (k18 k19 k21 k22-b k23 k24 k26 k27-b k29 k30 k31-b k36-b). k14-a stalled 5 times in Flow, even with a calmer prompt, so it is left out. Checked by eye: k30-a's silver mask may show two red marks, not one triangle.
- Plan: `cleanroom/r3/plan_r3.py` → `edit-plan-r3.json`: 214 cuts, 0.98 s average, 43 lyric shots from cut 2, 24 action clips, every cut snapped to a drum hit. Choruses, drop and outro cut on every beat; verses and break every 2 beats; drums out (2:55–3:07) one bar per shot; half-beat flurries on "Robbery!".
- Built: `cut3/preview.mp4` (209.6 s, no black, frozen frames or gaps). Premiere `Balaclava Gang 3` (720p at 24 fps, from a clip): song on A1, 214 cuts on V1, clip sound on A2 muted. 24 k clips imported into the bin "Balaclava Gang clips". Timeline page round 3 is the same link (https://claude.ai/artifact/8jVNcLhe45pFMDwXoodHH1). Page and sequence are in sync.
- Known: in the outro, the action clips come round in the same order as at the drop.

## 2026-11-04: round 3c, the gestures

- Jack: "do the gestures thanks". Sealed writers w10–w12 (briefs `cleanroom/r3/brief-w10..12.md`, web research only) wrote g01–g12. The same-prompt check flagged only the shared mask-rule sentence, kept on purpose. 24 stills (Nano Banana 2, line-up reference attached), all made. Mood board round 7 (the same link). Faults: g09 shows a GIN crate; g03's triangle sits near the centre; g04's masks are small in frame.
- Jack's picks (`feedback/moodboard-r7`): g08-b, g09-b, g10-b, g11-b, g12-b. And: "Add these picks but also just improve the gesturing of the existing rapping videos thanks."
- Round 3d clips: the 5 picks + 16 redos of the rap-to-camera clips (c03-a c03-b c04-a d01-a d06-a d08-b d10-a e03-a f01-a v01-b v03-b v05-b v06-b v11-b v13-b v14-a) with big sarcastic stage-rap moves, keys `<shot>g-<take>` (the old clips are kept). Sealed writers gw1–gw4 (`cleanroom/r3/make_gesture_clip_briefs.py`), jobs via `parse_gestures.py`.
- Built cut 4: all 21 clips made. Checked by eye: v05g-b turns his back partway through; d08g-b barely moves; d10g-a swings the mic stand up like a pole. Each pick replaces the clip on its exact line (g08→d08g, g09→d10g, g10→v14g, g11→e03g, g12→f08), so d08g/d10g/e03g/v14g are not in the cut. `edit-plan-r4.json`, `cut4/preview.mp4` (209.6 s, no black, frozen frames or gaps). Premiere `Balaclava Gang 4`: song on A1, 214 cuts on V1, A2 muted. Timeline page round 4 (the same link). Awaiting Jack.

## 2026-11-04 · Round 5: masks fixed (Balaclava Gang 5)
- Jack: *"the masks are wrong in a lot of the clips, watch and look for it then replace it"*, *"make sure you analyse the clips properly for the wrong masks to replace, i dont want to waste credits or time"*, *"please do the all 37"*.
- Audit of 65 gang clips: 37 wrong (`cleanroom/r3/mask-audit.md`). New stills r5 (Nano Banana 2, reference `gang-lineup-heads.jpg`), each checked by eye at full size, up to 3 tries (`r3/mask-picks.json`). One Omni clip per passed still with the old motion (`<shot>m-<take>`, `r3/make_mask_jobs.py`).
- Clip check (`r3/mask-clip-check.md`): 18 fixed, 8 better, 9 same fault (the triangle drifts to the middle in motion, or is lost on Crimson), 2 worse (d02, k31: old clips kept, KEEP_OLD in plan_r3.py).
- Built: `edit-plan-r5.json`, `cut5/preview.mp4` (209.6 s, no black or frozen frames, same timing as cut 4, 114 of 214 shots now remakes). Premiere `Balaclava Gang 5`: song on A1, 214 cuts on V1, no gaps, A2 muted, saved. 35 clips imported into the bin "Balaclava Gang clips". Timeline page round 5 (same link). Awaiting Jack; open question: re-roll the 11 still-wrong clips or not.
