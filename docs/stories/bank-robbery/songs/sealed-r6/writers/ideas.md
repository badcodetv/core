Here's what I found and the four experiments I'd run first.

**Research findings**

*How to prompt Suno v6*
- Suno still blocks artist names in the style box. Describe the era, tempo, instruments, vocal texture and production instead. That suits Jack's "clean room it" anyway: none of the four ideas name an artist or a song. ([roo.beehiiv](https://roo.beehiiv.com/p/best-suno-prompts-v6), [Undetectr](https://undetectr.com/blog/suno-v6-prompts))
- One guide now suggests 2–3 descriptive sentences of about 250–600 characters (the limit is 1,000) instead of a short tag list. Others say to keep the style line to one or two sentences. Unwanted sounds work better in the Exclude Styles field than as "no X" in the style box. Brackets inside the lyrics can carry short performance directions, one per bracket, and v6 reads them. ([roo.beehiiv](https://roo.beehiiv.com/p/best-suno-prompts-v6), [aimusicdaily](https://aimusicdaily.com/suno-v6-prompts), [mysoniq](https://www.mysoniq.com/blog/suno-prompts))
- Set Vocal Gender in More Options and also write it in the prompt. Set Variety to 0 when testing. Raise Style Influence if the style gets half-ignored. Repeating the chorus word for word helps Suno treat it as the hook, and these lyrics already do that. ([roo.beehiiv](https://roo.beehiiv.com/p/best-suno-prompts-v6), [sunostyles](https://sunostyles.com/blog/suno-v6-settings), [Undetectr guide](https://undetectr.com/blog/suno-ai-prompts-guide))
- These are third-party blogs. Suno doesn't publish an official tag spec.

*The three reference songs*
- **"I Ain't Worried":** opens on a simple whistle hook that sets a carefree mood, and the same melody comes back sung in the verse. The guitar and bass lock into a groove with a retro 1960s pop/rock sound and reverb. One transcription site lists it at about 140 BPM in D minor, which isn't confirmed. ([Hit Songs Deconstructed](https://hitsongsdeconstructed.com/hsd_wire/i-aint-worrieds-hooks), [vocals](https://hitsongsdeconstructed.com/hsd_wire/i-aint-worrieds-vocals), [Music Will chart](https://jamzone.musicwill.org/Songchart/Guitar-IAintWorried-OneRepublic.pdf), [Songwriting Mag](https://www.songwritingmagazine.co.uk/?p=62154))
- **"Million Dollar Baby" (Tommy Richman):** described as groovy basslines, "ghostly vocal stacks", catchy hooks and a bouncy, nostalgic feel. One site lists it at about 70 BPM in F# minor, also unconfirmed. ([Official Charts](https://officialcharts.com/chart-news/tommy-richman-million-dollar-baby-who-is-singer), [Complex](https://content-prod.adc-blue.infra.complex.com/music/a/j-rose/everything-you-need-to-know-about-tommy-richman))
- **"Eminence Front":** written from a chord progression on a Yamaha E70 organ. It's mostly two chords over a repeating sequenced synth figure that the guitar doubles. The bass is the centre of the groove, there's Rhodes piano, the lead vocal is cool and understated, and the band adds backing vocals. Reviewers call it arena rock and funk, "electro-disco", with a "strong bottom". The track runs 5:39. ([Wikipedia](https://en.wikipedia.org/wiki/Eminence_Front), [Something Else](https://somethingelsereviews.com/2011/07/16/something-else-featured-artist-series-the-who/), [American Songwriter](https://americansongwriter.com/story-behind-the-who-eminence-front), [DJDMac](https://www.djdmac.com/?p=39124))

*The genre*
- I found no source that defines "psych folk funk" as one genre. Putting the three parent styles together:
  - **Psych folk:** an acoustic base plus psychedelic touches such as chanting and non-Western instruments like sitar and tabla.
  - **Psych funk:** fuzz, wah, echo chambers and voice distorters on top of funk grooves.
  
  ([Psych folk](https://en.wikipedia.org/wiki/Psychedelic_folk), [Psych funk](https://en.wikipedia.org/wiki/Psychedelic_funk), [Psych rock](https://en.wikipedia.org/wiki/Psychedelic_rock))
- Two of the tempo figures fit together: about 140 BPM played with a half-time feel is about 70 BPM. That shared pocket is the starting point for experiments 1 and 3.

```json
[
  {
    "name": "falsetto-whistle-halftime",
    "idea": "This combines the two newer references. A male lead sings in a light, airy falsetto, with ghostly stacked harmonies doubling the ends of lines. The verses are sung in a relaxed rhythm with a lot of space, never rapped fast or double-time. Ask for the music in 2–3 plain prose sentences in the style box: sunny psychedelic folk-funk at about 140 BPM with a half-time feel, a whistled hook that opens the song and returns between sections, a strummed acoustic guitar with a spring-reverb 1960s feel, and a round, bouncy, melodic bass that carries the groove. Add brushed half-time drums and finger snaps. The 'Robbery, robbery!' chorus comes in as a carefree gang singalong. Keep the irony that the lyrics are angry while the music sounds untroubled. Long words like 'FREEEEEZING' and 'burrrrring' should be held, playful falsetto notes and should never be shouted. Put screaming, shouting, fast rap and double-time in Exclude Styles."
  },
  {
    "name": "cool-organ-sequencer-arena",
    "idea": "This one leans on the older reference. A male lead in his forties sings in a cool, dry, mid-range voice, half-speaking and half-singing, as if he's reporting the theft while shrugging. He stays understated and never rushes the words. Ask for the music as an era and production description: early-1980s arena rock that has turned to funk, built on a two-chord progression played on a home organ, with a sequenced synth figure looping the whole time and a clean electric guitar doubling it. Add a busy, nimble bass at the centre of the groove, steady four-on-the-floor drums at about 116 BPM, Rhodes piano, and a 12-string acoustic for the folk side. Fit the psychedelic part into the long instrumental breaks: a phased guitar solo and a tape-echo wash before each chorus. Low backing vocals from the band answer 'Debasement!' in the chorus. Use a long groove intro and a long outro so the song can run past five minutes."
  },
  {
    "name": "sitar-tabla-storyteller",
    "idea": "This is the folk end of the idea. A female lead with a warm, slightly smoky alto tells the lyrics like a folk storyteller at a late-night gathering: wry, rhythmic, close to the mic, sung and spoken in a relaxed rhythm with no rap speed. In the chorus a rough mixed crowd answers her in call-and-response. The prompt should list the instruments one by one: sitar drone and riffs, tabla, a fingerpicked nylon or steel acoustic guitar, a fuzz-and-wah electric guitar that slowly builds up through the song, a deep slow-funk bass, a hand-drum groove, and handclaps. Aim for about 70 BPM. Use only short directions in brackets, such as [Spoken], [Crowd Answers] and [Sitar Break]. The [Final Verse] should lose the drums and go almost a cappella over the sitar drone for 'hungry people, feed a revolution', so the words land. Then everyone comes back in for the end."
  },
  {
    "name": "duet-kids-choir-bracket-driven",
    "idea": "This is a voice and arrangement idea, and most of the arrangement lives in the lyric brackets, not the style box. A low, deep-voiced male baritone sings verses 1 and 3 of each group in a deadpan way. A bright, cheeky female voice takes verses 2 and 4, and they trade lines in the Pablo Escobar section. The chorus is shouted by a playful children's choir, which matches the line 'remember kids, the Fed is not your friend', and it should sound mischievous, not screamed. Keep the style box short, as one sentence: psychedelic funk-folk with a fat clavinet-and-bass groove at about 104 BPM, acoustic strumming, a wah guitar and a phased Hammond organ. Then use one-cue brackets on every section, such as [Intro: Clavinet and Bass Only], [Verse 1: Male Baritone, Deadpan], [Chorus: Kids Choir Chant], [Instrumental: Wah Guitar and Organ Freakout] and [Outro: Groove Fades, Whistled Melody]. Put fast rap, screaming and metal in Exclude Styles."
  }
]
```
