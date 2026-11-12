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

**b-grey-tableau-office** — Beat B. A static, centred tableau with shadowless flat light and a pale grey-green, desaturated palette, like an absurdist Swedish film set: BadCode sits behind a small, bare municipal desk in an otherwise empty waiting-room office, full figure visible, gloved hands folded neatly on the desk, staring straight down the lens. The balaclava is plain dark knit with a thin white ring around the wearer's left eye hole and a small rounded red triangle inside the ring at about 2 o'clock, pointing down. A wilted rubber plant, a wall clock with no hands, one empty visitor chair. Deep focus, wide-ish 35mm, camera at seated eye height; polite, patient, faintly tragic.

Other writers are doing the other experiments (a-aerial-wall-between, a-flash-banquet-left-standing, a-painted-bored-suburb, a-kerbside-furniture-deadpan, b-fireside-public-information, b-flash-doorstep-closeup, b-standing-in-the-drained-pool, c-blue-hour-empty-horizon). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame
- shares wording with other prompts in this round: Flow prompts: in the middle of the frame

Your previous draft:
```json
{
  "name": "b-grey-tableau-office",
  "prompt": "A portrait-format, dead-centre wide shot of a cramped, nearly empty council waiting office, framed square-on and perfectly level from the height of a seated person's eyes, the camera never closer than the far side of the room. In the middle of the frame a single figure sits upright behind a small bare municipal desk of pale laminate on thin steel legs, the whole body visible from the top of the head to the shoes under the desk. The figure wears a plain dark charcoal knitted ski mask that covers the entire head and neck, a dull grey-green office jacket buttoned to the collar, and dark wool gloves; the gloved hands rest folded one over the other on the empty desktop. On the mask, circling the wearer's left eye hole only, is a thin crisp white ring, and inside that ring, at roughly the two o'clock position, a small red triangle with softly rounded corners, point downward. The eyes inside the holes look straight down the lens, calm, patient and courteous, as if about to apologise for a long delay. Behind the figure, a blank wall painted a washed-out sage green, a round white wall clock with an empty face and no hands, and in one corner a rubber plant in a beige pot with its leaves drooping toward the lino. To one side of the desk, a lone moulded plastic visitor chair stands empty, facing the figure. The floor is speckled grey linoleum. Everything in the room is in sharp focus from the front edge of the desk to the back wall, rendered as if through a moderately wide 35mm lens with no distortion. Lighting is completely even and shadowless, a pale overcast-white glow from overhead panels with no visible source, no highlights and no dark corners. Palette is desaturated and chalky: putty grey, faded mint, dusty olive, off-white; the only saturated colour anywhere is the small red triangle. The mood is still, faintly ridiculous and quietly sad, like a polite interview that has already gone badly. No text, signs, posters, labels or lettering anywhere in the image. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/b-grey-tableau-office.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/b-grey-tableau-office.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-grey-tableau-office". Reply with just the two paths.