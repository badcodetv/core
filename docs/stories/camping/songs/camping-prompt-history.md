---
title: Camping — prompt history
status: archive
song: ./camping.md
---

# Camping — how the prompt got built

**Archive.** Fourteen rounds of generate → listen → diagnose → fix, from 2026-08-20 to
2026-08-21. The live prompt is [`./camping.md`](./camping.md); **nothing in this file is
an instruction.** It is kept because the *failure analyses* are reusable, and because the
same mistakes are easy to make twice.

The lessons that generalise beyond this track have been promoted into
[`docs/suno-gpt/`](../../../suno-gpt/README.md) — chiefly `files/suno-tag-mechanics.md`,
`files/lyricist-playbook.md` and `suno-voices.md` (Thread 4).

---

## The orchestral menu — five options, worked through one at a time

**Where we got to (2026-08-21).** The GPOM-borrowed strings never sat right; the dub
piano and horn section that replaced them turned the track **upbeat and bouncy**, losing
the haunting, emotive quality that was the whole point. The diagnosis worth keeping:
**an offbeat chord *is* the reggae feel, and a horn *section* playing *stabs* is ska
instrumentation almost by definition.** Brass was never the mistake — the section and the
stabs were.

> **⚠️ PARKED after round 12 (2026-08-21) — the whole category was the mistake.**
> Option 1 was tried and read **whimsical**, and worse, the pitched accompaniment made the
> two men start **singing instead of ranting**. Five separate attempts at an orchestral
> layer (GPOM strings → dub piano and horns → glockenspiel and French horn) each failed in
> a different way, which is the tell that no wording would have saved it: **the video is
> two men rapping, and an orchestra is the wrong register for that track.** The live
> direction is now **big wavetable synthesizers** — see §4c. The menu is kept because the
> options and their risks are sound, and a future BadCode track may want one of them.

Each is a complete, self-contained option: instruments, where they sit, what job they do,
and the risk it carries.

| # | Name | Instruments | Where | The job it does | Its risk |
|---|---|---|---|---|---|
| **1** ❌ *tried, failed* | **The cold music box** | Glockenspiel + French horn | Glock from bar one and under verse 1; horn swells once before the drop; glock over the drops | The glock is **memory**, the horn is **grief** — a child's toy against a ruined man. Both are one-note-at-a-time by nature, so the density fight never starts | Glockenspiel reads **twee** — music box, Christmas, lullaby |
| **2** | **The last post** | One solo muted trumpet, **no section** | Intro; returns over drop 2 | A lone bugle over a ruined country. The horn idea rescued from the reggae framing | Jazz-noir cliché, or ceremonial fanfare |
| **3** | **The colliery band** | Massed brass, hymn-slow, slightly out of tune | Under the drop; one phrase at the very end | Thematically the strongest in the list — a mining-town band playing a funeral march under a D&B drop *is* the song's argument in one sound | **Highest.** Brass band is one step from oompah, which is the round-8 pantomime failure returning |
| **4** | **The wheezing chapel** | Harmonium / pump organ, long held minor chords | Low under the verses; out at the drop | Bleak British interiority. No melody at all, so nothing can go busy | Horror-film cliché, or sacred and churchy |
| **5** | **The tolling** | Tubular bell + orchestral bass drum, **no pitched melody at all** | Intro, then only at the drops | Pure weight and time passing. **Literally cannot play a run** — the zero-density option | Overlaps GPOM's distant timpani; a bright bell reads as Christmas |

**The rule that applies to all five**, learned the hard way over rounds 8–10: *do not ask
an instrument to play sparsely — pick one that is sparse by construction, and name the
behaviour rather than the tradition.* Struck instruments (glock, bell) and single
sustained lines (horn, trumpet, harmonium) satisfy that; a piano and a string section do
not.

**Also standing for all five:** the layer goes in the Style box and the section cues only,
**never in My Taste** unless it should play from bar one — My Taste has no section scope.
And negatives go in the **Exclude** box, never in the Style box, where naming them invokes
them.

---

## Round log

### Round 1 — parenthesis casting + accents. Failed on three counts.

**What we tried:** no saved Voice; Bob in the lead slot; **every Tarquin line in
parentheses**; accents described in detail (adenoidal Merseyside vs clipped RP);
a bracket cue roughly every two lines.

**What came back:**

