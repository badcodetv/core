# Ableton Automation — a Bridge Like the Premiere One

Give a Claude session hands inside Ableton Live, the same way it already has hands inside
Premiere Pro: build a set, drop a clip, arrange it, automate a filter, bounce a WAV, listen to
what came out, change one thing, bounce again.

**Kai, 2026-09-12: not now.** The shortcut this season is that music and narration both come out
of Suno, so there is no bed to automate yet. This is the sequel to
[Make the Music Ourselves](ableton-bed-suno-voice.md) — pointless before it, obvious after it.

## What it would buy

- **The Suno loop, on a real DAW.** The thing that makes Suno work is not the model, it is the
  loop: change one variable, generate, *listen*, judge, repeat (`docs/suno-gpt/session-method.md`).
  A bridge puts that loop on a tool that does exactly what it is told.
- **The boring 80%.** Tempo, key, arrangement lengths, bouncing every variation of a bassline,
  rendering forty candidates overnight. Kai keeps the taste; the session does the clicking.
- **A closed ear-to-hand loop.** We can now *hear*: `design/2026-09-11-claude-can-hear.md` is the
  listening tooling, and the Suno playback capture is proven (memory, 2026-09-11). Bridge plus
  ears means a session can bounce, listen, and iterate without a human in the middle of every round.

## What it costs

- **A whole package, plus a protocol.** `packages/premiere-mcp` is a server *and* a panel *and* a
  wire protocol (`docs/premiere/bridge-protocol.md`), and it took a build plus a documentation pass.
- **Ableton's remote-control surface is not Premiere's.** Live has no UXP panel. The real routes
  are **Max for Live** (a device inside the set that can talk out), the **Live Object Model** via
  a Remote Script in Python, or **OSC**. Which of the three is a research ticket, not a guess.
- **A wide known-unknowns gap.** Premiere's own notes file is 1,500+ lines of "what Adobe claims
  versus what happens" (`docs/premiere/api-notes.md`). Assume Live has its own equivalent, unwritten.

## What already exists to build on

- **`packages/premiere-mcp` is the pattern, and the topology is the lesson.** A plugin inside the
  Windows host **cannot listen on a socket — it can only dial out**
  (`packages/premiere-mcp/README.md:23`). So the MCP server lives in WSL and is the WebSocket
  *server*; the panel is the *client*; nothing is installed on Windows but the panel. Any Ableton
  bridge inherits that shape wholesale.
- **`docs/premiere/`** — the four-file split works and should be copied: `recipes.md` (the
  cookbook), a catalogue of what is installed, `setup.md` (one-time per machine), `api-notes.md`
  (append every surprise).
- **The hard-won operating rules**, which will recur: a rebuild does not reload the plugin; every
  edit acts on the *active* document, so a human clicking another tab silently redirects the next
  call; and the tool must be able to **look at what it did** (`premiere_export_frame` — the audio
  equivalent is a bounce plus the listen tooling).
- **Serum is already in the room** — see [Serum via Computer Use](serum-via-computer-use.md).
  A bridge that can place a Serum instance and a computer-use agent that can *dial* it are the
  two halves of one job.

## What un-parks it

- [Make the Music Ourselves](ableton-bed-suno-voice.md) un-parks first — a bridge with no music
  to make is a toy.
- Or: Kai has bounced the same set by hand more than about three times and it grates.
- Or: the listening tools land properly (`design/2026-09-11-claude-can-hear.md` is paused at
  ticket T3, AI Studio refusing Chrome for Testing with a 403), because ears are what make the
  loop worth automating.
