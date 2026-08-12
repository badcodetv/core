# Gemini Omni Flash — video engine reference

**Model:** Gemini Omni Flash (`gemini-omni-flash-preview`). Announced at I/O 19 May 2026; developer
API access 30 Jun 2026. **Still public preview.**
**Researched:** 2026-08-12 · **Confirmed against our Flow session:** never.

> **Read the verdict first.** On current evidence Omni Flash is *not* a drop-in replacement for the
> Veo-based recipe in `docs/superpowers/flow-video.md`, and there is a specific reason why — see
> [The animate-slide problem](#the-animate-slide-problem). Nothing should be rewired until that
> question is settled by a test.

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

Combined with the `[community]` report of no true first-frame-to-video, the working conclusion is:

> **`animate-slide` stays on Veo 3.1.** The skill's contract — an approved panel is frame one —
> is a frame-anchoring problem, and in Flow that is Veo's job, not Omni's.

Still worth running the confirming test before treating this as closed, since it is one UI change
away from flipping:

> Take one accepted panel with a cast Flow Character. Generate with `task: image_to_video`. Does
> frame 1 match the panel pixel-for-pixel, or has the character been redesigned?

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

- **First-frame fidelity** (above). Blocks everything else.
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
