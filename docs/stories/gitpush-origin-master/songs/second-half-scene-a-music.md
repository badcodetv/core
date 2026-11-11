---
title: GPOM second half, scene A (kill bots): the boss's lines + the music
status: ✅ all picks recorded (23 Oct) — boss lines 1–4, patrol P1/P2, chase C3; 5 Nov round 5: quicker boss lines 1 + 3 recorded (boss-r18/)
kind: one narrator take (the boss, dry) + two instrumental cues (P the patrol, C the chase and the call)
model: v6
workspace: gpom-story
scene: docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/
created: 2026-10-21
---

# GPOM second half, scene A: the boss's lines and the music

Scene A is the kill bots. They roam, the HUD hears a muffled human argument, kill mode, they race
to the bunker while Maddie phones her boss (the narrator, "the AI"), and they stand down when he
uses his exploit. This sheet holds the three things Suno makes for it:

| Atom | What | Engine | Duration |
| --- | --- | --- | --- |
| `gpom-sh-a-boss` | the boss's four lines, one take, cut apart in the edit | Suno, Voice `badcode newsreader` | 40 |
| `gpom-sh-a-P1` / `gpom-sh-a-P2` | cue P, **the patrol**: roaming → the muffled argument → kill mode | Suno, instrumental | 45 |
| `gpom-sh-a-C1` / `gpom-sh-a-C2` | cue C, **the chase and the call**: racing to the bunker under Maddie's call → stand down | Suno, instrumental | 60 |
| `gpom-sh-a-boss-1` … `-4` | **round 2:** the boss's four lines, **one atom per line** (Kai: none of round 1's one-take reads worked) | Suno, Voice `badcode newsreader` | 15 |
| `gpom-sh-a-C3` / `gpom-sh-a-C4` | **round 2:** cue C again, **dramatic and dark** (Kai: C1/C2 "too happy… not just sort of fun notes") | Suno, instrumental | 60 |

**Kai's brief for the music (2026-10-21):** *"more sparse orchestra, solo violin, cello… not
Beethoven's 5th, more Chopin."* Intimate, NOT action-movie. Tension by silence, not drums.

**Rules in force:** generate verbatim from the blocks; Personalize off; Variety Off; record only
when Kai says "record"; listen only when Kai asks; never download. Each cue's two atoms are written
**bold, not meek** (different instruments, different room, different mix, per-variation excludes
that ban the other atom's sound).

## Settings

| Control | Boss (`gpom-sh-a-boss`) | Music (P1 P2 C1 C2) |
| --- | --- | --- |
| Model | v6 | v6 |
| Voice | **`badcode newsreader`** (the AI, Kai insists on this exact voice) | none (detached) |
| Style Influence | 50 (house) | 75 (the pair rule) |
| Audio Influence | 65 (house) | n/a |
| Weirdness | **pair: 25 (house) and 10** (lower, for word fidelity on a dry read; 35 garbled words before) | **pair: 30 and 60** |
| Variety · Max Mode · Personalize | Off · Off · Off | Off · Off · Off |
| Vocal Gender | unset (the Voice supplies it) | unset |
| Duration | 40 | P 45 · C 60 |
| Workspace | `gpom-story` | `gpom-story` |

**Why Songs + Voice and not Speech (beta):** Speech is untested here (`suno-v6.md` §1b, §12 test
0), has no saved Voice, and Suno's own warning is a British accent drifting Australian. Kai's
narrator is the saved Voice, which only the Songs form takes. So the boss goes through the house
path with a style that asks for no music at all. Suno cannot make true silence; expect a little
room or a faint bed, and plan to cut lines apart in the edit.

### `gpom-sh-a-boss` — the boss's lines, as dry as Suno allows

Style:

```
Spoken word narration, voice only. One calm British male voice, a newsreader, unhurried and wry, speaking privately on a phone call. No music at all: no score, no bed, no instruments, only his voice and quiet silence between the lines. His delivery follows the cues: mildly amused, then quietly surprised, then calm and firm, then relieved and wry. Close-mic'd in a dead, dry voiceover booth, no reverb, his voice loud and right at the front. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, mildly amused]
Maddie, are you making fun of my simulations again?

[Spoken, quiet surprise]
Oh. ... Oh, wow. ... And they've activated their firewalls.

[Spoken, calm, firm]
No. I've got it.

[Spoken, relieved, wry]
Phew. Glad I kept that little exploit up my sleeve.
[End]
```

## Round 2: the boss, one line per atom

Kai on round 1 (22 Oct): *"none of them quite work… it's hard with Suno… just voice alone… each time 'Maddie,
are you making fun of my simulations again?' I would pick one of those. So I just wonder if we need to do each
line on its own… the boss doesn't need to speak that much."* So each line is its own atom, read once, with a
short style and **one** delivery cue (v6 narration prompts stay simple: long styles and many cues mangle words).

Settings for all four: v6 · Voice **`badcode newsreader`** · Style Influence 50 · Audio Influence 65 · Weirdness
**pair 25 / 10** · Duration 15 (line 2, the longest: 20) · Variety, Max Mode, Personalize Off · workspace `gpom-story`. Exclude styles: the
same list as `gpom-sh-a-boss`, in each block.

### `gpom-sh-a-boss-1` — "making fun of my simulations"

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, mildly amused. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, mildly amused]
Maddie, are you making fun of my simulations again?
[End]
```

### `gpom-sh-a-boss-2` — "they've activated their firewalls"

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, quietly surprised. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, quiet surprise]
Oh. ... Oh, wow. ... And they've activated their firewalls.
[End]
```

