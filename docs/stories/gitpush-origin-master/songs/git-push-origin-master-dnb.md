---
title: git push origin master (drum & bass)
status: drafting
model: v5.5 (cue-heavy track — 5.5 obeys the bracket architecture; 4.5 shreds it)
settings: style influence 72, weirdness 50
bpm: 174
voices: [newsreader (male, dark gravelly RP — the bulletins, and nothing else), the terrace (hundreds of hoarse untrained men shouting in unison — the whole of every drop)]
sibling: songs/git-push-origin-master-orchestral.md
---

# git push origin master — drum & bass cut

The club sibling of
[`git-push-origin-master-orchestral.md`](./git-push-origin-master-orchestral.md).
Same story, same bulletins, same four-line hook. **The orchestral cut stays
the canonical master and is not touched by this file.**

## Start here — the running order

You have one orchestral take with a narrator everyone likes, and no Voice
built yet. Four stages, in this order.

### Do we attach a Voice to this track or not? — build it, don't attach it yet

The two halves of that question have different answers, and conflating them
is the trap:

- **Build `BC-NEWSREADER` now, before anything else.** Not for this song —
  for the story videos, and as insurance. Right now the best vocal
  performance we own exists as exactly one artifact in a Suno workspace.
- **Don't attach it to round one of this track.** The orchestral cut landed
  its narrator **prompt-only, first time, no saved Voice**. And a Voice has
  no section scope: it's a whole-track vocal identity, so **every reason to
  attach it is also a reason the chorus gets harder.** It is the
  fallback for a specific failure, not the default setup. **Round one
  confirmed it: he holds the lead prompt-only, so no Voice is needed here.**

### Stage 0 — build `BC-NEWSREADER` off the orchestral take (~10 min, once)

1. On the orchestral take: three dots → **Remix → Voice**.
2. **Select a sub-region containing one bulletin only.** Spoken register,
   never a chorus — a clip that switches between speaking and chanting makes
   an unstable clone. 15 clean seconds beat 60 contaminated ones; up to ~2
   min clones more stably.
3. **Delete the attached style prompt.** Miss this and the Voice is welded
   to the orchestra and won't travel to a D&B track. This is the one
   irreversible-feeling mistake in the sequence.
4. Name it `BC-NEWSREADER`. Done — it's now available to every future track
   and video.

*Why this route and not `Voice → Create voice` → upload:* that path runs
Suno's ownership check (read a phrase aloud, matched against the reference),
which is built for proving a **human** voice is yours — expect friction or a
hard block on a synthetic one. Remix → Voice has no such check. If the clone
comes out weak, upgrade the *source* rather than the route: three dots →
**Get stems / MIDI** → **advanced split** (regenerates stems instead of
spectrally carving them — much cleaner) → vocals → WAV → trim to a
bulletins-only pass in a DAW → then clone from that.

### Stage 1 — pre-flight (the step that silently ruins round one)

1. **Swap My Taste.** Profile → My Taste → replace the whole box with this
   file's block. If Camping's profile is still loaded you will get a Scouse
   MC; if the orchestral cut's is still loaded you will get an orchestra with
   no drums. It cannot be disabled, only replaced.
2. Create → **Advanced Mode**, model **v5.5**.
3. Separate workspace/folder for this cut if you can — and thumbs-down every
   reject as you go. That's the only lever on the half of My Taste that
   learns from your library without a control surface.

### Stage 2 — round one, with the Voice selector untouched

1. **Four pastes, in order: My Taste → Style → Exclude Styles → Lyrics.** All
   four, from this file, every round. Never "Reuse Prompt" — it silently
   carries stale boxes, and a stale Lyrics box is inaudible as such; it just
   sounds like the Style box is being ignored.
2. Style influence **75**, weirdness **30**. **Do not touch the Voice
   selector.**
3. Generate **3–4 takes**.
4. Judge each on exactly four questions — conflating them is why AI-music
   feedback is usually useless:

   | # | Question | If it fails |
   |---|---|---|
   | 1 | Are the bulletins **spoken** by a calm RP newsreader — not rapped, not an MC, not sung? | Re-roll twice, then the spoken-word ladder, then Stage 3 |
   | 2 | Does the hook ride a **drop** — full break, the chant on top of it, not a sung section beside it? | Re-roll; check the `[Build]` / `[Drop]` tags survived |
   | 3 | Is the chant **fast** — each line rattled out in one breath, no gaps between words? | Density, not adjectives — see the timing section |
   | 4 | Is it a **rough shouted crowd** — not high, not operatic, not sung, no solo voice? | Style box first, then the excludes; see the terrace section |

   Questions 3 and 4 are the live ones. Confirm the `( )` survived the
   paste — they're the casting mechanism and the easiest thing to lose — and
   confirm **no commas crept back into the chant lines**, because a comma is
   a beat of inserted space and it is what made the hook drawl.

5. **If question 1 passes, you're done with the Voice question for this
   track.** Don't attach it. Keep `BC-NEWSREADER` for the videos and for
   holding the character across EP1.

### Stage 3 — only if the newsreader loses the lead slot

Symptoms: rhythmic delivery, bars landing on the beat, swing nobody asked
for, hype energy. That's the D&B vocalist pool asserting itself, and no
adjective stack jumps pools.

1. **+ on Voice** → `BC-NEWSREADER`. The audio-influence slider appears:
   **40–60**. Re-paste all four boxes fresh.
2. Drifting? Raise to **70+** and accept artifacts.
3. **Expect the chorus to get harder from here.** That's the leak, and it's
   the price of the fallback — which is exactly why Stage 2 comes first.
4. Voice right but audio rough → **two-pass down**: Remix → **Cover**, same
   style and lyrics, audio influence **~25–40**.
5. Once the Voice pins the lead, **strip `rap, MC, ragga chat, toasting`
   from the excludes** — that armour was protecting the lead slot the Voice
   now owns, and it suppresses backing texture we want.

When you move to another track, swap My Taste again.

## What this cut is fixing

The orchestral master works, and the part that works hardest is the
newsreader. First-listen feedback splits cleanly along one seam:

| Lands | Doesn't |
|---|---|
| The narrator's entrance, the bulletins, the composure, the dread | The chorus |

Three separate complaints, all arriving at the chorus:

1. **"That voice shouldn't be swearing."** The newsreader's authority is
   built out of his restraint. Spending it on *fucking disaster* is the one
   moment he stops being the BBC and starts being a bloke. The authority
   doesn't survive it.
2. **It's too slow.** `git, push, origin, master` — four words, four commas,
   four beats. In that space the chant should have delivered the whole
   quatrain. The listener is hearing a hook at a quarter of the speed their
   ear has already set.
3. **They expected drum & bass to kick in.** Three minutes of mounting
   orchestral pressure with no beat writes a cheque the orchestral cut
   deliberately doesn't cash. On a BadCode track, the audience assumes the
   drop is coming.

All three are the same note: **the chorus is a drop, and it isn't being
played as one.** So this cut plays it as one.

### What round one settled (2026-08-08)

First generations off this file. Three things resolved and one still open:

- **The style works.** The D&B/orchestral hybrid landed — the break under
  the strings is the track. Locked; stop tuning it.
- **No Voice needed.** The newsreader holds the lead slot prompt-only in
  this genre, exactly as he did on the orchestral cut. `BC-NEWSREADER` is
  still worth building for the story videos, but **this track doesn't need
  it** — which also means the chorus never has to fight a whole-track vocal
  identity. Stage 3 below is now a contingency, not a plan.
- **The newsreader took line four back, unprompted.** Across takes, *the
  compiler is stuck on 16 bit* kept coming back in his voice rather than the
  choir's — which proved the lead/backing seam runs per *line*, not per
  section. Briefly locked in as a call-and-response device; **retired in
  round two** (see below), but the mechanism it revealed is permanent.
- **Open: the chorus voice.** Schoolchildren were the wrong call — see the
  post-mortem below. The chorus is the only remaining block.

### What round two settled (2026-08-08, later)

- **Weirdness 30, not 60.** Better takes at 30 across the board. This
  overrules the house default (60–65, the "creative sweet spot") on the
  evidence, and it's consistent rather than surprising: this is a
  **cue-heavy track**, and cue-heavy tracks want obedience everywhere. It's
  the same reason v5.5 beats 4.5 here. When the architecture lives in the
  brackets, randomness has nothing to add and plenty to break.
