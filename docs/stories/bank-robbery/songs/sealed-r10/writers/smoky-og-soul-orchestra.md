I built the style prompt from what v6 guides say works, using only things I found online this session. I didn't use any old prompts or the Suno skills/repo.

**What I found:**
- **Use sentences, not tag lists.** v6 seems to follow a descriptive sentence better than a list of tags. The advice is to start with the genre, say what each instrument and the voice are doing, and include the BPM. The suggested length is about 250–600 characters. Mine is one long sentence of about 460 characters.
- **Say what you don't want in Exclude.** Writing "no X" inside the style prompt doesn't work reliably, so I left all negatives out of it. Exclude gets short phrases: opera singing, choir, belting, screaming and double-time rap.
- **Don't name artists.** Suno blocks artist names, so I described the era, the instruments and the voice instead. Biggie stays in your lyrics as written, since that's a lyric, not a style instruction.
- **Section cues in the lyrics:** the pattern is `[Section | short direction]`, with one idea per bracket. Verses are marked intimate and sparse. Both Robbery choruses bring in the full strings, and the second one in each pair goes bigger.
- **Settings:**
  - **Variety off:** two takes can differ more than one wording change does, so it's off while we test.
  - **Style Influence 75:** the default (50%) can leave the style half-ignored, and a detailed prompt goes better with a strong setting.
  - **Weirdness 40:** just under the middle. One guide says raise it only if results sound generic.
  - **Duration 300 seconds:** v6 tends to stop around 3:10 unless you set the length, and these lyrics are long.
  - **BPM:** treat 84 as a rough target, not a locked tempo. That's why I also wrote "slow, unhurried" and "loose."

All of your words are unchanged, including the curly apostrophe in "heaven’s." Only the bracketed cues are new.

Sources:
- [Roo – The Best Suno Prompts After v6](https://roo.beehiiv.com/p/best-suno-prompts-v6)
- [Blake Crosley – Suno's Style Field and Style Influence Slider](https://blakecrosley.com/blog/suno-style-field-style-influence)
- [Jack Righteous – Suno V6 Style Prompts](https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/optimize-suno-v6-style-of-music-prompt)
- [Jack Righteous – Advanced Sliders](https://jackrighteous.com/es/blogs/guides-using-suno-ai-music-creation/how-to-use-suno-s-advanced-sliders-weirdness-style-audio-influence)
- [AI Music Daily – Suno v6 Prompt Guide](https://aimusicdaily.com/suno-v6-prompts)
- [Undetectr – Suno V6 Mastering Prompts](https://undetectr.com/blog/suno-v6-mastering-prompts)

```json
{
  "name": "smoky-og-soul-orchestra",
  "style": "Slow, unhurried 84 BPM 70s psychedelic soul-funk orchestra played as a classical concert, like the score of a smoky crime film, where string swells and glittering harp runs trade phrases with a fuzz-wah guitar, a breathy flute and warm Rhodes over loose, deep-pocket drums and round bass, while an older, gravelly male storyteller half-speaks and half-raps close to the mic in a relaxed, unbothered drawl, like he's telling the story over a drink.",
  "exclude": "operatic vocals, choir, belting, screaming, double-time rap",
  "lyrics": "[Intro | harp run into a slow string swell, Rhodes alone]\n\n[Verse 1 | intimate, sparse, Rhodes and bass only]\nThey say, ya can't make money from a tree\nlet's see, each day, make hay, not free, aay\nwork and get paid though, earning that dough\nbut where does it go? nobody knows!\n\nmeans of production means a reduction\nstandards bleeding, land-lords needing\nquantative easing, grandma FREEEEEEEZING!\nstimulus checks are next. Get wrecked!\n\n[Verse 2 | soft wah guitar creeps in, still sparse]\nrent seeking?... I'm just about eating\nsorry, did I interrupt your meeting?\nremember kids, the Fed is not your friend!\nit prints all the dollars that the government spends\n\nthis fiat system is insistent\non debts existence, sooooo\ndon't be hating on the credit rating\nor have resistance to the facts I'm stating\n\n[Chorus | full strings come in, big]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus | bigger, harp and flute on top]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 3 | drop back to intimate, flute and Rhodes]\nStacks and stacks of elastic cash\ndistracted by a dispraxic flash,\nmob, angry at their shitty little job\nthe right and the left both witness the theft\n\nblaming each other is a sick little cover\ninstitutional, dilutional, the usual\ndistraction IS the attraction\nthe intention is tension between the factions\n\n[Verse 4 | sparse, low strings murmur underneath]\ndivide and conquer, just look at the hand\nIt's not ya standard, propaganda, worth a couple grand-ahh\nit is, state, level, manipulation\nit is the devil, with a radio station\n\nstack up the vaults like a wheelbarrow\nrisk of default is really rather narrow\nBiggie said waaaay back in ninety seven\ndon't get high off your own supply\n\n[Chorus | full strings come in, big]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus | biggest, fuzz-wah wails over the orchestra]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 5 | intimate again, harp and bass]\nYou know the real star is Pablo Escobar,\nwho has elastic bands not plastic hands,\nstacking up the cash by the grands\nstandard plans are for the working man\n\nand this right here is a next level scam\nill gotten gains, no need to explain\n\"bail\" and \"out\", will never mean the same\nown the printer and you don't fear winter\n\n[Verse 6 | slow build, strings rising]\ncrime is asset inflation, passive creation;\nof a wealth gap that drives the situation\nworking people get paid in money, so it's not very funny\nwhen you print more and expect them not to worry\n\n[Outro | strings fall away, spoken over Rhodes]\nhungry people, feed a revolution,\nthen it's retribution, perhaps some execution\nit's time to give, not just to take\nbut for heaven’s sake, don't just eat cake\n\n[End | last harp run, string swell fades]",
  "model": "v6",
  "variety": "off",
  "weirdness": 40,
  "styleInfluence": 75,
  "vocalGender": "male",
  "durationSec": 300,
  "maxMode": true
}
```