### `gpom-sh-a-boss-3` — "No. I've got it."

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, calm and firm. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, calm, firm]
No. I've got it.
[End]
```

### `gpom-sh-a-boss-4` — "that little exploit up my sleeve"

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, relieved and wry. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, relieved, wry]
Phew. Glad I kept that little exploit up my sleeve.
[End]
```

## Round 3: boss lines 2–4, revision B (new words)

Kai on round 2 (22 Oct): line 1 picked (`boss-1-A-v6-w10`); lines 2–4 get **new words**. Line 2 drops the "Oh,
wow"; line 4 drops "Phew" and "Glad" (the takes had a strange gap after "Glad"). Only the lyrics change; style,
exclude and settings are round 2's (v6 · Voice `badcode newsreader` · SI 50 · AI 65 · pair w25 / w10 · **Duration 15
for all three** · Variety, Max Mode, Personalize Off · `gpom-story`). One line, one cue, nothing else in the box.

### `gpom-sh-a-boss-2` revision B — "they've activated their firewalls"

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, quietly surprised. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, quiet surprise]
Oh. And they've activated their firewalls.
[End]
```

### `gpom-sh-a-boss-3` revision B — "I will handle it"

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, calm and firm. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, calm, firm]
No, thank you, Maddie. I will handle it.
[End]
```

### `gpom-sh-a-boss-4` revision B — "that zero-day up my sleeve"

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, relieved and wry. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, relieved, wry]
It was useful to keep that zero-day up my sleeve.
[End]
```

## Round 5: boss lines 1 and 3, quicker (cut round 18)

Kai, cut round 18 (5 Nov): the boss's two lines in the call need to be quicker, and **re-recorded, not just sped
up**. Only the delivery changes: the same Voice, the same calm British newsreader, now brisk and quick. Settings are
round 2's (v6 · Voice `badcode newsreader` · SI 50 · AI 65 · pair w25 / w10 · Duration 15 · Variety, Max Mode,
Personalize Off · `gpom-story`). Line 3 says the words the cut already uses, "No, thank you. I will handle it." (round
10 cut "Maddie" out of the take by hand; this read never says it).

### `gpom-sh-a-boss-1` revision B — "making fun of my simulations", brisk

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, brisk, quick and mildly amused. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, brisk, mildly amused]
Maddie, are you making fun of my simulations again?
[End]
```

### `gpom-sh-a-boss-3` revision C — "I will handle it", brisk

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, brisk, quick, calm and firm. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, brisk, calm, firm]
No, thank you. I will handle it.
[End]
```

## Scene B (the bridge): the boss answers Maddie

Scene B's bridge (11 Nov): Maddie rolls away from the bunker and radios him, *"Hey, boss, are you there?"*. He
answers on the private line, dry and patient, faintly amused, the same register as his scene A phone lines; then she
reports. One line, one atom, the dry-voice recipe (`sound.md`, "The dry-voice recipe used for the second half"). Kai
approved one pair ("Suno OK", 11 Nov). Settings as round 2: v6 · Voice `badcode newsreader` (Keep Current styles) ·
SI 50 · AI 65 · pair w25 / w10 · Duration 15 · Variety, Max Mode, Personalize Off · workspace `gpom-story`.

### `gpom-sh-b-boss-1` — "Yes, what is it?"

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, dry and patient. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, dry, patient]
Yes, what is it?
[End]
```

### `gpom-sh-b-boss-2` — "OK, well done, Maddie."

Bridge round 12 (11 Nov): Kai's second line for the boss, after Maddie reports. Same settings as `gpom-sh-b-boss-1`;
only the delivery word changes.

Style:

```
Spoken word, voice only. One calm British male newsreader on a private phone call, quietly pleased. No music. Dry, close-mic'd, no reverb.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, quietly pleased]
OK, well done, Maddie.
[End]
```

## Cue P — the patrol (~45 s)

Under the kill bots roaming, the HUD hearing a muffled human argument, then kill mode. Eerie and
lonely: held cello, sparse piano, a thin violin line, tension by silence not drums.

### `gpom-sh-a-P1` — solo cello + felt piano nocturne (dry, close, wooden room)

Style:

