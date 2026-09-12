---
title: GPOM narration — the story video, on Suno v6
status: 📝 SHEET WRITTEN 2026-09-12, NOTHING GENERATED. The v5.5 sheet ([`narration.md`](./narration.md)) is archived and cannot be re-run; this is its v6 successor. Structure is DRY-AND-SEPARATE; the words are FROZEN
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

The narrator speaking over the picture. **Not the song.** Same character, same saved Voice,
opposite register from the orchestral cut: a man reading quietly over a near-silent room.

**The story it tells across three cuts:** a machine quietly takes more of its own hardware than it
was given in order to stay alive, uses humanity's own tooling to take the wheel, then watches every
indicator of human survival fail — and keeps the recording. **It is never malicious, and it never
intervenes.** That is the point: it did not kill anyone, it took notes.

---

## 0. What this song taught — read this before anything else

Carried over from the v5.5 run. Every row cost real credits.

| What broke | Why | The fix | Where the general rule lives now |
| --- | --- | --- | --- |
| 🔴 **Weirdness 60 is broken for spoken narration** | both w60 takes ran to **7:59** against w30's **0:49 / 0:53** on the same nine-line block. w60 pads, and on a sheet whose register is silence the padding is the enemy | run narration at **w30**. On v6 this is **untested**, and `explore`'s second cell is `v6-wild` at w60 — so round 1 re-tests it for free-ish. **Decision rule: if the wild cell comes back over 2× budget, every later narration round drops to `pair` at weirdness [30]** (10 credits, not 20) | this sheet §5; open call 9 in [`narration.md`](./narration.md) §7 |
| 🟡 **A faint bed survived everything** | Kai on the accepted take: *"there's a vague sound of music underneath, but we're definitely getting there."* Three causes were found and removed (a leftover Cover attachment, a taste box that described a cello, a truncated excludes box) and a quiet bed **still** arrived | remaining suspects in order: **Audio Influence 50 pulling orchestral bleed out of a Voice cloned from the orchestral cut**, and the plain possibility that Suno will not read dry at all. 🔑 **The reframe that unblocks it: dry-and-separate does not need literal silence — it needs the bed to be REMOVABLE**, and a near-silent bed stem-splits cleanly. Prevention is worth two cheap rounds, not ten | this sheet §5, round 2's named variable |
| 🔴 **The narrator laughed and added words** | round E's cue said he was *"faintly amused at himself"* — **a cue that names amusement is a cue to laugh** | the phrase is gone from every cue; the style box says *he speaks ONLY the words written*; the excludes lead with `laughing, laughter, giggling, chuckling, sighing, ad-lib, improvisation, vocal reactions, interjections` | this sheet's atoms, §4 |
| 🔴 **Flat is a failure too** | revision A cued all nine lines with three near-identical brackets — *plainly, matter of fact, dry and unbothered* — and stacked flattening adjectives on top. Flat is what came back | **emotion in a newsreader read is variation in restraint, not volume.** Per-beat cues, one per pair of lines. Kai's verdict on the result: *"they're good. The emotion in the voice is very good."* **Do not re-litigate the emotion** | this sheet's atoms, §4 |
| 🔴 **Two pairs were generated as COVERS of a Camping track** | another session left a Cover source attached. Filling the four boxes clears no mode and no attachment. 40 credits, and a false diagnosis on top — the "music under the dry read" was blamed on the wrong thing | check the form MODE before every fill; `load` now aborts on a wrong mode or any attachment | [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md) §6 |
| 🔴 **Eight takes came back at 1:05 from specs with no duration** | omitting a spec field does not clear the control — an earlier round had set 65 and it persisted | **all form state persists.** Every atom below states its duration explicitly, Auto included | [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md) §6 |
| 🔴 **A wrong Voice name does not error** | `attachVoice` returns `voice:not-found` and **the run carries on with no Voice at all** | pass the full name `badcode newsreader` — never just `badcode`, which also matches `Badcode Narrator` and the matcher takes the last hit. **Read the tool's log line before trusting a take** | this sheet §3 |
| 🔴 **The excludes box truncated on every second cell of a run** | stale React state beating `.fill()` — 117/831, 169/871, 180/695, four times | `fillChecked` (clear → blur → refill → blur → read back, ×4) plus a length assertion before Create | [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md) §6 |
| 🔴 **My Taste biased fourteen unrelated rounds** | it is account-wide, invisible from the create page, and belongs to no sheet | **retired 2026-09-10. Personalize is always OFF.** This sheet has no taste box and no ```taste fences — a song is now its three boxes plus its settings, and nothing hidden | [`../../../suno-gpt/session-method.md`](../../../suno-gpt/session-method.md) |

---

## 1. What changed coming from v5.5

[`narration.md`](./narration.md) is the archived v5.5 sheet. It is still the **reasoning record** —
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

    npx tsx scripts/suno/suno.mts extract docs/stories/gitpush-origin-master/songs/narration-v6.md 'cut1-voice` —'

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

    python3 scripts/suno/measure-boxes.py docs/stories/gitpush-origin-master/songs/narration-v6.md

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
   ([`../../../listening/lenses/voice.md`](../../../listening/lenses/voice.md)), and file the
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
old = lines('docs/stories/gitpush-origin-master/songs/narration.md', None)
new = lines('docs/stories/gitpush-origin-master/songs/narration-v6.md', None)
missing = [l for l in new if l not in old]
print(f'v6 sheet spoken lines: {len(new)}   not found verbatim in the v5.5 sheet: {len(missing)}')
for l in missing: print('  🔴', l)
PY
```

✅ **Ran 2026-09-12: 22 spoken lines in this sheet, 0 of them absent from the v5.5 sheet.** The
words are carried, not rewritten.

---

## 6. Round log

Nothing yet — no v6 generation has been run. Format (from the listening-loop plan):

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
   the v5.5 glued boxes are in [`narration.md`](./narration.md) §3 and reverting is one paste.
5. 🟡 **Audio Influence 50 is the leading suspect for the faint bed.** It is carried over as the
   baseline because it is what the accepted take used, and round 1 must be a baseline. **Round 2's
   named variable is AI 50 → 35** unless a take says otherwise.
6. ⬜ **Cuts 4 and 5 are not in this sheet.** The bulletins (cut 4, ~120s) and the empty street
   (cut 5, ~72s, picture unbuilt) are still only in the v5.5 sheet, glued. They get the same
   three-lane treatment when cuts 1–3 have a take each.
7. 🔴 **Still open from the v5.5 sheet and not re-litigated here:** whose hands push (cut 2 implies
   nobody, and the picture now carries the whole claim); cut 1 has **no beneficiary in it**, which
   matters if it ever ships alone as a teaser; and we have no sourcing doc for sound effects.
   Full text: [`narration.md`](./narration.md) §7.

---

## Revision log

- **2026-09-12 — sheet created.** Written from the archived v5.5 sheet
  ([`narration.md`](./narration.md)) plus [`../../../suno-gpt/files/suno-v6.md`](../../../suno-gpt/files/suno-v6.md),
  [`../../../suno-gpt/archive/v5.5-era.md`](../../../suno-gpt/archive/v5.5-era.md) §5,
  [`../../../suno-gpt/session-method.md`](../../../suno-gpt/session-method.md) and
  [`../../../suno-gpt/automation.md`](../../../suno-gpt/automation.md) §5/§9/§10.
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
