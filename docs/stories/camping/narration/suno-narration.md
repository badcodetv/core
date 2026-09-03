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
>
> **External sweep 2026-09-01** (round 10's research pass), four sources, all practitioner-grade:
> [Jack Righteous — spoken narration workflow](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-narration-workflow)
> (the labels, the prose layout, the negations-in-Style templates) ·
> [Jack Righteous — spoken word guide](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-word-when-the-world-was-a-whisper) ·
> [hookgenius — Suno prompt guide 2026](https://hookgenius.app/learn/suno-prompt-guide-2026/)
> (⚠️ the dissent: *"Suno doesn't support 'don't do X' directly"*) ·
> [roo — the formula that actually works](https://roo.beehiiv.com/p/suno-ai-prompt-guide-2026-copy-paste-templates-the-formula-that-actually-works)
> (the 5–8 tag / 15–30 word ceiling, and *"short prompts expose conflicts; long prompts hide them"*).
> **Second sweep 2026-09-01** (round 11, after round 10's take), two more:
> [dynamic control guide](https://acetaggen.com/blog/silent-architect-pause-space-hard-cut-dynamic-control-suno)
> (*"flat verse at constant volume"* is the default — a build has to be asked for; `[Energy: High]` as
> an untested level lock) ·
> [achieving specific vocal styles](https://www.anywiki.net/sunoai/achieving-specific-vocal-styles-in-suno-ai)
> (*"adding a geographical location can dramatically influence the accent and delivery"*).
>
> **None of it is tested by us.** Where it conflicts with a finding in the round log, the round log wins.
>
> ✅ **Round 10's result is promoted out of this sheet**, per `session-method.md`: the talking recipe
> is now [`suno-voices.md` Thread 5](../../../suno-gpt/suno-voices.md), the superseded parentheses
> recipe is annotated in `files/suno-tag-mechanics.md`, and the `suno-prompt` skill carries
> *"Getting a man to TALK"*.

## 🔴 RULED 2026-09-01 — this sheet's job is now the VOICE, not the narration

**Jack, after round 14: *"it sounds good but there is still music. it sings it sometimes."***

✅ **The voice is won and it is worth keeping.** Fourteen rounds produced a northern, mid-range,
intonating, deadpan working-class Manchester narrator, and Jack has confirmed it.

🔴 **But Suno cannot deliver the narration, and the reason is structural, not a prompting failure.**
This sheet's own §1 says it: **Suno cannot make silence.** It is a music generator. A bed is always
present and a sung phrase is always one re-roll away — which is exactly the three faults that
followed the voice being right: **music under it, occasional singing, and delivery on the grid.**

🔑 **So the lane changes, and the fourteen rounds are not wasted — they are the input.** The
approved take becomes the **reference clip** for a free local text-to-speech cloner, which has no
bed, no bar and no melody by construction. **The ruling and the engine ranking are in
[`voice.md`](./voice.md) → "RULED 2026-09-01 — go local, and clone the Suno take."**

**What this sheet is still for:** generating the *reference clip*. Round 14 (A6) is still worth
running once — a cleaner, bedless take makes a better clone — but **the full 21-line run does not
happen here**, and §4's saved-Voice consistency stack is superseded by the cloner.

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
| 9 | `Northern English spoken word, British kitchen-sink realism` (candidate F) | plain, hard, weathered mid range with grit | 🔴 **read like a poem** — and so was every round before it. The fault was the genre word, in all four boxes |
| **10** | **`Trip hop skit, 80 BPM, a man talking over a beat`** (A-min) · **`Audiobook narration, radio drama`** (B) | **deep, dry, weathered, ordinary speech rhythm** | ✅🔴 **HE TALKED.** Jack: *"ten times better, as the man talks not doing spoken word."* **The ten-round poetry fault is solved and the finding is promoted to `suno-voices.md` Thread 5.** Two new faults: **American accent**, and **the voice goes quiet as if waiting for a beat to drop** |
| **11** | **`Madchester skit, British, 80 BPM, a man talking over a beat`** (A2) | `deep, dry, weathered, gritty` | 🔴 **Still American, and now too deep.** ✅ Talking held. **The Style box was not ignored — it was outvoted by the Exclude box**, which held 37 British-coded bans against 3 British words, `Madchester baggy` among them |
| **12** | **`Madchester skit, Britpop snarl, Manchester, British`** (A4) | 🔑 **`mid-range, nasal and adenoidal, sandpaper rasp, sneering`** — depth re-banned | ⬜ untested. **Three changes: 45 British-coded bans cut from Exclude · `deep` → `mid-range` + nasal articulation (the Liam register) · pitch told to move** |
| **13** | 🔑 **`Madchester monologue, Britpop snarl, Manchester, British`** (A5) — **`skit` is deleted** | unchanged from 12 — `mid-range, nasal and adenoidal, sandpaper rasp, sneering`, plus a sharper intonation clause | ⬜ untested. 🔴 **The accent audit found five American-coded signals still in the atom against two strong British ones.** `skit`, `over a beat`, `dusty` and the four `American …` bans are all gone; the depth and intonation fixes from 12 are untouched |
| **14 — current** | **`Madchester monologue, Britpop snarl, Manchester, British`** (A6) — **voice casting untouched** | unchanged | ✅🔴 **THE VOICE IS RIGHT.** Jack: *"the voice is spot on now."* Accent, depth and intonation are all solved and **nothing in the voice clauses may be touched again.** New and final fault: **he is saying it TO THE BEAT instead of just talking.** Round 14 changes only the rhythm family — `80 BPM` deleted, the drum loop replaced by a pulse-less underscore, `free pacing` added |

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

### 🔴 Round 10 — "it's being read like a poem", and why that was inevitable

**Jack, 2026-09-01: *"it is spoken like it is a poem, I guess that is the problem with spoken word
being in the prompt."*** That is the right diagnosis and it is worse than it looks. **`spoken word`
is not a delivery mode. It is a performance-poetry genre** — slam, dub poetry, performance poetry —
and its canonical delivery is *metrical, end-stopped and declamatory*. We asked for a poem.

🔑 **And we asked 33 times.** `spoken word` appears in **every box in the atom**: the Style box pool
word, the My Taste line, and **all 29 bracket cues**. There is no box left over for anything else to
win in. Rounds 1–9 changed the adjectives around it and never touched the noun.

**Three separate mechanisms were voting for a poem, not one.**

| # | Cause | Why it makes a poem |
|---|---|---|
| 1 | **The genre word** | `spoken word` selects the poetry pool. A pool is a person, and this one is a performance poet |
| 2 | 🔑 **The lyric LAYOUT** | 29 lines, each its own bracketed section, blank line either side. **Suno reads a section break as a musical event** — so it lands the line, pauses, and restarts. That *is* the slam cadence, drawn as a page. **This was never a wording problem** |
| 3 | **The all-parentheses recipe** | Already flagged in this sheet as an untested suspect. Stacked on 1 and 2 it triple-votes for declamation |

⚠️ **Cause 2 is the one nobody had looked at**, and the repo half-knew: `lyricist-playbook.md` §3 —
*"when a cue is ignored, simplify rather than escalate… a tempo fault is now a reason to strip cues
before trying anything else"* — and its narration recipe is **`[Monologue]`, a minimal style box, and
short non-rhyming conversational sentences**, not a cue per line. Our escalation ladder
(`[spoken word]` → `[spoken word speech]` → `[spoken word speech talking]`) came from the producer
corpus and the playbook already records the tension. **This round resolves it against the ladder.**

### 🔑 The reframe: stop fighting for a cappella. Ask for a thing that exists.

**Jack's own idea is the fix, and it has a name — the *skit*.** A rapper talking over a beat before
the rap is a real, heavily-recorded form: the **hip hop skit / album interlude / spoken intro**.

**Suno cannot make silence.** So the two things we can actually ask for are:

| What we ask for | What is in the training data | What we get |
|---|---|---|
| A northern man talking over **nothing** | Poetry recordings, almost exclusively | **A poem.** Nine rounds of evidence |
| A northern man talking over **a low loop** | Skits, intros, interludes, radio drama, documentary VO — enormous | **A bloke talking** |

🔑 **So the beat is not a cost, it is the casting mechanism** — and it is **free**, because
[§5](#5-getting-the-voice-out--narration-is-a-stem-not-a-track) already delivers narration as a
**vocal stem**. We were paying nine rounds of casting damage to avoid an instrument we throw away
anyway. Jack's *"a whole song of just talking and we silence the instrumental in the studio"* is
exactly the existing workflow, and it removes the `a cappella` fight that cost rounds 3 and 4 and
about a third of the Exclude box.

🔑 **The rule that replaces the a-cappella ban: MELODY makes him sing; RHYTHM does not.** This
sheet's own evidence says so — *"British + spoken word + a bouncy **pitched** instrument is music
hall"*, and round 4's singing was caused by a glockenspiel and a French horn. **Pitched instruments
stay banned. A drum loop comes off the ban list**, because nothing about a drum invites a melody.

### 🔧 A stale ban, running the other way: **deep**

Rounds 1 and 4 came back *"too low"*, so `deep voice, low voice, bass voice, baritone, booming,
boomy, sub bass` went in the Exclude box and have sat there for six rounds. **Jack now asks for
"an interesting northern English deep voice."** Those bans would silently remove the exact thing
being requested — the round-8 catch running in reverse. **`deep` is lifted and is back in the Style
box.**

⚠️ **Why it is safe to lift now, when it was not in round 2:** the fault in rounds 1 and 4 was
*deep **and** monotone **and** unmodulated* — and round 5 found the real culprit was the word `flat`
casting a monotone pitch. **Depth was convicted on the monotone's evidence.** With `flat` gone and
conversational rhythm asked for explicitly, deep is a texture, not a drone.

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

### 🔴 Round 13 — the accent audit: count what NAMES America, in every box

**Jack, 2026-09-01: *"there must be something in there that is causing a conflict between the
accents."*** There is, and it survived round 12 because round 12 only audited the **Exclude** box.
🔑 **The Style box has been carrying an American word in genre position since round 10, and this
sheet convicted that word itself in §4 of Thread 5 — then kept it.**

`Madchester skit` is **a British place name welded to an American form-word**, in the one slot that
decides accent. That is the conflict, written down, in the first two words of every round since 10.

**The count that should have been run on both boxes at once** (`suno-voices.md` §4a's own rule,
applied to the box it was not applied to):

| Box | American-coded | British-coded |
|---|---|---|
| **Style (A4)** | 🔴 **`skit`** (genre position — *tested* as carrying US hip-hop gravity, Thread 5 §4) · **`a man talking over a beat`** (hip-hop framing — *over a beat* is the form's own phrase) · **`dusty` drum loop** (US boom-bap / crate-digging production vocabulary) | `Madchester`, `Britpop` (**pool words — strong**) · `Manchester`, `British`, `northern` (**adjectives — tested as buying nothing**) |
| **Exclude** | 🔴 `American accent, American vocal, transatlantic, southern drawl` · `US rap, young MC, rapping, bars, flow, trap` | the poetry pool (kept deliberately) |
| **My Taste** | `not rapping` | `working-class Manchester man` |

🔑 **Strong British: 2. Strong American: 3.** Every round since 10 has been a coin-toss the American
side was winning, and no amount of adjective surgery on `Manchester` / `British` / `northern` could
change it — those are the exact words §2a and §4 both record as buying nothing.

#### The four `American …` bans go, and here is the argument

They have been in the Exclude box through **rounds 10, 11 and 12, and he was American in every
one.** ✅ **They are tested as inert.** Two mechanisms could explain that, and both say delete:

| | |
|---|---|
| **If §4 is right** — nationality is a genre lever and the Exclude box cannot reach it | they do nothing, so they are four words of dilution in a box the model reads |
| **If §5's negation rule is right** — *"naming a thing puts it in the prompt however the rest of the sentence qualifies it"*, and `spoken word, not singing, no melody, no flow, no swagger` **generated a male rapper** | they are actively naming America four times against `Madchester` once |

⚠️ **`US rap, young MC, rapping, bars, flow, trap` STAY.** They guard a different, real failure —
*he's talking but he's 22* (§6) — and unlike the accent bans they have never been tested as inert.
**They are the next cut if A5 still comes back American**, and that is round 14's lever, not this
round's.

#### What replaces `skit`, and the risk stated plainly

🔴 **`skit` is the word that got him to TALK.** Deleting it is the one genuinely dangerous change in
this round, and it could bring the poem back. **`monologue` takes its job** on three grounds:

1. It is a **talking word with no nationality and no genre attached** — no US hip-hop gravity, and
   not a poetry pool the way `spoken word` is.
2. 🔑 **It matches the lyric label exactly.** `[Monologue]` is already the tested label in all five
   chunks, so the Style box and the Lyrics box now say the same word — which is this sheet's own
   redundant-reinforcement rule, for free.
3. It cannot name a *section between the songs*, which is the documented cause of the round-10
   ducking fault (Thread 5 §5). **Deleting `skit` may fix that too.**

⚠️ **If he recites again, `skit` is the revert** — put `Madchester skit` back and cut the Exclude
box's American bans instead, one axis at a time. **Do not go back to `spoken word` under any
circumstances.**

#### And the intonation, sharpened

Round 12 wrote `pitch rising and falling as he talks`, which is true of every human speaker and
therefore weak direction. **The Liam register's actual shape is a swoop up inside the sentence and a
drop away at the end of it** — the opposite of the question-mark lift the script's punctuation is
already avoiding. The clause is now `his pitch swoops up inside a sentence and drops away at the end
of it`, and `drawn out` became **`leaned on`**, which is the vowel behaviour rather than a duration.

### ✅🔴 Round 14 — the voice is right; he is talking TO THE BEAT

**Jack, 2026-09-01: *"the voice is spot on now, however it still sounds like he is saying it to a
beat, instead of just talking, which will not fit the narration."*** 🔑 **Accent, depth and
intonation are closed.** The A5 voice clauses are the most expensive thing in this sheet — fourteen
rounds — and **no round after this may edit a word of them.** This round touches the rhythm family
and nothing else.

#### The diagnosis: three things in the atom declare a grid, and the voice aligns to it

| # | What says "there is a grid" | Why it locks the delivery |
|---|---|---|
| 1 | 🔴 **`80 BPM`** | A stated tempo **is** a grid. The community field guide's own words for BPM in the style field are *"**lock** BPM and key in the style field, and reuse the same values for every generation"* — it is the anchor you set when you want sections to splice on the beat. We put it in at round 10 to buy an unhurried delivery from the arrangement. **It bought a metronome instead.** |
| 2 | 🔴 **`One plain drum loop`** | A metronome with a tone. This was the round-10 casting mechanism and it did its job — but see the correction below |
| 3 | 🟡 `Madchester`, `Britpop snarl` | Music-scene pools; their native vocal sits on the bar. **Kept anyway** — they are what makes him northern, and §4c says never trade the accent |

🔑 **The round-10 rule was half right, and this is the correction.** It read *"MELODY makes him
sing; RHYTHM does not"*, and it was written to justify lifting the drum bans so the skit pool could
cast a talker. It worked — and it hid the other half:

> **Melody makes him sing. Rhythm makes him rap. Narration wants neither — it wants a bed with no
> pulse.**

A man performing to a bar is the same fault as a man reciting a poem: **a performance, not speech.**
The skit recipe traded the poem for the bar and called it done.

#### The fix: not silence, not a beat — a **bed**. The third option nobody tried

⚠️ **The obvious move is to delete the bed, and it is the wrong one.** A cappella is what produced
the ten-round poem, and Thread 5's whole finding is that *a man talking over nothing* barely exists
in the training data. **Deleting the loop walks straight back into round 9.**

✅ **The research says there is a third thing, and every practitioner narration template uses it: an
UNDERSCORE** — a low, non-metrical ambient bed. Four independent 2026 guides describe narration the
same way and **not one of them puts a drum under it:**

| Source | The bed it prescribes |
|---|---|
| [Jack Righteous — narration workflow](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-narration-workflow) (documentary template) | `minimal ambient underscore, slow subtle pulse, low dynamics, voice-forward clean mix` |
| The same guide's **poetry** template | 🥇 `close dry voice, sparse … ambient texture, **free pacing**, no melodic vocal` |
| [The audiobook / storytelling prompt set](https://james-palm.medium.com/suno-ai-prompts-audiobook-storytelling-music-3761f7eec73f) | `restrained documentary instrumental … restrained dynamics leave space for narration` |
| [The community field guide](https://github.com/mttkllr/suno-field-guide) | *"Hyphens = speed. Punctuation = breath. Line breaks = phrases."* — and **no tested `free time` / `rubato` / `no-tempo` tag exists**, so this is a Style-box job, not a meta-tag job |

🥇 **`free pacing` is the single most valuable phrase the research turned up.** It is the only direct
anti-grid instruction in the whole corpus, it comes from a worked narration template, and it says
what we want in two words: *the pauses fall where he decides, not where the bar does.*

⚠️ **What the research explicitly does NOT support:** there is no `[Free Time]`, `[Rubato]` or
`[Ad Lib]` tag in any tested reference. The one adjacent finding — shifting each line 5–15 ms off the
grid — is a **DAW** fix applied after generation, and it is worth knowing as the floor if prompting
fails, since narration ships as a stem into Premiere anyway (§5).

#### The four changes, all in the rhythm family

| Out | In | Why |
|---|---|---|
| 🔴 **`80 BPM`** | *(deleted — no tempo stated at all)* | A number is a grid. Nothing in the corpus requires one, and its own guides call it a **lock** |
| 🔴 **`One plain drum loop that never changes and never gets quieter`** | **`Underneath, one low ambient underscore, no pulse and no rhythm, the same all the way through and never getting quieter`** | Keeps the bed that casts a talker; removes the metronome he is talking to. **The level clause survives inside it** — the ducking fault stays fixed |
| — | 🥇 **`Free pacing`**, front of the delivery clause | The corpus's one direct anti-grid phrase |
| — | **`pausing where the meaning breaks and never on a bar`** | The positive form of *off the grid*, in plain language rather than a negation |

⚠️ **What is deliberately NOT changed:** the whole voice clause, the pool words, and **every word of
the script.** The lyrics are already the corpus's prescribed shape — prose paragraphs, natural
punctuation, uneven sentence lengths, no rhyme — and *"line breaks = phrase/bar resets"* means
editing them re-opens the phrasing question the round-10 layout fix already closed. **If the cadence
is still gridded after A6, the lyrics are the next lever, not the voice.**

#### 🔧 Exclude: the round-10 drum lift is reversed, knowingly

Round 10 took `drums, drum kit, breakbeat` **off** the ban list under the melody-not-rhythm rule.
That rule is now corrected, so they go back with the rest of the grid family behind them: `drums,
drum kit, drum loop, percussion, breakbeat, beat, kick, snare, hi-hats, groove, four to the floor,
pulse, metronome, quantized, on the beat, in time with the beat, rhythmic delivery, cadence,
syncopation, bars, rap flow`.

🔴 **Round 14 also caught a stale ban that would have strangled its own fix: `underscore` was
banned.** It went in at round 4 inside `film score, underscore, orchestral score`, meaning *a film
cue*. This round's Style box asks for **`one low ambient underscore`** — so the two boxes were about
to contradict each other on the one word the whole round rests on, and the take would have come back
with **no bed at all**, which is round 9, the poem. **`underscore` is lifted.** `film score,
orchestral score, thriller score, cinematic swell` still keep an orchestra out; `melody, chord
progression, chords, synth lead, pad, ambient pad` still keep it unpitched.

⚠️ **That is the third stale ban in four rounds** (round 8's `warm`, round 12's 45 British words,
round 13's `bassline`). 🔑 **The check is now part of the round, not an afterthought: before pasting,
grep the Exclude box for every noun in the new Style box.** One minute, and it has cost four rounds.

⚠️ **The round's real risk, stated plainly: the bed was the casting mechanism.** Weaken it too far
and the poem comes back. **`ambient underscore`, `ambient bed`, `drone` and `room tone` are NOT
banned** — that distinction is what the whole round rests on, and it is why this is a swap and not a
deletion.

#### If A6 is still on the grid — the ladder, in order

| Try | Why |
|---|---|
| 1 · **Re-roll A6 twice** | Cadence is as probabilistic as everything else here, and the sheet's rule is re-roll before rewriting |
| 2 · **B2 — form word to `Madchester documentary voiceover, radio drama`** | 🔑 Thread 5's reframe applied to rhythm: *ask for a form that exists.* The form that exists **with no beat** is documentary VO / radio drama / audiobook — variant B, skipped for eleven rounds only because it had no British lever. **§4c removed that objection**: `Madchester` supplies the accent, the form word supplies the un-gridded delivery. ⚠️ It changes the form word, the one thing that has ever moved the voice — **only after the re-rolls** |
| 3 · **Widen the sentence-length spread in the lyrics** | `lyric-craft.md`: *measure syllables per line and look at the spread.* Even lengths let a bar pattern emerge; a 27-word sentence beside a 3-word one cannot sit on one |
| 4 · **Ellipses, deliberately placed** | The field guide's pacing table names the ellipsis as the documented drag, and the script already keeps three |
| 5 · **The floor — fix it in Premiere** | Nudge each line 5–15 ms off the grid on the vocal stem. Narration ships as a stem anyway (§5) |
| ❌ **Never** | Delete the bed entirely, or re-open the voice clauses |

## 2. Suno prompt — round 14, paste all four, in this order, every round

**Never trust what a box already contains.** "Reuse Prompt" silently carries old lyrics forward,
and a stale Lyrics box is inaudible as such — it just sounds like the Style box is being ignored.
That cost the Karen track four rounds.

🔑 **This is a whole-atom change** — all four boxes moved together, per the atom rule in
`.claude/skills/suno-automation`. Round 9's boxes are recorded in the round log and are superseded.
**Do not mix them**; a round-9 Style box under round-10 lyrics is a hybrid nobody designed.

### My Taste

Swap this in for the session and **restore the freedom token afterwards** — My Taste biases every
generation, cannot be turned off, and is account-wide.

```taste
Vocals: one male voice, and he is TALKING — not singing, not reciting. A working-class Manchester man in his forties, telling you something across a table: mid-range, nasal and adenoidal, a sandpaper rasp on it, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Close and dry right on the microphone. Free pacing — ordinary conversational speech, uneven sentence lengths, pausing where the meaning breaks and never on a bar, and his pitch swoops up inside a sentence and drops away at the end of it — never droning, never on one note. Bored, sarcastic and certain, giving nothing away, never signalling a joke. The voice stays loud and right in front the whole way through, never getting quieter. Music: one low ambient underscore underneath, no pulse and no rhythm and no drums of any kind, the same all the way through, no melody and no chords, nothing ever builds and nothing ever drops. Register: grim and funny, played completely straight.
```

### Style — variant A · the trip-hop skit 🥇

**The recommended one, and the pool changed after research on 2026-09-01.** The first draft said
`hip hop skit`, whose risk is named in §6: **that pool casts a young MC.** **Trip hop removes the
risk structurally** and is a better fit on four counts at once:

| | |
|---|---|
| **It is British by origin** | Bristol, not Atlanta. Nationality rides on the genre tag, and this tag is already ours |
| **It is slow** | Downtempo, 80-ish BPM. The brief wants *unhurried and certain*, and for the first time the pool agrees instead of being fought |
| **Its native vocal is a man half-talking, low** | Low, close, mumbled male delivery over a beat is the genre's signature — not a performance-poetry register, and not a rapper's |
| **Its beats are dusty and unpitched** | Which is exactly the bed the melody-not-rhythm rule allows |

#### 🥇 A6 — the box that gets pasted (round 14)

🔴 **The voice clauses are frozen.** Every word from `Working-class Manchester lad` to `drops away at
the end of it` is byte-identical to A5, which Jack confirmed as spot on. **Only the tempo, the bed and
the pacing move.**

🔴 **Everything above this line is commentary. The block below is the whole Style box — paste it
all, and paste nothing else.**

```
Madchester monologue, Britpop snarl, Manchester, British, one man talking, not singing. Working-class Manchester lad in his forties. Mid-range voice, nasal and adenoidal, sandpaper rasp, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Close and dry on the microphone. Free pacing, ordinary conversational speech, pausing where the meaning breaks and never on a bar. His pitch swoops up inside a sentence and drops away at the end of it. Bored, sarcastic, deadpan. Underneath, one low ambient underscore, no pulse and no rhythm, the same all the way through and never getting quieter. Voice loud and in front all the way, no singing, no melody.
```

#### B2 — the fallback if A6 is still on the grid (step 2 of the ladder)

Voice clauses identical again. **Only the form word changes** — `monologue` becomes the two forms
where a man talks with no beat under him at all.

```
Madchester documentary voiceover, radio drama, Manchester, British, one man talking, not singing. Working-class Manchester lad in his forties. Mid-range voice, nasal and adenoidal, sandpaper rasp, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Close and dry on the microphone. Free pacing, ordinary conversational speech, pausing where the meaning breaks and never on a bar. His pitch swoops up inside a sentence and drops away at the end of it. Bored, sarcastic, deadpan. Underneath, one low ambient underscore, no pulse and no rhythm, the same all the way through and never getting quieter. Voice loud and in front all the way, no singing, no melody.
```

#### A5 — round 13's box, superseded (the voice was right; the delivery was on the grid)


**One axis moves this round: the American-coded words come out.** Everything the round-12 box did
for depth and intonation is untouched, so if he is still too deep or still droning, that is A4's
fix failing and not this one's.

| Out | In | Why |
|---|---|---|
| `skit` | **`monologue`** | 🔴 The only American word in genre position, and *tested* as carrying US hip-hop gravity. `monologue` is a talking word with no nationality, and it **matches the `[Monologue]` lyric label** |
| `a man talking over a beat` | **`one man talking, not singing`** | *over a beat* is hip hop's own phrase for exactly this. The speech act survives; the form's nationality does not |
| `dusty` drum loop | **`plain` drum loop** | US boom-bap production vocabulary. `plain` says unpitched and unremarkable with no scene attached |
| `pitch rising and falling` | **`swoops up inside a sentence and drops away at the end of it`** | Rising and falling is true of all speech. This is the Liam shape specifically — and it is the opposite of the question-mark lift |
| `drawn out` | **`leaned on`** | Vowel behaviour, not duration. `drawn out` sits next to `languid`, which is banned |

**Five British-coded words, zero American ones, 80 words.** ⚠️ Still over the 15–30-word external
ceiling, knowingly: the trim ledger is unchanged — `Bored, sarcastic, deadpan` first, then
`Working-class Manchester lad in his forties`.

🔴 **Everything above this line is commentary. The block below is the whole Style box — paste it
all, and paste nothing else.**

```
Madchester monologue, Britpop snarl, Manchester, British, 80 BPM, one man talking, not singing. Working-class Manchester lad in his forties. Mid-range voice, nasal and adenoidal, sandpaper rasp, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Close and dry on the microphone. Ordinary conversational speech, his pitch swoops up inside a sentence and drops away at the end of it. Bored, sarcastic, deadpan. One plain drum loop that never changes and never gets quieter. Voice loud and in front all the way, no singing, no melody.
```

#### A4 — round 12's box, superseded (the accent audit found `skit` in it)


🔴 **The accent fix in this round is mostly in the EXCLUDE box, not this one.** See the Exclude
section below: eleven rounds of bans had accreted into 37 British-coded words against 3 in the Style
box, so `Madchester` was outvoted before it started. **Fixing the Style box alone would not have
worked, and did not.**

**What changes here, and why — three things.**

**1 · More British signal, front-loaded.** `Madchester skit, Britpop snarl, Manchester, British` —
four British-coded words in the first six, which is the repo's redundant-reinforcement rule applied
properly. `Britpop snarl` was cut back in round 4 for growing a guitar band; **it comes back
deliberately.** 🟢 The trade is sound: narration ships as a **vocal stem** (§5), so an unwanted band
is an inconvenience, while a wrong accent is a dead take. **Take the instrument risk, never the
accent risk.**

**2 · `deep` → `mid-range`, permanently.** Jack: *"the voice is too deep."* Rounds 1 and 4 said the
same, the ban was lifted in round 10 on Jack's own "deep northern voice" request, and round 11
reproduced the fault. 🔑 **The resolution: `deep` was never the right word for what was wanted.**
What was wanted is *weight and grain* — those are **texture** words (`rasp`, `grit`, `sandpaper`),
not **pitch** words. Pitch is now stated as `mid-range` and the depth family is back in Exclude for
good.

**3 · He has to intonate — the Liam Gallagher register, translated.** 🔴 **The name goes nowhere near
a box** (house rule: artist names never enter the prompt; steer through the four axes Suno renders).
Translated:

| Axis | What Liam actually is | What goes in the box |
|---|---|---|
| **Pitch** | not deep — a nasal mid-range | `mid-range voice` |
| **Texture** | adenoidal, sandpapery | `nasal and adenoidal, sandpaper rasp` |
| **Articulation** | hard flat Manchester vowels, dropped consonants, vowels dragged out | `hard flat northern vowels, dropped consonants, vowels drawn out and drooping` |
| **Delivery** | sneering, cocky, lazy, and it **moves** | `sneering and cocky` · `pitch rising and falling as he talks` |

⚠️ **And the word `level` is gone from the ducking clause.** Round 11 wrote `exactly the same level
start to finish` meaning *loudness* — but `level` is a **pitch** word too, and `flat`/`level` are
precisely what caused the round-5 monotone. It now says `never changes and never gets quieter`.

⚠️ **83 words, over the ceiling and knowingly so.** This round adds a whole axis (articulation and
intonation) plus three extra British front-load signals. **If the take is good but muddy, the trim
ledger is: `Bored, sarcastic, deadpan` first (derivable from `sneering and cocky`), then
`Working-class Manchester lad in his forties`.**

🔴 **Everything above this line is commentary. The block below is the whole Style box — paste it
all, and paste nothing else.**

```
Madchester skit, Britpop snarl, Manchester, British, 80 BPM, a man talking over a beat. Working-class Manchester lad in his forties. Mid-range voice, nasal and adenoidal, sandpaper rasp, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels drawn out and drooping. Close and dry on the microphone. Ordinary conversational speech, pitch rising and falling as he talks. Bored, sarcastic, deadpan. One dusty drum loop that never changes and never gets quieter. Voice loud and in front all the way, no singing, no melody.
```

#### A2 — round 11's box, superseded (still American, too deep)

✅ **Round 10 worked on the thing it was built to fix. Do not touch that part of it.** The man
talked. `Trip hop skit`, `a man talking over a beat`, prose lyrics under `[Monologue]` and the whole
poetry pool in the Exclude box are now **tested and load-bearing** — the finding is promoted to
[`suno-voices.md` Thread 5](../../../suno-gpt/suno-voices.md).

🔴 **Two faults left, and this box changes exactly one clause for each.**

**Fault 1 — he was American.** This is `suno-voices.md` §2a for the **third** time, and the trap was
identical to round 2's: round 10 deleted `Northern English post-punk spoken word` to kill the poetry
noun, and that phrase was **also the only British lever in the prompt**. Two things it proves:

| | |
|---|---|
| 🔴 **Exclude bans do not control nationality** | `American accent, American vocal, transatlantic, southern drawl` were all in the box the whole time, and he was American anyway. Nationality is a **genre lever**, full stop |
| 🔴 **`Trip hop` is too weak to survive `skit`** | Trip hop is Bristol by origin, but `skit` carries US hip-hop gravity and appears to beat it. A weak British word in front of a strong American one loses |

🔑 **The fix is the front word, and it is a place, not an adjective.** `Madchester` is a
**pool-selecting scene name** whose default performer is a northern working-class man half-talking
over a loop — the exact character — and it is not a poetry pool. Externally corroborated: *"adding a
geographical location can dramatically influence the accent and delivery."* `British` then repeats
twice behind it, which is the sheet's own redundant-reinforcement rule.
⚠️ **Madchester's own failure mode is a baggy guitar band**; `guitar, indie rock, guitar band, live
band` are already in the Exclude box.

**Fault 2 — the voice went quiet, as if waiting for a beat to drop.** This is an **arrangement**
fault, not a vocal one, and the cause is in the pool word: **`skit` and `interlude` literally name a
short section between the songs**, so the model builds toward whatever it thinks comes next and ducks
the voice for tension on the way. ⚠️ **It is not Suno's default** — external guidance is that it
gives *"flat verse at constant volume"* unless a build is tagged, so the build was **asked for**,
which means the fix belongs in the Style box rather than in a new tag: `one dusty drum loop,
unchanging, exactly the same level start to finish` + `voice loud and in front the whole way`, with
the dynamics bans behind it in Exclude.

**65 words, 423 characters** — four more words than A-min while carrying two extra jobs. What paid
for them: `not singing` at the front (duplicated `no singing` at the back), `uneven sentence lengths`
(derivable from the prose lyrics) and `never signalling a joke` (derivable from `deadpan`).

⚠️ **This round moves two variables, and that is deliberate** — but they are **separable by ear**,
so the round is still attributable:

| What you hear | Which fix failed |
|---|---|
| Northern, but still ducks | the **level clause**. Escalate to the untested `[Energy: High]` lever (§6) |
| Level, but still American | the **front word**. Go to A3 below |
| Both still wrong | neither lever is strong enough — the pool is wrong, not the wording |

🔴 **Everything above this line is commentary. The block below is the whole Style box — paste it
all, and paste nothing else.**

```
Madchester skit, British, 80 BPM, a man talking over a beat. British northern English working-class man, forties. Deep, dry, weathered, gritty. Hard northern consonants. Close and dry on the microphone. Ordinary conversational speech rhythm. Bored, sarcastic, deadpan. One dusty drum loop, unchanging, exactly the same level start to finish. Voice loud and in front the whole way, no singing, no melody, no build, no drop.
```

#### A3 — the fallback if `Madchester` still comes back American

`suno-voices.md` names `UK grime`, `UK garage`, `UK hip hop` as **the strongest British-vocal
controls that exist**. We have avoided them for nine rounds for one good reason — §2b, *a pool is a
person*, and these cast a **young MC**. But a young northern MC is a *different* wrong answer from an
American, and it is one the Exclude box has a real chance against, where it has none against
nationality.

⚠️ **Updated round 13: `skit` came out of this box too.** The audit convicts it wherever it appears, and A3's whole argument is that `UK hip hop` and `British rap` are strong *British* pools — welding an American form-word to them repeats the exact mistake A5 is fixing. ⚠️ **A3 also drops the `US rap, young MC, rapping, bars, flow, trap` bans**, which would otherwise ban the pool it is casting (`suno-voices.md` §4a: never ban a genre adjacent to the pool you are casting). **Take the young-MC risk here — it is a different wrong answer from an American, and one the rest of the box can fight.**

```
UK hip hop monologue, British rap, Manchester, British, 80 BPM, one man talking, not singing. Working-class Manchester lad in his forties. Mid-range voice, nasal and adenoidal, sandpaper rasp, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Close and dry on the microphone. Ordinary conversational speech, his pitch swoops up inside a sentence and drops away at the end of it. Bored, sarcastic, deadpan. One plain drum loop that never changes and never gets quieter. Voice loud and in front all the way, no singing, no melody.
```

#### A-min — round 10's box, superseded but tested

**This is the box that proved the talking recipe**, and it is the revert target. Its only known
faults are the two A2 fixes.


🔴 **Trimmed 2026-09-01 after external research, and the trim is the point.** The prose draft below
(**A-full**) is 82 words. Every current external guide puts the Style field at **5–8 comma-separated
tags, 15–30 words**, warns that **over ten tags produces conflicting signals**, and states the reason
plainly: *"short prompts expose conflicts; long prompts hide them… name one genre clearly instead of
three loosely and Suno commits instead of averaging."* `lyricist-playbook.md` §3 independently
prescribes a **minimal style box** for narration specifically. **A-full is over every one of those
ceilings**, and rounds 1–9 are what a long box costs: nine rounds of adjective surgery inside a box
where nobody could hear which word was doing what.

```
Trip hop skit, 80 BPM, a man talking over a beat, not singing. Northern English working-class man, forties. Deep, dry, weathered, real grit in it. Hard northern consonants. Close and dry on the microphone. Ordinary conversational speech rhythm, uneven sentence lengths. Bored, sarcastic, deadpan, never signalling a joke. One slow dusty drum loop, very low. Voice-forward mix, no singing, no melody.
```

**61 words, 400 characters, and every axis this sheet fought for is still in it** — pool, speech act,
region and class, texture, room, rhythm, attitude, bed, mix. What came out was **duplication, not
jobs**: `downtempo spoken interlude` (a second pool word next to `Trip hop skit`), `not rapping, not
reciting` (both already in the Exclude box, where negations belong), `no chorus` (ditto), and the
sentence connectives. ⚠️ **It is still twice the guides' word ceiling.** Getting to 30 means dropping
the texture axis — which is Jack's explicit ask — or the room axis, which is what fixed the echoing
take. **So the cut stops here, and a further cut is round 11's lever, not this round's.**

#### A-full — the prose draft, kept as the fallback

Paste this **only** if A-min comes back thin, generic, or under-specified — i.e. the fault is *too
little direction*, not the wrong direction.

```
Trip hop skit, downtempo spoken interlude, a man talking over a beat, 80 BPM. Not singing, not rapping, not reciting — talking. Northern English, working class, forties: deep, dry and weathered, real grit in it, hard northern consonants, close and dry right on the microphone. Ordinary speech rhythm — uneven sentence lengths, some run together, some stop dead. Bored, sarcastic and certain, never signalling a joke. Underneath, one slow dusty drum loop, very low. Voice-forward mix, no singing, no chorus, no melody.
```

🔧 **`80 BPM` is in the box deliberately** — naming a tempo is reported to stabilise rhythm, and a
slow one buys unhurried delivery from the arrangement instead of from an adjective competing for
attention. This is the round-6 pace problem solved by casting rather than by argument.

✅ **`no singing, no melody` in the Style box is now externally corroborated, and the doctrine
conflict is real.** House doctrine says negations go in the Exclude box. **Every field-tested
narration template we can find puts them in Style** — the Jack Righteous 2026 narration workflow's
three worked examples all end `voice-forward mix, no lead melody, no sung chorus` / `voice dominant,
no singing, no chorus`. ⚠️ **And one 2026 guide flatly contradicts that**, saying Suno *"doesn't
support 'don't do X' directly — be so specific about what you want that there's no room for what you
don't."* **So this is an open split, not a settled rule.** Both boxes carry the negations here; if a
take is otherwise good, **this is still the first thing to try removing.**

### Style — variant B · the narrator, if A brings a rapper

🔴 **A's residual risk is still its pool.** `skit` carries hip-hop gravity even with `trip hop` in
front of it, and that pool casts a young MC — the exact failure mode §6 already lists. If take A is a
22-year-old, do not add adjectives — **switch pool to B**, which buys talking from the
audiobook/radio tradition instead of the hip-hop one. Everything else in the atom is identical.

```
Audiobook narration, radio drama, documentary voiceover. A man talking to you, not performing and not reciting. Northern English, working class, forties. Deep, dry and weathered, grit in the voice, hard northern consonants, close and dry right up on the microphone. Ordinary speech rhythm — uneven sentence lengths, running some sentences together and letting others stop dead. Bored, sarcastic and certain; whatever is funny is in the words and he never signals it. Almost nothing underneath.
```

### Exclude Styles

🔑 **Three deliberate changes from round 9, and each one reverses a standing ban.**

1. **The whole poetry pool is now banned** — `spoken word, performance poetry, poetry slam, dub poetry, recital, declamatory, verse, stanza, rhyming, metrical, incantation`. This is the round-10 fault named directly.
2. **`deep, low voice, baritone, booming, sub bass` are LIFTED.** Jack asked for a deep voice; those bans would have silently removed it. See the stale-ban note in §1.
3. **`drums, drum kit, breakbeat, a cappella`-driven bans are LIFTED, pitched instruments are not.** The rule is **melody makes him sing, rhythm does not** — round 4's singing came from a glockenspiel and a French horn, not from a drum.

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, autotune, harmonies, backing vocals, choir, spoken word, performance poetry, poetry slam, dub poetry, beat poetry, poetry reading, recital, recitation, declamatory, verse, stanza, rhyming, metrical, incantation, dramatic reading, over-enunciated, elocution, female vocal, sung female vocal, torch song, jazz vocal, soul vocal, sultry, seductive, US rap, young MC, rapping, bars, flow, trap, piano, glockenspiel, strings, violins, horns, melody, chord progression, chords, synth lead, pad, ambient pad, deep voice, low voice, bass voice, baritone, booming, boomy, sub bass, chest voice, growl, monotone, flat delivery, level delivery, unmodulated, robotic, machine voice, text to speech, computerised, comedic, novelty, parody, jaunty, playful, whimsical, bouncy, uplifting, laugh track, audience laughter, applause, live audience, epic trailer music, cinematic swell, film score, orchestral score, thriller score, suspense, tension strings, movie trailer voice, epic narrator, reverb, echo, telephone voice, distorted vocal, vocoder, double time, tempo change, fast delivery, rapid fire, breathless, hurried, frantic, manic, shouting, screaming, yelling, gentle, soft vocal, softly spoken, mellow, soothing, breathy, whispered, calm narration, languid, wistful, build, buildup, riser, drop, beat drop, pre-drop, breakdown, crescendo, decrescendo, swell, dynamic build, tension build, fade in, fade out, quiet passage, half time, vocal ducking, distant vocal, buried vocal, drums, drum kit, drum loop, percussion, breakbeat, beat, kick, snare, hi-hats, groove, four to the floor, pulse, metronome, quantized, on the beat, in time with the beat, rhythmic delivery, cadence, syncopation, bars, rap flow, chanting along, sing-song
```

🔴 **Round 12 CUT this box by 45 words, and that cut is the accent fix.** The ban list had grown
across eleven rounds into a dense statement of *not British* — **37 British-coded bans against 3
British words in the Style box** — so the Style box was not being ignored, it was being **outvoted**.
Full evidence: [`suno-voices.md` §4a](../../../suno-gpt/suno-voices.md).

| Removed, and why | Words |
|---|---|
| 🔴 **Self-cancelling** — added in the same round as `Madchester skit` | `Madchester baggy, jangly guitars` |
| 🔴 **Madchester's whole sonic signature** — banning it banned the pool | `indie rock, guitar band, post-punk band, band, rock band, live band, guitar, acoustic guitar` |
| 🔴 **Three of the four strongest British-vocal pools we have** | `grime MC, UK drill, road rap` |
| **British class registers** | `RP, received pronunciation, BBC newsreader, after-dinner speaker, posh, plummy, polite` |
| **British comedy registers** | `music hall, vaudeville, pantomime, panto, cabaret, variety show, oompah, sitcom, comedian, comedy club, stand-up comedy, kazoo, slide whistle, tuba, banjo, whistling` |

**Two blocks were ADDED, both for the "too deep" fault:** `deep voice, low voice, bass voice,
baritone, booming, boomy, sub bass, chest voice, growl` — 🔑 **`deep` is now banned permanently**, see
§1 — and `flat delivery, level delivery, unmodulated` beside `monotone`, because this round asks for
**intonation**.

⚠️ **What is kept despite being British-coded: the poetry pool.** `spoken word, performance poetry,
poetry slam, dub poetry` are the one thing in this sheet that is **tested as working** — they are what
stopped the ten-round poem. The trade is deliberate.

⚠️ **Round 13 deleted the American bans.** They sat in this box through rounds 10, 11 **and 12** and he
was American every time — ✅ **tested inert**, three rounds running. And by this repo's own negation
rule (`suno-voices.md` §5: *"naming a thing puts it in the prompt however the rest of the sentence
qualifies it"* — `no flow, no swagger` **generated a male rapper**) they were the only four words in
the whole atom that named America. **Gone: `American accent, American vocal, transatlantic, southern
drawl`.**

🔴 **Round 13 cut four more that were fighting the pool**, same rule as round 12's 45:

| Removed | Why |
|---|---|
| **`bassline`** | 🔑 **Madchester's signature instrument.** Banning it bans the pool — §4a's exact ruling, missed in round 12. `melody, chord progression, chords, synth lead, pad` still keep pitched melody out |
| **`mumbling, muttering, trailing off`** | 🔴 **That is the register Jack is asking for.** A slurred, swallowed, drooping delivery *is* the Manchester/Liam articulation. They were added in round 10 to fix the *ducking* fault — but ducking is a **loudness** fault and `vocal ducking, distant vocal, buried vocal` already cover it. **A level ban should never be spent on a delivery word** |
| **`chanting`** | Terrace-coded and British. `singing, melodic vocal, sung verses` already do the job |
| **`lo-fi vocal`** | Redundant next to `distorted vocal`, and it argues with the dusty-loop bed the pool wants |

⚠️ **`US rap, young MC, rapping, bars, flow, trap` are deliberately KEPT.** They guard the *he's 22*
failure (§6), which is a different fault and has never been tested as inert. **They are round 14's
cut, not this round's** — and A3 above already drops them, because there they would ban the pool.

### Lyrics — all five chunks

🔴 **Reformatted 2026-09-01, and this is the biggest single change in the round.** The words are
identical to the 2026-09-01 rebuild; **the layout is not.**

**Round 9 gave every one of the 29 lines its own bracketed section with a blank line either side.
That is stanza layout, and Suno reads a section break as a musical event** — it lands the line,
pauses, and restarts. That is the slam cadence drawn as a page, and no amount of wording fixes it.

🔑 **Externally confirmed 2026-09-01:** the community field guide states plainly that **"line breaks
signal phrase resets."** Twenty-nine lines is twenty-nine phrase resets — the machine was doing
exactly what the page told it to.

**So: one label per chunk, sentences run together into paragraphs, no parentheses, natural
punctuation.** Pauses now fall where the *meaning* breaks instead of every nine words.
`lyricist-playbook.md` §3 backs this — its narration recipe is **`[Monologue]`, a minimal style box
and short non-rhyming conversational sentences**, and *"when a cue is ignored, simplify rather than
escalate."* ⚠️ **This retires the `[spoken word]` → `[spoken word speech]` → `[spoken word speech
talking]` escalation ladder for narration.** The playbook already recorded the tension between the
ladder and the simplify rule; round 10 resolves it against the ladder. **Write the finding back into
`docs/suno-gpt/` once a take proves it either way.**

**One label, repeated identically: `[Monologue]`.** It is a *talking* word with no genre attached,
and it is the one both sources recommend — `lyricist-playbook.md` §3 and the Jack Righteous
narration guide independently name `[Spoken narration]` / `[Monologue]`. The only variation is the
single `{WARM}` crack in chunk 5.

✅ **The prose layout is corroborated too, and by the same guide that named the label.** Its
formatting rules for narration are, verbatim: *short sentences with natural punctuation · minimise
rhyme patterns · **paragraph breaks between ideas** · avoid chorus repetition or verse structures ·
write conversationally rather than as song lyrics.* Every one of those describes the chunks below and
contradicts round 9's stanza layout. 🔑 **Two independent sources now say the same thing about
narration, and neither of them is us** — which is as close to tested as this gets before a take.

🔧 **The escalation ladder, if `[Monologue]` is ignored** — and note this ladder is *lateral*, not
longer, per the simplify-don't-escalate rule:

| Try | Why |
|---|---|
| 1 · **`[Monologue]`** | No genre word anywhere. The default |
| 2 · **`[Spoken Word Narration]`** | ⚠️ Puts the poison phrase back in the lyrics box — but this is the **only** speech tag with a documented working example, and `Narration` qualifies it the way `spoken vocal` qualified `Madchester` in round 7. **Safe now in a way it was not before, because the Style box no longer selects the poetry pool** |
| 3 · **`[Interlude]`** | A validated base tag meaning a non-sung section. Least direction, least to fight |
| 4 · **No label at all** | Bare prose under a skit Style box. The purest form of *simplify rather than escalate*, and untried |

🔴 **Invented tags are not documented as working.** The community field guide is explicit that it
lists tested tags only and flags experimental ones as *"system may ignore"*. **So the label stays a
bare recognised word** — an earlier draft of this round used `[Skit — a man talking, not performing]`,
which is a description dressed as a tag and would most likely have been ignored silently.

#### Chunk 1 — 2008

```lyrics
[Monologue]

Two thousand and eight. Tarquin, star trader on the NatWest floor, betting other people's houses on leveraged E.T.F.s. He is the reason it happens. Pain infliction usually looks this banal. Nice tie, though.

Meet Bob. Middle manager. Normal. Off for a few days with his wife Jo, away from the stress of it. Can you blame him, really.
```

#### Chunk 2 — 2026

```lyrics
[Monologue]

Eighteen years on. Tarquin runs the biggest private equity firm in the country. It buys social housing. It does not rent them out. Empty pays better than full — the price climbs either way.

What a brilliant businessman. He ditched the tie, at least. Driving home he spots this lot. Rates up one percent next week. You chaps'll have a few more mates soon.

His car heater broke last week. Worst four days of his life. Three ways past a man in a tent. Ignore him. Politely say no — ignoring him with manners. Or stop. Have a guess which one's rarest.
```

#### Chunk 3 — therapy

```lyrics
[Monologue]

Tarquin sought professional help. He'd felt a feeling, first time since the devil's lettuce at uni. The therapist explains that empathy for the homeless is not an emergency. It doesn't sink in.

So he gives up, and prescribes the strongest psychedelic known to man for his car crash of a personality. Forgive the pun.
```

#### Chunk 4 — the car park

```lyrics
[Monologue]

Parks how he usually does. Bob is none too pleased. I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit.

Bob calls them wank tanks. Most common vehicle in this car park. Tarquin clocks him. Not a wrestle with his conscience — just a small acknowledgement that it's in there. Then he shuts it.
```

#### Chunk 5 — Wales, and the newspaper

```lyrics
[Monologue]

Wales. Tarquin has never sat on a floor before. And somewhere in all that he works out that the distance between him and the man outside the supermarket is about four bad months and a bit of luck.

Thunder. He's out of the tent with his heart in his throat. Christ, that's strong stuff. Give it an hour.

Bob's at the fire, telling him to look at the date. Twenty thirty-one. Last one they ever printed.

It's not the drugs. The headline says the machines took the jobs. It doesn't say who owns the machines. Same man who owns the flats.

[Monologue — warmer, quieter]

Where the hell have you been. You alright.

[Monologue]

The paper goes on the fire. Nobody says sorry; the cans do it. I know how this ends. I've never been sure about this bit. Watch what goes up.
```

### What was changed from Jack's script, and why

**Two passes are recorded here.** The first was synthesis-only. The second rebuilt the script.

#### Pass 1 — synthesis normalisation (the listener hears no change)

| Change | Why |
|---|---|
| `2008` → `Two thousand and eight`, `2026` → `Twenty twenty-six`, `2031` → `Twenty thirty-one` | Bare digits get read as digits, or sung |
| `ETFs` -> `E.T.F.s`, `IPA` -> `I.P.A.`, `1%` -> `one percent`, `4x4's` -> **`4 by 4's`** | Raw abbreviations and symbols are mispronounced. Normalise before synthesis, never after. 🔧 **Ruled by Jack 2026-09-01: `4 by 4's`, not `four by fours`** — the spelled-out form was not getting it right by ear. ⚠️ Noted for the next engine: spelling numbers out is normally the safer form, so **re-test this one on any engine that is not Suno** |
| `Ayahuasca` → `ayawaska` | Respell for **sound**, not for the dictionary. **No hyphens** — an in-word hyphen stretches the note, so a hyphenated or foreign word renders slow by default |
| `devils lettice` → `devil's lettuce` | The phrase is *devil's lettuce*; the original is a typo |
| `em` → `him` | Dialect elision is a mispronunciation risk for no gain — the flatness carries the register |
| Semicolons → full stops | Semicolons produce muddy pacing |
| `Can you blame em, really?` → `...really.` | 🔑 **A question mark lifts the pitch, which sounds eager. A full stop keeps it flat, which is the joke.** Same ruling as Karen's `Who knew.` |
| `I don't know what's worse:` → `...worse.` | A colon does the same lift as a question mark |
| `Uh,` dropped before `Nice tie though` | A filled pause is the first thing a music model swallows or sings. The comma before `though` does the same work reliably |
| Ellipses **kept**, in three places | A trailing pause *with weight* — a real control, placed where a joke needs air |

#### Pass 2 — the rebuild, 2026-09-01 (the listener hears a different script)

🔴 **The canon bug, fixed first.** Chunk 5 told Tarquin to look at the newspaper's date and then said
**"twenty twenty-six"** — the year the Shard already carries in scene 4. **The reveal revealed
nothing.** [`../year-device.md`](../year-device.md) ruled on 2026-08-30 that the on-screen clock is a
**two-instance** device (2008 on `1a`, 2026 on `4a`) and *"the third date is spoken, not shown — the
newspaper stops being a clock and goes back to being a prop."* **That line is the film's third date,
and now the only place 2031 exists in the whole script.**

| Beat added | Brief's demand | The line |
|---|---|---|
| **Scene 1 · cause** | The trading floor reads as **cause**, not backdrop; keep the function of *"He was the reason 2008 hit"* | `betting other people's houses on leveraged E.T.F.s` + `He is the reason it happens.` |
| **Scene 4 · the mechanism** | Housing bought and **left empty because asset inflation pays better than rent** | `It does not rent them out. Empty pays better than full — the price climbs either way.` |
| **Scene 4 · the pairing** | Sarcasm **pinned to an undeniable consequence** in the same beat | `What a brilliant businessman.` now lands **after** the empty flats, not before. Previously it was pinned to nothing — the brief's own *sarcasm with no consequence* trap |
| **Scene 5 · cold, not guilt** | *his car heater broke last week* — briefly cold, not sorry | `His car heater broke last week. Worst four days of his life.` replaces `It is a tad chilly, though...` |
| **Scene 6 · the three reactions** | 🔑 The line aimed at the audience's own behaviour, which works because it never says *you* | `Ignore him. Politely say no — ignoring him with manners. Or stop. Have a guess which one's rarest.` |
| **Scene 8 · the crack shuts** | Register that scene 5's crack **slaps shut** | `Then he shuts it.` |
| **Scene 9 · the fragility** | The distance between him and that man is thinner than he thought — **and no AI** | `...is about four bad months and a bit of luck.` |
| **Scene 10 · the irony** | The narrator does the freak-out **and still thinks it's the drugs** | `Christ, that's strong stuff. Give it an hour.` — the one moment the audience is ahead of him |
| **Scene 11 · the last paper** | 🔑 From the transcript, still missing from canon; closes the *why does a paper exist* hole | `Last one they ever printed.` |
| **Scene 11 · the reach-back** | ⬅️ **Whoever owns the AI owned the flats** — without it *"the film becomes an anti-AI film by accident"* | `It doesn't say who owns the machines. Same man who owns the flats.` |
| **Scene 12 · the ending** | 🔴 The scene had **no narration at all**, so the `12d` tilt had no last word to be cut to | `The paper goes on the fire. Nobody says sorry; the cans do it.` then the close |
| **The one admitted uncertainty** | A narrator that is never wrong reads as a device | `I know how this ends. I've never been sure about this bit.` |
| **The last word, written first** | The `12d` tilt is timed to it, and the embers become the bad code | **`up`** — `Watch what goes up.` The tilt follows the smoke on the narrator's own instruction |
| **Cadence** | The brief's named fix: **one long cosmic sentence among the short ones** | The scene-9 line is **27 words** against a 9-word median. Its cue carries `one long unhurried sentence` so the delivery opens out with it |

| Beat cut | Why |
|---|---|
| The I.P.A. / beer-donations joke (38 words) | ⚠️ It aimed the contempt at **the people who donate** — ordinary passers-by. Against [`the-reader.md`](../../../marketing/the-reader.md) that is the Lee/Coe test failing: a hostile viewer seeing only that beat hears contempt for ordinary people. Scene 6's job is now done by the three reactions, which implicate without accusing |
| `Tarquin agrees that he needs to explore himself more, so he heads off to get supplies` | Pure transit. Chunk 5 opens in Wales anyway |
| `He's had enough, bless him. Time for bed.` | The picture does it |
| `Safe to say it has kicked in...` | The kaleidoscope does it, louder |
| `Bob spends his days in this oh-so-luxury tent` | The tent is on screen; narrating it is the brief's *lecture* trap |

⚠️ **One line is held back from canon pending the filter test.** Story canon gives Bob *"Where the
fuck have you been, then?"*; the script carries **`Where the hell have you been.`** If the
throwaway generation shows the filter passes `gives a shit`, restore Bob's word — it is his register,
and softening it is the only place this rebuild is quieter than canon.

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


## 🥇 ROUND 14 — the WHOLE script, one generation (2026-09-03)

✅ **Round 13 is validated.** It was logged ⬜ untested. **Jack has now heard it: *"it made something
quite cool… I like this."*** So `Madchester monologue, Britpop snarl, Manchester, British` is the
prompt of record, and 🔑 **`Britpop`, deleted at round 4 for summoning a guitar band, is rehabilitated
— it came back at 13 and the take held.** The round-4 ruling is superseded.

### 🔑 Why ONE generation, not six

The opposite call from the ElevenLabs sheet, for a reason specific to Suno:

| | |
|---|---|
| 🔴 **Suno drifts between generations** | Six takes is six different men. That drift is the reason narration left Suno in the first place. **One take is one voice, by construction** |
| ✅ **It fits** | Lyrics box caps at **5,000 characters** on v4.5+/v5/v5.5. This script is **~2,450** |
| ⚠️ **It is under the rushing threshold, but not by much** | Practitioner rule of thumb: *"~3,000 characters is the sweet spot before Suno starts to rush a song."* We are inside it — but this narration must be **unhurried**, so watch for rushing first, before anything else |
| ✅ **The film cuts it apart anyway** | Every line is a cut point in Premiere, so a single long take costs nothing downstream |

### ⚠️ Duration — aim ABOVE, because it will not stretch

**~440 words at an unhurried ~135 wpm is roughly 200 seconds.** 🔴 **Set the duration slider to
240s**, not 200 — [`suno-controls-and-workflows.md`](../../../suno-gpt/files/suno-controls-and-workflows.md)
§5: *"the duration control reliably **shortens** but repeatedly **fails to stretch**."* The
`suno-automation` rule is the same — **long trims; short is a reshoot.**

🔴 **Two duration controls exist and only one works.** Advanced Mode's is the slider inside **More
Options** (collapsed by default). The number input with Custom/Auto is the **Simple** panel's and is
**not linked** — writing to it does nothing, silently.

### The four boxes — paste in this order

**1 · My Taste** *(Jack's round-13 block, unchanged)*

```
Vocals: one male voice, and he is TALKING — not singing, not reciting. A working-class Manchester man in his forties, telling you something across a table: mid-range, nasal and adenoidal, a sandpaper rasp on it, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Close and dry right on the microphone. Free pacing — ordinary conversational speech, uneven sentence lengths, pausing where the meaning breaks and never on a bar, and his pitch swoops up inside a sentence and drops away at the end of it — never droning, never on one note. Bored, sarcastic and certain, giving nothing away, never signalling a joke. The voice stays loud and right in front the whole way through, never getting quieter. Music: one low ambient underscore underneath, no pulse and no rhythm and no drums of any kind, the same all the way through, no melody and no chords, nothing ever builds and nothing ever drops. Register: grim and funny, played completely straight.
```

**2 · Style** *(unchanged — 🔴 do not edit a prompt and its lyrics in the same round)*

```
Madchester monologue, Britpop snarl, Manchester, British, one man talking, not singing. Working-class Manchester lad in his forties. Mid-range voice, nasal and adenoidal, sandpaper rasp, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Close and dry on the microphone. Free pacing, ordinary conversational speech, pausing where the meaning breaks and never on a bar. His pitch swoops up inside a sentence and drops away at the end of it. Bored, sarcastic, deadpan. Underneath, one low ambient underscore, no pulse and no rhythm, the same all the way through and never getting quieter. Voice loud and in front all the way, no singing, no melody.
```

**3 · Exclude Styles** *(unchanged)*

**4 · Lyrics — the whole script, one `[Monologue]`, prose paragraphs**

🔴 **The layout votes as hard as the words.** One label, repeated never; six paragraphs, not
thirty-eight lines. *"Suno reads a line break as a phrase reset and a section break as a musical
event, so one bracketed section per line IS the slam cadence drawn as a page."*

```
[Monologue]

Two thousand and eight. Meet Tarquin. Star trader on the NatWest floor, betting heavily on leveraged E.T.F.s. Pain infliction usually looks this banal. Uh. Nice tie, though. Meet Bob. Standard middle-manager bloke. Getting away for a few days with his wife Jo, away from the financial stress of it all. Can you blame 'em, really.

Twenty twenty-six. Tarquin runs the country's biggest private equity firm, the one that buys up social housing. The bastard looks very pleased with himself. He ditched the tie, at least. Driving home from work, he spots this lot, and thinks: interest rates up one percent next week. You chaps are going to have a few more mates soon. Cannot wait for my bonus. It is a tad chilly, though.

Bob spends his days in this oh-so-luxury tent, taking any charitable beer donations he can get his hands on. I don't know what's worse. That his cause is so rarely supported. Or that the ones who do support it judge him for being an I.P.A. man. Fuck me.

Tarquin sought professional help. He'd felt a feeling, first time since the devil's lettuce at uni. The therapist tries to explain that empathy for the homeless does not warrant an emergency appointment. It does not sink in. So he gives up, and says there is no helping him. He needs the strongest psychedelic known to man to fix his car crash of a personality. Forgive the pun. Tarquin agrees that he needs to explore himself more. So he heads off to get supplies before his trip to Wales.

Parks how he usually does. Bob is none too pleased. I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit. Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them. Four by fours. Most common vehicle in this car park. Tarquin locks on to a background figure. Not so much a wrestle with his conscience — just a small acknowledgement that it is in there. It being Bob.

He heads off to Wales for this spiritual retreat. Before they hand over the ayawaska, they insist on meditation. Tarquin has never sat on a floor before. Safe to say it has kicked in. He's had enough, bless him. Time for bed. Awoken by the sound of thunder, with his heart in his throat. Stepping out of the tent, he spots an old newspaper. Warming his hands on the fire, Bob tries to calm him down. Tells him to pay attention to the date. Twenty thirty-one. Last one they ever printed. He takes the news well. Excuse the pun.
```

### What changed in the words, and why

| Change | Why |
|---|---|
| **All ElevenLabs markup stripped** — `[understated]`, `<break time>` | Those are TTS controls. Suno would sing or speak them |
| **`Safe to say it has kicked in.`** — ellipsis removed | Trailing ellipses are an ElevenLabs pause control. Suno gets its pauses from `free pacing` and full stops |
| **Six chunks joined into six paragraphs** | Paragraph = phrase group. The chunk boundaries were an ElevenLabs credit-repair device and mean nothing here |
| **Normalisation kept** — `Two thousand and eight`, `E.T.F.s`, `one percent`, `ayawaska` | Suno mispronounces raw numerals and initialisms the same way |
| 🔴 **`Twenty thirty-one`** | The date is the reveal. `7da1604` fixed this once already |

### Settings

**v5.5** · Style influence **75** · Weirdness **run the pair at 30 and 60** · Duration **240s** ·
Audio influence n/a. Name takes `camping-narration-full-A-w30` / `-w60`.

### Judge it in this order — the first fault masks the rest

1. 🔴 **Is he rushing?** The one new risk at this length. If yes, the fix is **not** a longer
   duration — it is fewer words. Cut the ~25 dead words the ElevenLabs sheet names.
2. **Does he drift** — accent, age or register — across three-plus minutes? This is the fault that
   drove narration off Suno. If it drifts, the answer is chunking after all.
3. **Is he talking, not reciting?** Rounds 1–13's whole war.
4. **Accent.** The audition line is *"I'd say it's a Mexican standoff, but there are no stakes and
   no one gives a shit."*

⚠️ **Instrumental is discarded** — vocal stem only, three dots → Get stems → advanced split (§5). So
judge the voice and ignore the bed entirely.


## 🔑 ROUND 15 — the layout was the brake, and I took it off (2026-09-03)

**Jack on round 14: *"closer, but the voice sounds echo-ey and AI-ee, it talks too fast, and it does
not pause at the end of sentences."*** Two different faults with two different owners.

### 🔴 Fault 1 · Too fast, no sentence pauses — my error in round 14

[`lyric-craft.md`](../../../suno-gpt/files/lyric-craft.md) §"Punctuation is the brake" states the
mechanism outright:

> **"Suno allocates a musical phrase per lyric *line*, then fits that line's syllables into it.
> Delivery speed is a function of syllable density per line — not of any tempo instruction."**
> **More syllables on one line → faster.** **No punctuation at all → a "wall of words" that gets
> rushed.**

🔴 **Round 14 put entire 60–90-word paragraphs on single lines.** Each paragraph became one musical
phrase and Suno compressed it to fit. **The rushing was written into the layout**, and no Style-box
word could have beaten it. Practitioner sources agree on the number: **"keep lines under 10–12
words — longer lines get rushed regardless of punctuation."**

⚠️ **And this looked like it was following the round-9 ruling, but it wasn't.** That ruling says the
poem came from *"one line per **bracketed section**"* — many `[...]` labels making stanzas. It never
said "no line breaks." **One label with line breaks inside it is a different thing from many labels.**

🥇 **The fix, and the only change this round: uneven line breaks at meaning boundaries.**

| | Round 14 | **Round 15** |
|---|---|---|
| Lines | 6 | **58** |
| Words per line | **60–90** | **mean 7.6, range 2–15** |
| Over 12 words | 6 of 6 | **1 of 58** |
| Bracket labels | 1 | **1 — unchanged** |
| Words | identical | **identical** |

🔑 **Uneven is the point.** Even line lengths read as verse and bring the recital back; an uneven
spread reads as speech. This is the sheet's own *"widen the sentence-length spread"* lever, applied
to layout instead of prose.

### ⚠️ Fault 2 · Echo — the POOL is wet, and the ban cannot reach it

`reverb, echo` have been in the Exclude box for rounds and it still echoes. **That is the signature
of an inert ban losing to a pool word**, which this sheet has now recorded four times.

🔴 **`Madchester` and `Britpop` ARE reverb-drenched vocals.** That wash is the baggy production
signature — it is not a defect the pool is adding by accident, it is what the pool *is*. And
[`suno-voices.md`](../../../suno-gpt/suno-voices.md) is blunt that Exclude bans do not beat pool
words.

🔴 **So do NOT strip the pool to fix this.** `Madchester, Britpop` is what finally delivered the
voice Jack likes after thirteen rounds. Removing it to chase a dry signal is the round-12 mistake in
reverse — and this sheet already records what happens when you strip a clause without checking what
it was holding up.

🥇 **Fix it in post instead. The voice is right; the processing is wrong, and there is a tool for
exactly that.**

**Studio → right-click the clip → remove effects** → returns a **dry signal**. It works on imported
audio as well as Suno's own, so the vocal stem can be stripped and re-processed to taste.
⚠️ **Vendor-sourced (`suno-studio.md`), so this SHOULD work — it is not tested here.** Ten minutes
settles it.

**Order of operations:** three dots → Get stems → **advanced split** → keep the vocal stem →
right-click → **remove effects**. The bed is being discarded anyway.

### ⬜ "Are there Suno tags like ElevenLabs tags?" — honestly, no

| | |
|---|---|
| `[Short Pause]`, `[Beat Transition]`, `[Musical Interlude]` | ⚠️ **Reported, never verified.** Suno publishes no tag list, so the whole vocabulary is folk knowledge. This toolkit's standing rule: **never promise a meta-tag will fire** |
| **Line breaks, line length, punctuation** | ✅ **Tested, and the mechanism is understood.** This is Suno's real equivalent of an ElevenLabs audio tag, and it is more reliable than one |

🔑 **The comma finding is tested by controlled A/B here:** a comma marks a **stress boundary**, and
the delay is a side effect. Full stops give *"a complete break — full breath, pitch reset"*, which is
precisely the *"pause at the end of sentences"* Jack is missing — and round 15 now has 58 of them
doing that job instead of 6.

### Lyrics — round 15. Same words, new layout.

```
[Monologue]

Two thousand and eight.
Meet Tarquin. Star trader on the NatWest floor,
betting heavily on leveraged E.T.F.s.
Pain infliction usually looks this banal.
Uh. Nice tie, though.

Meet Bob. Standard middle-manager bloke.
Getting away for a few days with his wife Jo,
away from the financial stress of it all.
Can you blame 'em, really.

Twenty twenty-six.
Tarquin runs the country's biggest private equity firm,
the one that buys up social housing.
The bastard looks very pleased with himself.
He ditched the tie, at least.

Driving home from work, he spots this lot, and thinks:
interest rates up one percent next week.
You chaps are going to have a few more mates soon.
Cannot wait for my bonus.
It is a tad chilly, though.

Bob spends his days in this oh-so-luxury tent,
taking any charitable beer donations he can get his hands on.
I don't know what's worse.
That his cause is so rarely supported.
Or that the ones who do support it judge him for being an I.P.A. man.
Fuck me.

Tarquin sought professional help.
He'd felt a feeling, first time since the devil's lettuce at uni.
The therapist tries to explain
that empathy for the homeless does not warrant an emergency appointment.
It does not sink in.

So he gives up, and says there is no helping him.
He needs the strongest psychedelic known to man
to fix his car crash of a personality.
Forgive the pun.

Tarquin agrees that he needs to explore himself more.
So he heads off to get supplies before his trip to Wales.

Parks how he usually does.
Bob is none too pleased.
I'd say it's a Mexican standoff,
but there are no stakes and no one gives a shit.

Bob's mind is thrown into a tailspin
every time he sees those wank tanks, as he calls them.
Four by fours. Most common vehicle in this car park.

Tarquin locks on to a background figure.
Not so much a wrestle with his conscience —
just a small acknowledgement that it is in there.
It being Bob.

He heads off to Wales for this spiritual retreat.
Before they hand over the ayawaska, they insist on meditation.
Tarquin has never sat on a floor before.
Safe to say it has kicked in.
He's had enough, bless him. Time for bed.

Awoken by the sound of thunder, with his heart in his throat.
Stepping out of the tent, he spots an old newspaper.

Warming his hands on the fire, Bob tries to calm him down.
Tells him to pay attention to the date.
Twenty thirty-one. Last one they ever printed.

He takes the news well. Excuse the pun.
```

**Everything else unchanged: My Taste, Style, Exclude, v5.5, duration 240s, pair at weirdness 30/60.**
Name them `camping-narration-full-B-w30` / `-w60` — **B**, because the prompt revision letter
advances when anything in the boxes changes, and the lyrics box did.

### Judge round 15

1. ✅ **Pace and sentence pauses** — the only thing that changed. If still rushed, cut words next, not duration.
2. 🔴 **Did the recital come back?** The one risk of adding line breaks. If he starts reciting, the
   answer is fewer, longer lines — not a return to paragraphs.
3. **Echo** — expected to be unchanged. It is a post-production job, not a prompt one.


## 🔑 ROUND 16 — measured the cram, and the form word was always too SHORT (2026-09-03)

**Jack: *"still talking to the beat, he speeds up randomly, maybe more tags would do the trick"*** —
and separately, *"unless there is a different way of saying talking to Suno, like how rappers do
before a song starts."* **The second instinct is the better one. The first is backwards.**

### 🔴 "More tags" is the wrong direction — and it is this exact symptom

[`suno-voices.md`](../../../suno-gpt/suno-voices.md) §4, tested: *"cue density chopping a verse into
**micro-sections that each re-decide their own phrasing**"* — and the ruling that follows is blunt:
🔴 **"a tempo fault is now a reason to STRIP cues before anything else."**

**"He speeds up randomly" is that finding's own description of itself.** We already carry exactly one
label, so there is nothing left to strip — but adding more would make this fault worse, not better.

### 🥇 The random speeding-up, measured

*"Measure before prescribing."* [`lyric-craft.md`](../../../suno-gpt/files/lyric-craft.md): **the
first line of a section sets the bar length, and every later line is force-fit into that slot.**

🔴 **Round 15 opened three paragraphs on a very short line.** *"Two thousand and eight."* is five
syllables; it set a five-syllable bar, and the eleven- and fourteen-syllable lines behind it crammed
to fit. **Cram is what "speeds up randomly" sounds like.**

| | Round 15 | **Round 16** |
|---|---|---|
| Paragraphs opening ≥3 syllables under their own mean | **3** | ✅ **0** |
| Paragraphs flagged | 6 of 15 | **4 of 15** |
| Worst spread | 16 | **9** |

⚠️ **The four remaining spreads are deliberate and should stay.** They are the punchlines — *"Fuck
me."*, *"Uh. Nice tie, though."*, *"Forgive the pun."* The asymmetry rule says a **short line gets
stretched, which sounds deliberate; a long line gets crammed, which sounds broken.** Short outliers
are the joke landing.

### 🔑 Jack's instinct, and what it exposes: every form word we have tried names a SHORT section

**`skit`** is a short section between songs. **`interlude`** is the same. So is the rapper's
**`intro`** he is reaching for. 🔴 **That is why round 10's voice ducked and built toward something —
we kept telling the model this was a short bit before the real thing starts.**

🔑 **The script is three and a half minutes of one man talking. The forms that natively mean *a man
talks, at length, with no beat* are different words entirely:**

| Form word | Why it fits |
|---|---|
| 🥇 **`audiobook narration`** | Long-form by definition. Enormous corpus, no grid anywhere in it, and a heavily **British** one — which is free accent reinforcement in the strong genre slot rather than a weak adjective |
| 🥇 **`documentary voiceover`** | The sheet's own ladder rung 2, untried. A man explaining something over an underscore |
| **`radio drama`** | Same family, same rung |

⚠️ **`monologue` stays** — it is the nationality-neutral talking form-word and it doubles the
`[Monologue]` label. **These are added beside it, not instead of it.**

### The two changes, and why they are separable

They fix **different faults**, so a single generation still tells you which worked:

| Change | Fixes | Risk |
|---|---|---|
| **A · Round 16 lyrics** (below) — layout only, not one word altered | The cramming and random speed-ups | Low |
| **B · Style box:** after `Madchester monologue, Britpop snarl,` insert **`audiobook narration, documentary voiceover,`** | Talking *to the beat* | 🔴 A new pool word can move the voice. Freeze everything else |

🔑 **Do A first if you only do one.** It cannot hurt the voice — it changes no words and no boxes.

### Lyrics — round 16

```
[Monologue]

Two thousand and eight. Meet Tarquin.
Star trader on the NatWest floor,
betting heavily on leveraged E.T.F.s.
Pain infliction usually looks this banal.
Uh. Nice tie, though.

Meet Bob. Standard middle-manager bloke.
Getting away for a few days with his wife Jo,
away from the financial stress of it all.
Can you blame 'em, really.

Twenty twenty-six. Tarquin runs the country's
biggest private equity firm,
the one that buys up social housing.
The bastard looks very pleased with himself.
He ditched the tie, at least.

Driving home from work he spots this lot,
and thinks: rates up one percent next week.
You chaps'll have a few more mates soon.
Cannot wait for my bonus.
It is a tad chilly, though.

Bob spends his days in this luxury tent,
taking any beer donations he can get.
I don't know what's worse.
That his cause is so rarely supported.
Or that the ones who do judge him
for being an I.P.A. man.
Fuck me.

Tarquin sought professional help. He'd felt a feeling,
first time since the devil's lettuce at uni.
The therapist tries to explain
that empathy for the homeless
does not warrant an emergency appointment.
It does not sink in.

So he gives up. There is no helping him.
He needs the strongest psychedelic known to man
to fix his car crash of a personality.
Forgive the pun.

Tarquin agrees he should explore himself more.
So he heads off for supplies,
before his trip to Wales.

Parks how he usually does.
Bob is none too pleased.
I'd say it's a Mexican standoff,
but there are no stakes,
and no one gives a shit.

Bob's mind is thrown into a tailspin
every time he sees those wank tanks.
Four by fours. Most common vehicle
in this car park.

Tarquin locks on to a background figure.
Not a wrestle with his conscience —
just a small acknowledgement
that it is in there. It being Bob.

He heads off to Wales for the retreat.
Before they hand over the ayawaska,
they insist on meditation.
Tarquin has never sat on a floor before.
Safe to say it has kicked in.
He's had enough, bless him. Time for bed.

Awoken by the sound of thunder,
with his heart in his throat.
Stepping out of the tent,
he spots an old newspaper.

Warming his hands on the fire,
Bob tries to calm him down.
Tells him to look at the date.
Twenty thirty-one. Last one they ever printed.

He takes the news well. Excuse the pun.
```

**Unchanged: My Taste, Exclude, v5.5, duration 240s, pair at 30/60.** Name `-C-w30` / `-C-w60`.

⚠️ **Before pasting, grep the Exclude box for every noun in the Style box** — the sheet's own rule,
after `underscore` was found banned while the Style box asked for one. **If you add `audiobook
narration, documentary voiceover`, check neither `audiobook`, `documentary` nor `voiceover` is
banned.** (`movie trailer voice` and `epic narrator` are banned; plain `narration` is not.)


## 🔑 SETTINGS — the pair has been running on the wrong axis (2026-09-03)

**Jack: *"could the weirdness and style influence be messed with more?"*** ✅ **Yes, and this may be
the largest untouched lever left.** Every round of this sheet has run the house pair — **weirdness 30
and 60** — and that pair is built for *music*, where surprise is the point. **Narration is the
opposite job.**

### 🔴 Weirdness 60 is the creative setting, and "speeds up randomly" is what it sounds like

| Source | On weirdness |
|---|---|
| [`suno-controls-and-workflows.md`](../../../suno-gpt/files/suno-controls-and-workflows.md) §1 | **0 = "maximum obedience. Use whenever you need an exact reproduction"** · **60–65 = "the creative sweet spot"** |
| Suno's own help + practitioner guides | The scale runs **Safe → Chaos**. Low values give *"predictable, genre-accurate output"*; high values introduce *"unexpected instruments, **non-standard rhythms**, and surprising transitions"* |

🔑 **"Non-standard rhythms" is the external documentation describing Jack's exact complaint.** A
narration read must be *predictable* — that is the entire brief. **We have been asking for surprise
in the one job that must not have any**, for sixteen rounds.

⚠️ **One discrepancy, stated rather than resolved:** the repo says weirdness **50 is "effectively no
randomness"**; external sources call 50 the *neutral midpoint of a Safe↔Chaos scale*, which is a
weaker claim. **Either way 0 is safer than 60 here**, so the ruling does not depend on settling it.

### 🥇 Style influence should go UP, because the prompt earned it

§1: **75 is "the working default for a prompt you trust"**, 100 *"can over-tighten and degrade
adherence"* — and the corpus's most-repeated tip is *"75, not 100."* **But the rule beside it is the
one that applies:**

> **"Push it up as your prompts get more specific — high style influence rewards good vocabulary and
> punishes vague prose."**

**This prompt is sixteen rounds of tested vocabulary.** External guidance agrees on where that lands:
at **70–100%, "every tag is treated as a hard constraint."** 🔑 **A prompt whose every clause has
been individually earned is exactly the case for pushing past 75.**

### The ruling — pin weirdness, pair on style influence

| | House default (used every round so far) | 🥇 **Narration setting** |
|---|---|---|
| **Weirdness** | pair at **30 / 60** | 🔴 **0, pinned. Not paired.** Maximum obedience |
| **Style influence** | 75 | **pair at 75 / 90** |

🔑 **The pair still runs — it just moves to the axis that matters.** Two takes:
`camping-narration-C-si75-w0` and `-si90-w0`.

⚠️ **Do not also jump to 100.** The corpus is consistent that 100 over-tightens and can *degrade*
adherence, which would be a hard fault to diagnose on top of everything else. **90 first.**

⚠️ **Sliders are Advanced/Studio only, and are reportedly absent on free-tier accounts.** If they are
not visible, that is the reason.

### Why this is worth a round on its own

**It changes no words and no boxes.** Style, Exclude, My Taste and the lyrics are all untouched, so
the round stays attributable — the sheet's own discipline: *"once an axis is confirmed right, freeze
it."* If weirdness 0 fixes the random speeding-up, that is one setting doing what four rounds of
prompt surgery could not.


## 🆕 ROUND 17 — stop naming a music genre at all (2026-09-03)

**Jack: *"weirdness 0 / style influence 75 and 90 sounds better, but the lyrics are still sung
sometimes, he still doesn't pause after a sentence, it still is not talking. Forget what we've done,
try something else."*** ✅ **Agreed. Sixteen rounds have all been variations of one idea, and this
round abandons it.**

### 🔑 The thing every round has had in common

**Every prompt since round 1 has led with a MUSIC-SCENE pool word** — `Madchester`, `Britpop`,
`skit`, `baggy`. §4c defended them because *"nationality rides on the genre"* and they were the only
thing delivering a northern accent. **But a music pool's native vocal SINGS, sits on a bar, and comes
with its scene's production.** That is the singing, the beat and the echo — **three faults, one
cause, and it is the word we kept protecting.**

🔴 **We have been buying the accent with the exact word that breaks the delivery.**

### 🥇 The new idea: make the genre slot a SPEECH form that is already British

**Do not name a music genre at all.** Put a *talking* form in the strongest slot — and pick one that
carries the accent by itself, so nothing is lost when the music pool goes.

| Lead | Why |
|---|---|
| 🥇 **`British kitchen-sink drama narration`** | 🔑 **This sheet's own variant F, listed 🟢 at the top of the file and never once tried.** Kitchen-sink *is* British working-class northern by definition — the accent arrives with the form instead of with a music scene. Its only flagged risk was inviting a film score, and `film score, orchestral score, thriller score` are all already banned |
| **`audiobook narration`** | Long-form by definition. No grid anywhere in the corpus, and a heavily British one |
| **`documentary voiceover`** | This sheet's own ladder rung 2, untried |
| 🔑 **`voice memo quality, close and dry, unproduced, no room`** | **Jack's rapper instinct, correctly named.** Practitioner sources give *"voice memo quality"* and *"casual studio chatter"* for exactly the before-the-beat talking he described. It is a **recording context, not a music genre** — so it attacks the **echo** as well, which no ban ever could |

⚠️ **Rejected: `[Sprechgesang]`.** It surfaces in guides as a spoken-vocal tag, but it literally means
*speech-song* and is a **singing** technique. Wrong direction for a track already drifting sung.

### 🔴 What this costs, stated plainly

**The voice Jack liked at round 13 came from `Madchester, Britpop`.** Removing them may lose it. **That
is the trade this round accepts** — and it is Jack's own call: *"forget what we've done, try something
else."* If the voice goes and the talking arrives, the next move is to add **one** music word back and
watch which fault returns.

### The Exclude box changes too — and it has to

🔑 **Round 12 UNBANNED the whole band/guitar family** (`indie rock, guitar band, post-punk band,
guitar, jangly guitars`) for one reason: those bans were strangling the Madchester pool. **The pool is
gone, so the reason is gone** — and they go back in, along with `Madchester, Britpop, baggy` themselves.

⚠️ **The grep audit caught three collisions with the new Style box** — the exact stale-ban trap this
sheet has hit four times. All three are fixed below: `calm narration` → **`calm delivery`**,
`ambient pad` → dropped (`pad` already banned), `dramatic reading` → **`theatrical recital`**.

### 1 · My Taste

```
Vocals: one male voice, and he is TALKING — not singing, not rapping, not reciting. He is reading a story out loud the way an audiobook or a television documentary is read. A working-class northern English man in his forties, telling you something across a table: mid-range, nasal and adenoidal, a sandpaper rasp on it, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Recorded like a voice memo — close and dry right on the microphone, unproduced, no room and no echo on him at all. Free pacing — ordinary conversational speech, uneven sentence lengths, and every full stop is a real stop with a breath in it, pausing where the meaning breaks and never on a bar. His pitch swoops up inside a sentence and drops away at the end of it — never droning, never on one note. Bored, sarcastic and certain, giving nothing away, never signalling a joke. The voice stays loud and right in front the whole way through, never getting quieter. Music: one low ambient underscore underneath, no pulse and no rhythm and no drums of any kind, the same all the way through, no melody and no chords, nothing ever builds and nothing ever drops. Register: grim and funny, played completely straight.
```

### 2 · Style

```
British kitchen-sink drama narration, audiobook narration, documentary voiceover. One man talking, not singing. Northern English working-class man in his forties. Mid-range voice, nasal and adenoidal, sandpaper rasp, sneering and cocky. Hard flat northern vowels, dropped consonants, vowels leaned on and drooping at the ends of words. Voice memo quality, close and dry right on the microphone, unproduced, no room. Free pacing, ordinary conversational speech, uneven sentence lengths, pausing where the meaning breaks and never on a bar. Every full stop is a full stop and he stops at it. His pitch swoops up inside a sentence and drops away at the end of it. Bored, sarcastic, deadpan. Underneath, one low ambient underscore, no pulse and no rhythm, the same all the way through and never getting quieter. Voice loud and in front all the way, no singing, no melody.
```

### 3 · Exclude Styles

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, autotune, harmonies, backing vocals, choir, spoken word, performance poetry, poetry slam, dub poetry, beat poetry, poetry reading, recital, recitation, declamatory, verse, stanza, rhyming, metrical, incantation, theatrical recital, over-enunciated, elocution, female vocal, sung female vocal, torch song, jazz vocal, soul vocal, sultry, seductive, US rap, young MC, rapping, bars, flow, trap, piano, glockenspiel, strings, violins, horns, melody, chord progression, chords, synth lead, pad, deep voice, low voice, bass voice, baritone, booming, boomy, sub bass, chest voice, growl, monotone, flat delivery, level delivery, unmodulated, robotic, machine voice, text to speech, computerised, comedic, novelty, parody, jaunty, playful, whimsical, bouncy, uplifting, laugh track, audience laughter, applause, live audience, epic trailer music, cinematic swell, film score, orchestral score, thriller score, suspense, tension strings, movie trailer voice, epic narrator, reverb, echo, telephone voice, distorted vocal, vocoder, double time, tempo change, fast delivery, rapid fire, breathless, hurried, frantic, manic, shouting, screaming, yelling, gentle, soft vocal, softly spoken, mellow, soothing, breathy, whispered, calm delivery, languid, wistful, build, buildup, riser, drop, beat drop, pre-drop, breakdown, crescendo, decrescendo, swell, dynamic build, tension build, fade in, fade out, quiet passage, half time, vocal ducking, distant vocal, buried vocal, drums, drum kit, drum loop, percussion, breakbeat, beat, kick, snare, hi-hats, groove, four to the floor, pulse, metronome, quantized, on the beat, in time with the beat, rhythmic delivery, cadence, syncopation, bars, rap flow, chanting along, sing-song, indie rock, guitar band, post-punk band, rock band, live band, guitar, acoustic guitar, jangly guitars, baggy, Madchester, Britpop, indie, anthemic, singalong, terrace chant
```

### 4 · Lyrics — round 16's layout, unchanged

**Do not change the words this round.** The layout was measured and fixed at round 16; leaving it
frozen is what makes this round attributable to the genre swap.

### Settings

**v5.5 · Weirdness 0 · Style influence 75 and 90 · Duration 240s.** Jack confirmed weirdness 0
*"sounds better"*, so it stays pinned. Name `-D-si75-w0` / `-D-si90-w0`.

### Judge it

1. 🔑 **Is he talking?** The whole point of the round.
2. **Does he pause at full stops?** The `every full stop is a full stop and he stops at it` clause is new.
3. **Is the echo gone?** `voice memo quality, unproduced, no room` is the first positive lever aimed at it.
4. 🔴 **Is the voice still right?** The known cost. If the accent has gone but he is finally talking,
   **that is progress, not failure** — accent is recoverable, delivery has not been.


## 🥇 ROUND 18 — the accent, without naming the singer (2026-09-03)

✅ **ROUND 17 IS THE BREAKTHROUGH.** Jack: ***"this has worked 10 times better than anything."***
🔑 **Dropping the music genre entirely is the ruling of this whole sheet.** Seventeen rounds of
adjectives could not do what deleting one word did. Record it as settled: **for narration, the genre
slot takes a SPEECH form, never a music scene.**

**Remaining fault: the accent, exactly as round 17 predicted it would be.**

### 🔴 Why the accent went — it is §4c, on schedule

**§4c: accent rides on the genre slot, and adjectives buy nothing.** Round 17 took `Madchester` and
`Manchester` out of that slot and put `British` in — so the accent fell back to generic British.
**This was written down as the cost before the round was run.**

🥇 **The fix is not to bring the music pool back. It is to put Manchester into the strong slot
as a modifier on the SPEECH form:**

```
British kitchen-sink drama narration   →   Manchester kitchen-sink drama narration
```

**Manchester is now in the genre position — where §4c says accent is decided — and it is still not a
music genre.** That is round 17's logic extended rather than reversed.

⚠️ **`Madchester` stays banned and `Manchester` is clear.** One is a music scene that sings; the
other is a city. The Exclude box already makes that distinction and the grep audit confirms it.

### 🔴 Liam Gallagher cannot be named, and does not need to be

Jack asked for that voice specifically. 🔴 **Artist names do not go in the boxes** — Suno's content
filter *"blocks silently and mislabels"*, and
[`../../karen/narration/voice.md`](../../karen/narration/voice.md) sets the house method for exactly
this: *"a blend of references, **none of which can be named to the engine** — descriptive traits
steer better anyway."*

🔑 **So the voice is specified by the mouth, per the sheet's own rule that articulation beats
attitude.** What is new this round, and what each clause is buying:

| Clause | What it is for |
|---|---|
| **`snarled through the nose`** | The defining quality. `nasal and adenoidal` was already there; the snarl is what sat on top of it |
| **`Chin up, jaw jutted forward, mouth barely opening`** | Physical, not emotional — the posture that produces that sound |
| **`drawn out and bent flat`** | The stretched, bent vowel |
| **`Glottal stops, dropped T's and dropped H's`** | Manchester consonants, stated as articulation |
| **`A curled lip on every line`** | The sneer as a mouth shape rather than a feeling |

### What is deliberately NOT changed

🔴 **Everything else is frozen** — Exclude box, lyrics, weirdness 0, style influence 75/90, duration.
**One axis moves.** Round 17 proved the delivery works; the only question this round asks is whether
the accent comes back without the delivery breaking.

⚠️ **The Style box hit its 1,000-character ceiling** and two clauses were cut to fit, both because
the new genre slot now supplies them free: `born and raised` (the city is in the genre word) and
`uneven sentence lengths` (the round-16 lyric layout already does this). **Ceilings, not targets.**

### 1 · My Taste

```
Vocals: one male voice, and he is TALKING — not singing, not rapping, not reciting. He is reading a story out loud the way an audiobook or a television documentary is read. A working-class Manchester man in his forties, born and raised there, telling you something across a table: mid-range, nasal and adenoidal, snarled through the nose, a sandpaper rasp on it, sneering and cocky. Chin up, jaw jutted forward, mouth barely opening. Hard flat Manchester vowels, drawn out and bent flat, leaned on and drooping at the ends of words. Glottal stops, dropped T's and dropped H's. A curled lip on every line. Recorded like a voice memo — close and dry right on the microphone, unproduced, no room and no echo on him at all. Free pacing — ordinary conversational speech, uneven sentence lengths, and every full stop is a real stop with a breath in it, pausing where the meaning breaks and never on a bar. His pitch swoops up inside a sentence and drops away at the end of it — never droning, never on one note. Bored, sarcastic and certain, giving nothing away, never signalling a joke. The voice stays loud and right in front the whole way through, never getting quieter. Music: one low ambient underscore underneath, no pulse and no rhythm and no drums of any kind, the same all the way through, no melody and no chords, nothing ever builds and nothing ever drops. Register: grim and funny, played completely straight.
```

### 2 · Style

```
Manchester kitchen-sink drama narration, audiobook narration, documentary voiceover. One man talking, not singing. Working-class man in his forties. Mid-range voice, nasal and adenoidal, snarled through the nose, sandpaper rasp, sneering and cocky. Chin up, jaw jutted forward, mouth barely opening. Hard flat Manchester vowels, drawn out and bent flat, leaned on and drooping at the ends of words. Glottal stops, dropped T's and dropped H's. A curled lip on every line. Voice memo quality, close and dry right on the microphone, unproduced, no room. Free pacing, ordinary conversational speech, pausing where the meaning breaks and never on a bar. Every full stop is a full stop and he stops at it. His pitch swoops up inside a sentence and drops away at the end of it. Bored, sarcastic, deadpan. Underneath, one low ambient underscore, no pulse and no rhythm, the same all the way through and never getting quieter. Voice loud and in front all the way, no singing, no melody.
```

### 3 · Exclude Styles — unchanged from round 17

### 4 · Lyrics — unchanged from round 16

### Settings — unchanged

**v5.5 · Weirdness 0 · Style influence 75 and 90 · Duration 240s.** Name `-E-si75-w0` / `-E-si90-w0`.

### Judge it

1. 🔴 **Is he still talking?** If round 17's delivery has broken, `Manchester` in the genre slot has
   pulled a music pool in with it after all — and the answer is to move it back to an adjective and
   accept a weaker accent.
2. **Is the accent Manchester rather than generic northern?**
3. **Has the echo stayed away?** `voice memo quality` is doing that job and is untouched.

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
| 🔴 **He's reciting — it sounds like a poem** | `spoken word` is a **performance-poetry genre**, not a delivery mode — and/or the lyrics are laid out one line per bracketed section, which Suno reads as stanzas and lands like slam | **Look at the LAYOUT before the wording.** Run the lyrics as continuous prose paragraphs under one label, and check no box anywhere says `spoken word`. See §1 round 10 |
| **He's talking but he's 22** | `skit` still carries hip-hop gravity, and that pool casts a young MC — `trip hop` in front of it reduces the risk, it does not remove it | **Switch to Style variant B** (audiobook / radio drama). Do not add adjectives to A — the pool is doing the casting |
| 🔴 **The voice goes quiet, as if waiting for a beat to drop** | **An arrangement fault, not a vocal one.** `skit` and `interlude` literally name *a short section between the songs*, so the model builds toward what it thinks comes next and ducks the voice for tension. Round 10, tested | Fix in the **Style box**, not with a tag — external guidance is that Suno gives *"flat verse at constant volume"* unless a build is tagged, so the build was **asked for**. Positive form: `one loop, unchanging, exactly the same level start to finish` + `voice loud and in front the whole way`. Bans behind it in Exclude. **Only if that fails**, the untested lever: `[Energy: High]` at the section start is reported to lock the vocal level — one source, assertion-grade. ⚠️ ALL-CAPS is reported by the same source as *"less reliable than ellipsis"*, and `shouting` is in our Exclude box — do not reach for it |
| 🔴 **He's American, and every box says British** | 🔑 **Something in the atom still NAMES America, and it is probably not in the box you are looking at.** Nationality is a **genre lever** — Exclude bans are tested inert across three rounds, and adjectives (`British`, `northern`, `Manchester`) buy nothing. What decides it is which nationality owns the *strong* slots: genre position, the form word, the production vocabulary | **Run the audit, both boxes at once, before touching a word.** Grep all four boxes for the wrong nationality's *whole family* — its scene names, its form words (`skit`, `interlude`, `cut`), its production slang (`dusty`, `boom bap`, `crate`), and the literal country adjective — then count strong-vs-strong. Round 13 found 3 American to 2 British with `Madchester` in the box. `suno-voices.md` §2a, Thread 5 §4 and §4c |
| 🔴 **The voice is right but he's saying it TO the beat** | 🔑 **Something in the atom declares a grid and the voice aligns to it.** Three usual suspects, in order of strength: a stated **BPM**, a **drum loop** of any kind, and a music-scene pool word. ⚠️ **The round-10 rule was half right** — *melody makes him sing* is true, but **rhythm makes him RAP**, which is the same fault in different clothes | 🔴 **Do not delete the bed — that is how the poem came back in round 9.** **Swap the beat for a bed:** delete the BPM number entirely, replace the drum loop with `one low ambient underscore, no pulse and no rhythm`, and add **`free pacing`** plus `pausing where the meaning breaks, never on a bar`. Then ban the whole grid family in Exclude while leaving `underscore, ambient bed, drone, room tone` unbanned. Ladder if it persists: re-roll ×2 → form word to `documentary voiceover, radio drama` → widen the sentence-length spread → ellipses. §1 round 14 |
| **Something you asked for is simply missing** | A **stale ban** — invisible, and it reads as the Style box being ignored | Grep the Exclude box **and** My Taste for the thing, its **category**, and any whole-palette adjective |

## 7. ⚠️ What is still open before the full run

**All four boxes are now round-9 ready.** The script was rebuilt on 2026-09-01 (see the pass-2 table
in §2) and every scene job in [`../narration-brief.md`](../narration-brief.md) is carried. Two things
are left, and only one of them is a decision.

### 🔴 The budget is over, and the budget is probably what is wrong

| | Before | After the rebuild |
|---|---|---|
| Words | 445 | **413** |
| Lines | 25 | **29** |
| At 155 wpm (the ceiling) | ~172s | **~160s** |
| At ~135 wpm (a narrator's real pace) | ~198s | **~184s** |
| Against the brief's 250–320 | +39% | **+29%** |

**Thirty-two words came out while five required beats went in** — scene 4's mechanism, scene 6's three
reactions, scene 11's reach-back, scene 12 in its entirety, and the long cosmic sentence. Getting to
320 from here means **cutting a job the brief says must be done.**

🔑 **So the honest reading is that 250–320 was derived from the wrong number.** It was back-solved
from `narration.mp3` at 150s — and [`../edit-plan.md`](../edit-plan.md) says that file is **dated 3
August, before the entire 24–30 August production run**, and calls it *"a proxy for length, not the
final track."* The same file measures the untrimmed picture at **272s**. A 184s narration sits
comfortably inside that, and the brief's own governing rule is **"cut to the words, not the other way
round."**

⬜ **Owed a ruling, and it is Jack's:** either the narration budget moves to **~180s** and the re-cut
is retimed against it, or five brief-mandated beats get struck. **Do not cut the script to hit 150s
by reflex** — that number's provenance is a superseded file.

### 🧪 The content filter — one throwaway generation settles it

The script carries *"gives a shit"* and *"wank tanks"*, and canon wants *"Where the fuck have you
been"* restored in scene 11 if the filter allows it.

🔑 **Make the test chunk 4.** It already contains both live phrases, it is the shortest chunk, and it
holds the **audition line** from §4 step 2 — *"I'd say it's a Mexican standoff, but there are no stakes
and no one gives a shit."* One generation therefore settles the filter **and** casts round 9, which is
still untested. If it trips, respell for **sound**, never for the dictionary — and note that changing a
vowel changes the read, so `shit` → `shite` is a **performance** decision, not a workaround.

### The order to do this in

1. **Rule on the budget** (above). ⬅️ *nothing below is wasted either way, but the re-cut waits on it*
2. ✅ **Done, round 13 — and it answered its question: he is northern, and the voice is spot on.** Re-run chunk 4 on the **round-14 A6** boxes, ~20 credits as a pair at weirdness 30 and 60. 🔑 **One question this round: does he stop delivering to a bar?** The voice clauses are frozen and byte-identical, so anything wrong with the voice now is a re-roll, not a rewrite.
3. **Then read the take against this table, and change ONE thing:**

   | What you got | Change | Do not also |
   |---|---|---|
   | **Northern, but still ducks** | Add `[Energy: High]` under the `[Monologue]` label and re-roll | touch the Style box |
   | **Talking freely, but the bed is dull or gone** | ✅ Nothing — the bed is a throwaway stem (§5). **Save the Voice** | re-add a drum to "fix" it |
   | **Still on the grid** | Re-roll twice, then paste **B2** (`Madchester documentary voiceover, radio drama`) | delete the bed, or touch a voice clause |
   | **Reciting again — it's a poem** | 🔴 The bed went too thin. Put a faint unpitched texture back (`low ambient underscore with a soft irregular tick`) — **not a drum loop** | go anywhere near `spoken word` |
   | **The voice changed** | It is a re-roll, not a rewrite. A6's voice clauses are byte-identical to the take Jack approved | edit a single voice word |
   | **Both still wrong** | Neither lever is strong enough — the **pool** is wrong, not the wording. Switch to **variant B** (audiobook / radio drama) | keep adding adjectives |
   | **He's a young MC** | Switch to **variant B** | add adjectives — the pool is doing the casting |
   | **He's reciting again** | 🔴 Something put a poetry word back. Grep all four boxes for `spoken`, `word`, `poetry` before anything else | touch a word of the script |
   | **He's talking, northern and level** | ✅ Save the Voice (§4). Then try deleting `no singing, no melody` from the Style box — that settles §2's open split for free | change two things at once |
4. **Save the Voice** (§4) from the winning take, then run chunks 1, 2, 3 and 5 with it attached.
5. **Restore Bob's word** in chunk 5 if the filter passed it.
6. **Stems out** (§5) — hand Premiere the vocal stem, never the mix.