```
A lonely nocturne for solo cello and felt piano, eerie and very slow, free rubato time. One low cello note is held in an empty room, a few soft piano notes fall into long silences, then a thin, high violin line drifts in from far away, barely there. All the tension comes from silence and space; nothing ever lands on a beat. Recorded close and intimate in a small dry wooden room, you hear the bow hair and the felt hammers. Near the end the cello sinks into a low, uneasy tremolo that never resolves.
```

Exclude styles:

```
vocals, singing, voice, choir, humming, drums, drum kit, percussion, timpani, beat, pulse, groove, string quartet, string section, full orchestra, pizzicato, brass, horns, woodwinds, harp, synth, electronic, pad, reverb wash, epic, heroic, action, trailer, bombastic, major key, happy
```

### `gpom-sh-a-P2` — string quartet, cold harmonics, lone violin (distant, stone hall)

Style:

```
Chamber string quartet playing sul ponticello and glassy harmonics, cold, hollow and unsettling. Viola and cello sustain one quiet, unresolved chord that barely moves while a lone first violin searches above it in thin, broken phrases with long held breaths between. The players seem to hold their breath: pianissimo throughout, a hush down to almost nothing, then one sharp dissonant swell at the very end that cuts off. Captured from the back of a large cold stone hall, distant, wide and reverberant.
```

Exclude styles:

```
vocals, singing, choir, piano, keys, felt piano, drums, percussion, timpani, beat, groove, pulse, brass, horns, woodwinds, synth, electronic, full orchestra, solo cello nocturne, warm, romantic, lush, epic, action, heroic, trailer, major key
```

## Cue C — the chase and the call (~60 s)

Kill bots racing to the bunker while Maddie phones her boss, ending when they stand down. Restless
but intimate: pizzicato and solo cello pulse, a solo violin that climbs, piano, quiet urgency, no
percussion kit, resolves softly at the end.

### `gpom-sh-a-C1` — pizzicato quartet, climbing violin (crisp, close, small ensemble)

Style:

```
Restless chamber music for string quartet and a little piano. Plucked pizzicato cello and viola pulse like a quick, nervous heartbeat, light on their feet, while a solo violin starts low and climbs phrase by phrase, higher and more urgent; soft piano chords punctuate the gaps. Quiet urgency, all made by strings and hands, never loud. In the last stretch the plucking slows, the violin settles onto one long tender note and the piece resolves softly into a warm, still major chord. Crisp, close and detailed, like a small ensemble playing in a living room.
```

Exclude styles:

```
vocals, singing, choir, drum kit, drums, snare, percussion, timpani, beat, electronic, synth, bass drop, brass, horns, full orchestra, string section, rubato nocturne, piano solo, epic, action, trailer, bombastic, heroic, dramatic, dark ambient
```

### `gpom-sh-a-C2` — Chopin-like piano étude with solo cello (warm parlour, rubato)

Style:

```
Romantic solo piano in the manner of a Chopin étude, agitated and fluid: a running left-hand figure in a minor key, breathless and restless, with a singing solo cello answering the piano's melody. One piano and one cello in a warm parlour, rubato, rising and falling in waves of quiet urgency, never pounding. A solo violin joins only near the end, climbing above the cello. Then the running figure dissolves, the tempo eases, and it closes on soft, still, resolved chords.
```

Exclude styles:

```
vocals, singing, choir, drums, drum kit, percussion, timpani, beat, string quartet, pizzicato, plucked strings, full orchestra, string section, brass, horns, synth, electronic, jazz, pop, epic, action, trailer, bombastic, heroic, cinematic
```

## Cue C, round 2 — the chase and the call, dark (~60 s)

Kai on C1/C2 (22 Oct): *"all of these are too happy… we need a more dramatic piece that's not just sort of fun
notes."* Still orchestral and intimate (Kai's 21 Oct brief: sparse, solo strings, not Beethoven's 5th), but tense,
dark and driving: no pizzicato, nothing playful, no drum kit, no action-movie brass. Two bold, unlike atoms; each
exclude list bans the other's sound. Settings as the music column: Style Influence 75, pair w30 / w60, Duration 60.

### `gpom-sh-a-C3` — relentless low-string ostinato (raw, close, small dry room)

Style:

```
Dark, driving chamber music for a small low-string ensemble. Two cellos saw out a relentless minor-key ostinato in hard, bowed sixteenth notes, like a heart running too fast, with a double bass digging in underneath on the downbeats. High violins shiver in a tight tremolo above, and every few bars a harsh dissonant chord tightens the screw. It never lets up: denser, louder and more desperate through the whole minute, building dread. Recorded raw and very close in a small dry room, you hear rosin, bow scrape and breath. Near the end the ostinato breaks off and only one low, uneasy held note remains.
```

Exclude styles:

```
vocals, singing, choir, pizzicato, plucked strings, playful, light, whimsical, happy, major key, piano, keys, drum kit, drums, snare, percussion, timpani, beat, brass, horns, epic, heroic, trailer, action movie, synth, electronic, reverb wash, distant, ambient, nocturne, romantic, warm
```

### `gpom-sh-a-C4` — lone piano in the deep bass, tremolo violin (cold, vast hall)

