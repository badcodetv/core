# Nano Banana 2 — image engine reference

**Model:** Gemini 3.1 Flash Image. Launched 26 Feb 2026.
**Researched:** 2026-08-12 · **Confirmed against our Flow session:** never — everything here is
`[vendor]` or `[community]` until a calibration run says otherwise (see [README](./README.md)).

## Identity & availability

- Nano Banana 2 is **Flow's default image model for all users**, at **zero credits** — including
  free tier. `[vendor]` `[community]`
- Also on: Gemini app (replacing Nano Banana Pro across Fast/Thinking/Pro), Google Search (AI Mode
  and Lens), AI Studio + Gemini API (preview), Vertex AI (preview), Google Ads. `[vendor]`
- The pitch: Nano Banana **Pro**'s world knowledge, quality and reasoning at Flash speed. It is a
  quality *upgrade* over what the camping / magic-money-tree / karen panels were generated on, not
  a sidegrade. `[vendor]`
- Every output carries **C2PA Content Credentials and a SynthID watermark**. `[vendor]`
- Knowledge cutoff Jan 2025, but **live data via real-time web search** is wired in. `[vendor]`

## Hard limits

| | Nano Banana 2 |
| --- | --- |
| Input context | 131,072 tokens `[vendor]` |
| Output | 32,768 tokens `[vendor]` |
| Resolutions | 512px (0.5K), 1K, 2K, 4K `[vendor]` |
| Aspect ratios | 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 — **plus** 1:4, 4:1, 1:8, 8:1 `[vendor]` |
| Reference images | up to **14** in a single prompt `[vendor]` |
| Character consistency | resemblance across up to **5 characters**; fidelity across up to **14 objects** `[vendor]` |
| Image formats | png, jpeg, webp, heic, heif `[vendor]` |
| Batch in Flow | up to 4 images per prompt `[community]` |

**The 5-character ceiling is the one to remember.** Panels with a crowd of named, face-bearing
recurring characters sit right at the edge of what the model claims to hold.

**Contested:** a Flow-specific tutorial states the real figures are **4 unique characters and 10
objects** tracked within the 14 references `[yt]`, against Google's blog claim of 5 and 14
`[vendor]`. Either the Flow surface is more limited than the raw model, or one source is wrong.
Assume the lower numbers when planning a crowded panel until we test it.

## Prompt structure

Google's own templates. Note how closely the first one already matches the shape
`badcode-art-direction` uses (house-style preamble + specific scene description).

**Text-to-image:** `[Subject] + [Action] + [Location/context] + [Composition] + [Style]` `[vendor]`

> "[Subject] A striking fashion model wearing a tailored brown dress… [Action] Posing with a
> confident, statuesque stance, slightly turned. [Location/context] A seamless, deep cherry red
> studio backdrop. [Composition] Medium-full shot, center-framed. [Style] Fashion magazine style
> editorial, shot on medium-format analog film, pronounced grain, high saturation, cinematic
> lighting effect."

**With reference images:** `[Reference images] + [Relationship instruction] + [New scenario]` `[vendor]`

> "Using the attached napkin sketch as the structure and the attached fabric sample as the texture,
> transform this into a high-fidelity 3D armchair render. Place it in a sun-drenched, minimalist
> living room."

The **relationship instruction is the load-bearing middle term** — say explicitly what each
reference contributes (structure vs. texture vs. face vs. wardrobe) rather than attaching images
and hoping. This is the vendor-side echo of our own hard-won casting rule.

**Editing without new references:** semantic masking via text. Be **explicit about what to keep
exactly the same**, and change **one variable at a time**. `[vendor]`

## Core rules

1. **Be specific** — concrete detail on subject, lighting, composition. Generic keyword lists
   underperform narrative structure. `[vendor]`
2. **Use positive framing** — "empty street", not "no cars". `[vendor]`
3. **Control the camera explicitly** — "low angle", "aerial view", photographic/cinematic terms.
4. **Start with a strong verb** telling the model the primary operation.
5. **Iterate conversationally** rather than rewriting from scratch.

### Creative-director levers `[vendor]`

- **Lighting** — "three-point softbox setup", "chiaroscuro lighting with harsh, high contrast",
  "golden hour backlighting creating long shadows".
- **Camera / lens / focus** — naming *hardware* shifts the whole look: "GoPro" (immersive,
  distorted), "Fujifilm" (authentic colour), "disposable camera" (nostalgic flash). Lens control:
  "shallow depth of field (f/1.8)", "wide-angle", "macro".
- **Colour grading & film stock** — "rendered as if on 1980s colour film, slightly grainy",
  "cinematic colour grading with muted teal tones".
- **Materiality** — name the material, not the object class: "navy blue tweed", not "suit jacket".

## Text rendering

Materially better than previous generations, and relevant to a decision we've already made.

- **Quote the words**: `"Happy Birthday"`, `"URBAN EXPLORER"`. `[vendor]`
- **Name the font**: "bold, white, sans-serif", "Century Gothic 12px". `[vendor]`
- **Translate/localise**: prompt in one language, specify the output language for the text. `[vendor]`
- **The text-first hack**: converse with the model to settle the text *first*, then ask for the
  image containing it. `[vendor]`

