---
name: mark-unverified-claims-as-unverified
description: Never write an inference as a finding — label anything not directly sourced as unverified.
metadata:
  type: feedback
---

State only what a source actually says. When something is an inference, a search
summary, or a guess, **say so in the same sentence**. Never let it enter a repo
doc as a bare fact.

**Why:** on 2026-09-03 I wrote "Multilingual v2 does not read audio tags — it
speaks them" into camping's narration sheet as a finding. It came from a search
summary hedged with *"would likely"*, and Jack's own Karen result contradicted it.
He had already asked twice for proper research; the cost of a wrong confident
claim is that he stops trusting the correct ones. Related: [[repo-records-intent-flow-holds-assets]].

**How to apply:** three tiers in docs — ✅ quoted from a named source, ⚠️ inferred
and untested, ❌ unknown. Before asserting a platform behaviour, ask whether a
**free** check exists (a History tab, an existing artefact, a UI label) and use it
before spending anything. And when the user reports what they observed, that
outranks an undocumented inference.
