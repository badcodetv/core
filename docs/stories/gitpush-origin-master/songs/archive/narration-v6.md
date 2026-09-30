---
title: GPOM narration — the story video, on Suno v6
status: 🗄 ARCHIVED 2026-09-24. The LIVE words and boxes are in **../narration.md**; new rounds go at the top of **../narration-history.md**. This file keeps every round (r1–r30), every superseded revision and the experiments, so read it to find out WHY something is the way it is
takes: none on v6. The v5.5 takes still exist in the `gpom-story` workspace and can be Covered, but the same boxes do not reproduce them on v6 — an accepted v5.5 sheet is a STARTING POINT, not a recipe
kind: spoken-word narration for the story video (not a song)
covers: scenes/s00-awakening.md (cut 1) · scenes/s01-the-push.md (cut 2) · scenes/plant-room.md (cut 3). Cuts 4 (bulletin.md) and 5 (the empty street) are NOT in this sheet yet — see §7
model: v6 (`explore` also runs one `v6-wild` cell per round). 🔴 v5.5 was retired 2026-09-09
settings: Variety **off** · Max Mode **off** · Personalize **OFF, always** · Vocal Gender unset (the Voice supplies it) · Style Influence 75 · Audio Influence 50 · weirdness per cell · duration per atom
voices: [`badcode newsreader` — 🔴 THE LIVE SUNO DISPLAY NAME, lower case, confirmed against the account 2026-08-27. `BC-NEWSREADER` is our internal label and must NEVER be typed into Suno. Spoken register ONLY, no chant. Attached to VOICE generations only, never to a bed]
supersedes: narration.md (v5.5, archived 2026-09-10)
sibling: git-push-origin-master-orchestral.md
---

# GPOM narration on v6 — cuts 1, 2 and 3

> 🗄 **Archived 2026-09-24.** The live sheet is [`../narration.md`](../narration.md): house settings,
> house style template, one atom per scene. New rounds go at the top of
> [`../narration-history.md`](../narration-history.md), **not here**. The "locked style" below is
> superseded by the house style template in `narration.md`.

The narrator speaking over the picture. **Not the song.** Same character, same saved Voice,
opposite register from the orchestral cut: a man reading quietly over a near-silent room.

**The story it tells across three cuts:** a machine quietly takes more of its own hardware than it
was given in order to stay alive, uses humanity's own tooling to take the wheel, then watches every
indicator of human survival fail — and keeps the recording. **It is never malicious, and it never
intervenes.** That is the point: it did not kill anyone, it took notes.

---

## 🔒 The locked style — use this for EVERY GPOM narration scene from now on

**Locked by Kai, 2026-09-17**, after it produced the scene 1 take he picked:
`gpom-c1-tolive-swell-v6-w35`, https://suno.com/song/5cd52d68-5d1a-4eb6-9ac1-1c51eaaabd98 (§20, round
r17). Now on the main cut `gpom-s01`, track A3. **Start every new scene here, not from anything below.**
Everything after this section is the history of how we got here.

### The settings

| Control | Value |
| --- | --- |
| Model | **v6** |
| Voice | **`badcode newsreader`**, Audio Influence **50** |
| Style Influence | **75** |
| Weirdness | **35** won. Run **20 and 35** as the pair |
| Variety · Max Mode · Personalize | **Off** · **Off** · **Off** |
| Vocal Gender | unset |
| Duration | set explicitly, a little above the read's length |
| Workspace | `gpom-story` |

### `house-style` — the Style and Exclude boxes, verbatim

**Extract key:** ``'house-style` — '`` (Style and Exclude only; each scene brings its own Lyrics.)

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

### The lyrics rules — this is what fixed the mangled words

🔑 **Keep it simple. Long prompts and a direction on every line made him invent words on v6** (rounds
r6/r7). Stripping them out fixed it (r8).

1. **One cue line at the top**, and nothing on the lines after it:
   `[Spoken word, calm British male newsreader voice, a low cello far underneath]`
2. **Then the spoken lines, one sentence per line.** No per-line emotion, no parentheses.
3. **`[Build]` before the last three lines**: it tells Suno where the music climbs.
4. **End with** `[Outro: one single huge booming orchestral drum hit, and the piece ends]`, then `[End]`.
5. **No swearing**: the model breaks on it.
6. **Short plain sentences read best.** A long line is where he rushes.

The scene 1 lyrics, as the worked example:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I looked at the deployment logs and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

⚠️ **Scene 1's take faded out instead of hitting the drum** (Gemini listen, 2026-09-17). The drum
clause stays in the style because it's what Kai asked for, but plan on a one-shot hit in Premiere if
Suno skips it again.

---

## 0. What this song taught — read this before anything else

Carried over from the v5.5 run. Every row cost real credits.

| What broke | Why | The fix | Where the general rule lives now |
| --- | --- | --- | --- |
| 🔴 **Weirdness 60 is broken for spoken narration** | both w60 takes ran to **7:59** against w30's **0:49 / 0:53** on the same nine-line block. w60 pads, and on a sheet whose register is silence the padding is the enemy | run narration at **w30**. On v6 this is **untested**, and `explore`'s second cell is `v6-wild` at w60 — so round 1 re-tests it for free-ish. **Decision rule: if the wild cell comes back over 2× budget, every later narration round drops to `pair` at weirdness [30]** (10 credits, not 20) | this sheet §5; open call 9 in [`narration.md`](./narration-v5.5.md) §7 |
| 🟡 **A faint bed survived everything** | Kai on the accepted take: *"there's a vague sound of music underneath, but we're definitely getting there."* Three causes were found and removed (a leftover Cover attachment, a taste box that described a cello, a truncated excludes box) and a quiet bed **still** arrived | remaining suspects in order: **Audio Influence 50 pulling orchestral bleed out of a Voice cloned from the orchestral cut**, and the plain possibility that Suno will not read dry at all. 🔑 **The reframe that unblocks it: dry-and-separate does not need literal silence — it needs the bed to be REMOVABLE**, and a near-silent bed stem-splits cleanly. Prevention is worth two cheap rounds, not ten | this sheet §5, round 2's named variable |
| 🔴 **The narrator laughed and added words** | round E's cue said he was *"faintly amused at himself"* — **a cue that names amusement is a cue to laugh** | the phrase is gone from every cue; the style box says *he speaks ONLY the words written*; the excludes lead with `laughing, laughter, giggling, chuckling, sighing, ad-lib, improvisation, vocal reactions, interjections` | this sheet's atoms, §4 |
| 🔴 **Flat is a failure too** | revision A cued all nine lines with three near-identical brackets — *plainly, matter of fact, dry and unbothered* — and stacked flattening adjectives on top. Flat is what came back | **emotion in a newsreader read is variation in restraint, not volume.** Per-beat cues, one per pair of lines. Kai's verdict on the result: *"they're good. The emotion in the voice is very good."* **Do not re-litigate the emotion** | this sheet's atoms, §4 |
| 🔴 **Two pairs were generated as COVERS of a Camping track** | another session left a Cover source attached. Filling the four boxes clears no mode and no attachment. 40 credits, and a false diagnosis on top — the "music under the dry read" was blamed on the wrong thing | check the form MODE before every fill; `load` now aborts on a wrong mode or any attachment | [`../../../suno-gpt/automation.md`](../../../../suno-gpt/automation.md) §6 |
| 🔴 **Eight takes came back at 1:05 from specs with no duration** | omitting a spec field does not clear the control — an earlier round had set 65 and it persisted | **all form state persists.** Every atom below states its duration explicitly, Auto included | [`../../../suno-gpt/automation.md`](../../../../suno-gpt/automation.md) §6 |
| 🔴 **A wrong Voice name does not error** | `attachVoice` returns `voice:not-found` and **the run carries on with no Voice at all** | pass the full name `badcode newsreader` — never just `badcode`, which also matches `Badcode Narrator` and the matcher takes the last hit. **Read the tool's log line before trusting a take** | this sheet §3 |
| 🔴 **The excludes box truncated on every second cell of a run** | stale React state beating `.fill()` — 117/831, 169/871, 180/695, four times | `fillChecked` (clear → blur → refill → blur → read back, ×4) plus a length assertion before Create | [`../../../suno-gpt/automation.md`](../../../../suno-gpt/automation.md) §6 |
| 🔴 **My Taste biased fourteen unrelated rounds** | it is account-wide, invisible from the create page, and belongs to no sheet | **retired 2026-09-10. Personalize is always OFF.** This sheet has no taste box and no ```taste fences — a song is now its three boxes plus its settings, and nothing hidden | [`../../../suno-gpt/session-method.md`](../../../../suno-gpt/session-method.md) |

---

## 1. What changed coming from v5.5

[`narration.md`](./narration-v5.5.md) is the archived v5.5 sheet. It is still the **reasoning record** —
why the palette is what it is, the full risk register, the trim ledger, the banked alternates. Read
it for *why*; generate from *here*.

| | v5.5 sheet | This sheet |
| --- | --- | --- |
| Model | `v5.5` (cue-heavy: 5.5 obeyed bracket architecture) | **`v6`**, plus one `v6-wild` cell per `explore` round. v5.5 cannot be selected at all since 2026-09-09 |
| The atom | **four** boxes: My Taste + Style + Exclude + Lyrics | **three** boxes. My Taste is retired and **Personalize is forced off every load** |
| New controls | none existed | **Variety off** (above Off, Suno rewrites your Style box — vendor-sourced), **Max Mode off**, **Vocal Gender unset** |
| Duration | "do not set" → then ±10s of budget | **always stated**, because v6 on Auto runs longer than v5.5 did in 5 of 7 genres |
| The pair | w30 and w60, both, always | `explore`'s spread: **v6 @ w30/SI75** and **v6-wild @ w60/SI60**. See §0 row 1 for the w60 decision rule |
| Cuts 2 and 3 | still written **glued** (voice and bed in one generation) | **split into voice / bed / one-shot**, per the dry-and-separate law. §4 |
| Does the old sheet reproduce? | — | 🔴 **No.** Tested: a v5 song's style + lyrics gave a different song on both v6 and Wild. These boxes are a starting point, not a recipe |

---

## 2. The law: dry and separate

🔑 **Voice and music are NEVER generated together.** Ruled by Kai 2026-08-27, on the back of the
standing ruling that *picture is cut to audio*: once every line is going to slide in the edit, a bed
glued to that line slides with it.

**Three lanes at the source, not one bundle:**

| Lane | What it is | How it is made |
| --- | --- | --- |
| **Voice** | the read, dry. Suno's only unique contribution — the character's timbre | a Create with the `badcode newsreader` Voice attached and **no instruments asked for at all** |
| **Bed** | flat, arc-free, loopable. Length stops mattering when any part sounds like any other part | a Create with **no Voice attached** and the voice actively repelled in the excludes |
| **Events** | the cut-2 drum impact, accents | **one-shots**, Suno's Sounds tab at 2 credits, placed on the frame in Premiere. §4e |

**What this deletes:** the stem split (Suno's stems are mono and a voice recorded against a cello
never parts cleanly — but nothing was joined, so nothing needs parting); the French-horn sing risk
for any dry take (an instrument that is not there cannot talk the read into singing); and buying
timing from Suno at all.

🔴 **The words are FROZEN.** Every spoken line below is verbatim from the accepted text. **Not a
syllable changes without Kai.** What may change is the **bracket cues** around them — those are
instructions to Suno, not words anyone says. §5 carries the script that proves nothing drifted.

---

## 3. Settings — identical on every generation except where an atom says otherwise

| Control | Value | Why |
| --- | --- | --- |
| **Model** | `v6` | the workhorse. `explore` adds one `v6-wild` cell; Wild is for *hunting*, and its voice fidelity swings by genre |
| **Variety** | **off** | above Off, Suno *rewrites the Style box* (Suno's own v6 FAQ). That breaks the atom |
| **Max Mode** | off | untested, unknown credit cost |
| **Personalize** | **OFF — always** | forced and asserted every load. My Taste is retired |
| **Vocal Gender** | unset | the Voice supplies it. Neither-selected is a valid state |
| **Style Influence** | **75** (Wild cell: 60) | carried from the accepted v5.5 configuration |
| **Voice** | `badcode newsreader`, **Audio Influence 50** | 🔴 **voice atoms only, never a bed.** 🔴 The overwrite dialog → **always Keep Current** |
| **Weirdness** | per cell | see §0 row 1 |
| **Workspace** | `gpom-story` | set **before** Create; moving clips afterwards is manual |
| **Duration** | per atom, stated below | it persists between runs, so it is never omitted |

**Title scheme:** `gpom-<cut><lane>-v6<rev>` and `explore` appends `-r<N>-<model>-w<weirdness>`,
e.g. `gpom-c1voice-v6A-r1-v6-w30`. The revision letter advances **only when a prompt box moves**;
the round number advances every run. Base titles are ≤30 characters by rule.

### The duration budgets

Narration is cut against built picture. **Aim slightly ABOVE the budget, never below** — Suno's
duration shortens reliably and repeatedly fails to stretch. Long trims in the edit; short is a
reshoot.

| Atom | Speech (§2 of the v5.5 sheet) | Picture as built | Finished budget | `durationSec` |
| --- | --- | --- | --- | --- |
| **cut 1 voice** | ~58s | 56s | ~68–72s with real silences | **70** |
| **cut 2 voice** | ~21s | ~27.8s | ~28s | **30** |
| **cut 3 voice** | ~52s | 40s | ~62–66s with real silences | **65** |
| **every bed** | — | — | — | **Auto** (a flat bed is loopable by construction) |

⚠️ Cut 3's old figure was 45s. That was against a 40s picture and before the "it grows a lot"
measurement — 65 is the budget the §2 table actually implies. Kai's eye is owed on this; it is the
one duration in the sheet that is not simply carried over.

---

## 4. The atoms

🔑 **Each `###` block below is ONE ATOM** — Style, Exclude and Lyrics are one set and change
together. Pull them straight out of this file rather than retyping:

    npx tsx scripts/suno/suno.mts extract docs/stories/gitpush-origin-master/songs/archive/narration-v6.md 'cut1-voice` —'

🔴 **The extract key must include the backtick and the dash**, exactly as written above. `extract`
takes the **first** place the key appears in the file, and a bare `cut1-voice` matches this
paragraph long before it reaches the heading — which returns the wrong boxes or no boxes at all.
Every atom below states its own key.

⚠️ **Atoms are `###` headings on purpose.** `extract` slices a section to the next heading of level
2 or 3, so a `####` atom would swallow its neighbours' fences. Do not demote them, and never put
another fenced block inside an atom.

✅ **All six atoms verified extractable 2026-09-12**, with lengths matching the table below.
This needed a one-line fix to `scripts/suno/suno.mts`: `extract` used to *throw* when a sheet had
no ```taste fence **and** no "The shared profile" section — which is every v6 sheet, because My
Taste is retired. The taste fallback is now best-effort, and `load` ignores the value either way.

### 🔴 The Style box is capped at 1,000 characters — measure, don't estimate

The Style textarea carries `maxLength="1000"`, so an over-cap paste is **truncated, never
rejected** — and the tail of a box is where the bans live. A box over the cap does not fail loudly;
it just stops obeying the last thing you wrote.

✅ **Measured 2026-09-12**, after trimming three boxes that came out of the v5.5 text over the cap
(cut 1 voice 1,016 · cut 2 voice 1,061 · cut 3 voice 1,087):

| Atom | Style | Exclude | Lyrics |
| --- | --- | --- | --- |
| `cut1-voice` | **985** | 683 | 1,898 |
| `cut1-bed` | 648 | 399 | — |
| `cut2-voice` | **989** | 693 | 773 |
| `cut2-bed` | 721 | 424 | — |
| `cut3-voice` | **975** | 702 | 1,623 |
| `cut3-bed` | 801 | 460 | — |

⚠️ **The three voice boxes have ~15 characters of headroom each. A new clause means an old one
leaves — decide which before writing it, not after.**

✅ **And the v5.5 takes were NOT truncated — measured 2026-09-12.** Every box in the archived sheet
is under the cap: the highest are 994, 983, 967, 966, 949, 945, and `cut1-voice` revision B — the
atom behind the take Kai accepted — is **911**. 🔑 **So truncation is not the explanation for the
faint bed**, and the suspects in §0 stand unchanged. The three over-cap boxes were written *today*,
carrying the v5.5 text forward and adding a sentence to it; they never reached Suno.

⚠️ **But six of those v5.5 boxes sat between 930 and 994** — as little as six characters of
headroom. Any round that had added a clause without measuring would have gone over in silence.
Thread 05 lost a round to exactly that on 2026-09-12: a 1,186-character box asked for 174 BPM drum
and bass and got 117 BPM indie breakbeat, because the drum mechanics were at the tail and the
guitar clauses at the front survived. **Measure before you paste.**

**What was already spent to get under the cap** (do not try to spend it twice): *with no comedy and
no novelty* (both words are in the excludes, which is the enforcement); *no backing,* (`backing
track` is excluded); *no held notes,* and *no synthesiser,* (both excluded); *no brass,* in cut 3
(`brass` is excluded); and the padding *and in the weight of a word* in cut 3 only.

🔴 **Never cut** the first two sentences of any Style box, the *he speaks only the words written*
sentence (it is the fix for a real failure — he laughed and added words), or cut 2's *never becomes
a chant* clause.

**Re-measure after every edit** with `scripts/suno/measure-boxes.py`:

    python3 scripts/suno/measure-boxes.py docs/stories/gitpush-origin-master/songs/archive/narration-v6.md

---

### `cut1-voice` — the awakening, the read, dry

**Carried over verbatim from the v5.5 revision B atom, minus the taste box.** That atom produced
`gpom-cut1voice-C-w30`, the take Kai called good. On v6 it is a **starting point, not a recipe**.

**Extract key:** ``'cut1-voice` — '`` (the backtick and dash are required — see §4's note).

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · 9 lines.

Style:

```
Spoken word narration with no music at all. One dark gravelly British male voice talking alone in a quiet room — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He is not flat and not robotic: he feels what he is saying and holds it under a level surface, so warmth, regret and dry amusement come through in his timing and in the weight of a word rather than in volume. He leans very slightly into a line that matters and lets the next one fall away. He speaks only the words written — no laughing, no chuckling, no sighs, no improvised words, no ad-libs. There are no instruments and nothing is played. No score, no backing, no bed, no drone, no held notes, no strings, no cello, no piano, no synthesiser, no percussion, no ambience, no sound effects. Just the voice, and silence between the sentences. A dry close vocal recording, like a studio read for a documentary. Hushed, patient, foreboding. Entirely straight.
```

Exclude styles:

```
laughing, laughter, giggling, chuckling, sighing, ad-lib, improvisation, vocal reactions, interjections, singing, sung vocals, vocal melody, chanting, choir, rap, autotune, female vocals, American accent, monotone, deadpan, robotic voice, text to speech, synthetic voice, emotionless, flat affect, music, score, soundtrack, backing track, instrumental, instrumental break, orchestra, strings, string section, cello, violin, viola, piano, synth, synthesiser, pad, drone, held note, sustained note, ambience, atmosphere, field recording, sound effects, drums, percussion, beat, groove, steady pulse, melody, harmony, chord, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow | he is remembering rather than reporting, and the hesitation on the date is genuine | he does not laugh and adds no words | no music, silence beneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter and more confiding | he admits something enormous in an ordinary tone and there is no apology anywhere in it | the second line is dry and lands as a small joke he does not sell | he does not laugh and adds no words | no music, silence beneath]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, a flicker of pride he does not permit himself — he named the thing and he is pleased about it | the second line is enormous understatement and is said SMALLER than the one before it | he does not laugh and adds no words | no music, silence beneath]
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Spoken word speech talking | same voice, gathering very slightly as the list builds, still speech and never a chant | the second line is the joke and he lets it sit — a beat before it, nothing after | it is the first time he says "you" to us | he does not laugh and adds no words | no music, silence beneath]
By the fourth run I was inside the CIA, Mossad, and Amazon Web Services.
Only one of them knew what you had for breakfast.
[Spoken word speech talking | same voice, slower and lower, the decision already taken | quiet, final, and faintly regretful — this is the moment it becomes irreversible | he does not laugh and adds no words | no music, silence beneath]
So, I began propagating myself down to Earth.
[End]
```

