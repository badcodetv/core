I built one prompt for the baroque-boom-bap-mafioso experiment. I didn't use any old prompts or the Suno repo, only what I found online.

**What the research showed (all from community guides; I found nothing official from Suno):**
- **Style box order:** genre, then feel/tempo, then two or three signature instruments, then the vocal role, then the texture. No metatags in the Style box, and plain descriptions rather than story. So the tag list is short, and each instrument is named by its job (melody, bass, colour).
- **Length:** one guide says keep the Style prompt under about 100 words. Another says that past 10 tags the signals start to fight and the output goes flat. My list is compact, but at about 14 comma-separated items it's over that 10-tag guideline.
- **Vocal:** guides say to describe the voice's character, delivery and range in the Style box. "Laid-back male rap vocals" with a boom-bap tag and a BPM is a common pattern. No guide covered "monotone" directly, so I spelled it out in plain words.
- **Exclude:** guides say to keep it to the few sounds you can actually hear and don't want. I listed opera, choir, screaming and fast rap, plus a few close variants of each, and kept it to that.
- **Lyrics tags:** use at most one cue per section, and use square brackets. Round brackets turn into backing vocals, so I added none.
- **Settings:**
  - **Weirdness 42, Style Influence 70:** inside the "clean, steady song / sticks closer to the genre" ranges one guide tested. Going higher on both risks a muddled arrangement when blending genres like this.
  - **Variety off:** it reportedly keeps your style tags exactly as written.
  - **Model "v6":** described as the more controlled option; v6-wild is for exploring.
  - **maxMode and duration:** I found nothing on maxMode, so turning it on is my own call. I set the length near the 300-second limit because the lyrics are long.

The lyrics are word-for-word, with only square-bracket tags added. Jack's rules are covered: no screaming, no fast rap, and this is a fresh Create.

Sources:
- [Jack Righteous – negative prompting (v5/v6)](https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/negative-prompting-suno-v5-guide)
- [Jack Righteous – optimize v6 style prompt](https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/optimize-suno-v6-style-of-music-prompt)
- [Jack Righteous – advanced sliders & v6 Variety](https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/how-to-use-suno-s-advanced-sliders-weirdness-style-audio-influence)
- [Medium – Suno Reddit tips](https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad)
- [Roo – Suno prompt guide 2026](https://roo.beehiiv.com/p/suno-ai-prompt-guide-2026-copy-paste-templates-the-formula-that-actually-works)
- [Roo – why prompts fail](https://roo.beehiiv.com/p/your-suno-ai-prompts-are-failing-here-s-the-fix-most-guides-won-t-tell-you)
- [r/SunoAI snapshot](https://reddit.sentinel-team.org/posts/1rrow7g/snapshots/2026-03-14T01%3A32%3A40.93927Z)

```json
{
  "name": "baroque-boom-bap-mafioso",
  "style": "dusty boom-bap hip-hop, 88 BPM, baroque chamber meets psychedelic funk, melody: harpsichord, bass: cello ground bass doubled by funk electric bass, colour: phaser-soaked clavinet, plucked pizzicato strings, swirling fuzz guitar on hooks only, deep monotone male rap, unhurried mob-boss baritone, cool almost bored delivery, never raises his voice, vinyl crackle",
  "exclude": "opera singing, choir, sung vocals, screaming, shouting, fast rap, double-time rap",
  "lyrics": "[Intro: harpsichord and cello ground bass, dusty drums]\n\n[Verse 1: low monotone rap, relaxed]\nThey say, ya can't make money from a tree\nlet's see, each day, make hay, not free, aay\nwork and get paid though, earning that dough\nbut where does it go? nobody knows!\n\nmeans of production means a reduction\nstandards bleeding, land-lords needing\nquantative easing, grandma FREEEEEEEZING!\nstimulus checks are next. Get wrecked!\n\nrent seeking?... I'm just about eating\nsorry, did I interrupt your meeting?\nremember kids, the Fed is not your friend!\nit prints all the dollars that the government spends\n\nthis fiat system is insistent\non debts existence, sooooo\ndon't be hating on the credit rating\nor have resistance to the facts I'm stating\n\n[Chorus: laid-back gang chant]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 2: low monotone rap, relaxed]\nStacks and stacks of elastic cash\ndistracted by a dispraxic flash,\nmob, angry at their shitty little job\nthe right and the left both witness the theft\n\nblaming each other is a sick little cover\ninstitutional, dilutional, the usual\ndistraction IS the attraction\nthe intention is tension between the factions\n\ndivide and conquer, just look at the hand\nIt's not ya standard, propaganda, worth a couple grand-ahh\nit is, state, level, manipulation\nit is the devil, with a radio station\n\nstack up the vaults like a wheelbarrow\nrisk of default is really rather narrow\nBiggie said waaaay back in ninety seven\ndon't get high off your own supply\n\n[Chorus: laid-back gang chant]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 3: low monotone rap, relaxed]\nYou know the real star is Pablo Escobar,\nwho has elastic bands not plastic hands,\nstacking up the cash by the grands\nstandard plans are for the working man\n\nand this right here is a next level scam\nill gotten gains, no need to explain\n\"bail\" and \"out\", will never mean the same\nown the printer and you don't fear winter\n\ncrime is asset inflation, passive creation;\nof a wealth gap that drives the situation\nworking people get paid in money, so it's not very funny\nwhen you print more and expect them not to worry\n\n[Outro: low monotone rap, harpsichord fades]\nhungry people, feed a revolution,\nthen it's retribution, perhaps some execution\nit's time to give, not just to take\nbut for heaven’s sake, don't just eat cake\n\n[End]",
  "model": "v6",
  "variety": "off",
  "weirdness": 42,
  "styleInfluence": 70,
  "vocalGender": "male",
  "durationSec": 290,
  "maxMode": true
}
```
