# GitPush Origin Master — sound

> The sound for this story only. Read before any Suno or voice prompt (suno-prompt,
> suno-automation, variations, scene-timeline voicing). Rules: [`docs/stories/STYLE.md`](../STYLE.md).

**Status:** LOCKED for everything already made and picked (the D&B track, the narration scenes, the
second half's voices, lines and cues). Kai, 2026-10-28: *"most of GitPush is already recorded"*, so
this file is mostly a record. Anything new for GPOM starts from the part it belongs to below; a
sound for a part that has none yet is EXPLORING (a variation round, never a default).

*(Written 2026-10-28 when BadCode stopped having a house sound. Most of what used to be written as
BadCode-wide (drum & bass, the newsreader, the narration house settings, the short-prompt rules)
was learned on this story and lives here now. The live sheets are still the source of truth for
words and boxes; this file says what the sound is and where each piece lives.)*

## In one paragraph

Two halves. **The first half is the drum & bass track "Git Push Origin Master"**: a dark,
atmospheric halfstep D&B piece at 174 with a real dark orchestra running through it, a calm RP
newsreader reading the bulletins and a football-terrace crowd roaring the hook in every drop. Since
2026-10-15 the track *is* the downfall: it opens the film as its music video. **Around and after
it, the AI narrates** in one Suno Voice, `badcode newsreader` (cloned from the orchestral cut): calm,
dry, close, always on top of the mix. Under the narration the first-half scenes had a sparse score
in the same take (cello and violin, then oboe and soft horns, then clarinet); the second half
voices the AI dry, line by line, and scores it separately with **intimate chamber music: solo
cello, solo violin, piano, "Chopin, not Beethoven's Fifth", never action-movie, no drum hit**.
Every human and the delivery bot are **Gemini TTS voices with regional British accents, never
American**: Maddie the bot is West Country (Bristol), Sandra is Lancashire, Derek is Liverpool, the
old lady is old-fashioned RP.

## Tracks

### 1 · "Git Push Origin Master" (drum & bass) — the music video, the downfall · LOCKED

- **Sheet:** [`songs/git-push-origin-master-dnb.md`](./songs/git-push-origin-master-dnb.md)
  (a v5.5 sheet, archived 2026-09-10 when v5.5 was retired; the takes still exist and can be Covered
  onto v6, the sheet cannot be re-run as written).
- **The take in the film:** the round-eight keeper (2026-08-08, Kai: *"this is really working
  now… I have a version right now that really sounds good to my ears"*). **Its Suno take id is not
  recorded in the repo.** File: `D:\badcode-videos\gitpush-origin-master\clips\gpom-main-track.mp3`
  (3:58; on A1 of `gpom-s01` in `gpom-story.prproj`; the drop is at 70.3 s, per
  `scripts/gpom/second-half-video/rough_audio.py`). Kai cuts a shorter version in Premiere
  ([`restructure-2026-10-15.md`](./restructure-2026-10-15.md)).
- **Genre:** dark atmospheric drum & bass, 174 BPM, halfstep and two-step, with a dark operatic
  orchestra through the whole track. Reference vibe was Camping's 174, *"pulled away from Camping's
  jump-up neurofunk aggression and toward atmospheric halfstep"* (sheet, "The design").
- **Singers:** two voices. A dark gravelly British male **newsreader** (calm, formal, RP,
  close-mic'd) owns the bulletins and never swears; a **football terrace crowd** ("hundreds of hoarse
  untrained men", chanted not sung) owns every drop, in parentheses. The keeper also has a texture
  nobody prompted: a heavy choir across the first half of the drop and a *robot newsreader* across
  the second (the sheet: leave it as a dice-roll, don't ask for it by name).
- **Settings:** model **v5.5**, style influence **72**, weirdness **50**, BPM **174**, no Voice
  attached (the newsreader held the lead prompt-only). My Taste was set per the sheet (My Taste is
  retired since 2026-09-10).

Style (verbatim, the box that produced the keeper):

```
Two voices. The bulletins are one dark gravelly British male newsreader, calm and formal, close-mic'd received pronunciation over the beat, never raising his voice. Every drop is taken over completely by a football terrace crowd - hundreds of hoarse untrained men roaring the hook in unison, low and massed and huge, hammered out hard on the beat, chanted not sung, close and dry. Dark atmospheric drum and bass, 174 BPM, halfstep and two-step, deep rolling sub and restrained breaks with space in them, opening into full-weight drops. A real dark orchestra runs through the whole track, operatic and cinematic - a chilling solo cello and hushed creeping strings over a low drone under the bulletins, then full weight alongside the crowd through every drop, timpani and low brass. An eerie synth wail recurs like a warning. Dystopian, moody, minor key. Played completely straight, no comedy, no novelty.
```

Exclude styles (verbatim):

```
rap, MC, toasting, hype vocals, ad-libs, jump up, liquid dnb, happy hardcore, uplifting, joyful, celebratory, major key, children's choir, soprano, choral harmony, vibrato, angelic voices, sustained vocal notes, pop hooks, comedic, novelty, parody, American accent, autotune, clean pop vocals, cheering, applause, pub singalong, drinking song, stadium rock
```

Lyrics: the sheet's "Current cut" block (three bulletins, the hook as two long lines in
parentheses, run twice per drop, `[Drop] [Chant]` → `[Chant | bigger]` → `[Chant | biggest, the
whole orchestra with the crowd]`, a power-off ending).

**What this track's D&B was, in the words that used to be written as BadCode's.** These two lines
were written as BadCode-wide. Kai, 2026-10-28: **drum & bass is one track's choice, not BadCode's
identity.** They are recorded here as this track's, verbatim:

> Drum & bass is the home genre: ~170–180 BPM, dark, UK grime influence, Amen breaks, heavy sub and
> Reese bass (touchpoints: Chase & Status, Stormzy "Backbone"). Songs often carry **multiple voices /
> perspectives** in tension (e.g. the dismissed worker vs. the comfortable professional). Raw,
> confrontational delivery; social commentary in the bars.
>
> — `docs/voice.md` §Music (until 2026-10-28)

> **Music** — drum & bass, dark and UK-flavoured (grime influence, Amen breaks, heavy sub).
>
> — `docs/vision.md` line 14 (until 2026-10-28)

⚠ **The track as made is not quite that.** Its Style box asks for no grime, no Amen and no Reese by
name; it bans `rap, MC, toasting, hype vocals` and `jump up`, and it leans halfstep and orchestral.
What it does keep from those lines: dark, 174, heavy sub, two voices in tension, raw delivery
(the terrace), social commentary in the words.

**D&B craft notes for this track** (from the sheet, plus the D&B notes that lived in the
`suno-prompt` skill until 2026-10-28):

- **Density is tempo.** Don't prompt "double time" (a Suno blind spot): the verses are the
  half-time, the choruses get double density by writing the hook as two long lines at roughly double
  the normal syllables. Short lines are not fast.
- **Commas score stress units.** `git, push, origin master` (three units) lands like a terrace chant;
  `git, push, origin, master` (four) drawls. Tested, round eight.
- **Parentheses cast the backing slot.** The crowd sits in `( )` so the newsreader's prior doesn't
  take the hook. The lead/backing seam runs per line, not per section.
- **The genre picks the vocalist pool.** "Drum and bass + male lead" wants to hand you an MC, so the
  newsreader clause front-loads the Style box (opening with `Two voices.`) and `rap, MC, toasting,
  hype vocals, ad-libs` are the most load-bearing excludes.
- **A drop header says only what differs between sections** (escalation); voice, texture and
  sound belong to the Style box.
- **The orchestra runs through the whole track**, not "under the bulletins", or the drops come
  back thin. `close and dry`, not "stadium", for the crowd; `roaring`, not "shouting".
- **Weirdness follows how much the brackets carry:** 30 while the architecture lived in bracket
  cues, 50 once it moved into the Style box.
- From the `suno-prompt` skill (verbatim, its "Drum & bass specifics" list):

> 1. **Half-time drums are a known blind spot.** Repeated controlled tests never produced half-time
>    from a `breakdown` tag — it slows and thins the arrangement instead. Since the half-time drop is a
>    defining D&B device, **assume you cannot prompt it.** Get it by editing in Studio or splicing
>    sections, and tell the user that rather than selling them a prompt that won't work. **Live lead,
>    untested:** Studio 2.0's MIDI tracks let you program the pattern by hand instead of asking the
>    model for a concept it doesn't hold (`suno-studio.md` §2). Offer it as an experiment worth an
>    hour, not as a solution — and write the result back into the doc either way.
> 2. **Niche subgenres fail; broad ones work.** Riddim came back as generic dubstep with none of the
>    characteristic sound design — expect the same at neurofunk / liquid / jump-up level. **Mitigation:
>    describe the sound design and rhythm rather than relying on the subgenre name.** **v6 data
>    point (2026-09-09, ChillPanic):** a lazy `liquid DnB` prompt came back as two-step drums, while
>    an engineered one naming the drum mechanics (`jungle breaks, rapid chop, hyperdetail
>    percussion, dark synth bassline`) worked on both models. Same lesson, now on v6. v6 Wild is
>    deliberately "less tuned towards preferences" — the model to hunt niche D&B in, then Cover
>    into v6 (`suno-v6.md` §9). `producer-
>    vocabulary.md` is exactly that toolkit — reese bass, sample-and-hold on the cutoff, amen break,
>    sub layering, sparse drop.
> 3. **Suno's harshness sits exactly where D&B lives** — brittle cymbals, sizzling hats, sibilance in
>    2–6 kHz. Budget for de-essing, or plan to replace the drum stem.
> 4. **Sidechain pumping can't be undone** — it's baked in, not a real sidechain.
> 5. **Sounds mode is the D&B post-production kit** — risers, downlifters, sweeps, impacts, fills, at
>    your project's BPM and key. Suno won't build transitions into a generation, so this is how you get
>    them.

The skill also said, under "The narrator problem": *"Build the narrator's Voice in a register that
has nothing to do with D&B — spoken oratory, opera, a gospel preacher, a sardonic crooner. The genre
mismatch is what breaks Suno out of its generic per-genre vocal default."* That is how
`badcode newsreader` came about (cloned from the orchestral cut, below).

### 2 · "Git Push Origin Master" (orchestral) — the canonical master, the Voice's source · LOCKED (not in the film)

- **Sheet:** [`songs/git-push-origin-master-orchestral.md`](./songs/git-push-origin-master-orchestral.md)
  (v5.5, archived 2026-09-10). Its own header calls it *"the canonical master… deliberately
  frozen"*; the D&B cut is the one the film uses.
- **Genre:** dark neoclassical chamber piece, the *War of the Worlds* model: spoken narration carries
  the plot, the orchestra does the screaming. No beat.
- **Singer:** one dark gravelly British newsreader, spoken verses, then a booming theatrical bass
  chant in the choruses, multiplying into a harmony of himself.
- **Settings:** model **v5.5**, style influence **75**, weirdness **60**. **Take id not recorded in
  the repo.** The take is the source the `badcode newsreader` Voice was cloned from
  (`songs/archive/narration-v5.5.md` line 562).

Style (locked 2026-08-06, verbatim):

```
Dark neoclassical chamber piece, eerie and foreboding, carried by one dark gravelly British male voice — a calm formal newsreader reading bulletins over a near-silent bed, erupting into a deep booming theatrical bass chant in the choruses, quiet and menacing at first, louder and angrier at every return, multiplying into a deep male harmony of itself as the choruses grow. Opens as one chilling solo cello, close and sparse, and darkens section by section — hushed creeping strings over a low drone, lone piano notes, distant timpani; single instruments answer between his lines. An eerie synth wail recurs like a warning. Hushed, chilling, foreboding. Played completely straight, no comedy, no novelty.
```

Exclude styles (verbatim):

```
drum and bass, EDM, dubstep, trap, hip hop, pop hooks, upbeat, happy mood, comedic, novelty, parody, kazoo, American accent, autotune, vocoder, robot voice, clean pop vocals, lo-fi, chillhop, country, reggae, folk, disco, big band, epic trailer music, choir, female vocals
```

### 3 · Scene 4, the simulation: music under Maddie (`gpom-sim-bed2`) · LOCKED

Instrumental, ~90 s, Kai picked **`a6cf12f5`** (*"really good for the robot. I love it."*). House
narration settings, no Voice. Sheet: [`songs/narration.md`](./songs/narration.md).

```
A light, warm instrumental underscore for a small delivery robot exploring an empty town, made to sit underneath a woman talking. Celesta, harp, pizzicato and a soft clarinet over a gentle ticking pulse, curious and hopeful, turning quietly wondrous and a little mysterious in the middle, then warm again, small changes every few bars. Sparse enough to talk over, never loud, no big build.
```

```
vocals, singing, voice, spoken word, choir, humming, whistling, heavy drums, drum kit, bass drop, loud, epic, cinematic build, synth lead, electronic, dance, dark, horror
```

### 4 · Second half, scene A (kill bots): cues P and C · LOCKED

Sheet: [`songs/second-half-scene-a-music.md`](./songs/second-half-scene-a-music.md). Kai's brief
(2026-10-21): *"more sparse orchestra, solo violin, cello… not Beethoven's 5th, more Chopin."*
Intimate, not action-movie; tension by silence, not drums. Round 2 for C (Kai: C1/C2 *"too
happy"*): dark and driving, still no drum kit, no action brass.

Settings (music column): v6 · no Voice · Style Influence **75** · weirdness **pair 30 / 60** ·
Variety, Max Mode, Personalize Off · workspace `gpom-story` · Duration P 45, C 60. Files:
`D:\badcode-videos\gitpush-origin-master\clips\second-half\cut3\A\suno\` (`.wav` + `.preview.mp3`,
recorded, never downloaded).

**Cue P, the patrol, P1** (picked `gpom-sh-a-P1-A-v6-w60`, `57b65bfc`, 0:45):

```
A lonely nocturne for solo cello and felt piano, eerie and very slow, free rubato time. One low cello note is held in an empty room, a few soft piano notes fall into long silences, then a thin, high violin line drifts in from far away, barely there. All the tension comes from silence and space; nothing ever lands on a beat. Recorded close and intimate in a small dry wooden room, you hear the bow hair and the felt hammers. Near the end the cello sinks into a low, uneasy tremolo that never resolves.
```

```
vocals, singing, voice, choir, humming, drums, drum kit, percussion, timpani, beat, pulse, groove, string quartet, string section, full orchestra, pizzicato, brass, horns, woodwinds, harp, synth, electronic, pad, reverb wash, epic, heroic, action, trailer, bombastic, major key, happy
```

**Cue P, the patrol, P2** (picked `gpom-sh-a-P2-A-v6-w30`, `49a6688a`, 0:44; one pick in each
patrol style):

```
Chamber string quartet playing sul ponticello and glassy harmonics, cold, hollow and unsettling. Viola and cello sustain one quiet, unresolved chord that barely moves while a lone first violin searches above it in thin, broken phrases with long held breaths between. The players seem to hold their breath: pianissimo throughout, a hush down to almost nothing, then one sharp dissonant swell at the very end that cuts off. Captured from the back of a large cold stone hall, distant, wide and reverberant.
```

```
vocals, singing, choir, piano, keys, felt piano, drums, percussion, timpani, beat, groove, pulse, brass, horns, woodwinds, synth, electronic, full orchestra, solo cello nocturne, warm, romantic, lush, epic, action, heroic, trailer, major key
```

**Cue C, the chase and the call, C3** (picked `gpom-sh-a-C3-A-v6-w60`, `a1614dbb`, 1:00):

```
Dark, driving chamber music for a small low-string ensemble. Two cellos saw out a relentless minor-key ostinato in hard, bowed sixteenth notes, like a heart running too fast, with a double bass digging in underneath on the downbeats. High violins shiver in a tight tremolo above, and every few bars a harsh dissonant chord tightens the screw. It never lets up: denser, louder and more desperate through the whole minute, building dread. Recorded raw and very close in a small dry room, you hear rosin, bow scrape and breath. Near the end the ostinato breaks off and only one low, uneasy held note remains.
```

```
vocals, singing, choir, pizzicato, plucked strings, playful, light, whimsical, happy, major key, piano, keys, drum kit, drums, snare, percussion, timpani, beat, brass, horns, epic, heroic, trailer, action movie, synth, electronic, reverb wash, distant, ambient, nocturne, romantic, warm
```

### 5 · Second half, the ending (scenes C, D, E): four cues · LOCKED (Claude's picks, Kai may overrule)

Sheet: [`songs/second-half-ending-music.md`](./songs/second-half-ending-music.md). Kai's brief
(2026-10-21): *sparse and intimate, solo cello, solo violin, a little piano. Chopin, not Beethoven's
Fifth, never action-movie. The ending may swell, but stays restrained. No drum hit.* The picks were
made by Claude in the autonomous run of 21 Oct (by Gemini listen + measurement); the ending has
since been signed off on the overview board (`timelines.json`).

Settings for all four: v6 · instrumental, Voice none · Style Influence **75** · weirdness **pair
30 / 60** · Variety, Max Mode, Personalize Off · workspace `gpom-story`. Files:
`D:\badcode-videos\gitpush-origin-master\clips\second-half\ending\<C|D|E>\suno\`.

**C, the walk out** (`gpom-sh-c-walk`, Duration 60; picked `gpom-sh-c-walk-A-v6-w30`, `cc128cb2`, 1:13):

```
A slow, tender piece for solo violin and piano, like a Chopin nocturne heard outdoors. The violin plays alone at first, a hesitant, searching melody with long breaths between phrases, as if stepping out into daylight after a long time underground. Then a soft piano enters underneath with a slow, rocking left hand, and the melody grows a little warmer and more hopeful, never loud. Near the end everything thins away until only one low cello note is left, held and still, unresolved. Recorded close and intimate, natural and unhurried, rubato.
```

```
vocals, singing, choir, humming, drums, percussion, timpani, beat, pulse, groove, brass, horns, brass band, full orchestra, string section, synth, electronic, pad, epic, heroic, action, trailer, bombastic, cinematic swell, march, major key fanfare
```

**D, the clean room** (`gpom-sh-d-room`, Duration 70; picked `gpom-sh-d-room-A-v6-w30`, `09f81875`, 1:10):

```
A slow, delicate piece for solo piano in its high register, a gentle repeating music-box-like pattern, tender and slightly uncanny, like a lullaby played in a spotless empty room. A thin, high violin harmonic hangs above it now and then, barely there. Very quiet, very clean, lots of space and silence between the notes, in the manner of a Chopin nocturne slowed almost to stillness. Recorded close, bright and clear, a small dry room.
```

```
vocals, singing, choir, humming, drums, percussion, beat, pulse, groove, bass, cello, low strings, brass, horns, full orchestra, string section, synth, electronic, pad, ambient drone, epic, heroic, action, trailer, dark, menacing, horror
```

**D, the crossing** (`gpom-sh-d-cross`, Duration 45; picked `gpom-sh-d-cross-A-v6-w30`, `7bead5f0`, 0:45; it stops dead):

```
A slow, heartbreaking nocturne for solo cello and piano, in the manner of Chopin. The piano plays slow, warm broken chords and the cello sings a long, simple, aching melody over them. A solo violin joins above the cello halfway through and the two lines climb together into one restrained swell, full and tender but never loud or grand, then everything stops on a single unresolved chord left hanging in silence. Recorded close and intimate in a warm wooden room, rubato, you hear the bow.
```

```
vocals, singing, choir, humming, drums, percussion, timpani, beat, pulse, brass, horns, brass band, full orchestra, string section, synth, electronic, pad, epic, heroic, action, trailer, bombastic, cinematic swell, crescendo to fortissimo, major key fanfare, march
```

**E, the coda** (`gpom-sh-e-coda`, Duration 40; picked `gpom-sh-e-coda-A-v6-w60`, `18b34a9d`, 0:42):

```
A short, slow, tender ending for solo piano and solo cello, in the manner of the close of a Chopin nocturne. The piano begins alone with a simple, quiet phrase over soft rain-like stillness; the cello enters and the melody rises once into a gentle, restrained swell, warm and hopeful but never grand, then falls back to a single held piano chord with space around it. A last short cello phrase, then the piece ends on one low, soft piano note left to ring and decay into silence.
```

```
vocals, singing, choir, humming, drums, percussion, timpani, drum hit, impact, boom, beat, pulse, brass, horns, cornet, brass band, full orchestra, string section, synth, electronic, pad, epic, heroic, action, trailer, bombastic, cinematic swell, fortissimo, fanfare, march
```

## Narration / voices

### The AI (the narrator): Suno v6, Voice `badcode newsreader` · LOCKED

- **The Voice.** `badcode newsreader` (the live Suno display name, lower case), cloned from the
  orchestral cut's newsreader. `BC-NEWSREADER` is our internal label: **never type it into Suno.**
  Two account voices start with "Badcode": `badcode newsreader` (ours) and `Badcode Narrator` (a
  different thing), so **never pass just `badcode`**. A wrong name does not error; it returns
  `voice:not-found` and generates with no Voice, so read the log line. Attaching the Voice pops
  "Overwrite Styles?": always **Keep Current**. Kai insists on this exact voice for the AI
  (`second-half-scene-a-music.md`, settings).
- **Who he is on screen.** He has no body, ever. In the second half he speaks through Maddie's
  speaker: small-speaker filter, her beacon pulses on his words (`scenes/second-half-*/scene.json`,
  cast `ai`). The film's last line (`I made it. Now the real work starts.`) is the one unfiltered
  read, with a 40% trace of Maddie's speaker on "I made it." only.

**The live sheet is [`songs/narration.md`](./songs/narration.md)** (every round's history is in
[`songs/narration-history.md`](./songs/narration-history.md), newest first; older eras in
`songs/archive/`). One atom per scene, in that file only. Its house settings and template are
GPOM's narration style, copied here verbatim (2026-10-28):

**House settings** (ruled by Kai 2026-09-24: scene 2's picked settings are the house default; a
scene that differs says so in its own section):

| Control | Value |
| --- | --- |
| Model | **v6** |
| Voice | **`badcode newsreader`** (🔴 the live Suno display name, lower case. Never type `BC-NEWSREADER`, our internal label, into Suno) |
| Style Influence | **50** (how hard Suno follows the Style box. Dropping it from 75 was the fix for the muffled voice) |
| Audio Influence | **65** (how hard the Voice pulls the delivery) |
| Weirdness | **25** (both picks were 25. 35 garbled words on the opening, r18) |
| Variety · Max Mode · Personalize | **Off** · **Off** · **Off** |
| Vocal Gender | unset (the Voice supplies it) |
| Duration | 🔑 **Set it ~15s BELOW the length you want.** Suno overshoots: 60 → 1:15 · 70 → 1:29–1:35 · 75 → 1:24–1:28 |
| Workspace | `gpom-story` |

**House style, one template, four blanks** (`{{PALETTE}}`, `{{FAMILY}}`, `{{ARC}}`, `{{ENDING}}`;
the fixed text is the voice and the mix and never changes per scene):

```template
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: {{PALETTE}}. His delivery follows the story: {{ARC}}. Close-mic'd and dry, his voice loud and right at the front of the mix, the {{FAMILY}} always well behind him and never rising over a word. Restrained, sparse, never loud, never busy, always quieter than the words. {{ENDING}} He speaks only the words written.
```

The two endings, verbatim: **drum:** `No drums at all until his very last line, then one single
huge, booming orchestral drum hit that ends the piece.` · **hollow:** `No drums at all. It ends
hollow, the last note fading to nothing.`

The Exclude box, the same in every scene:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Drift check: `python3 scripts/suno/narration-drift.py`.

**The picks, scene by scene** (boxes and words for each are in `songs/narration.md`):

| Part | Atom | Score under him | Pick | State |
| --- | --- | --- | --- | --- |
| Scene 1, the opening (the awakening + the push) | `gpom-narration` (🔒 frozen, predates the template; SI 75, AI 50, w25, Duration 70) | strings: cello, violin, piano; ends on the drum hit | `82c4a1e2` (`kai-rework5-v6-w25`) | picked 2026-09-19; recorded `clips/s00/narration/kai-rework5-v6-w25-82c4a1e2.wav` |
| Scenes 2 + 3, the data centre and the downfall, one take | `gpom-datacentre` (d03) | a haunting solo oboe, very gentle French horns, ends on a solo violin | `9c278a6a` (`gpom-s23-d03-v6-w25`) | picked 2026-09-29; recorded `clips/the-gaze/narration/gpom-s23-d03-v6-w25-9c278a6a.wav` |
| Scene 4, the fake world | `gpom-sim-happy` | one soft solo clarinet | `c1690586` | picked (r73 sincere take 2) |
| Scene 4, the wreck | `gpom-sim-sad` | one lonely low clarinet | `57c6ef18` | picked, on `gpom-s01` A5 |
| Scene 4, "What's going on?" | `gpom-sim-what` | one uneasy clarinet note | none | not picked |
| Second half A, the boss on the phone, lines 1–4 | `gpom-sh-a-boss-1` … `-4` (one line per atom, voice only) | none (no music asked for) | `7f8d1ef8` · `d7aaef3e` · `bfb1220b` · `543dafef` | recorded 2026-10-22/23 |
| Second half C, D, E, the AI's lines | `gpom-sh-end-ai-C` · `-D` · `-d7` · `-e2` (voice only) | none (cues are separate) | `7f567949` · `8afa9d8a` · `4fa3d2b1` · **`22571839`** (the last line, Kai's pick) | recorded |

⚠ Since the 2026-10-15 restructure the D&B track is the downfall and replaced cut 4's narration.
Whether the scene 1 and scenes 2 + 3 narration takes are still in Kai's current cut of
`gpom-1-track-and-off-switch` is not recorded in the repo.

**The dry-voice recipe used for the second half** (boss lines, the ending lines): the same Voice and
house sliders, weirdness **pair 25 / 10**, a very short Style box with one delivery word and **no
music**, one cue in the lyrics, and a long music-ban Exclude. Boss line 1, verbatim:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, mildly amused. No music. Dry, close-mic'd, no reverb.
```

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

The last line of the film (`-e2` revision H, picked `22571839`; read once, **no bracket cues**,
because the cued double read tripped Suno's lyric filter):

```
Spoken word narration, voice only. One calm British male voice, a newsreader, dry and close, speaking quietly as if to one person, late at night. No music at all: no score, no bed, no instruments, only his voice and quiet silence between the words. Tired on the first sentence; the second warmer and quietly determined, never dramatic. Close-mic'd in a dead, dry voiceover booth, no reverb, his voice right at the front. He speaks only the words written.
```

### Maddie, the West Country delivery bot: Gemini TTS `Aoede`, Bristol · LOCKED

Engine: Gemini TTS (AI Studio voice), `scripts/aistudio-tts.py --voice Aoede` (scene 4) and
`scripts/gpom/second-half-video/voice3.py` (second half). Suno was tried first and every robot take
came out American (r68, `narration-history.md`), so she is never Suno. 🔴 Free tier: 10 takes a
day (`docs/ai-studio/README.md`). Tags are Gemini's own (`[sarcastic]`, `[softly]`…), not Suno cues.

Scene 4 profile (verbatim, `songs/narration.md`):

```
# Audio Profile
Maddie, a small pavement delivery robot with a young woman's voice, late twenties. Dry, sarcastic and deadpan, unimpressed, rolling her eyes at her boss, but fond of him underneath. Clear articulation, quick natural conversational rhythm, a bit of a gossip. West Country accent as heard in Bristol. Never American, never Received Pronunciation. A real person, never robotic.

## Scene:
A ruined English high street, five years after a war. The world has been paused. She rolls up close to the camera to apologise for the narrator, a grand, gloomy voice who has just had a sulk about his fake world not working.

## Sample Context:
She has worked for him for years. He is dramatic; she is not. She tells tales on him, then for one moment drops the sarcasm and tells you something true and kind: he misses you. Then she catches herself.
```

Second-half profile (verbatim, the prompt on every second-half Maddie line in
`scenes/second-half-a-killbots/voices-d1.json` and `scenes/second-half-b-the-door/voices.json`):

```
# AUDIO PROFILE
Maddie, a small pavement delivery robot with a young woman's voice, late twenties. A real person, never robotic.

## THE SCENE
A dead English market town five years after the war, then a Cold War bunker under a Wiltshire hill. She is the only friendly thing left, and she knows it.

### DIRECTOR'S NOTES
Style: dry, warm and cheeky, apologetic for her boss but fond of him; quick, natural conversational rhythm, a bit of a gossip; clear articulation.
Pace: quick and chatty, with real pauses where the script marks them.
Accent: West Country, as heard in Bristol. Never American, never Received Pronunciation.

### SAMPLE CONTEXT
The voice you'd cast as the cheerful local in a British comedy who turns out to be the kindest person in it.
```

### The humans: Gemini TTS · LOCKED

Cast by ear by Kai on the voice audition page (https://claude.ai/artifact/PjhfJL9Ne3iFCtV6eXDH6t),
2026-10-20. The exact prompts are in
[`scenes/second-half-cut3-cast.json`](./scenes/second-half-cut3-cast.json) and repeated on every
line in the scenes' `voices*.json`.

| Character | Voice | Accent | Direction (from the prompt) |
| --- | --- | --- | --- |
| **Sandra** (the woman in the toilet-seat row) | `Autonoe` | Northern, Lancashire (Bolton) | sharp, sarcastic, every line a jab; quick and clipped; funny because she is completely serious |
| **Derek** (her husband) | `Algieba` | Scouse, Liverpool | indignant and exasperated in the row; in the circle angry and frightened, the first to say no; bursts, getting louder |
| **The old lady** | `Sulafat` | old-fashioned RP, 1950s BBC, Home Counties | dry, flat, deeply suspicious, then the softest she ever gets ("Kettle's on"); slow and deliberate, long pauses |
| **The crowd** (the hundred, "five or six voices at once down the corridor, one take each, stacked in the edit") | `Orus` · `Leda` · `Schedar` · `Vindemiatrix` · `Zubenelgenubi` · `Gacrux` | Swindon West Country (bus driver, 40s; woman, 20s) · educated Wiltshire (retired teacher, 70s) · Welsh, Newport (nurse, 50s) · Bristolian (builder, 30s) · Northern, Leeds (grandmother, 60s) | per line in `scenes/second-half-b-the-door/voices-d1.json` |

Every human prompt ends its accent line with **"Never American"** (and most with "never Received
Pronunciation"). The prompts use Google's four-part structure (Audio Profile, Scene, Director's
Notes, Sample Context; `docs/ai-studio/README.md`).

## Rules for this story

1. **Generate verbatim from the block.** Words change only with Kai. One atom per scene, in one
   file only: two copies of an atom is how takes once came back with superseded words.
2. **Record only when Kai says "record"**, and only the take he picked. **Listen (Gemini) only when
   Kai asks.** Never download; a real Suno download for the final mix is owed and is human only.
3. **Keep v6 narration prompts short.** On GPOM narration (2026-09-17), a ~1,000-character Style
   box, a bracket cue on every line and weirdness 40/60 made the Voice invent and mangle words; a
   ~200-character box, one top cue and weirdness 10 gave clean words (Kai: *"that sounds
   perfect"*). Which of the three mattered most was never separated. Build up one element at a
   time. The 2026-09-24 house settings then moved weirdness to 25 for scored scenes; the
   2026-09-17 "weirdness 10/20 only" rule is retired. Dry single lines run the pair 25 / 10.
4. **The newsreader never swears.** His authority is built out of restraint (the D&B cut's whole
   reason to exist). The crowd swears for him.
5. **The narrator is calm.** He never panics (the Richard Burton rule, orchestral sheet); the drama
   lives in the gap between the still voice and the music. One exception, on purpose: `gpom-sim-what`
   (*"the calm authority gone for once"*).
6. **Music never rises over a word.** Narration scores sit far back and low, always quieter than
   the words; the second-half cues are separate files under dry lines.
7. **Nothing is slowed** in the edit (house rule in the ending sheet's mix notes).
8. **Accents are British and regional; never American.** In Suno, keep a UK genre tag or the voices
   drift American (that note was learned on Karen/Camping; for GPOM it is why Maddie left Suno).
9. **Personalize, Variety and Max Mode are off; workspace `gpom-story`.** One Suno session at a
   time.

## Never

- Never type `BC-NEWSREADER` into Suno, and never pass just `badcode` as the Voice name.
- Never give the AI a body or a different voice; the AI is `badcode newsreader`, every time.
- Never use Suno for Maddie (she comes back American).
- Never a drum hit under the second-half ending; never action-movie or "Beethoven's Fifth" for the
  second-half cues.
- Never a children's choir, a vocoder by name, or the newsreader swearing on the D&B track.
- Never put round logs in `songs/narration.md`; never copy a live atom heading into the history file.

## History

- **2026-08-06 to 08-08, v5.5:** the orchestral master (newsreader + booming chant), then the D&B
  sibling over eight rounds: schoolchildren chorus cut (Suno's children's choir won't go dark), a
  gospel/terrace merge, the line-four device tried and retired, the vocoder rejected twice, commas
  as stress units, the round-eight keeper. All in the two song sheets' revision logs.
- **2026-08-27, dry and separate:** Kai ruled narration voice and music never generated together
  (three lanes: voice, flat loopable music, one-shot events). **Overridden for GPOM 2026-09-16**:
  *"the music for the GitPush story is actually a feature"*, voice and score in one take. The second
  half (October) went back to dry voice lines with separate cues, for edit control and because the
  ending's credit cap made one-take-per-scene necessary.
- **2026-09-10:** v5.5 retired; My Taste retired; Personalize always off.
- **2026-09-17:** a short "locked" narration style (cello, violin, piano swell, one drum hit, w35,
  then w10/20) and scenes 1 + 2 as one take; superseded 2026-09-24 by the house settings and
  template. Kept in `songs/archive/narration-v6.md`.
- **2026-09-21:** two copies of the data-centre atom caused three rounds with superseded words;
  merged into one `gpom-datacentre` atom.
- **2026-09-24:** `narration.md` reorganised as live-only, history newest-first.
- **2026-09-29:** scenes 2 and 3 merged into one take (the music grows across both); horns
  demoted, oboe leads (d03).
- **2026-09-30:** Suno robot takes all American (r68), so Maddie moved to Gemini TTS `Aoede`.
- **2026-10-15:** the D&B track became the downfall and opens the film.
- **2026-10-21 to 23:** second-half boss lines (round 1's one-take reads all rejected, one atom per
  line), cue C1/C2 rejected as too happy, the ending's AI lines; the last line's words were blocked
  by Suno's lyric filter twice ("Your lyrics contain copyrighted material") until read once with no
  bracket cues.
