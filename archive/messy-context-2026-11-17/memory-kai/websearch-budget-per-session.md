---
name: websearch-budget-per-session
description: WebSearch has a per-session cap (~200 searches); a 20-agent parallel research workflow exhausts it in ~30 min and later agents get zero searches — cap per agent, stagger, or split sessions
metadata:
  type: feedback
---

Observed 2026-08-22 during the story-craft sweep: WebSearch reported "budget exhausted (200/200)"
partway through a 20-agent Sonnet research workflow. Briefs launched later in the batch got no
searches at all and fell back to guessing URLs; a same-session re-run of three weak briefs also
had no search and had to work purely via WebFetch of known URLs (Wikiquote, authors' own sites).

**Why:** the cap is per session, shared across all subagents in the workflow, not per agent.

**How to apply:** for any multi-agent web-research workflow, (a) tell each agent its search
budget (e.g. "at most 8 searches; prefer WebFetch of primary URLs you already know"), (b) stagger
or batch launches so the critic/gap/re-run stages still have budget, or (c) run re-runs in a
fresh session. Direct WebFetch of Wikiquote / author sites / filmsound.org / Talkhouse / Valve
commentary worked well as a no-search fallback. Related: [[story-craft-initiative]].
