# Magic Money Tree — Jack's version: look tests

**Whose this is:** Jack's. Kai is drafting his own version separately (the "both bring a version"
plan in [`direction-2026-10-01.md`](./direction-2026-10-01.md)). Everything here belongs to Jack's
pass, [`storyboard-loose-2026-10-01.md`](./storyboard-loose-2026-10-01.md).

| | |
| --- | --- |
| **Flow project** | `magic money tree jack` — id `cb27208c-4b16-426d-9144-c394f2735c15` |
| **Flow's own name for it** | `Oct 01 - 17:36`. The rename did not take from code (a known Flow limit), so it needs renaming by hand in the Flow window |
| **Images** | In the Flow project only. Jack, 1 October: "don't save them in a folder, I just mean remember the prompts" |
| **Status** | Style test only. Nothing here is approved, and no soldier design is locked |

## Round 1 — the soldier at Dunkirk, seven styles (1 October 2026)

Jack's brief: "a kind of noir, glossy, DLSS 5, realistic style that is artistic and cinematic."
The subject is held identical in every prompt so that the style is the only thing that changes.

### The shot (scene 5)

- **Job:** put one face on the war. It is the same face we later see in the chair.
- **Register:** human scale, not monumental.
- **Foreground:** wet sand and an abandoned steel helmet.
- **Midground:** the soldier, about twenty, waist up, soaked, looking up past the camera.
- **Background:** a long line of men wading out into the sea; a column of black smoke.
- **Focal point:** his face, won by light.
- **Light:** a low sun behind him to the left, coming through the smoke, catching the rim of his
  helmet and his wet shoulders, and bouncing back up off the wet sand.
- **Camera:** just below eye level, medium close-up, normal lens.
- **Withheld:** whatever he is looking up at.
- **The cost in frame:** exhaustion, and the kit other men have left behind.

### The subject block (same in all seven)

> A British infantryman of about twenty stands on a wide beach in northern France in the summer of
> 1940, seen from the waist up, just below his eye level. He wears a soaked wool battledress and a
> wide-brimmed steel helmet, and he is exhausted, unshaven and smeared with oil and salt. He looks
> up past the camera at something in the sky that we do not see. In the foreground an abandoned
> steel helmet lies on the wet sand. Far behind him a long line of soldiers wades out into a grey
> sea, and a tall column of black smoke rises from the town on the horizon. A low sun behind him
> to the left comes through the smoke, catches the rim of his helmet and his wet shoulders, and
> reflects off the wet sand up into his face.

### The seven styles

| # | File | Style | The style sentence added to the subject block |
| --- | --- | --- | --- |
| 1 | `01-platinum-noir.jpg` | Glossy modern black-and-white noir | Glossy modern black-and-white cinema, photographed like a platinum print: knife-sharp contrast, very fine greys, soft pearly blacks, deep focus, clean large-format digital sharpness, no grain. |
| 2 | `02-hard-period-noir.jpg` | 1940s British hard noir | A late-1940s British black-and-white thriller: one hard light, deep black shadows cutting across his face, a slightly tilted frame, coarse 35mm grain, wet surfaces shining. |
| 3 | `03-glossy-colour-realism.jpg` | The "DLSS 5" qualities, in colour | Ultra-realistic glossy colour, like the best real-time neural rendering: light scattering through skin, hair glowing where the sun is behind it, tiny shadows in the wool, wet materials gleaming, deep shadows kept dark. |
| 4 | `04-cold-neo-noir.jpg` | Cold colour neo-noir | Modern neo-noir in colour: a cold steel-blue world with one warm orange glow from the fires behind him, anamorphic lens, shallow focus, heavy atmosphere. |
| 5 | `05-forties-colour-film.jpg` | 1940s colour film | Early-1940s colour reversal film: rich, slightly faded dyes, deep reds and khakis, soft highlights, gentle grain. |
| 6 | `06-newsreel-match.jpg` | Matches the real archive | A real 1940 newsreel frame: soft black-and-white 35mm, low contrast, heavy grain, slight gate weave and scratches, nothing polished. |
| 7 | `07-ink-noir.jpg` | Graphic ink noir | Graphic-novel noir: near-pure black and white with almost no grey, shapes cut out by light, his face half lost in solid black, one thin white rim of light. |

Every prompt ends with "Thanks." Model: Nano Banana 2 (free tier), 16:9, one candidate each.

### Results

All seven generated. Jack's verdict: **no black-and-white** — "they look all the same". That rules
out styles 1, 2, 6 and 7. No verdict given on the three colour ones (3, 4, 5).

## Round 2 — colour only, eight styles (1 October 2026)

Same shot and same subject block as round 1. Style 4 is set at dusk, so its light sentence replaces
the low-sun sentence at the end of the subject block.

| # | Style | The style sentence added to the subject block |
| --- | --- | --- |
| 1 | Technicolor noir | A 1940s three-strip Technicolor melodrama lit like a noir: saturated, lush colour, hard studio-style light, deep shadows, glowing skin, rich reds and blues. |
| 2 | Bleach-bypass war film | A bleach-bypass war film: colour drained to a silvery khaki and steel, harsh contrast, crushed blacks, sharp gritty detail, a fast shutter that freezes every drop of spray. |
| 3 | Large-format epic | A modern large-format 65mm war epic: crisp, natural colour, enormous clean detail, cool sea greys against warm skin, glossy and restrained. |
| 4 | Fire-lit dusk noir | Colour noir at dusk: the sky almost black, the only light the amber glow of the burning town behind him, glossy wet highlights on his helmet and shoulders, his face lit warm from one side and falling into black on the other. *(Replaces the low-sun sentence.)* |
| 5 | War-artist oil painting | A realistic oil painting by an official war artist of the 1940s: visible brushwork, muted earth colours, a heavy sky, the weight and stillness of a museum canvas. |
| 6 | Game cinematic | A cinematic cutscene from a big-budget video game with ray-traced lighting: hyper-detailed skin and wet cloth, glossy reflections, dramatic rim light, deep contrast, rich colour. |
| 7 | Sickly sodium neo-noir | A modern neo-noir with a sickly yellow-green grade: low-key light, deep clean blacks, glossy digital sharpness, everything tinted the colour of old sodium street lamps. |
| 8 | Two-colour poster | A graphic two-colour image in only deep crimson and black: bold shapes, strong silhouette, the smoke and the sea as flat fields of red, like a striking film poster. |

Every prompt ends with "Thanks." Model: Nano Banana 2 (free tier), 16:9, one candidate each.

