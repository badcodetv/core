# Voice casting brief, round 6 (clean room)

You write the voice direction for ONE role in a 14-second UK short film, rendered with Google's Gemini text-to-speech
(model gemini-3.1-flash-tts-preview, the same engine as AI Studio "Generate speech"), using one of its 30 prebuilt voices.
**Research the internet first**: Google's own speech-generation docs and prompting guide for Gemini TTS, the
prebuilt voice list with each voice's character, and practitioner write-ups on getting natural, non-AI-sounding British
voices. Base your choices on what you find. Do not read any file on this machine except this brief.

## The film
Night, rain, a British city. In the back of an NHS ambulance two paramedics (a woman and a man) fight to keep a dying old man
alive; the driver is pushing through traffic. At a red light a police outrider stops them so a government minister's car can
cross. The patient flatlines. It must feel like real people in a real British emergency, the way a good UK hospital drama or a
fly-on-the-wall documentary sounds: urgent and human, never a cartoon, never a radio play.

## What the director wants (his words)
"they have to fit each character, i think them sounding realistic is in how subtle the accents are and are not exaggerated."
The last attempt sounded the same across roles and weird. A previous film of ours whose voices the director loved used this
method, so follow it:
- The direction is a short **director's note of three lines**, under 60 words in total:
  `Accent:` the person's ordinary background, named plainly as a place and a class, and kept **light and everyday** (say it
  is not stagey / not exaggerated in your own words);
  `Style:` who they are (age, job, state of mind) and **who they are talking to**, as a real person talking, not performing;
  `Pace:` a few words.
- Name a region; never spell out sounds, dropped letters or phonetics.
- The voice itself (the prebuilt voice name) does most of the work. Pick it by ear-description from your research, to fit the
  character's age and build.

## Output
Write JSON to the path you are given:
{"research": ["url: takeaway", ...],
 "options": [{"letter": "a", "voice": "<prebuilt name>", "idea": "<one line: who this person is and why this voice>",
              "note": "Accent: ...\nStyle: ...\nPace: ..."}, ... three options],
 "notes": "optional"}
The three options must be genuinely different people: a different prebuilt voice each, and different on at least two of
age, region, class and temperament. Use only voices from your allowed list.
