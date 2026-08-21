import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest'
import { WebSocket } from 'ws'
import { Bridge } from './bridge'
import type { Hello } from './protocol'

// A real `ws` client stands in for the UXP panel — the panel is also just a WebSocket client
// dialling in (Decision 1: a UXP plugin cannot listen). Each test gets a fresh port to avoid
// EADDRINUSE across the suite.
let port: number
let bridge: Bridge | null = null
let sockets: WebSocket[] = []

beforeEach(() => {
  port = 21000 + Math.floor(Math.random() * 20000)
})

afterEach(async () => {
  for (const s of sockets) s.close()
  sockets = []
  await bridge?.close()
  bridge = null
})

async function startBridge(opts?: Partial<{ connectWaitMs: number; defaultTimeoutMs: number }>): Promise<Bridge> {
  bridge = new Bridge({ port, bind: 'local', ...opts })
  await bridge.listen()
  return bridge
}

function connectPanel(opts?: { sendHello?: boolean }): Promise<WebSocket> {
  const sendHello = opts?.sendHello ?? true
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(`ws://127.0.0.1:${port}`)
    sockets.push(ws)
    ws.once('open', () => {
      if (sendHello) {
        const hello: Hello = { type: 'hello', appVersion: '26.3.2', panelVersion: '0.1.0', protocol: 1 }
        ws.send(JSON.stringify(hello))
      }
      resolve(ws)
    })
    ws.once('error', reject)
  })
}

/** Bridge exposes no connect event, so tests poll the public `connected` getter — the same
 * thing a caller would have to do if they cared before their first `send()`. */
function waitForConnected(b: Bridge, timeoutMs = 1000): Promise<void> {
  return new Promise((resolve, reject) => {
    const start = Date.now()
    const check = (): void => {
      if (b.connected) return resolve()
      if (Date.now() - start > timeoutMs) return reject(new Error('timed out waiting for bridge.connected'))
      setTimeout(check, 5)
    }
    check()
  })
}