**This does not overturn our rule that load-bearing text belongs in the comic, not the image.**
Overlay text in `@badcode/comic` stays sharper, editable, translatable, and — decisively — cannot
be policy-blocked. Better in-image text rendering is useful for *incidental* signage where a
blurred fascia currently reads as a dodge, not for headlines and narration.

## Field tips from the YouTube pass `[yt]`

Harvested 2026-08-12 from the most-viewed tutorials (sources at the bottom). Several of these are
demonstrated on screen inside Flow, which puts them above forum hearsay — but read the bias warning.

### What Flow's image surface actually gives you

- **Model picker: Nano Banana Pro vs Nano Banana 2.** Practitioners prefer NB2 in Flow specifically
  because **Pro exhausts the rate limit far faster** — one reports generating for hours on NB2
  without hitting a cap, and 12–16 concurrent generations at quiet times.
- **1–4 images per prompt**, portrait/landscape toggle, per-project settings.
- **The reuse-prompt arrow** on every generated image re-loads *the prompt and the reference images
  it used*. This is the cheapest way to run a controlled variation.
- **Per-image history with a layers icon** — edits stack non-destructively and you can step back to
  any earlier state and branch from it.
- **Selection tools: box and lasso.** Make a selection, then prompt — the change is confined to that
  region. Say "in the selection" in the prompt text too; omitting it, the model may ignore the mask.
- **Sketch annotation, and it is colour-aware.** Pen, text and rectangle tools draw straight onto the
  image, then the prompt references the drawing by colour: *"add the horns to the helmet like in the
  red sketch and add a shield with the cross on it like in the green sketch."* This is the most
  precise spatial control on the image side and has no equivalent in prose prompting.
- **Crop tool** (fixed ratios or freeform) produces a new image; the pre-crop original stays in history.
- **Download original or upscaled** — 2K on the standard tier, 4K gated behind an upgrade.
- **Info icon** on each image shows the prompt, date and model used. Favourites, rename, search,
  sort and filter across project assets.
- **No visible watermark on Flow images** (invisible SynthID only) — unlike Flow *video*, which
  burns in a visible mark. SynthID is detectable: paste a generation into Gemini and it will say it
  is AI-generated. Relevant to any publication decision, not to whether it generates.

### The prompt formula everyone converges on

Two independent high-view tutorials teach the same six-slot structure, and it is a superset of
Google's own five-slot template:

> **Subject + Action + Environment + Art style + Lighting + Details**

