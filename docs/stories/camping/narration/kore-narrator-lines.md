---
title: Camping — the narrator's lines, render-ready for Kore
voice: Kore · profile [`profiles/nell-kore.md`](./profiles/nell-kore.md)
source: Jack's script, 2026-09-09
status: ⬜ extracted and prepared, never rendered
---

# The narrator's lines — all nine

**Extracted from Jack's 2026-09-09 script.** Every `NARRATOR {FLAT}` line, in film order, nothing
else. Bob's and Tarquin's lines are separate renders on their own voices.

## 🔑 Render all nine in ONE pass, not nine

⚠️ **~1 in 10 generations shifts accent or pacing on identical inputs.** Nine separate renders is
**nine chances to get a different narrator**; one pass is one voice state across the whole film.
**The blank lines between utterances give clean tops and tails to cut on** — every line lands in a
different scene anyway, so they get separated in Premiere regardless.

## What was changed from Jack's script, and it is only three things

**Every word is his. Three spelling-for-the-ear fixes, all forced:**

| Was | Now | Why |
| --- | --- | --- |
| `2008 trading floors` | `Two thousand and eight. Trading floors,` | 🔴 **Forced.** *"2008 trading floors"* spoken straight is **a quantity** — two thousand and eight of them. The period is what stops the number attaching to the noun |
| `4 by 4's` | `Four by fours` | Digits and an apostrophe-s do not survive TTS |
| `"wank tanks"` | `wank tanks` | The quotation marks add nothing spoken, and quotes are a known hazard on the sibling video engine. No reason to carry them |

⬜ **Not re-punctuated further.** [Period-separated fragments read choppy](../../../ai-studio/README.md#-the-prompting-rules-that-are-not-in-googles-docs-livekit-2026)
and several of these lines are exactly that — **but they are Jack's rhythm and the jabs may want
the chop.** Hear it first; the fix is commas and em-dashes and it costs one re-render.

## ⬜ The name inside the prompt stays "Nell"

Jack: *"let's just call the narrator Kore for now."* ✅ **In conversation, yes.** **Inside the
prompt, leave it as Nell** — [that build landed first take](./ai-studio-cast.md#-nell--the-narrator-ruled-2026-09-09-voice-kore-first-take)
and the character name is a live field the model reads. **Do not change a variable in a prompt that
just worked**, and *Kore* as a persona name inside a prompt whose `voice_name` is also `Kore` is an
untested collision for no gain.

---

## The transcript — paste under `## Transcript:`

```
Two thousand and eight. Trading floors, a cesspit of madness. Tarquin here, shorting the stocks he knows will plummet; profiting off of the sinking ship. Causing economic collapse, this prick stands without a scratch.

Nice tie, mate.

Bob, a struggling middle manager, decides that driving away from the stress of the economic crash with his wife is a better idea than watching politicians squirm on TV.

He's ditched the tie, at least.

I have always found that strange.

Will that even cut it?

Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them. Four by fours are the most common vehicle in this car park.

Tarquin off to do some spiritual work with drugs, of course.

Surprise, surprise he did not experience an ego death.
```

## Where each line lands

| # | Scene | Line |
| --- | --- | --- |
| 1 | **1** · trading floor | *Two thousand and eight. Trading floors…* |
| 2 | **1** · trading floor | *Nice tie, mate.* |
| 3 | **2** · the car | *Bob, a struggling middle manager…* |
| 4 | **4** · the Shard | *He's ditched the tie, at least.* |
| 5 | **6** · outside Waitrose | *I have always found that strange.* |
| 6 | **7** · therapy | *Will that even cut it?* |
| 7 | **8** · the car park | *Bob's mind is thrown into a tailspin…* |
| 8 | **9** · Wales | *Tarquin off to do some spiritual work with drugs…* |
| 9 | **9** · Wales | *Surprise, surprise he did not experience an ego death.* |

🔇 **Scenes 3, 5, 10 and 11 have no narrator line** — 3 and the scene-5 hold are
[silent by canon](../narration-brief.md); 10 and 11 are carried by Tarquin and Bob.

⚠️ **Scene 12 has no narrator line either, and the film currently has no last word.**
[The brief is explicit](../narration-brief.md): *the `12d` tilt ends exactly on the last word —
write backwards from it.* 🔴 **Nothing in this script closes the film.**

## To render

```bash
export GEMINI_API_KEY=...
python3 scripts/aistudio-tts.py chunk.txt out.wav --voice Kore --profile docs/stories/camping/narration/profiles/nell-kore.md
```

⚠️ **Rewrite the WAV to stereo** or Premiere shows it red.
