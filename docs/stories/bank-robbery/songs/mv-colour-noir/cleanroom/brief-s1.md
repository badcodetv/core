# What Jack said

please go to the bank robbery music video. lets forget the psychedelic styles, but keep the cool transitions if you know what i mean, but make them realsitic instead of trippy. lets make it like a colourful noir, basically the Fat Tony's den from the Simpsons vibe, and Shadows Of Evil from Black Ops 3. lets do lip syncing but the lip syncing comes from the conversations, so they talk the lyrics, the speakeasy bands sings the chourus/some of the song. their could be that same band singing under a bridge at night with the city lights reflecting off the water, the healights of the  cars illuminating the band, gangster style. it should be fast and full of car chases, i liked the first person car thing from the last one, maybe we follow that person throughout, not as a main theme just as one of many stories playing out. maybe a compilation of robberiers, like a car pulling a small safe out of a wall and it being dragged behind them with sparks flying as they flee the cops. balaclavas with the badcode logo on them, with people getting robbed. panning shots of pretty prohabition era cities with lights and refelections, interesting shots, not just the same old ai slop. maybe have old school hot rod racing.

please save this to the right file, lets just do the general shots, and we'll worry about lip syncing later. things i didnt like about the last sequence of the bank robbery music video were the ai slop, pschedlic transitions, the blue and red scarf/teams, the bakers walking in randomly, the story in general, i think lets just make a bunch of cool stuff instead then we'll make it make sense later. please get started with the stills and use the new scene thing. i dont want to have to remind you about the same prompt being made bug over and over, so what do i say so that you are aware of that, and only use interenet research (please research the internet to on how to make this in nano banana 2.1) Thanks.

# Web research on the engine

# Colourful noir on Nano Banana 2.1: web research (2026-10-30)

Tags: [vendor] Google; [tested] reported test; [reported] opinion or single source; [inference] mine.
**Evidence is thin.** I found no 2.1 test of reflections, motion blur, hands, driver POV or logos on fabric, and no Flow-specific prompt guide. Those are mostly inference.

