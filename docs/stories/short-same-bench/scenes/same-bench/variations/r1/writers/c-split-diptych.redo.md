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

**c-split-diptych** — Beat C, the button. One portrait frame split horizontally by a thin drawn panel border: the top panel is the 1919 bench with the soldier, the bottom panel the modern bench with the nurse, both in matching pen crosshatch, the rich man in exactly the same pose, angle and size in both, so he lines up like a stamp. The two companions differ completely; he does not differ at all. A clear white gutter strip between the panels holds the caption.

Other writers are doing the other experiments (a-crosshatch-wide-autumn, a-grease-crayon-low-angle, a-two-colour-overhead, b-crosshatch-hospital-dusk, b-crayon-closeup-hands, b-laid-paper-rain, c-portrait-straight-to-camera, c-red-spot-repeated-benches). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts: ending at the knee with the
- shares wording with other prompts in this round: Flow prompts: leg ending at the knee with
- shares wording with other prompts in this round: Flow prompts: nose in the air on the

Your previous draft:
```json
{
  "name": "c-split-diptych",
  "prompt": "Vertical page drawn entirely with a steel dip pen and black ink on warm, faintly yellowed newsprint, styled like a hand-drawn American daily-paper cartoon of the First World War years: swelling and thinning contour lines, layered diagonal hatching that tightens into near-black in the shadows, small dot stipple on the path, an underdrawing of soft pencil still faintly visible in places. The sheet is cut into an upper and a lower picture of equal size, each boxed by a fine hand-ruled border that wavers a little, and between them runs a broad strip of untouched paper, roughly one sixth of the page, left completely bare. Upper picture: a public garden around 1919, leafless plane trees, a cast-iron lamp standard, a low railing, and a park seat of iron arms and wooden slats viewed dead level at seated eye height. Occupying the seat's left side is a portly plutocrat, double chin, waxed moustache, a gleaming stovepipe hat, a black tailcoat buttoned over a patterned vest with a watch fob, white spats, one kid-gloved hand raised at shoulder height and flicking outward in dismissal, lids lowered, nose in the air. On the seat's right side, a hollow-cheeked infantryman home from France in a creased service tunic and wrapped puttees, his right leg ending at the knee with the fabric folded and fastened, a plain timber crutch leaning on the armrest, his cap held between his knees, turned toward the plutocrat. Lower picture: that identical seat from that identical viewpoint, but the surroundings are present day, a council recycling bin, a slim modern street light, a bus shelter and a mid-rise glass tower beyond the hedges, all rendered with exactly the same pen and hatching. The plutocrat is a perfect duplicate of the upper picture, placed on the same left side of the seat, drawn at the same scale and angle, the same lifted gloved hand, the same lowered lids, every crease of his coat and every highlight on his hat matching, so he sits precisely beneath his earlier self like an impression from one printing block. On the right side now sits an exhausted hospital nurse in baggy scrubs, an ID badge on a cord, rubber clogs, hair escaping its tie, back bowed, holding a takeaway coffee in both hands and looking up at him. His companions change completely from top to bottom; he changes not by a single stroke. Plain, shadowless overcast light in both pictures, strictly monochrome black ink on cream paper with visible fibres and a slight feathering where the ink soaked in. The picture contains no lettering of any kind: no words, numbers, signatures, labels or dialogue bubbles.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/c-split-diptych.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/c-split-diptych.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-split-diptych". Reply with just the two paths.