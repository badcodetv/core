My research found:

- **The reference page:** Both takes are on the same public Suno page, titled "brj-sr5-brixton-baritone-dub-echo-v6-w35", made by binocarlos on model V6. The page shows the short tags "psych, folk, funk", and the full style text is hidden behind "Show full styles". It also shows the lyric sheet with its bracketed directions. ([take 1](https://suno.com/song/7aa63b33-dbfa-4201-9b3b-78ae4ba48103), [take 2](https://suno.com/song/3dd31d66-3c71-498a-98df-9d57a340e4b2))
- **What went wrong in the reference:** The listening pass heard take 2 as boom-bap with a "UK male rap vocal", even though the box says "never rapped". Take 1's ride-out from 3:45 was also called long and repetitive. So every iteration below keeps the voice spoken or sung, and keeps the hook big without screaming.
- **Suno prompting tips:** Name specific instruments, because Suno reacts strongly to them. Don't stack too many genres in one box. "Choir harmonies" and "operatic choir" are the closest tested phrases for operatic backing. Texture words like "tape-saturated" and "wide stereo" help push a psychedelic sound. ([roo.beehiiv](https://roo.beehiiv.com/p/suno-prompting), [frankx.ai](https://www.frankx.ai/blog/suno-prompt-engineering-complete-guide), [Medium guide](https://medium.com/@abhisheksd2003/the-ultimate-suno-ai-prompt-guide-with-clear-tested-examples-2d827ffe8b3a), [Medium Reddit roundup](https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad))
- **Funk with orchestras, in history:** Isaac Hayes and Curtis Mayfield added orchestral instruments to psychedelic soul, a style called "cinematic soul" ([Wikipedia](https://en.wikipedia.org/wiki/Psychedelic_soul)). David Axelrod mixed heavily miked drums with baroque orchestration ([Wikipedia](https://en.wikipedia.org/wiki/David_Axelrod_(musician)), [Songs of Experience](https://en.wikipedia.org/wiki/Songs_of_Experience_(David_Axelrod_album))). Ghost Funk Orchestra carries that "futuristic grandeur" on today ([Treble](https://www.treblezine.com/ghost-funk-orchestra-a-song-for-paul-review/)). None of these sources describe operatic choirs in that music, so each iteration names its classical parts exactly: soprano, male chorus, string quartet, harpsichord or timpani.

```json
[
  {
    "name": "axelrod-baroque-strings-chorus",
    "idea": "Keep the box's opening, tin whistle, congas, crowd chant and dub layers. Make the funk heavier with Axelrod-style heavily miked breakbeat drums, a wah-wah clavinet and phaser on the skanks, next to the fuzz bass. Behind everything, a baroque string section and harpsichord play countermelodies in the verses, and a mixed opera chorus sings wordless 'aah' swells under the hook. The singer is the same deep South London baritone, now cool and chilled, a velvet late-night pirate-radio DJ murmuring the patter with a half-smile. He gets lively on the builds and sings out big and soulful on the hook, never shouting. Keep 'half-crooned, never rapped' word for word."
  },
  {
    "name": "soprano-descant-wah-funk",
    "idea": "Keep the tin whistle, hand drums, congas, crowd of mates, spring-reverb skanks and echo throws. Push the psych funk hard: fuzz-wah lead guitar licks between lines, tape-saturated phased drums and a rubbery slap-and-fuzz bass. The classical part is one operatic soprano singing a wordless high descant far back in the reverb, only in the hooks and the bridge, plus soft cello drones under the verses. The singer changes to a younger Brixton tenor-baritone: laid-back and stoned-cool, drawling the verses in sly half-sung patter. He lifts into a bright, eager soulful melody with falsetto flicks on the hook, excited but not screamed."
  },
  {
    "name": "male-opera-chorus-timpani",
    "idea": "Keep the same structure, tin whistle up front, congas and dub delay throws. Thicken the funk with a Leslie-swirled Hammond organ, a squelchy envelope-filter bass doubled by fuzz, and a phased wah guitar break. Add a low male opera chorus humming and chanting long notes like a Verdi crowd, French horns, and timpani rolls on each build, all behind the band. The singer is an older, smoky, gravel-edged South London raconteur, slow and conspiratorial like he's sharing a secret at closing time. He swells into a warm, gospel-tinged baritone belt for the hook and last hook, staying round and controlled."
  },
  {
    "name": "pizzicato-quartet-mellotron-psych",
    "idea": "Keep the box's frame: tin whistle, congas, slinky funk bass, crowd chant, spring-reverb skanks and echo throws. Make it more psychedelic with mellotron strings, backwards guitar swells, wide-stereo auto-panned wah and a deep head-nodding funk breakbeat, while keeping the fuzz bass doubling. The classical part is a string quartet whose pizzicato answers the tin whistle in the verses and bows sweeping lines in the bridge. One operatic tenor sings a soaring wordless line in the final hook only. The singer is a cool, dry, Gil Scott-Heron-style spoken-soul narrator with a London accent and a deep baritone, unbothered and understated. He sparks up with grinning, soulful runs and bigger held notes when the hook and bridge arrive, never rapped or double-time."
  }
]
```
