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
