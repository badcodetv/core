---
name: flow-prompt
description: Use when writing or debugging a prompt for Google Flow — a still image, an image-to-video motion prompt, a character reference, or a generation that failed. Encodes how the Flow platform actually behaves (Nano Banana and Veo), the policy-block triggers and rewrites, and the reference/consistency disciplines. Triggers on "write a Flow prompt", "why did this generation fail", "the prompt got blocked", "make this prompt better", "how do I animate this", or any prompt-craft step inside badcode-art-direction, new-image, edit-panel, animate-slide, make-comic or music-video-short. Platform craft only — the BadCode look lives in badcode-art-direction (panels) and new-image (brand imagery).
---

# Flow Prompt

How to get what you asked for out of Google Flow. This skill owns **platform craft** —
how Veo and Nano Banana actually behave. It does **not** own the BadCode look.

## The two things that are not this skill's job

| Question | Answer lives in |
| --- | --- |
| *What should a BadCode panel look like?* | `badcode-art-direction` — 35mm documentary register |
| *What should a BadCode brand image look like?* | `new-image` — near-black monolith register |
| *What is this specific story's style and cast?* | `docs/stories/<story>/prompts.md` |
| *How do I make Flow do what I asked?* | **here** |

A finished prompt is usually **register (from a skill) + craft (from here)**. Read both.
Never let this skill's example prompts leak their *look* into BadCode work — teal-and-orange
grading and glossy commercial beauty shots appear here as vocabulary, not as
recommendations.

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

1. **Get the register from the owning skill first** (`badcode-art-direction` for panels,
   `new-image` for brand imagery, the story's `prompts.md` for story style). Don't invent
   a look here.
2. **Draft in the platform's shape** — the formula from `image-prompting.md` §2 or
   `video-prompting.md` §1, with the four levers (lighting / camera+lens / stock+grade /
   materiality) as separate clauses.
3. **Run the policy pass** — `failure-modes.md` §A5. Check *every field*, not just the
   prompt: a Character's **name** is scanned too. This is cheap and saves ~90s per block.
4. **Critique before sending.** Is there exactly one action? One camera move? Is the
   light source a real thing in the scene? Is any load-bearing text better done as a
   comic overlay?
5. **Generate, look, subtract.** When it's wrong, remove a clause before adding one.

## Debugging a failure

**First: which kind of failure?**

- **No candidate landed, session healthy, two attempts** → policy block. Go to
  `failure-modes.md` Part A. Turn off "Enhance Prompt", then binary-search by
  subtraction. Check the reference image separately from the text.
- **Candidate landed but it's wrong** → quality failure. `failure-modes.md` Part B.
  Check it isn't a known-unreliable ask (hands, physics, legible video text, full 360°
  orbit) before blaming the prompt.
- **Tool error, wedged picker, stale tab** → not a prompt problem.
  `docs/superpowers/flow-selectors.md` and the `flow-operator` agent.

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
policy, controls. **Not** the BadCode visual identity (`badcode-art-direction`,
`new-image`), **not** browser automation or selectors (`docs/superpowers/flow-selectors.md`,
the `flow-operator` agent), **not** Suno or music (`suno-prompt`).
