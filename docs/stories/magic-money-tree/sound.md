# The Magic Money Tree — sound

> The sound for this story only. Read before any Suno or voice prompt (suno-prompt,
> suno-automation, variations, scene-timeline voicing). Rules: [`docs/stories/STYLE.md`](../STYLE.md).

**Status:**
- **The song "Magic Money Tree":** EXPLORING — lyrics in progress (Kai writes every bar); a jump-up D&B
  Style box is written in the sheet's front matter but no take is recorded. On 1 October 2026 Kai took on
  *"finishing the song and choosing its style"*, so the genre is open again.
- **Documentary narration:** EXPLORING — two routes on paper, neither generated: a scored Suno narration
  (Kai, 29 Sept; [`songs/narration.md`](./songs/narration.md), round 1 is a six-way style test) and, after
  the 1 Oct recut, a *"incredibly sarcastic"* narrator *"voiced with the Gemini voice API"* interviewing a
  soldier. Which one is not ruled.
- **Money For Something narrator:** LOCKED — AI Studio `Zubenelgenubi`, accent setting British (Brixton),
  nothing else in the boxes (Jack, 3–4 Oct 2026).
- **Money For Something on-camera voices (Oct episodes):** LOCKED — four Flow custom voices (*"I like the
  voices"*, Jack). **Host v2 (balaclava, from 25 Oct):** EMPTY — text-to-speech, voice not yet chosen.

## In one paragraph

Nothing about this story's sound is settled except Money For Something's narrator. The documentary wants a
**minimal documentary score that never announces itself** under an English narrator (Kai, 29 Sept), and,
after the recut, a **sarcastic narrator and a real-sounding old soldier**, the pair being the comedy (*"I'd
do a Ray Winstone on it, make it real"*, Kai). The song was written as **bouncy comedic jump-up drum &
bass** with a cheeky UK rapper, and its joke is *"paper comes from a tree"*. Money For Something is read
**straight**, Naked-Gun-flat, by a bored man from the future.

## Tracks

### "Magic Money Tree" — the song (EXPLORING)

Sheet: [`songs/magic-money-tree.md`](./songs/magic-money-tree.md). Shape ruled by Kai 2026-08-26: four
verses, **money / shake / starve / plant**; V1 locked; hook = the concession, *"you can't SHAKE it — you
PLANT it"*. Flow reference: *Don't Get High On Your Own Supply*
(<https://www.youtube.com/watch?v=OJM8yJTn_I0>). The liquid / spoken-word rework is deleted (Kai,
2026-08-18): *"do not resurrect it"*.

Style as written in the sheet's front matter (unproven — no take recorded; the genre is Kai's to re-choose):

```
Jump-up drum and bass, 172 BPM, bouncy and comedic. Hyperactive and cheeky, tongue-in-cheek energy, big playful drops. Wobbling gurgly jump-up bassline, chopped breakbeats, bright stabs, air-horn and rewind FX. A single UK comedic rapper — fast double-time flow, animated and witty, cheeky British accent, spoken-word punchlines landing on the beat, theatrical and sardonic. Clean punchy mix, club-ready, energetic. Satirical, fun, fast-talking.
```

```
liquid dnb, dark neurofunk, boom bap, lo-fi hip hop, pop, autotune, clean sung melody, soft female vocal, American accent, acoustic guitar, jazz, orchestral, ballad, slow tempo, melancholy, ambient
```

Voices: a rapper and a prim politician (*"there is no magic money tree"* bookends it). The 08:58 meeting
on 1 Oct floated spoken word, medieval or a bar song; both liked the bar song. Not ruled.

### Documentary narration — the Suno route (EXPLORING, nothing generated)

[`songs/narration.md`](./songs/narration.md), first draft 2026-09-29: voice and score in one Suno take, ten
parts, workspace `mmt-narration`. Proposed settings — **borrowed from GPOM — a candidate, not inherited; Kai to rule (2026-10-29 audit)**; nothing measured on this film:
v6 · Style Influence 50 · Audio Influence 65 with a Voice · Weirdness 25 · Variety, Max Mode, Personalize
off. Round 1 = P1 six ways: three palettes × with/without GPOM's saved Voice `badcode newsreader`. The
template, verbatim:

```
Spoken word narration for a British documentary. One calm English male narrator, warm, dry and unhurried, reading slowly with natural pauses, always clearly on top of the music. Underneath him, a minimal documentary score, mixed far back and low: {{PALETTE}}. His delivery follows the story: {{ARC}}. Close-mic'd and dry, his voice loud and right at the front of the mix, the music always well behind him and never rising over a word. Sparse, quiet, patient, never dramatic, never busy. {{ENDING}} He speaks only the words written.
```

Palettes to test: **A** felt piano · **B** English pastoral string quartet with solo cello · **C** a distant
colliery brass band chorale. Exclude, verbatim:

```
singing, sung vocals, humming, chanting, choir, rap, autotune, female vocals, synth, electronic, drum kit, drum machine, percussion, breakbeat, beat, groove, steady pulse, epic, cinematic trailer, bombastic, loud orchestra, dense orchestration, swelling climax, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, music louder than the voice, music over the vocal
```

⚠ Written before the 1 Oct recut: the words are the 15-minute storyboard's, and the narrator was calm and
warm, not sarcastic.

## Narration / voices

**Documentary, after the recut (1 Oct):** an *"incredibly sarcastic"* narrator voiced with AI Studio (Kai
*"mentions the West Country robot voice"*), interviewing **the soldier**, played real. Neither voice is
built. See [`direction-2026-10-01.md`](./direction-2026-10-01.md).
⚠️ **Flag for Kai (2026-10-29 audit):** the "West Country robot voice" is most likely GPOM's Maddie, the
West Country delivery bot (Gemini TTS `Aoede`, Bristol — `../gitpush-origin-master/sound.md`; the match is
an inference). Floated here, not ruled. Using it would put GPOM's voice on MMT's narrator; Kai to decide, and if
it is taken, write its settings here as MMT's own.

**Money For Something — the narrator** (over real clips): AI Studio, voice **`Zubenelgenubi`**, accent
setting **British (Brixton)**, nothing else in the boxes (Jack's pick, [`money-for-something-RESUME.md`](./money-for-something-RESUME.md)).
Reference take: `money for something\narrator\NARRATOR-VOICE-reference-zubenelgenubi-brixton.wav` (Jack's
disk). One take in ten is reported to drift; compare against the reference. (The Bank Robbery used this
narrator for its first cuts.)

**Money For Something — on camera** (Flow custom voices, project `cb27208c`, 3 Oct; performance texts in
[`money-for-something.md`](./money-for-something.md) §"The cast and their voices in Flow"):

| Character | Preset |
| --- | --- |
| The Host | `Sadachbia` — a man in his forties with a soft Irish accent, dry and rumpled |
| The British Soldier | `Algenib` |
| The German Soldier | `Alnilam` |
| The Politician | `Umbriel` |
| Podcast Host / Water Boss / HS2 Reporter (2026 episode) | `Fenrir` / `Schedar` / `Zubenelgenubi` |

In Frames mode the Host's saved voice is not bound and the accent wandered (American three times,
Australian once, Scottish once); Jack: *"the voice is fine"* (4 Oct).

**Host v2** (balaclava, from 25 Oct): text-to-speech over stock movement clips, mouth never seen. *"Worth a
short voice round in AI Studio (deadpan, unhurried, British) before the lines are recorded"*
([`money-for-something-2026-10-26-format.md`](./money-for-something-2026-10-26-format.md)). Not run.

## Rules for this story

- **Money For Something is read straight** — *"ridiculous jokes said with a straight face"* (Jack). No
  smile, no wink, no studio laughter (Jack ruled out audience laughter, 4 Oct). One sincere line at the end.
  Jack writes the jokes ([`money-for-something-voice.md`](./money-for-something-voice.md)).
- **A Flow line ending on a short tag** ("Moving on.") can be taken as a song cue; close the prompt with
  "No music and no singing".
- **Documentary score: minimal, never over a word**, never dramatic (Kai, 29 Sept: *"not GPOM's drama"*).
- **Song: Kai writes every bar**; never "we printed the war"; "Keynesian" is never a lyric; Keynes's own
  words are a spoken tag only, never the chant ([`songs/magic-money-tree.md`](./songs/magic-money-tree.md)
  §Guardrails).
- **Narration words change only with Kai**; record only when Kai says "record"; listen only when he asks.
- Pronunciations to listen for: Keynes (*rains*), Ruhr (`Roor`), Aneurin Bevan, Mone (`Moan`).

## Never

- Archive audio from the Crown films (not free).
- The liquid / spoken-word version of the song.
- Music louder than the narrator.

## History

- **2026-08-05 re-founding**: the song's two-versions policy (Version A evolving, Version B locked) — dead
  since 2026-08-18.
- **Song shapes**: the 08-21 ring → the 08-22 banknote arc → 08-26 shake / starve / plant (current).
- **Narration**: the fable treatments' narrator and tree voices — archived in
  [`archive/2026-09-11-superseded/`](./archive/2026-09-11-superseded/README.md).
- **Money For Something voices** — the voice plan and first takes: [`money-for-something.md`](./money-for-something.md)
  §"The room reference and the voice plan".
