# Stupidity Optimised: the film, rough 1

Scene folder: [`film/`](./film/). Shots, stills and motion prompts are in `film/prompts.json`; replacements are in
`film/rerolls.json` and `film/video-jobs.json`. Media is in `clips/film/` inside the Premiere project folder.

## Premiere

**Project:** `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\optimised stupidity\optimised stupidity.prproj`
**Sequence:** `Optimised rough 1`, 1280×720 at 24fps, 576s (9:36)
**Built:** 2026-11-01 by session (bridge), bin `film`

| Track | What |
| --- | --- |
| V1 | 71 clips of 8s each in shot order 1 to 71, then `72b.jpg` held for 8s, 0→576, no gaps |
| A1 | Each clip's own Flow sound effects, 0→568. The last 8s are silent |

**Applied**
- `v0:71` Motion Scale, keyframed 93.1 to 102 eased: a slow push-in on the held still. Keyframe time on a still is
  source time, which starts at 3600, not 0. Two stray keyframes at 0 and 8 sit outside the clip and do nothing.
- A marker on the last 8s explains the held still.

**Outputs**
- Frames in `frames/`, checked by eye. Premiere saved them as `.png.png`, so the bridge reports `EXPORT_FAILED` after
  waiting 120s even though the frame exists.
- Render: none, as Jack works in Premiere only.

**Needs a human**
- No voices or narration yet, so nothing is cut to length. Every shot runs its full 8s.
- Shot order is the shot list, not a cut: no flashing ambulance-light transitions, and the Scene 15 replay is not built.
- On-screen labels are not added.

## Premiere, rough 2

**Sequence:** `Optimised rough 2`, 1280×720 at 24fps, 532s (8:52), built 2026-11-01 as a new sequence. Rough 1 is untouched.
Layout comes from `film/rough2-plan.json`, with cuts under 1.2s merged into the next shot when placed.

| Track | What |
| --- | --- |
| V1 | 72 shots in order, 91 clips. A shot shorter than its lines repeats from its start, which reads as a jump cut. Shot 72 is the held still with the same push-in |
| A1 | Each clip's own Flow sound effects, about -32 to -43 LUFS |
| A2 | 87 voice lines, one clip each, trimmed at silence only, levelled to about -16 LUFS with clip Volume |
| A3 | 7 music cues, baked to -32 LUFS, then +3 dB clip Volume, so about -29. Tracks and credit are in `../sound.md` |

**Checked:** no clip overlaps on any track and no gaps on V1. An offline mix was written to the scratchpad only, to measure
levels (voices -16.2, music -32.0 before the +3 dB). Gemini heard a 90s stretch of it and said every word was clear over the
music. It also said no music was audible at 5:40–5:58, which is why the music went up 3 dB. Not re-measured after that.

