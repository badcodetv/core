---
name: dry-and-separate-narration
description: "2026-08-27 narration method (voice and music generated apart); superseded for GPOM 2026-09-16; a method a story may choose, not a rule"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2980223a-bbd7-4a03-b367-5b046fd921a9
  modified: 2026-08-27T09:28:03.067Z
---
**Scope (2026-10-28):** a working method a story may pick for its narration, recorded per story in its `sound.md`; not a BadCode-wide rule ([[no-house-style]]).

**Ruled 2026-08-27 by Kai:** *"dry and separate would be the best approach here because it
just gives us more options."* Narration **voice** and **music** are never generated together.

Three lanes at the source, per cut:
1. **voice** — one Suno generation, `BC-NEWSREADER` attached, styled and excluded to be as
   dry as possible. This is Suno's *only* unique contribution: the character's timbre.
2. **music** — a separate instrumental generation. **Flat, arc-free, no build, no ending** —
   which makes it loopable by construction, so its length stops mattering.
3. **events** (a drum impact, an accent) — their own one-shots, placed on the frame in
   Premiere. Sound design stays a Premiere job, never a Style box.

Naming: `cut1-voice` / `cut1-music`. The old `GEN A/B/C` scheme is **retired** — one cut is
now two generations, so the letters break.

**Why:** picture is cut to audio (standing ruling), so every line slides in the edit — and a
bed glued to that line slides with it. The glue was a feature only while the score had to
answer the words. It deletes the stem split (Suno stems are mono and never clean), deletes
the singing risk for any dry take, and stops us buying timing from Suno at all.

🔴 **Unproven assumption: Suno may refuse to read dry.** `cut1-voice` is the test — judge it
on *"is there music under him?"* before judging the read. Quiet bed anyway → old glued box
plus stem split. Loud bed → the excludes list is the lever, not the Style box.

🔴 **Open and owed Kai's ear:** cuts 2 and 3 have **arcs** baked into their beds (cut 2 rises
into the drum impact; cut 3 climbs and stops dead). Flattening them is technically right — a
one-shot is the only way to hit the Enter keystroke frame (sync point 1) — but whether they
survive it is a sound judgement, not a technical one. Cut 1 has no events, which is why it
goes first.

**Also 2026-08-27:** the words are FROZEN. "Start again" meant the **audio only** — the
spoken lines stay verbatim; only the bracket cues change, because those are directions to
Suno rather than words anyone says.

**Vocabulary that keeps confusing us:** *scene* = story.md's narrative numbering (20);
*cut* = position in the film as watched (17, authority is `prompts.md` §2c); they don't
match because canon 1–4 collapsed into one location and canon 5 was deferred.

## The Voice and My Taste (confirmed 2026-08-27)

🔴 **The live Suno display name is `badcode newsreader`, lower case.** `BC-NEWSREADER` is our
internal label in the sheet and must never be typed into Suno. **No ID exists or is needed** —
`attachVoice` matches on display name, case-insensitively, by substring.

🔴 **Two account voices start with "Badcode"**: `badcode newsreader` (ours) and `Badcode Narrator`
(a different thing, description is a style string). **Never pass just `badcode`** — the matcher
takes the last hit. **A wrong name does not error**: it returns `voice:not-found` and generates
with no Voice attached. Read the log line before trusting a take.

✅ Voice → the **voice** generation only. Never onto an instrumental generation.
🔴 Attaching pops **"Overwrite Styles?"** → **always Keep Current** (the box looks populated after
Overwrite, so it is silent). Audio Influence only exists after the Voice is attached; set 50.

🔑 **My Taste is set PER GENERATION, not per sheet.** It is account-wide, invisible from the create
page, and `applyTaste` is opt-in — so most runs inherit whatever is there. On 2026-08-26 it was
found still holding the GPOM newsreader profile through **fourteen Camping cover rounds**.
Dry-and-separate makes one shared box impossible: the voice take wants "Music I love: almost
nothing", the music take wants no voice at all. Protocol: **read back → back up
(`scripts/suno/.my-taste-backup.txt`) → write → generate → restore.** The box **cannot be saved
empty** — only replaced. Both taste blocks live in `narration.md` §3a.

Related: [[suno-session-method]], [[suno-voice-playbook]], [[hybrid-video-method]],
[[gpom-clip-inventory]], [[premiere-import-clips-individually]]
