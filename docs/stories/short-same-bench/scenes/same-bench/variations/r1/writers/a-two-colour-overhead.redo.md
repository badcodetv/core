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

**a-two-colour-overhead** — Beat A, 1919. A high overhead view looking down on the bench from a lamp post, like a printed magazine plate in black ink plus one flat spot colour, brick red, used only on the rich man's waistcoat, which is patterned with tiny dollar signs. The bench, the path and the long winter shadows make a strong diagonal; the soldier's crutch and single boot cast their own shadow. The rich man's hand waves away from the soldier. Off-white paper margin across the top for the caption.

Other writers are doing the other experiments (a-crosshatch-wide-autumn, a-grease-crayon-low-angle, b-crosshatch-hospital-dusk, b-crayon-closeup-hands, b-laid-paper-rain, c-split-diptych, c-portrait-straight-to-camera, c-red-spot-repeated-benches). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): for a caption

Your previous draft:
```json
{
  "name": "a-two-colour-overhead",
  "prompt": "Tall upright plate from a weekly magazine of 1919, printed letterpress in just two inks on warm cream stock: a black key drawing, and a single flat brick-red (#A63A2B) laid over it as a second plate, slightly off register by a hair. Our eye hangs at the top of an iron lamp standard and looks steeply down at a park bench in midwinter. Bench, raked gravel walk and the stretched shadows of bare plane trees all slant together in one strong line from bottom left to top right, cutting the page in half. On the bench's left end, seen from overhead, a vast round plutocrat: the glossy black disc of his topper, the slope of coat shoulders, a starched wing collar, and swelling out between his lapels a waistcoat that carries the sole patch of red on the whole plate, its flat red dotted with rows of minute dollar signs. One gloved arm swings out sideways away from his neighbour, palm out, flicking the air as though dismissing a waiter. Down at the opposite end, with bare slats yawning between them, a thin demobbed private hunches in a shabby army overcoat and field cap; his left leg ends at the knee, the empty khaki pinned up flat, his right foot in a hobnailed boot set square on the gravel, a crude ash-wood crutch propped by his side. Low winter sun throws the crutch and that solitary boot into two long, skinny black shadows that reach across the walk on their own. Line work is brisk dip pen, ruled parallel hatching for shade, solid black for the topper and coats; the red sits flat with no outline of its own; faint ink spread and paper tooth. Across the upper fifth, leave a blank band of bare cream paper, untouched, for a caption to go in later. No lettering, words, captions, monograms or word bubbles drawn on the plate. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/a-two-colour-overhead.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/a-two-colour-overhead.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "a-two-colour-overhead". Reply with just the two paths.