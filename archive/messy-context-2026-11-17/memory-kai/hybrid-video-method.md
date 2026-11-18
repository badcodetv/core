---
name: hybrid-video-method
description: "video lanes are LAYERS (2026-08-26 ruling) + 2026-08-27 amendment: camera-lock measured at 0-2px, but a hinge-able near field is a POST shot and wording/tier/duration are all non-levers"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 64a16109-6f7e-49f6-a47d-274a9605b3cb
  modified: 2026-08-26T18:44:25.572Z
---

**Ruled 2026-08-26 by Kai:** the video lanes are **layers, not alternatives**. On any shot where
the world moves *and* the camera moves — most of them — build all three:

- **Veo** animates the world with the camera **explicitly locked** (plate as `startImage`, motion
  only). Its regeneration bug is caused by camera *translation*, so locking the camera stops it
  firing. Still drifts 34–66px over 8s — stabilise or crop.
- **Premiere** moves the camera over the finished clip, on the `AE.ADBE Motion` intrinsic. Rigid by
  construction, any length, exact easing, free, instant to re-try.
- **ffmpeg** does what must be exact, procedural or headless — and it is the **only** lane that can
  put text on screen, because Premiere's API cannot write a string at all.

**8 seconds is never a reason to shorten a beat.** Chain: last frame of clip N → first frame of
clip N+1 (`flow_scene_save_frame position:"end"`, or `ffmpeg -sseof -0.05 … -frames:v 1`).
**Chain, never pin an `endImage`** — Frames-to-Video interpolates between two pictures and the
inconsistencies get animated away as sliding joins.

**Why:** we kept treating the lanes as a choice and so kept trading a living world against a moving
camera. Layering gets both, with neither tool asked for the thing it is bad at.

**🔴 AMENDED 2026-08-27 — proven on a whole scene, and one lane rule got sharper.**
GPOM cut 3 ran eight locked-camera plates. **Six held at 0–2px drift** (vs the 34–66px baseline) —
the lock sentence plus the rigid clause is a real, measured lever. The two that failed were the
only two with a **hinge-able surface in the near field** (rack doors, a louvre wall). On those,
**wording, tier (Fast vs Lite) and duration (4s vs 8s) are ALL non-levers** — a 4s request performs
the *same* move faster, which kills "chain in shorter segments" as a drift fix, and `vidstab` made
it worse. **A hinge-able near field means the shot is a locked plate + procedural life. Read
`docs/flow/video-prompting.md` §9 BEFORE the first roll** — it named this case in writing and
checking it after the fourth failed roll cost ~90 credits.

**Post can carry more than expected.** That scene shipped C0, B3 and B7 entirely from ffmpeg over
frozen plates, and B4/B5/B6 rescued in post (reversed tail, optical-flow retime, ping-pong).
🔑 **Moving grain is not optional on a locked plate** — without it the shot reads as a frozen JPEG.
🔑 **Reversal/ping-pong is only safe on light** (time-symmetric); never on settling matter.

**How to apply:** written up in `docs/video-fx/hybrid-method.md` (with the audited ffmpeg 4.4.2 /
frei0r surface and what ffmpeg does that Premiere cannot), and cross-linked from the `video-fx`,
`flow-automation`, `premiere-automation` and `shot-craft` skills, `docs/flow/post-production.md` §1,
`docs/cinematography/motion-and-cutting.md` §1, and CLAUDE.md.

Related: [[cinematography-initiative]], [[premiere-bridge-initiative]], [[flow-video-modes]],
[[clips-folder-convention]], [[gpom-clip-inventory]]
