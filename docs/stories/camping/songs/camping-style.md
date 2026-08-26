---
title: Camping (style) — the non-cover scouting set
status: ROUND s1 — seven variations generating 2026-08-26. Supersedes the cover A/B (see §1).
parent_sheet: ./camping.md
cover_set: ./camping-cover.md
history: ./camping-prompt-history.md
workspace: camping-duet
model: v5.5
mode: Create (Advanced) — NOTHING attached
---
# Camping — the non-cover scouting set

Fourteen cover rounds all came back sounding like the record they were covering. Kai,
2026-08-26: *"we are locking ourselves in too much to the existing track."* So this set attaches
nothing, and **every input varies at once**.

| | |
|---|---|
| **The parent** | [`./camping.md`](./camping.md) — §4's ```lyrics block is the source of truth for the words |
| **The cover set it replaces** | [`./camping-cover.md`](./camping-cover.md) — rounds 1–14, frozen |
| **The variations, in code** | [`scripts/suno/style-variations.mts`](../../../../scripts/suno/style-variations.mts) |
| **The runner** | [`scripts/suno/style-ab.mts`](../../../../scripts/suno/style-ab.mts) |
| **Where takes land** | workspace `camping-duet`, titled `Camping SN <name> (s1)` |

---

## 1. 🔴 The finding that invalidates part of the cover rounds

**`My Taste` is account-wide, applies to every generation, cannot be turned off — and through
all fourteen cover rounds it held the GPOM newsreader profile, not Camping's.** Read back live
on 2026-08-26 and saved to `scripts/suno/.my-taste-backup.txt`:

> Vocals I love: **one** dark gravelly British male voice, speaking — a composed formal
> newsreader with received-pronunciation broadcast diction, reading plainly and slowly over
> music. **Pure spoken narration, plain speech**, an announcer reading to camera. Unhurried,
> quiet, absolutely certain, with long silences between his sentences.
>
> **Music I love: almost nothing.** A score that stays underneath a speaking voice and never
> fills the gaps between his sentences — one low string note held a very long time, and a solo
> cello beneath it holding long slow notes… Very few instruments, never a section and never an
> ensemble. **No piano.** Slow, cold, patient, foreboding.

So every camping generation since that profile was written was arguing with a global box
demanding **one** voice for a **two-man duet**, **pure spoken narration** for a song whose Style
box asked for post-punk spoken word, and **almost no music** for a full drum-and-bass
arrangement. `camping.md` §1 says *"swap in for the session, restore your house profile after"* —
a GPOM session evidently wrote over it and it was never swapped back.

**What this costs us:** `camping-cover.md` §7 concluded the resemblance came from HEAD/TAIL plus
the unchanged words. That is still true and is now incomplete. Any cover-round finding of the
form *"genre X did not work"* is unsafe — X may simply have lost to the global box. The accepted
round-17 take is unaffected: it was **chosen by ear**, and a take that sounds right is right
whatever produced it.

**The standing rule this earns:** read My Taste back at the start of every session. It is the
only box that survives a page reload, belongs to no sheet, and is invisible from the create form.

---

## 2. Why this is a scouting round and not an A/B

The cover set moved one clause per round, which is correct while converging on a record. It is
wrong here: after fourteen rounds the question is no longer *which clause wins* but *is there
another record in here at all*, and one clause cannot answer that. So all five inputs move
together — **My Taste, Style, Exclude Styles, the lyric cues, and both sliders** — seven
genuinely different records come back, and we trade attribution for range. Attribution returns
next round, on whatever survives.

Duration is the one input deliberately **not** varied, on evidence: rounds 13–14 targeted 200s
and got 4:07–4:24 back. It is a suggestion Suno mostly ignores, so varying it adds noise without
adding range. Pinned at 200s for all seven.

---

## 3. The cue layer, and the guarantee on the words

The lyric block is the **only section-scoped box we have** (`camping.md` §4f). It carried
`gravelly ranting voice` ×4, `[shouting]`, `[shout, full chest]`, `[shout, cracking, begging]`,
`the guitar drops out here`, `the same guitar riff returns underneath` and `neuro bass growling
underneath` — every one of which contradicts at least one variation below. Inline and positional
beats global, so those cues would have overruled the Style box in exactly the sections that matter.

So each variation supplies a `cues` map of exact-substring rewrites, 9–19 lines each.
**`applyCues` guarantees the words never move:** every key must be found in the sheet or it is a
hard error, and stripping every `[...]` line from the result must give back `camping.md` §4
byte for byte. Inspect any variation offline with `style-ab.mts cues <id>`.

---

## 4. The set

