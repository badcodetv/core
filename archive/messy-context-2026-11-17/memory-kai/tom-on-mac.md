---
name: tom-on-mac
description: Tom (music) joined BadCode 2026-11-04, runs Claude Code + Suno automation on macOS; Mac gaps and setup fixes
metadata:
  type: project
---

Tom, a music person, joined BadCode on 2026-11-04 and makes Suno tracks with Claude Code on his Mac (no VM). See [[team-kai-and-jack]].

Setup sheet: docs/misc/2026-11-03-mac-setup.md; preflight: scripts/mac-check.sh.
On a Mac, `suno.mts record` and the listen tool don't work (PulseAudio is Linux only), and neither does Premiere. Everything else in Suno works.

**Why:** Kai wanted Tom to have the same experience as Jack, with as little friction as possible.
**How to apply:** if a session is on darwin, don't offer record/listen/Premiere. Two fixes Tom needed that the sheet lacks: (1) the gh CLI .pkg lives on github.com/cli/cli/releases/latest (macOS_universal.pkg), because the cli.github.com button gives a zip; (2) the Claude native installer puts `claude` in ~/.local/bin, which isn't on PATH, so add it in ~/.zshrc. Tom and Jack must not drive the same Suno account at once ([[suno-one-session-at-a-time]]).
