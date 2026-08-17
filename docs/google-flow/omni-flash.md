# Gemini Omni Flash — video engine reference

**Model:** Gemini Omni Flash (`gemini-omni-flash-preview`). Announced at I/O 19 May 2026; developer
API access 30 Jun 2026. **Still public preview.**
**Researched:** 2026-08-12 · **second pass 2026-08-14**
([Prompt craft](#prompt-craft-what-a-failed-shot-taught-us)) · **third pass 2026-08-14**
([Physics shots and the input-mode matrix](#physics-shots-and-the-flow-input-mode-matrix)) ·
**fourth pass 2026-08-14** ([References vs frames](#references-vs-frames-the-prompt-has-to-change-shape)) ·
**fifth pass 2026-08-14** ([Making a reference stick](#making-a-reference-stick-there-is-no-adherence-knob)) ·
**sixth pass 2026-08-14** ([Making motion read as real](#making-motion-read-as-real)) ·
**Confirmed against our Flow session:** ~~never~~ **first confirmed run 2026-08-14** —
see [What we actually confirmed](#what-we-actually-confirmed-2026-08-14).

> **Read the verdict first.** On current evidence Omni Flash is *not* a drop-in replacement for the
> Veo-based recipe in `docs/superpowers/flow-video.md`, and there is a specific reason why — see
> [The animate-slide problem](#the-animate-slide-problem). Nothing should be rewired until that
> question is settled by a test.
>
> **⚠️ Partly overtaken by events, 2026-08-14.** Omni's Frames tab is real and a supplied
> start frame is honoured — we ran it. That removes the main objection, though not the
> end-frame one. [What we actually confirmed](#what-we-actually-confirmed-2026-08-14).

## What we actually confirmed (2026-08-14)

**The first `[confirmed]` entries in this folder.** Everything else here is still
hypothesis. Source: the Karen river-drop clip (`docs/stories/karen/prompts-river-drop.md`
§2g.13), accepted after four failed rounds.

| Claim | Status |
| --- | --- |
| **Flow shows a Frames tab with Omni Flash selected** | `[confirmed 2026-08-14]` |
| **A start frame loaded there is honoured** — the anchor's geometry survived: no re-staging, no invented terrain, people on the correct side of the railing | `[confirmed 2026-08-14]` |
| **Occluding the hard motion works.** Framing so a falling object exits frame within a few frames produced a clip that reads as real, after four attempts that kept it in frame all failed | `[confirmed 2026-08-14]` |
| **The 24fps / 180° shutter clause earns its place.** Asked for it; the fall came back as a streak rather than a sharp object, and no post pass was needed | `[confirmed 2026-08-14]` |
| **A grain/speed pass in post was *not* required** for the clip to read as captured | `[confirmed 2026-08-14]` |
| **⚠️ Flow's UI will not let you attach a character to a start frame.** Frames and Ingredients are mutually exclusive in the interface — you get the anchor or the character binding, never both | `[confirmed 2026-08-16]` (Kai, at the UI) |
| **Same plate, same prompt text, two tabs:** Frames returned a different woman; **Ingredients held the room *and* the face.** A Frame-shaped prompt fired in Ingredients did **not** re-stage | `[untested]` — n=1 each way, see the discipline note below |

> ### ⚠️ The combined mode does not exist in Flow
>
> **`[confirmed 2026-08-16]`, and it contradicts this file.** [Choosing the
> mode](#choosing-the-mode) says *"**Both** → stack them: an anchor frame plus character
> references is a documented combined mode `[runware]`."* **That is not available in
> Flow's UI.** Selecting a start frame removes the ability to add `@Character`
> ingredients. The `[runware]` claim may hold at the API layer; it does not hold on the
> surface we actually work on. **Treat mode as an exclusive choice.**
>
> **The routing rule that follows, and it is simpler than the old one:**
>
> | What must survive | Tab | Why |
> | --- | --- | --- |
> | The **composition** — an accepted plate, a geometry, a camera position | **Frames** | Ingredients re-stages; no prompt fixes that |
> | Only the **person** — new angle, new room, no accepted frame to start from | **Ingredients** | The only binding available, and the scene gets written out in full |
>
> **⚠️ Do not assume a start frame carries the character's identity.** The one time we
> tried it, Frames returned a different woman and the Ingredients tab — same image, same
> prompt text, plus the Character — held her
> ([above](#frames-lost-the-face-ingredients-held-both-n1-each-way)). n=1, so this is a
> caution rather than a rule, but **if the face has to be right, put the Character in the
> shot rather than trusting the plate to carry it.**

> ### Frames lost the face; Ingredients held both. n=1 each way.
>
> **2026-08-16, Kai, Karen §2h.4v — the same plate, the same scene, two tabs:**
>
> | Tab | Prompt shape | Result |
> | --- | --- | --- |
> | **Frames to Video** | *"the locked opening frame"* | **a different woman** — *"she looks completely different"* |
> | **Ingredients to Video** | **the same text, unchanged** | **room and face both held. Accepted** |
>
> **Two things to take from this, and neither is a law.**
>
> **1. The `[runware]` mode table is not the whole story.** It says Ingredients treats an
> image as a guide and *"the model is expected to re-stage the scene"*, and that
> Frame-shaped prompts are wrong for it. **Here a Frame-shaped prompt fired in Ingredients
> preserved the staging.** The wording *"use the attached image as the locked opening
> frame"* appears to be doing real work as **text reinforcement** — which is exactly what
> [lever 4](#4-text-reinforcement-is-the-substitute-for-a-knob) predicts, since words are
> the only strength control there is. **Worth trying before assuming Ingredients will
> re-stage.**
>
> **2. Frames lost a face that Ingredients kept.** One run each. That is a hint, not a
> capability claim.
>
> > ### ⚠️ Discipline note — this entry was rewritten twice in one day
> >
> > It first read *"a start frame does not hold a face,"* declaring Frames
> > composition-only from one failure. It was then retracted from one success — which
> > turned out to be **a different tab entirely**, so the retraction was wrong too.
> >
> > **The failure mode is mine, not the engine's: generalising a capability claim from a
> > single generation.** These models are stochastic and every run is n=1. **Record what
> > was fired, in which tab, and what came back. Do not promote it to a rule until the
> > same thing happens twice with something else varying.** The four-round river-drop
> > entries earned their `[confirmed]` tags precisely because they did not do this.
>
> **The two tabs are still mutually exclusive in Flow's UI**
> ([above](#️-the-combined-mode-does-not-exist-in-flow)) — that one is a UI fact and
> stands.
>
> **Working practice, stated as practice and not as a finding:** with an accepted plate,
> **Ingredients + the attached still + the character + "locked opening frame" wording** is
> the recipe that has actually produced accepted clips. Use it. If the staging drifts,
> add room nouns to the text; if the face drifts, reroll.
>
> **Open, and cheap to test:** whether a near-miss on the safety filter degrades a
> generation rather than blocking it. The two runs also differed by the
> [policy rewrite](../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail),
> so tab is not the only variable that changed.

**What is still not confirmed, and matters:**

- **Whether frame one is pixel-identical to the supplied plate.** The geometry held,
  which is what the shot needed and what four rounds of Ingredients never gave us. That
  is not the same as a pixel match, and nobody measured one. **The 2026-08-16 identity
  drift above makes this materially more doubtful** — a tab that changes the face may not
  be continuing from the plate at all. `animate-slide`'s contract needs the stronger
  claim — see [below](#the-animate-slide-problem).
- **Whether Omni has an end-frame slot.** Not exercised; the run left it empty.
- **`<IMAGE_REF_0>` / `<FIRST_FRAME>` in Flow's prompt box.** Still untyped.

> **The pattern worth keeping.** Four rounds of prompt craft fixed four real bugs and
> every clip still failed. What finally worked was a **change of mode and a change of
> shot** — the same lesson twice. On this engine, when a clip fails, ask what the shot
> is asking the model to do before rewriting a single word of it.

## Identity & availability

- "Create anything from any input — starting with video." Combines Gemini reasoning with
  generative video. `[vendor]`
- In **Google Flow** at launch, for **AI Plus / Pro / Ultra subscribers** globally. Also the Gemini
  app, plus free access via YouTube Shorts and the YouTube Create app. `[vendor]`
- Transformer-based, natively multimodal across text/vision/video/audio. `[vendor]`
- Headline capability is **conversational multi-turn editing** — "change specific things, or change
  everything" across turns while holding character consistency, physics and scene continuity. `[vendor]`
- API runs on the new **Interactions API**, which replaces the older `generateContent` pattern. `[vendor]`
- **SynthID** on outputs. The model *can* change people's speech; Google has **restricted that
  capability** pending safety work. `[vendor]`

## Hard limits

| | Omni Flash | Veo 3.1 (for comparison) |
| --- | --- | --- |
| Max duration | **10s** per generation `[vendor]` `[community]` | up to 60s with extension `[community]` |
| Max resolution | **720p native**, upscale to 4K on download `[yt]` | up to 4K native `[community]` |
| Aspect ratios | **16:9 (default), 9:16 only** `[vendor]` | wider set |
| Pricing | ~$0.10 per second of output `[vendor]` | — |

`task` values in `video_config`: `text_to_video`, `image_to_video`, `reference_to_video`, `edit`. `[vendor]`

Multi-turn editing threads via a **`previous_interaction_id`** parameter — the model "remembers the
video context, applying your changes while preserving elements you did not mention." `[vendor]`

Delivery defaults to base64 inline (~4MB cap); pass `delivery: "uri"` for anything larger. `[vendor]`

## Explicitly not supported `[vendor]`

- **Video extension and video interpolation.** (Veo's extension feature has no equivalent.)
- **Reasoning across multiple videos.**
- **Voice editing.**
- **Audio references** — "uploading audio references is unsupported in the current version."
  This directly contradicts the launch announcement's claim that voice references were supported
  from day one. Treat audio input as unavailable until proven otherwise; the announcement was
  probably aspirational or describes a surface other than the API.
- **System instructions, temperature, `top_p`, stop sequences, and negative prompts.**
- Video references up to 3s are *accepted by the API schema* but **not correctly processed** by the
  model. A silent no-op, which is the worst kind.

**Regional restriction:** editing *uploaded* videos is excluded in the **EEA, Switzerland and the
UK**. `[vendor]` BadCode is UK-based — assume the `edit` task on our own uploaded footage is
unavailable until someone checks. This may be the single most consequential line in this file.

## Known failure modes

From Google's own model card `[vendor]`:

- Maintaining complete consistency throughout edits
- Generating scenes with complex motion
- Rendering perfectly accurate text

From practitioners `[community]` — the developer-forum thread is the best source we found:

- **Very high false-positive safety-block rate.** One creator reported ~90 of 100 generations
  failing on benign material ("a porcelain statue inside an orbital museum", dark-fantasy scenes).
- **Blocked generations still consume credits**, with no automatic refund. Google staff responded
  with policy links and a pointer to manual Cloud Billing refunds; they did not commit to automatic
  refunds or to explaining individual blocks.
- **No true first-frame-to-video.** Rather than accepting a precise starting frame, it references
  "through the agent", causing heavy redesign of characters and environments and loss of the
  intended visual identity.
- **Object permanence failures** — one report of the model introducing a statue present in neither
  the reference nor the prompt.
- Some users moved production work needing consistency to competing tools.

Preview-stage complaints age fast; re-check before treating any of this as settled. But the block
rate and the credit burn are consistent with what we already know about Flow's filter.

## The animate-slide problem

`animate-slide` exists to take an **already-approved, already-art-directed panel** and put it in
motion. The finished panel *is* the first frame — that is the entire contract. A model that treats
a supplied image as a loose reference and redesigns from it doesn't do a worse job of that; it does
a different job.

**The YouTube pass largely settled this, and the answer is bad for Omni Flash.** Kevin Stratvert,
demonstrating inside Google Flow itself, hits it directly: to use start *and* end frames you must
switch the model to **Veo 3.1 – Quality**, because "**Omni doesn't currently support an end
frame**" `[yt]`. Independently, a VFX creator running Omni through Higgsfield reports that when the
reference workflow kept redesigning his scene, "the only way I could get the result I was after was
actually just using the start and end frame feature" — i.e. frame-anchoring is what rescues a shot
Omni's reference mode mangles `[yt]`.

> **⚠️ Both halves of that paragraph are now contested — see
> [the input-mode matrix](#the-input-mode-matrix-and-a-conflict-worth-resolving) (2026-08-14).**
> Google's own feature page says first+last frames are **Veo 3.1 Lite and Fast, not Quality**,
> and Flow's changelog says **Omni gained Frames-to-Video in June 2026**. `[vendor]` outranks
> `[yt]`, so treat the Stratvert demo as describing an older build. The conclusion below survives
> — frame-anchoring is still Veo's job — but the specific model named in it is probably wrong.
>
> **Update, fifth pass 2026-08-14:** half of the conclusion no longer holds. Omni has a
> **first**-frame mode ([why](#1-mode--and-omni-does-have-frames-now)), so
> `animate-slide`'s single-anchor contract is now plausibly an Omni job too. Only
> **end**-frame pinning is still exclusively Veo's.

Combined with the `[community]` report of no true first-frame-to-video, the working conclusion is:

> **`animate-slide` stays on Veo 3.1.** The skill's contract — an approved panel is frame one —
> is a frame-anchoring problem, and in Flow that is Veo's job, not Omni's.

**Status 2026-08-14: the objection is half-dead.** Omni's Frames tab exists and honours
a start frame `[confirmed 2026-08-14]` — a supplied plate's geometry survived intact
through a clip that four Ingredients-mode attempts had re-staged. So the verdict above
now rests on the *end*-frame gap alone, which is narrower than what it was written on.

The confirming test still has not been run, and it is the one that decides it:

> Take one accepted panel with a cast Flow Character. Load it as a start frame in
> Omni's Frames tab. Does frame 1 match the panel **pixel-for-pixel**, or has the
> character been redesigned?

**"The geometry held" is not "the pixels matched."** `animate-slide` needs the stronger
claim, because its whole contract is that an already-approved, already-art-directed
panel *is* frame one. Until someone measures it, the skill does not move.

Omni Flash remains interesting for `music-video-short`, where clips are generated fresh and no
golden original is at stake — and for restyling clips Flow generated itself (see below).

Note also that Nano-Banana-keyframes-into-Veo is a workflow Google itself documents (generate
keyframes with Nano Banana, animate between them with Veo). That is essentially our existing
pipeline, and it is still the vendor-recommended path for image-anchored motion.

## Field tips from the YouTube pass `[yt]`

Harvested 2026-08-12 from the most-viewed tutorials (sources at the bottom). Practitioner
observation, not vendor doc — but several of these are demonstrated on screen, which puts them a
tier above forum hearsay.

### What Flow actually exposes

- **Video tab → model picker** switches between Omni and Veo. **Frames** (first/last) and
  **Ingredients** are the two input modes.
- **Ingredients is the high-control path** — upload video, audio, images, characters and reference
  sheets together and generate from the lot. Repeatedly called the most underrated feature in Flow.
- **30 credits per 10-second video** in Flow.
- **Agent mode**: plans and writes scripts, then generates images/videos itself. Settings let you
  cap the number of generations and require **approval before it generates** — set that, or it
  spends credits unattended.
- **Storyboard Studio** (left nav → tools → prompting): script → scenes → assets
  (characters / locations / props) → *autofill* → a full storyboard of consistent images, because
  every frame references the same asset set. Right-click any storyboard image to animate it or add
  it to a prompt as reference.
- **Shot Explorer** (tools): upload one image, click right / up / down / zoom out / surprise me, and
  it generates that image from a new camera angle.
- **Tools are user-authorable.** The gallery holds natural-language workflows built by Google and
  partners; you can remix one, build your own from a prompt, and share it by link `[vendor]`.
- **Flow Characters now carry a voice.** Create the character, use the built-in `+` prompt to
  generate a front / side / full / close-up **reference sheet**, then attach a stock or custom
  voice. The voice then stays consistent across every generation using that character.
- **Video downloads carry a visible watermark.** (Flow *images* do not — they carry only the
  invisible SynthID.)

### Prompt craft

> **Omni is not Veo, and Veo habits actively hurt here.** Google shipped a five-tip prompt guide
> with the model (May 2026) and the practitioner consensus around it is consistent: Omni wants
> **short natural language**, not the adjective stacks and long constraint blocks Veo rewards. It
> "doesn't need to be as prescriptive as Veo."

- **Formula:** `[Subject] + [Action] + [Setting] + [Camera] + [Lighting] + [Style]`, written as
  prose. Note it is the *same six slots* as the Nano Banana formula with Camera promoted.
- **Keep it under ~50 words.** Prompts beyond that are reported to **dilute focus and reduce output
  quality** — the single biggest difference from writing for Veo.
- **Lock the shot in the opening sentence.** `"Create a [duration]-second [aspect] [genre] video in
  one continuous shot."` This is reported to hold duration, format and single-take more reliably
  than any metadata setting.
- **⚠️ Omni defaults to cutting.** Left alone it "builds a short narrative from a few different
  shots." If you want one unbroken move you must say **single continuous shot / no scene cuts** —
  this is the failure mode most likely to ruin a slow push.
- **Camera verbs Omni actually parses:** Push (punch in, dolly zoom) · Pull (pull-back, pull-up,
  pull-down) · Reveal (ascend revealing, pull-back and rotate) · Orbit (orbit, sweep around,
  circle) · Pan (left, right, vertical) · Static (locked off, fixed, oner, continuous shot). Camera
  *character* also parses: natural smartphone zoom, film camera (warm grain), webcam, handheld
  (micro-jitter).
- **Lead with the camera phrase — "the first words set the shot grammar, and everything after
  fills it in"** `[runware]`. Consistent with [`camera-vocabulary.md`](../flow/camera-vocabulary.md#rules)
  rule 1. ⚠️ **In Ingredients mode this collides with the role-declaration line**, which also wants
  to be first. BadCode's resolution (Karen §2h.6v): **frame-lock line first, camera paragraph
  second, action third** — identity outranks grammar, and second position still beats burying the
  move mid-description.
- **Style preservation is an explicit list, not an assumption.** The working shape is
  `"[change]. Keep [X, Y, Z] exactly the same."` **Without naming what to preserve, Omni will
  re-style the whole scene when asked to change one element.**
- **With a reference image, say what the image is for** — and there are two distinct phrasings that
  select different behaviour `[community]`:
  - **`"Use the given image as the starting frame."`** — engages first-frame behaviour.
  - **`"Use the given image(s) as references for video generation. The images should not be used as
    literal initial frames."`** — engages loose reference behaviour.

  **This partially reopens the [animate-slide question](#the-animate-slide-problem).** The
  no-true-first-frame reports may describe the *default* behaviour rather than a hard limit — there
  may be an instruction that pins frame one. Worth testing before treating Veo as the only option.
  It does not affect the **end**-frame finding, which is separate and confirmed.
- **Spend the rest of the prompt on what the image cannot show**: motion, timing, audio.
  Re-describing what is already visible wastes the word budget and invites drift.
  **⚠️ True in Frame mode only** — in Reference/Ingredients mode the opposite holds and the
  prompt must carry the staging. See
  [References vs frames](#references-vs-frames-the-prompt-has-to-change-shape).
- **One main action per clip.** If the source image holds several elements, keep the prompt to a
  single action or the animation loses coherence. With no extension or interpolation available,
  **plan an action that starts and resolves inside the 10 seconds.**
- **Separate the three channels when editing:** source motion / new style / protected details —
  e.g. *"Keep the hand movement and timing. Change the object into translucent crystal. Replace the
  room with a moonlit studio. Preserve camera motion."*
- **Audio is part of the prompt.** Omni generates sound; unprompted it picks its own. Name it
  ("slow smoky jazz", "sizzling broth and soft city rain") and say "no dialogue" if you want none.
- **One change per edit turn**, and over-detailed edit instructions trigger unintended changes.
- **Large bold text renders well; small type garbles** — and the prompt guides go further: avoid
  mentioning on-screen text at all unless you need it, since any signage/labels/captions degrade.
- **Over-specifying camera can backfire.** One creator got a correct multi-shot sequence when he
  said little about camera, and total incoherence (flip direction reversing shot to shot,
  background people appearing and vanishing) when he gave detailed camera instructions.

### Motion difficulty ranking `[community]`

Worth knowing before you design a shot around a subject:

| Reliability | Motion |
| --- | --- |
| Best | walking, talking |
| Degrades | fine hand articulation — frame to hide hands where possible |
| Artefact-prone | **dancing, gymnastics, and playing instruments** |
| Weak | character consistency across 4+ shots (~3/5); use reference images |

The instrument-playing entry is a live constraint for BadCode: a jazz-trio shot should keep the
players near-static or in silhouette rather than asking for performance.

### The two-part constraints-first frame (Veo-style, still useful)

From a VFX creator with a decade in the industry: open with a block of **constraints — what must
NOT change** — then describe the effect. Reusable by swapping the effect and keeping the block.
**Use this for Veo.** On Omni, compress it to the `Keep [X, Y, Z] exactly the same` clause instead,
or the word count alone will cost you quality.

### Where it is strong, and where it falls over

**Strong:** object tracking through rotation, material and style swaps, relighting, restyling a
whole clip, replacing dialogue, single-position talking avatars, motion graphics with animated text,
generating extra camera angles from one take, subject replacement preserving original motion.

**Weak:** complex physics, multi-shot sequences, camera moves into areas the source never showed
(distortion in the unseen geometry), storyboard-driven cinematic sequences, small text.

### The asymmetry that matters most

**The policy filter is dramatically harsher on uploaded video than on video Flow generated itself.**
"You can barely edit your own uploaded videos without getting hit with policy violations… it works
much better with videos generated directly inside Flow." `[yt]`

Practical rule: **generate inside Flow, then edit — do not upload and edit.** This compounds with
the documented UK/EEA restriction on editing uploaded video, and it points the same direction: our
footage should originate in Flow if we want Omni to touch it.

### Prompt adherence is the recurring complaint

Independent of safety blocks, Omni sometimes simply does its own thing: returns the source footage
near-unchanged when asked for a clear effect, silently alters things nobody asked about (removing
glasses, flipping a cap's orientation, swapping an entire environment when asked only to change an
outfit), and occasionally ends a clip with a stuttering loop. One creator rates the adherence as
comparable to Veo 3.1 — a step down from current best-in-class. Budget for regenerations.

## The `<FIRST_FRAME>` tag — a documented binding mechanism `[vendor]`

**Found 2026-08-12** while writing the Karen §2d clip prompts, in Google's own API
reference. It was missed on the first pass and it bears directly on
[the animate-slide problem](#the-animate-slide-problem).

The API documents **explicit inline tags that assign a role to each uploaded image**:

- **`<FIRST_FRAME>`** — placed inline at the *start* of the prompt text, binds an
  image to the starting-frame role. Documented example: `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`** — reference images, **zero-indexed**, up to six. Documented
  example: `"in the style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking"`
- **Explicit declaration prefixes** for multi-image prompts:
  `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]`

**Why this matters.** The `[community]` complaint recorded above — "no true
first-frame-to-video… references through the agent, causing heavy redesign" — reads
very differently now. There *is* a first-frame binding mechanism; the complaint
most plausibly describes **default reference behaviour when the role was never
declared**. That is a configuration problem, not a model limitation.

**It does not overturn the verdict yet**, for two reasons: this is *API* syntax and
`animate-slide` runs through Flow's UI, and the **end-frame** finding is separate and
independently confirmed (Omni has no end frame; Veo 3.1 Quality does). But it
converts the first-frame question from "the model can't" to "we never asked
properly", and it makes the confirming test more urgent, not less.

**The cheap test:** type `<FIRST_FRAME>` into Flow's prompt box on a plate with a
known-exact composition and see whether frame one comes back pixel-matched. If Flow
passes prompt text through to the model unmodified, the tag should work there too.

Two further points from the same reference:

- **Guiding instructions go at the *end* of the prompt** — "add instructions at the
  prompt's end", e.g. `Use this image as the starting frame.` Our §2b prompts put it
  second; the Karen §2d set moves it last.
- **Timecodes parse**: `[0-3s] A person is walking`, or plain "after three seconds".
  Useful for beat-timed motion graphics, which is one of Omni's stronger modes.

Sources: [Generate and edit videos with Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni) `[vendor]` ·
[DeepMind Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/) `[vendor]`
(the latter now fetches, and confirms the five core elements and the
"you don't have to be as prescriptive" line the practitioner guides restate).

## Prompt craft: what a failed shot taught us

**Added 2026-08-14**, from a second research pass triggered by a real failure — the
Karen river-drop clip (a phone falling off a railing into water) came back wrong
repeatedly, and the diagnosis turned out to be entirely in the prompt. The full
post-mortem with the offending text is in
[`docs/stories/karen/prompts-river-drop.md`](../stories/karen/prompts-river-drop.md);
the reusable findings are here.

### ⚠️ Negatives do not work, and they actively backfire

The single most consequential finding, and it invalidates a habit carried over from
Veo and from Nano Banana.

- Omni Flash has **no negative-prompt parameter** `[vendor]` — already recorded above
  under *Explicitly not supported*, but the consequence was never spelled out.
- The workaround everyone reaches for — putting the negation in the prompt body — is
  **specifically counter-recommended**: instructive language using `no` or `don't`
  ("no walls", "don't show walls") performs *worse* than not mentioning the thing at
  all `[community]`. **Reframe constraints positively or omit them.**

The failed prompt carried ~20 negations and named *float*, *bounce*, *skip*, *hover*
and *second phone* into a model that cannot subtract them. It got what it asked for.

**The rewrite pattern — same constraint, positively stated:**

| Instead of | Write |
| --- | --- |
| `it does not float, bounce or reappear` | `the surface closes over it and goes dark` |
| `no reaction, no lunge, do not look down` | `the hand stays where it is` |
| `no slow motion, no speed changes` | `at real speed` |
| `do not chase it, no aggressive camera move` | `locked off` |
| `the Wonder Wheel does not turn` | `the Wonder Wheel stands still` |

Two established exceptions that appear to be safe, because they are the vendor's own
documented phrasing: **`no dialogue`** for audio, and **`no cuts` / `single
continuous shot`** for the shot lock. Both are recommended in Google's own guidance
`[vendor]`, so treat them as idiom rather than as negation. Everything else gets the
positive restatement.

### Length: three to four sentences, and the lever is subtraction

> *"The biggest single quality lever in Omni Flash prompting is what you remove, not
> what you add."* `[runware]`

The sources disagree on the surface and agree underneath:

| Source | Says | Tier |
| --- | --- | --- |
| Runware | three to four sentences covering the five elements | `[runware]` |
| geminiomniprompts | under ~50 words; beyond that dilutes focus | `[community]` |
| promptslove | 50–150 words; "specificity over brevity" | `[community]` |
| DeepMind | no word limit; *"the more detail you add, the more control"* | `[vendor]` |

**The resolution is that the axis is not length, it is kind.** DeepMind's own guide
says in the same breath *"you don't have to be as prescriptive"* and *"you don't need
to describe it across every frame."* Detail about **what the shot is** — the five
elements — buys control. Prescription about **how the model should achieve it** —
timecoded beats, frame-by-frame narration, mechanism explanations — buys nothing and
costs focus. The failed prompt ran ~450 words and almost all of it was the second kind.

### Do not explain physics to it

Omni reasons about gravity, kinetic energy and fluid dynamics from world knowledge
`[vendor]`. Naming the action is the documented method; explaining the mechanism is
waste:

> Instead of explaining how rain creates motion blur or how a beam refracts through
> water, state: *"The lighthouse beam rotates slowly through the dusk light, cutting
> through the rain."* `[runware]`

So `immediate downward acceleration under gravity`, `the phone gains speed
continuously as it falls`, `rotation remains physically consistent` are all dead
words. `the phone falls into the river` is the whole instruction.

### Design the shot around the difficulty ranking, not against it

The [motion difficulty ranking](#motion-difficulty-ranking-community) above is a
*shot-design* input, not trivia. The failed clip put **complex physics** (a water
entry) and **fine hand articulation** (the release) — the two documented weak
areas — in frame simultaneously, as the subject, with the camera tracking them.

Three counters that generalise:

- **Give a hard-to-track subject its own light.** A dark object moving through a dark
  frame is where morphing artefacts live; a small self-luminous object is the easiest
  possible tracking target. In the river shot this meant *the phone's screen is on* —
  which was also more truthful and gave the edit its cut point.
- **Let the camera not help.** A camera that anticipates an accident reads as staged,
  and a move into geometry the plate never showed is the documented distortion case
  `[yt]`. Locked off is both the safer and the more honest choice for anything
  unplanned.
- **When a shot needs a documented weakness, cut around it instead.** The fallback
  for the river drop removes the water entry from frame entirely and cuts to a
  different register for the underwater beat. The audience gets the full physics; the
  model never renders it.

### Ingredients: three slots, most important first

**Ingredients is the high-control input mode** in Flow `[yt]`. Practical rules:

- **Three reference images maximum** per generation in the Flow UI `[community]` —
  note the API documents up to six `<IMAGE_REF_N>` slots `[vendor]`, so this ceiling
  is a Flow-side limit and worth re-checking.
- **Order matters — put the most important element first** `[community]`.
- **Consistent look across ingredients helps the blend** `[community]`; mixing
  registers gives the model a choice it will make badly.
- **Every unnecessary ingredient is another thing to drift.** Leave slots empty.
- **Do not cast Flow Characters into a shot with no face in frame.** It buys nothing
  and adds a binding that can fail.

Role-declaration syntax, **still `[untested]` in Flow's prompt box** — see
[The `<FIRST_FRAME>` tag](#the-first_frame-tag--a-documented-binding-mechanism-vendor):

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]
```

Until that is confirmed, the plain closing sentence `Use this image as the starting
frame.` is still doing the work.

### Multi-turn: one category per turn

Consistent across sources and worth more than it sounds `[community]`:

- **Split edits by category** — one turn for lighting, one for camera, one for
  action, one for audio. Concentrating them in a single turn applies them all with
  measurably lower control.
- **End every edit turn with `Keep everything else identical.`** Without a
  preservation clause Omni drifts on elements nobody asked it to touch — the same
  finding as the `Keep [X, Y, Z] exactly the same` rule recorded above, generalised.

### Sources for this section (2026-08-14)

- **[Cinematic prompting for Gemini Omni Flash — Runware](https://runware.ai/docs/models/google-gemini-omni-flash/guides/cinematic-prompting) `[runware]`** — the most craft-useful single page found in either pass: the three-to-four-sentence scaffold, camera vocabulary first, name-the-action-not-the-mechanism, and the subtraction lever. New tier tag; it is a model-host's own doc, so above `[community]` and below `[vendor]`.
- [Gemini Omni Flash keeps rejecting your prompts — Segmind](https://blog.segmind.com/gemini-omni-flash-keeps-rejecting-your-prompts-9-fixes-that-actually-work/) `[community]` — the `no`/`don't` backfire finding.
- [Google Omni Prompting Guide — Promptslove](https://promptslove.com/blog/google-omni-prompting-guide/) `[community]` — world-knowledge grounding; the `Keep everything else identical` clause; per-category edit turns.
- [Veo 3.1 Ingredients to Video](https://www.veo3ai.io/blog/veo-3-1-ingredients-to-video-guide-2026) `[community]` — three-ingredient ceiling, order matters. Describes the **Veo** path; assumed to hold for Omni, unconfirmed.
- [AI Video Quality Checklist — Green Frog Labs](https://greenfroglabs.com/blog/ai-video-quality-avoid-slop-appearance) · [AI Slop: 12 Tells — Opus](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells) `[community]` — the motion tells: morphing edges, *"mathematically smooth rather than physically real"* movement, floating objects, hand-heavy shots.
- [DeepMind Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/) · [Gemini API — Omni Flash](https://ai.google.dev/gemini-api/docs/omni) `[vendor]` — re-fetched and unchanged from the 2026-08-12 pass.

**Everything in this section is `[untested]` against our own Flow session.** It is
better-sourced than a guess and it explains an observed failure, which is why it is
written down — but nothing here has been through the
[calibration protocol](./README.md#calibration-protocol-how-untested-becomes-confirmed).

## Physics shots, and the Flow input-mode matrix

**Added 2026-08-14, third pass.** Triggered by the Karen river drop failing a
*second* time, on a rewritten prompt. The two reported bugs were **the character
appearing on the wrong side of a railing** and **the falling phone glitching and
flying upward**. Both turned out to be structural rather than verbal, which is why
the prompt rewrite alone did not fix them.

### The input-mode matrix, and a conflict worth resolving

Flow's model picker is not interchangeable. From Google's own
[models & supported features page](https://support.google.com/flow/answer/16352836) `[vendor]`:

| Mode | Veo 3.1 Lite / Fast | Veo 3.1 Quality | Omni Flash |
| --- | --- | --- | --- |
| Text → video | ✅ | ✅ | ✅ |
| **Frames → video (first frame)** | ✅ | ✅ | ~~❌~~ **✅ `[confirmed 2026-08-14]`** |
| **Frames → video (first + last)** | ✅ | ❌ | ❌ |
| Ingredients / references → video | ✅ (8s) | — | ✅ (10s, incl. character & audio refs) |
| Durations | 4s / 6s / 8s (Fast also 10s) | 4s / 6s / 8s | **4s / 6s / 8s / 10s** |

> **⚠️ Two conflicts, both `[untested]` and both one click away from an answer.**
>
> 1. ~~**Omni and first frames.**~~ **Settled `[confirmed 2026-08-14]` — the help page
>    is stale.** The Frames tab is there with Omni selected and a start frame loaded
>    into it is honoured; we ran it. Flow's changelog was right and the matrix page is
>    out of date. Read the row below as **first frame ✅ / first+last ❌** for Omni.
> 2. **Veo Quality and end frames.** This page says first+last is **Lite and Fast
>    only**. That contradicts the `[yt]` claim recorded above — Kevin Stratvert
>    demonstrating that you switch to *Veo 3.1 Quality* for start and end frames.
>    `[vendor]` outranks `[yt]`, so the table above is what to believe until someone
>    looks.
>
> Either way the practical rule holds: **if a shot needs its end state pinned, that
> is a Veo 3.1 Lite/Fast job, not an Omni job.**

**The consequence we had missed:** a prompt ending `Use this image as the starting
frame.` does nothing structural if the image was loaded as an **Ingredient**.
Ingredients are *references* — the model is free to reinterpret the geometry, and it
will. That is a sufficient explanation for a character swapping sides of a railing.
**If the plate's geometry must be respected, it has to go in as a Frame, not an
Ingredient.**

### Why falling objects fail, and what actually fixes it

This is not a prompting problem and no wording fixes it. Video diffusion models have
**no physics engine**; they have absorbed the statistical pattern that unsupported
things accelerate downward, and they make **semi-independent decisions per frame, so
small errors compound over time** `[community]`. The documented symptoms are exactly
what we saw: *"objects float, accelerations drift, and collisions behave
inconsistently"* `[community]`.

A small object in multi-second free fall is therefore close to the **worst possible
subject** for the medium. Four levers, in order of how much they actually buy:

1. **Pin the end state.** A first **and last** frame turns free generation into
   interpolation between two known states — the model cannot fly the object upward
   because the final frame says where it ended up. This is the only true fix, and it
   means **Veo 3.1 Lite/Fast**.
2. **Occlude the hard motion.** Let the scene's own geometry hide it — a railing, a
   frame edge, a foreground object. Frames never rendered cannot drift. This costs
   nothing and usually looks *better*, because it is what a real camera would catch.
3. **Shorten the clip.** Drift compounds per frame, so **4s is meaningfully safer
   than 10s** for a physics beat. We had been defaulting to 10s everywhere out of
   habit; Flow offers 4s / 6s / 8s / 10s and the short end is free quality on any
   shot that does not need the runtime.
4. **Give the object its own light.** A self-luminous object is the easiest possible
   tracking target; a dark object against dark water is the hardest, and morphing
   lives there.

**And the one that removes the problem rather than mitigating it: render the event as
audio.** Omni generates sound natively, so a splash can be *heard* while nothing
splashes on screen. A real film would cut this way regardless. Physics you don't
render cannot go wrong.

### Spatial geometry: models have no world model

Related failure, same root. Models trained on 2D clips *"don't inherently understand
3D space, depth, or physics"* and exhibit **geometric warping and perspective
failures despite plausible per-frame visuals** `[community]`. "Which side of a barrier
is a person on" is genuinely unreliable, not a fluke.

Counters that work at the prompt and plate level:

- **Put the camera unambiguously on one side**, and say so. A camera described as
  *outside* a railing implies a viewpoint over the water, and the model may resolve
  that by moving the people out there too. *(This is precisely how our own plate
  caused the bug.)*
- **Show the ground plane.** Pavement under her feet in frame is an anchor no amount
  of prose replaces.
- **Use the barrier as a foreground occluder.** A rail crossing in front of the
  subject settles the depth ordering visually rather than verbally.

#### ⚠️ Moving objects *inside a reflection* — one observed failure, and the mechanism is here

**Karen §2h.6v round 1, 2026-08-17.** The clause was *"traffic moves in the reflection
behind her"* — a push-in on a woman in a glazed phone kiosk. Kai's verdict on what came
back: *"the traffic going past looked very strange."*

**n=1, so this is not a rule yet** — but it belongs under this heading rather than under
bad luck, because a reflection is **geometry twice over**: the engine has to hold where
the vehicle is, where its mirror image lands, and how both move, every frame, with no
world model to do it in. That is [the falling-object problem](#why-falling-objects-fail-and-what-actually-fixes-it)
with an extra transform on top.

**The working counter is substitution, not instruction.** Round 2 cut moving objects from
the glass entirely and replaced the ambient motion with **steam off a pavement vent** —
formless motion has no geometry to get wrong, which is why dust, steam and drifting light
keep earning their place in these blocks. The traffic moved to the **audio**, where it
reads free.

**Generalise carefully:** what is claimed here is that *this* shot failed and that the
mechanism is the documented one. Whether reflections of moving objects fail *reliably*
wants a second sighting with something else varying — see
[the discipline note](#frames-lost-the-face-ingredients-held-both-n1-each-way).

### Slop counters specific to motion `[community]`

Additions to the table in the previous section:

- **Film grain at 10–15% opacity** counteracts the too-clean look — for us this is
  already the §1 `STYLE LOCK`'s job, which is a point in the house style's favour.
- **A 10–15% speed adjustment in the edit** makes AI motion read as more natural.
  Post, not prompt, but worth knowing before a clip gets binned.
- **Review frame by frame before accepting** — flicker, morphing, inconsistent
  shadows. The failure is usually in a handful of frames, not the whole clip.
- **Less motion is safer motion.** Over-animation is the tell; explicit "motion
  bucket"-style restraint is the counter.
- **⚠️ When a moving element fails, demote it to sound.** BadCode's own rule, and the
  first thing here with **two independent sightings**: reflected traffic that came back
  "very strange" (Karen §2h.6v) and a background walker who vanished mid-stride (Karen
  §2j.5v), both 2026-08-17. In each case the element was **cut from the picture and kept
  in the audio** — distant traffic, a turnstile beep — and the scene still read as
  populated. **A sound never grows a second leg.** Prefer this to describing the element
  more carefully; a second attempt at the same motion is the expensive way to learn the
  same thing.
- **State emptiness positively.** *"The lobby behind her is empty and still, and stays
  empty for the whole shot"* does a negative's job without being one. If a figure still
  materialises, **crop the reference** so the doorway or turnstile is out of frame —
  nothing can hallucinate a walker into a wall.

### Sources for this section (2026-08-14)

- [Google Flow — models & supported features](https://support.google.com/flow/answer/16352836) `[vendor]` — the input-mode matrix and durations.
- [Google Flow changelog](https://labs.google/fx/tools/flow/changelogs) `[vendor]` — Omni Frames-to-Video, June 2026.
- [What about gravity in video generation? Post-Training Newton's Laws with Verifiable Rewards](https://arxiv.org/html/2512.00425v1) — *"objects float, accelerations drift, and collisions behave inconsistently."*
- [Making AI video generators smarter about physics — Johns Hopkins](https://engineering.jhu.edu/ece/news/making-ai-video-generators-smarter-about-physics/) — no physics engine; statistical patterns only.
- [Temporal consistency explained — Picto](https://picto.video/en/learn/temporal-consistency/) `[community]` — per-frame semi-independent decisions, errors compounding.
- [Measuring 3D Spatial Geometric Consistency in Dynamic Video Generation](https://arxiv.org/pdf/2603.19048) · [Why spatial awareness is the missing key](https://www.technoohub.com/why-spatial-awareness-is-the-missing-key-in-generative-video) `[community]` — no world model; geometric and perspective failures.
- [Veo 3.1 first/last frame](https://www.eachlabs.ai/google/veo3-1/veo3-1-first-last-frame-to-video) `[community]` — interpolation between pinned endpoints.
- [AI Video Quality Checklist — Green Frog Labs](https://greenfroglabs.com/blog/ai-video-quality-avoid-slop-appearance) `[community]` — grain opacity, speed adjustment, frame-by-frame review.

## References vs frames: the prompt has to change shape

**Added 2026-08-14, fourth pass.** Triggered by the Karen drop clip **ignoring its
reference image and re-staging the scene**. That is not a bug and no amount of
insisting fixes it — *"the model treats it as a subject and style reference rather
than locking it as the first frame, with the model expected to re-stage the scene…
this is the expected behavior"* `[community]`.

### The two modes want opposite prompts

From Runware's reference-driven guide `[runware]`:

| | **Reference / Ingredients** | **Frame** |
| --- | --- | --- |
| What the image is | visual ground truth for style, character, composition — a *guide* | the locked opening composition |
| How many | up to **7** (Flow UI exposes fewer) | **exactly 1** |
| What the prompt must do | **describe the new scene**, plus assign each image a role | *"emphasise action and narrative after the anchor"* — what happens **next** |
| Re-describing the scene | **required** — the text carries the staging | **wasteful** — the anchor carries it |

> **This resolves a contradiction that has been sitting in this file.** The
> [prompt-craft section](#prompt-craft-what-a-failed-shot-taught-us) says *"spend the
> rest of the prompt on what the image cannot show — re-describing what is already
> visible wastes the word budget and invites drift."* That advice is **correct for
> Frame mode and exactly wrong for Reference mode.** In Reference mode the model has
> no obligation to the image's staging, so a motion-only prompt leaves it nothing to
> hold and it invents a scene.
>
> **The failure that prompted this pass was precisely that mismatch:** a prompt
> written in Frame-mode shape, fired in Ingredients. Both halves were individually
> defensible and the combination had nothing in it.

**Corollary on length.** The three-to-four-sentence target assumes frame anchoring.
**Reference-mode prompts are legitimately longer** because they carry the staging as
well as the motion. That is not licence to return to 450-word specs — the extra words
buy *scene description*, never frame-by-frame narration or negation piles.

**Corollary on drift.** In reference mode, *"add detailed appearance descriptions to
your prompt, reinforcing your character's appearance in text to prevent the model
from drifting from the reference"* `[community]`. Wardrobe and staging in words, not
faces — our casting rule still holds, and it costs nothing here.

### Choosing the mode

- **The plate's exact composition matters** (an approved panel, a geometry that must
  survive) → **Frame**. ~~If Omni's Frames tab is unavailable, that is a Veo job.~~
  **Omni has a Frames tab as of June 2026** — see
  [the fifth pass](#1-mode--and-omni-does-have-frames-now). Only an *end* state that
  must be pinned still forces Veo.
- **Only the look, the characters or the props matter**, and the shot may be
  re-staged → **Reference / Ingredients**, with the scene written out in full.
- ~~**Both** → stack them: an anchor frame *plus* character references is a documented
  combined mode `[runware]`.~~ **⚠️ Not available in Flow — `[confirmed 2026-08-16]`.**
  Selecting a start frame removes the `@Character` option. See
  [the combined mode does not exist in Flow](#️-the-combined-mode-does-not-exist-in-flow).
  **Mode is an exclusive choice**, and a start frame that already shows the character
  does not need one.

### Realism: name the imperfections, and refuse to compose

The craft half of the same pass, and it lines up with the house `STYLE LOCK` `[community]`:

- **Explicit imperfection tokens stop the smoothing.** `film grain`, `motion blur`,
  `slight chromatic aberration`, `ISO noise`, `halation` — *"prompts that include
  these stop the AI from smoothing everything out."* Our §1 lock already asks for
  most of them on the image side; **clip prompts should carry them too**, and mostly
  have not.
- **Name the capture, not just the look:** focal length, film stock, lighting
  condition. Again already the lock's vocabulary.
- **For vérité, instruct it *not* to compose.** *"Documentary AI film prompts work
  best when you explicitly instruct the model not to compose cinematically —
  available light, handheld presence, and real-time pace are what separate vérité
  from everything else."* For an accident caught on camera, that **is** the cinematic
  choice: a camera that is not helping is what reads as real.

### Sources for this section (2026-08-14)

- **[Reference-driven video with Gemini Omni Flash — Runware](https://runware.ai/docs/models/google-gemini-omni-flash/guides/reference-driven-video) `[runware]`** — the mode table above: reference images as persistent ground truth vs a single locked opening frame, the 7-vs-1 limits, and the opposite prompt shapes each wants.
- [Gemini Omni Flash reference-to-video — ShortGenius](https://shortgenius.com/models/google-gemini-omni-flash-reference-to-video) `[community]` — *"treats it as a subject and style reference rather than locking it as the first frame… expected to re-stage the scene."*
- [Google Flow AI prompts guide](https://whiskailabs.net/google-flow-ai-prompts/) `[community]` — reinforce appearance in text to prevent drift from a reference; the `@` asset syntax.
- [Realistic AI video prompting — Magic Hour](https://magichour.ai/blog/realistic-ai-video-prompting) · [AI film prompts by genre — Imagine.art](https://www.imagine.art/blogs/ai-film-prompts-guide) `[community]` — imperfection tokens, capture specifics, and the don't-compose-cinematically rule for documentary.

## Making a reference stick: there is no adherence knob

**Added 2026-08-14, fifth pass.** Triggered by the Karen drop failing a *third* time —
this round the clip **invented terrain that was not in the plate**, dropping the phone
onto rocks under the railing where the plate had open water. Reported symptom: *"it not
paying enough attention to the reference image."*

That reading is right, and the research says the fix is not a stronger instruction.

### The knob does not exist — adherence is bought four other ways

**No strength, weight, denoise or influence parameter is exposed anywhere** on the
reference path — not in Google's API schema `[vendor]`, and not in the hosted
schemas, which list only `prompt`, `image_urls`, `aspect_ratio` and `duration`
`[runware]` (fal.ai's reference-to-video reference). Whatever the Flow UI shows you,
there is nothing behind it to turn up.

So adherence is entirely a function of four things you *do* control, in descending
order of how much they buy:

| Lever | What it does |
| --- | --- |
| 1. **Mode** | Frame = geometry is honoured. Ingredient = geometry is a suggestion. |
| 2. **Role declaration** | Naming what each image *is* changes how it is used. |
| 3. **What is in the image** | A reference carrying two roles at once gets read as one of them. |
| 4. **Text reinforcement** | Words are the only "strength" control there is. |

### 1. Mode — and Omni *does* have Frames now

> **The [input-mode matrix](#the-input-mode-matrix-and-a-conflict-worth-resolving)
> conflict is resolved, and the help page was the stale one.** Flow's changelog lists
> *"Frame to Video now available for Gemini Omni Flash"* (2026-06-04) and *"Omni
> Frames to Video"* (2026-06-10) `[vendor]`; the API documents a starting frame; and
> an independent review confirms starting-frame support while listing **last-frame
> control among the capabilities still "available soon"** `[community]`.
>
> **`[confirmed 2026-08-14]`** — we opened it, loaded a plate into it, and the plate's
> geometry came back intact. This is no longer a paper finding.

**Omni Flash: first frame yes, last frame not yet.** That changes our routing
materially — a shot whose *composition* must survive can go through **Omni's Frames
tab** and keep the native audio. Only a shot whose *end state* must be pinned still
has to go to Veo 3.1 Lite/Fast.

Google's own tips page draws the same line in its own words `[vendor]`:

| Feature | Google's description |
| --- | --- |
| **Frames to Video** | *"gives you precise control over your shot's composition"* |
| **Ingredients to Video** | *"use your pre-defined characters, objects and styles as a consistent reference"* |

**Read that as the routing rule.** Composition control is the Frames tab's stated
purpose and it is not the Ingredients tab's. If the answer to *"what must survive?"*
is a layout, a geometry or a camera position, no amount of prompt work makes
Ingredients do it.

### 2. Role declaration — say what the image *is*, at the top

The vendor's own worked Ingredients prompt opens by assigning every image a role
before it asks for anything `[vendor]`:

> *"**Using the provided images for the detective, the woman, and the office
> setting**, create a medium shot of the detective behind his desk…"*

Note *"the office setting"* — a **location** is a documented ingredient role, alongside
character, object and style `[vendor]`. The practitioner restatement is a template:

> `[Subject] stands in [scene], rendered entirely in [style]` `[community]`

And the rule under it: *"Do not just upload the ingredient and expect Flow to use it
automatically. Your text prompt must reference it… The explicit reference produces
dramatically more consistent results."* `[community]`

- **Order is a signal.** *"Pass reference images in the order you reference them in the
  prompt. The model uses position as a signal."* `[runware]`
- **`<IMAGE_REF_N>` is now double-sourced.** Google's API reference and fal.ai's hosted
  schema both document inline, zero-indexed role binding in the prompt text
  (`<IMAGE_REF_0>`) `[vendor]` `[runware]`. Still `[untested]` in Flow's prompt box —
  but two independent surfaces documenting the same syntax makes it worth the one
  cheap test.

**"Use the supplied image as the visual reference for the whole shot and hold its
staging"** — our round-4 phrasing — never says what the image *is*. It asks for
obedience without assigning a role, which is the one thing the documented shape
always does first.

### 3. ⚠️ A location reference must not contain subjects

The sharpest finding of this pass, and the likeliest single cause of the rocks:

> *"When you add ingredients to your prompt, provide subject or product references on
> a plain or segmented background. **Make sure location and style references don't
> contain extra subjects**, unless that is your creative intent."* `[community]`

A plate that is *both* the location and the two characters is a reference carrying two
roles at once. The model resolves the ambiguity by picking one — and the documented
strength of the reference path is **subject** carry-over, not environment carry-over
(Veo's API types a reference as `asset` or `style`, and the asset case is documented
as *"up to three images of a single person, character, or product"* `[vendor]`). So it
keeps the people, treats the rest as loose atmosphere, and re-stages the ground.

**The counter is to split the roles across slots:** a clean location plate with **no
people in it** as the scene ingredient, and the cast Characters as the subject
bindings. This is also why clean-background character references — the register that
looked like a divergence — are *correct* for this path.

Corollaries worth keeping:

- **Consistent look across ingredients helps the blend**, and a busy background on a
  subject reference confuses the read `[community]`.
- **Text and image must not contradict.** *"Your text prompt should complement, not
  contradict, your visual inputs."* `[community]` A prompt describing something the
  reference does not show is an instruction to re-stage.

### 4. Text reinforcement is the substitute for a knob

With no strength parameter, words carry the load:

- **Re-describe the thing you want preserved**, in the prompt, in addition to supplying
  it — *"…the woman with long brown hair and a blue jacket…"* `[community]`. Already
  recorded for wardrobe; it applies equally to a location.
- **Keep ~80% of the descriptive keywords identical** between shots that share a
  setting — lighting, lens, style — and change only the action. *"This prevents the
  character's face or the environment from drifting."* `[community]`
- **Build a reference pack, not one casual image** — several approved angles of the
  same subject or location `[community]`.

### The unrendered-region rule — why it invented a shore

Underneath the mode question sits a plainer mechanism, and it generalises past this shot.

**Any region the plate does not show is a region the model will invent**, and it
invents by likelihood, not by imagination: asked what is below a waterfront railing at
night, the statistically ordinary answer is a rocky shore. That is the same root as
the [no-world-model failures](#spatial-geometry-models-have-no-world-model) above —
*"vague or contradictory instructions force the model to interpret… it fills in details
based on probability rather than intent"* `[community]`.

Three counters, in order of strength:

1. **Show it in the plate.** Geometry that is visible cannot be guessed at.
2. **Name it positively in the prompt.** Not *"no rocks"* — that is the
   [negation backfire](#-negatives-do-not-work-and-they-actively-backfire), and it puts
   the word *rocks* into a model that cannot subtract it. Write what is there:
   *"deep open water runs right up to the wall below the railing."*
3. **Frame it out.** A region outside the frame for the whole clip is a region that
   never has to be resolved.

**And the diagnostic that follows from it:** before firing, look at the plate and ask
*"what does this image fail to answer?"* Whatever that is, the model will answer it,
and you will not like the answer.

### Sources for this section (2026-08-14)

- [5 tips for using Flow — blog.google](https://blog.google/innovation-and-ai/products/flow-video-tips/) `[vendor]` — Frames to Video *"gives you precise control over your shot's composition"*; Ingredients as *"a consistent reference"*.
- [Ultimate prompting guide for Veo 3.1 — Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) `[vendor]` — the *"Using the provided images for the detective, the woman, and the office setting…"* prompt shape; location as a first-class ingredient role.
- [Guide video generation using asset and style images — Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/use-reference-images-to-guide-video-generation) `[vendor]` — `referenceType: asset | style`; asset documented as up to three images of *a single person, character, or product*; one style image.
- [Google Flow changelog](https://labs.google/fx/tools/flow/changelogs) `[vendor]` — Omni Frames to Video, 2026-06-04 and 2026-06-10.
- [Create videos in Google Flow](https://support.google.com/flow/answer/16353334) `[vendor]` — the *"+ Add start frame"* / *"+ Add end frame"* slots and `@` asset referencing in the prompt box.
- [Reference-driven video with Gemini Omni Flash — Runware](https://runware.ai/docs/models/google-gemini-omni-flash/guides/reference-driven-video) `[runware]` — order as a positional signal; combined frame-anchor + references mode; 7 references / 1 frame anchor.
- [Gemini Omni Flash reference-to-video API — fal.ai](https://fal.ai/models/google/gemini-omni-flash/reference-to-video/api) `[runware]` — the full input schema, confirming **no strength/weight/adherence parameter**, and `<IMAGE_REF_0>` inline binding.
- [Google Flow AI prompts 2026 — Whiskai Labs](https://whiskailabs.net/google-flow-ai-prompts-2026-best-prompts-guide/) `[community]` — *"make sure location and style references don't contain extra subjects"*; the `[Subject] stands in [scene]` template; text must not contradict the visual inputs.
- [Fixing Google Flow: Ingredients to Video troubleshooting — Arsturn](https://www.arsturn.com/blog/fixing-google-flow-common-issues-with-ingredients-to-video) `[community]` — reuse the identical ingredient image; reinforce appearance in text; plain or segmented backgrounds.
- [Gemini Omni Flash review — BuildFastWithAI](https://www.buildfastwithai.com/blogs/gemini-omni-flash-review-google-ai-video-model-2026) `[community]` — starting frame supported; **last-frame control listed as still "available soon"**.
- [How Veo 3.1 maintains character & scene consistency — Sider](https://sider.ai/blog/ai-tools/how-veo-3_1-maintains-character-scene-consistency-in-ai-video) · [Veo 3 image-reference workflow — veo3ai](https://www.veo3ai.io/blog/veo-3-image-reference-workflow-2026) `[community]` — location profiles, reference packs, and the keep-80%-of-the-keywords rule.
- [AI video hallucinations — Hailuo](https://hailuoai.video/pages/blog/ai-hallucinations-video-generation-guide) `[community]` — underspecified regions get filled by probability rather than intent.

**Still `[untested]` against our own Flow session** — but two items here are answerable
in seconds and settle open questions for the whole repo: **does the Frames tab appear
with Omni selected**, and **does `<IMAGE_REF_0>` do anything in Flow's prompt box**.

## Making motion read as real

**Added 2026-08-14, sixth pass.** Triggered by the Karen drop failing a *fourth* time.
This round the geometry held and the terrain was right — and **the phone bounced off
the ground before going into the water**, and the whole clip *"looked very AI."* Two
separate problems, and the first one has a permanent answer.

### The shutter is the tell nobody prompts for

A real camera at 24fps with a 180° shutter exposes each frame for 1/48 of a second, so
**anything moving fast smears**. Video models default to rendering every frame sharp,
which is why fast motion reads as *"mathematically smooth rather than physically
real"* — the phrase already in this file from the slop research.

- *"Realistic AI video almost always conforms to cinema convention — 24 frames per
  second with a 180-degree shutter and natural motion blur, because that cadence is
  what audiences subconsciously equate with professional footage."* `[community]`
- *"Prompting 'high shutter speed, filmic tone with subtle motion blur' creates an
  immediate expectation for how motion should be rendered."* `[community]`
- The motion blur has to **match the motion** — a fast move rendered sharp, or a slow
  one smeared, both read as wrong `[community]`.

**Practical token, and it is cheap:** `shot at 24fps with a 180-degree shutter, so
anything moving fast smears with natural motion blur.` Our clip prompts have carried
`natural motion blur` as one item in a grain list; naming the *cadence* is stronger,
because it tells the model which frames to blur rather than asking for blur in general.

> **`[confirmed 2026-08-14]`.** Asked for it on the Karen drop; the falling phone came
> back as a streak rather than a sharp object, and **no post pass was needed** for the
> clip to read as captured. Use this clause on any shot with fast motion in it.

**Corollary for falling objects specifically.** A dropped object crossing frame in a
few frames should be a **streak**, not a crisp phone in four positions. If it is sharp,
it will read as pasted-on no matter how correct the trajectory is.

### The rule that outranks all of it: a real camera never catches the whole fall

Four rounds of evidence, and it lines up exactly with what the physics research
predicted:

> **Every frame the object is airborne on screen is a frame the model can get wrong,
> and it will use them all.** Occlusion is not a compromise — it is what real footage
> of an accident looks like.

**`[confirmed 2026-08-14]`.** Four clips that kept the falling phone in frame failed
four different ways. The fifth framed it so the phone exits within a few frames, and it
was accepted first time. This is the strongest rule in this file and the only one that
has survived contact five times.

Real handheld footage of someone dropping something catches the release and then loses
the object immediately: it exits the frame, or the operator doesn't follow it. The
audience fills in the rest and never questions it. **A shot that keeps a falling object
in frame from hand to landing is already a stylised shot**, which means we were asking
the model for the hardest possible version of the motion *and* a version that would
have read as staged even if it rendered perfectly.

The design rule that follows, and it is now a house rule rather than a per-shot fix:

| Instead of | Do |
| --- | --- |
| render the fall | render the **release**, and let the object leave frame within a few frames |
| render the landing | let it be a **sound**, delayed by the right beat |
| one continuous shot covering the event | **cut**: a wide that stages it, an insert that loses it, and the aftermath |

**Cutting is free and generating is not.** The three-shot version costs the same
credits as one failed ten-second attempt, and every shot in it is inside the model's
competence.

### The rest of the "looks AI" complaint

Independent of the physics, and consistent across every source `[community]`:

- **Perfection is the tell.** *"AI video defaults to an impossibly clean look because
  models were trained to produce 'high quality' output — but perfection is what makes
  it look fake."* Grain, slight overexposure, handheld wobble, imperfect focus.
- **Describe how a real operator would have shot it**, not how the scene looks —
  *"handheld camera with subtle movement, shot on 16mm, slightly warm colour cast"*
  beats *"smooth steady shot"* on realism every time.
- **Post does the last 10% — but it is a rescue, not a requirement.** A subtle grain
  layer *"instantly makes output feel captured rather than generated"*, and a 10–15%
  speed adjustment breaks the synthetic cadence. **On our one confirmed run neither was
  needed** `[confirmed 2026-08-14]`: a correctly framed shot with the shutter clause in
  the prompt read as real straight out of Flow. Reach for post when a clip is close,
  not as a standing step.

### Sources for this section (2026-08-14)

- [Why AI videos look fake (and how physics can fix it) — Medium](https://medium.com/@nandinilreddy/why-ai-videos-look-fake-and-how-physics-can-fix-it-bb84149831d8) `[community]` — models mimic the appearance of motion without mass, gravity or momentum.
- [The A to Z guide to Seedance 2.0 prompts](https://ethicalfounder.com/guide-to-seedance-2-0-prompts-claude-ai-video-prompt-generation/) `[community]` — 24fps / 180° shutter as the realism convention; motion blur must match the simulated shutter; describes another model, so treat the mechanism as directional and the token as cheap to try.
- [How to add realistic motion blur and depth of field to AI video — Higgsfield](https://geo.higgsfield.ai/task/blog/how-to-add-motion-blur-depth-of-field-ai-video) `[community]` — shutter-speed prompting sets the expectation for how motion renders.
- [5 ways to make AI video look less AI — Sunra](https://sunra.ai/blog/make-ai-video-look-less-ai) · [Why your AI videos look fake — Nemo](https://www.nemovideo.com/blog/why-ai-videos-look-fake-how-to-fix) · [Why AI video motion looks unnatural — AIVid](https://aivid.video/blog/why-ai-video-motion-looks-unnatural-and-how-to-fix-it) `[community]` — perfection as the tell; grain, wobble and imperfect focus; describe the operator, not the scene; grain and speed adjustment in post.

## Notes for BadCode `[untested]`

1. **10s per generation fits `music-video-short`'s 10–20s target as 2+ clips** — consistent with
   how that skill already works. No structural change needed.
2. **The credit burn on blocked generations raises the stakes on writing to pass first time.**
   The doctrine in `badcode-art-direction` ("two failures with no candidates = policy block;
   rewrite, don't retry") gets *more* important here, not less, because the failed attempts now
   cost money as well as minutes.
3. **No negative prompts** means the house style's "no lens flares" cannot be expressed as a
   negative on this engine at all. It needs a positive restatement or it does nothing.
4. **1080p ceiling vs Veo's 4K** matters for anything destined for the comic viewer at full width.
5. **16:9 / 9:16 only.** Fine for shorts, and fine for our landscape panels, but there is no
   21:9 escape hatch here the way there is on the image side.
6. **Multi-turn editing is the genuinely new thing** and has no analogue in our current pipeline.
   `previous_interaction_id` threading is closer to how `flow_refine` works for stills than to how
   we currently do video — a "refine the clip" loop is newly plausible, if consistency holds.
7. **We have no BadCode motion identity written down anywhere.** `badcode-art-direction` ends with
   "Stills only. Motion/Veo direction is future work." Whatever engine wins, that gap is real:
   camera grammar, what moves and what holds still, how long a beat sits. Worth writing regardless
   of the Omni Flash question, and it would belong in a skill rather than in this folder.

## Open questions

- **First-frame *fidelity*.** Narrowed twice and still open, and it blocks
  `animate-slide`. Omni has a Frames mode and it **honours a plate's geometry**
  `[confirmed 2026-08-14]` — but nobody has checked whether frame one is a **pixel
  match**. That is the remaining question, and it is the whole one.
- **Does Omni's Frames tab expose an end-frame slot?** The confirmed run left it empty.
  Vendor sources say no and call it "available soon"; one look answers it.
- **Does `<IMAGE_REF_0>` / `<FIRST_FRAME>` do anything in Flow's prompt box?** Two
  independent surfaces document the syntax `[vendor]` `[runware]`; nobody has typed it
  into Flow. One cheap test.
- Does the UK/EEA restriction on editing uploaded video apply to us in Flow, or only via API?
- Does Flow's UI surface `previous_interaction_id`-style threading, or is that API-only?
- Does the `flow` MCP server reach Omni Flash at all, or only the Veo path?
- ~~Do Flow Characters cast into video generations?~~ **Yes** — and they now carry a voice that
  stays consistent across generations `[yt]`. Open part: whether the MCP `character` parameter
  reaches the video path, or whether casting for video is browser-only.
- Does the harsher filtering on *uploaded* video also apply to stills we upload as references?

## Sources for the `[yt]` claims

Harvested 2026-08-12 via `scripts/fetch-youtube-transcripts.sh`'s method (yt-dlp auto-captions),
ranked by view count. Raw transcripts are research input and were left in scratch, not committed.

| Channel | Video | Views |
| --- | --- | --- |
| Paul J Lipsky | How To Use Gemini Omni (Google's Wild Video Model) | 230k |
| Kevin Stratvert | How to Use Gemini Omni (Step-by-Step Tutorial) | 113k |
| Jack Vs. AI | Google Just UNLOCKED the Nano Banana of AI Video (Gemini Omni Deep Dive) | 99k |
| Kevin Stratvert | Google Flow Tips & Tricks (9 Features You Need to Know) | 56k |
| TheAIGRID | How To Use Google Omni — Google Omni Tutorial | 30k |
| Yaroflasher | GEMINI OMNI NEW AI VIDEO MODEL | 27k |
| Jerrod Lew | Google Omni Flash Is Amazing — Full Tutorial! | 26k |
| King Charles Tv | How to Use Gemini Omni in Google Flow (How to Lock Characters) | 26k |
| Google | How to use Tools in Google Flow | 59k |

## Prompt-guide sources (2026-08-12)

- **[How to create effective prompts with Gemini Omni](https://deepmind.google/models/gemini-omni/prompt-guide/) — Google DeepMind's official prompt guide. `[vendor]`** Confirms the five core elements (shot framing & motion · style · lighting · location · action), the camera vocabulary ("oner", "static", "locked off", "push in", "punch in", "dolly zoom", plus camera *types* like "natural smartphone zoom" / "film camera"), and that the model **does not want overly prescriptive instructions** — describe intent and let its world knowledge fill in. This is the source the practitioner guides are restating; prefer it.
- [Gemini Omni Prompt Guide — Formula, Camera Vocab, Failure Modes](https://geminiomniprompts.org/guide/) — the most substantive of the practitioner guides; source of the word-limit, camera-verb list and motion difficulty ranking.
- [Gemini Omni Flash Prompt Guide – Tips & Examples](https://openart.ai/blog/gemini-omni-flash-prompt-guide/) — image-to-video reference handling, audio prompting, the default-to-cutting failure mode.
- [Generate and edit videos with Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni) — Google's API reference (parameters, not prose craft).

Google published an official five-tip prompting guide alongside the May 2026 launch; the tips above
are the version of it that survives independent restatement across several guides. The primary page
did not respond when fetched — **worth re-fetching and diffing against this section.**

**Bias warning:** most of these channels sell a course, a community, or a competing platform, and
several ran their tests on third-party wrappers (Higgsfield, OpenArt, Cue AI) rather than in Flow —
where limits, watermarks and filtering all differ. Where a claim above is Flow-specific it came from
someone demonstrably inside Flow; treat the rest as directional.
