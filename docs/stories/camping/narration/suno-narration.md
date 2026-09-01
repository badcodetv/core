---
title: Camping — narration (Suno)
status: drafting
model: v5.5
mode: Advanced
settings: audition style influence 85 / weirdness 60; production style influence 85 / weirdness 0-25; audio influence n/a (40–60 once a Voice is attached)
voices: [narrator]
---

# Narration on Suno — camping

> **What this is:** the four paste-ready boxes and the click-path for generating the camping
> film's narration in Suno as **spoken word**. The voice brief is [`voice.md`](./voice.md); the
> script's job list is [`../narration-brief.md`](../narration-brief.md). Built 2026-08-31 against
> `docs/suno-gpt/` — every casting decision below is a **tested** finding from our own Camping
> and Karen rounds, not a guess.

## ⚠️ Read this before you spend a generation

**We already moved narration off Suno once.** [`../../karen/narration/README.md`](../../karen/narration/README.md)
says so outright: *"thirty-odd lines across five acts will drift into three different men
otherwise"* — and [`voice.md`](./voice.md) records that the Suno attempts came back **echoing and
processed** because a "bare room tone" style line summoned a room. Suno is a **music** generator;
speech is a performance tendency it can be steered into, never a narration mode it guarantees.

That is a caution, not a veto — and the answer to it is **§4, the Voice**. One generation cannot
give you 21 consistent lines. A saved Voice can. **Do not skip §4.**

## 1. The casting — why there is no accent in this prompt

🔴 **Never write "Sheffield", "Yorkshire" or "northern accent" in the Style box.** Tested
2026-08-20 on this very story: a detailed Scouse spec — adenoidal Merseyside drawl, softened
consonants, rising line-ends — produced **no accent whatever**. Regional accent is
*describable, not summonable*.

🔑 **Nationality rides on the genre tag, and the genre tag carries a whole performer.** Camping
stripped its accent words and lost `UK grime influence` in the same edit — and both men came back
**American**. Then `UK grime` fixed the nationality and immediately miscast them as young MCs.

**So we cast a tradition, not a demographic.** The starter map in `suno-voices.md` names the pool
for exactly this man:

| Character | Pool that casts him | Not |
|---|---|---|
| Weathered working-class British bloke, 40s–60s | **British post-punk spoken word**; British performance poet | grime, drill, road rap — young MC by default |

### Where the two references go

### Round log — three cuts, and what each one proved

| Round | Pool | Pitch word | Result |
|---|---|---|---|
| 1 | `British post-punk spoken word` | **deep** gravelly, smoke-worn | 🔴 **too low** |
| 2 | `BBC English, after-dinner speaker` | **light** dry mid-range, thin | 🔴 **too gentle**, and posh with it |
| 3 | `Northern English post-punk spoken word, Britpop snarl` | chesty mid-range, grain, sandy rasp | 🔴 **not enough gravel, and it grew a band** |
| 4 | `Northern English post-punk spoken word, a cappella` | worn, rasping, gravel and old smoke, **chesty** | 🔴 **flat, too deep, strange** — three separate votes for monotone |
| 5 | `Sheffield art-pop spoken word, British punk poetry` | worn mid range, grain and rasp | — superseded by Jack's pick before testing |
| 6 | `Northern English punk poetry, Salford spoken word` (candidate A) | nasal, pinched, reedy | — superseded by Jack's pick before testing |
| 7 | `Madchester spoken vocal, Manchester spoken word` (candidate D) | ragged mid range, nicotine-worn, slurred | — superseded by Jack's pick before testing |
| 8 | `Northern English storytelling, British spoken-word monologue` (candidate E) | warm ragged mid range | — superseded by Jack's pick before testing |
| **9 — current** | **`Northern English spoken word, British kitchen-sink realism`** (candidate F) | **plain, hard, weathered mid range with grit** | ⬜ untested |

🔑 **What round 2 got wrong, and it is the lesson worth keeping: it moved two variables at once.**
The pool was never the fault — the *pitch word* was. Swapping the pool out as well threw away the
working-class northern casting along with the depth, which is why "too low" became "too gentle and
posh" in one step. This is `session-method.md`'s rule in miniature: **change one axis, listen,
change the next.**

🔑 **The distinction round 3 turns on: gravel is TEXTURE, depth is PITCH.** They are two of the
four axes Suno actually renders, and round 2 banned both when only one was the problem. `gravelly`
and `rasp` are therefore **back in the Style box**, while `deep voice, low voice, bass voice,
baritone, booming, sub bass` **stay banned**. A mid-range voice with grain in it is exactly the O2
register — the gravel never came from the depth.

### Round 4 — the two faults, diagnosed

**Fault 1: it grew instruments.** Not a weak Exclude box — **the Style box was asking for them.**

- 🔑 **`Britpop snarl` is a band genre.** So is post-punk. A genre word votes on the arrangement as
  hard as it votes on the voice, and `Britpop` summons a guitar band by definition. The Exclude box
  was fighting one of the strongest words in the prompt and losing. **Britpop is gone**; the
  `spoken word` qualifier on the surviving pool word is what pulls it toward a poet rather than a band.