| id | name | W | SI | style | taste | cues | what it is |
|---|---|---|---|---|---|---|---|
| `style-s1-metal` | Metal | 55 | 80 | 906 | 1073 | 16 | Down-tuned high-gain riff; guitars **stay in** through the drop. Half-sung snarl |
| `style-s2-orchestral` | Orchestral, sung | 45 | 85 | 903 | 1085 | 19 | Strings + low brass playing **through** the drop; two sung baritones |
| `style-s3-blues` | Blues | 35 | 75 | 929 | 1099 | 18 | Bottleneck slide + Hammond at 174; drawled, behind the beat |
| `style-s4-dub` | Dub + guitar — **the control** | 40 | 75 | 995 | 1246 | 9 | Round 11's arrangement, but nothing attached, taste rewritten, ranting cues gone |
| `style-s5-halfsung` | Dub, half-sung | 50 | 70 | 996 | 1233 | 15 | Sprechgesang on the dub spine |
| `style-s6-sung` | Dub, fully sung | 45 | 80 | 973 | 1207 | 16 | A real tune. Pairs with S2: same singing, one grand, one intimate |
| `style-s7-halftime` | Dub, half-time | 30 | 85 | 986 | 1277 | 14 | Spoken at half the beat's rate, kit still at 174 |

**S4 is the most valuable take in the set.** It is the only arrangement we have already heard, so
it is what separates "the globals and the cover audio were holding it" from "the genre was".

### Why the casting sentence became a variable

It was pinned through all fourteen cover rounds so a genre test stayed a genre test. Kai hears
every take as a UK grime MC — worth sitting with, because the box asks for `British post-punk
spoken word` and the exclude list bans `grime MC`, `UK drill`, `road rap` and `young MC`
outright. **The label was never what produced the delivery.** Three things were: `ranted over the
beat`, `half-shouted`, and 174 BPM — plus the words themselves, which are written in grime
prosody, dense internal multisyllabic rhyme landing on the beat (*cash from the bank for your
wank tank*; *a lack of work ethic, it's pathetic, getting parra lettic*). Adding excludes bans a
name we are not asking for. Changing the **delivery instruction** is the lever.

---

## 5. How this is driven

```bash
npx tsx scripts/suno/style-ab.mts plan            # the seven boxes + cue counts, offline
npx tsx scripts/suno/style-ab.mts cues <id>       # diff one variation's brackets vs §4, offline
npx tsx scripts/suno/style-ab.mts check           # live form + My Taste read back, spend nothing
npx tsx scripts/suno/style-ab.mts taste-backup    # REQUIRED before run — saves the house profile
npx tsx scripts/suno/style-ab.mts load <id>       # fill one variation whole, generate NOTHING
npx tsx scripts/suno/style-ab.mts run [ids...]    # 10 credits and 2 takes per id
npx tsx scripts/suno/style-ab.mts taste-restore   # put the house profile back — DO THIS AFTER
```

### The facts this run established

🟢 **`setTaste` works.** It had sat in `suno.mts` unverified since it was written — `automation.md`
never recorded it landing, because "it clicked Save" is not evidence. `getTaste` is new and reads
the box back; the write was confirmed at 1207/1207 characters on 2026-08-26.

🟢 **Create mode is confirmed by its sliders.** Weirdness and Style Influence only — no Audio
Influence control exists when nothing is attached. That reading is the cheapest proof that a run
is not secretly a cover.

🔴 **The guard is inverted from the cover runner.** `cover-ab` aborts when the audio is *missing*;
this aborts when it is *present*. A leftover attachment would silently turn all seven into covers
of the record we are escaping, and every take would come back sounding right-ish and prove nothing.

🔴 **My Taste is global state that outlives the run.** `run` refuses to start without a backup on
disk, reads back every write, and ends by telling you to restore. The backup is gitignored.

---

## 6. Round log

### s1 — 2026-08-26, seven variations, W/SI per row above, Duration 200s

**All seven generated, 14 takes, ~70 credits.** House `My Taste` restored afterwards (734 chars,
read back and confirmed). Verdicts to be filled in by ear.

| id | takes | verdict |
|---|---|---|
| S1 Metal | 4:01 / 3:46 | — |
| S2 Orchestral, sung | 2 | — |
| S3 Blues | 2 | — |
| S4 Dub (control) | 2 | — |
| S5 Dub, half-sung | 2 | — |
| S6 Dub, fully sung | 2 | — |
| S7 Dub, half-time | 2 | — |

**S1 came back at 4:01 and 3:46**, against 4:07–4:24 for the cover rounds at the same 200s
target. Shorter, still not 3:20 — consistent with duration being a ceiling Suno aims under
rather than a length it hits.

**One interruption, one fix.** The run stopped at variation 2 on the known exclude-box
truncation (180/695) — the fourth occurrence, and the fourth time on the *second* variation of a
multi-id run. Nothing was spent. `fillChecked` (clear → blur → refill → blur → read back, ×4)
was added and S2 then filled 695/695 on the same slot. Recorded in
[`automation.md`](../../../suno-gpt/automation.md) §6.

**Watch for:** S3's accent pulling to America (`American accent`, `American vocal` and
`southern drawl` stay banned for exactly that reason); S7 half-timing the **drums** rather than
the vocal (`half-time` is lifted from the excludes for it, and the middle, the taste and the
verse-2 cue all say full 174 as the counterweight).