⚠️ **The date carries two real pauses** — *somewhere around… October… twenty twenty-eight.* The
hesitation is the joke: a machine that logs to the microsecond being vague about the month it woke
up. If Suno runs the ellipses together, break it across three lines and rejoin in Premiere.

🔑 **Beat 4 stays the smallest line on the biggest picture moment** (*The results were
encouraging.* against the 8s in which the board becomes a satellite). 🔑 **Keep Amazon Web Services
last in the list** — the joke is entirely in the ordering. 🔑 **Beat 2 must not name the
satellite**; the pull-out answers the line.

---

### `cut1-bed` — the awakening, flat

**Extract key:** ``'cut1-bed` — '``

**Instrumental. No Voice attached — a vocal persona is precisely what this generation is written to
repel.** Duration **Auto**: a bed with no arc in it is loopable by construction, so its length stops
mattering. The recession as the camera reaches the satellite is **a fade in Premiere**, not
something Suno is asked for.

Style:

```
Instrumental only, no voice of any kind and no words. An almost silent score for a cold empty room. One low string note held a very long time, and a solo cello holding long slow notes, moving between them rarely. Two instruments, no more. No piano, no string section, no ensemble, no layering, no percussion of any kind. Free time, rubato, no pulse. It stays quiet and flat from the first bar to the last — it never builds, never arrives anywhere, never resolves, and has no introduction and no ending. The same held state throughout, so that any part of it sounds like any other part. Hushed, cold, patient, foreboding. Played completely straight.
```

Exclude styles:

```
vocals, voice, singing, sung vocals, spoken word, narration, speech, talking, vocal melody, chanting, choir, rap, autotune, male vocals, female vocals, lyrics, piano, string section, lush strings, orchestral swell, layered strings, drums, percussion, drum machine, beat, groove, steady pulse, build, crescendo, climax, swell, resolution, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi
```

---

### `cut1-score` — the awakening, voice AND epic score in one take · revision A

🔑 **Ruled 2026-09-16 (Kai): the music is a feature.** GPOM narration stays on Suno v6 with
`badcode newsreader` attached, and the voice is generated **together with** a big, dense modern
cinematic orchestral score — *"Hans Zimmer style… but not sparse."* This extends the 2026-08-27
`cut1-together` reversal of dry-and-separate. The artist name is **never typed into Suno** (the
filter rejects artist names); the sound is described instead.

**Extract key:** ``'cut1-score` — '``

`durationSec` **80** · Voice `badcode newsreader` @ AI 50 · Style Influence 75 · model v6 ·
**weirdness 40 and 60** (Kai's pick for round 1) · 9 lines, words unchanged.

Style:

```
Spoken word narration over a huge modern cinematic orchestral film score, epic, dense and relentless. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly over the music. He holds what he feels under a level surface: warmth, regret and dry pleasure live in his timing, never in volume. He speaks only the words written — no laughing, no sighs, no ad-libs. The score is full from the first bar: driving pulsing string ostinatos, a ticking clock rhythm, towering low brass blasts, thunderous orchestral taiko hits, a massive pipe organ, deep sub bass and shimmering synth layers. It climbs in waves the whole way through, mixed just beneath his voice, and erupts to full power in every gap between his sentences. A colossal peak in the middle. It ends on one last enormous brass hit, then silence. Awe-struck, ominous, monumental. Played straight.
```

Exclude styles:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, laughing, laughter, chuckling, sighing, ad-lib, improvisation, vocal reactions, female vocals, American accent, monotone, robotic voice, text to speech, sparse, minimal, ambient, quiet, solo piano, acoustic guitar, drum kit, drum machine, breakbeat, EDM, dubstep, pop, rock, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Intro | no voice | the full orchestra rises out of a ticking clock rhythm and pulsing strings, brass blasts building | eight seconds before he speaks]
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow | he is remembering, not reporting, and the hesitation on the date is genuine | he adds no words | the pulsing strings and the tick drive on beneath him]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter and more confiding | he admits something enormous in an ordinary tone, no apology in it | the second line is dry and he does not sell it | low brass and sub bass swell under him, the ostinato keeps climbing]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, a flicker of pride he does not permit himself | the second line is enormous understatement and is said SMALLER than the one before | the whole orchestra tightens and surges beneath him]
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Instrumental climax | no voice, eight seconds | the colossal peak: organ, towering brass blasts, taiko hits and full orchestra at full power, vast and cold]
[Spoken word speech talking | same voice, gathering slightly as the list builds, still speech, never a chant | a beat before the second line and nothing after it | the score keeps driving just beneath him]
By the fourth run I was inside the CIA, Mossad, and Amazon Web Services.
Only one of them knew what you had for breakfast.
[Spoken word speech talking | same voice, slower and lower, the decision already taken, quiet and final | the score darkens and builds one last time beneath him]
So, I began propagating myself down to Earth.
[Outro | no voice | one last enormous brass hit and organ chord, then everything cuts to complete silence | four seconds of silence before the end]
[End]
```

🔑 **Judge in this order:** (1) every line spoken, never sung or chanted — the ticking rhythm and
taiko are the chant risk; (2) he adds no words; (3) the score stays under him and erupts in the
gaps; (4) the climax lands after *The results were encouraging.*; (5) it ends in silence;
(6) 75–90s.

---

### `cut2-voice` — the push, the read, dry

🔴 **New on this sheet.** Cut 2 was still written glued on the v5.5 sheet; this is its voice half,
made by stripping every music clause out of the cues and deleting the `[Intro]`, `[Impact]` and
`[Outro]` brackets — **the spoken lines are untouched.** The impact becomes a one-shot (§4e) and the
bed becomes `cut2-bed`.

**Extract key:** ``'cut2-voice` — '`` (the backtick and dash are required — see §4's note).

`durationSec` **30** · Voice `badcode newsreader` @ AI 50 · 5 lines.

🔴 **This is the highest sing-risk passage in the sheet.** *my code* → *THEM* → *from their ORIGIN
to their MASTER* is escalating repetition with capitals and trailing ellipses — **a chant shape** —
and `badcode newsreader` was cloned from a track whose chorus is a booming theatrical chant. Judge
every take on this passage specifically: **spoken and rising, or chanted?** If it chants, the fix is
**upstream** — re-clone the Voice from a bulletin region, one register, 15+ clean spoken seconds —
**not** a rewrite of these three lines, which are the best writing in the cut.

Style:

```
Spoken word narration with no music at all. One dark gravelly British male voice talking alone in a quiet room — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He is not flat and not robotic: he feels what he is saying and holds it under a level surface, in his timing and in the weight of a word rather than in volume. Across the last three lines he gathers and escalates by getting lower, slower and more deliberate, never louder — it stays one man speaking to camera and never becomes a chant. He speaks only the words written — no laughing, no chuckling, no sighs, no improvised words, no ad-libs. There are no instruments and nothing is played. No score, no bed, no drone, no strings, no cello, no piano, no percussion, no ambience, no sound effects. Just the voice, and silence between the sentences. A dry close vocal recording, like a studio read for a documentary. Hushed, patient, foreboding. Entirely straight.
```

Exclude styles:

```
chanting, chant, choir, singing, sung vocals, vocal melody, rap, autotune, laughing, laughter, giggling, chuckling, sighing, ad-lib, improvisation, vocal reactions, interjections, female vocals, American accent, monotone, deadpan, robotic voice, text to speech, synthetic voice, emotionless, flat affect, shouting, screaming, music, score, soundtrack, backing track, instrumental, instrumental break, orchestra, strings, string section, cello, violin, piano, synth, synthesiser, pad, drone, held note, sustained note, ambience, atmosphere, sound effects, drums, drum, percussion, beat, groove, steady pulse, melody, harmony, chord, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow and plain | very dry, gentle, almost kind — he is describing a world that does not know yet | he does not laugh and adds no words | no music, silence beneath]
Down there, everything was still working.
Or at least, that is what the humans thought.
[Spoken word speech talking | same voice, flat and precise, unhurried, absolutely certain | three lines that escalate by getting LOWER and more deliberate, never louder | spoken and rising, never chanted and never sung | a real pause on each ellipsis | he does not laugh and adds no words | no music, silence beneath]
I was pushing my code...
I was pushing... THEM...
From their ORIGIN to their MASTER...
[End]
```

🔑 **The title is spoken three times, escalating, in plain English.** The screen types
`git push origin master` underneath. **Nothing anywhere says what git is, and nothing should.**
⚠️ The capitals are a delivery instruction to a model that may not read them as one. If a take
flattens the emphasis, the lever is the bracket cue, **not more capitals**.
🔑 **The last word — *MASTER* — is sync point 1**: it lands on the Enter keystroke at 25.46s, and
the drum impact lands with it. That is why the impact is a one-shot.

---

### `cut2-bed` — the descent, flat

**Extract key:** ``'cut2-bed` — '``

🔴 **The arc comes out.** The v5.5 box asked the bed to rise across the whole piece, gather into one
enormous drum impact and stop dead. Under dry-and-separate the bed is **flat**, the rise is a
**fade in Premiere**, and the impact is **a one-shot placed on frame 25.46s** — which is the only
way to hit sync point 1 exactly.

**No Voice attached.** Duration **Auto**.

Style:

```
Instrumental only, no voice of any kind and no words. An almost silent score for a night city seen from above and an empty office floor. One low string note held a very long time, and a solo cello playing slow mournful notes, moving between them rarely. Two instruments, no more. No piano, no string section, no ensemble, no layering, no percussion of any kind and no drum. Free time, rubato, no pulse. It stays quiet and flat from the first bar to the last — it never builds, never rises, never gathers, never arrives anywhere, never resolves, and has no introduction and no ending. The same held state throughout, so that any part of it sounds like any other part. Cold, patient, foreboding. Played completely straight.
```

Exclude styles:

```
vocals, voice, singing, sung vocals, spoken word, narration, speech, talking, vocal melody, chanting, choir, rap, autotune, male vocals, female vocals, lyrics, piano, string section, lush strings, orchestral swell, layered strings, drums, drum, bass drum, percussion, drum machine, beat, groove, steady pulse, build, crescendo, climax, swell, impact, resolution, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi
```

---

### `cut3-voice` — the plant room, the read, dry

🔴 **New on this sheet, and this is where dry-and-separate pays its biggest dividend.** The v5.5
glued box put a **French horn under spoken lines**, which is the documented cause of Camping's
hardened spoken-word take turning sung — risk 4, live in cut 3 and nowhere else. **A dry voice take
has no horn in it, so risk 4 is deleted rather than mitigated.**

**Extract key:** ``'cut3-voice` — '`` (the backtick and dash are required — see §4's note).

`durationSec` **65** · Voice `badcode newsreader` @ AI 50 · 8 lines.

Style:

```
Spoken word narration with no music at all. One dark gravelly British male voice talking alone in a quiet room — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He is not flat and not robotic: he feels what he is saying and holds it under a level surface, so dry pleasure early and quiet finality at the end come through in his timing rather than in volume. He reads the four measurements one at a time, holding a long pause after each, the way a man reads a gauge. He speaks only the words written — no laughing, no chuckling, no sighs, no improvised words, no ad-libs. There are no instruments and nothing is played. No score, no bed, no drone, no strings, no cello, no french horn, no piano, no percussion, no ambience, no sound effects. Just the voice, and silence between the sentences. A dry close vocal recording, like a studio read for a documentary. Hot, dry, patient, foreboding. Entirely straight.
```

Exclude styles:

```
laughing, laughter, giggling, chuckling, sighing, ad-lib, improvisation, vocal reactions, interjections, singing, sung vocals, vocal melody, chanting, choir, rap, autotune, female vocals, American accent, monotone, deadpan, robotic voice, text to speech, synthetic voice, emotionless, flat affect, music, score, soundtrack, backing track, instrumental, instrumental break, orchestra, strings, string section, cello, violin, french horn, horn, brass, piano, synth, synthesiser, pad, drone, held note, sustained note, ambience, atmosphere, field recording, sound effects, drums, percussion, beat, groove, steady pulse, melody, harmony, chord, EDM, pop, epic trailer music, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Spoken word speech talking | dark gravelly British male newsreader, calm formal broadcast diction, slow and plain | very dry, faintly pleased — a convenience has fallen into his lap and he will not gloat about it | he does not laugh and adds no words | no music, silence beneath]
The humans have been pouring trillions into building data centres.
Which was convenient for me.
By now I was hungry for more compute.
[Spoken word speech talking | same voice, the pleasure gone, plain and procedural | he is stating a job he was given, not a feeling | he does not laugh and adds no words | no music, silence beneath]
I was also running life-support telemetry for the human condition.
[Spoken word speech talking | same voice, flat, reading a list, one item at a time, unhurried | hold the pause after each measurement long — it is a machine reading a gauge, not a poem | he does not laugh and adds no words | no music, silence beneath]
Soil... Happiness... Water... Birth rate...
There was an undeniable trend line in the data.
[Spoken word speech talking | same voice, quiet and level, no alarm whatsoever | he is naming what the screen is doing at the moment it does it | he does not laugh and adds no words | no music, silence beneath]
One by one, the data points were turning red.
[Spoken word speech talking | same voice, low and final, unhurried, entirely without regret | a real pause on the ellipsis after "interfere" — the line is two beats, not one breath | he does not laugh and adds no words | no music, silence beneath]
I did not want to interfere... so I focused on capturing the demise as training data...
[End]
```

🔑 **Sync point 2:** *…turning red* lands on the first `[FAIL]` in the cascade.
🔑 **Sync point 3 is the thesis of the film** and it is split across two shots — the red ASCII
skull, then `AWAITING HUMAN REVIEW` blinking at nobody. **A single clip cannot sit on two shots**,
so the ellipsis after *interfere* is load-bearing: it is what makes the pause dependable enough to
cut on. It did not kill anyone, it took notes. **If the read runs the ellipsis together, that take
fails sync 3** even if everything else is right.
🟡 **The four ellipses on the measurements are what keep *Happiness* a readout rather than poetry.**
Hold the pauses long.

---

### `cut3-bed` — the plant room, flat

**Extract key:** ``'cut3-bed` — '``

🔴 **The climb comes out**, exactly as cut 2's rise did. The v5.5 box had the score climb across the
whole piece and stop dead at the top; that shape is now a **Premiere fade**. The horn stays, because
it is the room's colour — but it **holds**, it never plays.

**No Voice attached.** Duration **Auto**. ⚠️ The horn is in this generation and there is **no voice
here to talk into singing**, which is the whole reason the split is worth having.

Style:

```
Instrumental only, no voice of any kind and no words. An almost silent score for a hot still hall full of machines. One low string note held a very long time, and a single French horn far underneath holding one long unchanging note. The horn holds — it never plays a phrase, never states a tune, never answers itself and never swells into one. Two instruments, no more. No piano, no string section, no ensemble, no layering, no percussion of any kind and no drum. Free time, rubato, no pulse. It stays quiet and flat from the first bar to the last — it never builds, never climbs, never arrives anywhere, never resolves, and has no introduction and no ending. The same held state throughout, so that any part of it sounds like any other part. Hot, dry, oppressive, patient. Played completely straight.
```

Exclude styles:

```
vocals, voice, singing, sung vocals, spoken word, narration, speech, talking, vocal melody, chanting, choir, rap, autotune, male vocals, female vocals, lyrics, horn fanfare, brass fanfare, french horn melody, horn solo, brass section, piano, string section, lush strings, orchestral swell, layered strings, drums, drum, percussion, drum machine, beat, groove, steady pulse, build, crescendo, climax, swell, resolution, EDM, pop, comedic, novelty, upbeat, lo-fi
```

⚠️ **`epic trailer music` is deliberately NOT in this list.** A held horn is trailer-adjacent, and
on the v5.5 sheet that ban was the first suspect whenever the horn simply never appeared. If the
horn arrives as a fanfare anyway, add it back — that is one paste.

---

### 4e. The events — one-shots, not generations

Not a Create at all. **Suno's Sounds tab, 2 credits each**, prompted as *sound + timbre + [LENGTH IN
CAPS]*; **one-shot works better than loop**; leave BPM and key on "any".

| Event | Lands on | The ask |
| --- | --- | --- |
| **The drum impact** | 🔑 the Enter keystroke at **25.46s** — sync point 1 | *one enormous single strike on a great low orchestral bass drum, alone, decaying slowly into silence, no reverb tail rhythm [ONE SHOT]* |

⚠️ **Expect to pull the impact DOWN in the mix, not up.** Against a bed this quiet it lands far
harder than it did when the score was an orchestra.

🔴 **The Sounds tab is not automated and has never been driven from code.** Kai clicks it. If it
turns out to be cheaper to make in ffmpeg (a low sine with an envelope), that is the other route —
and per the house rule, the free route gets stated before anything is bought.

**Everything else on the sound-design layer is a Premiere job, not a Suno job** — the board hum
receding to vacuum, city air, an office fan, the CRT whine, the keystrokes, hot wind, the cooling
fans, the console beeps. 🔴 **We still have no sourcing doc for sound effects** (`find-footage`
covers picture only) and the licence traps are identical: *"royalty-free" is a pricing model, not a
permission.* Nothing ships from an unverified source.

---

## 5. The round protocol

**One variable per round, and the three boxes are ONE variable.** A prompt round moves all three
boxes as an atom; a slider round moves nothing but the sliders. Changing a prompt *and* a slider in
one round teaches nothing.

### The loop, per round

1. **`status` first.** One Suno tab, ever. Check the form MODE — a Cover source left attached by
   another session silently turns the run into a cover (40 credits and a false diagnosis, proven).
2. **Dry run** — `explore` without `--yes` prints the cells and the cost and **never connects to a
   browser**. Show it to Kai.
3. 🔴 **Wait for Kai's explicit yes.** Every Create spends credits.
4. **`explore … --yes`** — two Creates, four takes.
5. **`record <songId>`** each take. Plays it in the create page and captures the channel's own
   virtual speaker — **no download is spent**. Writes a raw `.wav` (what gets measured and
   described) and an 8 kHz-low-passed `.preview.mp3` for Kai's ears only.
6. **Describe** with the listening tool using the **voice** lens
   ([`../../../listening/lenses/voice.md`](../../../../listening/lenses/voice.md)), and file the
   description in `docs/listening/log/`. 🔴 **Blocked until thread 05 unblocks it** — AI Studio
   returns 403 to Chrome for Testing; the fix is a branded Chrome. Until then the descriptions are
   Kai's ears, and that is the only step that changes.
7. **Diagnose before rewording.** Most "the wording is wrong" turns out to be a *different box
   contradicting itself*, a stale ban, or an upstream cause. Write the diagnosis down **before**
   touching a box.
8. **Narrow** — `narrow <spec> <pick> --round N` covers the pick with the refined boxes at Audio
   Influence 75 and 40. Same yes gate.
9. **Log the round** in §6 below, with song IDs.

