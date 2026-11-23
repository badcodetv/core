# spy-swagger: what shaped it

- Genre markers taken from write-ups of 1960s spy scoring: a walking jazz bass doubled or answered by electric guitar,
  driving ostinatos, rapid brass chord stabs, vibraphone for a cool, mysterious shimmer, and the minor triad with added
  major 7th and 9th (the "spy chord"). I named the chord and the instruments generically so the prompt describes a
  genre and not any one famous theme.
  - https://vectree.io/pdf/c/1960s-spy-film-harmony
  - https://www.spaceagepop.com/lpspy.htm
  - https://www.allmusic.com/style/spy-music-ma0000012224
- Suno prompting: keep the style box under about 100 words, put the positive direction in the style box, keep exclude to
  fewer than ten categories that don't contradict the style box, and remember "instrumental" still means a full band.
  Exclude covers voices and humming, fade-outs and long intros (the cue has to start at once and end on a button),
  plus modern drum and synth drift.
  - https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/optimize-suno-v6-style-of-music-prompt
  - https://suno.com/release-notes/exclude-styles
  - https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad
- Shape: the style box describes the story arc in order (swagger walk, a dead stop on a sagging brass chord, strings
  climbing to major, a clean button). Suno won't hit exact seconds, so durationSec is 30, which leaves room to trim to
  about 18 s and line the sting up with 12.5 s in the edit. "Sparse, gaps for a narrator" is there to leave room for the
  four spoken lines.
- Settings: model v6 (not wild) and styleInfluence 75 keep it on genre. Weirdness 30 and normal variety give some
  freshness but discourage it from copying a well-known theme. maxMode is on for audio quality, and vocalGender is null
  because the track is instrumental. Lyrics are empty, as the brief requires.
- Risk: the "hope" here is grand (strings and brass) rather than warm, as the brief says. If takes drift towards a
  famous riff, lower styleInfluence or swap the baritone guitar for a vibraphone lead.
