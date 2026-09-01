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
| 9 | `Northern English spoken word, British kitchen-sink realism` (candidate F) | plain, hard, weathered mid range with grit | 🔴 **read like a poem** — and so was every round before it. The fault was the genre word, in all four boxes |
| **10 — current** | **`Hip hop skit, album interlude, a spoken intro over a beat`** (A) · **`Audiobook narration, radio drama`** (B) | **deep, dry, weathered, ordinary speech rhythm** | ⬜ untested. **First round with no `spoken word` anywhere, prose lyrics, a beat allowed, and `deep` un-banned** |

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

## 2. Suno prompt — round 10, paste all four, in this order, every round

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
Vocals: one male voice, and he is TALKING, not singing and not reciting. A deep, dry, weathered northern English working-class man in his forties, grit in the voice, hard northern consonants, close and dry right up on the microphone. Ordinary conversational speech rhythm — uneven sentence lengths, some sentences run together and some stop dead, exactly as a man talks. Bored, sarcastic and certain, giving nothing away, never signalling a joke. Music: one slow dusty low loop underneath, drums only, no melody and no chords. Register: grim and funny, played completely straight.
```

### Style — variant A · the skit 🥇

**The recommended one.** Casts the form Jack named: a bloke talking over a beat, which is a real and
heavily-recorded thing, where a northern man reciting over silence is a poetry record.

```
Hip hop skit, album interlude, a spoken intro over a beat. A man talking to you, not performing and not reciting. Northern English, working class, forties. Deep, dry and weathered, grit in the voice, hard northern consonants, close and dry right up on the microphone. Ordinary speech rhythm — uneven sentence lengths, running some sentences together and letting others stop dead. Bored, sarcastic and certain; whatever is funny is in the words and he never signals it. Underneath, one slow dusty drum loop, very low, no melody, no chords.
```

### Style — variant B · the narrator, if A brings a rapper

🔴 **A's one risk is its pool: `hip hop skit` can cast a young MC**, which is the exact failure mode
§6 already lists. If take A is a 22-year-old, do not add adjectives — **switch pool to B**, which
buys talking from the audiobook/radio tradition instead of the hip-hop one. Everything else in the
atom is identical.

```
Audiobook narration, radio drama, documentary voiceover. A man talking to you, not performing and not reciting. Northern English, working class, forties. Deep, dry and weathered, grit in the voice, hard northern consonants, close and dry right up on the microphone. Ordinary speech rhythm — uneven sentence lengths, running some sentences together and letting others stop dead. Bored, sarcastic and certain; whatever is funny is in the words and he never signals it. Almost nothing underneath.
```

### Exclude Styles

🔑 **Three deliberate changes from round 9, and each one reverses a standing ban.**

1. **The whole poetry pool is now banned** — `spoken word, performance poetry, poetry slam, dub poetry, recital, declamatory, verse, stanza, rhyming, metrical, incantation`. This is the round-10 fault named directly.
2. **`deep, low voice, baritone, booming, sub bass` are LIFTED.** Jack asked for a deep voice; those bans would have silently removed it. See the stale-ban note in §1.
3. **`drums, drum kit, breakbeat, a cappella`-driven bans are LIFTED, pitched instruments are not.** The rule is **melody makes him sing, rhythm does not** — round 4's singing came from a glockenspiel and a French horn, not from a drum.

```
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, chanting, autotune, harmonies, backing vocals, choir, spoken word, performance poetry, poetry slam, slam poetry, dub poetry, beat poetry, poetry reading, recital, recitation, declamatory, oratory, sermon, verse, stanza, rhyming, rhyme scheme, metrical, iambic, incantation, mantra, ritual, theatrical, dramatic reading, over-enunciated, elocution, female vocal, American accent, American vocal, transatlantic, southern drawl, US rap, grime MC, UK drill, road rap, young MC, rapping, bars, flow, trap, ragga MC, toasting, Jamaican accent, piano, glockenspiel, strings, violins, brass band, horns, guitar, acoustic guitar, melody, chord progression, chords, bassline, synth lead, pad, ambient pad, music hall, vaudeville, pantomime, ragtime, honky-tonk, jaunty, playful, whimsical, bouncy, comedic, novelty, parody, uplifting, epic trailer music, cinematic swell, film score, underscore, orchestral score, crime drama score, thriller score, suspense, tension strings, reverb, echo, telephone voice, lo-fi vocal, distorted vocal, vocoder, double time, tempo change, band, rock band, guitar band, live band, indie rock, post-punk band, full arrangement, instrumental intro, instrumental outro, instrumental break, monotone, robotic, machine voice, text to speech, computerised, fast delivery, rapid fire, breathless, hurried, frantic, manic, shouting, screaming, yelling, movie trailer voice, epic narrator, gentle, soft vocal, softly spoken, mellow, soothing, breathy, whispered, calm narration, polite, posh, plummy, RP, received pronunciation, BBC newsreader, after-dinner speaker, languid, wistful, stand-up comedy, comedy club, comedian, sitcom, laugh track, audience laughter, applause, live audience, cabaret, variety show, panto, kazoo, slide whistle, oompah, tuba, banjo, whistling
```

### Lyrics — all five chunks

🔴 **Reformatted 2026-09-01, and this is the biggest single change in the round.** The words are
identical to the 2026-09-01 rebuild; **the layout is not.**

**Round 9 gave every one of the 29 lines its own bracketed section with a blank line either side.
That is stanza layout, and Suno reads a section break as a musical event** — it lands the line,
pauses, and restarts. That is the slam cadence drawn as a page, and no amount of wording fixes it.

**So: one label per chunk, sentences run together into paragraphs, no parentheses, natural
punctuation.** Pauses now fall where the *meaning* breaks instead of every nine words.
`lyricist-playbook.md` §3 backs this — its narration recipe is **`[Monologue]`, a minimal style box
and short non-rhyming conversational sentences**, and *"when a cue is ignored, simplify rather than
escalate."* ⚠️ **This retires the `[spoken word]` → `[spoken word speech]` → `[spoken word speech
talking]` escalation ladder for narration.** The playbook already recorded the tension between the
ladder and the simplify rule; round 10 resolves it against the ladder. **Write the finding back into
`docs/suno-gpt/` once a take proves it either way.**

**One label, repeated identically:** `[Skit — a man talking, not performing]` — the label is a *description of the delivery*, not a
genre word, which is the whole point. The only variation is the single `{WARM}` crack in chunk 5.

#### Chunk 1 — 2008

```lyrics
[Skit — a man talking, not performing]

