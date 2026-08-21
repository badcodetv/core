# Physics and motion — how Veo handles weight

What the model actually gets right, what it reliably gets wrong, and the phrasings that move
the needle. **Read this at storyboard time, not while writing the prompt** — its first job is
to tell you whether a shot is worth attempting at all.

Failure *symptoms* and their mitigations stay in [`failure-modes.md`](./failure-modes.md).
This is the craft.

---

## 1. The measured picture

Google's own framing is **comparative, not absolute**: *"Participants choose Veo 3.1's outputs
over other models for having visually realistic physics on the physics subset of MovieGenBench
prompts."* (official, [deepmind.google/models/veo](https://deepmind.google/models/veo/))

Read it beside the absolute numbers, which are far less flattering.

| Measurement | Finding |
| --- | --- |
| Expert-annotated benchmark — 10,990 annotator traces, 22 physical categories, 5 models | **79.4%** of Veo 3.1 Fast *exocentric* clips carry at least one human-identifiable physics glitch (1.32 ± 1.11 glitches per video, severity 3.01 ± 1.74). Egocentric is **97.5%** (1.69 ± 1.12, severity 3.37 ± 1.56) |
| Google's own zero-shot-reasoning paper, on Veo 3 | Optical physics strong — refraction/reflection through a glass sphere **0.92**, additive colour-mixing **0.92**. Buoyancy inconsistent — bottle cap **0.58**, rock **0.83**. Object trajectory under gravity about **0.5**, on Earth and Moon alike |

