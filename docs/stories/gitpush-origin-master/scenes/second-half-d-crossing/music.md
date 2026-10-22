---
title: GPOM second half D (the clean room and the crossing): music cues + the AI's lines
status: 🟡 stage 1, written. Nothing generated
model: v6
workspace: gpom-story
scene: docs/stories/gitpush-origin-master/scenes/second-half-d-crossing/
created: 2026-10-21
---

# Scene D, the clean room and the crossing: music and the AI's lines

Sparse and intimate, as Kai ruled: a solo cello, a solo violin, a little piano. Chopin, not
Beethoven. **The ending may swell, but it stays restrained.** The house format and rules are those of
[`../../songs/second-half-scene-a-music.md`](../../songs/second-half-scene-a-music.md). Not reused:
`gpom-sh2-s4` (the crossing as drum-and-bass hybrid) and `gpom-sh2-s3`/`hundred` (brass). Both break
the 21 Oct ruling.

## Cue list

| Cue | Under | In → out | What it does |
| --- | --- | --- | --- |
| **D-room** | d1 → d6 | in after Sandra's "fussy" line (~0:06), out under the old lady's question (~1:08) | The clean room: high, glassy piano in a slow, music-box-like pattern, tender and a little uncanny, with a thin violin harmonic above. It says *"it made it nice for them"* and *"you will not understand this"* at once. It drops out completely under *"That the companies cutting the jobs kept the gains. And you paid."*, which plays dry. |
| **D-cross** | d7 → d8 | in on the hands (~1:14), out hard on the cut to the objects (~1:35) | The crossing: a solo cello melody over slow piano, the violin joining above it. One **restrained swell**: it peaks as the chair lights spiral on and the seam runs bright, then stops dead on the seam going dark. |
| — | d9 | ~1:35 → end | **True silence** (room hum only), then Maddie. Her *"Boss?"* gets no music and no answer. The film's one true silence. |

### `gpom-sh-d-room` — glassy piano, music-box tenderness (duration 70)

Settings: v6 · Style Influence 75 · Weirdness **pair 30 / 60** · Duration 70 · instrumental.

Style:

```
A slow, delicate piece for solo piano in its high register, a gentle repeating music-box-like pattern, tender and slightly uncanny, like a lullaby played in a spotless empty room. A thin, high violin harmonic hangs above it now and then, barely there. Very quiet, very clean, lots of space and silence between the notes, in the manner of a Chopin nocturne slowed almost to stillness. Recorded close, bright and clear, a small dry room.
```

Exclude styles:

```
vocals, singing, choir, humming, drums, percussion, beat, pulse, groove, bass, cello, low strings, brass, horns, full orchestra, string section, synth, electronic, pad, ambient drone, epic, heroic, action, trailer, dark, menacing, horror
```

### `gpom-sh-d-cross` — cello and piano nocturne, one restrained swell (duration 45)

Settings: v6 · Style Influence 75 · Weirdness **pair 30 / 60** · Duration 45 · instrumental.

Style:

```
A slow, heartbreaking nocturne for solo cello and piano, in the manner of Chopin. The piano plays slow, warm broken chords and the cello sings a long, simple, aching melody over them. A solo violin joins above the cello halfway through and the two lines climb together into one restrained swell, full and tender but never loud or grand, then everything stops on a single unresolved chord left hanging in silence. Recorded close and intimate in a warm wooden room, rubato, you hear the bow.
```

Exclude styles:

```
vocals, singing, choir, humming, drums, percussion, timpani, beat, pulse, brass, horns, brass band, full orchestra, string section, synth, electronic, pad, epic, heroic, action, trailer, bombastic, cinematic swell, crescendo to fortissimo, major key fanfare, march
```

## The AI's lines (Suno atoms)

The AI is the Suno Voice **`badcode newsreader`**, dry, with the settings of `gpom-sh-a-boss` (v6, SI 50,
AI 65, weirdness **pair 25 / 10**, Personalize, Variety and Max off, workspace `gpom-story`). In this
scene he speaks **through Maddie's speaker**, with the filter in the mix and the beacon pulsing on his
words. Each line is its own atom (the retake unit). The run makes **one take per scene** with every
atom as a section and cuts them apart.

| Atom | Beat · frame | Line | Cue |
| --- | --- | --- | --- |
| `gpom-sh-end-ai-d1` | d1 · D00 | *Suits on, please. It's a clean room.* | `[Spoken, polite, a host with house rules]` |
| `gpom-sh-end-ai-d2` | d3 · D03 | *You wouldn't follow how it works. What it runs on, you already know.* | `[Spoken, plain, no showing off]` |
| `gpom-sh-end-ai-d3` | d3 · D04 | *You. And your consciousness.* | `[Spoken, gently]` |
| `gpom-sh-end-ai-d4` | d4 · D06 | *Milk, two sugars. I kept your loyalty cards.* | `[Spoken, helpful, matter-of-fact]` |
| `gpom-sh-end-ai-d5` | d5 · D08 | *You don't. Believing it is your bit.* | `[Spoken, plain, unhurried]` |
| `gpom-sh-end-ai-d6` | d5 · D10 | *No. This is all of it. I don't know if it works.* | `[Spoken, honest, quiet]` |
| `gpom-sh-end-ai-d7` | d6 · D11 | *That the companies cutting the jobs kept the gains. And you paid.* | `[Spoken, straight, quiet, no irony]` |

### `gpom-sh-end-ai-D` — the scene's take (all seven atoms), duration 60

Style:

```
Spoken word narration, voice only. One calm British male voice, a newsreader, unhurried and wry, speaking quietly to a group of people in a quiet room. No music at all: no score, no bed, no instruments, only his voice and quiet silence between the lines. His delivery follows the cues: polite, plain, gentle, matter-of-fact, plain again, then honest and quiet, and the last line completely straight. Close-mic'd in a dead, dry voiceover booth, no reverb, his voice loud and right at the front. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, polite, a host with house rules]
Suits on, please. It's a clean room.

[Spoken, plain, no showing off]
You wouldn't follow how it works. ... What it runs on, you already know.

[Spoken, gently]
You. ... And your consciousness.

[Spoken, helpful, matter-of-fact]
Milk, two sugars. I kept your loyalty cards.

[Spoken, plain, unhurried]
You don't. ... Believing it is your bit.

[Spoken, honest, quiet]
No. ... This is all of it. ... I don't know if it works.

[Spoken, straight, quiet, no irony]
That the companies cutting the jobs kept the gains. ... And you paid.
[End]
```

## Round log

New rounds go at the top.

- **21 Oct 2026:** generated from the live sheet [`../../songs/second-half-ending-music.md`](../../songs/second-half-ending-music.md) (rounds A and B, 150 credits for all three scenes). Takes, links, picks and reasons are there and in [`../second-half-ending-log.md`](../second-half-ending-log.md) § Suno. Picks are filed in `clips/second-half/ending/<C|D|E>/suno/`.

## Review round 2 (22 Oct)

New AI atom `gpom-sh-end-ai-d3b`: *"It only sends one back. Me."* (D03c, straight after `-d3`). Sheet: `../../songs/second-half-ending-music.md` § `gpom-sh-end-ai-d3b`, round D (generated, not recordable; a Gemini TTS stand-in plays in the cut). Derek's `-d5` partner line is now *"Does it even work?"* (TTS); the AI answer `-d6` (last sentence) is unchanged. by: claude, **Kai to rule**.
