---
name: listen-only-when-asked
description: "2026-09-17 Kai: NEVER call the listen tool (Gemini listen_describe) unless Kai explicitly asks for a listen on that audio"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bac0f72a-b2b9-4ac0-95a5-ff2cbadd5647
  modified: 2026-09-17T16:35:39.076Z
---

Only run `mcp__listen__listen_describe` (or any Gemini listening pass) when Kai explicitly asks, e.g. *"could you please listen to this"*. Never run it on my own initiative: not after recording a take, not to find timestamps, and not to check a join.

**Why:** Kai, 2026-09-17, after I listened to every Suno take automatically (scene 2 Extend rounds r20/r21): *"the listening feature is very useful, but it's really important that we only listen when requested… I want to be much more careful about when we trigger the listening feature."*

**How to apply:**
- Record takes as usual (the recording itself is fine), then stop and report what was made.
- A listen isn't the only way to get timings. Offer ffmpeg measurements, which are local, or say the timestamps are owed and ask whether Kai wants a listen.
- When another session asks for timestamps, don't listen unprompted: tell it a listen needs Kai's say-so.

Related: [[claude-can-hear-initiative]], [[suno-playback-recording]], [[gpom-narration-scored]]
