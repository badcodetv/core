---
title: Camping — the Google AI Studio voice cast
engine: Google AI Studio · gemini-3.1-flash-tts-preview
status: 🟡 two profiles built and kept. Neither has been run against the real script
built: 2026-09-08
narrator_sheet: ./voice.md
toolkit: ../../../ai-studio/README.md
---

# Camping — the AI Studio voice cast

> **What this is:** the **verbatim box sets** for every camping voice built in Google AI Studio,
> so that "just make him sound like that again" is a copy-paste and not an afternoon.
> The *argument* about who narrates lives in [`voice.md`](./voice.md); this file is the store.

**Two men so far.** Both are prebuilt Google voices driven by a written profile — no cloning, no
reference audio, nothing uploaded.

| | Voice | Profile | Built |
|---|---|---|---|
| **Bob** | `Algenib` | 47, gravelly, worn down, southern English | 2026-09-08 — a **narrator** candidate |
| **Tarquin** | `Zubenelgenubi` | cold, condescending, neutral London | 2026-09-08 |

## The shared setup — the same for both

| | |
|---|---|
| **Where** | `aistudio.google.com/generate-speech` → **Composer** |
| **Account** | the Ultra account, `jacktttt330@…` — the one Flow runs on |
| **Model** | `gemini-3.1-flash-tts-preview` (Run settings) · ⚠️ **Preview, not GA** |
| **Voice** | Speaker settings → **Current voice** |
| **Output** | `audio/L16;rate=24000`, **mono** — 🔴 rewrite to stereo or Premiere shows it red |
| **Config** | `temperature 1` · `response_modalities: ["audio"]` |
| ✅ **Licence** | **cleared 2026-09-08** — free tier, commercial use, £0, no training on UK prompts. [`../../../ai-studio/README.md`](../../../ai-studio/README.md) § THE LICENCE |
| ⚠️ **Watermark** | every take carries **SynthID**, and it survives trimming and compression. Fine — we disclose AI anyway |

**To render from the command line rather than the browser:**

```
export GEMINI_API_KEY=...
python3 scripts/aistudio-tts.py chunk.txt out.wav --voice Algenib --profile bob.md
```

[`scripts/aistudio-tts.py`](../../../../scripts/aistudio-tts.py) is AI Studio's own **Get code**
export with its four faults fixed — one file per streamed chunk, the Transcript field holding the
profile, mono output, and a literal `ENTER_FILE_NAME_0`. ⬜ **Its API path is still unrun.**

---

## 🎙️ Bob — `Algenib`

## ✅ RESOLVED 2026-09-09 — this is BOB, the character. Not a narrator candidate.

**Jack: *"the Algenib build is a narrator is Bob."*** ✅ **And
[`../characters/bob.md`](../characters/bob.md) already said so** — *"Speaking voice built
2026-09-08, Google AI Studio, prebuilt voice `Algenib`"* — which this page's own caveat contradicted
for a day. **The character sheet was right.**

