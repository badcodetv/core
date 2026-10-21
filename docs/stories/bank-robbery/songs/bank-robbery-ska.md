---
title: The Bank Robbery — the song (2-tone ska, CANONICAL)
status: sound LOCKED 2026-10-21 (Kai); words and timing still to rework
model: v6
settings: style influence 75, weirdness 60, Variety off, Max Mode off, Personalize off, Vocal Gender unset, no Voice, Duration 180 s
workspace: bank-robbery
reference-take: br-song-ska-A-v6-w60 — https://suno.com/song/bca822dd-c443-48e3-8988-b2328ab916a7
sibling: robbery-styles.md (the eight-style sweep this came from)
---

# The Bank Robbery — the song (canonical)

🔑 **This is the sound.** Kai, 21 October 2026, on take `bca822dd`: *"I think we found our sound."*
What he loves: **a front man plus a chorus of three to five voices**, which makes it rich and
choral. The boxes below are **exactly the ones that made that take**, copied from the sweep without
a word changed. Don't "improve" them: on Suno v6 the same boxes never give the same take twice,
and nobody knows yet which words were holding the sound up.

**What happens next:** the words and the timing get reworked. The sound stays put.

## The reference take

| Take | Length | Link |
| --- | --- | --- |
| br-song-ska-A-v6-w60 ⭐ | 3:00 | https://suno.com/song/bca822dd-c443-48e3-8988-b2328ab916a7 |

Preview recording: `C:\Users\kai\Desktop\suno-recordings\br-song-ska-a-v6-w60-bca822dd.wav`.
This is a playback capture, not a download. Listening report:
[`docs/listening/log/2026-10-21-082552-br-song-ska-a-v6-w60-bca822dd.md`](../../../listening/log/2026-10-21-082552-br-song-ska-a-v6-w60-bca822dd.md).

## What the sound is (from the listen, 21 October 2026)

Heard by Gemini, compared against the boxes below, plus local measurements. It is one take,
heard by machine. Kai's ear outranks it.

- **Tempo:** 148 BPM measured (we asked for 150). Loudness −14.4 LUFS. Fairly narrow stereo, as
  on an early-80s record. Bright: the spectral centre is 3.9 kHz.
- **Front man:** British male, mid-register, dry and up front. He **toasts** (rhythmic
  chant-speaking, the Jamaican-rooted ska style) rather than sings.
- 🔑 **The gang:** it sounds like **three to five other men, shouting in unison or in octaves**. They
  do three jobs:
  1. **The intro shout:** "ROBBERY!" at 0:05.
  2. **Line-end answers inside verse 1:** "each day" 0:30, "earn that dough" 0:33,
     "nobody knows" 0:36, "FREEZING!" 0:47. Nobody wrote these answers. The model added them.
  3. **The whole chorus shouted together:** 1:18–1:31 and 2:23–2:36.
- **Band:** offbeat upstroke guitar skank, a round walking electric bass, trumpet and trombone
  stabs in harmony (horn solo at 1:44), Farfisa organ chords and swells, offbeat hi-hat with a
  rimshot snare.
- **Layout as it came out:** intro 0:00–0:26 · verse 1 0:26–1:18 · chorus 1:18–1:31 · post-chorus
  (lead + horn answers) 1:31–1:44 · horn break 1:44–1:57 · verse 2 1:57–2:23 · chorus 2:23–2:36 ·
  outro 2:36–2:57, ending on a hit.

