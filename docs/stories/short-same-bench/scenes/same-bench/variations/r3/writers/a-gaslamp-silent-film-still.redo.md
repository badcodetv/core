You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

keep experimenting with stills and stlyes, i want the rich fat cat to look ominous almost like a horror silent hill style Please clean room it all and research the internet to achieve it. Thanks.  thanks

## What happened in earlier rounds (facts)

Mood board round 1 (2026-11-12) showed nine takes on a 1910s pen-and-ink editorial cartoon look: a frosty park from above, a grease-crayon close-up of his dismissing hand, from behind the bench at noon, a flat-colour poster outside a hospital at night, him as an old cut-out in a rainy modern bus stop, over the nurse's shoulder, a banknote engraving portrait, a torn page 1919/today, him alone at sunset. Jack left no votes or notes on it.
Jack's next message, verbatim, is ask.md.

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

The war is over my boy
Rollin Kirby
Kirby
Silent Hill
Pyramid Head
Konami

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

Round 2 direction (Jack, 2026-11-12): the rich fat cat must look OMINOUS, almost horror: the dread of a foggy, rusting, nightmare-town survival-horror game. Take that feeling and translate it into this short; do not recreate any specific game's monsters, characters, places or imagery. The comedy of the short stays, the cartoon roots can stay or be pushed, but he should frighten.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**a-gaslamp-silent-film-still** — Beat A, 1919, done as a single frame of a silent horror film rather than a cartoon: orthochromatic nitrate look, chalk-white skin, crushed blacks with no mid-grey, heavy silver grain, scratches and an iris vignette. Night; a single gas lamp hangs right above the bench, so the hard top light turns the rich man's eye sockets into black pits under the hat brim while his polite smile glows white. Medium two-shot at eye level: he waves the soldier off with a limp hand; the soldier, crutch across his knee, is mostly in shadow. The darkness above the lamp leaves room for a caption.

Other writers are doing the other experiments (a-fog-swallowed-park, a-his-shadow-arrives-first, b-blurred-behind-the-nurse, b-crosshatched-grin-closeup, b-low-poly-short-draw-distance, c-black-painting-on-plaster, c-the-only-still-thing, c-rust-dust-wasteland). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): in the picture

Your previous draft:
```json
{
  "name": "a-gaslamp-silent-film-still",
  "prompt": "Archival still from a 1919 horror picture, tall vertical composition: a park at night reduced to one iron bench and the lamppost directly behind it, its glass lantern burning straight over the seat so every bit of light falls from above. Sitting under that lantern is a heavyset rich man in a towering silk hat and a tight black frock coat, a gold watch chain looped over his paunch. The downward glare puts both eyes in solid black hollows beneath the brim, empty except for one faint glint of flame, while his lower face is chalk-white greasepaint and his mild, gracious smile shines bright, the red of his lips gone near-black the way old blue-sensitive stock renders red. With a soft, bored flick of his kid-gloved fingers he shoos away the fellow seated next to him: a gaunt young infantryman back from the trenches, greatcoat hanging off him, one trouser leg pinned up short at the knee, a wooden crutch resting over his remaining knee. The soldier sits just outside the pool of lamplight, swallowed into silhouette, nothing lit but his knuckles on the crutch and a sliver of jaw. Eye-level camera at bench height, still and frontal, a medium two-shot with the pair sitting low in the picture; above the lantern the top third stays empty velvet black for a caption. Filmed through an uncoated lens on early orthochromatic nitrate with a hand-cranked camera: stark white highlights against crushed ink blacks with no mid-grey between them, heavy clumped silver-halide grain, fine vertical scratches, dust specks, softness toward the edges and a circular iris closing in on the corners. Black and white, anti-CGI, no digital smoothing, no clean render sheen, no lettering or text. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/a-gaslamp-silent-film-still.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/a-gaslamp-silent-film-still.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "a-gaslamp-silent-film-still". Reply with just the two paths.