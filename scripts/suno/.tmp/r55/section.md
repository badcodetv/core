## v6.47 Round r55 — film-score lanes, and the vocal-pacing stack (2026-09-21)

**Brief, Jack 2026-09-21, after hearing r54:** *"none of those were the right pacing vocally, please
make a faster paced grime rapper rap to the beat of the drum and bass, with orchestral stuff
interwoven in it, please make horror vibes, then action, adventure, thriller, please do film score
genres."*

### 🔴 Say the known risk once, then build it

Three measured rounds (r43 Zimmer, r47 `cinematic`, r48 `grimescore`) found that **the more
film-score a Camping lane carries, the slower the rap gets** — r48's score lane measured 4.6
vocal-band onsets/sec against 5.4 for the take Jack had already called too slow — along with the
weakest low end and the smallest dynamic range. r55 is a deliberate run *at* that finding because
Jack asked for it, so every lane carries the counter-guards: the score is given a **rhythmic job
inside the kit**, the drums are stated as louder than the orchestra, and the pacing stack below is
run at full strength. **If the film-score lanes come back slow again, that is the fourth
confirmation and the answer is a different genre axis, not a different wording.**

### The pacing stack — four levers, because three of them have failed alone

| # | Lever | Why this one |
|---|---|---|
| 1 | 🔑 **Duration 195 s → 155 s** | The same words in 20% less time. It is the only pacing lever that is not a prompt box, and v6 obeys a set duration to about ±1 s — 12/12 takes at r48, 24/24 at r54. Nothing in the Style box can quietly ignore it |
| 2 | **The flow written in musical units** — *eighth notes with sixteenth bursts, two syllables a beat* | Practitioner consensus is that adjectives lose to subdivisions ([HookGenius](https://hookgenius.app/learn/suno-hiphop-prompts/)). 🔑 The arithmetic matters: at 174 BPM sixteenths is 11.6 syllables/sec, which is not a human — **eighths (5.8/sec) with 16th bursts is what fast means here**, and asking for 16ths outright would have produced a chipmunk or been ignored |
| 3 | **The gaps banned** — *no pause at a line's end, never a bar left empty*, plus `[gruff MC, double-time… straight into the next line with no pause]` | r54's takes lost time *between* lines, not inside them |
| 4 | **Excludes carry the pause family** — `sparse flow, pausing between lines, empty bars, half-time flow, slow flow` on top of the standing slow-delivery bans | Delivery bans are the safe place for slowness; tempo bans strangle the opening (r53) |

### The lanes

The variety axis is the **film-score genre**, so the d&b is written as **drum mechanics per lane**,
not as a subgenre noun — `suno-v6.md` §9 has the v6 data point for that (a lazy `liquid DnB` came
back as two-step drums; an engineered breakcore/jungle prompt worked on both models).

| Lane | Score | Drums | The score's job inside the kit |
|---|---|---|---|
| `horror` | shrieking violin clusters, bowed metal, prepared piano | rapid chopped amen, hyperdetail percussion, distorted sub | shrieks land **on the snare**, low strings saw the sub's own notes |
| `action` | pounding low brass, taiko, minor-key brass ostinato | machine-tight breaks, morphing Reese | taiko is **an extra drum inside the break**; brass only in the holes |
| `adventure` | heroic french horn theme in a minor key, sweeping strings, tambourine | rolling jungle breaks, big warm sub, tumbling fills | horn cut into **short answers between the MCs' lines**; tambourine rides the break's hats |
| `thriller` | ticking pizzicato, muted piano, one cold low string | cold skippy breaks, tight snares, creeping Reese | pizzicato **ticks sixteenths against the break like a clock**; piano answers the snare |

### Settings

v6 · Style Influence **80** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 155 s** · workspace `camping-Jack` · weirdness **30 and 60**, a pair per
lane. 8 Creates, 16 takes.

⬜ **The untested lever we still own: Max Mode.** Suno aims it squarely at *songs over two minutes*
and at keeping vocals consistent across a whole track, and every Camping take is over three minutes.
We have never switched it on. It is a slider round, so it costs nothing to design —
`docs/suno-gpt/files/suno-v6.md` §8b.


### r55 horror atom

Style:

```
174 BPM drum and bass: rapid chopped amen breaks, hyperdetail percussion, a distorted sub. Scored like a horror film: shrieking violin clusters, bowed metal, prepared piano. The shrieks land on the snare and the low strings saw the sub's own notes: the score plays the drums' rhythm, one machine, never a soundtrack over a track. Opens on the prepared piano alone, no drums, two lines, already flat out. Under line three the violins climb in semitones and the breaks stutter in early. Drums and sub loudest, breaks never stopping, everything on one 174 grid. Dry, close, horrible, no reverb to hide in. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline. They ride the break in eighth notes with sixteenth bursts, two syllables a beat, consonants like percussion, no pause at a line's end, never a bar left empty.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, slow flow, half-time flow, steady rap pace, measured delivery, sparse flow, pausing between lines, empty bars, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, low brass hits, taiko, war drums, heroic brass, brass ostinato, french horn theme, soaring strings, orchestral tambourine, sleigh bells, ticking pizzicato, clock percussion, muted piano, cold sustained bass, lush strings, orchestral bed, ambient, calm, pretty, major key, uplifting
```

Lyrics:

```lyrics
[Verse 1 | a prepared piano thudding alone, no drums at all | gruff MC, close and quiet but already at full speed]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | the violins climbing in semitones and the breaks stuttering in early]
now, let me explain, how I'm just poor
[Drop | the amen and the distorted sub tear in, violin shrieks landing on the snare]
[gruff MC, double-time from here to the end, two syllables a beat, straight into the next line with no pause]
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
but I bet, that you paid for your wheels on tick
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
I can't live like this forever
I might be insane but I do want change,
let's see what we can arrange
now, I insist that I hold that door
please sir, can I fuckin, have some more?
[Chorus | sung, big and melodic, the shrieking strings take the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, double-time, two syllables a beat, sharp and cutting]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic,
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift
What about if we taxed the rich?
what the fuck you think this is, bitch
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Chorus | sung, big and melodic, the shrieking strings take the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines at full speed, the breaks at their heaviest, bowed metal under every line]
[gruff MC]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[cold MC]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both MCs together]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[cold MC]
you see as it turns out, there is very little clout,
in having the manager or any of the see sweet about
[gruff MC]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[cold MC]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gruff MC]
yet I don't begrudge you,
we were on the same side all along
[cold MC]
well we don't have long
and by the time it hits, we'll be gone
[Chorus | sung, the last time, the prepared piano returns under the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r55 action atom

Style:

```
174 BPM drum and bass: machine-tight breaks, a morphing Reese, hard rolling percussion. Scored like an action film: pounding low brass hits, taiko doubling the kick, a minor-key brass ostinato. The taiko sits inside the break as an extra drum and the brass hits land only where the break leaves a hole: part of the kit, not a layer above it. Opens on one low brass note and a taiko hit, no drums, two lines, flat out. Under line three the taiko doubles and doubles and the brass climbs. Break and Reese stay louder than the brass throughout, one 174 grid. Huge, hard, punchy, mastered loud, no air. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline. They ride the break in eighth notes with sixteenth bursts, two syllables a beat, consonants like percussion, no pause at a line's end, never a bar left empty.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, slow flow, half-time flow, steady rap pace, measured delivery, sparse flow, pausing between lines, empty bars, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, shrieking violins, string shrieks, prepared piano, bowed metal, sul ponticello, french horn theme, soaring strings, orchestral tambourine, sleigh bells, ticking pizzicato, clock percussion, muted piano, cold sustained bass, lush strings, orchestral bed, ambient, gentle, pretty, sentimental, major key
```

Lyrics:

```lyrics
[Verse 1 | one low brass note and a single taiko hit, no drums at all | gruff MC, close and quiet but already at full speed]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | the taiko doubling and doubling and the brass climbing a step at a time]
now, let me explain, how I'm just poor
[Drop | the machine-tight break and the Reese slam in with the brass on the same beat]
[gruff MC, double-time from here to the end, two syllables a beat, straight into the next line with no pause]
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
but I bet, that you paid for your wheels on tick
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
I can't live like this forever
I might be insane but I do want change,
let's see what we can arrange
now, I insist that I hold that door
please sir, can I fuckin, have some more?
[Chorus | sung, big and melodic, the brass takes the chorus alongside the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, double-time, two syllables a beat, sharp and cutting]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic,
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift
What about if we taxed the rich?
what the fuck you think this is, bitch
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Chorus | sung, big and melodic, the brass takes the chorus alongside the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines at full speed, the breaks at their heaviest, taiko inside every bar]
[gruff MC]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[cold MC]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both MCs together]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[cold MC]
you see as it turns out, there is very little clout,
in having the manager or any of the see sweet about
[gruff MC]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[cold MC]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gruff MC]
yet I don't begrudge you,
we were on the same side all along
[cold MC]
well we don't have long
and by the time it hits, we'll be gone
[Chorus | sung, the last time, one low brass note returns over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r55 adventure atom

Style:

```
174 BPM drum and bass: rolling jungle breaks, big warm sub, tumbling fills. Scored like an adventure film in a minor key: a heroic french horn theme, sweeping strings, orchestral tambourine. The horn theme is cut into short answers between the MCs' lines and the tambourine rides the break's hats: the score arrives as rhythm, never a bed. Opens on a lone french horn, no drums, two lines, spat fast over it. Under line three the strings sweep up and the break rolls in under them. Drums and sub above the orchestra throughout, break unbroken, one 174 grid. Wide, warm, cinematic but dirty, tape on the drums. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline. They ride the break in eighth notes with sixteenth bursts, two syllables a beat, consonants like percussion, no pause at a line's end, never a bar left empty.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, slow flow, half-time flow, steady rap pace, measured delivery, sparse flow, pausing between lines, empty bars, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, shrieking violins, string shrieks, prepared piano, bowed metal, sul ponticello, low brass hits, taiko, war drums, heroic brass, brass ostinato, ticking pizzicato, clock percussion, muted piano, cold sustained bass, lush strings, orchestral bed, ambient, cheerful, festive, major key, fanfare, triumphant
```

Lyrics:

```lyrics
[Verse 1 | a lone french horn, no drums at all | gruff MC, close and quiet but already at full speed]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | the strings sweeping up and the break rolling in underneath]
now, let me explain, how I'm just poor
[Drop | the jungle break and the warm sub arrive, the horn answering across the top]
[gruff MC, double-time from here to the end, two syllables a beat, straight into the next line with no pause]
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
but I bet, that you paid for your wheels on tick
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
I can't live like this forever
I might be insane but I do want change,
let's see what we can arrange
now, I insist that I hold that door
please sir, can I fuckin, have some more?
[Chorus | sung, big and melodic, the horns and strings take the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, double-time, two syllables a beat, sharp and cutting]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic,
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift
What about if we taxed the rich?
what the fuck you think this is, bitch
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Chorus | sung, big and melodic, the horns and strings take the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines at full speed, the breaks at their heaviest, horns answering each line]
[gruff MC]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[cold MC]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both MCs together]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[cold MC]
you see as it turns out, there is very little clout,
in having the manager or any of the see sweet about
[gruff MC]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[cold MC]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gruff MC]
yet I don't begrudge you,
we were on the same side all along
[cold MC]
well we don't have long
and by the time it hits, we'll be gone
[Chorus | sung, the last time, the lone french horn returns over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r55 thriller atom

Style:

```
174 BPM drum and bass: cold skippy breaks, tight snares, a low Reese that creeps. Scored like a thriller: a ticking pizzicato ostinato, muted piano notes, one cold low string. The pizzicato ticks sixteenths against the break like a clock and the piano answers the snare: timekeeping inside the drums, never atmosphere over them. Opens on the ticking pizzicato alone, no drums, two lines, close and fast. Under line three the ticking speeds up and the low string slides up into the drop. Break and Reese loudest, no gaps in the drums, everything on one 174 grid. Cold, tight, narrow, clinical. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline. They ride the break in eighth notes with sixteenth bursts, two syllables a beat, consonants like percussion, no pause at a line's end, never a bar left empty.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, slow flow, half-time flow, steady rap pace, measured delivery, sparse flow, pausing between lines, empty bars, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, shrieking violins, string shrieks, prepared piano, bowed metal, sul ponticello, low brass hits, taiko, war drums, heroic brass, brass ostinato, french horn theme, soaring strings, orchestral tambourine, sleigh bells, lush strings, orchestral bed, ambient, warm, pretty, major key, jazzy
```

Lyrics:

```lyrics
[Verse 1 | a ticking pizzicato ostinato alone, no drums at all | gruff MC, close and quiet but already at full speed]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | the ticking speeding up and a low string sliding upward into the drop]
now, let me explain, how I'm just poor
[Drop | the cold skippy break and the creeping Reese come in, the pizzicato ticking on through]
[gruff MC, double-time from here to the end, two syllables a beat, straight into the next line with no pause]
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
but I bet, that you paid for your wheels on tick
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
I can't live like this forever
I might be insane but I do want change,
let's see what we can arrange
now, I insist that I hold that door
please sir, can I fuckin, have some more?
[Chorus | sung, big and melodic, the pizzicato and the strings take the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, double-time, two syllables a beat, sharp and cutting]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic,
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift
What about if we taxed the rich?
what the fuck you think this is, bitch
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Chorus | sung, big and melodic, the pizzicato and the strings take the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines at full speed, the breaks at their heaviest, the piano answering every snare]
[gruff MC]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[cold MC]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both MCs together]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[cold MC]
you see as it turns out, there is very little clout,
in having the manager or any of the see sweet about
[gruff MC]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[cold MC]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gruff MC]
yet I don't begrudge you,
we were on the same side all along
[cold MC]
well we don't have long
and by the time it hits, we'll be gone
[Chorus | sung, the last time, the ticking pizzicato returns under the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```
