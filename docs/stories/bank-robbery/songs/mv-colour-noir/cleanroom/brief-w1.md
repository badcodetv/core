# What Jack said, word for word

please go to the bank robbery music video. lets forget the psychedelic styles, but keep the cool transitions if you know what i mean, but make them realsitic instead of trippy. lets make it like a colourful noir, basically the Fat Tony's den from the Simpsons vibe, and Shadows Of Evil from Black Ops 3. lets do lip syncing but the lip syncing comes from the conversations, so they talk the lyrics, the speakeasy bands sings the chourus/some of the song. their could be that same band singing under a bridge at night with the city lights reflecting off the water, the healights of the  cars illuminating the band, gangster style. it should be fast and full of car chases, i liked the first person car thing from the last one, maybe we follow that person throughout, not as a main theme just as one of many stories playing out. maybe a compilation of robberiers, like a car pulling a small safe out of a wall and it being dragged behind them with sparks flying as they flee the cops. balaclavas with the badcode logo on them, with people getting robbed. panning shots of pretty prohabition era cities with lights and refelections, interesting shots, not just the same old ai slop. maybe have old school hot rod racing.

please save this to the right file, lets just do the general shots, and we'll worry about lip syncing later. things i didnt like about the last sequence of the bank robbery music video were the ai slop, pschedlic transitions, the blue and red scarf/teams, the bakers walking in randomly, the story in general, i think lets just make a bunch of cool stuff instead then we'll make it make sense later. please get started with the stills and use the new scene thing. i dont want to have to remind you about the same prompt being made bug over and over, so what do i say so that you are aware of that, and only use interenet research (please research the internet to on how to make this in nano banana 2.1) Thanks.

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

# Your task

Write FOUR still-image prompts for Google Flow's Nano Banana 2.1 (16:9) on this one subject: **the speakeasy den and its band**.

The secret den where the mob and the band live: colourful noir, the heart of the look. Include the band in at least two of your four shots. Faces with closed mouths or mid-breath for now: a wide-open singing mouth gets refused by the engine, and lip sync comes later.

The band (the same people wherever they appear): five musicians in sharp 1930s gangster clothes: a very tall thin man on upright bass, a stout older man on trumpet, a young man on clarinet, a grey-haired woman on a small drum kit, and a broad woman in her forties with a silver streak in her black hair, who fronts the band at a period microphone.

Rules of the job:
- Read nothing on this computer apart from this brief. You may search the web yourself, especially for real photographs and film references of your subject.
- These are not a story. Jack wants "a bunch of cool stuff": each shot should stand on its own and make someone stop and look. Your four must differ from each other in place, vantage, scale and light.
- Everything Jack dislikes is in his words above. Don't describe those things, even to ban them.
- Write the look as visual traits. Never name a TV show, game, film, director, artist or real person in a prompt. The engine won't obey it, and we can't use it.
- No children in frame. No readable words anywhere: signs, plates and labels stay blank or illegible.
- Weapons stay out of frame. Never one pointed at a person.
- Known engine trap: the word "photograph" can give a baked-in cream border, so make sure your wording gives a picture that fills the frame edge to edge.
- Narrative prose, as long as the picture needs. No quality buzzwords.
- For each shot, also say one realistic way out of it into another shot when it's cut (a real transition, no trickery: a pillar passing the lens, a whip pan, a match on a shape or a light).

Write your output to `/home/jackt/projects/badcode/badcode/docs/stories/bank-robbery/songs/mv-colour-noir/cleanroom/w1.md`, exactly in this format and nothing else:

=== SHOT <n> ===
<the prompt>
WAY OUT: <one sentence>
WHY: <one sentence>

(repeat for all four, then reply with one line saying it is done)