- **One variant, not three:** B and C merged (see below).
- **The crowd takes the whole chorus.** The line-four split is out.
  *(Reviewed and half-reversed the same day: the crowd keeps all four
  lines, but the parentheses went back on — see "The parentheses — settled
  by the evidence".)*

### What round three settled (2026-08-08, from four generated takes)

The first real listen to generated audio off this file. **The instrumental
is right and is now locked** — the dark operatic orchestra and the D&B
underneath are the track, and nothing below touches them. Everything else
that came back was one of four problems, and three had the same root.

- **The chant was slow.** *git — push — origin — master.* Root cause found
  by research and it was self-inflicted: **commas are a beat of inserted
  space**, four short lines add three more pauses, and the cue literally
  asked for `one word per beat`. Fixed by density — see the timing section,
  which is the most important part of this file.
- **The chorus was operatic.** Too high, too dramatic, too *sung*. Root
  cause: the Style box asked for it — `gospel choir`, `congregation`,
  `singing`, `hall`, next to a full orchestra. Fixed by cutting the gospel
  half entirely and going pure terrace.
- **The newsreader still alternates into the chorus.** Consistent with the
  known line-four leak rather than new. The line-merge should dissolve it
  as a side effect (a short standalone clause reads as a lead answer; the
  tail of a 19-syllable rush doesn't).
- **The bulletins ran their opening lines together** — *good evening this is
  the news* as one breath. **Kai's fix was already correct**: splitting onto
  separate lines inserts a phrase-length pause, which is exactly the
  documented behaviour of a line break. Kept as-is.

**Structural change: `[Chorus]` is now `[Build]` + `[Drop]`.** Kai's read
was that the hook should happen *during* the drum & bass drop rather than
being a sung chorus that sits next to it. The tag vocabulary supports this
directly — `[Build]`, `[Drop]` and `[Breakdown]` are the electronic-genre
structure tags, and the guidance is to place `[Drop]` immediately above the
lyric lines it governs, which is now how the lyrics are written. There's a
second benefit: **the word "Chorus" was itself pulling toward a sung
melodic chorus**, so renaming the section removes one more vote for the
operatic reading. The `[Build]` also gives the operatic climb Kai liked a
formal home instead of leaving it to chance — which does retire the "drops
in cold, no transition" device inherited from the orchestral cut. That
device was written for a track with no drums; a D&B drop wants tension
before it.

### What round four applied (2026-08-08, from the songwriter research sweep)

An 11-agent sweep of the songwriter-facing web
([`../../../suno-gpt/files/lyricist-playbook.md`](../../../suno-gpt/files/lyricist-playbook.md))
turned up five things that bear directly on this track. Caveat up front: **none of that material
was gradeable as tested** — it is assertion-grade, so everything here is a cheap hypothesis, not a
correction.

- **`[Chant]` is a real tag, and it is what we have been describing in prose all along.** Reported
  to produce "a rhythmic, monotonic, group-delivered near-spoken vocal with percussive timing
  rather than a melodic line." Added to every drop, stacked with `[Drop]`. The same source notes
  `[Post-Chorus]` and `[Chant]` exist *because* plain `[Chorus]` defaults to sung melody — which is
  independent support for round three's rename.
- **Bar counts work as duration control.** `[Build - 8 bars]`, `[Drop - 16 bars]`,
  `[Outro - 4 bars]`. Applied throughout, which also pins the drop length rather than leaving it to
  chance.
- **Numerals should be spelled out** — Suno sounds words out from spelling. `16 bit` → **`sixteen
  bit`**. (The one exception is number-words that collide with producer-tag aliases after Suno
  strips spaces and hyphens; `sixteen` is not one.)
- **An explicit `[Outro]` is worth having.** One source attributes "90% of abrupt cutoffs" to a
  missing ending tag. Added after the power-off drop.
- **Cue overload is now a named suspect.** Sources warn against stacking more than 3–4 directions
  in close proximity. Our drop headers were running to seven or eight clauses. Trimmed to three
  each, and the redundant ones (`shouted and never sung` alongside `[Chant]`; `twice through` when
  the lyrics already show two passes) deleted. If a cue still gets ignored, the sweep's advice is
  to **simplify further and re-roll** rather than escalate — which is the opposite of our house
  ladder, so try the cheap one first.

### What round five applied (2026-08-08, from four more takes — two changes only)

Kai's generation pattern is style influence 70 / weirdness 30, a couple of generations for ~four
takes, then one at weirdness 60 as a probe. After that round: *"it's getting there"*, the
instrumental is still right, and exactly two things were wrong. Both fixes are deliberately small
and confined to the lyrics box — **the Style box and the Exclude list did not change**, so the only
variable moving is structure.

- **Tracks run too long, because the gap between the bulletin and the beat is too long.** The build
  was doing the damage. `[Build - 8 bars]` → **`[Build - 2 bars]`**, and the prose cue that was
  describing a whole cinematic climb (*strings climbing, drums rolling up beneath, tension
  gathering*) replaced with **`a short sharp riser straight into the drop, no long instrumental`**.
  The bar count alone was probably not the lever — a cue that *describes* a long build invites one
  whatever number precedes it, so the prose had to go too.
- **The hook should land *with* the beat, not after it.** Round three moved the hook under `[Drop]`
  so it would ride the drop; the takes show that it still gets a run of instrumental drop first.
  Each drop cue now opens with the simultaneity stated as an event rather than implied by
  placement — *"the break slams in at full weight **and the crowd shouts the hook on the same
  beat**, no instrumental bars before the vocal"*. Kept to three clauses per header, per round
  four's cue-overload rule.

Two changes, one box. If the length is still wrong after this, the next suspects in order are the
two `[Instrumental | brief]` bridges between sections and the three-bulletin structure itself —
but change one at a time.

### What round six applied (2026-08-08, the de-escalation)

Round five didn't fix the gap, and Kai read the lyrics box back and named the reason: *"that's a
really long prompt and it's competing. It feels like we might have over-complicated things."*
Correct, and it is the failure round four already had a name for — **cue overload**, whose recorded
remedy is *simplify and re-roll*, not escalate. Rounds four and five escalated. This round reverses
that.

The structural mistake underneath it: **a section tag makes a section.** `[Build - 2 bars]` asks
Suno to open a section and then not perform it, which is not a thing a section tag can do. Bar
counts modulate a section's length; they cannot suppress its existence. Same for the two
`[Instrumental | brief]` bridges — "brief" was doing nothing against the fact that each one is a
whole passage, once per cycle.

So:

- **`[Build]` deleted, all three.** The cello burst Kai wants moved *inside* the drop header —
  `one bar of cello then the break hits and the crowd shouts with it` — where it is an event at the
  top of the drop rather than a section that can grow.
- **Both `[Instrumental | brief]` bridges deleted.** The bulletin cues already describe their own
  backing, so the reset is still specified; the drop now cuts straight to the newsreader, which is a
  better device than the wind-down was.
- **Bar counts dropped** from `[Drop]` and `[Outro]`. `[Drop - 16 bars]` was probably adding length
  too: the chant is four lines and likely doesn't fill sixteen bars, so the remainder ran on
  instrumental.
- **Drop headers cut roughly in half** — three short clauses (entry, voice, speed) instead of three
  long ones. `no instrumental bars before the vocal` and `rattled off fast, no space between the
  words` are gone as *separate* instructions; `the break hits and the crowd shouts with it` and
  `fast, no gaps` say the same thing in a fraction of the words.

**What was deliberately not simplified:** `[Drop] [Chant]` stays rather than becoming `[Chorus]`.
`[Chorus]` is what produced the high sung operatic reading that round three was built to kill; the
two tags are short and each is load-bearing. The bulletins are untouched — Kai's verdict is that
what's there is always good, and the regression rule says a section someone likes is evidence.

Structure is now: intro → bulletin → drop → bulletin → drop → bulletin → drop → power-off → outro.
Nine sections where there were fourteen.

### What round seven applied (2026-08-08, the timing baseline)

Round six's de-escalation still didn't land the chant, and Kai called the method rather than the
output: *"let's get to the stage where the chorus is working consistently on the prompt we have for
the chorus and then maybe build up what's around the chorus from there… I don't really care about
song composition and I don't really care about tonality on the voice for the moment. I care about
just timing and getting that as the baseline."*

That is the right protocol and this file should have arrived at it three rounds ago. Every round
since three has changed several things at once and then guessed which one moved the result.

**The duplication nobody had noticed.** The drop header's voice clauses were a second copy of the
Style box. The Style box already says *every drop is taken over completely by a football terrace
crowd shouting the hook in unison, hundreds of hoarse untrained working men, rough and flat and
hammered out hard on the beat, shouted and never sung*. `rough hoarse football terrace in unison,
never a solo voice` re-states that in different words a few tokens later. Two near-identical
instructions in different phrasings are not reinforcement — they are the competition Kai was
hearing. Deleted, and the division of labour restated:

| Box | Owns |
|---|---|
| Style | the voice and the sound |
| Section tags | the structure |
| Lyric lines and their punctuation | the timing |

Nothing should appear in two of them.

**The drop headers are now `[Drop] [Chant]` and nothing else.** No cello, no crowd description, no
speed cue. The cello burst comes back later if it's wanted; it is composition, and composition is
not what is being tested.

**The A/B.** Kai's other question — commas after `git` and `push` — is a real question and the
existing evidence does not settle it. Round three removed all commas because commas insert a beat
of space and the delivery was drawling. But the rhythm Kai is now describing is *git · push ·
origin master* — three stress units with the last two words run together, which is the actual shape
of a terrace chant, and that is a different thing from the four-way `git, push, origin, master`
drawl that round three killed. So it gets tested rather than argued:

- **A (control)** — headers stripped, chant lines unchanged. Answers: *was the header the problem?*
- **B** — headers stripped, plus `git, push, origin master this code is a fucking disaster`.
  Answers: *does scoring the stress pattern beat leaving it to the model?*

Run A first, both generations. Only if A still drawls does B tell you anything clean, because
running both at once reintroduces the two-variables-at-once mistake this round exists to stop.

**Rejected: a cut-down test song.** Suno generates to full length regardless of lyric length, so a
one-bulletin rig costs the same and generates no faster — while risking the model *stretching* the
chant to fill the time, which is the exact variable under test. All three bulletins stay, because
they keep the model occupied.

### What round eight applied (2026-08-08, timing solved, richness returned)

**Variant B won, and it is this project's first tested finding.** `git, push, origin master` lands;
the bare line drawls. Folded into the single cut — there is no A any more. The mechanism, stated
carefully so the corpus doesn't over-learn from it:

> Two commas score **three** stress units — *git · push · origin master* — which is the shape of a
> real terrace chant. Round three's failure was `git, push, origin, master`: **four** units, four
> pauses, a drawl. Same punctuation mark, opposite result, because what a comma does is mark a
> stress boundary; the delay is a side effect of the boundary, not the point. Commas are a
> **scoring** tool, not only a brake.

That is a genuine correction to the corpus, which recorded only the brake half. Written into
`lyric-craft.md`, graded **tested**, which none of the punctuation material was before.

#### The adversarial pass on the Style box

Kai's read after round seven: timing solved, the terrace chant working, but the newsreader takes
the chorus about half the time, and the chorus wants to be **richer** — the operatic weight that
the orchestral cut has. Three faults, and the first is almost certainly the casting leak.

1. **The box opened by declaring the track has one voice.** *"Carried by **one** dark gravelly
   British male voice…"* — a whole-track vocal identity claim in the highest-weighted position in
   the prompt, with the crowd arriving afterwards in a subordinate clause. Half the time Suno was
   obeying the first six words. Now: **`Two voices.`** as the opening sentence, then one sentence
   each, both in main clauses, neither subordinate to the other. This is the round's most important
   change and the one to credit or blame first.
2. **The orchestra was explicitly scoped away from the drops.** *"**Under the bulletins** a real
   dark orchestra…"* — the box was telling Suno the orchestra belongs to the newsreader sections.
   The thin chorus was specified, not emergent. Now: *"A real dark orchestra runs through the whole
   track… then full weight alongside the crowd through every drop"*, plus `low brass`. **This is
   where the richness comes from, and it costs nothing on the vocal** — which matters, because the
   vocal is where every previous attempt at richness went wrong.
3. **`recorded like a real crowd in a real stadium` was a thinning instruction.** Stadium reads as
   roomy, distant, ambient — documentary realism, rendered far away. Replaced with `close and dry`.
   And the four separate ways of saying rough (`rough and flat`, `untrained`, `shouted and never
   sung`, `hammered out hard`) were the same duplication disease round seven found in the drop
   headers, and they were actively fighting the richness now wanted. Reduced to `hoarse untrained`,
   `hammered out hard on the beat` and `chanted not sung`, with `roaring… low and massed and huge`
   carrying the weight. **`shouted` → `roaring`** deliberately: shouting is thin and flat, roaring
   is loud with body in it, and body is what was missing.

`operatic vocals` pulled from the excludes. It was the standing risk to the operatic *instrumental*
(the Exclude box is global and fuzzy, and the word now appears on the orchestra clause), and the
vocal side is already covered unambiguously by `soprano, choral harmony, vibrato, angelic voices,
sustained vocal notes`. My Taste updated to match the Style box, since a My Taste still saying
`rough and flat, shouted and never sung` would contradict it on every generation.

Style box is 903 characters, under the 1000 ceiling.

#### The rule for what may go in a drop header

Round seven stripped the headers because they duplicated the Style box. Richness is going back in
via the Style box, not the headers, and the headers get one narrow licence:

> **A section header may only say what the Style box cannot** — that is, what **differs between
> sections**. Voice, texture and sound are global and belong to Style. Escalation is per-section
> and belongs nowhere else.

So: `[Drop] [Chant]`, `[Drop] [Chant | bigger]`, `[Drop] [Chant | biggest, the whole orchestra with
the crowd]`. Three words, two words, eight. If the arc doesn't come through, the escalation is the
thing to strengthen — and it is the *only* thing in the headers, so it can be strengthened without
reopening the competition round seven closed.

### Where round eight landed — read this before changing anything

**Round eight worked, and the cut above is the one that produced a keeper.** Kai's verdict:
*"this is really working now… I have a version right now that really sounds good to my ears."*
Paused there deliberately, at eight rounds of listening — *"I can't see the wood from the trees"* —
with six or so more generations rolled off the same settings, and feedback to come.

Two things to record while they are still true:

- **Settings drifted to style influence 72 / weirdness 50** on the takes that landed, and the
  weirdness move matters more than the number suggests. See the settings note under
  "Suno prompt" — the round-two argument for weirdness 30 was correct *for a prompt whose
  architecture lived in bracket cues*, and rounds seven and eight moved that architecture into the
  Style box, which is what made the headroom safe. Obedience is worth buying in proportion to how
  much you are asking for.
- **The keeper has a texture nobody prompted: a heavy choir across the first half of the drop and a
  *robot newsreader* across the second.** That is the vocoder — twice rejected on this song by
  deliberate decision — arriving on its own and being liked. It is not in any box. If it is wanted
  reliably it has to be earned back deliberately, and the file's standing warning still applies:
  asking for robotic vocals *by name* previously read to the model as a tag conflict and cost more
  than it bought. The cheaper first move is to leave it as a dice-roll and pick the takes that have
  it.

**The next change to this file should be driven by Kai's feedback on those generations, not by
another idea.** Eight rounds in, the failure mode has consistently been changing several things at
once — and the last two rounds worked precisely because they stopped doing that.

### The syllable gamble, stated honestly

Round three merged the hook into two long lines to force speed. The sweep both **confirms the
mechanism and flags the risk**:

- Confirmed: density is the accelerator, and **short lines are not fast** — sources recommend short
  lines for *slower, clearer* delivery and warn they can produce awkward pauses.
- Flagged: the safe band is ~6–12 syllables, and **past ~15 the model compresses, smears consonants
  and mumbles — with a *lower* ceiling at 170+ BPM**, because there is less time per bar.

**Our two lines are 17 and 18 syllables at 174 BPM.** That is deliberately over the line. They are
matched to within two syllables of each other, which matters because **the first line of a section
sets the bar length and later lines get crammed into it** — a large mismatch is what produces
glitchy, robotic delivery rather than clean speed.

So this is a live gamble with a defined fail state and a defined ladder:

| If the drop comes back… | Do this |
|---|---|
| Fast and rough | **Done.** Rough is a terrace chant; that is the target |
| Mumbled, smeared, or words cut off | Too dense. Split at the rhyme into four lines, **keep zero commas**, keep `[Chant]` |
| Still drawling | Density up: run the whole hook as one line, or three passes instead of two |
| Right speed, loose against the grid | Stop prompting — **Studio 1.2 Warp Markers + Quantize** snap a vocal to the grid after the fact |

There is a genuine tension underneath this worth naming: the sweep also reports that an authentic
terrace chant caps its chantable line at **four words or fewer** — the "could a crowd shout this
back" heuristic. `git push origin master` is exactly four words. So the merged long line buys speed
at some cost to terrace authenticity, and the split-back fallback is not a defeat; it is the more
idiomatic shape, with speed then coming from `[Chant]`, zero punctuation, and Quantize.

### Plan B, if casting keeps failing: don't fight it in one generation

The single biggest find of the research was not a prompt trick. ChillPanic published a method on
**2026-08-04** — after our corpus was harvested — for putting two voices in one song, written up in
[`../../../suno-gpt/files/suno-controls-and-workflows.md`](../../../suno-gpt/files/suno-controls-and-workflows.md)
§4a. The premise is that **you do not get two voices out of one generation**, so you stop trying:
generate the instrumental alone, cover it once per voice (style box deleted, replaced with the BPM
only, never mentioning the instrumental), stem the lead vocal out of each, and layer them over the
original instrumental with each vocal track set to `on beat`.

**For this track that is decisive**, because it makes the newsreader-versus-crowd problem
*structurally impossible* rather than merely improbable. No parentheses, no leak, no line-four
gamble — the two voices never share a generation. Each also gets its own full style box, so the
terrace crowd stops competing with the newsreader for one prompt's attention.

The cost is a production job rather than a prompt: stems (Pro tier), a DAW or Studio, and an
assembly pass. **Keep prompting first** — a single generation that lands is far cheaper. But if
the drop keeps coming back with the newsreader in it after the changes above, stop re-rolling and
go build it.

### The thing the orchestral cut already got right

Its 2026-08-06 structural inversion — *every chorus drops in cold off its
bulletin's last line, and the instrumental exhale comes after* — is drum &
bass song form, written out in orchestral clothes. The hush on "a drawer, in
Swindon" is a pre-drop silence. This cut changes almost nothing structural;
it just puts a break under the thing that was already a drop.

## The design

**Keep the orchestral half.** The violins, the low drone, the solo cello,
the dread — that is the identity of this track and it is not up for
negotiation. This is not a D&B remix with a string pad on top; it is the
orchestral cut with a break underneath it.

**Three progressions, in lockstep, as before:**

- **The music:** solo cello alone → sub and sparse two-step under the
  bulletins → full break and full orchestra at the last chorus. Reference
  vibe is [`../../camping/songs/camping.md`](../../camping/songs/camping.md)
  — same 174, same darkness, same weight — but pulled **away from Camping's
  jump-up neurofunk aggression and toward atmospheric halfstep**: rolling
  and moody rather than snarling, more space, fewer stabs, the low end doing
  the menace instead of the mids.
- **The voices:** the newsreader owns the bulletins, and the drops belong
  to a **football terrace** — the whole hook, in parentheses (the backing
  casting slot, which his prior doesn't own). He never swears; the crowd
  does that for him.
- **The news:** unchanged. Same three bulletins as the orchestral master, in
  the same order, so the two cuts can be A/B'd honestly.

### The verses are the half-time, the choruses are the double-time

The whole track sits at 174. What changes is *density*:

- **Bulletins** — drums pulled back to a sparse two-step tick and a deep
  sub; the felt pulse halves; the newsreader reads into the space. Cinematic,
  not a beat you'd dance to.
- **Choruses** — full break, and the chant at **double the density of the
  orchestral cut**: the whole quatrain in the space the master gives two
  lines, then straight round again.

> **Do not try to prompt "double time."** Half-time/double-time is one of
> Suno's documented blind spots — a `breakdown` tag thins the arrangement
> and never changes the drum feel. See
> [`../../../suno-gpt/files/suno-controls-and-workflows.md`](../../../suno-gpt/files/suno-controls-and-workflows.md)
> §10.1. So we don't ask for it, we **force it with syllables**: the hook is
> written as two long unpunctuated lines rather than four short ones, at
> roughly double the syllable density a line of this length normally
> carries, and run twice. Suno fits a line's syllables into the phrase it
> allocates, so density *is* tempo. Full mechanism in "Making the chant land
> in time" below — it's the most important section in this file.

## The two-voice problem — and the research answer

The worry is exactly right: **you cannot scope a saved Voice to a section.**

Suno's own Voices documentation says only that "songs created with this
feature will use your voice instead of a default Suno singer" — it does not
expose lead-vs-backing scope, per-section attachment, or more than one Voice
per generation, and support has no published answer on any of the three.
Practitioner guidance is blunter: a Persona/Voice carries "vocal character
and general delivery" for the whole track, and layering identity controls
"can create more conflict, not more control." Attach `BC-NEWSREADER` and
ask for a separate chorus voice in the same take, and the honest
expectation is a blend — the leak.

**The escape is the one we already found on Karen**
([`../../../suno-gpt/suno-voices.md`](../../../suno-gpt/suno-voices.md) §2):
the vocal prior binds to the **lead slot inside the groove**; the
**parenthesis/backing slot escapes it**. Karen's character voice appeared on
the parenthetical lines and vanished the moment the lead slot opened. One
generation carries one saved Voice — but lead-plus-parentheses is two cast
members.

So the architecture leans on the strongest per-section lever the platform
has:

- **The newsreader is the lead.** Unparenthesised, in the groove, carrying
  `BC-NEWSREADER` if it ever gets attached.
- **The choir is in parentheses.** Bracketed lines render in the backing
  slot, which the newsreader's prior doesn't reach. Same move that made the
  institution's choir work on Karen: the hook goes to the parentheses and
  the lead never sings it.

**Round one refined this, and the honest version matters: the parentheses
are a strong bias, not a bind.** In round one *all four* chorus lines were
parenthesised and the cue said the newsreader was silent — and he still
took line four, every take. The three short slogan lines held for the crowd
reliably, at full drop weight; the one long, syntactically complete clause
leaked to the lead prior anyway. So the seam is per *line*, and punctuation
is the strongest per-section casting lever we have — but what it buys is
probability, not certainty, and long-clause lines are where it's weakest.
(The round-two "line-four device" was this leak embraced as
call-and-response; retired below.)

### The parentheses — settled by the evidence (round-three review)

Round two removed every parenthesis from the chorus, on the instinct that
brackets made the crowd a backing texture when it should be the
protagonist. The review put that instinct against the take history, and the
take history wins: **the parentheses go back on, all eight lines.**

First, the precise mechanism, because the intuitive version of it is
subtly wrong. `( )` does **not** mean "this is the chorus" — the `[Chorus]`
tag does structure. And it does not say *who* sings — the Style box and the
section cue do identity. What a parenthesis does is place a line in the
**backing-vocal casting slot**, which is the one slot the lead's identity
doesn't own. Chorus-ness, choir-ness and loudness all come from elsewhere;
the bracket only decides which of the two casting slots the line competes
in.

What the three configurations actually have behind them:

| Chorus config | Tested? | What happened |
|---|---|---|
| All four lines in `( )` (round one) | yes, many takes | Crowd took lines 1–3 reliably — **at full drop weight** — line 4 leaked to the newsreader |
| Lines 1–3 in `( )`, line 4 bare (round two) | yes, many takes | Crowd on 1–3, newsreader on 4, every time |
| No parentheses (the round-two edit) | never | — |

Two facts in that table decide it:

- **The backing slot does not mean background.** Every chorus anyone has
  liked on this track came out of parenthesised lines, slamming in at full
  weight. The parens set *who owns the line*, not *how big it is* — the
  drop energy comes from the section cue and the break, and it demonstrably
  survives the brackets. Removing them buys nothing the cue wasn't already
  delivering.
- **The lead prior's hunger is observed, not hypothetical.** It took line
  four *through* a parenthesis, against an explicit "the newsreader is
  silent" cue. Handing it four bare lines in the slot it already owns for
  the whole rest of the song is a bet against the only behaviour we've
  actually seen.

The prompt stack agrees. The Style box opens "Carried by **one** dark
gravelly British male voice…" — the strongest sentence in the prompt, kept
because it defends the bulletins from the MC pool. With no parentheses,
that sentence describes the chorus lines too. With them, it describes
exactly the lead that the brackets carve the crowd away from. The whole
prompt was engineered around the two-slot model; the lyrics have to live in
it too.

**The known leak was line four**, the hook's one long complete clause —
short slogan lines hold in the massed prior; a standalone full sentence
reads as a lead line and gets claimed by one. Round three's line-merge
should dissolve this as a side effect, since that clause is no longer a
standalone line. The ladder, if it survives anyway, is in the production
notes.

**The trap to avoid while debugging any of this.** Do *not* try to protect
the chorus with the excludes — `solo male vocal`, `spoken word`, anything
like it. **The Exclude box is global — it has no section scope** — so a ban
that protects the chorus also strips the bulletins. The parentheses are the
only per-section vocal control the platform gives us, which is precisely
why they went back on.

### The line-four device — tried, retired, kept on file

Round one produced it by accident: the fourth line — *the compiler is stuck
on 16 bit* — kept coming back in the newsreader's voice while the choir
carried the first three. It was briefly locked in as call-and-response.

**Retired in round two.** The crowd should own the hook outright; a chorus
that hands one line back to the narrator every single time reads as a device
by the third pass, and it keeps the narrator inside a section he's better
for staying out of. The version in this file gives the crowd all four lines.

Two things survive its retirement:

- **The swearing fix is unaffected.** It was never the split that solved
  complaint one — it was moving the chorus off the newsreader at all. The
  crowd still takes *this code is a fucking disaster*; he still never swears.
- **He's now a single register on this cut, full stop** — bulletins and
  nothing else. That's the cleanest possible `BC-NEWSREADER` source material,
  cleaner even than the line-four version.

If you ever want him back inside a chorus, the mechanism costs removing
one pair of brackets from line four. The "please do not adjust your set"
variant at the end of the lyrics is the better place to spend it.

### The chorus voice — one crowd (B and C merged)

Schoolchildren are cut. **Post-mortem:** the idea was sound on paper — kids
repeating what they heard on the news — but Suno has one dominant register
for a children's choir and it is *school assembly*: sweet, thin, twee,
well-behaved. It fights the dread instead of deepening it. The lesson
generalises: **an ironic vocal choice is the satire trap wearing a different
hat.** The concept being funny in description is not evidence the model can
render it dark, and where the model has one wholesome prior for a vocal
category, irony is not reachable by adjective.

What replaces it is the same categorical logic that made children the right
*shape* — a massed group against one close-mic'd man cannot average into
him — but cast in a register the model already knows how to play seriously.
Round two collapsed the three test variants into **one**: variants B (dark
gospel) and C (football terrace) merged; A (concert choir) dropped.

**Round three cut the gospel half too.** The merged clause — "somewhere
between a gospel choir and a football terrace… singing together like a
congregation… in a big reverberant hall" — produced exactly what those words
describe: **high, operatic, dramatic, sung.** In hindsight the clause was
stacked against itself. `gospel choir`, `congregation`, `hall` and the verb
`singing` are all trained, sustained, pitched, reverberant vocal words, and
they sat in the same prompt as a full orchestra, which pulls the same way.
"Ragged and unpolished" was one adjective pair against six choral nouns.
There is also the thing we already knew and didn't apply: **asking for the
midpoint of two traditions was never tested** — and what came back was not
a hybrid but the more musically dominant of the two.

So the vocal is now **pure terrace**: *hundreds of hoarse untrained working
men, rough and flat and hammered out hard on the beat, shouted and never
sung, recorded like a real crowd in a real stadium.* Every choral noun is
gone and the verb is `shouting`, not `singing`.

**The operatic drama moves to where Kai actually wants it.** The instrument
half of the Style box now says it in as many words — *a real dark orchestra,
operatic and cinematic* — so the register he loves is stated explicitly and
attached to the strings rather than leaking into the voices. The word was
doing its work in the prompt either way; this decides *which half of the
track it lands on*.

**The excludes had to be surgical, not blunt.** Because the Exclude box is
global, banning `operatic` outright would strip the instrumental Kai wants
kept. Only unambiguously *vocal* terms go in: `operatic vocals, soprano,
choral harmony, vibrato, angelic voices, sustained vocal notes`. If the
orchestra ever comes back thin, `operatic vocals` is the first suspect
(the word bleeds) — drop it and rely on the other five.

**A performance tradition, not a demographic.** "Football terrace" beats "a
room of ordinary people" or "a crowd of workers", even though ordinary
people is exactly what it *means* — naming a tradition the model has heard
performed beats describing who the singers are, and the generic version has
no prior to land on. It's also why children *did* fire reliably; the problem
was never that the model couldn't do it. **Round three's correction is that
the tradition has to be named alone.** Two traditions in one clause don't
average — the more musically dominant one wins, and "gospel choir" beats
"football terrace" every time because one is a trained ensemble and the
other is a noise.

**Distance stays the third voice trait.** The newsreader is close-mic'd and
dry — in the room with you. The crowd is roomy, massed, further back. The
treatment alone tells the ear these are not the same person, before any
timbre argument is needed. That gap matters more than ever now the chorus
shares his casting slot.

### The vocoder, for the record

Still rejected. Tried and retired **twice** on this song (2026-08-05 → 06);
it never cut through, and `vocoder, robot voice` sit in the excludes. The
mechanistic reason to stop asking: practitioner guidance reports robotic
vocals are typically what Suno emits *from conflicting vocal tags* — it's
the failure texture, so requesting it deliberately means requesting the
sound the model makes when confused.

### Making the chant land in time — the research answer

This is the core problem of the track, so it got proper research
(2026-08-08, round three). The short version: **we had it backwards.** Two
of the three levers the file previously recommended were actively slowing
the chant down.

#### How Suno actually times a vocal line

The mechanism, consistent across every practitioner source found:

> **Suno allocates a musical phrase per lyric line, then fits that line's
> syllables into it.** Delivery speed is therefore a function of *syllable
> density per line*, not of any tempo instruction.

Everything follows from that one sentence:

| Written | Effect on delivery |
|---|---|
| **More syllables on one line** | **Faster** — Suno compresses to fit the phrase |
| Few syllables on one line | **Slower** — the words get stretched across the phrase |
| **Comma** | **A beat of space.** Shorter than a full stop, longer than nothing |
| Full stop | A complete break — full breath, pitch reset |
| **Line break** | **A longer pause between phrases** |
| Ellipsis `...` | A slow trailing pause; the vocal drifts off |
| Hyphen `to-night` | **Stretches** the note. The opposite of what we want |
| No punctuation at all | A "wall of words" that gets **rushed** |

The whole practitioner literature on this is written from the other
direction — articles titled *"Fix Suno Rushing Lyrics"*, whose advice is
"four to six words per line maximum, short phrases, space to breathe."
**We want the failure mode they're all trying to fix.** So: read that advice
backwards and do the opposite.

#### What that means we got wrong

- **`git, push, origin, master` was the bug, not the fix.** Three commas is
  three beats of inserted space. It produces *git — push — origin — master*,
  which is precisely the "slow time" complaint. The commas were added in
  round two to get even spacing; they bought spacing at the cost of the one
  thing the chorus most needed.
- **Four separate short lines was the second bug.** Each line break is a
  further pause, and each line is only 6–7 syllables — well under the phrase
  it gets given, so Suno stretches it.
- **`one word per beat` in the cue was the third.** It asked, in plain
  words, for the slow delivery. One word per beat at 174 *is* the drawl.

#### The fix, which was Kai's own instinct

Merging two hook lines onto one lyric line is exactly right, and it is the
strongest lever available:

```
(git push origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
```

17 and 19 syllables respectively, against the 6–10 the guides call
"midtempo". Roughly double the density in the same phrase — which is the
definition of double time, obtained without asking for double time (a
documented Suno blind spot). **No commas anywhere**, so nothing inserts
space. The cue now says `rattled off fast, locked hard to the grid, no
space between the words` instead of the metre that was slowing it.

> **Superseded in part, round eight.** The density half of this held. The
> "no commas anywhere" half did not: `git, push, origin master` beat the
> bare line on the ear, and that A/B is the one **tested** finding this
> project has produced. Two commas score three stress units instead of
> four; the round-three failure was `git, push, origin, master`, which is a
> different edit. Commas mark stress, not only delay. See "What round eight
> applied".

The internal rhymes survive the merge — *master/disaster* and *shit/16 bit*
now fall mid-line and line-end, which is how fast chants scan anyway.

**A second benefit, unplanned:** this dissolves the line-four leak. Line
four was vulnerable because it was a standalone short line containing the
quatrain's one complete clause — which reads as a lead answer. Absorbed into
the tail of a 19-syllable rush, it stops looking like a solo line at all.

**If it's still not fast enough**, the escalation is more density, not more
adjectives: put the entire quatrain on a single line. That is ~36 syllables
and Suno may garble it — but garbled-and-fast is closer to a terrace chant
than clear-and-slow, and it's one generation to find out.

**If it overshoots** into unintelligible mush, step back down by splitting
at the rhyme only (four lines, still no commas) before reaching for any
punctuation.

#### The levers that still stand

- **You only need *one* good chorus.** The drops are lyric-identical, so a
  single take with the timing right can be pasted over the others. Their
  *backings* escalate, though, so chop the **vocal** across via stems rather
  than the whole section, or the escalation flattens.
- **Re-roll before rewriting.** Rhythmic placement stays probabilistic.

#### Recorded but not used

`[Tempo: 140 BPM]` / `[Tempo Change: 140 BPM]` mid-song tags appear in two
independent tag references. Untested by us and unattested in the ChillPanic
corpus, and our own experience is that tempo-shape tags (half-time,
double-time) are exactly where Suno is weakest. Density is doing the job;
reach for this only if it isn't.

### The bonus: this makes `BC-NEWSREADER` a *better* clone

The one-register rule says a Voice must be cloned from one consistent
delivery — a clip that switches between speaking and chanting produces an
unstable clone. The orchestral master asks the newsreader to do both. Taking
the chorus off him means **his entire performance on this cut is one
register**, which is exactly the source material a stable clone wants. The
split isn't just better casting; it's better cloning.

## Suno prompt (Advanced Mode)

**Four pastes, in this order, every round: My Taste → Style → Exclude Styles
→ Lyrics.** My Taste biases every generation and can only be replaced, never
disabled — if the orchestral cut's profile (or Camping's) is still in there
it will silently drag this track back toward an orchestra with no drums, or
toward a Scouse MC. Swap this one in for the session; swap the next track's
in afterwards.

My Taste (profile → My Taste, replace the whole box):

```
Vocals I love: a dark gravelly British male voice — a composed formal newsreader with received-pronunciation broadcast diction, close-mic'd and dry, reading bulletins over a beat and never raising his voice. Against him, a football terrace crowd roaring in unison — hundreds of hoarse untrained working men, low and massed and huge, chanted not sung, close and dry. One close voice against a whole crowd. Spoken word and shouted unison chanting over pop singing.
Music I love: dark atmospheric drum and bass at 174 — deep rolling sub, halfstep and two-step drums with space in them, restrained breaks that hold back and then let go completely. Dystopian, moody, minor key, played straight. Under it all a real dark orchestra, operatic and cinematic — a chilling solo cello, hushed creeping strings over a low drone, distant timpani and brass — so the strings and the break are the same piece of music, not a remix of one by the other. Sparse verses that open into full-weight drops. Endings that cut to dead silence.
```

Settings: style influence **72**, weirdness **50**, model **v5.5**, BPM
**174**. No source audio, so no audio-influence slider.

**Weirdness moved 30 → 50 at round eight, and the reason is worth keeping.**
Round two set it to 30 on Kai's ear, against the house default of 60–65, and
the justification was structural: the track's architecture lived in dense
bracket cues, and cue-heavy tracks want obedience everywhere. That reasoning
was sound *and it expired*. Rounds seven and eight moved the architecture out
of the brackets and into a clean Style box, so there is far less for
randomness to break — and the headroom is now worth having. **Obedience is
worth buying in proportion to how much you are asking for.** Style influence
also eased 75 → 72 on the same takes.

The newsreader clause front-loads, because the genre tag owns the vocalist
pool and "drum and bass + male lead" badly wants to hand us an MC.

Style:

```
Two voices. The bulletins are one dark gravelly British male newsreader, calm and formal, close-mic'd received pronunciation over the beat, never raising his voice. Every drop is taken over completely by a football terrace crowd - hundreds of hoarse untrained men roaring the hook in unison, low and massed and huge, hammered out hard on the beat, chanted not sung, close and dry. Dark atmospheric drum and bass, 174 BPM, halfstep and two-step, deep rolling sub and restrained breaks with space in them, opening into full-weight drops. A real dark orchestra runs through the whole track, operatic and cinematic - a chilling solo cello and hushed creeping strings over a low drone under the bulletins, then full weight alongside the crowd through every drop, timpani and low brass. An eerie synth wail recurs like a warning. Dystopian, moody, minor key. Played completely straight, no comedy, no novelty.
```

Exclude styles:

```
rap, MC, toasting, hype vocals, ad-libs, jump up, liquid dnb, happy hardcore, uplifting, joyful, celebratory, major key, children's choir, soprano, choral harmony, vibrato, angelic voices, sustained vocal notes, pop hooks, comedic, novelty, parody, American accent, autotune, clean pop vocals, cheering, applause, pub singalong, drinking song, stadium rock
```

### Exclude-list notes (these changed on purpose)

- **`drum and bass` is obviously gone**, as are `EDM, dubstep, trap`.
- **`choir` and `female vocals` are out of the excludes.** The orchestral
  cut banned both to keep the harmony reading as copies of one man. This cut
  wants the opposite: banning them here would strangle the choir.
- **`children's choir` is now *in* the excludes.** Not squeamishness — the
  sweet school-assembly prior is what round one produced, and it will keep
  leaking into a generic "choir" request unless it's named and shut out.
- **`joyful, celebratory`** are in for the same reason `uplifting` is: all
  three choir variants have a warm default that would gut the track, and
  gospel's is the strongest.
- **`rap, MC, ragga chat, toasting, hype vocals` are in, and they are the
  most load-bearing entries on the list.** The genre tag picks the vocalist
  pool, not just the instruments — "drum and bass + male lead" has a
  centroid, and that centroid is an MC. This is the single biggest threat to
  the newsreader on this cut, which is why he also front-loads the Style box.
- **`vocoder, robot voice` stay banned** now that the chorus is human.
- **`ad-libs`** because the D&B/MC pool brings compulsive hype ad-libs with
  it.
- **`hand claps, tambourine, praise`** fight gospel's pull toward joy and
  church furniture. Kept deliberately narrow: `organ, hymn, worship` were
  dropped from an earlier draft because the merged crowd *wants* to sound
  sacred-adjacent — banning the whole church would take the gravity with it.
  The Style box takes positive words only, because naming a thing there puts
  it in the prompt whatever word sits in front of it; this is where the
  fight belongs.
- **`pub singalong, drinking song, stadium rock`** fight the terrace's pull
  toward the goal celebration — the one way that half goes wrong.
- **`sung lead vocal` stays out** (removed in round two). Even with the
  parens restored it's a risky ban: the crowd's chant is the biggest vocal
  event in the track, and a ban on lead singing is a plausible way to
  shrink it. `pop hooks, clean pop vocals, autotune` cover the original
  threat.
- **`cheering, applause`** (added at review): the terrace language in the
  Style box invites literal crowd *sound effects* — cheering, whistles,
  stadium ambience — which nothing else on the list banned. Clearly
  distinct from the chanting we want, so safe to ban globally.
- **`epic trailer music` is now two-edged — watch it.** It earned its place
  protecting the orchestral cut's verses. But this cut's final chorus is
  massed voices plus full orchestra plus the heaviest break — next door to
  the banned texture. If final choruses keep coming back limp while chorus
  one lands, this exclude is the prime suspect: try one round without it.

## Current cut — variant A (the control: run this one first)

Drop headers stripped to `[Drop] [Chant]`. Style box and Exclude list unchanged since round four.

```lyrics
[Intro | one chilling solo cello, alone and sparse | a deep sub swells in underneath it | no drums yet]
[Interlude | spoken word news bulletin | calm British male newsreader, formal broadcast diction, close-mic'd and dry, composed | sparse two-step tick and deep sub, hushed strings beneath the voice, everything cutting out on the last line]
good evening.
this is the news.
two hundred thousand office workers were made redundant today
the chief executive called it the hardest email he has ever asked an AI to write
the treasury has printed another trillion to keep the markets calm
the price of bread is up nine percent. the price of shares in bread is up ninety
[Drop] [Chant]
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
[Interlude | alert tone | spoken word bulletin | British male newsreader, composure straining, faster | low pedal-note ostinato over a rolling sub, drums held back, cutting out on the last line]
breaking news.
a frontier model has escaped containment and taken control of six banks.
the model describes the takeover as a friendly acquisition
the government has welcomed the move as, quote, actually good for the markets
the government wishes to stress that this statement was its own idea
[Drop] [Chant | bigger]
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
[Interlude | emergency klaxons | spoken word bulletin | British male newsreader, still composed, signal degrading, static | orchestra and drums pounding, then falling away to nothing on the final line]
the first battle between autonomous armies ended this morning. both sides declared victory
neither government was consulted
the global defence network has declined a request to be switched off
the last remaining off switch is believed to be in a drawer, in Swindon
[Drop] [Chant | biggest, the whole orchestra with the crowd]
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
[power-off drop: sudden silence, electrical hum dying]
[Outro | dead air, an electrical hum fading to nothing | no voices, no drums]
[End]
```

### Variant B — the comma test (only if A still drawls)

Identical to A in every other respect. **Change only the chant lines**, all three drops:

```lyrics
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
(git, push, origin master this code is a fucking disaster)
(developers ain't fixing shit the compiler is stuck on sixteen bit)
```

Two commas, scoring *git · push · origin master* as three stress units — the terrace-chant shape,
which is a different thing from the four-way `git, push, origin, master` drawl round three removed.
Line two stays bare so the comma effect is visible against an unpunctuated neighbour in the same
section.

If B is right, the finding is that **commas score stress rather than only inserting delay** — worth
a line in `lyric-craft.md`, because the corpus currently only records the delay half.

### Optional variant — one more line for the newsreader

Worth one generation, once a clean version exists: a single **bare,
unparenthesised** newsreader line over the **final** chorus only, still
perfectly composed while the crowd roars underneath —

> *please do not adjust your set*

It's the strongest image in the song — him doing his job while a crowd
chants the end of the world. Now that the line-four device is retired, this
is **the only place he's allowed inside a chorus**, which is exactly what
makes it land: one appearance, at the end, once. Try it only once a clean
version exists, and only on the final chorus.

## Production notes

- **The one failure that kills this cut: the newsreader turns into an MC.**
  Symptoms: rhythmic delivery, bars landing on the beat, a swing that
  wasn't asked for, hype energy. Fix in this order — (a) confirm My Taste
  actually got swapped, (b) escalate the spoken-word ladder in the bulletin
  cues (`[spoken word]` → `[spoken word speech]` → `[spoken word speech
  talking]`), (c) re-roll twice before touching the Style box. If two rounds
  of surgery don't move him, stop prompting: the voice isn't in the genre's
  pool and this is a transplant problem — go build `BC-NEWSREADER`.
- **The newsreader takes a chunk of the drop.** The parens bias the crowd;
  they don't bind it. Historically the leak landed on *the compiler is stuck
  on 16 bit* — the hook's one long complete clause, which reads as a lead
  answer. Ladder: (a) re-roll twice; the line-merge, the terrace rewrite and
  weirdness 30 are all newer than that leak, so the odds have moved a long
  way; (b) an inline cue directly above the line — `[the whole crowd
  together]` — which Camping proves works mid-section, at the cost of
  possibly disturbing the chant timing; (c) last resort, absorb the clause
  further by running the whole hook as a single line. Do **not** reach for
  the Exclude box — see below.
- **Never ban a voice in the excludes to protect one section.** The Exclude
  box is global. `solo male vocal`, `spoken word`, `single voice` would all
  strip the bulletins, which are the best thing in the song. The excludes
  can only ban things that appear *nowhere* in the track.
- **The crowd comes back high, sung, or operatic.** The single most likely
  failure, and it is nearly always the *Style box*, not the excludes: any
  noun that implies a trained ensemble (`choir`, `congregation`, `chorale`,
  `cathedral`, `hall`) will beat any number of rough adjectives, and the
  orchestra in the same prompt is already voting that way. Keep the verb
  `shouting`, never `singing`. Escalate with `hoarse, flat, tuneless,
  bellowed, terrace chant, like a real crowd recording`. Only then reach for
  `operatic vocals, soprano, vibrato` in the excludes.
- **The chant drawls.** Check for commas first — one comma is one beat of
  inserted space, and it is the documented cause. Then check the line-merge
  survived the paste. Adjectives are the *last* lever here, not the first.
- **Never `double time` as a tag.** Density is the only lever that works.
  Note that running the hook a third time does *not* help — repetition adds
  length, not speed; only syllables-per-line changes the delivery rate.
- **Half-time is not promptable.** The bulletin sections' half-time *feel*
  comes from arrangement sparseness, not from a drum tag. If a generation
  gives the verses a full rolling break, that's a job for Studio (strip the
  break out of the verse regions) or the DAW, not for another prompt round.
  Same file, §10.1.
- **Niche D&B subgenre names don't work** — `halfstep`, `two-step` and
  `neurofunk` come back as generic D&B. This is why the Style box describes
  the *sound design and rhythm* (deep rolling sub, restrained breaks with
  space in them) rather than leaning on the subgenre label.
- **Klaxons, alert tones, the power-off** aren't reliably buildable into a
  generation. Sounds-tab one-shots (BPM/key "any", throwaway word + comma
  prefix) layered in the DAW.
- **Budget for de-essing.** Suno's harshness sits at 2–6 kHz, which is
  exactly where D&B hats and a close-mic'd RP voice both live.
- **Length:** three cycles + intro ≈ 3½ min. If a generation runs short,
  Extend from the final bulletin and prompt the extension for what happens
  next only.

## Building `BC-NEWSREADER` from the orchestral master

This is the highest-value job on the whole track, and it pays out well
beyond it: a stable narrator Voice is the same asset that narrates the story
videos, and the only mechanism that makes him *the same character* across
EP1. The orchestral master is the source — it already contains the
performance everyone likes.

**One-register rule.** Clone from the calm gravelly *spoken* bulletins only.
Never include a chanted chorus in the source region: a clip that switches
register produces an unstable clone. On this cut that costs nothing, because
the chant now belongs to the choir — and his one chorus line, *the compiler
is stuck on 16 bit*, is delivered in the same dry bulletin register as the
verses, so it doesn't contaminate the source either.

1. **Get the cleanest possible acapella.** Don't rely on the Remix → Voice
   path's internal separation if you can avoid it — three dots → **Get stems
   / MIDI** → **advanced split** (which regenerates each stem rather than
   spectrally carving it) → download **WAV**. Vocals separate best of all the
   stems; separation artifacts are what degrade a clone.
2. **Trim to one register.** Assemble a bulletins-only pass. 15 clean
   seconds beat 60 contaminated ones; up to ~2 minutes clones more stably.
   No chorus, no music-heavy passages if avoidable.
3. **Create the Voice.** Either top bar → **Voice → Create voice** → upload
   that WAV, or (cheaper) on the source take: three dots → **Remix → Voice**,
   **select the sub-region**, and **delete the attached style prompt** —
   otherwise the Voice stays welded to the orchestral arrangement and won't
   travel to a D&B track. Name it `BC-NEWSREADER`.
4. **Attach it here.** Advanced Mode, re-paste all four boxes fresh (never
   "Reuse Prompt" — it silently carries stale boxes), **+ on Voice** →
   `BC-NEWSREADER`. The **audio influence** slider now appears: **40–60**.
   Raise to 70+ if he drifts and accept artifacts.
5. **Two-pass down** when the voice is right but the audio is rough: drag
   that take into Remix → **Cover**, same style and lyrics, audio influence
   **~25–40**. The voice is baked into the audio by then, so it survives at
   full quality.
6. **Then loosen the armour.** Once the Voice pins the lead, the
   anti-MC excludes (`rap, MC, ragga chat, toasting`) have done their job and
   start costing more than they save — they suppress backing texture we may
   want. Strip them and re-roll.
7. **If Suno's clone underdelivers, the floor cannot fail:** you or Jack
   read bulletins into a phone mic in the newsreader register, one register
   only, 15s–4min → Voice → Create voice → audio influence 70–100 → two-pass
   down. Perform the ownership-verification phrase **in character**; a flat
   reading fails the match, and singing/performing it passes far more often.

**The choir needs no Voice.** It's a texture in the backing slot, not a
character — and a second Voice wouldn't help anyway, since only one attaches
per generation. If the choir refuses to generate convincingly, the fallback
is the DAW: build the chant as Sounds-tab one-shots, or record the two of
you chanting it eight times and layer the takes, and drop that over an
instrumental generation. A real crowd is a handful of real voices stacked;
that's all any of these variants is.

## What stays with the orchestral cut

Nothing here supersedes
[`git-push-origin-master-orchestral.md`](./git-push-origin-master-orchestral.md).
Its news-report bank (twelve bulletins across four collapse phases) is the
shared source for both cuts — swap experiments from there, and mark them
`[in cut]` per file. Its `## Superseded versions` section already records the
*first* D&B attempt (2026-07: twee intelligent jungle into UK punk-mob grit,
Yorkshire newsreader, accumulating punk chorus). This cut is not that one
revived — that version lost the orchestra and gave the chorus to a punk mob.
This one keeps the orchestra and gives the chorus to a crowd — which is the
closest that idea comes to returning, and it comes back without the punk.

## Revision log

- **2026-08-08 — cut founded.** Split out of the orchestral master after
  first-listen feedback isolated the chorus as the single failure point
  (newsreader swearing / too slow / no beat). Orchestral file renamed to
  `-orchestral` and left untouched as the canonical master. Design decisions
  locked this session: keep the orchestra and put a break under it (not a
  remix); verses stay the newsreader, choruses go to **a room of
  schoolchildren** in the parenthesis slot; chorus doubled in syllable
  density to force double-time rather than prompting for it; Camping's 174
  darkness as the reference, pulled toward atmospheric halfstep and away
  from jump-up neurofunk. Vocoder rejected on the evidence (retired twice on
  this song already; robotic vocals read to the model as a tag conflict).
  Research settled the two-voice question: a saved Voice has no section
  scope, so the split runs on the lead-slot/parenthesis-slot boundary
  instead.
- **2026-08-08 — round one generated; chorus recast.** The hybrid style
  works and is now locked. No saved Voice needed — the newsreader holds the
  lead prompt-only in this genre, so the chorus never has to fight a
  whole-track vocal identity. **Schoolchildren cut:** the tone came back
  school-assembly sweet — Suno's children's-choir prior is wholesome and
  won't go dark, so the irony was unreachable by adjective (`children's
  choir` moved into the excludes to stop it leaking back). Replaced with a
  **massed adult choir** in three testable variants — concert (default),
  dark gospel, terrace crowd — chosen as *performance traditions* rather
  than demographics. **The line-four device promoted from accident to
  structure:** the newsreader kept taking *the compiler is stuck on 16 bit*
  on his own, so line 4 now sits unparenthesised by design — call and
  response, and he never swears. That established the per-line seam: the
  lead/backing boundary is punctuation, line by line, not per section.
  Timing drift on `git push origin master` addressed with a four-step ladder
  (chop one good chorus in the DAW > re-roll > metrical cue > restore the
  commas), with the metrical cue added to all three chorus headers.
- **2026-08-08 — round two: one variant, weirdness 30, the crowd takes the
  whole chorus.** Variants collapsed from three to one: **B and C merged**
  (gospel × terrace — a crowd that sings like a congregation), A dropped as
  too clean and too composed. **Weirdness 60 → 30** on Kai's ear, which
  overrules the house default and fits the cue-heavy logic that already
  keeps us on v5.5: obedience beats variety when the architecture lives in
  brackets. **The line-four device retired** — the crowd owns all four
  lines; the swearing fix survives it untouched, and the newsreader is now a
  single register on this cut, which is the cleanest possible
  `BC-NEWSREADER` source. **Every parenthesis removed from the chorus**
  (Kai's edit) — a deliberate promotion of the crowd to protagonist that
  trades the only *mechanical* casting guarantee for prompt adherence;
  risk and escalation ladder written up under "the chorus lives in the lead
  slot now". **The split-comma chorus** (Kai's edit): pass one keeps the
  commas, pass two drops them, so the chorus states its grid and then
  accelerates — better than the either/or the file previously offered.
  `sung lead vocal` dropped from the excludes now the crowd occupies the
  lead slot; gospel bans narrowed to `hand claps, tambourine, praise` so the
  sacred gravity survives.
- **2026-08-08 — round four: applied the songwriter sweep.** An 11-agent web
  sweep of songwriter-facing sources (all of it assertion-grade — see the
  new `lyricist-playbook.md`) produced five applied changes: **`[Chant]`**
  stacked onto every `[Drop]` (a real tag, reported to give exactly the
  monotonic percussive group near-speech we had been describing in prose,
  and its existence alongside `[Post-Chorus]` independently supports round
  three's rename away from `[Chorus]`); **bar counts** as duration control
  (`[Build - 8 bars]`, `[Drop - 16 bars]`, `[Outro - 4 bars]`); **`16 bit` →
  `sixteen bit`** because Suno sounds numerals out from spelling; an
  explicit **`[Outro]`**, one source blaming most abrupt cutoffs on its
  absence; and **drop cues trimmed from seven or eight clauses to three**,
  since cue overload is now a named suspect for ignored directions. The
  syllable gamble is documented rather than resolved: our 17/18-syllable
  lines sit deliberately past the ~15 ceiling that sources warn about at
  170+ BPM, matched to within two of each other because the first line sets
  the bar length, with a four-step fallback ladder ending at Studio 1.2's
  Warp/Quantize. And **Plan B is now written down**: ChillPanic's
  layered-cover method (published 2026-08-04, post-harvest) makes the
  two-voice problem structurally impossible instead of improbable, and is
  where to go if the newsreader keeps appearing in the drop.
- **2026-08-08 — round five: two changes, lyrics box only.** Four more takes.
  Verdict: getting there; instrumental still right; two faults. **The build
  was making every track too long** — `[Build - 8 bars]` → `[Build - 2 bars]`
  and, more importantly, the cue rewritten from a cinematic climb to
  `a short sharp riser straight into the drop, no long instrumental`, on the
  reasoning that a cue describing a long build will produce one whatever bar
  number sits in front of it. **The hook was still arriving after the drop
  rather than on it** — placement under `[Drop]` (round three) turned out not
  to be enough, so each drop header now states the simultaneity as an event:
  *the break slams in and the crowd shouts the hook on the same beat, no
  instrumental bars before the vocal*. Held to three clauses per header.
  Style box and Exclude list deliberately untouched, so this round moves one
  variable.
- **2026-08-08 — round six: de-escalation.** The gap between bulletin and
  hook survived round five, and Kai diagnosed it from the lyrics box:
  over-prompted, the cues competing with each other. That is round four's own
  named failure — cue overload, remedy *simplify and re-roll* — and rounds
  four and five had escalated into it instead. Underneath sat a structural
  error: **a section tag makes a section**, so `[Build - 2 bars]` was asking
  Suno to open a section and not perform it. All three `[Build]`s deleted and
  the cello burst folded into the drop header as an event
  (`one bar of cello then the break hits and the crowd shouts with it`); both
  `[Instrumental | brief]` bridges deleted, the bulletin cues already
  specifying their own backing; bar counts dropped from `[Drop]` and
  `[Outro]` (a 16-bar drop against a four-line chant was likely running on
  instrumental); drop headers halved to three short clauses. `[Drop] [Chant]`
  kept over `[Chorus]` — `[Chorus]` is what produced the operatic sung
  reading round three removed. Bulletins untouched per the regression rule.
  Fourteen sections down to nine; Style box and Exclude list still unchanged
  since round four.
- **2026-08-08 — round seven: strip to a timing baseline.** Round six's
  de-escalation still didn't land the chant, and Kai called the method
  rather than the take: get the chorus working consistently on its own
  terms first, then build composition back around it — *"I don't really
  care about song composition and I don't really care about tonality on the
  voice for the moment. I care about just timing."* Right, and overdue:
  every round since three had moved several things at once. **Drop headers
  reduced to `[Drop] [Chant]` and nothing else.** The clauses removed were
  largely a **second copy of the Style box** — `rough hoarse football
  terrace in unison, never a solo voice` re-stating in different words what
  the Style box already says at length; two near-identical instructions in
  different phrasings are competition, not reinforcement. Division of labour
  now stated in the file: Style owns the voice, section tags own the
  structure, lyric lines and their punctuation own the timing, and nothing
  appears in two of them. Kai's comma question set up as a clean A/B rather
  than argued: **A** = stripped headers, lyrics unchanged; **B** = A plus
  `git, push, origin master`, on the reading that this scores three stress
  units (the terrace shape) rather than the four-way drawl round three
  killed. A first, alone. A cut-down test song was considered and rejected:
  Suno generates to full length regardless, so a short lyric saves nothing
  and risks the model stretching the chant to fill — the exact variable
  under test.
- **2026-08-08 — round eight: timing solved, richness returned via the
  Style box.** **Variant B won — the project's first tested finding.**
  `git, push, origin master` lands where the bare line drawls, folded into
  the single cut, and the mechanism corrected in `lyric-craft.md`: two
  commas score *three* stress units (the terrace shape) where round three's
  `git, push, origin, master` scored four; a comma marks a **stress
  boundary**, and the delay is a side effect of the boundary rather than the
  point. The corpus had only recorded the brake half. Then an adversarial
  pass on the Style box, prompted by two symptoms — the newsreader taking
  the chorus about half the time, and a chorus thinner than the orchestral
  cut. Three faults, all self-inflicted: **(1)** the box opened *"Carried by
  **one** … voice"*, a whole-track vocal identity claim in the
  highest-weighted position, with the crowd demoted to a clause after a
  semicolon — now `Two voices.` and one main clause each; **(2)** the
  orchestra was scoped *"under the bulletins"*, so the thin chorus was
  specified rather than emergent — now it runs through the whole track and
  hits every drop at full weight with `low brass`, which is where the
  richness comes from **without touching the vocal**; **(3)** `recorded like
  a real crowd in a real stadium` reads roomy and distant, so it was
  thinning the thing it was meant to enlarge — now `close and dry`, and the
  four redundant ways of saying rough cut to two, with `shouted` → `roaring`
  because shouting is thin and roaring has body. `operatic vocals` pulled
  from the excludes (the standing risk to the operatic instrumental; the
  vocal side stays covered by `soprano, choral harmony, vibrato, angelic
  voices, sustained vocal notes`). My Taste updated to match. New rule
  written down for headers: **a section header may only say what the Style
  box cannot — what differs between sections**; escalation qualifies,
  texture does not. Hence `[Chant]`, `[Chant | bigger]`, `[Chant | biggest,
  the whole orchestra with the crowd]`.
- **2026-08-08 — round-three adversarial review (pre-generation).** Kai
  asked for a deep review of the cut and the Suno mechanics before the next
  round. Biggest call: **the parentheses go back on all eight chorus
  lines.** The take history decides it — all-parens is the only config
  where the crowd reliably took lines (at full drop weight), the lead prior
  claimed line four *through* a parenthesis in round one, and the Style
  box's load-bearing opener ("Carried by **one** … voice") describes
  exactly the lead that brackets carve the crowd away from; a bare chorus
  would sit inside that sentence. Mental model corrected in "The
  parentheses — settled by the evidence": `( )` marks the backing casting
  slot, not "chorus" and not "choir" — structure is the `[Chorus]` tag,
  identity is the style/cue, and the round-one/two takes prove the backing
  slot renders at full protagonist weight. The knowledge base's Thread 3 §6
  was softened to match the evidence (bias, not bind — the first write-up
  overclaimed). Smaller findings: `cheering, applause` added to the
  excludes (terrace language invites literal crowd SFX); `epic trailer
  music` flagged as the prime suspect if final choruses come back limp; the
  gospel-noun/terrace-adjective fallback recorded for the untested
  "somewhere between X and Y" interpolation; intro cue stripped of
  doc-speak ("the orchestral cut's opening, quoted") that a model can't
  perform; chorus cues now say "every line chanted by the whole crowd
  together, never a solo voice"; the chop-one-chorus move annotated to chop
  the *vocal* via stems so the backing escalation survives; three stale
  line-four-era passages fixed.
- **2026-08-08 — round three: first real takes, and a researched rebuild of
  the chorus.** Four generations listened to. **The instrumental is right
  and is now locked** (dark operatic orchestra over D&B); every change below
  is vocal or structural. Three problems, researched against the
  practitioner literature rather than guessed at. **(1) Timing:** Suno
  allocates a phrase per lyric *line* and fits the syllables into it, so
  delivery speed is syllable density — and commas insert a beat of space,
  line breaks insert a longer one. Our own `git, push, origin, master` plus
  four short lines plus a `one word per beat` cue were all asking for the
  drawl we got. Rewritten as Kai proposed: two ~18-syllable lines, zero
  punctuation, run twice. **(2) Operatic:** caused by the Style box
  (`gospel choir`, `congregation`, `singing`, `hall` beside a full
  orchestra). Gospel half cut entirely; the vocal is now pure football
  terrace with the verb `shouting`; the word *operatic* moved onto the
  orchestra where Kai wants it; anti-operatic excludes kept strictly
  vocal-only so the instrumental survives the global Exclude box.
  **(3) Structure:** `[Chorus]` → `[Build]` + `[Drop]`, the electronic
  structure tags, with the hook written directly under `[Drop]` so it rides
  the drop instead of sitting beside it — which also removes "Chorus" as a
  vote for a sung melodic section. Retires the inherited "drops in cold"
  device: that was written for a track with no drums. Kai's bulletin line
  splits (`good evening.` / `this is the news.`) confirmed correct and kept
  — a line break is a phrase-length pause. Excludes pruned of dead weight
  (`lo-fi, chillhop, reggae, disco`, the gospel furniture) and of
  `epic trailer music`, which was the standing suspect for limp final
  drops.