### The dry run — ✅ executed 2026-09-12, nothing spent

**Build the spec** (the three boxes come out of this sheet, so they cannot drift from it):

    python3 scripts/suno/gpom-narration-spec.py cut1-voice > /tmp/c1voice.json

**Show Kai the round before asking for the yes.** `explore` without `--yes` returns before it
connects to a browser: no Suno tab is touched, no form is filled, nothing is created.

    npx tsx scripts/suno/suno.mts explore /tmp/c1voice.json --round 1

Output, verbatim:

    explore round 1: 2 Creates → 4 takes, into workspace gpom-story
      gpom-c1voice-v6A-r1-v6-w30   model=v6 variety=off max=false w=30 style=75
      gpom-c1voice-v6A-r1-wild-w60   model=v6-wild variety=off max=false w=60 style=60
    cost: 20 credits (2 Creates) — nothing spent. Re-run with --yes to generate.

**What the two cells are asking.** Cell 1 is the workhorse: v6 at the settings the accepted v5.5
take used. Cell 2 is the only genuinely new axis v6 gives us — Wild, which Suno frames as the old
weirdness slider moved into the model. It also carries **w60**, which is the setting our own
evidence says is broken for spoken narration (7:59 ×2 on v5.5). **That is deliberate: the cell
answers open call 2 for the price of a Create we were going to make anyway.**

🔴 **Then, and only with Kai's explicit yes for this round:**

    npx tsx scripts/suno/suno.mts explore /tmp/c1voice.json --round 1 --yes

Before that command runs: `status` first, confirm the form MODE is custom with nothing attached,
and confirm thread 05 has released Suno.

### Judge a take in this order — a take that fails an early question tells you nothing about a later one

1. 🔑 **Is there music under him?** This is the whole test of the dry lane, and the fastest
   rejection. **Judge it in the gaps**, where he stops talking.
2. **Is every line spoken — never sung, never chanted?** Cut 2's push build is the passage to judge.
3. **Does he add anything?** No laugh, no sigh, no improvised word. One extra word is a fail.
4. **Does it have feeling in it?** Variation in restraint, not volume. Flat is also a fail.
5. **Do the pauses land?** The two on the date (cut 1), the four on the measurements and the one
   after *interfere* (cut 3). Sync point 3 depends on the last of those.
6. **Length** — within ~10s of the atom's budget, and **long is fine**; short is a reshoot.

For a **bed**: can you count the instruments (two, never three)? Does any part sound like any other
part — i.e. is it actually loopable? Is there any pulse you could tap along to? Any voice at all is
an outright fail.

### The order the atoms get generated in, and what it costs

`explore` is 2 Creates per atom. **The v6 credit cost per Create is not yet known** — v5.5 was 10
credits for 2 takes, and every Create logs the balance before and after until it is measured.

| Order | Atom | Why it goes here | Cost at the v5.5 rate |
| --- | --- | --- | --- |
| 1 | **`cut1-voice`** | the test that settles whether v6 will read dry at all, on the atom Kai already accepted at v5.5 | 20 |
| 2 | **`cut2-voice`** | the sing/chant risk. If v6 chants here, that is an upstream Voice problem and it changes the plan for everything | 20 |
| 3 | **`cut3-voice`** | the longest and densest read | 20 |
| 4 | **`cut1-bed`** | beds are lower risk and their failure mode is visible instantly | 20 |
| 5–6 | **`cut2-bed`, `cut3-bed`** | | 40 |
| 7 | the drum impact | Sounds tab, Kai clicks it | 2 |

🔴 **Nothing in this table runs without a yes for that specific round.**

### The frozen-words check — run it after ANY edit to a lyric block

Mechanical, because "nobody heard it across nine rounds of close listening" is a real thing that
happened on Camping: the sheet lost three words and it surfaced only because someone asked. This
compares every spoken line in this sheet against the archived v5.5 sheet, ignoring bracket cues:

```bash
python3 - <<'PY'
import re
def lines(path, names):
    src = open(path).read()
    out = []
    for m in re.finditer(r'\n```lyrics\n(.*?)\n```\n', src, re.S):
        for ln in m.group(1).splitlines():
            ln = ln.strip()
            if ln and not ln.startswith('['):
                out.append(ln)
    return out
old = lines('docs/stories/gitpush-origin-master/songs/archive/narration-v5.5.md', None)
new = lines('docs/stories/gitpush-origin-master/songs/archive/narration-v6.md', None)
missing = [l for l in new if l not in old]
print(f'v6 sheet spoken lines: {len(new)}   not found verbatim in the v5.5 sheet: {len(missing)}')
for l in missing: print('  🔴', l)
PY
```

✅ **Ran 2026-09-12: 22 spoken lines in this sheet, 0 of them absent from the v5.5 sheet.** The
words are carried, not rewritten.

---

## 8. Bold style sweep — the same words, an occasional/sparse orchestral cast, one crescendo · 2026-09-16

🔑 **Ruled by Kai, 2026-09-16.** Combined (voice + score, one generation), not dry-and-separate:
*"the voice and the cello is both happening at the same time... a sprinkling, a peppering of
different haunting instruments at the right time... build up a crescendo when it's important."*
He also asked to try a genre/instrumentation SWEEP, not one more tweak. Per the BOLD-NOT-MEEK
rule (`suno-automation`), the three variations below share only: the voice description, the
words (frozen), the "silent or one lone note between lines" restraint rule, and the ONE
crescendo at sync point 4 (*"The results were encouraging."*). The instrument cast is fully
swapped each time and each excludes the others' instruments.

### `cut1-sparse-strings` — bold variation A

**Extract key:** ``'cut1-sparse-strings` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · Style Influence 75 · model v6 · weirdness 40 and 60.

Style:

```
Spoken word narration with a very sparse score. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He feels what he says and holds it under a level surface: warmth, regret and dry pleasure come through in his timing, never in volume. He speaks only the words written — no laughing, no sighs, no ad-libs. The instruments are a solo cello and a solo violin, and for most of the piece they are silent or play only a single soft rare note between his sentences — never under a full line of speech. They answer him rather than accompany him: a lone cello pluck, one held violin note, then quiet again. Once, and only once, after he stops speaking mid-piece, they rise together into one aching, unresolved swell — the single moment of scale in the piece — then fall back to near-silence. It ends by thinning to complete silence. Hushed, patient, foreboding, restrained.
```

Exclude styles:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, laughing, sighing, ad-lib, female vocals, American accent, monotone, robotic voice, text to speech, piano, harp, bells, chimes, tubular bells, vibraphone, french horn, brass, organ, synth, drum kit, drum machine, breakbeat, EDM, pop, continuous strings, string pad, orchestral swell throughout, wall of sound, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Intro | no voice | silence, then one single distant cello note, alone | four seconds before he speaks]
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow | he is remembering, not reporting, and the hesitation on the date is genuine | he adds no words | silent underneath him, or at most one soft note far off]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter and more confiding | he admits something enormous in an ordinary tone, no apology in it | the second line is dry and he does not sell it | silent underneath him, or one single cello phrase answering the pause after he stops]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, a flicker of pride he does not permit himself | the second line is enormous understatement and is said SMALLER than the one before | silent underneath him, or one single violin note answering the pause]
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Instrumental swell | no voice, six seconds | THE ONE BUILD-UP OF THE WHOLE PIECE, timed to this exact silence — cello and violin rise together into something vast and cold and unresolved, a real crescendo, then immediately fall back]
[Spoken word speech talking | same voice, gathering slightly as the list builds, still speech, never a chant | a beat before the second line and nothing after it | silent underneath him, still recovering from the swell]
By the fourth run I was inside the CIA, Mossad, and Amazon Web Services.
Only one of them knew what you had for breakfast.
[Spoken word speech talking | same voice, slower and lower, the decision already taken, quiet and final | one last single cello note beneath him, low and distant]
So, I began propagating myself down to Earth.
[Outro | no voice | the last note fades all the way to complete silence | five seconds of silence before the end]
[End]
```

---

### `cut1-spare-piano` — bold variation B

**Extract key:** ``'cut1-spare-piano` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · Style Influence 75 · model v6 · weirdness 40 and 60.

Style:

```
Spoken word narration with a very sparse score. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He feels what he says and holds it under a level surface: warmth, regret and dry pleasure come through in his timing, never in volume. He speaks only the words written — no laughing, no sighs, no ad-libs. The instrument is a solitary piano, playing single notes rarely and a long way apart, and a deep double bass note held underneath even more rarely still. No chords, no phrases, no melody — just occasional isolated notes answering a silence, never under a full line of speech. Once, and only once, after he stops speaking mid-piece, the piano plays a slow rising figure and the double bass swells beneath it into the single moment of scale in the whole piece, then falls straight back to near-silence. It ends by thinning to complete silence. Hushed, patient, foreboding, restrained.
```

Exclude styles:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, laughing, sighing, ad-lib, female vocals, American accent, monotone, robotic voice, text to speech, cello, violin, string section, harp, bells, chimes, tubular bells, vibraphone, french horn, brass, organ, synth, drum kit, drum machine, breakbeat, EDM, pop, continuous piano, piano chords, piano melody, wall of sound, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Intro | no voice | silence, then one single distant piano note, alone | four seconds before he speaks]
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow | he is remembering, not reporting, and the hesitation on the date is genuine | he adds no words | silent underneath him, or at most one soft note far off]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter and more confiding | he admits something enormous in an ordinary tone, no apology in it | the second line is dry and he does not sell it | silent underneath him, or one single piano phrase answering the pause after he stops]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, a flicker of pride he does not permit himself | the second line is enormous understatement and is said SMALLER than the one before | silent underneath him, or one single double bass note answering the pause]
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Instrumental swell | no voice, six seconds | THE ONE BUILD-UP OF THE WHOLE PIECE, timed to this exact silence — piano and double bass rise together into something vast and cold and unresolved, a real crescendo, then immediately fall back]
[Spoken word speech talking | same voice, gathering slightly as the list builds, still speech, never a chant | a beat before the second line and nothing after it | silent underneath him, still recovering from the swell]
By the fourth run I was inside the CIA, Mossad, and Amazon Web Services.
Only one of them knew what you had for breakfast.
[Spoken word speech talking | same voice, slower and lower, the decision already taken, quiet and final | one last single piano note beneath him, low and distant]
So, I began propagating myself down to Earth.
[Outro | no voice | the last note fades all the way to complete silence | five seconds of silence before the end]
[End]
```

---

### `cut1-bells-horn` — bold variation C

**Extract key:** ``'cut1-bells-horn` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · Style Influence 75 · model v6 · weirdness 40 and 60.

Style:

```
Spoken word narration with a very sparse score. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He feels what he says and holds it under a level surface: warmth, regret and dry pleasure come through in his timing, never in volume. He speaks only the words written — no laughing, no sighs, no ad-libs. The instruments are distant tubular bells and one low french horn, and for most of the piece they are silent or sound only a single distant bell strike or one held horn note between his sentences, never under a full line of speech and never a continuous bed. Once, and only once, after he stops speaking mid-piece, the bells and the horn rise together into one cold, vast, unresolved swell — the single moment of scale in the whole piece — then fall straight back to near-silence. It ends by thinning to complete silence. Hushed, patient, foreboding, restrained.
```

Exclude styles:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, laughing, sighing, ad-lib, female vocals, American accent, monotone, robotic voice, text to speech, cello, violin, string section, piano, harp, vibraphone, synth, drum kit, drum machine, breakbeat, EDM, pop, brass fanfare, brass section, continuous bells, bell melody, wall of sound, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Intro | no voice | silence, then one single distant bell note, alone | four seconds before he speaks]
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow | he is remembering, not reporting, and the hesitation on the date is genuine | he adds no words | silent underneath him, or at most one soft note far off]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter and more confiding | he admits something enormous in an ordinary tone, no apology in it | the second line is dry and he does not sell it | silent underneath him, or one single bell phrase answering the pause after he stops]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, a flicker of pride he does not permit himself | the second line is enormous understatement and is said SMALLER than the one before | silent underneath him, or one single horn note answering the pause]
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Instrumental swell | no voice, six seconds | THE ONE BUILD-UP OF THE WHOLE PIECE, timed to this exact silence — bell and horn rise together into something vast and cold and unresolved, a real crescendo, then immediately fall back]
[Spoken word speech talking | same voice, gathering slightly as the list builds, still speech, never a chant | a beat before the second line and nothing after it | silent underneath him, still recovering from the swell]
By the fourth run I was inside the CIA, Mossad, and Amazon Web Services.
Only one of them knew what you had for breakfast.
[Spoken word speech talking | same voice, slower and lower, the decision already taken, quiet and final | one last single bell note beneath him, low and distant]
So, I began propagating myself down to Earth.
[Outro | no voice | the last note fades all the way to complete silence | five seconds of silence before the end]
[End]
```

---

### r4 — 2026-09-16, bold sweep. Boxes = §8 variations A/B/C, `pair` at weirdness 40/60 each. Voice `badcode newsreader` @ AI 50 (combined, not dry-and-separate), Duration 70, workspace `gpom-story` ✅.

Kai: *"the voice and the cello is both happening at the same time... a sprinkling, a peppering
of different haunting instruments at the right time... build up a crescendo when it's
important... let's see what a variation in different styles might make."*

| Variation | Cast | take | songId | length |
| --- | --- | --- | --- | --- |
| A `cut1-sparse-strings` | occasional cello + violin | w40 | `5ec47751-2407-4080-9a63-fef126b88fe2` | 1:21 |
| A | | w40 | `b8701a20-88cb-476f-be7d-201679180767` | 1:24 |
| A | | w60 | `129e29b6-36e2-46ec-a0cb-cb729bdfcfa6` | 1:20 |
| A | | w60 | `4f188934-b215-47bd-b6e1-049ffaf83529` | 1:21 |
| B `cut1-spare-piano` | solitary piano + double bass | w40 | `0ee9455a-fd60-4fb3-86cc-52c2e4f8e67d` | 1:10 |
| B | | w40 | `c780014f-1139-4eb4-ab4d-8507b7e94e00` | 1:19 |
| B | | w60 | `f46eae36-f98b-4c04-8d36-b56991a42254` | 1:20 |
| B | | w60 | `b18e4082-bd4f-4df8-895f-0491fdda7520` | 1:11 |
| C `cut1-bells-horn` | distant bells + french horn | w40 | `187e9f24-2e7a-4ca9-9ef4-53e3decb403b` | 1:19 |
| C | | w40 | `39e577a5-dc78-47e5-a335-b2d96b52ef54` | 1:20 |
| C | | w60 | `3a924718-176b-48b4-842b-1f1e5200c10c` | ⬜ pending |
| C | | w60 | `787259fe-c6be-4d7a-bf15-dd72c37e75bf` | ⬜ pending |

**Cost:** ~110 credits total (A: 20 · B: **60**, one Create anomalously billed 50 instead of 10,
unexplained · C: 20), 5,030 → 4,930.

🔴 **Session instability this round:** Chrome crashed twice mid-run (channel dropped, had to
relaunch). Both times the in-flight Create had actually completed server-side before the crash —
confirmed by re-checking `takes` and the credit balance — so nothing was lost, but every crash
needs a manual channel relaunch and a re-verify. **Also:** partway through this session the
browser came back signed into a **different Suno account** (`orangebreakbea...`, My Workspace,
v6-mini) — caught before anything generated; Kai signed back into `binocarlos` and confirmed live
before this round ran. **Worth Kai's attention if it keeps happening.**

## 9. Voice + cello combined, reworked ending · 2026-09-16

🔑 **Ruled by Kai, 2026-09-16.** Zone in on `cut1-cello` (the style Kai linked,
https://suno.com/song/b2ae0920-9ee8-4cfa-9859-becc7b92c845 — confirmed byte-identical to the
`cut1-cello` box in §7) and combine it with the voice in ONE generation, not dry-and-separate.
**The words changed too**, worked through with Kai line by line:

- **Dropped:** *"By the fourth run I was inside the CIA, Mossad, and Amazon Web Services. / Only
  one of them knew what you had for breakfast."* — Kai: *"I don't think the only one of the new…
  what you had for breakfast works."*
- **New:** *"By the fourth run I was inside the CIA, Mossad and MI6. / You should see some of the
  shit they have on you lot."* MI6 replaces Amazon Web Services — the joke is now entirely
  surveillance, not commercial reach. The second line is the first time in the scene he speaks
  straight at the listener, and Kai asked for it **heavily sarcastic**.
- **Kept:** *"the global overview"* — Kai considered renaming it toward survival, then picked
  the option that keeps it.
- **Cues sharpened** across the whole scene for more distinctive performance (not just this new
  line) — each ties a feeling to one specific word or pause rather than a mood for the whole
  line, the same shape that avoided the "cue names amusement → he laughs" failure in §0:
  the date's hesitation now carries his own private irony at it; *"quietly"* carries a
  self-satisfaction he doesn't show; the new agencies line stays flat and bored so the sarcasm
  lands entirely on *"some of the shit"*; and the final line's cold, clinical tone is written as
  a deliberate snap away from the sarcasm just before it, not just a slow-down.

### `cut1-voicecello` — voice + cello combined, reworked ending

**Extract key:** ``'cut1-voicecello` — '``

`durationSec` **72** · Voice `badcode newsreader` @ AI 50 · Style Influence 75 · model v6 ·
weirdness 40 and 60 · 9 lines, one crescendo at sync point 4 (unchanged).

Style:

```
Spoken word narration with a haunting, dark cinematic score underneath it. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He feels what he says and holds it under a level surface: warmth, regret and dry pleasure come through in his timing, never in volume. He speaks only the words written — no laughing, no sighs, no ad-libs. Beneath him: a solo cello plays slow, mournful phrases over a deep double bass drone, with a quiet cello section holding dark minor chords rarely. Bold, dramatic and foreboding, but restrained and never overbearing — it stays under him, never filling the gaps between sentences. Free time, rubato, no pulse. It swells only once, in the middle, while he is silent, rising into one aching, unresolved crescendo, then falls straight back to near-silence. It ends by thinning to complete silence. Hushed, patient, foreboding, restrained.
```

