---
name: gpom-opening-zoom-locked
description: 2026-09-17 GPOM s01→s02 space-to-terminal zoom LOCKED by Kai in gpom-s01 + the Flow/Premiere gotchas that cost time building it
metadata: 
  node_type: memory
  type: project
  originSessionId: 51d4ef89-2954-493c-a451-06a45733605e
  modified: 2026-09-17T17:19:20.501Z
---

2026-09-17 Kai: "we've nailed it, such a good opening scene". Picture locked in gpom-s01 (gpom-story.prproj):
EARTH-b7-orbit2 48–56 → flyover over the satellite toward Earth (sequence/bridge/0e-orbit2-flyover-b, first 3s, on V2) 56–59 → bay drop 59–62 → Blue Hour glide (2-glide-v2-b) 62–68.1 → HK-b3-pushin 68.1–75.7 → HK-b4-terminal 75.7–84.0, Enter 81.67. Narration = one combined Suno take c12 544fe82f on A4 from 0 (a 125 kbps recording, so swap in the real download); Kai times it by hand. Kai rejected: cold office still, the push-through-glass shot, continuing the *bridge* instead of orbit2 itself, and an orbit continuation that merely coasts — the extension has to MOVE (fly over the satellite toward Earth). The "git push origin master" on-screen text is still owed (ffmpeg lane). 2026-09-18 Kai: scene 1 DONE. Next: scene 2, with example images being cut in another thread.

**Why:** Kai re-cuts live in Premiere while I work, so refs and timings shift under me.
**How to apply:**
- Re-read the sequence before every edit. Never assume my last state.
- Overwrite-inserting an 8s clip into a smaller gap eats the next clip. Place it on V2 or trim first.
- 720p Flow clips need Motion Scale 150 in the 1080 sequence.
- Veo clips bring audio onto A1; delete it.
- A fresh Flow project can throw VIDEO_OPTION_UNAVAILABLE (Frames): click the Frames radio by hand, then retry.
- If a download fails with saveAs ENOENT, recover the clips from the flow-video-tile video src. Never re-roll.
- Related: [[hybrid-video-method]], [[flow-moved-to-flow-google-com]], [[gpom-narration-scored]]

**2026-10-26 update:** gpom-s01 was renamed gpom-1-track-and-off-switch (4:40). Its end runs straight into gpom-2-A-killbots-r1. See [[timeline-drives-premiere]].
