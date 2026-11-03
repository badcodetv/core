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
