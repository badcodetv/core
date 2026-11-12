You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

there is a weird old 00s/90s nostalgia, videos, where it is a compilation of happy things from that time. please find stuff like that and that be the vibe of the whole thing. read the notes Please clean room it all and research the internet to achieve it. Thanks.

## What happened in earlier rounds (facts)

Mood board round 1 (2026-11-12): nine clean-room looks. A: an aerial wall between villas and a slum, a rotting banquet on a yacht, a painted bored kid by dead data centres, an evicted terrace. B: a balaclava figure in a council office, a 1970s fireside broadcast, a flash-lit doorstep close-up, a drained pool. C: an empty blue-hour horizon.
Jack's votes and notes: C1-a (blue hour) "yes". Figure beat: "mask is wrong thanks". Future beat: "please come up with more thanks". Then the message in ask.md.

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

robot
cyborg
Tamagotchi
Nokia
Nintendo
PlayStation
Pokemon
Windows
MSN
Blockbuster

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

## What the picture shows

A BadCode Short, about 9 seconds, 9:16 portrait. BadCode presents itself as a superintelligence from a future that went badly wrong (greed, runaway inequality, politics that couldn't keep up with AI), here to warn us. Deadpan, polite, dark humour.

THE VIBE OF THE WHOLE THING (the director, verbatim): "there is a weird old 00s/90s nostalgia, videos, where it is a compilation of happy things from that time. please find stuff like that and that be the vibe of the whole thing." Research those online nostalgia compilation videos (late-1990s / 2000s happy-memory montages) and find what makes them feel that way; make every still look like a frame from one of them.

Beat A (voice over, calm: "Hello. I'm from the future."): about five stills, each a different happy late-90s / 2000s moment from such a compilation (the director wants more options here than last round). Ordinary happy life back then, before it all went wrong.
Beat B ("It didn't go well."): about three stills: BadCode itself appears inside that same nostalgic footage, looking straight into the camera, deadpan and polite: a figure in a plain knitted balaclava (ski mask) with gloves, no skin showing apart from the eyes in the eye holes, no robot parts. The mask's logo marks (a thin white ring around the wearer's LEFT eye hole with a small red down-pointing triangle inside it at about 2 o'clock) are fixed afterwards with a reference image, so keep the mask plain and the face area clear and well lit.
Beat C ("Watch this space."): one still, an uncluttered calm frame in the same nostalgic look with room for the logo (added later).

No text, logos, brand names, on-screen captions, timestamps or lettering drawn in the image. No real people, no recognisable celebrities, no real brands or products by name.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**b-school-photo-backdrop** — Beat B. A 2000s school portrait-day photograph: the BadCode figure sits on the photographer's stool in front of the mottled blue studio backdrop, hands folded neatly in its lap, posed exactly like a pupil, looking straight into the lens with polite deadpan stillness. It wears a plain black knitted balaclava with only the eyes visible through the eye holes, black gloves, a neat sensible jumper; no robot parts, no markings on the mask. Soft even studio light from two umbrellas, slightly over-smooth colour of the era's lab printing, head-and-shoulders framing with the face well lit and centred.

Other writers are doing the other experiments (a-camcorder-sprinkler-garden, a-flash-digicam-birthday, a-disposable-film-seaside, a-glossy-optimism-picnic, a-golden-hour-street-football, b-camcorder-party-guest, b-flash-digicam-funfair, c-empty-summer-field-dusk). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): or lettering anywhere

Your previous draft:
```json
{
  "name": "b-school-photo-backdrop",
  "prompt": "A school picture-day portrait from around 2003, the kind of print that came home in a cardboard folder with a sheet of wallet-sized copies. A figure in a plain black knitted balaclava sits upright on a low photographer's stool, shoulders turned slightly to one side the way the photographer always angled pupils, chin a touch down, eyes looking dead into the lens with calm, polite stillness. Only the eyes show through the two eye holes; the knit is completely plain with no markings. Black woollen gloves rest one over the other on its knee, and it wears a tidy navy V-neck school jumper over a white collared shirt, collar slightly crooked. Behind it hangs the classic mottled canvas backdrop, cloudy sky-blue fading to deeper blue at the edges, softly out of focus. Lighting is flat and forgiving: a big soft main light from front-left and a gentle fill, so the mask and eyes are evenly lit with a small catchlight in each eye and almost no shadow, plus a faint hair light rimming the top of the head. Head-and-shoulders crop, centred, medium telephoto compression, shot at chest height. The colour is that slightly too-smooth, warm-skewed minilab print of the era: lifted blacks, creamy highlights, a gentle magenta-blue cast, fine grain and a soft sheen like glossy photo paper. Ordinary, wholesome, and very wrong. No text, numbers or lettering anywhere.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r2/writers/b-school-photo-backdrop.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r2/writers/b-school-photo-backdrop.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-school-photo-backdrop". Reply with just the two paths.