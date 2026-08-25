/**
 * BadCode Bridge — the UXP panel that lets a Claude session in WSL drive Premiere.
 *
 * A UXP plugin cannot listen on a socket, so this side always dials OUT: the WebSocket *server*
 * lives in WSL inside `@badcode/premiere-mcp`, and this panel is its client. That one constraint
 * is why the whole bridge is shaped the way it is.
 *
 * The panel must stay open in Premiere — it is where the code runs. Close it and the session
 * loses Premiere entirely.
 */
import type { Cmd, ErrorCode, Log, Result } from '../../src/protocol'
import { commands, panelCapabilities } from './commands/index'
import { PanelError, appVersion } from './ppro'

const PANEL_VERSION = '0.3.0'
const PROTOCOL = 1 as const
const DEFAULT_URL = 'ws://localhost:7890'
const URL_STORAGE_KEY = 'badcode.bridge.url'
const MAX_BACKOFF_MS = 10_000
const MAX_LOG_LINES = 400

/* ---- UI ------------------------------------------------------------------------------------ */

const logEl = document.getElementById('log') as HTMLElement
const lightEl = document.getElementById('light') as HTMLElement
const stateEl = document.getElementById('state') as HTMLElement
const urlEl = document.getElementById('url') as HTMLInputElement
const connectEl = document.getElementById('connect') as HTMLElement

let logLines: string[] = []

function log(message: string): void {
  const stamp = new Date().toISOString().slice(11, 19)
  logLines.push(`${stamp}  ${message}`)
  if (logLines.length > MAX_LOG_LINES) logLines = logLines.slice(-MAX_LOG_LINES)
  logEl.textContent = logLines.join('\n')
  logEl.scrollTop = logEl.scrollHeight
}

function setConnected(on: boolean, label: string): void {
  if (on) lightEl.classList.add('on')
  else lightEl.classList.remove('on')
  stateEl.textContent = label
  connectEl.textContent = on ? 'Disconnect' : 'Connect'
}

/* ---- remembering the URL ------------------------------------------------------------------- */
/* localStorage is not guaranteed in every UXP host, and a missing one must not stop the panel
 * connecting — fall back to the default silently. */

function readSavedUrl(): string {
  try {
    return localStorage.getItem(URL_STORAGE_KEY) || DEFAULT_URL
  } catch {
    return DEFAULT_URL
  }
}

function saveUrl(url: string): void {
  try {
    localStorage.setItem(URL_STORAGE_KEY, url)
  } catch {
    /* not fatal */
  }
}

/* ---- socket --------------------------------------------------------------------------------- */

let socket: WebSocket | null = null
let reconnectTimer: ReturnType<typeof setTimeout> | null = null
/** Have we EVER completed a connection? Distinguishes "not started yet" from "went away". */
let everConnected = false
/** When the current quiet spell began, so the "this is normal" line is logged once, not hourly. */
let quietSince = 0
let attempt = 0
/** Set when the user pressed Disconnect, so we do not immediately dial back in. */
let stoppedByUser = false

function send(frame: Result | Log | Record<string, unknown>): void {
  if (!socket || socket.readyState !== 1) return
  socket.send(JSON.stringify(frame))
}

