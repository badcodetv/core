You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

" #2 Same Bench: the 1919 fat cat tells a veteran "Forget it", then says it to a nurse on the same bench today. He hasn't aged a day." lets do this, using the art style, but lets change it slightly so it doesnt get copywrighted. THanks

please show me stills of this in the new scene skill and the dialogue skill thing thanks.

## What happened in earlier rounds (facts)

Round r1 (2026-11-12): nine separate writers, one prompt each. The sameness gate still failed after two rewrites, so nothing ran and no stills were made.
Phrases it flagged as shared between prompts included: "no words letters numbers signature or speech", "on the bench's left end lounges", "end of the bench sits a", "a tall portrait drawing in black", "signature anywhere in the image thanks".
Jack, asked whether to run r1 anyway or start fresh: "Fresh round".

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

The war is over my boy
Rollin Kirby
Kirby

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

## What the picture shows

A BadCode Short, about 14 seconds, three beats. Mood board round 1: spread the round across all three beats (three stills per beat), each a genuinely different take on the look.

The art style: a 1910s pen-and-ink newspaper editorial cartoon (the inspiration is a 1919 Life magazine cartoon of a top-hatted fat cat on a park bench telling a one-legged soldier "The war is over my boy. Forget it."). Jack: use that art style, but change it so it is not a copy. Our own characters, poses, bench, park and composition; never recreate that panel.

Beat A (1919, the veteran): a park bench; a fat, top-hatted rich man sits beside a wounded soldier just back from the war (one leg, crutch). The rich man waves him off: "Forget it."
Beat B (today, the nurse): the same bench, the same rich man, identical and unaged, top hat and all; beside him now a tired nurse in scrubs. He waves her off the same way: "Forget it."
Beat C (the button): he hasn't aged a day. The same man, every time.

The rich man must look exactly the same in A, B and C (he becomes the reference for every later frame). Portrait 9:16. Leave room for a caption. No text or lettering drawn in the image.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**b-flat-colour-hospital-night** — Beat B, today. Flat colour in the old Munich satirical-magazine manner: heavy confident black outlines, three or four flat inks only (black, sodium orange, hospital teal, paper cream), no gradients. Night, the same style of park bench now outside a modern hospital's lit entrance, a sodium lamp above. The unchanged top-hatted rich man in his 1910s frock coat sits sprawled, palm out to the side; beside him a nurse in teal scrubs and trainers, hair escaping a clip, holds a paper cup of vending coffee and stares ahead. A black empty sky band at the top holds the caption.

Other writers are doing the other experiments (a-frost-park-from-above, a-crayon-dismissing-hand, a-behind-the-bench-noon, b-two-eras-two-pens, b-over-the-nurse-shoulder, c-banknote-engraving-portrait, c-split-century-bench, c-alone-at-sunset-wide). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): no lettering captions
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of any kind
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): silk top hat
- shares wording with other prompts in this round: Flow prompts: or marks of any kind drawn

Your previous draft:
```json
{
  "name": "b-flat-colour-hospital-night",
  "prompt": "A vertical 9:16 satirical magazine cover in the manner of a Munich colour-lithograph weekly from around 1905: thick, sure black contour lines and solid fields of colour printed from four inks only, ink black, sodium orange, hospital teal and warm paper cream, with every area filled flat and evenly, no blending, no shading ramps, no airbrush. The upper fifth is an unbroken slab of solid black night sky, left completely empty. Below it, seen straight on at eye level from a few metres away, a cast-iron and slatted-wood park bench stands on a strip of pavement in front of a present-day hospital entrance: a glass sliding door glowing as a flat cream rectangle, a canopy, a wall of dark teal panels. A tall streetlamp at the right edge pours a hard cone of orange down across the bench, and the shadows under the seat are cut as clean black shapes. Taking up most of the bench, a plump rich gentleman from 1910 slumps with his legs apart and his belly forward, tall silk top hat, black frock coat, cream waistcoat with a watch chain, round smug face, one arm flung out sideways with the palm turned flat towards his neighbour as if brushing her off. Pressed into the remaining end of the seat, a young nurse of today in teal scrubs and scuffed white trainers, a lanyard at her neck, hair coming loose from a clip after a long shift, both hands round a small paper vending-machine coffee cup, eyes fixed straight ahead in exhausted silence, ignoring his hand. Bold caricature in the figures, simplified geometric shapes in the architecture, an original composition. No lettering, captions or marks of any kind drawn anywhere in the picture. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/b-flat-colour-hospital-night.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/b-flat-colour-hospital-night.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-flat-colour-hospital-night". Reply with just the two paths.