# Brief: the kick into the taxi, one still + one video clip per staging ("Infinite Yous", shot D, 9:16)

You write prompts for Google Flow: Nano Banana 2 (stills) and Gemini Omni 1.2 Flash (image-to-video: the still is the clip's START FRAME, 8-second clip, 24 fps).

## The film
A 16-second UK satirical short, vertical 9:16, for phones. Late at night a drunk lad in his early twenties, car keys up, says "One version of me gets home fine" (he has read that there are infinite versions of him in parallel universes, so nothing matters). The screen splits into many versions of him; a figure in a balaclava and a white science lab coat squeezes them back into one: "There's only one." Then this shot: the figure boots the lad into a waiting taxi so he gets home. Cut to the end card. Funny first: a caring boot up the backside, cartoon-comic, nobody hurt.

## What the director wants (his words, verbatim)
"Make sure it looks like he kicks him and the guy flys in the taxi, how quick this is is what makes it funny. Please research the internet on how to do a kick in flow without saying kick."
Earlier: "write it like the way the guy in Django shoots the guy into the other room at the end" (the finale of Django Unchained: a character is whipped backwards through a doorway out of frame in an instant) and "basically I want him to fly into the taxi". And: "the current clip is AI slop, he turns around mid fall."

So the viewer must SEE the figure's leg swing and land on the lad's backside, and the lad must shoot into the taxi in a blink. The speed is the joke.

## The look
Reference photo (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/infinite-yous/reference/jack-taxi-night.png — night city street on a long lens, very shallow focus, background melted into big soft bokeh (warm amber, red, a little pink and cyan), silver cars with glowing yellow TAXI roof signs, inky blacks, the only light from signs, shop windows and street lamps.
The cast image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/infinite-yous/moodboard/CA2-a.jpg — the lad (white shirt, dark jeans) and the figure (balaclava with a white ring, goggles pushed up, white lab coat, black gloves) beside the silver taxi. **This image will be ATTACHED to your still as the reference for both people, the taxi and the street.** In the still prompt do not describe what the two people look like; call them "the young man in the white shirt" and "the figure in the lab coat" and give only position, pose, action, expression, framing and light.

## What has happened so far (facts, do not repeat the failures)
1. Video prompts with the word "kick" were refused by Flow's filter every time (3 tries each). A prompt with "a flat hand flicked out" + "yanked as if by a rope" + "snapping backwards" was also refused 3 times. Treat kick / boot / strike / hit / punch / shove / shoot / blast / attack / violent as refused; find other words.
2. Prompts that went through: "flops face-first onto the back seat with a comic bounce ... the figure lowers his foot, dusts off his gloves"; "whipped off his feet as if yanked by an invisible wire ... absurd over-the-top movie physics, played for laughs"; a fingertip touch to the forehead that sent him "rocketing back-first" into the seat. A STILL showing the figure with one leg raised straight out at hip height "like a calm dancer" generated fine, and so did a video from it.
3. What came back wrong: started from CA2-a (lad already half in the door), he floated UP out of the door, turned round, and sank in slowly over three seconds. The figure turned to face the camera. The fingertip version is clean but no kick is visible: the director wants the kick.
4. Omni tends to fill 8 seconds with slow motion unless the action is pinned early; timestamped segments ([00:00-00:01] ...) went through and put the action in the first second.

## Your task
1. Research first, on the open web, fresh: how people get kicks, fight moves and slapstick hits out of Google Veo / Flow / Gemini Omni (and other video models) without tripping the safety filter (prompt wording, describing the leg movement as choreography, dance, football, martial-arts practice, cartoon physics; starting the clip from a frame where the pose is already set); how slapstick films and cartoons time a boot up the backside (anticipation, contact, a few frames of launch); how to make a video model do the contact and the launch fast.
2. Write THREE genuinely different stagings, each a pair:
   - `still`: Nano Banana 2 prompt for the START FRAME, 60-120 words. The lad faces the open taxi door with his back (and backside) to the figure, standing clear of the car with room to fly in. The figure behind him, side-on to camera, in a pose that sets up the leg swing. Vertical 9:16, night-bokeh look.
   - `motion`: Omni prompt, 40-90 words, MOTION only. The figure's leg swings and lands on the lad's backside, the lad shoots head-first into the taxi and is gone in a blink, the car rocks, then everything holds. The lad never turns round; the figure never turns to camera.
3. Every prompt ends with the word "Thanks." No readable text except a plain TAXI roof sign. No real names of people, films or companies.
4. Read ONLY this brief and the two images; open no other file on this machine.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "anything the editor must do (speed ramp, cut point, sound)", "stagings": [{"idea": "...", "still": "...", "motion": "..."}, ...3]}
