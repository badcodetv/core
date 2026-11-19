# Brief: motion for real photos (clean room)

## The request, verbatim
Jack, 2026-11-19: "Please use the pics and animate them. We'll add more stills later if we need them. Thanks. Pre-search the internet. Make sure there's no pollution. Come up with some sort of filter as well. And do a bunch of varied ones. Thanks."

## What this is
A 9:16 short for phones, about 75 seconds: a laid-back late-1990s New York rap track counting down ten rules about who controls the money printer, ending on "no hand on the printer". These are real photographs (Unsplash) Jack picked to cut to the beat between rules. Each clip is 8 seconds; the edit uses one to three seconds of it.

## The stills (look at every image before writing)
- `U5-fix1`: Empire State Building, New York at night (searched as "new york sunrise skyline"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-fix1.jpg
- `U5-r10-bailout2`: a man riding a skateboard down a sidewalk next to tall pilla (searched as "bank building columns"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-r10-bailout2.jpg
- `U5-r3-press2`: time lapse photography of train station (searched as "wall street new york"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-r3-press2.jpg
- `U5-r4-supply2`: a tall building with windows lit up at night (searched as "new york apartment window"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-r4-supply2.jpg
- `U5-r8-debase1`: a pair of glasses sitting on top of a laptop computer (searched as "stock market screen"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-r8-debase1.jpg
- `U5-r8-debase2`: A pile of gold bars sitting on top of a table (searched as "gold bars"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-r8-debase2.jpg
- `U5-vibe10`: a gold necklace with a crown on it (searched as "gold chain"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe10.jpg
- `U5-vibe2`: A brick building with a car parked outside (searched as "brooklyn brownstone stoop"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe2.jpg
- `U5-vibe3`: Elevated urban train platform with graffiti at night (searched as "new york subway graffiti"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe3.jpg
- `U5-vibe4`: Person carrying a silver boombox by graffiti-covered door (searched as "boombox"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe4.jpg
- `U5-vibe5`: person holding black and grey DJ turntable (searched as "vinyl turntable dj"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe5.jpg
- `U5-vibe6`: glass panel door with green ATM signage (searched as "bodega new york"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe6.jpg
- `U5-vibe7`: Basketball court covered in snow with buildings behind (searched as "basketball court chain link fence"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe7.jpg
- `U5-vibe8`: yellow sedan parked in front of building (searched as "yellow cab new york night"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe8.jpg
- `U5-vibe9`: brown metal emergency exit stairs (searched as "fire escape new york"); image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/ten-economic-commandments/moodboard/U5-vibe9.jpg

## Write
For EACH still, TWO genuinely different motion prompts for image-to-video (Google Flow, Omni 1.2 Flash, Frames mode, the still as the start frame, 8 s, 9:16). Different means a different thing moving or a different mood, not the same idea reworded. Research on the web first how to prompt image-to-video motion on Google's Flow/Veo-family models so the photo stays itself (rigid buildings, no morphing, no new people).

Rules:
- The camera does not move (camera moves are done in the edit). Say so at the start and the end of each prompt.
- Only motion: what in the picture moves and how. The picture's look is the photo itself; do not restyle it.
- No new people, no faces appearing, no speech, no text or logos appearing, no money printed or drawn.
- Keep each prompt under 90 words.

## Output
Write JSON to docs/stories/short-ten-economic-commandments/scenes/ten-economic-commandments/cleanroom/anim-r5.json: a list of objects {"still": "<still id>", "option": "a" or "b", "idea": "<5 words>", "motion": "<the prompt>"}. Also write docs/stories/short-ten-economic-commandments/scenes/ten-economic-commandments/cleanroom/anim-r5.notes.md with your sources.