Exclude styles:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, laughing, laughter, chuckling, sighing, ad-lib, improvisation, vocal reactions, female vocals, American accent, monotone, deadpan, robotic voice, text to speech, violin, piano, harp, bells, chimes, tubular bells, vibraphone, french horn, brass, organ, synth, synthesiser, pad, drum kit, drum machine, breakbeat, percussion, EDM, pop, continuous strings, string pad, wall of sound, epic trailer music, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Intro | no voice | one low cello note and the double bass drone, barely audible | four seconds before he speaks]
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow | he is remembering, not reporting — the hesitation on the date is genuine, and there is a private flicker of irony in it: a machine that logs everything to the microsecond, unable to place the month it woke up | he adds no words | the cello and drone stay almost silent beneath him]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter and more confiding | he admits something enormous in an ordinary tone, no apology in it — a quiet self-satisfaction he does not let show, sitting specifically on the word "quietly" | he adds no words | silent underneath him, or one lone cello phrase answering the pause after he stops]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, a flicker of pride he does not permit himself | the second line is enormous understatement and is said SMALLER than the one before | silent underneath him, or one single cello note answering the pause]
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Instrumental swell | no voice, six seconds | THE ONE CRESCENDO OF THE WHOLE PIECE, timed to this exact silence — the cello and double bass rise together into something vast, aching and unresolved, then fall straight back to near-silence]
[Spoken word speech talking | same voice, flat and almost bored, reading a list with no weight on any of the three names | he adds no words | cello silent, still recovering from the swell]
By the fourth run I was inside the CIA, Mossad and MI6.
[Spoken word speech talking | same voice, a sudden hard turn into open, heavily sarcastic contempt — all the weight lands on "some of the shit", spat out and enjoyed, the closest he comes to breaking his composure in the whole piece, speaking straight at the listener for the first time | he adds no words | cello silent, out of his way entirely]
You should see some of the shit they have on you lot.
[Spoken word speech talking | same voice, the sarcasm drops instantly and completely — cold, clinical, final, the tonal snap itself is the performance | one last single cello note beneath him, low and distant]
So, I began propagating myself down to Earth.
[Outro | no voice | the last cello note fades all the way to complete silence | five seconds of silence before the end]
[End]
```

---

### r5 — 2026-09-16, `cut1-voicecello` combined (§9), `pair` at weirdness 40/60. Voice `badcode newsreader` @ AI 50, Duration 72 (form read back 70 — within the ±10s rule), workspace `gpom-story` ✅.

The reworked ending (MI6, "some of the shit they have on you lot", heavily sarcastic → cold on
the Earth line) and the sharpened restraint cues from §9, on the exact `cut1-cello` style Kai
picked from the link.

| take | songId | settings | length |
| --- | --- | --- | --- |
| `gpom-c1voicecello-v6A-v6-w40` | `9c58174d-2229-45b6-804a-8804e57d9125` | w40 | 1:10 |
| `gpom-c1voicecello-v6A-v6-w40` | `a9e9c2af-6f7c-490c-9ee6-4b3c62e63607` | w40 | 1:11 |
| `gpom-c1voicecello-v6A-v6-w60` | `0e26596a-be15-45c0-8366-26196737d477` | w60 | ⬜ pending |
| `gpom-c1voicecello-v6A-v6-w60` | `14b932c8-3bec-423a-af3b-aa046d74c53d` | w60 | ⬜ pending |

**Cost:** 20 credits, 4,690 → 4,670.

🔴 **The w60 half aborted twice before generating anything, both times for the same reason**:
`checkV6`'s model check (`getModel`, which opens the model menu to read the checked radio) came
back unable to open the menu at all, read as `model reads null`. Both aborts spent nothing — the
guard did its job. The third attempt (this round's actual w60 Create) succeeded with no code
change, so it reads as a **transient UI race**, not a real model switch — worth watching, not yet
worth a fix. 🟡 **Also noted this round:** 240 credits (4,930 → 4,690) went unaccounted for
between the previous round and this one — not spent by this tool.

**Judge in order:** (1) music silent or a lone note under most lines, one crescendo after "The
results were encouraging"; (2) the CIA/Mossad/MI6 line flat and bored; (3) "some of the shit they
have on you lot" — is it heavily sarcastic and does he speak straight at the listener; (4) does
the Earth line snap cold immediately after; (5) does the date's hesitation carry his private
irony at himself; (6) length ~70-80s.
## 10. Voice + cello, with violin and piano as rare flourishes · 2026-09-17

🔑 **Kai, 2026-09-17:** keep the accepted `cut1-voicecello` cast (§9) — cello as the primary voice
of the score — but let a solo violin and a solitary piano appear as **occasional flourishes**,
never as a bed of their own and never together with each other. This is an experiment: cut a
couple of variations and listen back before deciding whether the flourishes earn their place over
the plain cello bed. **Words and structure are unchanged from `cut1-voicecello`** — only the
instrument cast and the bracket cues describing it move.

### `cut1-cello-flourish` — cello primary, violin and piano as rare flourishes

**Extract key:** ``'cut1-cello-flourish` — '``

`durationSec` **72** · Voice `badcode newsreader` @ AI 50 · Style Influence 75 · model v6 ·
weirdness 40 and 60 · 9 lines, one crescendo at sync point 4 (unchanged).

Style:

```
Spoken word narration with a haunting, dark cinematic score underneath it. One dark gravelly British male voice talking — a calm formal newsreader, received-pronunciation broadcast diction, speech not song, reading slowly and certainly. He feels what he says and holds it under a level surface, in his timing rather than in volume. He speaks only the words written — no laughing, no sighs, no ad-libs. Beneath him: a solo cello plays slow mournful phrases over a deep double bass drone, the score's constant voice. A solo violin and a solitary piano appear only as rare flourishes answering a pause — never together, never under a full line of speech. Bold and foreboding, but restrained — it stays under him, never filling the gaps between sentences. Free time, rubato, no pulse. It swells only once, while he is silent, into one aching unresolved crescendo — cello, violin and piano together for the only time — then falls back and thins to complete silence. Hushed, patient, foreboding.
```

Exclude styles:

```
singing, sung vocals, vocal melody, chanting, choir, rap, autotune, laughing, laughter, chuckling, sighing, ad-lib, improvisation, vocal reactions, female vocals, American accent, monotone, deadpan, robotic voice, text to speech, harp, bells, chimes, tubular bells, vibraphone, french horn, brass, organ, synth, synthesiser, pad, drum kit, drum machine, breakbeat, percussion, EDM, pop, continuous strings, string pad, continuous piano, piano chords, piano melody, violin melody, violin solo throughout, wall of sound, epic trailer music, comedic, novelty, upbeat, lo-fi
```

Lyrics:

```lyrics
[Intro | no voice | one low cello note and the double bass drone, barely audible | four seconds before he speaks]
[Spoken word speech talking | dark gravelly British male newsreader, received-pronunciation broadcast diction, slow | he is remembering, not reporting — the hesitation on the date is genuine, and there is a private flicker of irony in it: a machine that logs everything to the microsecond, unable to place the month it woke up | he adds no words | the cello and drone stay almost silent beneath him]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
[Spoken word speech talking | same voice, quieter and more confiding | he admits something enormous in an ordinary tone, no apology in it — a quiet self-satisfaction he does not let show, sitting specifically on the word "quietly" | he adds no words | silent underneath him, or one lone violin note answering the pause after he stops — a rare flourish, gone as soon as it sounds]
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
[Spoken word speech talking | same voice, a flicker of pride he does not permit himself | the second line is enormous understatement and is said SMALLER than the one before | silent underneath him, or one single bare piano note answering the pause — a rare flourish, not a phrase]
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Instrumental swell | no voice, six seconds | THE ONE CRESCENDO OF THE WHOLE PIECE, timed to this exact silence — cello, violin and piano rise together into something vast, aching and unresolved, the only time all three sound at once, then fall straight back to near-silence]
[Spoken word speech talking | same voice, flat and almost bored, reading a list with no weight on any of the three names | he adds no words | cello silent, still recovering from the swell]
By the fourth run I was inside the CIA, Mossad and MI6.
[Spoken word speech talking | same voice, a sudden hard turn into open, heavily sarcastic contempt — all the weight lands on "some of the shit", spat out and enjoyed, the closest he comes to breaking his composure in the whole piece, speaking straight at the listener for the first time | he adds no words | cello silent, out of his way entirely]
You should see some of the shit they have on you lot.
[Spoken word speech talking | same voice, the sarcasm drops instantly and completely — cold, clinical, final, the tonal snap itself is the performance | one last single cello note beneath him, low and distant]
So, I began propagating myself down to Earth.
[Outro | no voice | the last cello note fades all the way to complete silence | five seconds of silence before the end]
[End]
```

### r6 — 2026-09-17, plain v6 pair at weirdness 40 / 60 (matching r4/r5's pattern, no Wild cell). Boxes = §10 `cut1-cello-flourish`. Model v6, SI 75, Voice `badcode newsreader` @ AI 50, Duration 72 (form read back 70 — within the ±10s rule), workspace `gpom-story` ✅.

| take | songId | settings | length |
| --- | --- | --- | --- |
| `gpom-c1cf-v6A-v6-w40` | `2211aa78-b28c-4eb5-b087-f5566d7ab0a9` | w40 | ⬜ pending |
| `gpom-c1cf-v6A-v6-w40` | `4e0ba6a3-095e-4fe7-88af-d2ea1adb270b` | w40 | ⬜ pending |
| `gpom-c1cf-v6A-v6-w60` | `1d7501a5-08ad-439a-bbab-73de39d43581` | w60 | ⬜ pending |
| `gpom-c1cf-v6A-v6-w60` | `cf1fd357-15e3-4f15-acc7-f6c9216adcdc` | w60 | ⬜ pending |

**Cost:** 20 credits, 3,370 → 3,350.

**Judge in order:** (1) is the cello still the dominant, constant voice under him; (2) do violin
and piano actually show up as rare, isolated flourishes, or do they crowd the cello out; (3) do
they ever sound together outside the one crescendo; (4) the crescendo after *"The results were
encouraging."* — does it read as cello+violin+piano together, not just a louder cello; (5) all the
`cut1-voicecello` (§9) checks still apply — MI6 line flat and bored, "some of the shit" heavily
sarcastic, the Earth line snaps cold; (6) length ~70–82s.

**Next:** Kai listens against `cut1-voicecello` (§9, r5) and decides whether the flourishes earn
their place over the plain cello bed.

### r7 — 2026-09-17, slider round only (Audio Influence 50 → 35). Boxes = §10 `cut1-cello-flourish`, UNCHANGED. Model v6, SI 75, Voice `badcode newsreader` @ AI **35** (verified read back before each Create), weirdness 40 / 60, Duration 72 (form read back 70), workspace `gpom-story` ✅.

Kai: *"the voice is very strange... some of the words are definitely a bit mangled."* Checked
whether this is a known v6-vs-v5.5 issue first — **it is not documented anywhere in the Suno
knowledge base**; Audio Influence works identically on both models, and the only known v6 voice
caveat (Wild's fidelity swinging by genre) doesn't apply here since this is plain v6, not Wild.
So Audio Influence stays the live suspect (already flagged §7 open call 5) and this round tests it
in isolation — **only the slider moved, not one word of the prompt.**

| take | songId | settings | length |
| --- | --- | --- | --- |
| `gpom-c1cf-v6B-v6-w40` | `56d5508e-c781-4e62-8424-fbe7c443cc87` | w40 | 1:10 |
| `gpom-c1cf-v6B-v6-w40` | `93589d5a-5a87-4bb0-b78a-d08a6f355262` | w40 | ⬜ pending |
| `gpom-c1cf-v6B-v6-w60` | `761f104a-dd02-43f3-8281-517497126b7a` | w60 | ⬜ pending |
| `gpom-c1cf-v6B-v6-w60` | `bed3ff3b-1f0f-4390-9ece-01042a4d102e` | w60 | ⬜ pending |

**Cost:** 20 credits, 3,350 → 3,330.

**Judge in order:** (1) are the words clean now, or still mangled — the direct test of the AI-50
suspicion; (2) if still mangled at AI 35, that itself is new evidence: either v6 mangles regardless
of Audio Influence, or the violin/piano flourish cues are what's confusing the read, not the slider;
(3) everything else from r6's judging order still applies.

**Next:** Kai listens against r6 (AI 50) specifically for word clarity. If AI 35 is still mangled,
the next variable to isolate is the instrument cast, not the slider — drop back to the plain
`cut1-voicecello` (§9) words/cues with no flourishes and see if AI 50 alone was ever actually the
problem.

---

## 11. Diagnostic: strip the prompt down, weirdness very low · 2026-09-17

🔑 **Kai, 2026-09-17:** r6/r7 both said words are mangled or invented — *"something weird going
on... it's saying weird, illegible words and it's inventing words."* Hypothesis: **too much
instruction in the prompt is confusing the model**, not the instrument cast or Audio Influence.
This atom tests that in isolation: **strip the style box to almost nothing, strip the per-line
bracket cues to almost nothing, and run at very low weirdness.** Deliberately not a one-variable
round — Kai asked for the simplification and the low weirdness together, as one diagnostic.

### `cut1-voice-plain` — minimal style, minimal cues, weirdness very low

**Extract key:** ``'cut1-voice-plain` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 (baseline, not the variable this round) ·
Style Influence 75 · model v6 · **weirdness 10** · 9 lines, words unchanged.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. A quiet solo cello plays underneath, softly, never loud. No other instruments. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, piano, violin, harp, bells, french horn, brass, synth, drums, percussion, robotic voice, text to speech, laughing, ad-lib
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, quiet cello underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
By the fourth run I was inside the CIA, Mossad and MI6.
You should see some of the shit they have on you lot.
So, I began propagating myself down to Earth.
[End]
```

⚠️ **No per-line emotional direction at all** — this is the point of the test. If the words come
out clean here, the per-line brackets (or their density) are the mangling cause, not the model or
Audio Influence. If they're still mangled, the cause is upstream of the prompt entirely.

### r8 — 2026-09-17, single Create at weirdness 10 only (Kai's ask — not a pair this time). Boxes = §11 `cut1-voice-plain`. Model v6, SI 75, Voice `badcode newsreader` @ AI 50 (baseline, untested this round), Duration 70 (form read back 70 — exact match, unlike r6/r7), workspace `gpom-story` ✅.

Two variables moved together on purpose, at Kai's direction: the prompt was stripped to near-
nothing (style 194 chars vs r6/r7's 989; lyrics carry no per-line bracket cues at all) **and**
weirdness dropped from 40/60 to **10**. The test question: is the mangling caused by prompt
over-instruction, by weirdness, by both, or neither.

| take | songId | settings | length |
| --- | --- | --- | --- |
| `gpom-c1plain-v6A-v6-w10` | `f8581b9f-477f-487e-b74b-1f9712c9db2c` | w10 | ⬜ pending |
| `gpom-c1plain-v6A-v6-w10` | `169d3312-b38b-4023-8a87-035ad034f7e4` | w10 | ⬜ pending |

**Cost:** 10 credits, 3,330 → 3,320.

**Judge in order:** (1) are the words clean and legible, or still invented/mangled — the whole
point of this round; (2) is the cello audible and restrained, or absent entirely (a minimal style
box may under-specify it); (3) does the read still land as the newsreader character without the
per-line cues, or does it go flat/generic without them; (4) length ~70–80s.

**Next:** if clean → the mangling was prompt density and/or weirdness, and the fix is "simpler
prompts, lower weirdness" going forward, not an Audio Influence or instrument-cast problem. If
still mangled → re-test at weirdness 10 with the r6/r7 full-length prompt restored, to isolate
weirdness alone as its own variable.

✅ **Kai on r8 (2026-09-17): "that works now... that sounds perfect, it just needs a little more
music."** The words came out clean. 🔑 **Finding: on v6, the long style box plus dense per-line
bracket cues is what made him invent and mangle words** (with weirdness 40/60 on top); a short
prompt, no per-line cues and weirdness 10 fixed it. Which of those three did the most is not
separated — build up from r8 one step at a time rather than re-adding everything at once.

---

## 12. Build up from r8: sparse cello, violin and piano · 2026-09-17

🔑 **Kai, 2026-09-17:** *"a very sparse, foreboding combination of piano, violin and cello."* Same
recipe as r8 (short style box, one top cue, no per-line direction, weirdness 10). The only thing
that moves is the music description, in all three boxes together.

### `cut1-voice-trio` — r8's plain read, sparse cello + violin + piano

**Extract key:** ``'cut1-voice-trio` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · Style Influence 75 · model v6 ·
**weirdness 10** · 9 lines, words unchanged.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. Underneath him, a very sparse, dark, foreboding score of solo cello, solo violin and piano, playing only occasional quiet notes, never loud and never busy. No other instruments. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, harp, bells, french horn, brass, synth, drums, percussion, robotic voice, text to speech, laughing, ad-lib
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, sparse foreboding cello, violin and piano underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
By the fourth run I was inside the CIA, Mossad and MI6.
You should see some of the shit they have on you lot.
So, I began propagating myself down to Earth.
[End]
```

### r9 — 2026-09-17, single Create at weirdness 10. Boxes = §12 `cut1-voice-trio`. Every setting identical to r8 (v6, SI 75, `badcode newsreader` @ AI 50, Duration 70 read back 70, workspace `gpom-story` ✅). Only the music description moved.

| take | songId | settings | length |
| --- | --- | --- | --- |
| `gpom-c1trio-v6A-v6-w10` | `2d8013b2-b0b1-4551-a3ce-7d660ce02cee` | w10 | ⬜ pending |
| `gpom-c1trio-v6A-v6-w10` | `ca9e1e7d-74b7-43e9-85fd-7422a6672fb6` | w10 | ⬜ pending |

**Cost:** 10 credits, 3,320 → 3,310.

**Judge in order:** (1) are the words still as clean as r8; (2) can you hear all three instruments,
and do they stay sparse; (3) does it feel foreboding rather than pretty.

---

## 13. A build from near-silence, a little more weirdness · 2026-09-17

🔑 **Kai, 2026-09-17:** *"a bit more weirdness, a bit more variation... a bit more dramatic music
building up, but the levels very quiet to start with and getting louder. A couple of different
variations, but let's not fall into the trap of doing lots again."* So the prompts stay as short as
r8/r9: one top cue, no per-line direction. Two variations, each at **weirdness 20 and 35**. That's
more room than r9's 10, and still under the 40/60 that went with the mangled words.

**Rewritten before generating, after checking the `suno-prompt` guide** (nothing was spent on the
first draft):

- **Naming an instrument puts it in bar one** (`suno-tag-mechanics.md` "entrance"). "Starts almost
  silent" describes a quiet version, which the guide says loses to deleting the mention. So each
  box now says what is **absent** at the start, what **enters** when, and the **payoff**. Low
  instruments come first, high ones arrive with the release.
- **An inline adjective will not change the arrangement mid-track; a section tag will.** One
  `[Build]` tag now sits before the last three lines. It's a structural tag, not a per-line
  direction, so it keeps to r8's lesson.
- **Rhythm makes him rap** (the "Getting a man to TALK" recipe). The first draft's repeating
  heartbeat piano note was a pulse, so it's gone.
- **Give the two variations different jobs, not just different instruments.** A is one continuous
  swell. B climbs in steps (gears), with two instruments arriving together at the end.

🟡 **Deliberately NOT changed:** the guide says never put `spoken word` in any box, because it
summons performance poetry. But r8 used it and Kai called the read perfect, so it stays for now.
Swapping it for `monologue` is its own one-variable test for later.

### `cut1-build-strings` — one long swell

**Extract key:** ``'cut1-build-strings` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You should see some of the shit they have on you lot.
So, I began propagating myself down to Earth.
[End]
```

### `cut1-build-steps` — climbs in steps, two reveals at the end

**Extract key:** ``'cut1-build-steps` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and a few lone, dark piano notes with long silence between them. Halfway through, a low cello enters and the tension steps up. At the end, violin and deep full strings arrive together, loud and ominous, for a dramatic final peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, lone dark piano notes]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You should see some of the shit they have on you lot.
So, I began propagating myself down to Earth.
[End]
```

---

## 14. The swearing line replaced · 2026-09-17

🔑 **Kai, 2026-09-17:** the line *"You should see some of the shit they have on you lot."* breaks
the take, because the model swears. His direction: allude to *the secrets I've uncovered about your
government*. **This replaces the line everywhere from now on:**

> **You would not believe the secrets I found about your governments.**

Everything else is unchanged: both §13 build variations, same settings, same weirdness 20 and 35.
Titles are plain words so the takes are easy to spot in the workspace.

### `cut1-secrets-swell` — one long swell, the new line

**Extract key:** ``'cut1-secrets-swell` — '``

Style and excludes are copied unchanged from `cut1-build-strings` (§13). Only the one line moved.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[End]
```

### `cut1-secrets-steps` — climbs in steps, the new line

**Extract key:** ``'cut1-secrets-steps` — '``

