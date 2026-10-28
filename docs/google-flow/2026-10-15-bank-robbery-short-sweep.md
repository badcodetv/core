# The Bank Robbery short sweep — 2026-10-15

Web pass run before the new stills and clips for the 74-second short
([`docs/stories/bank-robbery/short.md`](../stories/bank-robbery/short.md)): a Dunkirk beach in a 1990s war-film look,
the same picture as an oil painting on a café wall (the match-cut pull-out), café talk between Barry and Denise, a
printing press printing money, an estate agent's window, a jar of chocolate bars with a price label, Denise at the
sink, and the protest at dusk. It reports only what the
[10-08](./2026-10-08-anti-slop-sweep.md), [10-09 dialogue](./2026-10-09-dialogue-and-morph-sweep.md),
[10-09 crowd](./2026-10-09-crowd-vault-accent-sweep.md) and [10-12](./2026-10-12-shouting-faces-sweep.md) sweeps,
the README's shot table and the two model files do not already hold.

**Nothing here was tested by us.** Every item is reading, or my inference from reading plus our own records.
Pages were read through a summarising fetch tool, so re-open a page before ruling on its exact wording.

**Headline:** there is no Flow, Omni or Nano Banana change since the 10-09 sweep, and no source tests a war scene,
a painting on a wall, a printing press or a handwritten price label on these models. The useful new material is
(a) what the Saving Private Ryan look actually is, in words a prompt can carry, (b) Google's own wording for style
transfer and style transitions, and (c) two match-cut and clip-join rules. Most of the per-shot tactics in §3 are
my inferences, and are marked so. **Our installed Premiere effects can do the parts of the war look that Omni is
worst at** (shake, staccato, grain), which matters more than anything found online.

**Tiers:** **VERIFIED-PRIMARY** is a Google page fetched today. **HOST** is a model host's own doc.
**PRACTITIONER** is a named non-Google source; most sell a tool and show no method. **UNVERIFIED** is my
inference, a search summary only, or a different model.

## Use in prompts (short list)

Stills (Nano Banana):

1. **Describe the war-film look, do not name the film or the game.** Drained colour from a bleach-bypass print,
   hard grain, every droplet and grain of sand frozen sharp, water drops on the lens, the camera at the
   waterline. (§1)
2. **Make the painting from the accepted battle still**, as a fresh generation with that still as the only
   reference: "Recreate the exact content of the attached image as an oil painting on canvas", then name the
   physical paint (thick strokes, canvas weave in the thin parts, a varnish sheen). (§2)
3. **Put the painting on the café wall in Premiere, not in Nano Banana.** Corner-pin our full-size painting
   onto the frame in the café still. The model's own copy of the painting will not match, and at Flow's output
   size a painting a quarter of the frame wide is about 350 pixels across. (§2)
4. **Give every short text its exact words in quotes, its lettering and its place, and the currency.**
   "10p" handwritten in black marker on a torn white card, propped against the jar. Prices default to dollars
   unless pounds are named (our 10-07 observation). (§3.6)
5. **Give a count and a place for repeated objects**: "six price cards in two rows of three". A count with a
   place is a layout; "some cards" is a suggestion. (§4)
6. **Do not name the chocolate brand.** Naming a marque renders its badging (`nano-banana-2.md` §34). Describe
   small purple-wrapped bars. (§3.6)

Video (Omni 1.1 Flash):

1. **Do not ask Omni for handheld chaos. Lock the camera and put the chaos in the subject**; add the shake
   (`Camera Shake`), the staccato (`Posterize Time`) and the grain (`Noise`, about 4) in Premiere. (§1)
2. **For a narrow-shutter feel, say what is sharp, not "low shutter"**: "each splash and spray of sand is
   sharp in every frame, no motion blur, normal speed". "Low shutter speed" means a long exposure. (§1)
3. **The push-in and the pull-out are Premiere moves on stills**, as the hybrid method already says. (§2)
4. **Trim the last half-second of every clip you join to another**: generators slow the camera and the subject
   towards the end, which shows as a hitch at the cut. (§2)
5. **Printing press: show a continuous paper ribbon, not loose sheets**, already running in the first frame,
   with the rollers soft or cropped. (§3.4)
