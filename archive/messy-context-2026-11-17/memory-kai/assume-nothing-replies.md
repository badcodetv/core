---
name: assume-nothing-replies
description: Kai wants replies that assume no prior knowledge — gloss every ticket number/identifier, add a plain-terms overview and a "what do I actually decide" section; never dumb down, never drop detail
metadata:
  type: feedback
---

Kai finds terse status replies hard to parse: bare ticket numbers ("T20", "T11/T14") and unglossed identifiers mean nothing to them, and sentences that assume they remember the last session are unreadable.

**Why:** ADHD reader, walking in cold each session. Losing information is NOT acceptable; the fix is to add explanation, not remove detail.

**How to apply:** The Rundown output style (`~/.claude/output-styles/rundown.md`, locally edited 2026-08-26, backup at `rundown.md.bak`) now mandates: TL;DR → **In plain terms** (2–5 ELI5 lines) → state checklist → **You decide** (each real decision, options, cost, recommendation, or "Nothing to decide") → **Your move**. Every ticket/branch/file/acronym gets a plain-English gloss on first mention. Follow this even if the style file is ever reverted by an upstream update. See [[team-kai-and-jack]].
