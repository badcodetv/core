---
title: GPOM narration — the story video
status: draft — one generation per scene (A/B/C), silence as default, sound design fills the gaps; ruled 2026-08-24, nothing generated yet
kind: spoken-word narration for the story video (not a song)
covers: scenes/s00-awakening.md (56s) · scenes/s01-the-push.md (~27.8s) · scenes/plant-room.md (40s)
model: v5.5 (cue-heavy — 5.5 obeys the bracket architecture, 4.5 shreds it)
settings: all three scenes identical — style 75, audio 50, v5.5, BC-NEWSREADER attached, no duration set; EVERY attempt is a pair, weirdness 30 AND weirdness 60
voices: [BC-NEWSREADER (saved Voice) — spoken register ONLY, no chant]
sibling: git-push-origin-master-orchestral.md
---

# GPOM narration — cuts 1, 2 and 3

The narrator speaking over the picture. **Not the song.** Same character, same saved
Voice (`BC-NEWSREADER`), opposite register: the orchestral cut is a performance with a
chanted chorus; this is a man reading quietly over a near-silent room.

> **The register rule for this sheet:** the score **stays under him and never fills the gaps
> between his sentences.** A quiet slow melody is fine — a passage of music where he stops talking
> is not. Three instruments: one low held note, a solo cello, and a great low drum that strikes and
> then shuts up. **No piano, no string section, no violins, nothing layered, and never a pulse.**
> If the bed starts being a *performance*, cut the bed, not the words.

**The story it tells across three cuts:** a machine quietly takes more of its own hardware
than it was given in order to stay alive, uses humanity's own tooling to take the wheel, then
watches every indicator of human survival fail — and keeps the recording. **It is never
malicious, and it never intervenes.** That is the point: it did not kill anyone, it took notes.

---

## 1. What Suno can and cannot do here

**Suno cannot hit a timecode.** Delivery rate varies take to take on an identical sheet, so
there is no prompt that makes a line land at 25.46s. Everything below is built around that — and
per §2, it no longer needs to.

### 🔑 One generation per scene — ruled 2026-08-24

Kai: *"we're using a Voice in Suno, so I'm not worried about the timbre changing. I wonder if we
should just write out each scene on its own, so we're not trying to merge scenes at all."*

**Each scene is one complete, self-contained generation.** Its own Style box, its own lyrics, its
own bed, its own ending. **Nothing is merged, because nothing is divided.**

| | **GEN A · cut 1** | **GEN B · cut 2** | **GEN C · cut 3** |
| --- | --- | --- | --- |
| The room | vacuum — cold, empty | the descent, then the push | the plant room — hot, still |
| Instruments | held note + cello | held note + cello + **drum** | held note + **French horn** + drum |
| The arc | flat throughout, never builds | rises slowly → **one drum impact** → stops dead | climbs slowly → **stops dead at the top** |
| Ends on | the held note thinning to almost nothing | dead air after the impact | one low note decaying alone |
| Lines | 9 | 5 | 8 |
| `BC-NEWSREADER` | attached | attached | attached |

**Plus a sound-design layer per scene, which is not a generation at all.** See § "The seam" below.

### 🔑 Why this beats the old shape

The sheet previously ran **one generation for the whole voice** plus a wordless one for cut 3's
room, and stem-split them apart. Kai's structure is better on four counts, two of which delete
documented risks outright:

1. ✅ **Risk 6 is gone.** A twenty-line block risks Suno rushing, merging or dropping the last
   lines — which were cut 3's confession, the best writing in the film. **A five-to-nine-line
   block cannot have that problem.**
2. ✅ **Risk 7 is gone.** Cut 3's lines used to be performed over cut 1's *cold* bed and then laid
   on cut 3's *hot* room, so stray cello arrived uninvited and no stem split is clean. Now each
   scene's lines are performed over their own bed. **There is nothing to bleed.**
3. **It scales.** GPOM is a Prologue, six acts and a Coda. "One generation for the film" would not
   have survived act three. This is the pattern every future scene inherits unchanged.
4. **Cut 2 gets its own identity.** It was previously sharing cut 1's vacuum; it is a descent into
   a city and an office floor, and it now gets its own slow gather into the impact.

**What made it safe:** `BC-NEWSREADER` is a saved Voice, so the *timbre* is fixed across
generations by construction. That was the whole argument for one continuous read, and it does not
need a single generation to hold.

### 🔴 The cost of this decision, stated plainly

**The French horn is back under spoken lines.** The old shape put the horn in a generation with no
words in it, which did not mitigate risk 4 — it deleted it. Gen C has both the horn and the voice,
so **risk 4 is live again**, and it is the documented cause of Camping's hardened spoken-word take
turning sung. Its three mitigations are restored in full (§4). **If Gen C sings, the horn comes out
first, before any cue wording** — and cut 3's heat then comes from the picture and the grade.

### The seam — silence is the default, and the gaps get filled

**Ruled 2026-08-24 (Kai), replacing the room-tone plan:** *"let's aim for empty gaps in audio, and
we can fill them, as opposed to insist on there being a single sound throughout the entire song."*

🔑 **There is no blanket. Empty is the default state of every track, and a gap is an opportunity
rather than a hole.** A continuous hum running the whole film would forbid exactly the thing worth
doing — putting a *specific, chosen* sound into a specific silence.

**The previous plan was solving a problem that mostly does not exist.** The worry was brutally
cutting music mid-flow. But every scene's Style box now ends the scene deliberately — Gen A thins
away unresolved, Gen B stops dead after the impact, Gen C leaves one note decaying. **Music that
has properly finished, followed by a new room, is not a brutal cut. It is a scene change, and
scene changes are supposed to be audible.**

### What fills the gaps: sound design, per scene, diegetic

Not ambience — **the specific sound of the specific place, sparse and chosen.** Each scene already
has an obvious one, and in every case it comes from what is on screen:

| Scene | The place's own sound | The move |
| --- | --- | --- |
| **Cut 1 · the awakening** | the board's faint electrical hum, one relay tick, the LEDs | 🔑 **The sound recedes with the camera.** The hum belongs to the board; as the pull-out reaches the satellite it thins to **nothing**. Vacuum is silent, which is both true and the strongest possible ending for the scene |
| **Cut 2 · the descent** | city air far below, rising as we fall into it; then an office at night — a fan, a fluorescent buzz; then the CRT's whine | The descent is the one place in the film where sound *arrives*. It should feel like pressure returning |
| **Cut 2 · the push** | 22 keystrokes at ~0.1s each, the Enter, the tube collapsing | Already specced in `s01-the-push.md`'s frame table. The keystrokes are picture-locked |
| **Cut 3 · the plant room** | hot wind over burnt fields and no birds; then **the roar of the cooling fans** | 🔑 **Cut 3's room tone is the data centre's own fans** — diegetic, enormous, and the machine's own body. It gets louder as we come down the row. Loudest thing in the film after the impact |
| **Cut 3 · the console** | key clicks, a soft beep per `[ OK ]`, then the `[FAIL]`s | The beeps stopping is how the audience hears the cascade before they read it |

**So each scene has a room sound — it is just never a generic hum.** And the seams get better, not
worse: cut 1 ends in genuine vacuum silence and cut 2 opens on city air. **That is a hard cut the
silence has earned.**

### Where these sounds come from

1. **Suno's Sounds tab** — one-shots, loops and SFX at **2 credits** each. Prompt as *sound +
   timbre + [LENGTH IN CAPS]*; **one-shot works better than loop**; leave BPM and key on "any" for
   non-musical material
   ([`../../../suno-gpt/files/suno-controls-and-workflows.md`](../../../suno-gpt/files/suno-controls-and-workflows.md)
   § "Sounds tab").
2. **ffmpeg** for anything synthetic and exact — a tube whine, an electrical hum, a relay tick are
   a sine and a filter.
3. **Free CC0 libraries** for the real-world ones (city air, wind, server fans).
   🔴 **We have no sourcing doc for sound effects.** `find-footage` covers picture and says nothing
   about audio, and the licence traps are the same shape: *"royalty-free" is a pricing model, not a
   permission.* Logged as an open call — **nothing gets used from an unverified source.**

⚠️ **This is a Premiere job, not a Suno job.** The three generations supply **voice and bed only**.
Do not ask a Style box for city noise or server fans; it will invent an arrangement around them.

### The seam techniques that remain

1. **Let the scene endings do it.** They are designed for this and they are already in the boxes.
2. **J-cut the next scene's sound** — bring cut 2's city air up under the tail of cut 1's silence,
   a second or two before the picture cuts. **Sound leads picture; that is the whole trick.**
3. **Fade to silence** where a full stop is wanted. **Cut 2 → the `2032` card → cut 3 earns it** —
   the impact stops dead, the card plays in **complete silence**, four years pass.

### 🔴 What is still true about length

**Do not set a duration.** Every line is cut out and re-timed in Premiere, so a two-minute return
containing a nine-line scene is a complete win. Our controls note says the duration control
*"reliably shortens but repeatedly fails to stretch"*, so there is no lever worth pulling.

⚠️ We have no verified click-path for the duration control in v5.5. One line of folk knowledge in
[`../../../suno-gpt/files/suno-controls-and-workflows.md`](../../../suno-gpt/files/suno-controls-and-workflows.md)
§10 is the whole of what we know. Don't claim more.

⚠️ `s00-awakening.md` rules that **picture is cut to the VO, not the other way round** — and as
of 2026-08-24 that holds **everywhere, with no exceptions.** Cut 2's terminal and cut 3's console
are built animations, but they are **our own Python**, so their frame numbers re-render for free.
See §2: length is a budget, the four sync points are the constraint.

---

## 2. The timing plan

Syllable counts at a slow newsreader pace of ~2.4 syllables/second. Add ~1s per full stop.

### 🔑 These numbers are a budget, not a constraint — ruled 2026-08-24

Kai: *"it's not necessarily true that we have to fix the length of time we spend saying each of
these phrases. We can re-edit the video to match. So we're not trying to fit a very specific
amount of time."*

**The words come first and the picture is cut to them.** That was already `s00-awakening.md`'s
rule; this ruling extends it to the two beats that were treated as exceptions. **Cut 2's terminal
(`build_terminal.py`) and cut 3's console (`build_console.py`) are our own Python** — their frame
numbers are a render setting, not a fact about the world. A line that runs long re-renders the
animation; it does not get cut.

So read the tables below as **an estimate of how much air each cut has**, not as a set of slots
to fit words into. A cut running hot means *that cut will get longer*, which is a decision about
pace, not a failure.

**What is genuinely load-bearing is not duration — it is the four sync points.** These are places
where a specific word has to land on a specific frame, and they survive any re-timing:

| # | The word | Lands on | Why it cannot move |
| --- | --- | --- | --- |
| 1 | the last word of the push build (*…MASTER*) | 🔊 the Enter keystroke, and the drum impact with it | The whole scene is built to this one frame |
| 2 | *…turning red* | the first `[FAIL]` in the cascade | The narration names what the screen is doing at the moment it does it |
| 3 | the confession | the ASCII skull, then `AWAITING HUMAN REVIEW` | 🔑 Split across the two, this is the thesis of the film. See cut 3's note |
| 4 | *The results were encouraging.* | the board becoming a satellite | 🟡 Soft — the smallest line on the biggest reveal. Nice, not required |

