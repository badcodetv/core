# GitPush Origin Master

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
Humanity pushed its worst code straight to `master`: the AI from the bad branch watched the economy, then
the country, fall to the machines it ran, regrets it, and goes back to rebranch. Two films share one
opening: a **music video** (the drum & bass title track, 3:58, the downfall) and a **story film** (~9 min:
the downfall, then the last humans in a bunker, a delivery bot, and a time machine powered by them).

## Parts
- Music video: opening + push + drop, Chorus 1 "Skid Row Britain", the banks fall, Chorus "Outbreak Night", War in Swindon, MV ending (music video only) — `scenes/` — opening to war in Premiere and signed off/cut by Kai; MV ending in Premiere (`02 GPOM music end r1`).
- Story film: the music video's picture up to the end of the war, then A Kill bots (with Maddie's hologram), B Maddie at the door, C The walk out, D The clean room and the crossing, E The ending — `scenes/second-half-*` — all in Premiere (`00 RENDER story`); C, D, E signed off; A shortened 12 Nov.
- The off switch (fake Swindon → glitch → wreck) is out of the story film (4 Nov).
- **Each part has its own look. Don't carry one part's look into another.**

## Look
Status: LOCKED for every part made. A new part with no look is EXPLORING (variation round, Kai or Jack picks).
- **Holds across all parts:** one named light source in every frame; one bright anchor in any dark frame; a visible cost in any monumental frame; never an empty foreground; British places and pounds; no legible generated text; animation **dramatic** (a dive, a storm, a hard push), never twinkle-and-haze.
- **Opening/push/banks:** Earth from orbit → Hong Kong → café CRT (`git push origin master` is the one text Flow may render; type animated in post); 35mm documentary rooms; banks = the same rooms **empty**, one bright screen per room.
- **Chorus 1, Skid Row Britain:** winter, cold grey (dusk, overcast or night), 35mm feature-film stock; country-scale poverty (tent motorways, mile-long queues) seen wide; fire is the one warm colour.
- **Chorus, Outbreak Night:** night, 35mm photographic; sodium motorway lamps, cold white LED headlights, fire as the warm anchor, a red aviation light per crane. Explosions and three global one-beat shots allowed here only; people small, from behind, fleeing; no gore, no children.
- **War in Swindon:** Swindon today, overcast grey daylight, muted natural colour; **no humans, never a hit on screen**, only the wreckage after; one drone-feed beat (grainy/thermal).
- **MV ending:** night throughout; the red-robed army fills Britain, then fleets, then night-side Earth from orbit with the opening's satellite; no humans; the ring eye is a structure, never a face.
- **A · Kill bots:** grainy CCTV with a red HUD (HUD is an ffmpeg text layer); red vision = kill mode only. Maddie's hologram is a three.js scene through a CRT telly (blue beads, green ember, grey hairline string), not Flow.
- **B · The door:** 1980s BBC 16mm, the bunker naturalistic and lived in; the old lady's close-up is the one anamorphic exception.
- **C · Walk out:** overcast chalk downs, muted greens and greys, fine grain; the building's amber seam is the only warm colour.
- **D · Clean room:** clean, bright, futuristic, cool white, faint grain; light from the ceiling grid; Maddie gleaming, **no bunting**.
- **E · Ending:** night, rain, photographic; wet tarmac, sodium and shop light, the bus's lit top deck; ends on Parliament at night in the rain, camera locked, slow push.
- Second-half stills end with: `16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.`
- Cast: Maddie = Flow Character `West Country Bot` (dented grey box, six black wheels, amber beacon; torn bunting on her wheel in every shot **before** D, none from D on); Kill bots = Flow Character `Kill Bot`; Sandra, Derek, the old lady by fixed stills (see look.md Cast); the building, the chairs and the ring eye are fixed designs (look.md Cast).

## Sound
- **Music video:** the drum & bass track "Git Push Origin Master" — dark atmospheric halfstep D&B at 174, dark orchestra throughout, calm RP newsreader on the bulletins, a football-terrace crowd roaring the hook. LOCKED (made on a retired Suno model; full boxes in sound.md).
- **The AI (narrator):** Suno v6, Voice `badcode newsreader` (never type `BC-NEWSREADER`, never just `badcode`; on "Overwrite Styles?" always Keep Current). Calm, dry, close, always on top. Settings: Style Influence 50 · Audio Influence 65 · Weirdness 25 (dry single lines: pair 25/10) · Variety, Max Mode, Personalize off · Duration ~15 s below the target · workspace `gpom-story`. LOCKED.
- **Second-half score:** separate cues, intimate chamber music — solo cello, solo violin, piano, "Chopin, not Beethoven's Fifth"; never action-movie, no drum hit. v6, instrumental, Style Influence 75, weirdness pair 30/60. LOCKED.
- **Humans and Maddie:** AI Studio (Gemini TTS), regional British, never American: Maddie `Aoede` (Bristol), Sandra `Autonoe` (Bolton), Derek `Algieba` (Liverpool), the old lady `Vindemiatrix` (Sheffield, plain-spoken, not posh); the crowd `Orus`, `Leda`, `Schedar`, `Vindemiatrix`, `Zubenelgenubi`, `Gacrux`. Profiles in sound.md and `scenes/second-half-cut3-cast.json`. LOCKED.

## Story-only rules
- The AI is never given a body, face, orb or avatar; it speaks through Maddie's speaker and her beacon pulses on his words.
- Maddie is never voiced in Suno (she comes back American).
- The newsreader never swears and never panics; the drama is the gap between the still voice and the music.
- Music never rises over a word; nothing is slowed in the edit.
- No real brands; flashes at 3 a second or fewer (run the photosensitivity check).
- No stop-motion. Accepted plates are honed from the pick, never re-derived; Kai approves plates before video.
- Words change only with Kai; record only when Kai says "record".

## Library pieces in use
- none yet

## Where the detail is
- [look.md](./look.md) (full record, per-part table, cast) · [sound.md](./sound.md) (every box verbatim, takes, profiles)
- [timelines.json](./timelines.json) and the overview board https://claude.ai/artifact/AXJqmgAWTRhxK7fzMkKukp
- Part briefs: [chorus-poverty](./scenes/chorus-poverty/brief.md), [chorus-outbreak](./scenes/chorus-outbreak/brief.md), [war](./scenes/war/brief.md), [mv-ending](./scenes/mv-ending/brief.md), [C](./scenes/second-half-c-walk-out/brief.md), [D](./scenes/second-half-d-crossing/brief.md), [E](./scenes/second-half-e-ending/brief.md), [second-half storyboard plan](./scenes/second-half-storyboard-plan.md)
- Narration sheet: [songs/narration.md](./songs/narration.md) · story spine: [README.md](./README.md)

Unclear: whether the robot choir and ring eye at the opening's drop survive now that Outbreak Night replaced the robots in chorus 2 (the MV ending still uses the red-robed army).
