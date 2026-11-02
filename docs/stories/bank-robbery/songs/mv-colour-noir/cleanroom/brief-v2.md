# What Jack said

please go to the bank robbery music video. lets forget the psychedelic styles, but keep the cool transitions if you know what i mean, but make them realsitic instead of trippy. lets make it like a colourful noir, basically the Fat Tony's den from the Simpsons vibe, and Shadows Of Evil from Black Ops 3. lets do lip syncing but the lip syncing comes from the conversations, so they talk the lyrics, the speakeasy bands sings the chourus/some of the song. their could be that same band singing under a bridge at night with the city lights reflecting off the water, the healights of the  cars illuminating the band, gangster style. it should be fast and full of car chases, i liked the first person car thing from the last one, maybe we follow that person throughout, not as a main theme just as one of many stories playing out. maybe a compilation of robberiers, like a car pulling a small safe out of a wall and it being dragged behind them with sparks flying as they flee the cops. balaclavas with the badcode logo on them, with people getting robbed. panning shots of pretty prohabition era cities with lights and refelections, interesting shots, not just the same old ai slop. maybe have old school hot rod racing.

please save this to the right file, lets just do the general shots, and we'll worry about lip syncing later. things i didnt like about the last sequence of the bank robbery music video were the ai slop, pschedlic transitions, the blue and red scarf/teams, the bakers walking in randomly, the story in general, i think lets just make a bunch of cool stuff instead then we'll make it make sense later. please get started with the stills and use the new scene thing. i dont want to have to remind you about the same prompt being made bug over and over, so what do i say so that you are aware of that, and only use interenet research (please research the internet to on how to make this in nano banana 2.1) Thanks.

# Web research

# Research round 2 (web only, 2026-10-30)

[vendor] Google says so. [tested] a reported run, or a museum object or period text. [reported] claimed, no test shown. [inference] my reasoning. No Omni car test exists that I could find.

## A. Stills (Nano Banana 2.1)

**1. Period masks**
- Wool; ribbed neck and face band, garter crown; khaki, c.1915. [tested] https://www.awm.gov.au/collection/C972117
- All-rib, long neck, grey Jaeger wool, 1911. [tested] https://www.rmg.co.uk/collections/objects/rmgc-object-4007
- 1917 patterns: 3-ply, four No. 8 needles, knit 2 purl 2, about 12in of rib; optional cape pieces. [tested] https://gutenberg.org/cache/epub/76611/pg76611-images.html
- Some sat loose round the face; some had ear holes. [reported] https://pieceworkmagazine.com/knitting-comforts-for-the-troops/
- 1930s colour names (tapestry wool, not knitting yarn): silver grey, Windsor green, marine, china blue, dull mauve, crimson, flame, Indian red, rust gold. [tested] https://collections.vam.ac.uk/item/O316532/
- 1927 felt: colours appliquéd in layers, stitched in black thread or matching silk. Search excerpt only; page wouldn't open. [reported] https://search.library.wisc.edu/digital/A4GPTMPITY7KSK8V/text/A33BK3MAGYIPJZ8P
- 1920s appliqué stitches, on a quilt: buttonhole, chain, running, stem. [tested] https://www.artic.edu/artworks/60737/sunbonnet-sue-quilt
- Not found: a 1920s motoring helmet, or photos with suit and hat. Those pairings, uneven hand-knitting and cut felt edges are [inference].

**2. Ring and triangle**
- Name exact materials; describe what you want, not what you don't. Reference image plus stated relationship is the logo route. [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- Left and right can swap in 2.1; anchor to objects, here a named eye or ear. [reported] https://picsart.com/blog/nano-banana-2-1-prompts/
- Centre drift and outline-versus-solid: no direct source. Try a filled patch of named cloth with a stitched edge, bare knit at the centre, a reference image, and several takes. [inference]
- Hidden faces: describe continuous knit where features would be, not "no eye holes". [inference]

**3. Several people**
- Multiple references (up to 14) are Google's consistency route; no multi-person method given. [vendor, Google link]
- 2.1 reportedly holds several characters better than 2, no figures; list what must not change. [reported, Picsart]
- Keep construction wording identical, change only colour, tie each colour to a position. [inference]

## B. Video (Omni Flash)

**4. Motion from a start frame**
- Mix framing and motion, style, light, location, action; no need to describe every frame. [vendor] https://deepmind.google/models/gemini-omni/prompt-guide/
- Be specific about camera, subject, environment. It may cut by default: ask for one continuous shot. Time beats in words or `[0-3s]`. Negatives go inline. [vendor] https://ai.google.dev/gemini-api/docs/omni
- "No human hands" still produced a hand. [tested, three prompts] https://pixverse.ai/en/blog/gemini-omni-video-model-review
- Quality reportedly falls past about 50 words; use motion verbs, not camera brands. [reported] https://geminiomniprompts.org/guide/
- Exact 8s timing is unverified; one API accepts only 3, 5 or 10s. [tested, Segmind link in 8]

