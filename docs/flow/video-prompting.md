# Video prompting — Veo 3 / 3.1

Text→video, image→video, frames, audio and dialogue. Motion craft for
`animate-slide` and `music-video-short`.

## 0. 🔴 The order of operations — settle the look on a STILL first

**Ruling 2026-08-21 (Kai). This is the default method for every shot in a film, not an option.**
It was already what we did on both built GPOM scenes; it was never written down as the method,
which meant it read as a habit rather than a rule. It is a rule.

| Step | Do | Why here |
| --- | --- | --- |
| 1 | **Generate stills until the LOOK is right.** Iterate freely — palette, lens, scale, light, framing, what is and is not in shot | Stills are the cheap, fast, high-control surface. Nano Banana Pro takes correction well and a reroll costs seconds |
| 2 | **Accept exactly one.** That is the plate | The decision is made in the still, in daylight, before any motion is on the table |
| 3 | **Feed the plate in as `startImage`** and prompt **the motion only** | The plate is now the first frame of the clip, so the look is already locked into the output and cannot drift |
| 4 | **Judge the clip on movement alone** — did the right thing move, at the right weight? | The look is not up for re-litigation at this stage. If it is, step 2 was wrong |

**Three reasons this is not merely convenient:**

1. **Text→video re-decides the look on every roll.** Every reroll is a fresh interpretation of
   the whole frame, so you cannot converge — you are iterating on a target that moves. Fix the
   frame and the only remaining variable is the motion.
2. **The plate decides whether the move is possible at all.** Veo animates what the plate gives it
   something to animate — five takes across three dark, dense alley plates produced no rain, while
   one modern harbour plate moved immediately ([`physics-and-motion.md`](./physics-and-motion.md)
   §6b). That is a judgement you can make **by looking at a still**, before spending a video credit.
3. **A plate is worth keeping even if the clip never works.** If Veo will not move it, the shot
   becomes a locked plate with an eased move added in post — a first choice, not a defeat
   ([`post-production.md`](./post-production.md) §1). Either way the still was the right first buy.

**The corollary that costs money if ignored: never iterate on the look inside video.** A wrong
palette or a wrong lens is a still problem. Fixing it by rerolling 8-second clips is the single
most expensive mistake available in Flow, and it is slower as well as dearer.

### When to break it

- **The shot has no stable first frame** — a whip pan, a shot that starts on black, a pure
  interpolation between two pictures. Frames mode owns those (§4).
- **You want a move Veo will only produce unprompted**, and you intend to reverse or retime it.
  The GPOM descent was Veo's crane-up run backwards.
- **A quick text→video probe to find out whether a kind of motion exists at all.** Legitimate,
  but it is reconnaissance — throw the result away and come back through the plate.

---

## 1. The formula

`[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`