The consistent lesson is that **the failure mode is laziness in one slot** — "nice lighting" instead
of "dramatic window lighting creating a rim-light effect". Naming actual camera hardware ("shot on a
Canon 5D Mark IV", "85mm portrait lens", "Kodak", "Ektachrome 64") does heavy lifting, which is
exactly the mechanism our 35mm house-style preamble already relies on.

### Editing: the five action verbs

For edits, lead with an action verb. The five that reportedly work most reliably:

> **Add · Change · Make · Remove · Replace**

Structure: `<action verb> + <specific element> + <desired change> + <relevant details>`.

**The face-preservation finding is the one worth stealing.** A common complaint is that changing
someone's clothes changes their face. The reported fix is not a longer prompt but a *shorter, more
specific* one led by an action verb:

> "Replace the woman's white top with the black t-shirt in the image."

Demonstrated holding the face across a two-person shot. This is the opposite of the instinct to
over-describe, and it is directly relevant to our wardrobe-vs-face problem — though note our hard
rule stands: for a **recurring** character, cast the Flow Character; don't rely on this.

### JSON prompting — the style-lock technique

From the highest-viewed NB2-specific technique video (170k). Three moves:

1. **Extract the DNA.** Upload an image, prompt: *"Extract all the information from this image and
   convert it into structured JSON."* You get style, colours, objects and spatial structure as code.
2. **Surgical edit.** Re-upload, prompt *"Modify the image based on the following JSON data"* and
   paste the JSON with **one field changed**. Everything unmentioned stays intact.
3. **Style as a portable token.** Prompt *"Describe the photography techniques in this image in JSON
   format"* → lighting, composition, colour palette, optics/focus, post-processing as a reusable
   block. Paste that JSON with a new subject to reproduce the exact look.

Move 3 is potentially significant for us: it is a mechanism for extracting the **house style from an
accepted panel** as a structured token and re-applying it, instead of re-typing a prose preamble and
hoping. Worth testing against `docs/stories/*/storyboard/` originals.

Also available as plain-text instructions: `"Aspect ratio 9:16"` reframes an existing image,
`"Upscale this image to 4K"`, and outpainting by asking for a fuller shot at a new ratio.

### Repeated editing degrades quality — and the re-anchor fix

Iterating edits on the same image visibly softens faces and loses detail: *"the face quality changed
a little, and that can happen when you keep the same images and only change portions of it."*

Two reported workarounds: nudge the camera angle slightly so it regenerates rather than patches, or
— better for us — **copy the good generation and paste it back into the prompt as a fresh
reference**, re-anchoring the chain instead of extending it. This matters because our `edit-panel`
loop is explicitly built to always edit *from the golden original*, which is the same instinct.

### The calibration risk nobody flags

A comparison video puts NB2 next to Nano Banana Pro on the same portrait prompt and prefers **Pro**:
NB2 came out "too sharp… too overly contrast… almost overexposed", Pro "a lot more natural" `[yt]`.
Google's own copy promises "vibrant lighting, richer textures and sharper details".

**That is a direct collision with the BadCode look** — muted cool-neutral palette, lifted blacks,
naturalistic motivated light, film grain. The engine's default improvement direction is exactly the
axis our house style suppresses. If panels start reading glossy, this is why, and Nano Banana Pro
may be the better engine for us despite being the older, slower, more rate-limited one.

## Notes for BadCode `[untested]`

Hypotheses for the calibration run, not rules.

1. **Our house-style preamble maps cleanly onto the `[Style]` slot.** The 35mm documentary
   formula is already the right shape. Likely no rewrite needed — worth confirming it still lands
   with the same weight on a stronger instruction-follower.
2. **The positive-framing rule collides with our preamble.** "no lens flares" is exactly the
   negative construction Google says to avoid. Test whether it still suppresses flares, or whether
   naming them makes them *more* likely. If the latter, the fix is a positive restatement —
   "clean, unflared optics; light sources sit inside the frame without blooming" — but this is a
   change to `badcode-art-direction` and needs confirming before anyone touches that file.
3. **21:9 is available** and we've never used it. Worth a look for reveal panels where the current
   16:9 crop fights the scale.
4. **512px is new** and near-free — plausible as a fast composition-check pass before committing to
   a 2K/4K generation, especially on panels likely to trip the policy filter.
5. **Stronger instruction-following may reduce the need for prose over-specification** in the
   character-signal department (grey stubble, lanyard, cardigan). Do **not** assume this. The hard
   rule stands: never regenerate a face-bearing panel of a recurring character without casting
   their Flow Character. A better model is not evidence that prose holds a face.
6. **Flow Characters remain project-scoped.** Nothing in the model change affects this.
7. **Live web search is a new failure surface.** A prompt naming a real place or institution may
   now pull *current* imagery, which for a story set in a fictional near-future is a drift risk
   rather than a feature.

## Open questions

- Does the existing usage-policy trigger list (real brands, likeness phrasing, stacked destitution,
  institutional text) behave the same on this engine? The block rate is the single biggest time
  cost in panel generation, so this is the highest-value thing to calibrate.
- Does Flow's UI expose the resolution and aspect-ratio pickers the API documents, or a subset?
  Partially answered: Flow shows a portrait/landscape toggle and 2K/4K download upscaling `[yt]`,
  not the full 10-ratio API list.
- Does the `flow` MCP server's `character` parameter still cast correctly on the new engine?
- **Is Nano Banana Pro the better engine for the BadCode look**, given the over-sharpening report?
  This is now the second-highest-value calibration after the policy-trigger list.
- Do the sketch-annotation and selection tools reach the MCP layer, or are they browser-only? If
  browser-only, they are a reason to keep a human-in-the-loop lane for difficult panels.

## Sources for the `[yt]` claims

Harvested 2026-08-12 with yt-dlp auto-captions (the method in
`scripts/fetch-youtube-transcripts.sh`), ranked by view count. Raw transcripts are research input
and were left in scratch, not committed.

| Channel | Video | Views |
| --- | --- | --- |
| Kevin Stratvert | Nano Banana AI Tutorial | 434k |
| AI Master | ULTIMATE NANO BANANA TUTORIAL: 15 PROMPT TECHNIQUES | 304k |
| Hongzhao | Full Control AI Image Editing with JSON Prompting (Gemini Nano Banana 2) | 170k |
| AI2Play | Nano Banana 2 in Google Flow: Full Tutorial for Beginners | 138k |
| Dan Kieft | How To Use Nano Banana 2 Better Than 99% of People | 86k |
| Taylor Bay Studios | Master The Ultimate Nano Banana Prompt Formula | 86k |
| Dylan Davis | Stop Writing Nano Banana Pro Prompts. Let AI Do It Instead. | 56k |
| Salmaan Mohamed | Nano Banana 2 Explained in 10 Minutes | 54k |
| altArch | Master Nano Banana 2: Architect's Ultimate Guide | 49k |
| Atomic Gains | Nano Banana 2 tips! and 80 creative Prompts You have to Try | 41k |
| AI2Play | Nano Banana 2 Realistic Photography Prompts With Google Gems | 36k |

**Bias warning:** most of these channels sell a course, a prompt pack, a community or a competing
platform, and several ran their tests in third-party wrappers (OpenArt, Higgsfield) rather than in
Flow — where model limits, watermarking and content filtering all differ. Some material tagged
"Nano Banana 2" is demonstrably about **Nano Banana Pro** or the **original** Nano Banana; where a
claim above is version-specific it came from someone visibly on the right model. Treat the rest as
directional.
