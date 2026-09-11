# Claude can hear — execution index

Start here. This file tells an autonomous session what to build, in what order, and where it must
stop for a human. Written 2026-09-11 at the end of the session "claude-can-hear".

## What it is

Claude can't hear audio, and the humans driving Suno lack sound-design vocabulary. Two plans fix
that:

| Order | Plan | Builds |
|---|---|---|
| 1 | [`2026-09-11-listen-mcp.md`](./2026-09-11-listen-mcp.md) | the `listen` MCP server: give it an audio file, and it returns a description (Gemini 3.1 Pro via AI Studio's web page) plus local measurements, filed in `docs/listening/log/` |
| 2 | [`2026-09-11-understand-song-loop.md`](./2026-09-11-understand-song-loop.md) | the `music-session` skill: a guided Suno loop (explore → pick → understand → refine → narrow), recording takes silently from the browser |
| — | [`2026-09-11-suno-playback-recording-findings.md`](./2026-09-11-suno-playback-recording-findings.md) | evidence only: the proven recording method and its measurements |

Both plans are **approved** (Kai, 2026-09-11). Their EXECUTION RULES apply.

## Order of work

1. listen-mcp T1–T15, in dependency order.
2. The loop plan's tickets that don't need listen-mcp can run alongside: T1, T2, T4, T4b, T5, T6, T9 (T3
   needs listen-mcp T1). Its T13 needs listen-mcp T15.
3. Tick checkboxes and set Status in the plan files as you go. The files are the source of truth, so
   work can stop and resume at any time.

## 🔴 Stop and ask a human, and never work around these

| Where | Why |
|---|---|
| listen-mcp T3 | a browser channel must be signed into **Jack's Ultra Google account** |
| listen-mcp T3 stop gates | no Pro model accepts audio; or AI Studio saves uploads to Jack's Drive with no off switch |
| listen-mcp T12 (the signed-out check), T15 | manual checks and the end-to-end run need Kai |
| loop T4 / T4b stop gates | Suno's create page can't play a take without navigating away; or v6 Cover state can't be detected or the pick can't be attached unambiguously |
| loop T4, T4b, T7, T8 | the Suno channel must be signed in (account `binocarlos`); if signed out, stop |
| loop T6 | a human confirms that live audio is still audible |
| loop T9, T10 | **each 20-credit run needs Kai's explicit yes** — dry-run first, always |
| loop T13 | a human-driven session |

Everything else is autonomous.

## House rules that bind every ticket

- **Shared checkout.** Other sessions' uncommitted work lives in this tree. Commit per ticket on
  `main`, staging **only that ticket's files** (never `git add -A`), with the repo's sentence-style
  messages. **Never push.** Don't switch branches (it would move other sessions' commits).
- **One Suno tab, ever.** Never navigate away from `suno.com/create` (it wipes the form). Never
  automate a Suno download. Nothing spends Suno credits without Kai's yes.
- **Browser channels:** never pick a port by hand; use `./scripts/browser-channel.sh`. The listen
  server never takes channel 1 or a Flow browser.
- **Media outside the repo, words inside.** Recordings go to `LISTEN_MEDIA_ROOT` (default
  `/mnt/c/Users/kai/Desktop/suno-recordings`); descriptions and logs go in the repo.
- **The preview filter** (`lowpass=f=8000:poles=2` twice) touches only the human's preview copy,
  never the file Claude measures.
- Read `CLAUDE.md` first; read `docs/suno-gpt/automation.md` before touching `scripts/suno/`.

## When a gate is hit

Stop and report in the Rundown style: what's done, what's blocked and why, and the exact thing the
human must do. Append it to the plan's Discovered Issues Log too.
