---
title: The Bank Robbery — the song (2-tone ska, CANONICAL)
status: sound LOCKED 2026-10-21 (Kai); words and timing still to rework
model: v6
settings: style influence 75, weirdness 60, Variety off, Max Mode off, Personalize off, Vocal Gender unset, no Voice, Duration 180 s
workspace: bank-robbery
reference-take: br-song-ska-A-v6-w60 — https://suno.com/song/bca822dd-c443-48e3-8988-b2328ab916a7
sibling: robbery-styles.md (the eight-style sweep this came from)
---

# The Bank Robbery — the song (canonical)

🔑 **This is the sound.** Kai, 21 October 2026, on take `bca822dd`: *"I think we found our sound."*
What he loves: **a front man plus a chorus of three to five voices**, which makes it rich and
choral. The boxes below are **exactly the ones that made that take**, copied from the sweep without
a word changed. Don't "improve" them: on Suno v6 the same boxes never give the same take twice,
and nobody knows yet which words were holding the sound up.

**What happens next:** the words and the timing get reworked. The sound stays put.

## The reference take

| Take | Length | Link |
| --- | --- | --- |
| br-song-ska-A-v6-w60 ⭐ | 3:00 | https://suno.com/song/bca822dd-c443-48e3-8988-b2328ab916a7 |

Preview recording: `C:\Users\kai\Desktop\suno-recordings\br-song-ska-a-v6-w60-bca822dd.wav`.
This is a playback capture, not a download. Listening report:
[`docs/listening/log/2026-10-21-082552-br-song-ska-a-v6-w60-bca822dd.md`](../../../listening/log/2026-10-21-082552-br-song-ska-a-v6-w60-bca822dd.md).

## What the sound is (from the listen, 21 October 2026)

Heard by Gemini, compared against the boxes below, plus local measurements. It is one take,
heard by machine. Kai's ear outranks it.

- **Tempo:** 148 BPM measured (we asked for 150). Loudness −14.4 LUFS. Fairly narrow stereo, as
  on an early-80s record. Bright: the spectral centre is 3.9 kHz.
- **Front man:** British male, mid-register, dry and up front. He **toasts** (rhythmic
  chant-speaking, the Jamaican-rooted ska style) rather than sings.
- 🔑 **The gang:** it sounds like **three to five other men, shouting in unison or in octaves**. They
  do three jobs:
  1. **The intro shout:** "ROBBERY!" at 0:05.
  2. **Line-end answers inside verse 1:** "each day" 0:30, "earn that dough" 0:33,
     "nobody knows" 0:36, "FREEZING!" 0:47. Nobody wrote these answers. The model added them.
  3. **The whole chorus shouted together:** 1:18–1:31 and 2:23–2:36.
- **Band:** offbeat upstroke guitar skank, a round walking electric bass, trumpet and trombone
  stabs in harmony (horn solo at 1:44), Farfisa organ chords and swells, offbeat hi-hat with a
  rimshot snare.
- **Layout as it came out:** intro 0:00–0:26 · verse 1 0:26–1:18 · chorus 1:18–1:31 · post-chorus
  (lead + horn answers) 1:31–1:44 · horn break 1:44–1:57 · verse 2 1:57–2:23 · chorus 2:23–2:36 ·
  outro 2:36–2:57, ending on a hit.

**What most likely made the gang** (the listener's reading, not proven): the Style clause
`the hook a gang shout from the whole band`, the lyric tag `[Chorus: whole band gang shout]`, the
parenthesised `(Robbery!)` intro, and the capitals in `FREEZING!`.
🔴 **Leave `choir` in the Exclude box.** It did not stop the gang. What it probably did stop is the
gang turning into a sung church choir. That's untested, so it isn't a reason to take it out.

## Where the words fight the beat (what the rework fixes)

| Time | Line | Problem |
| --- | --- | --- |
| 0:49 | stimulus checks are next, get wrecked | "get wrecked" rushed |
| 0:58 | now let's get jiggy, just like Biggie | "just like Biggie" mumbled onto the downbeat |
| 1:36 | Institutional, dilutional, the usual | long words squeezed |
| 2:11–2:22 | It's not the standard … Hewlett and the kitchen sink | verse 2 heavily crammed |

The lines that land cleanly are short and punchy: chorus, "grandma FREEZING!", "nobody knows!".
That is the target shape. At 148 BPM, think **6–10 syllables a line**, with a word at the end of
each line the gang can shout back.

## Plan (Kai, 21 October 2026)

1. ⬜ **Kai writes the whole song:** structure first, then the words. In progress.
2. ⬜ **Claude expands the lyric guidance** on Kai's draft: syllables per line, shoutable last
   words, where the gang answers, bracket cues in the style of the take above.
3. ⬜ **Regenerate both ways, side by side:**
   - **A:** a Cover of `bca822dd` with the new lyrics, to keep this exact band.
   - **B:** fresh takes from the canonical boxes below, with only the Lyrics box changed, as the
     pair at weirdness 30/60.

## Suno prompt

Style:

```
2-tone ska, 150bpm: choppy offbeat guitar skank, a bouncing walking bassline, a stabbing trombone and trumpet horn section and a cheap Farfisa organ. A British vocal toasting the verses in rhythmic chant, the hook a gang shout from the whole band. Early-80s Coventry records, live in one room, tight and trebly, played straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, drum and bass, jungle, breakbeat, boom bap, grime, UK garage, big beat, acid, synth, distorted guitar, EDM, orchestral, choir, pop punk
```

Lyrics (exactly as generated; the rework starts from here):

```lyrics
[Intro: horn fanfare, organ, offbeat skank]
(Robbery!)

[Verse 1: toasting, rhythmic and chanted]
They say, ya can't make money from a tree
let's see, each day, not free, ay
work and get paid though, earn that dough
but where does it go? nobody knows!

means of production means a reduction
standards bleeding, land-lords needing
quantitative easing, grandma FREEZING!
stimulus checks are next, get wrecked

rent seeking? just about eating
sorry, did I interrupt your meeting?
now let's get jiggy, just like Biggie
don't get high off your own supply

this money system is insistent
on debts existence, so
don't be hating on the credit rating
or have resistance to the facts I'm stating

[Chorus: whole band gang shout]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in the basement!
Printer is burring, now what's occurring?

[Post-Chorus: lead vocal, horns answer]
There are stacks of ecstatic cash
A real homeopathic stash
Institutional, dilutional, the usual
bold, wrong and rash

[Instrumental Break: trombone solo over the skank]

[Verse 2: toasting, faster]
The real attraction becomes the distraction
the retention of the tension, between all the factions
state sponsored manipulation
delivered through the radio station

It's not the standard, propaganda, worth a couple grand-ahh
No, deep level, dancing with the devil and very well planned-ahh
Just to think, that we bust our balls to earn some ink
Then they come along with a Hewlett and the kitchen sink

[Chorus: whole band gang shout]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in the basement!
Printer is burring, now what's occurring?

[Outro: horns, organ, band stops on a hit]
```
