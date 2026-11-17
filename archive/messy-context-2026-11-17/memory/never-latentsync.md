---
name: never-latentsync
description: Jack 2026-11-16 — don't install or use LatentSync (the lip-sync-dub skill's "redraw" lane): "it does not work"
metadata:
  type: feedback
---

Jack, 2026-11-16 (True Scale, when asked whether to install it for lip sync): "dont install that lip syncing tool it does not work rememeber that please thanks".

Then: "you said you wanted to use the new tool for the lip syncing, do not do that, kai said that new one does not work. just use the skill we have been using for things like bank robbery story".

**Why:** Kai has judged it doesn't work for our clips (see [[latentsync-oom-kills-wsl]] for the earlier crash too).

**How to apply:** never offer or install LatentSync, even though the lip-sync-dub skill opens with it. Use the Bank Robbery method in that skill: re-shoot with the exact words, read mouth openings by eye from 12 fps mouth strips (mouth-track.py), place phrases with place-dub.py 0-0.1 s late, tempo 0.85-1.30. Never anchor on the clip's own audio or Whisper times (0.4 s early). For talking shots use the skill's other lanes: put the exact words in the Omni prompt so the mouth is drawn to them, size clips to the voice, fit the voice to the measured mouth; or keep the face off-screen/wide for that line. See [[dubbed-talking-clips-recipe]].
