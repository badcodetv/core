---
name: suno-four-box-atom
description: "Suno atom = style + exclude + lyrics (+ settings), changed together; My Taste RETIRED + Personalize ALWAYS OFF (Kai 2026-09-10); sliders are the only other level"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f80ca360-f993-437e-8c3d-b159c718af1e
  modified: 2026-09-10T09:27:35.992Z
---

**Amended 2026-09-10 by Kai:** *"we should stop trying to use the My Taste box and always have
personalize off when we generate a song, because then each song becomes an atomic unit."*
Also: running several Suno sessions at once is not important — don't optimise for it.

**A style is THREE boxes:** Style, Exclude styles, Lyrics (+ the settings). They **change together
or not at all** (original ruling 2026-08-27: *"if we're changing any of the prompts, we should
change all of the prompts… it's an atomic action"*). My Taste was the fourth box until 2026-09-10.

**Exactly two levels of change. Name which one before starting:**

| Level | Moves | Must NOT move |
|---|---|---|
| **Prompt round** | all three boxes, as one atom | — |
| **Slider round** | audio/style influence · weirdness · (v6) model · Variety · Max Mode | every prompt box |

**Never write a My Taste block; never set Personalize on.** `scripts/suno/suno.mts` forces
Personalize off, asserts it before every Create, refuses `personalize: true`, and no longer reads,
writes or ownership-checks My Taste. The freedom token (`MUST_REPLACE_HERE`) is retired.

**Why:** in our own logs My Taste only ever did harm (Karen voice leak, Camping bar-one strings,
GPOM newsreader under fourteen Camping rounds) and never provably improved a take; managing it
cost latency and blocked sessions. **Open, optional:** the "kazoo check" (absurd profile +
Personalize off) would confirm the premise that off really keeps the profile out.

Related: [[suno-v6]], [[suno-one-session-at-a-time]], [[suno-session-method]]