- 🔑 **`one held quiet drone and distant room tone` was an instrument call.** The repo rule is
  blunt: **naming an instrument puts it in bar one, and the fix is to delete the mention rather
  than describe a quiet version.** I described a quiet version. It is deleted — `dead silence
  behind it` names no instrument at all.
- ⚠️ **`drone` and `room tone` were also in My Taste**, which is global and *"should carry only what
  plays from bar one"*. That was a standing request for a bed on every generation. Gone.
- `documentary narration` dropped too — it invites an underscore.
- `a cappella` is now in the Style box **twice**, at the front and the back. It is the **positive**
  form of "no instruments", which is where a positive belongs; the negations went to the Exclude box.

**Fault 2: not enough gravel.** The prompt was diluting itself.

- 🔑 **Short prompt or the voice loses.** Suno spreads its attention across everything named, so the
  fix is **deleting what the pool already gives free**, not adding more adjectives. Gone: two of the
  three `British`s, `hard flat vowels and clipped consonants` (the northern pool supplies those),
  `behind the beat`, `the music never winks`. The Style box went **105 words → 78**, and every word
  cut was one that was competing with the voice.
- **The texture clause is front-loaded and thickened** — `worn rasping… all grain and gravel and old
  smoke` now sits immediately after the pool word, because a term being ignored gets moved to the
  very start.

🟢 **And the safety net, if instruments still appear:** it does not sink the take. **Three dots →
Get stems → advanced split → keep the vocal stem** (§5). The narration was always going to be
delivered as a stem, so a bed you did not want is an inconvenience, not a failed generation.

### Round 5 — the word that was causing "flat"

🔑 **`flat` was doing two jobs, and Suno picked the wrong one.**
[`../narration-brief.md`](../narration-brief.md) sets the baseline as `{FLAT}` — meaning **deadpan
in attitude**. Rounds 1–4 translated that literally, and the Style box ended up voting for
**monotone in pitch** three separate times: `talking flat`, `landing dead level`, `never lifting`.
That is a pitch instruction, and Suno obeyed it. Hence *flat, too deep and strange* — a monotone
low read is exactly what those words describe.

**The replacement vocabulary carries the attitude with no pitch meaning attached:** `deadpan`,
`unimpressed`, `arch`, `throwing every line away`, `matter-of-fact`, `letting the sarcasm sit`.
**The word `flat` does not appear in the Style box again**, and `monotone, robotic, machine voice,
text to speech` join the Exclude box. `chesty` goes too — it reads as depth.

### Six northern voices worth aiming at

Not a list of names — **a list of performance traditions**, because that is the only casting lever
Suno has. *"A pool is a person"*: accent, age, class and region arrive as one package, so choosing
the tradition chooses the man. Names stay in this table and never go in a box.