*(practitioner-with-evidence, both with named methodologies —
[arxiv.org/html/2603.19607v1](https://arxiv.org/html/2603.19607v1) and
[huggingface.co/papers/2509.20328](https://huggingface.co/papers/2509.20328))*

**Nobody should cite the DeepMind line as proof physics "just works" now.** The useful reading
is the *unevenness*: light behaves, weight does not. A shot whose point is a reflection, a
refraction or a colour mix is on solid ground. A shot whose point is that something is heavy
is a coin flip.

⚠️ Both studies test **Veo 3**, not 3.1, and say so. Whether 3.1 moved the numbers is unknown
and Google has not republished the study.

## 2. The stability clause — paste it

Defensive wording, not a technique with its own failure mode. Harmless if it does nothing.

> realistic shadows remain attached to the product · objects keep consistent weight and scale ·
> reflections match the product position · no impossible stretching or morphing ·
> camera moves like a smooth dolly, not a teleport

*(single-source, every phrase confirmed verbatim on the live page, no shown output —
[veo3ai.io](https://www.veo3ai.io/blog/veo-3-camera-control-prompts-2026))*

The last clause earns its place twice over: it is also the anti-morph instruction for a camera
move, and morphing mid-move is the family our own measured parallax-hinging failure belongs to.

## 3. Force verbs beat motion verbs

> *"Vague actions result in floaty, weightless movement because the model lacks a sense of force
> or resistance. To avoid this, define how energy moves through the body using force-based verbs
> like **push, pull, strike, slam, sway, ripple, or spiral**."*
>
> *"One dominant force per prompt produces cleaner, more believable motion."*

*(single-source, [invideo.io](https://invideo.io/blog/google-veo-prompt-guide/))*

This is rule 4 applied to physics rather than to camera: **one dominant force**, the same way
one action and one camera move.

### The labelled-clause patterns, from adjacent models

Both untested on Veo, both cheap to try, and both are the same move our own §11.2 already makes
without a name for it.

- **Runway** — *"Stop describing what things look like. Start describing the forces acting on
  them."* → `A heavy vintage sedan moving at high velocity impacts a concrete barrier.
  Physics: The front hood crumples inward…`
- **Sora 2** — *"Explain WHY things happen, not just WHAT you see."* → `A glass of milk is
  knocked over by a stray elbow. Causality: The glass tips on its fulcrum, liquid sloshes
  against the rim…`

*(practitioner, transfer-from-competitor —
[medium.com/@creativeaininja](https://medium.com/@creativeaininja/how-to-actually-control-next-gen-video-ai-runway-kling-veo-and-sora-prompting-strategies-92ef0055658b))*

## 4. Name the force AND the material in the same clause

Google's own showcase does exactly this — never just *water*, but the force that displaced it
and what it is made of:

> *"The impact sends an enormous, almost solid, opaque sheet of muddy water, **mixed with stones
> and debris from the riverbed**, spectacularly high into the air"* · *"water cascading from its
> roof and chassis"*

*(official, [deepmind.google/models/veo/prompt-guide](https://deepmind.google/models/veo/prompt-guide/))*

And **stacking distinct phenomena in one dense clause is rewarded**, on Veo's own model page —
mechanical dynamics + particulate + optical distortion + reflection, all named:

> *"The white Lamborghini Countach drifts sharply around a corner and slides into a perfect park
> on a sunlit city street, smoke and tire screech filling the air, camera panning fast with
> cinematic motion blur, dust particles and heat haze, dynamic reflections on the car,
> hyper-realistic lighting, upbeat and energetic vibe."*

*(single-source — prompt confirmed on the live page, output not viewed,
[fal.ai/models/fal-ai/veo3.1](https://fal.ai/models/fal-ai/veo3.1))*

**This does not contradict rule 4.** Rule 4 caps *actions and camera moves*. Physical detail
attached to a single action is the one axis where density pays.

## 5. Budget the motion detail

> *"Name the primary motion clearly, and name secondary motion (coat fluttering, hair moving,
> environment) if it matters. Skip the third-order detail."*

*(single-source, [sureprompts.com](https://sureprompts.com/blog/ai-video-prompting-complete-guide-2026))*

The model invents third-order motion anyway, and specifying it competes with the primary action
for the same attention budget.

## 6. Why stills-first is a physics decision

> *"By providing a static image, you allow the model to reallocate its resources from inventing
> a scene to perfecting the physics of the movement within it."*

*(content-mill, bare assertion with no A/B —
[leonardo.ai](https://leonardo.ai/news/mastering-prompts-for-veo-3))*

Weak evidence, but it gives README rule 6 a *mechanism* it currently lacks, and the mechanism is
plausible enough to change how we write an animate prompt: on an existing still, every word
spent re-describing the scene is a word not spent on the motion.

## 6b. 🔴 Veo animates what the plate gives it something to animate

Measured on GPOM scene 1, 2026-08-21, and it arrived as a correction to our own first reading.

| Plate | Takes | Result |
| --- | --- | --- |
| Grimy night alley, dense, dark, high-detail — asked for **rain** | 5 across 3 plates, 2 prompt strategies | One pedestrian walked. Nothing else moved in any of them. Rain never appeared, twice |
| Modern harbour city at night — asked for **water, ferries, cloud, window lights** | 1 | Moved immediately and well. Ferries tracking with visible wakes, thousands of windows twinkling, water surface breaking and reforming, cloud drifting |

Same tier (Veo 3.1 Fast), same settings, same prompt shape. **The variable is the plate, not the
tool.** Open water, distant traffic, cloud and a large field of small lights are things Veo will
move. Fine particulate — rain, drizzle, spray — over a dark, dense, high-detail surface is not.

So the storyboard-time question is not *"will Veo animate this?"* but **"what in this frame is Veo
already good at moving, and is any of it in shot?"** If the honest answer is nothing, the shot is a
locked plate and belongs in post ([`post-production.md`](./post-production.md) §1) — which is a
first choice, not a defeat.

### ⚠️ Over-locking the camera freezes the world

The trap that nearly hid the finding above. Prompts that stacked *"no pan, no tilt, no zoom, no
drift, no handheld shake… nothing else moves at all"* froze the **entire clip**, subject included —
identical to a still, and identical in the file to a plate Veo simply refused.

**Name the moving thing first and hard, then lock the camera.** One clause of camera lock at the
end does the job; a wall of negations reads as "hold everything".

## 7. Shot classes to avoid

Cross-referenced to [`failure-modes.md`](./failure-modes.md) Part B.

| Avoid | Why |
| --- | --- |
| **Repeated or periodic impacts beyond the first cycle** | The first bounce is right; later ones lose height, timing and rotation. Ask for one impact, not a rhythm |
| **Liquid that must respond to the frame's own acceleration** | No model tested passed the "glass of water in a moving car" test — gravity-driven water is fine, inertial water is not |
| **Near-field parallax past flat parallel structures** | Our own measurement: Veo hinges the geometry open instead. See `video-prompting.md` §9 — though the source still's depth-cue composition is an untested variable, not a ruled-out one |
| **Precise hand articulation** | Long-standing, unfixed |
| **Rain, drizzle or spray over a dark dense scene** | Measured GPOM scene 1, 2026-08-21: four takes across two prompt strategies produced no rain at all on a night alley plate. Fine particulate over high-detail dark surfaces is below what Veo renders. Post it, or pick a frame with water, cloud or traffic in it instead — see §6b |
| **Orbiting a rigid subject faster than ~35–40° per 8s clip** | Measured on GPOM scene 0, 2026-08-21, two candidate pairs from identical prompts. The take that arced ~90° stopped moving the camera and started **redesigning the object** — antenna swelling, solar arrays changing count, hull reproportioning. The ~35–40° takes held. Chain several slow stages instead of asking for one fast arc |

---

## Sources

Gathered by the **2026-08-20** ten-angle sweep and verified in an independent pass. Tiers are
marked inline on every claim; the two benchmark studies clear the ban on bare numeric claims
because both publish a methodology and an N.

- [Veo — DeepMind](https://deepmind.google/models/veo/) · [Veo prompt guide — DeepMind](https://deepmind.google/models/veo/prompt-guide/) *(official)*
- [Expert-annotated physics benchmark](https://arxiv.org/html/2603.19607v1) *(10,990 traces, 22 categories, 5 models)*
- [Video models as zero-shot reasoners](https://huggingface.co/papers/2509.20328) *(Google research team, per-phenomenon rates on Veo 3)*
- [AI video models compared](https://www.lovart.ai/blog/ai-video-models-compared-2026) *(5 models, 50 identical prompts, 250 outputs, scored by a CFD PhD candidate, Cohen's κ 0.84)*
- Secondary, phrasing only: [veo3ai.io](https://www.veo3ai.io/blog/veo-3-camera-control-prompts-2026) · [invideo.io](https://invideo.io/blog/google-veo-prompt-guide/) · [sureprompts.com](https://sureprompts.com/blog/ai-video-prompting-complete-guide-2026) · [fal.ai](https://fal.ai/models/fal-ai/veo3.1) · [leonardo.ai](https://leonardo.ai/news/mastering-prompts-for-veo-3)

**What only our own testing can settle:** whether Veo 3.1 moved the Veo 3 physics numbers;
whether our parallax-hinging failure is a motion-prompt problem or a source-still problem
(vary the still's depth-cue separation, hold the wording identical); and whether the labelled
`Physics:` / `Causality:` clause patterns do anything on Veo at all.
