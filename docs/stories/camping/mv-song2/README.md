# Camping MV on song 2: the beat cut (2026-11-07)

Jack's words: `cleanroom/jack.md`. Song: `songs\camping vid\action\song 2 maybe (audio).wav` (220.7 s, 172 BPM).
Premiere: **`camping song 2 beat 1`** (a clone of `camping song 2`, cleared and rebuilt). `camping`, `camping balaclava 1`,
`camping song 2` untouched.

## What song 2 is (measured, `analysis/`)

- `analysis/analyse.py`: faster-whisper words + librosa beats for the old song and song 2 (whisper lives in `~/.venvs/whisper`).
- Song 2 is the old song rearranged, not shifted: a 12 s intro (old: 25 s), verse 1 (Bob) 12–56, **new sung hook "I can't live
  like this forever"** 56–77.6, verse 2 (Tarquin) 77.7–121, hook 121.6–143.3, bridge 143.6–183.7, hook 183.7–205, outro to 220.7.
  The hooks sit where the old song had instrumental breaks. Some lines are rewritten.
- `analysis/breaks.py`: per-bar bass energy, which finds every drum dropout and drop. The listening tool's section map
  (docs/listening/log/2026-11-07-100153-…) was ~5 s off the transcript, so not used for timing.

## Jack's 14 s trick, measured

In `camping` at 12.44–14.72: black for 5 beats over the intro breakdown, then four 3–4-frame flashes of `clips/2.mp4` (each from a
different point in the clip: 0, 1.96, 3.52, 8.44 s) with one black frame between, over the last 2 beats, landing on the drop.
He used the same stutter six times (≈14, 19.6, 24.9, 117.7, 142.7, 204.7 s). In the new cut every stutter is rebuilt with its
flashes exactly on eighth notes (0.174 s, frame-rounded), landing on a beat: 13.44 (the 808 drop, the intro trick, black from
11.04), 105.16, 131.40, 187.76, all within 0.01 s of the beat.

## The cut (`cut/`)

