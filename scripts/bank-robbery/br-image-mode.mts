// Scratch: put the open Flow project's composer into image mode (model, 16:9, x1), and optionally upload reference files first.
// usage: npx tsx br-image-mode.mts "<model>" [file ...]
import { FlowClient } from '../../packages/flow-mcp/src/flow-client.ts'
const [model, ...files] = process.argv.slice(2)
const c: any = await FlowClient.connect()
try {
  await c.reloadProject(); await c.ensureAgentOff()
  for (const f of files) { await c.uploadToProject(f); for (let i = 0; i < 8; i++) { await c.page.waitForTimeout(500); const ok = await c.page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'I agree') as HTMLElement | undefined; b?.click(); return !!b }); if (ok) break } console.log('uploaded', f) }
  await c.ensureImageModeRebuilt(1, model, '16:9')
  await c.page.waitForTimeout(1000)
  await c.page.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/c92745b4-e5c8-4867-9e34-186a0e7ea281/scratchpad/bar.png' })
  console.log('image mode set:', model)
} catch (e: any) { console.log('ERROR', String(e?.message ?? e).split('\n').slice(0, 3).join(' | ')); process.exitCode = 1 }
finally { await c.browser.close().catch(() => {}) }
