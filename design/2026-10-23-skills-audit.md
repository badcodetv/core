# Skills audit — 2026-10-23

Kai asked: *"look through all the skills we have… have we duplicated some? Could some be merged together? I don't
want to leave a massive bombsite of half-finished skills that only get used once or twice."* Also: *"check that
the timeline page is also its own skill."*

This file is the audit trail: the evidence, a verdict per skill, the rulings owed, and the work left, as
tickets. **Done the same day** (see the Log): Kai followed the recommendations on all three rulings and added a fourth, splitting new-scene into stage skills.

## How it was measured

- **Size, age, commits:** `git log` on each `.claude/skills/<name>/` folder.
- **Use:** every Claude session still on disk (21 sessions, **24 Sep to 23 Oct 2026**; older ones are cleaned up
  automatically): counts of `Skill` calls, plus sessions that read the skill's SKILL.md directly.
  **One month is a short window.** A skill unused in it isn't dead, but it isn't part of how we work now.
- **Fit:** whether the skill matches how we work now. Films (GPOM, then Camping, Karen and Bank Robbery, as film + song on
  YouTube) are made through `new-scene` and timeline pages. The comic website pipeline has been quiet since August.

## The evidence

| Skill | Lines | Made | Last changed | Commits | Calls (month) | Sessions (month) | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| flow-automation | 714 | 08-20 | 10-17 | 16 | 13 | 8 | ✅ keep |
| suno-automation | 528 | 08-24 | 10-22 | 15 | 9 | 5 | ✅ keep |
| suno-prompt | 689 | 06-16 | 10-23 | 27 | 3 | 5 | ✅ keep |
| flow-prompt | 169 | 08-12 | 10-09 | 7 | 5 | 4 | ✅ keep |
| new-scene | 236 | 10-19 | 10-23 | 5 | 2 | 4 | ✅ keep, **split stage 4 out** (ruling 1) |
| shot-craft | 183 | 08-26 | 10-09 | 3 | 2 | 4 | ✅ keep |
| chief-of-staff | 97 | 10-14 | 10-19 | 5 | 1 | 4 | ✅ keep, absorbs new-marketing-idea |
| premiere-automation | 488 | 08-21 | 08-27 | 6 | 3 | 2 | ✅ keep |
| video-fx | 209 | 08-23 | 08-27 | 3 | 3 | 2 | ✅ keep |
| story-craft | 144 | 08-23 | 10-23 | 4 | 1 | 2 | ✅ keep |
| new-story | 89 | 06-17 | 10-23 | 7 | 0 | 2 | ✅ keep (the words; overview-board is the film) |
| lip-sync-dub | 136 | 10-19 | 10-21 | 4 | 1 | 1 | ✅ keep (new, specialist, in use on GPOM) |
| find-footage | 397 | 08-23 | 09-29 | 4 | 1 | 1 | ✅ keep (MMT and the footage budget depend on it) |
| overview-board | 105 | 10-23 | 10-23 | 1 | — | 1 | ✅ keep (made today) |
| new-idea | 123 | 06-29 | 08-23 | 3 | 0 | 0 | ✅ keep (cheap inbox, used when ideas pop) |
| new-image | 161 | 07-13 | 08-20 | 10 | 0 | 1 | 🔀 merge: absorbs the house-look half of badcode-art-direction |
| badcode-art-direction | 153 | 06-27 | 09-12 | 12 | 0 | 1 | 🔀 split: house look → new-image; panel half → comics archive |
| continuous-shot | 54 | 10-20 | 10-20 | 1 | 0 | 1 | 🔀 fold into a recipe (marked DRAFT, one use) |
| new-marketing-idea | 71 | 07-22 | 07-22 | 1 | 0 | 1 | 🔀 fold into chief-of-staff (which already "takes in a new idea") |
| music-video-short | 257 | 07-01 | 08-23 | 8 | 0 | 1 | 📦 archive (ruling 3): superseded by new-scene; never live-run |
| make-comic | 263 | 06-25 | 09-12 | 13 | 0 | 0 | 📦 archive as one comics bundle (ruling 2) |
| edit-panel | 122 | 07-14 | 08-20 | 6 | 0 | 0 | 📦 comics bundle |
| animate-slide | 399 | 06-25 | 08-25 | 13 | 0 | 0 | 📦 comics bundle |