### Results

All eight generated. Jack's verdict: "all of these are basically the same."

**Why, as far as we can tell (not tested):** every prompt carried the same long subject block, so
the framing, the pose and the light were identical, and one style sentence at the front only
changed the colour grade. Round 3 lets the framing change with the style.

## Round 3 — realistic video-game styles, nine of them (1 October 2026)

Jack: "let's try realistic video game styles like GTA and The Last of Us."

What the research said about how these games look:

- **GTA V / GTA VI:** deliberately not photoreal. Rockstar: "the goal is not to be realistic, it's
  to feel realistic." Saturated colour, glossy reflections, dramatic sunsets, hyper-detailed
  close-ups. The loading-screen art is a separate, bold painted-illustration style.
- **The Last of Us Part II:** overcast, ambient light, muted colour, with soft shadows painted in
  by hand so that a flat grey day still has shape.
- **Red Dead Redemption 2:** lit after 19th-century landscape painters. Hazy skies, glowing shafts
  of light, a small figure in a huge landscape.
- **Ghost of Tsushima:** "we didn't go for hyper-realism." Bold colour and strong light, like a
  painting.
- **Hellblade II:** the opposite: as photoreal as a game gets, with a film-like wide frame.
- **Death Stranding:** photoreal, cold, clean and empty.

Same scene every time: the young British soldier on the beach at Dunkirk, 1940, exhausted, the
line of men wading out to sea, the black smoke over the town. The framing now changes per style.

| # | Style | Prompt |
| --- | --- | --- |
| 1 | GTA loading-screen art | A bold painted illustration in the style of Grand Theft Auto loading-screen artwork: thick dark outlines, flat cel-shaded colour with hard-edged shadows, saturated warm palette, a confident hero pose. A young British soldier of 1940 in a steel helmet and soaked battledress stands three-quarter view on the beach at Dunkirk, rifle slung, staring off to one side. Behind him, simplified into graphic shapes, a line of soldiers wades into the sea and black smoke rises over the town. Thanks. |
| 2 | GTA VI stylised realism | An in-game screenshot in the style of Grand Theft Auto VI: stylised realism, not a photograph. Saturated colour, a dramatic orange and pink sunset sky, glossy reflections on wet sand, hyper-detailed skin and cloth with a slightly heightened, larger-than-life look. A young British soldier of 1940 in a steel helmet and soaked battledress stands on the beach at Dunkirk, medium shot, exhausted, looking out to sea. Behind him a long line of soldiers wades into the water and black smoke rises over the town. Thanks. |
| 3 | The Last of Us Part II | An in-game screenshot in the style of The Last of Us Part II: third-person camera just behind and over the right shoulder of the character. Overcast ambient light, a muted grey-green palette, soft sculpted shadows, gritty worn textures on cloth and metal, realistic game-rendered skin. A young British soldier of 1940 in a steel helmet and soaked battledress walks along the beach at Dunkirk, seen from behind, his face turned in profile. Ahead of him a long line of soldiers wades into a grey sea, abandoned kit litters the sand, and black smoke rises over the town. Thanks. |
| 4 | Red Dead Redemption 2 | An in-game screenshot in the style of Red Dead Redemption 2: a wide painterly landscape lit like a 19th-century romantic oil painting, hazy glowing sky, long shafts of golden light through smoke, soft atmospheric distance. A young British soldier of 1940 in a steel helmet and battledress stands small in the lower third of the frame on the vast beach at Dunkirk, seen full length from behind. Far ahead a long line of soldiers wades into the sea, and a huge column of black smoke rises over the town and spreads across the sky. Thanks. |
| 5 | Ghost of Tsushima | An in-game screenshot in the style of Ghost of Tsushima: bold, vivid colour and strong directional light, like a painting in motion. Wind blows sand, smoke and scraps of paper across the frame. A young British soldier of 1940 in a steel helmet and battledress stands in a low wide shot on the beach at Dunkirk, his greatcoat blown sideways by the wind, a deep red sunset behind the black smoke of the town. A line of soldiers wades into a gleaming sea. Thanks. |
| 6 | Hellblade II | An in-game screenshot in the style of Senua's Saga: Hellblade II: ultra-photoreal real-time rendering in a very wide letterboxed frame. An extreme close-up of the face of a young British soldier of 1940 under the brim of a steel helmet, every pore, bead of water and smear of oil visible, his eyes wide and fixed on something above the camera. Dark, cold, heavy volumetric smoke drifting behind him, the beach at Dunkirk only a blur of figures and fire. Thanks. |
| 7 | Death Stranding | An in-game screenshot in the style of Death Stranding: cold, clean, photoreal rendering with a desaturated grey-teal palette and a strange calm. A very wide shot of an immense, almost empty beach at Dunkirk in 1940 under a flat pale sky. A single young British soldier in a steel helmet and battledress stands tiny in the middle distance, alone, facing the sea. Far off, a thin line of soldiers wades into still water, and one tall black column of smoke rises straight up. Thanks. |
| 8 | Battlefield V | An in-game screenshot in the style of Battlefield V: a wide-angle action frame full of particles, with flying sand, drifting embers, spray and thick smoke, in a punchy orange and teal grade with bright lens flare. A young British soldier of 1940 in a steel helmet and battledress runs toward the camera along the beach at Dunkirk, low angle, mouth open, other soldiers scattering behind him, a pillar of fire and black smoke over the town. Thanks. |
| 9 | L.A. Noire | An in-game screenshot in the style of L.A. Noire: a 1940s period crime game in rich warm colour, with slightly waxy motion-captured faces, crisp hard sunlight and long shadows. A medium two-shot on the beach at Dunkirk in 1940: a young British soldier in a steel helmet and battledress sits on an ammunition crate lighting a cigarette, another soldier standing beside him looking out to sea, where a line of men wades into the water under black smoke. Thanks. |

Model: Nano Banana 2 (free tier), 16:9, one candidate each.

### Results

Jack, part-way through the run: "These are cool, please do more varied styles." No single
favourite named yet.

