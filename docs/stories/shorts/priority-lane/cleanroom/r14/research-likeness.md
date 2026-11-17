# Why the invented minister keeps turning into the real ex-PM (and how to stop it)

Researched 2026-11-17 for Priority Lane round 12. Inputs: `jack.md`, `evidence-r9-minister-prompts.json`,
`evidence-r11-prompts.json`, the reference BM9-b and the round 11 outputs PS11-b, PS11-c, PS11-d.
The real person is called "the real ex-PM" throughout.

## What we saw

- **BM9-b (the reference)** is an invented man who is already close to the real ex-PM: white-blond
  tangled mop, fat, navy chalk-stripe, club tie. What makes him *not* the real ex-PM is all in the
  face: he looks about 60, a long fleshy hooked nose with red veins, heavy-lidded narrow eyes,
  freckled blotchy skin, a sly half-smile.
- **PS11-b, c, d (the posters)** keep none of that. The poster faces are younger and smoother,
  with a short nose, round cheeks and a wide grin: the real ex-PM's press-photo face. It is
  strongest on the clean head-and-shoulders studio portrait (PS11-b) and the hard hat, hi-vis and
  thumbs-up shot (PS11-c).
- The poster face is tiny. In all three it is roughly 5 to 8% of the frame height, about 60 to 90
  pixels on a 1376-pixel-tall image.
- Side note (unverified): judged by content, the file PS11-b matches the prompt with id PS11-a
  (head-and-shoulders), PS11-c matches PS11-b (hard hat) and PS11-d matches PS11-c (nurse
  handshake). Check the naming before you log picks against prompts.

## What's causing it

