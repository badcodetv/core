---
name: cinematography-initiative
description: 2026-08-26 shot-craft skill + docs/cinematography/ from a 20-brief sweep; the visible-cost gate; the house-register question is OPEN and owed a Kai ruling
metadata:
  type: project
---

2026-08-26: BadCode had deep **platform** knowledge (what Veo/Nano Banana obey, `docs/flow/`)
and deep **story** knowledge (`docs/story-craft/`) but **zero cinematography judgement** — a
grep found 0 hits for rule of thirds, leading lines, 180-degree rule, screen direction, colour
script, contrast ratio across all of `docs/`. Kai spotted it as "visually it's not very
exciting what we've got."

**Built:** a 20-brief parallel sweep (14 + 6 gap-closers) with two adversarial critic passes in
`design/research/2026-08-26-cinematography/`, distilled into `docs/cinematography/` and driven
by the **`shot-craft`** skill. Tool-agnostic by design so it outlives Flow. 141 web searches,
zero AI-prompt-vocabulary leaks.

**The pipeline it completes:** `shot-craft` (what the shot IS) → `flow-prompt` (how to phrase
it) → `flow-automation` (drive the browser). The design stage never existed before, which is
why shots came out correct but inert.

**Three findings that change work:**
- **Darkness reads as depth only when one small region inside it is deliberately brighter.**
  Uniform near-black reads as a broken file, not mood. Mechanism: lightness anchoring
  (Gilchrist). This is our register's central problem and its one-sentence fix.
- **🔴 The visible-cost gate.** Every monumental shot must show wreckage, exhaustion, a body
  that failed. Without one, scale-and-symmetry reads as *celebration* of power — and doing it
  ironically does not protect you (Verhoeven on *Starship Troopers*, Harron on *American
  Psycho*). Independently arrives at the picture version of the-reader.md's ruled rule: never
  raise a fear without naming the beneficiary. See [[target-reader-pivot]].
- **A scene is a small argument; every shot is a step in it or it is decoration.**

**🔴 OPEN RULING (R1) — Kai owes a decision.** The corpus argues against our own near-black
monumental register two ways: it is the visual opposite of British social realism (the grammar
closest to our working-class UK reader), and it carries a documented aspirational-misreading
risk. **Neither brief proves the house look wrong; nobody has evidence either register works on
this reader.** Recommended next step (brief 17's own): run the visible-cost checklist against
3–4 shipped GPOM / Magic Money Tree panels — converts an unanswerable debate into evidence.
Until ruled: keep the register, apply the gate, never call it settled in canon or public copy.

**Also done:** retired the four dead `scene-prompt` references (a skill referenced everywhere
and never built) onto `flow-prompt` + `shot-craft`; near-black delivery findings added to
`docs/video-fx/delivery.md` with 5 additions owed to `scripts/delivery-qc.sh` (not yet
implemented).

**Method note:** wave one's critic caught systemic grade-laundering — building **P** grades
from three content-mill sites agreeing. `docs/cinematography/evidence.md` is the authority
over the briefs; several grades were lowered in distillation. Related: [[story-craft-initiative]],
[[websearch-budget-per-session]].
