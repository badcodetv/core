Here are four iterations. Each keeps the reference box (Brixton cadence, music-hall patter, never rapped, crowd of mates on the hook, tin whistle, congas, dub layers) and changes only three things: the psychedelic funk gets heavier, a classical or operatic layer goes in the background, and the lead becomes a cool, laid-back voice that lifts when the song needs it.

**What the research found**
- **Both reference takes:** Their public Suno pages only show the title, creator binocarlos, model V6, the tags "psych, folk, funk" and a 3538-character lyric. The full style box and the length aren't shown. ([take 1](https://suno.com/song/7aa63b33-dbfa-4201-9b3b-78ae4ba48103), [take 2](https://suno.com/song/3dd31d66-3c71-498a-98df-9d57a340e4b2))
- **The two takes drifted in different ways:** The AI listeners heard take 2 as UK boom-bap rap and both takes as clean guitar and keys. Neither heard much fuzz or psych. So the funk and psych need saying louder, and the "never rapped" voice wording has to stay firm.
- **Extra voices:** Suno adds backing voices when a prompt suggests group energy, like a choir lift or call-and-response. The Exclude box can't override a prompt that strongly asks for them. The fix is to name one lead singer clearly and say exactly where the choir or opera singer goes. Here that means behind the lead and away from the patter, so the lead doesn't turn operatic. ([jackrighteous.com](https://jackrighteous.com/de/blogs/guides-using-suno-ai-music-creation/stop-suno-adding-crowd-vocals-choirs-backing-voices))
- **Wording that works:** Tested prompts use plain classical terms like "full orchestral backing", "soft choir backing", "deep baritone", "pipe organ", "strings", "harpsichord" and "soprano". Vocal layering gets written out in full, for example "choir swells on the chorus". ([frankx.ai](https://www.frankx.ai/blog/suno-prompt-engineering-complete-guide), [Suno playlist 1](https://suno.com/playlist/e070c73f-dc02-4811-aad4-dc19398d3ce0), [Suno playlist 2](https://suno.com/playlist/363699c7-3c2f-4a2e-8014-7ccaa6c57731), [Medium guide](https://medium.com/@abhisheksd2003/the-ultimate-suno-ai-prompt-guide-with-clear-tested-examples-2d827ffe8b3a))
- **Real records that do this blend:** Isaac Hayes and Curtis Mayfield added orchestras to psychedelic soul, a style called cinematic soul. David Axelrod mixed sweeping strings with heavy beats. Shuggie Otis's *Inspiration Information* is a reference for psychedelic funk. ([Psychedelic soul](https://en.wikipedia.org/wiki/Psychedelic_soul), [David Axelrod](https://en.wikipedia.org/wiki/David_Axelrod_(musician)), [Psychedelic funk](https://en.wikipedia.org/wiki/Psychedelic_funk))
- **Gap:** I found no record that pairs opera vocals with psychedelic funk. The operatic parts below are my own call, not copied from an example.

```json
[
  {
    "name": "cinematic-soul-strings-soprano",
    "idea": "Keep the box's genre line, tempo, tin whistle, congas, fuzz bass and dub layers, but make the psychedelic funk heavier. Add a wah-wah rhythm guitar and a fuzzed lead guitar riff, still with the spring-reverb skanks. The classical layer is an Isaac Hayes-style cinematic string section: a slow, swelling bed of violins and cellos under the verses. A lone soprano sings a wordless operatic line far back in the echo-chamber delay, only in the hooks and the bridge, and never takes over the lead. The lead becomes a cool, unbothered South London baritone, low and smoky, almost murmuring the patter while leaning on the bar, never rapped. It warms into the big soulful full-throated hook while the crowd of mates chants back."
  },
  {
    "name": "opera-chorus-harpsichord-funk",
    "idea": "Same box, but the funk gets a stabbing clavinet and a rubbery slap-and-fuzz bass locked to the congas, with phased psych guitar on top of the skanks. The classical layer is a distant opera chorus, a mixed choir holding sustained 'aah' chords behind the hooks. A baroque harpsichord adds spiky counter-lines between vocal lines in the verses. The lead becomes a dry, sly South London tenor-baritone with a Brixton lilt: lazy, half-smiling, cool as you like in the spoken verses. His excitement climbs step by step through the builds and peaks in a theatrical, soulful hook, with the crowd of mates and the choir layered behind him. Never rapped, never shouted."
  },
  {
    "name": "axelrod-timpani-baritone-ghost",
    "idea": "Keep everything in the box. Make the funk heavier in a David Axelrod way: a fat, heavy-swinging breakbeat under the hand drums and congas, a grinding fuzz guitar, and psychedelic tape-echo swirls. The classical layer is sweeping orchestral strings and French horns, with timpani rolls into each hook. Far back in the mix, a deep operatic bass-baritone sings long, sustained counter-melody notes like a ghost in the echo chamber, only in the hooks and the last hook. The lead becomes a velvet, laid-back South London crooner, half-whispered and close-mic'd, sitting deep in the pocket. Under the 'Robbery' hook he lifts into a warm, excited, soulful melody, with the crowd of mates chanting back. Never rapped, no screaming."
  },
  {
    "name": "pipe-organ-mezzo-psych-funk",
    "idea": "Same box, but push the funk with a Hammond organ and a Leslie-speaker swirl, a choppy wah guitar and a fuzz bass doubling the bassline all the way through, not just in the hooks. The dub echo throws and spring-reverb skanks stay. The classical layer is a churchy pipe organ and a small chamber orchestra (cellos, oboe) playing grand, solemn chords behind the funk. A mezzo-soprano adds wordless operatic vocalise that drifts through the delay in the bridge and the final hook. The lead becomes a mellow, stoned-sounding, deadpan South London mid-baritone with a grin in his voice, relaxed and chatty in the patter, never rapped. He builds to a joyful, soaring soulful hook, with the crowd of mates and the whole room singing back."
  }
]
```