**What most likely made the gang** (the listener's reading, not proven): the Style clause
`the hook a gang shout from the whole band`, the lyric tag `[Chorus: whole band gang shout]`, the
parenthesised `(Robbery!)` intro, and the capitals in `FREEZING!`.
🔴 **Leave `choir` in the Exclude box.** It did not stop the gang. What it probably did stop is the
gang turning into a sung church choir. That's untested, so it isn't a reason to take it out.

## Where the words fight the beat (what the rework fixes)

| Time | Line | Problem |
| --- | --- | --- |
| 0:49 | stimulus checks are next, get wrecked | "get wrecked" rushed |
| 0:58 | now let's get jiggy, just like Biggie | "just like Biggie" mumbled onto the downbeat |
| 1:36 | Institutional, dilutional, the usual | long words squeezed |
| 2:11–2:22 | It's not the standard … Hewlett and the kitchen sink | verse 2 heavily crammed |

The lines that land cleanly are short and punchy: chorus, "grandma FREEZING!", "nobody knows!".
That is the target shape. At 148 BPM, think **6–10 syllables a line**, with a word at the end of
each line the gang can shout back.

## Plan (Kai, 21 October 2026)

1. ✅ **Kai writes the whole song:** done 21 October, in `score.md` § Lyrics.
2. ✅ **Claude expands the lyric guidance** on Kai's draft: syllables per line, shoutable last
   words, where the gang answers, bracket cues in the style of the take above.
3. 🟡 **Regenerate both ways, side by side:** generated 21 October (round B below), unheard.
   - **A:** a Cover of `bca822dd` with the new lyrics, to keep this exact band.
   - **B:** fresh takes from the canonical boxes below, with only the Lyrics box changed, as the
     pair at weirdness 30/60.

## Suno prompt

Style:

```
2-tone ska, 150bpm: choppy offbeat guitar skank, a bouncing walking bassline, a stabbing trombone and trumpet horn section and a cheap Farfisa organ. A British vocal toasting the verses in rhythmic chant, the hook a gang shout from the whole band. Early-80s Coventry records, live in one room, tight and trebly, played straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, drum and bass, jungle, breakbeat, boom bap, grime, UK garage, big beat, acid, synth, distorted guitar, EDM, orchestral, choir, pop punk
```

Lyrics (exactly as generated; the rework starts from here):

```lyrics
[Intro: horn fanfare, organ, offbeat skank]
(Robbery!)

[Verse 1: toasting, rhythmic and chanted]
They say, ya can't make money from a tree
let's see, each day, not free, ay
work and get paid though, earn that dough
but where does it go? nobody knows!

means of production means a reduction
standards bleeding, land-lords needing
quantitative easing, grandma FREEZING!
stimulus checks are next, get wrecked

rent seeking? just about eating
sorry, did I interrupt your meeting?
now let's get jiggy, just like Biggie
don't get high off your own supply

this money system is insistent
on debts existence, so
don't be hating on the credit rating
or have resistance to the facts I'm stating

[Chorus: whole band gang shout]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in the basement!
Printer is burring, now what's occurring?

[Post-Chorus: lead vocal, horns answer]
There are stacks of ecstatic cash
A real homeopathic stash
Institutional, dilutional, the usual
bold, wrong and rash

[Instrumental Break: trombone solo over the skank]

[Verse 2: toasting, faster]
The real attraction becomes the distraction
the retention of the tension, between all the factions
state sponsored manipulation
delivered through the radio station

It's not the standard, propaganda, worth a couple grand-ahh
No, deep level, dancing with the devil and very well planned-ahh
Just to think, that we bust our balls to earn some ink
Then they come along with a Hewlett and the kitchen sink

[Chorus: whole band gang shout]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in the basement!
Printer is burring, now what's occurring?

[Outro: horns, organ, band stops on a hit]
```

---

## Round B (21 October 2026): Kai's full song, cued

Kai, 21 October: *"completely replace my square brackets with your much better… square brackets…
any kind of character that we can add to the words would be amazing."* Then 15–16 versions across
both routes, a couple of styles, and a couple of slider settings.

**Words:** Kai's draft from [`score.md`](./score.md) § Lyrics, **word for word**. His deliberate
spellings are kept (`quantative`, `da basement`, `occuring`, `sooooo`, `waaaay`, `dispraxic`). Every
bracket of his is replaced. Three kinds of change only:

1. **Cues** in square brackets, on their own lines, at most three directions each. The front man
   has one fixed label, `toasting front man`, repeated word for word, because changing the
   wording reads to Suno as a new singer.
2. **Punctuation for the in-bar pauses Kai asked for.** A full stop is a clean break inside the
   line (`stimulus checks are next. Get wrecked!`). The `...` after `rent seeking?` is a hitch,
   not a drift. The commas in `it is, state, level, manipulation` are kept: each comma is a stress
   break, and this is the one line where the word-by-word drawl is the point.
3. **Two gang shouts that use the song's own word:** the `(Robbery!)` intro call, which the
   canonical take turned into its best shout, and the same call on the outro. No new lyrics.

How Kai's notes became cues:

| Kai's note | Now |
| --- | --- |
| grandma FREEZING as a choral shout | `[Gang shout doubles the lead]` on that line only |
| pause before "get wrecked" | a full stop plus a `[Stop-time hit…]` cue, ska's own trick: the band stops on one hit and the punchline lands in the gap |
| pause at "rent seeking?" | `?...` |
| sarcastic "interrupt your meeting" | `[Mock-polite, sarcastic, half-spoken]` |
| advert cut-away for "the Fed is not your friend" | `[Cutaway: chirpy high-pitched TV advert voice…]`, then `[toasting front man, band back in]` |
| chorus 2: up a key, not cheesy | the lyric stays identical and the **tag** escalates (`up a step, bigger gang, horns blaring`), plus police sirens and an alarm bell, which are this song's own sounds |
| bouncy timing on "propaganda" | `[Bouncy and syncopated, skip on every comma]` |
| pauses in "state, level, manipulation" | `[Staccato, one word per horn stab]` |
| one bar that sounds completely different | `[Sudden switch for one bar: dusty 90s boom bap beat, deep slow New York rapper]`. The artist is not named, and `boom bap` comes off every Exclude list so the switch is allowed |
| (new) the last stanza | `[Breakdown: drums and bass only, lead low and serious]`, so the revolution lines land heavy before the final shout |

🔴 **The risk:** verse 1 now carries five cues in 20 lines. Dense cueing once broke Camping into
double time (`lyricist-playbook.md` §3). If verse 1 rushes in every take, strip cues before
touching anything else.

### Round B lyrics (shared by every Round B take)

```lyrics
[Intro: horn fanfare, Farfisa organ, offbeat skank]
(Robbery!)

[Verse 1: toasting front man, gang answers the line ends]
They say, ya can't make money from a tree
let's see, each day, make hay, not free, aay
work and get paid though, earning that dough
but where does it go? nobody knows!

means of production means a reduction
standards bleeding, land-lords needing
[Gang shout doubles the lead]
quantative easing, grandma FREEZING!
[Stop-time hit, then the punchline alone]
stimulus checks are next. Get wrecked!

rent seeking?... I'm just about eating
[Mock-polite, sarcastic, half-spoken]
sorry, did I interrupt your meeting?
[Cutaway: chirpy high-pitched TV advert voice, jingle organ]
remember kids, the Fed is not your friend!
it prints all the dollars that the government spends

[toasting front man, band back in]
this fiat system is insistent
on debts existence, sooooo
don't be hating on the credit rating
or have resistance to the facts I'm stating

[Chorus: whole band gang shout, police sirens]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burring, now now what's occuring?

[Chorus: up a step, bigger gang, horns blaring, alarm bell]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burring, now now what's occuring?

[Verse 2: toasting front man, gang answers the line ends]
Stacks and stacks of elastic cash
distracted by a dispraxic flash,
mob, angry at their shitty little job
the right and the left both witness the theft

blaming each other is a sick little cover
institutional, dilutional, the usual
[Gang shout doubles the lead]
distraction IS the attraction
the intention is tension between the factions

divide and conquer, just look at the hand
[Bouncy and syncopated, skip on every comma]
It's not ya standard, propaganda, worth a couple grand-ahh
[Staccato, one word per horn stab]
it is, state, level, manipulation
it is the devil, with a radio station

stack up the vaults like a wheelbarrow
risk of default is really rather narrow
Biggie said waaaay back in ninety seven
[Sudden switch for one bar: dusty 90s boom bap beat, deep slow New York rapper]
don't get high off your own supply

[Chorus: whole band gang shout, police sirens]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burring, now now what's occuring?

[Chorus: up a step, bigger gang, horns blaring, alarm bell]
Robbery, robbery!
Call the police, it's a robbery!
Debasement! Debasement! It happened in da basement!
Printer is burring, now now what's occuring?

[Verse 3: toasting front man, menace building]
You know the real star is Pablo Escobar,
who has elastic bands not plastic hands,
stacking up the cash by the grands
standard plans are for the working man

and this right here is a next level scam
ill gotten gains, no need to explain
"bail" and "out", will never mean the same
[Gang shout doubles the lead]
own the printer and you don't fear winter

crime is asset inflation and the passive creation;
a wealth gap which drives the political situation
working people get paid in money, so it's not very funny
when you print more and expect them not to worry

[Breakdown: drums and bass only, lead low and serious]
hungry people, feed a revolution,
then it's retribution, perhaps some execution
it's time to give, not just to take
but for heaven’s sake, don't just eat cake

[Outro: whole gang shouts, band stops on a hit]
(Robbery!)
```

### Round B styles

Four ways in. Every one uses the lyrics above, Variety Off, Max Mode off, Personalize off, no
Voice, Duration 300 s (the song is now about twice as long as round A's).

| Run | Route | Boxes | Sliders | Creates |
| --- | --- | --- | --- | --- |
| **B-cover** | **A**: Cover of `bca822dd` (keeps that band) | canon Style + Exclude | audio influence 75 and 40, weirdness 30, style influence 75 | 2 |
| **B-canon** | B: fresh | canon Style + Exclude | style influence 75, weirdness 30 / 60 | 2 |
| **B-gang** | B: fresh | the gang Style below | style influence 75, weirdness 30 / 60 | 2 |
| **B-gang-si90** | B: fresh | the gang Style below | **style influence 90**, weirdness 30 / 60 | 2 |

The only change to the canonical Exclude list is that `boom bap` comes out, so the one-bar switch
is allowed.

#### Canon (B-cover, B-canon)

Style:

```
2-tone ska, 150bpm: choppy offbeat guitar skank, a bouncing walking bassline, a stabbing trombone and trumpet horn section and a cheap Farfisa organ. A British vocal toasting the verses in rhythmic chant, the hook a gang shout from the whole band. Early-80s Coventry records, live in one room, tight and trebly, played straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, drum and bass, jungle, breakbeat, grime, UK garage, big beat, acid, synth, distorted guitar, EDM, orchestral, choir, pop punk
```

#### Gang (B-gang, B-gang-si90)

The canonical sound, with the round-A listen written back into it: the gang's size and its jobs,
the sirens, and the two cut-aways, declared in the Style box so the lyric cues have something to
point at.

Style:

```
2-tone ska, 150bpm: choppy offbeat guitar skank, a bouncing walking bassline, stabbing trombone and trumpet, a cheap Farfisa organ, police sirens and an alarm bell on the chorus. A British front man toasting the verses in rhythmic chant, a gang of four or five mates shouting back his line ends and roaring every chorus in unison. Two sudden cut-aways: a chirpy TV advert voice, and one bar of dusty 90s boom bap. Early-80s Coventry records, live in one room, tight and trebly, played straight.
```

Exclude styles:

```
comedy, novelty, parody, kazoo, drum and bass, jungle, breakbeat, grime, UK garage, big beat, acid, synth, distorted guitar, EDM, orchestral, choir, pop punk
```

### Round B log (21 October 2026)

8 Creates, 10 credits each, **80 in all (10,280 → 10,200)**. All 16 takes are in the new
**`bank-robbery-Kai`** workspace (Kai made it for this run). Unheard; no pick yet.

| Take | Length | Link |
| --- | --- | --- |
| br-ska-B-cover-r1-v6-ai75-w30 | — | https://suno.com/song/b9b07375-7787-4119-80b8-9cd25e18ddb4 |
| br-ska-B-cover-r1-v6-ai75-w30 | — | https://suno.com/song/2324966a-d046-4acf-834e-5ce379bacdc5 |
| br-ska-B-cover-r1-v6-ai40-w30 | — | https://suno.com/song/6141fa6c-8096-4c27-95d9-b16806ffa2b0 |
| br-ska-B-cover-r1-v6-ai40-w30 | — | https://suno.com/song/8ffda9fe-871b-42bf-a872-cb082d51a986 |
| br-ska-B-canon-v6-w30 | 4:59 | https://suno.com/song/b3eed7d6-6e00-43fc-8305-d1285dccbb8c |
| br-ska-B-canon-v6-w30 | 4:59 | https://suno.com/song/350ff048-8244-4220-bb06-e7900c10a51b |
| br-ska-B-canon-v6-w60 | 4:59 | https://suno.com/song/0cd2b40a-1a94-4f80-b71b-0427461a8232 |
| br-ska-B-canon-v6-w60 | 4:59 | https://suno.com/song/f6098eff-88ca-445c-9c3e-067eb5cee641 |
| br-ska-B-gang-v6-w30 | 4:59 | https://suno.com/song/d72269b6-a832-447a-bfb1-79449e3f3449 |
| br-ska-B-gang-v6-w30 | 4:33 | https://suno.com/song/246886ed-d0fa-4bfa-86ff-d4defe56c619 |
| br-ska-B-gang-v6-w60 | 4:59 | https://suno.com/song/0df6a5e2-1d1f-49f9-b0fd-bf0d131bb655 |
| br-ska-B-gang-v6-w60 | 4:00 | https://suno.com/song/2bed1e38-edc8-49e8-abb8-1fc903a4491d |
| br-ska-B-gang-si90-v6-w30 | 4:55 | https://suno.com/song/df12350a-8cc8-4575-a501-796860c0fba1 |
| br-ska-B-gang-si90-v6-w30 | 4:59 | https://suno.com/song/f69daeaf-cac8-4cfa-a459-25f6d7f8daba |
| br-ska-B-gang-si90-v6-w60 | 4:59 | https://suno.com/song/66e78114-b2d0-4dd4-ba78-8be586af96d0 |
| br-ska-B-gang-si90-v6-w60 | 4:59 | https://suno.com/song/f766f4b5-94ce-463d-b06f-e439bbc3abb9 |

Cover lengths were unreadable because they were still rendering. **Check them first:** the source is
3:00 and the new words need about 5:00. If a cover stops at 3:00, it has dropped verse 3.

Two takes came back short, at 4:00 and 4:33. They may have dropped a section; check that verse 3
is there.

**How the covers were run:** `bca822dd` was no longer in any workspace list the tool could see, so
it was attached straight from the library by its ID (`runNarrow`, now exported from `suno.mts`).
The detach failed at the end of the run and worked on a retry, so the form is back in Custom.

---

## Round C (21 October 2026): darker, a gruff cockney front man, 3:30

Kai's notes on round B: put the cues **in `score.md`** (done: the lyrics there are now the cued,
live version, and round C sings them); cap the length at **3:30**; go **darker**; make the delivery
**direct** ("more like robbery, robbery"); and use a **gruff cockney** voice, "rather than a sort of
overtly reggae singing".

**Why it went reggae:** the Style box said `toasting` and the cues said `toasting front man`.
Toasting *is* the Jamaican sound-system delivery, so the reggae voice was asked for in two boxes.
That was Claude's word. It now goes in the Exclude list.

**How the voice is cast:** accent words alone don't move a Suno voice; that was tested on Camping
and again on Jack's song. A **translated singer reference** does: a real singer's scene, era, voice
and delivery, described in the Style box without the name (`suno-voices.md` §2c, Jack, 21 October).
It can also drag the band towards the singer's scene, so the ska music sentence stays **first**
and the singer comes after it. Three references, one per variation. The names are in this sheet
only, never in a box:

| Variation | Reference | Why |
| --- | --- | --- |
| **C-geezer** | Ian Dury | cockney, gruff, half-spoken, deadpan menace, a music-hall wit. The closest to "direct" |
| **C-punk** | Joe Strummer (the Clash's ska-punk side) | a hoarse, barked London punk voice; angrier |
| **C-terrace** | Jimmy Pursey (Sham 69) | a rough working-class terrace shouter, the bark of the chorus carried into the verses |

The music sentence is the same in all three, made darker: **minor key**, menacing horns, an eerie
wailing organ (the *Ghost Town* end of 2-tone, not the party end), sirens on the chorus. One
variable per round: only the singer changes.

**Length:** Duration 210 s (3:30). Suno sticks to the number closely, so the real risk is
**cramming**: 70 sung lines in 3:30 is about 10% faster than round A, which already rushed in places.
If the verses rush, the cheapest fix is to make the first chorus single instead of double,
which saves about 13 seconds.

Settings: v6, style influence 75, the pair (weirdness 30 / 60), Variety Off, Max Mode off,
Personalize off, no Voice, workspace `bank-robbery-Kai`. 6 Creates, 60 credits.

Exclude styles (all three):

```
comedy, novelty, parody, kazoo, reggae, toasting, dancehall, patois, crooning, smooth vocals, drum and bass, jungle, breakbeat, grime, UK garage, big beat, acid, synth, distorted guitar, EDM, orchestral, choir, pop punk
```

#### C-geezer

Style:

```
Dark minor-key 2-tone ska, 150bpm: choppy offbeat guitar skank, a heavy walking bassline, menacing trombone and trumpet stabs, an eerie wailing Farfisa organ, police sirens on the chorus. A gruff East London geezer in the late-70s pub-rock tradition, cockney vowels and dropped h's, half-speaking the verses straight at you with deadpan menace, a gang of four or five mates shouting back his line ends and roaring the chorus. Live in one room, tight and trebly, played straight.
```

#### C-punk

Style:

```
Dark minor-key 2-tone ska, 150bpm: choppy offbeat guitar skank, a heavy walking bassline, menacing trombone and trumpet stabs, an eerie wailing Farfisa organ, police sirens on the chorus. A hoarse 1979 London punk voice, gravelly and barked, snarling the verses direct and hard on the beat, a gang of four or five mates shouting back his line ends and roaring the chorus. Live in one room, tight and trebly, played straight.
```

#### C-terrace

Style:

```
Dark minor-key 2-tone ska, 150bpm: choppy offbeat guitar skank, a heavy walking bassline, menacing trombone and trumpet stabs, an eerie wailing Farfisa organ, police sirens on the chorus. A rough working-class London terrace shouter, a gravel-throated cockney bark, every verse line shouted short and blunt like a football chant, a gang of four or five mates shouting back his line ends and roaring the chorus. Live in one room, tight and trebly, played straight.
```

### Round C log (21 October 2026)

6 Creates, **60 credits (10,200 → 10,140)**, workspace `bank-robbery-Kai`. Unheard.

| Take | Length | Link |
| --- | --- | --- |
| br-ska-C-geezer-v6-w30 | 3:40 | https://suno.com/song/d4ed54df-5b00-417c-9bd0-8ade1a3a2de0 |
| br-ska-C-geezer-v6-w30 | 3:30 | https://suno.com/song/87e42bc8-109f-46df-b723-93b7b7c0371e |
| br-ska-C-geezer-v6-w60 | 3:30 | https://suno.com/song/f3958437-3ef7-4df2-b397-7f579b89641b |
| br-ska-C-geezer-v6-w60 | 3:30 | https://suno.com/song/0b2e79c1-52a3-41d3-88b6-f0e1b17b5cc4 |
| br-ska-C-punk-v6-w30 | 3:30 | https://suno.com/song/2d17e9f0-9b5a-4abf-a034-b9e51050b981 |
| br-ska-C-punk-v6-w30 | 3:31 | https://suno.com/song/bef4a5d2-deab-46a6-b4e2-50bb1a2557f7 |
| br-ska-C-punk-v6-w60 | 3:30 | https://suno.com/song/12533c00-278a-4581-bc6c-115c4e6204f0 |
| br-ska-C-punk-v6-w60 | 3:30 | https://suno.com/song/eca83a52-a8dc-4e83-bd6c-090b95084d20 |
| br-ska-C-terrace-v6-w30 | — | https://suno.com/song/0005a2d7-06b4-4d10-ae0f-635e4e4edf6e |
| br-ska-C-terrace-v6-w30 | — | https://suno.com/song/a8127c29-752b-4220-b104-b653ccc25fe9 |
| br-ska-C-terrace-v6-w60 | — | https://suno.com/song/af63574a-8ce0-4d41-b7f6-4ee65edb2a2a |
| br-ska-C-terrace-v6-w60 | — | https://suno.com/song/e62560df-399c-4e80-bd39-ea8d8e0d2233 |

Terrace was still rendering when listed. Round B's covers finished at **4:31–4:41**, so a v6 Cover
**does** run past its 3:00 source when the duration asks for more.
