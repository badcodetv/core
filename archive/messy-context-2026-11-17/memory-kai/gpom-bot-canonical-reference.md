---
name: gpom-bot-canonical-reference
description: The GPOM West Country delivery bot has ONE look — reference clips/simulation/stills/s3/s3-bot-00b-a.jpg on every shot; torn bunting always stays (Kai 2026-10-17) — EXCEPT the gleaming clean Maddie from ending scene D's clean room on: NO bunting (Kai 2026-10-23)
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5e62512e-e849-42fd-8b20-dc2bf04b897e
  modified: 2026-10-17T16:17:09.046Z
---

Every GPOM shot with the delivery bot passes `clips/simulation/stills/s3/s3-bot-00b-a.jpg` as a `flow_edit_image` reference (it is the bot in Kai's edit: dented boxy grey body, six chunky black wheels, amber beacon on a short stalk). **Keep the torn faded bunting on its wheel** in every prompt — Kai, 17 Oct 2026: *"a little detail that really resonates with me."*

**Why:** Kai saw the bot change design between storyboard frames (meeting stills had a different robot) and asked for a Flow Character to fix it. Flow's Character tools are unmapped on the rebuilt Flow (`flow_list_characters` → FLOW_REBUILD_UNMAPPED), so a reference image is the working substitute; "swap only the robot, keep everything else" edits worked first time on 6 frames.

**UPDATE 2026-10-17 (same day): Flow Characters are re-mapped and live in GPOM project `0558b1d5` ("Oct 15 - 14:42"): `West Country Bot` (portrait + body + info), `Kill Bot` (P1-patrol design), `Cream Jumper Woman` (portrait + body), `Green Jumper Man` (portrait only; Flow refused his body crop). Cast with `character: "West Country Bot"` on flow_generate_image / flow_edit_image (a reference image + the Character works). Prefer the Character over the reference-image trick now. **Cast in the fresh project `be451638` ("Oct 17 - 18:57", West Country Bot re-created there)**: the old one is ~200 images deep and returned old media as new (rebuild doc item 74). Debris: one `Untitled character` (the first failed attempt) is still in the project.

**How to apply:** same trick for any recurring object — the time machine's chair layout is locked to `moodboard/L3-wafer-pattern.jpg` (dark recliners in pools of light, square grid in a thin ring, cables to a round hub). Related: [[gpom-second-half-2026-10-16]], [[flow-moved-to-flow-google-com]].

**EXCEPTION 2026-10-23 (Kai):** from the clean room in ending scene D onward, Maddie is gleaming clean like the humans in their clean suits, with **no bunting at all** (not washed, not new). Before that point the torn bunting rule stands.
