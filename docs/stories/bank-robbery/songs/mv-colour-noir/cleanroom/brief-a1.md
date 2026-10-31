# What Jack said

# Jack, 2026-10-31, on `Colour Noir 1`

"so for the next sequence, please trim the clips and cut them to the beat, the clip at 23 secs should be redone it is ai slop two safes appear and morph, make it simple instead. ive cut the clip at 55 secs to where it should stop because afterwards it becomes ai slop, but before the cut it looks good so keep that part in the new sequence. all the band parts should be redone of them singing and lip syncing. all the lip syncing should be recut so that it actually lines up use the skills to do that. 2 mins 15 secs do this clip again the cars should be racing at high speed, not just going for a drive as it looks at the moment. i love all the lip syncing scenes of people singing, keep the themes settings and vibes, however there are duplicate people in almost all of them, please diversify them a bit too. please add the clips you have yet to make, add more lip syncing it should be sprinkled throughout, more action and fast cuts to the beat. please clean room the new stuff, reserach the internet on how to make it cool, in keeping with the vibe of it all, make it cinematic and cool. THanks."

# What Jack has said about clips so far, word for word

"so many barrels fall and morph and change alonside other objects, please just keep this one simple" · "the cars teleport" · "everything is so exaggerated please make it simple" · "there are cars on the river" · "it looks like a modern car" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one" · on the safe: "two safes appear and morph, make it simple" · on the race: "the cars should be racing at high speed, not just going for a drive".

So: the action is already happening in the still. In the clip, one plain thing moves. Everything else keeps its shape. Nothing enters or leaves the frame. Speed comes from what streaks past, not from the car changing place in frame.

# The film

A music video set in 1920s Prohibition America, in what we call colourful noir: saturated coloured light in deep shadow, glossy, lights and reflections everywhere, each shot with its own pair of colours. Cinematic and cool, real-looking, never cartoonish. It gets cut fast to the beat, so each shot plays one to four seconds.

# Web research

# Clean-room research, round 6 (web only, 2026-10-31)

Tags: [vendor] tool maker or a site selling tools. [practitioner] filmmaker, tester or researcher. [inference] my reasoning, untested. Pages were read through a summariser, and most AI-tool pages are SEO-grade. "Snippet" means seen in search results only, page not opened.

## 1. Where the energy comes from

