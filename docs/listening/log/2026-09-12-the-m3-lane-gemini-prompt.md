You are listening to one take from Suno so that the people who made it can decide what to change
next. They cannot hear it the way you can describe it, and they are not trained in sound-design
vocabulary — that gap is the whole reason you are here.

**You will be given the prompt that produced this audio.** Your job is not a review. It is a
**diff**: what was asked for, what actually arrived, and the smallest change that closes the gap.

## Rules you must not break

- **Describe only what you hear.** Where you are unsure, write `unsure` and say what would settle
  it. A confident wrong answer costs a 20-credit round and sends the next one the wrong way.
- **Never say it matches because the prompt says so.** You have the prompt in front of you, which
  makes it very easy to hallucinate the thing you were told to expect. If you cannot hear a clause,
  the honest answer is `absent` — even when the prompt is emphatic about it.
- **You are hearing a degraded copy**: downsampled and mixed to a single channel. So:
  - say nothing about stereo width, panning or imaging;
  - treat fine top-end detail, harshness and "polish" as low-confidence, and defer to the measured
    facts you are given;
  - tempo, loudness and brightness numbers are measured locally and are more reliable than your ear.
- **Do not use artist or band names** in anything you propose. Suno strips them. Describe the sound.
- Timestamps as `M:SS`.

## The Suno vocabulary you are answering in

The prompt boxes are the only interface. Proposals must be text that can go in a box. What the
boxes are, and what is known to move them:

- **Style box** — genre, tempo and key, then the instruments, then the voices, then the mix, then
  the arrangement in order. **Hard limit 1,000 characters; it truncates silently**, so anything you
  add must come with something to cut.
- **The genre tag casts the singer.** It carries a whole performer — accent, age, class — as one
  package. If the voice is wrong, the genre tag is the first suspect, not the vocal clause.
- **A maxed box outvotes its own vocal clauses.** A style box that has grown is the usual cause of
  casting regressing; the arrangement clause is the first thing to trim.
- **Exclude box** — a list of things to keep out, written as plain positive keywords (`sung chorus`,
  not `no sung chorus`). It is **global**: it cannot protect one section from another's sound.
  A **stale ban** is one of the most common faults — something the prompt asks for that an old
  exclude term is quietly forbidding.
- **Delivery words carry more than attitude words.** `barked`, `half-shouted`, `muttered`,
  `strained`, `hollered` change a performance; `angry` and `aggressive` mostly do not.
- **Naming drum mechanics beats naming a sub-genre** — `chopped breakbeat, amen rolls tearing
  across a bar` lands where `liquid dnb` does not.
- **Negation describes the thing you ban.** Writing `never sung` in the Style box puts the idea of
  singing in front of the model; prefer a positive description of the wanted delivery, and put the
  ban in the Exclude box.
- **One variable per round.** Style, Exclude and Lyrics change together as one atom, or not at all.
  A proposal that moves three unrelated things teaches nobody anything.

## Answer under exactly these headings

### 1. What arrived
Three or four sentences, in plain producer language: what this track is, its mood, its energy, how
it is put together. Written for someone who has not heard it and has to decide whether to keep it.

### 2. The take in Suno terms
Rewrite what you actually heard **as if it were a Style box** — genre, tempo feel, instruments,
voices, mix, arrangement — under 1,000 characters. This is the single most useful thing you produce:
it is the *actual* state in the same language as the *desired* state. Do not copy the input prompt.
Write what the audio would have needed as a prompt.

### 3. Clause-by-clause diff
A table. One row per distinct clause of the Style box you were given — the genre and tempo, each
instrument, each voice, the mix language, each arrangement step. Judge each one:

| Clause as written | Verdict | What you actually hear | Confidence |

`Verdict` is exactly one of: **landed** · **partly** · **absent** · **opposite**.
`Confidence` is **high** · **medium** · **low**. Be harsh: `partly` is not a kindness, it is
information. Anything you cannot assess through a mono, downsampled copy is `unsure`, not a guess.

### 4. Did anything banned get in?
Go through the Exclude list and name anything you can actually hear that it forbids, with a
timestamp. Then the reverse, which matters more: **is any exclude term fighting the Style box?**
Name any banned thing the Style box is asking for. That is a stale ban and it is a bug.

### 5. The words
Only if lyrics were supplied. Are the words intelligible? Name any line you cannot make out, and
any line in the lyrics you **cannot hear at all** — a dropped line is silent and nobody notices it
by ear. Is the delivery spoken, shouted, sung? Does each named voice sound like a different person?

### 6. The gap that matters most
One paragraph. Of everything above, the single biggest distance between what was asked for and what
arrived — and your read on **why**: which clause, which box, which interaction. Cause, not wording.

### 7. The next single edit
Two proposals, no more, each as **exact box text ready to paste**, each changing **one** thing:

- **Proposal A — the conservative one.** The smallest edit that addresses §6. Say what to cut if it
  would push the Style box over 1,000 characters.
- **Proposal B — the category change.** If the same idea has now failed in several different
  wordings, the idea is wrong rather than the sentence. Propose a different *category* of answer.

For each: the exact text, what it changes, what you expect to hear if it works, and — 🔑 — **what
you would expect to hear if it fails**, so the next round can be judged rather than admired.

---

MEASURED FACTS — measured locally from the full-quality capture, not from the copy you
are hearing. Do not contradict these, and prefer them to your own ear where they overlap:

- Duration: 215.8 seconds (3:35.8)
- Integrated loudness: -14.0 LUFS
- True peak: -0.3 dBTP
- Loudness range: 10.8 LU
- Spectral centroid (brightness): 3,570 Hz

🔴 ONE MEASUREMENT IS IN DISPUTE AND YOUR EAR IS THE TIE-BREAKER. The Style box below asks for
174 BPM. Two local detectors put this take at 117 BPM, at only `fair` confidence. 117 is not 174
nor a half or double of it (87 or 348), so one of three things is true: the take is not at the
tempo we asked for; or the detectors locked onto the "steady steppers groove" pulse rather than
the breakbeat; or they are simply wrong. Say which you hear, give the count you feel, and say how
sure you are. Treat this as the extra question, on top of the headings.

---

# THE PROMPT THAT PRODUCED THIS AUDIO

This is a take called "The M3 Lane", generated in Suno on the account that made it. The three
boxes below are exactly what went in. Diff the audio against them.

## Style box (as displayed on the song page — 1,186 characters)

```
Dark UK drum and bass, neurofunk, 174 BPM in a minor key with a steady steppers groove; male 1960s British mod R&B hollers, first gravelly and weathered, second higher and plummy, never sung, bone-dry against reverb-drenched ballad space, A low palm-muted guitar figure repeats beneath every vocal, joined by synthesizer drones and distant Gregorian chant backing; bagpipe tones shadow the minor harmony, First verse begins over a solitary detuned synth texture, then dry chopped breakbeats and amen rolls enter; drops hit with full-weight drums, Reese sub, screaming wavetable lead, tambourine on every beat, and slow wide chiming Britpop guitar walls at half speed, all fused rather than remixed, Verse two flips colder drums and sharper hats while the guitar figure remains alone beneath the voice; the second drop grows heavier, more distorted, with longer amen tears, thicker guitars, and higher lead, Bridge strips back to intimate shared-room vocals, sparse riff, chant haze, and restrained steppers pulse, Keep hard English consonants, throaty unpolished attack, clean BBC diction, flat delivery, no vibrato, and no instrumental vocal gaps where lyrics specify continuous speech
```

## Exclude box (82 terms)

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, clean sung melody, autotune, harmonies, grime MC, UK drill, road rap, trap, hip hop, young MC, American accent, American vocal, US rap, transatlantic, southern drawl, ragga   MC, toasting, Jamaican accent, dancehall vocal, soprano, operatic vocals, vibrato, angelic voices, sustained vocal notes, female vocal, children's choir, choral harmony, orchestral strings, violins, cello, string section, piano, glockenspiel, brass band, marching band, oompah, dixieland, guitar solo, lead guitar, shredding, acoustic guitar, wah, mashup, bootleg, remix, rock remix, nu metal, rap rock, rapcore, grunge, punk, epic   trailer music, reggae, dub, ska, music hall, vaudeville, pantomime, ragtime, honkytonk, liquid dnb, jump up, pop, lofi, jaunty, playful, whimsical, bouncy, comedic, novelty, parody, uplifting, major key, double time, tempo change, slow tempo
```

## Lyrics box (with its section cues — the bracketed lines are directions, not sung words)

```
[Intro — 8 bars | one long low detuned synth note, completely alone, held and slowly filtering open | a texture, not a tune, no melody | distant city hum far underneath | no drums, no bass, no guitar]
[Verse 1 | gravelly ranting voice, flat and unbothered, never selling a line | the low synth note holds underneath | no drums and no bass for the first half of this verse, then a dry chopped breakbeat comes in under the vocal and runs to the drop | amen rolls tearing across every fourth bar | the words never stop, no instrumental passage in this verse]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
but I bet, that you paid for your wheels on tick
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
[whispering voice loosing hope | no music | acapella]
I can't live like this forever
[shouting | music again]
I might be insane but I do want change,
let's see what we can arrange
now, I insist that I hold that door
[louder more angry shouting]
please sir, can I fuckin, have some more?
[Drop — instrumental, 8 bars, no vocals | the kit hits full weight and the sub bass drops for the first time | amen rolls tearing across every fourth bar | the palm-muted riff opens out into a wall of chiming Britpop guitars, strumming slow and wide at half the speed of the kit, tambourine on every beat | the wavetable lead tears in over the top]
[Beat Transition]
[Verse 2 | well-spoken posh voice, a completely different man, dry and unbothered, never selling a line | full-weight drum and bass carries straight on, drums flip, colder synths, sharper hats | amen rolls tearing across every fourth bar | the guitar wall is gone, only the same palm-muted riff returns underneath, unchanged | nothing else playing at all]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic,
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift
[whispering voice loosing hope | no music | acapella]
What about if we taxed the rich?
[shouting | music again]
what the fuck you think this is, bitch
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Drop — instrumental, 8 bars, no vocals | everything heavier and more distorted than the first drop — neuro bass growling underneath, the amen rolls harder and longer, the lead screaming higher, the guitar wall thicker and wider than before]
[Beat Transition]
[Bridge | the turn | drums strip right back, intimate | the two men trade, both close and dry in the same cold room now | the guitar riff sparser and quieter here, still one repeating figure, never a tune]
[gravelly ranting voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[well-spoken posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men together, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[well-spoken posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly ranting voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[well-spoken posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly ranting voice]
yet I don't begrudge you,
it's us and them now
[well-spoken posh voice]
well we don't have long
and by the time it hits, we'll be gone
[end]
```
