# r6 score: research notes (ideas writer, 2026-11-13)

Web research only; no repo files read.

## Prompting Suno for a short instrumental cue
- Put the main genre first: Suno weights the start of the style box most. Keep it to roughly 20-50 words, because a pile of mood words comes out muddy. Write a BPM number, not "fast". Pick one lane (suspense underscore, trailer, minimal bed) before writing "cinematic". https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad ; https://hookgenius.app/learn/suno-film-score-prompts/
- Scene-based prompting: write the scene as one camera shot, then name an arc. "Lift" is calm, build, intense; "collapse" is tension, then silence. Give each visual beat its own musical shift. Map visual cues to sound tags (tense silence = droning pad, pulsing bass). https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-scene-based-prompting-guide
- Endings: Suno does not document [End] as a guaranteed command. Describe the ending in plain words ("final hit with a clear stop, no fade", "cold end, all instruments drop"). A hard cut means the waveform and the room reverb stop instead of decaying. https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/suno-ai-end-prompt-guide ; https://howtopromptsuno.com/common-problems/how-do-i-end-the-song
- No vocals: turn the Instrumental toggle on and also write "instrumental" in the style box. Put choir, backing vocals and humming in Exclude. Pair each negative with a positive instruction, because a vague negative gets ignored. https://diyai.io/ai-tools/audio-generation/suno-exclude-styles/ ; https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/negative-prompting-suno-v5-guide ; https://help.suno.com/en/articles/3161921

## Scoring under dialogue
- The core of the voice sits around 500 Hz to 1 kHz. Keep the music out of that band, or the dub mixer pushes it down. https://thinkspace.ac.uk/blog/blog-how-to-underscore/
- Low-mid instruments (tenor sax, the middle of a piano, acoustic guitar) mask male voices. Leave a hole for speech and keep the centre of the stereo field free. https://www.prosoundweb.com/in-the-studio-balancing-dialog-in-post-production/
- Mix the music open in the low mids, because the voice fills them. https://www.robin-hoffmann.com/?p=4285
- Zimmer's counterview: the old rules are outdated, so test it by listening for whether every word is intelligible. https://www.masterclass.com/classes/hans-zimmer-teaches-film-scoring/chapters/scoring-under-dialogue

## Medical / procedural urgency
- The Pitt: the composer writes minimal, pulse-like material that is mixed in under the natural sound, so the tension is subconscious. https://zebrahomecinema.com/blog/the-anatomy-of-sound-design-bryan-parker-the-pitt-interview
- In TV scoring the ostinato works as a rhythmic motor, not a hook. Odd meters such as 5/4 add instability. A marcato string pulse over a percussion bed drives urgency. https://www.berklee.edu/node/2348071 ; https://vectree.io/pdf/c/tv-noir-bassline-innovation (the second source is auto-generated and weak)
- Production-music medical cues are tagged "dramatic pulsing tension, urgency", one at 114 bpm. https://www.warnerchappellpm.com/track/tv-club-tv186-38/MjI0NzI5MDAwLTQ3NjE1Yw ; https://sonoton.com/en/album/SFT0286
- Line of Duty (a UK police drama): an orchestral and electronic blend, racing rhythms, a circling piano figure that whips up tension, shimmering strings. https://www.classical-music.com/features/tv-and-film-music/line-of-duty-on-bbc-who-wrote-the-music-and-can-you-buy-the-soundtrack

## Tension devices
- Dunkirk: a Shepard tone (stacked octaves that seem to rise for ever without resolving) and a ticking watch turned into a synth pulse that gives the "metric pulse". https://www.cbc.ca/radio/q/blog/hans-zimmer-explains-the-audio-trickery-that-made-dunkirk-audiences-nauseous-1.4311684 ; https://faroutmagazine.co.uk/keeping-score-hans-zimmer-used-science-soundtrack-dunkirk/
- Under the Skin: a viola-led string score with discordant trembling tremolo, sliding pitch-bent strings, cymbal rolls and deliberately rough, airy recording. https://www.bfi.org.uk/sight-and-sound/interviews/away-from-picture-mica-levi-her-under-skin-soundtrack ; https://en.wikipedia.org/wiki/Under_the_Skin_(soundtrack)
