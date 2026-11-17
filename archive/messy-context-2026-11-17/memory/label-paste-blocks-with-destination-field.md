---
name: label-paste-blocks-with-destination-field
description: Every paste block handed to Jack must be headed with the exact UI field it goes into.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8bc935b0-60c0-4add-a19e-3427589cb9cb
  modified: 2026-09-15T14:03:37.784Z
---

Never hand over a bare copy-paste block. Head each one with its destination field —
`→ VOICE DIRECTION`, `→ SCENE`, `→ TRANSCRIPT`, `→ STYLE BOX`, `→ EXCLUDE STYLES` — naming the
exact box in the exact tool.

**Why:** Jack asked for this on 2026-09-04 after several rounds of Google AI Studio blocks where
the field was described in prose above rather than stamped on the block, and content landed in the
wrong box (the persona brief went into Sample Context instead of Voice Direction, which
under-steered the read). Multi-box tools — AI Studio's Composer, Suno's four boxes, ElevenLabs —
all make this failure cheap to cause and expensive to debug.

**Settings and attachments sit directly on top of the destination label** (Jack, 2026-09-15):
every Flow prompt is headed, in this order, immediately above its fence, with nothing between:

```
**Settings:** Nano Banana Pro · landscape toggle · x2
**Attach:** `@Bob`, then the accepted fog two-shot
**→ Flow image surface · prompt box**
```

Never only in the commentary higher up, and never inside the prompt. He was scrolling back through
the rationale to find them every time.

**How to apply:** one block per field, heading first, in the order they are filled in. If a block
has no field, say where it goes anyway. Commentary still goes ABOVE the block, never after it —
see [[paste-blocks-never-followed-by-prose]]. The AI Studio field map lives in
`docs/ai-studio/README.md`.
