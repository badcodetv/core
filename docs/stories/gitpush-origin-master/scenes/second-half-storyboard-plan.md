# Second half — picks and the storyboard plan (17 October 2026)

Kai's picks on the mood board (https://claude.ai/artifact/UkcXHKhuY8f2rzV7FtQ6e5, db `votes`), read
17 Oct 2026, with his spoken notes. This is the running order for a sequential storyboard page.
Beat letters are those in [`../restructure-2026-10-15.md`](../restructure-2026-10-15.md).
✅ = picked still exists · 🆕 = to generate · 🔊 = audio-led.

## Look rule

**The style travels from 1980s BBC 16mm to futuristic.** The bunker and the meeting are naturalistic,
lived-in 16mm; the clean room is clean, bright, futuristic. One exception, kept: the old lady's
close-up is anamorphic blockbuster.

## The HUD rule

Patrol is grainy CCTV with the red HUD. When the signal comes, the waveform (two voices tagged) sits
briefly **over the CCTV**: *"hang on…"* At **KILL MODE ENGAGED** the whole view **flips to full red
machine vision** and they race. Red vision means kill mode, never patrol. (Kai first said the red flip
comes at the signal, then moved it to kill mode; the kill-mode version is the ruling.)

## Running order

| # | Beat | Frame | Status |
|---|---|---|---|
| 1 | C | Roundabout, high aerial at dusk: kill bots are everywhere | ✅ P1-roundabout |
| 2 | C | Patrol, low and huge from the gutter | ✅ P1-patrol-blockbuster |
| 3 | C | Their POV: CCTV with the red patrol HUD | ✅ P1-pov-cctv-hud-patrol |
| 4 | C | Ping. ORGANIC SIGNAL DETECTED: waveform, two voices tagged, over the CCTV. Brief | ✅ P1-pov-cctv-hud-voices |
| 5 | C2 | The bunker: naturalistic, lived in, 1980s BBC 16mm | ✅ B1-lived-tunnel-threads |
| 6 | C2 | The lavatory: the source of the argument. **This pair are the row** | ✅ B5-the-lavatory |
| 7 | C2 | The row, up close, with **B5's pair** | 🆕 more iterations on the people (A1 dropped) |
| 8 | D | KILL MODE ENGAGED: the view flips to full red, racing | ✅ K5-pov-red-race-hud-kill |
| 9 | D | The bot left spinning in their wake | ✅ K8-bot-in-wake |
| 10 | D | Racing across the downs, aerial | ✅ K9-downs-aerial |
| 11 | H2 | 🔊 The bot to the AI: *"Do you know your kill bots are heading to an organic signal?"* AI: *"There is no organic signal."* Bot: *"Well there definitely is, look, they're racing."* | 🆕 frame for the call (bot, beacon pulsing) |
| 12 | E | Stand down refused; **self-destruct outside the bunker gate** | 🆕 kill bots blow up at the blast doors |
| 13 | E | Inside, the row carries on, oblivious | reuse 7 |
| 14 | F | Into daylight: they climb out, 1980s BBC 16mm | ✅ M1-emerge-threads |
| 15 | F | The bot comes in | ✅ M2-canteen-bot |
| 16 | F | The old lady, anamorphic blockbuster | ✅ M3-old-lady-blockbuster |
| 17 | G, H | The revolt; trust via the CCTV of the self-destruct | ⬜ nothing picked (H can reuse 12 as CCTV) |
| 18 | I | The building: the hundred walk in | ✅ L6-arrival-blockbuster |
| 19 | I | Bunny suits over their jumpers | ✅ L5-bunny-suits |
| 20 | I | The white hall | ✅ L2-white-hall |
| 21 | I | The wafer | ✅ L9-wafer-portal |
| 22 | I | **A hundred chairs laid out like a wafer**, overhead: how they connect to it | ✅ L3-wafer-pattern |
| 23 | I | The same chairs from the floor, looking sideways along the rows, occupied | 🆕 |
| 24 | I | Visible cost: mud on white | ✅ L17-mud-on-white |
| 25 | I | After: the bot alone among the **hundred empty wafer chairs** (CR7 had pods) | 🆕 (CR7-silence-after is the reference) |
| 26 | J | On the phone, on the bus | ✅ Y2-bus |
| 27 | J | Zoom out: the bus drives away down an ordinary high street. *"Don't make me come back twice"*, maybe less obvious | 🆕 |

