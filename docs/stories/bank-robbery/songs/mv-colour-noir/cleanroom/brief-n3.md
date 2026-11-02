# What Jack said

please go to the bank robbery music video. lets forget the psychedelic styles, but keep the cool transitions if you know what i mean, but make them realsitic instead of trippy. lets make it like a colourful noir, basically the Fat Tony's den from the Simpsons vibe, and Shadows Of Evil from Black Ops 3. lets do lip syncing but the lip syncing comes from the conversations, so they talk the lyrics, the speakeasy bands sings the chourus/some of the song. their could be that same band singing under a bridge at night with the city lights reflecting off the water, the healights of the  cars illuminating the band, gangster style. it should be fast and full of car chases, i liked the first person car thing from the last one, maybe we follow that person throughout, not as a main theme just as one of many stories playing out. maybe a compilation of robberiers, like a car pulling a small safe out of a wall and it being dragged behind them with sparks flying as they flee the cops. balaclavas with the badcode logo on them, with people getting robbed. panning shots of pretty prohabition era cities with lights and refelections, interesting shots, not just the same old ai slop. maybe have old school hot rod racing.

please save this to the right file, lets just do the general shots, and we'll worry about lip syncing later. things i didnt like about the last sequence of the bank robbery music video were the ai slop, pschedlic transitions, the blue and red scarf/teams, the bakers walking in randomly, the story in general, i think lets just make a bunch of cool stuff instead then we'll make it make sense later. please get started with the stills and use the new scene thing. i dont want to have to remind you about the same prompt being made bug over and over, so what do i say so that you are aware of that, and only use interenet research (please research the internet to on how to make this in nano banana 2.1) Thanks.

# What Jack said about the first clips, word for word

Rejected:
- "looks like ai slop, so many barrels fall and morph and change alonside other objects, please just keep this one simple."
- "ai slop please change it, the refernce image is the problem"
- "ai slop the cars teleport, maybe make the refence image where the cars are facing the same directiion"
- "ai slop everything is so exaggerated please make it simple"
- "ai slop there are cars on the river fix it"
- "it looks like a modern car please make it look like the prohabition era"
- "ai slop lets just remove this one" (bottles sliding off a tipping bar shelf and dropping through a hatch)

Approved, for scale: a red sedan pulling away under an elevated railway with sparks falling, then a pillar crossing the lens; a teal sedan and a police motorcycle on river ice; a view from a stopped car of a policeman and a theatre crowd, ending on a whip pan; a view back over a seat as a crimson sheet falls on the lens; a racing road seen from a water tower; a hot rod on a city street coming at the camera until its headlamp flares; a safe dragged on a chain with sparks.

What the rejected ones share: too many moving objects, things that change shape, cars that jump or point the wrong way, and everything turned up too high. So: one thing happens, it happens plainly, and everything else stays still.

# Web research

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

Write one still-image prompt per shot below for Google Flow's Nano Banana 2.1 (16:9). Each still will be the start frame of an 8-second video, and Jack judged the last one by how it moved, so build a frame that can move simply: few moving objects, cars already pointing the way they'll travel, nothing piled up or balanced that would have to change shape.

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web.
- Prohibition-era cars must be unmistakably period: tall upright bodies, separate mudguards, running boards, spoked wheels, upright windscreens.
- Never name a TV show, game, film, director, artist or real person. No children. No readable words anywhere. Weapons stay out of frame.
- The picture fills the frame edge to edge. Narrative prose. No quality buzzwords. Keep the colourful noir: saturated colour in paint, clothes and practical lights, with deep shadow, not everything turned up.

Write your output to `/home/jackt/projects/badcode/badcode/docs/stories/bank-robbery/songs/mv-colour-noir/cleanroom/n3.md`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots

