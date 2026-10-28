# Dialogue and morph sweep — 2026-10-09

Web pass run because the director named three faults in The Bank Robbery cut 5: props that change mid-clip,
British characters who sound American, and two characters who sound like one. It reports only what
[`2026-10-08-anti-slop-sweep.md`](./2026-10-08-anti-slop-sweep.md) does not already hold.

**Nothing here was tested by us** except the one item marked `[observed]`. Pages were read through a summarising
fetch tool, so re-open a page before building a hard rule on its exact wording. Reddit could not be fetched.

Tiers: **OFFICIAL** (a Google page) · **HOST** (a model host's doc) · **PRACTITIONER** · **ANECDOTE** ·
**UNVERIFIED**.

## 1. Props that change mid-clip

- **No Google source addresses prop permanence.** The Omni model card lists only "generating scenes with
  complex motion" and "maintaining complete consistency throughout edits". OFFICIAL.
  <https://deepmind.google/models/model-cards/gemini-omni-flash/>
- "Everything you describe is something the model may re-render, so describe only the change"; compound
  instructions "break consistency about twice as often". PRACTITIONER, no method shown (Morphic, Omni 1.1).
  <https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide>
- Write holds as positive states: "maintain static background geometry throughout the shot"; name the regions
  that stay still. PRACTITIONER, vendor (Atlas Cloud, Omni 1.1, 2026-09-04).
  <https://www.atlascloud.ai/blog/tips/gemini-omni-flash-1.1-image-to-video>
- Occlusion is a risk ("avoid extreme pose changes or occlusion"). A hand closing round a prop is occlusion:
  that reading is ours. UNVERIFIED.
- A pinned end frame hides incompatible geometry with "a fade, a rapid morph, an unexpected cut". PRACTITIONER,
  Veo 3.1. Agrees with our never-pin-an-end-frame rule. <https://flowveo3.com/posts/veo-3-1-first-last-frame-guide>
- Nobody has measured whether shorter clips morph less. Omni takes 3 to 10 s (HOST, Runware).
- `[observed, n=7 shots, one film, 2026-10-09]` In The Bank Robbery cut 5 every prop morph sat in the middle of
  the clip, at or just after the main action (an egg flip, a mug lifted, a remote pressed, keys swinging). The
  first second and the last two seconds of each clip were clean, and were enough to re-cut from. **So before
  re-making a morphing clip, look for its settled tail.**

## 2. Accent

- 🔴 **Voices attach to Ingredients generations only.** "You can add voice references only to video generations
  that use ingredients. For all other kinds of generations, you'll get an error." OFFICIAL.
  <https://support.google.com/flow/answer/16894016?hl=en> Already in `omni-flash.md`; repeated because every
  Bank Robbery talking clip was made in Frames. Whether a Character's own voice travels into Frames was not
  found anywhere.
- The accent goes in the custom voice's **Voice Performance** text. Google's own example: "Make the voice sound
  slightly raspy with a New York accent." OFFICIAL, same page.
- Name the accent inside the speech clause: "She says, in a warm and measured British accent:". HOST (Runware).
  <https://runware.ai/docs/models/google-gemini-omni-flash-1-1/guides/prompting>
- **The accent follows the picture**: Veo matches accent to the speaker's look and the setting "regardless of
  what you prompt it". ANECDOTE (r/VEO3, second-hand).
- A five-run test (Veo 3, Romanian) found an explicit accent request made no difference; its author calls it
  generation variance. ANECDOTE, one tester. <https://github.com/ulmeanuadrian/kie-mcp/issues/1>
- Omni 1.1 voice drift between clips is a reported regression (forum, 2026-09-11), no fix from Google. ANECDOTE.
- Fallback several creators use: change the voice in post. PRACTITIONER.
- **Not found:** any evidence that a regional label (Estuary, Yorkshire) beats "British", or that spelling
  tricks work.

## 3. Two speakers, one voice; the wrong mouth

All of this is Veo 3.x guidance. Nothing specific to Omni was found.

- "If both characters look or sound similar, Veo 3 smears the dialogue across both mouths or puts the wrong
  voice on the wrong person." Fix: widen the gap in pitch, accent and pace; tag the speaker by clothing inside
  the line. PRACTITIONER. <https://www.veo3ai.io/blog/veo-3-two-character-dialogue-guide-2026>
- Give the listener a visible job while the other talks; never both at once; two to four short lines in 8 s at
  most. Same source.
- Silent-mouth wording: "lips closed, breathing calmly". A bare "no talking" can summon speech. ANECDOTE.
  <https://apipass.dev/blogs/how-to-solve-veo-3-keep-generating-unwanted-dialogue>
- One speaker a clip, the line under about five seconds, cut shot and reverse shot. PRACTITIONER, repeated.
- Identify by clothing, not left and right: the model card lists left/right as weak.

## 4. Machine listeners cannot judge accent `[observed]`

`[observed, 2026-10-09, one file]` The same two-minute file of twenty talking clips went through two Gemini
models with the same question. **3 Flash preview called fourteen clips General American; 3.5 Flash called all
twenty London or Estuary.** 3.5 Flash had itself called several of the same lines American an hour earlier, in
the full-film pass. They agreed on words, on voice count, and on "both lines sound like the same person".

**Rule:** use the listening tool for words, for who is speaking, and for whether two lines share a voice. Do
not use it to decide whether an accent is right. That needs a person.

## 5. The test this led to

See the foot of `docs/stories/bank-robbery/review-cut5.md`.

**Result, `[observed, n=1, two machine listeners, 2026-10-09]`:** a two-speaker clip re-made in **Ingredients**
with both Characters attached (still as scene reference, accent in each speech clause, "lips closed" on the
listener) was heard as two different voices by one model and as "more different, still one actor" by the other;
the Frames take of the same lines was one voice to both. The shot was re-staged (wider, squarer) and one word
was stumbled. Submit to saved file took under a minute. Not heard by a person.