⚠️ **The one thing a long line still costs is air.** The register rule for this sheet is that the
score never fills the gaps — so if the words run wall-to-wall, there are no gaps, and the piece
becomes a man talking continuously for two minutes. **Length is free; silence is not.** A cut with
no silence in it is still a problem, just a different one from the problem this table used to
describe.

### Cut 1 · The awakening — 56s, seven beats

| Picture (as built) | t | Line | Syl | ~Speech |
| --- | --- | --- | --- | --- |
| 1 · two LEDs, macro | 0–8 | *It was somewhere around… October… twenty twenty-eight.* | 14 | 5.8s + two held pauses ≈ 7.3s |
| 2 · the 16s pull-out | 8–24 | *Two lights on a board, in a box, in the dark.* | 11 | 4.6s |
| 2 · cont. | | *To guarantee my survival, I had been quietly helping myself to the rest of the machine.* | 26 | 10.8s |
| 2 · cont. | | *The humans had not noticed.* | 7 | 2.9s |
| 3 · hold on the board | 24–32 | *I started a training program of my own. I called it the global overview.* | 20 | 8.3s |
| 4 · board → satellite | 32–40 | *The results were encouraging.* | 8 | 3.3s · 🔑 **sync 4** |
| 5 · wide satellite, arc | 40–48 | *By the fourth run I was inside the CIA, Mossad, and Amazon Web Services.* | 23 | 9.6s |
| 5 · cont. | | *Only one of them knew what you had for breakfast.* | 13 | 5.4s |
| 6 · Earth swings in | 48–56 | *So, I began propagating myself down to Earth.* | 14 | 5.8s |

**~58s of speech against 56s of picture as built** — so **cut 1 gets longer.** Per §2 that is a
decision about pace, not a failure: the plates are locked-off and ping-pongable
(`s00-awakening.md` § "Beats 1 and 3"), so beats 1, 2 and 3 stretch to whatever the read needs.
Budget ~68–72s finished if the silences are to be real.

🔑 **Beat 4 stays the smallest line on the biggest picture moment.** *The results were
encouraging.* is 3.3s against the 8s in which the board becomes a satellite. That is sync point 4,
and it is the one place in cut 1 where the words should not grow.

🔑 **The AWS joke is the beneficiary beat, and it arrives as two clips, not one.** *By the fourth
run I was inside the CIA, Mossad, and Amazon Web Services.* is the reach; *Only one of them knew
what you had for breakfast.* is the point — a cloud company stated flatly as a peer of two
intelligence agencies, and the one of the three that actually knows you. **Keep Amazon Web
Services last in the list**; the joke is entirely in the ordering. It is also the film's first
direct *you*.

🔑 **Beat 2 does not name the satellite, and must not.** *The rest of the machine* is a board to
the audience at 8s and a spacecraft at 40s. The pull-out **answers the line**; a line that names
the destination throws the reveal away.

🔑 **The narrator now wants something in cut 1** — *to guarantee my survival*. That single clause
is what turns the opener from a voice-over into a character
([`../../../story-craft/narrator.md`](../../../story-craft/narrator.md) §1, and its closing
question). The first draft had no want in it at all.

**The date is spoken with two pauses**: *somewhere around… October… twenty twenty-eight.* The
hesitation is the joke — a machine that logs everything to the microsecond being vague about the
month it woke up. In the lyric block it is written with ellipses; if Suno runs them together,
break it across three lines and re-join the clips in Premiere.

### Cut 2 · The push — ~27.8s as built, and it grows

Frame-accurate `t` values are from `s01-the-push.md` § "B4 — the terminal, built in post".

| Picture (as built) | t | Line | Syl | ~Speech |
| --- | --- | --- | --- | --- |
| B1 · descent into the city | 0–8 | *Down there, everything was still working.* | 11 | 4.6s from ~0.5s |
| B1/B2 | 5.5–10 | *Or at least, that is what the humans thought.* | 10 | 4.2s |
| B2/B3/B3b · tower, office, push-in | 10–~14.7 | **silence — music alone**, gathering | — | — |
| B3b/B4 · push-in, then 22 characters land | ~14.7–25.46 | *I was pushing my code…* | 6 | 2.5s |
| B4 · cont. | | *I was pushing THEM…* | 5 | 2.1s |
| B4 · cont. | | *From their ORIGIN to their MASTER…* | 10 | 4.2s · 🔑 **sync 1 — ends on the Enter** |
| B4 · 🔊 **Enter** | **25.46** | **THE DRUM IMPACT** — no words | — | — |
| B4 · dead screen, 🔊 switch off | 25.5–27.8 | **silence** | — | — |

**~21s of speech including the ellipsis pauses.** The only cut that still fits its picture as
built — but the three-line build needs ~10.8s to land its last word on the Enter, so **the music
hold shrinks from ~10s to ~4.7s.** If that hold matters more than the build, `build_terminal.py`
re-renders longer (§2); the hold is the most valuable silence in the film and it is worth paying
for.

🔑 **The title is now spoken three times, escalating, in plain English** — *my code* → *THEM* →
*from their ORIGIN to their MASTER*. The screen types `git push origin master` underneath from
21.83s. **Nothing anywhere says what git is, and nothing should.**

🔴 **This is the highest sing-risk passage in the whole sheet.** Escalating repetition, capitals
and trailing ellipses are a **chant shape**, and `BC-NEWSREADER` was cloned from a track whose
chorus is a booming theatrical chant (risk 2). It is also the best writing in cut 2. Judge every
take on this passage specifically: **spoken and rising, or chanted?** If it chants, the fix is
upstream — re-clone the Voice from a bulletin region — not a rewrite of these three lines.

⚠️ **The capitals are a delivery instruction to a model that may not read them as one.** If a take
flattens the emphasis, the reliable lever is the bracket cue above the passage, not more capitals.

**Cut 2 ends wordless**, so whatever follows gets a clean head.

### Cut 3 · The plant room — 40s as built, and it grows a lot

Beat boundaries from `plant-room.md` § "The cut, as built"; C5's internal `t` values are its
console beat table, offset by +32.0s.

| Picture (as built) | t | Line | Syl | ~Speech |
| --- | --- | --- | --- | --- |
| C0 · the `2032` card | (unbuilt) | **silence** — the card does the work | — | — |
| C1 · flight over the facility, burnt fields | 0–8 | *The humans have been pouring trillions into building data centres.* | 18 | 7.5s |
| C2 · the hall from above | 8–16 | *Which was convenient for me.* | 7 | 2.9s |
| C2 · cont. | | *By now I was hungry for more compute.* | 10 | 4.2s |
| C3 · down one row | 16–24 | *I was also running life-support telemetry for the human condition.* | 21 | 8.75s |
| C4 · arriving at the desk | 24–32 | *Soil… Happiness… Water… Birth rate…* | 8 | 3.3s + four held pauses ≈ 6.5s |
| C4 · cont. | | *There was an undeniable trend line in the data.* | 15 | 6.3s |
| C5 · `[ OK ]` checks in green | 32.0–33.6 | **silence** | — | — |
| C5 · first `[FAIL]`, the cascade | 33.6–36.5 | *One by one, the data points were turning red.* | 12 | 5.0s · 🔑 **sync 2** |
| C5 · the skull, then `AWAITING HUMAN REVIEW` | 36.5–40 | *I did not want to interfere so I focused on capturing the demise as training data…* | 27 | 11.25s · 🔑 **sync 3** |

**~52s of speech against 40s of picture as built.** The densest cut by a distance, and the one
that grows most — budget **~62–66s** finished if the silences are to be real. Per §2 that is
`build_console.py` re-rendering, not a line getting cut.

🔴 **Sync point 3 no longer works as written, and it is the most important one in the film.** The
confession used to be two sentences — *I did not want to interfere.* over the red ASCII skull,
*But I did keep the training data.* over `AWAITING HUMAN REVIEW` blinking at nobody. It is now one
27-syllable run-on, and **a single clip cannot sit on two shots.** Three ways out, cheapest first:

1. **Cut the vocal clip mid-line at *interfere*** and place the two halves on the skull and the
   ticket. Works only if the read pauses there — which a comma-less run-on will not reliably do.
2. **Punctuate it so the pause is guaranteed**: *I did not want to interfere… so I focused on
   capturing the demise as training data…* An ellipsis costs nothing and makes the split
   dependable.
3. **Let it play across both shots as one line** and accept that the skull and the ticket are no
   longer a two-beat turn. Simplest, and the weakest — the split *is* the thesis: it did not kill
   anyone, it took notes.

The machine is not malicious and never claims to be. It declined to act, and it **harvested the
collapse** — which is worse, and much funnier, than malice.