function wait(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

describe('hello handshake', () => {
  it('marks connected and records hello once the panel sends its hello frame', async () => {
    const b = await startBridge()
    await connectPanel()
    await waitForConnected(b)
    expect(b.connected).toBe(true)
    expect(b.hello).toEqual({ type: 'hello', appVersion: '26.3.2', panelVersion: '0.1.0', protocol: 1 })
  })

  it('is not connected before any panel has said hello', async () => {
    const b = await startBridge()
    expect(b.connected).toBe(false)
    expect(b.hello).toBeNull()
    await connectPanel({ sendHello: false })
    await wait(30)
    expect(b.connected).toBe(false)
  })
})

describe('send() connect-wait', () => {
  it('waits connectWaitMs for a panel, then rejects PANEL_NOT_CONNECTED', async () => {
    const b = await startBridge({ connectWaitMs: 60 })
    const start = Date.now()
    await expect(b.send('ping', {})).rejects.toMatchObject({ code: 'PANEL_NOT_CONNECTED' })
    expect(Date.now() - start).toBeGreaterThanOrEqual(50)
  })

  // Found live on 2026-08-21: after the panel was rebuilt for T5, the OLD spike panel was still
  // loaded in Premiere. It connected happily, its pre-T5 hello failed validation, and the caller
  // got a bare "No panel connected" — which sends you hunting a networking fault that isn't
  // there. A socket with no completed handshake must name the real fix.
  it('distinguishes a stale panel (connected, bad hello) from no panel at all', async () => {
    const b = await startBridge({ connectWaitMs: 120 })
    const ws = await connectPanel({ sendHello: false })
    ws.send(JSON.stringify({ type: 'hello', protocol: 1, panelVersion: '0.1.0-spike' })) // no appVersion
    await wait(30)

    await expect(b.send('ping', {})).rejects.toMatchObject({
      code: 'PANEL_NOT_CONNECTED',
      message: expect.stringContaining('older build'),
    })
    expect(b.connected).toBe(false)
  })

  it('succeeds once a panel connects within the wait window', async () => {
    const b = await startBridge({ connectWaitMs: 500 })
    const ws = await connectPanel()
    ws.on('message', (data) => {
      const frame = JSON.parse(data.toString())
      ws.send(JSON.stringify({ type: 'result', id: frame.id, ok: true, result: { appVersion: '26.3.2' } }))
    })
    await expect(b.send('ping', {})).resolves.toEqual({ appVersion: '26.3.2' })
  })
})

describe('serial FIFO queue', () => {
  it('delivers two concurrent send()s strictly one after another', async () => {
    const b = await startBridge()
    const ws = await connectPanel()
    await waitForConnected(b)

    const received: string[] = []
    let requestsInFlightAtFirstReply = 0
    ws.on('message', (data) => {
      const frame = JSON.parse(data.toString())
      received.push(frame.id)
      if (received.length === 1) {
        // If the bridge had already sent the second command by now, `received` would be 2 —
        // proving the queue is NOT serial. Delay the reply to give a non-serial bug time to show.
        setTimeout(() => {
          requestsInFlightAtFirstReply = received.length
          ws.send(JSON.stringify({ type: 'result', id: frame.id, ok: true, result: { appVersion: 'x' } }))
        }, 30)
      } else {
        ws.send(JSON.stringify({ type: 'result', id: frame.id, ok: true, result: { appVersion: 'x' } }))
      }
    })

    const p1 = b.send('ping', {})
    const p2 = b.send('ping', {})
    await Promise.all([p1, p2])

    expect(requestsInFlightAtFirstReply).toBe(1)
    expect(received).toHaveLength(2)
    expect(new Set(received).size).toBe(2) // distinct ids — not a reused/duplicated correlation id
  })

  it('a slow command times out with TIMEOUT and the next queued command still runs', async () => {
    const b = await startBridge({ defaultTimeoutMs: 50 })
    const ws = await connectPanel()
    await waitForConnected(b)

    ws.on('message', (data) => {
      const frame = JSON.parse(data.toString())
      if (frame.cmd === 'eval') return // never respond — simulates a stuck command
      ws.send(JSON.stringify({ type: 'result', id: frame.id, ok: true, result: { appVersion: 'x' } }))
    })

    const slow = b.send('eval', { code: '1' })
    const fast = b.send('ping', {})

    await expect(slow).rejects.toMatchObject({ code: 'TIMEOUT' })
    await expect(fast).resolves.toEqual({ appVersion: 'x' })
  })

  it('honours a per-call timeoutMs override shorter than the default', async () => {
    const b = await startBridge({ defaultTimeoutMs: 5000 })
    const ws = await connectPanel()
    await waitForConnected(b)
    ws.on('message', () => {}) // never respond

    const start = Date.now()
    await expect(b.send('ping', {}, { timeoutMs: 40 })).rejects.toMatchObject({ code: 'TIMEOUT' })
    expect(Date.now() - start).toBeLessThan(1000)
  })
})

describe('disconnect handling', () => {
  it('rejects an in-flight command with PANEL_NOT_CONNECTED when the panel disconnects mid-command', async () => {
    const b = await startBridge()
    const ws = await connectPanel()
    await waitForConnected(b)
    ws.on('message', () => {}) // never respond

    // Attach the rejection assertion in the same tick the promise is created — ws.close()
    // below rejects it from a server-side event that can otherwise race ahead of a `.rejects`
    // attached after an intervening `await`, which Node flags as a (harmless but noisy)
    // "handled asynchronously" unhandled-rejection warning.
    const inFlight = b.send('ping', {})
    const assertion = expect(inFlight).rejects.toMatchObject({ code: 'PANEL_NOT_CONNECTED' })
    await wait(20) // let the cmd frame actually go out before we pull the plug
    ws.close()

    await assertion
    expect(b.connected).toBe(false)
  })

  it('a second panel connecting supersedes the first, closing it with reason "superseded"', async () => {
    const b = await startBridge()
    const first = await connectPanel()
    await waitForConnected(b)

    const closed = new Promise<{ code: number; reason: string }>((resolve) => {
      first.once('close', (code, reasonBuf) => resolve({ code, reason: reasonBuf.toString() }))
    })

    const second = await connectPanel()
    const { reason } = await closed
    expect(reason).toBe('superseded')

    await waitForConnected(b) // the new panel's hello re-establishes connected
    expect(b.hello).not.toBeNull()
    void second
  })

  it('rejects an in-flight command with PANEL_NOT_CONNECTED when its panel is superseded', async () => {
    const b = await startBridge()
    const first = await connectPanel()
    await waitForConnected(b)
    first.on('message', () => {}) // never respond

    const inFlight = b.send('ping', {})
    const assertion = expect(inFlight).rejects.toMatchObject({ code: 'PANEL_NOT_CONNECTED' })
    await wait(20) // let the cmd frame actually go out before superseding

    await connectPanel() // supersedes `first`

    await assertion
  })
})

describe('malformed frames', () => {
  it('logs and ignores an unparseable frame without disrupting later commands', async () => {
    const spy = vi.spyOn(console, 'error').mockImplementation(() => {})
    try {
      const b = await startBridge()
      const ws = await connectPanel()
      await waitForConnected(b)

      ws.on('message', (data) => {
        const frame = JSON.parse(data.toString())
        ws.send(JSON.stringify({ type: 'result', id: frame.id, ok: true, result: { appVersion: 'x' } }))
      })

      ws.send('not json at all')

      await expect(b.send('ping', {})).resolves.toEqual({ appVersion: 'x' })
      expect(spy).toHaveBeenCalled()
    } finally {
      spy.mockRestore()
    }
  })

  it('logs and ignores a well-formed-JSON frame that matches no known shape', async () => {
    const spy = vi.spyOn(console, 'error').mockImplementation(() => {})
    try {
      const b = await startBridge()
      const ws = await connectPanel()
      await waitForConnected(b)

      ws.on('message', (data) => {
        const frame = JSON.parse(data.toString())
        ws.send(JSON.stringify({ type: 'result', id: frame.id, ok: true, result: { appVersion: 'x' } }))
      })

      ws.send(JSON.stringify({ type: 'mystery', foo: 'bar' }))

      await expect(b.send('ping', {})).resolves.toEqual({ appVersion: 'x' })
      expect(spy).toHaveBeenCalled()
    } finally {
      spy.mockRestore()
    }
  })
})

describe('log frames', () => {
  it('forwards a panel log frame to stderr', async () => {
    const spy = vi.spyOn(console, 'error').mockImplementation(() => {})
    try {
      const b = await startBridge()
      const ws = await connectPanel()
      await waitForConnected(b)

      ws.send(JSON.stringify({ type: 'log', level: 'warn', message: 'heads up' }))
      await wait(20)

      expect(spy).toHaveBeenCalledWith(expect.stringContaining('heads up'))
    } finally {
      spy.mockRestore()
    }
  })
})

describe('result correlation', () => {
  it('ignores a result whose id does not match the command in flight', async () => {
    const b = await startBridge()
    const ws = await connectPanel()
    await waitForConnected(b)

    ws.on('message', (data) => {
      const frame = JSON.parse(data.toString())
      // Reply with a stale id first, then the real one.
      ws.send(JSON.stringify({ type: 'result', id: 'not-the-real-id', ok: true, result: { appVersion: 'wrong' } }))
      ws.send(JSON.stringify({ type: 'result', id: frame.id, ok: true, result: { appVersion: 'right' } }))
    })

    await expect(b.send('ping', {})).resolves.toEqual({ appVersion: 'right' })
  })
})