**How the machine works:** sci-fi, explained away in a line. What matters is that it runs on
consciousness; the hundred chairs in the wafer's pattern are how they connect.

**Kill-bot look:** settled with the picks. The other options read as tanks and stay unused.

## Still owed

- **To generate (6):** the row with B5's pair; the bot's call; the self-destruct at the gate; the
  chairs at floor level; the empty chairs with the bot; the bus driving away.
- **Words:** the H2 call's lines are drafted above; the bot's apology (B) is still owed.
- **Unpicked:** the revolt (G) and the trust beat (H).

## The storyboard page (17 October 2026)

**https://claude.ai/artifact/EGgHQU6KzN9rgzGnyUHb6e**: 27 frames in story order. Each frame has its
still and three ways to animate it, and a "flip through the reel" player. Picks are stored in the db
`picks` collection (`kind` still|anim, `n`, `v`); notes are in `notes`. Data:
[`second-half-storyboard.json`](./second-half-storyboard.json) and
[`second-half-animation-options.json`](./second-half-animation-options.json), written by a
cinematography pass over `docs/cinematography/`, `docs/video-fx/hybrid-method.md`, `docs/flow/` and
`docs/google-flow/`. One change by Claude: frame 7's recommendation is moved to B, because the 15 Oct
ruling was narration, not lip-sync.
Rebuild with `python3 scripts/gpom/build-storyboard.py <storyboard.json> <animation-options.json> /mnt/d/badcode-videos/gitpush-origin-master/clips <out.html>`.

### The new stills (Nano Banana 2, one take each; media in `clips/second-half/storyboard/`)

All of them end with the house suffix: *"16:9 frame from a fictional near-future British film.
Full-frame image, no captions, logos, lettering or on-screen text."* The 16mm ones also carry:
*"Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy
grain."*

- **SB07a–c, the row** (`flow_edit_image`, reference B5-the-lavatory; SB07b used SB07a as its
  reference, because the first try came back unchanged): (a) a waist-up handheld two-shot, she points
  at the seat, he throws his arms wide; (b) a tight close-up of her mid-shout, jabbing a finger, his
  shoulder blurred at the edge of frame; (c) a close-up of him protesting over her shoulder, the seat
  up behind him. Each says to keep faces, hair, jumpers, tiles, the drain pipe and the fluorescent
  light the same.
- **SB11a–c, the bot's call** (16mm): (a) a low close shot of the bot alone at dusk, beacon pulsing
  bright as if speaking on a call, dust hanging where something raced away; (b) a side view at kerb
  height, the bot tilted back as if looking at the sky, a burnt-out bus behind; (c) an extreme
  close-up of the amber beacon and its speaker grille.
- **SB12a–c, the gate** (16mm except b): (a) a wide shot of a concrete Cold War bunker entrance in a
  grassy Wiltshire hillside, green blast doors shut, three kill bots bursting apart one after another
  in white flashes, sparks and black smoke, the doors untouched; (b) the same as grainy black-and-white
  security-camera footage from a pole; (c) the aftermath, three wrecks smoking on scorched grass, the
  doors unscathed.
- **SB23a–c, the chairs from the floor** (clean): (a) floor level along a curving row of occupied
  white reclining chairs in a wafer grid, white suits over jumpers, eyes closed, a line of light from
  each chair into the floor; (b) an old woman holds the hand of the boy in the next chair; (c) ground
  level along the full grid, pale-gold light rising under every chair at once.
- **SB25a–c, after** (clean): (a) the bot alone in the middle of a hundred empty wafer-grid chairs, a
  glove and a mug on the floor, beacon flashing slowly; (b) overhead, the bot tiny at the centre of
  the empty circular grid, gloves and a coat left on seats; (c) floor level from behind the bot along
  the empty rows, a muddy boot print and a child's drawing on the nearest seat.
- **SB27a–c, the bus drives away** (photographic, night, rain): (a) a wide shot of an ordinary high
  street, a red double-decker pulling away past a chip shop, pharmacy and betting shop; (b) from a
  first-floor window, the bus with its top deck lit, a man walking a dog; (c) a very high aerial of
  the market town, the high street a ribbon of light, one bus on it.