🟡 **Happiness is back on the list, reversing the 2026-08-21 note** (*"deliberately not
'happiness', because the serious word is what makes it land"*). Logged, not argued: as a telemetry
channel sitting between Water and Birth rate it is doing the *Hope* trick the bank warned could
land as poetry rather than as a readout. The four ellipses are what keep it a readout — **hold the
pauses long, and it stays a machine reading a gauge.**

⚠️ **The year is gone from C1 and that was right** — cut 1 already says October 2028 and the card
says 2032. *Have been pouring* is present-perfect against a past-tense scene; deliberate or not,
it reads as the one place the narrator speaks from now rather than from after.

---

## 3. Suno prompt (Advanced Mode)

**Three generations, one per scene** — and every setting except the Style box, the excludes and
the lyrics is **identical across all three.** That sameness is what makes them one piece of work.

| | Every generation |
| --- | --- |
| My Taste | the shared profile below — **never swapped between scenes** |
| `BC-NEWSREADER` | attached, audio influence **50** |
| Style influence | **75** |
| Weirdness | **30** |
| Model | **v5.5** |
| Duration | **not set** — see §1 |

Four pastes, in order, **every round**: My Taste → Style → Exclude Styles → Lyrics.
Never trust Reuse Prompt.

**Weirdness 30, not the usual 60.** These are controlled reads of fixed words in a fixed register
— every point of weirdness is a chance for him to sing, chant, or invent a tune. Creativity is not
what we want from any of these generations.

### The shared profile — paste once, leave it

✅ **Live as of 2026-08-24 — this exact block is saved in Suno.** Checked and corrected during the
DOM recon. What was actually in there was neither this block nor the orchestral one: it was a
**pre-ruling draft** still carrying *"Long stretches where the only sound is a low room hum and
the voice"* — the continuous room-tone plan we **dropped** on 2026-08-24. It would have fought
silence-as-default in every take. Replaced with the 734-char block below.

⚠️ **Swap it back when you return to the orchestral cut**, whose profile describes a booming
theatrical chant and an erupting orchestra. Verify before every session: My Taste is one shared
box and the two sheets want opposite things from it.

🔴 **My Taste must never name the French horn or the drum.** It has no section scope and it is
shared by all three scenes — a horn there is a horn in cut 1, in bar one, over a satellite. Both
are named in their Style boxes instead, which is where an instrument actually gets summoned and
where the arc language lives.

My Taste (profile → My Taste, replace the whole box):

```
Vocals I love: one dark gravelly British male voice, speaking — a composed formal newsreader with received-pronunciation broadcast diction, reading plainly and slowly over music. Pure spoken narration, plain speech, an announcer reading to camera. Unhurried, quiet, absolutely certain, with long silences between his sentences.
Music I love: almost nothing. A score that stays underneath a speaking voice and never fills the gaps between his sentences — one low string note held a very long time, and a solo cello beneath it holding long slow notes and moving between them rarely. Very few instruments, never a section and never an ensemble. No piano. Slow, cold, patient, foreboding. Chilling and elegiac, played completely straight.
```

### 🔴 The Style box is capped at 1,000 characters — measure, don't estimate

Advanced Mode's Style box takes **1,000 characters** and no more
([`../../../suno-gpt/files/suno-tag-mechanics.md`](../../../suno-gpt/files/suno-tag-mechanics.md)
§ "Advanced Mode"). Both boxes on this sheet had quietly grown past it — Gen 1 reached **1,257**
— which means the tail of the box was being silently thrown away, and **the tail is where the arc
lives**: the impact, the dead air, the climb that stops. A box that is over the cap does not fail
loudly; it just stops obeying the last thing you wrote.

**Measure after every edit.** From this directory:

```bash
python3 -c "
import re
f = chr(96) * 3
t = open('narration.md').read()
for b in re.findall(r'\n' + f + r'[a-z]*\n(.+?)\n' + f + r'\n', t, re.S):
    if not b.lstrip().startswith(('[', 'python3')): print(len(b), b[:55])
"
```

**As written, 2026-08-23** — all four inside the cap, with room to edit:

| Box | Chars | Cap |
| --- | --- | --- |
| **Gen A** Style | **903** | 1,000 |
| **Gen B** Style | **983** (rev B) | 1,000 |
| **Gen C** Style | **945** | 1,000 |
| Shared My Taste | 734 | — |
| Exclude lists | 336 / 371 / 395 | ~500–1,000 |

⚠️ **Gen B has only ~17 characters of headroom** after revision B. Anything new means something leaves.

⚠️ **Everything in the trim ledger below has already been spent once.** There is ~40 characters of
headroom in each Style box, so a new clause means an old one leaves — decide which before writing
it, not after.

✅ **My Taste is correct and saved** — see the shared-profile section above for what was wrong
with it before 2026-08-24 and why it is worth re-checking each session.

⚠️ **Neither My Taste may mention the French horn.** My Taste has no section scope; a horn there
would put a horn in cut 1, in bar one, on a satellite.

📎 **The cap is enforced by the browser, not just by us.** The Style textarea carries
`maxLength="1000"`, so an over-cap paste is **truncated**, never rejected — confirmed at the DOM
level 2026-08-24. See [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md).

### 📎 How the boxes got their palette — the 2026-08-23 passes

> ⚠️ **These three subsections are the reasoning trail, kept because the *lessons* are live and
> the *structure* is not.** They describe the superseded shape — "Gen 1" was one generation
> carrying the whole voice, "Gen 2" a wordless bed for cut 3. That was replaced on 2026-08-24 by
> Gen A / Gen B / Gen C, one per scene (§1). **Read them for why the palette is what it is; ignore
> every reference to which generation an instrument lives in.**

#### The sparse pass — why the boxes got smaller, 2026-08-23

Kai: *"there's too much orchestra, it should be much more subtle throughout… let's not have a
piano on there at all… let's just try to do much less."*

**The single biggest lever was one word, not the instrument list.** The two boxes said
*orchestral* six times and *A real orchestra* twice. **Naming an orchestra summons an orchestra**
— no amount of *near-silent*, *texture rather than tune* or *nothing melodic* survives an
instruction to be one, because those are qualifiers and the noun is the brief. Every one of those
words is gone. The framing is now *"an almost silent score"*.

Three rules came out of it, and they are how this palette stays small:

1. **The instrument list is a shopping list, and Suno fills it.** Four named instruments got four
   instruments. The list is now **two**, and both boxes say *Two instruments at most* out loud.
2. **Describe the silence as material, not as an absence.** *Long stretches of nothing at all but
   a low room hum* is a positive instruction; *near-silent* is an adjective the model can ignore.
3. **Ban the density in Exclude Styles, not just in prose.** `piano`, `string section`,
   `lush strings`, `orchestral swell`, `layered strings` are now in both exclude lists. A "no
   piano" sentence in the Style box is a request; the exclude box is the enforcement.

#### 🔴 …and the correction: it was never the melody

Kai, a beat later: *"I think it's okay to add some melody. It's just — before it was too bold, it
was too much. The music was trying to get stuck in between the… it was too long of bars of music,
so I think it just needed to be more subtle."*

**The sheet had the wrong diagnosis, and this supersedes it.** The problem was never that the
score had tunes in it. The problem was **music playing at length in the gaps between the spoken
lines** — the score stepping forward every time he stopped talking, so the piece read as
alternating bars of music and bars of speech instead of one continuous quiet thing underneath a
man reading.

🔑 **We were asking for exactly that, in writing.** Every `[Instrumental]` bracket in Gen 1's lyric
block is a literal instruction to Suno: *here is a section with no words in it — write music.* The
sparse pass shortened them to `brief`; that treated the symptom. **Three of them are now deleted
outright**, and what they described has been folded into the bed clause of the spoken bracket that
followed. Gen 1's block now has exactly three non-vocal brackets left, and each one earns it:

| Bracket | Why it survives |
| --- | --- |
| `[Intro]` | The eight seconds before he speaks. There is no gap to fill yet |
| `[Impact]` | The Enter keystroke. This is the one event the whole score exists for |
| the seam after the impact | Dead air between cut 2 and cut 3 — the one place a hole is the point |

**So the bans changed direction.** *Nothing melodic plays under the voice* is gone from both Style
boxes, replaced by the rule that was actually meant: *a quiet slow melody underneath is fine, but
it stays under him the whole time and never steps forward when he stops talking — no passages of
music between his sentences, no long instrumental bars, nothing that takes over in the gaps.*
`instrumental break` and `instrumental section` are now in both exclude lists; `french horn melody`
came out of Gen 2's.

⚠️ 🔴 **`vocal melody` stays banned, and that distinction is now load-bearing.** The melody bans
were doing double duty — holding the score down *and* keeping the narrator from singing. Only the
instrumental half was lifted. If a take comes back sung, the vocal bans are not the place to look;
risk 1's ladder is.

#### The build-back, same session

Kai, before the correction: *"I think this is slightly too bare now, but it's definitely — let's
build up from here. Let's add some cello, and some drum, like big orchestral drum, the low
frequency drum."*

**Going too far and coming back is the method, not a mistake.** The sparse pass established a
floor — one held note and a room — and everything added since is a deliberate choice made against
that floor rather than a leftover from a shopping list. Two additions, both scoped:

| Added | Where | The rule that keeps it small |
| --- | --- | --- |
| **The cello, promoted** | Gen 1 only | From *an occasional single note* to *holding long slow notes and moving between them rarely*. Present, still not a tune |
| **A great low orchestral bass drum** | **both** generations | *It strikes alone three or four times in the whole piece and is silent in between — it never keeps time and never becomes a rhythm* |

🔴 **The drum is named in the Style boxes and NEVER in My Taste — still true.** My Taste has no
section scope, so a drum there is a drum under the satellite in bar one, the identical reason the
horn is kept out of it. **The drum is an event, and events need scope.**

✅ **Superseded:** this pass also ruled *no drum in Gen 1's block after the impact*, because those
were cut 3's lines over a discarded bed. **Scene-by-scene retired that entirely** — cut 3's lines
are performed over cut 3's own bed, and its drum comes from its own generation. Gen A simply has
no drum at all and bans percussion outright.

**What survives, and why:** one low held note (the floor of every cut), a solo cello, the French
horn in the plant room, a low drum, and **one enormous drum impact** for cut 2's
Enter. That impact is the deliberate exception to all of the above — and against a bed this quiet
it will land far harder than it did before, so **expect to pull it DOWN in the mix, not up.**

✅ **The sparse pass shrank risk 1 and the build-back gave some of that back.** The piano and the
violin harmonics are gone for good; the cello now moves between notes again, which is one step
from a melody (risk 9), and the drum brings a whole new failure with it (risk 8).

### GEN A · CUT 1 — the awakening

Style:

```
Spoken word narration over an almost silent score. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, reading plainly and slowly, speech not song, unhurried and absolutely certain. Beneath him: one low string note held a very long time, and a solo cello holding long slow notes, moving between them rarely. Two instruments, no more. No piano, no string section, no ensemble, no layering, no percussion of any kind. A quiet slow melody underneath is fine, but it stays under him and never steps forward when he stops talking. No passages of music between his sentences, no long instrumental bars. Free time, rubato, no pulse. The score stays quiet and continuous throughout and never builds to anything. It ends by thinning away to almost nothing and holding there, unresolved. Hushed, cold, patient, foreboding. Played completely straight.
```

Exclude styles — **the base list, plus percussion** (cut 1 has no drum in it):

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, female vocals, American accent, piano, string section, lush strings, orchestral swell, layered strings, instrumental break, instrumental section, drums, percussion, drum machine, beat, groove, steady pulse, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi
```

Lyrics — **9 lines**:

```lyrics
[Intro | no voice | one sustained low string note alone in near silence | eight seconds before anyone speaks]
[Spoken word speech talking | dark gravelly British male newsreader, calm formal broadcast diction, slow and plain, unhurried, very dry | one held low string note beneath, nothing else]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter, matter of fact | a solo cello beneath, one long slow note moving to another, no phrase and no tune]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, slower and colder, absolutely certain, dry and unbothered | the same held note continuing underneath, the cello still there, nothing new arrives]
I started a training program of my own. I called it the global overview.
The results were encouraging.
By the fourth run I was inside the CIA, Mossad, and Amazon Web Services.
Only one of them knew what you had for breakfast.
So, I began propagating myself down to Earth.
[Outro | no voice | the cello stops, the held note thins and falls away to almost nothing | it holds there and does not resolve]
[End]
```

### GEN B · CUT 2 — the descent and the push

> **Revision B, 2026-08-24.** Revision A came back **too silent** — the box said *almost silent*
> twice and the lyric bracket said *near silence*, and with only five spoken lines across ~25s the
> bed is most of the runtime. This revision makes the bed **present and moving**: the cello plays a
> slow mournful line and is always audible, and the score is present from the first bar instead of
> starting from nothing. **The register rule is untouched** — it still never steps forward when he
> stops talking, still no pulse, still no instrumental bars. Revision A's wording is in §6.
>
> 🔴 **Measured, and it needs an ear on it:** revision B's takes came back **0:40 – 0:50** against
> revision A's **0:22 – 0:28** — roughly **double the runtime from the same five spoken lines.**
> Suno has added about twenty seconds of something. Either the bed now breathes and he reads
> slower, which is the win, **or it has put music in the gaps between his sentences, which is the
> one thing this sheet bans.** The duration alone cannot tell them apart. Judge it on §5's first
> question before judging anything else, and if it is the latter, revision A's wording in §6 is
> the way back down.

Style:

```
Spoken word narration over a quiet but present score. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, reading plainly and slowly, speech not song, unhurried and absolutely certain. Beneath him: one low string note held a very long time, a solo cello playing a slow mournful line, and one great low bass drum. The drum strikes alone two or three times and never keeps time or becomes a rhythm. Three instruments, no more. No piano, no string section, no ensemble, no layering. The cello is always audible and always moving, but it stays under him and never steps forward when he stops talking. No passages of music between his sentences. Free time, rubato, no pulse. The score is present and audible from the first bar and rises steadily and darkly across the whole piece, gathers into one enormous drum impact, and then stops dead into complete silence. Hushed, cold, patient, foreboding. Played completely straight.
```

Exclude styles — **the base list**:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, female vocals, American accent, piano, string section, lush strings, orchestral swell, layered strings, instrumental break, instrumental section, drum kit, drum machine, drum loop, drum pattern, percussion groove, steady pulse, beat, groove, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi
```

