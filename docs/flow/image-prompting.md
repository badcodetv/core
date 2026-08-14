# Image prompting — Nano Banana / Nano Banana Pro

Flow's still-image models. Platform behaviour only — the BadCode look lives in
`badcode-art-direction` (comic panels) and `new-image` (brand imagery).

## 1. The mental model

Nano Banana Pro is a **reasoning** image model: it plans the composition, generates,
reviews against your prompt, and self-corrects before returning pixels. Three
consequences:

- Compound spatial and logical instructions that a diffusion model would average out
  are actually honoured — "the text acts as a cut-out window", exact object counts,
  explicit left/right placement.
- **Prose beats keyword stacks.** Write like you're briefing a designer, not filling
  a search box.
- Iterative refinement beats front-loading. Short prompts already generate well;
  detail is a dial you turn up *where the output is ambiguous*, not padding you apply
  everywhere.

**A focused short prompt beats a long prompt containing competing styles or
viewpoints.** When output drifts, simplify — split run-on sentences into short
clauses — before adding description.

## 2. The formulas

**Text-to-image:** `[Subject] + [Action] + [Location/context] + [Composition] + [Style]`,
woven into one flowing paragraph rather than left as labels.

> **Official example:** "A striking fashion model wearing a tailored brown dress, sleek
> boots, and holding a structured handbag. Posing with a confident, statuesque stance,
> slightly turned. A seamless, deep cherry red studio backdrop. Medium-full shot,
> center-framed. Fashion magazine style editorial, shot on medium-format analog film,
> pronounced grain, high saturation, cinematic lighting effect."

**Multi-reference:** `[Reference images, each with its role named] + [Relationship
instruction] + [New scenario]`.

> **Official example:** "Using the attached napkin sketch as the structure and the
> attached fabric sample as the texture, transform this into a high-fidelity 3D armchair
> render. Place it in a sun-drenched, minimalist living room."

**Open with a strong verb naming the operation** — generate, transform, combine,
remove, edit — then layer subject, action, location, composition, style, lighting,
camera, materiality.

## 3. The four levers — keep each as its own clause

| Lever | Write it as | Examples |
| --- | --- | --- |
| **Lighting** | A named setup | "three-point softbox setup"; "chiaroscuro lighting with harsh, high contrast"; "golden hour backlighting creating long shadows" |
| **Camera / lens** | Focal length + aperture together | "low-angle shot with a shallow depth of field (f/1.8)"; "85mm lens at f/2.8"; "macro lens" |
| **Film stock / grade** | A trailing clause, after everything else | "as if on 1980s color film, slightly grainy"; "cinematic color grading with muted teal tones" |
| **Materiality** | Replace the category noun with the substance | not "suit jacket" → "navy blue tweed"; not "armor" → "ornate elven plate armor, etched with silver leaf patterns" |

Full term reference with reliability tiers: [`camera-vocabulary.md`](./camera-vocabulary.md).

## 4. Realism — defeating the plastic default

The model defaults to studio-perfect. Explicitly grant it permission to be a real
camera:

- "hyper-realistic skin texture with visible pores and subtle imperfections"
- "natural skin microtexture, subtle pores" — and prefer "soft key with diffusion"
  over "glossy skin"
- Scene-level: "a tiny smear on the lens", "subtle handshake blur", "faint light leak",
  "uneven exposure", "fine film grain"

Bare "photorealistic" as an adjective gets you plastic. The imperfection has to be
named.

## 4a. Expressions — name the muscles, never the emotion

**Added 2026-08-14.** The counterpart to §4: the same studio-perfect default that makes
skin plastic makes faces *overact*. Naming a feeling is what causes it.

> **"AI does not understand feelings. It understands facial muscles, micro-expressions,
> and physical changes in the face."** `[community]`
>
> *"Most people write 'sad person' and get an exaggerated crying face. Real sadness is
> quiet and lives mostly in the eyes."*

**So describe the face physically and let the emotion be inferred.** The word for the
feeling should not appear in the prompt at all.

| Instead of | Write |
| --- | --- |
| happy | genuine smile, cheeks lifted, eyes slightly squinting |
| sad | soft eyes, slight frown, down-turned lips |
| angry | tight jaw, lowered brows, intense eyes |
| hungover, exhausted | half-lidded eyes slow to track, mouth flat and slightly open, slack jaw, a pillow crease across one cheek |
| unimpressed, annoyed | brows relaxed and level, eyes aimed at nothing, the face doing almost nothing |

**The vocabulary, by feature** `[community]` — eyes: *engaged, soft, intense, wide,
half-lidded*; brows: *raised, lowered, relaxed, level, slightly raised (single)*; mouth:
*genuine smile, slight frown, slightly open, flat*; overall: *relaxed facial muscles,
tight jaw, controlled anger, realistic tension*.

**⚠️ Beware the opposite-of-happy trap.** Reaching for a scowl to convey displeasure
gets you Angry Face, which is just as overacted. Restraint reads as real: **a face that
does almost nothing** is usually the truthful version of irritation, boredom or
endurance.

