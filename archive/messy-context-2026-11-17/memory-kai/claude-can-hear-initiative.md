---
name: claude-can-hear-initiative
description: Claude can hear — WORKING 2026-09-12 via the Gemini API, NOT the AI Studio browser (it 403s any CDP-driven generation); listen MCP live with the suno-diff lens; start at design/2026-09-11-claude-can-hear.md
metadata: 
  node_type: memory
  type: project
  originSessionId: c1009392-aace-4273-8105-aa95d9dd4862
  modified: 2026-09-11T17:19:07.830Z
---

Approved by Kai 2026-09-11 and committed (`801e045`, on main, not pushed). **Start at
`design/2026-09-11-claude-can-hear.md`** — the index holding the order of work, every human gate,
and the shared-checkout commit rules.

- `design/2026-09-11-listen-mcp.md` — the `listen` MCP server (T1–T15): describe an audio file
  through AI Studio's chat page (browser, Jack's Ultra account, Gemini 3.1 Pro), with local
  measurements grounding it and a ledger in `docs/listening/log/`. It uses its own browser channel
  ≥ 2 and never Flow's.
- `design/2026-09-11-understand-song-loop.md` — the `music-session` skill (T1–T13 + T4b), the
  **front door for "I want to make some music"**. It's a guided walkthrough where every step is an
  AskUserQuestion: explore (v6 W30 SI75 + Wild W60 SI60, Variety Off, 20 credits), the human picks,
  understand (record + describe + a draft "as a prompt"), refine one variable, narrow (cover the
  pick at AI 75 / 40). There are three listening modes (both / you-first / claude-only); credits
  need a yes every time.

**Why:** Kai can't describe sound, so the Suno feedback loop was weak; he wants Claude to bring the
vocabulary and newcomers (Jack) to be guided through a session.

**How to apply:** new sessions execute from the index file; the plans' checkboxes/Notes are the
source of truth.

**State 2026-09-12 — IT WORKS, and the browser route is dead.** The `listen` MCP server is live in
`.mcp.json` with `listen_status` and `listen_describe`; 122 tests; commits `1c47e37`→`6b7825a` on
main, **not pushed**.

🔴 **AI Studio's web page cannot be automated, and branded Chrome did NOT fix it.** Installing real
Google Chrome fixed only the **hand-typed** case: Kai typed "hello" and got an answer, then code
driving *that same window, profile and his own hand-opened tab* still got
`403 The caller does not have permission` on `GenerateContent`. Ten variables eliminated one at a
time — both models, audio vs text-only, prompt size, Temporary chat on/off, grounding on/off, our
tab vs his — with `navigator.webdriver` false and the brand reading genuine Chrome 153. The only
remaining difference is that a CDP client is attached; the page calls Google's Web Application
Attestation endpoint. **So it is not WSL and not the Chrome build**, and moving to Windows would not
help. We do **not** engineer around an integrity check. Recorded as Trap 4b in
`docs/listening/automation.md`.

**The working route is the Gemini API** (`GEMINI_API_KEY` in `.env`, loaded by the server itself —
an MCP server is launched by the client, not from a shell). `Transport` abstracts it: `GeminiApi` is
the default, `StudioTransport` composes an AI Studio chat and stops at Run for a human. Measured on
our key: `gemini-3.5-flash` accepts audio and works; `gemini-3.1-pro-preview` is **listed but 429s**
("check your plan and billing details"), so listing a model is not permission to call it.

🔑 **New: the `suno-diff` lens** (`docs/listening/lenses/suno-diff.md`) takes the audio **and the
three Suno boxes that made it**, and returns a clause-by-clause verdict (landed / partly / absent /
opposite) plus the next single edit as pasteable box text. That is what makes it a loop rather than
a review. First real run on camping's "The M3 Lane": asked 174 BPM D&B, arrived **117 BPM indie
breakbeat**, cause = a **1,186-char Style box** against the silent 1,000 cap. Every box in every
written sheet measures under the cap — the violation came from outside any sheet we can find.

**Calibration to keep:** asked to name a 440 Hz tone it said 220 Hz — an octave out. Gemini's
absolute numbers are unreliable, which is why tempo/loudness/brightness are measured locally with
`scripts/audio-measure.py` and never asked of Gemini.

**Still pending:** the `music-session` skill (loop T11) and its end-to-end run (T13); loop
T9/T10 live runs (20 credits each, need Kai's yes).
Related: [[suno-playback-recording]], [[suno-v6]], [[suno-session-method]], [[suno-four-box-atom]]
