# Brief: the fling into the taxi, one still + one video clip per staging ("Infinite Yous", shot D, 9:16)

You write prompts for Google Flow: Nano Banana 2 (stills) and Gemini Omni 1.2 Flash (image-to-video: the still is the clip's START FRAME, 8-second clip, camera does not need to move).

## The film
A 16-second UK satirical short, vertical 9:16, for phones. Late at night a drunk lad in his early twenties, car keys up, says "One version of me gets home fine" (he has read that there are infinite versions of him in parallel universes, so nothing matters). The screen splits into many versions of him; a figure in a balaclava and a white science lab coat squeezes them back into one: "There's only one." Then this shot: the figure sends the lad flying into a waiting taxi. Cut to the end card. The point, never said aloud: there is one of you, and one mum waiting up. Funny first.

## What the director wants for this shot (his words)
"Write it like the way the guy in Django shoots the guy into the other room at the end (research what that is), then describe it aptly without setting off the failed prompt issue, basically I want him to fly into the taxi."
Research the scene he means (the finale of the film Django Unchained, a character blasted backwards through a doorway out of frame) and find what makes it funny: the speed, the direction, the physics. Use the GAG, not the gun: in our shot nobody holds a weapon. The figure's raised leg/pose implies what happened; the lad is launched, flat and fast, through the open back door into the taxi and is gone.
On the last try he said: "the current clip is AI slop, he turns around mid fall."

## The look
Reference photo (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/infinite-yous/reference/jack-taxi-night.png — a night city street on a long lens, very shallow focus, background melted into big soft bokeh (warm amber, red, a little pink and cyan), silver cars with glowing yellow TAXI roof signs, inky blacks, the only light from signs, shop windows and street lamps.
The cast image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/infinite-yous/moodboard/CA2-a.jpg — the lad (white shirt, dark jeans) and the figure (balaclava with a white ring and goggles pushed up, white lab coat, black gloves) beside the silver taxi. **This image will be ATTACHED to your still as the reference for both people, the taxi and the street.** So in the still prompt, do not describe what the two people look like (that makes the model redraw them); refer to them as "the young man in the white shirt" and "the figure in the lab coat" and give only position, pose, action, expression, framing and light.

## What has failed (do not repeat)
1. Refused by Flow's filter, every time (3 tries each): any prompt with the word "kick", and even a gentle "the young man topples onto the back seat" prompt started from CA2-a. Assume violent words (kick, shoot, gun, blast, hit, punch, strike, attack, hurt) are refused; describe the motion as physics and comedy.
2. Two clips that DID go through, both started from CA2-a, where the lad is already half inside the door: he sprang UP out of the doorway, flailed, turned round to face out, then sank slowly in over three seconds. A float, not a fling. Cause: no distance to travel, and the model filled 8 seconds with slow motion.
3. In both, the figure turned round to face the camera after a second. Its mask then came out wrong. The figure must stay side-on / in profile to the camera the whole clip.

## Your task
1. Research first, on the open web, fresh: the Django scene; how to prompt Gemini Omni / Google Flow image-to-video for fast action (Google's own prompt guide and recent practitioner write-ups); how comedy and stunt films shoot a body yanked out of frame (wire pulls, ratchets, undercranking, speed); how to make an AI video model do ONE fast action early and then hold, instead of slow-motion filling.
2. Write THREE genuinely different stagings. Each staging is a pair:
   - `still`: a Nano Banana 2 prompt for the START FRAME, 60-120 words. The lad must be clear of the taxi with room to fly (e.g. a step or two away from the open back door), the figure in a pose that implies what is coming or has just happened. Vertical 9:16, the night-bokeh look.
   - `motion`: an Omni prompt, 40-90 words, describing the MOTION only (the still carries the look). One action, early and fast: the lad leaves the ground and is through the door and gone inside in well under a second, the car rocks, then the frame holds. The lad never turns round; the figure never turns to camera.
3. Each prompt ends with the word "Thanks." No readable text except a plain TAXI roof sign. No real names of people, films or companies in any prompt.
4. Read ONLY this brief and the two images; open no other file on this machine.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "anything the editor must do (speed ramp, blur, cut point)", "stagings": [{"idea": "...", "still": "...", "motion": "..."}, ...3]}