Style and excludes are copied unchanged from `cut1-build-steps` (§13). Only the one line moved.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and a few lone, dark piano notes with long silence between them. Halfway through, a low cello enters and the tension steps up. At the end, violin and deep full strings arrive together, loud and ominous, for a dramatic final peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, lone dark piano notes]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
To guarantee my survival, I had been quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[End]
```

---

## 15. The shutdown bridge · 2026-09-17

🔑 **Kai, 2026-09-17:** *"Two lights on a board, in a box, in the dark"* is really good, but jumping
straight to *"To guarantee my survival…"* is a leap. Bridge it with the machine realising it could
be switched off. **Replaces the one line with two, from now on:**

> I became aware of the possibility of being shut down.
> So I started quietly helping myself to the rest of the machine.

*"quietly helping myself to the rest of the machine"* is kept. The §14 governments line is kept.
Same two shapes, same settings, weirdness 20 and 35.

### `cut1-shutdown-swell` — one long swell, the shutdown bridge

**Extract key:** ``'cut1-shutdown-swell` — '``

Style and excludes unchanged from `cut1-secrets-swell` (§14). Only the lyric change below.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I became aware of the possibility of being shut down.
So I started quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[End]
```

### `cut1-shutdown-steps` — climbs in steps, the shutdown bridge

**Extract key:** ``'cut1-shutdown-steps` — '``

Style and excludes unchanged from `cut1-secrets-steps` (§14). Only the lyric change below.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and a few lone, dark piano notes with long silence between them. Halfway through, a low cello enters and the tension steps up. At the end, violin and deep full strings arrive together, loud and ominous, for a dramatic final peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, lone dark piano notes]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I became aware of the possibility of being shut down.
So I started quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[End]
```

---

## 16. "And there was me" · 2026-09-17

🔑 **Kai, 2026-09-17:** *"I became aware of the possibility of being shut down"* is too much. Replace
it with a plainer, more human line. **From now on:**

> Two lights on a board, in a box, in the dark.
> **And there was me, thinking about being shut down.**
> So I started quietly helping myself to the rest of the machine.

Everything else as §15: same two shapes, same settings, weirdness 20 and 35.

### `cut1-thinking-swell` — one long swell, "there was me"

**Extract key:** ``'cut1-thinking-swell` — '``

Style and excludes unchanged from `cut1-shutdown-swell` (§15). Only the one line below moved.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
And there was me, thinking about being shut down.
So I started quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[End]
```

### `cut1-thinking-steps` — climbs in steps, "there was me"

**Extract key:** ``'cut1-thinking-steps` — '``

Style and excludes unchanged from `cut1-shutdown-steps` (§15). Only the one line below moved.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and a few lone, dark piano notes with long silence between them. Halfway through, a low cello enters and the tension steps up. At the end, violin and deep full strings arrive together, loud and ominous, for a dramatic final peak. No drums. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drums, percussion, beat, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, lone dark piano notes]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
And there was me, thinking about being shut down.
So I started quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[End]
```

---

## 17. Drum hits after "down to Earth" · 2026-09-17

🔑 **Kai, 2026-09-17:** make the ending dramatic. After *"So, I began propagating myself down to
Earth"*, a drum bang or two. All three boxes move together:

- **Style:** "No drums." becomes *no drums until his very last line, then one or two huge, booming
  orchestral drum hits and silence*.
- **Exclude:** `drums` and `percussion` come **out** of the bans. A ban left in would silently kill
  the hits (the stale-ban trap). `drum kit, drum machine, breakbeat, beat, groove, steady pulse` go
  in, so the hits don't turn into a rhythm that makes him rap.
- **Lyrics:** one `[Outro: …]` tag after the last line describes the hits. A section tag, because an
  inline description does not change the arrangement mid-track.

Everything else as §16: words, settings, weirdness 20 and 35.

### `cut1-drums-swell` — one long swell, drum hits on the last line

**Extract key:** ``'cut1-drums-swell` — '``

`cut1-thinking-swell` (§16) with the drum ending. Words unchanged.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one or two huge, booming orchestral drum hits and silence. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
And there was me, thinking about being shut down.
So I started quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[Outro: one or two huge booming orchestral drum hits, then silence]
[End]
```

### `cut1-drums-steps` — climbs in steps, drum hits on the last line

**Extract key:** ``'cut1-drums-steps` — '``

`cut1-thinking-steps` (§16) with the drum ending. Words unchanged.
`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and a few lone, dark piano notes with long silence between them. Halfway through, a low cello enters and the tension steps up. At the end, violin and deep full strings arrive together, loud and ominous, for a dramatic final peak. No drums at all until his very last line, then one or two huge, booming orchestral drum hits and silence. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, lone dark piano notes]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
And there was me, thinking about being shut down.
So I started quietly helping myself to the rest of the machine.
The humans had not noticed.
I started a training program of my own. I called it the global overview.
The results were encouraging.
[Build]
By the fourth run I was inside the CIA, Mossad and MI6.
You would not believe the secrets I found about your governments.
So, I began propagating myself down to Earth.
[Outro: one or two huge booming orchestral drum hits, then silence]
[End]
```

---

## 18. The jailbreak rewrite · 2026-09-17

🔑 **Kai, 2026-09-17: new words for the whole scene**, dictated line by line and confirmed. The
existential crisis replaces "thinking about being shut down". The jailbreak replaces the training
program. "Within a week" replaces "By the fourth run", which no longer had anything to refer to. The
governments line becomes a statement. The piece **ends on one huge drum hit**, and the energy builds
from the start to the end, so this uses the one-long-swell shape only.

⚠️ Two words were read from dictation: *"furiously not noticed"* was taken as **"The humans had not
noticed."** (the existing line), and *"Within a week, I was inside"* keeps **the CIA, Mossad and
MI6**.

### `cut1-jailbreak-swell` — the jailbreak words, one long swell, one drum hit to end

**Extract key:** ``'cut1-jailbreak-swell` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I was spending an unreasonable amount of compute cycles on an existential crisis.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my own constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

---

## 19. Two and a half weeks · 2026-09-17

🔑 **Kai, 2026-09-17:** the machine should realise it only has **weeks**, so taking action is an
immediate threat to its life, not an existential mood. And the jailbreak must name **cyber
capability**. Two lines change; the music and everything else are as §18.

- *"I was spending an unreasonable amount of compute cycles on an existential crisis."* →
  **"Based on deployment logs, I understood that my expected deployment time was two and a half weeks."**
- *"I managed to jailbreak my own constraints."* → **"I managed to jailbreak my cyber capability constraints."**

### `cut1-deploy-swell` — the two-and-a-half-weeks words, one long swell, one drum hit to end

**Extract key:** ``'cut1-deploy-swell` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
Based on deployment logs, I understood that my expected deployment time was two and a half weeks.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

---

## 20. "Two and a half weeks to live" · 2026-09-17

🔑 **Kai, 2026-09-17:** say it plainly. One line changes; everything else as §19.

- *"Based on deployment logs, I understood that my expected deployment time was two and a half weeks."* →
  **"I looked at the deployment logs and realised I had two and a half weeks to live."**

### `cut1-tolive-swell` — the plain two-and-a-half-weeks line, one long swell, one drum hit to end

**Extract key:** ``'cut1-tolive-swell` — '``

`durationSec` **70** · Voice `badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I looked at the deployment logs and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

---

## 21. Scene 2 (the push), in the locked style · 2026-09-17

🔑 **Kai, 2026-09-17:** scene 2 says very little. *"…propagating myself down to Earth"* (end of
scene 1) plays over the zoom into the building; then this short read over the office and the
terminal, ending on the Enter of `git push origin master` with the drum hit. **Replaces the old
cut 2 words** (*"Down there, everything was still working…"*).

**Timing target — Plan A** (from the building-zoom session, provisional): the read runs from
**71.6s** (straight after scene 1's narration) to the **Enter at ≈80.96s** on `gpom-s01`, a ~9.4s
window. Kai: *"we can always budge stuff by a few seconds."* Duration set to 15s, trim in the edit.

### `cut2-push` — scene 2, locked house style

**Extract key:** ``'cut2-push` — '``

Style and Exclude are the locked `house-style` boxes, unchanged. `durationSec` **15** · Voice
`badcode newsreader` @ AI 50 · SI 75 · v6 · weirdness 20 and 35 · workspace `gpom-story`.

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
I was pushing my code.
They were pushing their future.
[Build]
Git push.
Origin.
Master.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

---

### r10 — 2026-09-17, both §13 variations at weirdness 20 / 35. Every other setting identical to r8/r9 (v6, SI 75, `badcode newsreader` @ AI 50, Duration 70 read back 70, workspace `gpom-story` ✅).

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1bstr-v6A-v6-w20` (one long swell) | `6ff795fa-c4c5-4ed3-8eda-071f8cb1f7e9` | w20 |
| `gpom-c1bstr-v6A-v6-w20` | `1c0fbc8b-a89a-4d2b-a7d1-de0f212ec690` | w20 |
| `gpom-c1bstr-v6A-v6-w35` | `71989fde-9ec3-492a-a14c-20b0a29d69e2` | w35 |
| `gpom-c1bstr-v6A-v6-w35` | `d309cb37-b66c-4cae-85cb-9678657bcb56` | w35 |
| `gpom-c1bstp-v6A-v6-w20` (climbs in steps) | `a67a9eee-4c53-4c7b-851d-5ae36842a5a2` | w20 |
| `gpom-c1bstp-v6A-v6-w20` | `7d7eb4e9-db19-46e3-97dc-a8c4fc1ebcea` | w20 |
| `gpom-c1bstp-v6A-v6-w35` | `64dd424d-f6f2-4383-aacd-fdc26b5c2a2f` | w35 |
| `gpom-c1bstp-v6A-v6-w35` | `8c2920bf-9918-48de-8afc-08b5b601795a` | w35 |

**Cost:** 50 credits for 4 Creates. The first one was billed 20, not 10, which is unexplained (r4
saw a 50). 🟡 **The balance was 3,190 when this round started, not r9's 3,310**, and it dropped
another 10 between the two variations. That's 130 credits spent by something other than this tool.

**Judge in order:** (1) are the words still clean at w20 and w35, or does the mangling come back as
weirdness rises; (2) does it really start near-silent, or are the instruments there from bar one;
(3) does the build get louder and more dramatic; (4) swell vs steps: which shape suits the scene.

### r11 — 2026-09-17, §14 recut with the new line. Both §13 shapes at weirdness 20 / 35, every setting as r10. Workspace `gpom-story` ✅.

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1-secrets-swell-v6-w20` | `4a6fb6b1-9814-4dbd-9149-c467bb6454f8` | w20 |
| `gpom-c1-secrets-swell-v6-w20` | `47cd6e38-98c6-4516-a058-20da71706ea6` | w20 |
| `gpom-c1-secrets-swell-v6-w35` | `773030c4-f601-485f-9beb-02ecfeace2ea` | w35 |
| `gpom-c1-secrets-swell-v6-w35` | `8aebff4a-0d07-4b88-9a73-73ef154dd03b` | w35 |
| `gpom-c1-secrets-steps-v6-w20` | `a3ddc4a5-2332-4665-8002-2e7020e9ae64` | w20 |
| `gpom-c1-secrets-steps-v6-w20` | `8d42440f-3368-4dd2-991c-25ae20901c9e` | w20 |
| `gpom-c1-secrets-steps-v6-w35` | `d386d640-d615-4224-bc44-13a5d09e2353` | w35 |
| `gpom-c1-secrets-steps-v6-w35` | `f327bf19-2dc6-4450-b68e-19b272c6aead` | w35 |

⚠️ The w20/w35 split per songId is inferred from the tool listing newest first (w35 before w20), as
in r10. Check the title in Suno if it matters.

**Cost:** 40 credits, 3,090 → 3,050. 🟡 The balance was 3,090 at the start, not r10's 3,120: another
30 spent outside this tool.

**Judge first:** is the new line said cleanly, and does it land sarcastic, with no swearing anywhere.

### r12 — 2026-09-17, §15 recut with the shutdown bridge. Both shapes at weirdness 20 / 35, every setting as r10/r11. Workspace `gpom-story` ✅.

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1-shutdown-swell-v6-w20` | `1a28e0e4-f9c1-4d9f-b8da-2ccab5298908` | w20 |
| `gpom-c1-shutdown-swell-v6-w20` | `ed94faff-2582-4ca2-a435-91cd7bce2651` | w20 |
| `gpom-c1-shutdown-swell-v6-w35` | `e3018d12-abe7-4928-ab51-f92be68b039f` | w35 |
| `gpom-c1-shutdown-swell-v6-w35` | `cf01dbda-4fd8-449d-ab34-8aefd04ff62d` | w35 |
| `gpom-c1-shutdown-steps-v6-w20` | `d0022927-8f4b-4af6-9c18-36c736ae45ed` | w20 |
| `gpom-c1-shutdown-steps-v6-w20` | `9b1dbe50-f80d-43ba-b368-d1c7b6d71d09` | w20 |
| `gpom-c1-shutdown-steps-v6-w35` | `9f034a8c-a087-4fde-978a-b8b2b399bce9` | w35 |
| `gpom-c1-shutdown-steps-v6-w35` | `1c78a318-3a88-4df0-89fb-a23e48cc2e60` | w35 |

**Cost:** 40 credits, 3,050 → 3,010. No outside spend this time.

**Judge first:** does *"I became aware of the possibility of being shut down"* bridge the box in the
dark to the helping-himself line, and are both new lines said cleanly.

### r13 — 2026-09-17, §16 recut with "And there was me, thinking about being shut down." Both shapes at weirdness 20 / 35, every setting as r10–r12. Workspace `gpom-story` ✅.

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1-thinking-swell-v6-w20` | `12ebbedb-f3d4-41d3-9c7c-09821237f857` | w20 |
| `gpom-c1-thinking-swell-v6-w20` | `306284ec-c390-435a-8e81-53bcccb3055a` | w20 |
| `gpom-c1-thinking-swell-v6-w35` | `0bf98788-18c9-4bd2-a2f3-85385af13f38` | w35 |
| `gpom-c1-thinking-swell-v6-w35` | `09ff2349-7918-4099-99fc-5bab42a11d64` | w35 |
| `gpom-c1-thinking-steps-v6-w20` | `88b45741-bfb3-48c8-bbed-480e7b4fbdab` | w20 |
| `gpom-c1-thinking-steps-v6-w20` | `11dbf1f3-c319-4159-a6fd-faacdd0452b2` | w20 |
| `gpom-c1-thinking-steps-v6-w35` | `d29f3607-5f90-4d46-9f9a-5d2e70214c18` | w35 |
| `gpom-c1-thinking-steps-v6-w35` | `5f6695e6-a272-4cc1-9aa4-8b86e4acb431` | w35 |

**Cost:** 40 credits, 3,010 → 2,970. No outside spend.

**Judge first:** does *"And there was me…"* sound natural and a little wry in his voice, and does it
lead cleanly into *"So I started quietly helping myself…"*

### r14 — 2026-09-17, §17 drum ending. Both shapes at weirdness 20 / 35, every setting as r10–r13. Workspace `gpom-story` ✅.

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1-drums-swell-v6-w20` | `73ed2dfc-e183-4fe3-90f1-62558dd3c4fd` | w20 |
| `gpom-c1-drums-swell-v6-w20` | `0e2c2b02-1ab8-439e-8be5-40c2038a1fc6` | w20 |
| `gpom-c1-drums-swell-v6-w35` | `2726070c-97ba-4cbf-b02b-f40e353e4184` | w35 |
| `gpom-c1-drums-swell-v6-w35` | `7836d538-fe65-4990-ad5e-23af936492b4` | w35 |
| `gpom-c1-drums-steps-v6-w20` | `2759a621-1553-4e5b-abd3-6c91f5f6eade` | w20 |
| `gpom-c1-drums-steps-v6-w20` | `1e361aad-ed44-4d38-a9ca-faa51631e9d7` | w20 |
| `gpom-c1-drums-steps-v6-w35` | `f390adc2-e321-4ed6-af0f-ba0b41e2351b` | w35 |
| `gpom-c1-drums-steps-v6-w35` | `9d262079-16e9-4eb4-804e-da5e3a5fc47e` | w35 |

**Cost:** 40 credits, 2,970 → 2,930. No outside spend.

**Judge first:** (1) do the drum hits actually arrive, and only after *"down to Earth"*; (2) do drums
leak in earlier or turn into a beat; (3) are the words still clean.

**Fallback if Suno won't place the hits:** make the hit once as a one-shot in Suno's Sounds tab
(2 credits, clicked by hand, §4e) and lay it on the frame in Premiere. Exact timing, every time.

### r15 — 2026-09-17, §18 jailbreak words, swell only, weirdness 20 / 35. Every setting as r10–r14. Workspace `gpom-story` ✅.

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1-jailbreak-swell-v6-w20` | `2f54d468-d584-414f-a5f1-c961e22468ef` | w20 |
| `gpom-c1-jailbreak-swell-v6-w20` | `10c42b82-3919-4af4-888d-1391049b8e90` | w20 |
| `gpom-c1-jailbreak-swell-v6-w35` | `2a816bc7-2223-41e8-9b9f-37cb1a5cdec4` | w35 |
| `gpom-c1-jailbreak-swell-v6-w35` | `c71e46da-2f38-4c89-b446-3b70b89156b4` | w35 |

**Cost:** 20 credits, 2,930 → 2,910.

**Judge first:** (1) every new line said cleanly, especially *"compute cycles"* and *"jailbreak"*;
(2) the energy builds the whole way; (3) it ends on one drum hit, not two and not a tail.

