# Handoff: scene B, the bridge (Maddie at the door), 4 Nov 2026

From the maddie-at-door session to badcode-b6, which now owns GPOM and Premiere.

## Where it stands

- **Scene:** `docs/stories/gitpush-origin-master/scenes/second-half-b-the-door/` (draft 1G, "the bridge"). It runs from the end of A (the kill bots stand down) to the card "The next day.", then C.
- **Current round:** round 8, 1:28 (87.65 s), 17 shots.
  - Media: `D:\badcode-videos\gitpush-origin-master\clips\second-half\cut3\B-bridge-r8\` (`edl.json`, `preview.mp4`, `stems/`, `split/`, `video/`).
- **Timeline page:** https://claude.ai/artifact/4uBRnD5yJaUxYjRXaWBcK1 (v10).
  - Built by `python3 scripts/scene/build-timeline.py docs/stories/gitpush-origin-master/scenes/second-half-b-the-door <out-dir>`, then published with every file in `<out-dir>/media/`.
  - The out-dir was this session's scratchpad (`.../scratchpad/bridge-timeline`), so pick a new one. Republishing to the same URL keeps the notes.
- **Rebuild the cut:** `python3 scripts/gpom/second-half-video/cut-bridge.py --round 8`. Rounds 3 to 8 all go through `main3()`, and the round's changes are guarded by `ROUND3 >= N`.
- **Kai on round 7 (4 Nov):** "there's one note about voice syncing, but apart from that, we're there."
  - Round 8 answers that note: Sandra's first sentence is one fresh take fitted to her mouth (`voices-sandra-fit.json`, take c).
  - **Kai has not yet confirmed round 8.**

## Premiere

- **No bridge sequence exists yet.** Kai never said "build it". Hold until he does.
- **Name for the first build:** "04 GPOM story B bridge r1" (Kai's story-order names, relayed by gpom-second-half).
  - It goes into "00 RENDER story" right after A, and every later clip moves along by B's length (87.65 s).
- **Building it:** `scripts/scene/premiere-plan.py <edl> <plan> --tag r1 --seq "04 GPOM story B bridge r1"`.
  - Then follow the scene-timeline skill's "Building a sequence" steps.
  - Write the record into `scene.json` → `premiere`.
- **The old doorstep sequences** (gpom-3-B-door-r*) are in "zz old sequences". Leave them alone.
- **The Premiere MCP (port 7890, node pid 858303) is not mine.** Its parent is pid 7239, which is gpom-second-half. This session never connected to Premiere.

## Notes

- **Every note on the page is answered** (40 notes over rounds 1 to 7). Replies live in `cut-notes.json` (`replies`, and `replies_roundN` snapshots).
- **Feedback dumps:** `feedback/bridge-timeline-r2` … `bridge-timeline-r7`, `bridge-picks-r6`. The plain `timeline-rN` folders belong to the old door scene.
- **No notes are read but unanswered, and no fixes are half-built.**

## Picks

- **Round 6 picks are all done and in the cut** (`feedback/bridge-picks-r6`):
  - Maddie's aside: reading 2, "catch".
  - Hum: b.
  - Old lady still: a (`LADY6`).
  - Sandra still: c (`SANDRA6`).
- **Picks page:** https://claude.ai/artifact/Li9PdKYRWKuuGVsVJ9cD9S (spec in `bridge-r6-picks.json`).

## Decisions owed by Kai

1. **Is round 8 the one?** If yes: run `prov.py freeze <scene> --note "<his words>"`, build Premiere, mark the board row done, and commit when he asks.
2. **Re-voice the old lady's one line in scene D** in her new voice (Vindemiatrix, `voice-bridge.py` `LADY_AUDITION[1]` + `lady_profile`)? It's still in the old posh voice. Asked, but no answer yet.
3. **Small "keep or re-roll" calls I recommended keeping.** Kai never objected.
   - **br14, the boom clip:** the horn drops further and a second bulb appears.
   - **br20, the crowd shot:** the horn swings back up at about 2 s, so the cut uses its first 1.8 s forward then back (striped "looped" on V1). Re-roll = 1 credit.

## Stand-ins still in the cut

- **Shots carried over from the old door scene:**
  - The tannoy and door shots: `cut2-N3` (inside, looking up at the horn), `cut3-V5` and its push (Maddie at the shut doors).
  - The old lady's first shout: `br13` (LADY0).
  - Kai has noted the sync on these, not the shots themselves, so they're fine as far as anyone knows.
- **The red vault glow is baked into several room shots.** Never raised by Kai.

## Spend this session (4 Nov)

- **Video credits:**
  - Round 3: 2.
  - Round 6: 5 (br16 to br19, plus one re-run after a late tile mislabelled br16).
  - Round 7: 1 (br20).
- **Voices:** Gemini TTS only (aside ×10, hum ×3, Sandra fit ×6, and singles).

## Gotchas found

- **Late tiles:** a Flow late tile handed back br17's first submission as br16.
  - Renamed to `shb-br17-lady2c-LADY6-alt.mp4`, which is the take used for the vote. Its hum slot is 0.9–2.4 s.
  - Transcribe every harvested talking clip before using it.
- **Omni mouths:** Omni often holds one long open mouth shape on a short word. Fit the TTS to the clip (direct the rhythm, score by word starts) rather than cutting the voice into pieces. Written into `.claude/skills/lip-sync-dub/SKILL.md`.
- **Board publishes:** two sessions republished the overview board within minutes of each other. Always rebuild from `timelines.json`, check the other session's rows survived, then publish.

## Uncommitted files that are mine

Not committed: this session only commits when Kai asks.

- `docs/stories/gitpush-origin-master/scenes/second-half-b-the-door/`: `cut-notes.json`, `scene.json`, `trail.json`, `video-jobs.json`, `voices-sandra-fit.json`, `feedback/bridge-timeline-r6/`, `feedback/bridge-timeline-r7/`
- `scripts/gpom/second-half-video/cut-bridge.py`, `scripts/gpom/second-half-video/voice-sandra-fit.py`
- `.claude/skills/lip-sync-dub/SKILL.md` (two new table rows)
- `docs/provenance/cards/...` for `cut3/B-bridge-r6`, `r7`, `r8`, `audio/voice3/sandra-fit/`, and `_elsewhere/.../sandra-fit/`
- `docs/stories/gitpush-origin-master/timelines.json`: the b-door row only. Other sessions changed other rows; the file is shared.
- `docs/stories/gitpush-origin-master/timelines/index.html`: rebuilt from `timelines.json`, so it's shared too.
- This handoff file.

Not mine (left alone): `scenes/mv-ending/`, `scenes/second-half-a-killbots/`, `scenes/second-half-c-walk-out/`, `scenes/second-half-d-crossing/`, `scenes/second-half-e-ending/`, `scripts/gpom/second-half-video/ending/cut_end.py`.

## Flow

- This session used **channel 3 (port 9224)** and its own project `134ba9dc-1bc0-40b3-a2b7-75053e2c311a`.
- No Flow job is running.