**5. Cars** (none Omni-specific)
- Veo 3: artefacts in fast or close wheel shots; paint and glass reflections are tells. [reported] https://whichoneisreal.com/mode/videos/vehicles/
- Spell out physical behaviour and ground contact; state that objects persist; slower hides floatiness. [reported] https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix
- Driver's eye: say whose eyes and which body parts show. [reported] https://invideo.io/faq/how-do-you-generate-a-first-person-pov-shot-with-ai/
- Hands: one clear action beats controlling everything. [reported] https://hackernoon.com/how-to-fix-warped-hands-and-faces-in-ai-generated-video
- Omni environments held; articulated motion broke. [tested, one prompt] https://www.mindstudio.ai/blog/gemini-omni-1-1-flash-video-model
- Keep tyres mid-distance, one event per clip, sparks from a stated contact point. [inference]

**6. City vistas**
- Landscapes were Omni's weak category, looking "animated". [tested, text-to-video votes] https://notes.designarena.ai/gemini-omni-flash-a-video-model-for-directors/
- Nothing on skyline flicker. State unchanging light; avoid mixed sources. [reported, Genra]
- Background morphs under camera moves: simplify, ask for consistency. [reported, Veo] https://www.veo3ai.io/blog/veo3-scene-transition-guide
- Reflections called a hard limit. [reported] https://www.opus.pro/blog/ai-slop-aesthetic-12-tells

**7. Ending on a transition**
- No Google guidance for one-frame endings. Google's tool is first and last frames: state each, the exact move, no jump cuts. [vendor, DeepMind]
- Whip pan: name the direction, blur at the peak, cut there. Foreground wipe: object fills the frame briefly, cut at full coverage. Allow 2–3 tries. [reported, Veo, seller's site, link in 6]
- Blur is the glue, not a tour. [reported] https://www.media.io/ai-prompts/ai-video-transition-prompts.html
- Give it a physical motivation. [reported] https://www.veo3ai.io/blog/veo3-scene-transition-guide
- Push into dark, match on shape or light: no source. Use a dark object already in the frame, arrive late, keep "one continuous shot", and don't describe the next scene. [inference]

**8. Refusals and tells**
- Filters cover prompts and outputs and vary by region; recognisable people blocked. [vendor, API link]
- False refusals of harmless prompts, unresolved in May; current state unknown. [reported] https://piunikaweb.com/2026/05/20/google-investigating-issue-gemini-omni-flash/
- Twelve prompts: masks, swords, period rifle passed; real politician and gore blocked; crime untested. Retrying a refused input fails; rewrite. [tested] https://blog.segmind.com/gemini-omni-flash-keeps-rejecting-your-prompts-9-fixes-that-actually-work/
- Policy names dangerous or illegal activity. [reported] https://geminiomniprompts.org/blog/why-gemini-omni-blocks-your-prompts/ Robbery wording may matter. [inference]
- Tells: floaty weight, drifting objects, lighting flicker [reported, Genra]; hand morphs, too-smooth motion, gibberish text, broken background extras [reported, Opus].

# Your task

Write one image-to-video prompt per shot for Google Flow's Omni Flash, from one start frame, 8 seconds, 16:9. Each start frame is a still Jack picked, so keep the place, people and light. Describe what moves and what the camera does.

What Jack wants, in his words, is at the top of this brief. Fast, real, heavy cars; realistic transitions rather than trippy ones.

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web. Look at every start frame before writing.
- The song replaces the clip's sound, so nobody speaks or sings. Physical sound is optional.
- One clear action, single continuous shot, no scene cuts, no morphing. Cars move like heavy machines and don't teleport. No readable words. Weapons stay out of frame.
- End each clip on a realistic way out for the editor, starting from the suggestion given. Your own is fine if better.
- Plain prose, as short as does the job. No quality buzzwords. Each prompt must be different in approach from the others in your batch.

Write your output to `/home/jackt/projects/badcode/badcode/docs/stories/bank-robbery/songs/mv-colour-noir/cleanroom/v2.md`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
ENDS ON: <one line>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots

## pov1
Start frame: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/pov1-b.jpg
Suggested way out: The next green girder passes close to the lens and blacks out the whole frame, and the cut happens inside that dark.

## pov2
Start frame: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/pov2-b.jpg
Suggested way out: The crossroads light changes and the driver's eyes snap forward, so a fast whip pan right from the policeman's profile blurs across the windscreen pillar and lands in the next shot's movement.

## pov3
Start frame: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/pov3-b.jpg
Suggested way out: The nose keeps dropping until the dark steel deck fills the frame and the cut lands on the slam of the car hitting it, matched to a hard jolt at the start of the next shot.

## pov4
Start frame: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/pov4-b.jpg
Suggested way out: The big crimson sheet falls across the lens and fills the frame with red cloth, and the cut comes out of that cloth on a red shape or light in the next shot.