Two thousand and eight. Tarquin, star trader on the NatWest floor, betting other people's houses on leveraged E.T.F.s. He is the reason it happens. Pain infliction usually looks this banal. Nice tie, though.

Meet Bob. Middle manager. Normal. Off for a few days with his wife Jo, away from the stress of it. Can you blame him, really.
```

#### Chunk 2 — 2026

```lyrics
[Skit — a man talking, not performing]

Eighteen years on. Tarquin runs the biggest private equity firm in the country. It buys social housing. It does not rent them out. Empty pays better than full — the price climbs either way.

What a brilliant businessman. He ditched the tie, at least. Driving home he spots this lot. Rates up one percent next week. You chaps'll have a few more mates soon.

His car heater broke last week. Worst four days of his life. Three ways past a man in a tent. Ignore him. Politely say no — ignoring him with manners. Or stop. Have a guess which one's rarest.
```

#### Chunk 3 — therapy

```lyrics
[Skit — a man talking, not performing]

Tarquin sought professional help. He'd felt a feeling, first time since the devil's lettuce at uni. The therapist explains that empathy for the homeless is not an emergency. It doesn't sink in.

So he gives up, and prescribes the strongest psychedelic known to man for his car crash of a personality. Forgive the pun.
```

#### Chunk 4 — the car park

```lyrics
[Skit — a man talking, not performing]