Style:

```
Stark, cold, menacing solo piano hammering an obsessive minor figure in its lowest octaves, repeated over and over and slowly accelerating, each low note left to ring. A single violin hangs far above it on a thin, trembling tremolo, and a cello holds one dark drone that swells and sinks like breathing. Sparse and merciless: tension from repetition and silence, no melody to hold on to. Captured from the back of a vast empty concert hall, long cold decay, wide and distant. In the last stretch the piano figure thickens into clusters, then stops dead, and the violin tremolo is left alone, fading.
```

Exclude styles:

```
vocals, singing, choir, pizzicato, plucked strings, string quartet, string ensemble, ostinato strings, double bass, playful, light, whimsical, happy, major key, romantic, rubato, waltz, drum kit, drums, percussion, timpani, beat, brass, horns, epic, heroic, trailer, action movie, synth, electronic, close-mic, dry
```

## Round log

New rounds at the top.

### Round 7 (2026-11-11) · bridge round 12, scene B boss line 2 "OK, well done, Maddie." · recorded

Atom `gpom-sh-b-boss-2` revision A, 2 Creates (w25 + w10), counter 6,620 → 6,605 (lags; 20 expected). No Suno tab was
open on any channel, so one was opened (`open-tab`, channel 1); the form was empty. Same-prompt check: nothing close.
All four recorded (`record-checked.py`, never downloaded) to `clips/second-half/audio/boss-b/takes/`. Listen tool not run.

| Take | Length | Link | Measured |
| --- | --- | --- | --- |
| gpom-sh-b-boss-2-A-v6-w25 | 0:12 | https://suno.com/song/7a212072-9464-4f22-94c2-a8405dbb4180 | ✅ words right; tone at 7–8 s (cut off) |
| gpom-sh-b-boss-2-A-v6-w25 | 0:13 | https://suno.com/song/d6de1ae3-4e01-43c9-aa60-0e937031aeb5 | ✅ words right; tone/noises at 8–9.5 s (cut off) |
| gpom-sh-b-boss-2-A-v6-w10 | 0:05 | https://suno.com/song/8820f774-5bb5-40a9-a02c-805b7248c503 | ✅ words right, no tone |
| gpom-sh-b-boss-2-A-v6-w10 | 0:13 | https://suno.com/song/f3fb9bac-616d-4d5a-8752-c34b563ee7ca | ✗ says the line twice |

Every take pauses 0.8–1.2 s after "OK,". Tight cuts (pause closed to 0.35 s, 0.1 s head/tail): 7a212072 2.68 s,
d6de1ae3 2.52 s, 8820f774 2.57 s; pause-kept `takes/<take>-trim.wav`: 3.13 s, 3.22 s, 3.38 s. Whisper hears
"Okay, well done, Maddie." on all three.

### Round 6 (2026-11-11) · scene B boss line "Yes, what is it?" · recorded, pick owed (Kai)

Kai approved one pair ("Suno OK", 11 Nov). Atom `gpom-sh-b-boss-1` revision A, 2 Creates (w25 + w10) = **20 credits
expected**; the counter read 6,630 → 6,620 (it lags, as in rounds 3 and 5). Before loading, the form held *The Rules*
round 3 (`Rules r3-sampler-mangled-amen-v6-w80`, workspace `short-the-rules`, all eight takes finished and committed,
no Suno process running). Voice `badcode newsreader` attached, Keep Current. Same-prompt check: nothing close. All four
takes recorded (`record-checked.py`, never downloaded) to
`/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/audio/boss-b/takes/`. The listen tool was not run.

| Take | Length | Link | Measured |
| --- | --- | --- | --- |
| gpom-sh-b-boss-1-A-v6-w25 | 0:06 | https://suno.com/song/b790769c-3504-4ddc-bcfa-f9c3ff7a74bf | ✅ words right, 0.58 s pause after "Yes," · **recommended** |
| gpom-sh-b-boss-1-A-v6-w25 | 0:08 | https://suno.com/song/56eef7a5-3812-42f7-982c-c0bfd023f4cc | ✅ words right, quickest "what is it?", 0.86 s pause |
| gpom-sh-b-boss-1-A-v6-w10 | 0:10 | https://suno.com/song/a752d5cd-3d3f-4e73-93ef-29b31cc037d6 | ✅ words right ("Yes. What is it?"), slowest, 1.0 s pause; extra noises at 8–9 s |
| gpom-sh-b-boss-1-A-v6-w10 | 0:12 | https://suno.com/song/ee3b349a-85af-4f85-b378-f4bbf89702cd | ✗ says the line twice (second read at 8.3 s) |

