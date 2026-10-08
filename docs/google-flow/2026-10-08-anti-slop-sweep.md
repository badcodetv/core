# Anti-slop sweep — 2026-10-08

Web pass run because the director called the current stills and clips "AI slop". Three questions:
what reads as slop, how to prompt Nano Banana for photoreal stills, how to prompt Omni 1.1 Flash
from a start frame and from Ingredients. **Nothing here was tested by us.** Every item is reading.

Read first, so that only the delta is reported: `docs/flow/` (indexes and section headings),
`nano-banana-2.md` (prompt structure, anti-slop toolkit, passes 15 to 17 and the October notes),
`omni-flash.md` (confirmed table, length conflict, modes, passes from 2026-08-28 on),
`docs/cinematography/symptoms.md`.

## Tiers used in this file

- **VERIFIED-PRIMARY**: a Google page fetched today, quoted, with its URL. Fetches were read through
  a summarising tool, so quotes are as that tool returned them. Re-open the page before building a
  hard rule on exact wording.
- **PRACTITIONER**: a named non-Google source with URL. Most sell a competing tool.
- **UNVERIFIED**: inferred by me, seen only in a search summary, or measured on a different model.

## 1. Already in the repo (the sweep found these again, nothing to change)

- Slop is polish: too clean, too evenly lit, too symmetrical, too composed. Counter with a named
  capture, one positioned light, imperfection, off-centre framing, a foreground occluder.
- `photorealistic`, `cinematic`, `8K`, `masterpiece` are noise words.
- Describe the scene in sentences; positive framing ("empty street"); name materials; one camera.
- Quote sign text, describe the lettering, keep it large; small text garbles.
- Frames carries composition, Ingredients carries identity; describe each reference's job.
- One main action plus one small one; give motion its real speed; name force and consequence.
- Describe the audio or it is left to chance; "Single continuous shot, no scene cuts".
- 720p is native, 1080p and 4K are upscales. Timecoded beats are allowed.
- Texture tiling, hand contact points, floaty motion, text changing between frames, blink cadence.
- Handheld shake as a realism fix stays rejected (ruling R7).

## 2. New

### 2.1 Nano Banana 2.1 exists and Nano Banana 2 is deprecated in the API

`nano-banana-2.md` (2026-09-30) says "2.1" is unannounced. That is out of date.

- **VERIFIED-PRIMARY** Gemini API changelog, 2026-10-06: "Gemini Nano Banana 2.1 generally
  available (GA)", and "The `gemini-3.1-flash-image` model is deprecated (no shutdown date
  announced)." <https://ai.google.dev/gemini-api/docs/changelog>
- **VERIFIED-PRIMARY** Model page: "Improved visual quality and realism across `1K`, `2K`, and `4K`
  output resolutions", "Fixed tiling artifacts on wide and panoramic aspect ratios", "Enhanced text
  rendering and infographic layout accuracy", multi-turn character consistency for up to 4
  characters, up to 14 reference images, thinking levels minimal / medium (default) / high.
  <https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1>
- **VERIFIED-PRIMARY** DeepMind model card, published 6 October 2026, "based on Gemini 3.6 Flash".
  Limitations it lists: "Poor text rendering in small text (often blurry in 1k model), long
  paragraphs, page length"; "Character consistency is not always perfect between input images and
  generated output image"; "Occasional confusion around spatial localisation (e.g. left/right
  etc.)". Human preference Elo 1050 against 990 for Nano Banana 2 and 935 for Pro.
  <https://deepmind.google/models/model-cards/nano-banana-2-1/>
- **PRACTITIONER** It appeared in Flow's model picker on 2026-10-05, vanished, and came back on the
  6th; no 512px tier; reports say it costs credits in Flow.
  <https://apidog.com/blog/nano-banana-2-1/>
- **UNVERIFIED** Whether Jack's Flow picker shows 2.1, whether Flow's "Nano Banana 2" entry is now
  silently 2.1, and whether 2.1 is free in Flow. This matters because of the standing rule
  "always Nano Banana 2, it is free". **Look at the picker and the credit line before the next
  still.**
- **UNVERIFIED** Character count conflict: the model page says 4; the image-generation page's table
  appeared to say 5 for "2.1 and 3.1 Flash" but the table was flattened when read. Our own
  ceiling is four in one still, so no change either way.

What follows for prompts, all **UNVERIFIED** inferences from the model card:

- Small text is the stated weak point at 1K. A newspaper or a shop sign that must read wants 2K,
  short strings, and large lettering. Our round-3 banner result (ten words, large, correct at 1K;
  small shop signs garbled) fits this.
- Left/right is a stated weak point. Place things by a landmark in the frame ("nearest the lens",
  "by the door", "on the side where the window is") and keep "camera-left" for the light only.

### 2.2 Stills: what the 2026 photoreal guides add

- **PRACTITIONER** Hedra, 2026-06-20 (tested on GPT Image 2, not on Nano Banana):
  <https://www.hedra.com/blog/make-ai-images-look-like-real-photos-prompting>
  - "Describe the capture, not the beauty." Lead with camera, lens, light and flaws, and let the
    subject be ordinary. Subject plus quality words triggers "the glossy, plastic look".
  - **Half-committing to a camera look is its own tell**: "neither convincingly amateur nor cleanly
    pro, just off". Pick one capture and carry it through every clause.
  - **Golden-hour light is now an AI signature**: "every model reaches for it".
  - **Portra 400 and Cinestill 800T are over-prompted** and read as "trying to look like film".
    It suggests Kodak Gold 200, Ektachrome or Ilford HP5.
  - Humble gear: "a phone, a point-and-shoot, a Ricoh GR III, an old Canon AE-1". Studio rigs read
    as stock.
  - **Decorative signage the prompt does not specify gets filled with generic lettering.** Keep it
    out of frame, or say exactly what it reads.
  - People: an age range, a job, real skin texture, an in-between expression. Never describe what
    they are not.
  - "If the input looks like AI slop, the footage will too." The start frame sets the ceiling.
  - Working wordings from its examples: "harsh direct on-camera flash, bright hotspot on the faces,
    background falling into near-black, slight motion blur, framing a little tilted, ordinary
    everyday people, unposed"; "flat overcast daylight, no sun, muted cool color".
- **PRACTITIONER** fal, 2026-06-21: reasoning-based models gain less from quality boosters, which
  "crowd out concrete detail"; packing many instructions into one sentence makes the model drop
  some; "a street with no cars can still include cars"; 24mm stretches space, 85mm flatters a
  face. <https://fal.ai/learn/tools/how-to-generate-photorealistic-images-with-ai>
- **VERIFIED-PRIMARY** Google's photoreal template is short: "A photorealistic [type of shot] of a
  [subject description] in a [setting description]. [Description of the light]. Shot from a
  [camera angle] with a [lens type]." Text template: 'Create a [image type] for [brand/concept]
  with the text "[text to render]" in a [font style].' Advice: "Be clear about the text, the font
  style (descriptively), and the overall design."
  <https://ai.google.dev/gemini-api/docs/image-generation> (Google's own template uses the word
  "photorealistic", which our docs and every practitioner source call a noise word. We keep our
  rule; it has our own observations behind it.)
- **PRACTITIONER** Crowds: one sharp anchor figure, the rest motion-blurred or small, gives the
  model a focal hierarchy; avoid individual actions for many people. One vendor claims groups
  hold "up to 8 people". Marketing pages, not tests.
  <https://www.veed.io/learn/nano-banana-prompting-guide> ·
  <https://www.atlabs.ai/blog/nano-banana-2-prompting-guide>

### 2.3 Fire, smoke, rain, crowds: almost nothing new was found

- **UNVERIFIED** (search summary only, page not opened) A British Columbia wildfire analyst on fake
  fire photos: the fire behaviour shown would be "the most extreme … that's possible", and the
  images have a painterly, airbrushed orange. Reading for us: ask for a small, physically modest
  fire with one colour of flame and grey-brown smoke that leans one way, not a wall of orange.
  <https://cfjctoday.com/2025/08/05/bc-wildfire-service-warns-ai-photos-spread-misinformation-and-uncertainty/>
- No source found with tested guidance on smoke, rain or crowd realism for Nano Banana or Omni
  beyond what `omni-flash.md` (2026-09-30 rain pass) and `physics-and-motion.md` §6c already hold.
  Our own observations remain the best evidence we have.

### 2.4 Video: what viewers actually reject

