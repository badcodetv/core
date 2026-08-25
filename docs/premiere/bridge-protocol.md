# The bridge wire protocol

Between `@badcode/premiere-mcp` (a `ws` **server** in WSL) and the UXP panel (a WebSocket
**client** inside Premiere on Windows). **Read this only if you are changing the bridge itself** —
using the tools needs none of it.

Ground truth is [`packages/premiere-mcp/src/protocol.ts`](../../packages/premiere-mcp/src/protocol.ts),
which is shared by both halves. If this file and that one disagree, the code wins; fix this file.

## Why the server is in WSL and the panel dials out

A UXP plugin **cannot listen on a socket** — it can only make outbound connections, and the target
must be declared in `manifest.json`. Windows→WSL `localhost` forwarding is on by default in WSL2
NAT mode. Together those two facts settle the architecture: the server lives inside the MCP server
process in WSL, the panel connects out to it, and **nothing but the panel is installed on Windows**.

Verified live: plain `ws://localhost:7890` works on default WSL2 NAT — no mirrored networking, no
direct-IP fallback, no firewall rule.

## Frames

Four kinds, all JSON, all one message per frame.

```ts
type Hello  = { type: 'hello'; appVersion: string; panelVersion: string; protocol: 1 }
type Cmd    = { type: 'cmd'; id: string; cmd: CmdName; args: unknown }
type Result = { type: 'result'; id: string; ok: true;  result: unknown }
            | { type: 'result'; id: string; ok: false; code: ErrorCode; message: string; detail?: unknown }
type Log    = { type: 'log'; level: 'info' | 'warn' | 'error'; message: string }
```

- **`hello` is the handshake.** The panel sends it on connect. Until it arrives and validates, the
  bridge does **not** consider itself connected — a socket alone is not enough. This is deliberate:
  a stale panel from an older build opens the socket normally, so "port is up" proves nothing.
- **`id` correlates a `cmd` with its `result`.** Every command carries one; the server matches on it.
- **`log` frames are forwarded to stderr**, so the panel's own log reaches the session's transcript.
- Malformed frames are logged and ignored rather than taking the connection down.

## The rules the bridge enforces

1. **Strictly serial.** One command in flight, FIFO queue behind it. One Premiere, one panel — the
   same law as Flow's one browser.
2. **Connect-wait.** A `send()` issued before any panel has connected waits (15 s in the server,
   5 s by default in the class) and then rejects `PANEL_NOT_CONNECTED`. The wait exists because a
   panel reconnects on its own exponential backoff, capped at 10 s.
3. **Per-command timeout**, default 30 s, raised per call for slow ones (import 120 s, export 600 s).
   A command that times out does not block the next one.
4. **A second panel supersedes the first.** The old socket is closed with reason `superseded`, and
   🔴 **any command in flight on it is failed explicitly** — an earlier version let it hang until
   its own timeout, because by the time `close` fires the socket reference already points at the new
   connection.
5. **A disconnect mid-command rejects `PANEL_NOT_CONNECTED`** rather than hanging.

## Error codes

Every failure reaches the caller as `{ error: true, code, message, hint? }`.

| Code | Means |
| --- | --- |
| `NO_MEDIA_ROOT` | No `badcode.local.json`, and a tool needed the media root |
| `BAD_CONFIG` | The config file exists but is wrong |
| `PANEL_NOT_CONNECTED` | No panel, or one whose `hello` never validated (usually an unreloaded build) |
| `TIMEOUT` | No result in time — **almost always a modal dialog waiting in Premiere** |
| `NO_PROJECT` / `NO_SEQUENCE` | Nothing open / no active sequence |
| `ITEM_NOT_FOUND` / `CLIP_NOT_FOUND` | Bad project-item name/id, or a stale `v0:2` ref |
| `EFFECT_NOT_FOUND` / `TRANSITION_NOT_FOUND` | Match name not on this install — the message names the nearest three |
| `PARAM_NOT_FOUND` | No such param index or name, or an ambiguous name |
| `TRANSACTION_FAILED` | `executeTransaction` returned false |
| `IMPORT_FAILED` / `EXPORT_FAILED` | Premiere refused, usually a path or codec |
| `INVALID_ARGS` | Bad arguments — **or a stale panel**, which answers this to commands it should know |
| `EVAL_ERROR` | A `premiere_eval` snippet threw; the stack is in `detail` |
| `PANEL_ERROR` | Anything unexpected inside the panel |

⚠️ **A zod schema violation does NOT arrive in this shape.** It is rejected by the MCP layer before
the tool handler runs, so it comes back as `MCP error -32602: Input validation error: …`. Anything
parsing tool results must handle both forms.

## Conventions across the boundary

- **Times are seconds (number) at the tool boundary.** The panel converts with
  `ppro.TickTime.createWithSeconds(s)` and reports back via `tickTime.seconds`. There are
  **254,016,000,000 ticks per second**; a sequence's `timebase` is ticks per *frame*, so
  `frameRate = 254_016_000_000 / timebase`.
- **Track indices are the API's 0-based ones.** `SequenceState` carries the UI label (`V1`, `A2`)
  alongside, so nobody has to convert in their head.
- **The panel sees Windows paths exclusively.** Translation happens in `paths.ts` at the server
  boundary and nowhere else. 🔴 Premiere reports **extended-length paths** (`\\?\D:\…`), which
  `stripExtendedPrefix()` removes before anything else looks at the string.
- **Every mutation is one `executeTransaction`**, labelled `BadCode: <tool>` so it reads well in
  Edit ▸ Undo. Two documented exceptions: `apply_effect` is unavoidably two transactions (params
  cannot be addressed until the append commits), and neither export is an Action at all.

## Changing the protocol

`protocol.ts` is imported by both the server and the panel, so a change lands in both — **but the
panel does not reload itself.** After any panel change, someone must press **⋯ → Load** in UXP
Developer Tool. Bump `protocol` in `Hello` if the change is breaking; the bridge rejects a hello it
does not understand and says the build is stale, which is the behaviour you want.
