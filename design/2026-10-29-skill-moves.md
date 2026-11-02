# Skill moves — story taste taken out of the skills, for the story files (2026-10-29)

Handoff from the skill pass of [`2026-10-29-style-leak-audit.md`](./2026-10-29-style-leak-audit.md) §2.
The skills now say "from the story's `look.md` / `sound.md`" (or keep a labelled example). The
text below came out of a skill, or was relabelled there as one story's. **Nothing has been added to
any story file yet**: the story-file agent (or Kai/Jack) places each item, then ticks it.
"Already there" means the story file already carries the rule; add only what is missing.

## gitpush-origin-master — `look.md`

Section **Rules for this story** (the gates), unless noted.

- [x] **Already there** (`look.md` ~L102–111): one bright anchor in the dark, visible cost in any
  monumental frame, name the light source in the world. Shot-craft now calls these *GPOM's gates*
  (gate 2 = "does the story's look.md add a gate? GPOM's does"). If you want shot-craft's fuller
  wording of the visible-cost gate, it was:
  > **Is there a visible cost in frame?** Mandatory on any monumental shot — scale, symmetry, a
  > machine, an institution. Wreckage, exhaustion, a body that failed, someone the system is
  > failing. Without one, the grammar of power reads as celebration of it, and meaning it
  > ironically does not protect you. *(This is the picture version of `the-reader.md`'s standing
  > rule: never raise a fear without naming the beneficiary.)*
- [x] **Add — depth** (from shot-craft Design step 3):
  > Never leave the foreground empty — it is the most common cause of a flat frame and it is free.
- [x] **Add — camera movement** (from shot-craft Design step 9 and "The motion budget"; GPOM's still
  / documentary passages, not the dramatic ones in § the animation rule):
  > What moves, if anything: default is nothing. A single moving shot in a still body of work lands
  > with outsized force, and only if the stillness around it is real (*La Jetée* spends 26 minutes as
  > photographs and its one moving shot exactly once). Motivated stillness: free, always available.
  > Motivated movement: worth spending roughly once per sequence. (Camera movement only: a
  > locked-off frame full of working machinery does not spend the budget.)
- [x] **Add — held stills** (from shot-craft):
  > A still that truly holds still reads as a scanned photograph. Give it a reason to feel
  > photographed — a low-amplitude camera drift, one light changing, grain that lives.
