// Scratch: make one ordinary still on the working browser (port 9222), which also puts Flow's bar back in image mode after a video run.
import { FlowClient } from '../../../packages/flow-mcp/src/flow-client.ts'
import { readFileSync } from 'node:fs'
const [pf, out] = process.argv.slice(2)
const c: any = await FlowClient.connect()
try {
  await c.page.goto('https://flow.google.com/project/63d22c4b-4bb8-46c6-81a1-ac598fc01030'); await c.page.waitForTimeout(6000)
  const r = await c.generateImage(readFileSync(pf, 'utf8').trim(), out, { model: 'Nano Banana 2', aspect: '16:9', numOutputs: 1 })
  console.log(JSON.stringify(r))
} catch (e: any) { console.log('ERROR', String(e?.message ?? e).split('\n')[0]); process.exitCode = 1 } finally { await c.browser.close().catch(() => {}) }
