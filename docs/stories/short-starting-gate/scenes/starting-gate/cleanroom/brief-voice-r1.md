# Brief: the race commentator's voice (The Starting Gate), round 1

Write the JSON file named at the bottom. Read nothing else from the repo.

## The character
BadCode, a masked figure, is the race commentator in a short comedy film: a British horse race (flat racing on turf, a
wet English afternoon). He calls the race from the commentary box. We never see a mouth, so the voice carries everything.
Jack, the director: "make a horse racing commentator voice, research the internet to make it in google ai studio".

## His lines (fixed words; do not change or add words)
1. "New money's been printed, the gates are open... and they're off!"
2. "Shares flies out! Houses right on its tail! And Wages... Wages hasn't left the stalls."
3. "Houses home in seven years! And Wages is away! Eleven years... and nine months."
4. "Next race. One gate. Everybody out at once."

## The engine (Google AI Studio text-to-speech, model gemini-3.8-flash-tts)
- **Voice design:** a reusable voice is made once from a 1-2 sentence plain description (language en-GB): who, age, where
  from, the sound of the voice. Name a real place for the accent; never spell out phonetics.
- **Style per line:** a few words of delivery direction may go with a line (sent separately, never spoken), e.g. the
  pace or energy. Keep it to a few words; never an accent, age or persona there.
- **Pause tags** may go in the line itself: `<short pause>`, `<long pause>`. Tags are not words.
- Our tests: personality/performance adjectives in the description ("cheerful", "a wink in every word") push the engine
  into a caricature; who-and-where plus the voice's sound works. Delivery belongs in the per-line style instead.

## Your job
1. Research on the web how real British racing commentary sounds (TV and radio race callers): pace, pitch, how they build
   from calm to a climax at the finish, how they deliver names, what separates the real thing from a parody. Note sources.
   Never name a real commentator in your output.
2. Write **five** voice descriptions (1-2 sentences each), genuinely different men (age, region of England/the UK, voice
   texture), each plausible as a professional race caller.
3. For each of the four lines, write the per-line style (a few words) and the line with any pause tags, so the four lines
   build like a real race call: calm and quick at the off, rising through the break, a big call at "Houses home", then
   flat and deadpan for line 4. One set of line directions for all five voices.

## Output
Write `voice-r1.json`: {"research": "<5-8 lines with source URLs>", "designs": [{"name": "comm-a", "desc": "...", "why": "...", "rank": 1}, ... "comm-e"],
"lines": [{"key": "01-off", "text": "<line with tags>", "style": "<few words>"}, {"key": "02-break", ...}, {"key": "03-home", ...}, {"key": "04-onegate", ...}]}