function connect(): void {
  const url = (urlEl.value || DEFAULT_URL).trim()
  saveUrl(url)

  if (typeof WebSocket !== 'function') {
    log('FATAL: WebSocket is not available in this runtime.')
    setConnected(false, 'no WebSocket')
    return
  }

  log(`connecting to ${url} …`)
  setConnected(false, 'connecting')

  try {
    socket = new WebSocket(url)
  } catch (err) {
    log(`connect threw: ${String(err)}`)
    log('  → usually a manifest network permission miss. Check requiredPermissions.network.domains.')
    scheduleReconnect()
    return
  }

  socket.onopen = (): void => {
    attempt = 0
    everConnected = true
    quietSince = 0
    setConnected(true, 'connected')
    log(`connected · panel ${PANEL_VERSION} · host ${appVersion()}`)
    send({ type: 'hello', appVersion: appVersion(), panelVersion: PANEL_VERSION, protocol: PROTOCOL })
    send({ type: 'log', level: 'info', message: `panel caps ${JSON.stringify(panelCapabilities())}` })
  }

  socket.onmessage = (event: MessageEvent): void => {
    let frame: Cmd
    try {
      frame = JSON.parse(String(event.data)) as Cmd
    } catch {
      send({ type: 'log', level: 'error', message: 'unparseable frame from server' })
      return
    }
    if (frame && frame.type === 'cmd') void dispatch(frame)
  }

  socket.onerror = (): void => {
    // Deliberately silent. The 'close' that always follows is what drives reconnection and what
    // decides the wording; UXP gives no useful detail here, and a line reading "socket error"
    // every ten seconds while idle is exactly the false alarm this panel should not raise.
  }

  socket.onclose = (event: CloseEvent): void => {
    const wasConnected = everConnected
    socket = null

    // 🔴 A red light here is USUALLY NOT A FAULT, and saying "disconnected" made it read like
    // one. The bridge only exists while the MCP server is running in WSL, so between commands
    // there is genuinely nothing to connect to and the panel sits here retrying. Say that,
    // rather than reporting a close code that sends someone hunting a network problem.
    //
    // A code 1006 with no reason is the ordinary "nothing listening" case. Anything else — a
    // server that accepted us and then hung up — is worth showing in full.
    const ordinary = !event || event.code === 1006 || event.code === 1000
    if (stoppedByUser) {
      setConnected(false, 'stopped')
    } else if (ordinary) {
      setConnected(false, wasConnected ? 'waiting for Claude' : 'waiting for Claude…')
      if (!quietSince) {
        log('no bridge listening — this is normal between commands, the panel keeps retrying')
        quietSince = Date.now()
      }
    } else {
      setConnected(false, `closed (${event.code})`)
      log(`closed code=${event.code} reason=${event.reason || '(none)'}`)
    }
    if (!stoppedByUser) scheduleReconnect()
  }
}

function scheduleReconnect(): void {
  if (reconnectTimer || stoppedByUser) return
  attempt += 1
  const delay = Math.min(1000 * 2 ** (attempt - 1), MAX_BACKOFF_MS)
  // Once we are at the ceiling and quiet, stop narrating it — the state line already says so,
  // and a log that scrolls forever hides the message that actually mattered.
  if (delay < MAX_BACKOFF_MS) log(`reconnecting in ${delay}ms`)
  reconnectTimer = setTimeout(() => {
    reconnectTimer = null
    connect()
  }, delay)
}

function disconnect(): void {
  stoppedByUser = true
  if (reconnectTimer) {
    clearTimeout(reconnectTimer)
    reconnectTimer = null
  }
  socket?.close()
  socket = null
  setConnected(false, 'disconnected (by you)')
}

/* ---- dispatch --------------------------------------------------------------------------------- */

async function dispatch(frame: Cmd): Promise<void> {
  const handler = commands[frame.cmd]
  if (!handler) {
    log(`✗ ${frame.cmd} — not implemented in panel ${PANEL_VERSION}`)
    send({
      type: 'result',
      id: frame.id,
      ok: false,
      code: 'INVALID_ARGS',
      message: `Panel ${PANEL_VERSION} has no handler for "${frame.cmd}". Rebuild the panel and press ⋯ → Load in UXP Developer Tool.`,
    })
    return
  }

  const started = Date.now()
  try {
    const result = await handler((frame.args ?? {}) as Record<string, unknown>)
    log(`✓ ${frame.cmd} (${Date.now() - started}ms)`)
    send({ type: 'result', id: frame.id, ok: true, result: jsonSafe(result) })
  } catch (err) {
    const code: ErrorCode = err instanceof PanelError ? err.code : 'PANEL_ERROR'
    const message = err instanceof Error ? err.message : String(err)
    log(`✗ ${frame.cmd} ${code}: ${message}`)
    send({
      type: 'result',
      id: frame.id,
      ok: false,
      code,
      message,
      detail: err instanceof Error ? err.stack : undefined,
    })
  }
}

/** Results cross the wire as JSON; anything that will not serialise becomes its string form
 * rather than silently arriving as `{}`. */
function jsonSafe(value: unknown): unknown {
  if (value === undefined) return null
  try {
    return JSON.parse(JSON.stringify(value))
  } catch {
    return String(value)
  }
}

/* ---- boot ------------------------------------------------------------------------------------ */

urlEl.value = readSavedUrl()

connectEl.addEventListener('click', () => {
  if (socket && socket.readyState === 1) {
    log('disconnecting by request')
    disconnect()
  } else {
    stoppedByUser = false
    attempt = 0
    if (reconnectTimer) {
      clearTimeout(reconnectTimer)
      reconnectTimer = null
    }
    connect()
  }
})

log(`panel ${PANEL_VERSION} loaded · host ${appVersion()}`)
connect()
