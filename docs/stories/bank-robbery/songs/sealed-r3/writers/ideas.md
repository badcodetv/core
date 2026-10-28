I've researched and planned 8 experiments. I haven't written any prompts, and I haven't changed the repo, the skills or the scripts yet. I'm working in an empty folder with no access to the repo, which is the setup the clean-room rule requires.

**What the research found**
- **What the reference's page says:** the public page of "Best one" shows the title "best one" by binocarlos, model V6, and only two style tags: "psych folk, funk". The page summarises its lyrics as being about economic hardship, eviction, banks and European cities, so it is the older draft, not Kai's lyrics. The listening pass hears acoustic blues/flamenco-style guitar over a boom-bap stomp at about 90–93 BPM, with a raspy British voice half-rapping and half-singing and group shouts on the hooks. None of the ideas below borrow the stored prompt's sitar or psych folk wording. That wording is probably where the "Indian beginning" came from. https://suno.com/song/024b82e8-378c-47bd-bf73-bb5eafea2ed5
- **Short Style boxes work better.** One guide says aim for 4–7 descriptors: fewer sounds generic, and more makes the model average the instructions instead of following them. It also suggests a BPM number plus a pace word ("95 BPM, slow and deliberate"), and describing an instrument's character rather than just naming it. It says small changes, like one adjective or about 10 BPM, change the result a lot. This fits what we've seen: the 29-word "Best one" beat the 120–140-word boxes. https://roo.beehiiv.com/p/suno-v5-5-changed-the-prompting-rules-here-are-the-formulas-that-actually-work
- **Describe a voice in separate parts.** Another guide splits it into who the voice is (register, tone, diction, vibrato), how the performance builds, and the arrangement, and says which traits to avoid. I couldn't open the full page; this is from the search summary. https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/how-to-make-suno-preserve-a-natural-folk-tenor-suno-v5-5-voice-guide
- **Voice tags:** these can go in the Style box, or in the lyrics just before a section to change the voice for that section. That gives us a way to blend several voices in one take. https://roo.beehiiv.com/p/suno-prompting
- **Suno blocks many artist names.** Guides advise describing the decade, vocal texture, instruments and production instead. So the ideas below use types of performer, not real singers. https://medium.com/@abhisheksd2003/the-ultimate-suno-ai-prompt-guide-with-clear-tested-examples-2d827ffe8b3a · https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-prompt-contained-inappropriate-material
- **The same singer comes back when nothing else changes.** Guides that teach how to *keep* one singer say to hold everything steady and change one thing at a time. A Reddit user reports getting the same voice no matter which adjectives they used. To get a different singer, change the kind of performer, the wording, the structure and the settings all at once. https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/keep-same-singer-across-ai-songs-suno · https://reddit.sentinel-team.org/posts/1s47g9t/snapshots/2026-03-27T18%3A20%3A17.4177Z

The ideas below have no shared music paragraph and no shared delivery sentence. Each one has a different kind of performer and asks for the music in a different way. Settings vary too: Max Mode is on in some and off in others, durations range from 170 s to 240 s or unset, and weirdness and style influence differ. Variety stays Off in every one.