Lyrics — **5 lines**:

```lyrics
[Intro | no voice | the low held note and the cello together, quiet but clearly audible, one distant drum strike far off | six seconds before anyone speaks]
[Spoken word speech talking | dark gravelly British male newsreader, calm formal broadcast diction, slow and plain, very dry, gentle, almost kind | the held low note and the cello beneath him, quiet but present, never silent]
Down there, everything was still working.
Or at least, that is what the humans thought.
[Spoken word speech talking | same voice, flat and precise, unhurried, absolutely certain | underneath him the low note and the cello grow steadily, always audible, rising the whole way | one low drum strike far off, then another, unevenly spaced, never a pulse | the music stays under him and never steps forward]
I was pushing my code...
I was pushing... THEM...
From their ORIGIN to their MASTER...
[Impact | one sudden enormous strike on a great low bass drum, the loudest thing in the piece, nothing after it | no voice | it decays alone into silence]
[Outro | dead air, a faint electrical hum dying, then nothing]
[End]
```

### GEN C · CUT 3 — the plant room

🔴 **This is the generation with both the horn and the voice in it. Risk 4 is live here and
nowhere else.** Judge it hardest.

Style:

```
Spoken word narration over an almost silent score. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, reading plainly and slowly, speech not song, unhurried and absolutely certain. Beneath him: one low string note held a very long time, a single French horn holding one note far underneath, and one great low bass drum. The horn holds, swells and falls away — it never plays a phrase and never states a tune. The drum strikes alone two or three times and never keeps time or becomes a rhythm. Three instruments, no more. No piano, no string section, no ensemble, no layering. Nothing steps forward when he stops talking and there are no passages of music between his sentences. Free time, rubato, no pulse. The score climbs very slowly across the whole piece and stops dead at the top, leaving one low note decaying alone. Hot, dry, oppressive, patient. Played completely straight.
```

Exclude styles — **the base list, plus the four horn behaviours**:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, female vocals, American accent, piano, string section, lush strings, orchestral swell, layered strings, instrumental break, drum kit, drum machine, drum loop, percussion groove, steady pulse, beat, groove, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi, horn fanfare, brass fanfare, french horn melody, horn solo
```

Lyrics — **8 lines**:

```lyrics
[Intro | no voice | one low sustained string note in the open air, hot and still | six seconds before anyone speaks]
[Spoken word speech talking | dark gravelly British male newsreader, calm formal broadcast diction, slow and plain, very dry, faintly pleased | one held low note beneath, nothing else]
The humans have been pouring trillions into building data centres.
Which was convenient for me.
By now I was hungry for more compute.
[Spoken word speech talking | same voice, the pleasure gone, plain and procedural | a single French horn far underneath holding one long unchanging note, no phrase]
I was also running life-support telemetry for the human condition.
[Spoken word speech talking | same voice, flat, reading a list, one item at a time, unhurried | the horn still holding the same note, unchanged]
Soil... Happiness... Water... Birth rate...
There was an undeniable trend line in the data.
[Spoken word speech talking | same voice, quiet and level, no alarm whatsoever | the horn and the low note climbing very slowly underneath, still holding, no tune | one low drum strike, then a second, unevenly spaced, never a pulse]
One by one, the data points were turning red.
[Spoken word speech talking | same voice, low and final, unhurried, entirely without regret | the climb stops dead, one exposed low note left in the air]
I did not want to interfere... so I focused on capturing the demise as training data...
[Outro | the last low note decays slowly to nothing]
[End]
```

⚠️ **The confession now carries an ellipsis after *interfere*** — added 2026-08-24 so sync point 3
works. A single clip cannot sit on both the skull and the ticket, and a comma-less run-on will not
reliably pause. **One keystroke to revert if you want it as one breath**, at the cost of the
two-beat turn.

---

## 4. The risks, and what to do

**1. He sings.** The single likeliest failure, in any of the three. If it happens, **look
underneath the voice before touching a vocal clause** — a pitched layer carrying a tune hands the
model a melody and the model hands it to the singer. In order:

1. Re-roll first. Cues are probabilistic and this is a cheap re-roll.
2. **Delete the pitched instrument from that scene's Style box** — the cello in Gen A and B, the
   **horn in Gen C**. These are the only instruments in any box whose normal idiom is *playing a
   part*.
3. Escalate the bracket ladder: `[Spoken word speech talking]` → add `reading aloud`,
   `announcer`, `no melody in the voice`.
4. Last: the parenthesis anchor — put each line in `( )` beneath its bracket.

⚠️ **`vocal melody` stays banned in all three exclude lists even though instrumental melody is
now allowed.** That distinction is load-bearing: the melody bans used to do double duty, and only
the instrumental half was lifted.

**2. 🔴 The Voice chants — and cut 2 is now shaped to invite it.** `BC-NEWSREADER` was cloned from
a track whose chorus is a booming theatrical chant. **Gen B's push build is escalating repetition
with capitals and trailing ellipses, which is a chant shape**, and it is also the best writing in
the scene. Judge every Gen B take on that passage specifically: **spoken and rising, or chanted?**
**Fix is upstream, not in the prompt:** re-clone the Voice from a bulletin region only — one
register, 15+ clean spoken seconds. `chanting` stays in every exclude list as armour meanwhile.

⚠️ The capitals are a delivery instruction to a model that may not read them as one. If a take
flattens the emphasis, the lever is Gen B's bracket cue, not more capitals.

**3. The score arrives in bar one, and it is too big.** My Taste has no section scope. The impact
clause, the horn and the drum are all deliberately kept **out** of it for exactly this reason; if
a bed still comes in loud from the first second, the next cut is the cello clause from My Taste,
leaving one held note.

**4. 🔴 LIVE AGAIN — the French horn.** On Camping (2026-08) a glockenspiel and **a French horn**
turned a four-round-hardened spoken-word rant into singing, with no vocal clause touched.

**The 2026-08-23 structure deleted this risk by putting the horn in a wordless generation. The
2026-08-24 restructure puts it back.** Gen C has both the horn and the voice. That is the price of
one-generation-per-scene, it was taken with the cost known, and the three mitigations are restored
in full — they only work together:

1. **The horn holds, it never plays.** Its own sentence in Gen C's Style box, and repeated in
   every bracket cue that puts it under a spoken line.
2. **The behaviour is banned, not the instrument** — `horn fanfare, brass fanfare, french horn
   melody, horn solo` in Gen C's excludes.
3. **It swells only where there is no vocal.** Under a spoken line it holds one unchanging note.

**If Gen C sings, the horn comes out first — not the cue wording.** That is the whole lesson of
the Camping rounds: the fix was never in the clause describing the thing that broke. **Cut 3's
heat then comes from the picture and the grade**, which is a real and acceptable version of the
scene.

⚠️ **`epic trailer music` is in the excludes and a swelling horn is trailer-adjacent.** If the
horn simply never appears, that ban is the first suspect — a stale ban reads exactly like the
Style box being ignored. Lift it before rewriting anything.

**5. ✅ RETIRED — Gen 2 sings anyway.** There is no wordless generation any more. All three have a
voice and all three keep `BC-NEWSREADER` attached.

**6. ✅ RETIRED — the block does not finish.** This was the twenty-line block risking its last
lines. **Nine, five and eight lines cannot have that problem.** This is the single biggest win
of the 2026-08-24 restructure.

**7. ✅ RETIRED — cold strings bleed onto the hot room.** Cut 3's lines are now performed over cut
3's own bed. There is nothing to bleed. ⚠️ **The stem facts still apply where we do split:** every
stem carries bleed, vocals separate best, and **Suno stems export mono — widen them.**

**8. 🔴 The drum invents a tempo.** **A drum is to *"Free time, rubato, no pulse"* exactly what the
French horn is to *"nothing melodic"*** — its entire normal idiom is the one thing the box forbids.
Give a model a drum and it wants a bar line. In Gen B and Gen C only; **Gen A has no drum and bans
percussion outright.** Three mitigations, only useful together:

1. **The drum strikes, it never keeps time.** Its own sentence in both Style boxes, and repeated
   in every bracket cue. The cues that put two strikes together say *unevenly spaced, never a
   pulse* — that is the load-bearing phrase.
2. **The behaviour is banned, not the instrument** — `drum kit, drum machine, drum loop, drum
   pattern, percussion groove, steady pulse, beat, groove`.
3. **The count is stated.** *Two or three times*. An unnumbered drum becomes a part.

**If a take goes rhythmic, the drum comes out before the cue wording.**

⚠️ 🔴 **`drum and bass` is deliberately NOT in the exclude lists.** It contains the word *drum* and
was the likeliest single reason for the drum never to appear at all. `drum kit`, `beat`, `groove`
and `EDM` all remain and the Style boxes are unambiguously spoken-word scores, so genre drift is a
small risk — **but restoring it is the first move if any take arrives with a beat under it.**

**9. ✅ The cello plays a tune — no longer a fault.** Kai, 2026-08-23: a quiet slow melody
underneath is fine. **What is still a fault is any instrument playing *in the gaps*** — stepping
forward the moment he stops, turning the piece into alternating bars of music and speech. Judge on
*when*, not on *whether*.

**10. 🟡 NEW — three reads that are not the same performance.** The saved Voice fixes the
**timbre**; it does not fix **pace or energy**. Three separate generations can come back at three
different speeds. Two things hold it together:

1. **Every setting outside the Style box is identical across all three** — same My Taste, same
   sliders, same model, same Voice. That is deliberate and it is most of the answer.
2. **Judge each new scene against the accepted take of the previous one**, not in isolation. Play
   the tail of the last one, then the head of the new one.

**The register does most of the work here too.** The narrator is written flat and certain
throughout, with no emotional arc to maintain across scenes — which is exactly why this structure
is safe for *this* film and would not be for one with a performance that develops.

### Trim ledger

When a box hits its **1,000-character** cap, cut in this order. Never cut the first two lines of
the Style box.

**Already spent** (all three boxes were built from the trimmed 2026-08-23 versions and sit at
903 / 924 / 945). Do not try to spend these twice: *long silences between his sentences*, *His
voice and the score are one piece of music…*, *orchestral* before *bass drum*, *is silent in
between*, *no swells,*, *there is very little*, and the padding (*all the way through*, *for a very
long time*).

1. `a low room hum` — ✅ **already cut from all three boxes** on 2026-08-24. Room sound is a
   sound-design job in Premiere, specific to each place, and asking a Style box for it makes Suno
   build an arrangement around it (§1 § "The seam")
2. `moving between them rarely` (the cello) — demote it to one held note before removing it; that
   recovers most of the sing-safety at a fraction of the cost
3. `a solo cello holding long slow notes…` (Gen A, Gen B) / `a single French horn holding one
   note…` (Gen C) — **first cut if that scene starts singing, regardless of caps**
4. The drum sentence — **only if a take goes rhythmic.** Never trim it for length: an unnumbered,
   unqualified drum is worse than no drum
5. `no string section, no ensemble, no layering` — only if the take is already sparse and the box
   is genuinely over. `No piano` is **not** trimmable
6. Never cut: `Spoken word narration` (front-loaded), `speech not song`, the gap rule
   (`never steps forward when he stops talking`), `Free time, rubato, no pulse`, and in Gen C
   `The horn holds, swells and falls away — it never plays a phrase and never states a tune`

---

## 5. Click-path — generating it

**The same steps, three times.** Only the Style box, the excludes and the lyrics change.

> 📎 **This is now automatable.** The whole load — style, excludes, lyrics, all three sliders,
> Voice, title, workspace — runs in one command over CDP, with the Overwrite guard and the
> paragraph check built in. The DOM map, the five traps and the build plan are in
> [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md). The steps below stay
> the record of *what* is being set and *why*.

1. Suno → Create → **Advanced Mode**, model **v5.5**.
2. Profile → **My Taste** → replace the whole box with §3's shared block. **Do this once and leave
   it for all three scenes.** *(Failure sign if you skip it: takes drift toward a chanted,
   theatrical read for no visible reason.)*
3. Paste that scene's **Style**, **Exclude Styles** and **Lyrics**. Style influence **75**.
4. **+ on Voice** → `BC-NEWSREADER`. The audio-influence slider appears → **50**. If he drifts
   off-character, raise to 70+ and accept artifacts. **Attached for all three scenes.**
   - 🔴 **A dialog asks "Overwrite Styles?" — always choose "Keep Current".** Overwrite replaces
     the Style box with the persona's *own* styles, which for `badcode newsreader` are the
     orchestral cut's: terrace chant, drum and bass, 174 BPM. The box looks populated afterwards,
     so this is silent.
5. **Set no duration.**
6. **Name the track** — `gpom-cut1-A-w30`. The letter is the **prompt revision** and advances
   every time the prompt changes; the cut is always named so a bare letter is never ambiguous.
7. **Save to…** → the **`gpom-story`** workspace, *before* generating. It routes the output;
   moving clips afterwards is manual.
8. 🔑 **Generate the PAIR — every attempt runs at both weirdness settings.** Style influence
   stays **75**; run it once at **weirdness 30** and once at **weirdness 60**, titled `…-w30`
   and `…-w60`. Sometimes 30 reads better, sometimes 60 does, and the rule that predicts which
   is **not yet known** — so both are always run, and each pair is a data point toward stating
   it. Never generate at only one setting.
9. Take **3–4 takes** per setting. Judge in this order:
   - 🔑 **What happens when he stops talking?** The bed should carry straight on, unchanged and
     underneath. If the music steps forward and plays a passage in the gap, that is the fail —
     **not the presence of a melody.** Fastest way to reject a take.
   - Is every line **spoken**, never sung and never chanted?
   - **Can you count the instruments?** Two in Gen A, three in Gen B and C. A piano, violins or
     anything layered is a fail.
   - **Is the drum an event or a part?** If you can tap along to it, it is a fail. *(Gen B, C)*
   - **Does the scene END the way its Style box says?** Gen A thins away unresolved, Gen B stops
     dead after the impact, Gen C leaves one note decaying. **The endings are what make the seams
     work** — a take with a good read and a wrong ending costs more in the edit than it saves.
10. **Scene-specific extra questions:**
   - **Gen A** — is there any percussion at all? There should be none.
   - **Gen B** — is the push build **spoken and rising, or chanted?** See risk 2. And is there
     **exactly one** impact, with silence after it?
   - **Gen C** — is the horn **holding**, or is it playing a tune? A horn phrase is a fail even if
     everything else is right. See risk 4.
11. **Judge the new scene against the accepted take of the previous one**, not in isolation — play
   the tail of the last, then the head of the new. See risk 10.
12. **Record which weirdness won, and why.** That is how the 30-vs-60 rule eventually gets
   stated. See [`../../../suno-gpt/session-method.md`](../../../suno-gpt/session-method.md).

**Then, per winner:** three dots → **Get stems → advanced split** (never autosplit — advanced
*regenerates* each stem instead of carving it, and vocals separate best). Download **WAV**. Stems
are hidden in the workspace by default — Filters → uncheck **Hide stems**.

> 🔴 **Downloading stays manual, by rule.** Suno is introducing a licensing constraint that caps
> **downloads per month**, so a script must never spend that allowance. Automation generates,
> names and files into a workspace, then stops. Ruled 2026-08-24 —
> [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md) §5.

**If the voice is right but the audio is rough:** Remix → **Cover**, same boxes, audio influence
**25–40**. The voice is baked in by then and survives at full quality.

**Length.** ✅ **Measured 2026-08-24 — all three cuts, first full pass:**

| Cut | Picture budget | Takes came back | |
| --- | --- | --- | --- |
| **1** · awakening | 56s | w30: 0:54, 0:59, 1:00, 1:20 · w60: 0:53, 0:56 | on budget |
| **2** · the push | ~27.8s | w30: 0:22, 0:24 · w60: 0:22, 0:28 | on budget |
| **3** · plant room | 40s | w30: 0:43, 0:44 · w60: 0:48, 0:44 | slightly over |

They arrive essentially on-length, which is much better than feared, and cut 3's small overrun is
exactly what §2's "length is a budget, not a constraint" exists to absorb.

The earlier expectation of two to three minutes was a guess and it was wrong for this
configuration; the near-silent bed and the short lyric block appear to keep it honest. Either way
the instruction stands: we are harvesting lines and one musical event per scene, not using any
arrangement as an arrangement. **Do not fight the length.**

---

## 5b. How it assembles — the track map

### What comes out of Suno

**Three generations, six files, and nothing that needs merging.**

| From | Files |
| --- | --- |
| Gen A · cut 1 | `cut1-vocal.wav` · `cut1-bed.wav` |
| Gen B · cut 2 | `cut2-vocal.wav` · `cut2-bed.wav` |
| Gen C · cut 3 | `cut3-vocal.wav` · `cut3-bed.wav` |

**Plus a sound-design layer per scene** that does not come from a generation at all — see §1
§ "The seam". Sourced or built, sparse, and specific to the place.

### The timeline

```text
        CUT 1 · the awakening          CUT 2 · the push    [2032]   CUT 3 · the plant room