## References, visually
- **Morg City:** "bright lights and dark shadows", neon streaks, narrow alleys, fire escapes, murky canals, flame braziers, one purple [reported](https://www.callofdutyzombies.com/zombie-library/zombies-library/black-ops-iii/shadows-of-evil/zombies-tour-guide-book-r414). No palette source reachable.
- **Fat Tony's club:** basement [reported](https://simpsonswiki.com/wiki/Businessman%27s_Social_Club), stairwell, poker, race betting [reported](https://en.wikipedia.org/wiki/Bart_the_Murderer). No source gives its colours: look at frames.
- **Technicolor noir:** intense, painterly, dreamlike hues; strong backlight; colour coded to sets and costume [reported](https://offscreen.com/view/technicolor-noir-leave-her-to-heaven).
- **Speakeasy:** amber bulbs; plum, tobacco grey, almost-black green, navy, not black. A modern decorator's claim [reported](https://www.osmoz.com/inspiration/osmoz-magazine/2102/i-turned-my-basement-into-a-1920s-speakeasy-the-prohibition-aesthetic-finally-landed).
- **Period neon:** neon is clear intense red, argon cool greyish blue; coated tubes widened the range; lost tints include ruby red, midnight blue, noviol gold, uranium green [reported](https://americanheritage.com/neon). Bulb signs came first, so both can share a street [inference].
- **Dry lakes:** hard-packed alkali, dust churned by cut-down roadsters, flathead V-8s, finned heads, no helmets or belts, some night runs without headlights [reported](https://www.americanheritage.com/hot-rods-redux).

## 1. Slop, length, structure
- Keyword lists let the model add its own choices; full-sentence scenes rendered every named detail [tested, one run](https://fuser.studio/articles/nano-banana-prompt-guide).
- Structure: subject, action, place, composition, style; name materials ("navy blue tweed", not "suit jacket") [vendor, Nano Banana 2 and Pro](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana).
- Length: no tested ideal found. Write a brief, subject outward; lens and depth cues beat "close-up" or "professional"; not every layer is needed [reported, 2.1](https://runware.ai/docs/models/google-nano-banana-2-1/guides/prompting).
- 2.1 obeyed lighting direction where Pro reversed it [tested, one run each](https://fuser.studio/articles/nano-banana-2-1-vs-nano-banana-2-vs-pro); its reportage light can look more authentic, though Pro has finer texture [tested](https://www.cometapi.com/nano-banana-2-1-vs-nano-banana-pro/). So state where light comes from [inference].

## 2. Saturated noir without the defaults
- Vaguer prompts increase orange-and-teal; name your palette. Evidence is Midjourney and Ideogram, not Nano Banana [reported](https://datalab.flitto.com/en/company/blog/this-orange-and-teal-color-bias-shouts-that-your-image-was-ai-generated/).
- Describe what you want, not what to avoid [vendor](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana). A closing "Negative prompt:" list did change one output [reported](https://runware.ai/docs/models/google-nano-banana-2-1/guides/prompting).
- Chiaroscuro, film-stock phrasing, grain and high saturation are Google's own examples [vendor, same guide].
- Filmed night [inference]: give every light a physical source in frame (bulb sign, shop window, lamp, headlamp, fire), with falloff and true dark between. Put colour in painted walls, awnings, cars and clothes, not only in the light: that separates Technicolor from neon, and lets a dry street stay colourful. Treat weather as a choice: dry, fog, snow, dusk.

## 3. Reflections
- Reflectivity rises at shallow angles; distant water looks mirror-like [reported, graphics glossary](https://3d.irpr.agency/glossary/fresnel/). Smoother surfaces show it more sharply [reported](https://docs.unity3d.com/Manual/StandardShaderFresnel.html). So a low camera gets stronger reflections [inference].
- Night sources give contrast and colour depth; daylight reflections go flat [reported](https://121clicks.com/inspirations/quiet-poetry-of-rainy-streets-wet-city-nights/).
- Believability [inference, untested]: the reflection sits below its source, stretched toward the camera and dimmer than it. Road is patchy: puddle sharp, damp asphalt smeared, crown dry. Canal water breaks lights into bars. Only bright things reflect visibly. Name the surface's condition and which light lands where.

## 4. Speed
- Target: car sharp, background streaked; too fast a shutter leaves no streak [reported](https://reeflexstore.com/blogs/news/ultra-telephoto-motorsport-masterclass). Only what matches the pan stays sharp [reported](https://www.talkphotography.co.uk/threads/panning-can-anyone-identify-the-problem.153905/post-1766573).
- State blur direction and strength [reported](https://carat.im/en/prompt-gallery/motion-blur-portrait). Google's examples use "motion-blurred" action [vendor](https://deepmind.google/models/gemini-image/flash/).
- Real chase vantages: low bumper mount, through the windscreen, over the driver's shoulder [reported](https://www.documentarytube.com/blog/how-they-shot-the-famous-car-chase-in-the-french-connection/).
- Inference, untested: describe physics, not "speeding". Spokes blurred to discs, wheels turned, body rolled, nose dipped, dust trailing, horizon tilted, car cut by the frame edge. Sparks: name the metal, the contact point, spray direction opposite travel, light on the road beneath.

## 5. Driver's-eye
Nothing direct found. Inference, untested: state camera position (driver's eye height, behind the wheel), what crosses the frame bottom (rim, knuckles, cuffs), how each hand grips, each gauge by material, and what's beyond the windscreen. Check fingers.

## 6. Small logo on a mask
- Short exact text rendered first try, and a logo from a second image landed on an object [tested, one run](https://fuser.studio/articles/nano-banana-prompt-guide). Small text, especially at 1K, is a weak spot [reported, citing model card](https://www.cometapi.com/nano-banana-2-1-vs-nano-banana-pro/).
- Clear reference; describe colour, position, layout; avoid "pixel-perfect" commands; drift in 5 to 15% of attempts [reported, Pro](https://docs.apiyi.com/en/faq/nano-banana-pro-print-distortion.md). Embroidery with folds and light is a known route [reported](https://www.elephorm.com/formation/apprendre-ecrire-des-prompts-performants-pour-generer-des-images/creation-graphique-et-integration-typographique-avec-nano-banana).
- For exact fidelity, composite afterwards [reported](https://fal.ai/learn/tools/how-to-use-nano-banana-2). Make it large enough to read at frame size, or plan post [inference].

## 7. Vistas
No study of symmetry bias found. Inference, untested: choose a place someone could stand (fire escape, rail bridge, water tower, boat, pier) and name it. Put something large and cropped near the lens, skyline to one side, a street leaving at an angle, uneven heights, dark blocks without lit windows.
## 8. Refusals
- Google bars violent and harmful uses, with possible artistic exceptions; application to images is unstated [vendor](https://policies.google.com/terms/generative-ai/use-policy). The 2.1 card doesn't address weapons [vendor](https://deepmind.google/models/model-cards/nano-banana-2-1/).
- I found **no report** of Flow blocking robbery, masks or period gangsters. Unknown, not safe.
- Blocks can come without a reason. Retry once, change one thing; if the block follows the subject itself, stop, don't reword around it [reported](https://blog.laozhang.ai/en/posts/nano-banana-2-blockreason-other). Harmless terms can flag; describe the image more directly. Disguised requests are still filtered, and accounts risk consequences [reported](https://zilliz.com/ai-faq/is-there-a-way-to-bypass-safety-filters-in-nano-banana-2-prompts).
- Legitimate [inference]: describe what's visible, not the crime: masks, bags, a vault door, a waiting car. Leave weapons out of frame.

# Web research for this round

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

Rewrite these still-image prompts for Google Flow's Nano Banana 2.1 (16:9), one each. Jack liked each scene: keep its place, vantage, light and colours, and make only the change he asked for, written properly into the picture. The last round's prompt and an image are shown so you can keep what worked, and you are free to reword all of it.

The band (the same people wherever they appear): five musicians in sharp 1930s gangster clothes: a very tall thin man on upright bass, a stout older man on trumpet, a young man on clarinet, a grey-haired woman on a small drum kit, and fronting them at a period microphone, the singer: a broad man in his forties with black hair going silver at one temple, a broken nose and heavy eyebrows. Jack: "it needs to be a male singer, since the song itself is a man singing." Any wide-open singing mouth gets refused by the engine, so his mouth is closed or he is mid-breath.

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web.
- Never name a TV show, game, film, director, artist or real person. No children. No readable words: don't write a colour name right beside the word for a sign, because the engine printed "RUBY RED" on a sign last round. Weapons stay out of frame.
- The picture fills the frame edge to edge. Narrative prose. No quality buzzwords.

Write your output to `/home/jackt/projects/badcode/badcode/docs/stories/bank-robbery/songs/mv-colour-noir/cleanroom/s1.md`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots

## den1
Image(s): /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/den1-a.jpg, /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/den1-b.jpg
Jack's note: it needs to be a male singer, since the song itself is a man singing. thanks.
Last round's prompt: We sit on the plank floor of a cramped basement bandstand, at hip height behind a small drum kit, looking out past the musicians into the room they are playing to. Filling the left third of the frame, close and slightly soft, are the shoulder and pinned-up grey hair of a woman in a charcoal waistcoat, her brushes blurred over a snare, a brass cymbal edge cutting across the lower corner. Beyond her, seen from behind and in hard rim light: a very tall thin man in a double-breasted chalk-stripe suit, bent around an upright bass; a stout older man in a mustard three-piece lowering his trumpet; a young man in a too-big bottle-green suit with a clarinet. At the centre-right a broad woman in her forties in a garnet satin gown, a silver streak through her black hair, turns her head in profile to a heavy chrome period microphone, lips closed, chest lifted, taking a breath. A row of bare bulbs in tin reflectors along the lip of the stage throws amber light back at the camera, so every figure is edged in gold with their backs falling into dark. Past them, through cigar haze, the den burns in painted colour: plum walls, emerald leather booths, small crimson-shaded table lamps, men in wide-brimmed hats turned toward the stage. Between the lamps the room falls into true black. The picture runs to all four edges of the frame, with fine film grain.

## den4
Image(s): /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/den4-a.jpg
Jack's note: (none)
Last round's prompt: A long, low service tunnel of sooty vaulted brick behind the club, seen through a long telephoto lens from the far end, so that the depth is squeezed flat. Five musicians wait in single file along the right-hand wall between sets, stacked close by the compression. Nearest, big in frame and cropped at the knee, stands a broad woman in her forties in a dark green velvet coat over a satin gown, silver streak in her black hair, cigarette unlit between her fingers, jaw set, mouth closed, looking at nothing. Behind her is a stout older man polishing a trumpet bell on his sleeve, then a young man asleep on his feet with a clarinet under his arm, then a grey-haired woman in shirtsleeves tapping sticks against her thigh, and at the back a very tall thin man folded almost in half under a run of lagged pipes, holding the neck of an upright bass. Along the left side, an open coal furnace door is out of frame, and its orange firelight rakes across the bricks and up one side of each face. At the far end of the tunnel, a whole section of the brick wall has been rolled aside on iron rails, a hidden door standing open, and through the slot pours a hard blade of magenta and emerald light from the room beyond, laying a long coloured stripe down the wet flagstones toward us, broken by puddles. Steam drifts through the firelight. Dark brick swallows everything between the two light sources. The image carries all the way to the edges of the frame, with visible grain.

## bridge1
Image(s): /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/bridge1-b.jpg
Jack's note: (none)
Last round's prompt: Seen from the roof of a coal tug moored out in the middle of a wide black river at night, about four metres above the water, with the tug's soot-black funnel and a loop of wet hawser cropped hard against the left edge of the frame. Off to the right a colossal riveted steel arch bridge sweeps upward and leaves through the top of the picture, standing on one stone pier as big as a church. In the cold shadow beneath that arch, on the far bank, three long 1930s sedans, one oxblood, one cream, one bottle green, are parked nose-in on a cobbled quay, and their round tungsten headlamps meet in a single small warm pool of light. Inside that pool, tiny against all that iron, stand five people in sharp dark suits and hats: a very tall thin man with an upright bass, a stout older man with a trumpet, a young man with a clarinet, a grey-haired woman behind a small drum kit, and a broad woman at a period microphone. Thin river mist makes the headlamp beams visible as they cross the cobbles and die within a few metres. Behind the bridge a prohibition-era city climbs in uneven steps, some blocks entirely dark, others strung with bulb signs and coated neon tubes in ruby red, uranium green, pale gold and midnight blue, every sign too far away to read. The river takes those lights and breaks them into long trembling horizontal bars that run toward the camera, dimmer than their sources, with true black water between them. The picture runs to all four edges of the 16:9 frame.

