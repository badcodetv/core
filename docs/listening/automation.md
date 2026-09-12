# AI Studio chat page — the listen server's DOM map

The `listen` MCP server (`packages/listen-mcp`) drives AI Studio's chat page with **fixed Playwright
routines** — no model reads the page to decide a click. This file is the evidence behind every
selector in [`packages/listen-mcp/src/studio-dom.ts`](../../packages/listen-mcp/src/studio-dom.ts).
Format mirrors [`docs/suno-gpt/automation.md`](../suno-gpt/automation.md).

> 🔴 **Status 2026-09-12: the page is MAPPED and the code is written; blocked on one human step.**
> Everything in §2 is read off the live page and is now encoded in
> [`studio-dom.ts`](../../packages/listen-mcp/src/studio-dom.ts), with the routines in
> `studio-client.ts` and the `listen` server registered in `.mcp.json`. What remains is **not a
> mapping problem**: every generation is refused with **403 "The caller does not have permission"**
> (Trap 4), because AI Studio rejects Chrome for Testing — pressed by hand it says *"Failed to
> create interaction: permission denied."* **The fix is branded Google Chrome on the listening
> channel** (guarded in `scripts/flow-chrome.sh` as of 2026-09-12 so no other channel switches
> binary), then a human signs that window in. The reply's formatting and the running/done signal
> stay ⬜ until one run succeeds, which is why `waitForReply` trusts no single indicator.

## 1. Connecting

- **Channel 2** (`./scripts/browser-channel.sh up 2`, port 9223, profile `.flow-profile-9223`),
  signed into **Jack's Ultra account** (`jacktttt330@gmail.com`, badge `ULTRA` in the sidebar) on
  2026-09-11. Never channel 1 — that is Flow's (and Suno's) browser.
- Attach with `chromium.connectOverCDP`, `contexts()[0]`, and use **our own tab**, marked with
  `sessionStorage['__badcode_listen_tab'] = '1'` (same pattern as `scripts/suno/suno.mts`). Never
  `goto` on another tab — Jack may be using AI Studio in the same window.
- **New chat URL:** `https://aistudio.google.com/prompts/new_chat`. Adding
  `?model=<model id>` preselects the model — selecting Gemini 3.1 Pro in the menu rewrote the URL
  to `…/new_chat?model=gemini-3.1-pro-preview` (2026-09-11).

## 2. Selectors (2026-09-11)

| Control | Selector | Evidence |
|---|---|---|
| **Signed in?** | the account button's text `jacktttt330@gmail.com ULTRA` (`button.account-switcher-button`) | present after sign-in |
| **Signed out** | URL `https://aistudio.google.com/welcome` (marketing page, "Get started") | a fresh profile landed there — **no** accounts.google.com redirect |
| **New chat** | `button[aria-label="New chat"]` (or navigate our own tab to the new-chat URL) | top bar |
| **Model card** (opens the menu) | `button.model-selector-card`; current name = its `span.title` (`Gemini 3.1 Pro Preview`), id = first `span.subtitle` (`gemini-3.1-pro-preview`) | read back after selecting |
| **Model rows** | `ms-model-carousel-row button.content-button`, `id="model-carousel-row-models/<model id>"`; name in `.model-title-text` | 16 rows listed (below) |
| **Search grounding** | `button[role="switch"][aria-label="Grounding with Google Search"]`, `aria-checked` | 🔴 **ON by default** on a new chat; also shown as a chip with `button[aria-label="Remove Grounding with Google Search"]` |
| **Temperature** | `input[aria-label="Temperature"]` (range + spinbutton) | default `1` |
| **Thinking level** | `mat-select[aria-label="Thinking Level"]` | default `High` |
| **Attach** | hidden `input.file-input[type="file"]` inside `ms-add-media-button` (`multiple`, accepts `audio/*`, `.mp3`, `.wav`, …) — set it directly, never the OS chooser. Visible trigger: `button[data-test-id="add-media-button"]` ("Insert images, videos, audio, or files") | ✅ `setInputFiles` works — after the first-use dialog (Trap 5) |
| **Upload finished** | `ms-prompt-box ms-prompt-media` shows `<file name>` + **`<N> tokens`** | ✅ `tone.mp3 · 322 tokens` for 10 s — Gemini's 32 tokens/s, so the token count is the "processed" signal |
| **Prompt box** | `textarea[aria-label="Enter a prompt"]` | present |
| **Run** | `ms-run-button button` (text `Run Ctrl ↵`; **no** `type` attribute — `.type` merely defaults to "submit"); `aria-disabled="true"` while the prompt is empty, and again after a run | ✅ clicked |
| **Chat turns** | `ms-chat-turn`; the author is `[data-turn-role="User"]` / `[data-turn-role="Model"]` inside it. The upload is its own User turn (`audio_file tone.mp3 322 tokens`), then the prompt, then the Model turn | ✅ |
| **More actions** | `button[aria-label="View more actions"]` → menu items `Temporary chat`, `Save` (`No changes to save`), `Make a copy`, `Delete`, `Raw Mode` | opened live |
| Running/done signal · reply formatting | ⬜ | no run has succeeded (Trap 4) |