**Every take** carries a ~470–490 Hz pure tone at ~4–5 s, after the words (not at the start this time); no take has a
tone before the words, and the pauses sit 55–65 dB below the voice (no bed). Speech starts within ~10 ms of the file
start. Cuts (tone dropped, 0.1 s head/tail): `boss-b/<take>-tight.wav` (pause after "Yes," closed to 0.35 s: b790769c
2.17 s, 56eef7a5 1.60 s, a752d5cd 2.08 s) and `boss-b/takes/<take>-trim.wav` (pause kept: 2.38 s, 2.09 s, 2.71 s).
Whisper hears "Yes, what is it?" on every cut.

### Round 5 (2026-11-05) · boss lines 1 and 3 quicker (cut round 18) · picked by measurement, recorded

Kai asked for these two lines re-recorded faster (not sped up) and authorised the recording. 4 Creates (2 pairs, w25 +
w10) = **40 credits expected**; the on-page counter read 7,000 before and after (stale again, as in round 3). Workspace
`gpom-story`; form was empty and idle before loading (one Suno tab opened on channel 1). All 8 takes recorded
(`record-checked.py`, never downloaded) to `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/audio/boss-r18/takes/`.
The listen tool was not run.

| Take | Length | Link | Measured |
| --- | --- | --- | --- |
| gpom-sh-a-boss-1-B-v6-w10 | 0:06 | https://suno.com/song/67d3ebbb-c2e7-4aa9-a639-d47a6be5a9ae | ✗ opens on a ~0.25 s pure ~490 Hz tone |
| gpom-sh-a-boss-1-B-v6-w10 | 0:06 | https://suno.com/song/6e9f7089-58a6-47eb-af02-a832b30b54fa | ✗ the same tone |
| gpom-sh-a-boss-1-B-v6-w25 | 0:06 | https://suno.com/song/148779af-c790-4dd9-8c78-7f08036a5bd6 | ✅ **pick**: clean, words right |
| gpom-sh-a-boss-1-B-v6-w25 | 0:06 | https://suno.com/song/76980c9b-e753-42c2-ab61-7940a39c6892 | ✗ the same tone |
| gpom-sh-a-boss-3-C-v6-w10 | 0:07 | https://suno.com/song/56012b1c-393a-410d-b2d4-51420855d697 | ✗ a held sung-like note (233/282 Hz) after the words |
| gpom-sh-a-boss-3-C-v6-w10 | 0:05 | https://suno.com/song/1c2df008-8e72-469a-88f7-0a7323716767 | ✗ a 0.8 s 466 Hz tone after "it." |
| gpom-sh-a-boss-3-C-v6-w25 | 0:06 | https://suno.com/song/d447089a-aa36-4b83-a0e8-c8c547f376f2 | ✅ **pick**: clean, quickest read |
| gpom-sh-a-boss-3-C-v6-w25 | 0:08 | https://suno.com/song/f6a70f8b-0cd5-44f6-bde9-3e76faf4b148 | ✗ a tone near the end, 3.5 s of dead air |

**What "brisk" did.** On line 1, nothing measurable: every take reads "are you making fun of my simulations again?" in
~2.6 s exactly like the round 2 pick, and every take (old and new) stops ~1.1–1.5 s after "Maddie,". On line 3 it
worked on one take: d447089a says "Thank you, I will handle it" in one breath (speech 2.69 s against the old 4.12 s).

**The picks** (faster-whisper small.en hears every word; no bed in the pauses, -52 to -59 dB below the voice; f0
around 55–70 Hz like the old picks). The pause after the first word is closed to 0.3 s, because no take had none over
0.4 s; head and tail trimmed to 0.1 s:
- line 1: `boss-r18/gpom-sh-a-boss-1-b-v6-w25-148779af-tight.wav`, **3.51 s** (old pick trimmed the same way: 4.70 s;
  raw 6.76 s). Pauses kept: `takes/…148779af-trim.wav`, 4.72 s (no shorter than the old).
- line 3: `boss-r18/gpom-sh-a-boss-3-c-v6-w25-d447089a-tight.wav`, **2.36 s** (old `-noname` trimmed the same way:
  4.32 s; raw 5.42 s). Pauses kept: `takes/…d447089a-trim.wav`, 2.90 s.

⚠ The first record of d447089a came back 5.00 s (the stale-duration bug, `automation.md` §10); the re-record is 6.36 s
and replaced it in `takes/`.

### Round 4 (2026-10-23) · Kai's round 3 picks recorded · no Creates

