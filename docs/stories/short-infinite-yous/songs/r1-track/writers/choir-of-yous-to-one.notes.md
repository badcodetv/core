# choir-of-yous-to-one: what shaped it

- Sound effects inside a full Suno song are not an official command; concrete, specific cues (source, distance, texture) on their own line between section boundaries work best, reinforced in Styles, one or two per section. So each SFX is both in the style box and a bracketed cue placed at a section seam (intro rain/sax, outro cab door + horn).
  https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-ai-sound-effects-asterisks
- Speech instead of singing: positive wording ("spoken plainly, no melody") plus stripping anthem/chorus/hook words; short sentences. Used for the boy's line; "anthem, big chorus, polished pop vocal" go in exclude. Suno's separate Speech model exists but this experiment keeps everything in one Create.
  https://jackrighteous.com/es/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-narration-workflow
- Voice switches mid-song are unreliable unless tagged per section and changed structurally at the switch point; child voice is steerable by describing a boy/child. So the boy's line sits in its own [Break] where everything drops away. vocalGender stays "male" for the lad (the bulk of the track); risk: the child line may come out as the lad speaking.
  https://github-wiki-see.page/m/nefarious671/sophia/wiki/suno
  https://libreddit.winscloud.net/r/SunoAI/comments/1ji0g3c/guide_how_to_make_good_songs_with_multiple_voices
- v6 has a Duration control; set 15 s per the brief. Lyrics kept word for word; the choir is a direction only (no repeated words), so Suno must make the "many of him" from texture, not extra lyrics.
  https://help.suno.com/en/articles/13924801
- Settings: v6, variety normal, weirdness 60 (room for the odd stereo choir smear), styleInfluence 55 (the style box carries most of the SFX so it needs weight, but not so much it flattens the hush).