**23 skills now → 17 after the tickets** (16 kept or merged, plus the new timeline skill), with nothing deleted: archived skills
move to `.claude/skills-archive/`, where they aren't loaded but can be restored by moving the folder back.

## The duplicates and overlaps found

1. **The timeline page is not its own skill.** It's stage 4 of `new-scene`. But most timelines so far weren't made
   through new-scene's stages 1–3: GPOM cut 2, cut 3 A and B, and the ending C, D, E and reel were all built by
   their own scripts in `scripts/gpom/second-half-video/` and then fed to the shared timeline builder. The timeline is the part
   of the editor used most, and it's used on its own. → **Ruling 1.**
2. **Two "capture a marketing idea" doors.** `new-marketing-idea` (one commit, July) and `chief-of-staff` (which
   "takes in a new idea"). The chief of staff owns the board, so the idea should land there. → fold.
3. **Two "BadCode look" skills.** `badcode-art-direction` (panels) and `new-image` (brand images) each carry
   their own copy of the house look and the plan → critique → generate loop. → one home for the look.
4. **Two "make a video" pipelines.** `music-video-short` (10–20 s, July, never live-exercised per memory) and
   `new-scene` (what we actually use). Shorts for marketing now come from scene clips and the chief of
   staff's cut lists. → archive the old one.
5. **A one-use technique as a whole skill.** `continuous-shot` is a procedure (chain Omni clips last frame to
   first), marked DRAFT. It belongs as a recipe in `docs/video-fx/hybrid-method.md` §4 (which it already
   cites), with one line in `new-scene` and `flow-prompt` pointing at it.
6. **The comic pipeline, four skills deep.** `make-comic`, `edit-panel`, `animate-slide` and the panel half of
   `badcode-art-direction` serve the scroll-comic website. Untouched in the month; they reference the bucket
   pipeline (`comics-v2`, `assets.manifest.json`) and the `badcode panel` command. → **Ruling 2.**

Not duplicates, deliberately split (keep as they are): the **mechanics / craft pairs** (`flow-automation` /
`flow-prompt`, `suno-automation` / `suno-prompt`) and the **judgement / mechanics pair** (`video-fx` /
`premiere-automation`). They're the most-used skills and the split is what keeps each one readable.

Outside skills, noted for later and not in scope here: `docs/flow/` vs `docs/google-flow/` (already flagged in
CLAUDE.md), and **CLAUDE.md itself repeats every skill's description at length**. Once the skills settle, a trim
should cut CLAUDE.md's skill bullets to one line each.

## The editor, after the tickets

```
overview-board   the film       skeleton, running order, which part to open        (story level)
  new-scene      make a part    brief → mood board → storyboard → clips             (stages 1–3)
  scene-timeline cut a part     rough cut → timeline page → notes → rounds → Premiere   (NEW, from stage 4)
  provenance     how it was made  cards, trail, final.json   (a doc + prov.py; not a skill)
engines          flow-automation · flow-prompt · suno-automation · suno-prompt · premiere-automation · lip-sync-dub
judgement        story-craft · shot-craft · video-fx · find-footage
words & ideas    new-story · new-idea · chief-of-staff (incl. marketing ideas)
look             new-image (incl. the house look)
```

## Rulings owed (Kai)

1. **Split the timeline page into its own skill (`scene-timeline`)?** Recommend **yes**. It's the most-used part of
   the editor, it's used on cuts not made through new-scene, and the three-layer app (film → part → cut) reads
   cleanly. Cost: new-scene shrinks to stages 1–3 and points onwards; nothing else changes.
2. **Are comics still part of the plan?** If not soon: archive the four comic skills as one bundle (recommended,
   restorable). If yes: merge them into one `comic` skill (make, edit a panel, animate a panel) instead of four.
3. **Archive `music-video-short`?** Recommend yes: new-scene plus the chief of staff's cut lists do the job. Its
   `docs/shorts/` folder stays as it is.

## Tickets (the work remaining)

- [x] **T1 · scene-timeline skill** (needs ruling 1). Move new-scene stage 4 into `.claude/skills/scene-timeline/SKILL.md`. Cover:
  the edl format (`scripts/scene/timeline.py`), building and publishing, reading notes, answering on the page
  (`cut-notes.json`), rounds, provenance (`trail`, `check`, `freeze`), and building into Premiere as a new sequence. Add how to put an
  **existing** cut (made by its own script) onto a timeline page. new-scene stage 4 becomes a pointer.