| Symptom | Cause |
|---|---|
| The voice ping-ponged **within** verse 2 instead of staying Tarquin | Parentheses are a **mix-position** mechanism, not a name tag. They mean "backing singer standing behind the mic" — so a verse of nothing but parenthesised lines is a verse of nothing but backing lines, with a lead ghosting in and out. I used the slot as if it were a label. |
| **No Scouse at all** on Bob | The genre tag picks the vocalist pool, and accent adjectives are weak words fighting the prompt's strongest word. A regional accent isn't reachable by stacking adjectives. |
| Tempo **clicked into double time** for a stretch | Two suspects. Syllable cramming — when Suno crams too many syllables into a bar the vocal turns into a machine-gun rush. And cue density: a bracket every couplet chops a verse into micro-sections, each of which re-decides its own phrasing. |

**The ruling that follows: drop accents entirely.** Contrast the voices on
**texture and pitch**, which Suno renders easily, not on region, which it doesn't.

### Round 2 — texture contrast, no parentheses, stripped cues.

**Generated. Fixed the casting brief, broke the nationality:** with every accent
word removed, **both men came back American.**

Cause, and it's the useful one: the released take carried **"UK grime influence"**
in the genre stack. Round 2 dropped it. **The genre tag owns the vocalist pool** —
so the Britishness was never coming from the accent adjectives at all, it was
coming from the *genre*, and stripping the accents happened to strip the genre tag
that was holding the nationality up.

**Fix applied below, minimal:** `UK grime influence` restored to the genre stack and
front-loaded; `British` stated plainly and repeatedly in Style and My Taste;
Tarquin's register named as **BBC English** — a performance tradition the model
knows, rather than a region it can't render; the American exclusions widened.
Nothing else changed — the four-axis contrast, the zero parentheses and the
stripped cues all stand.

### Round 3 — round 2 plus UK anchoring.

**Generated. Nationality fixed, casting wrong:** both men came back as **UK grime
MCs** — a young-Black-British-MC register, when Bob is a fifty-something white
homeless Merseyside man and Tarquin a late-forties white City banker. The voices
stopped matching the characters we have pictures of.

**The refinement of §2a:** a genre tag doesn't carry a *nationality*, it carries a
whole **performer** — accent, age, class and race arrive together as one package.
Picking a genre for one attribute means accepting its default performer for all the
others. `UK grime` was doing exactly what it says on the tin.

**The fix is not to describe the men, it's to change the tradition.** Our own rule
(Thread 3 §7) is *cast performance traditions, not demographics* — a tradition the
model has heard performed lands; a demographic description averages into nothing. So:
swap grime for **British post-punk spoken word**, whose default performer is a
middle-aged white British man ranting over a beat. Same Britishness, right bloke, and
no demographic adjectives in the prompt at all.

### Round 4 — post-punk casting + the pronunciation pass.

**Generated. Casting solved.** Post-punk spoken word cast the two men correctly and
the nationality held. The remaining faults were word-level: `paralytic` and
`Châteauneuf-du-Pape`, both fixed by respelling (§4b) — `parra lettic` landed on the
third attempt and the wine came out fast and right first time.

### Round 5 — the orchestral layer, added. Right instruments, wrong entrance.

**Generated. The strings sounded good and arrived far too early.** Two faults, both
placement:

| Symptom | Cause |
|---|---|
| Cello and violin were **the first thing you hear**, before the voice | An instrument named in a prompt starts at bar one unless something stops it — and the lead-in cello cue plus a rich string paragraph in **My Taste**, which has no section scope at all, were between them pulling strings across the whole generation. It also made the track sound like GPOM, which is a real cost. |
| The drums that entered mid-verse-one were **the full drop kit** | Verse 1's header asked for `amen break + deep sub`, so verse one and the drop were the same weight. The drop had nothing left to reveal. |

**The ruling: three gears, and the orchestra is a drop-only event.** Nothing before the
drop is allowed to be at full weight — not the drums, not the strings.

### Round 6 — the three-gear arrangement. Strings fixed, gear 1 never showed up.

**Generated. The strings held off, and the middle gear didn't happen.** The
`[drums enter — a loose stripped-back break, dry and chopped, no sub bass yet]` cue
produced no audible change: the track went straight from no drums to the full drop kit,
so the run-up to the drop — the best part of the shape — wasn't there.

**Cause: an inline cue is a modifier, and the genre tag is the noun.** `UK drum and
bass, dark neurofunk` builds a track whose default kit *is* the full break; a
mid-section instruction asking for a weaker version of it is a weak word arguing with
the prompt's strongest word. Nothing had told the model a **new section** had started,
so nothing made it re-decide the arrangement.

**The fix is a section tag, not a better adjective** — see §4c.

### Round 7 — solo piano + four gears. Gear 1 arrived, and brought a hole with it.

