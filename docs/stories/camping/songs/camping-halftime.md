---
title: Camping (half-time) — the accepted direction, and the rounds off it
status: ACCEPTED s1/S7 take 1 (3:54). Iterating from here.
accepted_take: https://suno.com/song/1ac179f5-bc5c-42ec-9c66-96ef664a5c69  # "Camping S7 Dub, half-time delivery (s1)", 3:54
words_canon: ./camping.md  # §4 — the words, and only the words
scouting_set: ./camping-style.md  # where S7 came from
workspace: camping-duet
model: v5.5
mode: Create (Advanced) — NOTHING attached
---
# Camping — the half-time direction

**Kai, 2026-08-26: S7 take 1 is the one.** Dub soundsystem drum and bass, spoken vocal delivered
at half the speed of the beat. Fourteen cover rounds and a seven-way scouting set landed here.

**This sheet is the whole prompt.** Everything below is what produced the accepted take, verbatim
and complete — nothing to assemble, nothing to look up in another file. The rounds in §6 are
patches on it, one variable each.

| | |
|---|---|
| **The accepted take** | [S7 take 1](https://suno.com/song/1ac179f5-bc5c-42ec-9c66-96ef664a5c69), 3:54 |
| **The runner** | [`scripts/suno/halftime.mts`](../../../../scripts/suno/halftime.mts) |
| **Where takes land** | workspace `camping-duet`, titled `Camping HT <name> (<set>)` |
| **Where it came from** | [`camping-style.md`](./camping-style.md) — the scouting set, and the My Taste finding |
| **The words** | [`camping.md`](./camping.md) §4 is canon. §4 below must agree with it, and the runner checks |

---

## 1. My Taste

🔴 **Account-wide. Applies to every generation, cannot be turned off, belongs to no sheet, and is
invisible from the create form.** It was found holding the wrong song's profile through fourteen
Camping rounds ([`camping-style.md`](./camping-style.md) §1). `halftime.mts` backs the house
profile up before writing this, reads it back, and restores it after.

```
Vocals: indie rap-rock British male voices, rapped tight to the beat at full 174 — energetic, rhythmic, nu-metal attitude, aggressive rapped verses, melodic sung hook. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark industrial drum and bass at 174 BPM, minor key, mixed like a dub soundsystem. Sub bass first and loudest, everything else stripped back around it. Rusted metallic textures and factory noise in the gaps. Tape delay throwing the end of every vocal line across the bar, struck steel on the snare. Occasional clean high guitar flourishes trading call-and-response with a sparse dub piano, never a chord progression. A low brass section that arrives only at the drops — hard loud stabs on the downbeat, and silent the rest of the time. No other orchestral instrument anywhere on this record. Dry chopped breakbeats and chopped amen rolls that tear across a whole bar every few bars, loud and right at the front. No gap between vocal lines anywhere — the next line always comes straight in on the following bar — and no instrumental passage longer than two bars. The record never vamps and never waits.

Register: bleak, dystopian, angry and completely serious. Machine-cold and hopeless. Never jaunty, never bouncy, never feel-good, never ska. Whatever is funny lives in the words alone.

Subject: British class, money, work, and the people the economy left behind.
```

## 2. Style

**988/1000.** Rewritten three times on 2026-08-26. The **orchestral pass was wrong and is backed out**
— Kai: *"it doesn't work at all to try to make it an orchestral tune."* This is the accepted S7
box again, with exactly three changes and no orchestra anywhere.

**The Madness fix, without the orchestra.** Kai heard the accepted take as *"too like Madness"* —
2-tone, and therefore funny. Three causes, and **none of them was the exclude list**:

1. **`Dub soundsystem` as the genre anchor.** It pulls Jamaican, and the most famous British band
   in that lineage is exactly the one he named. **Demoted, not deleted:** the box now reads
   `Dark UK drum and bass, mixed like a dub soundsystem`. We buy the desk, not the whole cultural
   package — which is Kai's *"less overtly dub sounding"* with the dub foundation kept.
2. **The `chorus-pedal jangle` over the palm-muted riff.** That *is* the 2-tone guitar. Removed.
   The low palm-muted riff stays — it has been the thing Kai liked since round 0. `r12` puts the
   jangle back as the diagnostic, so we find out which of these two was really doing it.
3. **The register clause.** `Grim and bitter, played straight` → `Grim, bitter and serious,
   played straight, never jaunty`, with `2 tone`, `offbeat guitar`, `upstroke guitar` and
   `skank rhythm` added to the excludes. `dub` stays **lifted** — the foundation is wanted.

**The padding cut is kept, and was tightened again in h5.** The cues originally bought **32 bars**
of instrumental — 8 each for intro, both drops and outro, ≈44 seconds at 174 — plus two
`[Beat Transition]`s Suno could expand. Now **8 bars**, two each, the transitions folded into the
drop cues, and a no-gap clause in the style box, My Taste and all three vocal-section cues.

🔴 **It changed the length by nothing.** See §6 — neither this nor the duration target nor the
phrase rate moved the takes off ~4:00–4:40. The tighter cues are kept because the *shape* is
better (less dead air between verses, which is the thing Kai could actually hear), not because
they shorten anything.

🔴 **The amen clause was cut from the style box** to buy room for the no-gap clause. The roll is
still named in all four section cues, which is where it has always actually been won. **If the
fills go quiet, that is why** — put `Chopped amen rolls tear across a bar every four bars.` back
and take the 53 characters from somewhere else.

🔴 **Trimmed to 988, not left at the cap.** A maxed box outvotes its own vocal clauses (this
sheet's oldest rule). Cut from colour and from what the lyric cues already say — never the
casting, the `never a solo, never chords` guards, or the dub-desk clauses.

```
Dark industrial drum and bass, 174 BPM, minor key, mixed like a dub soundsystem — indie rap-rock vocal on top, rapped tight to the beat at full 174, nu-metal energy, aggressive rapped verses with a melodic sung hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. Four steps: a short clean high guitar lick; then the voice over occasional clean high guitar flourishes trading call-and-response with a sparse dub piano, never chords, tape delay throwing every line end across the bar, struck steel on the snare; then a dry chopped breakbeat, sub bass first, nothing else; then the drop, guitar out, a low brass section stabbing on every downbeat, kit at full weight, Reese sub and a distorted lead against it. Chopped amen rolls tear across a bar every four bars. Dystopian, grim and mechanical, never jaunty.
```

## 3. Exclude Styles

**931 characters.** `half-time` stays **lifted** — the one risky subtraction, normally banned
because it half-times the *drums*. The style box, My Taste and the verse-2 cue each say full 174
as the counterweight, and the accepted take proves it holds.

`dub` also stays lifted: Kai wants the dub foundation, and the narrower `2 tone` / `offbeat
guitar` / `upstroke guitar` / `skank rhythm` bans are the accurate way to kill the Madness read.
All the orchestral keywords are **banned again** after the h2 pass was backed out. Five low-value
bans were dropped to stay under the longest exclude fill this field has been proven to hold
(933) — each was already covered by a neighbour.

```
crooning, autotune, harmonies, grime MC, UK drill, road rap, trap, young MC, American accent, American vocal, southern drawl, ragga MC, Jamaican accent, soprano, operatic vocals, vibrato, sustained vocal notes, female vocal, choir, orchestral strings, violins, cello, string section, marching band, oompah, dixieland, guitar strumming, power chords, acoustic guitar, live rock band, reggae, ska, 2 tone, offbeat guitar, upstroke guitar, skank rhythm, music hall, vaudeville, pantomime, liquid dnb, jump up, feel good, feel-good, party, festival, anthemic, happy hardcore, bright synths, euphoric, pop, lo-fi, jaunty, playful, whimsical, bouncy, comedic, parody, uplifting, major key, double time, tempo change, slow tempo, long instrumental, extended intro, instrumental break, vamp, outro jam
```

## 4. Lyrics

**The words are canon and live in [`camping.md`](./camping.md) §4.** The bracket cues here are
this direction's own — half-time delivery, spoken rather than shouted — and this block is what
the runner loads. It compares the words in it against `camping.md` §4 on every run and refuses to
spend a credit if they have drifted apart, so editing timing in one file and generating from the
other cannot happen twice.

```lyrics
[Intro — 2 bars, high-register 80s rock guitar lick, straight to the beat]
[Verse 1 | gravelly rapped voice, tight to the beat | no drums for the first half, then the breakbeat]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
[whispered]
but I bet, that you paid for your wheels on tick!
[hard and slow]
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
[slower, flatter]
I can't live like this forever
[raised]
I might be insane but I do want change, 
[sarcastic, high pitched]
let's see what we can arrange!
now, I insist that I hold that door
[cracking, begging]
please sir, can I FUCKIN, have some more?
[Verse 2 | posh voice, a completely different man]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic, 
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift 
[mocking falsetto]
What about if we taxed the rich?
[angry]
what the fuck you think this is, BITCH!
[posh voice]
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Bridge | the two men trade, close and dry | drums stripped back]
[gravelly voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[pause | posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly voice]
yet I don't begrudge you,
it's us and them now
[pause | posh voice]
well we don't have long
[Outro — both voices]
and by the time it hits, we'll be gone
[end]
```

## 5. Sliders

| Control | Accepted | Note |
|---|---|---|
| Weirdness | **30** | the lowest in the scouting set |
| Style Influence | **70** | Kai, 2026-08-26 |
| Audio Influence | — | does not exist; nothing is attached |
| Duration | **240s** (4:00) | 🔴 **proven backwards** — see §6. Asking for 3:30 returned 4:16/4:39; asking for 4:00 returned 4:04/3:52 |

---

## 6. Rounds

One variable each, patched onto the baseline above. `npx tsx scripts/suno/halftime.mts plan`
prints the resolved boxes for any of them.

### h12 — 2026-08-26, drop the half-time spoken-word discipline. Baseline = h11, SI 75.

🔴 **The biggest pivot of the session.** Kai: *"a lot of them are veering into just, like, not
keeping to the beat — the words to the beat. Let's do a slightly more traditional drum and bass
indie-rap combo, kind of like Linkin Park."* This reverses the thing that has been fixed since
round 0: `never rapped, half the speed of the beat` was the entire identity of the accepted S7
take this whole sheet is built on. Flagging it as a pivot, not backing it out — Kai heard a real
problem (the half-time delivery drifting off the beat) and this is the direct fix.

| box | was | now |
|---|---|---|
| style | `spoken vocal on top, delivered at half the speed of the beat, one phrase every two bars, never rapped` | `indie rap-rock vocal on top, rapped tight to the beat at full 174, nu-metal energy, aggressive rapped verses with a melodic sung hook` |
| taste | `spoken British male voices delivered at half the speed of the beat — long vowels, dragging behind, one phrase every two bars, never ranted and never rapped, while the drums stay at full 174` | `indie rap-rock British male voices, rapped tight to the beat at full 174 — energetic, rhythmic, nu-metal attitude, aggressive rapped verses, melodic sung hook` |
| exclude | `singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, …, clean sung melody, …, hip hop, …` | all of those **lifted** — a rap-rock band with sung hooks (the whole nu-metal signature) was being banned by our own exclude list |

🔴 **`Linkin Park` was flagged by Suno itself as a bad word — a real-time warning, not a guess.**
Treated exactly like a Flow policy block: never retry the same wording, expand it into descriptive
style words instead. `Linkin Park in tone` → `aggressive rapped verses with a melodic sung hook`.
Named-artist references are now off the table for this sheet, the same rule already learned for
Google Flow prompts.
| exclude | `grime MC, UK drill, road rap, trap, young MC, American accent` | **kept banned** — steers toward US alt-rap-rock, away from UK grime/drill, and keeps the voices British |
| lyrics | `[Verse 1 \| gravelly spoken voice \| …]` → `[Verse 1 \| gravelly rapped voice, tight to the beat \| …]`; `[spoken hard and slow]` → `[hard and slow]`; `[raised, still spoken]` → `[raised]`; `[angry, still spoken]` → `[angry]` | every cue that hard-coded "spoken" now leaves the delivery to the (now rap) global instruction |

**Not touched:** the two-man casting (gravelly working-men's-club voice vs plummy BBC English),
the dark industrial dub foundation, the h11 clean-guitar/dub-piano call-and-response, and every
word line — this is a delivery change, not a words or casting change.

| id | W | SI | **actual** | verdict |
|---|---|---|---|---|
| `w16-w30` | 30 | 75 | — | — |
| `w17-w40` | 40 | 75 | — | — |
| `w18-w45` | 45 | 75 | — | — |

### h11 — 2026-08-26, clean guitar/dub piano call-and-response. Baseline = h10, SI 75.

Kai: *"less of the Steve Vai rock vibe, but still guitar licks in there — as a little flourish,
quite consistently. More of a style/taste thing than a lyrics thing. And a bit of dub piano — not
all the way through — an interplay, a call-and-response, between the clean guitar and the dub
piano."* Also: Kai edited `camping.md` himself, removing the `[shouting]` cue that was forcing
*"let's see what we can arrange!"* to be shouted. Checked — the half-time sheet's own cue there
(`[sarcastic, high pitched]`) never had that shout cue, and the word-only diff still matches, so
nothing needed mirroring.

**Kept out of the lyrics cues, on purpose** — Kai was explicit this is a style/taste-level
instruction, not a per-section cue, so §4 is untouched this round.

| was | now | box |
|---|---|---|
| `a short high-register 80s rock guitar lick` (intro step) | `a short clean high guitar lick` | style |
| `a high-register 80s rock lead guitar, Whitesnake and Steve Vai toned, melodic runs, never chords` | `occasional clean high guitar flourishes trading call-and-response with a sparse dub piano, never chords` | style, net −5 |
| My Taste: `One high-register 80s rock lead guitar, Whitesnake and Steve Vai toned, melodic runs, never a chord progression.` | `Occasional clean high guitar flourishes trading call-and-response with a sparse dub piano, never a chord progression.` | taste, +5 (within noise, taste has 350+ chars of headroom) |
| exclude: `piano` | *(lifted)* | exclude |

🔴 **Live tension flagged, not resolved:** `skank rhythm`, `2 tone`, `reggae` and `ska` all stay
**banned** — they were the specific fix for the "sounds like Madness" read in h3/h4, and dub piano
is culturally the same instrument playing that exact rhythm. If the piano comes back
inaudible or the wrong voicing, this ban is the first suspect — the fix is not to blanket-lift it
but to describe the *voicing* explicitly (e.g. sustained chords, not offbeat stabs).

| id | W | SI | **actual** | verdict |
|---|---|---|---|---|
| `w13-w30` | 30 | 75 | — | — |
| `w14-w40` | 40 | 75 | — | — |
| `w15-w45` | 45 | 75 | — | — |

### h10 — 2026-08-26, high-register 80s lead guitar. Baseline = h9, SI 75.

Kai: *"too much distortion now — the industrial bass kicks in distorted, and then we've also got
the guitar… let's go Whitesnake, Steve Vai level guitar. High-end 80s rock style. Less chords,
more melody."* The clash was two low, distorted layers fighting for the same register. Fix: move
the guitar up and out of the way.

🔴 **Critical fix bundled in.** The Exclude Styles box still banned `guitar solo`, `lead guitar`
and `shredding` — leftovers from the h3 Madness cleanup — which directly fought this new
direction. **Lifted**, along with `wah` (period-correct to the tone). Without this the style box's
new instruction and the exclude box would have been arguing with each other on every take.

| was | now | box |
|---|---|---|
| `a short high-register 80s rock guitar lick` *(unchanged wording, was already high-register from h9)* | — | style |
| `a low palm-muted guitar riff and a fuzzed indie guitar` (verse guitar) | `a high-register 80s rock lead guitar, Whitesnake and Steve Vai toned, melodic runs` | style, net −43 (dropped "never a solo" — no longer true, we want lead lines) |
| `[Intro …] heavy rock distorted guitar lick` | `[Intro …] high-register 80s rock guitar lick` | lyrics, +2 |
| My Taste: `One low palm-muted electric guitar riff with a fuzzed indie guitar over it, repeating, never a solo and never a chord progression.` | `One high-register 80s rock lead guitar, Whitesnake and Steve Vai toned, melodic runs, never a chord progression.` | taste, −18 |
| exclude: `guitar solo, lead guitar, shredding, ` and `wah, ` | *(deleted)* | exclude, shrinks |

**Kept:** `never chords` / `never a chord progression` in both style and My Taste — Kai's "less
chords" is still the rule; only the "never a solo" guard was dropped, since a Vai-toned melodic
lead is functionally a solo line.

| id | W | SI | **actual** | verdict |
|---|---|---|---|---|
| `w10-w30` | 30 | 75 | — | — |
| `w11-w40` | 40 | 75 | — | — |
| `w12-w45` | 45 | 75 | — | — |

### h9 — 2026-08-26, the heavy-rock intro lick. Baseline = h8, SI 75.

Kai: *"the intro should be very short, but a really wicked heavy metal electric guitar lick,
leading pretty quickly into a drum and bass drum with him singing to begin the song… whenever a
bit of melody appears on distorted electric guitar it's exciting — force it explicitly."* Two
swaps, both paid for:

| was | now | box |
|---|---|---|
| `one low detuned drone` (style step 1) | `a short heavy rock distorted guitar lick` | style, +19 |
| `one figure each, repeating, never a solo, never chords, under every vocal section` | `one figure each, repeating with occasional melodic bursts, never a solo, never chords` | style, net −3 (the "under every vocal section" clause dropped — the verse cues already say this) |
| `played straight, never jaunty` → `never jaunty` ; ` at full 174` dropped before `sub bass first` | — | style, −22 (paid the difference) |
| `[Intro — 2 bars, one low synth note]` | `[Intro — 2 bars, heavy rock distorted guitar lick, straight to the beat]` | lyrics, +36 |
| `[Verse 1 \| …, half the speed of the beat \| …]` and `[Verse 2 \| …, half the speed of the beat]` | the `half the speed of the beat` clause dropped from both — already stated once, globally, in the style box | lyrics, −56 |

**Net: style 952 → 946, lyrics cues shrank overall.** No new My Taste edit this round — the intro
and guitar-melody instructions are both section/structure-scoped, which is what the style box and
lyrics cues are for; My Taste stays at 1649.

| id | W | SI | **actual** | verdict |
|---|---|---|---|---|
| `w07-w30` | 30 | 75 | — | — |
| `w08-w40` | 40 | 75 | — | — |
| `w09-w45` | 45 | 75 | — | — |

### h8 — 2026-08-26, indie distorted guitar. Baseline = h7's dark industrial rewrite, SI 75.

Kai: *"more indie with more guitars — distorted guitars — keeping the dark industrial drum and
bass foundation."* Swaps only, per the h7 discipline: the clean `cold jangle` becomes a `fuzzed
indie guitar` in both the style box and My Taste, and the room is bought by deleting `corroded`
(style, redundant now the guitar carries the grit) and `hand-swept filters` (My Taste). No new
genre word added — "Dub soundsystem" as a bare genre anchor is what caused the Madness misread in
h3/h4, so the indie direction is carried by guitar texture only, not a label.

| id | W | SI | **actual** | verdict |
|---|---|---|---|---|
| `w01-w30` | 30 | 75 | — | — |
| `w02-w50` | 50 | 75 | — | — |
| `w03-w60` | 60 | 75 | — | — |

### h7 — 2026-08-26, dark industrial. Baseline = u02, SI 75, drops permanently deleted.

Kai: *"make it more dark industrial drum and bass and slightly less jump up, feel good — there's a
sort of dystopian vibe that we're missing."*

| id | W | SI | **actual** | verdict |
|---|---|---|---|---|
| `v01-w30` | 30 | 75 | **3:37 / 3:10** | — |
| `v02-w50` | 50 | 75 | **3:13 / 3:33** | — |
| `v03-w60` | 60 | 75 | **3:36 / 3:44** | — |

🟢 **The clock held. Mean 3:29 across six takes**, against 3:25 for `u02` — and the +10 characters
the industrial words cost changed nothing. So the text budget has slack at this size; it is the
difference between 616 and 2769 cue characters that matters, not ten.

🔴 **The new standing discipline, bought with h6: never add to a box in this sheet without taking
the same number of characters out.** The dystopian rewrite is made entirely of **swaps**:

| was | now |
|---|---|
| `Dark UK drum and bass` | `Dark industrial drum and bass` |
| `mixed like a dub soundsystem` | `mixed like a dub soundsystem, corroded` |
| `one low synth note` | `one low detuned drone` |
| `a chorus jangle` | `a cold jangle` |
| `spring reverb on the snare` | `struck steel on the snare` |
| `Grim, bitter and serious` | `Dystopian, grim and mechanical` |
| `Space used as an instrument…` *(deleted)* | `Rusted metallic textures and factory noise in the gaps.` |

The anti-jump-up excludes (`feel good`, `party`, `festival`, `anthemic`, `happy hardcore`,
`bright synths`, `euphoric`) were paid for by dropping five bans already covered by a neighbour
(`dancehall vocal`, `transatlantic`, `ragtime`, `honky-tonk`, `novelty`).

**Net: style 944 → 954, My Taste 1698 → 1661, cues 616 → 614.** The clock should hold at ~3:25.

### h6 — 2026-08-26, the subtraction ladder. Baseline W30 SI70, cues cut 2769 → 714 chars.

Kai: *"are we not over-complicating the style guide in square brackets… maybe we could get away
without any gap between the verses."* The first round in six passes that **removes** rather than adds.

| id | what is cut | cue chars | taste | verdict |
|---|---|---|---|---|
| id | what is cut | cue chars | taste | **actual** | verdict |
|---|---|---|---|---|---|
| h5 (for comparison) | nothing — the additive end point | 2769 | 1698 | 4:24 mean (n=8) | — |
| `u01-minimal` | every cue to the shortest fact only it can carry | **714** | 1698 | **3:58 / 3:39** | — |
| `u02-no-drops` | u01 **+ both drop cues deleted** — verse 1 runs straight into verse 2 | **616** | 1698 | **3:18 / 3:32** | 🟢 **ACCEPTED** — Kai, 2026-08-26 |
| `u03-bare` | u02 **+ My Taste cut** | **616** | **1178** | **3:30 / 3:15** | — |

### 🟢 SOLVED. Length is controlled by the VOLUME of prompt text, not by anything it says.

**h5 mean 4:24 → u03 mean 3:22. Sixty-two seconds, from deleting words.** `u03` take 2 at
**3:15** is the shortest take in the project, against 3:45 for the previous best and 4:48 for the
worst. Every step of the nested ladder moved in the same direction:

| cue chars | taste | mean |
|---|---|---|
| 2769 | 1698 | 4:24 |
| 714 | 1698 | 3:48 |
| 616 | 1698 | 3:25 |
| 616 | 1178 | 3:22 |

**The whole h2–h5 approach was backwards.** Six passes tried to shorten the song by adding
instructions — duration targets, bar counts, phrase rates, no-gap clauses — and every one of them
made it longer, because the instruction itself is what buys the time. Nothing that was *said* ever
mattered; only how much of it there was.

**The rule, and it now has forty takes behind it:** *the lyric cue box is a length control. Every
character in it costs musical time, whatever the character says.* `camping.md` §4a had the
mechanism written down the whole time — Suno allocates a phrase per **line** — and §4e recorded
that round 1's double-time fault came from cue **density**. We had the answer before we started.

**Deleting the drop cues (`u02`) was the single biggest step** — 3:48 → 3:25 from removing two
lines. Kai's call, and it is worth judging musically as well: verse one now hits verse two with no
instrumental break at all.

The ladder is **strictly nested** — each round is a subset of the one above — so if the length
moves we know which cut did it.

**What survived the cull, and why.** The lyric cue is the only **section-scoped** box we have
(`camping.md` §4f), so the only things it must carry are **which of the two men is speaking** and
**Kai's own performance cues**. Everything else was the style box restated in longhand:

```
[Verse 1 | gravelly spoken voice, half the speed of the beat | no drums for the first half, then the breakbeat]
[Verse 2 | posh voice, a completely different man, half the speed of the beat]
[Bridge | the two men trade, close and dry | drums stripped back]
```

**The style box was cut too, 988 → 944:** the no-gap clause is gone — it measurably made the gaps
bigger — and the amen clause that was sacrificed for it is back.

### h5 — 2026-08-26, the length pass. Baseline W30 SI70, instrumentals 8 bars.

| id | phrase rate | duration | actual | verdict |
|---|---|---|---|---|
| `t01-tight` | every 2 bars | 240s | **4:48 / 4:18** | — |
| `t02-onebar` | **every 1 bar** | 240s | **4:32 / 4:07** | — |
| `t03-tight-150` | every 2 bars | **150s** | **4:06 / 4:30** | — |
| `t04-onebar-150` | **every 1 bar** | **150s** | **4:41 / 4:17** | — |

### 🔴 The takes got LONGER as we tried to shorten them — and the prompt did it

Kai, 2026-08-26: *"why is everything taking much longer now?"* He is right, it is measurable, and
it is our doing.

| pass | what was added | n | mean |
|---|---|---|---|
| s1 scouting | — (the take Kai picked) | 14 | **4:09** |
| h1 sliders | nothing textual | 12 | **4:06** |
| h2 orchestral | orchestral cue text, 4-bar cues | 6 | 4:17 |
| h3 dub serious | — | 2 | 4:11 |
| h4 +horn | horn text in style, both drop cues, My Taste | 12 | **4:19** |
| h5 +no-gap | no-gap text in style, My Taste, 3 vocal cues; 2-bar cues | 8 | **4:24** |

**Before the horn: 4:09 mean (n=31). After: 4:21 (n=20). +12 seconds.**

And the thing that grew monotonically alongside it is **the amount of text**:

| | s1 | h5 |
|---|---|---|
| cue characters | 2199 | **2769** (+26%) |
| the first drop cue | 227 chars | **363 chars** |
| My Taste | 1277 | **1698** (+33%) |
| word lines | 48 | 48 |

**The mechanism is already written down in this repo.** `camping.md` §4a: Suno allocates a
musical phrase per **line**, and §4e records that round 1's double-time fault came from **cue
density**. A drop cue that says *"2 bars only"* in 363 characters is a bigger block of text
occupying that section than one that said *"8 bars"* in 227 — and the stated bar number has never
once been obeyed, while the text volume tracks the length almost perfectly.

**So every attempt to shorten the song made it longer, because every attempt added words.** That
is the finding, and it inverts the whole h2–h5 approach: the next length experiment is not another
instruction, it is **deleting instructions**.

### 🔴 Length cannot be controlled by ADDING to the prompt. Stop trying.

`t04` is the maximally compressed variant — instrumentals cut to 8 bars from 32, an explicit
no-gap instruction in the style box, My Taste and all three vocal cues, the phrase rate halved to
one per bar, and a 150-second target. **It came back at 4:41 and 4:17.** `t01`, which changed
none of the last three, came back at **4:48 and 4:18** — the longest take in the pass belongs to
the *least* compressed round and the second longest to the *most* compressed one, which is the
clearest possible statement that none of it is connected.

Everything tried, and what it did:

| lever | values tried | effect on length |
|---|---|---|
| Duration target | 150, 200, 210, 240 | **none** — all return 3:50–4:47 |
| Instrumental bar counts | 32 → 16 → 8 | **none** |
| Phrase rate | every 2 bars → every 1 bar | **none** |
| Explicit no-gap clauses | absent → in 5 places | **none** |
| Weirdness | 15–50 | none, except 15 running away to 7:59 |
| Style Influence | 55–95 | none |

Forty-odd takes across five passes: **this song comes back at ~4:00–4:40 whatever the prompt
says.** The one input never varied is the **48 lyric lines**, and the earlier arithmetic
(~4.6s/line) is now better read as a description than a mechanism — because if bars per line were
really the driver, halving the requested rate would have moved something.

**Two honest routes left, and neither is a prompt round:**

1. **Cut lyric lines and measure.** The only untested input. Both of Kai's edit rounds came out
   even at 48 lines, so it has genuinely never been tried.
2. **Cut it in the edit.** Suno Studio, or the Premiere bridge. `camping.md` §4a already routes
   the phrasing endgame to Studio for the same reason: the sheet gets it close, the edit gets it
   exact. Length is now in that category.

**What changed in the baseline:** instrumentals halved again (16 bars → 8 — intro, both drops and
outro are 2 bars each), and an explicit **no-gap** instruction added to the style box, My Taste,
and all three vocal-section cues (*"no gap between lines, every line lands on the bar after the
one before"*). The style box lost its amen clause to buy the room — the roll is still named in all
four section cues, which is where it has always actually been won. **If the fills go quiet, that
is why.**

🔴 **`[Beat Transition]` was Kai's hypothesis and the mechanism is real** — a bare cue on its own
line can buy its own section. It has been stripped from the generated block since h2, so it is not
the current cause.

### h4 — 2026-08-26, the slider grid on jangle-kept. Baseline W30 SI70 240s.

| id | variable | actual | verdict |
|---|---|---|---|
| `s01-anchor` | the anchor — jangle kept, horn escalated | 4:01 | — |
| `s02-w20` | Weirdness 30 → 20 | 3:50 / 4:18 | — |
| `s03-w40` | Weirdness 30 → 40 | 4:16 / 3:58 | — |
| `s04-w50` | Weirdness 30 → 50 | — | — |
| `s05-si55` | Style Influence 70 → 55 | 4:47 | — |
| `s06-si85` | Style Influence 70 → 85 | 4:25 / 4:37 | — |
| `s07-si95` | Style Influence 70 → 95 | 4:23 / 4:40 | — |
| `s08-no-taste-horn` | the control — horn removed from My Taste only | 3:59 / 4:37 | — |

🟢 **The diagnostic answered: the jangle was innocent.** `r12` kept the chorus-pedal jangle and
Kai picked it, so the Madness was coming from **`Dub soundsystem` as the genre anchor**, not from
the guitar. The jangle is back in the baseline permanently, and `mixed like a dub soundsystem`
is the phrasing we never promote back to a genre word.

🔴 **The horn had to be escalated in gears.** `r11` lifted `brass band` and asked for *one stab*
in the style box plus one cue — inaudible. Now it is a named low brass **section**, in the style
box, in **both** drop cues, and in My Taste. `s08` is the control: My Taste has no section scope,
so if the horn starts bleeding across the whole record, that round is what proves it.

🔴 **Weirdness 15 is not in this grid** — 7:59 on both takes, the only runaway in thirty. 20 is the floor.

### h3 — 2026-08-26, back to dub. Baseline W30 SI70 240s. ✅ `r12` WON.

| id | variable | actual | verdict |
|---|---|---|---|
| `r10-dub-serious` | **the candidate** — dub foundation, no jangle, no orchestra, serious register | ? / ? | — |
| `r11-dub-horn` | one low brass stab at each drop and nowhere else — a flourish, never a theme | 3:52 / 4:31 | — |
| `r12-jangle-kept` | the diagnostic — the jangle put back, to learn which cause was real | ? / ? | — |

### h2 — 2026-08-26, the orchestral pass. 🔴 REJECTED.

Kai, on hearing it: *"the orchestral thing is the wrong thing… it doesn't work at all to try to
make it an orchestral tune."* Backed out the same session. The lesson is worth keeping: **the fix
for a genre reading wrong is to remove what causes it, not to add a different genre on top.**
Rounds `r07-orch` (4:13 / 4:14), `r08-orch-heavy` (4:17 / 4:27), `r09-orch-w15` (**7:59 / 7:59**)
— 6 takes, superseded.

🔴 **Weirdness 15 ran away to 7:59 on both takes** — double the target, and the only pair in
thirty takes to do it. One data point at one Style Influence, but low Weirdness is now the first
suspect if a take comes back enormous, and 15 is not a setting to reach for casually.

### h1 — 2026-08-26, sliders and duration on the dub baseline. Style locked.

| id | W | SI | target | **actual** | verdict |
|---|---|---|---|---|---|
| `r01-d210` | 30 | 85 | 3:30 | **4:16 / 4:39** | — |
| `r02-d240` | 30 | 85 | 4:00 | **4:04 / 3:52** | — |
| `r03-w15` | **15** | 85 | 3:30 | 3:56 / 4:08 | — |
| `r04-w45` | **45** | 85 | 3:30 | 4:23 / 4:02 | — |
| `r05-si70` | 30 | **70** | 3:30 | 4:03 / 4:05 | — |
| `r06-si95` | 30 | **95** | 3:30 | 3:45 / 4:02 | — |

### 🔴 The duration target barely moves the length

All twelve takes are in. **Ten takes asked for 3:30 and averaged 4:07** (4:16, 4:39, 3:56, 4:08,
4:23, 4:02, 4:03, 4:05, 3:45, 4:02). **Two asked for 4:00 and averaged 3:58.** The accepted take
asked for 3:20 and returned 3:54.

So the honest reading is not that the control is inverted — the r01 pair being the longest two in
the set is within the spread. It is that **the target has little or no effect on length, and
asking for less certainly does not get less.** This song is a ~4:00 song and the slider does not
argue with it. 240s is kept as the setting because it is the only value that has ever been met.

🔴 **And the bar counts did not shorten it either — I predicted they would and they did not.**
The h2 and h3 passes both halved the instrumental cues from 32 bars to 16, which should have been
worth ~22 seconds. Takes after the cut: 4:13, 4:14, 4:17, 4:27, 3:52, 4:31 (plus the two 7:59
runaways). Before the cut: mean 4:07. **No change.** Either Suno is not reading the bar counts, or
it pads elsewhere to fill the length it wants.

### 🟢 What length is actually made of — measured 2026-08-26

Back-calculated from thirty takes rather than assumed. At 174 BPM a bar is 1.38s, and the takes
run 3:50–4:18 for **48 word lines plus 16 instrumental bars**. That solves to roughly **3.3 bars,
or ~4.6 seconds, per lyric line**:

| section | lines | ≈ seconds |
|---|---|---|
| Verse 1 | 16 | ~74 |
| Verse 2 | 16 | ~74 |
| Bridge | 15 | ~69 |
| Outro | 1 | ~5 |
| instrumental cues | 16 bars | ~22 |
| **total** | **48** | **~4:04** — which is what comes back |

🔴 **And that explains everything that failed.** `camping.md` §4a's rule is *one phrase per line*
— about 1.4s. These lines are costing 4.6s, because the prompt asks for the vocal at **half the
speed of the beat, one phrase every two bars**, and the gaps between phrases cost as much as the
phrases. **The half-time delivery is what makes the song long.** It is also the single thing Kai
picked out of thirty takes, so the two goals are in direct tension and that is worth naming rather
than fixing quietly.

**The one honest lever: cut lines.** Each is worth ~4.6 seconds. 4:00 → 3:30 is about **six or
seven lines**. Neither the duration target nor the instrumental bar counts moved the length at all,
so this is the only thing that will.

Kai's 2026-08-26 lyric edits came out **even at 48 word lines** both times, merges offset by
additions, which is why nothing got shorter from the words alone.

---

## 7. How this is driven

```bash
npx tsx scripts/suno/halftime.mts plan [ids...]     # resolved boxes, offline
npx tsx scripts/suno/halftime.mts check             # live form + My Taste, spend nothing
npx tsx scripts/suno/halftime.mts taste-backup      # REQUIRED before run
npx tsx scripts/suno/halftime.mts load <id>         # fill one round whole, generate NOTHING
npx tsx scripts/suno/halftime.mts run [ids...]      # 10 credits and 2 takes per id
npx tsx scripts/suno/halftime.mts taste-restore     # put the house profile back — DO THIS AFTER
```

### The three rules that cost real time to learn

🔴 **Read My Taste back at the start of every session.** See §1.

🔴 **Count paragraphs, never characters.** A Lexical `fill()` collapses the whole block into one
paragraph and still reports the right length, which for a cue sheet destroys the architecture.

🔴 **Bump `SET` on every lyric or cue change.** `create()` waits for two takes matching the title;
a re-run under an unchanged title matches the *previous* run's takes and reports a success it
never generated.
