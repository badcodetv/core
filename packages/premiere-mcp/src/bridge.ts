/**
 * The WS server the UXP panel dials into (a UXP plugin can only dial OUT — Decision 1 in the
 * plan). Strictly serial: one panel connection, one in-flight command at a time, the same law
 * as Flow's one browser (Decision 6). Every `send()` is a FIFO queue entry; the queue drains
 * one command at a time regardless of how many callers are waiting.
 */
import { WebSocketServer, type WebSocket } from 'ws'
import {
  IncomingFrameSchema,
  type CmdArgs,
  type CmdName,
  type CmdResult,
  type ErrorCode,
  type Hello,
} from './protocol'

const DEFAULT_CONNECT_WAIT_MS = 5000
const DEFAULT_TIMEOUT_MS = 30000
const SUPERSEDED_CLOSE_CODE = 4000

function isPlainObject(v: unknown): v is Record<string, unknown> {
  return typeof v === 'object' && v !== null && !Array.isArray(v)
}

export class BridgeError extends Error {
  constructor(public code: ErrorCode, message: string, public detail?: unknown) {
    super(message)
    this.name = 'BridgeError'
  }
}

interface QueueTask {
  cmd: CmdName
  args: unknown
  timeoutMs: number
  resolve: (v: unknown) => void
  reject: (err: BridgeError) => void
}

interface PendingResult {
  id: string
  timer: ReturnType<typeof setTimeout>
  resolve: (v: unknown) => void
  reject: (err: BridgeError) => void
}

export class Bridge {
  private readonly port: number
  private readonly bind: 'local' | 'all'
  private readonly connectWaitMs: number
  private readonly defaultTimeoutMs: number

  private wss: WebSocketServer | null = null
  private socket: WebSocket | null = null
  private _hello: Hello | null = null

  private readonly queue: QueueTask[] = []
  private pumping = false
  private connectWaiters: (() => void)[] = []
  private pendingResult: PendingResult | null = null
  private seq = 0

  constructor(opts: { port: number; bind: 'local' | 'all'; connectWaitMs?: number; defaultTimeoutMs?: number }) {
    this.port = opts.port
    this.bind = opts.bind
    this.connectWaitMs = opts.connectWaitMs ?? DEFAULT_CONNECT_WAIT_MS
    this.defaultTimeoutMs = opts.defaultTimeoutMs ?? DEFAULT_TIMEOUT_MS
  }

  get connected(): boolean {
    return this.socket !== null && this._hello !== null
  }

  get hello(): Hello | null {
    return this._hello
  }

  listen(): Promise<void> {
    return new Promise((resolve, reject) => {
      const host = this.bind === 'all' ? '0.0.0.0' : '127.0.0.1'
      const wss = new WebSocketServer({ host, port: this.port })
      wss.once('listening', () => resolve())
      wss.once('error', reject)
      wss.on('connection', (ws) => this.onConnection(ws))
      this.wss = wss
    })
  }

  close(): Promise<void> {
    return new Promise((resolve) => {
      this.socket?.close()
      this.socket = null
      this._hello = null
      if (!this.wss) {
        resolve()
        return
      }
      this.wss.close(() => resolve())
    })
  }

  /** Serial FIFO: queues the command and returns a promise settled once it is this command's
   * turn AND a result (or timeout, or disconnect) has come back. */
  send<C extends CmdName>(cmd: C, args: CmdArgs[C], opts?: { timeoutMs?: number }): Promise<CmdResult[C]> {
    return new Promise((resolve, reject) => {
      const task: QueueTask = {
        cmd,
        args,
        timeoutMs: opts?.timeoutMs ?? this.defaultTimeoutMs,
        resolve: resolve as (v: unknown) => void,
        reject,
      }
      this.queue.push(task)
      void this.pump()
    })
  }

  private onConnection(ws: WebSocket): void {
    // A second panel connecting supersedes the first (Decision 6). Fail anything in flight on
    // the old socket NOW rather than relying on its 'close' event — once `this.socket` has
    // moved on to the new connection, onClose() would see a stale `ws` and ignore it.
    if (this.socket) {
      this.socket.close(SUPERSEDED_CLOSE_CODE, 'superseded')
      this.failPending(new BridgeError('PANEL_NOT_CONNECTED', 'Panel disconnected mid-command.'))
    }

    this.socket = ws
    this._hello = null

    ws.on('message', (data) => this.onMessage(ws, data.toString()))
    ws.on('close', () => this.onClose(ws))
    ws.on('error', () => {
      // Swallow — the socket's 'close' event (which always follows) is what settles state.
    })
  }