| # | The archetype | What it sounds like | Pool phrase for the Style box | Why / risk |
|---|---|---|---|---|
| **A** | **The Salford punk poet** — the Bard of Salford, the Fall | Wired, nasal, adenoidal, fast, a *"Salford sneer"*. Mid-to-high, **never deep** | `Northern English punk poetry, Salford spoken word` | 🟢 Structurally cannot go deep or bland. 🔴 May be too manic for a narrator who is meant to be certain and unhurried |
| **B** | **The Sheffield art-pop narrator** — the bookish Britpop frontman | Dry, arch, conspiratorial, leaning right into the mic. Half-spoken, knowing, faintly camp menace. Mid-range | `Sheffield art-pop spoken word, British punk poetry` | 🥇 **The pick.** Sheffield is literally the O2 voice's own city, and *arch and knowing* is the BadCode narrator exactly. 🔴 Watch for melodic drift — keep the sung bans hard |
| **C** | **The minimal electronic rant** — the Nottingham spoken-word duo | Hard, unimpressed, spat, working-class fury delivered completely deadpan over almost nothing | `British minimal electronic spoken rant, post-punk rant` | 🥈 **Fixes the band problem structurally** — this genre's own arrangement is a bare loop, so it does not fight `a cappella`. 🔴 Angrier than the narrator should be |
| **D** | **The Madchester slur** — the baggy frontman | Slurred, menacing, funny, thrown away, ragged mid-range | `Madchester spoken vocal` | 🟢 Genuinely funny and off-hand. 🔴 `baggy` is a **band** genre — it will bring instruments straight back |
| **E** | **The working men's club compère** — northern stand-up storytelling | Warm, conversational, builds, relishes a word, talks *to* you | `northern English stand-up storytelling, working men's club compère` | 🟢 The warmest and most human option. 🔴 A comedy pool walks into the satire trap — novelty arrangements, winking music |
| **F** | **The kitchen-sink noir narrator** | Worn, grim, plain, unhurried | `British kitchen-sink drama narration, northern noir` | 🟢 Moody and serious. 🔴 `drama`/`noir` invite a film score, which is the instrument fault again |

**Recommendation: B, with A's punk-poetry phrase alongside it.** B supplies the arch, knowing,
close-mic register the film's narrator actually is; A's phrase is a **guard rail against depth and
blandness** — no punk-poetry pool has ever produced a BBC continuity announcer. C is the fallback
if instruments keep coming back, because it is the only one whose native arrangement is already
almost nothing.

### Round 6 — candidate A, the Salford punk poet

**Jack's pick.** Its structural advantage is that it **cannot go deep**: the pool's canonical
performers sit high in the nose, so the fault that killed rounds 1 and 4 has no way back in. The
articulation words are the repo's own recommended vocabulary — *nasal, pinched, over-enunciated* —
rather than feelings, which average into nothing.

⚠️ **The one real tension, and the thing to listen for.** This tradition's native delivery is
**fast** — machine-gun, rhyme-driven, breathless. The narrator in
[`../narration-brief.md`](../narration-brief.md) is **unhurried and certain**. The pool and the
brief disagree about pace.

**The fix is that pace is its own axis.** Delivery mode is one of the four things Suno renders
independently of the pool, so the pool supplies the sneer and the pitch while the delivery clause
governs the speed: *"Unhurried and certain — he takes his time and is in no rush at all."*
`fast delivery, rapid fire, breathless, hurried, frantic, manic` are in the Exclude box behind it.

**If it comes back gabbling, that clause lost.** Do not rewrite the whole prompt — front-load the
pace clause instead, ahead of the voice description, because a term being ignored gets moved to
the very start.

🔧 **Also changed this round: the lyric cues.** Every `| flat |` became `| deadpan |`. That is the
round-5 fault fixed at its second site — the cue box was still casting a monotone in every
section while the Style box had stopped. Same word, same bug.

### Round 7 — candidate D, the Madchester slur

**Jack's pick, and the cues moved with it.** Jack's note is correct and the repo backs it: the
lyric box is not inert. It is the **only section-scoped box we have**, every arrangement win in
the Camping sheet came through a cue and every accidental instrumental gap came from one. **So a
new pool gets new cues in the same edit** — leaving `deadpan` alone while the pool changed would
have left the old casting running underneath the new one.

**Cues this round:** `[spoken word speech talking | deadpan, matter-of-fact]`, fixed and repeated
identically in every section — **one label, never reworded**, because varied wording reads as a
new character. `slurred` is the single word that carries D into the sections; the chunk-5 crack
becomes `slurred, warmer, quieter` so the character survives its one warm beat.

**What D gets right that A could not.** A's tradition is natively **fast** and had to be fought.
D's is natively **unhurried and behind the beat** — the pool and
[`../narration-brief.md`](../narration-brief.md) finally agree about pace, so `lagging just behind
the beat` reinforces the pool instead of fighting it. That is one fewer clause competing for
attention.

🔴 **The known risk, handled up front: `Madchester` is a band genre.** This is precisely what
regrew the instruments in round 4, so three defences are stacked:
1. **`spoken vocal` qualifies it immediately**, the same way `spoken word` pulled post-punk toward
   a poet rather than a band.
2. **`Manchester spoken word` sits beside it** as a second, voice-only pool word — diluting the
   band vote while keeping the region.
3. **The genre's actual signature instruments are named in the Exclude box** — `baggy, indie
   dance, funk guitar, wah guitar, loose live drums, tambourine, congas, bongos, shaker, four to
   the floor, groove, jam`. Banning *behaviours and specific instruments* beats banning a category.

⚠️ **D's real cost, stated plainly: intelligibility.** Slurred, swallowed consonants are the
character — and this is a **narration** track where the words carry the entire story. `but every
word still lands` is in the Style box as the guard. **Judge every take on whether you can hear the
words, before you judge whether you like the voice.** If the character and the clarity cannot both
be had, clarity wins and D is the wrong pool.

### 🔎 An untested hypothesis worth knowing about — the all-parentheses script

Our lyrics are **100% parenthesised**, per the spoken-word recipe in `suno-tag-mechanics.md`, where
parentheses invert from the backing-vocal slot into an anchoring device for narration.

But `suno-voices.md` Thread 4 §1 found the opposite in a different context: **a section of nothing
but parenthesised lines has no lead line to answer, so the lead slot gets filled line by line and
the voice ping-pongs *inside* the section.** That finding came from a two-hander, and the
spoken-word exception is stated explicitly — so the recipe should still hold for one narrator.

**But it is a live candidate for the "strange" in round 6's result.** The test, if a take's voice
changes between lines *within* one chunk: **strip the parentheses from one chunk and rely on the
bracket cue alone.** One variable, one generation, and it settles which finding governs here.
Write the answer back into `docs/suno-gpt/`, either way.

### Round 8 — candidate E, the northern storyteller

**Jack's pick — built the long way round, on purpose.**

🔴 **The comedy noun is not going in the box, and that is the whole design of this round.** E was
listed as *"working men's club compère / northern stand-up storytelling"*, but the satire trap in
`suno-prompt` is explicit and expensively learned: **naming a thing puts it in the prompt however
the rest of the sentence qualifies it.** `Register: dark satire played completely straight` still
produced comic music, because `satire` is a comedy noun. `stand-up`, `comedian`, `comedy club` and
`compère` are all comedy nouns, and on the Karen track *"comedic deadpan"* summoned kazoos and
vaudeville — **less funny, not more.** `club` carries its own second risk: club music.

🔑 **So E's warmth arrives through the monologue tradition instead of the stand-up tradition.**
`Northern English storytelling, British spoken-word monologue` casts the same man — warm, direct,
confiding, timing-driven, talking *to* one person — with no comedy noun anywhere and the delivery
kept inside the spoken-word family, which has been the safest territory in this whole sheet.

🔑 **A stale ban was about to strangle this round, and it was found by looking twice.** Rounds 3–4
banned `gentle, soft vocal, softly spoken, mellow, soothing, tender, warm ballad vocal` to fix
*"too gentle"*. E's defining quality is **warmth**. Those bans would have silently removed the one
thing this candidate exists for — and a stale ban is invisible: the generation just comes back
without the thing you asked for, and it reads as the Style box being ignored. **They are lifted.**
The bans that fight *blandness* rather than warmth stay: `calm narration, polite, posh, plummy, RP,
BBC newsreader, after-dinner speaker, languid, wistful`.

⚠️ **The register tension, stated plainly.** [`../narration-brief.md`](../narration-brief.md) sets
a **`{FLAT}` baseline with exactly one `{WARM}` crack, spent in scene 11 and worth more than every
joke in the script.** E's native register is warm throughout. **If the whole read is warm, the
crack has nothing to land against and the film loses its best beat.**

**The resolution is a single clause: `Warm in the throat and cold in the attitude.`** Warmth is a
property of the instrument; the contempt is a property of the performance. The cue word follows
the same split — **`confiding`** carries E through every section, and **`warmer`** is still spent
once, in chunk 5 only.

### Round 9 — candidate F, the kitchen-sink narrator

**Two changes, and the slider one matters more than the pool one.**

🔴 **`noir` is not in the prompt.** It was in the menu description, but *noir* is a **film** word and
it invites a score — the same failure family as round 4's instruments. `British kitchen-sink
realism` carries the identical bleak-northern flavour from a **drama** tradition rather than a
cinematic one, and `crime drama score, thriller score, suspense, tension strings, brooding score,
orchestral score` are now named in the Exclude box behind it.

**`Northern English spoken word` is front-loaded ahead of it** as the actual pool word. Kitchen-sink
realism was heard as *dialogue*, not as song, so it may not select a vocalist pool at all — and a
pool word that does not fire drops you back to the default, which is American. The spoken-word
anchor is the insurance.

🔧 **The anti-gentle bans are back.** They were lifted in round 8 because E's whole point was
warmth; F's is hardness, so `gentle, soft vocal, softly spoken, mellow, soothing` return. **Bans get
re-decided per candidate, never accumulated** — that is the discipline the round-8 catch was about,
running in the other direction.

⚠️ **Words deliberately avoided in this prompt: `level`, `even`, `flat`.** All three are natural
English for what F is, and all three are the round-5 monotone bug wearing a different hat.
`matter-of-fact`, `steady` and `unadorned` say the same thing with no pitch instruction attached.

### The northern accent — the only lever that exists

🔴 **A bare accent adjective does nothing.** Tested on this story, 2026-08-20: a detailed Scouse
spec produced **no accent whatever**. Writing `northern English accent` in the Style box buys you
nothing at all.

🔑 **So the region rides on the genre phrase instead.** `Northern English post-punk spoken word` is
a *pool-selecting* term, and a pool is a person — accent, age, class and region arrive as one
package. The tradition's canonical performers are northern working-class men in exactly this age
band, which is why `suno-voices.md` names this pool for *"weathered working-class British bloke,
40s–60s"*. **That phrase is doing all the accent work in this prompt; do not delete it.**

`Britpop snarl` sits beside it from the same map — it adds edge without adding depth, which is the
precise gap round 2 opened.

### Where the two references go now

| Reference | What we take | How it enters the prompt |
| --- | --- | --- |
| The O2 voiceover | The **texture, class and region** — grain, rasp, worn northern weight | `Northern English post-punk spoken word` (the pool) + `real grain and a sandy rasp, worn and smoky` (texture axis) |
| The gravel-baritone comedic lead | The **attitude and the timing** — deadpan, cocky, underplayed | `deadpan and cocky` + `landing dead level and falling away at the end rather than lifting` (delivery axis) |

**Neither name goes anywhere near a box.** Both are steered through the four axes Suno renders —
**pitch, texture, delivery mode, room** — which is the practical takeaway of the whole Camping
voice thread.

✅ **The round-2 craft flag is resolved.** `BBC English` / `after-dinner speaker` were casting the
*establishment* register — Tarquin's register — which risked the Lee/Coe test in
[`../narration-brief.md`](../narration-brief.md) and the working-class reader in
[`the-reader.md`](../../../marketing/the-reader.md). Both words are now in the **Exclude** box, and
the narrator is cast working-class again.

## 2. Suno prompt — paste all four, in this order, every round

**Never trust what a box already contains.** "Reuse Prompt" silently carries old lyrics forward,
and a stale Lyrics box is inaudible as such — it just sounds like the Style box is being ignored.
That cost the Karen track four rounds.

### My Taste

Swap this in for the session and **restore your usual profile afterwards** — My Taste biases every
generation, cannot be turned off, and a stale profile is a competing identity fighting this one.

```
Vocals: one male voice only, plain and hard and weathered, mid range with grit in it, hard northern consonants and open vowels, speaking rather than singing, matter-of-fact and unadorned, steady and unhurried, giving nothing away. Northern English spoken-word delivery, close and dry right up on the microphone. Production: a cappella throughout. Voice alone, dead silence behind it. Register: grim, bitter and certain, played completely straight.
```

### Style

```
Northern English spoken word, British kitchen-sink realism, a cappella. British. A plain, hard, weathered mid-range male voice with grit in it, hard northern consonants and open vowels, close and dry right up on the microphone. Matter-of-fact and unadorned — stating what happened and moving on, steady and unhurried, giving nothing away. Grim, bitter and certain, played completely straight; whatever is funny lives in the words alone. A cappella throughout, voice alone, dead silence behind it.
```

### Exclude Styles

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, chanting, autotune, harmonies, backing vocals, choir, female vocal, American accent, American vocal, transatlantic, southern drawl, US rap, grime MC, UK drill, road rap, young MC, rapping, trap, hip hop, ragga MC, toasting, Jamaican accent, piano, glockenspiel, strings, violins, brass band, guitar, acoustic guitar, drums, drum kit, breakbeat, amen break, bassline, melody, chord progression, music hall, vaudeville, pantomime, ragtime, honky-tonk, jaunty, playful, whimsical, bouncy, comedic, novelty, parody, uplifting, epic trailer music, cinematic swell, reverb, echo, telephone voice, lo-fi, distorted vocal, double time, tempo change, band, rock band, guitar band, live band, indie rock, post-punk band, full arrangement, instrumental intro, instrumental outro, instrumental break, underscore, film score, ambient pad, synth pad, drone, room tone, atmosphere, sound design, deep voice, low voice, bass voice, baritone, booming, boomy, sub bass, monotone, robotic, machine voice, text to speech, vocoder, computerised, fast delivery, rapid fire, breathless, hurried, frantic, manic, shouting, screaming, yelling, punk rock, punk band, hardcore punk, baggy, indie dance, madchester band, funk guitar, wah guitar, dance beat, loose live drums, tambourine, congas, bongos, shaker, four to the floor, groove, jam, movie trailer voice, epic narrator, crime drama score, thriller score, suspense, tension strings, brooding score, orchestral score, gentle, soft vocal, softly spoken, mellow, soothing, breathy, whispered, calm narration, polite, posh, plummy, RP, received pronunciation, BBC newsreader, after-dinner speaker, languid, wistful, stand-up comedy, comedy club, comedian, sitcom, laugh track, audience laughter, applause, live audience, cabaret, variety show, circus, panto, kazoo, slide whistle, honky tonk piano, oompah, tuba, banjo, whistling
```

