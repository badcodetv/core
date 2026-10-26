I wrote one prompt, for the **duet-kids-choir-bracket-driven** experiment. It's built from Jack's three reference songs plus what I could find on how Suno reads brackets.

**How it's built:**
- **Brackets are hints, not commands.** Jack Righteous's v6 guides say Suno treats a bracket as a nudge and may ignore it. Each bracket should do one job (where we are, how it's sung, or what the band does), and if Suno sings a bracket out loud you shorten it or remove it. So every section gets one short bracket, and the singer and the arrangement go in separate brackets.
- **Duet labels drift.** A Reddit user reported Suno ignoring [male]/[female] and handing out voices at random. A duet guide suggests describing the duet in the style box and tagging lines in the lyrics. So the style sentence names all three voices, vocalGender is null, and the Pablo Escobar section has a Male or Female tag on every line, alternating.
- **Kids choir.** Suno's kids page recommends short chant lines and call-and-response, which fits the "Robbery, robbery!" chorus. The cue says "sing-along shout" and screaming is excluded, so it should come out cheeky rather than screamed.
- **The references.** "Eminence Front" is basically a two-chord synth loop, with guitar doubling the riff and a busy Entwistle bass line over a steady beat. That's the model for the clavinet-and-bass loop. "I Ain't Worried" runs at about 140 BPM, so I kept 104 BPM to give a funkier, slower pocket. I didn't find its whistle hook written up anywhere, so the whistled outro is my own idea taken from the song. I found nothing on how "Million Dollar Baby" was made beyond its chart history.
- **Settings.** I put styleInfluence at a medium 55 so the brackets steer more than the style box. The duration is 300 seconds, the maximum, because the lyrics are long. Exclude Styles covers fast and double-time rap, screaming, metal and growls.

I didn't add or change any words. The lyric lines are exactly as given, and only bracket tags were added. No Cover or Remix, just a fresh Create. Both songs' keys are disputed between sources (F major vs D minor for "I Ain't Worried"), so I left key out of the prompt.

```json
{
  "name": "duet-kids-choir-bracket-driven",
  "style": "Psychedelic funk-folk at 104 BPM locked on a fat clavinet-and-bass loop, with strummed acoustic guitar, wah-wah electric guitar and a phase-swirled Hammond organ, sung as a duet between a deep deadpan male baritone and a bright cheeky female voice, with a mischievous children's choir on the hooks.",
  "exclude": "fast rap, double-time rap, screaming, metal, growls",
  "lyrics": "[Intro: Clavinet and Bass Only]\n\n[Verse 1: Male Baritone, Deadpan]\nThey say, ya can't make money from a tree\nlet's see, each day, make hay, not free, aay\nwork and get paid though, earning that dough\nbut where does it go? nobody knows!\n\n[Verse 2: Female Voice, Cheeky]\nmeans of production means a reduction\nstandards bleeding, land-lords needing\nquantative easing, grandma FREEEEEEEZING!\nstimulus checks are next. Get wrecked!\n\n[Verse 3: Male Baritone, Deadpan]\nrent seeking?... I'm just about eating\nsorry, did I interrupt your meeting?\nremember kids, the Fed is not your friend!\nit prints all the dollars that the government spends\n\n[Verse 4: Female Voice, Cheeky]\nthis fiat system is insistent\non debts existence, sooooo\ndon't be hating on the credit rating\nor have resistance to the facts I'm stating\n\n[Chorus: Kids Choir Chant]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus: Kids Choir, Sing-Along Shout]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Interlude: Acoustic Strum and Clavinet]\n\n[Verse 5: Male Baritone, Deadpan]\nStacks and stacks of elastic cash\ndistracted by a dispraxic flash,\nmob, angry at their shitty little job\nthe right and the left both witness the theft\n\n[Verse 6: Female Voice, Cheeky]\nblaming each other is a sick little cover\ninstitutional, dilutional, the usual\ndistraction IS the attraction\nthe intention is tension between the factions\n\n[Verse 7: Male Baritone, Deadpan]\ndivide and conquer, just look at the hand\nIt's not ya standard, propaganda, worth a couple grand-ahh\nit is, state, level, manipulation\nit is the devil, with a radio station\n\n[Verse 8: Female Voice, Cheeky]\nstack up the vaults like a wheelbarrow\nrisk of default is really rather narrow\nBiggie said waaaay back in ninety seven\ndon't get high off your own supply\n\n[Chorus: Kids Choir Chant]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus: Kids Choir, Sing-Along Shout]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Instrumental: Wah Guitar and Organ Freakout]\n\n[Verse 9: Duet, Trading Lines]\n[Male]\nYou know the real star is Pablo Escobar,\n[Female]\nwho has elastic bands not plastic hands,\n[Male]\nstacking up the cash by the grands\n[Female]\nstandard plans are for the working man\n\n[Verse 10: Duet, Trading Lines]\n[Male]\nand this right here is a next level scam\n[Female]\nill gotten gains, no need to explain\n[Male]\n\"bail\" and \"out\", will never mean the same\n[Female]\nown the printer and you don't fear winter\n\n[Verse 11: Duet, Trading Lines]\n[Male]\ncrime is asset inflation, passive creation;\n[Female]\nof a wealth gap that drives the situation\n[Male]\nworking people get paid in money, so it's not very funny\n[Female]\nwhen you print more and expect them not to worry\n\n[Verse 12: Duet, Trading Lines]\n[Male]\nhungry people, feed a revolution,\n[Female]\nthen it's retribution, perhaps some execution\n[Male]\nit's time to give, not just to take\n[Female]\nbut for heaven’s sake, don't just eat cake\n\n[Outro: Groove Fades, Whistled Melody]\n\n[End]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 45,
  "styleInfluence": 55,
  "vocalGender": null,
  "durationSec": 300,
  "maxMode": true
}
```

Sources:
- [Jack Righteous – Suno MetaTags in V6](https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/suno-ai-4-5-metatag-tutorial)
- [Jack Righteous – Duet & Harmony Meta Tags for Suno](https://jackrighteous.com/de/blogs/guides-using-suno-ai-music-creation/duet-harmony-theme-meta-tags-suno)
- [Jack Righteous – Suno meta tags beginner structure map](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-meta-tags-basics-beginner-structure-map)
- [Reddit snapshot – Suno ignoring male/female tags](https://reddit.sentinel-team.org/posts/1rzuuw8/snapshots/2026-03-27T18%3A20%3A17.4177Z)
- [Suno – kids music use case](https://suno.com/hi/music-library/use-cases/kids)
- [Medium – What r/SunoAI users actually do](https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad)
- [American Songwriter – Story behind "Eminence Front"](https://americansongwriter.com/story-behind-the-who-eminence-front)
- [Something Else Reviews – The Who](https://somethingelsereviews.com/2011/07/16/something-else-featured-artist-series-the-who/)
- [Laughing Squid – "Eminence Front"](https://laughingsquid.com/the-who-eminence-front/)
- [Wikipedia – I Ain't Worried](https://en.wikipedia.org/wiki/I_Ain%27t_Worried)
- [Music Will – I Ain't Worried chart](https://jamzone.musicwill.org/Songchart/Guitar-IAintWorried-OneRepublic.pdf)
- [Musicnotes – I Ain't Worried](https://www.musicnotes.com/sheetmusic/kimbo/i-aint-worried/MN0265154)
- [Wikipedia – Tommy Richman](https://en.wikipedia.org/wiki/Tommy_Richman)
