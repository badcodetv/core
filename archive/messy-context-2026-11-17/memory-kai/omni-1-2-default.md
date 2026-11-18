---
name: omni-1-2-default
description: "2026-11-09 Kai: Omni 1.2 Flash is the Flow video model; Veo 3.1 Fast/Quality + Omni 1.1 leave Flow 5 Dec 2026"
metadata:
  node_type: memory
  type: project
  originSessionId: f96e60d4-a744-4baa-9e29-bfdd4ecc2d98
  modified: 2026-11-09T19:26:44.265Z
---

2026-11-09 Kai: Omni 1.2 Flash replaces Omni 1.1 Flash (and any Veo 3.1 Fast/Quality use) for Flow video. All active scene.json `video.model` values and the four story look.md files were switched the same day.

**Why:** Google retires Veo 3.1 Fast, Veo 3.1 Quality and Omni 1.1 Flash from Flow on 5 Dec 2026 (only Omni 1.2 + Veo 3.1 Lite stay). A 4-shot A/B came out 2 better / 2 ties / 0 worse, and Kai "can't tell any difference". Page: https://claude.ai/artifact/LAVzPiNXaC76hB1TGmgRaH; record: docs/google-flow/2026-11-09-omni-1-2-sweep.md.

**How to apply:** 1.2 costs ~2× 1.1 credits at 720p (360p is the cheap draft); it can insert a cut of its own, so ask for one continuous shot; length is a 3–15 s slider (flow-automation law 25). Still untested on 1.2: start+end frame, lip-sync by ear, cast characters, "Do not X" phrasing. Re-run tests with scripts/flow-tests/model-ab.mts. Related: [[flow-video-modes]], [[flow-video-credits-plentiful]].
