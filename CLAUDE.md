# CLAUDE.md

This file loads into every session, so it holds only what is true for every task. Everything else is
loaded when the task needs it. Rebuilt from scratch on 2026-11-17 (the context reset: why and how in
[`docs/context.md`](./docs/context.md); the old file and memory are in `archive/messy-context-2026-11-17/`).

## What BadCode is

Two people: **Kai** (main developer) and **Jack** (lead creative designer); either may be driving. An art
collective that puts political and economic ideas into people's heads through **stories** (films, shorts,
comics) and **music**, because people remember a story and absorb a song in a way they never absorb an
essay. The fiction: BadCode is a superintelligence from a future that went wrong, sent back to help.

What every piece is for, whatever it looks or sounds like:
- **Offer a way out, not just a complaint.** Show the mistake, then the better choice.
- **Democracy means you can change how government works,** not just vote for the next dickhead.
- **There is more than materialism.** Greed has an explanation, and it isn't the only option.
- **The logo is fixed:** [`docs/brand/`](./docs/brand/README.md). Never hand-edit it.

## Working on a story? Read its `badcode.md` first

Every story, film, music video and short has a folder under `docs/stories/` with a **`badcode.md`** at its top:
what it is, its look, its sound, its own rules and which library pieces it uses. **That file is everything
that applies to the story.** Nothing from another story, from a shared doc's examples, or from a past
session applies unless it is written there. If the look or sound is "Not decided", run `story-style`;
never invent a default. Longer files in the folder (`look.md`, `sound.md`, reviews) are the record, opened
only when `badcode.md` points to them.

- **Starting a new story or short:** set up its folder and `badcode.md` (`new-story` / `new-short`), then
  propose which pieces of the [library](./docs/library/README.md) (looks, sounds, tricks) it should take in.
  Jack or Kai picks; the pieces are **copied** into its `badcode.md`, so changing the story never changes
  the library.
- **"Remember this":** a story rule goes in that story's `badcode.md`; an engine mechanic in
  `docs/rules/<engine>.md`; a way of working in `docs/rules/working.md`; only something true for every
  task comes here (ask first). Memory is kept empty.

## Rules for every task

- **Creative rules are a guide, not a gate.** Use them as a starting point, experiment, and say what you
  changed. Not loosened: the law and footage licences, never AI people composited into real footage,
  accounts and money, the logo, the coin's trust statement.
- **Mark a guess as a guess.** Never write an inference as a finding; prefer a free check.
- **Write swear words in full.** If an engine filters one, swap the word, never asterisk it.
- **Paste blocks:** label each with the exact box it goes in, and put all commentary above it, never after.
- **Read the board, never ask.** On any picks or notes page, dump the votes and notes yourself and act on them.
- **Generated files leave a recipe** ([`docs/provenance/`](./docs/provenance/README.md)): the Flow MCP,
  `run.mts`, the TTS script and Suno `record` write it themselves; otherwise `scripts/provenance/prov.py card`.
- **Scan before you show.** Every generated still or clip goes through `tools/qa-scanner/qa.py qa-checklist.json`
  before Jack or Kai see it: fix the fails, rescan (up to three passes), then show the best take and name any flag left.
  Add every new fault they name to `qa-checklist.json`. How: [`docs/rules/flow.md`](./docs/rules/flow.md) ("scan every still").
- **Another story's example is never a recipe.** When a shared file names a story ("the Bank Robbery recipe", "Camping's
  narrator"), that's history: never copy its wording, settings or voice into another story unless Jack or Kai asks for
  exactly that. Write a prompt only from the story's own `badcode.md` and the engine's rules.
- **The same-prompt check** (`scripts/variations/fresh.py`) runs by itself before every Flow, Suno and voice call, and flags
  LEAK / MIXED STORIES when a prompt carries another story's words. It
  reports and never blocks: rewrite the repeat, or keep it on purpose and say so.

## Engines and tools: read the rules before you drive one

| Driving… | Read first | Skills |
| --- | --- | --- |
| Google Flow (stills one at a time; every video on the tab pool, `scripts/scene/pool.mts`) | [`docs/rules/flow.md`](./docs/rules/flow.md) | `flow-automation`, `flow-prompt`, `shot-craft` |
| Suno (songs, sound for shorts) | [`docs/rules/suno.md`](./docs/rules/suno.md) | `suno-automation`, `suno-prompt`, `variations` |
| AI Studio voices, lip-sync | [`docs/rules/voices.md`](./docs/rules/voices.md) | `voice-casting`, `lip-sync-dub` |
| Premiere | [`docs/rules/premiere.md`](./docs/rules/premiere.md) | `premiere-automation`, `drive-sync` |
| YouTube (uploads, labels, playlists) | [`docs/rules/youtube.md`](./docs/rules/youtube.md) | `youtube-channel` |
| Anything with Jack or Kai (rounds, picks pages, media folders, Drive) | [`docs/rules/working.md`](./docs/rules/working.md) | |

Skills live in `.claude/skills/` and load on demand: the film is made with `overview-board` → `new-scene` →
`scene-beats` / `scene-images` / `scene-animation` / `scene-timeline`. Engine manuals hold facts about how an
engine behaves, never a story's style.

## Where things live

| Path | What |
| --- | --- |
| `docs/stories/<story>/badcode.md` | Each story's whole context. Resume pointers for every story: [`docs/stories/resume-index.md`](./docs/stories/resume-index.md) |
| `docs/library/` | The tool shed: looks, sounds and tricks a story may copy in. Applies to nothing on its own |
| `docs/rules/` | Standing rules per engine, and how Jack and Kai work |
| `docs/ideas/` | Raw ideas before they become stories (`new-idea`) |
| `docs/marketing/` | Reaching people: the `chief-of-staff` skill runs it. Board: https://claude.ai/artifact/3uuL8QzYF47wPCVyJVLNZ9 |
| `docs/voice.md`, `docs/marketing/the-reader.md` | How the narrator's **words** sound, and who the work is for. Read before writing a script, lyric or public copy. Words only: they say nothing about a picture or a sound |
| `docs/using-ai.md` | How we talk about making the work with AI (public copy only) |
| `docs/coins/emperors-new-coin.md` | Read before writing any sentence about the coin |
| `docs/government/` | The BadCode government: **paused since 26 Nov 2026**, nothing runs; read [`PAUSED.md`](./docs/government/PAUSED.md) first |
| `docs/misc/` | Meeting notes and anything else |
| Timeline index | https://claude.ai/artifact/KVLjAMnfz3NerFP9RQhxn6: every film's and short's timeline page. Rebuild with `scripts/scene/build-timeline-index.py` and republish to the same link when a timeline page changes |
| `tools/qa-scanner/`, `qa-checklist.json` | The QA scanner for generated stills and clips, and our checklist of every fault named |
| `apps/web`, `packages/comic` | The website; comics are written in code ([`packages/comic/AUTHORING.md`](./packages/comic/AUTHORING.md) before touching one) |
| `chain/`, `packages/chain-*` | The coin toolchain ([`chain/README.md`](./chain/README.md) first; keep it coin-neutral) |
| Media | The repo holds the words; `D:` (backed up to Drive) holds the media. Resolve a path with `localmap.py` before saying a file is missing |

## Running things

- `./stack start | stop | status | test | check` runs every local service (`./stack help`). Never write
  `badcode …` or `chain …` in docs or UI copy.
- The site: `npm install`, `npm run dev` (port 5173); `npm run typecheck` and `npm run build` cover all workspaces.
- Bob (the agent runtime) is a separate repo, `~/projects/badcode/bob`: don't build it here.
