---
name: verify-a-cut-against-the-script
description: Before telling Jack a cut is built, transcribe the render and compare it to the script line by line; never trim speech on an LLM's timestamps
metadata:
  type: feedback
---

Jack, 2026-10-10, on the first Money For Something topical cut: "there are a lot of lines missing, please listen and watch it then compare it to the script". Seven of 27 lines had lost their endings, and I had reported the cut as built.

**Why:** I trimmed each clip at the time Gemini said the last word ended. Those times were out by up to three seconds wherever a line had a pause, and I never compared the finished cut with the script. The crowd-noise check I did run could not see it.

**How to apply:** for any cut with spoken lines, transcribe the finished render and diff it against the script before reporting (for this show: `scripts/money-for-something/topical-verify.py`). Take word timings from a local speech model with word timestamps (`topical-words.py`, faster-whisper in `~/.cache/badcode-whisper/venv`), and cut tight only where it heard every scripted word; otherwise keep the clip long. Join clips by re-encoding, not stream copy (the copy join left broken audio timestamps). My reading: this holds for every film with dialogue, not only this show. See [[mmt-topical-show-october]], [[mark-unverified-claims-as-unverified]].
