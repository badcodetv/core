# Work board — 2026-09-12 (Kai's brain-dump, digested)

Status: **coordination doc, nothing started.** Paste-ready prompts per thread: [`2026-09-12-threads/`](./2026-09-12-threads/README.md). Written from Kai's opening brain-dump on 2026-09-12.
Spans three repos: this one (BadCode), `../agent-bob`, `../agent-wolf`. Each thread names the file
that is its real source of truth; this board only coordinates.

## The threads

| # | Thread | Repo | Source of truth today | State |
|---|---|---|---|---|
| 1 | **Ops — the OVH box.** Order the server, build it, move every app off the Kubernetes cluster except NoCode and Franchise Cloud (both shut down next week). Purpose: run Agent Bob and Agent Wolf for real. | agent-bob | `docs/ops.md` (Part 2 = step-by-step); design `design/2026-09-11-ovh-compose-hosting.md` says "nothing provisioned, nothing bought" | ⬜ not started |
| 2 | **Agent Bob — running properly.** (a) Resume the paused onboarding fleet (3 tickets merged, 5 branches finished-but-unverified). (b) Define and run the first workflow for three real projects: Emperor's New Coin (with Richard), the BadCode government, the BadCode marketing manager. Product need: at the start of a project the user wants to see the architect's decisions fast, and its *reaction* to events, and to adjust the team. **Ruled 2026-09-12:** ENC gets a storage-only repo `agent-enc` (Bob's git projection target, no UI); Kai's WhatsApp becomes a Bob connection by reusing Platinum's WAHA session (W0 proves send-to-self + read the Richard thread); the Richard thread is ingested *through the channel* as named documents, and the ENC workers are designed only after reading it — three stages in `2026-09-12-threads/03`. | agent-bob | `design/2026-09-11-onboarding-work-plan.md` (RESUME HERE block); `docs/21-git-projection.md`; `feat/project-connections` (unmerged) | 🟡 paused mid-wave |
| 3 | **Agent Wolf — live so friends can log in and test.** Depends on 1 (a box) and 2a (Bob stable). | agent-wolf + agent-bob | `../agent-bob/design/2026-08-20-agent-wolf.md`; `./stack wolf up` | ⬜ local only |
| 4 | **Camping music video cut + test the listening tools.** Use the new listen/music-session tooling to hone the camping track against Jack's guidance (he has named a reference band — not yet in the repo). | badcode | `docs/stories/camping/music-video.md` (Kai's hand cut), `songs/camping-sheet.md` (Jack's 2026-08-27 brief: lost aggression and pace; try genres over D&B), `design/2026-09-11-claude-can-hear.md` | 🔴 listen-mcp paused at T3: AI Studio returns 403 to Chrome for Testing; fix = branded Chrome |
| 5 | **GPOM stills — scene by scene, WITH VARIETY.** Images are free, so storyboard hard up front: for each scene propose several genuinely different visual takes, Kai picks, we hone (the Suno listen→describe→refine loop, for pictures). Record this as a rule in the image skills. | badcode | `docs/stories/gitpush-origin-master/storyboard/`, `scenes/`; skills `badcode-art-direction`, `flow-prompt`, `shot-craft` | ⬜ |
| 6 | **MMT — stock footage research** for the war and the NHS. Sourcing lane, not Flow. | badcode | `docs/stories/magic-money-tree/documentary.md`; `find-footage` skill; `docs/video-fx/footage-sources.md` | ⬜ |
| 7 | **GPOM narration track** — Suno narration, dry and separate, same method as camping. | badcode | `docs/stories/gitpush-origin-master/songs/`; memory rule "dry-and-separate narration" | ⬜ |
| 8 | **Parked ideas (not now):** Premiere automation extensions; Ableton automation; sound design in Serum via computer-use (Astra/Fable desktop, Codex desktop); extract the newsreader's voice from Suno and make the music ourselves. Shortcut for now = music AND narration out of Suno. | badcode `docs/ideas/` | — | ⬜ park via `new-idea` |

## The style-guide question (answered)

Kai noticed every image is muted / dystopian and asked whether the style guide is too strong.
**Yes — it is written in as a rule, not a preference.** `.claude/skills/badcode-art-direction/SKILL.md`
rule 1 says the 35mm documentary preamble with "muted cool-neutral palette" *"is not a stylistic
option — it is the format"*, and rule 2 says warmth is allowed "only as argument". `new-image`
does the same for brand imagery ("LEDs are the only colour"). So the sameness is obedience.
Nothing in the skills asks for a spread of options; only `edit-panel` makes two candidates.

## Rules to add to the image skills (thread 5)

1. **Storyboard stills are proposed as a spread, not a pick.** Default 4 candidates per beat,
   each a *different idea* (framing, palette, register, distance, time of day) — not four
   seeds of one prompt.
2. **The house register is one candidate, never all four.** At least one candidate breaks the
   muted palette on purpose so the muted one is chosen, not defaulted.
3. **Hone like the music loop:** Kai picks → describes the change in words → we refine from
   the pick → narrow. Every candidate's prompt is recorded in the story's `prompts.md`.

## Inputs only Kai has

- Jack's camping guidance and the reference band name (thread 4).
- The WhatsApp thread with Richard on how Emperor's New Coin should work (thread 2b).
- OVH account / card, and Jack's Google account for the listening browser (threads 1, 4).

## Suggested split into sessions

- **Session A (agent-bob checkout):** thread 1, then 2a, then 3. Ops is sequential and blocks on Kai (ordering the box).
- **Session B (this checkout, BadCode):** thread 5 first (needs no human input; establishes the variety rule), thread 6 in parallel via subagent, thread 4 as soon as the band name + branded Chrome land.
- **Thread 2b** (the three Bob workflows) is design work; do it once 2a is verified.