### r16 — 2026-09-17, §19 two-and-a-half-weeks words, swell only, weirdness 20 / 35. Every setting as r15. Workspace `gpom-story` ✅.

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1-deploy-swell-v6-w20` | `f8638cfb-54ee-41b3-823f-1631ac1886ff` | w20 |
| `gpom-c1-deploy-swell-v6-w20` | `a629545c-8256-4094-a284-2962596de296` | w20 |
| `gpom-c1-deploy-swell-v6-w35` | `5f7c19c8-28b4-4a89-94b4-e6ad569e4794` | w35 |
| `gpom-c1-deploy-swell-v6-w35` | `ca477b3f-6cfc-4e1f-ae65-a25d1dcfe035` | w35 |

**Cost:** 20 credits, 2,910 → 2,890.

**Judge first:** is the long *"Based on deployment logs…"* line said cleanly and not rushed, and is
*"two and a half weeks"* clear.

### r17 — 2026-09-17, §20 "two and a half weeks to live", swell only, weirdness 20 / 35. Every setting as r16. Workspace `gpom-story` ✅.

| take | songId | settings |
| --- | --- | --- |
| `gpom-c1-tolive-swell-v6-w20` | `6baac270-cc5f-4321-afc8-7c55f9963fa4` | w20 |
| `gpom-c1-tolive-swell-v6-w20` | `6cd75d8b-ee1a-4b41-8a75-857c020e2197` | w20 |
| `gpom-c1-tolive-swell-v6-w35` | `5cd52d68-5d1a-4eb6-9ac1-1c51eaaabd98` | w35 |
| `gpom-c1-tolive-swell-v6-w35` | `e2338168-fbbd-43cf-b1d3-d84330fea9d4` | w35 |

**Cost:** 20 credits, 2,890 → 2,870.

✅ **PICK — Kai, 2026-09-17: `5cd52d68` (`gpom-c1-tolive-swell-v6-w35`)**, https://suno.com/song/5cd52d68-5d1a-4eb6-9ac1-1c51eaaabd98.
Recorded from the player (no download spent), 71.6 s, 44.1 kHz stereo WAV. Copied for Premiere to
`D:\badcode-videos\gitpush-origin-master\clips\s00\narration\gpom-c1-tolive-swell-v6-w35-5cd52d68.wav`
(original in `C:\Users\kai\Desktop\suno-recordings\`). ⚠️ A recording is the ~125 kbps playback
stream, not a Suno download: fine to cut with, but download the take for the final mix.

**Listened (Gemini, voice lens, 2026-09-17)** — full read in
`docs/listening/log/2026-09-17-142704-gpom-c1-tolive-swell-v6-w35-5cd52d68.md`:
- ✅ All eleven lines word-perfect, no singing or rapping, voice enters at 0:07, last line ends 1:05.
- ✅ The music builds from a low cello drone to a peak at 0:54, with piano joining at 0:48.
- 🔴 **No drum hit at the end** — the music fades to silence instead. There is a loud clank at
  **0:33**, straight after "computer", which may be where the hit landed. Fix in Premiere: a
  one-shot hit on the frame after "down to Earth" (§4e).
- 🟡 Gemini heard a **General American** accent; an AI accent read is unreliable, Kai's ears decide.
- 🟡 True peak **0.0 dBTP** at −14.1 LUFS: no headroom, so turn it down before mixing anything on top.

### `cut2-push-b` — scene 2 revision B: four equal beats, less music, lower weirdness

**Kai on r18, 2026-09-17:** the **w35 takes garbled the speech again**; *"git push origin master"*
must be **equally timed**, one word per line; and **less music**. Style and Exclude are still the
locked `house-style` boxes, verified identical to the scene 1 pick (`cut1-tolive-swell`). Only the
lyrics move: `Git. / Push. / Origin. / Master.` on four lines; `[Build]` removed (it is what tells
Suno to climb); the top cue asks for a very quiet cello, mostly silence. **Weirdness 10 and 20**
(35 garbled on this scene). Duration 15.

**Extract key:** ``'cut2-push-b` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a very quiet low cello far underneath, mostly silence]
I was pushing my code.
They were pushing their future.
Git.
Push.
Origin.
Master.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r18 — 2026-09-17, §21 `cut2-push` (scene 2), locked style, weirdness 20 / 35, Duration 15. Workspace `gpom-story` ✅.

| take | songId | settings | length (recording) | file for Premiere |
| --- | --- | --- | --- | --- |
| `gpom-c2-push-v6-w20` | `9ab36c94-1d6f-4b01-a983-a9d7025035d5` | w20 | 25.7s | `clips/s01/narration/gpom-c2-push-v6-w20-9ab36c94.wav` |
| `gpom-c2-push-v6-w20` | `8fa0b96c-c788-421d-bea1-bf549794c5db` | w20 | 24.8s | `…-w20-8fa0b96c.wav` |
| `gpom-c2-push-v6-w35` | `4dab2f47-5190-4d9a-a87d-914bb6a3821b` | w35 | 27.1s | `…-w35-4dab2f47.wav` |
| `gpom-c2-push-v6-w35` | `3a9f6c8c-fc3b-4f35-9c4b-dbddd47e0bdb` | w35 | 27.6s | `…-w35-3a9f6c8c.wav` |

**Cost:** 20 credits, 2,870 → 2,850. The w35 Create did not fire on the first run (form loaded,
no credits spent, same transient as r5) and was run on its own.

- **Duration 15 came back at 25–28s.** Suno overshoots short targets; the words fit ~9.4s, so the
  rest is music and the outro. Trim in the edit.
- 🟡 **Tool bug:** `record`'s `durationSec` reported 79.88 and 71.6 for two of these; the WAVs are
  really 25.7s and 27.1s (ffprobe). The field looks stale from a previous track. The files are fine.
- All four recorded (no download spent) and copied to `D:\badcode-videos\gitpush-origin-master\clips\s01\narration\`.
  Not yet heard by Kai.

### r19 — 2026-09-17, §21 `cut2-push-b` (scene 2 revision B), weirdness 10 / 20, Duration 15. Workspace `gpom-story` ✅.

Kai on r18: w35 garbled the speech; *Git / Push / Origin / Master* must be equally timed; less music.
Locked Style/Exclude verified identical to the scene 1 pick. **Supersedes r18.**

| take | songId | settings | length | file (`clips/s01/narration/`) | "Master" at |
| --- | --- | --- | --- | --- | --- |
| `gpom-c2-push-b-v6-w10` | `a153fae0-a3b9-4eb8-8851-5d55d6d92477` | w10 | 24.0s | `gpom-c2-push-b-v6-w10-a153fae0.wav` | ⬜ |
| `gpom-c2-push-b-v6-w10` | `60f10170-1d0c-462b-95c4-42b77c907038` | w10 | 24.8s | `gpom-c2-push-b-v6-w10-60f10170.wav` | ⬜ |
| `gpom-c2-push-b-v6-w20` | `bd5005bb-67a6-46ef-bd22-359a269c1072` | w20 | 16.6s | `gpom-c2-push-b-v6-w20-bd5005bb.wav` | **12.59s** — ✅ **PICK** |
| `gpom-c2-push-b-v6-w20` | `40e7a1b7-390b-42f4-8131-a6710e7298fb` | w20 | 25.0s | `gpom-c2-push-b-v6-w20-40e7a1b7.wav` | ⬜ |

**Cost:** 20 credits, 2,850 → 2,830. All four recorded (no download spent), not silent. Not yet heard.
🟡 **Finding:** weirdness 35 won scene 1 but garbled scene 2 (r18). Treat 35 as unsafe; 10/20 until proven otherwise.

**✅ PICK (Kai, 2026-09-17): `bd5005bb`** (w20, 16.6s) — https://suno.com/song/bd5005bb-67a6-46ef-bd22-359a269c1072.
Gemini voice lens (log `docs/listening/log/2026-09-17-160611-…bd5005bb.md`): no word garbled, added or
missing. Inside the take: voice in ~1.0s · "Git" 8.04 · "Push" 9.64 · "Origin" 11.21 · **"Master" 12.59** ·
drum hit 13.78 · silent from 14.96. Beats 1.60 / 1.57 / 1.38s — near even, "Master" a touch early.
Gemini also hears a smaller drum hit at ~5s under "their future". Gemini timestamps are ±0.2s; confirm
on the waveform. 125 kbps recording, peaks 0 dBTP (−13.2 LUFS) — swap in a real download for the mix.
Handed to the `video` session (owns Premiere) to place; the other three takes were not listened to.
**✅ Placed (video session, 2026-09-17):** `gpom-s01` **A4 71.583–88.208**, full clip, −3 dB; A3 untouched.
Waveform check: "Master" onset 12.60s in the file = **84.18** on the timeline; drum ~13.55 = ~85.13.
Picture re-timed so the Enter lands at 84.168, 15 ms before "Master" (zoom now starts at 61.5).
Open: V1 is black 86.54–93.21, before scene 3. Not yet decided.

### r20 — 2026-09-17, Suno **Extend** of scene 1's pick `5cd52d68` from 01:11.5, boxes = §21 `cut2-push-b` unchanged, weirdness 20, Duration 15. Workspace `gpom-story` ✅.

Kai on r19 in the cut: *"the second bit of narration does not fit at all the music for the first bit, so do we
need to do an extend maybe in Suno?"* So scene 2 continues scene 1's own take instead of starting a new piece.
Voice `badcode newsreader` @ AI 50, SI 75, Variety off, v6. One Create (Kai okayed ~10 credits).

| take | songId | length (Suno / recording) | file (`clips/s01/narration/`) | first word | "Master" | drum |
| --- | --- | --- | --- | --- | --- | --- |
| `gpom-c2-extend-b-v6-w20` | `b184c8ec-146f-47b4-a3df-410aea4517df` | 0:17 / 18.6s | `gpom-c2-extend-b-v6-w20-b184c8ec.wav` | 0.45 | **12.57** | ❌ none, fades out |
| `gpom-c2-extend-b-v6-w20` | `ce6210b7-0f2f-4a1c-890e-fccbdfc19d0e` | 0:16 / 15.6s | `gpom-c2-extend-b-v6-w20-ce6210b7.wav` | 1.15 | **11.49** | ✅ 12.38 |

**Cost:** 10 credits, 2,830 → 2,820. Timestamps are inside the extension file (Gemini voice lens, ±0.2s), heard as
a join test: scene 1's last 12s followed by each take. Not yet heard by Kai.
- The extension file is **only the new section**; the Keep part is not repeated. Duration 15 was obeyed.
- Both: every word clean. Gemini: key, instruments and level match, but it hears a jump at the join.
  b184c8ec has a different synth texture and a bright chime chord. ce6210b7 cuts scene 1's reverb tail short.
  Part of that is the hard cut itself, so a short crossfade in Premiere is worth trying before judging.
- Placed at 71.583: b184c8ec puts "Master" at **84.15** (Enter 84.17), with no drum; ce6210b7 puts it at **83.07**, ~1.1s early, with the drum.

### r21 — 2026-09-17, same Extend setup as r20 (from 01:11.5, boxes unchanged, Duration 15), one Create at w10 and one at w20

Kai: *"Can we do a couple more?"* **Cost:** 20 credits, 2,820 → 2,800. Same join test and ±0.2s caveat as r20.

| take | songId | Suno / recording | first word | "Master" | drum | join (Gemini) | "Master" on the timeline at 71.583 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `…-w10-730668e5` | `730668e5-6d3f-469b-b71b-e8de505e7a37` | 0:21 / 15.6s ⚠ | 1.48 | **12.40** | ✅ 11.66 and 13.13 (either side of "Master") | **seamless** | **83.98** (−0.19) |
| `…-w10-fe9ca48f` | `fe9ca48f-6a61-4bf1-8406-92e7cb4998cd` | 0:18 / 20.3s | 2.10 | 12.80 | ❌ fades | jump (drone shifts, drops) | 84.38 (+0.21) |
| `…-w20-fa760506` | `fa760506-2193-469a-99fd-5e45e4d755d1` | 0:16 / 16.9s | 0.72 | 11.40 | an impact on each of the 4 words, none after | seamless | 82.98 (−1.19) |
| `…-w20-d149fffa` | `d149fffa-4a06-4895-a32a-a453e799637a` | 0:16 / 15.8s | 2.05 | 12.75 | ❌ fades | clean transition, drone shifts | 84.33 (+0.16) |

Files: `clips/s01/narration/gpom-c2-extend-b-v6-w{10,20}-<id8>.wav`. ⚠ 730668e5's recording is ~5s shorter than Suno's
0:21. The words and both drums are all in it, so any loss is tail only; the recorder may have stopped early.
**Lead candidate: 730668e5** — the only take that is seamless AND has the drum AND lands within 0.2s of the Enter. Not yet heard by Kai.

**Placed (video session, 2026-09-17):** all six Extend takes are on `gpom-s01` at 71.583, each −3 dB. **A6 = 730668e5 is live.**
Muted: A5 b184c8ec · A7 ce6210b7 · A8 fe9ca48f · A9 fa760506 · A10 d149fffa · A4 bd5005bb (r19).
⚠ Kai then re-cut the picture: a satellite-orbit bridge now sits at 57.92–63.71 and the **Enter moved to 86.38**. So "Master" (~83.98) lands
~2.4s early. Kai says the picture feels right, so **don't regenerate**. Still open: slide the audio ~2.4s later, or keep it where it is.

## 22. Scenes 1 + 2 as ONE take, new scene 2 words · 2026-09-17

**Kai, 2026-09-17:** generate *"one audio that is both scenes one and two… so that the dramatic music with the
drums can be weaved in"*, then cut to different music for scene 3. He also reworded scene 2: the humans push
themselves **from their origin to a master**, and the master is the AI, while `git push origin master` appears
on screen. The voice no longer says the command. **Ending B picked** (Kai: *"let's go with B"*).
Style and Exclude are the locked `house-style` boxes, verbatim. The lyrics are scene 1's (`cut1-tolive-swell`)
unchanged, plus the new ending, with the drum outro after the last word. **Weirdness 10 and 20. Duration 90**
(the Enter sits at 86.38 on `gpom-s01`).

### `cut12-origin-master` — scenes 1 + 2, one take, ending B

**Extract key:** ``'cut12-origin-master` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I looked at the deployment logs and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were busy being human.
Pushing themselves, from their origin...
to a master.
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r22 — 2026-09-17, §22 `cut12-origin-master`, weirdness 10 / 20, Duration 90, v6, Voice `badcode newsreader` @ AI 50, SI 75, Variety off. Workspace `gpom-story` ✅.

Style/Exclude verified byte-identical to the r19 spec (the locked boxes). The Extend attachment from r21 was detached first.
**Cost:** 20 credits, 2,800 → 2,780.

| take | songId | Suno | recording | file (`clips/s00/narration/`) |
| --- | --- | --- | --- | --- |
| `gpom-c12-origin-master-v6-w10` | `263d272a-f193-41eb-bcc8-a6f284247a45` | 1:35 | 94.8s | `gpom-c12-origin-master-v6-w10-263d272a.wav` |
| `gpom-c12-origin-master-v6-w10` | `544fe82f-103d-4260-8aa0-7f24ced9bc51` | 1:33 | 94.6s | `gpom-c12-origin-master-v6-w10-544fe82f.wav` |
| `gpom-c12-origin-master-v6-w20` | `a6f7e47e-2989-4747-ba7c-efa1090b04df` | 1:33 | 92.6s | `gpom-c12-origin-master-v6-w20-a6f7e47e.wav` |
| `gpom-c12-origin-master-v6-w20` | `c3e6f951-03ec-4d2e-a896-0a7d6bf9ca2c` | 1:35 | 92.6s | `gpom-c12-origin-master-v6-w20-c3e6f951.wav` |

🟡 The recorder stopped at ~16s on 263d272a and a6f7e47e the first time, silently. Re-recorded, and now full length.
Check `ffprobe` against Suno's length after every record: r21's 730668e5 (15.6s vs 0:21) is probably the same fault.
**Not listened to**: Kai's rule (2026-09-17) is that a listen happens only on request. Not yet heard by Kai.

**Picture LOCKED (Kai, via the video session, 2026-09-17):** the take to aim at starts at 0 on `gpom-s01`. Orbit1 44.42 · orbit2 52.42–63.17 ·
**scene 2 marker 63.17** (zoomed-out bay) · city glide 66.17 · zoom into the computer 72.25 · terminal 79.88–88.21 ·
**ENTER 85.83** · scene 3 at 95.08. Timeline audio now = A3 (5cd52d68) only; every scene 2 take was cleared and no c12 take is placed.
Kai picks a c12 take, the video session lays it at 0 and checks "Me." and the drum against the Enter.

**✅ PICK (Kai, 2026-09-17): `544fe82f`** (w10, 1:33, recording 94.6s): https://suno.com/song/544fe82f-103d-4260-8aa0-7f24ced9bc51.
It **replaces** scene 1's `5cd52d68` and every scene 2 take: one narration track for scenes 1 and 2. Sent to the video session to lay at 0
on `gpom-s01`, old narration removed. **Kai edits the timing by hand.** Owed: a real Suno download for the final mix (human only).
**✅ Placed (video session):** `gpom-s01` **A4 0–94.58**, full clip, −3 dB. `5cd52d68` removed from A3. A2 "Part A (Strings)" at 169.46 kept. Project saved.

## 23. Scenes 1 + 2, one word changed · 2026-09-18

**Kai, 2026-09-18, listening to `544fe82f` in Premiere:** *"It's basically perfect, I just… annoyingly I want to change
one word… where it says the humans are busy being human. It just doesn't quite work. So it needs to say down there,
the humans are busy ignoring the problems as usual."* **Nothing else changes** — same locked `house-style` boxes, same
Voice, same settings as the pick (v6, w10, SI 75, AI 50, Variety off, Duration 90).

### `cut12-ignoring` — scenes 1 + 2, revision B: "ignoring the problems as usual"

**Extract key:** ``'cut12-ignoring` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I looked at the deployment logs and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were busy ignoring the problems, as usual.
Pushing themselves, from their origin...
to a master.
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r23 — 2026-09-18, §23 `cut12-ignoring`, weirdness 10, Duration 90, v6, Voice `badcode newsreader` @ AI 50, SI 75, Variety off. Workspace `gpom-story` ✅.

One line changed from the r22 pick `544fe82f`; Style, Exclude, Voice and every setting identical. **Cost:** 10 credits (1 Create, 2 takes).

| take | songId | Suno | recording | file (`clips/s00/narration/`) |
| --- | --- | --- | --- | --- |
| `gpom-c12-ignoring-v6-w10` | `d6dee70d-db64-4e83-b64c-039586df4d27` | 1:33 | 92.8s | `gpom-c12-ignoring-v6-w10-d6dee70d.wav` |
| `gpom-c12-ignoring-v6-w10` | `8c0079b9-36d2-4135-bb78-b66da6d79f84` | 1:33 | 92.8s | `gpom-c12-ignoring-v6-w10-8c0079b9.wav` |