### Lyrics — all five chunks

> 🔴 **These five chunks are NOT ready to paste — see [§7](#7-⚠️-what-is-still-open-before-the-full-run).**
> Audited 2026-09-01: **445 words against a 250–320 budget**, scene 12 missing entirely, and three
> of the brief's load-bearing jobs unwritten. The Style / Exclude / My Taste boxes above are round-9
> ready; **the script is the open item.**

The recipe is a **redundant word-cluster in the bracket, the line in parentheses beneath it**.
Parentheses are normally the backing-vocal slot; **for spoken word they are an anchoring device
for the primary line**, and that inversion is the mechanism.

**Generate chunk 1 first and lock the Voice (§4) before running 2–5.** Run them without it and
you get five different men. The chunks are written out here so the script is settled — not so
they can all be fired off in one sitting.

**Cues are deliberately short.** The Style box is global and already carries the voice, the drone
and the register; the lyric cue is the **only section-scoped box we have**, so it holds only what
is true of *this* section. Camping's own verse cue went 1,010 characters → 311 with nothing lost.

**One fixed label, repeated identically.** `[spoken word speech talking]` never varies — varied
wording reads as a new character. Only the delivery word after the pipe moves, and it moves
exactly once in a meaningful way: the single `{WARM}` crack in chunk 5, which
[`../narration-brief.md`](../narration-brief.md) says is worth more than every joke in the script
and must not be spent before scene 11.

#### Chunk 1 — 2008

```lyrics
[spoken word speech talking | deadpan, matter-of-fact | a cappella, voice alone from bar one]
(Two thousand and eight. Meet Tarquin, a star trader on the NatWest floor, who bets heavily on leveraged E.T.F.s.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(Pain infliction usually looks this banal. Nice tie, though.)

[spoken word speech talking | deadpan, matter-of-fact]
(Meet Bob. Standard middle-manager bloke. Decides to get away with his wife Jo, away from the financial stress of it all.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(Can you blame him, really.)
```

#### Chunk 2 — 2026

```lyrics
[spoken word speech talking | deadpan, matter-of-fact | a cappella, voice alone from bar one]
(Twenty twenty-six. Tarquin runs the country's biggest private equity firm, the one that buys up social housing.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(The bastard looks very pleased with himself. He ditched the tie, at least.)

[spoken word speech talking | deadpan, matter-of-fact]
(Driving home from work, he spots this lot and thinks. Interest rates up one percent next week. You chaps are going to have a few more mates soon. Cannot wait for my bonus.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(It is a tad chilly, though...)

[spoken word speech talking | deadpan, matter-of-fact]
(Bob spends his days in this oh-so-luxury tent, taking any charitable beer donations he can get his hands on.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(I don't know what's worse. The fact that his cause is not supported much. Or the fact that his donors judge the mere fact that he's an I.P.A. man. Fuck me.)
```

#### Chunk 3 — therapy

```lyrics
[spoken word speech talking | deadpan, matter-of-fact | a cappella, voice alone from bar one]
(Tarquin sought professional help, since he felt a feeling for the first time since he smoked the devil's lettuce at uni.)

[spoken word speech talking | deadpan, matter-of-fact]
(The therapist tries to explain that empathy for the homeless does not warrant an emergency appointment. It does not sink in.)

[spoken word speech talking | deadpan, matter-of-fact]
(He eventually just says there is no helping him, and he needs the strongest psychedelic known to man to fix his car crash of a personality.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(Forgive the pun.)

[spoken word speech talking | deadpan, matter-of-fact]
(Tarquin agrees that he needs to explore himself more, so he heads off to get supplies before his trip to Wales.)
```

#### Chunk 4 — the car park

```lyrics
[spoken word speech talking | deadpan, matter-of-fact | a cappella, voice alone from bar one]
(Parks how he usually does. Bob is none too pleased.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit.)

[spoken word speech talking | deadpan, matter-of-fact]
(Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them. Four by fours are the most common vehicle in this car park.)

[spoken word speech talking | deadpan, matter-of-fact]
(Tarquin locks on to a background figure. Not so much a wrestle with his conscience, but maybe a small acknowledgement that it is there... It being Bob.)
```

#### Chunk 5 — Wales, and the newspaper

```lyrics
[spoken word speech talking | deadpan, matter-of-fact | a cappella, voice alone from bar one]
(He heads off to Wales for this spiritual retreat. Before taking the ayawaska, they insist on meditation. Tarquin has never sat on the floor before.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(Safe to say it has kicked in...)

[spoken word speech talking | deadpan, matter-of-fact]
(He's had enough, bless him. Time for bed.)

[spoken word speech talking | deadpan, matter-of-fact]
(Awoken by the sound of thunder, with his heart in his throat. Stepping out of his tent, he spots an old newspaper.)

[spoken word speech talking | matter-of-fact, warmer, quieter]
(Warming his hands on the fire, Bob tries to calm him down, and tells him to pay attention to the date of the newspaper. Twenty thirty-one.)

[spoken word speech talking | deadpan, matter-of-fact, thrown away]
(He takes the news well. Excuse the pun.)
```

### What was changed from Jack's script, and why

Every one of these is a **synthesis** change — the words a listener hears are unchanged.

| Change | Why |
|---|---|
| `2008` → `Two thousand and eight`, `2026` → `Twenty twenty-six`, `2031` → `Twenty thirty-one` | Bare digits get read as digits, or sung |
| 🔴 **Chunk 5's reveal year `2026` → `Twenty thirty-one`** | **Not a synthesis change — a canon bug.** The line named the same year as scene 4, so the reveal revealed nothing. [`../year-device.md`](../year-device.md) §*Ruled by Jack, 2026-08-30*: the on-screen clock is a **two-instance** device (2008 on `1a`, 2026 on `4a`) and **the third date is spoken, not shown** — *"the newspaper stops being a clock and goes back to being a prop."* This line **is** the film's third date. It is now the only place 2031 exists |
| `ETFs` → `E.T.F.s`, `IPA` → `I.P.A.`, `1%` → `one percent`, `4x4's` → `four by fours` | Raw abbreviations and symbols are mispronounced. Normalise before synthesis, never after |
| `Ayahuasca` → `ayawaska` | Respell for **sound**, not for the dictionary. **No hyphens** — an in-word hyphen stretches the note, so a hyphenated or foreign word renders slow by default |
| `devils lettice` → `devil's lettuce` | The phrase is *devil's lettuce*; the original is a typo |
| `em` → `him` | Dialect elision is a mispronunciation risk for no gain — the flatness carries the register |
| Semicolons → full stops (×3) | Semicolons produce muddy pacing |
| `Can you blame em, really?` → `...really.` | 🔑 **A question mark lifts the pitch, which sounds eager. A full stop keeps it flat, which is the joke.** Same ruling as Karen's `Who knew.` |
| `I don't know what's worse:` → `...worse.` | A colon does the same lift as a question mark |
| `these lot` → `this lot` | Agreement |
| `Uh,` dropped before `Nice tie though` | A filled pause is the first thing a music model swallows or sings. The comma before `though` does the same work reliably |
| Ellipses **kept**, in three places | A trailing pause *with weight* — a real control, and each one is placed where a joke needs air before it lands |

## 3. Settings

| Control | Set to | Why |
|---|---|---|
| **Model** | **v5.5** | Cue-heavy tracks live or die on bracket obedience, and v4.5 shreds structure where v5.5 obeys it. This is nothing but bracket cues |
| **Mode** | **Advanced** | Subject matter belongs in the Lyrics box; the whole Style budget goes on sound |
| **Style influence** | **85** while auditioning · drop to **75** if a take comes back uncanny | 🔴 **Corrected 2026-08-31.** `suno-controls-and-workflows.md` §1: **100 "follows literally; can over-tighten and *degrade* adherence"**, and *"the single most-repeated numeric tip in the whole corpus is 75, not 100."* 85 is the compromise, because high style influence rewards specific vocabulary and these boxes are very specific — but 100 is a live suspect for the "strange" takes |
| **Weirdness** | **60** while auditioning · **0–25** once the Voice is saved | 🔴 **Corrected 2026-08-31.** On Suno's scale **50 is already "effectively no randomness"** and **60–65 is the creative sweet spot**. 10 and 30 both sit in the dead zone *below* where randomness begins — so the "pair at 10 and 30" was not a pair at all, and neither value can produce an interesting voice. **Consistency across 21 lines comes from the saved Voice (§4), not from a low weirdness**, which frees the audition to run where interesting lives |
| **Audio influence** | **40–60**, once a Voice is attached (§4) | The band where a Voice bites hardest. Above 70 only if it drifts; above 60 gives artifacts on a custom model |

## 4. 🔑 The Voice — this is the whole job, not an optional extra

One generation gives you a voice. **Twenty-one lines need the same voice**, and no prompt achieves
that. The mechanism does.

🔴 **If you already saved a Voice from the too-low take, do not attach it.** A Voice carries the
timbre — it will drag the new prompt straight back down. Start §4 again from a fresh chunk-1
generation on the revised boxes.

1. **Generate chunk 1** on the boxes above. Re-roll rather than rewrite — meta-tags are
   probabilistic, and an identical prompt often lands on the second attempt.
2. **Audition on the driest line in the film**, the same one used for every other engine:
   *"I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit."*
   Flat and amused wins. Any lift, any grandeur, any sense it knows it's funny is wrong.
3. **Save the winner as a Voice.** Song's three-dot menu → **Remix → Voice**. **Select the
   sub-region** where the voice is right — fifteen clean seconds beat sixty contaminated ones —
   name it, and **delete the attached style prompt** so the voice is not welded to this genre.
4. **Attach it to every later chunk.** Advanced → **+ on Voice** → choose it. Audio influence
   40–60.
5. **Expect a consistent, unique voice — not a specific one.** Suno generalises toward a nearby
   archetype. That is fine here: we need *one man*, repeatedly, more than we need a particular man.

**Optional, and this is the locked-in version:** the *brainwashing stack* — a **Custom Model** and
a **Voice** trained on the same clip, used together. Minimum 6 files; upload the same file six or
more times to build a model of one voice. Reserve it for when the voice is right and the drift is
the only remaining problem.

## 5. Getting the voice OUT — narration is a stem, not a track

🔴 **Never generate the narration and the score together.** [`../../karen/narration/README.md`](../../karen/narration/README.md)
makes this a standing rule: split them so a bad music bar does not cost you a good read.

Suno cannot make silence — it is a music generator, so it will put *something* under the voice.
The prompt above reduces that to a held drone. Then:

**Three dots → Get stems → advanced split → keep the vocal stem.** That is the file Premiere gets.
The drone stem is a free ambient bed if it happens to be any good; throw it away if not.

## 6. The failure signs, and what each one means

| What you hear | Cause | Fix |
|---|---|---|
| **He starts singing** | 🔑 A melodic layer crept in under the voice. On this very story a glockenspiel and French horn turned a four-round-hardened spoken-word rant into **singing**, with no vocal clause changed | **Look at the accompaniment before you touch a vocal clause.** Check the Exclude box still holds `melody, chord progression, piano, glockenspiel` |
| **He's American** | The UK genre word lost its weight, or got edited out | Front-load `British post-punk spoken word` and let `British` repeat after it. Nationality is a **genre** lever, never an adjective |
| **He's a young MC** | A grime/drill/road-rap word is pulling | Those pools cast a young performer by default. Strip them; the tradition word does the casting |
| **The tag is ignored and he sings anyway** | Meta-tags are probabilistic | **Re-roll before rewriting.** Then escalate the cluster: `[spoken word]` → `[spoken word speech]` → `[spoken word speech talking]`. Redundancy is a real technique here, not a smell |
| **It's gone comic or music-hall** | 🔑 **British + spoken word + a bouncy pitched instrument is music hall** — with no comedy word anywhere in the prompt | Diagnose by asking what changed in the *arrangement*, not by rereading mood words. Keep every pitched instrument out |
| **It's echoing and processed** | A room or FX word in the Style box | The word `reverb` and friends are already in the excludes. `close and dry` is the positive form |
| **Something you asked for is simply missing** | A **stale ban** — invisible, and it reads as the Style box being ignored | Grep the Exclude box **and** My Taste for the thing, its **category**, and any whole-palette adjective |

## 7. ⚠️ What is still open before the full run

**Round 9's boxes are ready to paste. The Lyrics box is not** — audited against
[`../narration-brief.md`](../narration-brief.md) on 2026-09-01, it is over budget, missing the
ending, and missing three of the brief's load-bearing jobs. Fix the script before spending
generations, or you pay for takes of lines that get cut.

### The length, measured

| Chunk | Lines | Words | At 155 wpm |
|---|---|---|---|
| 1 — 2008 | 4 | 54 | ~21s |
| 2 — 2026 | 6 | 119 | ~46s |
| 3 — therapy | 5 | 92 | ~36s |
| 4 — the car park | 4 | 84 | ~33s |
| 5 — Wales | 6 | 96 | ~37s |
| **Total** | **25** | **445** | **~172s** |

🔴 **155 wpm is the ceiling, and the brief says an authoritative voice sits *under* it.** At a
narrator's actual ~135 wpm this script is **~198 seconds of speech**, before the three canon-wordless
stretches and before a single pause for a joke to land. Against the brief's **250–320 words** it is
**39% over**, and against [`../edit-plan.md`](../edit-plan.md)'s 150s working shape it is a different
film's length. **Roughly 130 words have to go** — and the gaps below want some of that budget back,
so the real cut is deeper than 130.

### Coverage against the brief — scene by scene

| Scene | Brief's job | Script |
|---|---|---|
| 1 · 2008 Tarquin | Trading floor reads as **cause**, not backdrop | 🟡 *"bets heavily on leveraged E.T.F.s"* only **implies** it. The brief's load-bearing function — *"He was the reason 2008 hit"* — is not carried by any line |
| 2 · 2008 Bob | Deliberately unremarkable | ✅ |
| 3 · the crash | 🔇 **Silent** | ✅ correctly absent |
| 4 · 2026, the Shard | **Eighteen years**; name the mechanism — housing bought and **left empty because asset inflation pays better than rent**; sarcasm **paired with the empty flats** | 🔴 Names the firm and the buying. **The mechanism, the emptiness and the eighteen years are all absent**, and *"looks very pleased with himself"* is sarcasm pinned to nothing on screen — the brief's own *Sarcasm with no consequence* trap. **Scene 11 depends on this beat**, so this is the most expensive gap in the sheet |
| 5 · the drive | Tarquin's own contempt, then silence, then the **cold** U-turn — *his car heater broke last week* | 🟡 The contempt line is ✅. The U-turn is *"It is a tad chilly, though..."* — a narrator's aside, not the cold-empathy mechanism the brief specifies |
| 6 · outside Waitrose | 🔑 **ignore / politely reject / engage** — *"have a guess which one's rarest"*, the line aimed at the audience's own behaviour | 🔴 Absent. The IPA joke occupies the slot instead — and ⚠️ it aims the contempt at **the people who donate**, which is worth re-testing against [`the-reader.md`](../../../marketing/the-reader.md) before it survives the cut |
| 7 · therapy | Play for comedy, get out, punchline survives | ✅ the strongest chunk in the script |
| 8 · the standoff | One beat each; the scene-5 crack **slaps shut** | ✅ |
| 9 · the trip | 🔴 No mention of AI | ✅ clean |
| 10 · the wake-up | The **narrator** does the freak-out and **still thinks it's the drugs** — the one time the audience is ahead of him | 🟡 *"Awoken by the sound of thunder..."* narrates the picture instead. The dramatic irony is not written |
| 11 · the newspaper | *"It's not the drugs."* · 🔑 **the last newspaper ever printed** · Bob's *where the f\*\*\* have you been* · ⬅️ **the reach-back to scene 4** | 🟡 The date lands (✅ now 2031) and Bob calms him. **All four of the named jobs are missing** — and without the reach-back the brief says *"the film becomes an anti-AI film by accident, which is the one thing it is not"* |
| 12 · the fire | The apology the man way; the closing line; **the `12d` tilt ends exactly on the last word** | 🔴 **The scene does not exist in the script.** It ends on *"He takes the news well. Excuse the pun."* — **there is currently no last word for the tilt to be cut to**, and the brief says to write that word first |

### ⚠️ One trap the whole script trips

**Cadence monotony.** Twenty-five lines, every one a short-to-medium declarative. The brief's fix is
named and unused: **one long cosmic sentence among the short ones.** There is nowhere in this script
the narrator's voice opens out, and on a spoken-word generation that is also a *musical* problem —
25 identical phrase-lengths is the audio equivalent of `edit-plan.md`'s 34 identical 8-second clips.

### 🧪 The content filter — still untested, and now cheaper to test

The script carries *"Fuck me"*, *"no one gives a shit"* and *"wank tanks"*; the scene-11 gap wants
Bob's *"where the f\*\*\* have you been"* on top. Suno's filter is real and unpredictable.

🔑 **Test all of them in one throwaway generation, and make it chunk 4** — it already contains
*"gives a shit"* and *"wank tanks"*, it is the **audition line's own chunk** (§4 step 2), and it is
short. One generation settles the filter **and** casts round 9's voice. If it trips, respell for
**sound**, never for the dictionary — and note that a respelling that changes the vowel changes the
read, so `shit` → `shite` is a **performance** decision, not a workaround.

### The order to do this in

1. **Cut and rebuild the script** to 250–320 words against the table above. ⬅️ *this is the gate — everything below is wasted until it is done*
2. **Write the last word first** (scene 12), because the `12d` tilt is timed to it.
3. **Run chunk 4 once** on the round-9 boxes — filter test and voice audition in one generation.
4. **Save the Voice** (§4), then run chunks 1–3 and 5 with it attached.
5. **Stems out** (§5), and hand Premiere the vocal stem.
