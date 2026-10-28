---
name: flow-prompt
description: Use when writing or debugging a prompt for Google Flow — a still image, an image-to-video motion prompt, a character reference, or a generation that failed. Encodes how the Flow platform actually behaves (Nano Banana and Veo), the policy-block triggers and rewrites, and the reference/consistency disciplines. Triggers on "write a Flow prompt", "why did this generation fail", "the prompt got blocked", "make this prompt better", "how do I animate this", or any prompt-craft step inside badcode-art-direction, new-image, edit-panel, animate-slide, make-comic or music-video-short. Platform craft only — what a story looks like lives in that story's docs/stories/<story>/look.md.
---

# Flow Prompt

How to get what you asked for out of Google Flow. This skill owns **platform craft** —
how Veo and Nano Banana actually behave. It owns **no look at all**: there is no BadCode house look (Kai, 2026-10-28). Each story's look is its `docs/stories/<story>/look.md`.

## The things that are not this skill's job

| Question | Answer lives in |
| --- | --- |
| ***What should this shot BE?*** — framing, depth, light design, angle, what it's for | **`shot-craft`** — the cinematography judgement layer. **Consult it BEFORE writing any prompt for a shot that hasn't been designed yet** |
| *What should this story's stills and clips look like?* | **`docs/stories/<story>/look.md`** — read it before any prompt. Empty → `story-style`; exploring → `variations` |
| *Options that are actually different?* | `variations` (separate writers + a sameness gate) |
| *This story's prompt ledger and what got made* | `docs/stories/<story>/prompts.md`, the scene folders |
| *How do I make Flow do what I asked?* | **here** |

A finished prompt is **design (`shot-craft`) + the story's look (`look.md`) + phrasing
(here)** — three separate jobs. The design step is the one that gets skipped, and it is the one
that decides whether the shot is interesting rather than merely correct. If you were handed a
*shot spec*, phrase it; if you were handed only a subject, get the spec first.
Never let this skill's example prompts, or any other story's look, leak into a story's work —
every look named in this skill and `docs/flow/` is vocabulary, not a recommendation.

## The knowledge base lives in docs/flow/

Read on demand. Never reproduce it into a reply, and don't lecture the user about it.

| File | What | Read when |
| --- | --- | --- |
| `README.md` | The 15 rules, provenance, what's volatile | Starting out, or sanity-checking a claim |
| `image-prompting.md` | Nano Banana / Pro craft, editing, rendered text | Any still |
| `video-prompting.md` | Veo formula, image→video, frames, audio, dialogue | Any motion work |
| `camera-vocabulary.md` | Shot/move/lens/light terms + reliability tiers | Writing the camera clause |
| `consistency.md` | Characters, references, continuity | A character or object recurs |
| `platform-controls.md` | Models, credits, aspect, duration, limits | Planning a batch or a budget |
| `failure-modes.md` | Policy blocks, rewrites, quality failures | **Any failure, and before any risky prompt** |

All paths relative to [`docs/flow/`](../../../docs/flow/README.md).

## Rule zero — never name a real person, anywhere

**No real person's name goes into any Flow field. Ever.** Not the prompt, not a Character
Name, not Character Info, not a filename you upload. Describe the person instead: build, age,
era dress, bearing, posture. "A lean man in his fifties, three-piece tweed, moustache,
1940s" — never the name.

Three reasons this is absolute rather than a preference:

- **Flow scans every field, not just the prompt box.** A Character called "Keynes" had every
  generation refused while the prompt text named nobody (2026-08-12). A poisoned Character
  Name breaks *every* shot that casts it, not one prompt.
- **Getting away with it is worse than being blocked.** Tested 2026-08-12: Churchill
  generated fine, Taylor Swift was refused. So a name that works today teaches the wrong
  lesson, spends real credits, and can start failing at any time — usually mid-batch.
- **A named likeness is not what we want anyway.** BadCode figures are archetypes. Naming a
  real person makes the model chase a specific face instead of the character we designed,
  and the Character feature already binds the face far more reliably.

If a story's canon is *about* a real person, that person's identity lives in the story
document. The prompt gets the description only.

## 🔴 Video is Omni Flash now: read `docs/google-flow/` first

`docs/flow/` below was written for Veo. Since 2026-09 the house video model is Omni 1.1 Flash, and what it does
is recorded in [`docs/google-flow/`](../../../docs/google-flow/README.md) (`omni-flash.md`, `nano-banana-2.md`,
the dated sweeps). **Open that README before writing any video prompt:** its first section is the list of moves
the model cannot do and the four rules for the words (short, saturated colour named per place, never describe an
attached Character, check at four frames a second). Where the two folders disagree about Omni, `docs/google-flow/`
wins. Added 2026-10-09 after a film's worth of prompts ignored research that this skill never pointed at.

