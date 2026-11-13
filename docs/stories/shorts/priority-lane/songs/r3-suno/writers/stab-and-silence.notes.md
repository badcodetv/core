# stab-and-silence: notes (redo, 2026-11-13)

Rewritten after the sameness check flagged "spoken dialogue only" (Style) and "young man panicked" (lyric direction). Both phrases are gone: the Style box now opens "voices talk and yell, never sing", and the second medic is "Tenor medic, frightened, shrill".

What shaped it:
- Write a spoken performance, not a song. Put "no" phrasing in the Styles box against sung choruses or a melodic lead, take out melodic, hook and chorus words, use a plain [Spoken word] cue at the top of the lyrics, write short punctuated lines, avoid rhyme, and keep any underscore minimal. "rhyme" and "hook" went into the excludes for this reason. https://jackrighteous.com/fr/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-narration-workflow
- Suno does not publish a guaranteed metatag grammar, so bracketed directions only steer. They are kept short ("Sforzando violin stab. Quiet.") so Suno is less likely to read them aloud. https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/suno-ai-4-5-metatag-tutorial
- Suno's separate Speech beta (Oct 2026) makes speech and music together but has no duration control, so this prompt stays on v6 Create with durationSec 14. https://unite.ai/suno-launches-speech-beta-pairing-voice-and-music-in-one-model , https://cryptobriefing.com/suno-launches-speech-tool-spoken-word/

Settings: v6 rather than Wild, so the cast and timing stay readable. styleInfluence is 80 because the no-accompaniment instruction has to win. Weirdness is 55, enough to allow the odd string articulations. vocalGender is null because the cast is mixed.
