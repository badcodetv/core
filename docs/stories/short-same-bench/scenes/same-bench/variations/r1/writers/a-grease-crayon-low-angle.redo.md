You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

" #2 Same Bench: the 1919 fat cat tells a veteran "Forget it", then says it to a nurse on the same bench today. He hasn't aged a day." lets do this, using the art style, but lets change it slightly so it doesnt get copywrighted. THanks

please show me stills of this in the new scene skill and the dialogue skill thing thanks.

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

**a-grease-crayon-low-angle** — Beat A, 1919. Low angle from the gravel path, looking up so the rich man looms like a monument against a grey overcast sky, drawn in heavy black grease crayon with soft broken edges and a thin ink wash, the radical-magazine look rather than fine pen. His palm is raised flat toward the soldier, a stop gesture, cigar in the other hand. The soldier is in the lower corner, small, crutch across his knees, face half in shadow. Rough crayon grain carries all the tone; the bottom fifth is open path for the caption.

Other writers are doing the other experiments (a-crosshatch-wide-autumn, a-two-colour-overhead, b-crosshatch-hospital-dusk, b-crayon-closeup-hands, b-laid-paper-rain, c-split-diptych, c-portrait-straight-to-camera, c-red-spot-repeated-benches). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): a tall silk
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): a watch chain
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): a wooden crutch
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): anywhere in the
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): one trouser leg
- shares wording with other prompts in this round: Flow prompts: rich man in a tall silk

Your previous draft:
```json
{
  "name": "a-grease-crayon-low-angle",
  "prompt": "A hand-drawn editorial illustration in heavy black lithographic grease crayon on rough cream newsprint, with a thin grey ink wash laid underneath, in the blunt, angry manner of a 1910s radical magazine rather than fine pen work. The year is 1919, in a city park after the war. The viewpoint is very low, almost at gravel level on the path, looking steeply up at a wooden park bench. On the bench sits an enormous, well-fed rich man in a tall silk top hat, a fur-collared overcoat straining over his belly and a watch chain across his waistcoat. From this angle he towers like a statue on a plinth, his bulk and hat cutting a dark shape against a flat, heavy overcast sky. He holds one fleshy palm out flat toward his neighbour, a curt stop gesture, while a fat cigar smoulders in his other hand; his heavy-lidded face is bored and dismissive. Pushed into the lower left corner and drawn much smaller sits a young soldier just home from the front, in a worn army tunic, one trouser leg pinned up empty below the knee, a wooden crutch lying across his lap, his face half lost in shadow under his cap. All the tone comes from the crayon itself: broad dragged strokes, broken soft edges where the stick skipped over the paper tooth, dense solid blacks in the rich man's coat and hat, pale speckled grain in the sky. Palette is black, warm grey wash and the cream of the paper, nothing else. The bottom fifth of the frame is empty pale gravel path, kept clear for a caption. No text, no lettering, no signature, no speech balloon anywhere in the image. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/a-grease-crayon-low-angle.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/a-grease-crayon-low-angle.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "a-grease-crayon-low-angle". Reply with just the two paths.