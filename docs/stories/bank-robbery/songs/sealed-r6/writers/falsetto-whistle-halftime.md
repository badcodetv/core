I wrote one prompt for **falsetto-whistle-halftime**. This is what shaped it:

- **The whistle hook from "I Ain't Worried."** Hit Songs Deconstructed says the song opens with a simple whistled hook, then answers it with a short title hook after the chorus. Under it is a guitar-and-bass groove with reverb that gives a 1960s pop feel. The producer kept the whistle as recorded because of its "natural, indie" tuning. That's why the style box asks for a slightly loose, human-sounding whistle that opens the song and returns between sections, plus the 60s spring-reverb acoustic guitar. https://hitsongsdeconstructed.com/hsd_wire/i-aint-worrieds-hooks · https://audiotechnology.com/?p=68965 · https://www.songwritingmagazine.co.uk/?p=62154
- **The tempo, bass and falsetto from "Million Dollar Baby."** Wikipedia and Tunebat put the song at about 138 BPM. Wikipedia describes the bass as "ridiculously bouncy," and reviewers singled out Richman's high falsetto. That matches your 140 BPM half-time brief, so the bass is written as the main groove and the falsetto as light, never strained. https://en.wikipedia.org/wiki/Million_Dollar_Baby_(Tommy_Richman_song) · https://tunebat.com/Info/MILLION-DOLLAR-BABY-Tommy-Richman/5AJ9hqTS2wcFQCELCFRO7A
- **How to fill in Suno's fields.** I only had search snippets of these guides: their pages rate-limited me when I tried to open them. The advice was:
  - In the style box, name the genre, the feel, two or three signature instruments, the vocal's role and the mood.
  - Keep sung words and section tags in Lyrics.
  - Put only sounds you can hear in Exclude Styles, and treat it as a guide rather than a guarantee.
  - Use v6 when you want control, and v6-wild for exploring.

  So the style box is three sentences, the bracket directions are short, and Exclude only lists sounds. https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/optimize-suno-v6-style-of-music-prompt · https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/negative-prompting-suno-v5-guide

**Settings.** None of the sources covered the sliders, so these are my own judgement:
- **Model:** v6, so the track stays on brief.
- **Weirdness:** moderate (42), for some psychedelic colour.
- **Style influence:** fairly high (72), so the half-time feel and the whistle stick.
- **Duration:** 300 seconds, the maximum, because the lyrics are long.

**Structure.** The lyrics end on a verse with no chorus after it. I didn't add any words, so the song ends on a whistled outro instead.

```json
{
  "name": "falsetto-whistle-halftime",
  "style": "Sunny psychedelic folk-funk at about 140 BPM, played with a lazy half-time feel: a slightly loose, human whistled melody opens the track and comes back between sections, over a strummed acoustic guitar soaked in 1960s spring reverb and a round, bouncy, melodic bass that carries the whole groove. Brushed half-time drums and finger snaps keep it light, and the chorus turns into a carefree gang singalong, so the music sounds sun-warmed and untroubled however angry the words get. A male lead floats in a breathy, airy falsetto, singing unhurried verses with lots of space and ghostly stacked harmonies trailing the ends of lines, and he turns the long held words into playful sung falsetto notes, never shouted.",
  "exclude": "screaming, shouting, fast rap, double-time, rapid-fire rap, aggressive vocals, distorted vocals",
  "lyrics": "[Intro: whistled hook, acoustic guitar and bouncy bass]\n\n[Verse 1: airy falsetto, relaxed and spacious]\nThey say, ya can't make money from a tree\nlet's see, each day, make hay, not free, aay\nwork and get paid though, earning that dough\nbut where does it go? nobody knows!\n\nmeans of production means a reduction\nstandards bleeding, land-lords needing\nquantative easing, grandma FREEEEEEEZING!\n[held playful falsetto note]\nstimulus checks are next. Get wrecked!\n\n[Verse 1 continues: ghostly harmonies on line ends]\nrent seeking?... I'm just about eating\nsorry, did I interrupt your meeting?\nremember kids, the Fed is not your friend!\nit prints all the dollars that the government spends\n\nthis fiat system is insistent\non debts existence, sooooo\ndon't be hating on the credit rating\nor have resistance to the facts I'm stating\n\n[Chorus: carefree gang singalong, finger snaps]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus: everyone sings, sunny and light]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Interlude: whistled hook returns]\n\n[Verse 2: airy falsetto, laid-back half-time]\nStacks and stacks of elastic cash\ndistracted by a dispraxic flash,\nmob, angry at their shitty little job\nthe right and the left both witness the theft\n\nblaming each other is a sick little cover\ninstitutional, dilutional, the usual\ndistraction IS the attraction\nthe intention is tension between the factions\n\n[Verse 2 continues: bass melody steps forward]\ndivide and conquer, just look at the hand\nIt's not ya standard, propaganda, worth a couple grand-ahh\nit is, state, level, manipulation\nit is the devil, with a radio station\n\nstack up the vaults like a wheelbarrow\nrisk of default is really rather narrow\nBiggie said waaaay back in ninety seven\ndon't get high off your own supply\n\n[Chorus: carefree gang singalong, finger snaps]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus: everyone sings, sunny and light]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Interlude: whistled hook, spring reverb guitar]\n\n[Verse 3: airy falsetto, unhurried, lots of space]\nYou know the real star is Pablo Escobar,\nwho has elastic bands not plastic hands,\nstacking up the cash by the grands\nstandard plans are for the working man\n\nand this right here is a next level scam\nill gotten gains, no need to explain\n\"bail\" and \"out\", will never mean the same\nown the printer and you don't fear winter\n\n[Verse 3 continues: stacked ghostly harmonies]\ncrime is asset inflation, passive creation;\nof a wealth gap that drives the situation\nworking people get paid in money, so it's not very funny\nwhen you print more and expect them not to worry\n\nhungry people, feed a revolution,\nthen it's retribution, perhaps some execution\nit's time to give, not just to take\nbut for heaven’s sake, don't just eat cake\n\n[Outro: whistled hook, bass and snaps fade out]\n[End]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 42,
  "styleInfluence": 72,
  "vocalGender": "male",
  "durationSec": 300,
  "maxMode": true
}
```
