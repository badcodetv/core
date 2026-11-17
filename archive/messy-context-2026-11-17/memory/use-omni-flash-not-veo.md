---
name: use-omni-flash-not-veo
description: Standing preference — generate all Flow video on Omni Flash, not Veo 3.1.
metadata:
  type: feedback
---

Always use **Omni Flash** for video generation in Google Flow. Jack judges it clearly
better than Veo 3.1 on our footage.

**Why:** stated as a standing preference on 2026-08-25, from watching the actual
output across the camping shots. It overrides the repo's earlier
`Veo 3.1 Fast` default in `docs/flow/video-prompting.md`, which was ruled from a
bounded n=3 A/B on one plate and one near-static prompt.

**How to apply:** default to Omni Flash without asking. Two known limits worth
raising *at the time* rather than switching silently — Omni Flash **rejects a last
frame**, so the first+last-frame interpolation lock is Veo-only; and on 2026-08-25
Omni Flash on Frames lost both faces on a big expression arc where Veo held them
(see [[always-new-prompt-never-edit-an-image]] and the tab-rule bound in
`docs/google-flow/omni-flash.md`).