**Words:** each line was transcribed by Gemini and compared with `film/voice-lines.json`. Wrong takes were re-rendered up to
four times. Transcription is unreliable on one-word lines, so those are unproven. Still reading as different: 033 ("the
study the app sourced") and 052 ("verruca"). `by: claude` lines there are stand-ins, including the Scene 7 prophet lines and
"Got it"s, Scene 10's app line and "Oh my god. It works."

**Needs a human**
- Nobody has listened with real ears. Accents were only spot-checked (one narrator line read as Northern, not West Midlands).
- Mouths are not synced to the voices.
- Still missing: search-bar and app text, flashing ambulance-light transitions, the Scene 15 label replay.
- The "glitchy line" Jack reports could not be found: no line in the clip files on measurement across every clip, and none in
  exported Premiere frames. Next step is a screenshot from him.
  2026-11-02: captured the Premiere window itself (PowerShell PrintWindow, no focus change) at 1:00 and 4:10. The
  program monitor is clean. Two lines do run across every clip, both in the timeline panel, not the footage: the
  **yellow render bar** above the clips (no preview render yet; Sequence > Render In to Out turns it green) and the
  **white volume/opacity line** through each clip (the timeline's keyframe display). Neither exports. Awaiting
  Jack's confirmation of which one he meant.

## Picks and re-rolls

Claude chose every still and clip, as Jack asked on 2026-11-01. He has not reviewed them.

| Shot | Used | Why it differs from the first attempt |
| --- | --- | --- |
| 26 | `so-26-26b.mp4` | Flow returned nothing on the original motion, in which he chokes on pills. The softer motion worked. The cause is not confirmed |
| 41 | `so-41-41b.mp4` | The first still and clip had a second Brandon under the sink |
| 45 | `so-45-45b.mp4` | The first clip's ambulance became a white van marked POLICE and swung round |
| 65 | `so-65-65b.mp4` | `UPLOAD_REFUSED` three times; the same still re-saved at 1280 wide went through |
| 72 | `72b.jpg`, held | Jack asked for bloody shoes. Flow makes the still but fails every clip of it within seconds, across four submits and two motion prompts, so it is a held frame. `so-72-72.mp4` is a moving take with grubby trainers |

## Rough 3, BUILT (2026-11-02), awaiting Jack

**Jack's notes (2 Nov):** make it clear the meeting is about an **AI** data centre and they're anti-AI, not anti-water ("the
whole water argument makes no sense, people just don't know how they work"); the app, **Enough's Enough**, must appear on
screen on a phone the first time he uses it, designed like a real app; no lip sync anywhere; clip sound drowns the
narration; add the missing bits; watch and listen to the whole thing first.

**Watched first (done):** an offline watch copy of rough 2 (`scripts/scene/watch-copy.py`, scratchpad only, not a
render for Jack), frames every 3 s, a Gemini watch-through (`feedback/2026-11-02-gemini-watch-rough2.md`, loose, and not
checked point by point), and per-second levels. Findings:
- **Clip sound:** it peaks at -15 to -20 dB rms in about 44 s of the film, as loud as the voices (about -19). The Flow clips
  carry made-up babble speech at 0:40, 1:38, 5:10 and 6:00 (`feedback/2026-11-02-clip-sound-transcript.txt`).
- **The app** is never seen. The data-centre stakes only show up at 7:34.
- **The data-centre model shot** (62) holds static for 16 s.
- **Scene 15's label replay** is not built.

**Done:**
- ✅ Script: Scene 13 b3, Scene 14 b2, a new N line (14 b2b) and Scene 15 b5 rewritten, all marked as mine. Facts are in
  `../research-data-centre-water.md`.
- ✅ Voices: the four new takes, transcribed word for word, are in `clips/film/voices/trimmed-r3/` (-16 LUFS baked, so 0 dB
  clip Volume), recorded in `film/voice-lines.json` under `lines_r3`. The TTS venv is `~/.cache/badcode-tts/venv`
  (google-genai); the scripts' own Python lacks it.
- 🟡 Lip sync: a LatentSync batch of 31 jobs, one per speaker per talking shot, each on a crop of that speaker's face. Small
  faces are upscaled up to 4x. Each job's audio holds only that speaker's lines, so other mouths shut. Files:
  - Tools: `scripts/lipsync/crop-sync-prep.py` and `scripts/lipsync/latentsync-batch.py`.
  - Job files: `film/lipsync-r3/`.
  - Work dir: `~/.cache/badcode-scenes/stupidity-optimised/ls-r3/`; `jobs.json.log.jsonl` there shows progress.
  - A killed run restarts where it stopped: rerun the same command (see the batch script's docstring).
  - Shot 52 is synced to the new Jenny line.
  - Skipped as too small to read: 16, 30, 45, 55, 65, 66. Shot 56 is typing, not speech.
- 🟡 Graphics: `film/graphics/gfx.html` + `render.mjs` (Playwright, transparent ProRes 4444). The scenes are:
  - search bar (shot 6)
  - lock-screen ad (35)
  - first use: chat, study card, calendar Allow (36)
  - permission run (43)
  - partner (46)
  - sorry checklist (50)
  - journal (56)
  - goals (63)
  - Community Champion badge (64)
  - goal complete (66)
  - replay labels
  - planning notice on the model
  - Ted's leaflet
  - ambulance-light flash

  The script passes a syntax check. **Not rendered or looked at yet.** Jack stopped the session at the first test render.

**Session 2 (2 Nov, later):**
- ✅ Graphics rendered and looked at over their shots: 21 files in `animation\optimised stupidity\clips\film\gfx\`
  (ProRes 4444 with alpha; the leaflet is an opaque mp4, 6.2 s). The leaflet's fonts were fixed (Impact is not on Linux:
  now Anton and Archivo Black) and it was moved down so the headline is not cropped. Job list: `film/graphics/jobs.json`.
  Labels carry the original activity as a small line above (GOING TO BED / UPTIME).
- ✅ Lip sync: 30 of 31 jobs synced; **51-brandon failed (no face found)**, so shot 51 syncs Jenny only. Composed with
  `scripts/lipsync/crop-sync-compose.py` (soft ellipse per speaker, 24 fps, no audio) to
  `animation\optimised stupidity\clips\film\lipsync\so-NN-ls.mp4`. Checked by eye on before/after mouth strips: no seams,
  mouths move on the lines. Not yet checked against the voices by ear.
- ✅ Music: `m5-r3.wav` (Comfortable Mystery 4, 0 to 56.35 s) and `m6-r3.wav` (Lightless Dawn from 0:15, 121.66 s), faded,
  at about -32.5 LUFS, beside the old cues in `music\cues\`. Placed at +3.5 dB clip Volume.
- ✅ Plan: `scripts/stupidity-optimised/rough3-plan.py` (from rough 2's bridge state) and `rough3-place.py` (the two
  premiere_eval bodies: place, then levels). Inserts in rough-2 time: +1.8 s and the 19.8 s water block after shot 55 (377.83), +10.4 s of labels after shot 60 (441.17), and at E3: in rough 2's timeline shot 62 actually
  ends at 469.04 (its last sliver was merged into 63), so shot 62 runs on 1.6 s there by repeating from its start.
  - Water block (19.8 s after shot 55 + 1.8 s): leaflet 6.2 s (through "Rubbish"), the burst pipe (15) 6 s on the leak
    fact, the meeting (55) 3.4 s on "Nobody in that room…", the model (62) with the planning notice 4.2 s on "They're not
    against the water. They're against the AI."
  - Shot 55's extra 1.8 s: 0.75 s more of 55, then a 1.05 s cutaway to the hall (53).
  - Label replay over 40, 48, 36, 51, 54, 53, 56, 49, 1.3 s each from 2 s into each clip.
  - A1: each clip capped so its loudest second is at -38 dB rms; shots 7, 14, 47 and 54 muted (babble).

## Premiere, rough 3

**Sequence:** `Optimised rough 3`, 1280×720 at 24fps, 565.8 s (9:26), built 2026-11-02 as a new sequence in bin
`Optimised rough 3`. Rough 1 and rough 2 are untouched. Project saved.

| Track | What |
| --- | --- |
| V1 | 106 clips: rough 2's picture rippled for the three inserts. Shot 72 held still with the same push-in (Scale 93.1→102) |
| V2 | 24 lip-synced shots (`clips/film/lipsync/so-NN-ls.mp4`): 10, 11, 14, 17, 18, 21, 25–29, 32, 33, 37, 44, 47–49, 51 (Jenny only), 52, 54, 59, 64, 70 |
| V3 | 25 graphics: the app on the phone at 6, 35, 36, 43, 46, 50, 56, 63, 64, 66; the planning notice; 8 labels; 6 ambulance flashes |
| A1 | Clip sound, each clip's loudest second at -38 dB rms or lower; 9 clips muted (shots 7, 14, 47, 54: made-up babble) |
| A2 | 88 voice lines: rough 2's with 059, 065, 072 swapped for the r3 takes, plus 088 (the water block) |
| A3 | 7 cues; m5 and m6 are the longer r3 cuts |

**Checked:**
- Every clip on every track matches the plan (position, in point, length); no V1 gaps after two 1-frame gaps from the 1.3 s labels were closed.
- Levels measured on an offline mix (scratchpad only, not a render): clip sound peaks at -38.0 dB rms against voices at a median -17.9 while speaking (in rough 2 they were level); music median -29.8; mix -17.0 LUFS.
- 19 exported frames looked at (`frames/r3-*.jpg.jpg`): phones, leaflet, planning notice, labels, badge and the held still all sit right.
- The four new lines, cut from the mix, heard by Gemini: every word audible. It heard "how AI works" for "how one works", "earns the AI" for "earns the app", "spying on our town" for "spying on a town", and "And now he's" for "And he's". **Unverified**: the takes were transcribed word for word when voiced, and Gemini has been loose before. A human ear settles it.

**Needs a human**
- Nobody has watched or heard rough 3. The lip sync is checked on mouth strips by eye, not against the voices by ear.
- Shot 72 is synced (`ls-r3/72/`) but left off V2: its synced copy has no push-in, so it would jump against the moving still.
- 51-brandon could not be synced (no face found).
- Gary in 70 has his head down, so his sync barely shows.
- The new lines and the graphic design (cream, ink, signal-orange, "enough's enough.") are mine and not ruled.

**Departures, said on purpose:** `look.md` says no interface on the picture. Jack's note asks for the app on screen, so
phone inserts and labels now go in. I took the graphic design choices (cream, ink and signal-orange, serif wordmark
"enough's enough.") myself, and none of them is ruled.

## Premiere, rough 4 (current)

**Jack (2 Nov, after rough 3):** "this video is way too long… just trim the existing clips and speed up the speech, they
talk too slowly, maybe just make it times 2 or whatever sounds good, listen and watch it to suggest improvements."

**Sequence:** `Optimised rough 4`, 1280×720 at 24fps, **414.2 s (6:54), down from 565.8 s (9:26)**, built 2026-11-02 as
a new sequence in bin `Optimised rough 4`. Rough 3 is untouched. Nothing was removed: same shots, lines, graphics and
cues, in the same order. Project saved.

**How** (`scripts/stupidity-optimised/`):
- `fast-voices.py`: every line's pauses over 0.22 s cut down to 0.22 s, then time-stretched with ffmpeg rubberband
  (pitch and formants kept) towards 3.0 words a second, between ×1.08 and ×1.3; one- and two-word lines ×1.2. Not ×2:
  a test at up to ×1.45 was called rushed and chipmunky by Gemini. Exceptions: 009 ("Um, yeah… gains") kept at ×1.0
  with its pauses, since halting is the joke; 021 (100 pills) ×1.15. Speech total 381 s → 303 s. New files in
  `clips/film/voices/fast-r4/`.
- `rough4-plan.py`: one time map from rough 3 to rough 4. Lines shrink to their new length; a gap between lines
  keeps 0.3 s plus half the rest; the label replay keeps 80% so the labels stay readable (1.04 s each); the tail after
  "Asset dealt with" is capped at 2.5 s. V1 clips keep their in point and lose their tail. Lip-sync clips (V2) and
  graphics (V3) are re-timed frame by frame through the same map (`clips/film/r4/v2`, `r4/gfx`), so mouths and phone
  prompts follow the faster words. Flashes keep their speed. Cues cut to their new length with a fade (`r4/music`).
- Placed with `rough3-place.py`, then `proxy.py` built an offline watch copy (scratchpad only, not a render).
- The plans are kept beside the scene: `film/rough3-plan.json`, `film/rough4-plan.json` (with the time map's knots), and
  `film/voices-fast-r4.json` (each line's tempo and the pauses cut).

| Track | What |
| --- | --- |
| V1 | 106 clips, tails trimmed. Shot 72 still with the push-in (Scale 93.1→102 over its 5.96 s) |
| V2 | 24 lip-synced shots, re-timed |
| V3 | 25 graphics: 18 re-timed, 6 flashes, plus the planning notice |
| A1 | 104 clip-sound pieces at rough 3's levels (9 muted) |
| A2 | 88 faster voice lines at rough 3's levels; 067 replaced by `067b` (below) |
| A3 | 7 cues, cut to length |

**Checked:**
- All 155 video and 88 voice clips match the plan (file, start, length); no V1 gaps; 199 levels set, none missed.
- Mix measured on the offline copy: voices -19.1 LUFS integrated, music -29.0, clip sound -42.0, mix -19.4.
- Frames from the proxy: phones, the planning notice and labels sit on their shots.
- **Fixed an old fault:** 067 ("Best day of my life…") says "Ted's doing the leaflets" twice. The take had it from
  the start (it's in the `heard` field of `voice-lines.json`). `067b-brandon.wav` cuts the repeat; Gemini heard it
  end cleanly on "leaflets".
- Gemini compared three fast takes with their originals and heard the same words in each. Its "English soy cow",
  "high-tech center" and "Nissen hut" are its own mishearings, since it hears them in the originals too.

**Gemini's notes on the cut (watch and listen, UNVERIFIED, for Jack to judge):**
- Still rushed: the steroids confession (030), the permission prompts (035–038), the water block (088), the closing
  stakes line (072r3). These run at ×1.3.
- Beats lost before punchlines: "It doesn't." (012), "Can I lift." (060), "Handling them." (078), "Drink your shake,
  son." (054). Gaps over 0.3 s were halved.
- Still drags: the sun-on-the-balls run in Scene 7; 5 s of music before "You got me?" in Scene 17.
- Cut first: the water block (88, an info dump straight after the meeting speech), then Scene 7's liver and ice-bath
  beats.
- Lip sync: possible drift on the plumber at 1:17 and on Gary's "Logistics" at 3:32. Not checked by eye.
- Protect: the ambulance ("Put that protein shake down, love"), the steroids confession, and Gary under the bar into
  "Asset dealt with".

**Needs a human:** nobody has watched or heard rough 4. The open items from rough 3 still stand.
