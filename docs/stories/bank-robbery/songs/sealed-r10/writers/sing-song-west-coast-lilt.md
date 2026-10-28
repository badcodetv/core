I researched this from scratch and didn't use any old prompts or the Suno skills/repo. Most of what I found comes from third-party guides; I didn't find official Suno v6 documentation, and some of the guides disagree with each other.

**What shaped it:**
- **Tag order:** the guides say Suno gives more weight to words near the front of the style field. So the genre comes first and the voice comes straight after it, as the brief asks. I spent two of the 10 tags on the voice so the drawl doesn't get lost.
- **Tag count:** one guide warns that more than about 10 tags start to conflict, and another recommends 4 to 7. I used 10, the top of the 8–10 the brief allows. Each tag describes something different, so they shouldn't fight each other.
- **Blending funk and classical:** I listed the strings and the talkbox as named instruments. Then I added "string section and funk rhythm interlocked" so the two styles play together instead of taking turns.
- **Exclusions:** the guides say "no …" wording in the style field is unreliable, so everything Jack wants kept out is in the Exclude field instead.
- **Hook cue:** a vocal cue placed inside the lyrics, next to the lines it applies to, can stop Suno ignoring the vocal description. So the only cue is on the Robbery hooks.
- **Tempo:** Suno reportedly treats a BPM number as a rough guide. That's why "slow" sits next to "86 BPM".
- **Settings:**
  - Variety is off, because Suno's FAQ says 0 keeps your style tags fully under your control.
  - Style Influence is high (78), because a guide says a detailed style field should be paired with a strong setting.
  - Weirdness is 45. Suno calls 50 the normal result and lower values more conventional, so this stays slightly safe and keeps the strings from turning messy.
  - I chose plain v6 over v6-wild because the strict tags matter more here.
  - The length is set to the 300-second maximum because the lyrics are long and the tempo is slow.
  - I couldn't find any documentation on maxMode, so turning it on is a guess.

The lyrics are unchanged word for word, including the curly apostrophe in "heaven’s". I only added section tags.

Sources: [Blake Crosley – Style field & Style Influence](https://blakecrosley.com/blog/suno-style-field-style-influence) · [Suno Watermark – Variety, Style, Weirdness](https://sunowatermark.com/blog/suno-v6-variety-style-influence-weirdness/) · [Jack Righteous – optimise v6 style prompt](https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/optimize-suno-v6-style-of-music-prompt) · [Jack Righteous – sliders guide](https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/how-to-use-suno-s-advanced-sliders-weirdness-style-audio-influence) · [roo – 2026 prompt guide](https://roo.beehiiv.com/p/complete-suno-ai-prompt-guide-2026-301-styles-the-exact-formula-and-why-your-outputs-sound-random) · [Medium – r/SunoAI tips](https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad)

```json
{
  "name": "sing-song-west-coast-lilt",
  "style": "slow psychedelic funk, mellow slightly nasal West Coast rapper with a sing-song lilt, smooth stretched drawl on long vowels, 86 BPM, romantic-era string orchestra, legato violins, cello counter-melody, talkbox echoing the hook, string section and funk rhythm interlocked, warm analog low end",
  "exclude": "operatic vocals, soprano, choir, screaming, rapid flow",
  "lyrics": "[Intro]\n\n[Verse 1]\nThey say, ya can't make money from a tree\nlet's see, each day, make hay, not free, aay\nwork and get paid though, earning that dough\nbut where does it go? nobody knows!\n\nmeans of production means a reduction\nstandards bleeding, land-lords needing\nquantative easing, grandma FREEEEEEEZING!\nstimulus checks are next. Get wrecked!\n\nrent seeking?... I'm just about eating\nsorry, did I interrupt your meeting?\nremember kids, the Fed is not your friend!\nit prints all the dollars that the government spends\n\nthis fiat system is insistent\non debts existence, sooooo\ndon't be hating on the credit rating\nor have resistance to the facts I'm stating\n\n[Chorus: melodic drawl, talkbox answers]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 2]\nStacks and stacks of elastic cash\ndistracted by a dispraxic flash,\nmob, angry at their shitty little job\nthe right and the left both witness the theft\n\nblaming each other is a sick little cover\ninstitutional, dilutional, the usual\ndistraction IS the attraction\nthe intention is tension between the factions\n\ndivide and conquer, just look at the hand\nIt's not ya standard, propaganda, worth a couple grand-ahh\nit is, state, level, manipulation\nit is the devil, with a radio station\n\nstack up the vaults like a wheelbarrow\nrisk of default is really rather narrow\nBiggie said waaaay back in ninety seven\ndon't get high off your own supply\n\n[Chorus: melodic drawl, talkbox answers]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 3]\nYou know the real star is Pablo Escobar,\nwho has elastic bands not plastic hands,\nstacking up the cash by the grands\nstandard plans are for the working man\n\nand this right here is a next level scam\nill gotten gains, no need to explain\n\"bail\" and \"out\", will never mean the same\nown the printer and you don't fear winter\n\ncrime is asset inflation, passive creation;\nof a wealth gap that drives the situation\nworking people get paid in money, so it's not very funny\nwhen you print more and expect them not to worry\n\nhungry people, feed a revolution,\nthen it's retribution, perhaps some execution\nit's time to give, not just to take\nbut for heaven’s sake, don't just eat cake\n\n[Outro]\n\n[End]",
  "model": "v6",
  "variety": "off",
  "weirdness": 45,
  "styleInfluence": 78,
  "vocalGender": "male",
  "durationSec": 300,
  "maxMode": true
}
```
