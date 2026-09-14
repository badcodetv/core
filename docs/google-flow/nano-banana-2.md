# Nano Banana 2 — image engine reference

**Model:** Gemini 3.1 Flash Image. Launched 26 Feb 2026.
**Also covers Nano Banana Pro** (Gemini 3 Pro Image), the sibling model in Flow's picker —
see [Third pass](#third-pass--nano-banana-pro-and-the-anti-slop-toolkit), which is where the
Pro-specific prompting and the engine recommendation live.
**Researched:** 2026-08-12 · **second pass 2026-08-12** ·
**third pass 2026-08-14** ([Pro, and the anti-slop toolkit](#third-pass--nano-banana-pro-and-the-anti-slop-toolkit)) ·
**fifth pass 2026-09-09** ([the model names, and faces](#fifth-pass--the-model-names-and-faces-community-2026-09-09) — ⚠️ **there is no "Nano Banana Pro 2"**) ·
**Confirmed against our Flow session:** never — everything here is
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

## Second web pass — 2026-08-12 `[vendor]` `[community]`

Harvested while writing the Karen §2c title-sequence plates
([`docs/stories/karen/prompts.md`](../stories/karen/prompts.md)). Google's own
guide plus the current crop of NB2 playbooks. Seven things the first pass missed.

1. **A style reference does not carry style.** The most counter-intuitive finding
   and the most useful: an attached reference anchors **identity and content**,
   and the model **will not assume the output matches the reference's style
   unless the prompt says so** — style has to be stated explicitly every time,
   even with the reference attached. `[community]` This retroactively justifies
   the Karen §2a habit of pasting the full style lock *and* attaching a style
   reference. It is not redundancy.
2. **Naming the use case measurably improves output.** "A hero shot for a luxury
   perfume launch", "a print-ready conference poster" — the model reportedly uses
   that context "to make a thousand small decisions". `[community]` Cheap to add
   and we do not currently do it anywhere.
3. **Series membership can be stated in prose.** Recommended phrasing:
   *"this is panel 3 of a 6-panel sequence; maintain visual identity with panels 1
   and 2"*. `[community]` Directly relevant to storyboard panel runs, where we
   currently lean entirely on references and the Character system.
4. **Negatives work, but short ones.** This resolves the tension flagged in note 2
   of *Notes for BadCode* below. Google's house rule is positive framing only —
   "empty street", never "no cars" `[vendor]` — yet `Not photorealistic` appears in
   Google's own illustration examples, and NB2 is reported to honour targeted
   negations more reliably than earlier generations, with the caveat that **long
   exclusion lists dilute the effect**. `[community]` Working resolution:
   **negate the style family in a clause, describe everything else positively.**
   Our eight-line exclusion stacks are the shape most likely to be underperforming.
5. **Hex codes are understood** — strongly by Nano Banana Pro, "to a lesser extent"
   by NB2. `[community]` Untested by us, and the obvious lever for any palette that
   has to hold across a series.
6. **Two regenerations, then rewrite.** "If you have regenerated the same prompt
   more than twice… rewrite from scratch." `[community]` Matches what the
   `edit-panel` loop already assumes about re-anchoring.
7. **Keyframes → video is the vendor's own recommended path**: "create keyframes
   with Nano Banana to direct an animation, then use Veo to generate the video
   between them". `[vendor]` The Karen §2b plate→clip pipeline is doing the
   endorsed thing, not improvising.

**Sources:** [Google Cloud — Ultimate prompting guide for Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) ·
[Fliki — NB2 prompting guide](https://fliki.ai/blog/nano-banana-2-prompting-guide) ·
[RunDiffusion — consistent character campaign images](https://www.rundiffusion.com/nano-banana-2-consistent-character-images) ·
[Flowith — consistent characters across 50 storyboard frames](https://flowith.io/blog/nano-banana-consistent-characters-storyboard/) ·
[Pixeldojo — NB2 negative prompts](https://pixeldojo.ai/nano-banana-2-negative-prompt) ·
[Atlabs — NB2 prompting guide](https://www.atlabs.ai/blog/nano-banana-2-prompting-guide)

**Same bias warning as the `[yt]` table.** Most of these are vendor blogs for
competing platforms; several demonstrate in third-party wrappers rather than Flow.
Google's own guide is the only unambiguously `[vendor]` source in the list.

## Third pass — Nano Banana Pro, and the anti-slop toolkit

**Added 2026-08-14.** Written while drafting the Karen §1.7 morning-after plates, on
two questions: *how do we prompt Nano Banana **Pro** specifically*, and *how do we keep
these out of the generic-AI-image trap.* The engine-agnostic realism half is the more
valuable of the two.

### Pro is a different animal: it plans before it draws

- **It reasons first.** Pro runs a *"'Thinking' Process… reasons through your prompt
  before generating, fixing logic errors"* `[community]`, and *"operates more like a
  designer, planning a scene's logic before generating it"* `[community]`, where NB2 is
  the better conversational editor.
- **Consequence: statements of *intent* land on Pro in a way they do not on a pure
  diffusion model.** *"This panel must read as a deliberate rhyme with the previous
  one"* is an instruction Pro can act on. Worth exploiting for matched pairs and
  sequence panels; worth not bothering with on NB2.
- **Google's own slot order for Pro** `[vendor]`: **Subject · Composition · Action ·
  Location · Style · Editing instructions.** Note *Composition* is promoted above
  *Action*, unlike the NB2 template above.
- Aspect ratio, aperture and grade can be stated **inline in the prose** — *"a cinematic
  21:9 wide shot"*, *"shallow depth of field (f/1.8)"*, *"muted teal tones"* `[vendor]`.
- **Reference images: name each one's job.** *"Clearly define the role of each"* input —
  one for pose, one for style, one for background `[vendor]`; *"Keep the character from
  Image 1 but put them in the pose from Image 2"* `[community]`. Identical in shape to
  the finding on the video side, which makes it a Google-wide habit rather than a
  per-model quirk.

### ⚠️ "Descriptive, not repetitive" — and what it costs us

The line that should change how we write:

> *"You don't need '4k, trending on artstation, masterpiece' spam anymore."* Be
> **"descriptive, not repetitive."** `[community]` And from Google's own guidance: define
> the job, subject, composition, light, style and constraints, **then remove repetition
> and conflicts** — *"a focused short prompt can beat a long prompt with competing
> styles or viewpoints."* `[vendor]`

**This has a direct cost for the Karen house style.** The §1 `STYLE LOCK` is pasted
verbatim at the top of every plate — grain, halation, vignetting, bloom, soft blacks —
and our scene blocks have then *restated* texture and optics underneath it. On Pro that
is precisely the pattern named above: repetition plus a second, competing style
statement.

**Working rule, `[untested]`: the lock owns texture and optics; the scene block owns the
world.** If a word appears in the lock, it should not appear again below it. This does
**not** contradict the finding that style must be stated explicitly even when a
reference is attached (second pass, item 1) — state it **once**, in the lock.

### The anti-slop toolkit `[community]`

The generic-AI-image look is a set of specific, nameable defaults, and each has a
counter you can put in a prompt. This table is engine-agnostic and worth applying on
any image model:

| The tell | The counter in the prompt |
| --- | --- |
| Plastic, over-smoothed skin; the AI "glow" | Name the capture as unprocessed — `RAW`, `unretouched` — and ask for **natural skin texture** |
| Noiseless perfection | `ISO 1600`, `natural film grain visible in the shadow areas` |
| Vague "nice lighting" | **One named source with a position** — *"a single window camera-left"*, *"one overhead fluorescent tube"* |
| Symmetry and perfect centring | *"slightly off-centre, not quite level, candid"* — real photographs are asymmetric |
| Sterile, empty environments | **Environmental imperfections**: dust, a dried water ring, crumbs, clutter, a stain |
| Stiff posing | **Mid-action, not posed** — *"mid-laugh"*, *"hands mid-gesture"*, *"half out of the chair"* |
| Flawless optics | vignetting, chromatic aberration, focus breathing |
| Flat, 2D composition | **depth layering** — a foreground occluder, something out of focus in front |
| Generic colour grading | **Name a film stock** — `Kodak Portra 400`, `Tri-X`, `Fujifilm Classic Chrome` |

Most of this the Karen `STYLE LOCK` already buys. **The four it does not** are the ones
worth adding per-scene, because they live in the *world*, not the capture:

> **environmental imperfection · mid-action instead of pose · off-centre and not-quite-level
> framing · a foreground occluder.**

### ⚠️ Advert vocabulary commissions an advert `[observed 2026-08-26]`

**Camping 5a, round 2.** The prompt asked for a car that was *"immaculate, recently valeted,
water beading on the paint"*, *"glossy"*, on *"wet tarmac holding long smeared reflections"*,
turning its lit front three-quarter toward the lens. What came back was a flawless automotive
commercial — mirror-wet street, empty road, glowing DRLs, perfect bokeh, not a human being in
sight. **Every one of those words is a detailing-advert brief**, and the engine executed it
faithfully.

The prompt also carried the line *"the gloss reads as obscene rather than aspirational."* **A
statement of how an image should be *read* is not an instruction a model can act on** — it draws
gloss and drops the reading. Intent lands on Nano Banana **Pro** only where it is
[a structural instruction](#pro-is-a-different-animal-it-plans-before-it-draws) ("this panel must
rhyme with the previous one"), never as a request for a connotation.

**The counters, in the order that mattered:**

| The advert tell | What to write instead |
| --- | --- |
| glossy, immaculate, valeted, beading water | **A working vehicle**: rain-flecked, road film up the lower doors, salt haze, dirt behind the wheel arches |
| wet tarmac full of long mirror reflections | Wet road, but **broken up** — grit, a drain, worn markings, a patched repair |
| an empty street at night | **Put people in it.** A sterile environment is the named slop tell; one passer-by not looking at anything fixes it |
| hero front three-quarter, centred, lit | **Off-centre, not quite level, partly occluded** by something crossing the foreground |
| a connotation you want the viewer to feel | Nothing. Say what is *in* the frame and let the frame do it |

**And the lighting rule was broken in the same prompt** — it stacked cold sodium lamps, blue-white
tower glass, gold headlights flaring at the lens and warm wash on a wall. That is four ideas, and
[the rule is one key light with a stated direction plus its consequences](#5-anti-slop-restated-from-the-photorealism-pass).
Four sources is how a frame gets *lit* rather than *photographed*.

**Web pass, same date, one addition worth keeping:** the word **`photorealistic` is now noise** —
it appears in so much training data beside CGI and digital painting that it no longer
discriminates, and it averages toward the waxy look it is meant to prevent `[community]`. The
working substitute is the stack we already use: **named camera body, named stock, a stated ISO,
one positioned light, surface imperfection, and asymmetry.** Our house preamble says
*"hyper-realistic documentary photograph"* rather than *"photorealistic"*, which is the right
side of this line already — do not drift back.

Sources: [Why "photorealistic" doesn't work in AI prompts](https://roo.beehiiv.com/p/why-photorealistic-doesn-t-work-in-ai-prompts-and-what-to-write-instead) `[community]` ·
[Nano Banana Pro prompting tips — blog.google](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/) `[vendor]` ·
[Nano Banana 2 — blog.google](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) `[vendor]`

### The root cause, and the one habit to keep

> *"Vague prompts produce vague images, and most people are working from vague prompts —
> borrowed, recycled, entered in a rush with no particular vision behind them."*
> `[community]` The advice that follows is to **start fresh: craft a new brief for each
> creative problem** rather than reusing a saved prompt.

**Read carefully, that is an argument for what we already do, not against it.** Recycling
a *scene* is what produces slop. Locking a *style* is the opposite — it is the thing that
makes a series look authored. **Lock the register; never recycle the shot.**

### Negatives, revisited

The realism literature leans hard on exclusions — *"ask yourself what this image should
absolutely not be. Lens flare. Symmetrical composition"* `[community]` — against Google's
positive-framing house rule `[vendor]`. **The second pass's resolution survives and is now
better evidenced:** negate the *style family* in one short clause, describe everything else
positively, and keep the exclusion list short because long ones dilute. The Karen lock's
single `Exclusions:` line is already the right shape. **Do not add a second one.**

### Which engine for BadCode

The [calibration risk](#the-calibration-risk-nobody-flags) above still points one way, and
this pass reinforces it: NB2's reported failure mode is *"too sharp… too overly
contrast… almost overexposed"* against Pro's *"a lot more natural"* `[yt]` — and
over-sharpened, over-lit, over-contrasted is a fair description of the slop look itself.

> **Working recommendation, `[untested]`: use Nano Banana Pro for Karen plates**, and
> accept the tighter rate limit as the price. The house style is a *suppression* of
> exactly the axis NB2 pushes on. Pro also has the reasoning behaviour that matched-pair
> and sequence panels benefit from, and stronger hex-code handling for palette locks.
>
> **Cheap test:** run one plate on both, same prompt, and look at the skin and the
> highlights. Nobody has done this.

### Sources for this section (2026-08-14)

- [Nano Banana Pro prompting tips — blog.google](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/) `[vendor]` — the Subject/Composition/Action/Location/Style slot order; inline aspect ratio, aperture and grade; *"clearly define the role of each"* reference image.
- [Nano Banana Pro — Google DeepMind](https://deepmind.google/models/gemini-image/pro/) · [Nano Banana Pro announcement](https://blog.google/innovation-and-ai/products/nano-banana-pro/) `[vendor]` — model identity, 14 references / 5 people.
- [The ultimate Nano Banana Pro prompting guide — Atlabs](https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image) `[community]` — the "Thinking" process; *"descriptive, not repetitive"*; keyword spam is dead; role-assigning references.
- [Google Nano Banana Pro complete guide — WaveSpeed](https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026/) `[community]` — Pro plans scene logic; focused short prompts beat long conflicting ones.
- [The anti-slop playbook — OpenArt](https://openart.ai/blog/how-to-avoid-ai-slop/) `[community]` — slop as recycled vagueness; specificity over wishes; exclusions as guardrails; treat outputs as starting points.
- [How to make AI images look like real photos — Miraflow](https://miraflow.ai/blog/how-to-make-ai-images-look-like-real-photos-prompt-tricks) `[community]` — the tell→counter table above: camera bodies, ISO and grain, positioned lights, environmental imperfection, mid-action, optical flaws, film stock, depth layering.
- [How to make AI images look less like AI — Pixova](https://www.pixova.io/blog/how-to-make-ai-images-look-less-like-ai) · [Photorealistic AI image prompts — Artsmart](https://artsmart.ai/blog/ai-image-prompts-photorealistic/) `[community]` — asymmetry and imperfect framing; RAW/unprocessed to counter over-smoothing.

**All `[untested]`.** Same bias warning as everywhere else in this file: only the
blog.google and DeepMind links are `[vendor]`, and the rest sell something.

## Fourth pass — making it obey a reference `[vendor]` `[community]` 2026-08-18

Prompted by Kai on Karen §2j.11, where a reference-anchored plate needed to hold a set
while changing the camera. **Our house habit turned out to be actively wrong** on three
counts.

### 1. Name the job of every image, in the prompt

Google's own tip: with multiple uploads, *"clearly define the role of each"* — their example
is *"Use Image A for the character's pose, Image B for the art style, and Image C for the
background environment."* The community formula is the same idea written out:

> Image 1: main subject or product to preserve exactly. Image 2: character identity / face
> reference. Image 3: pose or composition reference. Image 4: environment or scene reference.
> … Create one final image that keeps the subject from image 1 intact, preserves the face from
> image 2, follows the pose from image 3, uses the environment from image 4.

**The prompt should describe the *relationships between images*, not only the final picture.**
An attached reference with no stated job is a suggestion; an attached reference with a stated
job is an instruction.

### 2. ⚠️ Do not restate what the reference already shows

The sharpest line in the camera-angle literature: **"Your job is not to restate all this. Your
job is to tell it the camera angle."** The foundation image carries the set, the light and the
look for free; a long prose re-description **competes** with it and is a known drift source.

**This is a direct hit on our practice.** Karen's §2j.0 ruling made the Location paragraph the
canon kiosk description *because no reference existed*. Once an accepted still exists, pasting
that paragraph forward **alongside** the still is two authorities on one set. **Rule: reference
attached → the Location slot shrinks to what the reference cannot show.**

Note this also agrees with the photorealism finding that **short specific prompts beat long
complex ones** when the goal is a real-looking photograph.

### 3. Say "keep the same X", never "do not copy X"

The working camera-angle template is positive throughout:

> *"High-angle shot of image 1. Camera positioned above the subject, looking downward. **Keep
> the same snowy environment and gritty style.**"*
> *"Create a Dutch angle shot of image 1. Tilted horizon, subject in foreground, background
> slightly blurred, **same lighting and environment**."*

**Our refusal block — *"do not copy its camera angle, its framing, or the woman's pose"* — is
negative prompting**, which [does not work here](#negatives-revisited) and puts the thing we
are refusing into the prompt. The replacement is a three-way split, all positive:

| Bucket | What goes in it | How to write it |
| --- | --- | --- |
| **Keep** | the set, the identity, the design, the look | *"Keep from image 1, exactly: …"* |
| **Change** | the camera, the time of day, the weather, who is on screen | *"Change from image 1: it is now night; the camera is inside the kiosk"* |
| **New** | what no reference shows | the Location slot, kept short |

Stating the change as a change is what stops it inventing a *different place* — the model is
told the location is the same and only the listed facts differ.

### 3b. ⚠️ Role labels do not make a second reference free — **house rule: one reference**

The literature says two references are fine when each has a **declared, non-overlapping** job,
and the "third opinion" warning is really about references *silently competing* for one job. All
true. **Kai ruled against it anyway for BadCode, 2026-08-18:** *"just describe the camera angle —
too much extra info/images in the prompt seems to mess it up."*

**That is consistent with the length finding**: a second image is more input competing for the
same attention, and a role label does not buy it back. **Default to one reference and describe
the rest**, reaching for a second only when the thing being transferred cannot be written down
(a face, a texture, a specific product).

The field formulation is still the one to keep for whatever *is* attached: **"the prompt should
describe the relationships between images"**, because *"Nano Banana Pro is good at inference —
your job is to reduce the number of bad inferences it has to make."*

### 3c. ✅ Name where the photographer stands, not what the shot looks like

**The counter to the set-rebuilding trap, and it is cheap.** *"A wide shot from across the
pavement"* is an abstract framing, and the model satisfies it by building whatever space it
needs. *"From the pavement a few steps in front of the kiosk, standing under the scaffolding,
camera at knee height"* is **a position that either exists in the reference or does not** — and
the model can check it against the picture it was handed.

Pair it with a named focal length: it fixes the perspective, straightens verticals, and bounds
how much world has to be invented.

**✅ The same trick works on subjects, not just cameras.** *"Further down the pavement"* is a
direction, and the model treats unclaimed space as free — Karen §3a.1 round 2 put a figure in the
road. *"On the pavement beside the subway entrance railings, between the kiosk and the green
globe posts"* is **a spot that exists in the attached reference and can be checked against it.**
Place people the way you place cameras: by landmark, not by vector.

### 🔴 `[confirmed 2026-09-09]` A reference carries a face only at the size the face is *in* it

**Camping 7e.** A close-up was built by attaching an accepted **wide two-shot** and stating its
job as *"the man's face, his hair and his clothes, and the room, the light and the colour."*
The room came back right. **The face changed.**

**The mechanism is arithmetic, not model behaviour.** In the wide, his head is a small part of the
frame. Asked for a chest-up portrait, there is nothing in the reference to *enlarge* — so the
engine invents the detail, and inventing detail on a face is changing the face.

> **The rule, and it is the missing half of [§2's "do not restate what the reference already
> shows"](#2--do-not-restate-what-the-reference-already-shows):** a reference only counts as
> carrying a thing if that thing is **roughly the size in the reference that it will be in the
> output**. **Going closer than the reference is the failure case.** Same size or wider is fine.

**It also sharpens the casting rule** — *cast a Character when the face is the shot, use
references when it isn't* — into something checkable: **compare the two framings before choosing.**
If the output is tighter on a face than the reference is, the reference will not hold it, and the
identity has to come from a Character or from a tighter reference.

**Two cheap fixes when no Character exists** (the therapist's case — she was invented in one
still and has no Character):

1. **Crop the reference to the face and attach the crop.** Same pixels, but the face now fills the
   frame it is being read from. Flow's [crop tool](#what-flows-image-surface-actually-gives-you)
   makes a new image and keeps the original in history. Zero generations — **try this first**.
2. **Make a Flow Character from the accepted still.** Permanent, and worth it the moment a
   character is going to appear more than once.

⚠️ **And the trade runs the other way for the *set*.** Dropping the reference to cast a Character
means the room goes back into prose, which the
[supersede-the-prose rule](#7--write-the-keep-list-from-the-accepted-still-not-from-the-prose-that-made-it)
warns against. **Take that trade.** A plain wall, a window and a radiator are forgiving and
re-describable; a face is neither. **Lose the room before you lose the face.**


### 🎯 Making a subject small: put something *else* in the Subject slot `[community]` 2026-09-09

**The engine hero-frames whatever you name first.** Write `Subject: an ordinary estate car…` and
you get a car, centred, filling the frame — however carefully the composition slot then argues for
small and off to one side. [Earlier clauses win when instructions compete](../flow/README.md), and
`Subject` is the earliest clause there is.

> 🔑 **The fix is to name the real subject of the picture, which is often not the object the
> story is about.** For camping 3c — a crash scene where the car should be barely visible at the
> frame edge — the Subject slot is **the wet road surface**, and the car is demoted into the
> composition as a thing at the edge. The slot order does the work no adjective could.

**Two supporting levers from the same pass** `[community]`:

- **State placement as explicit layout**, in the vocabulary the guides use: *"subject in the lower
  left third of frame, large expanse of empty road above and to the right, generous negative
  space as a compositional element."* Vague *"off to one side"* loses to the centring prior;
  a named third does not.
- 🔴 **Describe the empty part in detail, because the model fills empty space.** *"Add
  environmental specificity by describing the background in detail instead of leaving it
  generic."* An unspecified expanse is an invitation to invent something to put in it —
  **the same mechanism as [the set giving way to whatever the shot
  requires](#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set), seen
  from the composition side.** So the emptiness gets grit, a patched repair, a puddle, a worn
  line: occupied by specified texture rather than by invented content.

**Sources:** [Mastering negative space in AI image prompts — PromptAtlas](https://www.getpromptatlas.com/keywords/negative-space-techniques) ·
[Composition and framing terms for image prompts — Prompt Architects](https://prompt-architects.com/blog/461-composition-and-framing-terms-for-image-prompts) ·
[AI image composition tips — ZSky](https://zsky.ai/blog/ai-composition-tips) `[community]`


### 4. Slots: fewer is better, and order matters

**Up to 14 references, but only about 6 at high fidelity** — and the field advice is to
*"begin with 2 to 4 images, not 10-plus. More references only help when each one owns a
distinct role."* Put whatever must survive in the earliest slots. For us that is nearly always
**two**: the accepted still, and the Flow Character.

### 5. Anti-slop, restated from the photorealism pass

Two of these are new and both bear on night exteriors:

- **⚠️ Do not stack lighting ideas.** The named tell is *"a glowing face, a dark background, a
  bright window, a rim light, neon reflections and a golden sunset all somehow happening at
  once."* **One key light with a stated direction, plus its consequences.** Practicals are
  allowed if they are bounded to a job — *"one small point of colour, too weak to light
  anything."*
- **Prompt the capture, not the beauty** — *candid, documentary, unposed, imperfect
  composition, lived-in, realistic skin texture*. Already the §1 `STYLE LOCK`'s job for Karen.

### 6. ⚠️ If the camera cannot physically stand there, the model rebuilds the set `[observed]`

**The strongest reference-drift cause found so far, and it does not look like a reference
problem.** Karen §2j.11 round 2 (2026-08-18) asked for a camera *"inside the kiosk, in the
corner beside her"* on a reference showing an **open-fronted booth one person wide.** The shot
is physically impossible in that booth, so Nano Banana **enlarged the booth** — three walls, a
ceiling, room to stand back — and once the room was bigger, the wardrobe and the weather went
too.

**Check the requested camera position against the physical set before writing it.** A position
a human could not occupy is an instruction to rebuild the world, and it will be obeyed at the
reference's expense. The fix is nearly always a legal position a foot or two away.

**⚠️ To remove something, remove its noun from the keep-list.** Karen §3a.0 round 2 (2026-08-18)
asked for a frame without scaffolding while the setting clause still said *"the same pavement
scaffolding with plywood hoarding"* — carried forward because the reference does have it.
**Anything named in a keep-list is an instruction to draw it**, wherever the camera happens to be
pointing. Keep-lists are per-shot, not per-set: name only what this frame contains.

**⚠️ And it catches *space*, not just positions and surfaces** (Karen §2h.7, 2026-08-18). A low
wide shot *"from across the pavement, with the building above rising out of frame"* needs room
the canon corner does not have — scaffolding on the near side, a subway entrance immediately
behind. **The model moved the kiosk onto an open plaza where the picture was possible.** Third
sighting of one rule: **the set gives way to whatever the shot requires.** Before writing a
framing, ask where a photographer would have to stand and whether that spot exists.

**The fix when the framing is wanted anyway: name a narrower lens.** 28mm instead of an implied
ultra-wide keeps the angle, straightens the verticals (bending buildings are a slop tell), and
**gives the model less world to invent**, which is the actual cure.

**⚠️ The same trap catches surfaces, not just camera positions** (Karen §2h.6, 2026-08-18). The
prompt asked for the street *"reflected in the glass in front of her"* while the camera stood at
the kiosk's **open front** — there is no pane there. **A shot that needs a surface the set does
not have is an instruction to build the surface**, in that case a glass door on a doorless
booth. Reflections, shadows cast on walls, light through windows: check the thing exists before
asking it to do something. And **state the geometry positively** — *"the front of the kiosk is
open, with no door and no glass across it"* — because a set fact left unsaid is a set fact the
model gets to decide.

### 7. ⚠️ Write the keep-list from the accepted still, not from the prose that made it

Same shot, second cause: the keep-list said *"glazed on three sides, a hinged door"*, carried
forward from the prompt that **generated** the reference. The generated image has neither.
**Picture and words disagreed and the words won** — which is the same lesson as §2 above, seen
from the other side.

**Any canon-prose description of a set is superseded the moment a still of that set is
accepted.** Re-read the picture and describe what is actually in it.

### 8. Small rules that fell out of the same failure

- **Do not change hair and wardrobe in one pass** — together they drift more than either
  alone — and put *"keep the same face, pose and background"* **before** any clothing
  description. Better still, **add no garment nouns at all**: one new coat invited a whole new
  outfit.
- **State the weather even when there isn't any.** Night + New York + a coat produced snow that
  nothing had asked for. *"The pavement is dry and the air is clear."*
- **Whatever the shot is *about* goes in the keep-list**, not mid-paragraph in Action. A woman
  on hold who is not holding the phone is a lost frame.
- **Prompt length is negatively correlated with adherence** — measured across ten text-to-image
  models, not folklore. When a reference is doing the heavy lifting, **cut the scene down and
  drop the slot labels**; most of what the slots were carrying is already in the picture.

### 9. ⚠️ A strong reference hedges its own change-list `[observed]`

**The cost of the fixes above, and it arrives the moment they start working.** Once a
reference is genuinely driving the image, **it also becomes the baseline every change is
measured against, and it wins the ties.** Karen §2j.11 round 3 (2026-08-18) held the set, the
wardrobe and the identity perfectly and then met all three of its changes halfway: *"it is now
night"* came back as blue hour, *"the camera is close to her"* came back at the reference's own
distance, and the reference's alert pose survived an instruction to look away.

**Change instructions need magnitude and consequences, exactly like weather nouns.** This is
[the snow lesson](omni-flash.md) reappearing on the image side:

| Hedged | Renders |
| --- | --- |
| *"it is now night"* | *"the sky is black, every window above is dark, the shopfronts are unlit and shuttered, the only light is the street lights"* |
| *"the camera is close to her"* | *"she fills the frame from the top of her head to her waist"* |
| *"she is not looking at the camera"* | *"she looks out past it, down the street, at nothing in particular"* |

**And state framing, not camera position.** *"Two feet from her"* is a fact about a tripod
nobody can see; **what fills the frame is the only thing the model can actually draw.** Camera
*position* language works when it changes the visible geometry (low, from behind, from the
doorway); camera *distance* language should always be converted to a crop.

### 10. ⚠️ The atmosphere family is rendered for free and overdelivers when named `[observed, n=3]`

**Kai, 2026-08-18, on a reflection that would not go away: *"it seems to do it naturally when
you don't ask."*** That is the rule.

**Reflections, dust, steam, haze, bokeh** are everywhere in the photography these models learned
from, so they arrive unasked and at a believable strength. **Name one and it stops being a
property of the scene and becomes an effect applied to the shot** — dust filled the whole frame
in Karen §2j.9v, and a named reflection came back as a double exposure smeared over the
subject's face in §2h.6 **even after the camera had been moved to a genuine pane of glass.
Moving the camera did not help, because the instruction was the problem.**

**The counter-move is deletion, not moderation.** There is no *"faint"* or *"subtle"* setting;
say nothing and take what the engine gives you.

**Mirror image: weather nouns underdeliver** and need magnitude and consequences pushed at them
(*"a full storm, not a light dusting"*; shadows thrown right across the carpet). **Atmosphere
needs deleting; weather needs shouting at.** The two instincts are opposite and both are
counter-intuitive, which is why this keeps being relearned.

### 11. ⚠️ A camera position without a background is half a shot `[observed]`

**Karen §2h.6, 2026-08-18 — *"what camera shot is this supposed to be, because it is showing
multiple."*** The prompt said where the camera stood and never said what was behind the subject,
and the engine filled the background with **everything available at once**: through the near
glass, past her, through the far glass, plus the near panel's reflection. Four layers in one
frame, which reads as a double exposure rather than a photograph.

**An undefined background stacks, the same way an undefined surface grows text.** One sentence
fixes it — *"behind her is one soft out-of-focus background and nothing else"* — and it is worth
naming what stays sharp, because *only the subject is sharp* is the instruction that collapses
the layers.

**Watch for this wherever the subject is inside something transparent**: vehicles, kiosks,
shopfronts, conservatories, anything shot side-on through two panes.

**And name the shot type.** The documented camera form is *"[shot type] of image 1"* — *"a
medium close-up in profile"* is a framing the model knows; *"the camera has moved round to the
side and is close"* is a description of a tripod, and it renders as one.

### 12. ⚠️ A Character binds to a face. No face in the shot, no likeness `[observed]`

Obvious once said, and it cost a generation. Karen §3a.1 round 1 (2026-08-18) attached
`@Aarron` to a shot specified as *"seen from behind… only a sliver of the side of his face"* —
**and the likeness did not appear, because there was nothing for it to appear on.**

**Design the shot and the Character attachment together.** An anonymising framing — from behind,
silhouetted, face out of frame, too small to read — is a decision to **not use the Character**,
and that is legitimate as long as it is a choice.

**⚠️ Corollary, and it cost two more generations: describing the person in prose overrules the
Character.** Karen §3a.1 rounds 1–2 wrote *"a hoodie, a jacket and trainers with a small
backpack"* into shots with `@Aarron` attached — **and his canon look is a patterned crewneck and
a wearable keyboard rig.** The prose won, so he came back as a different man each time. Our
character files already carry the rule (*"scene blocks describe the shot only"*); it is worth
restating here because the failure looks like *Character binding is unreliable* when it is
actually *the prompt was arguing with it.*

**The reliable configuration is two sources agreeing**: the Character attached **and** the person
present in the attached reference still, with **nothing about their appearance in the text**.
That is why Karen has never drifted in this film and Aarron drifted every time.

**When a character must be recognisable without a face, give them one load-bearing object** —
Aarron's rig identifies him from behind — and name the object, not the outfit. The consistency guidance asks for a reference
that *"clearly shows the face"*; the same holds on the output side.

### 13. ✅ Prompt order for camera work: **angle → lens → composition → lighting → style**

The field convention, and it matches what has worked here: **set the spatial rules before adding
any detail.** Composition instructions written after lighting and style tend to lose. Pairs with
naming the photographer's standing position — angle first, and make it an angle a person could
occupy.

### 14. ✅ Long lenses are under-used and hard to fake `[community]`

**Telephoto compression stacks foreground, midground and background together** and isolates the
subject; 135mm is the workhorse, 200mm+ is extreme. Two reasons it earns a place in an anti-slop
kit:

- **Nearly all AI street imagery is wide.** A compressed frame reads as a lens choice somebody
  made, which is most of what "cinematic" means.
- **It is motivated whenever the subject is unaware.** *"Telephoto lenses work well for candid
  street shots where you want distance between camera and subject"* — so it carries story as well
  as look, which is the only kind of style decision worth making.

### 15. ✅ If the setting keeps coming back wrong, check whether the shot needs a setting at all

Karen §3a.2a burned four rounds and a location turnaround trying to render a street corner from a
viewpoint the reference had never seen. **The shot was a long lens wide open — at which point the
entire background is out of focus and none of that geometry appears in the picture.**

**Ask what actually has to be sharp.** Anything soft does not have to be accurate, and
**describing it as a blur is strictly easier than describing it correctly**: a blur has no
geometry to get wrong. This inverts the usual instinct, which is to specify harder when a frame
comes back wrong.

Applies wherever a shot has a shallow-focus excuse: long lenses, wide apertures, night, rain,
distance, foreground occlusion.

### 16. ✅ Natural language beats camera data for optics `[community]`

Testing found *"a telephone with a shallow depth of field"* produced the effect more reliably than
f-stops and focal lengths. **These models parse description better than specification.** Keep the
focal length when the *perspective* matters (compression, distortion), but say *"thrown completely
out of focus"* rather than trusting `f/2.8` to deliver it.

### 17. ⚠️ Light streaks need lights — the lighting has to permit the technique `[observed]`

Karen §3a.2a spent three variants (long exposure, bokeh, zoom burst) trying to get *"streaks of
light"* out of **flat overcast mid-morning**, which has no point sources in it. The engine was
right and the prompt was wrong: **a long exposure of a grey street gives grey smears.** Bokeh
discs, light trails and flare all need lamps, headlights, neon or specular highlights to exist.

**Check the light before choosing the technique.** If the effect needs sources the scene does not
have, the fix is to change the *time of day*, not the prompt — or to isolate with **exposure**
instead of focus (underexpose ambient, light the subject) which works in any light.

### 20. 🔴 If the named source cannot physically light the scene, the model invents fill `[confirmed 2026-08-27]`

Camping **9a**, twice. A yurt interior lit by *"a cluster of candles on the rug, and nothing
else"*, with the falloff written out at length — *"steeply from below, shadows thrown upward,
above chest height everything falls away"*. **Both rounds came back with a soft even frontal
fill from nowhere**, an evenly-lit lattice wall and a fully readable roof. Not one upward shadow
in either frame.

**This is [§6](#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set-observed)
in the lighting domain.** Candles on a floor cannot light a room full of people, and the engine
resolves the contradiction between *"a visible room full of people"* and *"only candles"* the
same way it resolves an impossible camera — **by rebuilding the scene so the request becomes
satisfiable.** It adds the light the picture would need.

**So more falloff language does not help, and that is the trap** — the wording was not the
problem and rewriting it harder spends rounds. **Give the light a source that could plausibly do
the job, or shrink what needs lighting.** For 9a: a wood-burning stove low on one side, which is
standard in a glamping yurt, lights every face from one low angle, leaves the far half of each
face dark and gives the roof nothing. The candles then stay as a **bounded practical** — *"small
points of flame, far too weak to light anything"* — which is [§5's](#5-anti-slop-restated-from-the-photorealism-pass)
own phrasing for a practical that is allowed because it has a job.

**The general rule:** a lighting instruction is a physics claim. If the physics does not close,
the engine closes it for you.

### 24. 🔴 On a POV shot the reference's **body position** is inherited, whether or not you asked `[observed 2026-08-28]`

Camping **11b(i)**, round 2. The prompt asked for a **standing, walking** first-person POV and
attached the accepted 10a frame *"for the place, the weather and the light"*. 10a is a POV from
**inside a tent, lying down** — its defining composition is a man's legs and sleeping bag
stretching away toward a doorway. **The frame came back with his legs stretched out in front of
him as though he had fallen over.**

**Nothing disobeyed.** [§9](#9--a-strong-reference-hedges-its-own-change-list-observed) says a
strong reference is the baseline every change is measured against and wins the ties; the engine
was handed two authorities on where the body goes and took the picture.

**Rule: a POV reference is never "just the location."** It carries camera height, view direction
and **posture**, and posture is the one nobody writes down. Before attaching a reference to a POV
shot, ask what body it is teaching.

**The fix that works is geometric, not adjectival.** *"He is standing"* is a statement about
someone the camera cannot see. *"The nearest thing in the picture is wet tarmac about a metre
ahead of him, so the whole bottom edge of the frame is wet ground"* is a fact the engine can
check — **and if the nearest ground is a metre away there is nowhere to put a pair of legs.** Same
shape as the camera-height lesson: ignored as a number, obeyed as a consequence.

**And delete the anchor that the wrong body grew from.** Round 2 kept a boot at the bottom edge to
lock the POV; that boot is what the legs attached to.
[§18](#18--their-face-is-not-visible-does-not-hide-a-face-only-geometry-does-confirmed-2026-08-27)'s
escalation generalises — *a body part that is not in the picture cannot grow.* Hands alone lock
first person; the boots were never needed.

### 22. ⚠️ Tiling and cloning in crowd scenes are a *resolution* problem, not only a prompt problem `[community 2026-08-28]`

Researched for camping's ruined-car-park wide — a frame containing a hundred shelters and a
hundred figures, which is the exact input that produces this.

**The named failure:** *"tiling artifacts appear as repeating patterns — a face pattern repeating
across a crowd, wallpaper-like repetition in textures, or structural elements that clone across
the image."*

**The primary cause is resolution mismatch** — generating well above the model's native resolution
*"forces the model to tile its learned patterns"*. The secondary cause is an ambiguous count in
the prompt.

🔑 **This cuts against our standing "always 2K or 4K" habit, and the trade has to be made
per-shot.** [`image-prompting.md` §5](../flow/image-prompting.md) says go high whenever a word
must survive; this says going high is what makes a crowd repeat. **On a frame that is both — a
crowd *and* a legible sign — the sign occupies a small region and the crowd occupies most of the
frame, so 2K is the safer default and the sign is the thing to check first.**

**The prompt-side counter, restated positively** (the community advice is a negative prompt, which
[does not work here](#negatives-revisited) and puts the thing you are refusing into the prompt):
**name the variety and name the counts.** *"No two shelters alike — different sizes, colours, ages
and states of collapse"* does the work that `duplicate, clone, tiling` cannot.

### 23. ✅ Fresh web advice usually arrives as negatives. Convert it before use `[2026-08-28]`

Three separate sources this session gave their best guidance as negative prompts — *"no warped
buildings, no melting objects, consistent architecture"*, *"duplicate, multiple, clone, tiling"*,
*"no fantasy style"*. **On these engines that is the one construction guaranteed to backfire.**

**The habit: read the negative for the failure it names, then write the positive consequence.**
*"No warped buildings"* → *"the buildings are square and true, their rooflines straight and
unbroken."* This is the same move as writing camera height as what it does rather than as a
number, and it should be applied to every piece of borrowed advice before it reaches a prompt.

### 21. 🔴 A multi-part change to one object loses outright to a reference showing it intact `[observed 2026-08-28]`

Camping **10a**, round 1. The reference showed a clean lit supermarket fascia. The prompt asked
for it broken in **five parts at once** — cracked tubes, one letter hanging from a bracket, one
fallen away, a paler scar on the panel behind it, and two named letters still lit. **Every part
was ignored and the reference's sign came back untouched and brighter.**

**This is [§9](#9--a-strong-reference-hedges-its-own-change-list-observed) past its limit.** §9
says a strong reference *meets a change halfway*; that holds for a change with one axis
(*"it is now night"* → blue hour). **A change with five sub-clauses on one object does not get met
halfway — it gets dropped**, because there is no halfway state for the engine to find. The other
four changes in the same prompt, each a single fact, all landed.

**Rule: one object, one new state.** *"The sign is dead — unlit, grimed, no colour"* is a state
the engine can hold. A per-letter reconstruction is a compositing job described in prose.

**And the second-order rule, which is the expensive one:** if the detail genuinely matters,
**it has left the generator's lane.** Camping moved the W-AI-trose gag to a post comp on the
second failure rather than a third prompt — load-bearing text was already
[`image-prompting.md` §5](../flow/image-prompting.md)'s call, and this is the same boundary seen
from the failure side.

### 25. 🔴 §19 inverts for an UNBOUND body part — describe it or get young, clean and generic `[observed 2026-08-29]`

**§19 says a cast Character or an attached reference means no appearance description at all.
The opposite case is a body part with nothing bound to it, and it obeys the opposite rule.**

Camping `12c` is an insert: a hand entering frame to drop a newspaper on a fire, no face, no
body, **no Character cast** — there was no identity for one to hold. The prompt described the
hand by **position and action only** — *"a man's hand and forearm, palm down and fingers open,
just having let the paper go. His sleeve is soaked."*

**What came back was a hand in its twenties** — pale, smooth, unblemished, short clean nails —
**in sharp focus despite an explicit `thrown out of focus`**, splayed flat in a presenting
gesture. On a character who has lived outdoors in a camp for five years it contradicted the
entire act.

**The fix was the §-4a move applied to a hand: describe it as anatomy and condition, not as
position.** Thick-knuckled, weathered and reddened, cracked across the knuckles, dirt engrained
in every crease and under short broken nails, scarred and hairy, a frayed soaked cuff — plus the
gesture rewritten from *held flat and open* to **loosely curled and falling open**. **Round 2
landed it first time.**

| Case | Rule |
| --- | --- |
| Character cast, or reference attached | **§19** — no appearance description at all. Action and expression only |
| **Body part with nothing bound to it** | **This section** — describe it fully as anatomy and condition, or the default arrives |

🔑 **The default is not neutral, it is young, clean, symmetrical and middle-class.** Anywhere our
work needs a body that has had a hard life, silence gets us the opposite of the story. Treat an
unbound hand, forearm, neck or boot as **a prop that must be dressed**.

---

### 26. ✅ TWO Characters DO hold in one frame — if each is anchored to a named side `[observed 2026-08-30]`

**This overturns a working assumption, so it is worth stating plainly.** The field position we
had recorded was *"two characters interacting in the same shot still produce identity blurring on
every platform as of mid-2026"* — features blending between them, faces swapping, or one identity
lost. **Camping had been redesigned twice to avoid it.**

Camping `12a` put `@Bob` and `@Future-Tarquin` in one still — two faces, both legible, both lit by
the same fire — **and both identities held.** Accepted by Jack.

**Four things were true, and we do not yet know which are load-bearing:**

| Condition | Grade |
| --- | --- |
| **Each Character anchored to a named side of the frame** — *"on the left of the frame… on the right of the frame"* — rather than left to the model to infer | 🔑 The one we believe did the work. It is also the field's documented fix, and it agrees with Google's own Ingredients guidance to **state the role each reference plays** |
| A **still**, not a clip — identity holds for one frame, not through motion | Likely load-bearing. `2b` needed Veo 3.1 for two faces *through motion*, which is a different problem |
| The two men are **visually very unalike** | Named by the sources as what keeps identities separate |
| **No appearance description for either** (§19) | Standing rule; not specific to this case |

⚠️ **What this does NOT license.** One accepted still is not a rule for clips, for more than two
Characters, or for two similar-looking faces. **The claim is: two unalike Characters, side-anchored,
in a still — observed once, worked once.**

🔴 **Order of attachment mattered enough to record:** both Characters in the earliest slots,
the location reference last.

**Cost of the old assumption, so the saving is visible:** `8b` was pushed to a forty-metre long
lens specifically to keep two faces out of one frame, which took the faces out of the argument.
That retreat may not have been necessary.

⚠️ **`out of focus` on a foreground element is weakly obeyed and needs reinforcing** — round 1
ignored it outright. Round 2's *"thrown completely out of focus so that it is a soft blur"* held.

### 27. 🔴 Ask for an object, never an absence — a subtractive shape comes back **inverted** `[observed 2026-08-30]`

Camping `1a-year` asked for the numerals **2 0 0 8 torn out of an overcast lid — holes in the
cloud showing pale sky behind, not writing, not light, not projected.** The clause said what it
was not, three ways, and restated *"the cloud has simply parted in that shape."*

**What came back was the exact inverse: four dark soot-coloured shapes sitting *on* the cloud** —
smoke writing, which is the one thing the shot was designed to avoid.

🔑 **The cause is not disobedience, it is vocabulary.** The model has no trained visual for *an
absence shaped like a glyph*; it has a large one for *smoke written across a sky*. Given a shape
it can only render as a positive, it renders it as a positive and picks the trope it owns. Piling
on more negations does not help — it has nothing to substitute *toward*.

⚠️ **A second, independent failure rode along, and it is worth checking for separately:** the
device was **self-defeating on contrast**. A hole in flat grey overcast shows *pale grey sky* —
almost no separation. The prompt had also banned glow and bloom, so the only route left to make
the shape legible was to make it **dark**. **Before blaming the wording, check whether the frame
physically contains the contrast the instruction needs.** If it does not, no phrasing fixes it.

**The rule:** state the thing as **a positive object with a material, sitting on a ground that
contrasts with it.** Camping's fix moved the same four numerals from *holes in cloud* to *matted
black river weed lying on pale wet mud* — additive, material named, ground named, contrast
guaranteed by the ground reflecting the sky.

**Related:** §23 (convert negatives into positives before use) — this is the sharpest case of it
found so far, and it upgrades that entry from a phrasing preference to a **failure mode**.

### 28. ⚠️ Ground-plane lettering breaks where it foreshortens — and the model under-delivers height `[observed 2026-08-30]`

Camping `1y` asked for four numerals laid flat on a foreshore, shot from **five metres up at a
45° down tilt**. The return came back nearer **two to three metres at ~30°** — a consistent
under-delivery of both height and tilt, worth budgeting for on any stated camera elevation.

**The consequence is specific and predictable:** a shallower angle puts the glyph row into hard
perspective, and the numeral **furthest from the lens compresses most**. Three of the four
rendered clean; the far one — an `8` — had its waist open into two disconnected pieces and read
closer to `%`.

🔑 **So when in-frame text lies on the ground, the fix for a malformed glyph is usually the
camera, not the text clause.** Steepen the tilt until the row is near-flat to the lens and the
compression that broke it is gone. Ask for more height and more tilt than you want, since some
of it will not arrive.

**Pair it with a closure clause** naming the specific failure — *each numeral is one continuous
unbroken band, the eight is two closed loops joined at a clear narrow waist* — the same
name-the-failure pattern as camping `4b`.

### 29. ✅ To overrule a reference on ONE element: declare its role narrowly, then negate the old value `[observed 2026-08-30]`

§21 says a reference showing an object intact **beats** a multi-part change instruction to that
object. Camping `4y` had to run straight at that: the same foreshore plate, everything held, but
the four weed numerals changing from `2008` to `2026` — one object, and it *is* the change.

**It worked first time.** Two clauses appear to be why, and they are cheap to reuse:

1. 🔑 **Declare the reference's role narrowly and exclusively** — *"the attached image is the
   reference for the location, the camera position, the framing and the light, **and for nothing
   else**."* Then list what to reproduce from it, item by item. The element you intend to change is
   conspicuously **not on that list**, which is what stops the reference claiming authority over it.
2. 🔑 **State the new value early and positively, then negate the old one explicitly** — *"They
   read 2 0 2 6. They do not read 2008."* Naming the old value is what makes the negation
   actionable; without it the model has nothing to push against.

**Everything else in the frame was left to the reference and came back matching** — far bank,
stumps, cobbles, handrail, horizon, overcast and water level all held well enough that the two
plates read as one place. So this pattern does **not** cost you the reference's grip on the rest of
the frame, which was the obvious worry.

**Use it wherever a reference has to be overruled on exactly one element.** n=1, so it is a
pattern, not a law — but it is a cheap first thing to try before falling back to a full
restatement.

### Fifth web pass — 2026-09-08 `[community]`

Two sources, run against the camping `8b-fog` failures. **Most of it corroborates findings this
file already reached from production, which is the useful part** — independent arrival, not news.

- 🔑 **"Adjectives do not render."** Replace every load-bearing adjective with a visual fact or a
  comparison. **This is [§30](#30--a-physical-analogy-overrules-a-stated-number--and-it-is-how-28-keeps-happening-observed-2026-09-08)
  and [§33](#33--an-unresolvable-colour-brief-is-settled-by-the-engines-strongest-object-prior-observed-2026-09-08)
  arrived at independently**, and it is the shortest statement of the habit this whole file keeps
  rediscovering: *describe the picture, never the rule.*
- **Pro plans composition before it paints, and *"the more it knows about the job, the sharper its
  planning step gets."*** The job sentence at the top of our prompts is feeding the reasoning pass,
  not decorating it. Keep it concrete and keep it first.
- ✅ **Negatives belong in a terminal, scoped constraint block** — *"no other props, no hands, no
  visible brand logos, no harsh specular hotspots on the metal"* — **not floating in the body.**
  This squares §27 and §31 with the fact that our markings constraint has always worked: an absence
  fails as a *subject*, succeeds as a closing constraint attached to named things.
- **Prompt shape:** seven slots — subject · action · setting · style · composition & camera ·
  lighting & colour · constraints. A superset of what we already use.
- ⚠️ 🔴 **"One or two imperfection words per prompt, three max — over-correction makes images look
  intentionally degraded."** **Contradicted by our own measurement:** camping A9's twelve-plus
  imperfection tarmac clause was the single strongest anti-slop element in the frame and delivered
  exactly as designed. **Not adopted.** Logged as `[community]`, unverified against our work; the
  working compromise is roughly four, and the real rule is probably *specific to the subject, not
  counted*.
- **`photorealistic` remains noise** — restated by both sources, consistent with the 2026-08-14 pass.

Sources: [Nano Banana Pro prompting guide — fal](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide) `[community]` ·
[Creating AI images that don't look like AI — usetoolai](https://usetoolai.com/blog/how-to-create-ai-images-that-dont-look-like-ai-2026) `[community]`

🔴 **One piece of their advice we reject outright:** both slop guides recommend prompting for
*"rule of thirds"*. [`cinematography/evidence.md`](../cinematography/evidence.md) grades it a
**myth** — no supporting study, and the measured priority is motion, faces, and lines that lead to
a subject. **Compose lines onto a subject instead of onto a grid intersection.**

### 30. 🔴 A physical analogy overrules a stated number — and it is how §28 keeps happening `[observed 2026-09-08]`

Camping `8b-fog` A9 asked for a camera *"raised about seven metres above the tarmac **as if
standing on the roof of a van**, sixty metres back."* It came back at roughly **two to three
metres**, barely tilted — which is exactly the height of a van roof.

🔑 **The engine did not ignore the elevation. It obeyed the wrong half of the sentence.** A number
is an abstraction; *the roof of a van* is a picture the model already owns, and given both it
draws the picture. **Second confirmation of [§28](#28--ground-plane-lettering-breaks-where-it-foreshortens--and-the-model-under-delivers-height-observed-2026-08-30)'s
height under-delivery, with a mechanism attached: check every analogy for the value it smuggles
in.** An analogy chosen to make a number vivid will quietly replace it.

**The fix is the file's standing habit — describe the picture, never the rule, and here never the
number either.** State what a camera at that height *sees*: the roof panel of the car as a flat
shape, a tent dome as a full oval rather than a hump, figures seen from above the level of their
heads so shoulders are wider than feet. Those are facts the engine must satisfy geometrically.

### 31. 🔴 §27 catches the OUTPUT FRAME too: "no letterbox bars" produces letterbox bars `[observed 2026-09-08, n=3]`

Camping `8b-fog`, three consecutive runs, each asking *"Fill the whole frame with the photograph,
with no black bars, no letterbox borders and no white margin of any kind."* **All three came back
matted.** This was logged twice as *"unverified whether it is the model or Flow's output framing"*
— it is neither. It is
[§27](#27--ask-for-an-object-never-an-absence--a-subtractive-shape-comes-back-inverted-observed-2026-08-30)
firing on a part of the image nobody thought of as content.

⚠️ **And the same prompts commissioned the matte in their own opening words.** *"A still
photograph **for a film**"*, plus *"documentary press photograph"* and *"16:9"*, is a brief for a
**cinematic still** — and a cinematic still has bars. The negation was arguing with the subject line.

🔴 **DOWNGRADED 2026-09-08 — the fix was tried and FAILED.** Camping A7b deleted both the negation
and the words *"for a film"*, and the bars came back regardless: five consecutive mattes. **The
causal claim above is not supported.** *Never negate the frame in prose* survives as good practice
for [§27](#27--ask-for-an-object-never-an-absence--a-subtractive-shape-comes-back-inverted-observed-2026-08-30)
reasons; the letterbox explanation does not.

🔑 **The live hypothesis now points away from the prompt.** An accepted plate banked weeks earlier
from an unrelated prompt carries **the same bars with the same thin white inner line**, and every
sample under review is ~1240×695 — an odd size that indicates **a screenshot of Flow's viewer, not
a downloaded original.** ⬜ **Test before writing another word about it: download the original and
read its dimensions.** If it is 2K and clean, the matte is Flow's UI, not the model.

### 34. 🔴 Naming a marque renders its badging, and no downstream constraint removes it `[observed 2026-09-08]`

Camping A7b named *"a large black BMW coupe-SUV"*, then stated the badge was too small to resolve
and banned all lettering, script and numbers on the car in the Constraints block. **The roundel came
back crisp and gained legible model script beside it** — more readable than the round before.

**The marque name carries the badging inside the prior, and a ban arriving later loses to it.**
Same shape as [§27](#27--ask-for-an-object-never-an-absence--a-subtractive-shape-comes-back-inverted-observed-2026-08-30):
**you cannot subtract, only substitute.** There is no phrasing that names a brand and suppresses
its emblem.

**The three real options, cheapest first: paint it out afterwards** (a small still, seconds, exact);
**turn the surface out of legibility** with geometry; or **drop the marque and describe the body
shape only**, accepting silhouette drift. ⚠️ **Do not spend generations on it** — the badge is a
thirty-second post fix and a re-roll risks whatever else the frame got right.

### 32. 🔴 Weather is a physics claim, exactly like light — falling rain needs something dark to fall against `[observed 2026-09-08]`

Camping `8b-fog` A9 asked for *"raining hard, not drizzling… visible as fine streaks falling
across the whole frame and as rings breaking the standing water"* in a shot that is a **pale grey
fog wall from edge to edge**. The ground came back wet and **not one drop came back in the air**.

**This is [§20](#20--if-the-named-source-cannot-physically-light-the-scene-the-model-invents-fill-confirmed-2026-08-27)
in the weather domain, and it generalises the entry beyond lighting.** Rain is only legible where
it is brighter or darker than what is behind it; the photography literature is unanimous that
backlighting or a dark background is the *only* way rain reads, and that against a bright even sky
there is no separation to be had. `[community]` The engine was right and the prompt was wrong —
same verdict as [§17](#17--light-streaks-need-lights--the-lighting-has-to-permit-the-technique-observed).

**The fix is never more weather language. Find the dark thing already in the frame and give the
rain to it:** streaks legible only where they cross the black car and the near-black patches of
tarmac, rings and bounce-spray on the standing water, and a plain sentence saying that against the
fog it disappears into the grey.

⚠️ **The wider rule, now sighted in three domains — camera position (§6), lighting (§20) and
weather (§32): any instruction that is physically impossible in the scene as described will be
resolved by the engine, not refused.** It rebuilds the set, invents the fill, or drops the effect.
**Before rewriting the clause, check whether the frame contains the contrast the clause needs.**

### 33. ⚠️ An unresolvable colour brief is settled by the engine's strongest object prior `[observed 2026-09-08]`

The same prompt said *"faded mid-blue upper panels"*, *"very low saturation"* and *"the car's rear
lights are the only colour in the picture"* — three clauses that cannot all be true. What came
back was a **vivid stock-photo blue tent**, the brightest and most saturated thing in frame,
beating the rear lights outright and taking the eye off the two men.

**Given a contradiction the model does not average, it picks the prior it holds most strongly** —
and its prior for *dome tent* is a bright blue one. **State colour comparatively and physically,
never as a rule about the palette:** *the blue has weathered chalky until it is closer to grey
than to blue*, and *the red of the rear lights is the most saturated thing in the picture by a
wide margin*. Both are checkable against the rendered image; *"the only colour"* is not.

### 19. 🔴 §2's "do not restate the reference" applies to PEOPLE, not just sets `[confirmed 2026-08-27]`

Camping **8c(i)**. `@Bob` was cast **and** his canon appearance was pasted in as prose — beanie,
oversized charity-shop coat, hoodie, stubble, age, weathering. **The outfit came back wrong.**

**The rule was already here and was being applied to only half the problem.** The fourth pass §2
says a prose re-description competes with the attached reference and is a known drift source; the
repo had internalised that for **locations** and not for **characters**. Same mechanism, same fix.

**Rule: a Character cast or a reference attached means no appearance description at all.** Not
wardrobe, age, build, hair, skin or grooming. Write *"the man from the character reference"*.

**What still belongs in the prompt, because the reference cannot carry it:** what the person is
**doing** — posture, action, position in frame — and the **face as muscle description** (brows,
eyelids, mouth, where the eyes are aimed), per
[`image-prompting.md` §4a](../flow/image-prompting.md). Action and expression are not appearance.

**The one narrow exception:** where the figure is too small or too turned away for the Character
to bind at all (§12), prose is the only lever left — camping's forty-metre 8b long lens. **A face
in frame at any workable size means the reference carries it.**

⚠️ **A "keep the same" clause is not a loophole.** Camping 8c(ii), same day: *"the lower legs and
shoes of a man standing on the tarmac, **in the same dark jeans and tan shoes as in the reference
image**"* was caught immediately. Wrapping the garment in a preservation verb still puts the
garment in the prompt, and the prompt then competes with the reference exactly as §2 describes.
Write *"the standing man from the reference image"*.

*(Ruled by Jack: "please don't describe the character when there is a reference image or
character attached, because Flow messes it up.")*

### 18. 🔴 "Their face is not visible" does not hide a face. Only geometry does `[confirmed 2026-08-27]`

Camping **8b(i)**, round 1. An over-the-shoulder with a foreground figure whose face was
explicitly excluded twice — *"Only his back is in view. His face is turned away and is not in the
picture."* The engine returned him in **three-quarter profile with a fully rendered, invented
face**: cheek, beard, ear and eye all legible, sharper than the depth of field allowed for.

**The instruction was not partially obeyed. It was inverted** — the engine appears to read a
named body part as a request to render it. This is the same failure class as
[§6](#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set-observed) and the
camping camera-height finding: *stating a constraint does not bind; stating its physical
consequence does.*

**The fix that works is occlusion the engine has to honour to draw the scene at all:** put the
camera square behind the skull so the back of the head physically hides the rest, push the figure
close enough to the lens to be far out of focus, and **describe the result, not the rule** —
*"the back of his head faces us squarely and hides the whole of the rest of his head behind it;
the picture holds only the hair on the back of his skull, his collar and his coat."* If a cheek
still survives, **delete the head from the frame** and keep only a shoulder — a body part that
is not in the picture cannot grow a face.

**Why it costs more than a re-roll.** An invented face in frame is an **uncast character**. It
has no Character and no reference, so every later shot containing that person now has a likeness
to match that was never designed — which is exactly what camping's one-face-per-generation
method exists to prevent. Sibling of
[§12](#12--a-character-binds-to-a-face-no-face-in-the-shot-no-likeness-observed): a Character
binds to a face, and **an unbound face is a liability, not a blank**.

**Standing rule, now confirmed rather than inferred:** where a face does not need to be legible,
**hide it with the camera**, never with a sentence.

### Sources for this section

- [Google — prompting tips for Nano Banana Pro](https://blog.google/products/gemini/prompting-tips-nano-banana-pro/) `[vendor]`
- [Google AI — Nano-Banana Pro prompting guide & strategies](https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n) `[vendor]`
- [Nano Banana Pro reference images: setup and drift fixes](https://www.aifreeapi.com/en/posts/nano-banana-pro-reference-images) `[community]`
- [Nano Banana Pro camera control guide](https://techyheaven.com/nano-banana-pro-camera-control/) `[community]`
- [How to make AI images look real (2026)](https://imagera.ai/blog/make-ai-images-look-real-2026) `[community]`
- [Camera angles & composition for AI image generation (2026)](https://www.gensgpt.com/blog/camera-angles-composition-ai-image-generation-2026-guide) `[community]` — prompt order, telephoto compression, foreground layering
- [How to keep characters consistent in Google Flow](https://veobulk.com/en/blog/consistent-characters-google-flow) `[community]`
- [DetailMaster — can your text-to-image model handle long prompts?](https://arxiv.org/pdf/2505.16915) `[research]` — the length/adherence correlation
- [Consistent style in Nano Banana image edits](https://sider.ai/blog/ai-tools/how-to-write-prompts-that-produce-consistent-style-in-nano-banana-image-edits) `[community]` — hair-and-wardrobe drift, keep-before-change ordering

## Fifth pass — the model names, and faces `[community]` 2026-09-09

Run while writing camping **7c**, on two questions Kai asked directly: *optimise this for
"Nano Banana Pro 2"*, and *stop the engine overplaying facial expressions*.

### ⚠️ There is no "Nano Banana Pro 2" `[vendor]` `[community]`

The family, as of 2026-09-09, is **Nano Banana** (Gemini 2.5 Flash Image, Aug 2025) → **Nano
Banana Pro** (Gemini 3 Pro Image, Nov 2025, GA May 2026) → **Nano Banana 2** (Gemini 3.1 Flash
Image, 26 Feb 2026) → **Nano Banana 2 Lite**. Nothing called *Pro 2* has shipped.

**The naming is genuinely misleading and will be asked again:** "2" is the *Flash* line and "Pro"
is the older, larger model, so the higher number is not the better model. Engadget's framing is
the clearest one-liner — *"Nano Banana 2 is a faster version of Nano Banana Pro."* In Flow's
picker there are two entries: **Nano Banana 2** (default, all users, zero credits) and **Nano
Banana Pro** (AI Pro / Ultra, tighter rate limit).

🔴 **Corrected 2026-09-13 — "the higher number is not the better model" is a NAMING fact, and
this file previously let it stand as a QUALITY fact. It is not one.** See
[the benchmark check below](#-corrected-2026-09-13-nano-banana-2-beats-pro-on-the-leaderboards-community).

**Our standing recommendation is narrowed** — [use Pro](#which-engine-for-badcode) where the job
is *suppressing* sharpness and contrast **and** the composition is spatially complex, which is
most BadCode work; but **Pro is no longer the blanket default**, and where the two disagree the
answer is a two-generation A/B, not a leaderboard.

**Update 2026-09-11 `[community]` `[unverified against Google]`:** there's now a third entry,
**Nano Banana 2 Lite** (`gemini-3.1-flash-lite-image`, announced 2026-06-30). A third-party API
wrapper says Flow's picker offers `nano-banana-2-lite`, `nano-banana-2` and `nano-banana-pro`,
with **Lite the default since July 2026**
([useapi.net](https://useapi.net/docs/articles/google-flow-nano-banana-compare),
[blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)).
**Check the picker before every session.** You may be on Lite without having chosen it. Still
nothing called "Pro 2".

⚠️ **Google's own style examples are slop tells.** Its prompting guides use *"cinematic colour
grading with muted teal tones"*, *"cinematic lighting"* and *"golden hour backlighting"*, and
the anti-slop literature names every one of those. **Take Google's *structure*, not its example
styles.**

### 🔴 Corrected 2026-09-13: Nano Banana 2 beats Pro on the leaderboards `[community]`

**Asked directly — "surely NB2 is best for image quality" — and the honest answer is that the
challenge was right and this file was wrong.** The naming fact (the "2" is the Flash line, Pro is
the larger model) was being used here to carry a quality claim it does not support.

**Human-preference Elo, text-to-image — NB2 wins, and not narrowly:**

| Leaderboard | Nano Banana 2 | Nano Banana Pro |
| --- | --- | --- |
| Arena.ai, text-to-image | **1,280** | 1,238 |
| Artificial Analysis, text-to-image | **1,264** | 1,220 |
| Arena.ai, image editing | **1,401** *(preliminary, ~3,000 votes — inside the noise)* | 1,398 |
| Artificial Analysis, image editing | 1,233 | **1,250** |

Source: [DeepLearning.AI's *The Batch*](https://www.deeplearning.ai/the-batch/nano-banana-2-aka-gemini-3-1-flash-image-makes-edits-easier-and-faster)
`[community]`. It also records NB2 as **~4× faster and roughly half the cost per image**, and
**both models supporting the same resolutions** — 512, 1K, 2K and 4K across 14 aspect ratios. So
the old "take 2K on Pro" advice is not a Pro-only capability.

**🔑 Where Pro still wins, and it is the reason not to switch blindly.** fal's side-by-side
review is mixed on photorealism (it gives a portrait to NB2 on detail, a product shot to Pro on
restraint) but is unambiguous on one axis: Pro *"spends more time thinking before it renders"*
complex multi-element compositions, and is the pick for scenes with *"specific spatial
relationships, layered lighting, and a particular mood"*, because Gemini 3 Pro Image
*"allocates more compute to understanding relationships between elements in your scene"*
([fal](https://fal.ai/learn/tools/nano-banana-pro-vs-nano-banana-2)) `[community]`.

⚠️ **That is exactly the BadCode frame.** Off-axis geometry, single-source falloff, an
individuated background crowd at three distances, a foreground occluder — and it is precisely
where camping `1m-l` round 1 failed (centred, two of three figures cloned, the worn surfaces
lost). **So the leaderboard does not settle our case**, because general preference Elo is
dominated by pretty single-subject images, which is the opposite of what we ask for.

🔴 **Reseller "95% of Pro's quality" figures are marketing, not measurement.** Several API
resellers repeat *"NB2 reaches ~95% of Pro's quality, Pro leads 5–8% on 4K texture and lighting"*
with no method behind it. **Do not cite those numbers.**

⬜ **The open question, and it is cheap to close:** fire one identical BadCode prompt on Pro and
on NB2, back to back, and judge the pair. **Our own measured finding outranks every row above.**
Until that runs, *neither* model is the house default by evidence — Pro is the default by
**continuity**, because the accepted camping montage frames were made on it and the montage cuts
at about one frame per second, where a look shift between frames would show.

⚠️ **Nano Banana 2 Lite is not in this argument.** It is the small, fast, cheap tier and it is the
silent default in Flow's picker. Never leave a session on it.

### 35. ⚠️ A flash described as an object in the room is drawn as a lamp `[observed 2026-09-11, n=1]`

Camping `1m-e`'s Light paragraph opened *"a flash on top of the camera is the only strong
light"* and then gave its falloff. What came back was **a bright lamp blowing out in the
top-right corner of the frame**, with the room evenly lit again. It's the §27 family: a light
named as a noun gets placed in the picture. **Untested fix:** name the flash as *camera
hardware* in the Style line (the body and the Speedlite), describe only its consequences in the
Light line, and put the sources' positions in Constraints: *"the flash is behind the lens, the
tubes are above the top edge of the frame."*

> ✅ **`[observed 2026-09-11, n=1]` The fix worked first time.** Camping `1m-2` named *"a Canon
> EOS-1D Mark III with a Speedlite"* in Style, described the flash only as consequences, and
> pinned the source positions in Constraints. It came back as a proper on-camera flash: hard
> light on the subject, the room falling to green, moving people ghosted. **Naming the hardware
> brought in the whole photographic register; describing the light as an object brought in a
> lamp.**

**The same frame also came back with every monitor blank black.** The inferred cause is that
*"the monitors carry no readable lettering"* was met by switching them off. Give screens
content that is **too small or too soft to read** instead of forbidding the text.

### 🎯 Faces: an emotion word gets a caricature; anatomy gets a face `[community]`

The single highest-value finding of this pass, and it independently confirms what camping **7a**
found the hard way on 2026-08-26.

- **Writing `happy`, `sad`, `angry`, `confused` alone tells the model almost nothing**, and what
  it fills in is the exaggerated version — a pantomime frown, a crying face, a grin. The counter
  is to describe the **muscles**: which eyebrow end lifts, where the crease sits, whether the
  lips part, where the chin points.
- **Real emotion is small.** *"A tiny eyebrow raise or a slight jaw tighten looks more realistic
  than extreme expressions."* Say so explicitly — an instruction that the expression **stays
  small** is worth a clause in `Constraints:`.
- **🔴 It lives in the eyes.** *"The eyes communicate more than any other facial feature, and if
  the eyes look dead or mismatched, the whole image fails."* Working rule: **the eye description
  should be longer than the mouth description.**
- **Subtle expressions are a known weak spot** for commercial multimodal models, not a prompting
  failure to be brute-forced — a peer-reviewed study of AI-generated emotional faces reports
  exactly this. Budget a reroll rather than escalating the wording, because escalating the
  wording is what produces the caricature.

**And keep 7a's other half: name the wrong readings.** *"This is not weariness, not amusement,
not sadness and not calm"* is the clause that did the work. It is a
[style-family negation](#negatives-revisited), the one place negatives are allowed — short,
one clause, everything else stated positively.

**Add a floor, not just a ceiling.** 7c's phrasing is worth stealing: *"a stranger looking at
this photograph would take a second to notice anything was wrong with him at all."* It bounds the
performance from below in a way "subtle" does not.

### ⚠️ Kodak Portra 400 may now be a slop tell `[community]` `[untested]`

Uncomfortable, because it is in nearly every camping and Karen prompt we have written.

> *"A few film stocks are now so over-prompted they read as trying to look like film — Portra 400
> and Cinestill 800T especially. Reach for Gold 200, Ektachrome, or Ilford HP5 instead."*

**One `[community]` source, no test behind it — do not act on this yet, and above all do not
change stock mid-story.** Continuity beats a hypothesis: camping's accepted frames are Portra and
a new stock would not cut against them. What it is worth is a **cheap calibration**: next time a
*new* piece needs a look decided, run one plate on Portra 400 and one on Kodak Gold 200 with
everything else identical, and look. Promote or delete after that.

The rest of the pass restated what the [third-pass table](#the-anti-slop-toolkit) already has —
that the 2026 tell is *"too good: too clean, too evenly lit, too symmetrical, too composed"*, and
that the counters are a named body and focal length, a named stock, one positioned light, stated
imperfections and asymmetry. **One addition worth keeping:** *"candid", "street photographer",
"shot from the hip"* imply **a human behind the camera**, which is a different lever from
imperfection keywords and cheaper than any of them.

### Sources for this section (2026-09-09)

- [Nano Banana 2 — blog.google](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) · [Nano Banana 2 and Nano Banana Pro are generally available — Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-and-nano-banana-pro-are-generally-available) `[vendor]` — the model line-up and the launch dates
- [Google's Nano Banana 2 is a faster version of Nano Banana Pro — Engadget](https://www.engadget.com/ai/googles-nano-banana-2-is-a-faster-version-of-nano-banana-pro-160000695.html) · [TechCrunch](https://techcrunch.com/2026/02/26/google-launches-nano-banana-2-model-with-faster-image-generation/) `[community]` — the "2 is not newer than Pro" framing, and Flow's default
- [How to create realistic facial expressions in AI images — Medium](https://medium.com/write-your-world/how-to-create-realistic-facial-expressions-in-ai-images-2026-guide-prompt-examples-63438c54c65f) `[community]` — emotion words vs anatomy; the eyes; keep it subtle
- [AI-generated face images of emotional expressions — Journal of Nonverbal Behavior](https://link.springer.com/article/10.1007/s10919-026-00517-3) `[academic]` — subtle expressions are a measured weak spot
- [How to create AI images that don't look like AI (2026)](https://usetoolai.com/blog/how-to-create-ai-images-that-dont-look-like-ai-2026) · [Pixova](https://www.pixova.io/blog/how-to-make-ai-images-look-less-like-ai) · [Hedra](https://www.hedra.com/blog/make-ai-images-look-real-photos-prompting) `[community]` — "too good" as the 2026 tell; the over-prompted film stocks; "candid / shot from the hip" as a human-behind-the-camera lever

**All `[untested]` against our own session.**

## Sixth web pass — 2026-09-12 `[research]` `[practitioner]` `[vendor]`

Run while writing camping's three added montage frames (`1m-c`, `1m-m`, `1m-l`), on Jack's two asks:
*optimise for Nano Banana Pro*, and *avoid AI slop*. **This is the first pass with real `[research]` in it** —
peer-reviewed perception and era/culture studies rather than vendor blogs — and the research disagrees with
the blogs about what the problem even is.

### 🔑 The enemy is the register, not the artifact `[research]`

511 participants' free-text reasons for calling an image AI, coded into 576 mentions: **stylistic artifacts
190** (*"smoothness, irregular surfaces or overly polished materials"*), **semantics/logic 178**, **physics
82**, **geometry 78**, **intuition 48**. Overall accuracy **63.7%**; against the best generator in the set
people were right **29%** of the time. And against the strong models the artifact hunt collapses into
register — participants wrote *"the whole style reminds me of AI, I cannot explain it exactly"* and *"too
perfectly arranged."*

A second study puts humans at **62% across ~287k judgements** (12.5k participants), with **portraits easiest
to spot and natural and urban scenes hardest**.

🔑 **Two consequences for us.** The thing to suppress is *too-perfectly-arranged*, not fingers and spelling —
which is what this file's anti-slop table has been doing by instinct and can now claim evidence for. And our
subjects (urban interiors, car parks, skylines) sit in the **hard** category; a face in close-up is the
risky one.

### ✅ Period accuracy is a vendor-sanctioned constraint — and a hedge, not a fix

- **Google's own example of a factual constraint is era**: *"ensure historical accuracy for the Victorian
  era."* `[vendor]` So **"Ensure historical accuracy for 2008."** is a legitimate `Constraints:` line and is
  now in all three camping montage prompts.
- 🔴 **But a `[research]` study measures generators inserting modern hardware because they prioritise the
  activity over the era** — anachronism rates ~25% (SD3, 1930s), ~12–13% (FLUX.1), <5% (SDXL) — and finds
  prompt-level mitigation *"insufficient to fully counteract learned stylistic tendencies."* It shifts the
  bias; it does not remove it. ⚠️ **Their decade series stops at the 1990s, so 2008 is not measured by
  anyone, and Nano Banana Pro was not tested.** **Check every screen, handset and monitor on round 1.**
- **US/Global-North default is documented** — country-agnostic prompts *"default to Global-North,
  modern-leaning depictions that flatten cross-country distinctions."* `[research]`
- ⚠️ **So *"British"* on its own is weak.** The one practical UK account found says what worked was **naming
  concrete British architecture and explicitly excluding the American features**, not adding the adjective.
  `[community]`

### 🔑 Iterative editing erodes cultural and era fidelity — external support for our no-edit rule

The same `[research]` paper finds **image-to-image editing degrades cultural fidelity while metrics stay
flat**, because models apply *"superficial cues (palette shifts, generic props) rather than era-consistent,
context-aware changes."*

⚠️ **This matters because Google's own guidance points the other way:** *"if an image is ~80% right, ask for
the specific change instead of regenerating"* `[vendor-adjacent]`, and a practitioner source recommends
fixing a bad background face by masking and re-prompting that region. **Our house rule is the opposite —
always a new prompt, never an image edit — and it is now the better-evidenced position for anything carrying
a period or a place.** Keep it.

### ✅ Name both ends of the exposure, or the model compensates in the shadows `[practitioner]`

*"Without blowing highlights"* / *"preserve highlight texture"* has to be paired with what the shadows do,
or the engine protects the highlights by lifting everything else. Adopted in the camping montage prompts:
the flash frames **grant** the clipping on his shirt and ask the shadows to hold detail; `1m-l` asks for deep
shadow that **keeps a trace rather than going to solid black**.

Related, and it is the same shape as [§20](#20--if-the-named-source-cannot-physically-light-the-scene-the-model-invents-fill-confirmed-2026-08-27):
**mood words are exposure words.** *dramatic, cinematic, moody, noir* silently darken the whole frame, so a
frame that needs dark *shape* rather than dark *everything* states the source and leaves the mood word out.
`[community]`

### 🔑 The 2008 on-camera-flash register — and the one place crushed black is correct

A documented look, and it is exactly what camping's montage is reaching for: **direct undiffused on-camera
flash, shutter fast enough that ambient barely registers, the background falling to a near-black crushed void
past the flash's short range, cool blue-green white balance, highlights clipping to featureless white, fine
digital grain and mild chromatic noise.** `[community]`

🔑 **In this register a crushed near-black background is period-correct rather than a fault** — which is the
one exception to the general realism advice below, and worth knowing because it is rare to get our register
and the realism advice pointing the same way.

⚠️ **Against it, two independent craft sources say the opposite for images generally:** keep the darkest
shadow *just above* pure black, and *"lift the blacks slightly — pure black reads as digital."*
`[practitioner]` `[community]` 🔴 **This is material to the open ruling
[`cinematography/principles.md` §R1](../cinematography/principles.md) and must not be used to close it** —
two craft blogs are not evidence about our reader, and the distinction they actually draw is **detail lost**
versus **blacks lifted to dark grey**, which is a grading decision we make at delivery, not a prompt clause.

### ✅ Crowd realism is individuation, not adjectives `[practitioner]`

The named root cause is **under-specification**: an unconstrained crowd leaves *"nothing to disambiguate one
face from the next"*, so the model fills in a statistically plausible pattern and bleeds features between
faces. The fix is to **state how many distinct individuals, what each is doing, and how far apart they
stand** — which is [§22](#22--tiling-and-cloning-in-crowd-scenes-are-a-resolution-problem-not-only-a-prompt-problem-community-2026-08-28)'s
*name the variety and name the counts* arrived at from the other direction.

- **Motion blur on background people is the cheapest crowd-realism lever there is.** `[community]` ⚠️ Not
  always available: camping `1m-c` needs its background **still**, because the stillness is the argument. There
  the only lever left is individuation.
- **Off-native resolution is a named cause of duplication and tiling** `[community]`, which corroborates §22
  and supports taking **2K over 4K on any frame with a crowd in it**.

### ⚠️ Fake depth of field has its own tells `[practitioner]` `[community]`

Not just *soft* — **segmentation halos** around the subject, people sliced at the frame edge, and a
background that reads **painterly rather than defocused**. Our standing phrasing
(*"thrown completely out of focus so that it is a soft blur"*,
[§26](#26--two-characters-do-hold-in-one-frame--if-each-is-anchored-to-a-named-side-observed-2026-08-30))
is still the right instruction; this is a thing to **check in the returned frame**, where it shows up at the
occluder's edge.

### ⚠️ The quality-word kill list now includes "cinematic"

*"8K", "ultra-realistic", "hyperrealistic", "masterpiece", "beautiful"* — and **"cinematic"** — are reported
to trigger the model's aesthetic mode and produce the glossy plastic look. `[practitioner]` **Note the
collision already flagged in this file: Google's own examples use *"cinematic colour grading"* and
*"cinematic lighting"*.** Take Google's structure, not its example styles. Our *"a newspaper photograph
of…"* opener is on the right side of this.

Also restated: **name humble gear rather than studio rigs**, and **avoid Portra 400 and CineStill 800T** in
favour of Gold 200, Ektachrome or Ilford HP5. ⚠️ **Irrelevant where the shot is digital** — camping's montage
names a 2008 press DSLR, so there is no stock to swap, and
[the standing warning against changing stock mid-story](#-kodak-portra-400-may-now-be-a-slop-tell-community-untested)
is unaffected.

### ✅ Engine facts worth having straight `[vendor]`

- **Thinking cannot be disabled.** Pro generates up to two uncharged interim *"thought images"* to refine the
  composition before the final output; `thinking_level` is minimal or high. 🔑 **So the job sentence at the
  top of our prompts is feeding the reasoning pass, not decorating it** — keep it concrete and keep it first.
- **Google's own stated weaknesses:** *"can still struggle with small faces, accurate spelling, and fine
  details"*, and *"masked editing, major lighting changes (like day to night), or blending multiple images
  may sometimes produce unnatural results"*, and character consistency *"may not always get it right."*
  🔑 **Small faces is the one to design around** — it is the vendor confirming
  [§12](#12--a-character-binds-to-a-face-no-face-in-the-shot-no-likeness-observed) and
  [the reference-size rule](#-confirmed-2026-09-09-a-reference-carries-a-face-only-at-the-size-the-face-is-in-it)
  from the other side. **And *day-to-night* being named is a caution for any relight**, including the
  scene-10 lightning work.
- **Resolutions:** Pro 1K / 2K / 4K (value strings `"1K"`, `"2K"`, `"4K"`); NB2 adds 512px. On Vertex, **1K
  and 2K are GA and 4K was still Preview** at the GA post (2026-05-29).
- **Aspect ratios (Pro):** 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9. NB2 adds 1:4, 4:1, 1:8, 8:1.
- **Flow:** its help page names **Nano Banana Pro, Nano Banana 2, Nano Banana 2 Lite** and gives **no
  per-model numbers** for ratios, resolution or reference limits. You set **aspect ratio and number of
  outputs** before generating; references are dragged into the prompt box; Characters are addressed as
  `@Name`. Flow's own rule for references: *"your text prompt should complement, not contradict, your visual
  inputs."*
- **The 480-token prompt cap that circulates as a Gemini-image limit is Imagen 4 only** and does not apply
  here. No documented Nano Banana prompt-length limit beyond model token limits.
- **Labelled prompt sections are sanctioned, not a hack** — Google AI's own writeup uses
  `Face Consistency:` / `Subject:` / `Graphics:` blocks for complex jobs. Our `SCENE: / Camera: / Subject: /
  … / Constraints:` skeleton is the endorsed shape.

### ⚠️ Positive framing versus exclude-lists is still unresolved — but our shape is corroborated

Google says positive framing only (*"empty street"*, not *"no cars"*); **three practitioner sources report
explicit exclude-lists working**, including hard ones (*"Do NOT introduce new characters/objects not present
in the reference image"*). That is the same split this file resolved on 2026-09-08 —
**negatives belong in a terminal, scoped constraint block attached to named things**, never floating in the
body — and the resolution now has outside company. ⬜ **Cheap A/B nobody has run:** one frame with our
`Constraints:` block, one without, everything else identical.

### 🚫 Do not cite

- **"95% consistency, tested across 500+ generations", "IDENTITY LOCK"** — SEO content with no methodology.
- **"Viewers clock AI in under a second"** — asserted, no study.
- **"Film grain searches +31%, motion blur +15%"** — no primary source; the named trend pages do not carry
  the figures.
- **Diffusion-specific fixes** (CFG values, VAE, emphasis weights) — Nano Banana Pro exposes none of those
  controls.

### ⬜ Could not verify

- **Per-slot reference maxima for Pro.** The API docs break slots into categories and describe Pro as taking
  *fewer* images than Flash; the developer blog says *"six high-fidelity shots… or as many as fourteen
  standard inputs"*; DeepMind says five characters / fourteen objects. The Vertex spec tables would not load.
  **Treat exact per-slot counts as unknown** — our one-reference house rule is unaffected.
- **Flow's "3 ingredients per prompt" limit** — repeated widely, **not stated on the Flow help pages**.
- **Whether Flow exposes 2K/4K today, and whether Pro is Ultra-only** — the Flow changelog needs sign-in.
- **Any *measured* brightening or centring bias.** There is plenty of prompt advice for fighting both and no
  source demonstrating either. Do not write it as a finding.
- **2008 City trading-floor visual specifics** (CRT/TFT mix, monitor counts, lanyards, dress). ⬜ **If a
  montage frame comes back wrong on period detail, the fix is to pull three or four dated 2008 editorial
  frames and look**, not to write more prose. ⚠️ Licence check first — the
  [`camera/reference/README.md`](../stories/camping/camera/reference/README.md) ruling on CC BY-SA pixels
  applies to anything attached.

**Useful context for a future "it went waxy" complaint:** a real Vertex-side quality regression ran
**2026-05-07 → fixed 2026-05-15**, acknowledged by Google staff on their own forum, root cause undisclosed.
`[community, first-party forum]`

### 36. 🔴 A carried garment with no worn garment stated returns BOTH `[observed 2026-09-12, n=1]`

Camping [`1m-l`](../stories/camping/prompts.md#1m-l--round-1-not-accepted-jack-2026-09-12-it-looks-like-ai-slop)
round 1. The `Action:` block said *"his suit jacket is hooked over the other shoulder on one
finger"* and **said nothing about what was on his body.** It came back with him **wearing a suit
jacket and carrying a second one.** Jack: *"he is carrying his jacket over his shoulder whilst
wearing one."*

**Mechanism:** [§25](#25--19-inverts-for-an-unbound-body-part--describe-it-or-get-young-clean-and-generic-observed-2026-08-29)
exactly — an unstated attribute returns the **generic default**, and the default for a City trader
is a suit jacket. Naming the carried one did not displace the worn one; it added to it.

🔑 **The rule, and it generalises past jackets:** **a garment described as carried, removed, slung
or held is a claim about an object, not a claim about the body.** State the body separately. Bag,
coat, hat, tie, lanyard — same shape.

**Two clauses, and the second is the cheap insurance:**

- In the body: **`he is wearing his suit jacket, done up, and he carries nothing over his arm.`**
- In `Constraints:`: **`he wears one jacket and it is on his body.`** A count, in the terminal
  scoped block where [negation is allowed](#negatives-revisited).

⬜ **And check the wardrobe of everyone else while you are there.** `1m-l` round 2 turns the bug
into the argument: **he is the only person in the picture wearing a suit jacket**, and the people
being walked out are in shirtsleeves and a jumper. One clause, two jobs — the duplicate is
impossible and the class difference is stated in cloth.

### 37. 🔴 A square-on architectural feature is a symmetry magnet, and a composition adjective will not move it `[observed 2026-09-12]`

Same frame. The `Camera:` block said *"the lit lift car sits **right of centre** and the dark lobby
runs away to the left."* It came back **dead centre and near-symmetrical**, with the lift doors
square to the lens and the lobby balanced either side.

**This is the [`1b` tell](../stories/camping/prompts.md#scene-1-montage--the-80s-job-montage-2026-09-11)
again in a different building** — the symmetry-and-cloning bundle,
[`symptoms.md` A](../cinematography/symptoms.md). And the centring bias is reported independently:
*"AI models default to centred, symmetrical compositions because that is what dominates their
training data"* `[community]`.

🔑 **The finding is about precedence: a strong architectural feature outranks a placement
adjective.** A lift bank, a doorway, a corridor and a window each carry their own symmetry axis,
and the model composes onto it. *Right of centre* is a preference; the axis is a structure.

**Two levers, and the house one has already been proven twice:**

| Lever | Why it works |
| --- | --- |
| 🔑 **Put the ROOM in the `Subject:` slot and demote the feature to a thing inside it** | [§546](#-making-a-subject-small-put-something-else-in-the-subject-slot-community-2026-09-09). This is exactly how [camping 3c round 2 was fixed](../stories/camping/prompts.md#3c--the-lane-hours-later--still--written-2026-09-09-unrun) after round 1 centred the car — *put the ROAD in Subject* |
| **Take the camera off the feature's plane** | *"seen slightly from its left side, so it reads as a leaning rectangle rather than a square-on one"* — remove the axis and there is nothing to snap to. Cheaper than arguing with it |

⚠️ **Do not reach for a numeric fix.** *"Subject at 30% from the left edge"* is the shape
[§30](#30--a-physical-analogy-overrules-a-stated-number--and-it-is-how-28-keeps-happening-observed-2026-09-08)
says loses. Move the camera instead.

### 38. 🔴 A mechanical in-progress state returns fully open (or fully shut) — give it a physical analogy `[observed 2026-09-12]`

Same frame, and it cost the beat outright. The prompt said the doors *"have begun to close"* and
*"he is framed in the gap between them"* — **twice**. The lift came back **wide open**, and *the
doors closing on him*, which is the entire point of the shot, is simply not in the picture.

**Mechanism:** a lift door has two strong priors, **open** and **shut**, and *"has begun to close"*
is a **stage direction** — a claim about time, which a still cannot hold. The model resolves it to
the nearest state it knows. Same family as
[§27](#27--ask-for-an-object-never-an-absence--a-subtractive-shape-comes-back-inverted-observed-2026-08-30):
an instruction that is not a describable *shape* gets resolved into whatever is.

🔑 **The fix is [§30](#30--a-physical-analogy-overrules-a-stated-number--and-it-is-how-28-keeps-happening-observed-2026-09-08)'s
lever pointed at state instead of size: describe the geometry, not the process.**

| Instead of | Write |
| --- | --- |
| `the doors have begun to close` | **`the gap between the leading edges is narrower than a man's shoulders, so the doors crop him at both arms`** |
| `the door is ajar` | `the gap is about the width of a hand` |
| `the drawer is half open` | `the drawer stands out from the cabinet by the length of a pencil` |

⬜ **And say it twice, in two systems.** In `1m-l` round 2 the light restates the same fact — the
car throws a **narrow strip** across the carpet rather than a rectangle — so the geometry has to be
right in the shadow as well as in the metal. `[untested]`

### 🔴 §38 at n=3 — a mechanical in-progress state is near-unbeatable. Design the stillness in `[observed 2026-09-13]`

**Three camping frames have now asked for a machine mid-action and got the machine at rest**, through
four different phrasings:

| Shot | Asked for | Came back |
| --- | --- | --- |
| `1m-l` rounds 1–5 | lift doors almost shut — a stage direction, then a physical analogy, then a proportion of the doorway, then the shape of the light on the floor | **fully open**, every time |
| `1m-p` round 1 | banknotes riffling through a counter's throat as an arc of blur | **stopped** — notes static and sharp |

⚠️ **One counter-example worth keeping:** `1m-t`'s treadmill belt **did** come back smeared under the
same drag-shutter clause. The difference is that a belt is **one continuous surface** while doors and
banknotes are **discrete objects with a start and an end state** — 🔴 **inferred from n=3, untested.**

🔑 **The useful half is the planning consequence, not the diagnosis: stop paying rounds against it.**
A machine at rest is not a failed plate — **it is frame 0 of the clip in which the machine starts.**
The still shows the state; the clip shows the change. That has now produced a *better* shot twice
running: `1m-l`'s open doors became a clip that closes them and takes the light out of the room, and
`1m-p`'s stopped counter became a clip that starts it.

**Working:** [`camping/prompts.md`](../stories/camping/prompts.md#-38-at-n3--a-mechanical-in-progress-state-is-near-unbeatable-and-it-is-worth-planning-around).

### ⚠️ Six worn nouns lose to one building prior — and the counter is a scoped negation `[observed 2026-09-12]`

Same frame, worth recording because it is a *quantity* observation. The `Environment:` block named
**scuffed kick plates, a dark stone-tiled wall, grey carpet tiles with a worn track, a dented
skirting board, a red fire extinguisher, two dead ceiling fittings.** What came back was a
**polished marble atrium with a mirror floor** — not one of the six survived.

🔑 **Positive nouns describing wear do not defeat a luxury prior; they get absorbed into it.** The
counter is the shape [§29](#29--to-overrule-a-reference-on-one-element-declare-its-role-narrowly-then-negate-the-old-value-observed-2026-08-30)
already established for overruling a reference, moved into the terminal `Constraints:` block:
**name the surface, then negate the old value.**

> *"The lobby is worn and ordinary — carpet tiles rather than stone, a matt painted wall rather
> than marble, and a floor that reflects nothing."*

This is squarely inside the [2026-09-08 resolution](#negatives-revisited) — negatives are allowed
**scoped, terminal and attached to named things** — and it now has outside company from the three
practitioner sources reporting exclude-lists working
([sixth web pass](#️-positive-framing-versus-exclude-lists-is-still-unresolved--but-our-shape-is-corroborated)).

⚠️ **Related, and it is the register half of the same failure:** the frame came back reading as a
**corporate-thriller poster** — glossy stone, mirror floor, smooth skin, no grain — despite the
Style line naming *ISO 3200* and *coarse digital noise*. The lever that was available and unused is
the cheapest one in this file: **a human behind the camera**. *"A candid press photograph… taken
quickly"* is [a different instrument from imperfection keywords](#-kodak-portra-400-may-now-be-a-slop-tell-community-untested),
and it costs four words.

### 🚫 Rejected: "remove polite phrases like 'please'" `[community]` `[untested]`

A Nano Banana Pro guide recommends stripping conversational filler and writing in
*"command-line style syntax"*. **No test behind it**, and it collides with the standing house rule
that every Flow prompt ends with `Thanks.` **We keep the `Thanks.`** Recorded so it is not
re-derived every time someone reads a prompting guide.

### Sources for this section (2026-09-12)

**`[research]`** — [Frontiers, why people think an image is AI (511 participants, coded reasons)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1707336/full) ·
[arXiv 2507.18640 — 62% across ~287k judgements](https://arxiv.org/abs/2507.18640) ·
[REVEAL — forensic cue families](https://arxiv.org/html/2511.23158v2) ·
[Synthetic History — era bias and anachronism rates](https://arxiv.org/abs/2505.17064) ·
[Cultural Blindspots — editing erodes cultural fidelity](https://arxiv.org/abs/2510.20042) ·
[AI-generated emotional faces (from the fifth pass, still the best source on subtle expression)](https://link.springer.com/article/10.1007/s10919-026-00517-3)

**`[vendor]`** — [Nano Banana Pro prompting tips](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/) ·
[Ultimate prompting guide — Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) ·
[Gemini API image generation docs](https://ai.google.dev/gemini-api/docs/image-generation) ·
[Google AI — Nano Banana Pro prompting strategies](https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n) ·
[fal — Nano Banana Pro prompting guide](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide) `[community]` ·
[Higgsfield — Nano Banana Pro high-control prompting](https://higgsfield.ai/nano-banana-pro-prompt-guide) `[community]` ·
[Pixova — making AI images look less like AI (the centring bias)](https://www.pixova.io/blog/how-to-make-ai-images-look-less-like-ai) `[community]` ·
[ZSky — why your AI images look bad](https://zsky.ai/blog/why-ai-images-look-bad) `[community]` ·
[DeepMind model page](https://deepmind.google/models/gemini-image/pro/) ·
[NB2 + Pro generally available](https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-and-nano-banana-pro-are-generally-available) ·
[Flow — models and supported features](https://support.google.com/flow/answer/16352836?hl=en) ·
[Flow — generating with references](https://support.google.com/flow/answer/16353334?hl=en)

**`[practitioner]`** — [fal — Nano Banana Pro prompting guide](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide) ·
[Chase Jarvis — relighting an image](https://chasejarvis.com/blog/how-to-re-light-an-image-with-nano-banana-pro/) ·
[getimg.ai — why AI skin looks fake (dated 17-model test)](https://getimg.ai/blog/why-ai-skin-looks-fake-how-to-make-it-real) ·
[Hedra — making AI images look like real photos](https://www.hedra.com/blog/make-ai-images-look-like-real-photos-prompting) ·
[Envato Elements — prompts for realistic images](https://elements.envato.com/learn/prompts-for-realistic-ai-images) ·
[Prompt Architects — crowd faces](https://prompt-architects.com/blog/388-hands-faces-and-text-fixing-ais-classic-failures) ·
[Beverly Boy — avoiding crushed blacks](https://beverlyboy.com/filmmaking/how-to-avoid-crushed-blacks-in-shadows/) ·
[Fstoppers — spotting fake bokeh](https://fstoppers.com/post-production/can-spot-fake-bokeh-574880)

**`[community]`** — [Miraflow — the 2008 flash register](https://miraflow.ai/blog/ai-flash-filter-prompts-2026) ·
[VSCO — digital camera effect](https://www.vsco.co/learn/digital-camera-effect) ·
[zsky — too-dark images](https://zsky.ai/blog/ai-image-too-dark-fix) ·
[zsky — artifacts guide](https://zsky.ai/blog/ai-image-artifacts-guide) ·
[Upsampler](https://upsampler.com/blog/make-ai-images-look-real) ·
[Adobe forum — UK scenes drifting American](https://community.adobe.com/questions-404/proper-uk-representation-of-scenes-1477922/index2.html) ·
[awesome-nanobanana-pro (prompt library)](https://github.com/ZeroLu/awesome-nanobanana-pro) ·
[Vertex quality regression thread](https://discuss.ai.google.dev/t/low-image-quality-in-nano-banana-pro-2-on-vertex-ai-studio/144258)

**Everything here is `[untested]` against our own Flow session except where it corroborates a finding this
file already reached from production — and where it does, the production finding is the one that governs.**


## Seventh web pass — 2026-09-13 `[vendor]` `[academic]` `[community]`

Run for camping `2g` (light 2008 couple stills). **New or contradicting items only. None tested on our work.**

- 🔴 **NB2 has Image Search grounding too**, which contradicts `docs/flow/image-prompting.md` §8 ("Pro only").
  It **cannot search for people**, only places, buildings and species. ⬜ Unverified whether Flow exposes it.
  `[vendor]` [blog.google](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) ·
  [dev.to/googleai](https://dev.to/googleai/getting-the-most-out-of-nano-banana-2-502k)
- ⚠️ **NB2 thinking is a switch, and Google says to leave it off by default.** Turn it on only for nonsense
  results or complex spatial work. So *"the job sentence feeds the reasoning pass"* holds on Pro, and on NB2 only
  when thinking is on. ⬜ Unverified whether Flow exposes it. `[vendor]` (same dev.to post)
- 🔑 **AI faces are "hyper-average"**: symmetrical, smooth and attractive. The counter is distinctive,
  non-average features, not generic imperfection. ⚠️ The studies used older GAN-type generators, and **this conflicts
  with [§19](#19--2s-do-not-restate-the-reference-applies-to-people-not-just-sets-confirmed-2026-08-27)
  whenever a reference is attached.** In that case the reference carries the face and §19 wins. It applies only to
  unreferenced people. `[academic]` [Psych Sci 2023](https://journals.sagepub.com/doi/10.1177/09567976231207095) ·
  [PubMed 2026](https://pubmed.ncbi.nlm.nih.gov/41705896/)
- **Unreferenced people default to young, thin and attractive.** State age, build and skin as facts.
  `[academic]` [PMC10737815](https://pmc.ncbi.nlm.nih.gov/articles/PMC10737815/)
- **Women get more smiles and more downward head tilts** (DALL-E 2 only). State the head angle and mouth for
  every figure, not just the lead. `[academic]` [arXiv 2305.10566](https://arxiv.org/abs/2305.10566)
- **Emphasising happiness produces rows of small, bright teeth.** Use closed mouths, and give each person a named
  thing to look at to fix dead eyes. `[community, unverified]`
- 🚫 **Do not cite** the "AI teal-orange bias" article (anecdotal, Midjourney, 2024).

## Eighth web pass — 2026-09-14 `[academic]` `[community]`

Run for camping `2g-2` (a chip stolen at a services table). **New items only. None tested on our work yet.**
There is still no Nano Banana 2 prompting guide or model change dated after 2026-09-01, and still no
"Nano Banana Pro 2": only knock-off domains use that name.

- **Hands gripping an object render better than open hands. Hands near the face fail more often.**
  `[community]` [zsky.ai](https://zsky.ai/blog/how-to-fix-ai-hands). Supported by
  [GraspDiffusion, arXiv 2410.13911](https://arxiv.org/abs/2410.13911) `[academic]`, which tested older
  diffusion models, not Nano Banana. §25 covers what a hand looks like; this covers how it's posed.
- **Models miscount, and piles of overlapping objects do worst.** Gemini was among the nine systems tested.
  `[academic]` [NumBench, arXiv 2608.28206](https://arxiv.org/html/2608.28206). Ask for *one* of the object
  that matters, and keep any pile small.
- **Food is a slop category of its own:** uniform texture and gloss, too-perfect arrangement, cutlery
  melting into food. `[community]` [ico-optics](https://www.ico-optics.org/why-ai-food-photos-always-look-so-unnaturally-fake/) ·
  [X-AIGD, arXiv 2601.19430](https://arxiv.org/abs/2601.19430) `[academic]`, which lists hand–object
  contact and food as separate artifact categories.
- **Brand eras:** Burger King changed its logo in 2021. ⬜ *Inferred, unverified:* since the model can pull
  current imagery from search, naming a brand in a period shot probably gives the *current* badge, which is
  §34 plus a period error.
- **Name what someone is looking at, not "looking away".** `[community]`, tested on other engines. Confirms
  the seventh pass.

## Ninth web pass — 2026-09-14 `[academic]` `[community]`

Run for camping `9-walk` (Tarquin walking up to a yurt at blue hour, the first frame of a clip). **New items
only. None tested on our work yet.** There is still no model change and no "Nano Banana Pro 2".

- **Walking figures:** generators swap which leg is nearer the camera when legs overlap. The counter-cue is
  the arm opposite the forward leg swinging forward. `[academic]`
  [arXiv 2312.07854](https://arxiv.org/pdf/2312.07854), older pipeline, not NB2. Describe the stride as a
  shape (heel lifting, foot planted), not as *walking*. That is the §38 family.
- **Choose frozen or blurred and say which**, or the model averages the two. `[community]`
  [prompt-architects, 2026-09-02](https://prompt-architects.com/blog/359-sports-and-action-motion-prompts)
- **A still meant as the first frame of a clip:** keep head and feet inside the frame with ground below,
  and leave out motion blur and busy backgrounds. Cropped feet get invented and rarely match.
  `[community]` [wearview, 2026-07-16](https://wearview.co/blog/walking-video-from-single-photo)
- **Warm windows against a blue-hour sky is the real-estate HDR genre** (bracketed 3–5 stops). ⬜ *Inferred,
  unverified:* the scene itself pulls toward a glossy poster, the same shape as *advert vocabulary commissions
  an advert*. Counter it with "a single handheld exposure", both ends of the exposure named, and no *HDR*.
  `[community]` kolorheaven · digital-photography-school
- **The glamping slop look is fairy lights on canvas and trunks with a "warm ethereal glow".** Name the
  objects in a final scoped constraint. `[community, weak]`
- **Generated shadows fail on hard light and complex shapes, and soft shadows pass.** `[academic]`
  [arXiv 2311.17138](https://arxiv.org/abs/2311.17138) (CVPR 2024, older models). Soft whole-sky light, such
  as overcast or blue hour, is the easy case.

### 🔴 Observed on `9-walk` round 1, 2026-09-14 (n=1)

- **"The blue evening sky is the only light on him, dim and cool" came back as bright, even dusk.** The
  frame was readable everywhere, and his face and clothes were fully lit. A time of day plus *dim* does not
  darken the frame. Round 2 tries *"twenty minutes after sunset"*, *"falls away towards near-dark"* and a
  figure against the sky.
- ✅ **`@Tarquin-new` carried the whole outfit with zero wardrobe words**, including the sock-less loafers.

## Tenth web pass — 2026-09-14 `[academic]` `[community]`

Run for camping `9-walk` round 2 (the yurt large in the foreground, the man small far down a track). **New
items only. None tested on our work yet.**

- **Deep focus is the alternative to fake depth of field:** a wide lens, stopped down, with both the near
  and far layers stated as sharp. Community advice phrases it as "no DOF blur"; convert it per §23.
  `[community]` [prompt-architects](https://prompt-architects.com/blog/226-camera-and-lens-terms-that-change-your-ai-images)
- **Frame slightly wider than needed** when the still will seed a clip, so the clip can reframe or push in.
  `[community]` [film.fun, 2026-02-28](https://www.film.fun/articles/nano-banana-2-prompting-guide-frame-composition-and-reframing-for-ai-video)
- **Vanishing points are a known failure:** parallel lines don't meet properly. A path or road is two
  parallel lines. Check them, and curve the path rather than aiming it at the centre. `[academic]`
  [ControlVP, arXiv 2512.07504](https://arxiv.org/abs/2512.07504), tested on SD, not NB2.
- **A foreground object looks pasted on when its perspective or camera height doesn't match the scene.**
  `[community, weak]` (product compositing sources)
- **Small figures hold identity by silhouette and hair, not the face** (around 50px). Confirms §12.
  `[community]` [theneuralpost, 2026-01-28](https://theneuralpost.com/2026/01/28/nano-banana-vs-the-world-why-character-consistency-is-finally-solved/)
- **In image-to-video, a figure walking towards the camera morphs at the face first.** Counters: cast the
  Character in the clip, slow the approach, and stop it before a medium shot. `[community, inferred]`
  [wearview](https://www.wearview.co/blog/walking-video-from-single-photo)
- 🚫 **Do not cite** felo.ai on "Nano Banana Next / 3". It's reseller rumour with no Google source.

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
