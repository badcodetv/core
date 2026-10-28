---
title: GPOM second half E (the ending): music cue + the AI's last line
status: 🟡 stage 1, written. Nothing generated
model: v6
workspace: gpom-story
scene: docs/stories/gitpush-origin-master/scenes/second-half-e-ending/
created: 2026-10-21
---

# Scene E, the ending: music and the AI's last line

The ending may swell, but it stays restrained (Kai, 21 Oct). Chopin, not Beethoven. **No drum hit.**
The 17 Oct coda `gpom-sh2-s5` (a solo cornet, then "one single huge booming orchestral drum hit") is
**not reused**: brass and a trailer hit both break the ruling. The house format and rules are those of
[`../../songs/second-half-scene-a-music.md`](../../songs/second-half-scene-a-music.md).

## Cue list

| Cue | Under | In → out | What it does |
| --- | --- | --- | --- |
| — | e1 | 0:00 → ~0:05 | **The cut lands on sound, not music:** rain, traffic, the bus's diesel, and the phone's tiny *"...you go."*, the tail of Maddie's D16 line, which D16 cuts off after *"...Mind how"* |
| **E-coda** | e2 → e4 | in as she looks up (~0:05), out on black (~0:38) | Solo piano, then a cello. A simple, slow phrase that rises once, restrained, under the pull-back, and **leaves room for the line**: it drops to a single held piano chord under *"I made it. They didn't."*, then the cello's last phrase after *"twice"*. It ends on one low piano note that decays into black. |

### `gpom-sh-e-coda` — piano and cello, one restrained rise, one low last note (duration 40)

Settings: v6 · Style Influence 75 · Weirdness **pair 30 / 60** · Duration 40 · instrumental.

Style:

```
A short, slow, tender ending for solo piano and solo cello, in the manner of the close of a Chopin nocturne. The piano begins alone with a simple, quiet phrase over soft rain-like stillness; the cello enters and the melody rises once into a gentle, restrained swell, warm and hopeful but never grand, then falls back to a single held piano chord with space around it. A last short cello phrase, then the piece ends on one low, soft piano note left to ring and decay into silence.
```

Exclude styles:

```
vocals, singing, choir, humming, drums, percussion, timpani, drum hit, impact, boom, beat, pulse, brass, horns, cornet, brass band, full orchestra, string section, synth, electronic, pad, epic, heroic, action, trailer, bombastic, cinematic swell, fortissimo, fanfare, march
```

## The AI's last line (one atom)

**`gpom-sh-end-ai-e1`** · beat e3 · frame E03.

The line was picked from three drafts (scene `brief.md` § The AI's last line; **Kai to rule**):

> *I made it. They didn't. Don't make me come back twice.*

The **narrator treatment**: the Suno Voice **`badcode newsreader`**, dry, **unfiltered**, full range and
close. This is the first time in the second half that he is not coming through Maddie's speaker. The
settings are those of `gpom-sh-a-boss` (v6, SI 50, AI 65, weirdness **pair 25 / 10**, Personalize,
Variety and Max off, workspace `gpom-story`), duration 40.

The same take also carries the re-aimed variant **`gpom-sh-end-ai-e1b`** (brief review, finding 8; **Kai to rule** which plays): *I made it. They didn't. Don't let the same lot make me come back twice.* It costs nothing extra: it is a second section in the same take, cut apart in the edit.

Style:

```
Spoken word narration, voice only. One calm British male voice, a newsreader, unhurried, dry and certain, speaking quietly and close, as if to one person, late at night. No music at all: no score, no bed, no instruments, only his voice and quiet silence between the words. A short pause after each sentence; the second sentence quieter; the last sentence plain and level, never dramatic. Close-mic'd in a dead, dry voiceover booth, no reverb, his voice right at the front. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, dramatic, trailer voice, music, instrumental, score, soundtrack, background music, underscore, strings, piano, cello, violin, orchestra, brass, synth, pads, drone, ambient, drums, percussion, beat, reverb
```

Lyrics:

```lyrics
[Spoken, dry, close, unhurried]
I made it.

[Spoken, quieter]
They didn't.

[Spoken, plain, level]
Don't make me come back twice.

[Pause]

[Spoken, dry, close, unhurried]
I made it.

[Spoken, quieter]
They didn't.

[Spoken, plain, level]
Don't let the same lot make me come back twice.
[End]
```

## Suno budget for the three scenes (cap 200 credits)

| What | Creates | Credits |
| --- | --- | --- |
| AI takes: `gpom-sh-end-ai-C`, `-D`, `-e1`, each a pair (w25 / w10) | 6 | 60 |
| Music: `gpom-sh-c-walk`, `gpom-sh-d-room`, `gpom-sh-d-cross`, `gpom-sh-e-coda`, each a pair (w30 / w60) | 8 | 80 |
| **Planned** | 14 | **140** |
| Reserve for retakes (single atoms, then music) | ≤ 6 | ≤ 60 |

Each cue is **one** atom, not the two bold atoms of scene A, to stay under the cap. If a cue's pair
misses, the second atom is written then.

## Round log

New rounds go at the top.

- **21 Oct 2026:** generated from the live sheet [`../../songs/second-half-ending-music.md`](../../songs/second-half-ending-music.md) (rounds A and B, 150 credits for all three scenes). Takes, links, picks and reasons are there and in [`../second-half-ending-log.md`](../second-half-ending-log.md) § Suno. Picks are filed in `clips/second-half/ending/<C|D|E>/suno/`.
