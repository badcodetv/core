# Nano Banana 2 — image engine reference

**Model:** Gemini 3.1 Flash Image. Launched 26 Feb 2026.
**Also covers Nano Banana Pro** (Gemini 3 Pro Image), the sibling model in Flow's picker —
see [Third pass](#third-pass--nano-banana-pro-and-the-anti-slop-toolkit), which is where the
Pro-specific prompting and the engine recommendation live.
**Researched:** 2026-08-12 · **second pass 2026-08-12** ·
**third pass 2026-08-14** ([Pro, and the anti-slop toolkit](#third-pass--nano-banana-pro-and-the-anti-slop-toolkit)) ·
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
