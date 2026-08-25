/**
 * T5's check: is the panel alive, and does it answer?
 *
 *   npx tsx packages/premiere-mcp/src/smoke-status.ts
 *
 * Brings up the bridge, waits for the panel to dial in, sends `ping`, prints what came back.
 * Nothing else may be holding the port — stop any other bridge server first.
 */
import { Bridge, BridgeError } from './bridge'
import { ConfigError, loadConfig } from './config'

const WAIT_MS = Number(process.env.SMOKE_WAIT_MS ?? 20_000)

async function main(): Promise<void> {
  let port = 7890
  let bind: 'local' | 'all' = 'local'
  try {
    const cfg = loadConfig(process.cwd())
    port = cfg.premiere.port
    bind = cfg.premiere.bind
    console.log(`config: mediaRoot=${cfg.mediaRoot} port=${port} bind=${bind}`)
  } catch (err) {
    if (!(err instanceof ConfigError)) throw err
    console.log(`config: ${err.code} — falling back to port ${port}. ${err.hint ?? ''}`)
  }

  const bridge = new Bridge({ port, bind, connectWaitMs: WAIT_MS, defaultTimeoutMs: 15_000 })
  await bridge.listen()
  console.log(`listening on ws://${bind === 'all' ? '0.0.0.0' : '127.0.0.1'}:${port} — waiting up to ${WAIT_MS}ms for the panel …`)

  try {
    const started = Date.now()
    const result = await bridge.send('ping', {})
    const elapsed = Date.now() - started
    console.log(`\n✅ ping (${elapsed}ms):`, JSON.stringify(result, null, 2))
    console.log('   hello:', JSON.stringify(bridge.hello))
    if (elapsed > 1000) console.log(`   ⚠️  slower than T5's 1s acceptance criterion (${elapsed}ms)`)

    // Round two: an unregistered command must come back as INVALID_ARGS rather than hanging.
    try {
      await bridge.send('list_effects', {})
      console.log('\n⚠️  list_effects answered — the panel has more commands than T5 registers.')
    } catch (err) {
      if (err instanceof BridgeError && err.code === 'INVALID_ARGS') {
        console.log(`\n✅ unknown command → INVALID_ARGS: ${err.message}`)
      } else {
        console.log('\n❌ unknown command gave the wrong error:', err)
        process.exitCode = 1
      }
    }
  } catch (err) {
    console.error('\n❌ ping failed:', err instanceof BridgeError ? `${err.code}: ${err.message}` : err)
    if (err instanceof BridgeError && err.code === 'PANEL_NOT_CONNECTED') {
      console.error('   Is the panel open? Premiere ▸ Window ▸ Extensions (UXP) ▸ BadCode Bridge.')
      console.error('   Rebuilt the panel recently? Press ⋯ → Load in UXP Developer Tool.')
    }
    process.exitCode = 1
  } finally {
    await bridge.close()
  }
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