**Kai's round 3 picks, recorded** (never downloaded; `record-checked.py`, length matched to the takes list; 0 credits):
boss line 2 = `gpom-sh-a-boss-2-B-v6-w25` [d7aaef3e](https://suno.com/song/d7aaef3e-9921-4d23-9384-107f917b9425) (6.40 s),
boss line 3 = `gpom-sh-a-boss-3-B-v6-w10` [bfb1220b](https://suno.com/song/bfb1220b-2b48-4993-89d4-5047cac9f4a1) (6.00 s),
boss line 4 = `gpom-sh-a-boss-4-B-v6-w25` [543dafef](https://suno.com/song/543dafef-3e5e-449f-a783-7260e599c848) (7.60 s).
Files in `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/cut3/A/suno/` (`.wav` + `.preview.mp3`).

Whisper (faster-whisper small.en) hears every word on all four boss picks: line 1 *"Maddie, are you making fun of my
simulations again?"*; line 2 *"Oh, and they've activated their firewalls."* (1.7 s pause after "Oh"); line 3 *"No. Thank
you, Maddie. I will handle it."*; line 4 *"It was useful to keep that zero day up my sleeve."* (a 1.1 s stretch on
"useful to" and a 1.0 s one on "day up": the read is slow, not gapped). The listen tool was not run.

⚠ **Recording incident:** WSLg's PulseAudio wedged after the first take (`pactl` timing out, then connection refused;
`SINK_NOT_FOUND` / `PLAY_NOT_MAPPED` / `PULSE_FAILED`). Fixed per `docs/listening/automation.md`:
`./scripts/audio-server.sh` started the private PulseAudio (`unix:/tmp/badcode-pulse/native`, records but is not
audible in WSL), then `browser-channel.sh down 1 && up 1` relaunched channel 1 onto it and `suno.mts open-tab` reopened
the one Suno tab. The other two recorded first time. Channel 1 now plays into the private server until it is relaunched
again with WSLg healthy.

### Round 3 (2026-10-22) · boss lines 2–4 revision B (new words) · picks owed (Kai)

**Kai's round 2 picks, recorded** (never downloaded; `record-checked.py`, length matched to the takes list):
boss line 1 = `gpom-sh-a-boss-1-A-v6-w10` [7f8d1ef8](https://suno.com/song/7f8d1ef8-2548-4eff-a155-3a69b3677fd8) (6.76 s),
chase cue C = `gpom-sh-a-C3-A-v6-w60` [a1614dbb](https://suno.com/song/a1614dbb-401a-4930-b759-7ad5b9cd3ce4) (60.00 s; the
first try came back 12.4 s, the playbar trap, and the re-record matched). Files in
`/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/cut3/A/suno/` (`.wav` + `.preview.mp3`).

Before the round: an outside session (not this team) spent 470 credits (8,420 at the end of round 2 → 7,950) while the form sat idle on our C4, and
closed the suno.com tab; we held until Kai said Suno was free, then opened one tab. Balance at the start **7,950**.

6 Creates (3 pairs, w25 + w10), expected **30 credits**; the on-page counter did not refresh during the run (it read
7,950 throughout, per-Create readings of 5 and 10 are noise), so the true after-balance is unread. Workspace `gpom-story`.
Nothing listened to, nothing recorded from this round.

| Take | Length | Link |
| --- | --- | --- |
| gpom-sh-a-boss-2-B-v6-w25 | 0:06 | https://suno.com/song/d7aaef3e-9921-4d23-9384-107f917b9425 |
| gpom-sh-a-boss-2-B-v6-w25 | 0:07 | https://suno.com/song/da519086-a759-461e-87bd-48d033270027 |
| gpom-sh-a-boss-2-B-v6-w10 | 0:08 | https://suno.com/song/4a9523b4-eb5d-4f4c-b54d-2e83011b72b7 |
| gpom-sh-a-boss-2-B-v6-w10 | 0:07 | https://suno.com/song/4c2b009e-51ce-484b-8c1b-e0f89207eeba |
| gpom-sh-a-boss-3-B-v6-w25 | 0:08 | https://suno.com/song/b158e816-75f7-4ba9-9e1d-ee8ab454b32b |
| gpom-sh-a-boss-3-B-v6-w25 | 0:07 | https://suno.com/song/a2ebbbc9-7b03-4883-8bc9-ded726ba512c |
| gpom-sh-a-boss-3-B-v6-w10 | 0:06 | https://suno.com/song/f36a3b14-3576-4bb4-b0bf-839aa598075b |
| gpom-sh-a-boss-3-B-v6-w10 | 0:06 | https://suno.com/song/bfb1220b-2b48-4993-89d4-5047cac9f4a1 |
| gpom-sh-a-boss-4-B-v6-w25 | 0:07 | https://suno.com/song/543dafef-3e5e-449f-a783-7260e599c848 |
| gpom-sh-a-boss-4-B-v6-w25 | 0:07 | https://suno.com/song/c3549816-3772-4593-a5ca-4576da00d93b |
| gpom-sh-a-boss-4-B-v6-w10 | 0:08 | https://suno.com/song/cacc500d-125b-4c9f-a9d8-7fdf76544526 |
| gpom-sh-a-boss-4-B-v6-w10 | 0:07 | https://suno.com/song/9c4b3ba9-7694-4b2b-876c-612fed0a13cc |

**Notes.** All twelve came in at 0:06–0:08 (one line each, Duration 15 is a ceiling, not a target). Whether the words
are clean, and whether the gap after line 4's old "Glad" is gone, is unheard.

### Round 2 (2026-10-22) · boss one line per atom, C3/C4 dark · picks owed (Kai)

**Kai's round 1 picks, recorded** (never downloaded; `record-checked.py`, length matched to the takes list):
P1 = `gpom-sh-a-P1-A-v6-w60` [57b65bfc](https://suno.com/song/57b65bfc-430e-4ec3-b944-97b57ef2d7af) (0:45),
P2 = `gpom-sh-a-P2-A-v6-w30` [49a6688a](https://suno.com/song/49a6688a-0bfa-424f-b476-7585158dbfb5) (0:44) — one pick
in each patrol style. Files: `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/cut3/A/suno/`
(`.wav` + `.preview.mp3`). No pick for the boss or for C1/C2 (notes above each new atom).

12 Creates, **80 credits (8,500 → 8,420)**, workspace `gpom-story`. Before the round the form held another session's
bank-robbery take (`br-poet-G-carter-v6-w60`, workspace `bank-robbery-Kai`, style 512, exclude 207, 97 lyric
paragraphs, w60, SI 75, Duration 210); credits held at 8,500 and the title did not move for 4+ minutes, so we loaded
over it. Nothing listened to.

⚠ **Recording older takes:** `suno.mts record` only finds rows mounted in the create page's virtualised list, so a take
from yesterday is `TAKE_NOT_FOUND` once ~30 newer takes sit above it. Worked around by wheel-scrolling the list until the
row mounted, then recording. Whoever owns `suno.mts` could make `findTake` scroll.

| Take | Length | Link |
| --- | --- | --- |
| gpom-sh-a-boss-1-A-v6-w25 | 0:09 | https://suno.com/song/f2097ef5-a26f-4d9e-87a8-46d8f7532589 |
| gpom-sh-a-boss-1-A-v6-w25 | 0:09 | https://suno.com/song/3bc74680-d553-4d52-bf7e-ea8afcbc1bea |
| gpom-sh-a-boss-1-A-v6-w10 | 0:07 | https://suno.com/song/7f8d1ef8-2548-4eff-a155-3a69b3677fd8 |
| gpom-sh-a-boss-1-A-v6-w10 | 0:12 | https://suno.com/song/3b37a3f3-5622-4abb-afb7-2adefc5042af |
| gpom-sh-a-boss-2-A-v6-w25 | 0:10 | https://suno.com/song/f8e44f50-8f47-4ecb-8a62-3ac1c6f82211 |
| gpom-sh-a-boss-2-A-v6-w25 | 0:10 | https://suno.com/song/7efca8ec-f5ce-44d2-a1be-31f109c1eea2 |
| gpom-sh-a-boss-2-A-v6-w10 | 0:10 | https://suno.com/song/2f1c52cb-a7b6-4a67-b2c8-e9c9c9540e82 |
| gpom-sh-a-boss-2-A-v6-w10 | 0:10 | https://suno.com/song/27f5cae7-2fa5-4d5d-85f1-1fe022029f98 |
| gpom-sh-a-boss-3-A-v6-w25 | 0:08 | https://suno.com/song/497f5363-5fe9-4e85-9fdd-6b94cf6c6159 |
| gpom-sh-a-boss-3-A-v6-w25 | 0:07 | https://suno.com/song/34f0fc0a-3175-4241-9392-7532c4d0d2a7 |
| gpom-sh-a-boss-3-A-v6-w10 | 0:07 | https://suno.com/song/db21608c-d7b7-4df5-9e3c-daed5a509f99 |
| gpom-sh-a-boss-3-A-v6-w10 | 0:06 | https://suno.com/song/07ca6aee-424f-4895-9030-d68101e20f39 |
| gpom-sh-a-boss-4-A-v6-w25 | 0:07 | https://suno.com/song/f890b363-26fa-4c35-887c-1b570137c1ea |
| gpom-sh-a-boss-4-A-v6-w25 | 0:08 | https://suno.com/song/50a82181-807c-44ed-b64e-8db6f17413bc |
| gpom-sh-a-boss-4-A-v6-w10 | 0:08 | https://suno.com/song/0405c2f4-f6d5-4caf-a22e-6ae674891ee1 |
| gpom-sh-a-boss-4-A-v6-w10 | 0:07 | https://suno.com/song/3eb2c01f-1d49-40e3-94a3-ab70f48e9fdc |
| gpom-sh-a-C3-A-v6-w30 | 1:00 | https://suno.com/song/df233838-5a4f-4a51-9665-df868b9d6c2a |
| gpom-sh-a-C3-A-v6-w30 | 1:03 | https://suno.com/song/9d14e097-cda5-45c4-ad00-a8631ce705c3 |
| gpom-sh-a-C3-A-v6-w60 | 1:00 | https://suno.com/song/752f3869-dc3c-4587-9853-4656216f96dd |
| gpom-sh-a-C3-A-v6-w60 | 1:00 | https://suno.com/song/a1614dbb-401a-4930-b759-7ad5b9cd3ce4 |
| gpom-sh-a-C4-A-v6-w30 | 1:10 | https://suno.com/song/b3fb99e7-d056-4df6-ab34-7540abd39d4d |
| gpom-sh-a-C4-A-v6-w30 | 1:00 | https://suno.com/song/bf0579b8-6c73-445b-beb6-caaf4256c189 |
| gpom-sh-a-C4-A-v6-w60 | 1:00 | https://suno.com/song/b6c5973d-42c5-45e3-b2ea-006ce284e36c |
| gpom-sh-a-C4-A-v6-w60 | 1:00 | https://suno.com/song/d9f611a3-9319-4e89-a729-d63aef1af81b |

**Notes.** The one-line boss takes stop short of their 15/20 s target (0:06–0:12), which is what a single line should
do. Whether each says its words cleanly is unheard. C3/C4 came in on target (1:00–1:10).

### Round 1 (2026-10-21) · revision A of all five atoms · unheard

10 Creates, **100 credits (10,120 → 10,020)**, 10 per Create, workspace `gpom-story`. Settings as
the table above. Nothing recorded, nothing listened to, nothing downloaded. Before the round the
form held another session's bank-robbery round D (`br-ska-D-geezer-v6-w60`, `bank-robbery-Kai`); we
waited until it had finished and the form had been quiet for 4+ minutes, then loaded over it.

| Take | Length | Link |
| --- | --- | --- |
| gpom-sh-a-boss-A-v6-w25 | 0:30 | https://suno.com/song/ae6b3568-3e33-4a85-a588-a3392d0cd0f3 |
| gpom-sh-a-boss-A-v6-w25 | 0:21 | https://suno.com/song/22e2c2a3-57be-4fdd-98a1-6f8ca1ca58e6 |
| gpom-sh-a-boss-A-v6-w10 | 0:30 | https://suno.com/song/1d4c1eb0-b646-46d3-98de-f37209664eca |
| gpom-sh-a-boss-A-v6-w10 | 0:36 | https://suno.com/song/47f4ae23-4ccc-4d6b-bdf4-08b694e1218e |
| gpom-sh-a-P1-A-v6-w30 | 0:45 | https://suno.com/song/4967ea91-6b84-4736-b321-db36c0f23abd |
| gpom-sh-a-P1-A-v6-w30 | 0:45 | https://suno.com/song/af7d1f63-2683-4a87-8c32-5dbb891bc4f7 |
| gpom-sh-a-P1-A-v6-w60 | 0:45 | https://suno.com/song/57b65bfc-430e-4ec3-b944-97b57ef2d7af |
| gpom-sh-a-P1-A-v6-w60 | 0:47 | https://suno.com/song/aaf6f059-c631-475b-8571-8f3c525e3ddb |
| gpom-sh-a-P2-A-v6-w30 | 0:44 | https://suno.com/song/49a6688a-0bfa-424f-b476-7585158dbfb5 |
| gpom-sh-a-P2-A-v6-w30 | 0:45 | https://suno.com/song/fdc26ec1-65d0-4722-a27a-9e5eac14bc5c |
| gpom-sh-a-P2-A-v6-w60 | 0:44 | https://suno.com/song/dd3f78e8-aca6-4f4f-a922-2c632215b69d |
| gpom-sh-a-P2-A-v6-w60 | 0:45 | https://suno.com/song/fa09bff7-4e88-4e62-b743-46cf12ecd770 |
| gpom-sh-a-C1-A-v6-w30 | 1:00 | https://suno.com/song/51a8d60f-c9ee-4709-a001-456fc8533513 |
| gpom-sh-a-C1-A-v6-w30 | 1:08 | https://suno.com/song/f45603ec-b8fd-42b2-b5fc-9371051a2431 |
| gpom-sh-a-C1-A-v6-w60 | 1:00 | https://suno.com/song/acf437d2-4ea8-41ca-807a-39eab3c00c70 |
| gpom-sh-a-C1-A-v6-w60 | 1:00 | https://suno.com/song/f88dba0a-2a87-4333-bc4b-d47e0f060fd9 |
| gpom-sh-a-C2-A-v6-w30 | 0:59 | https://suno.com/song/8f29b1ef-dbce-472c-a695-02e90b3d8e70 |
| gpom-sh-a-C2-A-v6-w30 | 1:02 | https://suno.com/song/746eb1fe-cf3b-4581-bb26-b58c132fa1bd |
| gpom-sh-a-C2-A-v6-w60 | 1:00 | https://suno.com/song/6d0d8745-41dc-4497-a8aa-66ab0c7fd75f |
| gpom-sh-a-C2-A-v6-w60 | 1:02 | https://suno.com/song/f5e6e4ce-5685-40a2-ac44-dcf5fb8f8b5e |

**Notes.** The instrumentals came in on target (45 → 0:44–0:47, 60 → 0:59–1:08). The boss takes
came in **short of the 40 s target** (0:21–0:36): there are only ~15 s of words, so a dry read
stops early. **`boss-A-v6-w25` 0:21** is short even against its twin (the house rule 5 symptom):
check it says all four lines before judging it. Whether any take is truly music-free is unheard.
