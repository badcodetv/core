---
name: auto-push-on-commit
description: Commits here do NOT reach origin automatically any more — always check and push explicitly
metadata:
  node_type: memory
  type: project
  originSessionId: 69d1b5b2-6447-4521-8b4e-292bb23097cf
  modified: 2026-08-12T10:23:17.849Z
---

Historically (observed 2026-06-03) commits on a branch reached `origin` (GitHub:
`git@github.com:binocarlos/badcode.git`) without an explicit `git push`. **That is no
longer true.** On 2026-08-08 a commit on `main` stayed local, and on 2026-08-12 two
commits on `feat/enc-program` stayed local — `git status -sb` read `ahead 2` and
`git log origin/<branch> -1` was still on the old HEAD. Checked that day:
`.git/hooks/` has nothing but samples, `core.hooksPath` is the default, and there is
no husky setup. There is no auto-push mechanism in the repo now.

**Why it matters:** the live risk is the *opposite* of what this memory used to warn
about — work Kai believes is published sitting local on his machine. Do not tell him
something is pushed because you committed it.

**How to apply:** After committing, always confirm with `git status -sb`. If it reads
`ahead N`, the work is local. Kai says "commit" and "push" as separate things — pushing
is outward-facing, so ask (or note it plainly) rather than pushing unprompted. Still
never commit anything that shouldn't eventually be public. Related: [[project-overview]].
