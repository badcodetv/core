---
name: camping-recut-initiative
description: "2026-07-25 recut of the LIVE camping v1 comic to 24 pages — built, reviewed page-by-page, and refined; uncommitted pending Kai's look"
metadata: 
  node_type: memory
  type: project
  originSessionId: efc1d01c-1efb-416c-ab81-d97091da67d0
  modified: 2026-07-27T15:16:37.772Z
---

2026-07-25: Recut of the **live camping v1 comic**, 53 pages → **24 pages** (23 slides + ATM stinger). Movements JUDGE 1–9 / SEE 10–14 / BECOME 15–24, bookended on the tent-door POV. Distinct from [[camping-karen-rework-initiative]] (camping-v2 rebuild, separate).

**Status: built, fully reviewed in browser, refined — NOT COMMITTED** (Kai to look; commits auto-push, see [[auto-push-on-commit]]).

Locked devices: two-parking-spaces mirror, "let's circle back" as the trip's exit line, the retreat delivering what it advertised, W-**AI**-trose (only A+I lit), Bob's name beat, "▸ STAY PUT / thank you for banking with us" stinger.

**Review pass changed three things beyond the plan — the reason to read the spec's §2b before trusting §3:**
1. **Cut spec-slide 12** (second near-identical yurt frame = scroll stall); its rifle thought moved onto slide 11 as beat 2 of 3. Everything after renumbered down one.
2. **Regenerated slides 2/3/4/7** as `i40`–`i43`: v1's city Tarquin was a visibly different, older man than the camp Tarquin, which breaks the story's central mirror. Flow will NOT reproduce a face (policy forbids likeness phrasing), so city-man ≠ camp-man still — that residual gap is parked on the multi-year collapse, where a changed face is motivated. The yurt (same weekend) was the indefensible one, hence the cut.
3. **Slide 7 traded vehicle continuity for face continuity** — every tent-beside-expensive-car prompt was policy-blocked. See [[flow-policy-blocks]].

**Other build lessons:** SpeechBubble default fontSize is 18; v1's `fontSize={10}` is unreadable — recut uses 14. `parsePanelRecord` was widened to accept all `**Prompt …:**` heading variants. Asset keys carry extensions (`img/i40.png`) — records/page-map/manifest must agree.

Sources of truth: `docs/camping/storyboard/index.md` (as-built map) and `docs/superpowers/specs/2026-07-25-camping-recut-plan.md` (§2b review outcome, §3 original plan, §9 policy lessons).

**2026-07-27 Tarquin-face incident, FIXED same day:** the 07-25 regenerated city panels i40–i43 (p02/03/04/07) were a *third* face — the `@Tarquin` Flow Character (camping-v2 project, id `29e97ae3-…`) was never cast: wrong project, MCP-only lane, policy-safe phrasing binding wardrobe not face. Fix: regenerated all four in the camping-v2 Flow project with `flow_generate_image({character: "Tarquin"})` (the MCP DOES support casting now — skill's stale caveat corrected + HARD RULE added to [[flow-mcp-and-art-direction-initiative]]'s badcode-art-direction skill). New keys `img/i44`–`i47`, records/index/page-map/manifest updated, bucket verified. Bonus: p07's tent is back beside the SUV — tent+luxury-car passes the usage filter once brand triggers (marque, plate, legible fascia) are stripped; the base gen still drew a legible ASDA, one edit pass removed the lettering (plain gable). Lessons: Flow Characters are project-scoped; a `flow_generate_image` FLOW_ERROR waiting for the "Upload media" dialog after a prior character-cast generation = stale page state → reload the project URL and retry. Bubble TUNE pass on p04 (and zoom focal on p07) may be needed after Kai's look.