**Models offered on the Ultra account (2026-09-11):** Gemini 3.8 Flash · Gemini 3.5 Flash Lite ·
**Gemini 3.1 Pro Preview** · Gemini 3.5 Live Translate Preview · Gemini 3.1 Flash Lite · Gemini 3
Flash Preview *(Paid)* · Nano Banana 2 Lite · Nano Banana 2 *(Paid)* · Nano Banana Pro *(Paid)* ·
Gemini 3.5 Transcribe · Gemini Pro Latest · Gemini Flash Latest · Gemini Flash-Lite Latest ·
Gemini Robotics-ER 2 Preview · Gemini 3.5 Transcribe Live · Gemini Omni 1.1 Flash *(Paid)*.
The default model on a new chat was **Gemini 3 Flash Preview**, which is marked *Paid* ("only
available via a Google AI plan or pay per request with an API key"). **Gemini 3.1 Pro Preview is
not marked Paid.** Whether it accepts audio is ⬜ (Trap 4).

## 3. Settings that exist

- **User Settings** (Settings → User settings): Theme · Submit prompt key · Autocomplete · Applet
  notifications. **Nothing about saving, history or Drive.**
- **Temporary chat** (More actions): the page then reads *"Temporary chat · Your conversation won't
  be saved automatically"*, so an ordinary chat **is** saved automatically.

## 4. Traps

### Trap 1 — 🔴 uploads go to Google Drive, even in a Temporary chat

Verbatim, from the Temporary chat banner (2026-09-11): *"Your conversations won't be saved.
However, any files you upload will be saved to your Google Drive. Logging policy still applies even
in Temporary chat."* No account-level switch was found. So every listen would leave its mp3 in
**Jack's** Drive. This was the plan's stop gate (2). **Ruled 2026-09-11 (Kai): accepted** — it is
Jack's and Kai's shared workflow and Jack will use the tool himself; tell Jack, and keep the files
together. The server always opens a **Temporary chat**, so only the audio lands in Drive, never
the conversation.

### Trap 2 — Search grounding is on by default

A new chat starts with **Grounding with Google Search** on. The server must switch it off every
time (`disableSearchGrounding`), or a description can be padded with web results about the song's
title instead of what is heard.

### Trap 3 — the signed-out page stays on aistudio.google.com

`/welcome` is on the same host, so "has an aistudio.google.com tab" is not proof of a sign-in
(`browser-channel.sh` reports `yes` for it). `listen_status` is the authority.

### Trap 4 — 🔴 403 "The caller does not have permission" on every run (open)

Seen 2026-09-11 on Jack's freshly signed-in channel-2 profile, six runs: Gemini 3.1 Pro Preview with
the tone, 3.1 Pro with text only, Gemini 3.8 Flash with text only, Temporary chat on and off, and
after a reload. The page shows a Model turn reading **`error` · `An internal error has occurred.`**;
the network shows `POST alkalimakersuite-pa.clients6.google.com/$rpc/…MakerSuiteService/GenerateContent`
→ **403** `[,[7,"The caller does not have permission"]]`. Not audio-specific, not model-specific.
The prompt bar's `No API key selected` button leads to **"Link a paid API key" → Choose project →
Set up billing** (🔴 never click "Set up billing"); opening it added `?project=gen-lang-client-0044990194`
("Default Gemini Project") to the URL, but the first failure happened before that. Cause unknown;
the next test is a human typing a prompt by hand (in this window, and in a normal browser).

**Narrowed later the same day:**
- ✅ **The account is fine.** Kai typed "hello" in Jack's **normal browser** (dark theme, the saved
  test chat opened from History) and Gemini 3.8 Flash answered *"Hello, nice to meet you."*
- 🔴 **Channel 1 fails too** — the long-established Flow profile, same account, a fresh tab: 403. So
  it is not the fresh profile.
- 🔴 **Real keystrokes fail too** (`pressSequentially` + the Run button, and Ctrl+Enter).
- 🔴 **Detached fails too** — prompt typed, the page scheduled to click Run 4 s later, CDP
  disconnected before it fired: 403.
- The channels run **Playwright's bundled Chromium** (`~/.cache/ms-playwright/chromium-1234`,
  `Chrome/151.0.7922.34`, Linux UA) — `flow-chrome.sh` falls back to it because no branded Google
  Chrome is installed in WSL. **Hypothesis (unproven):** AI Studio's `GenerateContent` refuses
  non-branded Chromium, while Flow does not. The decisive test is a human pressing Run by hand in
  the channel-2 window; the likely fix is a branded Google Chrome for the listening channel.
  Do NOT spoof browser headers to get around it.

