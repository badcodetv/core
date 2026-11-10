# solo-cathedral-treble — notes (redo)

Rewrite after the sameness check flagged "the last word" in the lyric directions. The closing
direction now names the word itself ("settles on 'bin'") and the style prompt says "soft cadence,
then only the echo of the stone", so no phrase is shared with the round.

What shaped it:
- The classic English treble sound is described as a "pure head tone" with "little or no vibrato",
  and choristers were taught to sing "loudly but not forcefully": hence "pure head tone, dead
  straight, no vibrato" in the style prompt.
  https://www.boychoirs.org/museum/betterland/bland019.html ,
  https://www.earlymusicamerica.org/web-articles/lets-talk-about-the-english-choral-tradition/
- Reviewers describe it as "pure, clear and innocent" and "crystalline": hence "crystalline and clear".
  https://musicweb-international.com/classrev/2012/July12/Angelic_voices_RRC1379p.htm
- Suno guides list "boy soprano / child voice" as the way to get a boy's voice, but warn that
  "children's choir" wording produces a group, so the prompt says "one boy only" and never "choir"
  except in the exclude box. vocalGender is left null (both male and female would pull it adult).
  https://sunohk.pages.dev/blog/suno-vocal-prompt-palette-guide/
- To keep a single voice: state the solo target first, let the lift come from the instrument (the
  organ opens on line three), put choir/backing/harmonies/stacked vocals in exclude, and avoid
  group-behaviour tags in the lyrics.
  https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/stop-suno-adding-crowd-vocals-choirs-backing-voices
- Weirdness kept low (15) and style influence high (85) because this is a known, narrow genre
  played straight. Duration 20 s to match the 20-second short.