🔑 **It stopped being a narrator candidate the moment [Nell won](#-nell--the-narrator-ruled-2026-09-09-voice-kore-first-take).**
The role it was auditioning for is filled, and the voice it was built with fits the man it is named
after. ✅ **So the three-voice cast is complete:** Nell `Kore` · Bob `Algenib` · Tarquin
`Zubenelgenubi`.

> ### ⬜ One thing still disagrees, and it is the accent
>
> [`bob.md`](../characters/bob.md)'s `voice:` field reads ***"Scouse, weathered street-poet —
> adenoidal Merseyside drawl, softened 'ck', rising sing-song intonation, lo-fi phone texture"*** —
> and **that is the register the released song is built on.** This build asks for the opposite:
> *"neutral southern English accent as heard in Reading or Guildford, no Cockney vowels."*
>
> ⬜ **They may legitimately be different assets** — a stylised singing register in a track and a
> speaking voice in a film are not the same job. **But an accent is not a register**, and Scouse
> versus Reading is the same man in two places.
>
> 🔑 **If Scouse is wanted, the move is a different VOICE NAME, not a rewritten direction.**
> That is the lesson [Nell just paid for](#-nell--the-narrator-ruled-2026-09-09-voice-kore-first-take)
> — three rounds of prose contributed nothing and one voice change did it. **Writing *Scouse* into
> Algenib's Voice Direction is the exact failure we spent today diagnosing.**
>
> ⬜ **Jack's call:** leave Bob southern in the film and let the song be its own register, or hunt a
> voice that carries Merseyside so the release and the film agree.

**Composer → Voice Direction:**

```
Bob, 47. Deep, gravelly, low chest tone, slightly rough from years of smoking. Restrained and inward. Intelligent, cynical, worn down. Delivery sits under the material rather than selling it. Natural conversational rhythm, short pauses, firm downward endings. Neutral southern English accent as heard in Reading or Guildford, faint London edge, no Cockney vowels or slang.
```

**Composer → Scene:**

```
A small voiceover booth, late at night. No audience. He's reading from a page he half agrees with.
```

**Composer → Sample Context:**

```
Bob has narrated this kind of story many times before and is no longer surprised by any of it.
```

**Composer → Speech block** — 🔑 the regression line. Read it back after any change to check Bob
still sounds like Bob:

```
Hi there! We're introducing a new feature where I can read this aloud, in a natural, human-like voice.
```

**As one blob**, for the API or any single-box interface — the `DIRECTOR'S NOTES` shape:

```
# AUDIO PROFILE: Bob, 47
A man who has seen how it turns out and stopped expecting better.

## THE SCENE
A small voiceover booth, late at night. No audience. He's reading from a page he half agrees with.

### DIRECTOR'S NOTES
Style: Deep, gravelly, low chest tone, slightly rough from years of smoking. Restrained and inward. Intelligent, cynical, worn down. Delivery sits under the material rather than selling it.
Pacing: Natural conversational rhythm. Short pauses. Firm downward endings on every sentence.
Accent: Neutral southern English as heard in Reading or Guildford, faint London edge, no Cockney vowels or slang.

### SAMPLE CONTEXT
Bob has narrated this kind of story many times before and is no longer surprised by any of it.

#### TRANSCRIPT (speak only the following aloud):
[script here]
```

---

## 🎙️ Tarquin — `Zubenelgenubi`

**The posh half of the duet, as a speaking voice.** Consistent with canon:
[`../characters/tarquin.md`](../characters/tarquin.md) casts him posh London and sneering, and the
song's second verse is *"plummy BBC English, precise and unhurried, talking down at you from a wide
room."* 🔑 **This profile gets there without the word "posh"** — it describes a *situation* (second
explanation, to someone who should have understood) rather than a class, which is the same trick
that made `v-pub` work in the song sheet: **describe the performance, not the attitude.**

**Composer → Voice Direction:**

```
Tarquin. Deep, masculine English voice. Calm but openly unimpressed. Cold, condescending, mildly irritated by incompetence. Flat delivery with clipped consonants and heavy downward sentence endings. Speaks as though the conclusion was obvious some time ago. Neutral London accent, well-educated but not aristocratic. Offhand rather than warm.
```

**Composer → Scene:**

```
A quiet office. He is explaining something for the second time to someone who should already have understood it.
```

**Composer → Sample Context:**

```
Tarquin has just been asked a question he considers beneath him, and is answering anyway.
```

**Composer → Speech block** — 🔑 the regression line:

```
It was always going to end this way. Everyone involved knew that.
```

🔴 **The code export DROPPED the last sentence of the Voice Direction.** The Composer field ends
*"…not aristocratic. **Offhand rather than warm.**"*; the exported `# Audio Profile` block ends at
*"not aristocratic."* — the final clause is gone. ⬜ **Unverified whether that changed the take**,
but the two are not the same prompt. **The Composer text above is the authority**; the blob below
has the sentence restored.

**As one blob**, in Google's own export shape — 🔑 note this is a *different structure* to Bob's
`DIRECTOR'S NOTES` blob above. Google emits this one. **Which performs better is untested.**

```
Read the following transcript based on the audio profile.

# Audio Profile
Tarquin. Deep, masculine English voice. Calm but openly unimpressed. Cold, condescending, mildly irritated by incompetence. Flat delivery with clipped consonants and heavy downward sentence endings. Speaks as though the conclusion was obvious some time ago. Neutral London accent, well-educated but not aristocratic. Offhand rather than warm.

## Scene:
A quiet office. He is explaining something for the second time to someone who should already have understood it.

## Sample Context:
Tarquin has just been asked a question he considers beneath him, and is answering anyway.

## Transcript:
[script here]
```

---

## ⬜ What nobody has done yet

- ✅ **Both voices now have a script to read.** [`three-voice-script.md`](./three-voice-script.md),
  written 2026-09-09 — Bob in past tense, Tarquin in present, the narrator reduced to bookends plus
  four interventions. **It is the first thing either voice has been given that is actually from the
  film.** Unread, unrendered.
- ⬜ **The therapist is reported, not heard** — Tarquin repeats her verdict in the new script, which
  is funnier and removes the third-voice dependency below.
- 🔴 **There is no therapist voice, and Scene 7 may now need one.** The therapist was recast female
  2026-09-09 ([`../style.md`](../style.md)) and the
  [`7c-y2`](../prompts.md#7c-y2--the-therapist-explains-a-feeling-mouths-moving--video--written-2026-09-09-unrun)
  clip has her **visibly speaking** — which commits the film to a recorded voice for her, because
  the mouth in the picture has to belong to somebody. Scene 7's punchline is hers, so spending it
  on a character rather than the narrator is plausibly an upgrade. **Spec:** a Black British woman,
  early fifties, London, warm and unhurried, completely unbothered, delivering a verdict as calmly
  as a change of diet. Built the same way as the two below — a prebuilt Google voice plus a written
  profile. ⬜ **Only needed if `7c-y2` beats `7c-y`; the pause version needs no new voice.**

- ⬜ **Neither voice has read a line of the actual film.** Bob's only heard line is Google's generic
  feature-announcement sample; Tarquin's is a single test sentence
- ⬜ **Bob has never been A/B'd against the Hume take** — same chunk, both engines, same day
- ⬜ **The two men have never been heard together.** The whole point of the duet casting in
  [`../songs/camping-sheet.md`](../songs/camping-sheet.md) is that they must not blend, and that has
  only ever been tested in Suno
- ⬜ **Nothing has been rendered from `aistudio-tts.py`** — the browser is still the only route used
- ⚠️ **Preview model.** Render and archive the WAVs; do not assume either voice exists in three months

---

## 🎙️ THE NARRATOR — three candidates, built 2026-09-09

**Why a new voice at all.** Jack rewrote the narration 2026-09-09
([`three-voice-script.md`](./three-voice-script.md)) and the narrator's job changed shape:

| | Old script | New script |
|---|---|---|
| Longest narrator run | a full paragraph | **two sentences** |
| Typical line | narration | **a one-line jab** — *"Nice tie, mate."* · *"He's ditched the tie, at least."* · *"Will that even cut it?"* · *"Surprise, surprise he did not experience an ego death."* |
| Register | telling the story | **commenting on it, often addressed at Tarquin** |

🔴 **So the ruled Hume Octave voice is now the wrong instrument, and this is the whole argument for
rebuilding.** [`voice.md`](./voice.md) describes it as *"pulp-horror-novelist narration: portentous,
gravelly, hammered emphasis, total sincerity."* That is a large instrument built for long portentous
paragraphs. **A portentous read murders "Nice tie, mate"** — the comedy in this script is timing and
throwaway, not weight. *(The Hume take is not deleted; it is the wrong fit for these words.)*

### The constraints every candidate below obeys

| Rule | Source |
|---|---|
| 🔴 **Northern is dropped.** Ask for an accent the vendor documents | [ruled 2026-09-04](../../../ai-studio/README.md#-ruled-2026-09-04--northern-is-dropped-ask-for-an-accent-the-model-already-does) |
| 🔴 **Ask for pressure, never flatness.** *Banked, contained, clipped* — never *flat, quiet, no rush* | [the anger ruling](../../../ai-studio/README.md#-ruled-2026-09-04--the-missing-ingredient-was-anger-and-it-is-the-cure-for-boring) |
| **Pitch as pitch, not as archetype.** No *"deep gravelly"* next to *"never an announcer"* | the self-cancelling pair |
| **No field sits neutral** — a neutral field votes for the model's default, which is General American | the box audit |
| **One name in every field** | the documented top mistake |
| **A different voice family from `Algenib` and `Zubenelgenubi`** | Bob and Tarquin are already cast; three voices in one film must be separable by ear |

⬜ **Only six of the sixteen male voices have published descriptors** (`Algenib` gravelly/low,
`Charon` American ~160wpm ~152Hz, `Puck` upbeat, `Fenrir` excitable, `Zubenelgenubi` casual,
`Iapetus` clear). **Every voice suggestion below is an audition pair, not a pick.**

⚠️ **Not proposed: the corporate-induction inversion.** It is the obvious fourth idea and
[Jack ruled it out 2026-09-04](../../../ai-studio/README.md#-the-register-swing--the-induction-video-narrator)
— *"not very BadCode."* Recorded so it does not come back.

---

### 🥇 Candidate A — **DEZ**, the man at the end of the bar who is cleverer than you

**The pitch.** South-east London, forties. Not grand, not grave — **quick**. He is not narrating a
film, he is giving you the running commentary, and the jokes land because he throws them away rather
than sells them. *"Nice tie, mate"* is his native register.

🔑 **Brixton is the safest British ask on this engine** — it is named in Google's own worked example
and in the documented accent set — **and it is native to a film about the NatWest floor, the Shard
and a Waitrose car park.** The other two voices are a neutral southern man and a posh one; a London
working voice completes the class triangle without a single line of exposition.

**Audition:** `Iapetus` (Clear) and `Achird`. ⬜ Undescribed voices are a lottery — run both.

```
Composer → Voice Direction
```
```
Dez, 44, from Brixton in south London. Pitched in the middle of his natural speaking range, dry and slightly nasal, never grand. Quick-witted and impatient. Anger banked down and held still under everything he says. Sarcasm used as a weapon rather than as a joke. He throws his best lines away instead of landing them, and clips the ends of sentences short. South-east London accent, working class, no Cockney caricature.
```

```
Composer → Scene
```
```
The back of a south London pub on a wet Tuesday afternoon, half a lager gone, telling it to one person who has not asked.
```

```
Composer → Sample Context
```
```
Dez is a Londoner who has watched the money leave his own city for thirty years and has run out of ways to be surprised by it.
```

```
Composer → Speech block — the regression line
```
```
Nice tie, mate.
```
🔑 **That is the regression line on purpose.** It is four words and it is the hardest thing in the
script to read: too much weight and it is a threat, too little and it is nothing. **If a candidate
cannot land it, the rest does not matter.**

---

### 🥈 Candidate B — **NEV**, furious and refusing to show it

**The pitch.** The [anger ruling](../../../ai-studio/README.md#-ruled-2026-09-04--the-missing-ingredient-was-anger-and-it-is-the-cure-for-boring)
made into a whole character rather than a note. Dez is *amused*; **Nev is angry**, and every joke in
the script is the thing stopping him raising his voice. Same words, completely different film.

🔑 **This is the candidate that best fits the new scene 6.** Bob's line — *"work camps, euthanasia,
sectioned… I just wanted a sandwich"* — is followed by the narrator saying only ***"I have always
found that strange."*** **From an amused voice that is a shrug. From a contained one it is the
angriest line in the film**, and it is the script's emotional hinge.

**Audition:** `Orus` and `Umbriel`. ⬜ Both undescribed; if either comes back grave rather than
tight, jump family rather than rewriting the notes.

```
Composer → Voice Direction
```
```
Nev, 51, from Brixton in south London. Pitched low, at the bottom of his natural speaking range, tight rather than resonant. Controlled and compressed. He is angry the whole time and never once raises his voice; the pressure comes out as sarcasm instead. Tightens under pressure rather than getting louder. Short clipped sentences, hard consonants, firm downward endings. South-east London accent, working class.
```

```
Composer → Scene
```
```
A south London kitchen at two in the morning, the radio off, explaining something to somebody who should already understand it.
```

```
Composer → Sample Context
```
```
Nev has watched this happen to people he knows and has decided that losing his temper about it would let everybody off.
```

```
Composer → Speech block — the regression line
```
```
I have always found that strange.
```
**Different regression line to Dez's, deliberately.** Nev's risk is not the throwaway joke, it is
**the sincere line reading as sentimental**. If *"strange"* comes back soft, the anger is not banked
underneath it.

---

### 🥉 Candidate C — **RAY**, General American — and this one is a strategy, not a voice

**The pitch.** [The engine's native default](../../../ai-studio/README.md#-ruled-2026-09-04--northern-is-dropped-ask-for-an-accent-the-model-already-does)
and therefore the least likely to fight us, **and Karen's narrator is already cast as General
American with a faint Western ease — and Karen worked.**

🔴 **Which makes this the same call Jack raised on 2026-09-09** about whether one entity may wear
more than one voice ([`voice.md`](./voice.md) § the open ruling). **Choosing Ray collapses that
question: camping and Karen converge on one house narrator**, and BadCode gets the recognition
asset a serialised run actually runs on. Choosing Dez or Nev keeps them separate and commits us to
*fixed grammar, variable timbre*.

⚠️ **The cost, stated plainly.** An American voice narrating a film aimed at
[a working-class UK reader](../../../marketing/the-reader.md), about a British trading floor and a
Waitrose car park, is a register mismatch the film has to carry. **It may read as distance — which
is arguably right for a narrator that is not human — or it may read as *not for me*, which is the
one thing this film cannot afford.**

**Audition:** `Charon` — the measured American male, and the only voice in the set with published
numbers.

```
Composer → Voice Direction
```
```
Ray, 50, American, plain General American with no regional colour. Pitched in the middle of his natural speaking range, even and unhurried. Detached and precise. Anger banked down and held still under everything he says; sarcasm used as a weapon rather than as a joke. He states things rather than performing them, and does not lift at the ends of sentences.
```

```
Composer → Scene
```
```
An empty American control room, long after everybody else has gone home, reading a report about another country out loud to nobody.
```

```
Composer → Sample Context
```
```
Ray has been over these events many times and is no longer looking for a different outcome.
```

```
Composer → Speech block — the regression line
```
```
Surprise, surprise. He did not experience an ego death.
```

---

### How to run the audition — and it is cheap

1. **Two lines, not the script.** *"Nice tie, mate."* and *"I have always found that strange."*
   Those two carry the whole range: throwaway contempt and banked sincerity. Everything else in the
   part sits between them.
2. **One field at a time from the winning box set** — the discipline that produced
   [Bob's build](#-bob--algenib).
3. **Then the box audit** — count accent-coded tokens per field before blaming the prose.
4. ⚠️ **Rewrite the WAV to stereo** or Premiere shows it red.
5. **Deliver in one pass**, test in chunks.

⬜ **Not built. Three box sets, no takes.**

---

## 🥇 RULED 2026-09-09 by Jack — **DEZ** is the narrator. The optimised build.

**Candidate A picked.** Below is the box set rebuilt against
[LiveKit's rules](../../../ai-studio/README.md#-the-prompting-rules-that-are-not-in-googles-docs-livekit-2026)
and a fresh web pass, **which found three faults in the first draft of it.**

### 🔴 What the optimisation pass changed, and two of them apply to Bob's build too

| Fault | Fix | Applies to |
| --- | --- | --- |
| 🔴 **`DIRECTOR'S NOTES` as a section label** | LiveKit is explicit: **multi-word headers and apostrophes fail.** Use **`### PERFORMANCE`** and **`### CONTEXT`** | ⚠️ **Also [Bob's blob](#-bob--algenib) and [Tarquin's](#-tarquin--zubenelgenubi)** — both carry it verbatim. They worked anyway, so the label costs something nobody measured rather than breaking outright. **Fix on next touch** |
| 🔴 **No "do not speak the directions" preamble** | *"Synthesize speech for the performance defined below. Speak ONLY the lines under TRANSCRIPT."* Load-bearing, and the fresh web pass confirms it independently — Google's own guidance says to *"add a clear preamble instructing the model to synthesize speech, and explicitly label where the actual spoken transcript begins"* | ⚠️ Same |
| 🔴 **"throws his best lines away"** | Reads as *low energy*, which is the [flatness family that produced "boring"](../../../ai-studio/README.md#-ruled-2026-09-04--the-missing-ingredient-was-anger-and-it-is-the-cure-for-boring). Replaced with **"lands his best lines sideways, on the way to something else"** — same behaviour, described as motion instead of absence | this build |

### 🔴 And one fault is in the SCRIPT, not the box

**LiveKit: *"period-separated fragments sound choppy."*** Jack's opening is
*"2008 trading floors, a cesspit of madness. Tarquin here, shorting the stocks… Causing economic
collapse, this prick stands without a scratch."*

🔑 **Punctuation is the music, and it is a separate cause of "boring" from the direction.** The rule
set: **commas** between clauses, **periods only at real sentence endings**, **em-dashes** for
micro-pauses, **ellipses** (one or two per utterance) for a trailing pause. **Re-punctuating costs
nothing and changes the read more than another rewrite of the profile will.**

### 🆕 The Voice Library applet — the audition route nobody has used

**Found in the 2026-09-09 web pass** `[vendor]`: AI Studio ships a **Voice Library applet** for
trying speech styles and voices before building anything. ⬜ **Untried.** It is the cheapest
possible way to settle `Iapetus` vs `Achird` — audition there before spending a build.

---

### The four Composer fields — paste-ready

**Where:** [aistudio.google.com/generate-speech](https://aistudio.google.com/generate-speech) →
**Composer** · Model `gemini-3.1-flash-tts-preview` · Temperature 1 ·
**Voice: audition `Iapetus` first, then `Achird`** — change nothing else between the two.

**Composer → Voice Direction**

```
Dez, 44, a Londoner from Brixton. Pitched in the middle of his natural speaking range, dry and a little nasal. Quick-witted, impatient, and angry underneath in a way he keeps clamped down. Sarcasm is the weapon rather than the joke — he lands his best lines sideways, on the way to something else, and clips his sentence endings short. Tightens under pressure rather than raising his voice. South-east London accent as heard in Brixton, working class.
```

**Composer → Scene**

```
The back room of a Brixton pub on a wet Tuesday afternoon, half a lager gone, telling it to one person who did not ask.
```

**Composer → Sample Context**

```
Dez has watched the money leave his own city for thirty years and has run out of ways to be surprised by it. The man he is describing works in the City of London and has never once had to worry.
```

**Composer → Speech block — the audition text**

```
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

Nice tie, mate.
```

🔑 **Why this text and not the script.** It carries the two hardest things in the part: **a long
clause-chained run** (which is what the re-punctuation buys) and **a four-word throwaway jab**.
*"Nice tie, mate"* is the real test — too much weight and it is a threat, too little and it is
nothing. **If a voice cannot land it, nothing else matters.**

⬜ **No inline tags in the audition.** Custom emotional adjectives are
[the weak kind](../../../ai-studio/README.md#-the-prompting-rules-that-are-not-in-googles-docs-livekit-2026);
add from the proven set (`[sarcastic]`, `[serious]`, `[sighs]`) only if a specific line needs it.

### The box audit — every field votes, none is neutral

| Field | Accent-coded tokens | Verdict |
| --- | --- | --- |
| **Voice Direction** | `Londoner`, `Brixton` ×2, `south-east London`, `working class` | ✅ Strong |
| **Scene** | `Brixton pub`, `lager` | ✅ Spent |
| **Sample Context** | `his own city`, `City of London` | ✅ Spent |
| **Speech block** | `mate`, `prick`-register vocabulary | ✅ Spent |

**And no self-cancelling pair:** pitch is stated as *"the middle of his natural speaking range"* —
a range, not an archetype — so there is no `deep` for a `never boomy` to fight.

### As one blob, for `scripts/aistudio-tts.py` or any single-box interface

**Headers rebuilt to LiveKit's shape — no apostrophes, single-word section labels.**

```
Synthesize speech for the performance defined below. Speak ONLY the lines under TRANSCRIPT.

# AUDIO PROFILE: Dez, 44
A Londoner who has watched the money leave his own city and has run out of ways to be surprised by it.

## SCENE
The back room of a Brixton pub on a wet Tuesday afternoon, half a lager gone, telling it to one person who did not ask.

### PERFORMANCE
Style: Pitched in the middle of his natural speaking range, dry and a little nasal. Quick-witted, impatient, and angry underneath in a way he keeps clamped down. Sarcasm is the weapon rather than the joke.
Pacing: Lands his best lines sideways, on the way to something else. Clips his sentence endings short. Tightens under pressure rather than raising his voice.
Accent: South-east London as heard in Brixton, working class.

### CONTEXT
The man Dez is describing works in the City of London and has never once had to worry.

#### TRANSCRIPT
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

Nice tie, mate.
```

### If it comes back wrong

1. **Wrong accent** → the fault is almost never the prose. **Jump voice family** rather than rewording — `Iapetus` → `Achird` → `Puck`.
2. **Boring** → check for flatness words first, then **re-punctuate the transcript**. Both are documented causes and neither is a profile problem.
3. **Directions spoken aloud** → the preamble is missing or the section boundary is vague.
4. ⚠️ **Rewrite the WAV to stereo** or Premiere shows it red.

⬜ **Not built. Box set only.**

---

## 🥈 **NEV** — the contained-anger build, optimised 2026-09-09

**Jack asked for candidate B built out too.** Same part, same words, **different film**: Dez is
amused, Nev is angry and every joke in the script is the thing stopping him raising his voice.

🔑 **Nev is the [anger ruling](../../../ai-studio/README.md#-ruled-2026-09-04--the-missing-ingredient-was-anger-and-it-is-the-cure-for-boring)
made into a character rather than a note.** *"Deadpan is a lid on something, not an absence of it."*
Dez's contempt is entertainment; Nev's is a decision he is making every second not to shout.

### 🔴 The one clause that decides this build

**Contained anger needs a *narrow* melody — and every word for that is banned.** `flat`, `level`,
`monotone`, `never getting louder` are all
[flatness-inducing](../../../ai-studio/README.md#-three-dials-that-are-easy-to-confuse--placement-melody-and-accent-strength),
and they are exactly what produced *"boring"* the first time.

> 🔑 **The trick is to describe restraint as an action rather than an absence.**
> *"His intonation stays inside a narrow band — you can hear him deciding not to let it rise."*
> **A decision is a force. Flatness is a vacuum.** Same move as Dez's *"lands his lines sideways"*
> in place of *"throws them away."*

### 🆕 What the 2026-09-09 web pass added

| Finding | Status |
| --- | --- |
| 🔑 **The emotion tags have intensity granularity** — *"subtle differences between emotions like `[angry]` and `[furious]`"* `[community]` | ⬜ **Testable, and a possible exception to LiveKit's rule** that custom emotional adjectives are weak. `[angry]` may be *trained* rather than custom. **Worth one A/B on a single line — not on the whole script** |
| ⚠️ **A documented restrained-emotion example reads *"speak softly, with restrained sadness and a slower pace"*** `[community]` | 🔴 **Do not copy it.** `softly` and `slower pace` are two of [LiveKit's banned flatness words](../../../ai-studio/README.md#-the-prompting-rules-that-are-not-in-googles-docs-livekit-2026), and our own *"boring"* post-mortem is `[confirmed]` on our own material. **The construction *"restrained X"* is the transferable part; the delivery words around it are not** |
| **Classify the emotional register first, then pick tags** — never a universal template | Matches our own discipline |

### 🔴 Correction to the DEZ entry — the audition is not blind

I said only six of the sixteen voices have published descriptors. **That is true of this repo, not
of the UI.** [The picker labels every voice](../../../ai-studio/README.md#-three-dials-that-are-easy-to-confuse--placement-melody-and-accent-strength)
— *"Charon · Informative · Lower pitch"*, *"Achird · Friendly · Lower middle pitch"*. **Read
`Orus` and `Umbriel` in the picker before auditioning either.**

🔑 **And it matters more here than for Dez**, because `voice_name` owns timbre: *"if a take is not
deep enough, change the voice, not the words."* Nev needs low placement, and **that is a voice
choice, not a prose one.**

---

### The four Composer fields — paste-ready

**Where:** [aistudio.google.com/generate-speech](https://aistudio.google.com/generate-speech) →
**Composer** · `gemini-3.1-flash-tts-preview` · Temperature 1 ·
**Voice: read the pitch labels, then run `Orus`, then `Umbriel`** — change nothing else between them.

**Composer → Voice Direction**

```
Nev, 51, a Londoner from Brixton. The voice sits low, at the bottom of his natural speaking range, tight rather than resonant. His intonation stays inside a narrow band — you can hear him deciding not to let it rise. He is angry the whole time and never once raises his voice; the pressure comes out as sarcasm instead. Tightens under pressure. Short clauses, hard consonants, endings landed firmly rather than trailed. South-east London accent as heard in Brixton, working class.
```

**Composer → Scene**

```
A kitchen in south London at two in the morning, the radio off, explaining something to somebody who should have understood it the first time.
```

**Composer → Sample Context**

```
Nev has watched this happen to people he grew up with in Brixton, and has decided that losing his temper about it would let everybody off.
```

**Composer → Speech block — the audition text**

```
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

I have always found that strange.
```

🔑 **Different audition text from Dez's, and deliberately.** Dez's risk is the throwaway jab;
**Nev's risk is the sincere line coming back sentimental.** *"I have always found that strange"* is
[the script's emotional hinge](./three-voice-script.md) — it answers Bob's *work camps, euthanasia,
I just wanted a sandwich* — and **from a contained voice it is the angriest line in the film. If it
comes back soft, the anger is not banked underneath it and the build has failed.**

⚠️ It also has to follow a long clause-chained run without the run flattening it, which is why the
opener is attached rather than auditioning the line alone.

### The box audit

| Field | Accent-coded | Verdict |
| --- | --- | --- |
| **Voice Direction** | `Londoner`, `Brixton` ×2, `south-east London`, `working class` | ✅ Strong |
| **Scene** | `south London` | ✅ Spent |
| **Sample Context** | `Brixton` | ✅ Spent |
| **Speech block** | register vocabulary | ✅ Spent |

**Dials named separately**, per the three-dials rule: **placement** = *"low, at the bottom of his
natural speaking range"* (a range, not `deep`); **melody** = *"inside a narrow band… deciding not to
let it rise"* (a decision, not `flat`); **accent strength** = a named town, no phonemes.
**No self-cancelling pair.**

### As one blob

```
Synthesize speech for the performance defined below. Speak ONLY the lines under TRANSCRIPT.

# AUDIO PROFILE: Nev, 51
A Londoner who is angry about this and has decided that losing his temper would let everybody off.

## SCENE
A kitchen in south London at two in the morning, the radio off, explaining something to somebody who should have understood it the first time.

### PERFORMANCE
Style: The voice sits low, at the bottom of his natural speaking range, tight rather than resonant. He is angry the whole time and never once raises his voice; the pressure comes out as sarcasm instead.
Melody: Intonation stays inside a narrow band. You can hear him deciding not to let it rise.
Pacing: Short clauses. Hard consonants. Endings landed firmly rather than trailed. Tightens under pressure.
Accent: South-east London as heard in Brixton, working class.

### CONTEXT
Nev has watched this happen to people he grew up with in Brixton.

#### TRANSCRIPT
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

I have always found that strange.
```

### How to judge Dez against Nev

**Run both on the same two lines and ask one question:** *does the sarcasm sound like entertainment
or like restraint?*

| | Dez wins if | Nev wins if |
| --- | --- | --- |
| *"Nice tie, mate."* | it lands as a shrug on the way past | it lands as the last thing he says before he stops talking |
| *"I have always found that strange."* | it reads as a wry aside | it reads as the angriest line in the film |

🔴 **They are not interchangeable and this is not a coin toss.** Dez makes the film funnier; **Nev
makes it hurt**, and it is Nev that fits the new scene 6. ⬜ Jack's call by ear.

⬜ **Not built. Box set only.**

---

## 🥇 **NELL** — the narrator, female, accent fixed. Built 2026-09-09.

**Two changes from [NEV](#-nev--the-contained-anger-build-optimised-2026-09-09): the speaker is a
woman (Jack, 2026-09-09), and the accent is asked for completely differently.** Same character —
angry, contained, every joke the thing stopping her raising her voice.

### 🔴 THE FIX — copy an accent, do not prompt one

**Jack: *"the accent on all of these prompts is ridiculous and over the top like a cartoon."***
Every box set so far has taken a **General-American-default voice and tried to talk it into London
with prose**. 🔑 **And this repo's oldest standing finding on the whole narration problem says not
to:**

> ***Every route that works COPIES an accent. None invent one.***

**The voice picker searches 5,000+ voices with filters for Language · Accent · Gender · Age · Style**
([the UI is the truth, not the 30 in the docs](../../../ai-studio/README.md#the-ui-map--observed-live-2026-09-04)).
**Filter Gender: Female + Accent: English, and audition voices that already sound like her.**

🔑 **Then the prose stops carrying the accent and only has to carry the performance** — which is
the half prose is good at, and **a prompted accent is the definition of a performed one.**

⬜ **If a filtered voice already has the accent, delete the accent clause from the Voice Direction
entirely.** It is there below only as a fallback for a neutral voice.
**Named fallbacks if the filter disappoints:** `Kore`, `Achernar`.

### 🔴 And re-roll twice before changing a word

[~1 in 10 generations shifts accent or pacing on identical inputs](../../../ai-studio/README.md#-ruled-2026-09-09--the-accent-is-ridiculous-and-over-the-top-like-a-cartoon-five-causes)
`[community]`. **Some cartoon takes are a lottery.** Every previous *"too over the top"* note in
this file may have been diagnosed against a single sample.

### What was cut from Nev, and why

| Cut | Reason |
| --- | --- |
| 🔴 **`working class`** | A class **archetype**, and archetypes summon caricatures — the same mechanism as `deep` → movie-trailer read. It has no measurement to fall back on. **Class belongs in the words of the script, not in a box** |
| 🔴 **`hard consonants`** | A **phonetic instruction** in disguise, and this toolkit already records that *"every 'too over the top' note traces to these"* |
| 🔴 **`Brixton` ×2, `south-east London`, `Londoner`** | The accent was voted for in **all four boxes**. [The box audit is a balance rule, not a maximise rule](../../../ai-studio/README.md#-1-the-big-one--the-box-audit-is-a-balance-rule-not-a-maximise-rule) — four accent votes read as *performed*, the same way four light sources read as *lit* |
| 🔴 **The pub Scene** | *"A Brixton pub, half a lager gone, telling it to one person"* is a **casting brief**, and a casting brief gets an actor. A Scene should set a mood, not cast a character actor |
| ✅ **Added: the not-performing clause** | *"She is not doing an accent. This is simply how she talks and she has never thought about it."* Never once said in any previous build |

**Accent now votes twice, not four times:** once properly in Voice Direction, once quietly as a
place in the Scene. Sample Context is deliberately accent-free.

---

### The four Composer fields — paste-ready

**Where:** [aistudio.google.com/generate-speech](https://aistudio.google.com/generate-speech) →
**Composer** · `gemini-3.1-flash-tts-preview` · Temperature 1
🥇 **Voice: `Gacrux`** — researched 2026-09-09, the only voice of the thirty that is female AND
low-pitched, and Google describes it as *mature and experienced*. **A/B it against `Kore`** (firm and
confident, higher) — firmness may carry restraint better than lowness does. Full shortlist and the
evidence: [`../../../ai-studio/README.md`](../../../ai-studio/README.md#-the-female-voice-shortlist--researched-2026-09-09).

**Composer → Voice Direction**

```
Nell, 51. The voice sits low, at the bottom of her natural speaking range, tight rather than resonant. Her intonation stays inside a narrow band — you can hear her deciding not to let it rise. She is angry the whole time and never once raises her voice; the pressure comes out as sarcasm instead. Tightens under pressure. Short clauses, endings landed firmly rather than trailed. A mild, everyday south London accent, the kind nobody would remark on. She is not doing an accent — this is simply how she talks, and she has never thought about it.
```

⬜ **Delete the last two sentences if the chosen voice already carries the accent.**

**Composer → Scene**

```
A kitchen in London at two in the morning, the radio off, explaining something to somebody who should have understood it the first time.
```

**Composer → Sample Context**

```
Nell has watched this happen to people she grew up with, and has decided that losing her temper about it would let everybody off.
```

**Composer → Speech block — the audition text**

```
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

I have always found that strange.
```

🔑 **The second line is the whole test.** It is
[the script's emotional hinge](./three-voice-script.md) — it answers Bob's *work camps, euthanasia,
I just wanted a sandwich* — and **from a contained voice it is the angriest line in the film.
If it comes back soft, the anger is not banked underneath it.** The long run above it is attached
so the run does not flatten it.

### As one blob

```
Synthesize speech for the performance defined below. Speak ONLY the lines under TRANSCRIPT.

# AUDIO PROFILE: Nell, 51
A woman who is angry about this and has decided that losing her temper would let everybody off.

## SCENE
A kitchen in London at two in the morning, the radio off, explaining something to somebody who should have understood it the first time.

### PERFORMANCE
Style: The voice sits low, at the bottom of her natural speaking range, tight rather than resonant. She is angry the whole time and never once raises her voice; the pressure comes out as sarcasm instead.
Melody: Intonation stays inside a narrow band. You can hear her deciding not to let it rise.
Pacing: Short clauses. Endings landed firmly rather than trailed. Tightens under pressure.
Accent: A mild, everyday south London accent, the kind nobody would remark on. She is not doing an accent, this is simply how she talks.

### CONTEXT
Nell has watched this happen to people she grew up with.

#### TRANSCRIPT
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

I have always found that strange.
```

### If it still sounds like a cartoon

**In this order, and change one thing at a time:**

1. **Re-roll twice.** ~1 in 10 shifts on identical inputs.
2. **Change the voice, not the words.** `voice_name` owns timbre and accent-by-filter beats
   accent-by-prose every time.
3. **Delete the accent clause entirely** and let the filtered voice carry it alone.
4. **Then, and only then**, touch the Voice Direction — and remove a clause rather than adding one.

⬜ **Not built. Box set only.** ⚠️ Rewrite the WAV to stereo or Premiere shows it red.

### ⬜ Knock-on: a female narrator changes the cast balance

The film would then be **a woman narrating two men**, with the therapist also a woman
([recast 2026-09-09](../style.md)). ⬜ **Not a problem, and possibly an improvement** — the two
people in the film with any perspective on Tarquin are both women, and neither is a love interest
or a victim. **Worth noticing rather than ruling on.**

---

## ✅ **NELL — THE NARRATOR. RULED 2026-09-09.** Voice `Kore`, first take.

**Jack: *"the Kore one works."*** 🔑 **After roughly fifteen rounds across two sessions and four
engines, the camping narrator exists — and she is a woman.**

### What actually did it, in order of contribution

1. 🥇 **The right voice.** `voice_name` owns timbre, and `Kore` (*firm and confident*) was reached
   by **following the reference rather than the adjective**: the brief said *51 and low* and picked
   `Gacrux`; the reference said *in charge and not old* and picked `Kore`. ✅ **Authority comes
   from control, not from depth** — that A/B is now settled.
2. 🥈 **One bounded accent vote instead of four.** *"A mild, everyday north London accent, the kind
   nobody would remark on"*, once, plus `Camden` in the Scene. **No class marker, no phonetics, no
   iconic place, no negation.**
3. 🥉 **A described reference, never named** — the technique that also produced the only other
   *"that worked"* on this engine.

⚠️ **What was NOT needed:** Voice Design, cloning, billing, the Accent filter, or another rewrite
of the Voice Direction. **The last three rounds of prose edits contributed nothing that the voice
name did not.**

### 🔴 Consequences

- **This challenges the [Hume Octave ruling](./voice.md)** of 2026-09-04, which stands *"until a
  challenger is run against the real script."* ⬜ **One has now been run — and it is female, which
  the Hume take is not.** Jack's call whether Nell replaces it outright or Hume stays as the
  fallback.
- 🔑 **The three-voice cast exists for the first time:** **Nell** `Kore` (narrator) ·
  **Tarquin** `Zubenelgenubi` · and ⬜ **Bob — still missing.**
- 🔴 **Bob the character has no voice.** The `Algenib` build [filed above](#-bob--algenib) is a
  *narrator* candidate that happens to be called Bob and, by its own note, *"sounds nothing like
  the character"* — canon casts him as a **Scouse street-poet**.
  **That is the next voice job**, and it is the last one the script needs.
- ⬜ **The therapist is still reported, not heard** — [7c-y2](../prompts.md) has Tarquin repeat her
  verdict, so no fourth voice is owed unless Jack wants her on screen speaking.

✅ **The exact working prompt is saved** at
[`profiles/nell-kore.md`](./profiles/nell-kore.md) — AI Studio's own `Get code` export, de-indented,
with `## Transcript:` left open. **Render with one command:**

```bash
python3 scripts/aistudio-tts.py chunk.txt out.wav --voice Kore --profile docs/stories/camping/narration/profiles/nell-kore.md
```

🔴 **And that export corrected the blob format used everywhere else in this file.** AI Studio puts
the whole performance direction in **one paragraph under `# Audio Profile`** — there is no
`### PERFORMANCE`, no `### CONTEXT`, and no `Style / Pacing / Accent` sub-labels. Those were our
invention and are unconfirmed. See
[the real blob shape](../../../ai-studio/README.md#-confirmed-2026-09-09--the-real-blob-shape-taken-from-ai-studios-own-export).

**The winning box set is below, unchanged.**

---

## 🥇 **NELL v2** — built from Jack's reference, 2026-09-09

**Jack: *"try to make the main woman's voice from the Gentlemen."*** ✅ **It is the right reference
and it sharpens the brief in two ways the earlier builds had guessed at.**

🔴 **The reference is described and never named.** [The unnamed-reference
technique](../../../ai-studio/README.md#-the-unnamed-reference-technique--carried-over-and-it-still-applies)
— *"name a real person to yourself, never to the engine. Cloning-of-real-people filters trip on
names, and descriptive traits steer better anyway."* **No actor, no character, no title in any
box.**

### 🔑 What the research changed — and it flips the voice pick

| Finding `[community]` | What it changes |
| --- | --- |
| 🔑 **The performer built the accent from her friends' mums** — north London, Camden, working-class women she actually grew up around | 🔴 **The accent moves from south London to NORTH London**, and more importantly: **it is an accent assembled from ordinary women rather than performed from a stage tradition.** That is the exact register these builds have been failing to get — *"the kind nobody would remark on"* is not an approximation of the reference, **it is the reference's own method** |
| **The character is early-to-mid thirties, not fifty** — *"an absolute boss… cool-headed charisma… commands every space she enters"* | 🔴 **Nell drops from 51 to 38**, and that **flips the voice recommendation** |

> ### 🔴 The voice pick changes: `Kore`, not `Gacrux`
>
> [Yesterday's shortlist](../../../ai-studio/README.md#-the-female-voice-shortlist--researched-2026-09-09)
> picked **`Gacrux` (mature and experienced)** because the brief said *51* and *low*. **The
> reference is neither.** It is **firm and in charge and not old** — which is Google's own
> descriptor for **`Kore`: firm and confident.**
>
> ✅ **This also settles the A/B that shortlist left open** — *does firmness carry restraint better
> than lowness does?* The reference answers it: **the authority comes from control, not from
> depth.** `Gacrux` drops to the alternate.

### ⚠️ And a correction to what I said last round

I called the prose lever *"exhausted."* **That was too absolute.** The 2026-09-04 build that
produced *"that worked"* used **exactly this method** — one described reference, one named town,
no phonemes. **What failed today was my prompts** — [four boxes stacking the accent, a class
marker, and phonetic instructions in disguise](../../../ai-studio/README.md#-ruled-2026-09-09--the-accent-is-ridiculous-and-over-the-top-like-a-cartoon-five-causes)
— not the technique. This build uses the one that has actually landed.

---

### The four Composer fields — paste-ready

**Where:** [aistudio.google.com/generate-speech](https://aistudio.google.com/generate-speech) →
**Composer** · `gemini-3.1-flash-tts-preview` · Temperature 1 · 🥇 **Voice `Kore`** (alternate:
`Gacrux`) · **re-roll twice before changing a word.**

**Composer → Voice Direction**

```
Nell, 38. The voice sits low for a woman, at the bottom of her natural speaking range, controlled and completely unhurried. She has total authority and never once raises her voice; the pressure comes out as sarcasm instead, and the more serious it gets the more precise she becomes. Her intonation stays inside a narrow band — you can hear her deciding not to let it rise. Clipped, economical, endings landed firmly. Faintly amused by almost everything and impressed by none of it. A mild, everyday north London accent, the kind nobody would remark on.
```

**Composer → Scene**

```
An office above a business in Camden, late, one lamp on, explaining something to somebody who should have understood it the first time.
```

**Composer → Sample Context**

```
Nell has never once had to raise her voice to be listened to, and she is not going to start now.
```

**Composer → Speech block — the audition text**

```
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

I have always found that strange.
```

### The box audit — two votes, not four

| Field | Accent-coded | Verdict |
| --- | --- | --- |
| **Voice Direction** | `north London` ×1, and bounded by *mild / everyday / nobody would remark on* | ✅ One strong, bounded vote |
| **Scene** | `Camden` | ✅ One quiet vote — a place, no accent adjective attached |
| **Sample Context** | none | ✅ **Deliberately clean.** Its job is the *disposition*, and it is the line that carries the reference |
| **Speech block** | register vocabulary only | ✅ |

**No class marker. No phonetics. No iconic place. No negation** — *"the kind nobody would remark
on"* bounds strength without ever using the word *accent* in a refusal.

### As one blob

```
Synthesize speech for the performance defined below. Speak ONLY the lines under TRANSCRIPT.

# AUDIO PROFILE: Nell, 38
A woman who runs things and has never once had to raise her voice to be listened to.

## SCENE
An office above a business in Camden, late, one lamp on, explaining something to somebody who should have understood it the first time.

### PERFORMANCE
Style: The voice sits low for a woman, at the bottom of her natural speaking range, controlled and completely unhurried. Total authority. She never raises her voice; the pressure comes out as sarcasm instead, and the more serious it gets the more precise she becomes. Faintly amused by almost everything and impressed by none of it.
Melody: Intonation stays inside a narrow band. You can hear her deciding not to let it rise.
Pacing: Clipped and economical. Endings landed firmly.
Accent: A mild, everyday north London accent, the kind nobody would remark on.

### CONTEXT
Nell is not going to start raising her voice now.

#### TRANSCRIPT
Two thousand and eight, trading floors — a cesspit of madness. Tarquin here, shorting the ship he knows is sinking, profiting off the lot of them, and walking out of an economic collapse without a scratch on him.

I have always found that strange.
```

### ⬜ If the accent is still wrong — the order, and it is short

1. **Re-roll twice.** ~1 in 10 shifts on identical inputs.
2. **`Gacrux` instead of `Kore`.** Voice before words, always.
3. **Delete the accent line entirely** and hear what the voice does unassisted. If that is the best
   take, the accent was never the prose's job.
4. ⬜ **Then the picker's Accent filter**, which
   [nobody has looked at since 2026-09-04](../../../ai-studio/README.md#-the-female-voice-shortlist--researched-2026-09-09)
   and which is the last untried thing.

⬜ **Not built.** ⚠️ Rewrite the WAV to stereo.