- **PRACTITIONER (academic)** arXiv 2601.20297 (2026-01): viewers judge by the presence and
  severity of an artifact, not by average quality: "a video with large-scale warping is
  immediately dismissed". Its axes are Appearance (texture corruption, object deformation), Motion
  (flicker, motion discontinuities) and Camera (unstable trajectories, implausible parallax).
  <https://arxiv.org/html/2601.20297v1>
  Reading, **UNVERIFIED**: one warped second costs the whole shot, so trim to before it. A clean
  3.5 seconds beats 8 seconds with a morph at 6.
- **UNVERIFIED** (abstract via search summary) arXiv 2602.03374: once viewers suspect AI they stop
  watching and start hunting for anomalies. Reading: the first shots of a film matter most.
  <https://arxiv.org/abs/2602.03374>
- **PRACTITIONER** OpusClip's twelve tells, 2026-04-17. Not in our files as named tells:
  **background extras with broken legs or gait** ("generation attention goes to the subject"),
  **mirror and reflection breakdowns**, and **physics that changes between cuts** because each
  clip is generated alone. It calls hands, reflections and in-scene text "genuine limitations".
  <https://www.opus.pro/blog/ai-slop-aesthetic-12-tells>
  Reading, **UNVERIFIED**: keep walking extras out of the plate or below the knee line; keep
  mirrors and shop-window reflections of people out of clips; carry weather and wind direction in
  the same words across clips of one scene.
- **UNVERIFIED** (search summaries) Segmind's first-and-last-frame test on 1.1: small print "degrades
  into gibberish as soon as the lighting moves". RuntimeWire's head-to-head: "sponsor lettering
  mutates", small effects are "understated". Consistent with our comp-the-sign-in-post rule.

### 2.5 Video: prompt wording that is new to us

- **VERIFIED-PRIMARY** Gemini API Omni page, fetched today <https://ai.google.dev/gemini-api/docs/omni>:
  - "For best results with image-to-video, use high-resolution images and provide specific motion
    descriptions. Vague prompts like "make it move" produce less compelling results than detailed
    descriptions of the camera movement, subject motion, and environmental effects."
  - "If the generated video contains things you don't want, include simple negative prompts to
    avoid them": "No dialogue", "No embellishments", "No extra sound effects"; and "you can put
    your negatives in the regular prompt: e.g., "Do not do X"". The same page lists negative
    prompts (the parameter) as not supported.
  - "By default the model will try to generate an appropriate audio track … You can use your
    prompt to describe the type of audio you want."
  - "Simple prompts work best for video editing. Overly descriptive prompts can lead to unintended
    changes." and "Keep everything else the same".
  - Tag wordings: "Use this image as the starting frame."; for references, "Use the given image(s)
    as references for video generation. The images should not be used as literal initial frames."
  - "You can prompt to include text in your video and Gemini Omni will render in a way that is
    correct and readable." (The model card and every test above disagree for small text.)
- **VERIFIED-PRIMARY** Flow Help: "Your text prompt should complement, not contradict, your visual
    inputs."; for frames, "describe the action or transition that should happen between the
    frames"; "Make sure location and style references don't contain extra subjects"; "A consistent
    look and feel across all your ingredient images helps the model blend them more effectively."
  <https://support.google.com/flow/answer/16894016?hl=en>
- **PRACTITIONER** Runware, Omni 1.1 first and last frame guide:
  <https://runware.ai/docs/models/google-gemini-omni-flash-1-1/guides/first-and-last-frame>
  - "With one frame the model is free at the end, so the prompt has to carry the whole arc."
  - "Say what moves and in what order" and "say what holds still".
  - ""No camera movement" is worth writing explicitly"; without it "the model will otherwise add a
    drift".
- **PRACTITIONER** Morphic, Omni 1.1 guide (undated, "updated in August 2026"):
  <https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide>
  - **Timecode ranges are budgets, not edit points. An event trigger lands more precisely**:
    "When the person touches the mirror, it ripples like liquid."
  - Silence must be asked for: "No music, just room tone." Unspecified audio gets generic music.
  - Four or more tracked subjects "tend to merge or drift".
  - Undefined on-screen text gets invented. (Our dollar-bill and apron-lettering observations.)
  - Attach every reference before the first generation.
