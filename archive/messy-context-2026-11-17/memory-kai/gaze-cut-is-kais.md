---
name: gaze-cut-is-kais
description: gpom-the-gaze-cut-46 is hand-cut by Kai from 2026-09-21 — never rebuild it from script
metadata: 
  node_type: memory
  type: project
  originSessionId: 51d4ef89-2954-493c-a451-06a45733605e
  modified: 2026-09-21T14:18:17.743Z
---

**2026-09-21:** GPOM scene 2 ("the gaze") has all 49 clips rendered and laid down in cut order in
the Premiere sequence `gpom-the-gaze-cut-46`. From this point **Kai cuts it by hand against the
narration.** Never re-create, re-order or re-time that sequence unless he asks in words. New clips
go to the end of the timeline or into a separate sequence for him to place.

**Why:** every tool that built it (`scripts/gaze-board/motion.py`, `run_videos.mts`,
`match_clips.py`) rebuilds the sequence from scratch. Running any of them over the top silently
destroys his edit, and there is no undo once the project is saved. Premiere now holds the running
order of record, not the script — `motion.py`'s numbering deliberately no longer matches (the
three "spoils" shots are 47–49 but belong at 3–5), because renumbering renames the clip files and
Premiere holds them by path, which would take the whole sequence offline.

**How to apply:** if asked to change the gaze cut, edit clips or add media additively and let Kai
place them; only rebuild if he says so explicitly. Project shape is one sequence per scene
(`gpom-s01`, `gpom-the-gaze-cut-46`), later nested into a master.

Related: [[gpom-the-gaze-sequence]], [[premiere-import-clips-individually]],
[[still-approval-gate]].

**2026-10-26 update:** Kai retired gpom-the-gaze-cut-46 from the film ("it can go"). It now sits in the `_not-in-film` bin, not deleted. See [[timeline-drives-premiere]].
