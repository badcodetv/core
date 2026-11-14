# violin-jab-music-box: what shaped it

Kai's recipe taken literally: voice, jab, small foreboding pattern. Three events in the lyrics box, one per bracket, so the model has room between them in 15 s.

- **Speech, not song.** Styles name the delivery directly ("spoken-word", "no singing", "beatless", "voice-forward mix") and avoid hook/chorus/anthem words, which signal a song; lines kept as plain prose, no rhyme, no repeats. Source: https://jackrighteous.com/es/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-narration-workflow
- **Parentheses around the spoken words** under a [Spoken ...] tag, one blog's claim that bare text tends to get sung (unverified; it is a cheap hedge). Source: https://apipass.dev/blogs/7-pro-suno-prompt-hack
- **Bracket tags as stage directions** in the lyrics box ([Single violin stab], [Detuned music box loop], horn) and sound in the style box. No source documents sound-effect brackets in v6, so treat these as experiments; if a tag is read aloud, move it into Styles. Sources: https://blakecrosley.com/guides/suno-ai-music-generation, https://jackrighteous.com/es/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-narration-workflow
- **Named instruments first and few.** Suno is very sensitive to named instruments, so only two are named (solo violin, music box) and drums are excluded and replaced by "beatless, rubato". Source: https://alexanderweichart.de/2_Areas/Music/Suno-Instructions
- **Max Mode on**: Suno's v6 FAQ ties it to vocal consistency, per https://sunowatermark.com/blog/suno-v6-vocal-prompts-2026/
- **vocalGender null** because there are two speakers (young man, older woman); the gender toggle would flatten one of them.
- Model v6 rather than v6-wild: the shape (three separate events) matters more than surprise. Weirdness moderate (35) for the detuned music box; style influence high (75) so the beatless/no-singing direction holds.
- Caveat: Suno is not a TTS engine and exact words are not guaranteed; check the take against the two lines before using it. A separate Speech beta exists (Oct 2026) if the words drift.