```json
[
  {
    "name": "folk-club-baritone-storyteller",
    "idea": "An older singer from English folk clubs, a deep, chesty, untrained baritone who tells the lyrics like a story at a pub session. He leans on the consonants and lets the long held words ('FREEEEEEEZING', 'burrrrrrrring') wobble rather than shout. Ask for the music as one short line, about 25–35 words, describing what the reference sounds like: a dark acoustic blues guitar riff over a heavy stomping boom-bap kick and snare, about 92 BPM, dry and close. Do not mention sitar, psych or anything Indian. Settings: Max Mode off, Vocal Gender male, style influence around 75, weirdness around 25, Duration 170–190 s. Exclude: screaming, double-time, autotune, sitar, EDM."
  },
  {
    "name": "low-crew-unison-blend",
    "idea": "A blend: a deep, weathered English lead voice, joined on every 'Robbery, robbery!' and 'Debasement!' line by a crew of low male voices singing in rough unison, like dock workers or a rugby club singing. The lead stays rough and conversational in the verses. Write the Style box only as comma-separated tags, no sentences, 5–7 tags in total, e.g. boom-bap acoustic stomp, gang vocal hooks, a BPM tag near 90. In the lyrics, mark sections with tags such as [Lead] and [Crew in unison] so the blend is driven from the lyrics, not the Style box. Settings: leave Vocal Gender unset, Max Mode on, style influence about 60, weirdness about 35, no Duration set."
  },
  {
    "name": "sneering-sixties-crooner",
    "idea": "A deep English crooner from the 1960s, a smooth, resonant, slightly sneering baritone who sings every line in tune with sly, theatrical irony. The joke comes from a polished voice singing angry words. Describe the music as a short scene in plain prose: nylon-string guitar strummed in a flamenco style over a dusty, slow breakbeat at about 93 BPM, with a round bass, in a dark, dry room. Set weirdness higher (about 50–55) and style influence lower (about 55) so Suno has room to find an unexpected blend. Max Mode off, Vocal Gender male, Duration about 210 s. Exclude: rap, screaming, smooth R&B, sitar."
  },
  {
    "name": "laid-back-london-talk-singer",
    "idea": "A low-voiced London talk-singer, halfway between speaking and singing, with an unhurried behind-the-beat flow like someone talking over a record at a late-night party. It must be slow and spacious, never double-time or fast rap. In the verses he half-sings, and on the choruses he really sings, in tune, in his low register. Write the Style box in the order rhythm first, then instruments, then voice: something like an 88–90 BPM head-nod groove, a picked acoustic blues riff, a warm mid bass, then the voice. Keep it under 30 words. Settings: Max Mode on, style influence about 80, weirdness about 20, Duration 240 s. Exclude: double-time, fast rap, trap hi-hats, screaming, autotune."
  },
  {
    "name": "cathedral-bass-and-low-choir",
    "idea": "A real, trained deep bass voice, like a lay clerk from an English cathedral choir who has walked into a protest song. The voice is huge and calm with clear diction. On the hooks a small choir of low male voices answers him, so the blend is call and response, not unison. Keep the music description minimal, one line naming only the acoustic guitar riff and stomping drums, about 90 BPM, so the voice description takes most of the Style box. In the lyrics, mark the answers with tags such as [Choir answers]. Settings: Vocal Gender male, Max Mode on, style influence about 70, weirdness about 40, Duration about 200 s. Exclude: opera, screaming, orchestra, sitar, EDM."
  },
  {
    "name": "northern-deadpan-post-punk",
    "idea": "A deadpan baritone from northern England in the late-70s post-punk style: flat, dry, droll and lightly bored, almost reciting, but on pitch and melodic in the choruses. He finds the lyrics funny without performing the joke. Describe the music by era and texture rather than by genre: something like a stark late-70s room sound, an acoustic guitar played like a rhythm machine, tom-heavy stomping drums and a plain bass, about 95 BPM, raw and dynamic. Keep the Style box to about 20–30 words. Settings: Max Mode off, style influence about 65, weirdness about 45, Duration unset. Exclude: shouting, screaming, polished pop, autotune, rap."
  },
  {
    "name": "british-blues-boom-gravel",
    "idea": "A singer from the 1960s British blues boom, with a deep, gravelly, smoky voice: a working-class English man singing American-style blues with his own accent showing through. He growls the low notes, without screaming. Make the Style box extremely short (about 10–15 words: era, acoustic blues stomp, boom-bap drums, the gravel voice). Put the rest of the direction into short bracketed section tags in the lyrics, such as [Verse – low and close], [Chorus – full chest, band hits], [Bridge – guitar only]. Settings: Vocal Gender male, Max Mode off, style influence about 85, weirdness about 15, Duration about 180 s. Exclude: country, harmonica solo, screaming, double-time, sitar."
  },
  {
    "name": "trip-hop-two-voice-duet",
    "idea": "A blend of two different deep English voices trading lines: a murmured, close-mic baritone in the verses and a rougher, older, weathered voice that takes the choruses. They sing the last chorus together. Ask for the music as Bristol-style trip-hop: a slow 86–88 BPM dusty break, dub-weight bass, a picked acoustic guitar loop, smoky and dark, very dynamic between sparse verses and full hooks. Mark each voice with lyric tags such as [Voice 1] and [Voice 2] and [Both]. Leave Vocal Gender unset. Settings: Max Mode on, style influence about 70, weirdness about 30, Duration about 220 s. Exclude: female vocal, screaming, fast rap, EDM drop, sitar."
  }
]
```

Your message also asks for repo and skill changes so this can't happen again. I couldn't make those from here. When we're back in the repo, I suggest:
- Make `sameness.py` a hard block that can't be overridden.
- Have it also flag rounds where the settings are all alike, such as every take having Max Mode on and 285–300 s.
- Add one house rule: each experiment brief must name a different kind of performer and a different way of asking for the music.

**Sources:**
- https://suno.com/song/024b82e8-378c-47bd-bf73-bb5eafea2ed5
- https://roo.beehiiv.com/p/suno-v5-5-changed-the-prompting-rules-here-are-the-formulas-that-actually-work
- https://roo.beehiiv.com/p/suno-prompting
- https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/how-to-make-suno-preserve-a-natural-folk-tenor-suno-v5-5-voice-guide
- https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/keep-same-singer-across-ai-songs-suno
- https://reddit.sentinel-team.org/posts/1s47g9t/snapshots/2026-03-27T18%3A20%3A17.4177Z
- https://medium.com/@abhisheksd2003/the-ultimate-suno-ai-prompt-guide-with-clear-tested-examples-2d827ffe8b3a
- https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-prompt-contained-inappropriate-material