**Cutting**
- About two-thirds of 329 music videos cut in time with the beat; performance videos lean to the bar; editors often anticipate the music slightly ([arXiv](https://arxiv.org/abs/2108.00970)) [practitioner, numbers from snippet].
- Identical clip lengths let viewers predict the cut ([No Film School](https://nofilmschool.com/2014/09/larry-jordan-teaches-us-how-create-video-montage-set-music)) [practitioner, snippet].
- Rapid cutting alone had "only limited" success on one filmmaker's chase. The speed must be inside the shot ([Oseman](https://neiloseman.com/?p=6289)) [practitioner].

**Speed is what passes near the lens** ([Oseman](https://neiloseman.com/?p=6289)) [practitioner]
- Near objects read faster: alleys, lamp posts, telegraph poles, hedges a foot or two from the car. Open road kills speed.
- Camera near the road, so the surface zips by.
- Long-lens pan: car held, background speed set by the pan.
- Let the car pass a static camera, or track toward it.
- Pools of light and shade flashing over the car. Coloured light bands on bodywork would suit this look [inference].

**Also**
- "Road rush": bumper height or lower, wide, slow shutter, lane lines and wet asphalt streaking; the road is the subject ([Melies](https://melies.co/cinematic-techniques/camera-movement/road-rush)) [vendor].
- *The French Connection*: bumper mount, shot at 18fps so the chase runs faster ([PremiumBeat](https://www.premiumbeat.com/blog/how-to-film-a-car-chase/)) [practitioner].
- *Ford v Ferrari*: low trailer shooting back at the driver with the track receding; side-on suction mounts ([PremiumBeat](https://www.premiumbeat.com/blog/ford-v-ferrari-cinematography-at-100-mph)) [practitioner].

**Frames for a 1 to 3 second cut** [inference]
1. Front wheel and running board fill the frame, wet cobbles smeared, red light raking the tyre.
2. Lens on the road, car tail ripping away, neon streaks on the wet surface.
3. Driver through side glass, coloured bands sliding over his face, world a blur.
4. Static kerb camera, lamp post by the lens, car gone in under a second.
5. Long-lens pan: car sharp, storefronts a coloured smear.
6. Tyre smoke across a low lens, headlamp burning through.

**Period:** bootleg cars were the hot rod's ancestors: cheap Model Ts and As and light roadsters, stripped and tuned to outrun police ([Wikipedia](https://en.wikipedia.org/wiki/Hot_rod)). Some famous "bootleg car" stories are really 1930 to 1933 ([forum, snippet](https://mail.jalopyjournal.com/forum/posts/11385089)).

## 2. High speed without warping

**Reported behaviour**
- Veo: write only motion, the image sets the rest. Camera motion over a static scene is "the simplest and most reliable" dynamism ([Google](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice)) [vendor].
- Omni: unprompted it may build a multi-shot sequence, so say "single continuous shot, no scene cuts" ([Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide)) [vendor]. Name the move, or the camera stays mostly static ([relayed Google tips](https://pasqualepillitteri.it/en/news/3513/mastering-gemini-omni-flash-video-prompting-guide)) [vendor].
- "Consistency can drift during big scene changes or fast camera moves" ([Atlabs](https://www.atlabs.ai/blog/ultimate-gemini-omni-flash-prompting-guide-2026)) [vendor]. Camera and physics prompts "sometimes even alter the geography of the shot"; object-on-object works "roughly 50/50"; violent contact is dampened ([InVideo review](https://invideo.io/blog/gemini-omni-flash-review/)) [practitioner].
- Jitter comes from competing micro-motions (rain, crowds, foliage): ask for "stable background, motion isolated to subject". Smear is speed plus texture. Fast zooms warp. Cue: "crisp edges during movement" ([CrePal](https://crepal.ai/blog/aivideo/veo-motion-controls-ai/)) [practitioner, informal].
- Grounded moves only (tracking, low reveal, road-level pass). Check tyres, reflections, proportions and road contact on every take ([Dreamina](https://dreamina.capcut.com/ai-video/cinematic-ai-car-videos-realistic)) [vendor].
- If the object's shape changes, regenerate; do not patch ([Laozhang](https://blog.laozhang.ai/en/posts/fix-logo-distortion-ai-product-video.md)) [practitioner, about logos].
- Shared prompts use "motion blur on fast wheels, realistic wheel motion", negative "deformed vehicle, extra wheels" ([Carat](https://carat.im/en/prompt-gallery/traffic-video)) [practitioner, unproven].

**What to do** [inference]
- Hold the car nearly still in frame and move the world. A camera at matching speed leaves the car's pixels barely changing, so there is little to redraw.
- Avoid cars crossing frame, overtaking or swerving: each forces the model to invent unseen bodywork. Teleports likely start there.
- One speed source per clip: road, or lamp posts, or wall. No traffic, no pedestrians.
- Close framing needs no whole-car geometry: wheel arch, bonnet, driver.
- Generate at a speed the model holds, then take the cleanest 1 to 3 seconds and speed up 130 to 200% in the edit, adding shake and directional blur there.
- Cut hard to a new angle instead of asking for position continuity.

Example: "Single continuous shot, no scene cuts. Camera travels low alongside the car at matching speed, holding the same framing. The wet road and lamp posts streak past in motion blur. The car keeps its exact shape and stays in place in frame. No other vehicles. Engine roar, tyre hiss on wet cobbles."

## 3. A crew of different people

**Craft**
- Nano Banana 2: reliable at 4, often 5; at 6 or more, face merging and limb errors with any model ([Morphed](https://morphed.app/blog/nano-banana-prompts-for-friends)) [practitioner, one site, no method]. Same source: a distinct action each is the biggest lever; placement beats "five together"; vary height and depth; 30 to 50 words, as instructions past about 60 may be ignored. For 5 or more: two sharp faces, the rest blurred, silhouetted or back-turned.
- Attractiveness words pull faces together; describe face shape, brow, eye spacing, nose bridge, jaw, age, skin ([Higgsfield](https://geo.higgsfield.ai/blog/recommended/why-does-my-ai-character-s-face-keep-changing-every-generation-8108c5)) [vendor].
- In video, "four or more tracked subjects merge or drift" ([Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide)) [vendor].

**Writing it** [inference]
- Vary what cannot average out: decades of age (19, 35, 58), build (bull-necked, rake-thin, heavy-bellied), nose, ears, scar, baldness, teeth, glasses, one man in the wrong clothes. Skip "handsome", "rugged".
- Give each a place and job. Three or four faces; everyone else in the coloured dark.
- For a whole band or gang, shoot several stills of 2 to 3 people and let the cut build the group.

**Who was there**
- Gangs mostly organised by ethnicity out of poor immigrant districts; Prohibition leaders "crossed ethnic, racial, and geographical lines" ([EBSCO](https://ebsco.com/research-starters/history/gangsters-prohibition-era)).
- Chicago's North Side Gang: mainly Irish American, with German, Polish, Jewish and Italian American members ([Wikipedia](https://en.wikipedia.org/wiki/North_Side_Gang)).
- Detroit's Purple Gang: predominantly Jewish hijackers ([Wikipedia](https://en.wikipedia.org/wiki/Purple_Gang)).
- Harlem: Stephanie St. Clair, a Black woman, ran a numbers bank with Bumpy Johnson as lieutenant ([Mob Museum](https://themobmuseum.org/notable_names/stephanie-st-clair/)). Numbers, not bootlegging.
- Texas Guinan, Helen Morgan and Belle Livingstone led New York nightlife; Guinan had gangster backing and her clubs barred Black patrons ([Wikipedia](https://en.wikipedia.org/wiki/Texas_Guinan)) [snippet].
- Cotton Club (Owney Madden): Black musicians onstage, Black patrons barred ([Stanford](https://news.stanford.edu/stories/2015/05/stanford-music-scholar-redefines-the-jazz-and-cabaret-culture-of-1920s-harlem)).
- Black and tan clubs were the mixed rooms ([Wikipedia](https://en.wikipedia.org/wiki/Black_and_tan_clubs)). A Black band before a mixed crowd there is honest. An integrated band on one stage would be unusual [inference, no source].

## 4. A believable sung performance

- Single-speaker sync holds 6 to 7 seconds; several people talking is "a major weakness" ([InVideo](https://invideo.io/blog/gemini-omni-flash-review/)) [practitioner].
- Wide and medium hide errors; tight close-ups need frame checks; tie a line to a visual description ("the man in the red coat"), as the model has no names ([Prompt Architects](https://prompt-architects.com/blog/101-veo-dialogue-prompts)) [practitioner].
- Use only "says" or "sings" as the verb ([Solovev](https://cy.linkedin.com/in/nicksolovev)) [practitioner, snippet]. Nothing found tests singing on Omni; vendor claims of perfect sync are contradicted by reviews.
- Omni takes no uploaded audio reference ([Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide)) [vendor]. Exact sync to a track is reported as hard, handled by a separate tool ([Trilogy AI](https://trilogyai.substack.com/p/ai-music-videos)) [practitioner].
- Hype Williams used extreme wide lenses to make performers larger than life, set contrast through colour in wardrobe and set, and on one clip moved a hard source across faces in time with the music ([American Cinematographer](https://www.oocities.org/hypepaul/articles/acin0107.html)) [practitioner].

**Recipes** [inference]
- Face a third to half of frame height, low wide lens: the mouth reads but cannot be audited.
- One short phrase per clip, early in the clip: "He sings hard into the lens, leaning in, neck straining, jaw wide: '[line]'". Effort sells it: chest, breath, veins, sweat under a coloured backlight.
- Gang vocal: no sync. Three men shouting one word on a downbeat, heads back.
- Instruments: hands and horn bell in foreground, player behind. A horn covers the mouth, so no sync at all. Cut before fingers fail.

## 5. Keep a prop shot simple

- Motion only, general nouns ([Google](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice)) [vendor]. One camera move ([EachLabs](https://www.eachlabs.ai/blog/image-to-video-prompt-guide-best-practices-for-realistic-results)) [vendor].
- Nothing found addresses duplicates directly. The rest is [inference]:
- Still: one safe, chain and car all whole, on an empty road, with no boxes, cases or other cars for the model to copy.
- Camera moves with the prop so it never leaves frame; exits and re-entries are where pop-ins start.
- Prompt: "Single continuous shot. Camera moves low alongside at matching speed. The chain drags the safe along the road, bouncing. Sparks spray where it scrapes. Nothing else enters the frame."
- If sparks run wild, generate few and add a stock sparks layer in the edit.
- Reject any take where the count changes. Use 1 to 2 seconds.

## Gaps

No tested source for Omni with vehicles, wrong-way wheels, pre-blurred start frames (keep the car sharp in the still until tested), or Omni singing versus speaking.

# Your task

Action shots with no singing. Write a still and a motion prompt per shot, and use the research on speed and on keeping props simple. A fast cut uses one to three seconds. Exactly the number of cars, safes and people named, and say so in the motion prompt.

The robbers' masks:

The masks are BadCode's own, from its show. Facts: the whole head is in a hand-knitted wool balaclava with no eye holes and no mouth hole, so no skin and no eyes show; collars up and gloves on, so no skin shows anywhere on a robber. The logo is the face: one thin ring stitched in wool around the face, and high inside that ring, over where one eye would be, one small solid red felt triangle with rounded corners, sewn on, pushed up near the ring's edge and well away from the centre. In the show it is cream wool, a black ring and red felt. The two faults so far: the triangle drifts to the centre, and it sometimes comes back as an outline instead of solid. Nobody could wear a logo on the forehead: that was the mistake in the last round.

- `safe1`. A car pulling a safe out of a wall. There was a clip: a yellow 1920s sedan in a brick alley under one lamp, a masked driver leaning out of the window, a chain to one small green safe. It went wrong because two safes appeared and morphed. Make it simple: exactly one safe, chain tight, it slides out of the broken wall and across the cobbles. Nothing else. A locked camera.
- `rods4`. Two old-school 1920s hot rods, one teal, one black, racing flat out down a concrete river channel under arched bridges at dusk. Jack's words on the last one: 'the cars should be racing at high speed, not just going for a drive'. Use the research on speed. Close to the car, the world tearing past. Exactly two cars and they keep their shape.
- `a1`. A chase: the front wheel and running board of a 1920s car fill the frame, wet cobbles smeared under it, red light raking the tyre.
- `a2`. A chase: lens almost on the road, the tail of a 1920s car ripping away from us, neon streaks on the wet surface.
- `a3`. The getaway driver seen through the side glass at full speed, bands of coloured light sliding over his face, the world outside a blur. He is a sharp-faced man of about 30, gloves on the wheel, and his mouth is shut.
- `a4`. A static kerb camera with a lamp post beside the lens: a 1920s roadster blasts past and is gone in under a second, spray hanging.
- `a5`. A long-lens pan on a 1920s roadster at speed: car sharp, the lit storefronts behind a coloured smear.
- `a6`. Tyre smoke rolling across a low lens on a dark street, one 1920s headlamp burning through it, a car just about to leap off.
- `a7`. A robber in a BadCode balaclava fires a Thompson straight up at a bank's ornate ceiling: muzzle flash lights the wool, plaster dust drifts down, marble behind.
- `a8`. Two robbers in BadCode balaclavas run out of a bank's brass doors toward the lens carrying sacks, alarm lamp flashing red and white behind. Just the two.
- `a9`. The back seat of an open touring car at full speed at night: a robber in a BadCode balaclava holds a split sack and banknotes pour away behind the car into the coloured dark.
- `a10`. A police motorcycle rider of the 1920s, big and close beside us at speed, seen from a car's running board, his red lamp flaring, street lights streaking.
- `a11`. Lens low beside one small green safe being dragged on a chain down a cobbled street at speed: only the safe, the chain, and a wide fan of sparks, the road a streak.
- `a12`. A flatbed printing press close-up in a cellar: sheets of banknotes flying through it, flames reflected in the steel. The printer is burning.
- `a13`. First person, from the driver's seat of a 1920s roadster: gloved hands fight the big wheel, a wet night street with neon pouring toward us, the bonnet vibrating.
- `a14`. Night, a level road beside a dark river: two 1920s black sedans side by side at speed in long lens, door to door, sparks where they touch, lights streaking behind.

# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, director, artist or real person in a prompt. No children. No readable words anywhere in the picture.
- Guns are allowed as held, period Thompsons and revolvers, pointing up or away, never at the camera or at anybody. Nobody is wounded and there's no blood. Violence is property: glass, barrels, cars, fire, sparks, money.
- Period-correct 1920s cars, clothes, hats and lights. The picture fills the frame edge to edge.
- Each shot differs from the others in angle, lens and light. Natural prose, no quality buzzwords, about 60 to 130 words for a still.
- MOTION is an image-to-video prompt, under 50 words, starting with what the camera does, then one plain thing that moves.

Write your output to `/home/jackt/projects/badcode/badcode/docs/stories/bank-robbery/songs/mv-colour-noir/cleanroom/a1.md`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
MOTION: <motion prompt>
SECONDS: <4 or 6>
WHY: <one sentence>

Then reply with one line saying it is done.