  private onClose(ws: WebSocket): void {
    if (this.socket !== ws) return // a stale/superseded socket closing — already handled in onConnection()
    this.socket = null
    this._hello = null
    this.failPending(new BridgeError('PANEL_NOT_CONNECTED', 'Panel disconnected mid-command.'))
  }

  private failPending(err: BridgeError): void {
    const pending = this.pendingResult
    if (!pending) return
    this.pendingResult = null
    clearTimeout(pending.timer)
    pending.reject(err)
  }

  private onMessage(ws: WebSocket, text: string): void {
    let raw: unknown
    try {
      raw = JSON.parse(text)
    } catch {
      console.error('[premiere-mcp] malformed frame (not JSON), ignored:', text.slice(0, 200))
      return
    }

    const frame = IncomingFrameSchema.safeParse(raw)
    if (!frame.success) {
      // A rejected `hello` is the signature of a panel built against an older protocol. Say so,
      // because "malformed frame" sends you looking for a networking problem that isn't there.
      if (isPlainObject(raw) && raw.type === 'hello') {
        console.error(
          '[premiere-mcp] a panel connected but its hello was rejected — it is an older build. ' +
            'Rebuild the panel and press ⋯ → Load in UXP Developer Tool. Frame:',
          text.slice(0, 200)
        )
      } else {
        console.error('[premiere-mcp] malformed frame, ignored:', text.slice(0, 200))
      }
      return
    }
    const f = frame.data

    if (f.type === 'hello') {
      if (this.socket !== ws) return // hello from a socket we've already superseded
      this._hello = f
      this.notifyConnected()
      return
    }

    if (f.type === 'log') {
      console.error(`[panel ${f.level}] ${f.message}`)
      return
    }

    // result — settle only if it matches the command currently in flight.
    const pending = this.pendingResult
    if (!pending || pending.id !== f.id) return
    this.pendingResult = null
    clearTimeout(pending.timer)
    if (f.ok) pending.resolve(f.result)
    else pending.reject(new BridgeError(f.code, f.message, f.detail))
  }

  private notifyConnected(): void {
    const waiters = this.connectWaiters
    this.connectWaiters = []
    for (const w of waiters) w()
  }

  /** Resolves true once a panel is connected, false if `ms` elapses first. */
  private waitForConnection(ms: number): Promise<boolean> {
    if (this.connected) return Promise.resolve(true)
    return new Promise((resolve) => {
      const onConnect = (): void => {
        clearTimeout(timer)
        resolve(true)
      }
      const timer = setTimeout(() => {
        this.connectWaiters = this.connectWaiters.filter((w) => w !== onConnect)
        resolve(false)
      }, ms)
      this.connectWaiters.push(onConnect)
    })
  }

  private async pump(): Promise<void> {
    if (this.pumping) return
    this.pumping = true
    try {
      while (this.queue.length > 0) {
        const task = this.queue.shift()!
        await this.run(task)
      }
    } finally {
      this.pumping = false
    }
  }

  private async run(task: QueueTask): Promise<void> {
    if (!this.connected) {
      const gotConnection = await this.waitForConnection(this.connectWaitMs)
      if (!gotConnection) {
        // A socket with no completed handshake is a panel that IS running, just not this
        // version of it — a very different fix from "open the panel".
        task.reject(
          this.socket
            ? new BridgeError(
                'PANEL_NOT_CONNECTED',
                'A panel is attached but never completed the handshake — it is almost certainly an older build. ' +
                  'Rebuild it (npm run build:panel) and press ⋯ → Load in UXP Developer Tool.'
              )
            : new BridgeError('PANEL_NOT_CONNECTED', 'No panel connected.')
        )
        return
      }
    }

    const socket = this.socket
    if (!socket) {
      // Connected briefly, then dropped before this task could send — treat like any other
      // disconnect; the next queued task gets its own fresh connect-wait.
      task.reject(new BridgeError('PANEL_NOT_CONNECTED', 'Panel disconnected before the command could be sent.'))
      return
    }

    const id = `c${++this.seq}`
    await new Promise<void>((settle) => {
      const timer = setTimeout(() => {
        this.pendingResult = null
        task.reject(new BridgeError('TIMEOUT', `Command "${task.cmd}" timed out after ${task.timeoutMs}ms.`))
        settle()
      }, task.timeoutMs)

      this.pendingResult = {
        id,
        timer,
        resolve: (v) => {
          task.resolve(v)
          settle()
        },
        reject: (e) => {
          task.reject(e)
          settle()
        },
      }

      socket.send(JSON.stringify({ type: 'cmd', id, cmd: task.cmd, args: task.args }))
    })
  }
}