- [x] **Add — what carries the motion** (from scene-animation; section **Rules**, beside "animate
  dramatically", which is already there at ~L137):
  > Few movers: give the motion to rain, haze, light and one actor. The motion is an argument: the
  > machine that doesn't care, the wealth piling while the room dims.
- [x] **Already there** (~L147–152, Calibration): teal-orange "name the real light source instead";
  "Over-lit 'epic' scenes and the centred lone posed figure. Symmetry belongs to architecture, not
  to a hero." new-image now keeps that list as a diagnostic only, with no "symmetry" ruling and no
  "one named light?" check (that check was GPOM's: "one named light" in the prompt critique).
- [x] **Already there**: "darkness that reads as depth" (~L105). scene-images no longer says it.
- [ ] **Check** *(story-files agent, 2026-10-29: "Bulletin realism" is not in any GPOM file; left unplaced, nothing invented)* — the scene.json template in `new-scene` used GPOM's looks as its example
  (`"styles": {"threads": "1980s BBC 16mm"}`, `"looks": {"news": "Bulletin realism"}`). 16mm is in
  § Per part (B · Maddie at the door). "Bulletin realism" is not found in `look.md`: if it is a GPOM
  look name, add it to § Per part.

## gitpush-origin-master — `sound.md`

- [x] **Narration / voices — per-cut duration budgets** (from suno-automation "Timing"; ruled
  2026-08-24, within ±10 s of the cut's budget):

  | Cut | Budget | `durationSec` |
  | --- | --- | --- |
  | 1 · awakening | 56s | 60 |
  | 2 · the push | ~27.8s | 30 |
  | 3 · plant room | 40s | 45 |

  ⚠ Conflict to settle while placing it: suno-automation says *aim slightly ABOVE the budget*
  (Suno "shortens reliably but fails to stretch"); `songs/narration.md` L44 says *set it ~15 s BELOW*
  (Suno overshoots on v6). Both are in the skill/doc now; one of them is stale.
- [x] **Narration / voices — the saved Voice** (from suno-automation, now labelled GPOM's there):
  > The Suno Voice `badcode newsreader` is GPOM's narrator Voice. Attaching it offers "Overwrite
  > Styles?" with the persona's own style — the orchestral 174 BPM chant. Always Keep Current.
- [x] **Narration / voices — how the narrator Voice was built** (from suno-prompt "The narrator
  problem"; the skill now keeps only the engine fact):
  > Build the narrator's Voice in a register that has nothing to do with the song's genre — spoken
  > oratory, opera, a gospel preacher, a sardonic crooner. The genre mismatch is what breaks Suno out
  > of its generic per-genre vocal default, and it's the cheapest route to a vocal no other Suno D&B
  > track has. Audio influence 40–60 for the strongest effect.
- [x] **History — the old standing slider pair** (deleted from suno-automation as a BadCode-wide
  rule). It was born on GPOM narration (titles `gpom-cut1-A-v6-w30` / `-w60`); GPOM's later rounds
  ran weirdness 25 / w10–20, so place it under History unless Kai says another story still uses it:
  > Every attempt is a PAIR — Style influence 75, run once at weirdness 30 and once at weirdness 60,
  > titled `…-w30` and `…-w60`. Sometimes 30 reads better, sometimes 60 does, and the rule that
  > predicts which is not yet known — so both always run. Never generate at only one setting.
  > Record which won and why. On v6 the pair was one row of a grid; the proposed R1 was
  > {v6, v6-wild} × weirdness {30, 60} (`docs/suno-gpt/automation.md` §9, awaiting Kai).

## karen — `sound.md`

- [x] **Rules for this story** (from suno-prompt "The satire trap"; the skill now keeps only the
  engine fact that comedy words summon kazoo/vaudeville novelty). It was written as BadCode's whole
  register, learned on the Karen track (2026-07); placed in Karen's file per the audit. If Kai wants
  it for another story, that story writes it too:
  > Dark satire played straight — the joke is in the words, never in the music. Whenever the concept
  > is absurd but the sound must be serious, state the register explicitly and negate the default,
  > with the negation repeated for weight: `…no comedy, no novelty, played completely straight.` Put
  > comedic/novelty/parody in Exclude Styles as well. This holds even when the user literally asks
  > for a funny song: "Funny hip hop" translated faithfully ("comedic deadpan", "comedy-skit energy"
  > in the Style box) summons kazoos and vaudeville — less funny, not more. The humour goes in the
  > lyrics and the conceit; the arrangement stays sincere and warm. (Karen track, 2026-07: first
  > drafts led with "comedic" and had to be stripped.)

  (Karen's Exclude list already bans kazoo / slide whistle / circus / novelty, `sound.md` ~L42, L120.)

## bank-robbery — `sound.md`

- [x] **Tracks / History** (optional; both clauses already live verbatim in
  `songs/bank-robbery-jack.md` L2158 and L2528, so nothing is lost). suno-prompt still quotes them,
  now labelled "Bank Robbery's — never paste into another story":
  - `Bristol trip hop, a hushed close-mic murmuring English man…` (genre-first voice move)
  - `London retro soul, a raw husky contralto woman with a heavy North London accent` (a real
    singer, translated; 2026-10-21, `suno-voices.md` §2c)

## bank-robbery — `look.md`

- [x] **Already there** (§ Rules ~L21, L47): saturated colours per place, two lights of different
  colours. flow-prompt now calls it Bank Robbery's answer to the muted default, not every prompt's.
- [x] **Add, if not there** (new-image now cites it as an example): Bank Robbery prompts run short —
  Jack 2026-10-09 asked to halve the prompt (memory `bank-robbery-prompts-short-colour-design-round`).

## camping — `sound.md`

- [x] **Narration / voices — pointer** (from suno-prompt "Getting a man to TALK"; the table stays in
  the skill, now labelled "Camping's tested narration boxes"). Add a pointer so Camping's own file
  owns it: "The narration boxes that got a man talking (2026-09-01, ten rounds) — skit/interlude pool
  word, `a man talking over a beat`, one unpitched bed; the whole poetry pool excluded; `[Monologue]`
  + prose paragraphs — are in suno-prompt §Getting a man to TALK and `docs/suno-gpt/suno-voices.md`
  Thread 5."
- [x] **History — casting by tradition** (from suno-prompt, now labelled Camping's there):
  `British post-punk spoken word` for the middle-aged working-class bloke, `BBC English` /
  newsreader for the establishment one; `UK grime` fixed the nationality but cast both as young MCs;
  stripping `UK grime influence` with the accent language sent both men American.
- [x] **Already there**: the 174 BPM drum-and-bass foundation as Camping's one shared constant in a
  genre sweep (suno-automation used it as its example; now it says "Camping's brief named its drum
  foundation").
