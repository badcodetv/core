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

**A narrator candidate, not a ruling.** The Hume Octave take is still the one that produced
*"got the voice"* — see [`voice.md`](./voice.md).

🔴 **The name collides with canon.** [`../characters/bob.md`](../characters/bob.md) casts Bob as a
**Scouse street-poet**, and the released song is built on that. This is a *narrator* who happens to
be called Bob and sounds nothing like the character. **Rename it if it wins.**

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

- ⬜ **Neither voice has read a line of the actual film.** Bob's only heard line is Google's generic
  feature-announcement sample; Tarquin's is a single test sentence
- ⬜ **Bob has never been A/B'd against the Hume take** — same chunk, both engines, same day
- ⬜ **The two men have never been heard together.** The whole point of the duet casting in
  [`../songs/camping-sheet.md`](../songs/camping-sheet.md) is that they must not blend, and that has
  only ever been tested in Suno
- ⬜ **Nothing has been rendered from `aistudio-tts.py`** — the browser is still the only route used
- ⚠️ **Preview model.** Render and archive the WAVs; do not assume either voice exists in three months