**The formula is Google's** — re-corrected 2026-08-20, and the 2026-08-18 correction that
claimed otherwise was itself wrong. Google's Cloud Blog publishes this exact five-part sequence
under the heading *"A formula for effective prompts"*: *"A structured prompt yields consistent,
high-quality results. Consider this five-part formula for optimal control."* Read at source
2026-08-20. (official, blog tier —
[cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

Two caveats survive the re-correction:

- It is a **checklist, not a mandated string order.** Google's own worked example on that page
  reads *"Medium shot, a tired corporate worker, rubbing his temples in exhaustion, in front of
  a bulky 1980s computer in a cluttered office late at night…"* — the formula's order, but
  presented as a way to think, not a syntax.
- **What stays ours and measured is that earlier clauses win when instructions compete.** Google
  never says that.

⚠️ **Camera-first is not a cross-platform norm.** OpenAI's Sora cookbook sequences Scene
Description *before* Cinematography, and a Kling guide gives Subject + Primary Action +
Environmental Motion + Camera Motion. Do not carry this ordering to another model as craft.

**The official component list** — the video-generation prompt guide's "Anatomy of a prompt",
in its own order:

| # | Component | Google's gloss |
| --- | --- | --- |
| 1 | **Subject** | the "who" or "what" the action revolves around — "specificity helps avoid generic outputs" |
| 2 | **Action** | the verb: movements, interactions, subtle expressions, transformations |
| 3 | **Scene or context** | the where and when — location, time of day, weather, period, atmospheric detail |
| 4 | **Camera angles** | viewpoint (see [`camera-vocabulary.md`](./camera-vocabulary.md)) |
| 5 | **Camera movements** | the move, listed separately from the angle |
| 6 | **Lens and optical effects** | focal length, depth of field, flare, rack focus |
| 7 | **Visual style & aesthetics** | four sub-parts: lighting · tone/mood · artistic style · ambiance |
| 8 | **Temporal elements** | pacing, evolution within the clip, rhythm |
| 9 | **Audio** | "we recommend that you use separate sentences to describe the audio" |
| 10 | **Cinematic terms** | editing-grammar words: match cut, jump cut, montage, split diopter |

"You don't need to use all elements in every prompt" — the list is a palette, not a checklist.
Note that **camera angle and camera movement are two separate components**: Google splits them,
and so should the prompt (§11.3).

Not every element every time — know them so you can add them deliberately. The formula
**constrains the model's improvisation**; it is not a requirement. A one-line prompt is
a legitimate opening move precisely because it shows you what Veo invents by default,
which you then override one clause at a time.

> **Official (all five parts):** "Medium shot, a tired corporate worker, rubbing his
> temples in exhaustion, in front of a bulky 1980s computer in a cluttered office late at
> night. The scene is lit by the harsh fluorescent overhead lights and the green glow of
> the monochrome monitor. Retro aesthetic, shot as if on 1980s color film, slightly
> grainy."

> **Official (camera-led):** "Crane shot starting low on a lone hiker and ascending high
> above, revealing they are standing on the edge of a colossal, mist-filled canyon at
> sunrise, epic fantasy style, awe-inspiring, soft morning light."

> **Official (mood-led):** "Close-up with very shallow depth of field, a young woman's
> face, looking out a bus window at the passing city lights with her reflection faintly
> visible on the glass, inside a bus at night during a rainstorm, melancholic mood with
> cool blue tones, moody, cinematic."

> **Official (pure world-building — no camera, no character direction, still a model
> example):** "A snow-covered plain of iridescent moon-dust under twilight skies.
> Thirty-foot crystalline flowers bloom, refracting light into slow-moving rainbows. A
> fur-cloaked figure walks between these colossal blossoms, leaving the only footprints
> in untouched dust."

## 2. Length — the resolved rule

Sources contradict each other: community guides say 3–6 sentences and that overlong
prompts get partly ignored; DeepMind's own guide showcases a very long prompt as a
technique for maximum control, and frames the choice as stylistic rather than as a
performance ladder — *"You can use different sorts of prompts – long and short – to create
worlds"* / *"The more detail you add, the more control you'll have over the final output."*

⚠️ **The "~1,100-word" figure this file used to quote is withdrawn.** A recount on 2026-08-20
measured that page's longest example (the off-road rally shot) at roughly 650–700 words. Cite
the page's own framing, not a word count.

**Ruling:** *dense and long* is different from *padded and long*. Length costs nothing
when every clause describes one coherent action in a single scene. What gets dropped is
repetition and **competing actions**. Default to 3–6 sentences and one atomic action per
clip; go long only when a single complex action genuinely needs that many distinct facts.

**The real ceiling is 1,024 tokens.** The Veo API's `prompt` is a single plain-text string —
*"prompt: The text description for the video. Supports audio cues."* — with a documented
*"Text input: 1,024 tokens"* limit. At typical English tokenisation that is roughly 700–800
words. **Nothing in Flow shows you the count**, so a genuinely enormous prompt can be silently
truncated and you will never be told. (official,
[ai.google.dev](https://ai.google.dev/gemini-api/docs/veo))

## 3. Image-to-video — the `animate-slide` case

**The rule that matters most: the source image already supplies subject, scene and
style, so describe only the motion.** Do not re-describe the character, the background
or the lighting. Redundant description gives the model competing signal about what the
frame should look like, and it drifts toward regenerating rather than animating.

- **Refer to the subject generically** — "the subject", "the woman", "he".
- **Source-image quality gates everything downstream.** Sharp, one clear subject,
  readable detail, enough negative space for the camera to move into.
- **An unspecified camera is NOT a still camera — corrected 2026-08-18.** This file used to
  say "Veo's default is near-static". That is wrong and it cost us real time. Leave the camera
  unstated and Veo *invents* behaviour — generic framing, a slow drift, a sway, an unrequested
  push-in. **Name the move every time.** When you want no move at all, say so explicitly:
  `static`, `locked-off`, `no camera movement`. Silence is not a request for stillness.
  ⚠️ **Bounded 2026-08-21: saying it does not make it so.** An explicit static instruction is
  still the right thing to write — it demonstrably reduces the drift — but it does **not**
  produce a locked frame on any model we have. See *"Static" is not a lever* below.
- **Name the subject motion too.** Separately from the camera: an unstated subject can come
  back near-frozen even while the camera is busy.
- **1–2 motion types maximum.** "Slow dolly in, leaves rustling, clouds moving, water
  rippling, light shifting" is five competing instructions.
- Get one axis working (camera *or* subject) before adding the other.
- **Partial animation:** name the moving element and the pinned one in the same
  sentence — "Rotate the shoe, keep everything else still." / "Animate only trees and
  sky; keep buildings static." / "background stays still and in focus".
- **Style lock is the one permitted exception to "don't re-describe":** a short clause
  like "Maintain the style of the image" or "Maintain the old indie film or VHS tape
  aesthetic" anchors treatment without giving the model content to regenerate.
- **Motion intensity is a three-tier vocabulary:** "Very subtle movement, minimal motion,
  nearly still" / leave unspecified / "Energetic movement, dynamic motion throughout".
  If it returns too subtle, add "Visible movement throughout."
- Ambient motion that reads cinematic without moving the subject: "subtle morning mist,
  light rays, otherwise still".
- **Debugging a bad animate: reduce scope.** Lock the subject, cut to one animated
  region, try a different aspect ratio. Adding corrective description makes drift worse.
- **The source image is literally frame 1, so anything in it that must persist needs its own
  instruction** — *"Maintain the text 'replicate' on the screen for the first few seconds."*
  *"The input image will always be the starting frame of your video."* (practitioner,
  [replicate.com](https://replicate.com/blog/using-and-prompting-veo-3))
- **Style lock, two more attested phrasings:** *"Maintain the animation style of the original
  image"* / *"Maintain the vintage feel of the image"*. Replicate also reports Veo carries the
  input's grade by default — *"Veo 3 goes beyond animation — it retains the filtering and color
  grading of the input image"* — so explicit style-lock language is mainly needed on complex
  scenes. (practitioner, [replicate.com](https://replicate.com/blog/veo-3-image))

> **Minimal and valid:** "Make him run!"

### 🔴 "Static" is not a lever — every clip drifts (measured 2026-08-21)

**We asked for a locked-off camera in the plainest words available and got a moving one, on
both models, in every take.** This is the single most useful thing to know before planning a
shot that depends on the frame holding still: you cannot get one out of the prompt.

**The test.** Plate `docs/stories/magic-money-tree/storyboard/img/p01.jpg` (Dawn at the
bedside — two faces, joined hands, dim ward, fine grain). One prompt, sent identically to two
models at 8s / 16:9:

> Static locked-off camera, no camera movement. The nurse blinks and breathes slowly, her
> thumb stroking the back of the patient's hand once. Everything else in the ward stays still.
> Very subtle movement, minimal motion. Maintain the style, grain and lighting of the image.

**The measurement.** Drift is measured on a **subject-free crop** — the left third of frame
(wall, fluorescent tube, equipment), which is static in the fiction — phase-correlated against
frame 0, sampled every 6th frame. That isolates camera movement from the nurse's own motion;
a whole-frame diff would conflate the two and tell you nothing.

| Clip | Net drift at 8s | Peak vertical | Frames off-lock |
| --- | --- | --- | --- |
| Veo 3.1 Fast, take a | **+66 px** (5.2% of frame width) | 5 px | 31/32 |
| Veo 3.1 Fast, take b | +42 px | 6 px | 30/32 |
| Gemini Omni Flash | +34 px | 12 px | 30/32 |

**Every take drifted, and all of it was horizontal creep in the same direction** — a slow
unrequested push/pan, not a shake. Omni Flash drifted least laterally and most vertically;
the spread between the two Veo takes (66 px vs 42 px) is as large as the spread between the
models, so **treat drift as a per-take lottery, not a model property.**

**What this changes:**

- **Do not design a beat that depends on a locked frame.** If the shot only works held
  perfectly still, it is not a Flow shot — it is a locked plate with the move added in post
  ([`post-production.md`](./post-production.md) §1).
- **Budget ~2–5% of frame width of unplanned travel per 8s clip.** Frame with that headroom:
  anything critical parked hard against an edge can walk out of shot by the last second.
- **Cuts between two clips will not match.** Each take has drifted a different distance by its
  last frame, so a join between two "static" clips carries a visible framing bump. Either
  stabilise both before the cut, or cut on motion so the bump reads as intent.
- **Keep writing the static instruction anyway.** It is not useless — silence produces worse,
  and the rule above still stands. It sets an upper bound on the drift; it does not remove it.

### ⚠️ Leaderboard rank does not transfer to our register (2026-08-21)

The same A/B was run to answer a second question: Gemini Omni Flash sits ~280 Elo above
Veo 3.1 on the Artificial Analysis **image-to-video (no audio)** board (1366 vs 1084, Aug 2026).
Is our `Veo 3.1 Fast` default leaving quality on the table?

**On this plate: no.** Detail retention against the plate was a tie — 92–97% of the plate's
high-frequency energy across all three clips, whole-frame, with no model preserving grain or
skin texture better than another. Character identity held on all three. Neither invented
dialogue (all clips −43 to −46 dB mean, room tone only).

**⚠️ Superseded 2026-08-25 — Jack rules Omni Flash, always.** Watching the actual output
across the camping shots, the call is that Omni Flash is clearly better on our footage.
**Generate all video on Omni Flash unless a shot needs one of the two things it cannot do:**
it **rejects a last frame**, so the first+last-frame interpolation lock is Veo-only; and on
2026-08-25 it lost both faces on Frames on a big expression arc where Veo held them
([the tab-rule bound](../google-flow/omni-flash.md)). Raise those at the time; do not switch
silently. The ruling below stands only as the record of what the A/B measured.

**Ruling (superseded): keep `"Veo 3.1 Fast"` as the `flow_generate_video` default.** The arena is won on
bright, busy, generic prompts; our register is dark, single-source-lit and identity-critical,
and the ranking did not survive the move. ⚠️ **Bounds:** n=3 clips, one plate, one near-static
prompt. This rules out a *large* Omni Flash advantage here. It does not rule out a small one,
or one on a motion-heavy or brighter shot — re-test before trusting it beyond this case.

⚠️ **Omni Flash ignored `count`** — a `count: 2` call returned one clip with `partial: true`,
so the run is 2 Veo samples against 1 Omni sample. Known `flow-mcp` gap; don't plan a
multi-candidate round on Omni Flash until it is fixed.

### The first frame decides whether the move is possible

Added 2026-08-20. Composition of the *still* constrains the motion prompt, and none of this
is recoverable later.

- **Frame for the move you are going to ask for.** *"If a subject's head is touching the top of
  the frame in the source image, the AI has no pixels to work with if the requested motion is a
  slight upward tilt or a camera crane movement."* For a push-in, *"frame slightly wider than
  your final shot"*.
- **Give the frame layers.** *"clear foreground, midground, and background layers. This gives
  the motion model a clear hierarchy for parallax effects."*
- **Reframe the still, never the finished clip.** *"Reframe the still image first, then animate.
  You get much better results because the i2v model works with the full intended composition."*
  Cropping the video afterwards throws away pixels Veo never had.
- **Generate a still that implies what happens next.** Mid-gesture, cloth already displaced,
  subject off-centre — *"Imply motion, don't freeze it. Generate frames that suggest what
  happens next."* A static symmetric moment gives the motion model nothing to continue.

*(single-source, [nerdbot.com](https://nerdbot.com/2026/04/27/rethinking-first-frame-quality-through-nano-banana/)
and [film.fun](https://www.film.fun/articles/nano-banana-2-prompting-guide-frame-composition-and-reframing-for-ai-video))*

🔴 **This is a live hypothesis about our own worst failure.** Our parallax-hinging measurement
varied prompt wording across three prompts and two tiers, and never varied the source still's
depth-cue composition. If layering is the variable, a whole shot class comes back. Untested.

### Words are Flow's only motion lever

Runway's Motion Brush lets you *"paint the specific area and assign a direction vector and speed
to that region"*; Kling's *"'Static Brush' feature enables users to designate static areas by
brushing and fix pixels in the brushed areas, preventing camera movement."* **Flow's compose bar
has no equivalent.** Any cross-model "motion control" technique referencing brushes, masks or
numeric parameters is a UI feature, not craft, and does not transfer — our partial-animation
discipline has to carry the whole job in prose. (corroborated,
[kling.ai](https://kling.ai/quickstart/how-to-animate-image-parts))

## 4. First / last frame (Frames to Video)

Three separate prompts. Each **still** prompt is a complete, self-sufficient scene
description. The **Veo** prompt names only the camera move connecting them, plus any
dialogue spanning the transition.

> **Official (all three):**
> *Start frame:* "Medium shot of a female pop star singing passionately into a vintage
> microphone. She is on a dark stage, lit by a single, dramatic spotlight from the front.
> She has her eyes closed, capturing an emotional moment. Photorealistic, cinematic."
> *End frame:* "POV shot from behind the singer on stage, looking out at a large,
> cheering crowd. The stage lights are bright, creating lens flare. You can see the back
> of the singer's head and shoulders in the foreground. The audience is a sea of lights
> and silhouettes. Energetic atmosphere."
> *Veo prompt:* "The camera performs a smooth 180-degree arc shot, starting with the
> front-facing view of the singer and circling around her to seamlessly end on the POV
> shot from behind her on stage."

**BadCode application: this is the panel-to-panel technique.** Art-direct page N and
page N+1 as clean stills, feed both into Frames mode, and let the video prompt carry
purely the connective camera language. Cheaper and far more controllable than asking
one generation to invent the journey.

**Motion-only is Google's own instruction for Frames specifically**, not an inference from
single-image animate — *"In your text prompt, describe the action or transition that should
happen between the frames."* And the spend rule: *"Do not use the prompt to repeat everything
already visible in both images. Spend most of the prompt on what the images cannot show:
movement, timing, camera path, material behavior, atmosphere, and sound."* The full shape is
**subject continuity + physical action + camera path + environmental change + timing + ending
instruction + audio + exclusions**. (official,
[support.google.com](https://support.google.com/labs/answer/16353334?hl=en); the formula
single-source, [flowveo3.com](https://flowveo3.com/posts/veo-3-1-first-last-frame-guide))

### 🔴 Frames to Video INTERPOLATES between two pictures — it does not move a camera

**Measured 2026-08-20, GPOM scene 0 v2, and it is the most important thing we know about Frames
mode.** Kai's diagnosis, confirmed in one generation.

**Symptom.** On a pull-back generated with a pinned start *and* end frame, the subject is never
truly rigid. Whole components stop being invented once the prompt is right, but **panel joins,
seams and small structures still visibly deform and slide** throughout the move. No amount of
rigidity prose fixed it: *"every panel and surface stays rigid, flat, level and sealed"*, *"the
hull is one solid piece and holds its exact shape"*, *"nothing tilts, pivots, folds or rotates"*
all helped with other faults and none stopped the creep.

**Cause — and Google says so in its own parameter reference.** Confirmed 2026-08-21 by a targeted
research sweep. The `lastFrame` doc string reads: *"The final image for an **interpolation** video
to transition. Must be used in combination with the `image` parameter."* DeepMind markets it the
same way — *"Create smooth, artful, and epic **transitions between images** provided for the first
and last frame."* **Google never claimed this moves a camera.** It is a morph tool, and Google's
own tutorial builds the pair as two fully independent image-generation calls (*"Step 2: Create the
ending frame: Generate a second, complementary image… such as a different POV angle"*), with
lamb→tiger and room-remodel morphs as the flagship demos.

The two pinned frames are therefore **two separately generated images**, not one object
photographed at two distances. Veo is not travelling a camera through a scene — it is finding a
path from picture A to picture B, and **every inconsistency between them has to be animated away
somewhere**. That animation is the join creep. It is structural, so no wording removes it.

**Proof.** Identical start image, identical prompt shape, tier and duration. The only change was
dropping `endImage`:

| Run | End frame | Rigidity |
| --- | --- | --- |
| `reveal-f3` | pinned | 🔴 joins slide and deform throughout |
| `reveal-noend-{a,b}` | **none** | ✅ **completely rigid.** Panel lines dead straight, rivet rows solid, the subject simply gets smaller |

**The rule: if the subject must stay rigid, do not pin an end frame.** Animate from the start
image alone, then **save the last frame and start the next clip from it**
(`flow_scene_save_frame position:"end"`). Chaining buys rigidity; pinning buys arrival.

**What you give up, and how to get it back.** With no end frame the destination is *invented* —
our two takes produced a flat plate and a riveted capsule, neither the satellite we had designed,
and both drifted from near-black to high-key silver. So the prompt has to carry the whole
destination in words, including the register, because no image is carrying it any more. Budget
takes: you are picking a destination, not specifying one.

**Why it breaks worst on a big scale change.** Google has never published Frames-to-Video's
internals, so this is mechanism-class analogy, not a claim about Veo: *Generative Inbetweening*
(ICLR 2025, UW + Google DeepMind + UC Berkeley, on Stable Video Diffusion) shows this class of
model runs **two separate diffusion trajectories** — forward from frame 1, backward from frame 2 —
and fuses them at every sampling step. It documents the failure at exactly our condition:
*"When the input pairs are captured at such distant intervals that they have sparse
correspondences… it becomes difficult to fuse the forward and backward motions. This situation,
where the overlapping areas are minimal, leads to artifacts in the intermediate frames."* A macro
circuit board and a wide satellite hull share almost no pixels. Related: *Geometry Forcing* finds
that *"video diffusion models trained solely on raw video data often fail to capture meaningful
geometric-aware structure"* — nothing makes Veo hold a subject rigid by default.

⚠️ **Nobody warns about this.** Google names the mechanism and never names the failure; no
practitioner source found in two sweeps mentions it either. If you are debugging deformation in
Frames mode, this file is the only place it is written down.

⚠️ **Matching seeds across the two stills will not save it.** Google: *"It doesn't guarantee
determinism, but slightly improves it"* — and seed is a Veo 3 parameter, not 3.1.

### 🔧 The fix that keeps both: shoot it backwards

**Rigidity comes from having no end frame; arrival comes from making the destination frame 1.**
You can have both by generating the move in reverse and flipping it in post:

1. Feed the **art-directed destination plate as the single start image** — no `endImage`.
2. Prompt the opposite move (a push-in where you want a pull-back), decelerating into the arrival.
3. `ffmpeg -i in.mp4 -vf reverse -an out.mp4`. Audio is stripped anyway, so reversing costs nothing.

Veo never has to invent the destination *and* never has to reconcile it against a second picture.
The drift also inverts: a no-end-frame take drifts *away* from its start over 8s, so run backwards
that drift lands on the **opening** frame — where the viewer has no reference to compare against —
and the clip resolves onto your exact plate as the payoff.

⚠️ **A reversed dolly-in is indistinguishable from a dolly-out only if nothing physical moves.**
Drifting dust, a flicker, a spark or settling debris all read as running backwards. The prompt must
name nothing that moves except the camera, and the air must be explicitly empty.
💡 The ease curve reverses too — ask the push-in to *decelerate into* the subject and you get a
pull-back that *accelerates out of* it.

**When to pin anyway.** Frames mode is still right when **arrival matters more than rigidity** —
a transition between two art-directed plates, or a shot where the subject is soft (cloth, water,
crowd) and nobody can see the reconciliation happening. Rigid machinery is its worst case, and
morphing is what the feature was built for.

### 🔴 Across a big scale change, describe the MIDDLE — not just the move

Measured on GPOM scene 0 v2, 2026-08-20, four runs against one identical frame pair. Applies
**when you are pinning an end frame** — see the section above for when not to.

| Run | Prompt | Tier | Result |
| --- | --- | --- | --- |
| 1 | Long — names what fills the frame *during* the pull ("more and more of the flat unbroken hull comes into view around it", "the flush seams and rivet lines slide outward past the lens") | Fast | ✅ Clean, evenly paced |
| 2 | **Short** — front-loaded "camera-only move, nothing else moves", middle left unspecified | Fast | 🔴 Invented capacitors at 3s, a whole RAM-slot motherboard at 4.5s, then a hard jump to the end frame |
| 3 | Short | **Quality** | 🔴 Same invention, same late jump |
| 4 | Long **+ an explicit no-invention clause** | Fast | ✅ **Best take.** No invention, board rigid, evenly paced |

**Why.** Two pinned end frames tell the model where to start and where to stop. Across a ~30×
scale change they say **nothing about the seven seconds in between** — and an unspecified middle
is not left empty, it is *filled with invention*, then paid for with a rushed jump to reach the
end frame on time.

This is Google's own instruction read properly: *"Spend most of the prompt on what the images
cannot show."* On a big scale change the thing they cannot show **is the middle**. Naming the
intermediate content is not re-describing the scene — the rule against re-describing applies to
what the frames already carry.

**The clause that stopped the invention**, added to the long prompt:

> *"The [subject] itself is rigid and bolted down: it holds its exact shape and position in the
> frame and does not shift, slide, rotate, drift or change angle, and no new component ever
> appears, grows or disappears on it. Nothing in the entire frame moves except [the one thing
> that should] and the camera itself."*

⚠️ **Subtraction is the wrong reflex here.** Rule 4 and §12 both say cut a clause when a shot is
not landing. That holds for *competing actions*; it does **not** hold for an underspecified
middle, where cutting made it materially worse. Two different failure modes, opposite fixes.

### ⚠️ Quality is not automatically better — and was worse here

Same frame pair, same short prompt, Fast vs Veo 3.1 Quality: **both Quality takes invented
components the start frame did not contain**, and paced the move as linger-then-jump. Fast
invented nothing on the equivalent long-prompt run.

Working read: on a shot whose whole job is a **rigid camera-only move**, extra model capability
gets spent generating content we did not ask for. Iterate *and* lock on Fast for this shot class;
save Quality for shots where something in the world genuinely has to move and be beautiful.

⚠️ n=2 per tier, one frame pair, one session. Observed, not established — but it cost 200 credits
to learn and it is the opposite of what rule 5 would lead you to assume, so it is written down.

**First+last frame is supported on all three Veo tiers** — it is *Ingredients/References* that
Quality refuses. So Quality is genuinely available for a Frames shot; it just did not help.

### Frame-pair compatibility — check before you generate

**Two good stills do not automatically make a workable transition.** The end state has to be
*"reachable through an understandable action: rotate, walk, open, unfold, pour, rise, assemble,
move forward, change lighting, or shift weather"* — *"two attractive images do not automatically
make a workable transition."* Check that subject geometry, camera height, scale and background
landmarks agree.

**The five ways a frame pair fails:**

> *"Subject scale changes dramatically between frames. Camera perspective jumps from wide to
> macro shots. Lighting from opposite directions without motivation. Too many transformations
> in one 8-second clip. [The prompt] describes an edit effect instead of a physical action."*

**Pace the ends deliberately.** To land frame 1 already in motion and frame 8 resolved for a
cut, say so at both ends — *"Motion begins immediately. The subject starts walking in the first
moment while the camera tracks at the same pace."* / *"Maintain continuous movement through most
of the shot, slow naturally near the end, and reach the final composition only in the last
moment."* The source's own caveat holds: this is direction, not a guarantee.

*(single-source, [flowveo3.com](https://flowveo3.com/posts/veo-3-1-first-last-frame-guide))*

## 5. Timestamp prompting — multi-beat inside one generation

Format: `[MM:SS-MM:SS] <shot description>. SFX: … Emotion: …`

> **Official:**
> "[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel
> and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal a
> hidden path.
> [00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with
> awe as she gazes upon ancient, moss-covered ruins in the background. SFX: The rustle of
> dense leaves, distant exotic bird calls.
> [00:04-00:06] Tracking shot following the explorer as she steps into the clearing and
> runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder and
> reverence.
> [00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small in
> the center of the vast, forgotten temple complex, half-swallowed by the jungle."

Use this for reveal → reaction → detail → pull-back inside 8 seconds. Use clip-chaining
([`consistency.md`](./consistency.md) §7) for continuity *across* 8-second windows.

⚠️ Nobody has published a reliability test of this — every source is either Google's showcase
example or an assertion that it works. How often the beat boundaries actually land is unmeasured.

### Causal chaining — a beat structure without brackets

Added 2026-08-20, and **structurally different from the bracketed technique above**: timestamps
hand the model discrete beat boundaries; this hands it one unbroken causal chain and lets
duration emerge from the physics. Google's own prompt guide choreographs a multi-beat compound
event inside one continuous 8-second shot with **no cuts and no timestamps**, by chaining each
event's consequence into the next event's trigger:

> *"Within an 8-second sequence, one of the lead vehicles… approaches a wide, shallow river
> crossing at incredible speed. Without the slightest hesitation, its unseen driver powers
> straight into the water. The impact sends an enormous, almost solid, opaque sheet of muddy
> water… spectacularly high into the air, completely engulfing the small buggy for a terrifying
> moment, obscuring it from view… **Right on its tail**, a pursuing, equally mud-encrusted,
> custom-built truck… arrives at the river crossing **just as** this massive wall of airborne
> water reaches its peak. Instead of slowing… the truck's driver… plunges directly into and
> through this opaque, turbulent curtain of muddy spray at full throttle."*

**Reach for it when the shot must read as one continuous take.** The load-bearing words are the
temporal connectives — *right on its tail*, *just as*, *for a terrifying moment* — not any
timing syntax.

**The lightweight version of the same mechanism** — three short present-tense clauses, one
stage of a journey each, no camera or timing language at all. Try this on a simple beat before
reaching for the rally-style choreography:

> *"A paper boat sets sail in a rain-filled gutter. It navigates the current with unexpected
> grace. It voyages into a storm drain, continuing its journey to unknown waters."*

*(official, [deepmind.google](https://deepmind.google/models/veo/prompt-guide/))*

**The community's bracket-free syntax** chains three states with *"first… then… finally…"*, and
works for emotional and camera-position arcs alike — *"The character starts confused and
uncertain, then gradually becomes confident and determined, finally ending with a satisfied
smile of accomplishment."* / *"The scene begins with a wide establishing shot, then smoothly
transitions to a medium shot at the 3-second mark, finally ending with a close-up on the
character's determined expression."* The guide itself files this as an untested community
discovery. (practitioner, [github.com/snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide))

**A full emotional arc with no beat syntax at all**, the sequence of reactions carrying the
structure — *"A slow push-in shot captures a young woman cleaning a spill on a hardwood floor…
As the camera gets closer, the woman abruptly freezes her cleaning motion. She raises her head,
her eyes wide with fear as if she has just heard something off-screen. After a tense moment, her
fearful expression melts into one of profound sadness and resignation, and she lowers her gaze
back to the floor."* (corroborated,
[curiousrefuge.com](https://curiousrefuge.com/blog/veo-31-quality-ai-video-generator-review))

**The shot-list alternative to MM:SS** — label each beat as a numbered clip with its own duration
and full shot spec, summing to 8s:

> *"Clip 1 (2.5s): Wide establishing, 24mm, slow drone push-in over misty forest at dawn; soft
> god rays; ambient wind; quiet tone. Clip 2 (3s): Medium close-up, 50mm, tripod static; subject
> turns toward light from window; motivated key from screen; subtle particle dust."*

This allocates **total shot duration to a beat**, not the execution speed of one move, so it is
not the banned second-level camera-timing pattern — but whether fractional durations are honoured
is untested. (single-source, [sider.ai](https://sider.ai/blog/ai-tools/best-prompt-techniques-for-veo-3_1-video-output-a-field-guide-to-cinematic-control))

## 5b. Temporal elements and editing grammar

Two officially-listed components we had never written down. Both are cheap and both do work
inside an 8-second clip.

**Temporal elements — how time flows in the shot.**

| Lever | Terms Google lists |
| --- | --- |
| Pacing | `slow-motion` · `fast-paced action` · `time-lapse` |
| Evolution (kept subtle for short clips) | "a flower bud slowly unfurling" · "a candle burning down slightly" · "dawn breaking, the sky gradually lightening" |
| Rhythm | `pulsating light` · `rhythmic movement` |

> **Official (evolution):** "A close-up of a single red rose bud, its petals tightly closed.
> The camera remains static as the flower slowly and gracefully unfurls over the course of the
> shot, revealing its vibrant inner layers. The evolution is subtle, showing a clear but
> gradual change"

Note what that example does: it **states the camera is static and gives the subject the
motion**. That is §3's rule arriving from the other direction.

**Mood-register pacing is distinct from literal speed.** Alongside `slow-motion` and
`time-lapse`, a register phrase does different work: *"the pace is unhurried and reflective,
evoking a naturalistic and quiet mood"*. (content-mill,
[imagine.art](https://www.imagine.art/blogs/veo-3-1-prompt-guide))

**Cinematic terms — editing grammar inside one generation.** Google lists `match cut`,
`jump cut`, `establishing shot sequence`, `montage`, `split diopter effect`.

> **Official (jump cut):** "A person sitting in the same position but wearing different
> outfits, with sharp jump cuts between each outfit change. The background should stay static
> and the person should reappear instantly in the new outfit, creating a fast-paced, rhythmic
> jump cut effect. The lighting and framing should remain consistent to emphasize the sudden
> changes"

**BadCode read.** These matter more than they look, because our constraint is a cut every 8
seconds. A `match cut` asked for *inside* one generation gives you two shots for one credit
spend, and an `establishing shot sequence` can carry a location change that would otherwise
cost a whole extra clip. Untested by us — flagged as an opportunity, not a proven technique.

## 6. Audio

🔴 **Veo 3.1 audio is ALWAYS ON and cannot be turned off.** Google's model-feature table lists
audio as "✔️ Always on" for Veo 3.1, 3.1 Fast and 3.1 Lite alike — there is no silent mode and
no toggle in Flow. Verified against our own footage on 2026-08-18: every one of the nine Flow
clips in the GPOM scene-0 folder carries an AAC track; only the ffmpeg-rendered ones don't.

**So for BadCode, where the track comes from Suno: strip it in post, don't fight it in the
prompt.**

```bash
ffmpeg -i clip.mp4 -c:v copy -an clip-silent.mp4
```

Do still write one short audio line (below) — not to *get* audio, but because unspecified
audio is where Veo hallucinates laughter, studio-audience noise and stray dialogue, and a
generation can be **killed outright by an audio failure** (see
[`failure-modes.md`](./failure-modes.md) B0). Cheap insurance on a track you're about to
delete.

**Prompt audio as its own scene layer** — labelled clauses placed after the visual
description:

- `SFX: thunder cracks in the distance`
- `Ambient noise: the quiet hum of a starship bridge`
- `Audio: Crunchy, sugary typing sounds, delighted giggles.`

Rules:

- **One line of dialogue + one primary SFX + one ambient bed.** A crowded soundscape is
  muddier and less controllable.
- **Specify audio even when you want near-silence** — unspecified audio invites
  hallucinated laughter and studio-audience noise. "completely silent except for distant
  traffic"; "quiet studio room tone, no music".
- **Tie SFX to a visible beat for sync:** "Add [sound] exactly when [visible action]
  happens. Keep it [volume/style]."
- **Music: describe mood, instrumentation and dynamics; never name an artist, song or
  brand-genre.** For BadCode this is mostly moot — **the track comes from Suno and is
  laid in post. Do not ask Veo to score anything.**
- In a timestamped multi-shot prompt, give each beat its **own** SFX line rather than one
  global note.
- **Ambience must not compete with dialogue.** One bed, kept low.
- **Budget audio rerolls separately from picture.** Audio is materially less reliable; a
  good visual take frequently arrives with garbled dialogue. If audio is close but not
  right, take the picture and re-voice in post rather than burning credits.

## 7. Dialogue — the resolved syntax

Google still contradicts itself, and both sides were re-checked at source on 2026-08-18:

| Page | What it does |
| --- | --- |
| **Video generation prompt guide** (Cloud) | **colon** — *"the man in the red hat says: Where is the rabbit?"*, and again in its worked example: *"The seasoned detective says: Your story has holes."* |
| **Gemini API Veo guide** (ai.google.dev) | **quotes** — *"Dialogue: Use quotes for specific speech."* |

Its older Vertex best-practices page states the reason for the colon outright: *"To prevent
the model from rendering text in the video, use a colon (:) after the speaker's action to
denote speech and avoid using quotation marks."* Two of the three primary pages point at the
colon, and only the colon page gives a mechanism. We keep the colon.

**Default form:**

```
The man in the green coat says: We have to leave now.
(no subtitles, no captions, no on-screen text)
```

Plus, where a negative field exists: `subtitles, captions, on-screen text, text overlay,
burned-in text`.

Why: burned-in subtitles are a **documented, Google-acknowledged, only partially fixed**
Veo behaviour — the model learned captioning from caption-heavy training video, and
Google's on-record workaround is literally "try your prompt again". Quote marks are the
strongest available signal that a string should be *rendered*. Use quotes only if the
colon form fails to trigger speech at all; treat this as model-version-sensitive.

Other dialogue rules:

- **Attach voice, accent and tone immediately before the speech verb**, not trailing
  after the line: "Bigfoot says in a rough, deep, and booming Scottish male voice: …"
- **Name every speaker by a visual identifier every time they speak:** "The woman
  wearing pink says: …" / "The man with the glasses replies: …"
- **One punchy sentence per clip** — roughly 8 seconds of speech maximum. Longer runs
  rushed and slurred; too short leaves gibberish filler.
- **Spell uncommon names phonetically** ("foh-fur"). Relevant for BadCode's invented lore.
- **Screenplay form is officially attested too:** `Speaker: 'line'` labels work.
- **Lip sync:** anchor the visual first ("speaker faces camera for the line", "mouth
  movement matches the words without exaggerated expression"), then the line. Perfect lip
  sync is not always achievable — keep a re-voice-in-post fallback.
- If Veo keeps inserting dialogue you didn't ask for, don't write "silent" — write the
  actual intended soundscape.

**The dialogue block is not a Veo quirk, it is model-agnostic craft.** OpenAI's own Sora
cookbook independently lands on the same fix — place spoken lines in a labelled block below the
prose description *"so the model clearly distinguishes visual description from spoken lines"*,
e.g. `Robot says quietly: "Almost lost it… but I got it!"` under a dedicated **Dialogue**
heading. Two labs, same failure mode, same answer. (first-party OpenAI documentation,
[developers.openai.com](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide))

## 8. Negatives — three channels, three syntaxes

| Channel | Syntax | Example |
| --- | --- | --- |
| Vertex API `negativePrompt` | Bare nouns. **Never** "no"/"don't"/instructive language | `wall, frame` · `people, animals` · `overhead lighting, bright colors` |
| Flow's negative field, where exposed | Short comma list, 3–7 items | `subtitles, captions, blur, shaky camera, distorted hands` |
| Inside the main prompt | Positive description of the end state | "a desolate landscape with no buildings or roads" · "low angle, ceiling out of frame" |

> **Official (the negative-prompt field, verbatim):** *"Not recommended: using instructive
> language or words such as 'no' or 'don't'. For example, avoid prompts such as 'no walls' or
> 'don't show walls'. Recommended: Describe what you don't want to see. For example, 'wall,
> frame'."* Its worked pair generates an autumn-oak animation, then re-generates it with the
> negative prompt `urban background, man-made structures, dark, stormy, or threatening
> atmosphere`.

⚠️ **Flow's compose bar exposes no negative-prompt field.** The bare-noun syntax above is an
**API** affordance (Vertex / Gemini `negativePrompt`). Inside Flow you only have row 3 —
positive description of the end state. Don't paste bare-noun exclusion lists into the Flow
prompt box expecting API behaviour; there they are just more nouns naming the thing you don't
want (see below). Kling publishes a real negative-term list — *"blur, distortion, watermark,
text overlay, low quality, compression artifacts, flickering, inconsistent lighting, morphing
faces, extra limbs, unnatural physics"* — which is why practitioners arriving from Kling keep
pasting exclusion lists into Flow's compose bar. There is nothing there to receive them.
(practitioner, [ambienceai.com](https://www.ambienceai.com/tutorials/kling-prompting-guide))

Google's guide does show a trailing list form inside the prompt ("no logos, no extra
text, no crowds") for removing *artifacts*, and that works. What does not work is
sentence-form prohibition ("don't include logos") or negating a whole subject category
("no people") — use framing or a positive empty-scene description instead.

### The failure this rule exists for (2026-08-18)

Naming the thing you don't want **summons it**. Three attempts at one shot, all three broken
by the same artefact:

| Attempt | What the prompt said about doors | Result |
| --- | --- | --- |
| v1 | nothing at all | a cabinet door swung open |
| v2 | "every door, panel and surface stays shut… nothing opens, swings, rotates" | doors swung open |
| v3 | the words door/panel/swing/rotate/open never appeared | doors swung open, wider |

Two lessons, and they are different:

1. **The negation in v2 was worse than useless** — it put "door", "swing", "rotate" and
   "open" into the prompt five times. That is this section's rule, and it was already written
   down here when the prompt was authored. It was read and ignored.
2. **But v3 proves wording was never the real lever.** The artefact survived a prompt that
   never mentioned it. See §9 — this was a capability limit, not a prompt defect, and no
   amount of rewriting was going to fix it. **Two identical failures with different wording
   means stop rewriting and question the shot.**

### ⚠️ A flagged exception to rule 12 — documented in the wild, untested by us

Added 2026-08-20. **Do not adopt; run our own comparison first.**

Replicate's own Veo blog recommends brute-force repeated negation for subtitles specifically,
as a last resort after both the colon form and `(no subtitles)` have failed — *"if all else
fails, keep saying No subtitles. No subtitles! Multiple times"*. Replicate operates Veo at API
scale. Separately, a practitioner page with five shown photorealistic outputs writes *"no AI
look, no stylization"* directly into the main prompt body of all five prompts.

Neither shows an A/B isolating the clause — the shown outputs prove the whole prompt worked, not
that clause. And our own door-hinge test above is measured on this account, which is better
evidence than either page. **But both can be true**: naming-summons may hold for *subjects in
the world* and not for *rendering artefacts like captions*, which are a different failure class.

The test that settles it: one clip with `(no subtitles, no captions, no on-screen text)` as now,
one with the repeated-negation form, otherwise identical. Rule 12 does not move until it runs.
(practitioner, [replicate.com](https://replicate.com/blog/using-and-prompting-veo-3) and
[blog.designhero.tv](https://blog.designhero.tv/veo-3-flow-cinematic-realism-midjourney/))

### A second, independent data point for the door-hinge failure

A developer-forum report describes a deliberately armless, non-humanoid spherical character
coming back with human arms, hands and shoulders across dialogue and action shots, despite a
correct reference image and repeated worded negations — *"No arms / No hands / Armless /
Leg-only entities / Hermetically sealed spherical bodies / Zero upper appendages"*. One
unresolved post with no replies, so it is consistent with our measurement rather than
independent proof of it: **negation plus a correct reference still loses to a strong anatomical
prior.** (practitioner,
[discuss.google.dev](https://discuss.google.dev/t/veo-3-1-model-ignores-negative-prompts-for-non-humanoid-character-anatomy/351836))

## 9. What Veo cannot do — reach for post instead

Some shots are not prompt problems. Recognising them early is worth more than any phrasing.

**Near-field parallax past flat parallel structures.** Dolly down a corridor, an aisle, a row
of columns or racks, and Veo fakes the parallax by *rotating the geometry* — surfaces hinge
open like doors as they pass. Measured 2026-08-18 across three prompts and two tiers; wording
made no difference. If a shot travels close past parallel flat surfaces, expect this.

✅ **PARTLY SOLVED, 2026-08-20 — and the lever was art direction, not wording.**

That test varied *prompt wording* across three prompts and two tiers. It never varied **the
geometry in the frame**. It turns out that is the whole variable.

**Measured on GPOM scene 0 (v2), same session, same tier:** a pull-back from a macro circuit
board out to a satellite was run twice against two different target stills.

| Target still's geometry | Result |
| --- | --- |
| Board recessed in a **bay with angled panels** either side | 🔴 The panels **rotated closed over the board** as the camera pulled back — the hinge, running in reverse |
| Board mounted **flush in one continuous sealed hull**, flush rivet lines, level seams | ✅ **No hinge at all.** Eight seconds of clean continuous pull, hull rigid throughout |

**The rule: Veo hinges what is hinge-able.** Given a surface that *could* plausibly pivot — a
door, a bay panel, a rack front, a louvre — it will animate parallax by rotating that surface
instead of translating the camera. Given a surface with no plausible pivot, it cannot, and it
translates instead.

**So the fix is upstream of the prompt.** Art-direct the hinge out of the frame:

- Flush-mount anything that must stay put. *"one continuous unbroken flat panel… smooth and
  uninterrupted… flush rivet lines and shallow engraved seams that lie completely level with
  the surface"*.
- Avoid recesses, bays, covers, louvres and anything that reads as a door in the **still**,
  not just in the prompt.
- Support it in the motion prompt positively: *"Every panel and surface stays rigid, flat,
  level and sealed for the entire shot; the hull is one solid piece and holds its exact shape;
  nothing on it tilts, pivots, folds, rotates or changes angle at any point."*

⚠️ **The original finding still stands for genuinely hinge-able subjects.** A server hall of
rack doors has pivots in it by definition, and no wording removes them — that shot still belongs
in post. What has changed is that hinging is now a **property of what you put in frame**, not a
blanket capability limit on travelling moves.

⚠️ Depth-cue layering in the source still (§3) remains a separate untested variable.

**The rule that follows: a camera-only move on a still belongs in post, not in Veo.**

If nothing in the world actually moves — no cloth, no water, no crowd, no machine turning —
and the only motion is the camera (push, pull, pan, tilt, drift), then it is a scale-and-crop
on one image. Render it with ffmpeg or in the edit and you get:

| | Veo | Post |
| --- | --- | --- |
| Artefacts | hinging, morphing, invented motion | **none possible** — it is one image |
| Length | 8s hard cap | **any** |
| Resolution | 720p base | **source resolution** |
| Ease curve | whatever it feels like | exact |
| Cost | 10–100 credits per attempt | free, seconds |

Worked example: `docs/stories/gitpush-origin-master/storyboard/img/s00-pullback-post-12s.mp4`
— a 12s 1080p zoom-out that Veo failed at four times, rendered in one ffmpeg pass.

🔴 **The full post lane now has its own file: [`post-production.md`](./post-production.md).** The
Veo-or-post decision, the tested recipe book (reverse, ping-pong loop, eased `zoompan` move on a
still, retime, chain, crop, contact sheet), and the resolution ceiling that decides which shots
post can actually take. **Read it before spending a credit, not after a failure.**

**Reserve Veo for shots where something in the world has to move.** That is what it is for,
and it is very good at it — the same session's orbital arc and atmospheric descent were both
single-take successes.

### Repair the take instead of rerolling it

Flow ships two targeted edit paths this file never named, and both make some bad takes
salvageable rather than discardable.

- **Insert** adds an element to an already-generated clip and *"handles complex details like
  shadows and scene lighting, making the addition look natural"* — a prop-continuity fix that
  does not cost the whole shot.
- **Lasso** draws a freehand selection around a region of a still *or a video frame* and takes
  a plain-language change (*"remove the man"*, *"add Koi fish in the water"*). On video the edit
  *"intelligently applies your described change consistently across the relevant portion of the
  clip, maintaining continuity of motion, lighting, and physics."*

🔴 **Lasso is announced on Google's blog and absent from the current Flow help page.** Verify it
exists in our app before planning a workflow around it — five-minute check.
⚠️ Neither works after an Extend ([`consistency.md`](./consistency.md) §7).

*(official, [blog.google](https://blog.google/innovation-and-ai/products/veo-updates-flow/) and
[blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/))*

## 10. Meta-prompting

Google's own recommended pattern: ask Gemini to draft Veo prompts in batches of 5–10,
giving it (1) a specific task, (2) a precise format constraint, (3) concrete material
constraints ("foil paper or shiny paper", not "paper"), and (4) the emotional target.
Flow's help says the same: "Send Gemini your prompt, an image, or even a video and ask
it to write you new prompts."

This is essentially what a flow-driving skill does when it plans a wave of shot prompts.

**The persona meta-prompt, verbatim.** Google's own Flow blog publishes a drop-in system prompt:

> *"You are the world's most intuitive visual communicator and expert prompt engineer. You
> possess a deep understanding of cinematic language, narrative structure, emotional resonance,
> the critical concept of **filmic coverage** and the specific capabilities of Google's Veo AI
> model. Your mission is to transform my conceptual ideas into meticulously crafted,
> narrative-style text-to-video prompts that are visually breathtaking and technically precise
> for Veo."*

Note the term it introduces that our camera vocabulary does not carry: **filmic coverage**.

🔴 **Gemini drops consistency between batched prompts unless you order it not to.** Google says
so outright — *"If you're using Gemini to help generate multiple clips that have scene
consistency, you'll need to explicitly tell Gemini to repeat all essential details from prior
prompts."* This is the missing link between rule 9 and this section: the identical-wording
discipline has to be an **explicit instruction inside the meta-prompt**, because the default
batch behaviour silently discards it.

*(official, [blog.google](https://blog.google/technology/ai/flow-video-tips/))*

## 11. Three things that reliably improve a prompt

Added 2026-08-18 from the external sweep; each is absent from the rest of this file.

**1. Replace speed adjectives with timestamps.** "Slow", "quickly" and "gradually" are
weakly honoured — the model has no scale to hang them on. A timestamped beat is unambiguous
about how long something takes:

> ❌ `a very slow push toward the planet`
> ✅ `[00:00-00:06] the camera pushes toward the planet, covering barely a third of the
>    distance in the whole shot`

**Live proof (2026-08-18, GPOM scene 0):** two takes of one prompt containing "slow
continuous dolly-in" — one crossed the whole move in 4.5s of an 8s clip, the other paced it
across the full 8. Same words, different speeds. The adjective did nothing; only the
timestamps in the sibling prompt held.

**2. Describe the physics, not just the subject.** Name how a thing *behaves* and the clip
stops looking synthetic: `smoke curls rather than billows`, `rain falling at 45 degrees`,
`the fabric settles a beat after she stops`. Material behaviour is where the uncanny lives.
Full treatment, with measured rates and a paste-ready stability clause, in
[`physics-and-motion.md`](./physics-and-motion.md).

Two labelled-clause patterns worth stealing, both transfer-from-competitor, both untested on
Veo. From **Runway**: *"Stop describing what things look like. Start describing the forces acting
on them."* → `A heavy vintage sedan moving at high velocity impacts a concrete barrier. Physics:
The front hood crumples inward…` From **Sora 2**: *"Explain WHY things happen, not just WHAT you
see."* → `A glass of milk is knocked over by a stray elbow. Causality: The glass tips on its
fulcrum, liquid sloshes against the rim…` (practitioner,
[medium.com/@creativeaininja](https://medium.com/@creativeaininja/how-to-actually-control-next-gen-video-ai-runway-kling-veo-and-sora-prompting-strategies-92ef0055658b))

**3. State the camera separately from the action.** Keep the camera clause and the subject
clause in separate sentences rather than braided into one. Veo parses both more reliably
when they are not competing inside a single instruction — and it makes the "one move per
clip" rule visible at a glance, because the camera clause is right there on its own.

**And here is the mechanism it defends against** (added 2026-08-20). A camera move gets silently
dropped in two nameable ways, neither of which is the wording of the move:

1. **Subject-motion substitution.** *"A common example: 'Character walks toward camera as the
   camera dollies in.' If the subject already 'moves toward camera,' the model can satisfy the
   'getting closer' idea without moving the camera at all."*
2. **Contradiction collapse.** *"If your prompt implies both handheld and locked-off, or
   tripod-stable and shaky documentary, the model may resolve the contradiction by choosing the
   simplest outcome: minimal camera motion."*

Also named: *"narrative dilution [when] too many actions bury the camera instruction"* — which is
rule 4 arriving from a third direction.

**The fix is the ordering we already use — camera at the top of the stack — plus never letting
subject motion carry the same read as the camera move.** If the shot needs both, make them
different reads: the subject moves *across*, the camera moves *in*. (single-source,
[veo3gen.app](https://www.veo3gen.app/blog/veo-31-prompt-slotting-fix-why-your-shot-ignores-the-camera-move-and-how-to-rewr))

## 12. Iteration discipline

- **Don't re-roll the same failing prompt.** Similar prompts yield near-identical
  outputs. Change a verb, a camera term, or the framing of the action.
- When a result is wrong, the productive revision is **subtraction** — remove
  content-description, cut to 1–2 motion instructions — before adding anything new.
- **Repetition is not emphasis.** Restating a word or phrase to weight it does not add weight,
  and tends to make output noisier and less focused. Vary the phrasing instead. (The one flagged
  exception is in §8, and it is unadopted.) (practitioner,
  [eachlabs.ai](https://www.eachlabs.ai/blog/structuring-veo-3-prompts-for-better-motion-control))

---

## Sources

Platform behaviour in this file that is marked "verified live" comes from our own smoke tests
against Flow (`packages/flow-mcp/src/smoke-*.ts`) and is dated where it was checked. The
prompt-craft guidance was cross-checked against these on **2026-08-18**:

**Primary sources, read end to end on 2026-08-18** — not from search snippets, which is how
the previous pass cited the first of the secondary links below without ever opening it:

- [Video generation prompt guide — Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) — the "Anatomy of a prompt" component list, every camera/lens/lighting/style term, the negative-prompt rule, the dialogue colon. *Moved: the old `cloud.google.com/vertex-ai/generative-ai/docs/video/…` URL 301s here.*
- [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) — the model-feature table (durations, resolutions, audio always-on), limitations, Extend semantics, reference images and first/last frame.
- [Learn about Google Flow models & supported features](https://support.google.com/labs/answer/16352836?hl=en) — the per-tier matrix Flow actually enforces.
- [Create videos in Google Flow](https://support.google.com/labs/answer/16353334?hl=en) · [Edit videos & build scenes in Google Flow](https://support.google.com/labs/answer/16935718?hl=en) — ingredients, frames, characters, voices, Extend, Scenebuilder.

Secondary, from the 2026-08-12 sweep:

- [Ultimate prompting guide for Veo 3.1 — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) *(Google-authored, blog tier)*
- [How to prompt Veo 3.1 — Replicate](https://replicate.com/blog/veo-3-1)
- [Veo 3.1 Prompt Guide — LTX](https://ltx.io/blog/veo-prompt-guide)
- [The ultimate prompting guide for Veo 3.1 — Atlabs](https://www.atlabs.ai/blog/the-ultimate-prompting-guide-for-veo-3-1)
- [Structuring Veo 3 Prompts for Better Motion Control — Eachlabs](https://www.eachlabs.ai/blog/structuring-veo-3-prompts-for-better-motion-control)
- Veo 3 negative prompts — Anakin *(link dead as of 2026-08-18; claim survives only as recorded here)*
- [30 Cinematic Camera Prompts for Veo 3 and Kling — Prompt Architects](https://prompt-architects.com/blog/25-30-cinematic-camera-prompts-for-veo3-and-kling)
- [Best Prompt Techniques for Veo 3.1 Video Output — Sider](https://sider.ai/blog/ai-tools/best-prompt-techniques-for-veo-3_1-video-output-a-field-guide-to-cinematic-control)

**Added by the 2026-08-20 ten-angle sweep** (verified in an independent pass; tiers marked
inline on every claim):

- [Veo prompt guide — DeepMind](https://deepmind.google/models/veo/prompt-guide/) *(official — the causal-chaining and long-form showcase examples. Not previously cited: we had been citing the Cloud guide instead)*
- [5 tips for using Flow — blog.google](https://blog.google/technology/ai/flow-video-tips/) *(official — the persona meta-prompt and the Gemini-batch consistency warning)*
- [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) *(official — the 1,024-token prompt cap)*
- [Flow updates, February 2026](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/) · [Veo updates in Flow](https://blog.google/innovation-and-ai/products/veo-updates-flow/) *(official — Lasso and Insert)*
- [Sora 2 prompting guide — OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) *(first-party, other lab — the labelled dialogue block, and Sora's scene-first ordering)*
- Secondary, phrasing only: [flowveo3.com](https://flowveo3.com/posts/veo-3-1-first-last-frame-guide) · [replicate.com](https://replicate.com/blog/using-and-prompting-veo-3) · [veo3gen.app](https://www.veo3gen.app/blog/veo-31-prompt-slotting-fix-why-your-shot-ignores-the-camera-move-and-how-to-rewr) · [film.fun](https://www.film.fun/articles/nano-banana-2-prompting-guide-frame-composition-and-reframing-for-ai-video) · [nerdbot.com](https://nerdbot.com/2026/04/27/rethinking-first-frame-quality-through-nano-banana/) · [github.com/snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)

**Where they and we disagree, we win on platform mechanics and they win on prompt craft** —
our mechanics are measured on this account, and none of them have measured it; their craft
guidance is drawn from far more generations than we have run.
