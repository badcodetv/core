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

## 7. Constraints and negatives — "semantic negative prompts"

That is **Google's own name for it**, and worth using because it says what the technique is:
you get exclusion by describing the world you want, not by naming what to leave out.

> **Official:** *"Use 'semantic negative prompts': Instead of saying 'no cars,' describe the
> intended scene positively: 'an empty, deserted street with no signs of traffic.'"*

There is **no negative-prompt field on the image side.** Describe the desired end
state: "empty street", not "no cars". For a genuine hard boundary ("do not change the
logo"), pair the exclusion with a positive restatement of the required result.

## 8. Search grounding (Nano Banana Pro only)

`[Search request] + [Analytical task] + [Visual translation]`.

> **Official:** "[Search for current weather and date in San Francisco] + [Analytically,
> use this data to modify the scene (e.g., if raining, make it look grey and rainy)] +
> [Visualize this in a miniature city-in-a-cup concept embedded within a realistic,
> modern smartphone UI.]"

## 8b. The official templates we didn't have

Google publishes a re-usable template beside each worked example. These five were missing from
this file; all are quoted verbatim from the image-generation guide.

| Job | Template |
| --- | --- |
| **Photorealistic scene** | `A photorealistic [type of shot] of a [subject description] in a [setting description]. [Description of the light]. Shot from a [camera angle] with a [lens type].` |
| **Sequential art / comic panel** | `Make a 3 panel comic in a [style]. Put the character in a [type of scene].` — pass the character image as input. Google notes these "work best with Gemini 3 Pro and Gemini 3.1 Flash Image". |
| **Character consistency, 360 view** | `A studio portrait of [person] against [background], [looking forward / in profile looking right / etc.]` — *"include previously generated images in subsequent prompts to maintain consistency"* |
| **High-fidelity detail preservation** | `Using the provided images, place [element from image 2] onto [element from image 1]. Ensure that the features of [element from image 1] remain completely unchanged. The added element should [how it integrates].` |
| **Style transfer** | `Transform the provided photograph of [subject] into the artistic style of [artist/art style]. Preserve the original composition but render it with [stylistic elements].` |
| **Combining images** | `Create a new image by combining the elements from the provided images. Take the [element from image 1] and place it with/on the [element from image 2]. The final image should be a [description].` |
| **Minimalist / negative space** | `A minimalist composition featuring a single [subject] positioned in the [bottom-right/etc.] of the frame. The background is a vast, empty [color] canvas, creating significant negative space. Soft, subtle lighting. [Aspect ratio].` |

**Two of these are directly ours.** The **360-view** template is the documented way to build a
character sheet — iterative, one angle per turn, feeding each result back in — which is exactly
the shape that worked for us (Portrait → native Create Body) and not the single-call composite
that never lands (`consistency.md` §5). And the **minimalist / negative-space** template is how
you generate a plate that a `NarrationBox` will sit on without fighting it.

## 8c. Google's four best practices

Beyond "be specific", which this file already says three ways:

1. **Provide context and intent.** *"Explain the purpose of the image… 'Create a logo for a
   high-end, minimalist skincare brand' will yield better results than just 'Create a logo'."*
   The model reasons about the brief, so give it the brief.
2. **Use step-by-step instructions for complex scenes.** *"First, create a background of a
   serene, misty forest at dawn. Then, in the foreground, add a moss-covered ancient stone
   altar. Finally, place a single, glowing sword on top of the altar."* Sequence beats one
   dense paragraph when there are many elements to place.
3. **Iterate conversationally.** *"That's great, but can you make the lighting a bit warmer?"*
   — cheaper and more accurate than re-authoring the whole prompt. This is what `flow_refine`
   is for, and why `edit-panel` loops rather than rewrites.
4. **Control the camera with photographic language.** See
   [`camera-vocabulary.md`](./camera-vocabulary.md).

## 9. Specs

- **References — corrected 2026-08-18, we had this wrong.** The caps are per model, and "5"
  was never a count of *people*:

  | Model | Reference capacity, verbatim |
  | --- | --- |
  | Nano Banana Pro (`gemini-3-pro-image`) | "supports 5 images with high fidelity, and up to 14 images in total" |
  | Nano Banana 2 (`gemini-3.1-flash-image`) | "character resemblance of up to 4 characters and the fidelity of up to 10 objects in a single workflow" |
  | Nano Banana (`gemini-2.5-flash-image`) | "works best with up to 3 images as input" |

  So Pro's 14 is a *total* with only the first 5 held at high fidelity, and the "4 characters"
  figure belongs to NB2, not Pro. *(Our `flow_edit_image` tool caps at 3 by schema and the
  flow-mcp README says use exactly one — an upload-reliability limit on our side, well inside
  every model limit above.)*
- **Resolution:** 1K / 2K / 4K (Nano Banana 2 also 512px).
- **Aspect ratios:** 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (NB2 adds 1:4,
  4:1, 1:8, 8:1). **State it as its own clause** — "A cinematic 21:9 wide shot".
- **Inputs:** PNG / JPEG / WebP / HEIC / HEIF, plus text and PDF.
- **All outputs carry C2PA Content Credentials and SynthID watermarking.** Relevant to
  any BadCode provenance or disclosure decision on published art.

---

## Sources

Read end to end at source on **2026-08-18**. Every quotation marked "Official" is from the
first link; the BadCode caveats and the register notes are ours.

- [Image generation with Gemini ("Nano Banana") — Gemini API](https://ai.google.dev/gemini-api/docs/image-generation) — the prompting guide and its templates, editing templates, best practices, limitations, aspect-ratio and resolution tables, the model line-up.
- [Learn about Google Flow models & supported features](https://support.google.com/labs/answer/16352836?hl=en) — which image models Flow actually offers and which is default on which plan.
- [Create & edit images in Google Flow](https://support.google.com/labs/answer/16729550?hl=en) — the in-Flow image surface.

**Model line-up, in Google's words:** Nano Banana 2 (`gemini-3.1-flash-image`) is *"your go-to
image generation model"*; **Nano Banana Pro** (`gemini-3-pro-image`) is *"designed for
professional asset production and complex instructions"* with search grounding, a default
**"Thinking" process that refines composition prior to generation**, and up to 4K. That
Thinking pass is the thing §1 of this file calls a reasoning model — it is documented, not
inferred. Imagen is deprecated and shuts down 2026-08-17; do not reach for it.