## Version 2 (17 October 2026): one bot, one chair layout, two new beats

- **The bot is one design everywhere.** Every bot shot is a `flow_edit_image` with
  `clips/simulation/stills/s3/s3-bot-00b-a.jpg` (the bot in Kai's edit) as a reference, and the
  **torn bunting stays** (Kai: *"a little detail that really resonates with me"*). Flow Characters
  can't be used yet: they are unmapped on the rebuilt Flow. Swapped onto the canonical bot: frame 9
  (SB09a from K8), 11 (SB11a–c), 16 (SBCANTa/b from M2) and 19 (SBEMERa/b from M1). The originals
  are kept as `*-v1.jpg`.
- **The time machine's chairs are locked to L3** (frame 24): dark recliners, each in a pool of
  light, in a square grid inside a thin ring, with cables running to a round hub. Frames 25 (SB23a/b)
  and 27 (SB25a–c) are re-made with L3 as the reference.
- **New beats after "the row carries on":** 14, *the doors open* (SBDOORa/b: the blast doors open
  mid-row and the pair freeze and turn, *"Whoa, hang on a minute"*); 15, *Hello* (SBHELLOa/b: the bot
  rolls in through the smoke). Then the meeting happens inside, in the canteen. **Into daylight**
  moves after the trust beat: it is now the walk out to the building.
- The frames are renumbered to 29. `anim` in the storyboard JSON keys into the animation-options
  file, and the `#N` references in that file were remapped to the new numbers.

## The clip run (17 October 2026)

Kai's picks (db `picks`, read 17 Oct): animation option **a** everywhere except frames 2 and 3 (**c**);
still **SB27a** for frame 29; no notes. Prompts, picks and deviations are in
[`scripts/gpom/second-half-video/shots.py`](../../../../scripts/gpom/second-half-video/shots.py); the runner is
`run.mts` beside it (waves of 5, submit then harvest, first-frame matching). Omni 1.1 Flash, Frames, 16:9, 720p,
8s, x1, camera locked, motion-only prompts, in Flow project `be451638`. Media:
`/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/video/` (each clip with a `-sheet.jpg`).

- **Made: 20 frames, 26 clips**, every one first-frame matched to its plate. Post-only frames (no Flow clip):
  4, 11, 13, 16, 18, 21, 23, 24, 27.
- **Extras:** a second speaker for frame 7 (SB07c), the explosion element on black for 12, cast takes of 9 and
  20, and a re-roll of 15.
- **Bot cast** with the West Country Bot Character by `@` mention on 9-c, 15, 15-r2, 19, 20-c. The MCP's
  ingredient-picker cast does not work in Frames mode (`docs/flow/automation-2026-09-rebuild.md` items 75–77).
- **Frame 19:** Flow refused SBEMERa at upload, so SBEMERb stands in.
- **Frame 15 is not solved.** All three takes shrink the bot back toward the doors in the first second.
- **Cutting-room board:** https://claude.ai/artifact/LyD3odnVmN5rrdo9m1TpZp. Verdicts go in its db `picks`
  (`verdict` keep|redo, `note`). Rebuild: `python3 scripts/gpom/second-half-video/build-board.py <out-dir>`.

## Post-only frames (17 October 2026)

`scripts/gpom/second-half-video/post.py` renders the nine frames that need no Flow clip as `sh-<key>-post.mp4`
(1280×720, 24 fps, limited range, no audio): 04 the ping hold · 11 the bot held · 13 the tail of 07-2 · 16 a slow
push over 10 s · 18a the crowd + 18b frame 12 replayed as grey CCTV · 21 bunny suits held · 23 the wafer pull-back
250→100% · 24 the chair lights coming on in a spiral · 27 the beacon slowing to dark. Not yet: on-screen text
(HUD, waveform, timestamps) and any beacon pulse that must hit a word; both wait for the audio.

## Premiere

**Project:** `/mnt/d/badcode-videos/gitpush-origin-master/gpom-story.prproj`
**Sequence:** `gpom-second-half`: 1920×1080 @ 24, 134.5 s. Built 17 Oct 2026 over the bridge.
**Bin:** `07-second-half` (36 clips + `slug-1080p24.mp4`).

| Track | What |
| --- | --- |
| V1 | 31 shots in story order, first-pass lengths, from `scripts/gpom/second-half-video/edl.py` (placed with its `eval` bodies, 4 evals, no failures) |
| A1–A3 | empty: audio is planned, not made |

**Applied:** every V1 clip Motion → Scale 150 (1280×720 sources in a 1080p sequence). Checked by eye at 2 s, 63 s, 108 s.
**How the sequence got 24 fps:** Premiere ships no 1080p 24 preset, so it was created `fromItems` a 1-s black
1920×1080 24 fps slug, which the first placement overwrote.

**Sound script:** https://claude.ai/artifact/FH9mz25HGZWCfQzMaDqubx (War of the Worlds shape: the AI narrates, two themes, Gemini for every voice), from
[`second-half-audio-plan.json`](./second-half-audio-plan.json) (the single source for the second half's words, effects and music; every line a draft for Kai). Kai's notes
in its db `notes`. Rebuild: `python3 scripts/gpom/second-half-video/build-audio-plan.py <out-dir>`.

**Needs a human / not done:** frame 12's explosion element (`sh-12-element.mp4`) is in the bin, not keyed onto V2;
no transitions; no audio.

## Rough cut with sound (17 October 2026)

**Sequence `gpom-second-half-rough`** (1080p24, 3:10.9; bin `08-second-half-rough`). Render:
`/mnt/d/badcode-videos/gitpush-origin-master/renders/gpom-second-half-rough-20261017-2153.mp4` (−16.5 LUFS integrated).
V1 picture · A1 narrator · A2 dialogue · A3 music + the crowd. The picture-only `gpom-second-half` is untouched.

How it was built, all re-runnable from `scripts/gpom/second-half-video/`:
1. `voice.py` — every line of `second-half-audio-plan.json` as its own Gemini TTS take (30 takes, all first try),
   rough-cut casting: AI/narrator Algenib · Maddie Aoede · Sandra Kore · Derek Fenrir · old lady Gacrux ·
   crowd Puck/Leda/Orus/Zephyr. Trimmed of silence into `audio/voice/trim/`.
2. `timing.py` — re-times the picture to the voices (dialogue stays in its frame, narration may run on, a voiced
   frame waits for the voice before it) → `audio/rough-cut.json`. 134.5 s → 190.9 s.
3. `extend.py` — clips that need more than their source: ping-pong (frame 16's push: a held last frame) → `video/rt/`.
4. Suno v6, workspace `gpom-story`, every cue a pair at weirdness 30/60, 100 credits (6,915 → 6,815). Takes:

| Cue | Takes (w30 ×2, w60 ×2) | Used in the rough cut (not Kai's pick) |
|---|---|---|
| The Hundred (hymn) | `gpom-sh2-hundred-A-v6-w30/w60` | d221a26b (w30, 0:45) |
| S1 the hunt | `gpom-sh2-s1-A-v6-w30/w60` | 805b38c7 (w30, 0:25) |
| S3 the meeting | `gpom-sh2-s3-A-v6-w30/w60` | fca27332 (w30, 0:50) |
| S4 the crossing | `gpom-sh2-s4-A-v6-w30/w60` | 88a66171 (w30, 0:45) |
| S5 coda | `gpom-sh2-s5-A-v6-w30/w60` | 2b7bee8a (w30, 0:15) |

   Kill mode (S2) is `clips/gpom-main-track.mp3` from its drop at 70.3 s (RMS −15 → −11 dB at 70.5 s).
   Nobody has listened: the takes were chosen by length. Recorded preview copies in `suno-recordings/`.
5. `rough_audio.py` — levels (voices −16 LUFS, music −15 to −32 by role), the AI's small-speaker filter, the row's
   tiled echo, the radio filter, the duck under Maddie's call, fades → `audio/rough/`.
6. `rough_place.py` — the placement evals (64 placements; three hit the known `resolveProjectItem` null and
   went in on retry), then Motion → Scale 150 on V1.

**Not in it yet:** sound effects (none at all: the CCTV replay at 2:10 is five seconds of silence), the HUD and
on-screen text, the keyed explosion element, the casting tests, Covers of the GPOM riff (the themes are
independent generations for now).
