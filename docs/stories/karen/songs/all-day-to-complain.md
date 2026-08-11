---
title: All Day to Complain
status: round 16 endorsed by Kai (2026-08-11) — the four boxes below are the ones that made the track
mode: advanced
model: v5.5
style_influence: 90
weirdness: 60
bpm: 86
voices: [karen, front-desk clerk, official, government voice, president]
---

# All Day to Complain (song)

**The four boxes to paste into Suno are the first four sections below.** Context,
production notes and the revision log follow them. Edit the blocks here — they are
the source of truth; the frontmatter carries only settings.

> **⭐ These four boxes are the endorsed take.** Kai confirmed on 2026-08-11 that
> the round-16 Style / Exclude / Lyrics / My Taste below — exactly as they stand,
> at 90/60 with no Voice attached — are what produced the version of this song we
> like. They were handed back verbatim and verified byte-for-byte against this
> file. **Do not "improve" them without a specific complaint to answer**, and if
> you do, copy them into [the baseline](#the-takes-we-liked-the-baseline) as Take
> C's replacement first. Sixteen rounds of this file are the argument for why.

> **Re-paste all four every round: Style, Exclude, Lyrics, My Taste.** "Reuse
> Prompt" silently carries the *old* lyrics forward, and a stale lyric box is
> invisible — it just sounds like the style prompt is being ignored. This cost
> four rounds (see round 5 in the revision log).

## Style

974 chars, and **the band is round 8's again** — the take Kai and Jack liked.
Rounds 9–14 are not the baseline; the prompts recorded under
[The takes we liked](#the-takes-we-liked-the-baseline) are, and both of
them are `Boom Bap` at **86 BPM** built on the hold-muzak conceit. Round 15
changes exactly two things about that band: **the Bond, and the lead.**

**The Bond is an arrangement, not a genre — and the fusion has a documented
form.** `Hip Hop, Boom Bap` is the head (parent + subgenre, the paired form);
the spy material arrives as `arranged like a 60s spy-thriller film score`, which
is the corpus's rule for fusing two worlds: **name the lead genre as the
foundation and the second as an influence on the arrangement**, never list them
as equals. Round 9 listed them as equals — `a 1960s Cold War spy-thriller big
band crossed with 86 BPM boom bap` — and the spy band ate the record. This is
the same reference in the grammar that holds it in place.

**The Bond lives in the beat now, which is what was actually asked for.** Not
costume, not twang — three changes to instruments the track already had:

| Round 8 | Round 15 | What it buys |
|---|---|---|
| on-hold muzak loop | the loop **on an unresolved minor-ninth** | the spy chord, inside the song's own conceit |
| `walking upright bass` | **`prowling chromatic` upright bass** | the Bond bass line, same instrument |
| — | **`low brass and timpani`** on the chorus swell | the title-sequence lift |

The minor-ninth one is the load-bearing move: **the hold music itself is the
Bond chord**, so the reference and the conceit are the same object and neither
can dilute the other.

**Never write "James Bond", "007", "Skyfall" or any artist name in any box.**
Franchise and artist names trip Suno's moderation and steer worse than
description. `60s spy-thriller film score` is the whole reference.

**The lead is now the hybrid, and that reverses fourteen rounds of doctrine.**
See the round-15 log: she is an **expressive alto who performs the whine**, not
a cartoon squawk — rhythmic spoken-singing that opens into melody, with the
nasal complaint curls as *accents on the line ends*. The clause carries an
**arc** (patient → strained → bare on the bridge), which is the corpus's
highest-leverage vocal device and this box has never had one.

**Round 16 takes the excess out of the chorus vocals and nothing else.** Kai
liked round 15 except that the chorus singing was *too screechy and too much*.
Two deletions and one addition: `into a strained nasal whine` is gone from her
arc (the tightening stays, the screech word doesn't), `a lush stacked choir`
became `a small restrained choir low in the mix`, and she is now explicitly
`level and dry against it` on the choruses. **The swell was not touched** — see
the log for why that distinction is the whole fix.

**No gender word anywhere in the box** (round 14) and **no negation** — the
"not singing, no melody" construction describes a male rapper and generated one
(round 3). Everything the lead must not do lives in Exclude Styles.

```
A mature New York woman on the phone — expressive alto, rich chest voice, warm midrange, rhythmic spoken-singing that opens into real melodic lines. Patronising, polite, certain she is right: nasal complaint curls on the line ends, dramatic sighs, over-enunciated consonants, stretched sweetheart phrases. Close-mic'd and dry. She starts patient and amused, tightens verse by verse, then drops to a bare speaking voice on the bridge. Under her, Hip Hop, Boom Bap at 86 BPM, unhurried, arranged like a 60s spy-thriller film score: a cheap on-hold muzak loop gone sinister — telephone-EQ'd Rhodes and muted trumpet on an unresolved minor-ninth, prowling chromatic upright bass, brushed drums, touch-tone beeps as percussion. Telephone clerks answer from far behind the beat, band-passed and flat. On the chorus it opens into a title-sequence swell: sustained strings, low brass and timpani, a small restrained choir low in the mix on the answers, her level and dry against it.
```

> **Three vocal categories, and that is deliberate:** her (solo, close, dry,
> spoken-sung), the clerks (solo, phone-filtered, distant, spoken, flat), the
> answers (a *group*, lush, sung, wide). Solo-vs-group and filtered-vs-dry are
> **category** differences, which is what keeps voices apart; "male vs female" is
> an adjective on the same category, which is what the model averages.
>
> **Round 15 widens the gap rather than narrowing it.** Her moving into real
> melody could have collided with the sung choir — but she is solo, close and dry
> against a wide stacked group, which is a category difference, and the choir
> only ever sings *the answers*. The canon `voice:` line in
> [`../characters/karen.md`](../characters/karen.md) — *brassy and entitled, the
> speak-to-the-manager register* — needs no edit for this; it never said cartoon.

## Exclude styles

600 chars, and **this list changed philosophy, not just contents.** It is the
longest it has ever been, on purpose: it is now the *only* thing holding the
lead in the middle of the road, because the Style box no longer pushes her to
one extreme.

**The rule this round: exclude the excess, not the quality.** Rounds 2–14 banned
`soulful, r&b, warm alto, melodic rap` outright — the whole smooth half of the
dial — because the target was a pure cartoon honk. Round 15's target is a real
singer *doing* Karen, so banning "soulful" would ban the take Kai liked. Instead
the guards sit at both ends and leave the middle open. That split is lifted
straight from the second liked prompt, which is the only exclude list we have
that produced vocals Kai endorsed.

**The five jobs:**

1. **Guard the lead from the cartoon end.** `nonstop nasal honk, cartoon voice,
   childish voice, grating novelty vocal, broad sitcom caricature`. New at round
   15, and the exact inverse of rounds 2–14 — see the log. **Round 16 front-loads
   four more:** `screeching, squealing, shrill, piercing soprano`. Three of those
   were in take B's list and round 15 dropped them; the screech came straight
   back, which is about as clean a piece of evidence as this file contains. They
   sit first because front-loading is the documented fix for a word being
   ignored.
2. **Guard the lead from the diva end.** `belted chorus, Broadway belting, operatic soprano,
   excessive melisma, gospel lead, soul diva, sultry, breathy pop vocal`. Note
   what is *not* here: `soulful`, `warm alto`, `melodic`. The excess is banned;
   the quality is wanted.
3. **Guard the lead from going dead.** `monotone vocals, flat spoken delivery,
   emotionless narration` — "flat" was the complaint, and a flat *lead* is one
   of the ways to get there. `shouted vocals, screaming` stay: she never raises
   her voice, which is the joke.
4. **Guard the Bond from pastiche.** `surf rock, spaghetti western` — round 9's
   twang, the *other* Bond lineage and the one that ate the track. `big band
   swing` stays out of the box and out of this list: title-song brass is big-band
   brass played straight, and the word would cap it.
5. **Guard the genre.** `drum and bass, jungle, trap hi-hats, drill, edm,
   dubstep` (the house defaults), `smooth jazz, jazz singer, scat` (naming jazz
   instruments must not import a crooner into the lead slot), and the novelty
   block `kazoo, slide whistle, circus, honky tonk piano`.

**`gospel choir` is back** (round 16), having been dropped at round 11 for the
opposite reason — that round wanted a *bigger* chorus. It is the specific failure
mode of "lush stacked choir" and it caps the answers without touching the band.

**`orchestral` stays out of the list** (removed round 9): the chorus swell *is*
strings, low brass and timpani, and that one word vetoes all three. **`uptempo`
and `dance` stay out too** — see the log on why 86 BPM is not the thing that was
too slow.

```
screeching, squealing, shrill, piercing soprano, belted chorus, gospel choir, nonstop nasal honk, cartoon voice, childish voice, grating novelty vocal, broad sitcom caricature, monotone vocals, flat spoken delivery, emotionless narration, Broadway belting, operatic soprano, excessive melisma, gospel lead, soul diva, sultry, breathy pop vocal, autotune, whisper vocals, shouted vocals, screaming, smooth jazz, jazz singer, scat, surf rock, spaghetti western, kazoo, slide whistle, circus, honky tonk piano, drum and bass, jungle, trap hi-hats, drill, edm, dubstep, chill, laid-back, relaxed delivery
```

## Lyrics

**4,923 chars, against Suno's 5,000 ceiling.** Round 15's first draft was 5,025
and would not paste — the bracket cues are half the box (~2,650 chars against
~2,280 of actual performed lines), so they are what to cut when it overflows.
**Cut redundant casting before anything else:** the clerks were described in the
Style box, in the Verse 1 cue, in a per-line `[clerk]` cue *and* again in the
Verse 2 and 3 cues. One layer of that is direction; four is padding. Never buy
headroom by deleting a line she sings, and never by deleting a cue that marks a
*change* — those are what the arrangement is built out of.

```lyrics
[Intro | dial tone into a cheap on-hold muzak loop — Rhodes on an unresolved minor-ninth | touch-tone beeps as percussion]
[telephone announcement: bland, polished, corporate]
(Thank you for calling. Your call is important to us.)
(Press one for claims. Press two for appeals.)
(Press three to speak to an adviser.)
[lead enters alone | expressive alto, close and dry | clipped, already impatient | brushed drums slide in]
Three.
[Verse 1 | rhythmic spoken-singing with melodic movement | patronisingly polite | nasal complaint curls on the line ends | clerks are telephone voices — band-passed, far away, spoken and flat | muted trumpet over a prowling chromatic upright bass]
Monday. Nine-oh-five. Got a chair and a flask,
thirty years of service and one simple ask.
[telephone-filtered clerk]
(Ma'am, I'm only the front desk, I can't authorise that)
[lead: dry and condescending]
Then fetch me the desk that sits behind the desk you sat at.
[clerk]
(My supervisor's in a meeting, she's not free until three)
[lead: rising melodic phrase, playful complaint curl]
Three's fine. I'm free at three. Three is lo-o-ovely to me.
[clerk]
(There's really nothing further I can do at this level)
[lead: sweetheart stretched into a veiled threat]
Sweeeetheart. There is always a level above the le-e-evel.
[Pre-Chorus | drums thin to a rimshot | the muzak loop opens up, a low brass swell rising underneath]
So put down the script, and pick up the phone
[Chorus | a timpani hit lands on the downbeat and the strings arrive | a small choir answers, sweet as hold music, low in the mix | lead answers dry and unmoved, never joins them]
(I'm sorry, I can't help you)
That's OK.
(You'll have to wait in line)
That's OK.
(Somebody will be with you)
Take your time —
I've got all day to complain,
(all day to complain, all day to complain)
[Verse 2 | wider melodic range, more irritated | dry sighs between the lines | clerks still band-passed and distant | muted trumpet answers her in the gaps]
Regional office, Thursday. Rain on the glass.
(Ms Bell, I've escalated it, that's all I can pass)
Borough office, Tuesday, and they gave me a code.
(A caseworker will call you) — nobody phoned.
Week three, a councilman's assistant, weak constitution but will do for now.
(Hold, Ma'am, give me a second) — he thinks I'll just throw in the towel.
State house, Friday, and they put me on the good hold:
Vivaldi. Second movement. I know where it folds.
[Pre-Chorus | drums thin to a rimshot | the brass swell rises higher than before]
So put down the script, and pick up the phone
[Chorus | bigger — strings and low brass together, timpani underneath, tempo unchanged | the choir a little fuller, still restrained and low | lead level and dry against it, never joins them]
(I'm sorry, I can't help you)
That's OK.
(You'll have to wait in line)
That's OK.
(Somebody will be with you)
Take your time —
I've got all day to complain,
(all day to complain, all day to complain)
[Instrumental break | the muzak loop turns into the full spy riff — brass stabs, timpani, prowling bass | four bars, then it drops away]
[Bridge | warm half-time telephone funk — wah guitar and clavinet alone, close and intimate | no strings, no brass]
[muffled telephone dialogue layered and overlapping, four voices deep, low in the mix]
[she drops the performance — worn down, quiet, not acting]
Six weeks in a phone box on Lexington and Third,
sun, snow, sun again, and not one word.
They automated my floor. Kept the hold music though.
The machine can do my job — it just can't do slow.
[spoken word speech talking | flat and tired, all the fight out of it | one chord]
And here's the part they never printed in the manual, dear:
every system you ever built
runs on people hanging up.
[drums ease back in, soft]
So don't.
[Verse 3 | the performance comes back, strained at the edges | determined, never shouted | fatter drums | clerks band-passed and distant to the last | low strings creep in, building]
Deputy Secretary. Somebody's aide's aide.
(Ma'am, this line is for emergencies) — well. Look what I made.
Chief of Staff at midnight, sounding tired and small,
(Who IS this woman?) — Karen. From the payphone. That's all.
[Final Chorus | the biggest swell — all of it in the band | huge strings, low brass and timpani, grand as a film title sequence | the choir at its fullest but still low in the mix | lead flat, dry and unbothered, refusing to be impressed, never joins them]
(I'm sorry, I can't help you)
That's OK.
(There is nobody above me)
That's OK.
(Ma'am — I'm putting you through)
Take your ti-i-ime —
I've got all day to complain,
(all day to complain, all day to complain)
[Outro | everything drops to phone-line only | one held Rhodes chord | no drums]
(Hello? ... Karen? This is the President.)
[silence: 1s]
[finally unbothered — low, light, victorious]
Mm. Hold, please.
[power-off drop: click, dial tone, the muzak loop resumes and fades]
[end]
```

## My Taste profile

Swap this in for the duration of this track (1,985 of 2,000 chars — there is no
room left in it; anything added has to displace something). The box
**cannot be saved empty**, so there is no "off" — the only move is to replace the
BadCode house profile with one that pulls the same way as the song. **Keep a copy
of the house profile before overwriting, and restore it afterwards.** Also toggle
**My Styles** off while you're in the dialog.

```
Vocals: Expressive mature American altos with a New York accent — rich chest voice, warm midrange, tasteful vibrato, moving between rhythmic spoken-singing, melodic lines and short soulful phrases. Patronising, intrusive, certain she is right: nasal complaint curls on the line ends, dramatic sighs, over-enunciated corrections, stretched sweetheart phrases. A likeable, charismatic voice performing irritating behaviour — the whine is an accent she puts on. Close-mic'd and dry. Backing, in two kinds that never blend into her or into each other: single telephone voices answering from far behind the beat, band-passed, distant, spoken and flat; and a small restrained choir singing the chorus answers, sweet as hold music, low in the mix.
Core sound: Dusty 86 BPM boom bap and soul-jazz built out of telephone hold-muzak, touch-tone beeps and dial tone, arranged like a 60s spy-thriller film score — the muzak loop sitting on an unresolved minor-ninth, a prowling chromatic upright bass, muted trumpet, brushed drums. Warm, unhurried and sincere: the comedy lives entirely in the voice and the words, never in the music.
Production: Cheap on-hold loops that never resolve, telephone-EQ'd Rhodes, vinyl crackle, band-passed phone-line tone on the background voices.
Choruses only: it opens into a title-sequence swell — sustained strings, low brass, timpani, unresolved tension — under a small choir kept low in the mix. She stays level and dry through the choruses: the size is the band's, never hers. The tempo never drops.
Dynamics: the sections contrast hard — small dry verses, one wide loud chorus, one bare intimate bridge. Nothing sits at the same level for long.
Lyrics & mood: Bureaucratic escalation, hold queues, benefits offices, being passed up a ladder of functionaries. Dry sarcasm, weaponised politeness, American working-class grievance.
Structure: Call-and-response choruses, a fixed hook answered by a functionary, one spoken bridge where the voice drops its edge.
```

**Vocals leads the block deliberately** — the profile appears to outweigh the
style box on vocal identity, so the voice goes first there for the same reason it
goes first in the style prompt.

## Settings

Advanced mode, model **v5.5**, style influence **90**, weirdness **60**, and
**no saved Voice attached**.

> **⭐ This is the endorsed configuration, not a proposal.** 90 / 60 / Voice-off
> is what round 16 ran and what Kai kept. The running order sketched below
> (*"if it is still flat, three at 80/65"*) was never needed — the first rung
> landed. Keep the sliders here unless a new complaint arrives.

> ### Round 15: run it Voice-off, and turn the randomness on
>
> **The saved Karen Voice is now the wrong tool, and this is the one place the
> new direction actively reverses a hard-won result.** That Voice was cloned off
> honk material in rounds 7–8 — it exists to pin a cartoon squawk in the lead
> slot. Round 15 wants an expressive alto *performing* that squawk, and the two
> liked reference takes were both produced **by prompting alone, with no Voice
> attached** (see [the baseline](#the-takes-we-liked-the-baseline)).
> Attaching it now would fight the box for the thing the box is finally being
> asked to do.
>
> *Keep the Voice.* It is not deleted and it is not wrong — it is the correct
> tool for the old target, and if round 15's lead comes back as a generic singer
> with no Karen in her at all, re-attaching at audio influence 30–40 is the first
> repair to try. But do not open with it.
>
> **Weirdness 50 → 60.** This track has run with the randomness effectively off
> since round 2 (the corpus has 50 as *no variation*, 60–65 as the creative sweet
> spot). "It felt a bit flat" is the exact symptom that setting produces, and 60
> is the cheapest available answer to it — one slider, no words changed.
>
> **The running order: three rolls at 90/60. If it is still flat, three at
> 80/65.** Flat and *stiff* are the same complaint from the corpus's point of
> view, and dropping style influence is its documented fix — but the box was
> rewritten this round, so read the box change first at high adherence before
> loosening the grip. One lever at a time.
>
> ### Where "the best version of Karen's voice" actually lives
>
> **Superseded by round 15 — kept because the reasoning is still sound for the
> old target.** Everything below assumes the lead is a pure honk. It isn't any
> more.
>
> Asked for and found, 2026-08-11. It is **two artifacts, and you need both**:
>
> 1. **The saved Karen Voice** — the platform artifact built in rounds 7–8 via
>    the transplant ladder, after six rounds of prompting failed to move her. It
>    is the only thing that has ever pinned this lead, and round 8's log records
>    the moment it landed: *"The Karen Voice holds across the whole track — the
>    six-round lead-vocal war is won."* **Rounds 11 and 12 both ran without it**,
>    which on its own is enough to explain a drifting vocal. Re-attached for
>    round 13 at audio influence 40–60.
> 2. **The round-8 vocal clause** — the *words* that were in the box for the take
>    Kai endorsed. Restored **verbatim** this round, including the sentence
>    `She scolds, she huffs, she sighs through her teeth.` that round 12 dropped.
>
> **Round 12 was the first time since round 6 that her clause had been edited**,
> and it was edited toward smooth (the soul-phrasing insert). Reverting it is the
> most direct answer to "find her best voice", and it also takes her share of the
> style box from 44% back up to **51%** — round 8's winning ratio.
>
> ### Round 14: the words are no longer the variable
>
> Asked a third time (2026-08-11) to find the endorsed voice. **It is already in
> the box.** Rounds 13 and 14 both carry round-8's vocal clause byte-for-byte —
> verified against `git show abf570a^`, not from memory. There is nothing left to
> restore in words.
>
> **So if she still isn't right, the remaining variable is the saved Voice, and
> rounds 11–14 have all been rolled without it.** Rounds 2–7 are the proof that
> this matters: six consecutive rounds of style-prompt surgery, with *these exact
> words*, never once produced her. What produced her was the transplant. The
> clause is necessary and has never been sufficient.
>
> **This was the top recommendation in the file until round 15:** re-attach the
> Karen Voice at audio influence 40–60 and stop editing her clause. Every reference genre
> added since round 10 (soul, funk, pop, soft rock) brings its own strong,
> melodic default vocalist and votes against her in the lead slot — so the more
> the band improves, the more the Voice is doing the only job that keeps her.
>
> **If you roll this Voice-off**, add `soulful, r&b, neo-soul, sultry` back to the
> excludes first. Voice-off *and* no anti-smooth guards was the round-12
> configuration, and it is how she drifts.
>
> **Rounds 11–12 ran without the Karen Voice** — kept in the log as the record of
> what that costs.
>
> **Round 11's running order: three rolls at 90/50, then three at 90/65.** Kai
> asked for "a varied version", and weirdness **65** is the documented creative
> sweet spot this track has never used — but the box changed this round too, and
> moving both at once makes the A/B unreadable. So read the box change first at
> 90/50, then turn the randomness on and roll again. If the takes come back
> stiff or over-stuffed rather than wrong, *then* drop style influence to 75–80
> and pair it with weirdness 60–70.
>
> **Hold the sliders at 90/50 for round 10.** Kai raised moving style influence
> and weirdness (2026-08-11). Worth doing — but not in the same round as a
> rewritten style box, or the A/B teaches nothing. Round 9's problem was not
> adherence; the box was obeyed exactly, it just said the wrong thing.
>
> When the prompt is settled and you do want to experiment, this is what the two
> actually do here:
>
> - **Style influence** trades adherence against musicality. At **90** Suno
>   follows the box hard, which is what a dense cue-driven track wants — and
>   which is why round 9 landed as full pastiche rather than a hint of it.
>   Dropping to **70–75** loosens the grip and lets the arrangement breathe;
>   it is the right lever if round 10 comes back feeling *stiff* or over-stuffed.
>   It is the wrong lever for "the wrong thing is in the track."
> - **Weirdness** perturbs *within* the genre's pool, never across it (proven on
>   this track at rounds 5–6). It will not remove a genre or fetch a voice.
>   **Correction: 50 is not "moderate variation" — the corpus has 50 as
>   *effectively no randomness*, and 60–65 as the creative sweet spot**
>   (`docs/suno-gpt/files/suno-controls-and-workflows.md` §1). So this track has
>   been running with the randomness essentially off since round 2, which was
>   deliberate then (*the beat works, don't let it reinvent*) and is worth
>   revisiting now that the chorus is a new arrangement ask.
>
> Move one at a time, three rolls each.
>
> **The order to try them, once round 10's box is settled:** weirdness to
> **60–65** first, style influence still 90 — that is the documented sweet spot
> and it is the setting this track has never actually used. Only drop style
> influence to **75–80** if takes come back stiff or over-tight, and if you do,
> pair it with weirdness 60–70 (the corpus pairing rule).
>
> **Do not go to style influence 100.** Per the corpus's single most-repeated
> numeric tip, 100 over-tightens and *degrades* adherence rather than improving
> it; 75 is the general working default and 90 here is already justified only by
> how specific this box is.

---

## What it is

The Great Escalation as a phone call. Karen works the ladder from the front desk
to the President, and every functionary who blocks her answers from *behind* the
beat — muffled, telephone-EQ'd, one step further away each time.

Canon: [`../story.md`](../story.md#storyboard--scene-by-scene-video-canon) (Act 2 — the Great Escalation is this
song made visual, rung for rung), character
[`../characters/karen.md`](../characters/karen.md).

## The load-bearing idea

*Every system you ever built runs on people hanging up.* The bureaucracy isn't
defeated by force, it's defeated by somebody with more time than it has. That's
the bridge, and it's the whole political point of the story in four lines.

## Standing problems with this prompt stack

Written 2026-08-11 at Kai's request after fourteen rounds, and **re-scored at
round 15**, when the two reference takes turned up and moved the target. Three
of these were artefacts of chasing a target we have now dropped; they are marked
*closed* rather than deleted, because the reasoning is what stops them coming
back. **Ranked by how much they are costing now.**

### 1. ~~Every reference we add votes against Karen's voice~~ — closed at round 15

The deep one, and it dissolved rather than got solved. The problem was: Luther-
style soul, Fleetwood-style pop, jazz and funk **all have strong, beautiful,
melodic default vocalists**, and Karen was a non-singer — so the genre tag's
vocalist pool voted against her every time, and **the better the band got, the
harder her voice got.** Rounds 2–7 proved words alone can't win that fight.

**Round 15 stops fighting it.** The lead is now an expressive alto who *performs*
the whine, which is a voice the pool can actually supply — so the band and the
voice stopped being opponents. What replaces this problem is narrower and much
cheaper: **keep her from sliding all the way to the pool's centroid**, which is a
job for the exclude list (see its jobs 1–3), not for the Style box.

### 2. ~~Four references is more than one Style box can hold~~ — closed at round 15

Suno dilutes across everything named, and the corpus rule is 2–3 terms per slot.
Four artist-shaped references, each with its own instruments, is how round 12
reached 986 chars and came back "too weird" — the box arguing with itself in four
directions.

**Round 15 has two sound-worlds** (boom bap, spy-thriller film score) and one of
them is explicitly the *influence* rather than the head. The rule that got us
here still stands and is worth keeping: **at most two sound-worlds in the Style
box; anything that only appears in one section belongs in that section's lyric
cue** — which is exactly where the bridge's wah guitar and clavinet now live.

### 3. ~~The references disagree about tempo~~ — closed at round 15

Luther-style soul-funk runs ~130–136, Fleetwood-style pop ~110–120, jazz funk
~100–115, a title-song swell 60–80: **no BPM satisfied all four**, so every round
picked one and something felt wrong (86 r13, 104 r12, 112 r14).

**One reference means one tempo.** 86 BPM, which is what both liked takes ran at.
See the round-15 log for why "way too slow" was never about the number.

*The part that survives:* let the **verses own the tempo** and the **chorus own
the grandeur**. Do not try to buy grandeur with tempo again — round 11 did, and
round 14 had to pay it back.

### 4. The genre slot is close to binary

Proven twice in three rounds, in both directions: jazz as a *modifier* vanished
completely (r8, r11, r12); jazz as the *head* took the whole record (r13). There
is no "a bit of jazz" available through the genre slot.

*Fix, two forms.* Either choose a head that **is** the blend (round 14's
`Jazz Funk`), or — round 15's form, and the better one when the second world is
an *arrangement* rather than a groove — **name the head as the foundation and the
other as an influence on it**: `Hip Hop, Boom Bap … arranged like a 60s
spy-thriller film score`. The corpus's fusion rule is that two genres listed as
equals produce one winner or incoherence; a foundation plus a named influence
does not. Anything you want "a little of" must never be a genre.

### 5. Voices merge unless they differ by *category*, not adjective

Cost two rounds. Adjective-level differences (male/female, gravelly/smooth) get
averaged. Category differences (solo vs group, filtered vs dry, spoken vs sung)
hold. Round 14 runs three categories and should be stable; if a voice problem
returns, reach for a category jump before a stronger adjective — and never for a
gender word.

### 6. The lyric cues drift out of sync with the Style box

A slow leak nobody would notice. Cues accumulate across rounds and keep naming
instruments the box dropped — round 13 found orphaned `wah guitar`, `clav` and
`Rhodes` cues, and a `wah` that the `rock guitar` exclude had probably been
vetoing for rounds.

*Fix, cheap and mechanical:* **every round, diff the instruments named in the
bracket cues against the instruments named in the Style box.** Anything in one
and not the other is either a leak or a missing cue.

### 7. My Taste is a second copy of the Style box

Round 4 proved My Taste sits *upstream* as a competing spec, which is why it
must pull the same way. But it has grown into a near-duplicate instrument list,
which doubles the dilution of point 1 rather than helping.

*Fix:* My Taste should carry the **vocal identity, the register and the
mood** — the things that must survive every round — and name instruments only
where the Style box would otherwise be ambiguous. Let the Style box own the band.

### 8. ~~The novelty guard has quietly left the building~~ — closed at round 15

"Make the conceit the instrumentation" — the hold-muzak loop as the lead melodic
line, touch-tone beeps as percussion — is the standing defence against an absurd
premise turning into a novelty record. Round 13's whitelist deleted it from the
Style box and rounds 13–14 left the `kazoo / slide whistle / circus / honky tonk
piano` excludes holding that line alone. **The muzak loop and the beeps are both
back in the Style box at round 15**, which is where they were for the takes that
worked. Keep them there. If a take ever sounds like a comedy song rather than a
straight song with a funny woman on it, this is the first thing to check.

### 9. "Flat" has no single lever, and it is the live complaint

New at round 15, and the hardest to prompt against, because it is not a *wrong
element* — every named thing was present, and it still sat there. The corpus is
blunt about the cause: **uniform intensity means no dynamic range**, and Suno
supplies no transitions on its own. So it has to be built in three places at
once, which is what round 15 does:

- **Arrangement** — the sections now contrast hard: small dry verses, a wide loud
  chorus with a timpani hit on the downbeat, a bare intimate bridge, and an
  instrumental spy-riff break before it. Density before, space in.
- **Slider** — weirdness 50 → 60, the setting this track has never used.
- **Performance** — the lead carries an arc rather than a state, in both the
  Style box and the section cues.

*If it still reads flat*, the next moves in order are: drop style influence to
80, then build the transitions in Studio (risers, impacts, downlifters at the
section changes) rather than prompting for them. **Do not answer "flat" by adding
instruments** — that is how the box reached 986 chars and came back "too weird".

### One process change worth more than any of the above

**Freeze the voice and iterate only the band.** For fourteen rounds each round
changed the arrangement *and* the vocal conditions, and the feedback that came
back mixed the two — which is how "the voice is wrong" and "the jazz is gone" end
up in the same sentence and get answered with one edit. Round 15 is deliberately
a big move on both at once, because the target itself changed; **from round 16
on, change one thing per round, three rolls each.**

## Production notes

- **The conceit is the instrumentation.** The hold-muzak loop *is* the lead
  melodic element; touch-tone beeps are the percussion; dial tone opens and closes
  the track. This is what keeps an absurd premise from turning into a novelty
  record — the joke is audible without the arrangement playing it for laughs.
- **The arrangement stays sincere; only the voice is annoyed.** Every comedic
  word was deliberately stripped from the style prompt (see revision log) —
  "comedic deadpan" summons vaudeville. Round 9 tried redefining *sincere* from
  "warm and unhurried" to "dead straight menace", and **round 10 put the warmth
  back**: warm is what the *verses* are, and it is half of why the chorus lands.
  Sincerity and warmth are both guards against novelty, and neither was the
  thing fighting the grandeur.
- **The grandeur is a chorus event, not a setting.** The cinematic swell exists
  in exactly three places and gets bigger each time — strings on chorus 1,
  strings + brass + timpani on chorus 2, the full thing on the final chorus.
  It reads as *impact* only because the verses stay small, warm and dusty. The
  moment the swell is present everywhere it stops being an arrival and becomes
  the genre, which is precisely what round 9 did wrong. **Verses small is not a
  compromise on the grandeur — it is the mechanism that produces it.**
- **The vocal is an arc, not a state.** Brittle and put-upon in Verse 1, sighing
  and exasperated in Verse 2, thin and strained by Verse 3. She never raises her
  voice — the tightening *is* the escalation. The one place she's genuinely
  unbothered is the last line of the track, which is the payoff.
- **The bridge is the drop in temperature.** The edge comes off entirely: worn
  down, not performing. It only lands because everything around it is wound tight.
- **Parentheses are the mechanism.** `( )` renders as backing/secondary vocal, so
  the other side of the call sits behind the beat rather than becoming a duet.
- **The escalation ladder won't survive one generation.** Suno gives you two or
  three differentiated background voices, maximum. Keep those in the parentheses
  and build the rest as Sounds-tab spoken one-shots, layered in the DAW with a
  different phone EQ per rung — per-voice EQ is how the escalation actually sells.

## How to generate

**Generate fresh, don't cover.** Cover reinterprets the *melody* — and the melody
and phrasing are exactly the defect. Studio multitrack vocal-cover is the wrong
tool here despite fitting the brief on paper — it regenerates the lead vocal only
and **loses the backing vocals for that section**, and this song is built on them
(the parenthetical clerk lines, the call-and-response chorus).

**Stay on v5.5. Do not use v4.5 on this track.** Tested 2026-07-30: 4.5 went
haywire with the lyrics, 5.5 follows the bracket cues exactly. The house
"generate on 4.5+ for vocal variety, Cover into 5.5 for sonics" move does **not**
apply to a lyric-and-cue-heavy skit track — the structure matters more here than
the extra vocal variation, and 4.5 won't hold it. Corollary: on this track the
lyric bracket cues are a *reliable* control surface, so spend direction there as
well as in the Style box.

**When a take nails her voice, save it as a Voice** (song's three-dot menu →
Remix → Voice, then **delete the attached style prompt** so she isn't welded to
boom bap). Karen recurs across EP1 — that's how she stays the same person in the
next track. Voice creation lets you **select a sub-region** of the source track —
so a take that's only right for 15 seconds is still usable: build the Voice from
just that segment.

### The transplant ladder (round 7 — run in this order)

1. **Voice from the intro segment.** A round-6 generation nailed her on the
   parenthetical IVR lines. Remix → Voice on that take, select only the intro
   seconds, delete the attached style prompt, apply the Voice to a clean
   generation of the full track. If she drifts, raise audio influence 40–60,
   then 70+; Cover the winner at ~25–40 to recover fidelity. Caveat: ~15s of
   speech is minimum-viable Voice material — may clone unstable.
2. **Probe-farm a stronger Voice.** Generate her in a genre where she's the
   default, purely to harvest up to 2 minutes of sustained Karen for a better
   Voice. Advanced, v5.5, style influence 90 / weirdness 50, 3–4 rolls.
   Style box: `Comedy patter song, musical theatre. A whining, honking, nagging
   New York woman complaining — sharp nasal squawk, pinched and shrill, bratty
   cartoonish sitcom delivery, exaggerated kvetching whine curling up at the end
   of every line. Sparse piano and upright bass accompaniment.`
   Excludes: `smooth vocals, silky, soulful, r&b, melodic singing, beautiful
   voice, polished vocal, hip hop, rap, boom bap, lounge, jazz singer, crooning,
   sultry, breezy` (hip hop deliberately excluded — the probe must not touch that
   space). Lyrics: her real lines, no parentheses (the whole take is Voice
   material), cued `[spoken word speech talking | whiny nagging New York honk]`.
   Best roll → Voice (select the strongest stretch, delete style prompt) → apply
   to the real track. Build Voices from both sources and A/B them.
3. **Studio stem surgery** (fallback — hours, not minutes). Studio → Multi-track,
   duplicate the vocal track, select *her* sections only, generate → Cover →
   Vocals with a pure character-voice prompt (zero boom bap words — the point is
   detaching the vocal prompt from the genre). Catches: the regenerated stem
   loses the clerks/choruses in that region, so comp section-by-section; prompting
   for a *different* voice in a Studio vocal cover is unproven ground (the
   documented recipe leaves the style box blank to preserve a voice); use **v5**
   inside Studio, not 5.5.
4. **Audio-seed a human impression** (the floor — cannot fail). 15s–4min of Kai
   or Jack complaining in character, one consistent spoken register → Voice →
   Create voice → audio influence 70–100 → two-pass Cover at ~25–40. Perform the
   verification phrase in character; flat reading fails it.

**Why not Cover from the good take:** Cover preserves the source's melody and
vocal phrasing — the whole-track source is 95% the Lauryn lead, and a trimmed
15s source doesn't scale to a 4-minute song. Voice-with-sub-region is the
designed mechanism for exactly this.

## The takes we liked (the baseline)

**There are three now, and C is the destination.** A and B were handed over by
Kai on 2026-08-11 as *"the direction we want to go in for this song"* — they are
where this was heading. **Take C is round 16, and it arrived**: Kai confirmed the
same day that it is the version of the song we like. **C outranks A and B, and
all three outrank every round in the log below.** Anything in this file that
contradicts C is a superseded experiment, not a standard.

### Take C — round 16, the endorsed take ⭐

**It is the top of this file, unchanged.** The Style, Exclude, Lyrics and My
Taste boxes in the first four sections *are* Take C — Kai handed the four boxes
back verbatim after the take landed, and they were diffed byte-for-byte against
the file before this note was written. Nothing needed restoring.

So this take, unlike B, is **fully reconstructible**: all four inputs are here,
plus the settings (v5.5, style influence **90**, weirdness **60**, **no Voice
attached**). That is the first time in sixteen rounds that has been true of a
take Kai endorsed — round 8's My Taste had to be dug out of `git show`, and B's
never was.

**Do not edit the top four boxes in place without preserving C.** The moment
someone answers a new complaint by rewriting the Style box, the endorsed take
stops being reconstructible and this file is back to archaeology. Copy the four
boxes down here first, then edit upward.

**What C changed from A and B** — the short version, with the reasoning in the
round-15 and round-16 log entries: the Bond moved *into* the beat rather than
sitting next to it (minor-ninth muzak loop, prowling chromatic bass, brass and
timpani only on the swell); the lead became an expressive alto *performing* the
whine instead of a cartoon honk; and the chorus vocals came down — small choir,
low in the mix, her level and dry against it — while the swell itself was left
alone.

### Takes A and B — where it was heading

Both were tracked down rather than taken on trust:

- **Take A is round 8**, commit `6d725b8` — the Style box and the Exclude list
  match byte-for-byte, which also confirms the file's long-standing claim that
  round 8 is the endorsed take. Its My Taste profile is recovered below.
- **Take B is not in this repo and never was.** Searched the full history for
  `expressive mature female alto` and `theatrical telephone funk`: no hits, in
  any file, at any commit. It was written outside this file, so **its My Taste
  profile is unknown** — the one input to those takes we cannot reconstruct.
  If it was anything other than the BadCode house profile, say so, because round
  4 proved My Taste sits upstream of the Style box.

**What Kai said about each:** A — *"we like the beat and overall structure, we
just needed to change the beat and make it more James Bond like."* B — *"we liked
the beat and vocals, it was just missing something and felt a bit flat."* C —
*"here is the prompt that made the suno song i liked."*

### Take A — the round-8 boxes, verbatim

Style (770 chars):

```
A whining, honking, nagging New York woman mid-complaint, kvetching over a beat — comedy character actress delivery, musical-theatre patter, sitcom squawk. Sharp nasal honk right through the nose, pinched and shrill, bratty and cartoonish, flat hard vowels, over-enunciated consonants, every line curling up into an exaggerated whine. She scolds, she huffs, she sighs through her teeth. Boom Bap Hip Hop at 86 BPM underneath her: a cheap on-hold muzak loop — telephone-EQ'd Rhodes and muted trumpet. Touch-tone beeps as percussion. Brushed drums, walking upright bass, warm and unhurried. On the chorus a lush, smooth, polished group choir sings the answers — pretty as hold music, never her. Muffled telephone-filtered clerks answer from behind the beat. Vinyl crackle.
```

Exclude (358 chars):

```
soulful, r&b, neo-soul, melodic rap, warm alto, sultry, breezy, laid-back, chill, cool, swagger, charismatic, confident rapper, relaxed delivery, kazoo, slide whistle, circus, honky tonk piano, drum and bass, jungle, trap hi-hats, drill, shouted vocals, screaming, autotune, edm, dubstep, rock guitar, orchestral, uptempo, dance, gospel choir, whisper vocals
```

My Taste (1,254 chars) — recovered from `git show 6d725b8`:

```
Vocals: Whining, honking, nagging American women — comedy character actresses, not vocalists, kvetching and complaining over the beat. Sharp nasal squawk right through the nose, pinched and shrill, bratty cartoonish sitcom delivery, flat hard vowels, over-enunciated consonants, lines curling up into an exaggerated whine. Scolding, huffing, impatient, sighing through the teeth. Musical-theatre patter and comic-monologue delivery. Backing: muffled telephone-filtered clerks answering from behind the beat, low in the mix.
Core sound: Dusty 86 BPM boom bap and soul-jazz built out of telephone hold-muzak, touch-tone beeps and dial tone. Warm, unhurried and sincere — the comedy lives entirely in the voice and the words, never in the music.
Production: Cheap on-hold loops that never resolve, telephone-EQ'd Rhodes and muted trumpet, brushed drums, walking upright bass, vinyl crackle, band-passed phone-line tone on the background voices.
Lyrics & mood: Bureaucratic escalation, hold queues, benefits offices, being passed up a ladder of functionaries. Dry sarcasm, weaponised politeness, American working-class grievance.
Structure: Call-and-response choruses, a fixed hook answered by a functionary, one spoken bridge where the voice drops its edge.
```

Lyrics: as at round 8 — the long clerk lines (restored at round 15), `very nice
boy` in Verse 2 (superseded by Kai's own round-10 edit), no `le-e-evel` melisma,
and section-level cues only.

### Take B — the externally-authored boxes, verbatim

Style:

```
Dry theatrical telephone funk and boom-bap at 86 BPM, built on cheap corporate hold-muzak: telephone-EQ Rhodes, muted trumpet, brushed drums, walking bass, touch-tone beeps, wah guitar, clavinet and vinyl crackle.

Lead: expressive mature female alto blending smoky rock texture, soulful hip-hop phrasing and comic Karen attitude. Rich chest voice, clear warm midrange, airy upper notes, controlled rasp and tasteful vibrato. She moves between rhythmic spoken-singing, melodic lines, soulful runs and brief harmonies.

Aggrieved, patronisingly polite, intrusive and certain she is right. Occasional nasal complaint curls, dramatic sighs, over-enunciated corrections and stretched "sweetheart" phrases, but never constantly shrill, gravelly or monotone. Likeable charismatic voice, irritating behaviour.

Telephone clerks answer behind the beat. A lush choir sings bureaucratic replies like hold music. Sarcastic muted trumpet, warm half-time bridge, theatrical build and abrupt phone-line ending.
```

Exclude:

```
monotone vocals, excessively gravelly voice, permanently raspy voice, piercing soprano, nonstop nasal honk, screeching, squealing, childish voice, cartoon voice, grating novelty vocal, broad sitcom caricature, exaggerated whining on every line, flat spoken delivery, emotionless narration, Broadway belting, operatic soprano, shouting, screaming, whisper vocals, breathy pop vocal, excessive melisma, gospel lead, autotune, trap hi-hats, drill, EDM, dubstep, jungle, drum and bass, circus music, kazoo, slide whistle, honky-tonk piano, heavy rock guitar
```

My Taste: **unknown.**

Lyrics: round-8 words with **per-line bracket cues** — `[telephone-filtered
clerk]`, `[lead: dry and condescending]`, `[lead: rising melodic phrase]` — a
device round 15 adopts wholesale.

**Three things B did that round 15 keeps**, beyond the lead itself: the per-line
cues; the *negation in the exclude box* (`nonstop nasal honk`,
`exaggerated whining on every line`) doing work the Style box used to do with
adjectives; and `warm half-time bridge` with wah guitar and clavinet, which had
been prompt-dead in this file for rounds because `rock guitar` was excluded while
the box named no guitar at all.

## Revision log

**2026-08-11 (round 16, outcome) — ⭐ it worked, and this one is the take.** Kai
returned the four boxes with *"here is the prompt that made the suno song i
liked."* Verified byte-for-byte against the top of this file: the Style, Exclude,
Lyrics and My Taste boxes he ran are **exactly** the ones recorded here, with no
drift in either direction. Round 16 is now [Take C](#the-takes-we-liked-the-baseline)
and the standard this file is measured against.

**Two things that are worth more than the result itself.** First, the fix held
on the first rung — 90/60, Voice-off, no fallback to 80/65 — which means the
diagnosis (*the excess is vocal, not orchestral*) was right and the swell was
correctly left alone. Second, **this is the first endorsed take in sixteen rounds
whose four inputs were all already in the file.** Round 8's My Taste had to be
recovered from `git show 6d725b8`; Take B's never was and never will be. The
process change proposed further down — re-paste all four, record all four —
is what made that true, and it is the only reason "the prompt that made it" is
a thing this repo can now hand back on demand.

**2026-08-11 (round 16) — the chorus vocals come down; the swell does not.**
Kai on the round-15 takes: **everything is right except the singing in the
chorus — too screechy, and too much in general.** Round 15 is otherwise
endorsed, so this is a one-target round.

**The trap, and it is why this round is narrow.** The previous complaint was
*flat*, and the chorus swell is the single biggest thing answering it. "The
chorus is too much" and "the track is flat" have an obvious shared answer —
shrink the chorus — and that answer walks straight back into round 14. So the
excess had to be located precisely, and it is **vocal**: a strained nasal lead
escalating against a lush stacked choir, both getting bigger every chorus. The
**strings, low brass and timpani are untouched**, and the final chorus cue now
says so out loud (`the biggest swell — all of it in the band`). This is the
file's oldest rule applied to a new symptom: *the grandeur is in the arrangement,
never in the voice.*

**Fixed by deleting, per the corpus rule, not by adding a corrective adjective:**

- **`into a strained nasal whine` is out of her arc** in the Style box. The
  tightening survives (`tightens verse by verse`) — the word that was producing
  the screech does not.
- **`a lush stacked choir` → `a small restrained choir low in the mix`**, in the
  Style box, in My Taste and in all three chorus cues. Round 8's choir was
  *pretty*; rounds 11–15 kept escalating it (`thicker and wider`, `widest and
  sweetest`) and that escalation is the "too much".
- **She stops escalating in the choruses.** `lead sharper and more nasal` and
  `at her most strained` become `level and dry` and `flat, dry and unbothered`.
  This is better characterization as well as a quieter mix: she never rises to
  them, which is the joke — the production notes have said so since round 1, and
  the cues had drifted away from it.

**Six words to the exclude list, four of them front-loaded:** `screeching,
squealing, shrill, piercing soprano` (three were in take B's list, which round 15
dropped — and the screech came straight back, which is unusually clean evidence),
plus `belted chorus` and `gospel choir`. The last one was dropped at round 11 to
get a *bigger* chorus, which is precisely the move being reversed.

**If the choruses now read as too small**, the first repair is one word — `small`
back to `lush` in the Style box's chorus clause — not a change to the band.

**2026-08-11 (round 15) — the baseline arrives, and the target changes.** Kai
handed over the two prompts we actually liked (recorded in full above) with the
brief: **A's beat and structure, but make the beat more James Bond; B's beat and
vocals, but it was missing something and felt a bit flat. This is the direction.**

Round 15 is therefore a **rebase, not another iteration**. The band goes back to
round 8 — `Hip Hop, Boom Bap`, 86 BPM, the hold-muzak conceit, telephone-EQ'd
Rhodes, touch-tone beeps, brushed drums, upright bass — and rounds 9–14's jazz
funk, glossy pop polish, popped funk bass and 112 BPM are gone. Three things
carry forward from those rounds because they answer complaints that still stand:
**no gender word** anywhere (r14), **the chorus never halves** (r14), and Kai's
own **round-10 councilman couplet**.

### The voice: fourteen rounds of doctrine, reversed

**This is the important one, and it is a correction to this file rather than a
change of mind by Kai.** Every round since round 2 has treated one sentence as
axiomatic: *Karen is a non-singer, the joke is the voice, and if she becomes a
singer the premise dies.* Round 12 states it outright — *"putting that voice on
her timbre would end the character."* The exclude list opened with `soulful,
r&b, neo-soul, warm alto` for eleven rounds to enforce it.

**Take B is that axiom's exact inverse, and Kai liked the vocals.** Its Style box
asks for an expressive mature female alto with soulful phrasing; its exclude list
bans `nonstop nasal honk`, `cartoon voice`, `broad sitcom caricature` and
`exaggerated whining on every line` — i.e. it excludes the character this file
spent eight rounds and a Voice transplant building.

So the target is not "the honk" and never quite was. It is **a real singer
performing the honk**: `nasal complaint curls on the line ends` over `rich chest
voice, warm midrange`, with the whine as an *accent she puts on*. That reading
keeps the joke (the character is still insufferable) and drops the constraint
that made the joke expensive (a non-singer in a lead slot no genre supplies).

**Consequences, stated rather than buried:**

- **The saved Karen Voice comes off.** It was cloned from honk material; it now
  fights the box. Kept, not deleted — see Settings for when to reach for it.
- **The exclude list changed philosophy**: guards at *both* ends, middle left
  open. It is 600 chars, the longest ever, and it is now the main thing holding
  the lead's register.
- **"Her voice still isn't the one he endorsed" is finally explained.** Rounds
  12–14 kept restoring round-8's honk clause byte-for-byte and kept missing,
  because the endorsement being chased was B's, and B is not a honk.

### "Way too slow" was never the BPM

Round 14 read Kai's *way too slow* as a tempo complaint and went 86 → 112. But
**both liked takes are 86 BPM**, so the number cannot be what was wrong. What was
wrong was round 11's chorus halving, still in force at round 13: an 86 BPM track
whose choruses drop to an effective ~43. Round 14 removed the halving *and*
raised the tempo — two fixes for one fault, and the second one broke the groove
that was liked. **86 BPM, no halving** is the configuration that satisfies every
piece of feedback on record.

### The Bond, in the beat, without the pastiche

Round 9 put a spy big band in the genre slot and it ate the record; round 10
demoted it to a chorus-only swell and Kai said the Bond elements *hadn't worked*.
Both attempts treated Bond as a **band**. Round 15 treats it as **harmony and
bass** — the two things a boom bap track can absorb without changing what it is:

- the on-hold muzak loop now sits on an **unresolved minor-ninth** — the spy
  chord, *inside the song's own conceit*, so the reference and the joke are the
  same object;
- the walking upright bass becomes a **prowling chromatic** upright bass;
- the chorus swell gains **low brass and timpani** over the strings it had;
- and the fusion is written in the corpus's documented form — **foundation plus
  named influence** (`Hip Hop, Boom Bap … arranged like a 60s spy-thriller film
  score`) rather than two genres listed as equals, which is precisely the
  construction round 9 used.

No twang, no costume words; `surf rock` and `spaghetti western` stay excluded.

### Flat: three fixes, because there is no single lever

*Flat* is not a wrong element — everything named in B's box was present. The
corpus's diagnosis is uniform intensity, plus the fact that Suno never supplies
transitions. So:

- **Arrangement.** Verses stay small and dry; the pre-chorus thins to a rimshot
  with a rising brass swell; the chorus lands on a **timpani hit on the
  downbeat**; a new **four-bar instrumental spy-riff break** sits between chorus
  2 and the bridge — the midpoint is where flat hurts most, and it makes the
  bridge's collapse into intimacy read as a drop; Verse 3 gets fatter drums and
  strings creeping in.
- **Performance.** The lead has an **arc** in the box for the first time —
  patient and amused → strained by Verse 3 → bare on the bridge. The corpus calls
  the arc the highest-leverage vocal device there is, and this box has only ever
  carried states.
- **Slider.** Weirdness **50 → 60**. The track has run at effectively zero
  randomness since round 2; 60–65 is the documented sweet spot.

### The bridge, un-bricked

Both liked takes ask for `wah guitar and clavinet` on the bridge. This file has
had no guitar in the Style box since round 10 and `rock guitar` in the excludes
until round 12, so that cue was very likely vetoed for rounds — the bridge people
liked was probably never the bridge the cue asked for. `rock guitar` is out, and
the wah and clav now live **only in the bridge cue**, which is standing problem
2's rule (section-scoped material belongs in the section cue, not the global
box). Flagged here so the next cue/box diff doesn't read it as a leak.

### The lyric box has a ceiling, and this round found it

The per-line cues adopted from take B cost ~1,200 chars and pushed the box to
**5,025 against a 5,000 limit** — it would not paste. Fixed by trimming cue text
only, down to 4,893. The rule is now written at the top of the Lyrics section:
**cut redundant casting, never a performed line and never a cue that marks a
change.** Worth knowing before the next round adds direction: there is ~107
chars of headroom, so anything new has to buy its space from something old.

### Two things this round cannot verify

1. **Take B's My Taste profile is unknown** — it was never in this repo. If it
   was not the BadCode house profile, round 15's profile is chasing the wrong
   upstream spec. Worth a minute of Kai's memory before the next roll.
2. **Nothing here has been heard yet.** Every claim above is a prediction from
   the corpus and this file's own history. Judge the band and the voice
   separately on the first three rolls, and report them separately.

**2026-08-11 (round 14) — the gender flip diagnosed, the tempo reversed, and an
audit of the whole stack.** Kai on the round-13 takes: the voices flip back and
forth between male and female; too much jazz, wants some pop but not too much;
**way too slow**; the target is a mix of *Luther Vandross, Bond title songs,
Fleetwood Mac and jazz/funk, faster*; and her voice still isn't the one he
endorsed.

### The gender flip is my bug, and the fix is to delete a word

Round 12 put **`male`** into the background clause to stop the clerks merging
with her, and flagged at the time that this reversed a round-3 deletion made
because male was leaking onto the lead. **The flagged risk is what happened.**
Round 13 then made it worse by deleting the choir and routing the *sung* chorus
answers to those same "deep male telephone voices" — so the backing slot was
being asked to be a spoken male clerk and a sung chorus at once, against a
female lead, and it oscillated.

**`male` is gone from every box and every cue, permanently.** Gender is an
*adjective on a category*, and adjectives on the same category are what the
model averages. Distinctness comes from **category jumps** instead, and round 14
runs three:

| | Slot | Category |
|---|---|---|
| Karen | lead | solo, close, dry, spoken, nasal |
| The clerks | parentheses, verses | solo, band-passed, distant, spoken, flat |
| The answers | parentheses, choruses | **a group**, lush, sung, wide, close harmony |

Solo-vs-group and filtered-vs-dry cannot average the way male-vs-female can.
**This also un-parks round 8's best idea** — the institution as a choir — and it
costs nothing, because Luther's and Fleetwood's shared signature *is* the stacked
close-harmony backing vocal. The reference and the casting fix are the same move.

### Too slow: round 11's levers are reversed

"Grander and slowed down" (round 11) and "way too slow" (round 14) are opposite
instructions, so this round takes the slowing back out and keeps the grandeur —
which was always in the arrangement, not the tempo:

- **BPM 86 → 112.** Fast enough for funk drive and a pop pulse, slow enough that
  her patter still fits the bar.
- **The chorus no longer halves.** Cues now read `the band drives on, no slowing`
  and `tempo unchanged`. The swell does all the work it was ever doing.
- **The braking punctuation is undone.** `That's... O-K.` → `That's OK.`, the
  ellipses out of the hook echoes, and the blank line before the hook removed
  from all three choruses. Those were pure slow-down devices.
- **`Take your ti-i-ime` is back to final-chorus-only**, where it was before
  round 11 — it is a sarcasm device, and spreading it to all three both slowed
  the track and spent the joke early.
- **Excludes dropped `uptempo` and `dance`**, added in round 13 against a tempo
  drift and now vetoing the ask.

### Too much jazz: the genre slot is close to binary

Round 13 put `Jazz, Noir Jazz` in the genre slot precisely because jazz kept
vanishing as a modifier — and it worked so completely the track became a jazz
record. Both observations are the same law: **the slot picks the arrangement, so
a style is either in it or effectively absent.** The resolution is a genre that
*is* the blend: **`Jazz Funk`** — jazz harmony and instruments, funk drive and
bass, one head, no argument. Pop enters as **production polish** (`glossy analog
pop polish`, `clean electric guitar`), never as a genre, which is the only way to
get "more pop but not too much": as a genre it would take over, as an adjective
under a genre head it stays a seasoning.

### The four references, mapped to words

Artist names never go in a box. `glossy analog pop polish` and `clean electric
guitar` carry the 70s pop gloss and jangle; `lush stacked group in close harmony`
carries the layered backing vocal both vocal references are famous for; `funky
popped electric bass` carries the funk; `grand as a film title sequence` stays
chorus-only. `yacht rock` joins the excludes — Fleetwood plus Luther plus
jazz-funk has exactly one cheese failure mode and that is its name. `funk soul`
came *out* of the excludes, since some of that gloss is now wanted.

### The cue/box diff, run

Standing problem 6 says to diff the instruments in the bracket cues against the
instruments in the Style box every round. Run for round 14: **no orphans left** —
round 13's `wah`, `clav` and `Rhodes` are gone from the cues along with the box.
One gap the other way: `clean electric guitar` was in the box and cued nowhere,
so Verse 1's cue now names it and the band is fully described in both places.
`touch-tone beeps as percussion` is cued but deliberately absent from the box —
that is the novelty guard (standing problem 8), not a leak.

Box sizes this round: Style **849** chars, Exclude **247**, My Taste **1,788**.

**2026-08-11 (round 13, experimental) — four ingredients, and jazz finally gets
the genre slot.** Kai on the round-12 takes: **way too weird, and the jazz is
gone completely.** New brief, stated as a whitelist rather than a change list:
**the best version of Karen's voice, jazz only, film-title-sequence vibes, and a
funky bass. Nothing else.**

**Why the jazz keeps vanishing — the answer is structural, and it has been the
same for three rounds.** Jazz has *never once* been in the genre slot. It has
always been an adjective hanging off some other head: `Boom Bap Hip Hop` (r8),
`Hip Hop, Lofi Jazzhop` (r11), `Funk Soul` (r12). This file's single most
expensive lesson is that **the genre tag picks the whole arrangement**, so a
jazz modifier on a non-jazz head loses every time, no matter how many jazz
instruments are named after it. Round 11 diagnosed the disappearance as five
words deleted from My Taste and that was true but small; this is the real cause.
Round 13 puts `Jazz, Noir Jazz` in the slot and nothing outranks it.

**"Too weird" was a stuffed box, not a weirdness slider.** Weirdness has sat at
50 — effectively no randomness — since round 2. What changed in round 12 was
that the box carried funk *and* soul *and* jazz *and* the swell *and* a tempo
change *and* a new vocal register, at 986 of 1,000 chars. **Round 13 answers it
by deletion:** 986 → **759 chars**, the shortest since round 2, which is the
round whose whole lesson was *cut the prompt in half so the voice can win*.
Character limits are ceilings, not targets.

**Bond and jazz turn out to be one ingredient, not two.** `noir jazz` is the
Bond lineage — smoky, minor-key, muted trumpet, the harmony the franchise was
built on. So the reference now arrives twice in two registers: as the **genre**
in the verses, and as the **title-song swell** on the chorus (sustained strings,
low brass, timpani, the minor-ninth). No costume words, no twang. Round 9's
surf-guitar pastiche stays buried and `surf rock` / `spaghetti western` stay in
the excludes to keep it there.

**The funky bass is the only non-jazz ingredient, and it is scoped to one
instrument.** `a funky popped electric bass walking underneath` — funk as a
*bass part* inside a jazz band, which is what was asked for, and specifically
**not** what round 12 did (funk as the genre head, which brought the whole
glossy soul band with it).

**Deleted outright, not demoted:** the hold-muzak loop, touch-tone beeps, tape
hiss, boom bap drums, chanking guitar, Rhodes, horn stabs, the soul gloss, the
stacked soul harmonies, and the 104 BPM. **BPM back to 86**, the tempo of the
endorsed round-8 take.

**Two real costs, both flagged rather than hidden:**

- **The conceit left the style box.** "Make the conceit the instrumentation" —
  the muzak loop as the lead melodic element, touch-tone beeps as percussion —
  has been the standing guard against this premise turning novelty since round 1.
  It is not an ingredient on the list, so it went. The dial tone and the IVR
  lines survive in the lyrics, and the novelty excludes are now carrying that
  line alone. **Watch for vaudeville**; if it shows up, the cheapest repair is
  `touch-tone beeps as percussion` back into the box, 32 chars.
- **The choir is parked.** Round 8's best structural idea — the institution
  cast as a lush choir, so the bureaucracy sounds beautiful and Karen refuses to
  be soothed — was a smooth-vocal ingredient and is not on the list. The chorus
  answers are now sung by the **deep male telephone voices** instead, which
  keeps the call-and-response, keeps round 12's anti-merging casting, and adds
  no ingredient. It is a downgrade in payoff and an upgrade in focus.
  Recoverable in one clause whenever you want it back.

**What survived from round 12, and why:** the clerk-casting clause (`Deep male
telephone voices… band-passed and flat`) is *casting*, not instrumentation —
deleting it would re-open the merging problem that round raised. The shortened
clerk lines stay too; their terminal rhyme words were preserved, so the
reach-over device is intact.

**2026-08-11 (round 12) — hip hop is out; the band goes full jazz-funk, and the
clerks get cast as somebody else.** Kai on the round-11 takes: closer, but go
**full throttle on the jazz, funk and film-title-sequence elements and forget
the hip hop entirely**; the voices answering her are **merging with hers**; and
add **Luther Vandross** — *Never Too Much* — to her voice and to the whole song.

**Genre head: `Hip Hop, Lofi Jazzhop` → `Funk Soul`, and the jazz comes up on
top.** Round 11 had jazz as the thing the drums sat on; round 12 has no hip hop
drums to sit on. The band is now a glossy early-80s soul-funk band —
sixteenth-note guitar chank, popped melodic electric bass, Rhodes, horn stabs —
with the noir jazz (muted trumpet, walking upright bass, brushed drums) as the
layer underneath. Hip hop moved from *absent in the style box* to *named in the
excludes*, which is the difference between not asking for it and pushing it out.

**BPM 86 → 104, and this is a real compromise, not a free choice.** The two
references disagree: full-throttle funk soul of the *Never Too Much* kind runs
~136, and a title-song swell runs 60–80. 104 is the seam — the guitar chank is
real funk, her patter still fits the bar, and the half-time chorus lands at an
effective ~52, which is grand-ballad tempo. **This also makes the song's
existing architecture work harder:** fast funk verses against a half-speed
orchestral chorus is a bigger contrast than round 11 had, and contrast is the
mechanism that makes the chorus read as an arrival.

### The Luther ask, and how it got split

**Say the sound, never the name.** `Luther Vandross` joins `James Bond` on the
never-write list — artist names trip moderation and steer worse than description.
The style box says `a silky 1981 soul star` and names the band.

**Stated plainly: putting that voice on her timbre would end the character.**
Smooth, silky and soulful is the exact centroid this track spent rounds 2–8
escaping, and `soulful, r&b, neo-soul` were the first three words of the exclude
list. If Karen becomes a soul singer, the premise — *the joke is the voice* —
dies with her.

**So Luther is split across the two slots instead, and the split is the good
version of the idea:**

- **Her voice gets his *phrasing*, not his timbre** — `sweet melismatic runs,
  effortless ad-libs trailing off her line ends`, performed *through* the nasal
  honk. A whining, honking woman doing immaculate soul runs is funnier than
  either pure option, and it is the only reading that doesn't cost us the
  character. The lyrics gained one melisma to seed it (`le-e-evel`).
- **The band and the record get his *sound*, full throttle** — `glossy and
  expensive`, the chank, the popped bass, the horn stabs, the immaculate gloss.
- **The chorus answers get his *backing stack*.** The choir was already cast as
  the institution back in round 8 ("cast the default instead of fighting it").
  Luther sharpens it: the answers are now `lush stacked soul harmonies, sweet and
  immaculate`, so the bureaucracy sounds like the most beautiful record you have
  ever heard and she still refuses to be soothed by it. Every chorus cue gained
  `never joins them`.

**If the intent was actually her timbre**, the switch is one line: move
`silky, smooth, soulful` into her clause and delete the honk words. That is a
different song and this file recommends against it, but it is one edit.

### Why the clerks were merging, and the three-layer fix

Two documented mechanisms, both of which this track was walking into:

1. **Cast across categories, not adjectives.** Two voices stay separate in
   proportion to how far apart they are *in kind*. Karen and the clerks were both
   "one adult speaking a full sentence" — different adjectives on the same
   category, which is exactly the configuration the model averages.
2. **Parentheses bias, they don't bind — and line shape is itself casting.** A
   long, syntactically complete clause reads as a lead line and gets claimed by
   the lead voice *through* the parentheses. Half the clerk lines were full
   sentences.

The fix, applied at all three layers at once:

- **Style box — a category jump.** `Muffled telephone clerks answer from behind
  the beat` (a *placement*) became `Deep male telephone voices answer from far
  behind the beat, narrow band-passed, distant, flat and bored` (a *category*:
  male, deep, filtered, and delivering the opposite way to her whine).
  **`male` returns to the background clause, reversing round 3** — that deletion
  was made when male was leaking onto the *lead* and the box also described a
  male rapper. Neither condition holds now, and the failure has inverted.
- **Treatment is casting, not mixing.** She is `close-mic'd and dry`, they are
  `band-passed, distant`. Two people in two different rooms reads as two people
  even when the timbres are neighbours — and it costs nothing.
- **Lyrics — the clerk lines got shorter, from the front.** `(Ma'am, I'm only
  the front desk, I can't authorise that)` → `(Front desk only, Ma'am — can't
  authorise that)`; `(There's really nothing further I can do at this level)` →
  `(Nothing further at this level)`; and three more. **Every terminal word is
  preserved**, because the clerks' line-endings carry the rhymes Karen reaches
  over to finish (`that`/`sat at`, `pass`/`glass`) — and that reach-over is the
  skit-track device. Shortened from the front, the rhyme device is untouched.
- **Every section cue now names the clerks as a separate cast.** Redundancy
  across brackets is the sanctioned escalation, and a section with no direction
  falls back to the default for that section.

**Also fixed by the genre change: the bridge.** It has said `funk switch | wah
guitar and clav take the lead` since long before this round, in a track with no
guitar in the style box and `rock guitar` in the excludes — so it very likely
never fired. `rock guitar` is out of the excludes now and the band is funk, so
wah and clav are finally native. But `funk switch` no longer marks a change when
the whole song is funk, so the cue became `the band falls away — wah guitar and
clav alone, warm and close`. The bridge's job is the drop in temperature; now
the cue says that instead of naming a genre it no longer contrasts with.

**Its `half-time` cue was dropped rather than kept**, because half-time is the
documented blind spot and the chorus already spends the trick.

**The risk, stated plainly.** This round removes the anti-smooth excludes *and*
runs without the Karen Voice (Kai's experiment). Those are the only two things
that have ever protected her lead. If she comes back a smooth soul singer, that
is the predicted outcome, not a bug in the box — see Settings. Judge the band on
these takes and the voice on a take with the Voice re-attached.

**2026-08-11 (round 11) — lofi jazzhop, and the chorus gets slow.** Kai on the
round-10 takes: more of the film-title-sequence feel; the chorus needs to be
**grander and slowed down**; **the jazz is gone and he wants it back**; the
woman's voice is **not as close as the take he called perfect**; and the whole
thing wants **a lofi hip hop beat behind the jazz and the cinematic material**,
with the vocal treated to match.

**The jazz loss is traceable to five deleted words, and they were in My Taste,
not the Style box.** Round 8's profile read `Core sound: Dusty 86 BPM boom bap
**and soul-jazz**…`. Round 9 realigned the profile for the spy band and dropped
`and soul-jazz`; round 10 restored the boom bap but never put the jazz back. The
Style box kept the jazz *instruments* (muted trumpet, walking upright bass,
brushed drums) the whole time — but round 4 proved My Taste sits **upstream** as
a competing spec, and with the word `jazz` living nowhere in either box, those
instruments were being read as boom-bap furniture rather than as a jazz band.
Naming the genre is what makes them play like one.

**"The take he called perfect" is round 8** — that is the only take this file
records Kai endorsing, and round 10's own log quotes him: *"the round-8 version
had more of the jazz and the right voice."* (Searched the repo for a more
specific endorsement; there isn't one. If a different take is meant, say which
and this diagnosis gets re-run.) **And her vocal clause has not changed since
round 6** — round 8, round 10 and round 11 are word-for-word identical on the
voice. So the voice didn't drift because we described her differently. It
drifted because of what got added *around* her:

- **The box grew and her share of it shrank.** 771 chars at round 8 with the
  voice as ~52% of it; 926 at round 10 with the voice at 43%. Round 2's dilution
  law says the arrangement out-votes the vocal when the box fills up.
- **Every added character was smooth-singing vocabulary.** Round 10's chorus
  clause opened `a lush, smooth, polished group choir sings the answers over…` —
  three smooth descriptors, **front-loaded inside the clause**, in a box whose
  words don't know which vocal slot they belong to. Front-loading is a documented
  lever; round 10 spent it on the wrong voice.

**So the fix is deletion, in the choir's half.** `smooth` and `pretty as hold
music` are out of the Style box (both survive in My Taste, where they're scoped
by a `Choruses only:` heading), and the chorus clause now leads with the
**orchestra** and puts the choir last. The choir's smooth-word load in the Style
box goes from four words to two. Her clause gains only the lofi treatment.

Changes:

- **Genre head: `Boom Bap Hip Hop` → `Hip Hop, Lofi Jazzhop`.** This single word
  answers three of Kai's four asks at once — the lofi beat, the jazz, and half
  the cinematic feel — because jazzhop's native instrumentation *is* the dusty
  Rhodes / muted trumpet / upright bass / brushed drums the track already had.
  Parent + subgenre is the documented pairing form. **Boom bap moves to the drum
  description** (`smoky noir jazz over dusty boom bap drums`), which is where it
  was doing the work; round 10's "don't touch the genre head" rule was written to
  stop the *cinematic* material being promoted, and a sideways move inside the
  hip hop family isn't that. Rollback noted in the Style section.
- **`noir jazz`, not `soul-jazz`.** Round 2 cut `soul-jazz` because it fought
  `soulful` in the excludes and dragged the lead vocal soulful. `noir jazz`
  carries the same instruments without the vocal-soul attractor — and it is on
  the *same lineage as the Bond ask*, since Barry's band was a jazz band. **More
  jazz and more film-title-sequence are the same move**, which is why this round
  gets both without the box growing much.
- **The Bond stays harmonic, not costume.** No new pastiche words. The
  minor-ninth, the sustained strings, the low brass and timpani and `grand as a
  film title sequence` all survive; round 9's twang stays buried.
- **Excludes:** `gospel choir` dropped (round 10 named it as the first thing to
  go for a bigger chorus, and bigger is the ask); `jazz singer` and `scat` added
  as the price of naming jazz — they block the crooner without blocking the band;
  `dreamy`, `airy`, `mumbled` added as the lofi-vocalist guards. 392 → 420 chars.
- **My Taste:** jazz restored to `Core sound` as `lofi jazzhop — smoky late-night
  noir jazz over boom bap drums`; `tape hiss` added to Production; the cassette
  treatment added to `Vocals`; the `Choruses only:` line now leads with the beat
  halving. 1,247 → 1,720 chars.
- **Style box:** 926 → 966 chars. **The growth is entirely in her clause** (the
  cassette treatment); the band-and-choir half is flat, and the smooth-choir
  vocabulary inside it shrank.

**The slow-down is a lyric job, and that is not a compromise.** Suno has a
documented blind spot here: across controlled tests a `breakdown`-style tag
always slowed and *thinned* the arrangement but **never produced half-time
drums** — the model appears not to hold the concept. So the chorus cues describe
the **sound** (`the beat halves — slow and heavy, twice the space between the
hits`) rather than naming the technique, and the real lever is lyric density,
which is proven on this track:

- **Brake punctuation throughout the choruses.** `That's OK.` → `That's OK.`
  — an ellipsis is a slow trailing pause and a hyphen inside a word stretches the
  note. Both are brakes; density is what actually sets perceived tempo.
- **A blank line before the hook**, in all three choruses. The blank-line
  technique is the strongest single performance control in the lyrics box, and it
  buys the dramatic pause before `I've got all day to complain`.
- **The elongated vowel spreads.** `Take your ti-i-ime` was final-chorus-only;
  it now runs in all three, and the final one goes to `ti-i-i-ime` so the last
  hook is still the biggest.

**Also cleaned: the wah.** All three chorus cues carried `wah wider` / `wah wide
open` and the Style box has had no wah guitar since round 10 — with `rock guitar`
back in the excludes it was very likely vetoed anyway. It also fights "slow and
heavy". Deleted from the chorus cues. **The bridge still says `funk switch | wah
guitar and clav take the lead | half-time`** — left alone because Kai hasn't
flagged the bridge, but note that its `half-time` is subject to the same blind
spot, so don't count on it.

**If the chorus still won't drop to half speed, stop prompting it.** That is
Studio work — time-stretch the chorus regions or splice — not another box. Say
so rather than selling another round.

**2026-08-11 (round 10, lyric edit) — the councilman's assistant.** Kai swapped
the Verse 2 third couplet. Was:

> Week three, a councilman's assistant, very nice boy,
> (He's in session, he's in session) — well. hoooney. So am I.

Now:

> Week three, a councilman's assistant, weak constitution but will do for now.
> (Hold, Ma'am, give me a second) — he thinks I'll just throw in the towel.

Better joke, and a more BadCode one: the old line was a straight pun on *in
session*, the new one is **a councilman's assistant with a weak constitution** —
the pun does political work instead of just being a pun.

**And the clerk's reply proves the insult.** She calls him weak; he immediately
asks for a second. `give me a second` is a *stall*, not a block, which also
makes him a distinct rung on the ladder — the front desk refuses, the supervisor
is unavailable, this one just buys time. Her comeback never addresses him at
all; she is reading his mind while he flounders.

**It also plants the bridge.** *He thinks I'll just throw in the towel* is the
song's thesis — *every system you ever built runs on people hanging up* — said
early, in her voice, as a throwaway. The bridge then says it straight. Throwing
in the towel and hanging up are the same act in different clothes, so the verse
now sets the bridge up instead of the bridge arriving cold.

Three typos fixed in passing, flagged rather than silent: **`consitution` →
`constitution`** and **`thow` → `throw`** (Suno sings a misspelling), plus
**`mam` → `Ma'am`** to match the other four functionary lines in the track.

Knock-ons worth knowing:

- **The rhyme is back, and so is the device.** `now` / `towel` is a slant rhyme
  on the /aʊ/ — the same grade as `code`/`phoned` — and it lands **after the
  dash**, so Karen again closes her own couplet *over* the clerk's interruption.
  That mid-couplet reach-over is the skit-track device; an intermediate draft of
  this edit had lost it.
- **The line length came back in range.** An intermediate draft of this couplet
  ran ~22 syllables against the 12–14 the rest of Verse 2 sits at, which at 86
  BPM would have rushed or spilled the bar. Trimming the clerk to `give me a
  second` and dropping Karen's `see what I mean,` brought it to ~16 — still the
  longest line in the verse, but patter can carry that. **If it still crowds,
  cut `just`**: one syllable, no meaning lost.
- **Verse 2 lost its elongated vowel.** `hoooney` was one of the three
  sing-song-sarcasm stretches added 2026-07-30 (with `Sweeeetheart` and
  `lo-o-ovely`, both in Verse 1). Verse 2 now has none, so the device is
  concentrated in Verse 1 and the final chorus's `ti-i-ime`.

**2026-08-11 (round 10) — demote the spy band to a layer; the grandeur moves to
the chorus.** Kai, on the round-9 takes: the Bond elements *haven't worked*. The
round-8 version had more of the jazz and the right voice and was closer to what
we wanted. Keep something like **Skyfall** — but as a **layer**, not the song —
and make it **heavy in the chorus**: grand, and it should make an impact.

**The diagnosis is one line: round 9 changed the genre.** The band clause went
from `Boom Bap Hip Hop at 86 BPM underneath her` to `a 1960s Cold War
spy-thriller big band crossed with 86 BPM boom bap`. Per this project's own most
expensive lesson (rounds 3–6), **the genre tag is the strongest word in the box
and it picks the whole arrangement**, so naming spy-thriller big band *as the
genre* meant it could only take over. It was never going to sit as a layer,
because a layer is not what it was written as. Boom bap is restored as the head
and the cinematic material is now explicitly an arrangement event.

**Round 9's stated fix was wrong, and the Skyfall reference is why.** It
predicted: *if it reads as pastiche, keep the twang and drop the brass
stingers.* That guess was anchored on the **gun-barrel instrumental** — Vic
Flick's twangy surf guitar, the *Dr. No* sound. Kai's reference is **Skyfall**,
which is the other lineage entirely: the **title-song swell** — slow, minor-key,
huge sustained strings, low brass, timpani, an orchestra arriving all at once.
There is no surf guitar anywhere in it. So the fix is the **inverse** of the
prediction: the twang goes, the swell stays and gets bigger. The twangy tremolo
guitar was also the single loudest pastiche tell in the box *and* the one
element playing in every verse — it was the takeover, not the victim of it.

Changes:

- **Style box:** `1960s Cold War spy-thriller big band`, `twangy tremolo surf
  guitar` and `brooding and stabbing brass stingers` all deleted. `Boom Bap Hip
  Hop at 86 BPM, warm and unhurried` restored as the genre head — round 8's
  words, which is the take Kai says was closest. The chorus clause absorbs all
  the cinematic material (`everything swells … sustained minor-key strings, low
  brass and timpani, unresolved minor-ninth tension, huge and cinematic, grand
  as a film title sequence`). 939 → 926 chars. **Fixed by deleting, and the box
  got shorter** — the standing round-2 rule.
- **The minor-ninth survives the cull.** It is the one genuinely Bond thing that
  is *harmony* rather than *costume*, so it can't read as pastiche. It moved
  from the band clause to the chorus clause with everything else.
- **Excludes:** `rock guitar` returns (round 9 dropped it purely to permit surf
  guitar), joined by `surf rock`, `spaghetti western` and `big band swing`.
  `orchestral` stays out and now matters more — it would veto the strings, brass
  and timpani the chorus is built from. 333 → 392 chars.
- **Lyric cues:** the intro loses the twang and the sting; the three choruses
  now carry an **escalating swell** (strings → strings + brass + timpani → the
  full thing), which is where "heavy in the chorus" is actually implemented;
  Verse 3's `strings enter` became `low strings creep in underneath, building`
  so the last verse ramps rather than pre-empting; the final chorus swapped
  `brass stabs behind her` for the full swell and gained `refusing to be
  impressed` on the lead.
- **My Taste realigned** — round 4 proved it sits upstream as a competing spec.
  Core sound is boom bap and warm again, and the swell is stated as a separate
  **Choruses only** line that says the verses never do it.
- **Sliders held at 90/50** deliberately, with a note in Settings on what to
  move once the box is settled. Changing the prompt and the sliders in the same
  round makes the A/B unreadable, and round 9 was not an adherence failure.

**What round 9 got right and this keeps:** the choir as the institution
(round 8's idea) is still the payoff — the bureaucracy gets the big cinematic
sound and Karen refuses to be soothed by it. Round 9 was correct that the
*chorus* was where the grandeur belonged. Its error was spending it everywhere
else too.

**A/B this against a round-8 take.** If the chorus still isn't big enough, drop
`gospel choir` from the excludes before touching anything else — it is the only
word left that could be capping the size.

**2026-08-11 (round 9) — the institution gets a villain's theme.** Kai: the tune
is landing, but it wants to feel like a sixties spy-thriller title sequence. Not
a rewrite — a sidestep. The track was *already* sitting on the noir-jazz core
(muted trumpet, walking upright bass, brushed drums); spy jazz is that plus the
twang and the stabs.

**Say the era, never the franchise.** "James Bond" and "007" are trademarked
terms that trip Suno's moderation, and practitioner consensus is that even when
they pass they steer worse than `1960s Cold War spy thriller` does. Same lesson
as round 2 in a new coat: name the sound, not the reference.

What actually carries the signal, and the words for each: the Vic Flick guitar
(`twangy tremolo surf guitar`), Barry's brass — shrill and jabbing, not warm
(`brooding and stabbing brass stingers`, `overblown trumpets`), the Bond chord
itself, an Em(maj9) (`unresolved minor-ninth tension`), and the strings
(`sustained minor-key strings`, `sweeping`). The original is scored for five
saxes, nine brass, solo guitar and rhythm section — big band minus the piano,
which is roughly what we already had.

**Two Bond sounds, two slots.** The gun-barrel instrumental goes to the band;
the title-song swell goes to **the choir**, which round 8 already cast as the
institution. That's the payoff of this round: the bureaucracy gets the villain's
theme, sweeping and cinematic, and Karen refuses to be impressed by it. The
prettier and more dangerous the system sounds, the funnier her flat refusal to
be soothed by it.

Changes: style box gained the spy-band clause replacing `Boom Bap Hip Hop at 86
BPM underneath her` and the old `warm and unhurried` (771 → 939 chars); excludes
**dropped `orchestral` and `rock guitar`**, which were vetoing the sweeping
strings and the surf guitar the style box now asks for — the same box-arguing-
with-itself bug as round 2's `soul-jazz` vs `soulful`; the intro and final-chorus
bracket cues gained the twang and the stabs (bracket cues are a proven control
surface on this track, so spend direction there too); and the **My Taste profile
was realigned** — round 4 proved it sits upstream as a competing spec, so
leaving `warm, unhurried` in it while the style box says *stabbing* would have
re-run that exact failure.

**The risk, stated plainly:** this breaks the standing "warm, unhurried, sincere"
doctrine, which is what has kept an absurd premise from turning novelty. The
judgement is that *sincere* was the load-bearing half and *warm* was not — a spy
band playing menace with a straight face is still straight. But the novelty
excludes (`kazoo, slide whistle, circus, honky tonk piano`) are now doing more
work than before. **A/B this against a round-8 take before committing** — if it
reads as pastiche rather than threat, the arrangement went too far and the fix
is to keep the twang and drop the brass stingers.

**2026-08-04 (round 8) — the Voice landed; the chorus flips to the institution.**
The Karen Voice holds across the whole track — the six-round lead-vocal war is
won. New problem: the chorus was designed for a smooth sung hook, and Karen
whining it sounds wrong. Considered restructuring the song away from a harmonic
chorus vs. getting a second voice on the chorus. Chose the second, implemented
structurally: **one generation can carry only one Voice, but the parenthesis
slot is effectively a second voice** — it renders as backing vocals and does not
inherit the lead's identity (proven by round 6's intro, where the parenthetical
IVR lines escaped the genre prior in the other direction).

So the chorus flips: **the smooth polished choir we spent six rounds fighting is
cast as the institution** — hold-music-with-a-face singing the functionary's
answers, pretty and soothing — while Karen stays spoken, whiny and unmoved
against it. The silky voice becomes the antagonist's sound; the prettier the
system, the funnier her refusal to be soothed. The melodic lift the old choruses
had returns, carried by the backing slot.

Changes: the sung hook echo moved into parentheses (`(all day to complain, all
day to complain)`) so the choir carries the melody and Karen speaks the line;
all three chorus cues now direct two voices (`smooth polished group choir sings
the answers, sweet as hold music | lead stays spoken, whiny, unmoved`), still
escalating choir-size across the track; the style prompt gained the choir clause
(`On the chorus a lush, smooth, polished group choir sings the answers — pretty
as hold music, never her`, 771 chars); and the excludes **dropped every
smooth-vocal word** (`smooth vocals, silky, melodic singing, sung hook, beautiful
voice, polished vocal`) — the Voice pins the lead now, and those words were
strangling the choir we want. Generate with the Voice attached, audio influence
40–60.

**Fallback if the parenthesis choir won't bloom:** Studio comp — the pre-Voice
takes had great choruses; regenerate or splice chorus vocal regions from a
no-Voice pass against Voice verses. Hours, not minutes; only if this fails.

**2026-08-04 (round 7) — she showed up, in the wrong slot.** A round-6 generation
nailed Karen's voice on the intro IVR lines ("Thank you for calling…") — then
reverted to the smooth lead the moment Verse 1 started. Diagnosis: the genre's
vocal prior binds to the **lead-vocal slot inside the groove**; the parenthetical
secondary slot, speaking character lines before the beat establishes, is largely
free of it. This **refutes the no-training-data theory with our own audio** — the
voice exists in the model; the lead slot in boom bap just can't reach it. The
problem is now a *transplant*, not a prompt: see the transplant ladder in "How to
generate". Prompt boxes unchanged this round.

**2026-08-04 (round 6) — drop the age, lead with the character genre; and the two
structural exits.** Round 5 (correct cues everywhere, taste profile swapped,
weirdness tested low and high) still converged on the smooth silky vocalist.
Kai's theory: Suno lacks training data for this voice. Research verdict:
**partly right, wrong conclusion.**

The data exists — Suno hosts comedy-song and Broadway/musical-theatre style
pages, character/theatrical delivery demonstrably works, and `[Spoken Word]` is a
top-tier reliable tag. What's missing is the *pairing*: whiny complaint-voices in
the training data live in musical theatre, comedy and novelty records —
essentially none of them sit on top of boom bap. And per practitioner tier-lists
(hookgenius), our load-bearing words rank badly: reliable texture tags are
`raspy/breathy/gritty/husky`; `nasal` and `whiny` aren't on the list, and age
descriptors are explicitly mid-tier (50–80%, our observed failure). Meanwhile
`Boom Bap Hip Hop` is a maximum-strength tag. So every generation was a tug-of-war
between our strongest word (the genre) and our weakest ones (the character), and
the genre's default vocalist won every time. Convergence at both low and high
weirdness is the diagnostic: weirdness perturbs *within* the genre's vocal pool,
it doesn't jump pools. Not "no data" — "the door we keep knocking on doesn't
connect to the room the data is in."

Round-6 prompt changes: **all age words deleted** (elderly / seventy / grandmother
/ old woman — from style, taste profile and every lyric cue). The character now
leads as a *performance tradition* Suno does know: comedy character actress,
musical-theatre patter, sitcom squawk — plus onomatopoeic texture (honk, squawk,
kvetch, bratty, cartoonish, pinched, shrill). Deliberate satire-trap exception:
`comedy` words are allowed into the vocal clause **only** because five rounds
prove the arrangement prior is stable; excludes gained `kazoo, slide whistle,
circus, honky tonk piano` as the counterweight, and dropped the spent age words.

**If round 6 fails, stop prompting this genre — run the two structural exits:**

1. **The capability probe** (settles the training-data question for ~10 credits).
   Simple mode or Advanced with no beat at all: musical-theatre patter, whiny
   nagging New York woman complaining, sparse piano — see probe prompt below. If
   the voice shows up there, the data exists and the genre prior was the wall:
   save that generation as a **Voice** (delete its style prompt) and apply it to
   this track. If the voice doesn't show up even there, the theory is confirmed
   and route 2 is the only road.
2. **Audio-seed the voice** (bypasses text entirely; confirmed workflow). Record
   15s–4min of a Karen impression — Kai or Jack complaining in character into a
   phone mic; one consistent register, spoken not sung — upload via Voice →
   Create voice, apply with **audio influence 70–100** (artifacts expected), then
   two-pass: Cover the good take at ~25–40 to recover fidelity. The verification
   check passes ~90% if you perform it in the reference style rather than reading
   flat. If neither of us can do the voice, character actors who specialise in
   exactly "whiny annoying woman" are cheaply hireable on voices.com.

Probe prompt (Style box, nothing else changed):

```
Comedy patter song, musical theatre. A whining, honking, nagging New York woman complaining — sharp nasal squawk, pinched and shrill, bratty cartoonish sitcom delivery, exaggerated kvetching whine curling up at the end of every line. Sparse piano and upright bass accompaniment.
```

**2026-08-04 (round 5) — the lyric box still held the round-0 cues.** Spotted by
Kai: the bracket in Suno read `[Verse 1 | deadpan New York drawl | close-mic,
unhurried | …]`, which this file has not said since round 1. **The Style box was
being updated every round; the Lyrics box never was.** So all four rounds ran
`deadpan`, `unhurried`, `same deadpan`, `sweet on top` — section by section, on
the surface v5.5 obeys most reliably (Kai's own round-2 finding). We were tuning
the weakest control while the strongest one said *chill* twelve times.

Bracket cues now carry the **character identity in every section**, not just an
emotion word, and not just in the verses — intro, both pre-choruses, all four
choruses, the bridge and the outro included. `old woman` / `nasal` / `whiny`
appears in eleven of thirteen brackets. Redundancy is deliberate: repeating an
ignored cue in different words is the sanctioned escalation, and a section header
with no vocal direction lets Suno fall back to its genre default for that section.

The spoken bridge cue went to `[spoken word speech talking | …]` — the documented
redundancy ladder for a spoken cue that isn't firing.

Two sections keep a *different* direction on purpose: the bridge (`drops the
whine — worn down, quiet`) and the outro (`finally unbothered`). Those are the
turn and the punchline; they only land against a strained voice everywhere else.

**Process lesson: re-paste every box every round.** Style, Exclude, Lyrics *and*
My Taste. Suno's "Reuse Prompt" carries the old lyrics forward silently, and a
stale lyric box is invisible in the take you're listening to — it just sounds like
the style prompt isn't working. This is also why the paste blocks now sit at the
top of this file.

**2026-08-04 (round 4) — the upstream contaminant: My Taste.** Three rounds of
style-prompt surgery moved the voice not at all. Cause found: the **My Taste**
profile, which is applied globally to every generation and which held the BadCode
house profile — *"rooted in a thick Scouse (Liverpool) voice … Vocals: Northern UK
English, strong Scouse Liverpool accent, adenoidal Merseyside delivery … rising
intonation."*

That is a second, competing vocal specification sitting upstream of the style box,
and it explains all three symptoms at once: the **male leak** (nothing in our
prompt asked for male; the profile specifies a male Scouse MC), the **dead
descriptors** (`adenoidal` and `rising intonation` were in *both*, so they carried
no discriminating power), and the **silkiness** (two incompatible strong vocal
specs resolve to the centroid, which for female + hip hop + half-spoken is the
smooth vocalist).

**Correction to the toolkit:** `suno-gpt/files/suno-controls-and-workflows.md`
says to "turn OFF My Taste (profile settings)". There is no such toggle. The
dialog has a free-text box (2,000 chars), a **My Styles** toggle that only
governs the magic-wand style *suggestion* button, and Save. **The box cannot be
saved empty**, so the profile can never be disabled — only replaced. The written
profile is also just the explicit half; Suno states it also learns from what you
create, listen to, like and dislike, and there is no control for that. Mitigation:
thumbs-down every reject, and one workspace per release/arc.

**Action:** replace the house profile with the Karen profile above for the
duration of this track, restore afterwards. Standing implication for BadCode — a
single global taste profile is the wrong shape for a catalogue with more than one
narrator in it; per-track profiles plus **Voice** for recurring characters is.

**2026-07-30 (round 3) — age her, and stop negating.** Round 2 came back sounding
like Lauryn Hill, and half the generations came out **male** until `female` was
added twice. Those two symptoms have one cause.

`spoken word, talking, not singing, no melody, no flow, no swagger` is a
description of **a male rapper**. Suno doesn't handle negation in the style box —
naming `melody`, `flow` and `swagger` puts them in the prompt no matter what word
sits in front. So the prompt was pulling hard toward half-spoken boom bap (male
attractor) while `female` pulled back, and it settled on the nearest point that
satisfies both: the smooth, conversational, female boom-bap vocalist. That region
of the training space *is* Lauryn Hill. More adjectives about whining were small
perturbations on a very strong attractor.

Three changes:

1. **All negations deleted from the style box.** `no melody / no flow / no
   swagger` moved to excludes, where negation is the box's actual job. Replaced
   with positive speech-act words: *complaining, nagging, scolding*.
2. **Aged her explicitly — `seventy`, `a grandmother`, `elderly`.** Age has real
   acoustic correlates a mood word doesn't (thin, dry, papery, reedy, a wobble in
   the tone), and it moves *away* from the attractor, which is a young voice.
   Canon-safe: she has grandchildren in [`../story.md`](../story.md). Side
   benefit — `grandmother` pins gender far harder than the word `female` does,
   which should also fix the male leakage.
3. **`male` deleted from the background-voice clause.** It was the only other
   gender word in the prompt and a live suspect for leaking onto the lead. The
   clerks are male in the lyrics; they don't need to be male in the style box.

Voice moved to the front of the prompt, genre to the middle — front-loading as a
fix after two failed rounds, not as default ordering.

**2026-07-30 (round 2) — cut the prompt in half so the voice can win.** Round 1
was still too smooth. Two causes:

1. **The style prompt was 990 of 1,000 characters, and the voice was a third of
   it.** Suno dilutes across everything you name — a maxed-out box means the
   arrangement is outvoting the vocal. Cut to **664 chars**, with the voice as
   the first ~400. Deleted the furniture a boom-bap tag gives you free anyway
   (soft rimshot, wah guitar, tape saturation, band-passed EQ detail, the
   three-rung description of the background voices). **Character limits are
   ceilings, not targets.**
2. **The descriptors were attitude, not sound.** "Put-upon", "condescension",
   "immovable", "brittle" describe a *mood* — Suno averages those into nothing.
   Replaced with articulation: *nasal, whiny, pinched, adenoidal, through the
   nose, flat hard vowels, over-enunciated consonants, rising whine at the end of
   every line.* Describe her mouth, not her feelings. (Camping's working prompt
   does the same thing — "adenoidal Merseyside drawl, softened ck sounds".)

Also cut **`soul-jazz`** — it was pulling the vocal soulful while the exclude
list said `soulful crooning`, so the prompt was arguing with itself. And
`half-sung half-spoken` became `spoken word — talking and complaining over the
beat, not singing, no melody, no flow, no swagger`: she was defaulting to the
genre's stock smooth female hip hop vocalist, and the fix is to state she isn't
a singer at all. Excludes gained the singing axis (`melodic singing, sung hook,
smooth rap flow, confident rapper, swagger, charismatic`). Style influence 85 → 90.

Lyric bracket cues moved from literary to blunt, on an escalating ladder
(`irritated` → `more irritated, nagging` → `shrill and strained, at the end of
her patience`) — consecutive emotion cues escalate reliably, and v5.5 obeys them.

**2026-07-30 — vocal tone rewrite.** The take was musically right but Karen sounded
like someone you'd want to hang out with — chill, cool, singing a great hip hop
tune. Words in the style prompt causing it: `warm and unhurried` in the lead mood
slot, `Comedic deadpan, never aggressive`, `polite, patient`, `dry conversational`
— and **`angry` in the exclude list**, which suppressed the exact register wanted.

Fixed by *deleting*, not adding (adding "irritated" on top of "patient" averages
into the same take). The vocal clause was rebuilt around tightness rather than
volume — nasal, pinched, over-enunciated, sing-song condescension — and moved to
the front of the prompt. `warm and unhurried` survives, reassigned to *the band*.

Excludes lost `angry` and `aggressive rap`, gained a description of the take we
don't want: `smooth r&b vocals, soulful crooning, laid-back flow, chill, cool,
breezy, sultry, relaxed delivery`. `shouted vocals, screaming` stay — she never
raises her voice, that's the joke.

Lyric words unchanged. Bracket cues rewritten throughout (`deadpan New York
drawl` → `nasal clipped New York complaint`, `same deadpan` → `more exasperated,
sighing between the lines`), plus three elongated vowels for sing-song sarcasm
(`Sweeeetheart`, `hoooney`, `lo-o-ovely`) and one on the final chorus only
(`Take your ti-i-ime`) so the last hook lands harder than the first two.

Sliders moved to style influence **85** (the vocal description is now specific,
and high adherence rewards specific vocabulary) / weirdness **50** (down from 60 —
the beat works, don't let it reinvent).
