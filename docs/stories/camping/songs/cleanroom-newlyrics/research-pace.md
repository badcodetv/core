# Research: fast, continuous, gravelly MC rap over 174 BPM DnB in Suno v6 Add Vocals / Edit vocals

Web-only research, 2026-11-06. Tags: [vendor] Suno's own docs, [tested] someone ran it and showed results,
[reported] blog or forum claim, [inference] my reasoning. Nothing here was measured by us.

## Answer (levers, most promising first)

1. **Write for the rate you want.** Suno fits the words it is given into the time it has, so put roughly 2 bars of 174 BPM words on each lyric line (about 8–10 words, 12–16 syllables), and drop any end-of-line full stop or comma. Line ends with punctuation are the documented pause signals. [reported + inference]
2. **Fewer, longer lines; join run-ons.** Short lines and periods or ellipses are what guides say to use when you WANT space, so do the opposite: run the thought over the line break (enjambment, no end punctuation, the next line starting mid-phrase). [reported, inverted by inference]
3. **Say "half-time" is wrong in the style box.** DnB guides assume the vocal sits at half-time against 174 BPM. That is the likely cause of 2.5 words/s with gaps. Spell the feel out: "MC flow locked to the 174 BPM drums, one syllable on every beat, continuous, no pauses between lines", not "fast" or "rapid" alone. [reported + inference]
4. **Pair the speed word with a density word, and put delivery on each section header**, e.g. `[Verse | rapped, tight to the beat, continuous]`. A bare header leaves delivery to chance; "rapid" alone often gives a normal pace. [reported]
5. **Variety 0, and raise Audio Strength/Influence.** Variety 0 keeps Suno from rewriting the style tags [vendor]. Raising audio influence anchors the "rhythm, phrasing" of the source more [reported], so the vocal should lock harder to the uploaded drums [inference, untested].

## 1. Lyric box: what removes pauses

- Suno's FAQ-style material says line breaks and punctuation insert short pauses. [reported] https://www.scribd.com/document/859627879/suno-wiki
- "Continuous text gives Suno no signal to pause between phrases"; "ellipses in particular tell Suno to pause"; periods and question marks mark phrase ends; "4-6 words per line" gives slower, clearer delivery. That page is about fixing rushed vocals, so do the reverse here: longer lines, no ellipses, no end stops. [reported] https://hookgenius.app/learn/fix-suno-rushed-lyrics/
- Commas are short pauses, ellipses trail off, ALL CAPS gives a shouting effect, hyphens STRETCH a syllable ("lo-ove"). So for speed, **avoid hyphens and ellipses**. ALL CAPS may add grit and energy but is a shout, not speed. [reported] https://github.com/bitwize-music-studio/claude-ai-music-skills/blob/main/reference/suno/best-practices.md
- "Leave breath every 2–4 lines (comma, short line, or rest word)" is the opposite of what we want, and it confirms that short lines and commas are read as breaths. [reported] https://suno.ing/blog/suno-rap-hiphop-guide/
- Dense or long lyrics make Suno "rush, compress sections, or skip content", and past about 15 syllables a line it smears consonants. This is the ceiling: aim for about 12–16 syllables a line, not 20+. [reported] (bitwize link above); https://hookgenius.app/suno-lyrics/
- Rap density guides give 12–16 syllables per bar for hip-hop [reported] https://hookgenius.app/learn/suno-custom-lyrics-guide/. At 174 BPM a bar is about 1.38 s, so one word per beat is about 4 words a bar, or about 5–6 syllables a bar. Our target is NOT dense in bar terms. It only looks fast because the bars are short. [inference]
- One r/SunoAI commenter staggers lines with carriage returns and uses "dots and exclamation marks" as beat markers to steer tempo. [reported] https://reddit.sentinel-team.org/posts/1stkj44/snapshots/2026-04-23T19%3A50%3A08.686072Z
- Run-on technique to test [inference, untested]: one lyric line per 2 bars, no end punctuation, the next line starting with a conjunction or the second half of a phrase ("...and the gnome in the hedge / never blinked when the..."). Keep blank lines only between sections, never inside a verse, because a blank line reads as a section or phrase break.
- Arithmetic check [inference]: a 47 s verse at ~3 words/s is ~140 words. At 2.5 words/s with gaps, the verse probably had fewer words than the time allowed, so Suno spread them out. **Count the words first: ~135–150 per 47 s verse.** If the verse is shorter, the model will fill the time with pauses whatever the style box says.

## 2. Style box: speed and density words

- "rapid" or "rapid-fire" alone often gives a normal-paced vocal; pair it with "multisyllabic". They also say going much over 100 BPM makes rapid lyrics rushed or unclear. That is boom-bap advice: at 174 we want one word per beat, which is not rapid in syllable terms. [reported] https://lyromusic.com/prompts/fast-technical-rap
- Name the flow, because Suno "defaults to a generic mid-tempo cadence". Their examples are triplet, double-time and laid-back. [reported] https://hookgenius.app/learn/suno-rap-prompts/ ; https://hookgenius.app/learn/suno-hip-hop-prompts/
- "double-time" is the word to AVOID, since we do not want twice the speed. "half-time" is also wrong. Describe the target instead: "one syllable per beat at 174 BPM", "steady sixteenth hats feel", "continuous MC chat over the breaks". [inference]
- Jungle guides say "Vocal: mc / toasting", "an MC riding the rhythm with hype call-outs", per-section delivery like "[Verse | rapped, tight to the beat]", verse lines ~10 syllables, and Variety at 0. **They also state "DnB vocals sit at half-time against 174 BPM drums, so lines can be longer and legato"**, the likely default we are fighting. [reported] https://sessionsheet.com/suno-prompts/jungle
- "energetic", "driving", "upbeat", "fast-paced" push delivery faster; "laid-back", "relaxed", "unhurried" slow it. Use the first set and keep the second out of every box. [reported] https://hookgenius.app/learn/fix-suno-rushed-lyrics/
- Stop the singing: put "[Rapped]" before each verse and "rapped delivery, spoken cadence, no melody on verses" in the style box. [reported] https://academy.techpresso.co/prompts/suno-prompts (search summary). V6 follows the style box "more literally" than v5, and can "read" over-packed lines rather than rap them. [reported] https://undetectr.com/blog/write-lyrics-for-suno-ai
- A tempo number in the style box is "a strong hint, not a lock" and can double or halve. On Add Vocals the instrumental already fixes the tempo, so state 174 to describe the beat, not to set it. [reported] https://hookgenius.app/learn/suno-tempo-bpm-guide/

