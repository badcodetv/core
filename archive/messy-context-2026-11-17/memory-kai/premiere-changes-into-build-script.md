---
name: premiere-changes-into-build-script
description: "2026-11-11 Kai: Premiere-only changes must be written back into the scene's build script so no rebuild drops them; \"Premiere ahead\" must carry its reason"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 33a4fdac-9db2-4eb1-a4f9-b5fb47322a30
  modified: 2026-11-11T11:48:22.597Z
---

Kai, 11 Nov 2026 (GPOM): "it's not that we have to line things up for the sake of it… I don't want us, by mistake, to miss a change that we meant to keep."

**Why:** scene A's page rebuilt from cut3.py had quietly lost two of his Premiere-era decisions: the side and overhead angles, and his tinny song-tail radio. He only caught it by watching 00 RENDER story.

**How to apply:**
- When Kai's hand edit (or anything done only in Premiere) differs from the page, port it into the scene's build script (e.g. cut3.py) as the page's version too. Don't only note it.
- A round record that stays different on purpose carries `premiere_ahead` (the reason, in words). premiere-check.py then shows "Premiere ahead", not red.
- After any big rebuild, audit the sequences for shots past their file's end and for V1 gaps. premiere-plan.py now handles pre-trimmed files, which caused the bridge's 3 s of black.

Related: [[no-split-brain]], [[timeline-drives-premiere]], [[gpom-premiere-naming]].
