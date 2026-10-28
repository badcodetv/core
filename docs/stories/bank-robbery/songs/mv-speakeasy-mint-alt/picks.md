# The Speakeasy Mint: ALT style (second cut)

Jack, 2026-10-28: *"try a different style on the same Premiere file in a different sequence… still that gangster
prohibition era… a realistic style that merges with a noir / James Bond opening sequence, colourful, full of lights,
vibrancy, an interesting dream-like art style, spray-paint sprayed… mostly realistic, but the lights and colours are
exaggerated and cinematic… show me lots of different versions."*

- **Plan:** same 33 scenes and script as `../mv-speakeasy-mint/script.md`; new stills → new Omni clips → a new sequence
  (e.g. `Speakeasy Mint ALT 1`) in the same `bank robbery.prproj`. The K3a rough cut is untouched.
- **Round 1 (2026-10-28):** 8 styles × 2 test frames (scene 5 slot door, scene 13 press), NB2 ×2 each, 16:9, Flow project
  `706836d3` ("Oct 28 - 09:38"). 32/32 landed, none blocked. Prompts: `moodboard.json` (generator `make_rows.py`).
  Voting page: https://claude.ai/artifact/J3kgSozdL3NZfgdazG2R8z
- **My read (Jack decides):** strongest S1 noir neon (press-b), S2 spy titles (gold/magenta smoke, slot-b), S6 double
  exposure (the city inside the gangster's coat, red moon held; flames inside the mayor). Also good: S4 Technicolor,
  S3 spray (slot-a has the most spray-paint feel). Weaker: S7 painted light (paint blobs look stuck on; cream strips on
  slot-a), S8 airbrush (glossy, invented "FIRE" text), S5 stage haze (reads as a nightclub).

## Round 2 (2026-10-28): psychedelic overlays + transitions

Jack: *"like the city in the man's jacket, but psychedelic, constantly transitions settings in clever ways (zoom into the
basement fire, zoom out of a fire at a protest)… keep the realistic style with psychedelic styles overlaid… a bunch of
different types that massively vary… in the same vein as Tarquin's ayahuasca trip but its own style… avoid AI slop."*

- **Kept apart from Tarquin's trip** (`docs/stories/camping/prompts.md` 9-plea r2: acid green, violet/magenta mist,
  geometric lattice, serpents). None of those here; most layers are 1920s or money objects (banknote engraving,
  newsprint dots, a brass kaleidoscope, cut crystal).
- **Anti-slop rules used:** never write psychedelic / surreal / trippy / neon / glowing / cinematic (`omni-flash.md`);
  name the physical thing that makes the effect (a heat camera, oil on a projector, a kaleidoscope, a whiskey glass);
  one named light; real skin + ordinary specific features; similes avoided where they'd draw the object.
  Web pass agreed: "trippy" alone gives the model nothing; name 3–4 concrete descriptors; keep part of a face crisp
  in a double exposure.
- **Results, 12 × 2 + transition pair, all landed** (P8 stalled at 99% once, retry fine). Flow project `706836d3`.

| # | Layer | Scene | Verdict |
| --- | --- | --- | --- |
| P1 | Banknote engraving | 5 | 🟡 Too subtle: green tint + a banknote border on b; the lines barely reach the surfaces |
| P2 | Brass kaleidoscope | 12 | ⭐ Striking gold-and-black star of mirrored Mint; a best |
| P3 | Liquid light show | 17 | ⭐ Oil blobs over the band, mayor + both leaders read clearly |
| P4 | Heat camera | 24 | ⭐ The most distinctive; carries the furnace/attic heat argument by itself |
| P5 | Infinite picture | 13 | ✅ Furnace door holds the room holds the door (b best); subtle but clever, a natural zoom transition |
| P6 | Silhouette windows | 15 | 🔴 Failed: no silhouettes, the Mint just pasted into the crowd; cream border on a |
| P7 | Colour trails | 15 | ⭐ RGB afterimages on the brawlers, the gangster with the sack pin-sharp: the gag is the style |
| P8 | Melting world | 21 | ✅ Money and walls run like honey and wax; strong but closest to a familiar melting-clock look |
| P9 | Spray-tagged photo | 30 | 🟡 Reads as stickers on top; cream border on a |
| P10 | Op-art rings | 6 | ✅ Rings ripple from grandma's eye, real face holds; quiet and hypnotic |
| P11 | Newsprint dots | 18 | ✅ b is the pop one; cream borders |
| P12 | Cut-crystal prism | 8 | 🔴 The glass sits there; no refraction |
| TX | Fire → fire | 24→15 | ✅ Same tall centre flame in both: TX-a-b (square furnace door) pairs with TX-b-b |