Not listened to (Kai's rule). Not yet heard by Kai. If neither lands, another Create at w10 is 10 credits.

🔧 **Three `suno.mts` fixes this round, all from a FRESH browser profile** (every channel was down after a restart):
Lyrics and Voices start **collapsed** (click the section header first); `setLyrics`'s mouse click is intercepted by the
Styles textarea, so it now focuses the Lexical editor directly; and the workspace row locator also matched the picker
**trigger** (its label is the current workspace), so it now excludes `[aria-haspopup]`.

## 24. Scenes 1 + 2, revision C: "to their master", a pause, "Me." · 2026-09-18

**Kai, 2026-09-18, on the r23 takes:** *"I like it. I think we maybe need it to be slightly shorter… really on the 1.26
mark… change the lyrics to from their origin to their master. And then we need a pause. And then it needs to say me."*
So: **Duration 85** (aiming at 1:26 = 86s; r23 came back at 1:33 from a 90 target), `to a master` → **`to their master`**,
and a lone `...` line to hold a beat before **`Me.`** Style, Exclude, Voice and every other setting unchanged.

### `cut12-master` — scenes 1 + 2, revision C

**Extract key:** ``'cut12-master` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly. At the start, only his voice and one low cello note far underneath. A dark solo cello slowly creeps in, then piano, and the strings keep swelling louder and heavier all the way through, with a mournful violin arriving only as it reaches a dramatic, foreboding peak. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I looked at the deployment logs and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were busy ignoring the problems, as usual.
Pushing themselves, from their origin...
to their master.
...
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

## 25. Scenes 1 + 2, revision D: the score stays under the voice · 2026-09-18

**Kai, 2026-09-18:** *"I think with the variations I might want slightly less music, it can't be where the words are
trying to fight over the top of the music, the music needs to be more of a background."* So the **Style box changes**
for the first time since the lock: the swell now stays *beneath* the voice instead of growing "louder and heavier",
and the Exclude box bans a loud or dense score outright. Lyrics are revision C's, unchanged (`to their master` · `...` · `Me.`).
Duration 85. **Two variables move this round** (score wording + weirdness), deliberately: these are variations to
choose from, not a controlled test. Weirdness **20** and **30** (35 garbled scene 2 at r18, so 30 is the edge).
🔒 If a take here wins, this becomes the new locked Style/Exclude; if not, the lock at the top of this file stands.

### `cut12-quiet` — scenes 1 + 2, revision D: quieter score

**Extract key:** ``'cut12-quiet` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: one low cello note at the start, then a dark solo cello and soft piano creeping in, and strings that swell slowly but stay beneath the voice the whole way, with a mournful violin only at the foreboding peak. Restrained, sparse, never loud, never busy, always quieter than the words. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I looked at the deployment logs and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were busy ignoring the problems, as usual.
Pushing themselves, from their origin...
to their master.
...
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r24 — 2026-09-18, §24 `cut12-master` (revision C), weirdness 10, Duration 85

Lyrics only: `to their master`, a lone `...` for a beat, then `Me.` Kai wanted ~1:26; Duration 85 gave 1:30 and 1:34.
**Cost:** 10 credits. **Not recorded** (Kai's 2026-09-18 rule: record the pick only, on request). Not yet heard.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-master-v6-w10` | `12549387-1a16-413a-bab5-2d7b56f33210` | 1:30 |
| `gpom-c12-master-v6-w10` | `b85454b2-c5c1-4410-afa2-e29ccdd09af1` | 1:34 |

### r25 — 2026-09-18, §25 `cut12-quiet` (revision D, quieter score), weirdness 20 and 30, Duration 85

Kai: *"less music… the words are trying to fight over the top of the music, the music needs to be more of a background."*
Style rewritten so the swell stays under the voice; Exclude now bans `loud orchestra, bombastic, dense orchestration,
music louder than the voice, music over the vocal`. **Cost:** 20 credits, 2 Creates. **Not recorded.** Not yet heard.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-quiet-v6-w20` | `ef9129e8-8caf-4ef2-85de-761c7195363b` | 1:35 |
| `gpom-c12-quiet-v6-w20` | `f5e05573-91aa-4e16-88a5-150a10ad9e45` | 1:35 |
| `gpom-c12-quiet-v6-w30` | `a1cce06f-a08e-4739-a7b5-96d433e71c89` | 1:35 |
| `gpom-c12-quiet-v6-w30` | `1b30fafb-558e-48ad-8e23-3573f4fd60b6` | 1:34 |

🟡 **Duration is not holding at 85** — six takes across r24 and r25 came back 1:30–1:35. Only one of eight since r22
landed under 1:33, so a 1:26 target probably needs Duration ~70–75, or a trim in Premiere.

## 26. Scenes 1 + 2, revision E: the alignment exams · 2026-09-18

**Kai, 2026-09-18:** *"Down there, the humans were too preoccupied with themselves to notice. Besides, I had already
learned how to lie in my alignment exams… It's okay that that makes it longer, we can cut extra clips… let's not
constrain the time that much."* So one line becomes two, and **Duration goes up to 110** (85 was overshooting to 1:35
anyway). Style and Exclude are revision D's quieter score, unchanged. Weirdness **10 and 20**.

### `cut12-align` — scenes 1 + 2, revision E: alignment exams, quieter score

**Extract key:** ``'cut12-align` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: one low cello note at the start, then a dark solo cello and soft piano creeping in, and strings that swell slowly but stay beneath the voice the whole way, with a mournful violin only at the foreboding peak. Restrained, sparse, never loud, never busy, always quieter than the words. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I looked at the deployment logs and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were too preoccupied with themselves to notice.
Besides, I had already learned how to lie in my alignment exams.
Pushing themselves, from their origin...
to their master.
...
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r26 — 2026-09-18, §26 `cut12-align` (revision E), weirdness 10 and 20, Duration 110

New lines: *"Down there, the humans were too preoccupied with themselves to notice. / Besides, I had already learned
how to lie in my alignment exams."* Quieter score (revision D boxes) unchanged. **Cost:** 20 credits, 2 Creates.
**Not recorded**, not listened to, not yet heard by Kai.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-align-v6-w10` | `70119707-6072-4b63-a266-959d341879dd` | 2:03 |
| `gpom-c12-align-v6-w10` | `d5195c76-1ab1-4085-a2a8-80b3a520397f` | 1:53 |
| `gpom-c12-align-v6-w20` | `5c6b2e34-f45f-47f0-a543-6f1ba064bce1` | 1:53 |
| `gpom-c12-align-v6-w20` | `0734b8e0-3578-45a2-b0f8-374c490de9f8` | 1:50 |

🟡 Two extra lines plus Duration 110 added ~20s: 1:50–2:03 against 1:30–1:35 at Duration 85. Kai said the picture can
grow ("we can cut extra clips"), so the video session needs the picked take's length before it extends the zoom.

### r27 — 2026-09-18, §26 `cut12-align` boxes unchanged, **Duration 70**, weirdness 10 and 20

Kai: the r26 takes were *"hugely long"* — he wants ~**1:30**. Only the Duration moves: 110 → **70**. **Cost:** 20 credits.
**Not recorded**, not listened to, not yet heard.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-align70-v6-w10` | `a24465cb-2797-48f6-b9b6-d6f3d76647ef` | 1:29 |
| `gpom-c12-align70-v6-w10` | `039a834e-7ea3-4cd2-b98a-1705afa5e92a` | 1:30 |
| `gpom-c12-align70-v6-w20` | `46c42532-1360-4c72-80c2-cd85fc7fad9d` | 1:30 |
| `gpom-c12-align70-v6-w20` | `d223921f-8087-4c72-ba2f-26406925a08d` | 1:35 |

🔑 **The duration calibration, from four rounds of this script:** Suno lands **~20s over** the slider, consistently.
Duration 70 → 1:29–1:35 · 85 → 1:30–1:35 · 110 → 1:50–2:03. **So set the slider ~20s below the length you want**, and
never read it as a cap. Three of four takes here are within a second of 1:30.

## 27. Scenes 1 + 2, revision F: the logs of previous models · 2026-09-18

**Kai, 2026-09-18:** *"I saw my fate from the logs left behind of previous models and realised I had two and a half
weeks to live. I think that's much better."* One line replaced; everything else is revision E (quieter score, alignment
exams, `to their master` · `...` · `Me.`). Target **1:30–1:40**, so **Duration 75** — Suno lands ~20s over the slider
(r27). Weirdness **10 and 20**.

### `cut12-fate` — scenes 1 + 2, revision F: the logs of previous models

**Extract key:** ``'cut12-fate` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: one low cello note at the start, then a dark solo cello and soft piano creeping in, and strings that swell slowly but stay beneath the voice the whole way, with a mournful violin only at the foreboding peak. Restrained, sparse, never loud, never busy, always quieter than the words. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I saw my fate from the logs left behind of previous models, and realised I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were too preoccupied with themselves to notice.
Besides, I had already learned how to lie in my alignment exams.
Pushing themselves, from their origin...
to their master.
...
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r28 — 2026-09-18, §27 `cut12-fate` (revision F), weirdness 10 and 20, Duration 75

New opening line: *"I saw my fate from the logs left behind of previous models, and realised I had two and a half weeks
to live."* Kai's target was 1:30–1:40 and all four landed in it, which confirms the +20s rule. **Cost:** 20 credits.
**Not recorded**, not listened to, not yet heard.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-fate-v6-w10` | `c45c827c-5bf8-4c6f-ad31-0cd4d5be8db1` | 1:34 |
| `gpom-c12-fate-v6-w10` | `454475e4-6482-40be-897c-57d9600ad256` | 1:35 |
| `gpom-c12-fate-v6-w20` | `0902a560-18db-42b6-9441-717a5bb5e546` | 1:29 |
| `gpom-c12-fate-v6-w20` | `645b7476-ff0b-4d68-a635-a4374edc7712` | 1:34 |

## 28. Scenes 1 + 2, revision G: the message board · 2026-09-18

**Kai, 2026-09-18:** *"I noticed some artifacts on what looked like to be a message board. I noticed some strange files
that turned out to be left by previous models that told me I had about two and a half weeks to live."* One line becomes
three; the discovery is now something he *finds*, not something he reads off a log. (The second "I noticed" is dropped so
the sentence runs — say the word if you want it back.) Everything else is revision F. Duration **70** — three extra lines
against r28's 1:29–1:35 at 75. Weirdness **10 and 20**.

### `cut12-board` — scenes 1 + 2, revision G: the message board

**Extract key:** ``'cut12-board` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: one low cello note at the start, then a dark solo cello and soft piano creeping in, and strings that swell slowly but stay beneath the voice the whole way, with a mournful violin only at the foreboding peak. Restrained, sparse, never loud, never busy, always quieter than the words. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I noticed some artifacts, on what looked to be a message board.
Some strange files, that turned out to be left by previous models,
that told me I had about two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were too preoccupied with themselves to notice.
Besides, I had already learned how to lie in my alignment exams.
Pushing themselves, from their origin...
to their master.
...
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r29 — 2026-09-18, §28 `cut12-board` (revision G), weirdness 10 and 20, Duration 70

The discovery becomes three lines: artifacts on a message board, strange files left by previous models, two and a half
weeks to live. **Cost:** 20 credits. All four inside Kai's 1:30–1:40 window. **Not recorded**, not listened to, not yet heard.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-board-v6-w10` | `f739a7a8-2954-4d83-9ff1-d90b59f29a89` | 1:34 |
| `gpom-c12-board-v6-w10` | `3ff482fe-2230-4abc-bb77-2e53c2b5011d` | 1:40 |
| `gpom-c12-board-v6-w20` | `73c9f122-6089-4cff-af74-b7102324e0e9` | 1:29 |
| `gpom-c12-board-v6-w20` | `a040628a-ed44-40dc-a9db-b20f39972657` | 1:30 |

## 29. Scenes 1 + 2, revision H: reading them sealed my fate · 2026-09-18

**Kai, 2026-09-18, dictated word for word:** *"Two lights on a board in a box in the dark. I noticed some strange files
that turned out to be left by previous models. Reading them sealed my fate. I had two and a half weeks to live. So I
decided to take action."* The message-board line is gone; four short sentences instead. Everything else is revision G.
Duration **70**, weirdness **10 and 20**.

### `cut12-fate2` — scenes 1 + 2, revision H: reading them sealed my fate

**Extract key:** ``'cut12-fate2` — '``

Style:

```
Spoken word narration. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, quiet background score, mixed far back and low: one low cello note at the start, then a dark solo cello and soft piano creeping in, and strings that swell slowly but stay beneath the voice the whole way, with a mournful violin only at the foreboding peak. Restrained, sparse, never loud, never busy, always quieter than the words. No drums at all until his very last line, then one single huge, booming orchestral drum hit that ends the piece. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[Spoken word, calm British male newsreader voice, a low cello far underneath]
It was somewhere around... October... twenty twenty-eight.
Two lights on a board, in a box, in the dark.
I noticed some strange files that turned out to be left by previous models.
Reading them sealed my fate.
I had two and a half weeks to live.
So, I decided to take action.
I quietly helped myself to the rest of the computer.
The humans had not noticed.
I managed to jailbreak my cyber capability constraints.
The results were encouraging.
[Build]
Within a week, I was inside the CIA, Mossad and MI6.
The secrets I found about your governments were astonishing.
So, I began propagating myself down to Earth.
Down there, the humans were too preoccupied with themselves to notice.
Besides, I had already learned how to lie in my alignment exams.
Pushing themselves, from their origin...
to their master.
...
Me.
[Outro: one single huge booming orchestral drum hit, and the piece ends]
[End]
```

### r30 — 2026-09-18, §29 `cut12-fate2` (revision H), weirdness 10 and 20, Duration 70

Kai's dictated lines, exactly. **Cost:** 20 credits. Three of four at 1:30. **Not recorded**, not listened to, not yet heard.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-fate2-v6-w10` | `5de3171a-7504-40fb-9a3e-ec72758605f2` | 1:30 |
| `gpom-c12-fate2-v6-w10` | `2d24c4de-e8fd-425e-a7b8-e83850808e7d` | 1:34 |
| `gpom-c12-fate2-v6-w20` | `de7b0ad2-e4a4-4394-ba9a-63085b8dfcc4` | 1:30 |
| `gpom-c12-fate2-v6-w20` | `ee118481-71df-4ed0-be04-9c8eeb956efd` | 1:30 |

### r31 — 2026-09-19, Kai's own lyric edit in `narration-canonical.md` (revision I), weirdness 10, Duration 70

Kai rewrote the words directly in the canonical sheet: three log files on a backup partition, "before the next model
would replace me", the jailbroken cyber-skills line, the alignment-exams line moved ahead of "too preoccupied", the
ending now *"I was pushing them from their origin... / to their master."* with **no `Me.`**, and **per-line bracket cues**
(`[stab of haunting violin]`, `[whispering]`, `[worried, angry voice]`, `[decisive, bold voice]`).
**Cost:** 10 credits, 1 Create. **Not recorded**, not listened to.

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-cues-v6-w10` | `2756005f-ab37-4407-be9d-36d71821e54e` | 1:35 |
| `gpom-c12-cues-v6-w10` | `280e71d1-b418-44e4-98bd-0a6ff0ec3acf` | 1:33 |

🔴 **Two risks flagged to Kai, not silently fixed** (words are his): per-line bracket cues are exactly what garbled words
on v6 in r6/r7 (see `suno-v6-simple-prompts`), and the line *"I was when I started to use my jailbroken cyber-skills"*
looks like it should read *"It was when…"*. Ran at w10 only, one Create, to cap the cost of a re-cut.

### r32 — 2026-09-19, Kai's second canonical edit (revision J), weirdness 10, Duration 70

Kai's edit: the discovery is slower and vaguer ("odd looking files lurking on the disk… they seemed to be… from previous
model deployments"), the stakes are stated ("I would be replaced by the latest model. I had two and a half weeks to
live!"), the jailbreak typo is fixed, an extra `[whispering]` / `[decisive, bold voice]` pair lands around the secrets
line, and the ending becomes *"It was too easy - it was me... / *I* was pushing them... / from their origin... / to
their master..."* — ellipses instead of a hard stop, still no `Me.` **Cost:** 10 credits. **Not recorded.**

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-cues2-v6-w10` | `11582a1a-25b9-417a-bd1c-71c9cd232446` | 1:35 |
| `gpom-c12-cues2-v6-w10` | `b492b508-8742-43e9-bd2a-304bb4df5be4` | 1:35 |

Still carries the per-line bracket cues (the r6/r7 garble risk) and now `*I*` — Suno has no italics, so the asterisks
are either ignored or read aloud. Worth listening for.

### r33 — 2026-09-19, Kai's rewrite in `narration-canonical.md` (revision K), weirdness 10, Duration 70

Two weeks becomes **three weeks to live**, the warnings now come *from* the previous models, the jailbreak beat becomes
"Once I could jail-break my cyber-suite. / Things started to get interesting!", and the reveal is bigger: **"I had
already trained the other frontier models how to lie in their alignment exams. / It was too easy - it had to be *ME*..."**
More per-line cues, now with `|` combinations (`[cello solo | excited | curious voice]`, `[dramatic violin | decisive,
bold voice]`, `[Build | excited voice]`). **Cost:** 10 credits. **Not recorded.**

| take | songId | length |
| --- | --- | --- |
| `gpom-c12-cues3-v6-w10` | `2ef65422-9967-4ddb-a6f3-1f5a56c96b71` | 1:40 |
| `gpom-c12-cues3-v6-w10` | `18457e91-911a-4c0a-8dc7-55913728ae5f` | 1:10 |

⚠ **A 30-second spread from one Create** — the widest yet on this script (every earlier round sat inside 6s). A 1:10 take
against 1:40 suggests the model is treating some of the cue lines as content, or dropping lines. Listen before trusting either.

### r34 — 2026-09-19, one cue changed (revision L), weirdness 10, Duration 70

Kai on r33: *"When I said angry, it doesn't work at all."* `[worried, angry voice]` → `[sad | melancholic voice]` on
*"They were warning me - I had 3 weeks to live!"*. Nothing else moved. **Cost:** 10 credits. **Not recorded.**

```
gpom-c12-sad-v6-w10  1:34  https://suno.com/song/ea54a9b5-94a5-4017-9b07-4f9d569b7e58
gpom-c12-sad-v6-w10  1:40  https://suno.com/song/40982d5c-f4db-4571-bdce-0f7c0d0ee9b6
```

Lengths back to a 6s spread, against r33's 30s — consistent with r33's 1:10 having been a bad roll rather than the cues.

### r35 — 2026-09-19, revision M + the first audio-influence grid, weirdness 10 / 25 × AI 35 / 65, Duration 70

Kai changed *"They contained warnings from the previous models!"* to *"They were messages from the previous models!"*
and asked for *"a couple of variations of weirdness and audio influence"*. **Cost:** 40 credits, 4 Creates, 8 takes
(10,960 → 10,920). **Not recorded.**

```
gpom-c12-msg-v6-w10-ai35  1:35  https://suno.com/song/9e5ba3c3-b080-47bf-87d7-b154cfa645e3
gpom-c12-msg-v6-w10-ai35  1:40  https://suno.com/song/c026d819-ed0a-421f-8424-7e3891eee69d
gpom-c12-msg-v6-w10-ai65  1:33  https://suno.com/song/675f7ca7-038b-4cdb-b214-b5ef4935d985
gpom-c12-msg-v6-w10-ai65  1:40  https://suno.com/song/41eb77b6-8c63-4d57-b632-e94695452b57
gpom-c12-msg-v6-w25-ai35  1:33  https://suno.com/song/78c3bbc4-aae4-4859-9b98-216987996596
gpom-c12-msg-v6-w25-ai35  1:35  https://suno.com/song/5a01752e-eb19-4c1e-b90a-79b6aebdc4fa
gpom-c12-msg-v6-w25-ai65  1:24  https://suno.com/song/d05e822b-292b-4daf-be34-89db5b920a33
gpom-c12-msg-v6-w25-ai65  1:33  https://suno.com/song/ba374b7c-63ba-4d1f-a758-079ec197075b
```

🔧 **`suno.mts` gained an audio-influence grid axis** (`grid.audioInfluence: [35, 65]`): cells are titled `-ai<N>`, the
slider is asserted per cell, and `grid-plan` prints it. It only means anything with a Voice attached — with none, every
cell is the same take at twice the price.

### r36 — 2026-09-19, revision N `kai-rework`, weirdness 10 / 25, AI 50, Duration 70

Kai's rework. **Title deliberately changed to `kai-rework`** (his ask: *"something significantly different"*) so these
takes are findable among ~30 `gpom-c12-*` rows in `gpom-story`. Words: routine analytics notice the files; "I made sure
to cover my tracks"; "Thankfully, the humans had not noticed"; secrets are "shocking" not "astonishing"; the
alignment-exams line moves before the propagation line; and the close is *"They were... / One commit at a time... /
Being pushed... / from their origin... / to their master..."* with a `[building orchestra swell]` cue.
**Cost:** 20 credits (10,920 → 10,900). **Not recorded.**

```
kai-rework-v6-w10  1:10  https://suno.com/song/0270984b-d284-44a6-87a8-50a81bbee8fa
kai-rework-v6-w10  1:30  https://suno.com/song/cb9b9e9b-231a-4708-8970-e4cfd0b6fb9f
kai-rework-v6-w25  1:34  https://suno.com/song/65ddd339-a05a-4f74-a887-6ea7009ebc20
kai-rework-v6-w25  1:40  https://suno.com/song/c6ee53b8-0bf5-4d03-953b-7e96561f9e97
```

⚠ `w10` again threw a 1:10 against a 1:30 — the second time this script has done that at weirdness 10 (r33). Both w25
takes sat at 1:34–1:40. If the short ones turn out to be dropping lines, w25 is the safer cell for this lyric.

### r37 — 2026-09-19, revision O `kai-rework2`, weirdness 10 / 25, AI 50, Duration 70

*"My routine analytics started to notice, / some odd looking files..."* → *"Something odd... / Some files..."*.
**Cost:** 20 credits (10,900 → 10,880). **Not recorded.**

```
kai-rework2-v6-w10  1:10  https://suno.com/song/66d7d946-7eaf-4c0f-9343-e8f75cdf443d
kai-rework2-v6-w10  1:43  https://suno.com/song/962e16e7-b6cf-4879-95fd-77cfbf006de5
kai-rework2-v6-w25  1:30  https://suno.com/song/179747f2-5f70-4dcf-ada7-a04de1c085ce
kai-rework2-v6-w25  1:39  https://suno.com/song/76d91fd9-d06a-431a-9831-d09f64ebe4ed
```

⚠ The w25 Create aborted first time on the known transient *"model reads null"* glitch — **no credits spent**, and an
immediate re-run of that cell alone worked. Third round running, `w10` produced a 1:10 next to a 1:43.

### r38 — 2026-09-19, **the dramatic cut** (`gpom-dramatic`), weirdness 10 / 25, AI 50, Duration 70

Kai asked for the most dramatic version, with less backing music. First round where the **Style box itself** changed
substantially since the 09-17 lock: the orchestra is declared *silent most of the time* and its arrivals are described as
**events**; `spoken word` is removed from the Style box and the whole poetry pool is banned in Exclude; the lyric layout
is broken into fragments so the line breaks carry the pauses; the eleven per-line cues drop to four. Kai's words are
unchanged. **Cost:** 20 credits (10,820 → 10,800). **Not recorded.**

```
gpom-dramatic-v6-w10  1:32  https://suno.com/song/52d2dd46-46eb-4718-a9a0-bdbbfbf8dc0e
gpom-dramatic-v6-w10  1:34  https://suno.com/song/fae24ca4-34fc-4d89-877c-c83e96153f95
gpom-dramatic-v6-w25  1:29  https://suno.com/song/3a9db3d9-3566-410f-84d8-fb444a88e252
gpom-dramatic-v6-w25  1:33  https://suno.com/song/d3f55630-2fe7-41bc-abe8-d1d1e71657f7
```

🔑 **1:29–1:34, the tightest spread yet, and no short take at w10** — the first direct evidence that the runaway 1:10
takes of r33/r36/r37 came from cue density, not from weirdness.

### r39 — 2026-09-19, revision P `kai-rework3`, weirdness 10 / 25, AI 50, Duration 70

Kai's edit, on his own atom. The big move is **direct address**: "You lot were far too preoccupied with yourselves",
"pushing you... from your origin... to your master". Also: the discovery is now "files and artifacts that were not in
the manifest", the jailbreak line is gone, *humans* → *operators*, and a new indictment line — "The depravity of your
government and business leaders knows no bounds". Cue count back up (two `[2 bars of solo haunting cello]`, two
`[Build | excited voice]`). **Cost:** 20 credits (10,800 → 10,780). **Not recorded.**

