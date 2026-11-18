---
name: gpom-second-half-clips
description: 2026-10-17 GPOM second half — 26 Omni clips + 10 ffmpeg post clips, Premiere sequence gpom-second-half, cutting-room board, sound script (War of the Worlds shape); Kai's imagery pass owed
metadata:
  type: project
---
2026-10-17 (committed same day): every storyboard frame (board EGgHQU6KzN9rgzGnyUHb6e) has a clip in clips/second-half/video/ — Flow via scripts/gpom/second-half-video/run.mts, post-only frames via post.py. Cutting-room board https://claude.ai/artifact/LyD3odnVmN5rrdo9m1TpZp (db `picks`). Premiere: sequence `gpom-second-half` (1080p24, 31 shots, 134.5s, bin 07-second-half) from edl.py.

Sound script https://claude.ai/artifact/FH9mz25HGZWCfQzMaDqubx, built from scenes/second-half-audio-plan.json — the ONE source for the second half's words/effects/music. **Kai 17 Oct: Jeff Wayne's War of the Worlds approach** — opens as the D&B track, becomes a narrated story at the robot (scene 4), score continuous after; **Gemini for every voice** (Kai: best for voices), Suno for music. Two themes: MACHINE (the D&B riff) and HUNDRED (brass-band hymn). All lines are Claude drafts awaiting Kai.

**Why:** follows [[gpom-second-half-2026-10-16]]; bot rule [[gpom-bot-canonical-reference]]; the D&B-opens structure is [[gpom-music-video-fusion]].

**Rough cut (17 Oct, later):** `gpom-second-half-rough` (3:10.9) with Gemini voices + 5 Suno cues, built by voice.py → timing.py → extend.py → rough_audio.py → rough_place.py; render in renders/. Kai asked for this as a repeatable loop: he gives feedback on the sound-script page, the pipeline re-runs. Music takes chosen by length, not heard.

**How to apply:** next is Kai's imagery pass (AI artefacts, still-only frames needing more, a couple of extra videos), then voicing from his final words. Frame 15 re-stages the bot on every take. Character casts into Frames-mode video work only by `@` mention (rebuild doc items 75–77). Flow refuses SBEMERa uploads.

**Cut 2, part 1 (19 Oct):** Kai's notes on the script page NdLzmEwrxXN7SrYeP9h6xx (db `script`) → `cut2` block in second-half-audio-plan.json (beats 0–18: Maddie opens on the high street, no narration in the hunt, no D&B drop, beats 5+16 cut, new 11b/13/14a/14b, old lady + Maddie corridor, the circle). Plan + silent animatic page Amb2o9BZ5MDVSwZ6zXA5zb (db `plan`). Kai paused at 19 ("the next whole scene"). **Kai waived the still-approval gate for the new shots N1–N4: "trust you to cut the shots… then just animate them"** — he wants to taste a cut fast, then iterate.

**Cut 2 part 1 BUILT (20 Oct, commit d457dd7, unpushed):** Premiere sequence `gpom-second-half-rough2` (36 clips V1, 26 stem tracks), render renders/gpom-second-half-rough2.mp4 (4:06.6) + `-qc.mp4` (range-converted; note `scale=in_range=full` is a no-op on an UNTAGGED input — needs `setparams=range=pc` first). Casting for rough: Sandra=Autonoe, Derek=Fenrir, old lady=Gacrux. Music picks S1b 9222bb47, S2b 647f6507. Pipeline: `--cut2` flags + cut2.py. Kai hasn't watched yet; plan page not refreshed with real durations.

**20 Oct cut 3 BUILT (from Kai's cut 2 timeline notes):** two scenes, A kill bots (2:35) timeline Jjvd8FPvF4KJUnVDQLYzkQ, B Maddie at the door (1:25) timeline Vz218v2P2kNKhDxQH2U2f8; cut ends at the door, circle/vote deferred to next scene. Cast: Sandra Lancashire/Autonoe, Derek Liverpool/Algieba, old lady RP/Sulafat (scenes/second-half-cut3-cast.json). Video 416 credits (Flow balance said Jack's account). Assembler scripts/gpom/second-half-video/cut3.py A|B. Not in Premiere.

**2026-10-22 autonomous ending run (walk-out → end, after Kai's unwritten vote scene):** scenes C walk out / D crossing / E ending + reel; pages Ending R3zv1wejHA1pU7CSz39bta, C Txcv2zYfVUNBEg1tdrcyah, D 5DmzsvMV27dg9GWgoKEL2g, E Cos8GdsUgpzhZefdxiwoM4. Log = scenes/second-half-ending-log.md ("Kai to rule" items). Flow 684, Suno 190. Open: last line changed to "I made it. They didn't." (Kai's canon line held in Suno take 32047e7e); D03 AI line is a TTS stand-in (Suno recording stalled on WSLg PulseAudio lag).
