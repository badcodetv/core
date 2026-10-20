/**
 * Probe, no credits: configure the video popover (Omni 1.1 Flash, Frames, 16:9, <dur>s, x<count>) and read
 * Flow's own credit-cost label, plus any credit balance the page shows. Never clicks Create.
 *   FLOW_CDP_PORT=<port> npx tsx scripts/gpom/second-half-video/probe-price.mts [dur] [count]
 */
import { FlowClient } from '../../../packages/flow-mcp/src/flow-client'
const PROJECT = 'be451638-f0ac-4f7e-8185-7b89f3c74f5c'
const dur = Number(process.argv[2] ?? 8), count = Number(process.argv[3] ?? 1)
const c: any = await FlowClient.connect(`http://localhost:${process.env.FLOW_CDP_PORT}`)
const page = c.page
try {
  if (!page.url().includes(PROJECT)) { await page.goto(`https://flow.google.com/project/${PROJECT}`, { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(5000) }
  await c.ensureAgentOff()
  const cfg = { model: 'Omni 1.1 Flash', aspect: '16:9', duration: dur, count, frames: true }
  await c.ensureVideoConfigRebuilt(cfg).catch(async () => { await page.waitForTimeout(1500); await c.ensureVideoConfigRebuilt(cfg) })
  await c.openSettings()
  await page.waitForTimeout(800)
  const cost = await page.evaluate(() => [...document.querySelectorAll('flow-credit-cost-label, .credit-cost-label')].map((e) => (e as HTMLElement).innerText.replace(/\s+/g, ' ').trim()))
  const credits = await page.evaluate(() => (document.body.innerText.match(/[^\n]{0,60}credit[^\n]{0,60}/gi) || []).slice(0, 10))
  await c.closeSettings()
  const label = ((await c.settingsTrigger().textContent()) ?? '').replace(/\s+/g, ' ').trim()
  console.log(JSON.stringify({ label, cost, credits }))
} finally { await c.close?.().catch(() => {}) }
