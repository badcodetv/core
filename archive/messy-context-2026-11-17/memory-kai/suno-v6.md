---
name: suno-v6
description: "2026-09-10 Kai ruling — ALL new Suno work is v6 in the new UI; v5.5 archived; suno.mts re-mapped live (model required, grid/controls commands); R1 grid not yet run"
metadata: 
  node_type: memory
  type: project
  originSessionId: f80ca360-f993-437e-8c3d-b159c718af1e
  modified: 2026-09-10T08:04:43.021Z
---

Suno v6 launched 2026-09-09 (v6 / v6-wild / v6-mini). **Kai, 2026-09-10: "any new work we do in
Suno is in the new UI on V6"** — v5.5 knowledge moved to `docs/suno-gpt/archive/v5.5-era.md`, and
the 11 song sheets pinned to v5.5 carry an archive banner (history sheets; a new round starts a v6
sheet). Research: `docs/suno-gpt/files/suno-v6.md` (§3 = one-word/one-bar fix ladder) + ledger
`docs/misc/2026-09-10-suno-v6-research.md`.

Kai's asks that shaped it: automation = **pre-fill prompts + settings into a workspace to
mass-generate experiment permutations** (NOT automating Studio); Studio = knowledge only, so Claude
suggests "you can do that in Studio, here's how" unprompted; top pain = fixing one word / one bar.

**Why:** v5.5 cannot generate any more; everything model-specific before 2026-09-09 is history.
**How to apply:** every spec needs `model` ('v6' | 'v6-wild'); `suno.mts` sets + reads back model,
variety, maxMode, vocalGender, personalize (live-proven 2026-09-10 via `controls`). `grid-plan` is
free; `grid`/`pair` spend credits (v6 cost unknown — logged per Create). Suno can switch the model
on its own ("Model changed" toast) so it is read back last. Open: Personalize's "My Taste" button
semantics (affects [[suno-four-box-atom]]); R1 = {v6, v6-wild} × {w30, w60} awaits Kai; on
2026-09-10 My Taste held another session's profile, not the freedom token. Related:
[[suno-form-state-persists]], [[suno-check-form-mode]].

**2026-10-14 refresh (Kai):** ChillPanic 2026-10-09 video + a 10-agent workflow sweep (5 researchers + 5 adversarial verifiers) rewrote suno-v6.md: §1b **Speech (beta, shipped 2026-10-01)** — script + ONE style box, ~8 min, Variety Exact style, word Replace works on Speech takes, British accent failed in 2 outside tests; §3 rung 1b self-Cover (Var Off/AI100/SI0/W0) + Subtle Remaster for problem B; §9 tempo words (`slow`/`half-time` halve BPM — prime suspect for our D&B half-time drift). Tests 0 / 0b–0d queued in §12, none run. Uncommitted at time of writing — check `git log`. Ledger docs/misc/2026-10-14-suno-v6-refresh.md. Links: [[gpom-narration-scored]], [[listen-only-when-asked]].
