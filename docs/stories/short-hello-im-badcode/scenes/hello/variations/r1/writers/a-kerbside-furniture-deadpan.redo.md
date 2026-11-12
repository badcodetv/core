You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

"Hello, I'm BadCode: "I'm from the future. It didn't go well."" lets mess around with this. THanks

Answers to the questions: who is BadCode on screen = "Mix of both" (open on the future that went wrong, then cut to the balaclava figure for the punchline); angle = "Deadpan intro" (polite and calm, the understatement is the joke); shape and look = "9:16, explore looks".

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

robot
cyborg

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

## What the picture shows

A BadCode Short, about 9 seconds, three beats. Mood board round 1: spread the round across the beats (about four stills for A, four for B, one or two for C), each a genuinely different look. BadCode presents itself as a superintelligence from a future where humanity careered into disaster (greed, runaway inequality, politics that could not keep up with AI); it has come back to warn us. Dark humour, total authority, deadpan.

Beat A (the future, voice over "Hello. I'm from the future."): the future that went wrong, glimpsed and never explained. Show the aftermath of a society that failed itself, not monsters or robots attacking: what is left when greed won.
Beat B ("It didn't go well."): cut to BadCode itself: a figure in a balaclava looking straight into the camera, deadpan, calm, a little polite. The balaclava is a plain knitted ski mask; on it, around the LEFT eye hole (the wearer's left), a thin white ring, and a small red triangle with rounded corners pointing down, sitting inside the ring at about 2 o'clock. No skin visible, gloved hands, no robot parts. Where they are and how they are shot is yours to choose.
Beat C ("Watch this space."): the button; the BadCode logo is added afterwards in the edit, so leave a calm, uncluttered frame.

Portrait 9:16. No text, signs or lettering drawn in the image.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**a-kerbside-furniture-deadpan** — Beat A. A deadpan, straight-on large-format colour photograph of an ordinary street of identical small terraced houses at flat noon light under a pale sky. Outside every single front door, the whole contents of each home sit stacked on the pavement: sofas, cots, a fridge, framed photos face-down, boxes in the rain, all left out like an eviction day that happened to the entire street at once. Front doors are boarded with fresh plywood. Shot from the middle of the empty road with deep focus and a symmetrical vanishing point; nobody visible; the banality is the horror.

Other writers are doing the other experiments (a-aerial-wall-between, a-flash-banquet-left-standing, a-painted-bored-suburb, b-grey-tableau-office, b-fireside-public-information, b-flash-doorstep-closeup, b-standing-in-the-drained-pool, c-blue-hour-empty-horizon). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame

Your previous draft:
```json
{
  "name": "a-kerbside-furniture-deadpan",
  "prompt": "A tall portrait colour photograph taken with a view camera on a tripod planted on the centre line of a quiet residential road, perfectly level and square-on, the two rows of identical small red-brick terraced houses running away on either side and meeting at a single vanishing point in the middle of the frame. On the pavement outside every single front door sits the entire inside of that home, piled neatly at the kerb as if put out by the same hand on the same morning: a floral three-seater sofa, a white cot with its mattress, a fridge-freezer with its door taped shut, kitchen chairs stacked seat on seat, a standard lamp, black bin bags, cardboard boxes gone soft and dark from a shower that has only just stopped, picture frames laid face-down on top of a chest of drawers. The same arrangement repeats house after house to the far end of the street. Every front door and ground-floor window is covered with a fresh, pale, unpainted plywood board screwed flush to the frame, no numbers, no letterboxes, no markings anywhere. The road surface is wet and empty, no parked cars, no people, no animals. Flat, shadowless midday light from a uniform pale grey-white sky, soft and even, no sun and no drama. Everything sharp from the kerb at the bottom of the frame to the last chimney pots on the horizon, fine grain, natural muted colour: brick red, damp grey slate, cream and beige furniture, the raw yellow of the plywood repeating like a pattern. Neutral, patient, documentary, almost bored; the calm is the point. No text, no writing, no signs, no logos.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/a-kerbside-furniture-deadpan.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/a-kerbside-furniture-deadpan.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "a-kerbside-furniture-deadpan". Reply with just the two paths.