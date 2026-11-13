// Drive Suno's Sounds tab: one sound per call (Create gives two takes).
//
//   node scripts/suno/sounds.mjs <spec.json> [--yes]
//
// spec.json: {"prompt": "...", "type": "One-Shot"|"Loop", "bpm": null|<number>, "workspace": "<workspace name>"}
// Without --yes it fills the form, reads every field back and stops (nothing spent). With --yes it clicks Create
// once and prints the two newest clips in the workspace list (id, title, length) a little later.
// Built 2026-11-13 for Priority Lane (Jack: "suno for it all"). Live DOM, 2026-11-13: tabs Songs/Speech/Sounds; a
// textarea labelled "Sound"; Type buttons One-Shot/Loop; an input labelled "BPM" (placeholder Auto; it can hold a
// stale value from an earlier run, so it is always set or cleared); a Key button ("Any"); Create = aria-label
// "Create song". The form is shared and persistent (docs/suno-gpt/automation.md), so every field is set, then read back.
import { readFileSync } from 'node:fs'
import { chromium } from 'playwright'

const [specPath, flag] = process.argv.slice(2)
const spec = JSON.parse(readFileSync(specPath, 'utf8'))
const b = await chromium.connectOverCDP(process.env.SUNO_CDP_ENDPOINT || 'http://localhost:9222')
const p = b.contexts().flatMap((c) => c.pages()).find((x) => x.url().includes('suno.com/create'))
if (!p) throw new Error('no suno.com/create tab: run `npx tsx scripts/suno/suno.mts open-tab` first')
const fail = (m) => { console.error('🔴 ' + m); process.exit(1) }
try {
  await p.getByRole('tab', { name: 'Sounds', exact: true }).click()
  await p.waitForTimeout(800)
  if (spec.workspace) {
    const ws = p.locator('button[aria-pressed="true"]').filter({ hasText: new RegExp(`^${spec.workspace}$`) })
    if (!(await ws.count())) fail(`workspace "${spec.workspace}" is not the selected one: select it in Suno first`)
  }
  const box = p.getByRole('textbox', { name: 'Sound', exact: true })
  await box.fill(spec.prompt)
  const type = spec.type || 'One-Shot'
  await p.locator('button').filter({ hasText: new RegExp(`^${type}$`) }).first().click()
  const bpm = p.getByRole('textbox', { name: 'BPM' }).or(p.locator('input[aria-label="BPM"]')).first()
  await bpm.fill(spec.bpm ? String(spec.bpm) : '')
  await bpm.press('Tab')
  await p.waitForTimeout(400)
  const got = { prompt: await box.inputValue(), bpm: await bpm.inputValue() }
  if (got.prompt !== spec.prompt) fail(`prompt did not stick: ${JSON.stringify(got.prompt).slice(0, 80)}`)
  console.log(`✅ form: type=${type} bpm=${got.bpm || 'Auto'} prompt=${spec.prompt.length} chars`)
  if (flag !== '--yes') { console.log('dry run: nothing created (add --yes)') } else {
  const before = await p.locator('a[href^="/song/"]').evaluateAll((as) => as.map((a) => a.getAttribute('href')))
  await p.getByRole('button', { name: 'Create song' }).click()
  let found = false
  for (let i = 0; i < 40; i++) {
    await p.waitForTimeout(3000)
    const now = await p.locator('a[href^="/song/"]').evaluateAll((as) => [...new Set(as.map((a) => a.getAttribute('href')))])
    const fresh = now.filter((h) => !before.includes(h))
    if (fresh.length >= 2) { console.log(JSON.stringify({ created: fresh.slice(0, 2).map((h) => 'https://suno.com' + h) })); found = true; break }
  }
  if (!found) { console.error('🔴 no two new clips appeared in 2 minutes: check the workspace list (they may still have been made)'); process.exitCode = 1 }
  }
} finally {
  // Leave the form on Songs: suno.mts refuses a form left in SOUNDS mode (2026-11-13, it stopped a whole round).
  await p.getByRole('tab', { name: 'Songs', exact: true }).click().catch(() => {})
  process.exit(process.exitCode ?? 0)  // the CDP connection would otherwise keep node alive for ever
}