### Trap 4b — 🔴 SETTLED 2026-09-12: AI Studio refuses generations from a CDP-attached browser

Branded Google Chrome fixed the **hand-typed** case and nothing else. Kai typed `hello` in the
channel-2 window at 14:26 and Gemini answered. Driven from code in **that same window**, every
generation still returns 403 `The caller does not have permission` on
`MakerSuiteService/GenerateContent`.

**Eliminated by measurement, one variable at a time (all on branded Chrome 153.0.8010.36):**

| Suspect | Test | Result |
|---|---|---|
| The model | Gemini 3.1 Pro, text only | 403 in 5 s |
| The model | Gemini 3.8 Flash, text only | 403 in 4.6 s |
| Audio / file size | text only, no attachment | 403 — so not audio |
| Prompt size | 30 characters | 403 |
| Temporary chat | on **and** off | 403 both |
| Search grounding | on **and** off | 403 both |
| A tab we created | `ctx.newPage()` | 403 |
| **A tab the HUMAN opened** | drove Kai's own tab, no navigation | **403** |
| Chrome brand | `navigator.userAgentData.brands` → `Google Chrome 153` | genuine |
| The obvious automation flag | `navigator.webdriver` | **false** — the page cannot see it |

So it is not WSL, not the Chrome build, not the profile, not the tab, not the flags, not the model
and not audio. The one remaining difference between a working run and a failing one is that **a CDP
client is attached**. The page also calls `waa-pa.clients6.google.com/$rpc/…Waa/Create` — Web
Application Attestation, Google's environment-integrity check — which is a plausible mechanism,
though we have not proven that is the specific gate.

🔴 **We do not engineer around this.** Spoofing headers, patching `navigator.webdriver`, or
detaching the debugger to slip a click past an integrity check are all circumvention of a control
the site is deliberately applying. The sanctioned programmatic route is the **Gemini API**, which
exists for exactly this and needs no browser.

**Consequence for the listen server:** the browser transport (`studio-client.ts`) is a
**human-assisted** path only — it can compose the prompt and a human presses Run. Automated
describes need an API transport. Everything else in the server is transport-independent: the lens,
the prompt composer, the measurements, the timestamp remap and the ledger all stay exactly as they
are. See `design/2026-09-12-listening-transport.md`.

### Trap 5 — a first-use media dialog swallows the first upload

The first file ever attached on an account opens *"Start creating with media in Google AI Studio"*
(rights reminder + Prohibited Use Policy) with **Cancel / Acknowledge**; the file attaches only
after Acknowledge (`mat-dialog-container button` "Acknowledge"). Acknowledged once on Jack's account,
2026-09-11, under Kai's ruling that uploads are fine.

### Trap 6 — New chat asks for confirmation, and is disabled on an empty chat

`button[aria-label="New chat"]` opens *"Create a new chat — Content of your current prompt will be
deleted"* → **Discard and continue**; on an already-empty chat it is `aria-disabled="true"`.
Navigating the tab to the new-chat URL does **not** start a new chat — the old turns come back.
**Temporary chat is sticky**: it stays on across New chat until switched off.

## 5. Verified

| Claim | Status |
|---|---|
| Channel 2 is signed into Jack's Ultra account | ✅ 2026-09-11 |
| Gemini 3.1 Pro Preview is offered and selectable | ✅ 2026-09-11 |
| Search grounding is on by default | ✅ 2026-09-11 |
| Uploads are saved to Drive even in a Temporary chat | ✅ 2026-09-11 (the page says so) — ruled acceptable |
| Upload works and reports a token count | ✅ 2026-09-11 — 10 s tone → 322 tokens |
| A Pro model accepts audio and replies | 🔴 every run 403s (Trap 4) |
| Run/done signal, `innerText` keeps headings | ⬜ |
| Error wording | ✅ `An internal error has occurred.` (UI) / `The caller does not have permission` (403) |

## Revision log

- **2026-09-12 (later)** — Trap 4b: the 403 is the CDP attachment, not the browser. Branded Chrome
  fixed hand-typing only. Ten variables eliminated by measurement, including driving the human's own
  tab. The browser transport is human-assisted only; automated describes need the API.
- **2026-09-12** — the map is encoded in `studio-dom.ts` and driven by `studio-client.ts`;
  `listen_status` / `listen_describe` are live in `.mcp.json`; `flow-chrome.sh` now gives branded
  Chrome to the listening channel ONLY (other channels keep Playwright's Chromium, so Flow's and
  Suno's profiles are not locked out by a version downgrade). Still one human step: install Chrome,
  sign in.
- **2026-09-11 (later)** — Drive gate ruled; upload, chip, turns and Run mapped; Traps 4–6. Every
  generation 403s — T3 blocked on it.
- **2026-09-11** — first live map (listen-mcp T3), stopped at stop gate (2) before any upload.