- **PRACTITIONER** Veo3Gen, 2026-06-18, written about Runway, so **UNVERIFIED on Omni**. The
  "slow-mo look" is missing speed cues, not frame rate. Wordings:
  <https://www.veo3gen.app/blog/runway-gen-4-slow-mo-complaints-veo3gen-11-motion-readability-fixes-when-your-cl>
  - Countable beats: "3 quick steps then stop; hold still for a beat."
  - Impulse and settle: "Push off hard, accelerate, then decelerate into a planted stance."
  - Micro-collisions: "Object taps the table, then stillness."
  - Build the cut points in: a clear start pose, one action beat, a clear end pose, an end hold.
  - Near objects passing fast and far ones slowly, for a sense of speed.
- **PRACTITIONER** The stated cause of default slow motion: slow motion changes fewer pixels a
  frame, so it is the model's safe option (vendor blog, one interpretation).
  <https://ltx.io/blog/how-to-fix-slow-motion-in-ai-generated-video>

## 3. Contradicts the repo

| # | Repo says | Source says | Tier | Proposed handling |
| --- | --- | --- | --- | --- |
| 1 | `omni-flash.md`: "Negatives do not work, and they actively backfire" (community source) | Google's Omni page recommends "simple negative prompts": "No dialogue", "No extra sound effects", "Do not do X" | VERIFIED-PRIMARY | Narrow our rule. Short negatives for **audio and embellishment** are vendor-endorsed. Piles of visual negations stay banned. Our own record is mixed: "No music" failed 4 of 32, a positive sentence fixed laughter |
| 2 | `nano-banana-2.md` toolkit: name a film stock, example `Kodak Portra 400` | Portra 400 and Cinestill 800T are over-prompted and read as trying to look like film; use Gold 200, Ektachrome, HP5 | PRACTITIONER, different model | Untested on Nano Banana. Cheap pair test: same prompt, Portra against Gold 200 |
| 3 | `nano-banana-2.md` 2026-09-30: "2.1 … still unannounced" | Nano Banana 2.1 is GA since 2026-10-06 and Nano Banana 2 is deprecated in the API | VERIFIED-PRIMARY | Update the file; check the Flow picker and the price |
| 4 | Standing rule: Nano Banana 2 because it is free | Reports that 2.1 uses credits in Flow | PRACTITIONER | Unverified. Read the credit line |
| 5 | Motion-only prompts on Frames; preservation lists rejected (2026-09-29) | Runware 1.1: "say what holds still"; write "No camera movement" | PRACTITIONER | Partly compatible with our narrow exception (one sentence on what may move). Our observed fixes of 2026-10-06 ("stands still on the step", "apron … stays plain") agree with Runware. Suggest: one hold-still sentence per clip is now practice, a list is still out |
| 6 | Google guide example "Golden hour backlighting" quoted in `nano-banana-2.md` | Golden hour is an AI signature | PRACTITIONER | Avoid golden hour unless the story needs it; prefer flat overcast, sodium street light, one tube |
| 7 | Timestamp prompting in `video-prompting.md` §5 | Timecodes are budgets; event triggers are more precise | PRACTITIONER | Prefer "when X, Y" for the second beat |
| 8 | `nano-banana-2.md` notes 512px as a cheap composition check | 2.1 has no 512px tier | PRACTITIONER | API-only point; Flow never exposed it |

## 4. Checked and not found

- No blog.google post for Nano Banana 2.1, and no Google prompting guide newer than the Cloud guide
  dated 2026-03-06, which does not mention 2.1.
- No Omni or Veo entry in the Gemini API changelog since Omni 1.1 Flash (2026-08-27). An "Omni 1.5"
  page exists on one reseller site as speculation only.
- No peer-reviewed study isolating which cues lay viewers use to call a video AI. Survey numbers
  disagree (83% say they can spot it, Animoto; 9.5% reliably can, Kapwing) and both come from tool
  vendors. Do not cite either.
- No tested guidance for crowds, smoke or fire from a start frame on Omni 1.1.
- Google's "Mastering Gemini Omni" guide (2026-05-26) was not reachable as a primary page; we hold
  it only through the Pillitteri summary already cited in `omni-flash.md`.

## 5. Cheap tests this suggests (none run)

1. Portra 400 against Kodak Gold 200 against no stock, same still prompt, two candidates each.
2. Nano Banana 2 against 2.1 (if the picker has it) on one crowd still and one newspaper still.
3. A clip with "No camera movement." against the same clip without it, same plate.
4. A clip whose second beat is an event trigger against the same clip with a timecode.
5. A clip ending "…then holds still" to see whether the back half stops drifting.