## 3. Meta tags: [Fast Rap], [Chopper], [MC], [Flow: ...]

- [Fast Rap] appears in third-party tag lists for v5. Nobody shows what rate it produces. [reported, untested] https://openmusicprompt.com/blog/suno-ai-metatags-guide ; https://musci.io/blog/suno-tags
- [Chopper]: no source found that shows it working in Suno. In real rap, chopper means 2–3x the syllables of normal rap, which is exactly the double-time we must avoid. **Do not use it.** [inference] https://en.wikipedia.org/wiki/Chopper_(rap)
- [Rap Verse] with a parenthetical "(aggressive rap flow)" is suggested as a fix when Suno sings. [reported] (bitwize link above)
- A header plus delivery in one bracket (`[Verse | rapped, tight to the beat]`) is the most specific tested-style suggestion found, but it is still unmeasured. [reported] (sessionsheet link above)
- **Not found:** any measured test of a bracket tag changing words per second, in any Suno version.

## 4. Add Vocals / Edit vocals settings

- Add Vocals works on an uploaded or generated instrumental. You enter lyrics; the "Audio Strength" slider (advanced options) "controls how closely the new song follows the original instrumental". Describe the existing instrumental as accurately as you can in the style box. [vendor] https://help.suno.com/en/articles/6882817
- v6 FAQ: Variety "adjusts and updates your style prompts"; set it to 0 to keep control of your style tags. Max Mode keeps "vocals and style consistent through the whole track". [vendor] https://help.suno.com/en/articles/13924481
- Raise Audio Influence "when the source melody, rhythm, phrasing or character should matter more". Suggested 65–85 to preserve an upload. That is the author's workflow, not a Suno preset. [reported] https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/how-to-use-suno-s-advanced-sliders-weirdness-style-audio-influence
- Weirdness over ~75 tips into chaos (one Reddit user); 50 is "normal". [reported] (same jackrighteous page / Reddit snapshots)
- **Not found:** anything showing that any slider changes vocal TIMING or words per second in Add Vocals. The "Edit vocals" label in the new card menu is not documented on the web yet; the help article still says "Add Vocals". My inference is that higher Audio Strength ties the vocal to the drum grid, and that a high Style Influence makes Suno read the flow words more literally. Test one slider at a time.

## 5. Gravelly MC voice

- "gravelly" sits in common Suno voice tag lists beside raspy, rough and aggressive, and the descriptors go at the start of the style box. [reported] (bitwize link above)
- A single adjective underperforms; stack texture words ("rough, raw, gravelly, weathered"). [reported] https://reddit.sentinel-team.org/posts/1rt6sqr/snapshots/2026-03-17T01%3A21%3A22.866161Z
- One user found repeated "raspy" drifted to a whispery female-pop rasp. **Prefer "gravelly / rough / hoarse" and "male" over "raspy"**, and keep "breathy" and "whisper" out. [reported] (Reddit snapshots via search, link not confirmed)
- Voice tags are inconsistent in v5+; the top advice is to use a Persona/Voice if one exists. [reported] https://reddit.sentinel-team.org/posts/1sbpl3c/snapshots/2026-04-09T19%3A10%3A59.878122Z
- Lines bleeding into each other: no Suno source covers this. The closest is the run-on lyric formatting in section 1 plus a style phrase like "no breaths between lines, phrases run into each other". [inference, untested]

## Candidate wording (untested, no artist names)

Style: `gravelly rough male MC, jungle drum and bass 174 BPM, MC chat locked to the breaks, one syllable on every beat, continuous flow with no gaps between lines, phrases run into each other, rapped not sung, hoarse UK voice, energetic, driving` / Exclude: `singing, melody, half-time vocal, double-time, laid-back, whisper, breathy, auto-tune`
Lyrics: `[Verse | rapped, continuous, tight to the beat]`, then about 17 lines of 8–9 words each (~140 words per 47 s), no end punctuation, no hyphens, no ellipses, no blank lines inside the verse.
Settings: Variety 0; Audio Strength up from your last value in steps (e.g. +15); Weirdness ~40–50.

## Could NOT find

- Any measured words-per-second results for any Suno tag, style word or slider.
- Anything on DnB/jungle MCing in Suno beyond prompt-template sites. No tutorials, and no Discord summaries reachable.
- Suno documentation on "Edit vocals" (the new label), or on how Audio Strength affects vocal timing.
- Proof that [Fast Rap], [Chopper], [MC] or [Flow: ...] tags do anything in v6.
- r/SunoAI threads specifically on "pauses at line ends"; search surfaced none.
