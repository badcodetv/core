# Cut the Bank Robbery music video: one of five different cuts

You are one of five editors. Each of you cuts the same film from the same footage under a different rule, so the director (Kai) can play all five and take the bits he likes from each. **Your rule is at the bottom of your prompt. Push it hard; the point is that the five cuts differ.** He finishes the chosen cut by hand in Premiere, so it does not need to be perfect, it needs to be a clear, good version of your rule.

## The film

A glossy 1920s Prohibition music video: six masked robbers in sharp suits (PLUM, BOTTLE, CRIMSON, MARINE, RUST, SILVER) doing heists, and rapping to camera, over a cockney woman's rap about money printing and inequality ("the version.wav", 92.3 beats a minute, a beat every 0.65 s). The film ends at **187.0 s** on the line "Don't just eat cake" (the picture fades out there; there is no outro).

## Files (all in `/home/kai/projects/badcode/badcode/docs/stories/bank-robbery/songs/mv-gang/cleanroom/r10/cuts/`)

- `catalogue-1.json` … `catalogue-6.json`: every clip you may use (72, split in six files), described by people who watched it: place, who, whether the gang raps at the camera, energy, what it shows, the best seconds, faults. **Only these clips exist.** Clips whose ref starts with `h` are the 13 new ones made today: the whole gang rapping at the camera in places from the film (Kai asked for them: "a modern London drill group of five or six guys, all gesticulating towards the camera").
- `pool.json`: each clip's length in seconds (`secs`) and where the previous cut (cut 9) used it (`in_cut9`).
- `music-map.json`: every sung line with its start (`start` is the speech recogniser's, loose by up to 0.3 s; `start_snapped` is the nearest strong drum hit or half beat, usually the better cut point), the beats, the bars, the `strong_hits` (the loudest drum hits), loudness per bar (0–1), the sections, and the `events` Kai named.
- `anchors.md`: **Kai's notes on cut 9, verbatim, each with the shot cut 9 had at that moment.** Read every one. They bind all five cuts (see below).
- `../../../edit-plan-r9.json`: cut 9, Jack's cut (128 shots), for reference: its order and its `line`/`why` fields show which shot was chosen for which line.
- `validate.py`: the checker.

## What every cut must do (from Kai's notes)

1. **Timing.** Cut 9's cuts all sit on a beat, but only 19 of 113 land on a strong hit, and the drop at 10.82 s is cut late (11.15). Cut on the music's events: the drop, line starts (`start_snapped`), phrase ends, strong hits, the 2:56 tone change. A cut point must be a beat, a half beat or a strong hit (within 0.045 s).
2. **The intro (0–20.14 s)** builds: calm first ("a guitar being strummed", the gang "just chilling out somewhere", not robbing yet), quick transitions are fine, then medium action from about 13 s. **A picture change exactly on the drop at 10.82.** No rapping-to-camera shots before 20.14. Kai suggested the shot cut 9 had at 26.4 s as a candidate for the very beginning.
3. **The verses**: rapping-to-camera shots start the moment the words start (20.14). Kai: "a wrapping scene followed by a non wrapping scene followed by a wrapping scene" (your rule says how strictly).
4. **Keep in place** (the same clip at about the same moment): 24.5 s, 29.6 s, 49.9 s (printing money, "perfect"), 96.9 s (the dilution part), 113.0 s ("keep it exactly here"), 183.5 s ("excellent"); see anchors.md for which clip each is.
5. **Lines that need their picture**: "grandma freezing" only on that line (not before); money thrown around on "quantitative easing"; printing on "stimulus checks"; an explosion on "Sorry, did I interrupt your meeting?"; the devil-horn shadow booth on "It is the devil with the radio station"; "call the police" shots held only while the line is sung; something better than the train for the line at ~161 s; better "distraction" shots just before "Just look at the hand" (~104 s).
6. **The choruses** cut into the car chase on the first "Robbery!" (61.86 / 123.74, not early), and the second half of each chorus is basement, underground and printing. **Chorus 2 repeats chorus 1's pictures** in the same order and timing (shifted by 61.88 s).
7. **2:56 (about 176 s)**: the tone of the music changes dramatically, so the picture switches dramatically to a completely different scene.
8. **The end**: finish on the man on the bank steps (the shot before cut 9's 186 s ending shot; check the catalogue), held to 187.0.
9. **Footage**: fewer repeats in verse 5 (use the new crew clips there). Avoid clips the catalogue marks with bad faults (wrong mask, extra men, morphing) unless nothing else fits; never use a clip twice in a row; a repeated clip uses a different stretch (`in`).
10. The gramophone moment around 122 s: Kai will time it by hand in Premiere; just put it there.

## Output

Write `plan-<LETTER>.json` in the cuts folder: a JSON list of every shot in order, `{"start": s, "end": s, "clip": "<ref>", "in": <seconds into the clip>, "line": "<the sung line here, or ''>", "why": "<a few words>"}`. Shots butt end to start with no gaps, the first starts at 0, the last ends at 187.0, no shot under 0.3 s, `in + (end - start)` within the clip's `secs`. Write it with a small Python script (keep the script beside it as `make-<LETTER>.py`), then run `python3 validate.py plan-<LETTER>.json` until it passes.

Also write `about-<LETTER>.md`: three to six plain sentences for the director on what your cut does and where it is strongest, then any place you broke a rule above and why.

Do not read anything on this computer apart from the files named here. Reply with the validate.py output and one line saying you are done.
