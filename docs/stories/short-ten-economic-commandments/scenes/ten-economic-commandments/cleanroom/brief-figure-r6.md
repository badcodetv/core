# Brief: the BadCode figure rapping in ten New York locations (clean room)

## The request, verbatim
Jack, 2026-11-19: "So, a lot of these locations should have the bad guy in it, rapping like he was, you know? Like, uh, yeah. Thanks."

## What this is
A 9:16 short for phones, about 75 seconds: a laid-back late-1990s New York rap track counting down ten rules about who controls the money printer. Jack picked real photos of New York places. Now each place gets a NEW picture with the rapper in it, performing the verse to camera, like a 90s rap video shot on location.

## How the picture is made
Google Flow, Nano Banana 2.1, edit mode, 9:16. Two images are attached to each call:
1. the location photo (listed below): keep its real layout, perspective, light and time of day; it is a template, not a background to paste onto.
2. the figure reference: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/RU4-3-a.jpg (full figure) — his outfit and mask exactly.
The result must be a completely new photograph of the place with him in it.

## The figure (must match the reference)
A heavyset man in a baggy beige thrift-store suit, a plain cap, a black roll-neck, gloves into the cuffs, full-length trousers and black socks: no skin anywhere. His face is fully covered by the BadCode balaclava. Paste this sentence verbatim into every prompt:
"The balaclava exactly as in the attached image: no holes, no skin, gloves."
He raps to camera: mid-verse, chest out, one gloved hand chopping the air or pointing at the lens, the other at his side or on the mic. His masked face is turned toward the camera. No mouth shows (the mask has no holes).

## Locations (look at every photo before writing)
- `F6-vibe2`: A brick building with a car parked outside (searched as "brooklyn brownstone stoop"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-vibe2.jpg
- `F6-vibe3`: Elevated urban train platform with graffiti at night (searched as "new york subway graffiti"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-vibe3.jpg
- `F6-r3-press2`: time lapse photography of train station (searched as "wall street new york"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-r3-press2.jpg
- `F6-vibe6`: glass panel door with green ATM signage (searched as "bodega new york"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-vibe6.jpg
- `F6-vibe7`: Basketball court covered in snow with buildings behind (searched as "basketball court chain link fence"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-vibe7.jpg
- `F6-vibe8`: yellow sedan parked in front of building (searched as "yellow cab new york night"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-vibe8.jpg
- `F6-vibe9`: brown metal emergency exit stairs (searched as "fire escape new york"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-vibe9.jpg
- `F6-r10-bailout2`: a man riding a skateboard down a sidewalk next to tall pilla (searched as "bank building columns"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-r10-bailout2.jpg
- `F6-vibe4`: Person carrying a silver boombox by graffiti-covered door (searched as "boombox"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-vibe4.jpg
- `F6-fix1`: Empire State Building, New York at night (searched as "new york sunrise skyline"). Layout photo: /tmp/claude-1000/-home-jackt-projects-badcode-badcode/9852d996-da1d-48e2-9f11-6d8b51bc439c/scratchpad/tec-refs6/U5-fix1.jpg

## Rules
- Research on the web first how to prompt Google's Nano Banana image edit with two reference images (one for place, one for character) so the place keeps its layout and the character keeps his outfit.
- One prompt per location, each staging him differently (where he stands, how big in frame, his gesture), under 120 words.
- No other people's faces; any passers-by stay blurred and far away. No text, lettering or logos anywhere; paste this verbatim too: "No text, lettering, logos or brand names anywhere in the image."
- No real currency, no real rapper, no real person's likeness.

## Output
Write JSON to docs/stories/short-ten-economic-commandments/scenes/ten-economic-commandments/cleanroom/figure-r6.json: a list of {"still": "F6-<location>", "layout": "<layout photo path>", "prompt": "<the prompt>"}. Notes and sources to docs/stories/short-ten-economic-commandments/scenes/ten-economic-commandments/cleanroom/figure-r6.notes.md.