6. **Price cards flipping to double, the 10p becoming 20p and the rent figure are post jobs.** Generate the
   picture once with blank or fixed cards and change the numbers in ffmpeg. (§3.5, §3.6)

## 1. The war-film look, in words

What the look is made of, from the film's own accounts:

- **PRACTITIONER** Janusz Kamiński shot the landing with the shutter narrowed (45 or 90 degrees against the
  usual 180), so flying sand, water and debris are sharp separate particles; handheld, with water and sand on
  the lens; an "Image Shaker" vibrated the camera for explosions; the lenses had their coatings stripped to look
  older; and the print was desaturated (bleach bypass). His word for the result: a "staccato" in the movement.
  Several secondary sources agree; the exact 45 degree figure was not found in a primary source.
  <https://ymcinema.com/2023/12/05/the-25th-anniversary-of-spielbergs-saving-private-ryan-a-milestone-in-filmmaking/> ·
  <https://nofilmschool.com/saving-private-ryan-changed-war-movies> ·
  <https://www.ilm.com/vfx/saving-private-ryan/>
- **PRACTITIONER** (forum) Part of the jerky look was **step-printing** (repeating or dropping frames) in post,
  not the shutter alone. <https://www.dvinfo.net/forum/archive/index.php/t-12582.html>
- **PRACTITIONER** Melies glossary (2026, undated, no model named): working wording "short shutter angle,
  reduced motion blur, crisp rain and limb edges, staccato cadence"; for video "sharply segmented body movement,
  no smooth slow motion, no artificial frame skipping". It warns **"low shutter speed" is photography's term for
  a long exposure** and summons blur. <https://melies.co/cinematic-techniques/time-and-motion/low-shutter>

What that means for us:

- **UNVERIFIED** This is the opposite of our only confirmed motion clause (`omni-flash.md`, "the shutter is the
  tell": a 180 degree shutter so fast things smear, `[confirmed 2026-08-14]`). That clause was for a falling
  phone. For the beach, ask for sharpness, but expect Omni to lean back to its default; Omni's default for fast
  action is slow, smooth motion (10-08 sweep §2.5). Say "normal speed" and give countable beats.
- **UNVERIFIED** The two things Omni is worst at, a shaking camera and a stuttering frame rate, are both
  **installed Premiere effects**: `Camera Shake` (`AE.Impact_Camera_Shake_FX`) and `Posterize Time`
  (`AE.ADBE Posterize Time`), plus `Noise` (`AE.ADBE Noise2`, 4 is a usable grain) and ffmpeg `framestep`
  ([`effects-catalogue.md`](../premiere/effects-catalogue.md), [`ffmpeg-catalogue.md`](../video-fx/ffmpeg-catalogue.md)).
  The drained colour is a grade. So the clip only has to supply men, water, sand and a locked camera. This fits
  the hybrid method and ruling R7 (handheld is a style choice, never a realism fix): here it is the style, and
  post does it exactly.
- **PRACTITIONER** Stacked camera instructions on Veo 3.1 blended into "a generalized forward drift"; aggressive
  camera moves near faces and hands raise warping. Veo, not Omni.
  <https://www.vidau.ai/free-ai-video-prompts-comparison-veo-3-1-vs-kling-3-0/>
- **PRACTITIONER** (glossary, not tested) "stabilized handheld" for little shake, "shaky handheld" for chaos.
  Not adopted; see above. <https://geminiomniprompts.org/glossary/>
- **UNVERIFIED** (search summary only; the article returned 404) Period scenes come out of film and game
  imagery more than period photographs, so details drift (wrong kit, modern boots). For us the film prior is the
  look we want, but name the kit: steel Brodie helmets, khaki wool battledress, rifles slung, a wooden open
  boat, a destroyer burning offshore. <https://digitalbiztalk.com/article/why-ai-generated-historical-content-looks-terrible-in-2026>
- **UNVERIFIED** Do not name *Saving Private Ryan* or *Call of Duty* in the box. Named titles pull in posters,
  logos and, for a game, a game render. Describe the capture instead (Hedra's "describe the capture" rule, 10-08
  sweep §2.2).
- **UNVERIFIED** Colour: the README's rule 2 (name saturated colours, "muted" and "grey" made cut 7 grey) is
  right for the café and wrong for the beach. The beach is meant to be drained, and the café's colour after it is
  the contrast. Keep one warm thing alive in the beach (a burning ship's orange, a lifejacket) so it does not read
  as a broken file (see `docs/cinematography/` on lightness anchoring).
- **Not found:** anything on whether Flow blocks a 1940s battle. Our record: street disorder passed in stills;
  a gun pointed at a person was refused as video. Keep rifles slung or pointed at the sky, and no wounds; "a
  soldier dragging a mate" reads as exhausted and soaked, not injured. One forum thread reports harmless Omni
  edits refused within seconds, and (search summary only, UNVERIFIED) that Omni **editing of uploaded video is
  not offered in the UK**, which matches `docs/flow/platform-controls.md` finding it absent from our account.
  <https://discuss.ai.google.dev/t/omni-video-editing-instantly-rejects-harmless-prompts-in-flow-and-gemini-app/147152> ·
  <https://agentpedia.codes/blog/why-gemini-omni-flash-refuses-your-clips>

## 2. The painting and the match cut

- **VERIFIED-PRIMARY** Google's Nano Banana guide (2026-03-06): "Style transfer: Upload a photo and ask the model
  to recreate its exact content in a different artistic style, such as transforming a photo of a modern city
  street into a Van Gogh-style painting." <https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana>
  - Our own record agrees: restyling our accepted still with one reference held face, pose and set
    (`nano-banana-2.md` §39, n=2). This is a fresh generation with a reference, not an image edit, so it fits the
    standing never-edit rule.
- **PRACTITIONER** Physical-paint wording from the painting-prompt guides (no model named, no test shown):
  "thick visible brushstrokes, palette knife texture", "canvas grain showing through thin passages", describe how
  light falls across the paint surface. One reason given for a fake look: everything evenly smooth and over-
  saturated. <https://zsky.ai/blog/ai-painting-prompts-guide.html> ·
  <https://www.goenhance.ai/prompts/image-prompts/impasto-oil-painting-portrait-style>
  - **UNVERIFIED** For a café-wall painting, ask for an ordinary painting: an amateur or souvenir-shop oil, a
    little clumsy, slightly yellowed varnish, in a cheap gold-painted moulded frame. A museum masterpiece is the
    polished register we keep getting called slop for.
- **VERIFIED-PRIMARY** DeepMind's Omni prompt guide shows **style transitions inside one clip**: "Transition
  seamlessly into a graphite pencil sketch on textured paper", "Conclude the sequence with a tactile risograph
  print look". It also says first-and-last-frame generation suits "zoom transitions".
  <https://deepmind.google/models/gemini-omni/prompt-guide/>
  - **UNVERIFIED** Not recommended as the main route. A clip that turns into a painting is asking Omni to *reach*
    a state (README table), and a pull-back invents new picture on all four edges (`omni-flash.md`, "pull-back is
    structurally riskier"). Pinning the café still as an end frame breaks our never-pin-an-end-frame rule. Worth
    one test clip at most.
- **PRACTITIONER** invideo (2026-10-08) on AI match cuts: keep the shared thing at the same centre, apparent
  size and angle in both shots; keep camera movement minimal so the shapes can be compared at the cut; judge the
  outgoing and incoming frames side by side. <https://invideo.io/blog/how-to-create-match-cut-videos-with-ai/>
  - Restyling the same still gives this for free: the soldier's face is in the same place in both.
- **PRACTITIONER** HackerNoon (2026-09-16, one project, no measurement): "Most generators ease the camera and the
  subject toward stillness in the last handful of frames", which reads as a hitch at a cut. Fix: trim the tail,
  and take any chained start frame from before the slow-down.
  <https://hackernoon.com/how-to-chain-ai-video-clips-into-one-shot-without-the-hidden-stutter-at-every-cut>

**UNVERIFIED** The build this suggests, every step exact:

1. Battle still (Nano Banana) → battle clip (Omni, camera locked) → shake, staccato, grain and grade in post.
2. Painting still: the accepted battle still restyled as an oil painting, full frame, same aspect.
3. Café still: Barry and Denise under an **empty cheap frame on the wall**, or any painting the model draws
   there; it will be covered.
4. Premiere: Corner Pin the full-size painting still into the frame on the café still. Push in on the battle
   clip's soldier, dissolve or cut to the painting still at the same face size and place, then scale the whole
   composite out to reveal the café. The painting layer is full resolution, so the start of the pull-out is sharp.
   The battle audio cuts to café clatter on the reveal.

## 3. Per shot

### 3.1 Dunkirk still and clip

See §1. **UNVERIFIED** For the clip: the first frame already shows the spray and the sand in the air (a fire
plate on Frames came back with nothing happening, `omni-flash.md` 2026-09-16; continue a state, do not reach one).
One mover: the soldier dragging his mate towards the boat. The dive bomber is best left to the sound and, at most,
a shape crossing the top edge; an aircraft crossing the whole frame is a "whole fall" shot (`omni-flash.md`).

### 3.2 The painting

See §2.

### 3.3 Café interiors (Barry and Denise)

Nothing new beyond the rules we hold (one speaker a clip in Ingredients with the Character attached; Barry is
not a Flow Character yet, so a line from him wants his back to the lens or a Character made first). Two reminders
from the sweeps: **say what is on the walls** (the painting, a menu board with its quoted words, a calendar),
because unspecified signage is filled with generic lettering; and the brief says no flags, so do not write the
word at all, even as "no flags" (§27, ask for an object not an absence). The television showing a small boat:
no readable text on it (10-14 observation: a still that looks like real news is refused as video).

### 3.4 The printing press

- **Not found:** any test of a printing press, rollers or gears on any video model.
- **PRACTITIONER** A real-or-AI vehicle quiz: generated wheels "rotate inconsistently, wobble or change spoke
  pattern". <https://whichoneisreal.com/guides/ai-vehicle-video-quiz/> **PRACTITIONER (academic)** GeCo
  (arXiv 2512.22274): models add motion to things that should be rigid. <https://arxiv.org/pdf/2512.22274>
- **UNVERIFIED** readings, from these and our own record:
  - Our §38 counter-example: a treadmill belt smeared and moved correctly, discrete objects (doors, banknotes)
    stopped. So prefer a **web-fed press**: one continuous ribbon of printed paper running over the rollers and
    into a cutter, with a stack of cut sheets growing. Loose sheets flying out one by one is the hard version.
  - The still shows the press already running: the ribbon taut, a stack already tall. The clip continues it.
  - Keep the roller ends and any spoked wheels out of frame or soft; spinning spokes are a named tell.
  - Do not show a banknote face (10-09 sweep): sheets seen edge-on or from low, the print too small to read,
    and the currency named in the clip prompt (a vague note became a US dollar bill once; naming the currency
    held, n=35, `omni-flash.md`).
  - **Not found:** any statement on whether Nano Banana or Omni refuses printing banknotes. Our "shrink-wrapped
    blocks of paper" pallets passed 39 of 39.

### 3.5 Estate agent's window

- **UNVERIFIED** Generate the window once with the cards in place and the prices either large and quoted, or
  blank white cards to be filled in post. "Every card flips to double" is a mechanical change of state plus small
  text changing between frames, the two things Omni is worst at; do the flip as two stills or as ffmpeg text.
- **UNVERIFIED** Invent and quote the agent's name, or show none. A generic "estate agent" may summon a real
  brand, as "tabloid newspaper" summoned a real masthead (2026-10-08 observation).
- **PRACTITIONER** Shop-window reflections of people break down in clips (OpusClip tells, 10-08 sweep). Keep
  passers-by out of the reflection; the Donor walking out is best as a separate shot from inside the doorway.

### 3.6 The chocolate jar and its label

- **HOST** Runware, Nano Banana 2.1 prompting (2026-10-06): pair each object with a count and a region;
  "Exactly three bowls in a row across the middle" is a layout, "Some bowls on a table" is a suggestion.
  <https://runware.ai/docs/models/google-nano-banana-2-1/guides/prompting>
- **PRACTITIONER** Fuser, tested on 2.1 (2026-10-06, one output each): quoted strings came back exact; describe
  the lettering ("hand-lettered white chalk capitals") rather than naming a font, and say where each text sits.
  <https://fuser.studio/articles/nano-banana-prompt-guide>
- **UNVERIFIED** readings: `"10p"` in quotes, "written by hand in thick black marker on a torn piece of white
  card, taped to the front of the jar, the card as wide as the jar's lid" (big text; the model card names small
  text as the weak point). The bars: "small purple-wrapped chocolate bars", no brand. For the 20p shot, **reuse
  the same still and change the label in post**, so the jar is identical in both and the payoff reads.

### 3.7 Denise at the sink

Nothing new found. Our fluids note holds (`omni-flash.md`: fluids fail two named ways; put the hard half outside
the clip). **UNVERIFIED**: hands already in the water with one plate in contact in the first frame; the tap running
in a thin steady stream rather than splashing; the rent letter lying open on the side, figure unreadable, with
the doubled number composited in post if it must read.

### 3.8 The protest at dusk, flares

Nothing new found; the 10-09 and 10-12 sweeps hold the evidence. Reminders from our own record: "WE CAN'T AFFORD
TO LIVE HERE" came back spelt right at 1K when large; flares and burning bins were not blocked; a prompt noun can
leak onto a sign, so say what each sign reads.

## 4. Engine news since the 10-09 sweep

- **VERIFIED-PRIMARY** Gemini API changelog, fetched today: entries on 10-08 and 10-13 are text models (Gemini 4
  Argon GA, Flash deprecations). **No image or video entry since Nano Banana 2.1 on 10-06**, and no Omni entry since
  1.1 Flash on 08-27. <https://ai.google.dev/gemini-api/docs/changelog>
- **VERIFIED-PRIMARY** Flow help (answer 16894016) still says "By default, Google Flow sets the model to Nano
  Banana Pro" and does not mention 2.1; the credits page still lists no image model cost. The picker question in
  the 10-09 sweep §5 (is "Nano Banana 2" still there, and is it free) is **still open: read the picker.**
  <https://support.google.com/flow/answer/16894016?hl=en> · <https://support.google.com/flow/answer/16526234?hl=en>
- **HOST** Runware's 2.1 guide says exclusions go in a closing clause "Negative prompt:" listing nouns, not
  sentences. This is their API surface. It conflicts with our §27 (ask for an object, never an absence) and is not
  adopted for Flow.
- **Not found:** any Flow release note or blog.google post for September or October 2026 (one October article
  only republishes the 08-27 post).

## 5. Contradicts the repo

| # | Repo says | Source says | Tier | Proposed handling |
| --- | --- | --- | --- | --- |
| 1 | `omni-flash.md`: ask for a 180 degree shutter so fast things smear (confirmed on a falling phone) | The war-film look is a narrow shutter: every particle sharp | PRACTITIONER | Not a contradiction of the finding, a different goal. Use "sharp in every frame" for the beach only; untested on Omni |
| 2 | README rule 2: name saturated colours; "muted" made cut 7 grey | The look asked for is drained | (brief) | The beach is drained on purpose; keep one warm object; the café carries the colour |
| 3 | Never pin an end frame | DeepMind: first and last frames suit "zoom transitions" | VERIFIED-PRIMARY | No change; already noted in `omni-flash.md`. Do the zoom in Premiere |
| 4 | R7: handheld rejected as a realism fix | Practitioners use handheld for war scenes | PRACTITIONER | Compatible: here handheld is the style, and Premiere adds it exactly |

## 6. Cheap tests this suggests (none run)

1. Beach clip, same still: "each splash sharp in every frame, no motion blur, normal speed" against no shutter
   words. Watch at four frames a second.
2. Painting restyle: amateur café oil against museum oil, two candidates each, same reference.
3. Printing press: web-fed ribbon against sheet-fed sheets, same room, two clips each.
4. One Omni clip of the battle still with "transition seamlessly into a thick oil painting on canvas", only to see
   whether the composition holds; the Premiere route stays the plan.