**Supporting tokens that stop the stock-photo look** `[community]`: `natural skin
texture`, `slight asymmetry`, `unposed`, `unaware of the camera`, `caught mid-gesture`.
And put the state in the **world** as well as the face — a pressed-out blister pack and
a half-drunk pint of water say *hungover* more reliably than any adjective on a face.

**Sources:** [Realistic facial expressions in AI images — Medium](https://medium.com/write-your-world/how-to-create-realistic-facial-expressions-in-ai-images-2026-guide-prompt-examples-63438c54c65f) ·
[Prompt keywords to make images less fake — Promptaa](https://promptaa.com/blog/prompt-key-words-to-make-images-less-fake-looking)
`[community]`. Consistent with the repo's own long-standing note in
[`video-prompting.md`](./video-prompting.md) — *"mouth movement matches the words
without exaggerated expression"*.

## 5. Rendered text

Nano Banana Pro is genuinely strong at legible in-image text — the one place Flow will
hold a word steady.

1. Put the exact string in quotes: `"URBAN EXPLORER"`.
2. Name the typography separately, in prose: "bold, white, sans-serif font".
3. **Text-first trick:** settle the wording in a Gemini chat turn, then ask for the
   image carrying that agreed text.
4. Localisation: write the prompt in one language, name the target language for the
   rendered text.

> **Official (multi-line typography):** "A high-end, glossy commercial beauty shot of a
> sleek, minimalist nude-colored face moisturizer jar resting on a warm studio
> background. The lighting is soft and radiant. Next to the product, render three lines
> of text with the following exact styling: For the top line, the word 'GLOW' in a
> flowing, elegant Brush Script font. For the middle line, the text '10% OFF' in a
> heavy, blocky Impact font. For the bottom line, the text 'Your First Order' in a thin,
> minimalist Century Gothic font." → then: "translate the text into Korean and Arabic."

> **Official (text as composition):** "A typographic poster with a solid black
> background, bold letters spell 'New York', filling the center of the frame. The text
> acts as a cut-out window. A photograph of New York skyline is visible ONLY inside the
> letterforms."

**Two BadCode caveats.** Veo cannot hold text steady in *video* — any lettering that
must stay legible in motion is a still composited later (`failure-modes.md`). And our
own story guardrails ban legible text in most panels anyway, both because it reads as
AI and because text attributed to a real institution is a policy trigger. Load-bearing
words belong in a `NarrationBox`, not in the pixels.

## 6. Editing — semantic masking

This is what `edit-panel` runs on. You define the mask **in words**, not pixels. Both
halves are mandatory:

- **Name the operation with a strong verb, first:** "Remove the man from the photo."
- **State explicitly what must stay the same.** Omitting this is why edits wander.

Google's own edit template, which `edit-panel` already uses verbatim:

> "Using the provided image, change only [the thing] to [the change]. Keep everything
> else in the image exactly the same, preserving the original style, lighting, and
> composition."

For identity-preserving edits from a golden reference, escalate to explicit identity-lock
language naming the held features:

> "The subject from the uploaded image, maintaining the exact real face, hairstyle, skin
> tone, and body identity unchanged" → "100% identity lock, no alteration."

⚠️ **That phrasing is a policy trigger in our register** — likeness language ("same
face, same bone structure") is BadCode block trigger #2. Use it only when the subject is
an invented character, never when the reference is derived from a real person. See
`failure-modes.md`.

Refine conversationally across follow-up turns rather than rewriting one giant prompt
each round.

## 7. Constraints and negatives

There is **no negative-prompt field on the image side.** Describe the desired end
state: "empty street", not "no cars". For a genuine hard boundary ("do not change the
logo"), pair the exclusion with a positive restatement of the required result.

## 8. Search grounding (Nano Banana Pro only)

`[Search request] + [Analytical task] + [Visual translation]`.

> **Official:** "[Search for current weather and date in San Francisco] + [Analytically,
> use this data to modify the scene (e.g., if raining, make it look grey and rainy)] +
> [Visualize this in a miniature city-in-a-cup concept embedded within a realistic,
> modern smartphone UI.]"

## 9. Specs

- **References:** up to 14 per prompt; identity held for up to 5 distinct people in one
  composition. *(Our `flow_edit_image` tool caps at 3 by schema and the flow-mcp README
  says use exactly one — that's an upload-reliability limit on our side, not a model
  limit.)*
- **Resolution:** 1K / 2K / 4K (Nano Banana 2 also 512px).
- **Aspect ratios:** 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (NB2 adds 1:4,
  4:1, 1:8, 8:1). **State it as its own clause** — "A cinematic 21:9 wide shot".
- **Inputs:** PNG / JPEG / WebP / HEIC / HEIF, plus text and PDF.
- **All outputs carry C2PA Content Credentials and SynthID watermarking.** Relevant to
  any BadCode provenance or disclosure decision on published art.
