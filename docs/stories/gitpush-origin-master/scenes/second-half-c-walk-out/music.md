---
title: GPOM second half C (the walk out): music cues + the AI's lines
status: 🟡 stage 1, written. Nothing generated
model: v6
workspace: gpom-story
scene: docs/stories/gitpush-origin-master/scenes/second-half-c-walk-out/
created: 2026-10-21
---

# Scene C, the walk out: music and the AI's lines

**Kai's brief for the music (21 Oct 2026, scene A notes):** sparse and intimate. A solo cello, a solo
violin, a little piano. Chopin, not Beethoven's Fifth, and never an action movie. This sheet uses the
house format of [`../../songs/second-half-scene-a-music.md`](../../songs/second-half-scene-a-music.md):
generate verbatim from the blocks; Personalize, Variety and Max Mode off; never download; record only
the pick (in this run Claude picks and records, `suno.mts record`).

**Not reused:** the 17 Oct cues `gpom-sh2-s4` (the crossing) and `gpom-sh2-hundred` (the brass-band
hymn). S4 is an "epic orchestral and drum and bass hybrid" and the hymn is a brass band. Both break
Kai's 21 Oct ruling.

## Cue list

| Cue | Under | In → out | What it does |
| --- | --- | --- | --- |
| — | c1 Off the step | 0:00 → 0:07 | **No score.** Wind at the door and birdsong. The step exchange plays dry, so the trust lands without help. |
| **C-walk** | c2 → c5 | in on the first walkers into daylight (~0:07), out on the reveal (~0:58) | A lone violin in open air, hesitant, then the piano joins as the line crosses the downs. Hopeful but wary. It thins to **one low held cello note** under the building's reveal. |
| — | c5 → c6 | the reveal → the end | That cello note holds under *"I tried to make it nice"*, then stops dead on *"Mind the step."* The scene ends on room tone at the door: a low hum and the wind. |

Duration target: **60 s** (the cue runs ~51 s in the cut; it is trimmed in the mix, and its ending is
the held cello note).

### `gpom-sh-c-walk` — lone violin and piano, open air

Settings: v6 · Style Influence 75 · Weirdness **pair 30 / 60** · Duration 60 · instrumental · Voice none.

Style:

```
A slow, tender piece for solo violin and piano, like a Chopin nocturne heard outdoors. The violin plays alone at first, a hesitant, searching melody with long breaths between phrases, as if stepping out into daylight after a long time underground. Then a soft piano enters underneath with a slow, rocking left hand, and the melody grows a little warmer and more hopeful, never loud. Near the end everything thins away until only one low cello note is left, held and still, unresolved. Recorded close and intimate, natural and unhurried, rubato.
```

Exclude styles:

```
vocals, singing, choir, humming, drums, percussion, timpani, beat, pulse, groove, brass, horns, brass band, full orchestra, string section, synth, electronic, pad, epic, heroic, action, trailer, bombastic, cinematic swell, march, major key fanfare
```

## The AI's lines (Suno atoms)

The AI is the Suno Voice **`badcode newsreader`**, made dry (Kai's ruling). The settings are those of
`gpom-sh-a-boss`: v6, Style Influence 50, Audio Influence 65, weirdness **pair 25 / 10**, Personalize,
Variety and Max off, workspace `gpom-story`. In this scene he speaks **through Maddie's speaker**: the
small-speaker filter is applied in the mix, and her beacon pulses on his words.

Each line is its own atom: one id, one line, the unit for a retake. **To save credits, the run makes
one take per scene with every line of the scene as its own section**, cut apart in the edit, as
`gpom-sh-a-boss` did. Only an atom that comes back wrong is re-run on its own.

| Atom | Beat · frame | Line | Cue |
| --- | --- | --- | --- |
| `gpom-sh-end-ai-c1` | c5 · C06 | *I tried to make it nice.* | `[Spoken, a little shy, hopeful]` |
| `gpom-sh-end-ai-c2` | c6 · C07 | *Come in. Mind the step.* | `[Spoken, warm, precise, a host at his own door]` |

### `gpom-sh-end-ai-C` — the scene's take (both atoms), duration 30

Style:

```
Spoken word narration, voice only. One calm British male voice, a newsreader, unhurried and wry, speaking quietly to a small group of people in front of him. No music at all: no score, no bed, no instruments, only his voice and quiet silence between the lines. His delivery follows the cues. Close-mic'd in a dead, dry voiceover booth, no reverb, his voice loud and right at the front. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, a little shy, hopeful]
I tried to make it nice.

[Spoken, warm, precise, a host at his own door]
Come in. ... Mind the step.
[End]
```

## Round log

New rounds go at the top.

- **21 Oct 2026:** generated from the live sheet [`../../songs/second-half-ending-music.md`](../../songs/second-half-ending-music.md) (rounds A and B, 150 credits for all three scenes). Takes, links, picks and reasons are there and in [`../second-half-ending-log.md`](../second-half-ending-log.md) § Suno. Picks are filed in `clips/second-half/ending/<C|D|E>/suno/`.