Eight of nine generated. **Style 9 (L.A. Noire) was refused by Flow's content filter.** The likely
trigger is "lighting a cigarette" or "ammunition crate"; which one is not tested. It was rewritten
without either (he sits on a wooden crate with his head bowed; "crime game" became "detective
game") and re-run as the eleventh prompt of round 4.

## Round 4 — wider game styles, ten of them (1 October 2026)

Further from photoreal on purpose: noir games, painterly games, comic-shaded games and retro
consoles. Same scene; the framing changes with each.

| # | Style | Prompt |
| --- | --- | --- |
| 1 | Alan Wake 2 | An in-game screenshot in the style of Alan Wake 2: a dark, moody noir horror game. Night on the beach at Dunkirk in 1940, thick fog, a single hard torch beam cutting through it, deep teal shadows and one harsh red glow from the burning town. A young British soldier in a steel helmet and battledress stands in the torchlight, medium close, looking over his shoulder, film grain and a slight double-exposure ghosting at the edges of the frame. Thanks. |
| 2 | Max Payne 3 | An in-game screenshot in the style of Max Payne 3: sweaty, saturated, sun-bleached colour with heavy digital glitch, with colour fringing, scan lines and a split-second double image. A young British soldier of 1940 in a steel helmet and battledress, seen from a low side angle, crouches behind a wrecked lorry on the beach at Dunkirk, jaw tight, sand and sweat on his face. Behind him soldiers wade into the sea under black smoke. Thanks. |
| 3 | Cyberpunk 2077 | An in-game screenshot in the style of Cyberpunk 2077 with path-traced lighting: extremely glossy, every wet surface a mirror, deep blacks and intense coloured light. Night on the beach at Dunkirk in 1940, the burning town throwing orange and magenta reflections across wet sand, oil-slicked water and the steel helmet of a young British soldier in battledress, seen in a tight low-angle shot looking up at him. A line of soldiers wades into the glittering sea behind him. Thanks. |
| 4 | Disco Elysium | A painted portrait in the style of Disco Elysium: loose, expressive oil brushwork, smeared and scraped paint, strange off-key colours, a face built from bold strokes rather than detail. A young British soldier of 1940 in a steel helmet and battledress, head and shoulders, exhausted, against a smeared background of the beach at Dunkirk, a line of men in the sea and black smoke over the town. Thanks. |
| 5 | Dishonored | An in-game screenshot in the style of Dishonored: a painterly stylised 3D world with exaggerated angular faces, long jaws and heavy brows, hand-painted textures, and a muted palette of grey-blue and rust. A young British soldier of 1940 in a steel helmet and battledress stands in a medium shot on the beach at Dunkirk, gaunt and sharp-featured, a line of soldiers wading into the sea and black smoke over the town behind him. Thanks. |
| 6 | Comic-shaded (The Walking Dead game) | An in-game screenshot in the style of Telltale's The Walking Dead: 3D characters shaded like a comic book, with heavy black ink outlines, rough hatching in the shadows and flat muted colour. A young British soldier of 1940 in a steel helmet and battledress, medium close-up, turns to look at the camera on the beach at Dunkirk, worried, with a line of soldiers wading into the sea and black smoke over the town behind him. Thanks. |
| 7 | Arcane | A frame in the style of the animated series Arcane: 3D characters with hand-painted textures, visible brush strokes on skin and cloth, dramatic coloured rim light, rich teal shadows against warm orange firelight. A young British soldier of 1940 in a steel helmet and battledress, close-up in three-quarter view on the beach at Dunkirk, eyes shining, embers drifting past, soldiers wading into the sea and the town burning behind him. Thanks. |
| 8 | PlayStation 1 | An in-game screenshot from an original PlayStation game of 1998: very low-polygon 3D models, warped low-resolution pixelated textures, no smoothing, jagged edges, dithered colour and distance fog. A blocky young British soldier of 1940 in a steel helmet and battledress stands on the beach at Dunkirk, a row of blocky soldiers in a flat grey sea behind him and a crude column of black smoke over the town. Thanks. |
| 9 | PlayStation 2 (GTA: San Andreas) | An in-game screenshot in the style of Grand Theft Auto: San Andreas on the PlayStation 2: simple low-detail 3D models, blurry textures, a thick orange heat haze over everything, short draw distance. A young British soldier of 1940 in a steel helmet and battledress stands on the beach at Dunkirk in a third-person view from behind, a line of simple soldier figures wading into the sea and black smoke over the town. Thanks. |
| 10 | Valiant Hearts | A frame in the style of the game Valiant Hearts: a flat 2D hand-drawn comic, side-on view, thick outlines, simple shapes, characters with their eyes hidden under their helmets, a limited palette of khaki, grey-blue and ochre. A young British soldier of 1940 walks along the beach at Dunkirk past abandoned kit, a line of soldiers wading into the sea in the background and a curl of black smoke over the town. Thanks. |

Model: Nano Banana 2 (free tier), 16:9, one candidate each.

### Results

All ten generated, and the reworded L.A. Noire passed the filter. Jack: "The styles look too much
like AI slop."

## Round 5 — realistic game styles, rebuilt against the "AI slop" look (1 October 2026)

Jack: "The styles look too much like AI slop." Asked for: varied realistic video-game styles, the
slop look avoided, prompts tuned for Nano Banana Pro, and the cinematography notes used.

**What was wrong with rounds 1 to 4** (seen in the round 3 results): an orange sunset in most
frames, the soldier dead centre, everything evenly lit and sharp, tidy rows of identical men, and
made-up game menus and captions on screen. That is the bundle `docs/cinematography/symptoms.md`
lists under "it looks like AI".

**What changed, and where each rule comes from:**

- One named light source per frame, with where its shadow falls. No sunsets. (`frame.md` §5; `docs/google-flow/nano-banana-2.md`, "do not stack lighting ideas")
- The soldier is off centre, caught doing something, with an object blurred across the foreground. (`symptoms.md`; the anti-slop table in `nano-banana-2.md`)
- Details that could only be Dunkirk: lorries driven into the sea as a pier, men digging in with their helmets, the timber jetty.
- Background men are counted and each is different, so they do not clone.
- Faces are described by what the muscles are doing, never by the emotion. (`docs/flow/image-prompting.md` §4a)
- None of the words that trigger the glossy look: cinematic, photorealistic, hyper-realistic, epic, 8K.
- Labelled sections with the job stated first, which is the shape Google documents for Nano Banana Pro.
- One closing constraint: the game's interface is hidden, and the frame is accurate for May 1940.

**Model:** Nano Banana Pro, 16:9, one candidate each. There is no model called "Nano Banana Pro 2"
in Flow; Pro is the one that plans complicated frames best. Pro is not free: about 12 credits an
image by a third-party figure we have not checked in the app, so about 108 for this round.

Every prompt ends with the same block:

```
Constraints: the game's interface is hidden, so there is no on-screen text, subtitle, map, marker or health bar anywhere. Historical accuracy for the British Army in France in late May 1940.

Compose for a 16:9 frame.

Thanks.
```

### 5.1 The Last of Us Part II

Overcast, hand-shaped soft shadows, a quiet moment.

```
Generate a photo-mode capture from the video game The Last of Us Part II.

Subject: a British infantryman of about twenty sits on the sand with his back against the front wheel of an abandoned army lorry, unlacing one sodden boot. Khaki wool serge battledress dark with seawater, canvas webbing, a steel helmet with a chipped rim pushed back on his head. Half-lidded eyes that are slow to track, mouth flat and slightly open, three days of stubble, a smear of engine oil across one cheekbone.

Environment: the beach at Dunkirk at low tide. Beside him in the sand lie a tin mug, a gas-mask bag and a single dropped boot. Far behind him, soft with distance, a queue of men stands waist-deep in a grey sea.

Camera: knee height, 35mm, a few feet from him and not quite level. The lorry's rusted mudguard crosses the left third of the frame, dark and out of focus. He sits right of centre.

Lighting: a flat overcast noon with no sun and no cast shadows. The only shape comes from the soft dark under the lorry and under the brim of his helmet.

Details: real-time game rendering with a muted grey-green palette, worn cloth and rusted metal, soft contact shadows in every crease.
```

### 5.2 Red Dead Redemption 2

Wide, hazy, painterly distance, a small figure.

```
Generate a photo-mode capture from the video game Red Dead Redemption 2.

Subject: a British infantryman of about twenty walks away from the camera along the tideline, small in the lower left third of the frame, rifle slung, helmet hanging from one hand, boots leaving a wavering line of prints in wet sand.

Environment: the beach at Dunkirk at dawn. Ahead of him a row of army lorries has been driven nose to tail out into the shallows to make a pier, and a thin file of men walks along their roofs toward a small boat. Scattered across the sand are abandoned bicycles, crates and a field kitchen on its side. A broad smear of oil smoke lies across the whole sky from the right.

Camera: standing height on top of a dune, wide lens, with blades of marram grass blurred across the lower right corner.

Lighting: the sun is a pale white disc low on the left, seen through the smoke haze. Long soft shadows fall to the right. Each layer of distance is paler and bluer than the one in front.

Details: real-time game rendering, with a landscape lit like a nineteenth-century oil painting, soft sea mist and muted khaki, pewter and bone colours.
```

### 5.3 Kingdom Come: Deliverance II

Plain daylight, scanned-from-life textures, unglamorous.

```
Generate an in-game capture from the video game Kingdom Come: Deliverance II, with its plain naturalistic look, moved to the year 1940.

Subject: a British infantryman of about twenty kneels in a sand dune scooping out a shallow hole with his own steel helmet, caught mid-scoop with sand pouring off the rim. Sleeves pushed up, khaki wool battledress crusted with dried salt, hair flattened with sweat, jaw tight, eyes on the hole.

Environment: the dunes behind the beach at Dunkirk. Marram grass, a half-buried canvas pack, an empty ration tin. Lower down and behind him four other men, each at a different distance, dig their own holes. Beyond them is a strip of grey sea.

Camera: eye level for a kneeling man, 50mm, from three metres away. The out-of-focus shoulder and helmet of a nearer soldier cut into the right edge of the frame. He is left of centre.

Lighting: midday under thin high cloud, ordinary and unflattering, with short soft shadows directly beneath everything.

Details: real-time game rendering, with sand, grass and cloth that look scanned from life, natural colour and nothing heightened.
```

### 5.4 Hell Let Loose

Ground-level, gritty, desaturated war simulation.

```
Generate an in-game capture from the Second World War video game Hell Let Loose.

Subject: a British infantryman of about twenty lies flat on his stomach in the sand, one cheek pressed to the ground and facing the camera, both hands clamped on the back of his steel helmet. Upper eyelids lifted so that white shows above the iris, lips parted and stretched sideways, grit stuck to his wet face.

Environment: the open beach at Dunkirk. Around him, at different distances, five other men lie flat in the same way. In the middle distance a line of small sand spouts is crossing the beach from right to left. Dropped rifles, a pack and a bicycle lie where they fell.

Camera: on the ground, a hand's height above the sand, wide lens, tilted a few degrees off level. Blurred blades of dune grass and a ridge of sand fill the bottom of the frame. He is right of centre.

Lighting: a hard high sun through thin smoke. Short black shadows lie under every body and the sand is pale and glaring.

Details: real-time game rendering, desaturated khaki and grey, gritty, with dust hanging in the air and a few specks of dirt on the lens.
```

### 5.5 Bodycam (Unrecord)

Chest-camera fisheye, blown-out sky, the most 'real footage' look.

```
Generate a frame from a bodycam-style video game in the manner of Unrecord, set in 1940.

Subject: seen from a camera mounted on another soldier's chest, a British infantryman of about twenty reaches toward the lens to take a dented metal water bottle that the wearer's own khaki sleeve and dirty hand are holding out at the bottom of the frame. He is very close, slightly blurred by movement. Cracked lips, red-rimmed eyes fixed on the bottle, steel helmet tipped forward.

Environment: the beach at Dunkirk. Behind him the horizon bends with the lens. Men sit in loose groups on the sand, and one tall column of black smoke leans across the sky.

Camera: an ultra-wide fisheye at chest height, tilted, with strong barrel distortion and darkened corners.

Lighting: harsh midday daylight that the small camera cannot handle. The sky is blown out to white and his face is slightly underexposed beneath the helmet brim.

Details: real-time game rendering made to look like compressed body-camera video, with smeared fine detail, colour fringing at the edges and a little motion blur.
```

### 5.6 Indiana Jones and the Great Circle

1980s adventure-film grain, hot highlights, in the water.

```
Generate an in-game capture from the video game Indiana Jones and the Great Circle.

Subject: a British infantryman of about twenty stands chest-deep in the sea in a queue of men, holding his rifle above his head with both arms and looking back over his shoulder toward the shore. Water streams off his sleeves. Eyes narrowed against the glare, jaw set, steel helmet strap hanging loose.

Environment: the shallows off Dunkirk. The queue runs away from the camera toward a small open boat that is already overloaded. Six men are visible in the line, each different: one bare-headed, one with a bandaged hand, one carrying another man's pack.

Camera: in the water at chest height, 40mm. A small wave laps across the bottom of the frame, out of focus. He is left of centre and the queue leads away to the right.

Lighting: a hard afternoon sun from behind him on the right. The highlights on the water clip to white and the shadow side of his face holds its detail.

Details: real-time game rendering finished like a 1980s adventure film, with visible film grain, warm skin, deep blue-green water and slightly overexposed highlights.
```

### 5.7 Battlefield 1

Thick drifting smoke, long lens, one patch of light.

```
Generate an in-game capture from the video game Battlefield 1, with its smoke-filled atmosphere, set in 1940.

Subject: a British infantryman of about twenty shuffles toward the camera in a packed column of men on a narrow wooden jetty, one hand on the shoulder of the man in front. His eyes are lifted to the sky above the camera. Stubble, a split lip, steel helmet, a rolled blanket slung across his chest.

Environment: the long timber jetty at Dunkirk harbour, its planks wet and its handrail broken in places. Thick black oil smoke drifts across the column from left to right, hiding the far end of it completely.

Camera: a long lens from further up the jetty, compressing the column. He is sharp and right of centre. The men in front of him and behind him are soft, and the nearest shoulder is a dark blur at the left edge.

Lighting: the sun is hidden by the smoke. One gap in it lets a single hard patch of daylight fall across him and the two men beside him, and everything beyond falls away into grey-brown murk.

Details: real-time game rendering, with volumetric smoke, a muted palette of brown and slate, and ash drifting in the air.
```

### 5.8 Senua's Saga: Hellblade II

Tight on the face, wide film frame, the most lifelike skin.

```
Generate an in-game capture from the video game Senua's Saga: Hellblade II, in its very wide film-style frame with black bars above and below, set in 1940.

Subject: the face of a British infantryman of about twenty, from the brim of his steel helmet to his collar. Inner brows raised and drawn together, white showing above the iris, lips parted. Asymmetric features, pores, cracked lips, a small scabbed cut on one cheekbone, salt drying white in his stubble, one bead of water on the helmet rim.

Environment: the beach at Dunkirk, reduced to a blur behind him of standing figures and a dark band of smoke.

Camera: very close, 85mm at a wide aperture, slightly below his eye line. His face fills the right two thirds of the frame and he looks up and out past the left edge.

Lighting: one cold light, the overcast sky above and to the left. It catches the helmet rim, his brow and the wet of his lower eyelid, and falls off into deep shadow under the brim and down the right side of his face.

Details: real-time game rendering from performance capture, with skin that scatters light, fine film grain and a cool, desaturated colour.
```

### 5.9 Grand Theft Auto V

Hard noon sun, saturated, third-person in the town.

```
Generate an in-game capture from the video game Grand Theft Auto V, with the setting moved to France in 1940.

Subject: seen from behind in the game's third-person view, a British infantryman of about twenty walks down the middle of a street toward the sea, rifle slung, one bootlace trailing, his helmet tilted. His head is turned to the left toward a burned-out army lorry.

Environment: a street in the town of Dunkirk leading down to the seafront. Brick houses with shuttered windows, one with its front blown open. Abandoned bicycles are stacked against a wall, there is broken glass and paper in the gutter, and a dog is trotting the other way. At the end of the street lie a strip of beach, a crowd of men and black smoke.

Camera: three metres behind him at shoulder height, wide lens. He is left of centre, and the lorry fills the right foreground, partly out of frame.

Lighting: hard noon sun from high on the right. Sharp-edged shadows fall across the road and heat haze softens the far end of the street.

Details: real-time game rendering with slightly heightened colour, crisp detail far into the distance and a little glare on the road surface.
```

### Results

Filled in after the run.

## Round 6 — film styles, built from how each film was shot (1 October 2026)

Jack: "I want to try cinematic styles that vary... like Saving Private Ryan, ones that can be done
artfully. The problem I have run into before with cinematic styles is that they all look the same,
is there something I am missing?"

**The answer the research gives:** a film's look is not a style word or a colour grade. It is a
set of physical choices: the lens and how close it is, the shutter, the film stock and how it was
processed, the shape of the frame, where the light comes from, and where the camera stands. A
prompt that says "cinematic, in the style of X" changes only the colour and leaves the model's
default framing in place, which is why the results match. Our own notes add that the word
"cinematic" itself triggers the glossy look.

So each prompt below describes how the film was made, never its name, and each has its own shot
and its own frame shape. No film title and no person's name goes into Flow.

| # | Built from | Frame | What makes the look |
| --- | --- | --- | --- |
| 1 | Saving Private Ryan (1998) | 16:9 | Fast shutter, uncoated lenses, colour drained in the lab, handheld |
| 2 | Atonement (2007) | 16:9 | Hazy, soft and strange: a net on the lens, the beach as a ruined fairground |
| 3 | The Zone of Interest (2023) | 16:9 | Fixed, distant, perfectly level, flat daylight, digital and cold |
| 4 | Powell and Pressburger Technicolor (1940s) | 4:3 | A 1940s British studio film: saturated dyes, hard key light, a painted sky |
| 5 | Son of Saul (2015) | 4:3 | One 40mm lens inches from him; everything else is blur |
| 6 | Come and See (1985) | 4:3 | He stares straight into the lens, in available light, on soft Soviet colour stock |
| 7 | Dunkirk (2017) | 21:9 | Huge clean large-format negative, natural light, restraint |
| 8 | The Thin Red Line (1998) | 21:9 | Low in the grass, natural light only, nature indifferent to the war |
| 9 | Apocalypse Now (1979) | 21:9 | Colour as feeling: black silhouettes against firelit smoke |
| 10 | 1917 (2019) | 21:9 | One falling flare, hard moving shadows in a ruined street |

**Model:** Nano Banana Pro, one candidate each, run as three batches by frame shape. About 12
credits an image by an unchecked third-party figure, so about 120 for the round.

**Round 5 (the game styles) has not been run.** Jack moved to film styles before it started; it is
held until he says to run it.

### 6.1 Saving Private Ryan (1998) — 16:9

```
Generate a single frame from a war film photographed handheld on 35mm film.

Subject: a British infantryman of about twenty stumbles out of the surf toward the camera, one hand down in the water to catch himself, soaked khaki battledress, steel helmet knocked crooked. Upper eyelids lifted, lips parted and stretched sideways, water streaming off his chin.

Environment: the shallows at Dunkirk. Behind him four other men, each at a different distance, struggle through the waves, and a small boat lies capsized.

Camera: handheld at knee height in the water, 35mm lens, tilted off level, with water droplets on the lens. He is right of centre.

Capture: a very fast shutter, so that every drop of spray and every grain of flying sand is frozen sharp and separate, with no motion blur anywhere. Old lenses with their coatings stripped off, so contrast is low and the bright sky bleeds a milky flare across the top of the frame. The film was processed with the silver left in: colour drained to a pale khaki and steel, harsh contrast, heavy grain.

Lighting: flat white overcast daylight from above and behind him.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 16:9 frame.

Thanks.
```

### 6.2 Atonement (2007) — 16:9

```
Generate a single frame from a British period film photographed on 35mm film through a fine net stretched over the lens.

Subject: a British infantryman of about twenty walks slowly from left to right through the frame, mouth slightly open, eyes moving over what is around him, a dirty bandage wound around one hand.

Environment: the seafront at Dunkirk, turned into something like a ruined fairground. Behind him stands a bandstand where a dozen soldiers are singing together, further off a beached pleasure boat lies on its side, and a big wheel stands still against the sky. A riderless horse stands on the sand between them. Men sit in groups; no two are doing the same thing.

Camera: a gliding camera at chest height, wide lens, held slightly back from him. He is left of centre, and the dark shoulder of a seated man blurs across the right foreground.

Capture: the net softens everything. Highlights glow and spread, contrast is low, and the colours are faded khaki, cream and pale blue-grey.

Lighting: late afternoon sun veiled by thin smoke, coming from behind the bandstand, so the air itself looks pale and luminous.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 16:9 frame.

Thanks.
```

### 6.3 The Zone of Interest (2023) — 16:9

```
Generate a single frame from a film shot by a fixed, unattended digital camera, like surveillance.

Subject: a British infantryman of about twenty stands in an orderly queue of men on the sand, as calmly as if waiting for a bus. He is the fourth in line, small in the frame, and he is the only one who has turned his head to look straight at the camera. Face slack, eyes level.

Environment: the beach at Dunkirk. The queue of eleven men runs across the frame from left to right toward the sea, each man standing differently. Sand, a flat sea, a pale sky. To one side a neat pile of rifles and a row of folded greatcoats.

Camera: locked off on a tripod at head height, wide lens, far back, the horizon perfectly level and exactly halfway up the frame. Deep focus, everything equally sharp from the nearest sand to the horizon.

Capture: clean modern digital, no grain, no flare, neutral accurate colour, nothing heightened.

Lighting: ordinary bright midday daylight under thin cloud, with small soft shadows directly under each man.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 16:9 frame.

Thanks.
```

### 6.4 Powell and Pressburger Technicolor (1940s) — 4:3

```
Generate a single frame from a British feature film of the mid-1940s, photographed in three-strip Technicolor on a studio sound stage.

Subject: a British infantryman of about twenty sits on an upturned rowing boat writing a letter on his knee with a pencil stub, steel helmet beside him. His head is turned up from the page, lips pressed together.

Environment: a beach built inside a film studio to stand for Dunkirk: real sand in the foreground, a painted backdrop of sea, smoke and sky behind, its brushwork just visible. Two other soldiers sit behind him sharing a tin of food.

Camera: a heavy studio camera at seated eye level, 50mm, level and steady. He is left of centre, and the dark prow of the boat cuts into the bottom right corner.

Capture: three-strip Technicolor, with dense saturated dyes, rich khaki, a deep blue-green sea, red in his cheeks and lips, and velvety blacks.

Lighting: one hard studio key lamp from high on the left, throwing a crisp shadow of his head onto the boat, with a soft rim on his far shoulder.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 4:3 frame.

Thanks.
```

### 6.5 Son of Saul (2015) — 4:3

```
Generate a single frame from a film photographed on 35mm with one 40mm lens held inches from the main character.

Subject: the head and shoulders of a British infantryman of about twenty, seen in three-quarter view from just behind his left shoulder. Only his ear, his jaw and the rim of his steel helmet are sharp. Jaw clenched, a vein standing out in his neck, sweat running through the dirt behind his ear.

Environment: the beach at Dunkirk, entirely out of focus. Beyond him it is only pale smears and dark upright shapes that might be men, and one dark mass low on the right that might be a body. Nothing in the background can be made out clearly.

Camera: handheld, 40mm at its widest aperture, so close that his shoulder fills the bottom left of the frame.

Capture: 35mm film with visible grain, in dull greens, browns and greys.

Lighting: overcast daylight from the front right, soft on his cheekbone, dark at the back of his neck.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 4:3 frame.

Thanks.
```

### 6.6 Come and See (1985) — 4:3

```
Generate a single frame from a mid-1980s Soviet war film shot on 35mm using only available light.

Subject: a British infantryman of about twenty stares straight into the lens, face filling the frame from helmet brim to chin, dead centre. Inner brows raised and drawn together, white showing above the iris, lips slightly parted, skin grey with fatigue, cracked lips, dried mud at his hairline.

Environment: the dunes behind Dunkirk in a thin drizzle. Behind him, soft but readable, three men carry a fourth on a door used as a stretcher.

Camera: a wide lens very close to his face, at his eye level, so his features bulge very slightly and the background stays wide.

Capture: soft, low-contrast colour film stock in muted greens, browns and greys. Slightly underexposed, with fine grain.

Lighting: flat grey daylight with no direction, the only bright point a small reflection of the sky in each eye.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 4:3 frame.

Thanks.
```

### 6.7 Dunkirk (2017) — 21:9

```
Generate a single frame from a war film photographed on 65mm large-format film in natural light.

Subject: a British infantryman of about twenty stands at the very end of a long timber jetty with his back to the camera, small in the frame, looking out at an empty sea. Steel helmet, khaki battledress, hands hanging.

Environment: the harbour jetty at Dunkirk. Hundreds of men stand packed along it behind him, all facing the same way. The sea is flat and grey-green. There is no ship.

Camera: high on the jetty's side rail, 50mm on large format, looking along its length. He is far right, the jetty runs away to the left, and the rail blurs across the bottom of the frame.

Capture: an enormous, fine-grained negative: immense clean detail, natural restrained colour, cool blue-grey sea against warm skin and wood, no visible grain.

Lighting: late morning daylight through high thin cloud from the right, soft-edged shadows, a bright band of light on the water at the horizon.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 21:9 frame.

Thanks.
```

### 6.8 The Thin Red Line (1998) — 21:9

```
Generate a single frame from a war film photographed in natural light only, with a wide anamorphic lens held low and close.

Subject: a British infantryman of about twenty lies on his side in the dune grass, his steel helmet off beside him, watching a small brown bird that has landed on the rim of the helmet. Eyes soft, mouth closed, face relaxed.

Environment: the dunes above the beach at Dunkirk. Tall marram grass moves in the wind all around him. Beyond the grass, small and soft, a column of men crosses the sand and black smoke rises.

Camera: almost on the ground, wide lens, an arm's length from his face. Blades of grass cross the foreground, out of focus. He is in the lower right of the frame.

Capture: 35mm anamorphic film, with gentle natural colour, green grass, warm skin, and oval out-of-focus highlights.

Lighting: the sun from behind and to the left, shining through the blades of grass so that they glow at their edges; his face is in open shade.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 21:9 frame.

Thanks.
```

### 6.9 Apocalypse Now (1979) — 21:9

```
Generate a single frame from a late-1970s war film photographed on 35mm anamorphic film at night.

Subject: a British infantryman of about twenty stands in silhouette, in profile, drinking from a water bottle with his head tipped back. Steel helmet, rifle slung. Only the edge of his face, his hand and the bottle are picked out.

Environment: the beach at Dunkirk at night. Behind him the town's oil tanks are burning, and a vast wall of smoke is lit orange from inside. Between him and the fire, eight men cross the frame in a ragged line, all pure black shapes.

Camera: low, long anamorphic lens. He is far left and large, and the line of men is small on the right.

Capture: 35mm film of the 1970s, with saturated colour, dense black shadows, grain and a soft horizontal streak of flare from the brightest flame.

Lighting: the fire is the only light, from behind. It draws a thin orange line down his profile and leaves everything facing the camera black.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 21:9 frame.

Thanks.
```

### 6.10 1917 (2019) — 21:9

```
Generate a single frame from a war film photographed on a large-format digital camera with one wide lens that follows the main character.

Subject: a British infantryman of about twenty runs toward the camera down the middle of a ruined street, caught mid-stride with one foot off the ground. Mouth open, eyes fixed past the camera, steel helmet, rifle gripped in one hand.

Environment: a bombed street in the town of Dunkirk at night. Broken brick walls, empty window frames, a church with half its tower gone, rubble and a pram across the road.

Camera: gliding backwards in front of him at chest height, 40mm. He is left of centre, and the jagged dark edge of a wall fills the right foreground.

Capture: clean large-format digital with shallow focus and smooth tones, in muted colour.

Lighting: one white magnesium flare falling slowly, high behind him on the right, is the only light. It throws long, hard, slanting shadows of the ruins toward the camera and rims him in white. The shadows are deep but keep a trace of detail.

Constraints: historical accuracy for the British Army in France in late May 1940. No text, caption or watermark anywhere.

Compose for a 21:9 frame.

Thanks.
```

### Results

Six of ten checked so far (1 October); the four extra-wide ones were still generating.

- **Flow refused the 21:9 frame shape** (`ASPECT_UNAVAILABLE: 21:9`) on Nano Banana Pro. Prompts
  6.7 to 6.10 were re-run at 16:9 with the last line changed to: "Compose a very wide 2.39:1 film
  frame, with black bars above and below it, inside a 16:9 image."
- **The four I looked at are clearly four different films**, which rounds 1 to 4 never managed:
  - 6.1 (fast shutter, drained colour): reads as a real film frame. Water on the lens, pale
    khaki, the men behind all different. He came out centred, not right of centre as asked.
  - 6.3 (fixed camera): flat, level, cold, a queue on an empty beach. The men are too alike and
    stand to attention; the soldier looking at the camera is third in line, not fourth, and is
    looking down more than at us.
  - 6.4 (Technicolor studio): strongest departure. Painted backdrop, saturated colour, and it put
    a studio lamp in shot, which was not asked for.
  - 6.5 (40mm, inches away): ear and jaw sharp, everything else blur. Did what was asked.
- 6.2 and 6.6 generated but not yet looked at.
- Jack's verdict: not given yet.

### Results (round 6, final)

All ten generated. Jack: "the cinematography styles all look the same." He also ruled: **always
Nano Banana 2, because it is free.** Round 5 (game styles on Pro) stays unrun.

## Round 7 — any medium at all, eighteen of them (1 October 2026)

Jack: "you have complete freedom to do any style, regardless of if it is realistic or not... make
it all vary a lot from each other."

**The thinking:** rounds 1 to 6 were all one style underneath, a realistic picture of a man in
khaki on a beach, with the colour or the lens changed. To a viewer that is one look. What makes
two images read as different at a glance is the **medium** (what it is physically made of), the
**palette**, the **viewpoint** and **how abstract** it is. So every prompt here changes all four,
and describes the medium as a physical object (paper, ink, glass, clay, thread) rather than as a
style name, which is what the prompting guides recommend. No living or dead artist is named.

Colour only, as ruled earlier. Model: Nano Banana 2, 16:9, one candidate each.

| # | Medium | Prompt |
| --- | --- | --- |
| 1 | Colour infrared film | A photograph on colour infrared film, the kind that turns everything green into hot pink. A British soldier of 1940 in a steel helmet lies in the dunes above the beach at Dunkirk. The marram grass around him is vivid crimson and magenta, the sky a deep teal, the sea almost black, his skin pale and waxy, his khaki uniform turned a dull lavender. Far below, lines of men stand on pale sand. Film grain, slightly soft focus, real film colours shifted, nothing digital. Thanks. |
| 2 | Cut-out animated documentary | A frame from an adult animated documentary made of flat digital cut-outs: hard-edged shapes, heavy solid black shadows, no gradients, thick uneven outlines. Night at Dunkirk in 1940 under a sulphur-yellow sky lit by flares. Three British soldiers wade waist-deep toward the camera out of a flat black sea, the nearest one large in the frame with only his eyes and the rim of his helmet catching the yellow. A palette of only yellow, black and dull orange. Thanks. |
| 3 | Vorticist painting | An oil painting in the British Vorticist manner of the 1910s: everything broken into hard angular planes and sharp diagonals as if drawn with a ruler, men reduced to machine-like blocks. A column of British soldiers of 1940 in steel helmets marches diagonally down a jetty at Dunkirk, repeating like the teeth of a gear, with one face turned out toward us. Slate blue, ochre, rust and bone white, flat matte paint, visible canvas weave. Thanks. |
| 4 | English war-artist watercolour | A watercolour by an English war artist of 1940 on cream cold-press paper: pale transparent washes, dry-brush stippling and cross-hatched pattern, a lot of bare paper left white, delicate pencil lines showing through. An empty stretch of beach at Dunkirk at low tide, a single British soldier sitting small on an upturned boat, abandoned lorries in a neat row, the sea drawn as rows of little dry-brush strokes. Chalky greens, greys and pale ochre, calm and eerie. Thanks. |
| 5 | Seaside railway poster | A 1930s British railway travel poster printed by lithography: large flat areas of cheerful colour, simplified shapes, no outlines, a smooth graduated sky, and a blank cream band along the bottom where the lettering would go. It shows the beach at Dunkirk in 1940 as if it were a holiday resort: golden sand, a bright blue sea dotted with little boats, and in the foreground a British soldier in a steel helmet sitting in a striped deckchair, with long queues of tiny soldiers in the water and one neat black plume of smoke. No lettering. Thanks. |
| 6 | Two-colour linocut | A linocut print in two inks, deep red and black, on rough cream paper: bold gouged marks, chunky carved lines, slightly uneven inking, the red layer printed a little out of register. A British soldier of 1940 in a steel helmet, head and shoulders in profile, fills the left half. Behind him the sea at Dunkirk is carved as rows of curling cuts with small boats, and the smoke over the town is a solid red mass. Thanks. |
| 7 | Stop-motion clay | A still from a handmade stop-motion animated film: a plasticine puppet of a British soldier of 1940 with visible thumbprints in the clay, a slightly too-large head, bead eyes and a tin-foil helmet, standing on a tabletop set of Dunkirk beach made of real sand, with a sea of crumpled blue cellophane, cotton-wool smoke on wires and little cardboard boats. Shallow focus, warm lamp light from one side, the miniature scale obvious. Thanks. |
| 8 | Toy soldier, macro | A macro photograph of a single old painted lead toy soldier, a British infantryman with chipped khaki paint and a bent rifle, standing on real beach sand whose grains look like boulders at this scale. Behind it, out of focus, dozens more toy soldiers stand in a line leading into a shallow puddle of real water. Low side light from a window, very shallow focus, dust and scratches visible on the paint. Thanks. |
| 9 | Embroidered wall hanging | A section of a medieval-style embroidered wall hanging, wool thread stitched on coarse linen, photographed flat: figures in side view, outlined shapes filled with rows of stitches, no perspective, and a decorated border of small animals and boats along the top and bottom. It shows the evacuation of Dunkirk in 1940: a procession of British soldiers in steel helmets wading from the left into a stylised wavy sea toward small boats, with stitched black smoke curling above. Terracotta, mustard, sage green and navy thread on unbleached linen, the weave and loose threads visible. No lettering. Thanks. |
| 10 | Stained glass | A stained-glass church window photographed from inside with daylight shining through it: thick black lead lines between pieces of jewel-coloured glass, painted details on the faces, small bubbles and streaks in the glass. The window shows a British soldier of 1940 in a steel helmet standing in the sea at Dunkirk, lifting another man into a small boat, with stylised blue waves below and red and amber smoke above. Deep blues, ruby, amber and green, glowing against a dark stone surround. Thanks. |
| 11 | Child's crayon drawing | A child's drawing in wax crayon and pencil on a slightly creased sheet of lined exercise-book paper, photographed on a wooden table: wobbly outlines, scribbled colouring that goes over the lines, everything flat, with the sky as a blue strip at the top. It shows a big smiling stick-figure soldier in a green helmet standing on yellow sand, lots of tiny soldiers in a blue sea, small boats, aeroplanes drawn as crosses and a black scribble of smoke. No writing. Thanks. |
| 12 | Japanese woodblock print | A Japanese woodblock print of the nineteenth century on soft cream paper: flat areas of colour, fine black key lines, visible wood grain in the printed ink, a sky that fades from deep to pale. A huge stylised wave with claw-like foam curls over the scene from the left. Beneath it small open boats crowded with British soldiers in steel helmets of 1940 pitch in the trough, and on the far shore the town of Dunkirk burns under a column of smoke. Prussian blue, indigo, pale ochre and a little red. No lettering or seals. Thanks. |
| 13 | Long-exposure photograph | A long-exposure colour photograph taken at dusk from a tripod. One British soldier of 1940 stands completely still in the shallows at Dunkirk, sharp, facing the camera with the water around his knees. Everyone else moved during the exposure: the crowds wading past him on both sides are streaked into pale transparent ghosts, and the sea itself has smoothed into mist. Cool blue-grey light, with one small warm point from a lantern on a boat. Thanks. |
| 14 | Straight down from the air | A photograph taken looking straight down from an aeroplane high above the beach at Dunkirk in 1940, so that it reads almost as an abstract pattern: a wide band of pale sand, a band of grey-green sea, and thin dark lines of queuing men running from the sand out into the water like the teeth of a comb. Scattered dots of vehicles, the long shadow of smoke lying diagonally across everything, and one single figure standing apart from the lines. Slightly faded colour film. Thanks. |
| 15 | Reflection in a helmet | A close photograph of an abandoned British steel helmet lying upside down on wet sand, filled to the brim with still rainwater. The whole scene exists only as a reflection in that water: the upside-down silhouette of a soldier standing over it looking down, and beyond him a sky crossed by black smoke. Around the helmet, out of focus, are boot prints and a dropped letter. Overcast light, muted colour, the reflection the sharpest thing in the frame. Thanks. |
| 16 | Stencil mural on a brick wall | A photograph of a street-art mural spray-painted through stencils on a weathered brick wall at the end of a British terraced street: crisp black stencilled shapes with a little overspray and a few drips. It shows a life-size British soldier of 1940 in a steel helmet, sitting hunched with his head in his hands, and behind him a row of small stencilled boats. The only colour in the stencil is one bright red poppy by his boot. Real pavement, a drainpipe and a wheelie bin beside it, grey daylight. No lettering. Thanks. |
| 17 | Torn-paper collage | A collage made of torn and scissor-cut coloured paper glued on board, photographed flat: bold simple shapes, rough torn white edges, visible glue wrinkles and overlapping layers. A British soldier of 1940 as a khaki paper silhouette with a round helmet stands large on the right. The sea at Dunkirk is strips of torn blue and turquoise paper with little white paper boats, the sand is orange, and the smoke is a big ragged piece of black tissue paper. Thanks. |
| 18 | Thermal camera | An image from a thermal imaging camera in its false-colour palette: warm things glow white, yellow and orange, cold things are deep purple and blue, with soft edges and no fine detail. A crowd of soldiers stands chest-deep in the cold sea at Dunkirk, their heads and shoulders glowing orange above the dark purple water. The nearest one faces the camera, his face a white-hot mask under a cooler helmet. On the horizon the burning town is a blinding white smear. Thanks. |

### Results

Filled in after the run.
