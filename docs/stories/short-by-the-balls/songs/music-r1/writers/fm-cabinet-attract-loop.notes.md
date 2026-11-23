# fm-cabinet-attract-loop: notes

What shaped it:

- The sound source: the Yamaha YM2151 (OPM), an 8-channel, 4-operator FM chip used on Sega arcade boards from 1985 and by Konami, Capcom, Data East, Irem and Namco through the mid-to-late 1980s. Sega's racing board paired it with a separate PCM chip for sampled sounds, which is where the "thin sampled drums" over an FM lead and bass come from. So the style names the 4-operator FM lead, the FM slap bass and the PCM drums, and leaves out any game titles or composers.
  - https://en.wikipedia.org/wiki/Yamaha_YM2151
  - https://segaretro.org/Sega_OutRun
  - https://vgmrips.net/wiki/OPM
- Suno style-box practice (community guides, not official docs): put genre and era first, then the named instruments, and keep the whole thing short, under about 100 words. Put unwanted things only in Exclude and keep that to a few items, because negations written in the style box can pull the unwanted thing in. Turning Variety down keeps tight control of the style tags. The guides also note that sections inherit from the style, so the shape goes in as one plain sentence.
  - https://pastebin.com/ZFsx2ZAt
  - https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad
  - https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/where-to-put-your-suno-prompt-guide
- Shape for the 15-20 s short: an eager loop for the claw attempt, a minor game-over figure when the couple loses, one nearly empty bar with just a held pad under the spoken line (about 3 s, which is roughly two bars at 140 BPM, so trim in the edit if needed), then a stage-clear fanfare for the win. durationSec is 30 to give room to cut.
- Settings: v6, Variety off and styleInfluence 80 to hold to the tags, and weirdness 30 to stay in the genre.
