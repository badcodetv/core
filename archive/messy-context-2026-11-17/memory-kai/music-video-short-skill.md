---
name: music-video-short-skill
description: "The music-video-short skill — a human-in-the-loop guide for 10–20s BadCode music videos; shipped to main, never yet live-exercised"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0bee9251-0c38-4d1b-a557-bd2407f977f3
---

`music-video-short` skill (shipped to main 2026-07-01, commits d1fa257..6b631e4) takes a BadCode short-form music video (10–20s) from idea to a **cut-ready package**, NOT a rendered mp4. Lives at `.claude/skills/music-video-short/SKILL.md`; each short is standalone-lightweight under `docs/shorts/<name>/` (convention doc: `docs/shorts/README.md`).

**Deliberately a guide, not full automation** — Kai's call: automating Suno end-to-end is "a fool's game" because Suno needs several rolls before a take hits, so a human moderating is a feature. Two **manual gates** (Suno generation → human returns `audio/track.mp3`; final cut → skill emits `edit-plan.md`, human edits). Only the one proven mechanical link is automated: Flow `image→video` clips (⚙). Six gated stages, `make-comic` family: concept → song → look & cast → scene breakdown → clips → edit plan.

**Load-bearing design choices:** the **song leads** (generated Stage 2 so it bakes through Suno rolls; everything cuts to its `ffprobe`-measured duration, never a guess); composes [[flow-automation-integration]] tools (`flow_generate_image/_video/_create_character`) + `suno-prompt` + `badcode-art-direction`; per-scene `sNN.md` records (exact still+motion prompts + revision log) make "change scene N" a one-scene reroll.

**v1 out of scope (future cycles):** auto-muxing the final mp4 (contract ends at the plan), automating Suno, automatic beat/section detection (human's ear is truth), anchoring a short to an existing `docs/<story>/` canon, website publishing.

**Status:** authored + committed via a Sonnet/low workflow, but **never live-exercised** — no real short built yet. First real run needs `./scripts/flow-chrome.sh` logged in (Flow) + a human doing the Suno + cut gates. Spec: `docs/superpowers/specs/2026-07-01-music-video-short-skill-design.md`; plan: `docs/superpowers/plans/2026-07-01-music-video-short-skill.md`.