- `flatten.py` → `edl-old.json`: `camping balaclava 1` as the topmost clip at each frame (no effects or keyframes anywhere, checked).
- `timemap.py`: old → new time from 343 matched lyric words, DTW in the hook gaps; hand anchors at the bridge end (Jack's black on
  "And by the time it hits", his drop shot 35.mp4 on song 2's drop at 183.65).
- `plan.py` → `edl-new.json`: 136 pieces, 96 of 99 cuts on a beat (flicks under 6 frames keep their place before the cut they
  lead into), the intro trick, the hook-3 gap (song 2's hook 3 is 21 s longer than the old outro).
- `overlays.py` → `overlays.json`: V2 action shots on their lyric lines (Waitrose, M3, resent me, Chateau, car park in the rain,
  got the sack, the AI, robots, government) and hook montages (hook 1 Bob's life, hook 2 Tarquin's life, every other bar);
  a long rap shot may cut away mid-line, keeping 1 s either side; Jack's own cutaways are never covered (white tank, tent, tax the
  rich and door already had his own shot, so those were left). V3: four shots from the v2 world (different look and cast; mute V3
  to lose them). Hook-3 gap on V1: x3 x4 16 29 x5 25 18 (4 beats each), then u25 17 x6 32 held 8 beats into the end card.
- Extra Bob/Tarquin action used: Jack's unused 5, 7(not used), 16, 17, 18, 25, 27, 29, 31, 32 (26 left out: he sings into a mic);
  v2: gp-w9, 05, 24, 25 (1080 copies in `action\v2-1080\`).
- `build.py` → `place-N.js` (run through premiere_eval). Clip audio on A2/A3 (muted); A1 = song 2 only.
- Checked: 136 V1 pieces match the plan exactly, no slivers, all 29 black gaps intended. Saved.
- `preview.py`: a low-res check render to the scratchpad only (it drifts late on; trust the Premiere timeline).

## Stage-rap swap (done 2026-11-07)

- All 13 rap shots swapped for the round-5 stage-rap clips (`../mv-balaclava/cleanroom/r5/`, bin "stage rap clips"):
  `cut/swap_rap.py`, same slots and lengths; holds over 4.2 s split on the beat nearest the middle (second half re-enters
  0.8 s in); s05p used to 5 s (jacket changes after), t06p to 4 s (head turns side-on). No old rap clip left, no slivers. Saved.
- Flags for Jack: s03p turns side-on ~3.5 s (triangle out of view briefly); the split holds repeat a move (a jump cut on the beat).

## Round 6: Venom-style rap clips (2026-11-07) — ▶ RESUME HERE: `camping song 2 beat 2` BUILT, awaiting Jack

Jack said the stage-rap clips "float in the air". All 13 were redone, grounded (see `../mv-balaclava/picks.md` "Round 6").
Clips `cb-<shot>v-*.mp4` (1080p copies in `balaclava/video/premiere/`), all checked. Flags: t06 turns side-on briefly at ~1 s
and ~7 s (triangle out of view); t04 goes quiet after ~4 s.
**Built:** `camping song 2 beat 1` cloned to **`camping song 2 beat 2`** (beat 1 untouched); the 13 clips are in bin `venom rap clips`;
`cut/swap_venom.py` (run on beat 1's state) → 34 overwrites on V1, same slots. A slot split in two now carries on through the clip
(the second piece starts where the first ended) rather than repeating a move. Checked: all 34 match the plan, no r5 piece left, no
slivers, every other V1 piece unchanged. Saved.

## Round 7: T3 rap clips + the beat re-cut (2026-11-07 evening) — ▶ RESUME HERE: `camping song 2 beat 4` BUILT, awaiting Jack

Jack: *"just use T3 locked, understated style for all the clips for rap gesturing then put it in a new sequence, once they are in,
watch and listen to it, then cut it to the beat with complete freedom, since the cutting/trimming does not match the beat"*.
- **`camping song 2 beat 3`**: clone of beat 2, every r6 rap piece swapped for its T3 clip (`cut/swap_t3.py`, bin `t3 rap clips`),
  old timing. Checked: 34 pieces match, nothing else moved. Saved.
- **Why the cut was off the beat (measured, `analysis/bars.py`, `analysis/grid.py`):** the song is **88 BPM**, straight, snare on 2 and 4
  (listening log `docs/listening/log/2026-11-07-152100-…`); librosa's beat list was EIGHTH notes (172-176) and ran ~57 ms late (up to
  169). Only **12 of 167** cuts in beat 2 sat on a real beat (median 179 ms off). Downbeat phase from the big energy entrances
  (99.0, 205.4, 210.9 s all land on the "1"); local drum drift ±30 ms, +60 ms in the last 30 s, followed.
- Fresh sealed web research `cleanroom/research-beat-cut.md` (hip-hop cuts cluster on bar lines; picture early is safe, late is not;
  sections open on the one; verses hold, hooks 2 beats to a bar, bridge long holds).
- **`camping song 2 beat 4`** (`cut/recut.py` → `edl-beat4.json` → `cut/build4.py`): a clone of beat 3, cleared and rebuilt. Same shots in
  the same order (lyric matching kept), every cut re-placed on the beat 0-1 frame early, sections open on their downbeat (verse 1 19.87,
  hook 1 55.32, verse 2 77.13, hook 2 120.76, bridge 142.59, hook 3 183.55, outro 205.41), min holds verse/hook 2 beats, bridge 1 bar;
  Jack's stutters rebuilt as 3-frame flashes an eighth apart over the 2 beats before the landing beat (13.73, 105.09, 126.23, 131.68,
  187.66). 19 short pieces merged into neighbours and 12 dropped (`cut/recut-report.json`). Checked from the saved state: 134 pieces
  match the plan, **all 86 main cuts 0-2 frames before the beat**, median shot 1.36 s. Saved.
- Not watched as a render (Jack's no-renders rule): checked structurally only. Flags: the downbeat reading is measured, not
  confirmed by ear (rap lines come in on beat 2 under it); the first 0.72 s is now black before the logo.

## Round 9: `camping song 2 beat 5` (2026-11-07 night) — BUILT 2026-11-09

Jack: *"do Ghostface Killah for all clips ... make a new sequence, also those 4 bits where it flashes to black to the beat that i asked
you to keep, get rid of and do your own version but only do it for the start and end where bob is running through the tunnel"*.
- **`camping song 2 beat 5`** = a clone of beat 4 (beat 4 checked untouched first: 106/24/4 pieces = plan). Beat 4 untouched.
- `cut/recut5.py` → `edl-beat5.json`: every T3 piece → that shot's Ghostface clip (`../mv-balaclava/cleanroom/r9/picks.json`); stutters
  at 103.68, 124.84, 130.28 closed (rap clip runs on / next shot starts on the first flash's beat); the start (10.96-13.68) and end
  (186.24-187.60) stutters replaced by an accelerating tunnel-run cut from `clips/2.mp4` on the 88 BPM grid, no black: start =
  back view 2 beats, running at us 1 beat, face 1/8, shout 1/8 → m12; end = back view 1 beat, running at us 1/8, face 1/8 → 16.mov.
- `cut/build5.py` → `b5-clear.js` + `b5-place-N.js` (premiere_eval on beat 5, active). Before: import the 1080p copies
  (`../mv-balaclava/cleanroom/r9/to1080.sh`, bin `ghostface rap clips`). Waits on the s01 clip (recut5 needs every shot's pick).
- **Built 2026-11-09:** s01 clip made (closed-fist rewrite), all 13 Ghostface clips imported to bin `ghostface rap clips`, beat 5 cleared
  (215 items) and rebuilt from `b5-*.js`: 122 pieces (V1 94 / V2 24 / V3 4), no fails. Every stutter gone; the six one-beat blacks of
  beat 4 (2.08, 98.92, 120.72, 133.68, 181.44, 217.64) are Jack's own and kept. Tunnel run at 10.96 and 186.24 checked on the state file.
  Beat 4 untouched (106/24/4). Saved. Next: Jack's notes.

## Round 10: `camping song 2 beat 6` — the stadium opening + the bridge face-off (2026-11-09) — ▶ RESUME HERE: BUILT, awaiting Jack

Jack's words: `cleanroom/r10/jack.md`. Clean room: three web-only researchers (`cleanroom/r10/research-stadium.md`, `-faceoff.md`,
`-cut.md`), four sealed writers who read one brief each (`brief-st/du/re/ly.md` → `st/du/re/ly.md`, `parse.py` →
`prompts-r10.json`, `clips-r10.json`), run verbatim (`run_stills.mts`, NB2 + per-shot references kept in
`~/.cache/badcode-scenes/camping-r10/ref`; clips Omni Flash via `scripts/scene/run-rolling.mts` on scene `../mv-r10`, Flow project
`72255ea1`). Media: `songs\camping vid\r10\` (moodboard, video, video/premiere 1080p). Still checks and picks: `cleanroom/r10/check.md`,
`picks.json`. All 31 clips strip-checked at 1 fps.
- Watched and listened first: beat-5 check render (scratchpad only) + the listening tool on the intro and bridge (logs 2026-11-09-0951*).
- **Opening 0–10.96:** the dark bowl (st01d) → the DJ in one beam (st04d) → BADCODE snaps on with the first drum hit 2.76 (st02) →
  a floodlight bank (st03) → DJ lit (st04) → the whole lit stadium on the bass 4.12 (st01, the matched pair of st01d) → crowd at the
  barrier (st05), another bank, the stands (st06), DJ arms up, crowd → him from behind over the crowd (st07) → the tunnel run, unchanged.
- **Bridge 142.56–183.52:** masked rappers trading lines (du01–07) cut against the real Bob and Tarquin meeting and arguing in the car
  park at night (re01–06), speaker matched to the lyric sheet (unverified on song 2). Cutaways on the words: rained on (b23), the sack
  (t21), drank (ly01), broke my back (ly02), the AI does the fast part (ly03), will it allow / in charge now (ly04, barrier stays down),
  C-suite (ly05), robots (ly06), government debased (ly07), "when we very first met" = Jack's verse-1 Waitrose clip 4.mp4. Regret holds
  longer (re04, du06 2 s+). **The clink lands on "same SIDE" (178.96: contact at 3.55 s into du08).** "We'll be gone" is one held two-shot
  (du09) over the drum stop into the hook. The "woods" clips (last verse 5, 6.1) are gone; V2/V3 inside the bridge cleared.
- `cut/recut6.py` → `edl-beat6.json` → `cut/build6.py` → `b6-*.js`; bin `r10 stadium + bridge clips`. Beat 5 cloned to beat 6, cleared
  (191) and rebuilt: V1 123 / V2 19 / V3 0, every piece matched the plan (du09 one frame short, trimmed to 183.52), no slivers. Saved.
  Beat 5 untouched.
- **Timeline page (notes): https://claude.ai/artifact/WbEmR8LxhyoT4LSjL1nbjM** (page round 1 · camping song 2 beat 6 · in sync).
- Flags for Jack: Jack's one-beat blacks at 2.08 (opening) and 181.44 (the shout) are now covered by picture; the other four stay.
  du01 (two 1.4 s pieces): the posh man's triangle sits on his right eye in profile. Tarquin's green jacket reads as dark leather at night.
  Bob's "I was wrong" starts 0.2 s before his shot.

## Round 11: Jack's timeline notes → `camping song 2 beat 7` (2026-11-09 pm) — ▶ RESUME HERE: BUILT, awaiting Jack

Jack (on beat 6): *"this is almost ready, just need to timestamp a few changes, it is great though"*. 20 notes on the timeline page
https://claude.ai/artifact/WbEmR8LxhyoT4LSjL1nbjM, dumped to `../mv-r10/feedback/timeline-r1/`, answered on the page (`../mv-r10/cut-notes.json`).
- ⚠ The round-1 page ran ahead of the song (up to 1.4 s by the end): `scripts/camping-mv2/song2-timeline.py` (and the older
  `balaclava-timeline.py`) cut pieces with `-t`, which lost a frame here and there. Now frame-exact (`-frames:v`), drift 0. Notes were
  read against what Jack saw (page piece map), not edl times.
- Jack had edited beat 6 by hand (the ending: logo at 212.2, song ends 214.6): found by diffing the sequence before building, kept.
- Edits from footage we had: film clips from `Camping Comic/Camping Video NEW!/new clips` (bin `r10 film clips`; 17 is 4K, a 1080p copy
  `r10/video/premiere/film-17-1080.mp4`), Jack's clip 37.mov = the M3. New (clean room writer fx, `cleanroom/r10/brief-fx.md`): st11d/st11p
  (the dark stadium + its floodlit twin, cut 3 frames lit on each beat) and du02x du05x du06x du07x (masks closed, triangle showing, no neck).
- `cut/recut7.py` → `edl-beat7.json` → `cut/build7.py`: beat 6 cloned to beat 7, cleared (192), rebuilt: V1 138 / V2 18, all match,
  no slivers, du09 trimmed to 183.52. Saved. Page round 2 · camping song 2 beat 7 · in sync.
- Open for Jack: the wine twice (118.7 V1, 121.4 V2); the wine clip pours rather than drinks.

## Round 12: `camping song 2 beat 8` (2026-11-09 pm) — BUILT

Jack: *"read my notes please and only make those changes, change nothing else this is literelly perfect"* — one new note (at1154,
0:46): no rapping there. Beat 7 cloned to beat 8 and ONE shot overwritten: 44.36-47.08 clip 13 → ly07 (money in the gutter) from 5.0 s,
the car rolling in on the drop (`cut/recut8.py` → `edl-beat8.json`); its orphan muted A2 clip removed. Checked: 0 other video
differences. Saved. Page round 3 · camping song 2 beat 8 · in sync. Seven suggestions are on the page (cut-notes.json plan), NOT done:
Bob's verse-1 action sandwich, one look for the TV DJ in hooks 1-2, more opening pulses, ly07 and the wine each used twice, du01's
triangle; the ending was listened to and is clean.

## Round 13: `camping song 2 beat 9` (2026-11-09 pm) — ▶ RESUME HERE: BUILT, awaiting Jack

Jack (chat): *"at 3 mins 15 seconds, bobs bag dissapears, please use an action clip from a prevoius camping music video sequence there
instead"*. Beat 8 cloned to beat 9, ONE shot: 194.48-195.84 x3 → Jack's clip 33 (boot stamping into the mud by a MANAGER badge; in the
earlier song-2 sequences, not in beat 8), from 2.2 s (`cut/recut9.py` → `edl-beat9.json`). Checked: 0 other video differences. Saved.
Page round 4 · camping song 2 beat 9 · in sync. The seven round-3 suggestions still wait for Jack.
