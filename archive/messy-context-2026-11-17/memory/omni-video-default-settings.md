---
name: omni-video-default-settings
description: Omni Flash video defaults — 720p x2 8s, an 8s prompt carries two beats, never suggest a 360p draft.
metadata:
  type: feedback
---

**Default Flow video settings: Omni Flash · 720p · x2 · 16:9 · 8s.** **Never suggest a 360p draft.**

**Why:**
- 360p: Jack, 2026-09-15: *"these always come out awfully."* A fresh 720p generation is a new take
  (no seed), so a draft can't predict it.
- 8s: Jack, same day, overruling a shorter default: *"the video being longer is helpful, so that when
  the narration goes over the clip's length, we have more video to put there as filler."*

**How to apply:** Omni pads one action stretched over 8s with drift, so **write every 8s prompt with two
beats**: the action the shot is for, then one small later beat (a gaze moving, a weight shift). Upscale to
1080p (free) only for delivery, and never pay for 4K. Settings go on the Settings line above the prompt
([[label-paste-blocks-with-destination-field]]). Ruling: `docs/google-flow/omni-flash.md` → *Default
settings*. Related: [[use-omni-flash-not-veo]].
