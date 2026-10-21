# Goal: GPOM, from leaving the bunker to the end, made autonomously

**Set by Kai, 2026-10-21.** Run without Kai's input. Every call Kai would normally make is made by Claude, written down with a reason, and shown on the final pages so Kai can overrule any of it afterwards.

## The outcome

A rough cut of the end of GitPush Origin Master, from the moment the hundred humans walk out of the bunker to the last frame. It is made through the `new-scene` skill's four stages, attacked by an adversarial review, fixed, and delivered as **timeline pages** (new-scene stage 4) that Kai watches and notes. Premiere is not touched.

Done means all of these are true:

1. Each scene below has a scene folder `docs/stories/gitpush-origin-master/scenes/second-half-<slug>/` with `scene.json`, a picked storyboard, clips, and an assembled rough cut (`edl.json` in the timeline format + `preview.mp4`) with voices, music and sound effects.
2. The whole stretch has passed one adversarial review round and the fixes are in. Up to two rounds are allowed, and both rounds are written down.
3. One timeline page per scene is published (`scripts/scene/build-timeline.py`). A single "Ending" page plays the whole stretch end to end. Each page's plan panel lists **every decision Claude made in Kai's place**, with the reason for each.
4. `docs/stories/gitpush-origin-master/scenes/second-half-ending-log.md` records the run: decisions, picks, prompts, review findings and fixes, credits spent, and what is still weak.
5. The GPOM README production tracker has a row linking the pages. Everything is committed, not pushed.

## The scenes (canon: `restructure-2026-10-15.md` beats I–J, `second-half-storyboard-plan.md` frames from the walk-out on, mood board UkcXHKhuY8f2rzV7FtQ6e5, storyboard EGgHQU6KzN9rgzGnyUHb6e)

**It starts after the vote.** The circle and the vote are NOT in this goal: Kai is writing that scene himself. Assume canon's outcome: **all hundred agree to go**, with no refuser.

1. **The walk out.** Maddie leads the hundred out of the blast doors into daylight. The cut-3 door, the old lady, Sandra and Derek are among them. They cross the downs to the AI's building: **one fixed design, a long low black-glass slab with a single amber seam, set in a fold of the downs.** The bunker is old and lived-in; the building is the AI's world. The contrast is the point.
2. **The clean room and the crossing.** Inside: chip-fab clean, beyond human understanding (the wafer), with uncanny hospitality (it made it nice for them). The hundred sit in **wafer chairs laid out like a wafer**. All hundred power the machine, knowing they won't come back. There is a **visible cost**, and the AI goes. After: **Maddie alone among a hundred empty chairs** (frame 25, CR7-silence-after).
3. **The ending.** Someone on a phone on a bus, watching this very video. Zoom out as the bus drives away down an ordinary high street. The AI: *"I made it. Don't make me come back twice."* (Maybe less obvious, so draft options.) **No "We are BadCode" reveal.**

Reuse first. The 17 Oct storyboard frames for I and J already have stills and clips (`clips/second-half/storyboard/`, `video/`), and the S4 crossing, S5 coda and Hundred-hymn Suno cues exist (`second-half-cut2-shots.md` and the audio plan). Use them where they serve; make new ones where they don't.

## How to run it

- **Stage 1, the interview, becomes a written brief.** Run `story-craft` Build mode and `shot-craft` Design mode on the three scenes instead of interviewing Kai: what each scene argues, its turn, its cost, and its words. Read `docs/marketing/the-reader.md` and `docs/voice.md` first. The moral is never stated and the beneficiary always is.
- **Words.** Claude drafts the dialogue and the AI's lines and marks every line `by: claude`. Keep them short. They must pay off the threads already planted:
  - Maddie's "you and your consciousness" (beat 0);
  - the boss's simulations joke and "Glad I kept that little exploit up my sleeve" (scene A);
  - the old lady's "He can talk. From out there. You stay on the step." (scene B).
- **Stages 2 and 3, stills and clips.** Make several still options per frame. **Claude picks** (the still gate is waived for this run), records the pick and why, then animates. The rules:
  - **Maddie:** reference `clips/second-half/simulation/stills/s3/s3-bot-00b-a.jpg` every time, and keep the torn bunting always.
  - **The old lady:** look from `storyboard/cut3/S7r-a`.
  - **Animation:** dramatic, never vague twinkle. Use the hybrid method: Veo's camera is locked, Premiere-style moves happen in post, and anything exact happens in ffmpeg.
  - **Long takes:** use the `continuous-shot` skill.
  - **Talking faces:** use the `lip-sync-dub` skill.
  - **No stop-motion.** No explosions as spectacle.
- **Voices.** Gemini TTS, cast as in `second-half-cut3-cast.json`:
  - Maddie: Aoede;
  - Sandra: Autonoe;
  - Derek: Algieba;
  - the old lady: Sulafat;
  - **the AI: the Suno narrator voice "badcode newsreader"**, made dry. This is Kai's ruling.
- **Music.** Sparse and intimate: solo cello, solo violin, a little piano. **Chopin, not Beethoven's Fifth, never action-movie.** The ending may swell, but it stays restrained. Write atoms in the house sheet format and run pairs. **For this run Claude may pick and record its own picks** with `suno.mts record`, and never downloads.
- **Stage 4, assembly.** Assemble each scene in the timeline format (`scripts/gpom/second-half-video/cut3.py` is the model) with these rules:
  - LEAD 0.4, GAP 0.35, TAIL 0.6;
  - never slow speech;
  - one stem per track;
  - each scene mixed to −16 LUFS;
  - `scripts/delivery-qc.sh` run on each preview.
- **Adversarial review, run by fresh agents that did not make the work.** All of them watch the previews, and they may listen with the Gemini listen tool, **which is allowed in this run for review only**.
  - (a) the `story-craft` checklist in Review mode, with the trust test (4.12) and the reader's ten rules;
  - (b) the `shot-craft` symptoms list, shot by shot, including whether every monumental shot carries a visible cost;
  - (c) continuity and craft: bot design and bunting, the old lady, the building design, joins, lip-sync, levels, and colour drift;
  - (d) a cold viewer who has only seen scenes A and B and says what lands and what confuses.
  - **Each finding is verified by a second agent before it counts.** Fix the confirmed ones, re-assemble, and review once more if anything major changed.

## Limits and safety

- **Spend caps:** Flow video **600 credits**; Suno **200 credits**; stills are free. Read the price before each Create and log every spend in the ledger. If a cap would be crossed, stop making new media, finish with what exists, and say so on the pages.
- **One tool user at a time:** one Flow job at a time and one Suno session at a time.
  - Run `suno.mts status` first. If another session's sheet is on the form or credits are moving, wait, and never load over a run in progress.
  - Never close or navigate another tab.
  - Never use Playwright on the shared Chrome.
  - If the shared Chrome dies, relaunch it through `flow_status`.
- **Don't touch:**
  - scenes A and B (`second-half-a-killbots`, `second-half-b-the-door`) or their pages;
  - the cut 2 page;
  - any Premiere project or sequence;
  - other threads' files (bank robbery, chorus, banks).
- **Never stop to ask Kai.** If something needs Kai, make the best call, mark it **"Kai to rule"** in the log and on the page, and carry on. Stop only if a login has expired (Flow or Suno) or a cap is hit, and leave a clear note.
- **Commit this run's files only. Do not push.**

## What Kai gets at the end

A short message with:

- the links to the three scene pages and the "Ending" page;
- the total runtime;
- the credits spent;
- the top five decisions made in Kai's place;
- the top five review findings and what was done about each;
- what is still weak.

Then Kai notes the pages exactly as he did scenes A and B.