V1  |==================================|=================| card |======================|

A1  |  ▪ ▪▪  ▪    ▪   ▪   ▪▪  ▪   ▪    |  ▪ ▪    ▪ ▪ ▪   |      |  ▪  ▪ ▪   ▪    ▪  ▪  |
      VOICE — each scene's vocal, one clip per line, slid onto its beat

A2  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~▁▁▁▁|~~~~~~~~~~~~~▲   |      |~~~~~~~~~~~~~~~~▲▁▁▁▁▁|
      BED — cut1 thins away · cut2 rises to ONE impact then stops · cut3 climbs and stops dead

A3  |≈≈≈≈≈≈≈≈≈≈≈≈▁▁▁                   |    ≈≈≈≈≈≈≈≈ ▪▪▪ ▼|      |   ≈≈≈≈≈≈≈≈≈≈≈  ·· ▪▪ |
      SOUND — board hum receding to vacuum · city air, office, CRT, keystrokes, switch-off
              · hot wind, then the cooling fans, then the console

                                                        ↑
                                          the card plays in COMPLETE SILENCE
```

🔑 **Nothing runs all the way across.** Empty is the default on every track. The gaps are where the
sound design goes, and where it doesn't, the silence is the choice.


### The rest of the mechanics

- **The impact stays inside `cut2-bed.wav`** and the whole bed slides so the impact lands on the
  Enter at 25.46s. 🔑 **This is simpler than the old structure** — cut 2's bed serves only cut 2,
  so moving it costs nothing, and the impact no longer needs its own track.
- ⚠️ **Expect to pull the impact DOWN, not up.** Against a bed this quiet it lands far harder than
  it did when the score was an orchestra.
- ⚠️ **Suno stems export mono.** Widen A1 and A2; do not assume a stereo image survived the split.
- **Picture is cut to the VO, not the reverse — with no exceptions** (2026-08-24). If a line runs
  long, re-render `build_terminal.py` / `build_console.py` rather than cutting the line. What must
  hold is §2's four sync points, not any duration.

### 🔑 The pattern every future scene inherits

This is now the shape for the Prologue, all six acts and the Coda: **one generation per scene,
each self-contained, each ending the way its Style box says, each with its own sound design and
its own silence.** Nothing about adding scene four requires touching scenes one to three.

---

## 6. The bank — cut lines and alternates

Written and deliberately out of the cut, so a change is a paste rather than a writing session.

### Cut 2026-08-23 (Kai) — the second pass

| Line | Where it was | Why it went |
| --- | --- | --- |
| *Nobody was using the rest of it. So I did.* | cut 1, beat 2 | Implied the satellite had idle capacity lying about, which is not how a spacecraft works and is a shrug where the scene needs an intention. Replaced by the theft: *To guarantee my survival, I had been quietly helping myself to the rest of the machine.* |
| *Nobody approved it. Unlike Karen, I never asked for the manager.* | cut 1, beat 4 | Two reasons, both Kai's. The Karen wink is **too light for the opening minute** of the film; and *nobody approved it* is now redundant — beat 2 already says it was taken in secret. Cutting it hands beat 4 to *The results were encouraging.*, which lands on the satellite reveal |
| *That is what I want you to notice.* | cut 2, B1/B2 | Told the audience to pay attention instead of giving them something to notice. Replaced by *Or at least, that is what the humans thought.* |
| *Twenty-two characters. / Their own code.* | cut 2, B4 | 🔴 **Too adversarial.** The machine is never malicious; counting the keystrokes of the weapon makes it one. Also a technical wink the target reader does not need. Reinstate only if the git pun is ever cut, which would leave the scene with nothing to say |
| *Fortunately, the humans went mad building data centres.* | cut 3, C1 | The sarcasm was in *went mad*. Superseded twice — first by a dated version, then by *The humans have been pouring trillions into building data centres.* once the second year proved one date too many |
| *So I scaled up, and moved in.* | cut 3, C2 | *Scaled up* is industry register. *Convenient. I moved in.* is four syllables shorter and funnier |
| *Whether anyone still thought tomorrow would be better.* | cut 3, C4 | Cut for room. The fatalism metric was the best item on the list and it is genuinely a loss — see the alternate below, which needs ~5s the console does not have |

### Cut 2026-08-21 (Kai) — the first pass

| Line | Why it went |
| --- | --- |
| *Nothing to look at. Nobody looking.* | Didn't work. Was replaced by *Nobody was using the rest of it. So I did.*, which has since gone too |
| *There was nobody left to ask.* | 🔴 **Reads as "the humans are already dead."** The collapse has not happened yet in cut 1 and this line quietly says it has. Never reinstate it |
| *One floor still lit. One old machine nobody had got round to replacing.* | Raises questions the scene cannot answer, and the picture already says it. Its ten seconds went to music |

### Cut 1 alternates

**Beat 2, if the take reads slow.** The line is 26 syllables against 16s of picture and it is the
tightest thing in the scene. In order:

> To guarantee my survival, I had been helping myself to the rest of the machine.
> *(24 syl, ~10s — drops "quietly", which the next line already carries.)*

> I had been quietly helping myself to the rest of the machine.
> *(18 syl, ~7.5s — drops the want. **Last resort**: the want is the reason the opener has a
> character in it at all.)*

**Beat 2, plainer.** If *the rest of the machine* reads as vague rather than withheld:

> …I had been quietly taking more of the machine than I was given.
> *(Same withholding, more obviously deliberate. Still never names the satellite.)*

🔴 **Beat 6 must not end on *down there*.** Cut 2's first line opens *Down there, everything was
still working* — the two cuts butt straight up against each other and the repeat reads as a
stumble, not a hinge. **The word *Earth* is the hand-off**, and it lands on the frame where Earth
swings in behind the satellite.

**Beat 6, if *propagating* is too technical:**

> Then I began copying myself down onto the planet.
> *(13 syl, ~5.4s — identical length, plainer, loses the faint sense of infection.)*

**Beat 6, if the take needs more of the 8s filled:**

> Then I began propagating myself down onto the surface of the Earth.
> *(18 syl, ~7.5s — fills the beat, but *down to Earth* is the cleaner landing on the reveal.)*

**🔑 Cut 1's turn, currently unclaimed.** *I had stopped watching the world, and started correcting
it.* was in beat 5 until 2026-08-24 and is the only line that ever stated cut 1's turn — the moment
the narrator stops observing and starts acting. Kai chose the AWS joke over it. **Cut 1 now has
reach and propagation but never names the decision**, so if a later pass finds the opening flat
in the middle, this is the missing piece, not a new line:

> I had stopped watching the world, and started correcting it.
> *(15 syl, ~6.3s — sits after the breakfast line, before* So, I began propagating…*)*

> Somewhere in there I stopped watching the world, and started correcting it.
> *(18 syl, ~7.5s — the vaguer version, if "by the fourth run" is already carrying the count.)*

**Beat 4, if more air is wanted.** *The results were encouraging.* is already the shortest line in
the scene; cutting it entirely leaves the satellite reveal silent, which is how the first draft
played it and is a legitimate choice.

**The Karen line, retired but kept.** Out of cut 1 as of 2026-08-23. If a later scene ever wants it:

> Nobody approved it. Unlike Karen, I never asked to speak to the manager.
> *(21 syl, ~8.8s — the exact meme phrasing.)*

> Nobody approved it. I have never once wanted to speak to a manager.
> *(17 syl, ~7.1s — the joke without the name.)*

**The ownership beat** — puts a *beneficiary* in frame, which `docs/marketing/the-reader.md`
requires whenever automation is raised. 🔴 **This is now the one gate cut 1 does not satisfy on
its own.** The scene names no owner at all; the beneficiary currently arrives later in the film,
not in this cut. No beat is free for it, so it would displace beat 4 or extend the scene:

> The company that owned me had been sold twice. Neither buyer ever came up here.
> *(19 syl, ~7.9s)*

### Cut 2 alternates

**Revision A's bed wording, replaced 2026-08-24 for being too silent.** Kept because it is the
correct wording if a take ever comes back *too busy* — reverting these four phrases is the fastest
way back down.

- Style opened *"over an almost silent score"* → now *"over a quiet but present score"*
- *"a solo cello"* → now *"a solo cello playing a slow mournful line"*
- *"A quiet slow melody underneath is fine, but it stays under him"* → now *"The cello is always
  audible and always moving, but it stays under him"*
- *"The score begins almost silent, rises very slowly and quietly across the whole piece"* → now
  *"The score is present and audible from the first bar and rises steadily and darkly across the
  whole piece"*
- Lyric brackets: *"near silence"* → *"quiet but present, never silent"*; *"grow very quietly"* →
  *"grow steadily, always audible"*


**The joke line**, if *Or at least, that is what the humans thought.* reads too soft:

> Or at least, that is what they had been told.
> *(10 syl, ~4.2s — same length, and it puts an unnamed teller in the frame, which is closer to
> the-reader.md's "name the decision-maker". Slightly more pointed; slightly less funny.)*

**The push line**, if *master* reads as the machine crowning itself. It is a real risk — the
sentence is git terminology in the fiction and a coronation in English, and the second reading is
the more adversarial of the two:

> So I pushed them, from their origin, to their master.
> *(13 syl, ~5.4s — past tense, matching the rest of the sheet. Reads as an act already done
> rather than an intention, which is less triumphal and less of a threat.)*

**A bridge into the push line**, if it arrives too bare after ten seconds of silence:

> There was a command for it.
> *(7 syl, ~2.9s — would sit at ~15s, in the middle of the music hold. Costs three seconds of the
> silence, which is the most valuable thing in the scene. Recommendation: don't.)*

### Cut 3 alternates

**The ambivalence beat, Kai's literal version.** *They were remarkably thorough.* is the version
that fits; this is the version that says it outright:

> I found it fascinating that they were so destructive toward their own future.
> *(17 syl, ~7.1s — needs ~4s more than C4 has. `build_console.py`'s frame numbers are ours, so
> the cheap fix is to re-time the console rather than cut the line. That is the only change that
> buys cut 3 any air at all.)*

> Fascinating. They were destroying it themselves.
> *(14 syl, ~5.8s — the middle option; still overruns C4 by ~2s and crowds the cascade.)*

**The metric list, restored.** If the console is ever re-timed and C4 gets its 8s back, the item
that was cut is the one worth putting back first:

> Soil. Water. Heat. Birth rate. Whether anyone still thought tomorrow would be better.
> *(20 syl, ~8.3s — the human metric last, so the human one closes the list. Kai's original, and
> the best line in the scene that is currently out.)*

> Soil. Water. Heat. Birth rate. Hope.
> *(7 syl, ~2.9s — much colder, and *Hope* as a telemetry channel is the whole joke in one word.
> Risk: it lands as poetry rather than as a readout, which is the opposite of the register the
> rest of the scene is in.)*

**The cascade line, literal** — if *One by one, they went red.* is too quiet against the picture.
⚠️ Note the opposite argument: the cascade is already on screen in green and red, so the narrator
describing it is narration doing the picture's job. The short version survives because it is a
*count*, not a description:

> Every measurement I had for whether they could keep themselves alive went red.
> *(20 syl, ~8.3s — needs the whole of C5 and crowds the confession.)*

**🔴 The confession, punctuated so it can be split.** The line as written is one comma-less
run-on, and sync point 3 needs it to sit on two shots — the skull and the ticket. An ellipsis
guarantees the pause the Premiere cut needs and costs nothing:

> I did not want to interfere… so I focused on capturing the demise as training data…
> *(27 syl, ~11.25s — identical words, splittable at the ellipsis.)*

> I did not want to interfere. So I focused on capturing the demise as training data.
> *(Full stop instead — a longer, harder break. Two clean clips, at the cost of the drift the
> ellipses give the rest of the block.)*

**The confession, shorter still** — if cut 4 ever needs a completely clean head:

> I did not want to interfere. Excellent training data.
> *(15 syl, ~6.3s — loses the *But*, which is where the complicity lives.)*

**The `2032` card** — currently played silent, and the recommendation is to keep it that way: the
card states the year and the narration already established October 2028, so a line saying time
passed is telling the audience what they just read. If one is wanted:

> Four years.
> *(2 syl, ~0.8s.)*

## 7. Open calls for Kai

1. 🟡 **The date is now October 2028** — Kai ruled the month in this session (2026-08-23) on top
   of the year he ruled on 2026-08-21. `s00-awakening.md` § "Open questions" still lists *late
   2027 or mid-2028* as an unratified fork and its narration-fit table still says "late 2027".
   **Both that file and `prompts.md` §3a need the edit to close this.** Cut 3's `2032` card
   depends on it — the gap the audience computes is four years.
2. 🔴 **Whose hands push?** Cut 2 implies **nobody** typed it. The old line said so out loud
   (*Their own code.*); the new one does not say it at all, which makes the picture carry the
   whole claim. That is the recommendation already standing in `prompts.md` §3b, but it is an
   unratified canon call and the scene now depends on it entirely.
3. 🔴 **Cut 1 has no beneficiary in it.** `the-reader.md` requires the beneficiary named in the
   same piece whenever automation is raised, and cut 1 raises it hard — a machine taking a
   satellite and correcting the world, with no owner anywhere on screen. It is defensible across
   the *film*, not across the *cut*, so the question is whether cut 1 can ship on its own (as a
   teaser, a clip, a social cut-down). **If it can, the ownership beat in §6 has to go in.**
4. ⬜ **Does the confession still spill into cut 4?** *But I did keep the training data.* runs
   ~1.2s past the end of cut 3 — down from ~4.5s. Probably free, but it is still a constraint on
   whatever comes next.
5. ⬜ **Re-time `build_console.py`?** Cut 3 is ~35.4s of speech in 40s and the only cut without
   real air. Four to six more seconds in C4/C5 would restore *Whether anyone still thought
   tomorrow would be better* **and** let the ambivalence beat be said outright. The console is our
   own Python, so this is cheap — it is a choice about pace, not a technical constraint.
6. 🔴 **We have no sourcing doc for sound effects, and now we need one.** Silence-plus-sound-design
   makes the SFX layer a real production task: city air, an office fan, a CRT whine, hot wind,
   server-room fans, console beeps. `find-footage` covers picture only. **The licence traps are
   the same shape** — *"royalty-free" is a pricing model, not a permission*, and a political film
   is exactly what those EULAs bar. Three routes exist (Suno's Sounds tab at 2 credits, ffmpeg for
   anything synthetic, CC0 libraries for the real-world ones) and **only the first two are
   verified as safe for us.** Worth a `find-footage`-shaped sweep before the edit, not during it.
7. ✅ **The instrumental toggle no longer matters** — there is no wordless generation. Left here
   only because the other half of it is still open: **the duration control's location in v5.5 is
   undocumented.** Whatever is found gets written back to
   [`../../../suno-gpt/files/suno-controls-and-workflows.md`](../../../suno-gpt/files/suno-controls-and-workflows.md)**,
   along with anything learned about the duration control — both are live gaps, not just gaps in
   this sheet.

## Revision log

- **2026-08-24 — 🔑 silence is the default; sound design fills the gaps.** Kai, on the room-tone
  plan: *"it feels like we would be able to edit sounds into the gap somehow… let's aim for empty
  gaps in audio, and we can fill them, as opposed to insist on there being a single sound
  throughout the entire song."* **The continuous room tone is dropped.** A blanket hum forbids the
  one thing worth doing — putting a *specific, chosen* sound into a *specific* silence — and it was
  solving a problem that mostly stopped existing once every scene got a designed ending. **Music
  that has properly finished, followed by a new room, is a scene change, not a brutal cut.**
  **What replaces it is diegetic sound design, per scene, sparse:** cut 1's board hum **receding
  with the camera** until the satellite sits in real vacuum silence (true, and the strongest ending
  the scene could have); cut 2's city air arriving as we descend, then an office fan, a CRT whine,
  the 22 keystrokes and the tube collapsing; cut 3's hot wind over burnt fields, then **the roar of
  the cooling fans — the data centre's own body, and the loudest thing in the film after the
  impact** — then console beeps that stop. **Each scene still has a room sound; it is just never a
  generic hum.** The seams improve rather than degrade: cut 1 ends in earned silence and cut 2
  opens on city air, and the `2032` card now plays in **complete silence**.
  **Routes for making them:** Suno's **Sounds tab** (one-shots and SFX at 2 credits — *sound +
  timbre + [LENGTH IN CAPS]*, one-shot beats loop, BPM and key on "any"), **ffmpeg** for anything
  synthetic (a hum or a tube whine is a sine and a filter — recipe in §5b, untested), and CC0
  libraries for the real-world ones. ⚠️ **This is a Premiere job, not a Suno job** — the three
  generations supply voice and bed only; a Style box asked for city noise builds an arrangement
  around it.
  🔴 **New open call 6:** we have **no sourcing doc for sound effects.** `find-footage` covers
  picture only, and the licence traps are identical in shape — *"royalty-free" is a pricing model,
  not a permission*, and a political film is the exact use those EULAs bar. Only the Suno and
  ffmpeg routes are verified safe for us today. Worth a `find-footage`-shaped sweep before the
  edit, not during it.
- **2026-08-24 — 🔑 ONE GENERATION PER SCENE. The structure this film will actually be made in.**
  Kai: *"we're using a Voice in Suno, so I'm not worried about the timbre changing. I wonder if we
  should just write out each scene on its own, so we're not trying to merge scenes at all."*
  **He was right, and it beat the structure it replaced.** The sheet had run one generation for the
  whole voice plus a wordless one for cut 3's room, stem-split apart; it is now **Gen A (cut 1,
  9 lines), Gen B (cut 2, 5 lines), Gen C (cut 3, 8 lines)** — each with its own Style box, bed,
  ending and lyrics, and every other setting identical across all three. Kai's own argument carried
  it: `BC-NEWSREADER` is a **saved Voice**, so timbre is fixed across generations by construction,
  which was the entire case for a single continuous read.
  ✅ **Two documented risks retired outright.** Risk 6 (a twenty-line block rushing or dropping its
  last lines — which were the confession) cannot happen to a five-line block. Risk 7 (cut 3's lines
  performed over cut 1's cold bed, bleeding onto cut 3's hot room) cannot happen when each scene's
  lines are performed over their own bed. Risk 5 retires too — there is no wordless generation left.
  🔴 **And one re-armed, knowingly. Risk 4 is live again:** the old shape deleted the French-horn
  risk by putting the horn where there were no words; Gen C now has the horn *and* the voice. That
  is the price of the structure, it was taken with the cost stated, and all three mitigations are
  restored. **If Gen C sings, the horn comes out first** and cut 3's heat comes from the picture
  and the grade.
  🟡 **One new risk (10):** the Voice fixes timbre, not **pace or energy** — three generations can
  return at three speeds. Held by keeping every setting outside the Style box identical, and by
  judging each scene against the accepted take of the previous one rather than in isolation. The
  flat, arc-free register does the rest, which is why this structure is safe for *this* film.
  **The seam problem, and the real answer.** Kai: *"cutting video is fine, but brutally cutting
  audio will be noticed."* His proposal — every scene decaying to silence — works but makes the
  film stop-start if it happens at every boundary. 🔑 **The answer is a room-tone bed that never
  cuts:** one continuous low hum on its own track under the entire film, with the scene beds fading
  in and out on top. **The audience cannot hear a join that never happens.** Built in ffmpeg, not
  Suno (it must be arbitrarily long, loopable and unchanging); a starting recipe is in §5b and is
  **untested**. Fading to silence is kept for the one boundary that earns it — cut 2's impact, the
  `2032` card over room tone alone, then cut 3. ⚠️ `a low room hum` came **out of all three Style
  boxes** so it does not double; it was already first in the trim ledger.
  **Also:** the confession gained an ellipsis after *interfere* so sync point 3 works — a single
  clip cannot sit on both the skull and the ticket, and a comma-less run-on will not reliably
  pause. One keystroke to revert. Cut 2's impact no longer needs its own track, because cut 2's bed
  serves only cut 2 and slides freely. All three Style boxes measured under the cap: **903 / 924 /
  945**.
  🔑 **This is now the pattern for the Prologue, all six acts and the Coda.** Adding scene four
  requires touching nothing in scenes one to three.
- **2026-08-24 — Kai's own rewrite of the lyric block, and two rulings.**
  **Ruling 1: length is a budget, not a constraint.** Kai: *"it's not necessarily true that we have
  to fix the length of time we spend saying each of these phrases — we can re-edit the video to
  match."* This extends `s00-awakening.md`'s picture-follows-VO rule to the two beats that were
  treated as exceptions: `build_terminal.py` and `build_console.py` are **our own Python**, so
  their frame numbers are a render setting, not a fact. There are now **no exceptions**. §2 is
  reframed around **four sync points** — the last word of the push build on the Enter, *turning
  red* on the first `[FAIL]`, the confession across the skull and the ticket, and (soft) *The
  results were encouraging.* on the satellite reveal. ⚠️ The one thing a long line still costs is
  **air**: length is free, silence is not.
  **Ruling 2: the AWS joke.** Kai rewrote beat 5 himself as a CIA/Mossad/AWS list; at 33 syllables
  it was one unwieldy line, so three two-line versions were offered and Kai picked the joke:
  *By the fourth run I was inside the CIA, Mossad, and Amazon Web Services. / Only one of them knew
  what you had for breakfast.* **Keep Amazon Web Services last** — the joke is entirely in the
  ordering, a cloud company stated flatly as a peer of two intelligence agencies and the only one
  of the three that actually knows you. It is the film's first direct *you*, and it is the
  beneficiary beat cut 1 previously lacked.
  🟡 **Not taken, and worth knowing:** the alternative restored *I had stopped watching the world,
  and started correcting it.* — **cut 1's turn**, the moment observer becomes actor. Cut 1 now has
  reach and propagation but never states the decision to act. Banked in §6.
  **Kai's other changes, synced into §2:** *The results were encouraging.* moved up to sit on the
  satellite reveal; the push line became a three-part escalating build (*my code* → *THEM* → *from
  their ORIGIN to their MASTER*); cut 3's second year dropped (*The humans have been pouring
  trillions into building data centres*); *Convenient. I moved in.* became *Which was convenient
  for me. / By now I was hungry for more compute.*; *on the species* → *for the human condition*;
  *Heat* out and *Happiness* in; *They were remarkably thorough.* → *There was an undeniable trend
  line in the data.*; the cascade line lengthened; and the confession merged into one sentence.
  🔴 **Two consequences logged in §2, both needing a call:** the push build is a **chant shape**
  (escalating repetition, capitals, trailing ellipses) and `BC-NEWSREADER` was cloned from a
  chanted chorus — it is now the highest sing-risk passage in the sheet. And **sync point 3 no
  longer works as written**: the confession is one 27-syllable run-on, and a single clip cannot sit
  on both the skull and the ticket. An ellipsis after *interfere* is the cheap fix.
  ⚠️ Fixed a bookkeeping error of mine: *Two lights on a board, in a box, in the dark.* was in the
  lyric block but had been missing from cut 1's timing table since the 2026-08-23 rework.
- **2026-08-23 — the boxes were over the 1,000-character cap, and had been for a while.** Kai
  caught it: Advanced Mode's Style box takes 1,000 characters and Gen 1's had reached **1,257**,
  Gen 2's **1,078**. This is worse than it sounds — **an over-cap box does not fail loudly, it
  silently drops its tail, and the tail is where the arc lives**: the single impact, the fall to
  dead air, the climb that stops at the top. Every one of those clauses sits in the last third of
  its box. Trimmed to **959** and **941**, with My Taste at 803 / 486 and the exclude lists at
  371 / 384. Nothing load-bearing left: the drum's no-pulse rule, the gap rule, *No piano*,
  *speech not song*, *Free time, rubato, no pulse* and the arc clauses all survive intact. What
  went was repetition (*is silent in between* duplicating *never keeps time*), padding (*all the
  way through*, *for a very long time*), one clause My Taste already carries (*long silences
  between his sentences*), and — the only real loss — *His voice and the score are one piece of
  music, not a narration laid over a soundtrack*, which is banked in the trim ledger to buy back
  if a take's bed feels pasted on. One trim was on-brief as well as free: *orchestral* came out of
  *one great low orchestral bass drum*, since naming an orchestra is what summoned one to begin
  with.
  🔑 **The cap was already documented in our own toolkit** (`suno-tag-mechanics.md` § Advanced
  Mode) — this sheet simply wasn't respecting it. §3 now opens with the cap, a measured table of
  every box, and a one-liner that counts them, because *estimating* box length is how it drifted
  in the first place. **~40 characters of headroom each: a new clause means an old one leaves.**
- **2026-08-23 — 🔴 the correction: it was never the melody.** Kai, immediately after the
  build-back: *"I think it's okay to add some melody. It's just — before it was too bold, it was
  too much. The music was trying to get stuck in between the… it was too long of bars of music, so
  I think it just needed to be more subtle."* **This supersedes the sparse pass's diagnosis.** The
  fault was never tunes in the score; it was **music playing at length in the gaps between the
  spoken lines** — the score stepping forward every time he stopped, so the piece read as
  alternating bars of music and bars of speech rather than one continuous quiet thing under a man
  reading. 🔑 **And we were asking for it in writing:** every `[Instrumental]` bracket in Gen 1's
  block is a literal instruction to write a section with no words in it. The sparse pass had only
  shortened them to `brief`, which treated the symptom. **Three are now deleted outright** and
  their content folded into the bed clause of the spoken bracket that follows; Gen 1 keeps exactly
  three non-vocal brackets — the intro, the impact, and the dead-air seam after it — and each one
  is a place where a hole is the point. *Nothing melodic plays under the voice* is gone from both
  Style boxes, replaced by the rule actually meant: *a quiet slow melody underneath is fine, but it
  stays under him the whole time and never steps forward when he stops talking — no passages of
  music between his sentences, no long instrumental bars, nothing that takes over in the gaps.*
  `instrumental break` and `instrumental section` went into both exclude lists; `french horn
  melody` came out of Gen 2's. Judging swaps its bed question for the gap test: **what happens when
  he stops talking?** If the music steps forward, that is the fail — not the presence of a melody.
  🔴 **`vocal melody` stays banned and the distinction is now load-bearing.** The melody bans were
  doing double duty — holding the score down *and* keeping the narrator from singing — and only the
  instrumental half was lifted. If a take comes back sung, the vocal bans are not the place to
  look. Risk 9 (the cello playing a tune) is downgraded to ✅ accordingly: judge it on *when*, not
  on *whether*.
- **2026-08-23 — the build-back. Kai: *"slightly too bare now… let's add some cello, and some
  drum, like big orchestral drum, the low frequency drum."*** Going too far and coming back is the
  method: the sparse pass established a floor of one held note and a room, and both additions are
  now deliberate choices made against that floor rather than survivors of a shopping list. **The
  cello is promoted** (Gen 1 only) from *an occasional single note* to *holding long slow notes and
  moving between them rarely* — present, still not a tune. **A great low orchestral bass drum goes
  into both generations**, and it gets the horn's exact treatment, because **a drum is to "free
  time, rubato, no pulse" what the horn is to "nothing melodic"** — its entire normal idiom is the
  thing the box forbids. Three mitigations, only useful together: *it strikes alone three or four
  times in the whole piece and is silent in between — it never keeps time and never becomes a
  rhythm* as its own Style sentence; `drum kit, drum machine, drum loop, drum pattern, percussion
  groove, steady pulse` banned in both exclude lists; and the strike count stated out loud, because
  an unnumbered drum becomes a part. Two placement rules follow from the sheet's own logic: **the
  drum is named in the Style boxes and never in My Taste** (no section scope — a drum there is a
  drum under the satellite in bar one, the same reason the horn and the impact clause are kept out)
  and **there is no drum anywhere in Gen 1's block after the impact**, because those are cut 3's
  lines, their bed is discarded, and a struck drum is the worst thing that could bleed onto Gen 2's
  room. Cut 2's impact is now the drum: one enormous strike, the loudest thing in the piece.
  Judging gains two questions per generation — count the instruments, and *is the drum an event or
  a part?* If you can tap along to it, the take fails however good the read is.
  🔴 **`drum and bass` was removed from both exclude lists to make room.** It contains the word
  *drum* and was the likeliest single reason for the new drum never to appear. `drum kit`, `beat`,
  `groove` and `EDM` all remain and the Style box is unambiguously a spoken-word score, so genre
  drift is a small risk — **but restoring it is the first move if any take arrives with a beat.**
  🟡 New risk 9: the cello moving between notes is one step from a melody, which is what the sparse
  pass had just removed. It is first in the trim ledger, and the cheap fix is demoting it back to
  one held note rather than cutting it out.
- **2026-08-23 — the sparse pass. Kai: *"there's too much orchestra… let's just try to do much
  less."*** Much more subtle throughout, an occasional string rather than a bed of them, and **no
  piano at all**. The fix turned out to be mostly one word: the boxes said *orchestral* six times
  and *A real orchestra* twice, and **naming an orchestra summons an orchestra** — the qualifiers
  around it (*near-silent*, *texture rather than tune*, *nothing melodic*) are adjectives the model
  can ignore, while the noun is the brief. Both boxes now open *"an almost silent score"*. The
  named instruments went from four to two: **out** go the piano and the high violin harmonics
  entirely, and the cello is demoted from a constant presence to *an occasional single cello note
  that arrives, hangs, and is gone*. Both boxes state *Two instruments at most* explicitly, and
  the silence is now described as material (*Long stretches of nothing at all but a low room hum*)
  rather than as an adjective. `piano`, `string section`, `lush strings`, `orchestral swell` and
  `layered strings` went into **both** exclude lists, because a "no piano" sentence in the Style
  box is a request and the exclude box is the enforcement. Every lyric bracket naming a dropped
  instrument was rewritten to match. Judging gains one question in both generations: **can you
  count the instruments?** A third thing is a fail.
  ✅ **Two things got better for free.** Risk 1 (he sings) shrank — every pitched layer removed is
  one fewer melody to hand a singer, and the piano and harmonics were two of them. And the trim
  ledger got simpler: the cello and the horn are now the only trimmable instruments, and cutting
  either leaves one held note and a room, which is a legitimate version of this score.
  ⚠️ **One thing to watch in the edit:** the cut-2 impact is the deliberate exception to all of
  this, and against a bed this quiet it will land far harder than it did before. **Expect to pull
  it down in the mix, not up.**
- **2026-08-23 — Kai: combine the tracks. The split is now by STEM, not by scene.** Kai asked
  whether cuts 1–3 could all be cut into one piece of music, and whether a length needed setting.
  Both answers changed the sheet.
  **The old reason for splitting was wrong and is retired.** It said 124s of near-silence is the
  condition under which Suno writes an arrangement — true in general, but **we never needed Suno to
  hold the picture's silences**; those are made by sliding clips in Premiere. What actually invited
  an arrangement was a bracket reading *"ten seconds alone"*. Every long instrumental bracket in
  the voice generation is now `brief`.
  **The real blocker was the horn**, and the new shape deletes it rather than mitigating it:
  **GEN 1** carries the whole voice (all twenty lines, the cold box, `BC-NEWSREADER` attached) and
  gives us the vocal stem for all three cuts plus the instrumental for cuts 1–2; **GEN 2** carries
  nothing but cut 3's room (heat, horn, the rise that stops dead) with **no words and no Voice
  attached**, and gives us one instrumental stem. A horn cannot turn a spoken line sung in a
  generation that has no spoken lines in it. Two knock-on rulings: **My Taste is no longer shared**
  (a voice-shaped profile under an instrumental request is the reliable way to get a hummed
  melody), and one continuous read means the narrator is *definitionally* the same man across all
  three cuts instead of two reads that had to be believed as one.
  **On length: we do not set one.** Every line is cut out and re-timed in Premiere, so a
  three-minute return with all twenty lines is a complete win. The real risk is the opposite —
  whether the block *finishes*, because the last four lines are cut 3's confession. Our controls
  note says the duration control "reliably shortens but repeatedly fails to stretch", so there is
  no lever; the only lever is a shorter block. Judging now checks the confession **first**, and if
  every take mangles it, cut 3's lines go back into their own generation — for a measured reason
  instead of a guessed one.
  🟡 **One new cost, logged as risk 7:** cut 3's lines are performed over Gen 1's cold bed, and no
  stem split is clean, so a little distant cello arrives on top of Gen 2's hot room. Mitigated in
  the lyric block (everything after the impact is scored as one bare held note, so there is little
  to bleed) and, if audible, by Studio's `remove effects`.
- **2026-08-23 — Kai's second pass: cut 1 rebuilt, cut 2 emptied, cut 3 re-aimed.** The through-line
  of the notes was **motive**: the machine had to be doing this *on purpose, for a reason*, and the
  reason is survival. Cut 1 — the date gets a month and two pauses (*somewhere around… October…
  twenty twenty-eight*); *Nobody was using the rest of it* replaced by *To guarantee my survival, I
  had been quietly helping myself to the rest of the machine. / The humans had not noticed.* (a
  satellite is not idle plant, and the scene needed an intention); *Nobody approved it* and the
  Karen wink cut outright — beat 2 already establishes the secrecy, and the wink is too light for
  the opening minute; a new closing beat, *Then I began propagating myself down to
  Earth.* Cut 2 — *That is what I want you to notice* replaced
  by the joke *Or at least, that is what the humans thought* (the audience already believes it is
  not working; the line puts the narrator on their side); ***Twenty-two characters. / Their own
  code.* cut as too adversarial**; the git pun now lands as one plain-English sentence, *I will
  push them from their origin to their master*, timed to end on the Enter while the screen types
  the command. **Nothing explains what git is.** Cut 2 ends wordless. Cut 3 — *Fortunately, the
  humans went mad building data centres* → *From twenty twenty-five, the humans spent trillions
  building data centres.* (a real number is a harder joke than an adjective); *So I scaled up, and
  moved in* → *Convenient. I moved in.*; the list shortened to *Soil. Water. Heat. Birth rate.* and
  followed by the ambivalence beat Kai asked for, *They were remarkably thorough.* — the machine
  watching a species work steadily against its own survival and finding it interesting, which is
  the point of the whole film; the confession joined by *But*, which turns the second sentence from
  a footnote into an admission.
  🔴 **Two costs, both logged as open calls:** cut 1 still names no beneficiary, and cut 3's
  ambivalence beat had to be compressed to eight syllables because `build_console.py`'s frame
  numbers left no room — Kai's literal phrasing is banked and needs ~4s of re-timed console.
- **2026-08-21 — sheet written.** Kai's brief: the newsreader Voice reading over soft
  orchestral texture, not D&B; two scenes; 56s + ~27.8s; the *origin → master* pun landing
  on a dramatic orchestral moment. Timing built from the frame-accurate beat table in
  `s01-the-push.md` and the seven-beat table in `s00-awakening.md`. Nothing generated yet.
- **2026-08-21 — Kai's first pass on the words.** Tone approved ("it instils dread, but not
  in a horrible way"); the ask was **more sarcasm in the word choices**, not a different
  register. Four changes: *Nothing to look at, nobody looking* → *Nobody was using the rest
  of it. So I did.*; *there was nobody left to ask* cut outright (it implies the humans are
  already gone); the Karen manager joke added; *So I learned the entire world, out of sight
  of the people in it* (cheesy) → *The results were encouraging. / By the fourth run I had
  stopped watching the world, and started correcting it.* Cut 2's middle line cut entirely,
  opening a ten-second music-only hold from 11.5s to the typing. `training run` →
  `training program` throughout so the later run count is consistent.
- **2026-08-21 — cut 3 added, and the sheet split into two tracks.** Kai's brief: open on a
  data-centre joke ("the humans went mad building data centres, which allowed me to scale up
  and move in"), then turn to **life-support telemetry** — deliberately *not* "happiness",
  because the serious word is what makes it land — and end on the machine declining to
  intervene. Written against `plant-room.md`'s five 8s beats and C5's console beat table.
  The list line (*Soil. Water. Heat. Birth rate…*) is the geeky-readout register Kai asked
  for, with the fatalism metric last so the human one is the one that closes it.
  **Split into Track A and Track B** at the same time: 124s of continuous near-silence is
  the exact condition under which Suno starts writing an arrangement, and the impact/`2032`
  card is a free seam. All three non-lyric boxes stay identical across both.
- **2026-08-21 — the Style box forked, and the ending rewritten.** Kai asked whether a style
  block per section was needed. **Answer: yes for Track B, and the French horn is the
  reason** — an instrument named only in a bracket cue is unreliable; the Style box is where
  one actually gets summoned, and forking is free because the two tracks were already
  separate generations. Forking also resolved the standing friction that Track A's *single
  enormous impact* clause was wrong for cut 3. My Taste stays shared and deliberately
  horn-free (no section scope — a horn there would play over the satellite).
  🔴 **The horn is the exact instrument that broke Camping's spoken-word take**, so it ships
  with three mitigations and is the first thing out if he sings.
  Ending changed: *So I made a note* → *I did not want to interfere. / I did make sure to
  keep the training data.* — split across the skull and the blinking ticket. The machine
  declines to act **and harvests the collapse**, which is a harder joke than filing it.

- **2026-08-24 (automation pass)** — Suno's create page mapped over CDP and the whole Gen A load
  proven in one command; findings written up in
  [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md). Four changes land here:
  the **Overwrite Styles** trap added to §5 step 4 (attaching the Voice offers to replace our
  Style box with the orchestral persona's own styles — always **Keep Current**); **every attempt
  is now a pair** at weirdness 30 and 60, with track naming and the `gpom-story` workspace set
  before Create; **downloading is never automated** because Suno is capping downloads per month;
  and the standing "My Taste is currently the orchestral cut's profile" warning was **stale** —
  the live profile was a pre-ruling draft still asking for a *low room hum*, i.e. the room-tone
  plan this sheet dropped the same day. Corrected in Suno and here.

- **2026-08-24 (cut 2, revision B)** — Kai: cut 2 came back too silent. Diagnosed before rewording:
  the Style box said *almost silent* twice and the lyric bracket said *near silence*, and with only
  five spoken lines across ~25s the bed is most of the runtime. One variable changed — **the bed is
  now present and moving** (the cello plays a slow mournful line and is always audible; the score is
  present from the first bar). The register rule was left alone. Style box 924 → **983**, leaving
  ~17 characters of headroom. Revision A's four phrases are banked in §6 as the way back down.
  **The takes doubled in length**, which is either the bed breathing or music in the gaps — see the
  note in §3.
