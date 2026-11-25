# Automatic QA for Flow stills and clips (research, 2026-11-25)

The human reviewer keeps catching obvious defects (levitating players, extra arms, readable crests,
pasted-in people, all-white crowds, wrong head counts, giant flags, wrong stadium, morphing) that a general
"does this look right?" pass missed. This note covers how other teams catch defects like these with a vision
model, and gives a recipe for us. Companion to [`2026-11-25-recurring-bugs.md`](./2026-11-25-recurring-bugs.md).
Tags: **[vendor]** Google docs, **[research]** papers, **[community]** forums, **[our guess]** untested here.

## 1. VLM-as-judge for stills

**Methods.**
- **TIFA / DSG** split the prompt into many small questions and have a VQA model answer each one. DSG
  orders the questions as a graph and skips the child questions when a parent fails
  ([DSG](https://arxiv.org/abs/2310.18235)) [research].
- **VQAScore** asks one yes/no question and scores the image by P(yes). It beats CLIPScore on
  compositional prompts, counting included
  ([VQAScore](https://blog.ml.cmu.edu/2024/10/07/vqascore-evaluating-and-improving-vision-language-generative-models))
  [research].
- **GenEval / T2I-CompBench** check objects, counts, colours and positions. GenEval 2 finds that per-question
  soft TIFA matches humans best, and that counting gets harder as prompts grow
  ([GenEval 2](https://arxiv.org/pdf/2512.16853v1)) [research].
- **ImageReward-style scorers** rank images by preference. They are useful for choosing the best of N, but
  they never name the defect [research].

**How reliable they are, per defect.**
- **Prompt match (stadium, kits, a rough number of people):** good [research].
- **Anatomy:** weak. General VLMs miss human-figure artefacts that a dedicated detector catches
  ([Human Artifact Detection](https://pdf.arxiv.org/pdf/2411.13842),
  [Distortion-5K](https://arxiv.org/html/2503.00811v1), [AnomReason](https://arxiv.org/html/2510.10231v1)).
  Few-shot multi-VLM scaffolds help ([ArtifactLens](https://arxiv.org/abs/2602.09475)) [research].
- **Small text and crests:** weak on the full frame and much better on crops. Small objects get too few
  visual tokens, and zooming or tiling fixes this ([CropVLM](https://arxiv.org/abs/2511.19820),
  [Why VLMs miss small objects](https://arxiv.org/pdf/2610.09313)) [research].
- **Counting 22+1:** unreliable when the model states a number. Counting its boxes in code is better
  [our guess].
- **Physics:** physics judges disagree with humans and hallucinate violations
  ([PhyGenBench](https://arxiv.org/html/2410.05363v1), [PhyRubric](https://arxiv.org/pdf/2611.13576))
  [research]. A narrow question about one person's feet is far easier for the model than "is the physics
  right?" [our guess].

**Tricks that improve detection.**
1. **One yes/no question per item, never "any problems?"** This is the core of TIFA, DSG and VQAScore
   [research]. Word each question so that "yes" means a defect, and make the model give a reason and a box.
2. **Locate, then judge.** Gemini returns `box_2d` = `[ymin, xmin, ymax, xmax]` normalised to 0-1000
   ([image understanding](https://ai.google.dev/gemini-api/docs/image-understanding)) [vendor]. Count the
   boxes and measure flag size against player height in code.
3. **Crop and zoom.** Use overlapping tiles (about 3x2 on a 16:9 frame), and send each person crop
   upscaled 2x for the anatomy and text questions [research; grid is our guess].
4. **Reference side by side.** Send the stadium reference and the take together, and ask about specific
   differences [our guess].
5. **Consensus.** Ask each hard-fail question 3 times, or once each to Flash and Pro, and flag when 2 of 3
   answers say yes [our guess].
6. **Trust a "fail" more than a "pass".** The judge (Gemini) and the generator (Nano Banana) come from the
   same family [our guess].

## 2. Video clips

- **Gemini on a whole file** samples at **1 fps by default**, which misses fast motion. Set
  `video_metadata=types.VideoMetadata(fps=...)` (up to 24), use `start_offset`/`end_offset` to clip, and set
  `media_resolution` (66 or 258 tokens per frame). Refer to moments as `MM:SS`
  ([video understanding](https://aistudio.google.com/docs/video-understanding)) [vendor]. For an 8 s
  clip, use fps 8-12 at high resolution [our guess].
- **Frame sampling:** extract every 3rd frame with ffmpeg. Run the still checklist on 4-6 of those frames
  and box detection on all of them [our guess].
- **VBench's temporal dimensions:**
  - *Subject consistency:* DINO-feature similarity between frames.
  - *Temporal flickering:* the difference from one frame to the next.
  - *Motion smoothness:* an interpolation prior.

  ([VBench](https://arxiv.org/abs/2311.17982)) [research]
- **Cheap version for us** [our guess]:
  - Compute DINOv2 or CLIP embeddings per tracked person crop, and flag a drop in similarity between
    adjacent frames (a morph or identity swap).
  - Flag a box centre that jumps more than 15% of the frame width in one frame (a teleport).
  - Flag a change in the head count when no one enters or leaves the frame.
- **Physics:** ask narrow, timestamped questions, and never trust a single physics score [research,
  judge-bias findings above].

## 3. The fix loop

- **Best-of-N** is the strong simple baseline. Reflection loops, which feed the critique into the next
  generation, beat it at equal compute ([Reflect-DiT](https://arxiv.org/abs/2503.12271),
  [ReflectionFlow](https://arxiv.org/abs/2504.16080), [Idea2Img](https://arxiv.org/abs/2310.08541))
  [research]. Repeated small edits can degrade the image [research, UniT CVPR 2026 supplement].
- **Choose the fix by defect type** [our guess]:
  - **Re-roll:** a random local defect (one extra arm, one floater, one readable crest). It is seed noise.
  - **Edit or inpaint** (`flow_edit_image`): one localised fix on a take that is otherwise a keeper, such
    as a crest or one flag. Allow at most 2 passes, then re-check the whole frame.
  - **Rewrite the prompt:** the same defect in 2 or more of the last 4 takes (a white crowd, a wrong
    count, the wrong stadium). Feed the judge's reasons into the rewrite.
- **Budget:** 4 takes per prompt and at most 2 rewrites, so at most 12 takes per shot. Keep every take's
  score, and show the human the top 2 by score with their flags [our guess].
- **Score:** a hard fail (anatomy, readable text, levitation, wrong count, pasted-in person) vetoes the
  take. Soft items (stadium match, diversity, flag size, light) add up to a 0-1 rank [our guess].

## 4. Recipe (google-genai SDK) [our guess]

1. For each take, call `gemini-3-flash-preview` with JSON output (`response_schema`) and get back boxes for
   `person`, `referee`, `flag`, `shirt_text_or_logo` and `ball`.
2. Check in code: 22 players and 1 referee when the shot needs them, every flag shorter than 1.5x a
   player's height, each team in its own half.
3. Crop each person box and each text box. Ask the anatomy, contact and text questions 3 times per crop,
   and take the majority.
4. Ask the whole-frame questions with the stadium reference attached. A Pro-class model gives a second
   opinion on anything Flash flags.
5. Write `qa.json` next to the take. Then re-roll, edit or rewrite as section 3 says. The picks page shows
   the flags.
6. **Calibrate first:** run the checks on rounds 1-4 against the reviewer's notes. Any question that misses
   more than 1 in 5 of the known defects stays human-only.

Check the model names first: the docs list newer Flash models and an opt-in agentic video mode
(`media_processing="AGENTIC"`), which is meant for long videos [vendor].

## 5. Checklist: women's football stadium still ("yes" = defect; give a reason and a box)

1. Does anyone have extra or missing arms, legs or heads, or a limb merging into another person?
2. Are any hands or fingers malformed (crop)?
3. Is anyone airborne with no jump cue (no crouch or stride, feet together), or are the feet of anyone
   meant to be standing off the grass?
4. Is a shadow missing, or pointing against the other shadows?
5. Does anyone look pasted in: wrong scale for their depth, different light or sharpness, a hard edge?
6. Is any number, letter, logo, crest or sponsor readable on a shirt, board, flag or screen (crop)?
7. When the whole pitch is in shot, is the player count not 11 per team, or is the referee count not 1?
8. Are the players and the crowd mostly one skin tone when the shot asks for a mix?
9. Is any flag taller than about 1.5 players, or does any flag cover a whole stand section?
10. Next to the reference, do the roof, stands, tiers, floodlights or seat colour differ?
11. Is a kit the wrong colour, or is a player wearing the wrong team's kit?
12. Is the ball missing, doubled, or floating with no player near it?
13. Is any face in the crowd warped, melted or duplicated (tiles)?

## 6. Checklist: clip (fps 8-12; answer with `MM:SS`)

1. Does anyone change face, kit or hair between frames?
2. Does anyone appear, vanish or teleport?
3. Does a limb multiply, melt, or pass through a body or the ball?
4. Does anyone float, or hang in the air too long?
5. Do feet slide over the grass?
6. Does the ball change size, split, or move without being touched?
7. Does any text or crest become readable?
8. Does the stadium bend or shift while the camera is still?
9. Does the head count change with no one entering or leaving?
10. Does the clip contradict the still it started from (kit, layout, light)?
11. Is there flicker, or a sudden jump in light or colour?

Plus the code checks: a drop in an identity embedding, a box jump of more than 15% of the frame width, and
a change in the head count.
