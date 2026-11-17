---
name: flow-unusual-activity-refresh-retry
description: "On Flow's \"unusual activity\" failure OR when the start-frame slot doesn't fill, refresh the page and retry ~10s later; no long back-off, no pause between clips."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 21b57ced-98b2-4c2d-b887-960b50a16bec
  modified: 2026-09-28T14:57:01.202Z
---

**Every Flow retry starts with a real page refresh.** It applies in two cases:
- the **"We noticed some unusual activity"** failure card
- the **start-frame slot not filling** (`FRAME_SLOT_NOT_FILLED`)

Refresh, wait about **10 seconds**, retry. Don't back off for minutes, and don't pad the gap between clips.

**Why:** Jack, 2026-09-28, during the Camping mv2 26-clip Omni run:
- *"just needs a refresh and retry. Drop the long back-off … and cut the pause between clips."*
- then, *"remember to refresh the page when you retry, as well as when … the start-frame slot didn't fill."*

The card says "You have not been charged", so a retry is free. The old advice ("wait a couple of minutes") was too slow. Jack asked for a real refresh (`page.reload()`), not just navigating to the project URL again.

**How to apply:**
- In any automated Flow loop: refresh, then retry in ~10s, for a handful of tries.
- If one clip keeps failing, defer it to the end rather than stopping the run.
- Upload each plate once per project, then reuse it; re-uploading on every retry piles up duplicates.
- The rule is also in `.claude/skills/flow-automation/SKILL.md` §3.

Related: [[flow-hand-driven-not-automated]].

**Fast detect (Jack 2026-11-09, "please remember that trick and save it"):** the image tools (`flow_generate_image`,
`flow_edit_image`) never read the "unusual activity" card, so each one sat out a 90 s TIMEOUT (half the tries on the
Paraguay presenter run). Trick: count "unusual activity" in `document.body.innerText` before submitting, poll every 2 s
while the generation runs, and the moment the count goes up, abandon it → real reload → 10 s → retry the SAME prompt
straight away (not deferred to the end). Seconds lost instead of ~2 min. Worked example:
`docs/stories/magic-money-tree/scenes/paraguay-presenter/cleanroom/r2/run_stills.mts`. Also: a real reload before
EVERY prompt kept most tries clean. The proper fix is to wire `detectFailureCard()` into the image wait loop in
flow-client.ts (failure-card.ts already classifies the card as `refused`); not done yet.