Parks how he usually does. Bob is none too pleased. I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit.

Bob calls them wank tanks. Most common vehicle in this car park. Tarquin clocks him. Not a wrestle with his conscience — just a small acknowledgement that it's in there. Then he shuts it.
```

#### Chunk 5 — Wales, and the newspaper

```lyrics
[Skit — a man talking, not performing]

Wales. Tarquin has never sat on a floor before. And somewhere in all that he works out that the distance between him and the man outside the supermarket is about four bad months and a bit of luck.

Thunder. He's out of the tent with his heart in his throat. Christ, that's strong stuff. Give it an hour.

Bob's at the fire, telling him to look at the date. Twenty thirty-one. Last one they ever printed.

It's not the drugs. The headline says the machines took the jobs. It doesn't say who owns the machines. Same man who owns the flats.

[warmer, quieter, still not performing]

Where the hell have you been. You alright.

[Skit — a man talking, not performing]

The paper goes on the fire. Nobody says sorry; the cans do it. I know how this ends. I've never been sure about this bit. Watch what goes up.
```

### What was changed from Jack's script, and why

**Two passes are recorded here.** The first was synthesis-only. The second rebuilt the script.

#### Pass 1 — synthesis normalisation (the listener hears no change)

| Change | Why |
|---|---|
| `2008` → `Two thousand and eight`, `2026` → `Twenty twenty-six`, `2031` → `Twenty thirty-one` | Bare digits get read as digits, or sung |
| `ETFs` → `E.T.F.s`, `IPA` → `I.P.A.`, `1%` → `one percent`, `4x4's` → `four by fours` | Raw abbreviations and symbols are mispronounced. Normalise before synthesis, never after |
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
f\*\*\* have you been, then?"*; the script carries **`Where the hell have you been.`** If the
throwaway generation shows the filter passes `gives a shit`, restore Bob's word — it is his register,
and softening it is the only place this rebuild is quieter than canon.

## 3. Settings## 3. Settings

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
| 🔴 **He's reciting — it sounds like a poem** | `spoken word` is a **performance-poetry genre**, not a delivery mode — and/or the lyrics are laid out one line per bracketed section, which Suno reads as stanzas and lands like slam | **Look at the LAYOUT before the wording.** Run the lyrics as continuous prose paragraphs under one label, and check no box anywhere says `spoken word`. See §1 round 10 |
| **He's talking but he's 22** | Variant A's `hip hop skit` pool cast a young MC | **Switch to Style variant B** (audiobook / radio drama). Do not add adjectives to A — the pool is doing the casting |
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

The script carries *"gives a shit"* and *"wank tanks"*, and canon wants *"Where the f\*\*\* have you
been"* restored in scene 11 if the filter allows it.

🔑 **Make the test chunk 4.** It already contains both live phrases, it is the shortest chunk, and it
holds the **audition line** from §4 step 2 — *"I'd say it's a Mexican standoff, but there are no stakes
and no one gives a shit."* One generation therefore settles the filter **and** casts round 9, which is
still untested. If it trips, respell for **sound**, never for the dictionary — and note that changing a
vowel changes the read, so `shit` → `shite` is a **performance** decision, not a workaround.

### The order to do this in

1. **Rule on the budget** (above). ⬅️ *nothing below is wasted either way, but the re-cut waits on it*
2. **Run chunk 4 once** on the **round-10 variant A** boxes — filter test and the poem test in one generation, ~20 credits as a pair. **Judge it on one question first: is he talking, or reciting?** Voice quality is round 11's problem.
3. **If he's reciting**, the layout change did not land — strip the chunk to a single paragraph with no label at all and re-roll before touching a word. **If he's a young MC**, switch to Style variant B and change nothing else.
4. **Save the Voice** (§4) from the winning take, then run chunks 1, 2, 3 and 5 with it attached.
5. **Restore Bob's word** in chunk 5 if the filter passed it.
6. **Stems out** (§5) — hand Premiere the vocal stem, never the mix.
