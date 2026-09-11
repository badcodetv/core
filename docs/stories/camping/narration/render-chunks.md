---
title: Camping — the narration render sheet, in chunks
status: ⬜ READY 2026-09-11 — 9 renders to do (3 narrator, 6 Tarquin). Bob is complete.
source: Jack's script (the 110-line paste). Words from kore-narrator-lines.md and tarquin-lines.md, which carry the three spelling-for-the-ear fixes
---

# Render sheet — small chunks, every take checked

## 🔴 Why the one-pass renders failed

Checked 2026-09-11 by transcribing the three takes word by word:

| Take | Pasted | Came back | Verdict |
| --- | --- | --- | --- |
| `nell.wav` (Kore) | all 9 narrator lines | 42.6s — lines 1–3, then stops mid-word in line 4 | 🔴 truncated |
| `tarquin.wav` (Zubenelgenubi) | all 14 Tarquin lines | 29.3s — T1, **skips T2 entirely**, T3, T4, stops mid-word in T5 | 🔴 truncated **and** a line dropped |
| `bob.wav` (Algenib) | all 5 Bob lines | 49.2s — all 5, clean ending | ✅ complete |

**It is not our prompt and it is not a length limit.** The output ceiling is ~10 minutes and these
stopped at 29s and 43s. It is a **known, acknowledged bug in the preview TTS model**
(`gemini-3.1-flash-tts-preview`), reported by many users and reproduced by Google, still unfixed
— full detail in [`../../../ai-studio/README.md`](../../../ai-studio/README.md#-chunk-or-whole-script--chunk-small-and-check-every-take-revised-2026-09-11).

**So: yes, chunks.** Small ones — **≤ ~40 words (~15s) per generation** — because the failure is
random, not a fixed cut-off, and a short take is cheap to re-roll.

## How to run each chunk

1. `aistudio.google.com/generate-speech` · model **`gemini-3.1-flash-tts-preview`** · Temperature **1**
2. Set the **Voice**, **Voice Direction** and **Scene** once per character — **identical for every
   chunk** (that is what keeps it the same person).
3. Per chunk, change only **Sample Context** (Tarquin only) and the **speech block**.
4. 🔑 **Listen to the last word of every take.** If it stops early, skips a line, or goes quiet,
   **just re-roll that chunk** — same boxes, press Run again.
5. Save as `camping jack/narration/new/<chunk id>.wav` (e.g. `N-1.wav`). Drop them there and a session
   can transcribe every file and confirm each word is present before you place anything.

---

## NARRATOR — voice `Kore`

### ✅ 2026-09-11, Jack's request: the whole narrator part fresh, 5 renders

Replaces the 3-render set below if used. All nine lines, so the narrator is one consistent read.

| Chunk | Lines | Words |
| --- | --- | --- |
| **N-1** | N1 — *Two thousand and eight…* | 38 |
| **N-2** | N2 + N3 — *Nice tie, mate. / Bob, a struggling middle manager…* | 32 |
| **N-3** | N4 + N5 + N6 | 17 |
| **N-4** | N7 — *Bob's mind…* | 29 |
| **N-5** | N8 + N9 | 20 |

N-1 speech block: `Two thousand and eight. Trading floors, a cesspit of madness. Tarquin here, shorting the stocks he knows will plummet; profiting off of the sinking ship. Causing economic collapse, this prick stands without a scratch.`
N-2 speech block: `Nice tie, mate.` + blank line + `Bob, a struggling middle manager, decides that driving away from the stress of the economic crash with his wife is a better idea than watching politicians squirm on TV.`
N-3, N-4 and N-5 are the old N-1, N-2 and N-3 below, word for word.

### The earlier set — 3 renders (N1–N3 kept from `nell.wav`)

N1–N3 are already fine in `nell.wav`. These redo N4 whole plus the six that were never rendered.

**→ Voice Direction** (all narrator chunks)

```
Nell, 38. The voice sits low for a woman, at the bottom of her natural speaking range, controlled and completely unhurried. She has total authority and never once raises her voice; the pressure comes out as sarcasm instead, and the more serious it gets the more precise she becomes. Her intonation stays inside a narrow band — you can hear her deciding not to let it rise. Clipped, economical, endings landed firmly. Faintly amused by almost everything and impressed by none of it. A mild, everyday north London accent, the kind nobody would remark on.
```

**→ Scene** (all narrator chunks)

```
An office above a business in Camden, late, one lamp on, explaining something to somebody who should have understood it the first time.
```

**→ Sample Context** (all narrator chunks)

```
Nell has never once had to raise her voice to be listened to, and she is not going to start now.
```

### N-1 — scenes 4, 6, 7 (N4, N5, N6)

```
He's ditched the tie, at least.

I have always found that strange.

Will that even cut it?
```

### N-2 — scene 8 (N7)

```
Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them. Four by fours are the most common vehicle in this car park.
```

### N-3 — scene 9 (N8, N9)

```
Tarquin off to do some spiritual work with drugs, of course.

Surprise, surprise he did not experience an ego death.
```

---

## TARQUIN — voice `Zubenelgenubi` (6 renders)

### ✅ 2026-09-11, Jack's request: the whole Tarquin part fresh, 11 renders, in script order

Replaces the 6-render set below. One chunk per line group, never over ~45 words, in film order.
Sample Context follows his state (the four values are the ones below).

| Chunk | Scene | Line | Sample Context |
| --- | --- | --- | --- |
| **T-1** | 1 | *Leveraged E.T.F.s…* | In control |
| **T-2** | 4 | *Twenty twenty-six…* | In control |
| **T-3** | 5 | *Rates go up a point…* | In control |
| **T-4** | 5 | *It is a tad chilly though…* | 🔑 The first crack — `Tarquin has just noticed something he does not want to have noticed, and is talking to himself.` |
| **T-5** | 7 | *I booked an emergency appointment…* | In control |
| **T-6** | 7 | *She says there is no amount of therapy…* | In control |
| **T-7** | 8 | *Why is he watching me park?* | In control |
| **T-8** | 8 | *Get a job you fuckwit…* | The rant |
| **T-9** | 9 | *I cannot bloody meditate… / Oh… / I can't… / I would like to go to bed…* | The trip |
| **T-10** | 10 | *Holy-fucking-shit, what the…* | Terror |
| **T-11** | 11 | *Twenty thirty-one, huh?* | 🔑 Acceptance — see below |

#### T-11 revised 2026-09-11 — Jack: *"huh" came out breathed; it should be a casual question, him accepting his fate*

- **`huh.` → `huh?`** A full stop on a one-syllable interjection lets it fall away as an exhale; the
  question mark lifts the pitch and makes it a spoken word. (Toolkit: *"a question mark lifts the pitch"*.)
- **Own Sample Context** — the "in control" one (*a question beneath him*) is the wrong man here:
  `Tarquin has just read the date on the newspaper and knows it is all true. The fear has gone out of him and he has accepted it. He says it casually, as a light rhetorical question to the man beside him, every word clearly voiced, with a small shrug in it.`
- ✅ **LANDED 2026-09-11 — Jack's own line: `Twenty thirty-one then huh?`** *"It worked."* The
  `then` gives the word before `huh` something to lean on, and the `?` keeps it voiced.
- ⬜ Superseded suggestion — **Jack, 2026-09-11: replace "huh" altogether.** New line: **`Twenty thirty-one, is it?`** — two
  voiced words, a built-in rising question, and it is how an English public-school man accepts
  something without admitting it. Alternatives offered: `Twenty thirty-one, eh?` · `Twenty thirty-one, then.`
  · `So it's twenty thirty-one.`
- **No tag first.** `[sighs]` and `[tired]` would add the breath back. ⬜ If still breathed, try
  `Twenty thirty-one… huh?`, then `[reluctantly] Twenty thirty-one, huh?` (`[reluctantly]` is in
  Google's own examples). Untested.

Fixes carried from `tarquin-lines.md`: `Kubain` → `Cobain` (Jack, 2026-09-09), `i` → `I`, `Dog` → `dog`.

### The earlier set — 6 renders (T1, T3, T4 kept from `tarquin.wav`)

T1, T3 and T4 are already fine in `tarquin.wav`. These are the eleven that are missing or broken.
**Voice Direction and Scene never change. Sample Context changes with his state** — the method in
[`tarquin-lines.md`](./tarquin-lines.md).

**→ Voice Direction** (all Tarquin chunks)

```
Tarquin. Deep, masculine English voice. Calm but openly unimpressed. Cold, condescending, mildly irritated by incompetence. Clipped consonants and heavy downward sentence endings. Speaks as though the conclusion was obvious some time ago. Neutral London accent, well-educated but not aristocratic. Offhand rather than warm.
```

**→ Scene** (all Tarquin chunks)

```
A quiet office. He is explaining something for the second time to someone who should already have understood it.
```

### T-1 — scenes 4, 8, 11 (T2, T7, T14) · in control

**→ Sample Context**

```
Tarquin has just been asked a question he considers beneath him, and is answering anyway.
```

**→ Speech block**

```
Twenty twenty-six. I run the largest private equity firm in the country. We buy mouldy old empty social housing, easy money really.

Why is he watching me park?

Twenty thirty-one, huh.
```

### T-2 — scene 7, first half (T5 whole) · in control

**→ Sample Context**

```
Tarquin has just been asked a question he considers beneath him, and is answering anyway.
```

**→ Speech block**

```
I booked an emergency appointment because I felt something in the car. She says empathy is not an emergency.
```

### T-3 — scene 7, second half (T6) · in control

**→ Sample Context**

```
Tarquin has just been asked a question he considers beneath him, and is answering anyway.
```

**→ Speech block**

```
She says there is no amount of therapy that can help me. She says I need the most powerful psychedelic known to man. Well, that sounds splendid, to unravel the enigma that is my psyche. Yeah, I shall.
```

### T-4 — scene 8 (T8) · the rant

**→ Sample Context**

```
Tarquin has lost his temper in a car park and is shouting at a stranger.
```

**→ Speech block**

```
Get a job you fuckwit, judge me swimming there in your pool of piss, even if I give you money you'll shoot it up your arm. Look less like Kurt Cobain's skid mark, then have a go at me.
```

### T-5 — scene 9 (T9–T12) · the trip

**→ Sample Context**

```
Tarquin is coming up on a powerful psychedelic and has stopped being able to perform composure.
```

**→ Speech block**

```
I cannot bloody meditate, and I have never sat on a floor before. What am I, a dog?

Oh. Oh, that's kicked in alright!

I can't fucking handle this.

I would like to go to bed now, please.
```

### T-6 — scene 10 (T13) · terror

**→ Sample Context**

```
Tarquin has just woken up somewhere he does not recognise and is frightened.
```

**→ Speech block**

```
Holy-fucking-shit, what the…
```

⬜ If the hyphens get run together, the fallback is `Holy. Fucking. Shit. What the…`

---

## BOB — nothing to render

✅ All five lines are complete in `bob.wav` (checked word by word 2026-09-11).

## ⚠️ Known costs of chunking

- **Voice drift between takes** is documented (~1 in 10 shifts accent or pacing). Keep every field
  byte-identical and compare each chunk against the existing take; re-roll any that sound like a
  different person.
- 🔴 **The script still has no closing line** for scene 12 — nothing here closes the film.
