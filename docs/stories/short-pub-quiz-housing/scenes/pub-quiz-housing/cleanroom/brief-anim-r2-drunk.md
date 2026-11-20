# Brief: clip motion, round 2 (clean room): the drunk regular's three cutaways

You write motion prompts for Google Flow's video model **Omni 1.2 Flash**, image-to-video in **Frames** mode: the still
below is the first frame, the clip is **8 seconds**, portrait 9:16. Read only this file and the three images named
below. Do your own web research where it helps (how image-to-video models handle falls, slumps and slapstick timing;
what makes a body move believably; keeping the camera locked). Write your output to the JSON file named at the end.

## The film
A vertical short in an old English pub on quiz night, lit by on-camera flash. One table whispers its answer against the
clock. These three clips are cutaways to **a very drunk regular at the bar**, a running gag that gets worse each time.
Each cutaway plays for only about 1.5 seconds in the edit, so **the whole gag must happen in the first 2 seconds** of
the clip; the rest can settle. Pure silly physical comedy; he is never hurt and never pitiful. He does not speak.

## The three shots (first frames)
All in `/home/jackt/.cache/badcode-refs/pub-quiz-housing/shots/`:
- `P13.jpg` Cutaway 1: he sits on a green stool leaning badly to one side, pint held up.
- `P14.jpg` Cutaway 2: he has slid most of the way off the stool, one arm over the bar, legs splayed.
- `P15.jpg` Cutaway 3: mid-fall backwards off a tipping stool, pint flying, beer in the air.

## Write two options per shot
An option **a** and an option **b**, genuinely different (for example: cutaway 1, he sways further and catches himself,
or he tries to sip and misses his mouth; cutaway 2, he slides the last bit to the floor still smiling, or he tries to
climb back up and fails; cutaway 3, he lands flat on the floorboards with the stool clattering, or the pint lands
upright in his hand). One clear action per option.

## Rules for every prompt
- Start with "The camera does not move." and end with "The camera does not move." then "Thanks." on its own line.
- One continuous shot, no cuts. Only he moves (and the stool, the pint, the beer). Nobody else enters the frame.
- His face, hair and clothes stay exactly as in the first frame.
- No speech. Sound: a quiet pub murmur, plus the thud or clatter of the gag.
- No text appears. Under 90 words each.

## Output
Write `/home/jackt/projects/badcode/badcode/docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing/cleanroom/anim-r2-drunk.json`:
```json
[{"key": "13a", "still": "P13", "idea": "<one line>", "motion": "<the prompt>"}, ...]
```
Six entries: 13a, 13b, 14a, 14b, 15a, 15b. In your final reply, one line per option.