## safe3
Jack's note: "ai slop there are cars on the river fix it". The car dragging a thread of sparks, seen from far above: the road and the water must be clearly separate, and everything that moves stays on a road. A view where no road crosses water is safest.
Images of what he saw: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/safe3-a.jpg
Last prompt: Seen from the catwalk of a rooftop water tower, looking steeply down over a corroded iron rail that crosses the lower right corner close to the lens and out of focus, a 1920s city an hour after sundown, with the last dull violet still in the sky off the top edge of the frame and only a sliver of it visible. Far below, a black canal cuts diagonally through crowded blocks of uneven height, and a narrow iron girder bridge crosses it. On that bridge a car no bigger than a grain of rice, its yellow paint only just readable under a passing lamp, is dragging a single thin bright thread of orange sparks that starts two streets back, follows the curve of the road around a corner and over the bridge, and fades to dull red as it cools. The canal holds a broken double of the thread: below the bridge the sparks and the lamps are shattered into short shaking bars on the water, dimmer than their sources. Behind the thread come three pairs of small white headlamps, closing, spaced unevenly. The surrounding rooftops are mostly dark, tar and water tanks and chimney stacks, with a few long skylights glowing amber, one rooftop painted in faded jade, and a row of bulb signs seen from behind so they show only as scaffolding and rows of dots, no letters. Thin coal smoke lies across one block and catches the light of a street below it. Nothing else in the city has noticed. A long-lens view with flattened layers of buildings, deep plum shadows, saturated film colour, a fine grain, filling the entire 16:9 frame without any margin.

## safe1
Jack's note: "the logo is in the wrong place on the balaclava otherwise its perfect". Keep the whole scene exactly. Fix only the mask: The mask, a fact of this film: a hand-knitted wool balaclava over the whole head with no eye or mouth holes; a thin wool ring stitched around the face; one small solid red felt triangle with rounded corners sewn high inside the ring, over where one eye would be. The approved image r2-mask1-b shows where the logo sits. The face must be turned far enough toward the camera to show it.
Images of what he saw: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/r2-safe1-a.jpg, /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/r2-safe1-b.jpg, /tmp/claude-1000/-home-jackt-projects-badcode-badcode/73bf0394-8c1a-47fb-b2e3-008f706c9a77/scratchpad/noir-picks/img/r2-mask1-b.jpg
Last prompt: The instant a small safe leaves a wall, seen from across a narrow back alley at night in 1928, the camera at chest height against the opposite wall with a rusted iron drainpipe cut off by the left edge of the frame. An egg-yolk yellow sedan with black mudguards stands at a hard angle on the right, its rear wheels spinning on wet-dark cobbles and throwing thick grey tyre smoke, lit deep red by its two small tail lamps. From its rear axle a heavy chain runs dead straight, rigid as a bar, across the alley and into a ragged hole in an oxblood brick wall with a flaking bottle-green painted band. The safe, a squat cast-iron box in chipped forest-green enamel with a brass dial, hangs tilted in the air a foot outside the hole with the chain wrapped around it, while bricks, mortar and pieces of green wall fall around it through a cloud of pale dust. One bare amber bulb in a tin shade above a wooden back door, high on the left, is the only other light, so the dust glows amber on one side and red on the other, and the far end of the alley drops into true black. A man leans far out of the sedan's rear window toward the camera, big enough in the frame to read clearly, dark overcoat collar turned up, both leather-gloved hands gripping the door, his head turned back over his shoulder to watch the hole so that the front of his mask faces us at three-quarters. His whole head is inside a hand-knitted balaclava of marine-blue wool, slightly uneven, with a ribbed neck tucked into the collar and continuous knit running unbroken across the place where eyes, nose and mouth would be. One thin ring of cream wool, chain-stitched by hand, circles the whole face from brow to chin. High inside that ring, above the eye nearer the camera and pushed up close against the cream stitching, sits one small triangular patch of solid red felt with rounded corners, the whole patch filled with flat red cloth and its hand-cut edge sewn down with tiny black running stitches. The rest of the ring's interior, including its centre, is bare blue knit. Falling bricks are slightly blurred, while the chain, safe and mask are sharp. Rich saturated colour film with visible grain and hard shadows on the brick, the picture running edge to edge across the whole 16:9 frame.

