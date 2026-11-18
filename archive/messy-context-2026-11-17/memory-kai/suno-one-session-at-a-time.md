---
name: suno-one-session-at-a-time
description: Suno cannot be driven by two sessions at once — one create form and one account-wide My Taste box; browser channels do NOT fix this
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2980223a-bbd7-4a03-b367-5b046fd921a9
  modified: 2026-08-27T10:03:16.748Z
---

**Proven 2026-08-27.** Browser channels make **Flow** safely concurrent. They do **not** make
Suno concurrent, because both blockers are **account-level**, not tab-level:

1. **ONE create form.** A single shared surface. A second session's `load` **wipes** what the
   first was holding, with **no draft recovery**.
2. **ONE My Taste box.** Account-wide, cannot be turned off, invisible from the create page,
   applies to every generation regardless of channel.

**How to spot another session before you break it:** run `status` first. If the form holds a
title/workspace belonging to another sheet, **stop and ask**. A **credit balance that drops
mid-session** is the other tell (it dropped 30 during a `load`, which spends nothing).

**Direction of the 2026-08-27 collision:** the GPOM narration session loaded over a Camping
cover form (`camping-duet`, take c3). Record the title, workspace, `styleLen`, `excludeLen`
and sliders from `status` **before** loading, so the other session can rebuild.

🔑 **The My Taste pollution ran GPOM → Camping, not the reverse**, and it predates this
collision: the box held the **GPOM newsreader profile** through all fourteen Camping cover
rounds (found and documented 2026-08-26 in `docs/stories/camping/songs/camping-style.md` §1).
Camping's findings of the form *"genre X didn't work"* are unsafe; the accepted round-17 take
is **fine** because it was chosen by ear.

**Not Kai's fault to carry:** the tooling let two sessions reach one account with no lock. The
fix is procedural (`status` first) until something better exists.

Related: [[dry-and-separate-narration]], [[suno-session-method]], [[concurrent-browser-sessions]],
[[camping-duet-recut]], [[suno-voice-playbook]]
