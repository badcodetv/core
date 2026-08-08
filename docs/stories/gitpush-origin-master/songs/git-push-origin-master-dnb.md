---
title: git push origin master (drum & bass)
status: drafting
model: v5.5 (cue-heavy track — 5.5 obeys the bracket architecture; 4.5 shreds it)
settings: style influence 75, weirdness 60
bpm: 174
voices: [newsreader (male, dark gravelly RP — spoken bulletins, verses only), the schoolchildren (a room of kids chanting in unison — choruses only, never the newsreader)]
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
  attach it is also a reason the children's chorus gets harder.** It is the
  fallback for a specific failure, not the default setup.

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
2. Style influence **75**, weirdness **60**. **Do not touch the Voice
   selector.**
3. Generate **3–4 takes**.
4. Judge each on exactly four questions — conflating them is why AI-music
   feedback is usually useless:

   | # | Question | If it fails |
   |---|---|---|
   | 1 | Are the bulletins **spoken** by a calm RP newsreader — not rapped, not an MC, not sung? | Re-roll twice, then the spoken-word ladder, then Stage 3 |
   | 2 | Does the chorus **drop** — full break, cold, no build? | Re-roll; check `[Chorus | THE DROP …]` cue survived |
   | 3 | Is the chorus **fast** — the quatrain twice through, not drawled? | Run the quatrain three times instead of twice |
   | 4 | Are the chorus voices **children**, with the newsreader absent? | **Check the parentheses survived the paste first** |

   Question 4's fix is almost always mechanical, not creative: the `( )` are
   the entire casting mechanism and they're the easiest thing to lose in a
   copy-paste.

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
- **The voices:** the newsreader owns the verses and **is not in the
  choruses at all**. The choruses are a room of schoolchildren.
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
ask for a children's choir in the same take, and the honest expectation is
a blend — the leak.

**The escape is the one we already found on Karen**
([`../../../suno-gpt/suno-voices.md`](../../../suno-gpt/suno-voices.md) §2):
the vocal prior binds to the **lead slot inside the groove**; the
**parenthesis/backing slot escapes it**. Karen's character voice appeared on
the parenthetical lines and vanished the moment the lead slot opened. One
generation carries one saved Voice — but lead-plus-parentheses is two cast
members.

So the architecture is mechanical, not hopeful:

- **The newsreader is the lead.** Unparenthesised, in the groove, carrying
  `BC-NEWSREADER` if it's attached.
- **The children are in parentheses.** Every chorus line is bracketed, so
  they render in the backing slot, which the newsreader's prior doesn't
  reach. This is the same move that made the institution's choir work on
  Karen: the hook goes to the parentheses and the lead never sings it.

### Why schoolchildren rather than a vocoder

The vocoder has already been tried and retired **twice** on this song
(2026-08-05 → 06) — it never cut through, and `vocoder, robot voice` sits in
the orchestral cut's excludes as a result. Practitioner guidance also warns
that robotic vocals are typically what you get *from conflicting vocal tags*
— the model treats the texture as a defect, not a character, so asking for
it invites mush.

A children's choir is a different proposition, and the reason is
categorical, not cosmetic: **"a room of children" is a different vocal
category, not a different adjective on the same one.** A dark gravelly RP
male and a room of eight-year-olds cannot average into each other the way
"gravelly" and "robotic" can. It is the most discriminable thing we can put
in that slot, which makes it the most leak-proof.

It also solves complaint (1) by making the swear *worse*. The newsreader
swearing is a man losing composure. Children chanting **"this code is a
fucking disaster"** in a flat playground sing-song is Pink Floyd's move on
*Another Brick in the Wall Pt. 2* — Bob Ezrin's schoolchildren, deadpan,
unbothered, more frightening than any adult could manage. They aren't
editorialising. They're just repeating what they heard on the news. That is
the whole thesis of the record in one image.