How it works in general: image models do not need the name. A famous face is stored as the place
where many cues overlap (hair, build, nationality, job, typical clothes, typical photo, slogans), and
once enough of those cues are stacked the output "snaps" to that identity instead of blending
([identity basins paper](https://arxiv.org/html/2602.18533v1): with no name and no photos, adding
one hair-colour anchor raised the hit rate on a famous face from about 8% to about 60%. This is one
unreviewed preprint on SD 1.5, so the numbers are only indicative). Benchmarks of celebrity
"erasure" make the same point: a one-sentence description with no name is enough for people
*and* models to land on the celebrity ([EMMA benchmark](https://arxiv.org/pdf/2512.17320)).
Google's own developer forum reports Gemini faces drifting to famous people even from generic
prompts ([forum thread](https://discuss.ai.google.dev/t/my-ai-generated-image-looks-like-jennifer-lawrence/113914)).
Our prompts stack almost every cue this person has.

| # | Cue in our prompts | Why it pulls to the real ex-PM | Confidence |
|---|---|---|---|
| 1 | **The face is tiny inside a poster.** The attached reference cannot steer a 70-pixel face, so the model fills it from its strongest prior for "this kind of man on this kind of poster". | Reference-identity methods carry fine facial detail, and small renders have little room for it. No study tests Nano Banana on small faces, so this is an inference from the outputs and the face-identity literature ([FlashFace, via search summary](https://arxiv.org/pdf/2403.17008); [InstantID](https://arxiv.org/pdf/2401.07519)). The BM9 car shots, where the face is large, kept the invented face. | **Strong** (from what we saw); mechanism **likely** |
| 2 | **White-blond / straw-blond / platinum "mop", "shock", "flops over his brow", "unbrushed"** (r9) | Hair colour is the single strongest anchor in the identity-basin study, and this hair is the real ex-PM's trademark. It is the director's must-keep, so it has to be offset by other cues, not removed. | **Strong** |
| 3 | **"Campaign photo" + "SAVE OUR NHS" + a "bus" shelter** | The real ex-PM's best-known image is the 2016 referendum bus: "We send the EU £350 million a week, let's fund our NHS instead" ([Vote Leave bus](https://en.wikipedia.org/wiki/Vote_Leave_bus)). The prompt puts NHS, a political campaign and the word "bus" in one image. Our test does not separate the slogan from the other cues. | **Likely** for NHS + campaign together; the word "bus" alone is a **guess** |
| 4 | **Hard hat + orange hi-vis + thumbs up** (PS11 prompt b) | His builder's photo-op habit was widely mocked ([Spinoff on hard hats](https://thespinoff.co.nz/politics/25-03-2026/hard-hats-the-ultimate-accessory-for-the-plan-challenged-politician); hi-vis photo-op coverage). Other leaders use it too, but blond hair + UK + hi-vis narrows it to him. PS11-c is one of the strongest likenesses. | **Strong** |
| 5 | **"Glossy campaign photograph, head and shoulders, beaming into the lens", navy suit, plain backdrop** (PS11 prompt a) | This is the format of an official portrait, the most common photo of any PM in training data, so a generic prompt lands on the most-photographed man who fits. | **Likely** |
| 6 | **"Not a different politician" / "recognisably the same man"** | It puts "politician" back into a poster prompt that otherwise named no job, and naming what you don't want tends to invite it, because image models handle "not X" poorly (general prompting knowledge, not tested here). | **Guess**, unverified |
| 7 | **"English politician / minister", "upper-class", "posh", "old-school / club tie", "London", chauffeur car** (r9) | Each cue is weak on its own, but they narrow the space to British Conservative politicians, where the blond hair leaves one candidate. These shaped BM9-b itself, which is why the reference is already a near-lookalike. | **Likely** (stacking); any single word is a **guess** |
| 8 | **Pointing straight at the viewer** (PS11 prompt d) | The pose reads as a recruiting poster, not specifically this man. | **Guess**, weak |
| 9 | **Handshake with a nurse in a navy NHS uniform** (PS11 prompt c) | The real ex-PM had well-photographed hospital visits, but so has every PM. Most of its pull comes from cue 3 (NHS). | **Guess** |
| 10 | **The reference itself is a near-lookalike** | Pushed slightly, BM9-b falls into the basin: the paper describes identities with "sharp boundaries" that outputs snap into. The invented man's distinguishing features (hooked veined nose, age, narrow eyes, freckles) are exactly what gets lost at small size. | **Likely** |

A word that is **not** a trigger to add: the real ex-PM's own NHS slogans were "Stay home, Protect
the NHS, Save lives" (COVID) and the bus line above. "Save our NHS" is a generic union and
campaigner chant and not his, so the slogan itself is probably not the main problem (**likely**,
not tested). Variants that use **"protect"**, **"fund our NHS"**, **"£350 million"**, **"take back
control"**, **"get it done"** or **"build back better"** would make the likeness worse.

## How to fix it: rules for the prompt writer

1. **Make the face big. This is the main fix.** Make the poster in two steps:
   - **Step A: the poster artwork alone**, full frame, a 9:16 or 4:5 portrait, with BM9-b attached
     and his face at least a third of the image height. Check that it is still him. Pick it.
   - **Step B: the street shot**, with the picked poster image attached as the reference ("the
     printed advert from the reference image, reproduced exactly, in the shelter's lit panel").
     The model then copies a flat picture into a panel instead of inventing a face.

   Unverified that Flow keeps a poster exact in step B, but the advice to reference a clean,
   sharp image and let it carry the subject is the standard Nano Banana guidance
   ([Runware NB2 guide](https://runware.ai/docs/models/google-nano-banana-2/guides/character-consistency.md)).
   If you must do it in one shot, bring the camera close so the panel fills most of the window and
   the face is at least ~20% of frame height (a guess at the threshold).
2. **Use one reference, cropped to the face.** Crop BM9-b to head and shoulders so the face fills
   ~40-50% of the reference (one blog suggests 30-50%; not official). Use no second reference of a
   different man. Refer to him only as "the man in the reference image".
3. **Remove every job and nationality word from the poster prompt.** No politician, minister,
   campaign, English, British, posh, upper-class, Conservative, party, election. Call it "a
   health-service advert" or "a public notice poster". The satire comes from the ambulance and
   the car scene around it, not from the poster saying "politician".
4. **Remove the photo-op props and poses.** No hard hat, hi-vis, thumbs up or handshake with a
   nurse, and no beaming studio head-and-shoulders on a plain backdrop. Prefer a pose the real
   ex-PM is not famous for, or BM9-b's own sly sideways half-smile. Examples: hands clasped
   solemnly, a hand on heart, a slow nod. The satire comes from the sincerity of the poster
   against the ambulance stuck behind his car.
5. **Restate the features that make him not the real ex-PM.** This is the push-pull idea from the
   identity-basin paper: pull toward the target face and away from the famous one. Write BM9-b's
   distinguishing features into the poster prompt: about sixty, a long fleshy hooked nose with red
   veins, heavy-lidded narrow eyes, freckled blotchy skin, a sly half-smile. Standard guidance says
   to let the reference carry the face, but here the reference is losing, so this is a deliberate
   departure. If the house rule is "never describe a referenced character", break it here and say
   so. Optionally add one bold feature the real ex-PM never has: reading glasses on a cord, a clipped
   grey moustache or a bow tie. The forum advice (specific imperfections take a face away from a
   celebrity) supports this, but the bold-feature idea is a **guess**.
6. **Keep the hair, but don't make it the headline.** Leave the blond hair to the reference and
   don't describe it in the poster prompt. If you describe it, use words his press doesn't:
   "greying sandy-blond, thinning at the crown, combed but escaping", not "mop", "shock",
   "flops", "unbrushed", "white-blond". Rule 6 is a **guess**; test it in the same round as rules
   1-5.
7. **Don't write "not a different politician" or any "not X".** Say what you want ("his own face
   from the reference: the hooked nose, the narrow eyes"), never what you don't.
8. **Change the street furniture name.** Say "a lit advertising panel on the pavement" or "a
   roadside billboard" instead of "bus shelter". This one is a **guess**: it removes the token "bus"
   next to "NHS" and costs nothing.
9. **Clean room:** write the new poster prompts from this file and the director's notes, not from
   the r9 or r11 prompts. Every r9 prompt has the "English politician/minister + blond mop" stack
   in it.

## The slogan

- **Keep "SAVE OUR NHS"**. On the evidence it is not his slogan (**likely**). The pull comes from
  NHS + campaign + blond + bus together.
- If a test with rules 1-8 still lands on him, the fallbacks that keep the joke (a man who
  blocks an ambulance while selling himself as the NHS's saviour) are:
  - "YOUR NHS IS SAFE WITH ME", the most pointed, with the hypocrisy in the "me".
  - "I ♥ THE NHS", the cheapest and the funniest under the strobe.
  - "PUTTING PATIENTS FIRST", which turns into the punchline.
  - "SAVE OUR NHS" kept, with a small tagline underneath ("Vote for me") so the joke points at
    vanity, not at a real campaign.

  Avoid "protect", "fund", "£350m", "take back control", "get it done" and "build back better",
  which are all the real ex-PM's or his government's.

## Sources

- Morphological Addressing of Identity Basins (preprint, 2026): https://arxiv.org/html/2602.18533v1
- EMMA concept-erasure benchmark (describing a celebrity without the name): https://arxiv.org/pdf/2512.17320
- Google AI developer forum, Gemini faces resembling a celebrity: https://discuss.ai.google.dev/t/my-ai-generated-image-looks-like-jennifer-lawrence/113914
- Runware, Nano Banana 2 character consistency: https://runware.ai/docs/models/google-nano-banana-2/guides/character-consistency.md
- Face-size advice (30-50% of the reference), vendor blog, unverified: https://blog.laozhang.ai/en/posts/nano-banana-pro-face-consistency-guide
- FlashFace (face detail is lost when identity is squeezed into one token): https://arxiv.org/pdf/2403.17008
- InstantID: https://arxiv.org/pdf/2401.07519
- Vote Leave bus (the NHS slogan): https://en.wikipedia.org/wiki/Vote_Leave_bus
- Hard hats and hi-vis as political photo-ops: https://thespinoff.co.nz/politics/25-03-2026/hard-hats-the-ultimate-accessory-for-the-plan-challenged-politician