- [x] **T2 · Fold new-marketing-idea into chief-of-staff.** Its interview (lever, trigger, channels, human gate,
  dependencies, success signal) becomes a section of the chief of staff's intake. Archive the skill.
- [x] **T3 · One home for the BadCode look.** Move the house-look calibration and the anti-generic-AI section from
  `badcode-art-direction` into `new-image` (renamed in its description to cover any still in the house look). The
  panel-specific half goes with the comics (T5).
- [x] **T4 · continuous-shot → recipe.** Its procedure goes into `docs/video-fx/hybrid-method.md` §4 (or its own file in
  `docs/video-fx/`), with pointers from `new-scene` and `flow-prompt`. Archive the skill.
- [x] **T5 · Comics** (needs ruling 2). Either archive `make-comic`, `edit-panel`, `animate-slide` (and the panel half of
  art-direction) to `.claude/skills-archive/comics/`, or merge them into one `comic` skill.
- [x] **T6 · music-video-short** (needs ruling 3). Archive it.
- [x] **T7 · The archive itself.** Make `.claude/skills-archive/README.md`: what's there, why, the date, and how to restore
  (move the folder back). Fix every link to an archived skill (CLAUDE.md, other skills, docs) so nothing points
  at a skill that no longer loads.
- [x] **T8 · CLAUDE.md trim.** After T1–T7: one line per skill in the "How to work" list, the detail left in each
  skill. Update the repo-map skills row.
- [x] **T9 · Sweep.** Check every remaining SKILL.md for dead references (old Flow URLs, removed tools, superseded
  rulings), and that each description's trigger phrases don't collide with another skill's.

## Kai's ruling (2026-10-23)

*"I'm just going to follow your guidance."* Rulings 1–3 as recommended (timeline split out, comics archived as a
bundle, music-video-short archived), plus a fourth from Kai: **each stage of new-scene is its own skill**, and
new-scene just runs them. *"Stage one is talk about what the rough beats are… then image ideation… a sequence of
those images into animated ones… then timeline. And the overview strings these timelines together."*

## What was done

| Ticket | Outcome |
| --- | --- |
| T1 | new-scene split into **`scene-beats`**, **`scene-images`**, **`scene-animation`**, **`scene-timeline`**; new-scene is now the conductor holding the shared folder layout, `scene.json` and tools. scene-timeline also covers cuts made by their own script (they only need an edl) |
| T2 | the marketing-idea interview is part of `chief-of-staff` intake; its triggers moved into the CoS description |
| T3 | `new-image` is the one home of the look: MACHINE and PEOPLE registers, variety mode, calibration, casting. The comic panel record format stays in the archive |
| T4 | `docs/video-fx/continuous-shot.md`, linked from `hybrid-method.md` §4 and `scene-animation` |
| T5, T6 | archived to `.claude/skills-archive/` (`comics/` bundle + `music-video-short`, `new-marketing-idea`, `continuous-shot`). **Rescued first:** animate-slide's engine-agnostic "what the model cannot do" motion rules, now in `scene-animation` |
| T7 | archive README; every *live* reference fixed (skills, the flow-operator agent, CLAUDE.md, docs/README, the docs/flow, docs/google-flow, cinematography, marketing and shorts READMEs). Historical plans, specs, research, scene logs and code comments keep the old names on purpose |
| T8 | CLAUDE.md 407 → 212 lines: the skill paragraphs became one grouped map. Every "fact that saves the most time" was checked to exist in its skill or doc first |
| T9 | every path cited by a live skill exists, bar two harmless ones: `packages/suno-mcp` (described as future) and an old example clip in flow-automation that moved out with the media |

**20 skills live** (was 23): overview-board, new-scene, scene-beats, scene-images, scene-animation, scene-timeline,
lip-sync-dub, flow-automation, flow-prompt, suno-automation, suno-prompt, premiere-automation, story-craft,
shot-craft, video-fx, find-footage, new-story, new-idea, new-image, chief-of-staff.

## Log

- 2026-10-23: audit made (this file); rulings 1–3 asked.
- 2026-10-23: Kai ruled (follow the guidance, plus split new-scene into stage skills); T1–T9 done the same day.