- 🔴 **Cream baked-in borders** on P1-b, P6-a, P9-a, P11-a/b: the known NB2 print-style tell; crop or reroll.
- **The transition method (proposed, untested):** (1) hybrid: Premiere push into the furnace flame on clip A, cut on the
  flame, clip B starts scaled up on the drum flame and eases out; free and certain. (2) Omni first + last frame
  (TX-a as first, TX-b as last, "the camera pushes into the flames; as they fill the frame they become the drum fire
  at a street protest"): Google's docs say Omni interpolates between two frames for zoom transitions [vendor].
  Our rule is never to pin an endImage because it morphs, but here the morph IS the shot. Needs one test (credits).
- **The film's shape (proposal):** one overlay per verse/chorus, every scene change a match cut on a shared shape
  (flame → flame, coin → moon, slot eyes → banknote portrait eyes, candle → furnace, press roller → ...).

## Round 3 (2026-10-28): the whole ALT film

Jack: *"I like all of them, so let's use each psychedelic style that fits each scene… more pretty colourful lights and
reflections, keeping the realistic style, interesting David Lynch camera angles… a similar story but with more gangster
and bank robbery imagery: tommy guns, bank vaults, car chases with police… speakeasies, pool, the bands, poker…"*

- **Scene map:** `script-alt.md` (lyric · layer · transition out); prompts generated by `make_rows_r3.py` → `moodboard.json`.
  Same 33 lyric lines and story beats as the K3a cut; new gangster imagery: car chase (1), poker room (8), pool hall +
  band (9), bank lobby seen from inside the vault (10), blowtorch on the vault with tommy guns (11), getaway car behind
  the mayor's flash (14), tommy-gun raid (22), counting room with a card game (25), abandoned getaway car (33).
- **Layers by job:** heat camera on the warm/cold argument (6, 24, 28); colour trails on the action (1, 14, 15);
  newsprint dots on the propaganda (7, 18); kaleidoscope on the Mint and the counting room (12, 25); melting on the
  vault and the money mountain (11, 21); double exposure on who's hiding what (10, 23, 31); the last scene has no layer
  (the trip ends).
- **Lynch angles (traits, never the name):** from inside a drain, an oven, a vault door; straight down a stairwell;
  at the height of the felt; tilted frames; a wide lens close to faces.
- **Guns:** never pointed at a person (Flow refuses): up at the sky, at the ceiling, across the chest, on the floor.
  All passed. The US cops wear peaked caps and long blue coats (the first draft said "tall helmets", which means British).
- **Results:** 33/33 landed, 66 stills, Flow project `706836d3`.
  - ⭐ Strongest: 5a noir slot, 6b heat grandma, 12 kaleidoscope, 13 spy-title press, 15a trails riot, 16 mirror men,
    22 raid from inside the oven, 24 heat furnace, 28 heat split, 4a stairwell.
  - 🟡 The banknote engraving (2, 20) still comes out as a banknote frame round the edge, not lines on the surfaces.
  - 🟡 8a: the prism cloned faces (two bakers, repeated gangsters); 8b reads better.
  - 🟡 29a drew two buildings side by side; 29b is the clean doll's house.
  - 🔴 Cream baked-in borders on about a dozen (2, 4b, 7, 14b, 15b, 16, 18, 20, 27b, 29a, 32, 33b): crop in Premiere
    (scale ~106%) or reroll.

## Cast as Flow Characters (2026-10-28)

Jack: *"make the characters in Flow, so that they look consistent"*. Ten Characters, portrait + body each, in project
`706836d3`; table and ids in `cast.md`. All cast picks are mine (Jack hasn't seen them).
- Automation notes (for `docs/flow/automation-2026-09-rebuild.md`): the MCP create's name saved but read back late
  (CHARACTER_NOT_FOUND, then present minutes later); `br-make-chars.mjs` made 8/9 cleanly; one portrait upload
  (the baker's) hung at 99% three times and never saved, so the baker was rebuilt as "SM The Baker".

## Round 4 (2026-10-28): the cast scenes with Flow Characters, and my picks

Jack: *"keep the characters, please make the stills for the story, pick your favourite… cinematic and with no
artefacts or mistakes… where is the new scene skill, I want to experiment in that."*

- **Method:** `flow_edit_image` with the scene's main Character (`character`) **plus** each cast member's portrait as a
  reference (`referenceImages`, up to 3), prompt says "the man from the character reference, dressed exactly as in his
  portrait reference" and describes nobody. Fixed the dropped gold chain (0/2 → 2/2 on scene 13). Prompts ≤ ~150 words
  (`make_rows_r4.py` → `r4-jobs.json`).
- **Lead changed to "A frame from a feature film… filling the frame edge to edge"** (was "a realistic 1920s
  photograph"): **0 cream borders in 44 cast stills**, against ~12 of 66 with "photograph". The one dotted frame that
  kept a vignette (7a, 18a) is the newsprint layer itself.
- 22 scenes re-stilled (2, 5–8, 11–15, 17, 18, 20–24, 26–29, 32); uncast scenes keep their round-3 still.
- **QC by eye at half resolution:** scene 15's banners printed garbled words ("PROTESTST!") → re-rolled with "plain blank
  cloth banners" → B15r-a clean. No gun points at a person in any pick. Banknote engraving finally landed in 2 (B02-a).
- **My picks (first still per frame on the storyboard), runner-up second:** 1 A01-a · 2 B02-a · 3 A03-b · 4 A04-a ·
  5 B05-a · 6 B06-a · 7 B07-b · 8 B08-a · 9 A09-b · 10 A10-a · 11 B11-b · 12 B12-a · 13 B13-b · 14 B14-b · 15 B15r-a ·
  16 A16-b · 17 B17-b · 18 B18-b · 19 A19-b · 20 B20-a · 21 B21-a · 22 B22-a · 23 B23-b · 24 B24-a · 25 A25-b · 26 B26-a ·
  27 B27-b · 28 B28-b · 29 B29-b · 30 A30-b · 31 A31-b · 32 B32-b · 33 A33-a.
- 🟡 Known: 16 (A16) still has its cream border from round 3 (crop ~106% in Premiere); 20's engraving layer is faint.
- **Storyboard page** (new-scene stage 2→3, with an animation idea and the transition out per frame):
  `storyboard.json`, `animation-options.json`, built by `make_storyboard.py` + `scripts/scene/build-storyboard.py`.

## Video round 1 (2026-10-28): all 33 animated

Jack: *"animate"*. Omni 1.1 Flash, Frames, 16:9, 720p, 8s, via `scripts/scene/run.mts` (8 waves, ~1h30). Prompts:
`make_video_r1.py` → `animation-options.json` (camera locked, one main + one ambient motion, shutter named, ~60–78
words, sound effects, fire steady, no "flash"/"burst"). Clips: `Desktop\Youtube Vids\animation\songs\bank robbery\alt\video\sma-NN-<still>.mp4`.

- 32/33 first time. **25** gave no candidate 3× (silent block) → `25-r2` with only the kaleidoscope turning (no counting
  hands / rubber bands / card game) → landed first time.
- **QC:** every clip at 1 fps on contact sheets (`vqc/`), first 5 checked before the rest spent credits; rough flash check
  (whole-frame brightness swings) on all 33: none.
- **Re-rolls (mine):** `06-r2` ✅ (r1's breath billowed into smoke over her hands), `17-r2` ✅ (r1's oil blobs became solid
  balls and paddles), `01-r2` ❌ (police car turned modern and white with POLICE printed on it) → **keep 01 r1** (its
  colour trails read as solid neon ribbons; a re-roll candidate with a different still if Jack minds).
- **Clips in film order:** 01 · 02 · 03 · 04 · 05 · 06-r2 · 07 · 08 · 09 · 10 · 11 · 12 · 13 · 14 · 15 · 16 · 17-r2 · 18 · 19 · 20 ·
  21 · 22 · 23 · 24 · 25-r2 · 26 · 27 · 28 · 29 · 30 · 31 · 32 · 33.
- ⬜ Premiere: the panel was not connected (status 2026-10-28 15:10). Next: new sequence `Speakeasy Mint ALT rough 1` in
  `bank robbery.prproj`, bin `speakeasy-mint-alt clips`, existing sequences untouched.

## Premiere (2026-10-28)

**Project:** `songs\bank robbery\bank robbery.prproj` (Jack's Desktop). **Sequence:** `Speakeasy Mint ALT rough 1` —
1280×720 @ 24, 264s (4:24), built with `premiere_create_sequence(fromItems)` from the 33 picks in film order.

| Track | What |
| --- | --- |
| V1 | `sma-01-A01-a` 0 → … one 8s clip per scene … → `sma-33-A33-a` 256–264 (06, 17, 25 are the r2 takes) |
| A1 | each clip's own Omni sound effects, under its picture |

- **Bin:** `speakeasy-mint-alt clips`, all 36 takes (incl. 01-r2, 06 r1, 17 r1).
- **Untouched:** `Speakeasy Mint rough 1` (the K3a cut) and every other sequence.
- **Looked at:** frame at 100s (scene 13) exported and read: full frame, right shot.
- **Not done yet:** no song (take still unpicked), no trims, no Premiere camera moves, no match-cut transitions, scene 16
  still needs its ~106% scale to hide the cream border.
- **Undo:** delete the sequence; the bin can stay.

## Timeline page, round 1 (2026-10-28)

Jack: *"can we do this for the whole thing on there, only in the new scene skill for now"*. The whole ALT film as one
new-scene timeline page: https://claude.ai/artifact/4GmevWxQcqgrxfgQ6LgHuH. 33 beats (one per scene, act = song
section, Kai's lyric as the line), V1 = same picks as the Premiere sequence, A1 = the clips' own Omni sound. No song.
Built by `make_timeline.py` → `<media>\alt\cut\edl.json` + `preview.mp4` (each clip normalised to 8 s first: a raw
concat broke the timestamps into a 27-minute file) → `scripts/scene/build-timeline.py`. Premiere not touched.
- delivery-qc on the preview: FAIL colour range (full-range content tagged limited); loudness -21 LUFS, peak -0.1. Not
  fixed: the preview is for noting only, and the final export comes from Premiere.

- **Round 1 notes (Jack):** scene 1 "looks like AI slop: cars teleport, trails too basic, setting AI". Answered on the page (`cut-notes.json`): options A (inside the getaway car, light trails under an elevated railway; my pick), B (one sedan sliding under the El, time-smear), C (three 2 s shots). Owed: Jack picks, and whether the note is film-wide.

## 2026-10-28: clean room for scene 1 (sealed writers) + Kai's no-house-style change

- Jack: "most of the film looks like ai slop … can we do this with the first scene" (the clean-room fix that worked for Suno).
- `cleanroom/`: jack.md (his words, verbatim) + facts.md → ideas.md (3 ideas: running-board flank mount, road-level puddle, pursuer's windscreen) → w1–w3.md (one sealed writer per idea, STILL + VIDEO prompt each). Written with a copy of the sealed writer, now deleted because Kai retired it the same day.
- Kai, 2026-10-28: no house style. The ALT look's rules now sit in `docs/stories/bank-robbery/look.md` → Per part (EXPLORING). Later exploring rounds use the `variations` skill (in-repo, Flow supported).
- Next: run w1–w3 in Flow verbatim (stills, then Omni), then add them to the timeline page next to A/B/C.