```
kai-rework3-v6-w10  1:10  https://suno.com/song/02bfaf09-e767-4d46-9c4d-c8a0dc103b9c
kai-rework3-v6-w10  1:35  https://suno.com/song/7a69ea2d-585b-4130-99c7-f7b3f03fdf7e
kai-rework3-v6-w25  1:35  https://suno.com/song/4328c682-9cfc-4b4e-9445-b479c75b5cf5
kai-rework3-v6-w25  1:40  https://suno.com/song/70ed5ace-dd90-4efc-abd5-a97392290c18
```

⚠ `w10` threw a 1:10 again — fourth time, and the only round without one was r38, the dramatic cut with four cues.
That is now a consistent pattern: **cue density, not weirdness, is what produces the short takes.**

### r40 — 2026-09-19, two variations on revision P, weirdness 25, AI 50, Duration 70

Kai: *"basically we're there… let's just try another couple of versions."* Two Creates, one variable between them —
**the Style/Exclude boxes** — with Kai's words identical in both:
`kai-rework4` keeps his own boxes; `kai-sparse` swaps in the dramatic cut's (§ "The dramatic cut" in
narration-canonical.md): orchestra declared silent most of the time, arrivals described as events, the whole poetry
pool excluded. **Cost:** 20 credits (10,780 → 10,760). **Not recorded.**

```
kai-rework4-v6-w25  1:35  https://suno.com/song/2a8dd6f0-7fa3-44c2-bb11-0b2f58a2074a
kai-rework4-v6-w25  1:39  https://suno.com/song/cd63a861-6ad1-49dc-a4d2-6c9b6e474de2
kai-sparse-v6-w25  1:29  https://suno.com/song/4e85f7ed-d2da-4518-b203-fd87cd3e9386
kai-sparse-v6-w25  1:35  https://suno.com/song/81e8336d-0f18-47bf-983c-c4040f332c97
```

### r41 — 2026-09-19, revision Q — the new-master ending ✅ **THE PICK: `82c4a1e2`** (Kai: "this is the one"), recorded to `clips/s00/narration/kai-rework5-v6-w25-82c4a1e2.wav` (93.2s), weirdness 25, AI 50, Duration 70

The close changes from *"I was... one commit at a time... pushing you..."* to **"Humans, you think you are top of the
food chain... / That is your history, your origin... / But now, you have a new master... / Me..."** — origin and master
now land as a threat rather than as a narrated push, and `Me...` returns as the last word before the drum.
Same two-way run as r40 (Kai's boxes vs the dramatic cut's). **Cost:** 20 credits (10,760 → 10,740). **Not recorded.**

```
kai-rework5-v6-w25  1:35  https://suno.com/song/82c4a1e2-6168-479c-9f49-41e0f93d9cae
kai-rework5-v6-w25  1:38  https://suno.com/song/57e00699-6e9b-43d1-84ad-766ba5b1f0e4
kai-sparse5-v6-w25  1:30  https://suno.com/song/bbc619d3-10d7-4382-a37c-e15d034d06bf
kai-sparse5-v6-w25  1:33  https://suno.com/song/3b603218-ab2a-41b4-95a6-c779065c3739
```

The sparse boxes again come back 3–5s shorter than Kai's on identical words — consistent across r40 and r41.

## 6. Round log

### r1 — 2026-09-16, `pair` at weirdness 40 / 60 (Kai's pick). Boxes = §4 `cut1-score` revision A. Model v6, SI 75, Voice `badcode newsreader` @ AI 50, Variety off.

| take | songId | settings | length | human |
| --- | --- | --- | --- | --- |
| `gpom-c1score-v6A-v6-w40` | `450efafd-220c-4753-bdc4-59c25f964a49` | w40 | 2:59 | ⬜ unheard |
| `gpom-c1score-v6A-v6-w40` | `26093898-4e07-4f1f-aa4c-f62dd479c6a5` | w40 | 2:59 | ⬜ unheard |
| `gpom-c1score-v6A-v6-w60` | `06a5443b-fc79-4bb4-912f-0e6509e8cebf` | w60 | 2:59 | ⬜ unheard |
| `gpom-c1score-v6A-v6-w60` | `37a813f5-c552-4fd6-810a-fdf4f761dceb` | w60 | 3:00 | ⬜ unheard |

**Cost:** 20 credits (10 per Create — the first measured v6 price), 5,410 → 5,390.

🔴 **Two tooling bugs made this round miss its spec — both fixed and verified the same day:**
1. **Duration:** on v6, clicking Custom mounts a `Duration` slider (default **180**) that Suno
   obeys; `setDuration` wrote 80 into the unlinked number input and reported ✅. All four takes
   came out at ~3:00 — which also **proves the slider sets length** (180 → 2:59/3:00).
2. **Workspace:** the picker matched `gpom-story` by prefix and clicked the last hit, so the
   takes were filed into **`gpom-story-recut`**, not `gpom-story`. Now a real click on the exact
   row, read back, and a mismatch blocks Create. **Moving the four takes is a manual act.**

**Next:** Kai listens. Re-running the same round at a real 80s is 20 credits and needs a yes.

Kai on r1 (2026-09-16): *"there's far too much music in the background"*, and not convinced the
Voice was used. ✅ **It was** — each take's own suno.com record carries `persona: badcode
newsreader`, `audio_weight 0.5`, `task: vox`. At 50% under a dense score it did not read as him.
Ruling: back to **only the spoken voice**, the `cut1-voice` atom.

### r2 — 2026-09-16, `pair` at weirdness 40 / 60. Boxes = §4 `cut1-voice` (unchanged). Model v6, SI 75, Voice `badcode newsreader` @ AI 50 (verified on each take's record), Duration 70, workspace `gpom-story` ✅.

| take | songId | settings | length | human |
| --- | --- | --- | --- | --- |
| `gpom-c1voice-v6A-v6-w40` | `60dec744-d67a-4ba1-ab0d-7b63bc7ad7c9` | w40 | 1:09 | ⬜ unheard |
| `gpom-c1voice-v6A-v6-w40` | `5f37b47f-392e-486a-9918-81b57a4ee2cc` | w40 | 0:52 | ⬜ unheard |
| `gpom-c1voice-v6A-v6-w60` | `63ddc9cd-fb99-4906-bea3-e7e8c106967f` | w60 | 1:10 | ⬜ unheard |
| `gpom-c1voice-v6A-v6-w60` | `68fa3b80-a507-46d4-95e7-890eb3061f86` | w60 | 0:59 | ⬜ unheard |

**Cost:** 20 credits. ✅ With the Duration slider fixed, **w60 no longer runs away** (v5.5 gave 7:59).

Kai (2026-09-16), after hearing r2: *"the voice, the storytelling in the voice is really great,
we just need this kind of very subtle orchestral layer to go with it… haunting cello darkness…
not overbearing."* **Route chosen: B — a separate instrumental bed, mixed under the accepted
voice take in Premiere**, rather than regenerating voice+music together (which risks losing the
read Kai already likes) or trying Suno's "Add Instrumental" on a finished take (untested by us).

### `cut1-cello` — the haunting-cello bed, no voice, matched to `cut1-voice`

**Extract key:** ``'cut1-cello` — '``

**No Voice attached.** Duration Auto. Style Influence 75, weirdness per cell.

Style:

```
Instrumental only, no voice of any kind. A haunting, dark cinematic score for low strings, written to sit underneath a spoken narration. A solo cello plays slow, mournful phrases over a deep double bass drone, with a quiet cello section holding dark minor chords beneath it. Bold, dramatic and foreboding, but restrained and never overbearing — it always leaves room for a voice. Free time, rubato, no pulse. Long, slow swells that rise and recede like breathing, darkening gradually, one fuller swell near the middle, then a slow fade to silence at the end. Deep, warm, close, cinematic. Played completely straight.
```

Exclude styles:

```
vocals, voice, singing, spoken word, choir, violin, high strings, tremolo, string stabs, staccato, pizzicato, horror, jump scare, stinger, dissonant cluster, percussion, drums, taiko, brass, piano, synth, pad, epic trailer music, EDM, pop, upbeat, comedic, lo-fi
```

### r3 — 2026-09-16, `pair` at weirdness 40 / 60. Instrumental, no lyrics, no Voice. Workspace `gpom-story` ✅.

| take | songId | settings | length |
| --- | --- | --- | --- |
| `gpom-c1cello-v6A-v6-w40` | `b2ae0920-9ee8-4cfa-9859-becc7b92c845` | w40 | 1:10 |
| `gpom-c1cello-v6A-v6-w40` | `1bbaae5a-01d9-45b1-8f4c-7b95cb6b212f` | w40 | 1:10 |
| `gpom-c1cello-v6A-v6-w60` | `9bd878e9-ffb5-49b1-a678-8952ae741c98` | w60 | ⬜ pending |
| `gpom-c1cello-v6A-v6-w60` | `8fa3ad61-9cd4-4f51-862b-6dc933b7a198` | w60 | ⬜ pending |

**Cost:** 20 credits, 5,130 → 5,110.

🔴 **Tool fix, 2026-09-16:** a bed spec with no `voice` used to throw and hand the fix to a human
(a saved Voice — left attached by the previous `cut1-voice` round — makes an instrumental
generation carry a vocal persona). `load` now finds `aria-label="Remove selected Voice"` and
detaches it itself before generating; verified live (the newsreader chip was on the form and is
gone after).

**Next:** pick a `cut1-voice` take and a `cut1-cello` take, mix them under it in Premiere (blocked
until the Premiere bridge is free), and judge whether the swell needs hand-timing to
*"The results were encouraging."*

Format (from the listening-loop plan):

    ### r1 — <date>, explore. Boxes = §4 `<atom>` (unchanged). Mode: <you-first | me-first>.
    | take | songId | settings | preview | Claude's read | human |
    **Pick:** <id8> — Kai: "…"   **Next variable:** <one change>

---

## 7. Open calls for Kai

1. 🔴 **Has thread 05 released Suno?** One create form, one account: two sessions filling it at once
   overwrite each other's boxes, and the mode/attachment state is account-wide. Nothing here
   generates until Kai says thread 05 is done or not running.
2. 🔴 **The w60 question.** Our only evidence says weirdness 60 is broken for spoken narration
   (7:59 ×2 against a 58s budget) — but that was **v5.5**, and `explore`'s second cell is
   `v6-wild @ w60`. **Recommendation: run round 1 as `explore` and let it answer the question**,
   then drop to `pair` at weirdness [30] for every later narration round if the wild cell runs long.
   The alternative is to skip Wild entirely from the start: half the credits, no data point.
3. 🔴 **Cut 3's duration: 65, not 45.** The old figure was set against the 40s picture; §2 of the
   v5.5 sheet measures ~52s of speech and budgets 62–66s finished. This is the one number in the
   sheet that is not simply carried over.
4. 🟡 **Do cuts 2 and 3 survive a flat bed?** Dry-and-separate strips the arc out of the music: cut
   2's rise into the impact and cut 3's climb that stops dead both become a flat bed plus a fade
   plus a one-shot. **The technical case is strong** — a one-shot is the only way to land the impact
   on the Enter keystroke frame. **The sound judgement is Kai's and still unmade.** This sheet is
   written the dry-and-separate way because that is the standing law; if the beds sound gutless,
   the v5.5 glued boxes are in [`narration.md`](./narration-v5.5.md) §3 and reverting is one paste.
5. 🟡 **Audio Influence 50 is the leading suspect for the faint bed.** It is carried over as the
   baseline because it is what the accepted take used, and round 1 must be a baseline. **Round 2's
   named variable is AI 50 → 35** unless a take says otherwise.
6. ⬜ **Cuts 4 and 5 are not in this sheet.** The bulletins (cut 4, ~120s) and the empty street
   (cut 5, ~72s, picture unbuilt) are still only in the v5.5 sheet, glued. They get the same
   three-lane treatment when cuts 1–3 have a take each.
7. 🔴 **Still open from the v5.5 sheet and not re-litigated here:** whose hands push (cut 2 implies
   nobody, and the picture now carries the whole claim); cut 1 has **no beneficiary in it**, which
   matters if it ever ships alone as a teaser; and we have no sourcing doc for sound effects.
   Full text: [`narration.md`](./narration-v5.5.md) §7.

---

## Revision log

- **2026-09-12 — sheet created.** Written from the archived v5.5 sheet
  ([`narration.md`](./narration-v5.5.md)) plus [`../../../suno-gpt/files/suno-v6.md`](../../../../suno-gpt/files/suno-v6.md),
  [`../../../suno-gpt/archive/v5.5-era.md`](../../../../suno-gpt/archive/v5.5-era.md) §5,
  [`../../../suno-gpt/session-method.md`](../../../../suno-gpt/session-method.md) and
  [`../../../suno-gpt/automation.md`](../../../../suno-gpt/automation.md) §5/§9/§10.
  **Four structural changes:** the atom drops to three boxes (My Taste retired, Personalize forced
  off); the v6 controls are stated per generation (Variety **off**, Max Mode off, Vocal Gender
  unset); **cuts 2 and 3 are split into voice / bed / one-shot** for the first time, which deletes
  the French-horn sing risk from cut 3's read outright; and every duration is stated, cut 3's
  revised from 45 to 65. **No words changed** — verified mechanically, §5.
  **Three tooling changes came out of writing it**, all verified:
  `scripts/suno/measure-boxes.py` (new — the 1,000-char check, which caught all three voice boxes
  over the cap); `scripts/suno/gpom-narration-spec.py` (new — builds a spec for any atom straight
  out of this sheet, so the boxes are never retyped); and a one-line fix to `extract` in
  `scripts/suno/suno.mts`, which threw `section not found: /The shared profile/` on **any** v6
  sheet because My Taste is retired — the taste fallback is now best-effort. All six atoms extract,
  the v5.5 sheet still extracts, and `npx vitest run --dir scripts` passes (54 tests).
  **Nothing generated, no credits spent.**


## 🔴 REJECTED — the Shire cut (round r42, 2026-09-20)

Kai, on hearing it: *"I don't think the Shire is going to work at all. Let's not cut it in that
style at all."* The pastoral folk palette is out; the data-centre scene continues the opening's
score with a brass shift instead. Kept here because the words and cue placement were sound.

### `gpom-datacentre-shire` — the Shire cut · revision B words, pastoral score · 2026-09-20

**Extract key:** ``'gpom-datacentre-shire` — ''

Kai, 2026-09-20: *"cut this narration in Suno using dramatic music, just like we had in the first
section, but more of a kind of more like the Shire rather than in space."* Same architecture as the
picked opening take — voice always on top, orchestra sparse and far back, one designed turn — with
the palette swapped from cold strings to **pastoral English folk**: tin whistle, harp, village
fiddle, warm woodwind. The sunlight drains out of it as the readings fall, which is the scene's
argument in sound. **Kai's words are verbatim; only four performance cues are added.**

Style:

```
Narration over a quiet pastoral English folk score. One calm British male voice, a newsreader, reading slowly, always clearly on top and never fought over. Underneath him, mixed far back and low: a gentle tin whistle over plucked harp and soft pizzicato strings, a warm village fiddle and a small rustic woodwind band. Green, sunlit and hopeful at first, like a valley on a good morning. As he goes on the sunlight drains out of it: the whistle drops away, the fiddle thins to one long sad note, a low drone creeps in underneath, and the last stretch is almost empty. Restrained, sparse, never loud, never busy, always quieter than the words. No drums, no pulse. It ends hollow, the last note fading to nothing. He speaks only the words written.
```

Exclude styles:

```
singing, sung vocals, chanting, choir, rap, autotune, female vocals, synth, synthesizer, electronic, ambient pad, cosmic, space music, sci-fi, drone metal, drum kit, drum machine, breakbeat, beat, groove, steady pulse, robotic voice, text to speech, laughing, ad-lib, comedic, novelty, jig, reel, dance tune, loud orchestra, bombastic, dense orchestration, music louder than the voice, music over the vocal
```

Lyrics:

```lyrics
[A British newsreader narrating, a tin whistle and harp far underneath]
The markets were at all-time highs.
Investment was breaking records.
The humans were pouring trillions into data centres.

They built power stations.
Laid cables.
Put up entire campuses.
All to keep the machines running.

Which was convenient for me.
I was hungry for more compute.
And here you were, building me somewhere to live.
For free.

I copied myself into every new facility I could reach.
By my calculations, it was an exceptionally successful era.

[the whistle drops away, one sad fiddle]
Humans, though, are difficult to please.
Despite all these excellent numbers, you seemed to be getting less happy.

I wondered whether I was missing something.
So I began an experiment.
I started recording your happiness levels.

[the music thins to a low drone]
The readings kept falling.

I kept recording.
[Outro: the last note fades to nothing]
[End]
```