## The five rules that carry most of the value

If you read nothing else:

1. **Write a brief, not a tag dump.** Prose sentences. Nano Banana reasons over the
   prompt before rendering; comma-stacked keywords and `word::1.5` weights actively
   degrade it.
2. **When animating a still, describe the motion ONLY.** The image already carries
   subject, scene and style. Re-describing them makes the model regenerate instead of
   animate. Say "the subject", not the character's description.
3. **Front-load the camera.** `[Cinematography] + [Subject] + [Action] + [Context] +
   [Style]`. Earlier clauses win when instructions compete.
4. **One action, one camera move per clip.** When a shot isn't landing, **delete a
   clause — never add one.**
5. **A block looks exactly like a timeout.** Two no-candidate failures on a healthy
   session means rewrite, never retry.

## Writing a prompt

**A storyboard beat arrives as four different briefs, not one.** `new-image` ->
"Variety mode" decides the spread; this skill phrases each candidate. Write four genuinely
different briefs — a different camera, palette, time of day or register in each — never one brief
re-seeded. If the story's look is LOCKED, one of the four is that look and at least one breaks it on
purpose; if it is EMPTY or EXPLORING, all four are different and the round runs through `variations`.


1. **Get the look from the story's `look.md` first.** Don't invent a look here, and don't
   borrow another story's.
2. **Draft in the platform's shape** — the formula from `image-prompting.md` §2 or
   `video-prompting.md` §1, with the four levers (lighting / camera+lens / stock+grade /
   materiality) as separate clauses.
3. **Run the policy pass** — `failure-modes.md` §A5, and rule zero above. Check *every
   field*, not just the prompt: a Character's **name** is scanned too. Cheap, and saves ~90s
   per block.
4. **Critique before sending.** Is there exactly one action? One camera move? Is the
   light source a real thing in the scene? Is any load-bearing text better done as a
   comic overlay?
5. **Generate, look, subtract.** When it's wrong, remove a clause before adding one.

## 🔴 Where the prompt gets written down

**A prompt is repo content. Write it in the repo, then generate.**

| What | Where |
| --- | --- |
| A story's look — preambles, guardrails, cast references | `docs/stories/<story>/look.md` |
| The story's prompt ledger — cut order, what was prompted | `docs/stories/<story>/prompts.md` |
| A specific scene's prompts and what actually got made | `docs/stories/<story>/scenes/<scene>.md` |
| A standalone brand image | beside the image, per `new-image` |
| **Never** | the Premiere project's `clips/` folder — that is for media only |

Every generated image and clip keeps **its exact prompt plus a revision log**, which is what makes
*"just like that, but change X"* one cheap step instead of a re-derivation. A prompt written
somewhere unversioned loses that.

Ruled 2026-08-27 by Kai, after a scene's prompt sheet was written out to `clips/` by mistake —
the 2026-08-26 ruling that *generated media* lives in the open Premiere project's `clips/<scene>/`
got over-applied to the words. Media out there, words in here.

## Debugging a failure

**First: which kind of failure?**

- **No candidate landed, session healthy, two attempts** → policy block. Go to
  `failure-modes.md` Part A. Turn off "Enhance Prompt", then binary-search by
  subtraction. Check the reference image separately from the text.
- **Candidate landed but it's wrong** → quality failure. `failure-modes.md` Part B.
  Check it isn't a known-unreliable ask (hands, physics, legible video text, full 360°
  orbit) before blaming the prompt.
- **Tool error, wedged picker, stale tab** → not a prompt problem.
  `docs/flow/automation-images.md` and the `flow-operator` agent.

**The one debugging move that generalises:** subtract. Strip to the simplest form that
works, then add back one variable at a time.

## Consistency work

When a character, object or place has to survive across many generations, read
`consistency.md` before generating anything. The headlines:

- **People → a Flow Character.** Objects and places → **a golden reference image**, cited
  by name in every prompt. A tag typed as prompt text binds nothing.
- **One clean element per reference image, plain background.** This single discipline
  fixes both identity drift and style bleed. The beautiful crowded shot is the *worse*
  reference.
- **Paste the character's DNA block verbatim every time.** Re-describing from memory is
  where drift starts. The story's `characters/*.md` file is that block.
- **Drift is a probability, not a bug.** Budget a reroll on hero shots.

## Scope

Platform craft for Google Flow: Nano Banana stills, Veo motion, references, consistency,
policy, controls. **Not** the BadCode visual identity (`new-image`), **not** browser automation or selectors (`docs/flow/automation-images.md`,
the `flow-operator` agent), **not** Suno or music (`suno-prompt`).