**Generated. The section tag worked — and worked too literally.** `[Build]` did force the
arrangement change that the inline cue couldn't, so the breakbeat finally appeared. But
it also inserted **eight bars of instrumental** after *"but I bet that you paid for your
wheels on tick!"*, cutting the verse in half. The beat was never meant to interrupt the
words; it was meant to arrive underneath them.

**Cause, and it corrects last round's advice:** a section tag brings its **genre
convention** with it. In dance music `[Build]` *means* an instrumental lift into the
drop — that connotation is exactly why it succeeded at changing the arrangement, and
exactly why it emptied the section of vocals. **A tag whose name carries your intent
carries the rest of its meaning too.**

**Fix:** keep `Build` as the first word (it's what made gear 1 happen at all), delete the
bar count — a number is an invitation to fill that many bars — and state the vocal
continues, three ways over.

### Round 8 — the beat under the vocal, 16-bar drops. Structure right, register wrong.

**Generated. The shape landed and the mood collapsed.** The gap was gone, the beat
arrived under the vocal, the drops were the right length — and the whole track had turned
**pantomime**. The anger and resentment that four rounds of casting work had bought were
replaced by something bouncy and comic.

**Two causes, and neither is a mood word we asked for.** Nothing in any box requested
comedy; `comedic, novelty, parody, uplifting` were all already excluded. The register
drifted anyway:

| Cause | Why |
|---|---|
| **`a Chopin nocturne`** | A nocturne is a *melodic, ornamented, flowing* form — busy by definition, full of runs and arpeggios. Naming a **form** imports its **texture**, whatever adjective you attach. `mournful` never stood a chance against it. And the combination is the real damage: **British + spoken word + a bouncy piano is music hall**, which is pantomime almost by definition. The instrument flipped the genre from underneath the mood words. |
| **`Register: dark satire…`** in My Taste | `satire` is a **comedy noun**. The sentence went on to say "played completely straight", but naming a comic genre in the mood line invites comic scoring regardless — the same "naming a thing puts it in the prompt" rule that put the strings in bar one. |

**The ruling: describe the *silence*, not the composer.** Sparseness is a texture and has
to be asked for as one. And **state a register by what it is, not by the genre it
satirises.**

### Round 9 — sparse piano, register restated. Register fixed, density and gap both survived.

**Generated. Two faults left, and both had been described rather than specified.**

| Symptom | Cause |
|---|---|
| **Still too much piano** — a sequence of notes played fairly quickly, not the occasional note | Every instruction was an *adjective* (`utterly sparse`, `more silence than notes`, `no melody, no runs`). Adjectives are comparative and the model grades them against a piano's normal idiom — which is playing. **A piano's default behaviour is to perform a part**, so "sparse piano" resolves to "a sparse piano part", not to silence with notes in it. |
| **The gap in verse 1 refused to go away** even with `no instrumental gap` stated three times | The tag still opened with **`Build`**. In dance music that word *means* an instrumental lift, and the connotation outvoted three explicit denials. We were asking one word to mean the opposite of itself. |

**Both fixes replace description with specification** — a **rate** for the piano, and a
tag whose keyword implies **vocals** for the gap.

### Round 10 — the rate, and the end of the GPOM borrow.

**Generated. Two manual edits from Kai and one change of direction.**

Manual edits, both kept: the wine reverted to **`shatoe nerf doo pap`** (`narf` was worse
by ear), and the mid-verse `[Verse 1 continues …]` tag **deleted outright** — it was still
inserting a break, so the arrangement change now lives only in the `[Verse 1]` header,
where it cannot create a boundary. **That is the third mechanism tried for gear 1, and the
first one that cannot fail in this particular way.**

**The change of direction, and it came from a happy accident.** One take had an offbeat
piano chord sitting behind the beat — the reggae **skank** — and it fitted Camping better
than anything the orchestral pass had produced. Combined with a standing worry that the
GPOM borrow was becoming an overfit, that settled it:

| Was | Now |
|---|---|
| Solo piano playing sparse single notes | An **offbeat dub piano skank** — short staccato chords on the upbeats |
| Cello and violins, borrowed from GPOM | A **dub horn section** — trombone, trumpet, low tuba |

**Why this is the better idea and not just a different one:** the skank *is* sparse by
construction. Three rounds were spent trying to make a piano play fewer notes, and the
answer turned out to be **a rhythmic technique whose definition is one short chord and
then silence.** Stop asking for sparseness; ask for a pattern that has it built in.

### Round 11 — dub piano and horns. A style, but the wrong one.

**Generated. Coherent and wrong.** The dub layer produced a real, identifiable style —
and it was **upbeat and bouncy**, trading away the haunting, emotive quality that was the
whole reason for adding a second layer. The reggae feel also read as approximate rather
than convincing.

**The diagnosis worth keeping: an offbeat chord *is* the reggae feel, and a horn section
playing stabs is ska instrumentation almost by definition.** Brass was never the problem —
the **section** and the **stabs** were. That distinction is what keeps a solo horn on the
table (menu options 1 and 2) while the dub framing goes.

Also this round: **Suno's filter rejected the word `skank`** outright — an artist-alias
collision, not a content one. Recorded in §4c.

**Ruling: strip the dub, return to bare dark drum and bass, and choose the second layer
deliberately from a menu** rather than one instrument at a time. See
[the orchestral menu](#the-orchestral-menu--five-options-worked-through-one-at-a-time).

### Round 12 — menu option 1. Abandoned the whole orchestral idea.

**Generated. Two faults, and the second one ends the direction.**

| Symptom | Cause |
|---|---|
| **Whimsical** — the glockenspiel and horn read as twee despite every guard | An orchestral layer on a track whose *video* is two men rapping is a mismatch of register the prompt cannot argue its way out of. Five rounds of trying (GPOM strings → dub → glock/horn) all failed differently, which is the tell that the category is wrong rather than the wording. |
| **They started singing instead of ranting** | **A melodic accompaniment invites a melodic vocal.** Pitched instruments carrying a tune under a verse hand the model a melody, and it hands the melody to the singer. Four rounds of casting work were being undone by the *accompaniment*, not by any vocal clause. |

**Ruling: no orchestra, no acoustic instruments at all.** The second layer is now **big
wavetable synthesizers** — the sound of the genre the video already looks like, rather
than a layer imported from another one. **The orchestral menu is parked, not deleted**;
if a future track wants that treatment, the five options and their risks stand.

### Round 13 — big synths. **Working.**

**Generated and approved.** Six rounds of trying to import a layer from another genre
ended the moment we used the one the genre already has. Casting, timing, register and
delivery all held.

### Round 14 — plus a low electric guitar riff. *Drafted below, ungenerated.*

**Added, nothing removed.** A low palm-muted single-note guitar figure under both verses —
the *Lose Yourself* engine: bottom strings, dry and tight, one short figure repeating and
changing note only every bar or two. Not a solo, not chords, not fast.

**Two mechanical blockers had to be cleared first, and this is the reusable bit:**

| Blocker | Why it would have silently killed the guitar |
|---|---|
| `guitars` was in the **Exclude** box | Added rounds ago to keep a rock band out. A banned instrument does not appear no matter how well the Style box describes it. **Replaced with narrower bans** — `guitar solo, lead guitar, shredding, guitar strumming, power chords, acoustic guitar, wah` — which forbid the *behaviours* we don't want while permitting the instrument. `rock band` stays. |
| `no acoustic instruments anywhere` was in **My Taste** | Written to hold the orchestral wreckage out, but it is a *category* ban and an electric guitar sits close enough to trip it. Narrowed to `no orchestral instruments and no piano anywhere`, which says what we actually mean. |
| `Machine-made throughout` was in **My Taste** | The subtlest of the three, and it was missed on the first pass. A guitar is *played by hand*; a blanket "machine-made" argues against any played instrument. Cut. |
| `rock band` was in the **Exclude** box | Banned an ensemble but also dampened the guitar **tone**. Narrowed to `live rock band`. |

**A third blocker turned up only on a second pass, which is the real lesson.** My Taste
opened its instrument sentence with **`Machine-made throughout`** — written to keep the
orchestra out, but an electric guitar is *played by hand*, and that phrase argues against
it. Cut to `No orchestral instruments and no piano anywhere`, which bans what we actually
mean. **Two blockers found by looking, a third found only by looking again** — so the
grep is a procedure, not a glance.

**And `rock band` was narrowed to `live rock band`.** The old wording banned an ensemble
*and* dampened the guitar *tone* we now want. The new one is unambiguously about
instrumentation.

**Tone is stated three times, identically.** `distorted rock tone` in the Style box, and
`a distorted, overdriven rock guitar tone, hard and dirty` in both verse cues — because an
unstated tone defaults to whatever the model likes, which for `electric guitar` is often
clean. Verse 2's cue previously said only *"guitar"*; it now says
`distorted electric guitar` like the others. **Every mention names the instrument and the
tone in the same words** — varied wording reads as a second instrument.

**The general rule: before adding an instrument, grep the Exclude box *and* My Taste for
the instrument, for any category that contains it, and for any adjective describing the
palette as a whole** (`machine-made`, `electronic`, `acoustic`, `organic`). Both boxes
accumulate bans across rounds, and **a stale ban is invisible** — the generation comes
back without the thing you asked for, and it reads as the Style box being ignored.

---

## What the research says

Searched fresh, because round 1's failure was a casting failure and our own notes
were built on a different song. It agrees with the take you heard:

- **There is no multi-voice control in Suno, full stop.** "A Persona is not a
  separate singer lane." Role labels like `[Male]` / `[Female]` / `[Both]` are
  **"steering cues, not hard commands"** — Suno does not document any guaranteed
  switch that locks Singer A and Singer B to specific lines. It may follow you,
  partly follow you, blend the voices, swap the roles, or collapse the duet into
  one lead with harmonies.
- **More labels make it worse, not better.** "Adding more labels can sometimes
  make a duet worse." This is the direct rebuttal of round 1, where I answered a
  casting problem by adding casting markup to every single line.
- **Alternating short complete lines is the easiest duet pattern to stabilise.**
  Long simultaneous blocks are the hardest. Reduce lyric density before adding
  markup.
- **The reliable answer is production, not prompting** — generate the pieces
  separately and assemble them: *"That is not cheating. That is production."*
- **On the timing:** cramming syllables into a bar produces the machine-gun rush;
  the recommended resets are shorter lines and a `[Beat Transition]` /
  `[Short Pause]` between sections to give the model room to breathe.

**The structural insight this hands us:** *Camping isn't really a duet.* It's two
**solo** verses separated by a 32-bar instrumental drop, plus one traded bridge.
The verses never overlap — so the hard problem (two voices sharing a section) only
exists in the bridge, and the bridge is short-line alternating, which is the shape
Suno handles best. Everywhere else, **the drop is a seam we can cut on.**

---

### Superseded — the orchestral and dub attempts (kept for the diagnoses)

> **Everything from here to §5 is history.** None of it describes the current prompt.
> It is kept because the *failure analyses* are reusable — and several have been promoted
> into `docs/suno-gpt/` where they apply to any track. Read it for why, never for what.

Lifted from
[`../../gitpush-origin-master/songs/git-push-origin-master-dnb.md`](../../gitpush-origin-master/songs/git-push-origin-master-dnb.md),
which runs a real orchestra under 174 BPM drum and bass without either half
sounding bolted on. **Added, not swapped** — no vocal clause, lyric line, line break
or delivery cue was touched.

**The recipe, five parts, and the fourth is the one doing the work:**

1. **Name instruments with adjectives; never say "orchestral" and stop.**
   `a chilling solo cello`, `hushed creeping strings over a low drone`,
   `distant timpani`. The generic word alone buys generic strings.
2. **Say "a real dark orchestra."** `real` is fighting synth-preset strings.
3. **Scope it to the structure** — *sparse under the verses, full weight through the
   drops.* An orchestra with no dynamic instruction sits at one level all track and
   reads as a pad.
4. **The unity sentence: "so the strings and the break are one piece of music, not a
   remix of one by the other."** This is the load-bearing clause in GPOM's whole
   prompt. Without it Suno builds a D&B track and lays strings over the top; with it
   they're written together. If the orchestra sounds pasted on, this is the sentence
   that failed.
5. **Ban the operatic *voice* so you can keep the operatic *orchestra*.**
   `soprano, operatic vocals, vibrato, angelic voices, sustained vocal notes` are now
   in the excludes. The word `operatic` in the Style box is describing scale and
   drama; without those bans it also invites someone to start singing like that —
   which would wreck two spoken-word leads. `choir`, `female vocal` and
   `clean sung melody` were already there and pull the same way.

**Where it sits in Camping — and this is the one place we deliberately *don't* copy
GPOM.** GPOM opens on its solo cello, because the orchestra is that track's whole
identity. Camping is a D&B track that an orchestra walks into, so the orchestra has to
**earn its entrance** — and round 5 proved that a lead-in cue is not an entrance, it's
just an earlier start.

**The four gears.** The arrangement climbs in steps and nothing arrives at full weight
before the drop, so **the drop reveals three things at once**: the sub, the full kit and
the full strings.

| Gear | Where | Drums | Orchestra |
|---|---|---|---|
| **0a** | Intro, 8 bars | **none** | **solo glockenspiel, completely alone** — one note every few seconds, struck hard, cold, slightly detuned, ringing out into silence |
| **0b** | Verse 1, first half | **none** | the same glockenspiel, now under the voice |
| **1** | Second half of verse 1 — **no tag at all now**, the `[Verse 1]` header carries it, because every mid-verse bracket tried so far inserted a break | **dry chopped breakbeat, drums alone, no bassline** | glockenspiel continues; under the last two lines **one long low French horn note** swells and holds — also stated in the header, for the same reason |
| **2** | The drop, **16 bars** | **full weight, the Reese sub arrives** | **glockenspiel struck hard and high over the break**, cold and ringing. **No horn here** — the Reese owns the low-mid and the two would fight |
| **3** | Verse 2 onward | **stays full**, no going back | **nothing at all under verse 2** — the layer stays an event, not wallpaper. Drop 2 gets the glockenspiel higher and colder, plus the low horn held underneath |

**Camping's second layer is no longer GPOM's.** The orchestral borrow was always at risk
of becoming an overfit — two releases in one house style — and after five rounds of trying
to make strings sit right on this track, the honest read is that they never did. Camping
now has **its own lineage**: a dub piano skank and a dub horn section, which is reggae
sound-system music heard at drum-and-bass tempo. GPOM keeps the strings; Camping gets the
brass. **The recipe below still transfers — the instruments no longer do**, which is
exactly what "transplant the recipe, not the wording" was asking for all along.

**Brass rather than strings, and it does a different job.** GPOM's cello is *dread*, a
creeping bed under everything. Camping's horns are *punctuation* — short hard trombone and
trumpet stabs landing with the break, low tuba underneath for weight. Two BadCode releases,
two different orchestral families, two different functions.

**The skank retired this whole problem, and that is the lesson.** Three rounds went into
making a piano play fewer notes. The answer was not a better instruction — it was a
**different musical technique**, one whose definition is *a short chord on the upbeat and
silence everywhere else*. **When you keep asking an instrument to do less, look for the
playing style that already does less**; a named technique is specification, an adjective
is negotiation. The escalation below is kept because the ladder is reusable, but note that
none of its rungs beat simply changing the technique:

1. **`a Chopin nocturne, mournful`** (round 8) — worst of all. Naming a **form** imports
   its **texture**, and a nocturne is melodic and ornamented by definition. The mood word
   beside it was ignored.
2. **`utterly sparse, more silence than notes, no melody, no runs`** (round 9) — better,
   still busy. **Adjectives are comparative, and the model grades them against the
   instrument's normal idiom.** A piano's normal idiom is *playing a part*, so "sparse
   piano" resolves to "a sparse piano part" — which is still a part.
3. **`one low piano note every two seconds and silence in between`** — a **rate**. A
   number is not comparative; there is nothing for the model to grade it against.

**The general rule: when an instrument's default behaviour is the thing you're fighting,
give a number.** The intro cue goes further and denies that a part exists at all — *"this
is not a piano part and not a performance: it is five or six separate notes standing in
empty space"* — because the noun `piano` is itself an invitation to play one.

**How the offbeat piano is worded — and the one word you cannot use.** The correct
musical term is **`skank`**: reggae's offbeat chord stab, played on guitar or keys on the
upbeats between the kick hits. **Suno's tag filter rejects it** — almost certainly an
artist-alias collision (there is a well-known Brazilian rock band called Skank), which is
the same failure mode the playbook already records for hyphen- and space-stripped tag
matching. The term stays in this document because it is the right word for research; it
must not appear in any of the four boxes.

**The replacement is a plain mechanical description, and it is arguably better.** Name the
**behaviour**, not the tradition: `an offbeat dub piano — one short staccato chord stabbed
on each upbeat and nothing on the downbeat`, plus the dub production signature: `soaked in
spring reverb and tape delay`, `ringing away into empty space`. This costs a few
characters and gains precision — a genre term is a bundle you have to trust, whereas the
description says exactly which beat the chord lands on. The intro cue adds `the offbeat
chords alone set the pulse`, because an offbeat pattern with no drums has nothing to be
offbeat *from* and the model needs telling that's deliberate.

**Two traps this brings, both now excluded.** `ska, ska horns, oompah, brass band,
marching band, dixieland, New Orleans, upbeat horns` — an offbeat chord plus a tuba is
*literally* oompah, which is the pantomime failure of round 8 waiting to happen again. And
`ragga MC, toasting, Jamaican accent, dancehall vocal` — dub carries a default vocalist
exactly as grime did, and this track's casting took four rounds to win.

**The lever not pulled: `jungle`.** Jungle is what happens when dub and reggae are played
at 174 BPM — it is the historically correct name for what this arrangement now is, and
adding it to the genre stack would get the dub relationship for free at no tempo cost
(jungle lives at 160–175). **It is deliberately not in the prompt**, because a genre tag
carries a whole performer and jungle's default vocalist is a ragga MC. If the dub feel
comes back too weak, that is the next thing to try — and the excludes above are already in
place to protect the casting when it is.

**This deliberately reverses round 5's ruling, and the reversal is safe because it runs
downhill.** Round 5's problem was holding an instrument *out* of bar one, which is the
hard direction. Putting the piano *at* bar one is the easy direction — naming it is
enough. What's now hard is holding the **violins** back to gear 1, and that gets the
round-5 treatment:

1. **The French horn is named in exactly three places** — the `[Verse 1]` header, drop 2,
   and one clause of the Style box. Nowhere else. Every instrument we have removed —
   `violins, cello, string section, orchestral strings, reggae, dub, ska` — now sits in the
   **excludes**, which is where a removed instrument belongs.
2. **The horn stays out of My Taste**, which has **no section scope**. The glockenspiel
   *is* in My Taste, and that's consistent rather than contradictory: an instrument that
   should play from bar one is exactly what My Taste is safe for, and one that must arrive
   late never belongs there.
3. **The intro cue says `no horn` explicitly.** This is the one place naming an absence is
   worth the risk, because the glockenspiel has already told the model a second layer
   exists — which is the leak path this arrangement creates.

**Gear 1 gets a section tag, not an adjective — this is the round-6 lesson.** The inline
`[drums enter — a loose stripped-back break…]` cue did nothing, because an inline cue is
a *modifier* and the genre tag is the *noun*: `dark neurofunk` builds a track whose
default kit is the full break, and a mid-section request for a weaker version is a weak
word arguing with the strongest word in the prompt. **`[Build]` is a real structural tag
that Suno treats as a section boundary**, which is what forces a fresh arrangement
decision — and in drum and bass it already *means* "the bars before the drop", so it
carries the intent for free. The voice label is repeated inside it so the section break
can't be read as a cast change.

**But the convention is a package deal, and rounds 7–9 paid for it three times.**
`[Build]` in dance music means an *instrumental* lift, so the tag that finally produced
the breakbeat also produced bars with no words in them — and it kept doing it after
`no instrumental gap` was stated three separate ways. **A recognised keyword's connotation
beats any number of denials, because the denials are adjectives and the keyword is the
noun.**

**The fix, round 10: keep a recognised structural keyword, but pick one that implies
vocals.** `[Verse 1 continues — no pause, no gap, the same man carrying straight on into
the next line | …]`. `Verse` is as structural as `Build`, so the section boundary — the
only thing that ever made the breakbeat appear — survives; but a verse *is* the sung part,
so there is nothing to fill with music. **When a tag fights you, don't argue with it,
replace the keyword.**

**And say it twice, in the header and at the point of change.** The `[Verse 1]` header
now also carries `no drums and no bass for the first half of this verse, then a dry
chopped breakbeat comes in underneath the vocal and runs to the drop | the words never
stop and there is no instrumental passage anywhere in this verse`. A **header** is not a
section boundary, so it costs nothing and cannot create a gap — it is free reinforcement.

Two corrections kept from round 7, both still cheap:

- **Delete the bar count.** `[Build — 8 bars]` is an instruction to fill eight bars, and
  with no lyric under it the model fills them with music. Length is inferred from the
  lines instead.
- **Say the vocal continues, more than once.** `the beat arrives underneath the vocal, no
  instrumental gap, no break in the words` and `carrying straight on` are three
  statements of one thing, which is the right amount for a clause fighting a genre
  convention.

**The trade to know, and it is now the live risk:** `Verse 1 continues` has no
build-up connotation to trade on, so it may not carry enough energy-change signal to
trigger the breakbeat at all — which is round 6's failure returning by a different road.
**If the drums never arrive, that's the cause.** Escalate in this order: add
`the beat kicks in here` to the same tag → then `[Verse 1 continues | Build]` (both
keywords, vocals first) → and only then go back to `[Build]` and accept the gap.

**`breakbeat` is deliberately not in the Style box.** As a genre tag it drags the whole
track toward ~130 BPM big beat, and this track's tempo took a round to settle. Gear 1 is
described instead — `loose and stripped back, dry and chopped, no sub` in the Style box,
and a bracket cue in the lyric sheet where its scope is unambiguous.

**No vocal cue, lyric line, line break or respelling was touched by any of this** —
every arrangement instruction sits in an instrumental cue, a section header's
arrangement clause, or the Style box.

### Two corrections worth keeping (2026-08-20)

**Transplant the recipe, not the wording.** The first pass lifted GPOM's string language
*verbatim* — `a chilling solo cello`, `hushed creeping strings over a low drone`,
`distant timpani`. Of course it sounded like GPOM: it **was** GPOM. The five-part recipe
above is portable; the specific phrases are that track's identity and are not. Two
BadCode releases sounding like one house style is a real cost, and the fix is to write
the second track's strings in its own words.

**So Camping's orchestra does a different job with the same instruments.** GPOM's is
*atmospheric* — a creeping bed of dread running the whole track. Camping's is
**rhythmic** — hard short stabs cut against the amen break, arriving only at the drops.
Same section of the orchestra, opposite function, and that difference reads more
strongly than placement alone.

**An orchestra with no start instruction starts at bar one**, and round 5 confirmed it
the hard way. Naming an instrument anywhere in a prompt puts it in the track from the top
unless something says otherwise. The absence is therefore stated *positively* — `intro
and first half of verse one are city noise and voice alone, no drums` — rather than as
"no strings", because naming a thing puts it in the prompt whatever word sits in front of
it. **Deleting the mention beats describing its absence.**

**The bridge cue was left alone deliberately** — it's carrying the fragile two-voice
trade, and diluting that clause to add strings is a bad trade. If the orchestra should
do story work anywhere it's there (it's the turn, and the warmth arrives), so that's
the *next* thing to try once the casting is settled.

**Two things to watch:**

- **`epic trailer music` is a two-edged exclude.** It keeps the strings from going
  generic-cinematic, but GPOM records it as the prime suspect when big sections come
  back limp. **If the drops lose weight, remove this one first.**
- **The Style box is 991 characters** against a 1,000 ceiling — it runs close every round.
  A maxed box outvotes its own vocal clauses, and these voices took four rounds to win, so
  **if the casting regresses, the arrangement clause is the newest thing in the box and the
  first suspect.**
  **Already spent** (do not go looking for these): `a working-men's-club voice through a
  cheap mic`, `Rolling Reese bass and chopped amen breaks`, `the same age`, `unhurried`,
  `close-mic'd`, and `dark neurofunk` folded into a leading `Dark`.
  **Trim next, in this order:** `slowly filtering open, cold and menacing` (the intro cue
  carries it) → `bending, formant-morphing` (the drop cues carry it).
  **Never trim:** the unity sentence; `dry chopped breakbeat … no bassline` (that is the
  mid-verse gear, which has already failed twice); `British post-punk spoken word` (the
  casting rides on it); or `one steady tempo throughout`.
- **Both drops are 16 bars, down from 32.** There is no chorus, so two 32-bar
  instrumentals were ~45 seconds each with nobody talking; 16 bars at 174 BPM is ~22
  seconds. Drop 2 was shortened too, though only "the drop" was asked for — two drops of
  different lengths would read as a mistake rather than a choice. One number reverts it.
- **`skank` is filter-blocked and must never go in a box.** Suno rejected it outright. If
  any other plainly innocuous musical term comes back rejected, assume an **artist-name
  collision** rather than a content filter, and describe the mechanic instead of naming
  it — which is the more robust prompt anyway. Same reasoning keeps `Serum 2` out.
- **The guitar and the synth stab both repeat, and they may fight.** The stab arrives with
  the breakbeat in the second half of verse 1, over a guitar figure that is already
  repeating. Kept because nothing was to be removed this round, but **if the run-up to the
  drop sounds cluttered or muddy, cut the synth stab first** — the guitar is the new thing
  and the one carrying the reference.
- **The guitar is deliberately out of My Taste**, which has no section scope: it must not
  play under the intro. It is named in exactly three places — the Style box and the two
  verse headers.
- **The intro could open on the guitar instead.** *Lose Yourself* does, and it would give
  the track a hook. It is not written that way because the bare single-synth opening is
  the one part of the arrangement that has worked from the first attempt. One edit to try
  it.
- **Listen for the register and the delivery before anything else.** Two failures arrived
  without a single mood or vocal word changing: round 8 went **pantomime** because a busy
  piano plus British spoken word is music hall, and round 12 made the two men **sing**
  because a melodic accompaniment invites a melodic vocal. **If either returns, look at
  what is playing underneath — not at the adjectives.** Guards in place: the anti-comic
  and anti-singing sets in the excludes (negatives live there, never in the Style box
  where naming them invokes them), `bitter and angry` and `ranted and spoken throughout`
  stated positively in the Style box, and `no orchestral instruments and no piano anywhere`
  in My Taste. **The guitar riff is a low single-note figure, not a tune** — the reference
  track is rapped over, which is the evidence it will not invite singing the way the
  glockenspiel did.

## Sources

- [Can Suno Use Multiple Personas in One Song? Duets, Bands, and AI Casts](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/can-suno-use-multiple-personas-duets-bands-ai-casts)
- [Suno Duet & Harmony Guide: Vocal Roles, Labels & Fixes (2026)](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/duet-harmony-theme-meta-tags-suno)
- [Suno Song Structure: Brackets, Vocal Tags & Lyric Formatting](https://paddystudio.com/blog/suno-song-structure-and-vocal-tags/)
