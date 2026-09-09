---
title: Camping — Tarquin's lines, render-ready
voice: Zubenelgenubi · profile [`profiles/tarquin-zubenelgenubi.md`](./profiles/tarquin-zubenelgenubi.md)
source: Jack's script, 2026-09-09
status: ⬜ extracted and prepared, never rendered
---

# Tarquin's lines

## 🔴 Do NOT render these in one pass — and this is the opposite of the narrator's advice

**The narrator has nine flat jabs and wants one voice state across all of them.** Tarquin does not.
His lines run **cold boardroom arrogance → the first crack → a screaming rant → a psychedelic
collapse → terror**, and one pass at one setting will flatten the four that matter most.

🔑 **The method, and it is cheap: hold identity fixed, change only the situation.**
Google defines `Sample Context` as the field that *"helps the model enter the scene you set up
naturally"* — so **Voice Direction and Scene stay byte-identical across every render** (that is his
identity, and changing it is how a character stops sounding like himself), and **only Sample Context
moves.** One field, five values.

| # | Group | Lines | Sample Context to use |
| --- | --- | --- | --- |
| **A** | **In control** — the default profile, unchanged | Scenes 1, 4, 5a, 7, 8 opener, 11 | *(the profile's own, unchanged)* |
| **B** | **The first crack** | Scene 5b | `Tarquin has just noticed something he does not want to have noticed, and is talking to himself.` |
| **C** | **The rant** | Scene 8 | `Tarquin has lost his temper in a car park and is shouting at a stranger.` |
| **D** | **The trip** | Scene 9 | `Tarquin is coming up on a powerful psychedelic and has stopped being able to perform composure.` |
| **E** | **Terror** | Scene 10 | `Tarquin has just woken up somewhere he does not recognise and is frightened.` |

⚠️ **B is the one to protect.** *"It is a tad chilly though…"* is
[the film's turn](../narration-brief.md) — the moment his own joke curdles. The default profile's
*calm, unimpressed, offhand* is **exactly wrong** for it, and a one-pass render will deliver it as
another sneer and lose the scene.

---

## 🔴 Three things in the script to settle before rendering

### 1. `Kurt Kubain's` → `Kurt Cobain's` ✅ FIXED 2026-09-09 on Jack's instruction

**It will be spoken as *Koo-bain*.** The spelling is wrong. **And it is a real, dead person's name
inside an insult about addiction** — the film's own standing rule is that
[the contempt is for the mistake, never the people](../../../marketing/the-reader.md), and this is
the one line that aims it at a person who existed. ✅ **Jack ruled 2026-09-09: fix the spelling, leave the reference.** Corrected everywhere.

### 2. The scene-8 rant breaks the beat canon rules

[`shot-list.md`](../shot-list.md) on scene 8: ***"One beat of judgement each — no prolonging. The
crack from 5d slaps shut. Cut."*** The script gives Tarquin **~40 words** against Bob's half-line
*"Fucking wank tanks, if only I could have..."*

🔑 **The symmetry is the joke.** Two men, same length, neither hearing the other. At forty words
against six, it stops being a collision and becomes **a scene of a rich man abusing a homeless man
at length** — and the audience is asked to sit in it rather than clock it and move on.
⬜ **Not fixed here. Jack's call**, and it is a script call, not a render one.

### 3. `Holy-fucking-shit` — the hyphens

Written as a clipped, hammered delivery. ⬜ **Untested what this engine does with mid-word hyphens**
— it may read them as micro-pauses, which is what is wanted, or run them together. **Try it as
written first**; if it flattens, `Holy. Fucking. Shit.` is the fallback.

## What else changed, and it is only typos

`i give you money` → `I give you money` · `a Dog` → `a dog`. **Every other word is Jack's**,
including the mixed `cannot` / `can't`, which is his rhythm.

---

## A · In control — one pass, default profile

```
Leveraged E.T.F.s. If you do not understand that, it is rather the point. Some twat is going to lose a house over this trade, and I am never going to meet them. That is not callousness. That is good business.

Twenty twenty-six. I run the largest private equity firm in the country. We buy mouldy old empty social housing, easy money really.

Rates go up a point next week. You lot are going to have a few more mates out here soon. I cannot wait for my bonus.

I booked an emergency appointment because I felt something in the car. She says empathy is not an emergency.

She says there is no amount of therapy that can help me. She says I need the most powerful psychedelic known to man. Well, that sounds splendid, to unravel the enigma that is my psyche. Yeah, I shall.

Why is he watching me park?

Twenty thirty-one, huh.
```

## B · The first crack — its own render

```
It is a tad chilly though…
```

## C · The rant — its own render

```
Get a job you fuckwit, judge me swimming there in your pool of piss, even if I give you money you'll shoot it up your arm. Look less like Kurt Cobain's skid mark, then have a go at me.
```

## D · The trip — its own render

```
I cannot bloody meditate, and I have never sat on a floor before. What am I, a dog?

Oh. Oh, that's kicked in alright!

I can't fucking handle this.

I would like to go to bed now, please.
```

## E · Terror — its own render

```
Holy-fucking-shit, what the…
```

---

## ⬜ One improvement to the profile, not applied

The Voice Direction says **`Flat delivery`** — and `flat` is
[on the banned flatness list](../../../ai-studio/README.md#-the-prompting-rules-that-are-not-in-googles-docs-livekit-2026)
that this toolkit blames for *"boring"*. **Removed from the profile file** in favour of the clause
that follows it doing the same job (*clipped consonants, heavy downward endings*).
⬜ **Unverified whether it changes the take** — the original wording is in
[`ai-studio-cast.md`](./ai-studio-cast.md) if the new one reads worse.

## To render

```bash
python3 scripts/aistudio-tts.py chunk.txt out.wav --voice Zubenelgenubi --profile docs/stories/camping/narration/profiles/tarquin-zubenelgenubi.md
```

⚠️ **Rewrite the WAV to stereo** or Premiere shows it red.


---

## ✅ ALL LINES, ONE PROMPT — Jack's request, 2026-09-09

**He asked for a single prompt with every Tarquin line in it.** Delivered below.
⚠️ **The one cost, stated once:** a single pass holds one voice state, so
*"It is a tad chilly though…"* — [the film's turn](../narration-brief.md) — will land in the same
register as the sneers around it. **If it comes back as another sneer, re-render that one line
alone** with the group-B Sample Context above. Everything else is fine in one pass.

**Every word is Jack's. One change: `Kubain` → `Cobain`.**

```
Read the following transcript based on the audio profile.

# Audio Profile
Tarquin. Deep, masculine English voice. Calm but openly unimpressed. Cold, condescending, mildly irritated by incompetence. Clipped consonants and heavy downward sentence endings. Speaks as though the conclusion was obvious some time ago. Neutral London accent, well-educated but not aristocratic. Offhand rather than warm.

## Scene:
A quiet office. He is explaining something for the second time to someone who should already have understood it.

## Sample Context:
Tarquin has just been asked a question he considers beneath him, and is answering anyway.

## Transcript:
Leveraged E.T.F.s. If you do not understand that, it is rather the point. Some twat is going to lose a house over this trade, and I am never going to meet them. That is not callousness. That is good business.

Twenty twenty-six. I run the largest private equity firm in the country. We buy mouldy old empty social housing, easy money really.

Rates go up a point next week. You lot are going to have a few more mates out here soon. I cannot wait for my bonus.

It is a tad chilly though…

I booked an emergency appointment because I felt something in the car. She says empathy is not an emergency.

She says there is no amount of therapy that can help me. She says I need the most powerful psychedelic known to man. Well, that sounds splendid, to unravel the enigma that is my psyche. Yeah, I shall.

Why is he watching me park?

Get a job you fuckwit, judge me swimming there in your pool of piss, even if i give you money you'll shoot it up your arm. Look less like Kurt Cobain's skid mark, then have a go at me.

I cannot bloody meditate, and I have never sat on a floor before. What am I, a Dog?

Oh. Oh, that's kicked in alright!

I can't fucking handle this.

I would like to go to bed now, please.

Holy-fucking-shit, what the…

Twenty thirty-one, huh.
```
