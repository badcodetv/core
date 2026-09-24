## v6.46 Round r54 — six lanes, varied on BOTH axes (2026-09-21)

**Brief, Jack 2026-09-21, on the r53 optimised pair:** *"the optimised ones made the timing weird,
the rap should be fast and to the beat, the beginning was too slow before the drop, it should be an
exciting build up until then and the blend of orchestral elements with the drum and bass grime voice
mix has not been done well enough, they should all be layered and compliment each other… the
orchestral elements have been all the same, as well as the drum and bass, so make massively varied
versions of all of them."* Reference to build on, again:
[1127446d](https://suno.com/song/1127446d-abe8-4079-9bbe-6b281e12aa74).

### The diagnosis — why the last three rounds sounded like one record

r50–r53 varied **one** axis. Every lane opened on *"a lone sad piano and a solo violin"*, every lane
said *"174 BPM UK drum and bass at full weight, chopped amen breaks"*, and only the guest instrument
moved (guqin, steelpan, smallpipes, organ…). So the orchestral **opening** and the **drums** were
literally the same text in every lane — which is exactly the complaint. r54 varies **both axes at
once**: a different d&b subgenre *and* a different instrument family *and* a different job for that
family, per lane.

### The four fixes, and where each one lands

| Complaint | Fix | Where it goes |
|---|---|---|
| **"the timing went weird"** | an explicit grid lock in every Style box — *one 174 grid, every rapped line square on the beat* — plus `drifting tempo, tempo change, rubato, rapping behind the beat, off-grid vocal` in every Exclude | Style + Exclude. Practitioner consensus is that a constant-tempo clause measurably reduces v6 drift ([MixMasterAI](https://www.mixmasterai.co/suno-prompts/fix/wrong-tempo), [GenX Notes](https://blog.genxnotes.com/en/fix-suno-bpm-tempo-drift/)) |
| **"the rap should be fast and to the beat"** | the r43 cast sentence kept verbatim, and the rapid-fire cue restated **at the drop** (`every line landing square on the beat`) | Style + the lyric cue |
| **"too slow before the drop — make it an exciting build up"** | r53's opening cue literally said **`slow and emotional`**; it now reads `urgent and already tense`, the opening is **two lines not three**, and line three gets a **build device** that differs per lane (timpani roll, filter sweep, gong + doubling hats, flutter-tongue riser, climbing strings, racing brushes) | lyric cue + Style |
| **"the orchestral and the d&b aren't layered / don't complement"** | every lane states the orchestra's **rhythmic job** against the break — doubling the kick, doubling the Reese an octave up, doubling the hi-hats, answering the MC in the bar gap, playing the drums' own pattern — instead of describing a texture | Style, the `job` clause |

🔑 **The build is written as `[Verse 1 continues — no pause…]`, never `[Build]`.** A `[Build]` tag
reliably inserts eight **instrumental** bars with no vocal, and three explicit denials did not stop
it — the noun wins (`docs/suno-gpt/files/suno-tag-mechanics.md`). A `Verse` tag is just as
structural, so Suno re-decides the arrangement, but a verse is the sung part, so there is nothing to
fill with music.

### The six lanes

| Lane | Subgenre | Family | The orchestra's job | Build device | Production |
|---|---|---|---|---|---|
| `brass` | jungle / amen | trombone, tuba, timpani | stabs in the break's holes, timpani doubles every kick | timpani roll + snare roll to 16ths | 1994 white label, tape-hot |
| `cello` | techstep | solo cello, double bass | plays the Reese riff an octave up, note for note | bowing hardens + filter opens | surgical, cold, airless |
| `bells` | rollers | tubular bells, glockenspiel, gongs | bells as a clock, glockenspiel doubles the hi-hats | gong swell + hats doubling | glossy, reverberant, club-loud |
| `woodwind` | dark liquid | bass clarinet, flute | counter-line above the sub; flute answers each rapped line | flutter-tongue + soft riser | warm, close, tape, night-bus |
| `spiccato` | darkstep | dry spiccato strings | 16ths locked to the break, playing the drums' pattern back | strings climb + distorted riser | dry, brutal, nearly mono |
| `noir` | jazzstep | upright bass, muted trumpet | bass walks under the sub; trumpet answers between bars | brushes race + bass doubles up | smoky, valve, room, hiss |

### Settings

v6 · Style Influence **80** · Variety **Off** · Max Mode off · Vocal Gender **Male** · Personalize
off · no Voice · **Duration 195 s** · workspace `camping-Jack` · **weirdness 30 and 60**, a pair per
lane. 12 Creates, 24 takes.

### BOLD check

Longest shared run between any two Style boxes: **232 characters (23%)** — and it is **only the
r43 cast sentence**, which the rules explicitly allow to be shared. No shared production language,
no shared opening, no shared drum description. (r52's lanes shared ~640 characters including the
opening, the balance clause and the unity clause.)


### r54 brass atom

Style:

```
Jungle, 174 BPM, minor key, chopped amen breaks, grime over the top. Opens with no drums: one tolling low piano note and a lone trombone, two lines, tense from bar one. Under line three a timpani roll speeds up and a snare roll doubles to sixteenths: a build, not a ballad. Then the drop, the amen tearing in with a huge rolling sub, brass landing on the same beat. Trombone and tuba stab in the holes the break leaves, timpani doubling every kick: brass as percussion, written into the drums, not laid over them. Drums and sub loudest throughout, break never stopping, all of it on one 174 grid, every rapped line square on the beat. A big sung chorus hook three times, the only sung thing. Dubplate-loud, overdriven, tape-hot, like a 1994 white label. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, solo cello, double bass, sawing strings, string quartet, chamber strings, tubular bells, glockenspiel, celesta, gongs, chimes, music box, bass clarinet, flute, flutter-tongue flute, oboe, woodwinds, spiccato strings, staccato string ostinato, violin section, string stabs, muted trumpet, upright bass, walking bass, brushed drums, jazz, swing, techstep, neurofunk, rollers, dancefloor drum and bass, liquid drum and bass, liquid funk, darkstep, amen assault, jazzstep, jazzy jungle, orchestral film score, epic trailer music, symphony orchestra, lush strings, glossy production, radio pop
```

Lyrics:

```lyrics
[Verse 1 | one tolling low piano note and a lone trombone, no drums at all | gruff MC, quiet and close, urgent and already tense]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | a timpani roll speeding up and a snare roll doubling underneath, the tension climbing into the drop]
now, let me explain, how I'm just poor
[Drop | the amen and the sub tear in at full weight and the brass stabs land on the same beat]
[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]
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
[Verse 2 | straight in, no break, the beat bigger | cold MC, rapid-fire, sharp and cutting]
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
[Bridge | the two MCs trade lines, the breaks at their heaviest, brass stabs answering every line]
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
[Chorus | sung, the last time, the lone trombone returns over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r54 cello atom

Style:

```
Techstep, 174 BPM, minor key, cold and mechanical, grime over the top. Opens with no drums: a solo cello and a double bass sawing one dark riff, two lines close over them. Under line three the bowing hardens and a low filter opens, hauling the track into the drop: rising, never slow. Then the drop, surgical metallic breaks, machine hats, a morphing Reese bass. The cello plays that Reese riff an octave up, note for note, so bass and strings are one instrument doubling itself, and the double bass answers each MC with two plucked notes. Break and Reese loudest, unbroken to the end, one rigid 174 grid, the rap exactly on the beat. A big sung chorus hook three times, the only sung thing. Surgical, wide and cold, airless, every transient sharpened. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, low brass, trombone, tuba, timpani, brass stabs, fanfare, marching band, tubular bells, glockenspiel, celesta, gongs, chimes, music box, bass clarinet, flute, flutter-tongue flute, oboe, woodwinds, spiccato strings, staccato string ostinato, violin section, string stabs, muted trumpet, upright bass, walking bass, brushed drums, jazz, swing, jungle, amen jungle, ragga jungle, rollers, dancefloor drum and bass, liquid drum and bass, liquid funk, darkstep, amen assault, jazzstep, jazzy jungle, orchestral film score, epic trailer music, symphony orchestra, lush strings, warm, mellow, organic, live band
```

Lyrics:

```lyrics
[Verse 1 | a solo cello and a double bass sawing one dark riff, no drums at all | gruff MC, quiet and close, urgent and already tense]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | the bowing hardening and a low filter opening underneath, hauling the track up into the drop]
now, let me explain, how I'm just poor
[Drop | surgical breaks and a morphing Reese slam in, the cello doubling the bass riff an octave up]
[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]
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
[Chorus | sung, big and melodic, the cello and the Reese play the hook together under the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, rapid-fire, sharp and cutting]
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
[Chorus | sung, big and melodic, the cello and the Reese play the hook together under the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines, the breaks at their heaviest, the double bass plucking between the lines]
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
[Chorus | sung, the last time, the solo cello returns alone over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r54 bells atom

Style:

```
Rolling dancefloor drum and bass, 174 BPM, minor key, grime over the top. Opens with no drums: tubular bells tolling, a glockenspiel picking a cold figure, two lines close. Under line three a gong swells and the hats come in alone, doubling and doubling: a fast build, not a slow intro. Then the drop, a relentless rolling break and a deep round sub that never lets go. The bells ring on the first beat of every eighth bar like a clock, the glockenspiel doubles the hi-hats note for note, a gong marks each turn: metal as percussion, cut into the break. Drums and sub own the mix, no gaps, one steady 174 grid, the rapping dead on the beat. A big sung chorus hook three times, the only sung thing. Huge, glossy, reverberant, long metal tails, loud for a club rig. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, low brass, trombone, tuba, timpani, brass stabs, fanfare, marching band, solo cello, double bass, sawing strings, string quartet, chamber strings, bass clarinet, flute, flutter-tongue flute, oboe, woodwinds, spiccato strings, staccato string ostinato, violin section, string stabs, muted trumpet, upright bass, walking bass, brushed drums, jazz, swing, jungle, amen jungle, ragga jungle, techstep, neurofunk, liquid drum and bass, liquid funk, darkstep, amen assault, jazzstep, jazzy jungle, orchestral film score, epic trailer music, symphony orchestra, lush strings, lo-fi, tape hiss, muddy mix
```

Lyrics:

```lyrics
[Verse 1 | tubular bells tolling and a glockenspiel over them, no drums at all | gruff MC, quiet and close, urgent and already tense]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | a gong swelling and the hats arriving alone, doubling and doubling into the drop]
now, let me explain, how I'm just poor
[Drop | the rolling break and the deep sub slam in, a bell ringing across the first bar]
[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]
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
[Chorus | sung, big and melodic, the bells ring out through the chorus over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, rapid-fire, sharp and cutting]
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
[Chorus | sung, big and melodic, the bells ring out through the chorus over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines, the breaks at their heaviest, a gong on every turn]
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
[Chorus | sung, the last time, the tubular bells return alone over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r54 woodwind atom

Style:

```
Dark liquid drum and bass, 174 BPM, minor key, grime over the top. Opens with no drums: a bass clarinet low and slow, a flute breathing above it, two lines close. Under line three the flute flutter-tongues and a soft riser climbs, the room tightening bar by bar into the drop. Then the drop, warm rolling breaks with a deep sub beneath them, smooth but heavy. The bass clarinet runs a counter-line an octave above the sub, note for note, and the flute answers each rapped line in the gap at the bar's end: a third voice trading with the MCs, never a pad. Break and sub loudest, no holes, a constant 174 grid, every line landing on the beat. A big sung chorus hook three times, the only sung thing. Warm, deep and close, soft tape saturation, night-bus melancholy. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, low brass, trombone, tuba, timpani, brass stabs, fanfare, marching band, solo cello, double bass, sawing strings, string quartet, chamber strings, tubular bells, glockenspiel, celesta, gongs, chimes, music box, spiccato strings, staccato string ostinato, violin section, string stabs, muted trumpet, upright bass, walking bass, brushed drums, jazz, swing, jungle, amen jungle, ragga jungle, techstep, neurofunk, rollers, dancefloor drum and bass, darkstep, amen assault, jazzstep, jazzy jungle, orchestral film score, epic trailer music, symphony orchestra, lush strings, harsh, industrial, distorted
```

Lyrics:

```lyrics
[Verse 1 | a bass clarinet low and slow with a flute breathing above it, no drums at all | gruff MC, quiet and close, urgent and already tense]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | the flute flutter-tonguing and a soft riser climbing underneath, tightening into the drop]
now, let me explain, how I'm just poor
[Drop | warm rolling breaks and a deep sub arrive, the bass clarinet doubling the sub an octave up]
[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]
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
[Chorus | sung, big and melodic, the flute carries the hook with the break underneath]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, rapid-fire, sharp and cutting]
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
[Chorus | sung, big and melodic, the flute carries the hook with the break underneath]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines, the breaks at their heaviest, the flute answering each line]
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
[Chorus | sung, the last time, the bass clarinet returns under the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r54 spiccato atom

Style:

```
Darkstep, 174 BPM, minor key, fast and violent, grime over the top. Opens with no drums: a dry spiccato string figure bouncing in sixteenths, no sustain, two lines spat over it. Under line three the strings climb a step at a time and a distorted riser rips up beneath: pure tension, over fast. Then the drop, an amen assault, breaks tumbling and tearing, a filthy distorted sub. That figure never stops and never swells: short dry sixteenths locked to the break, playing the drums' own pattern back at them, a rhythm part inside the kit. Drums and sub loudest in the room, breaks never stopping, one 174 grid, the rap flat on the beat. A big sung chorus hook three times, the only sung thing. Dry, brutal, nearly mono, no reverb anywhere, clipped at the edges. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, low brass, trombone, tuba, timpani, brass stabs, fanfare, marching band, solo cello, double bass, sawing strings, string quartet, chamber strings, tubular bells, glockenspiel, celesta, gongs, chimes, music box, bass clarinet, flute, flutter-tongue flute, oboe, woodwinds, muted trumpet, upright bass, walking bass, brushed drums, jazz, swing, jungle, amen jungle, ragga jungle, techstep, neurofunk, rollers, dancefloor drum and bass, liquid drum and bass, liquid funk, jazzstep, jazzy jungle, orchestral film score, epic trailer music, symphony orchestra, lush strings, legato strings, sustained strings, ambient, reverb-drenched
```

Lyrics:

```lyrics
[Verse 1 | a dry spiccato string figure bouncing in sixteenths, no drums at all | gruff MC, quiet and close, urgent and already tense]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | the strings climbing a step at a time and a distorted riser ripping underneath]
now, let me explain, how I'm just poor
[Drop | the amen assault and the distorted sub tear in, the strings locking to the break]
[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]
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
[Chorus | sung, big and melodic, the strings hammer through the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, rapid-fire, sharp and cutting]
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
[Chorus | sung, big and melodic, the strings hammer through the chorus with the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines, the breaks at their heaviest, the strings sawing under every line]
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
[Chorus | sung, the last time, the dry strings return alone over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```


### r54 noir atom

Style:

```
Jazzstep, 174 BPM, minor key, smoky and dangerous, grime over the top. Opens with no drums: an upright bass walking, a muted trumpet smearing above it, two lines tired and close. Under line three brushes race on a snare and the walking bass doubles its speed into the drop, a few bars only. Then the drop, chopped funk breaks and a fat round sub, swung but locked hard. The upright bass walks under the sub the whole way and the muted trumpet answers the MCs with one smeared phrase between their bars: players in the room with the break, not sampled over it. Break and sub loudest, drums never out, one hard 174 grid under the swing, every line on the beat. A big sung chorus hook three times, the only sung thing. Smoky, room-recorded, valve warmth, hiss left in. Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline.
```

Exclude styles:

```
American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female vocal, teenage voice, boyish voice, falsetto, choir, laid-back, chill, mumbled, lazy flow, steady rap pace, measured delivery, spoken word, rapping behind the beat, off-grid vocal, drifting tempo, tempo change, rubato, comedic, novelty, parody, low brass, trombone, tuba, timpani, brass stabs, fanfare, marching band, solo cello, double bass, sawing strings, string quartet, chamber strings, tubular bells, glockenspiel, celesta, gongs, chimes, music box, bass clarinet, flute, flutter-tongue flute, oboe, woodwinds, spiccato strings, staccato string ostinato, violin section, string stabs, jungle, amen jungle, ragga jungle, techstep, neurofunk, rollers, dancefloor drum and bass, liquid drum and bass, liquid funk, darkstep, amen assault, orchestral film score, epic trailer music, symphony orchestra, lush strings, digital, surgical, clinical
```

Lyrics:

```lyrics
[Verse 1 | an upright bass walking and a muted trumpet smearing above it, no drums at all | gruff MC, quiet and close, urgent and already tense]
Once again, and you catching my eye,
and you looking to the side in shame, but why
[Verse 1 continues — no pause, the same MC carrying straight on | brushes racing on a snare and the walking bass doubling its speed into the drop]
now, let me explain, how I'm just poor
[Drop | chopped funk breaks and a fat sub slam in, the upright bass walking on underneath]
[gruff MC, rapid-fire from here to the end, every line landing square on the beat, never slowing]
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
[Chorus | sung, big and melodic, the muted trumpet takes the chorus over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Verse 2 | straight in, no break, the beat bigger | cold MC, rapid-fire, sharp and cutting]
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
[Chorus | sung, big and melodic, the muted trumpet takes the chorus over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[Bridge | the two MCs trade lines, the breaks at their heaviest, the trumpet answering between the lines]
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
[Chorus | sung, the last time, the muted trumpet returns over the break]
I can't live like this forever
I can't live like this forever
I might be insane but I do want change
I can't live like this forever
[end]
```