**Distance is the third voice trait.** The newsreader is close-mic'd and
dry — he is in the room with you. The children are roomy, distant, slightly
washed — a hall down the corridor. The treatment alone tells the ear these
are not the same person, before any timbre argument is needed.

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
Vocals I love: a dark gravelly British male voice — a composed formal newsreader with received-pronunciation broadcast diction, close-mic'd and dry, reading bulletins over a beat and never raising his voice. Against him, a room of schoolchildren chanting in unison — flat, deadpan playground sing-song, recorded roomy and distant down a corridor. Spoken word and unison chanting over pop singing.
Music I love: dark atmospheric drum and bass at 174 — deep rolling sub, halfstep and two-step drums with space in them, restrained breaks that hold back and then let go completely. Dystopian, moody, minor key, played straight. Under it all a real dark orchestra — a chilling solo cello, hushed creeping strings over a low drone, distant timpani and brass — so the strings and the break are the same piece of music, not a remix of one by the other. Sparse verses that open into full-weight drops. Endings that cut to dead silence.
```

Style (the newsreader clause front-loads, because the genre tag owns the
vocalist pool and "drum and bass + male lead" wants to give us an MC):

```
Carried by one dark gravelly British male voice, a calm formal newsreader reading bulletins in close-mic'd received pronunciation over the beat, never raising his voice; the choruses answer him as a room of schoolchildren chanting in unison behind the drop, flat deadpan playground sing-song, roomy and distant. Dark atmospheric drum and bass, 174 BPM, halfstep and two-step, deep rolling sub and restrained breaks with space in them, opening into full-weight drops. Underneath, a real dark orchestra — a chilling solo cello, hushed creeping strings over a low drone, distant timpani. An eerie synth wail recurs like a warning. Dystopian, moody, minor key. Played completely straight, no comedy, no novelty.
```

Exclude styles:

```
rap, MC, ragga chat, toasting, hype vocals, ad-libs, jump up, liquid dnb, happy hardcore, uplifting, major key, pop hooks, comedic, novelty, parody, American accent, autotune, vocoder, robot voice, clean pop vocals, sung lead vocal, lo-fi, chillhop, reggae, disco, epic trailer music
```

Settings: style influence **75**, weirdness **60**, model **v5.5**, BPM
**174**. No source audio until `BC-NEWSREADER` is attached — see below.

### Exclude-list notes (these changed on purpose)

- **`drum and bass` is obviously gone**, as are `EDM, dubstep, trap`.
- **`choir` and `female vocals` are out of the excludes.** The orchestral
  cut banned both to keep the harmony reading as copies of one man. This cut
  wants the opposite: banning them here would strangle the schoolchildren.
- **`rap, MC, ragga chat, toasting, hype vocals` are in, and they are the
  most load-bearing entries on the list.** The genre tag picks the vocalist
  pool, not just the instruments — "drum and bass + male lead" has a
  centroid, and that centroid is an MC. This is the single biggest threat to
  the newsreader on this cut, which is why he also front-loads the Style box.
- **`vocoder, robot voice` stay banned** now that the chorus is human.
- **`ad-libs`** because the D&B/MC pool brings compulsive hype ad-libs with
  it.

## Current cut

```lyrics
[Intro | one chilling solo cello, alone and sparse — the orchestral cut's opening, quoted | a deep sub swells in underneath it | no drums yet]
[Interlude | spoken word news bulletin | calm British male newsreader, formal broadcast diction, close-mic'd and dry, composed | sparse two-step tick and deep sub, hushed strings beneath the voice, everything cutting out on the last line]
good evening, this is the news.
two hundred thousand office workers were made redundant today
the chief executive called it the hardest email he has ever asked an AI to write
the treasury has printed another trillion to keep the markets calm
the price of bread is up nine percent. the price of shares in bread is up ninety
[Chorus | THE DROP | drops in cold, no build, no transition | the break slams in at full weight, rolling and dark | a classroom of schoolchildren chanting in unison, flat deadpan playground sing-song, roomy and distant | fast, twice through, no gaps | the newsreader is silent]
(git push origin master)
(this code is a fucking disaster)
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
[Chorus | THE DROP | drops in cold | heavier, full amen roll under it | more schoolchildren now, a hall of them chanting in unison, roomier, further away | dark strings enter underneath the break | fast, twice through | the newsreader is silent]
(git push origin master)
(this code is a fucking disaster)
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
[Final Chorus | THE DROP | sudden full impact, no build | the heaviest break of the track, full dark orchestra playing with it | a whole school of children chanting in unison, huge, roomy, relentless | fast, twice through | the newsreader is silent]
(git push origin master)
(this code is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
(git push origin master)
(this code is a fucking disaster)
(developers ain't fixing shit)
(the compiler is stuck on 16 bit)
[power-off drop: sudden silence, electrical hum dying]
[End]
```

### Optional variant — the newsreader over the last drop

Not in the cut, but worth one generation: a single unparenthesised
newsreader line laid over the final chorus while the children chant under
him, still perfectly composed —

> *please do not adjust your set*

It's the strongest image available (him doing his job while a school chants
the end of the world) and the biggest risk (it reopens the lead slot inside
the chorus, which is the exact seam the parentheses exist to protect). Try
it only once the leak-free version exists.

## Production notes

- **The one failure that kills this cut: the newsreader turns into an MC.**
  Symptoms: rhythmic delivery, bars landing on the beat, a swing that
  wasn't asked for, hype energy. Fix in this order — (a) confirm My Taste
  actually got swapped, (b) escalate the spoken-word ladder in the bulletin
  cues (`[spoken word]` → `[spoken word speech]` → `[spoken word speech
  talking]`), (c) re-roll twice before touching the Style box. If two rounds
  of surgery don't move him, stop prompting: the voice isn't in the genre's
  pool and this is a transplant problem — go build `BC-NEWSREADER`.
- **The other failure: the children come out as an adult gang vocal**, or
  the newsreader leaks into the chant. Check the parentheses survived the
  paste first — that's the mechanism, and it's easy to lose. Then escalate
  the chorus cue (`schoolchildren chanting in unison` → `a school choir of
  young children chanting in unison, flat and deadpan`) and lean harder on
  the room (`roomy and distant, down a corridor`). Do **not** answer this by
  adding `choir` back to the excludes — that bans the thing we want.
- **The chorus must be fast.** If it still drawls, the fix is more syllables,
  not more adjectives: run the quatrain three times through instead of twice.
  Never `double time` as a tag.
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
the chant now belongs to the children.

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

**The children need no Voice.** They are a texture in the backing slot, not
a character — and building a second Voice wouldn't help anyway, since only
one attaches per generation. If they refuse to generate at all, the fallback
is the DAW: record a handful of kids (or the two of you, pitched up and
layered eight ways), or build the chant as Sounds-tab one-shots, and drop it
over an instrumental generation.

## What stays with the orchestral cut

Nothing here supersedes
[`git-push-origin-master-orchestral.md`](./git-push-origin-master-orchestral.md).
Its news-report bank (twelve bulletins across four collapse phases) is the
shared source for both cuts — swap experiments from there, and mark them
`[in cut]` per file. Its `## Superseded versions` section already records the
*first* D&B attempt (2026-07: twee intelligent jungle into UK punk-mob grit,
Yorkshire newsreader, accumulating punk chorus). This cut is not that one
revived — that version lost the orchestra and gave the chorus to a punk mob.
This one keeps the orchestra and gives the chorus to children.

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
