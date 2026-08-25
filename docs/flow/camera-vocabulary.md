# Camera vocabulary

Shot, move, lens, lighting and grade terms, with how reliably Veo actually honours
each. Applies to both stills and video unless noted.

## Reliability tiers

⚠️ **These tiers are Veo's, and vocabulary does not port.** A named studio protocol (5 tests,
one generation per model) found the prompt *"POV shot of a man who just fell standing up fast
and running. Fast-paced shot. quick movements."* produced a clip that *"resembled more of a
tracking shot"* on Veo 3.1 — which also *"added a random additional person to the mix"* — while
the same prompt read correctly on Kling. **A term working on another model is not evidence about
this one.** (corroborated, [curiousrefuge.com](https://curiousrefuge.com/blog/kling-vs-veo))

**Tier 1 — dependable, use freely.**
Shot sizes: extreme wide / establishing, wide, medium, medium close-up, close-up,
extreme close-up, two-shot, over-the-shoulder, POV.
Moves: **push-in / dolly-in** (the safest move there is), dolly-out, pan, tilt,
tracking, static / locked-off, handheld.
Focus: shallow depth of field, bokeh, deep focus.
Angles: eye-level, low angle, high angle, Dutch angle, bird's-eye, worm's-eye.

**Tier 2 — works, expect retries.** Crane / jib, arc / orbit, rack focus, whip pan.
Google's own 180-degree arc phrasing generalises to any partial sweep pinned between two named
viewpoints — *"Camera moves 45 degrees from front-left to front-right."* Low risk: an arbitrary
degree value gets approximated, not refused. (content-mill,
[veo3ai.io](https://www.veo3ai.io/blog/veo-3-camera-control-prompts-2026))

**Tier 3 — hero-shot only, budget failures.** Dolly zoom (vertigo), full 360° orbit,
anything requiring precise hand articulation in frame.

**Google backs the idea of tiering, without publishing tiers.** Its prompt guide carries the
same caveat twice, once over the angle list and once over the lens list: *"Some advanced camera
angles are not officially supported. The results and reliability may vary depending on the
overall prompt and your specific use case."* So the model has a supported core and a fringe;
which terms sit where is ours to measure, and the tiers above are that measurement.

## The official catalogue

Every term below is listed by name in Google's video-generation prompt guide, with the gloss
and the example it gives. Terms **not** in our tiers above are marked 🆕 — they were missing
from this file until 2026-08-18.

**Camera movements** — note that Google treats these as a *separate prompt component* from the
angle, which is why §Rules 1 asks for the camera in its own clause.

| Move | What it is | Google's example |
| --- | --- | --- |
| Static (fixed) | camera completely still | "static shot of a serene landscape" |
| Pan (left/right) | rotates horizontally **from a fixed position** | "slow pan left across a city skyline at dusk" |
| Tilt (up/down) | rotates vertically from a fixed position | "tilt down from the character's shocked face to the revealing letter in their hands" |
| Dolly (in/out) | camera **physically moves** closer or further | "dolly out from the character to emphasize their isolation" |
| 🆕 **Truck (left/right)** | camera physically moves **sideways**, often parallel to the subject | "truck right, following a character as they walk along a busy sidewalk" |
| 🆕 **Pedestal (up/down)** | camera physically moves **vertically**, keeping a level perspective | "pedestal up to reveal the full height of an ancient, towering tree" |
| Zoom (in/out) | the **lens** changes focal length; the camera does not move | "slow zoom in on a mysterious artifact on a table" |
| Crane | mounted on a crane, vertical or sweeping arcs | "crane shot revealing a vast medieval battlefield" |
| 🆕 **Aerial / drone** | high altitude, smooth flying movement | "sweeping aerial drone shot flying over a tropical island chain" |
| Handheld / shaky cam | less stable, jerky; realism, immediacy, unease | "handheld camera shot during a chaotic marketplace chase" |
| Whip pan | extremely fast pan that blurs; a transition | "whip pan from one arguing character to another" |
| Arc | circular or semi-circular path around the subject | "arc shot around a couple embracing in the rain" |

🔴 **Dolly and truck and pedestal are three different words for three different moves, and
"zoom" is none of them.** Naming the wrong one is the most common way a camera clause quietly
fails: ask for a "zoom" when you meant to travel through the space and you get a flat
magnification with no parallax. Our own scene-0 descent needed exactly this distinction — the
shot reads as a descent because it *pedestals and dollies*, and read as Google Earth when it
was written as a zoom.

**Lens and optical effects** — all officially listed: wide-angle, telephoto, shallow depth of
field (bokeh), deep depth of field, lens flare, 🆕 **rack focus**, fisheye, 🆕 **vertigo effect
(dolly zoom)**.

> **Official (rack focus):** "A medium shot of a detective's hand in the foreground, holding a
> single, spent bullet casing. The camera then performs a slow rack focus, shifting from the
> casing to reveal the anxious face of a witness in the background, now in sharp focus"

Rack focus is worth knowing precisely because it is **a move that is not a move** — it changes
what the shot is about without travelling, which makes it safe on the flat-parallel-surface
geometry Veo cannot dolly past (`video-prompting.md` §9).

⚠️ **Lens flare is officially supported and house-banned.** It is on Google's list, it works,
and `badcode-art-direction` forbids it. The GPOM orbital shots are a named exception recorded
in that story's ledger — don't generalise them.

## Rules

1. **Camera instruction goes first, as its own clause or sentence.** "The camera pulls
   back" standing alone beats the same words buried mid-description. Camera language
   appended after a long scene description gets ignored.
2. **One primary move per clip, two maximum.** Pan + tilt + orbit + zoom + handheld in
   one 8-second clip produces confusion.
3. **Describe start position, path, and end reveal.**
   > "Create a six-second smooth pan across a clean creator desk. Camera starts on a
   > notebook and coffee cup, pans right to reveal a laptop showing a video editing
   > timeline."
   > "Create a five-second slow push-in on a modern app dashboard displayed on a tablet.
   > Camera starts with the full tablet visible, then moves closer to the main analytics
   > card."
4. **Use plain speed adverbs, not seconds.** "slow", "gentle", "quick", "rapid",
   "smooth", "sharply". Second-level timing inside a movement clause ("dolly in over 0.5
   seconds") is unreliably parsed — the one source with comparative testing measured
   ~39% adherence and recommends adverbs instead. *This corrects a widely-repeated tip
   claiming exact durations improve specialty moves; they don't.*

   **But "slow" is not one speed.** There is a usable scale below it — *"Imperceptible /
   barely-there — used for subtle pushes that build tension without obvious motion… Slow —
   most cinematic default, works on every model… Steady / measured — locked, deliberate
   pace."* Padding does not help: *"Padding the movement description with adjectives ('a
   smooth, fluid, cinematic dolly that elegantly moves toward the subject') rarely helps and
   sometimes confuses the model."* ⚠️ Whether *imperceptible* differs from *slow* in output is
   untested, and our register lives at exactly that end of the scale.

   **The speed instruction that actually recurs in practice is relative, not absolute** — tie
   the camera's pace to something already in frame rather than naming a speed in isolation:
   *"match the subject's pace"* / *"match the vehicle's pace"* / *"natural walking or reaching
   pace"* / *"smooth controlled push/retreat"* / *"slow controlled constant motion"*.

   **Staging *when* a move starts is not the banned pattern.** `Static for first 2 seconds,
   then slow dolly-in toward [subject].` That allocates a beat of stillness before the move; it
   does not try to time the move's *execution*, which is the thing measured at ~39% adherence.

   *(single-source, [lzyprompt.com](https://lzyprompt.com/blog/ai-video-camera-movement-prompts/);
   relative-pace phrasings content-mill, [aicameramovements.com](https://www.aicameramovements.com/))*
5. **To lock the camera, say so positively:** "static shot", "fixed camera", "the camera
   is locked and still". Don't try to fight motion with negatives.
6. **Angle carries emotional register** and pairs with a shot size in one clause
   ("low-angle wide shot"): eye-level = natural, trustworthy; low = power, dominance;
   high = vulnerability; Dutch = unease; worm's-eye = mythic scale; bird's-eye =
   surveillance or flat-lay.

## Lens and focal length

18mm expansive · 24–35mm natural-wide · 50mm natural · 85mm portrait compression ·
100mm macro · telephoto isolation.

Put aperture in the same clause as the focal length: "50mm prime lens with a shallow
depth of field", "85mm lens at f/2.8", "low-angle shot with a shallow depth of field
(f/1.8)".

**Give the aperture a stated reason rather than a bare f-stop** — *"shot on an 85mm lens at
f/8 so the whole product stays sharp while the background falls into soft blur"*. (corroborated
— generated image shown beneath the prompt,
[fal.ai](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide))

Fisheye recipe: "Wide-angle / fisheye lens (10mm–14mm) – Strong foreground distortion on
hands + faces – Bright, saturated colors – High contrast, punchy sunlight."

> **Compact working combo:** "Medium shot, 35mm, slow dolly-in, subject centered, shallow
> DOF; background city bokeh; handheld micro-sway for intimacy."

## Lighting

Named photographic setups transfer directly: golden hour, blue hour, chiaroscuro,
Rembrandt, high-key, low-key, three-point softbox, hard fluorescent, rim light.

**"Motivated lighting"** — light visibly coming from an in-scene source (streetlamp,
window, monitor) — reliably grounds a scene, and is the term to reach for when a shot
looks artificially lit. *(This is also the BadCode house rule: name the actual light
source in the prompt rather than letting the model invent photogenic lighting.)*

**State source, direction and colour temperature explicitly, and repeat the same
phrasing across every clip in a sequence.** That repetition is the primary defence
against colour creep down a shot chain.

> **Official:** "The scene is lit by the harsh fluorescent overhead lights and the green
> glow of the monochrome monitor."
> "Film noir cinematography with dramatic chiaroscuro lighting, deep shadows, venetian
> blind light patterns, and high contrast black and white aesthetic."
> "golden hour rim light on a dancer in a warehouse with backlight creating a halo and
> dust particles in light beams"

### Near-black: name the light, then claim the shadow

**This is the second half of our own motivated-lighting rule** — which currently names the
source and never claims the shadow. Describing a frame as "dark" or "near-black" is not an
instruction. Say which single source is lit, and state explicitly where everything else falls:

> *"one hard light source from a window at camera left, deep falloff into shadow, a thin rim of
> light along the fruit's edge"*

The low-key siblings: *"Low-key, motivated by a single warm practical lamp; the rest of the room
in shadow."* / *"Soft single key light from a large window, deep falloff into shadow (Rembrandt
lighting)."*

*(corroborated — exact prompt with generated image shown,
[fal.ai](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide); low-key siblings
single-source, [sider.ai](https://sider.ai/blog/ai-tools/best-prompt-techniques-for-veo-3_1-video-output-a-field-guide-to-cinematic-control))*

**Why near-black is uphill.** Average frame brightness is the noise component that survives
longest during forward noising in diffusion training, so a standard denoise pass cannot move
global brightness far — near-black prompts tend to render as **muddy dark-grey rather than true
black** unless the prompt compensates. Background rationale, not a phrase to write: the
actionable half is the one-light-plus-stated-falloff recipe above. (practitioner-with-evidence,
[crosslabs.org](https://www.crosslabs.org/blog/diffusion-with-offset-noise))

🔴 **This is the BadCode register's structural enemy** — near-black with one thin light is
exactly what the model's training pulls against. Nobody outside has tested it for our register;
the settling test is a histogram, not a vibe.

### Two more lighting levers

**Numeric key:fill ratios are usable prompt vocabulary**, a lexical tier below named setups —
*"2:1 exposure ratio, shallow depth of field, realistic lens flares, soft analog bloom"*, with
2:1 or 4:1 for *"a balance of shadow detail and contrast"* and tighter ratios pushed toward
near-black. The underlying ASC convention is a real film-industry standard regardless of AI
leverage. (corroborated — five shown generated images tied to numbered prompts,
[blog.designhero.tv](https://blog.designhero.tv/veo-3-flow-cinematic-realism-midjourney/))

**Two opposing colour temperatures in one frame plus a single continuous move reads as
production value inside 8 seconds** — *"Slow dolly-in on a lighthouse keeper reading by lamplight
as a storm builds outside the window, warm interior light against cold blue dusk, rain against
glass, distant thunder"*. The pattern is generic cinematography craft; the source's own output
claim is a vendor thumbnail and is not evidence. (content-mill,
[videogen.io](https://videogen.io/veo-3-prompts))

## Film stock, grain, grade

Composable into one dense trailing clause. Terms that land: "shot on 35mm film",
"anamorphic lens", "fine film grain", "halation", "gate weave", named stocks ("Kodak
Portra 400"), "teal-and-orange", "desaturated", "sepia", "muted teal tones".

> "Shot on 35mm anamorphic with shallow depth of field, oval bokeh from background
> lights, fine film grain, and subtle halation around the brightest highlights. Calm,
> intimate, slow-cinema mood."
> "Teal-and-orange cinema grade: warm orange skin tones against deep teal-blue shadows,
> high but smooth contrast, rolled-off highlights, anamorphic 35mm, subtle blue lens
> flare, fine grain."

**Anamorphic is two independent optical traits, so name both.** Oval bokeh comes from the
lens's oval entrance pupil; the blue horizontal streak flare comes from cylindrical-element
coatings. Ask for "anamorphic" alone and the model may deliver one and drop the other — write
*"oval bokeh from background lights"* and *"subtle blue lens flare"* explicitly when both are
wanted. Real optics, independently documented in mainstream cinematography literature, not an
AI-behaviour claim. (corroborated,
[diyphotography.net](https://www.diyphotography.net/this-is-why-anamorphic-lenses-have-oval-bokeh-its-nothing-to-do-with-the-aperture/))

**Named stock vocabulary beyond Kodak Portra 400** — Kodak Vision3 500T (cool shadows, held
highlights), Fujifilm Eterna (muted, desaturated, low-contrast indie), *"CineStill 800T,
tungsten-balanced, visible halation around lights"* (the halation is stock-specific, not
generic), Technicolor three-strip (punchy saturated reds/cyans), *"Bleach bypass process, silver
retention, desaturated with crushed contrast"*. ⚠️ **Phrasing value only** — the stock-look
mappings are true photographically, but nothing tests whether Veo or Nano Banana differentiates
these names from generic "warm grainy film". (content-mill, no shown output,
[veo3ai.io](https://www.veo3ai.io/blog/veo-3-cinematic-film-look-color-grading-2026))

### The one-line Style Bible

Lock a single dense descriptor once per project — light direction, palette, contrast character,
grain and halation in one clause — and paste it **verbatim** into every prompt:

> *"soft north-light rim; muted earth tones; low-contrast filmic; subtle halation; fine grain"*

Same discipline as the character DNA block ([`consistency.md`](./consistency.md) §4), applied to
the grade. ⚠️ Source unreadable (403), snippet only — the template is harmless, the attribution
is weak. (practitioner, snippet-only,
[wimarys.com](https://www.wimarys.com/lighting-colour-in-google-veo-palette-control-grade-intent-consistency/))

⚠️ Teal-and-orange is the *opposite* of the BadCode comic register, which calls for
muted cool-neutral and bans movie-poster grading. Quoted here as vocabulary, not as a
recommendation.

## Camera hardware as a style token — low confidence

Naming hardware ("GoPro", "Fujifilm", "cheap disposable camera", "shot on iPhone,
handheld", "Arri Alexa Mini") is widely recommended as shorthand for an optical
signature. It is **documented by Google for the image side** — the Nano Banana guide
explicitly lists GoPro / Fujifilm / disposable camera as style levers — and is **absent
from Google's Veo guide**, which teaches descriptive technique language instead.
**One weak video-side data point now exists, and it says the rig name was not the variable.**
In a fixed cross-model run, *"Cinematic tracking shot through a rain-soaked Tokyo alley at
night… The camera glides forward slowly, revealing layers of depth — hanging lanterns, dripping
pipes, distant city glow. Shot on ARRI Alexa with Panavision C-series anamorphic lenses."*
executed the glide correctly at the start and then ran out of budget — *"Beautiful composition
and lighting, but 8 seconds isn't enough for a proper tracking shot. Camera shows the beginning
of the alley but doesn't reveal the depth."* **The bottleneck was the 8-second cap, not the
hardware token.** It neither helped nor hurt. (single-source,
[clipia.ai](https://clipia.ai/en/blog/seedance-2-vs-kling-3-vs-veo-3))

**Use it for stills. On video, describe the signature itself** ("fisheye distortion,
blown highlights, on-camera flash, handheld urgency") rather than trusting a brand name
to carry it.

## When words cannot get the move: hand Veo the motion itself

Google's own production account of **ANCESTRA** describes building a *reference video* of the
exact motion — a virtual 3D body model moved through the intended trajectory, or existing
footage of the target motion — and having Veo *"track the draft shot's motion and generate new
videos using that same movement,"* with the text prompt specifying **content only, never the
move**. A second sequence used *"reference videos of this motion"* to match organic movement
that would have been *"complex and time-intensive"* via traditional CGI. Described as shipped in
the released film, not as a demo.

**This is the most literal answer to "exact camera movement" the research found**, and it is
official. 🔴 Whether it is reachable from the Flow app — as opposed to the research pipeline
Google gave that production — is entirely unknown and worth one live check.

*(official, [blog.google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/ancestra-behind-the-scenes/))*

## Simplicity is the technique

Single-subject, single-move shots outperform crowded ones. Complexity yields weirdness.
When a shot isn't landing, the fix that works most often is **removing** a camera-movement
or lighting clause, not adding one.

---

## Sources

Read at source on **2026-08-18**. Every term in "The official catalogue" is quoted from the
first of these; the reliability tiers, the rules and the BadCode notes are ours.

- [Video generation prompt guide — Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) — camera angles, camera movements, lens and optical effects, lighting, tone, artistic style, ambiance, temporal elements, cinematic terms.
- [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) — the shorter component list ("Camera positioning and motion", "Composition", "Focus and lens effects", "Ambiance") and its worked examples.
- [Image generation with Gemini — Gemini API](https://ai.google.dev/gemini-api/docs/image-generation) — the still-side camera guidance ("Control the camera: use photographic and cinematic language") and the camera-hardware style levers noted below.

The **camera-hardware-as-style-token** section stands as written: it is documented for the
image side and absent from every Veo page re-read in this pass. One weak video-side data point
was added on 2026-08-20 and it points the same way — the rig name was not the variable.

**Added by the 2026-08-20 ten-angle sweep:**

- [ANCESTRA behind the scenes — blog.google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/ancestra-behind-the-scenes/) *(official — reference-video motion transfer, and the "add object" compositing path in [`consistency.md`](./consistency.md))*
- [Kling vs Veo — Curious Refuge](https://curiousrefuge.com/blog/kling-vs-veo) *(named protocol, 5 tests — vocabulary does not port between models)*
- [Diffusion with offset noise — Crosslabs](https://www.crosslabs.org/blog/diffusion-with-offset-noise) *(the mechanism behind near-black rendering as muddy grey)*
- [Nano Banana Pro prompting guide — fal.ai](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide) *(prompts with shown outputs — the near-black recipe, the reasoned aperture)*
- Secondary, phrasing only: [lzyprompt.com](https://lzyprompt.com/blog/ai-video-camera-movement-prompts/) · [blog.designhero.tv](https://blog.designhero.tv/veo-3-flow-cinematic-realism-midjourney/) · [veo3ai.io](https://www.veo3ai.io/blog/veo-3-cinematic-film-look-color-grading-2026) · [clipia.ai](https://clipia.ai/en/blog/seedance-2-vs-kling-3-vs-veo-3)
