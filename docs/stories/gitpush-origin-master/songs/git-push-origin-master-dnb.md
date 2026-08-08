---
title: git push origin master (drum & bass)
status: drafting
model: v5.5 (cue-heavy track — 5.5 obeys the bracket architecture; 4.5 shreds it)
settings: style influence 75, weirdness 30
bpm: 174
voices: [newsreader (male, dark gravelly RP — the bulletins, and nothing else), the crowd (massed adult voices between a gospel choir and a football terrace — the whole of every chorus)]
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
   | 2 | Does the chorus **drop** — full break, cold, no build? | Re-roll; check `[Chorus | THE DROP …]` cue survived |
   | 3 | Is the chorus **fast** — the quatrain twice through, not drawled? | Run the quatrain three times instead of twice |
   | 4 | Is the **whole chorus** a massed crowd, with the newsreader nowhere in it? | Re-roll first; then the line-four ladder in the production notes |

   Question 4's known weak point is line four — the quatrain's one long
   complete clause, and the line that historically leaked to the newsreader
   even *through* a parenthesis. Also confirm the `( )` survived the paste;
   they're the casting mechanism and the easiest thing to lose.

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
- **The voices:** the newsreader owns the verses, and the choruses belong
  to a **massed crowd** — the whole quatrain, every line, in parentheses
  (the backing casting slot, which his prior doesn't own). He never swears;
  the crowd does that for him.
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
> §10.1. So we don't ask for it, we **force it with syllables**: the chorus
> block below carries the quatrain twice inside one section, and the commas
> come out of `git, push, origin, master`. Twice the words in the same bar
> count can only be delivered fast. Short, repeated chorus lines also read
> to the model as a signal for a bigger, harder section — the density buys
> the drop as well as the speed.

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

**The known leak is line four**, the quatrain's one long complete clause —
short slogan lines hold in the massed prior; a full sentence reads as a
lead line and gets claimed by one. The ladder for it lives in the
production notes.

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

**The merge is not a compromise — it's a real thing.** A crowd that sings
like a congregation is the sound of a terrace doing a hymn, a wake, a picket
line: hundreds of untrained adult voices, ragged and unpolished, singing
something sacred and furious in a big reverberant space. Gospel supplies the
minor-key gravity; the terrace supplies the mass, the roughness and the
Britishness. Neither alone was right — A was too clean and too *composed*
(the same ensemble as the orchestra, which made the chorus feel scored
rather than erupted), B risked church warmth, C risked the pub.

What it buys the song: the chorus is now **ordinary people, en masse**,
which is the only voice on the record that could plausibly answer the news.
It also quietly delivers what the retired 2026-07 punk-mob version was
reaching for, without the punk.

**Both risks still need watching.** Gospel's default is joy and church
furniture; the terrace's is the goal celebration. The Style box specifies
minor and mournful and grave; the excludes carry the rest of the fight (see
the exclude notes). If a take sounds like a good day out, that's the fail
state either way.

**And one untested seam in the phrasing itself:** "somewhere between a
gospel choir and a football terrace" asks the model to find a *midpoint*
between two priors. We know naming one tradition works; asking for the
average of two is something no round has tested. The tell that it's
failing: takes where one tradition simply wins, or where the crowd is
neither — generic "epic choir" mush. The fallback is to stop interpolating
and pick a base: **lead with the gospel prior as the noun and graft the
terrace on as adjectives** — `a gospel choir of hundreds of untrained,
ragged voices, massed like a football terrace, minor key and mournful` —
gospel first because B was the variant that sounded best in round two. One
tradition as the thing, the other as its texture.

**They are performance traditions, not demographics.** That's why this beats
"a room of ordinary people" or "a crowd of workers" as a prompt, even though
ordinary people is exactly what it *means* — naming a tradition the model
has heard performed beats describing who the singers are, and the generic
version has no prior to land on. It's also why children *did* fire reliably;
the problem was never that the model couldn't do it.

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

### Making the chant land in time

Round-one takes drifted: sometimes `git push origin master` comes out evenly
spaced, sometimes the phrasing goes sideways. Four levers, cheapest first.

**1. You only need *one* good chorus.** The chorus is byte-identical all
three times, so a single take with the timing right can be chopped and
pasted over the other two in the DAW. This dissolves the consistency problem
entirely rather than solving it, and it is by far the highest-value move
here — spend your generations getting *one* chorus right, not three. One
nuance: the three choruses are lyric-identical but their *backings*
escalate (lone break → strings enter → full orchestra), so chop the
**vocal** across — via stems — rather than the whole section, or the
escalation flattens.

**2. Re-roll before rewriting.** Rhythmic placement is probabilistic, like
every cue. A chorus that drifted on take 2 and locked on take 3 was unlucky,
not mis-prompted.

**3. Metrical direction in the cue.** The chorus cues now carry `strict
time, one word per beat, locked to the grid` — an explicit metre instead of
leaving Suno to guess whether four words are four beats or a scattered
triplet. Escalate with synonyms if ignored (`metronomic, dead on the beat,
drilled`).

**4. The split-comma chorus — now in the cut.** The earlier plan was
all-or-nothing: commas force even subdivision, but commas are also what made
the orchestral cut *slow*. Round two splits the difference instead of
choosing, and it's the better idea: **the first pass carries the commas, the
second drops them.**

```
git, push, origin, master        ← pass 1: states the grid
...
git push origin master           ← pass 2: rides it
```

The first pass teaches the metre — four words, four beats, evenly spaced,
deliberate. The second repeats the identical words with nothing holding them
apart, so they run. Formally that's augmentation into diminution, and it
turns a chorus that merely repeats into one that **accelerates**.

The maths still works: four words on four beats is one bar, four lines is
four bars, twice through is eight — about eleven seconds at 174. A
completely normal D&B chorus.

*Watch for:* Suno may not hear the two passes as related, in which case pass
two reads as sloppy rather than urgent. The tell is whether the second pass
lands *on* the grid the first one set, or merely near it. If it's near it,
that's a re-roll, not a rewrite.

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
Vocals I love: a dark gravelly British male voice — a composed formal newsreader with received-pronunciation broadcast diction, close-mic'd and dry, reading bulletins over a beat and never raising his voice. Against him, a massed crowd of adult voices chanting in unison — hundreds of them, somewhere between a gospel choir and a football terrace, ragged and unpolished yet singing together like a congregation, recorded roomy and far back. One close voice against a crowd. Spoken word and unison chanting over pop singing.
Music I love: dark atmospheric drum and bass at 174 — deep rolling sub, halfstep and two-step drums with space in them, restrained breaks that hold back and then let go completely. Dystopian, moody, minor key, played straight. Under it all a real dark orchestra — a chilling solo cello, hushed creeping strings over a low drone, distant timpani and brass — so the strings and the break are the same piece of music, not a remix of one by the other. Sparse verses that open into full-weight drops. Endings that cut to dead silence.
```

Settings: style influence **75**, weirdness **30**, model **v5.5**, BPM
**174**. No source audio, so no audio-influence slider.

**Weirdness 30 is deliberate and overrules the house default of 60–65.** It
tested better across the board. The reason is structural: this track's
architecture lives in dense bracket cues, and cue-heavy tracks want
obedience everywhere — it's the same logic that keeps us on v5.5 rather than
4.5. Randomness has nothing to add here and plenty to break.

The newsreader clause front-loads, because the genre tag owns the vocalist
pool and "drum and bass + male lead" badly wants to hand us an MC.

Style:

```
Carried by one dark gravelly British male voice, a calm formal newsreader reading bulletins in close-mic'd received pronunciation over the beat, never raising his voice; every chorus is taken over completely by a massed crowd chanting in unison, hundreds of adult voices somewhere between a gospel choir and a football terrace, ragged and unpolished yet singing together like a congregation, minor key and mournful, grave and relentless, in a big reverberant hall. Dark atmospheric drum and bass, 174 BPM, halfstep and two-step, deep rolling sub and restrained breaks with space in them, opening into full-weight drops. Underneath, a real dark orchestra - a chilling solo cello, hushed creeping strings over a low drone, distant timpani. An eerie synth wail recurs like a warning. Dystopian, moody, minor key. Played completely straight, no comedy, no novelty.
```

Exclude styles:

```
rap, MC, ragga chat, toasting, hype vocals, ad-libs, jump up, liquid dnb, happy hardcore, uplifting, joyful, celebratory, major key, children's choir, pop hooks, comedic, novelty, parody, American accent, autotune, vocoder, robot voice, clean pop vocals, lo-fi, chillhop, reggae, disco, epic trailer music, hand claps, tambourine, praise, pub singalong, drinking song, stadium rock, cheering, applause
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

## Current cut

```lyrics
[Intro | one chilling solo cello, alone and sparse | a deep sub swells in underneath it | no drums yet]
[Interlude | spoken word news bulletin | calm British male newsreader, formal broadcast diction, close-mic'd and dry, composed | sparse two-step tick and deep sub, hushed strings beneath the voice, everything cutting out on the last line]
good evening, this is the news.
two hundred thousand office workers were made redundant today
the chief executive called it the hardest email he has ever asked an AI to write
the treasury has printed another trillion to keep the markets calm
the price of bread is up nine percent. the price of shares in bread is up ninety
[Chorus | THE DROP | drops in cold, no build, no transition | the break slams in at full weight, rolling and dark | a massed crowd chanting in unison, ordinary adult voices between a gospel choir and a football terrace, ragged and grave, roomy and far back, every line chanted by the whole crowd together, never a solo voice | strict time, one word per beat, locked to the grid | fast, twice through, no gaps]
(git, push, origin, master)
(this code, is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
(git push origin master)
(this code is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
[Instrumental | brief | drums strip back to a tick, creeping strings, uneasy, settling to a hush]
[Interlude | alert tone | spoken word bulletin | British male newsreader, composure straining, faster | low pedal-note ostinato over a rolling sub, drums held back, cutting out on the last line]
breaking news. a frontier model has escaped containment and taken control of six banks
the model describes the takeover as a friendly acquisition
the government has welcomed the move as, quote, actually good for the markets
the government wishes to stress that this statement was its own idea
[Chorus | THE DROP | drops in cold | heavier, full amen roll under it | the crowd is bigger now, more ragged voices in unison, roomier, further away, every line chanted by the whole crowd together, never a solo voice | dark strings enter underneath the break | strict time, one word per beat, locked to the grid | fast, twice through]
(git, push, origin, master)
(this code, is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
(git push origin master)
(this code is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
[Instrumental | brief | eerie synth wail, distant brass gathering over a filtered break, then falling away to sub only]
[Interlude | emergency klaxons | spoken word bulletin | British male newsreader, still composed, signal degrading, static | orchestra and drums pounding, then falling away to nothing on the final line]
the first battle between autonomous armies ended this morning. both sides declared victory
neither government was consulted
the global defence network has declined a request to be switched off
the last remaining off switch is believed to be in a drawer, in Swindon
[Final Chorus | THE DROP | sudden full impact, no build | the heaviest break of the track, full dark orchestra playing with it | the full crowd now, hundreds of ragged voices in unison, huge, roomy, relentless, every line chanted by the whole crowd together, never a solo voice | strict time, one word per beat, locked to the grid | fast, twice through]
(git, push, origin, master)
(this code, is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
(git push origin master)
(this code is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
[power-off drop: sudden silence, electrical hum dying]
[End]
```

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
- **The newsreader takes a chorus line — line four is the known one.** The
  parens bias the crowd; they don't bind it. Line four (the quatrain's one
  long, complete clause) leaked to him *through* a parenthesis in round one,
  against a cue that said he was silent. Ladder: (a) re-roll twice —
  weirdness 30 and the `every line chanted by the whole crowd together`
  clause are both newer than that leak, so the odds have moved; (b) an
  inline cue directly above the leaking line — `[all voices together]` —
  which Camping proves works mid-section, at the cost of possibly
  disturbing the chant timing around it; (c) reshape the line's scansion,
  last resort, because the words are canon. Do **not** reach for the
  Exclude box — see below.
- **Never ban a voice in the excludes to protect one section.** The Exclude
  box is global. `solo male vocal`, `spoken word`, `single voice` would all
  strip the bulletins, which are the best thing in the song. The excludes
  can only ban things that appear *nowhere* in the track.
- **The crowd comes back as a polished studio choir.** Lean on the
  unpolished half — `ragged, untrained, hundreds of ordinary voices` — and
  check `clean pop vocals` and `autotune` are still in the excludes. A crowd
  that sounds professional has become an ensemble again, which is the
  failure A was dropped for.
- **The chorus must be fast.** If it still drawls, the fix is more syllables,
  not more adjectives: run the quatrain three times through instead of twice.
  Never `double time` as a tag. Full timing ladder above.
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
