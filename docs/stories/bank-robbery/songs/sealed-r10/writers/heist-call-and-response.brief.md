You are writing Suno v6 prompts for a songwriter called Jack. Research the internet first (search and read pages) and base your work on what you find.

## Jack's request, word for word

okay so keep the opera stuff, but remove the opera singing and add back the laid back gangster voice, also intertwine the psychedelic funk with the classical stuff, do not use any old prompt or the suno skills/repo just research the internet and use a clean room approach thanks

Jack's standing rules (his own words, always true): no screaming; no fast or double-time rap;
no Covers or remixes — every take is a fresh Create.

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
They say, ya can't make money from a tree
let's see, each day, make hay, not free, aay
work and get paid though, earning that dough
but where does it go? nobody knows!

means of production means a reduction
standards bleeding, land-lords needing
quantative easing, grandma FREEEEEEEZING!
stimulus checks are next. Get wrecked!

rent seeking?... I'm just about eating
sorry, did I interrupt your meeting?
remember kids, the Fed is not your friend!
it prints all the dollars that the government spends

this fiat system is insistent
on debts existence, sooooo
don't be hating on the credit rating
or have resistance to the facts I'm stating

Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burrrrrrrrring, now now what's occurrrrrrrring?

Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burrrrrrrrring, now now what's occurrrrrrrring?

Stacks and stacks of elastic cash
distracted by a dispraxic flash,
mob, angry at their shitty little job
the right and the left both witness the theft

blaming each other is a sick little cover
institutional, dilutional, the usual
distraction IS the attraction
the intention is tension between the factions

divide and conquer, just look at the hand
It's not ya standard, propaganda, worth a couple grand-ahh
it is, state, level, manipulation
it is the devil, with a radio station

stack up the vaults like a wheelbarrow
risk of default is really rather narrow
Biggie said waaaay back in ninety seven
don't get high off your own supply

Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burrrrrrrrring, now now what's occurrrrrrrring?

Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burrrrrrrrring, now now what's occurrrrrrrring?

You know the real star is Pablo Escobar,
who has elastic bands not plastic hands,
stacking up the cash by the grands
standard plans are for the working man

and this right here is a next level scam
ill gotten gains, no need to explain
"bail" and "out", will never mean the same
own the printer and you don't fear winter

crime is asset inflation, passive creation;
of a wealth gap that drives the situation
working people get paid in money, so it's not very funny
when you print more and expect them not to worry

hungry people, feed a revolution,
then it's retribution, perhaps some execution
it's time to give, not just to take
but for heaven’s sake, don't just eat cake
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**heist-call-and-response** — Make it a slinky 94 BPM psychedelic funk heist cue, scored like a classical thriller: tremolo strings, timpani hits, harp glissandos and a brass section answering a wah-wah guitar. The voice is a cool, confident gangster lead with a slow drawl, plus a laid-back male crew who answer him in a low murmur on 'Robbery, robbery!' and 'Debasement!'. This is call and response, never shouting. Ask for the music as a scene description in prose (a midnight bank job, the orchestra and the funk band playing the same groove), followed by a short tag line with the BPM and the voice. In the lyrics, tag the choruses [Chorus: call and response, low crew answers] and the last verse [Verse: strings drop out, bass and voice only]. Exclude operatic vocals, choir, screaming and double-time rap.

Other writers are doing the other experiments (g-funk-overture, smoky-og-soul-orchestra, baroque-boom-bap-mafioso, opera-in-acts, sing-song-west-coast-lilt, minimal-six-tags-low-variety, stoned-string-quartet). Make yours sound like itself, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the voices come out the same. Problems:
- shares wording with other prompts in this round: Style boxes: rapper with a

Your previous draft:
```json
{
  "name": "heist-call-and-response",
  "style": "A midnight bank job scored like a classical thriller. A slinky psychedelic funk band and a chamber orchestra lock into one shared groove: rubbery bass and dry pocket drums under tremolo strings, timpani hits on the turnarounds, harp glissandos sliding between bars, and a brass section answering every wah-wah guitar lick. Phaser haze, vault-door tension, cool and unhurried. The lead is a cool, confident gangster rapper with a slow drawl, sitting relaxed behind the beat; a laid-back male crew murmurs low answers in the hooks.\n94 BPM, psychedelic funk heist cue, laid-back gangster drawl lead, low murmured male crew call and response",
  "exclude": "operatic vocals, opera singing, choir, screaming, shouting, double-time rap, fast rap, belting, gang chants",
  "lyrics": "[Intro: tremolo strings, wah-wah guitar, timpani hit]\n\n[Verse 1: slow drawl, relaxed behind the beat]\nThey say, ya can't make money from a tree\nlet's see, each day, make hay, not free, aay\nwork and get paid though, earning that dough\nbut where does it go? nobody knows!\n\nmeans of production means a reduction\nstandards bleeding, land-lords needing\nquantative easing, grandma FREEEEEEEZING!\nstimulus checks are next. Get wrecked!\n\nrent seeking?... I'm just about eating\nsorry, did I interrupt your meeting?\nremember kids, the Fed is not your friend!\nit prints all the dollars that the government spends\n\nthis fiat system is insistent\non debts existence, sooooo\ndon't be hating on the credit rating\nor have resistance to the facts I'm stating\n\n[Chorus: call and response, low crew answers]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus: call and response, low crew answers]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 2: slow drawl, brass answers wah guitar]\nStacks and stacks of elastic cash\ndistracted by a dispraxic flash,\nmob, angry at their shitty little job\nthe right and the left both witness the theft\n\nblaming each other is a sick little cover\ninstitutional, dilutional, the usual\ndistraction IS the attraction\nthe intention is tension between the factions\n\ndivide and conquer, just look at the hand\nIt's not ya standard, propaganda, worth a couple grand-ahh\nit is, state, level, manipulation\nit is the devil, with a radio station\n\nstack up the vaults like a wheelbarrow\nrisk of default is really rather narrow\nBiggie said waaaay back in ninety seven\ndon't get high off your own supply\n\n[Chorus: call and response, low crew answers]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Chorus: call and response, low crew answers]\nRobbery, robbery!\nCall the police, it's a robbery!\nDebasement! Debasement! It happened in da basement!\nPrinter is burrrrrrrrring, now now what's occurrrrrrrring?\n\n[Verse 3: slow drawl, harp glissando, timpani hits]\nYou know the real star is Pablo Escobar,\nwho has elastic bands not plastic hands,\nstacking up the cash by the grands\nstandard plans are for the working man\n\nand this right here is a next level scam\nill gotten gains, no need to explain\n\"bail\" and \"out\", will never mean the same\nown the printer and you don't fear winter\n\ncrime is asset inflation, passive creation;\nof a wealth gap that drives the situation\nworking people get paid in money, so it's not very funny\nwhen you print more and expect them not to worry\n\n[Verse: strings drop out, bass and voice only]\nhungry people, feed a revolution,\nthen it's retribution, perhaps some execution\nit's time to give, not just to take\nbut for heaven’s sake, don't just eat cake\n\n[Outro: instrumental, tremolo strings return, final timpani hit, harp glissando, fade]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 40,
  "styleInfluence": 75,
  "vocalGender": "male",
  "durationSec": 295,
  "maxMode": true
}
```

Answer with a short note on what shaped it (with source URLs), then ONE fenced ```json block: a
single object with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "heist-call-and-response".