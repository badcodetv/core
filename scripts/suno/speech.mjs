// Drive Suno's Speech (beta) tab: one voice-only take per call (Background music OFF).
//
//   node scripts/suno/speech.mjs <spec.json> [--yes]
//
// spec.json: {"script": "...", "tone": "...", "gender": "Male"|"Female", "workspaceId": "<wid uuid>"}
// Without --yes it fills the form, asserts it and stops (nothing spent). With --yes it clicks Create once.
// Built 2026-11-13 for Priority Lane (Jack: "a speech only tool on suno … then we add the sound effects
// and music after"). The song form's traps apply here too (docs/suno-gpt/automation.md): the form is
// shared and persistent, so every field is set and read back before Create. Variety is left as the
// form has it (Normal); the slider is not driven yet. Speech has no title box: takes get Suno's titles,
// so the caller identifies them by order in the workspace list right after Create.
import { chromium } from 'playwright'
import { readFileSync } from 'node:fs'

const [specPath, flag] = process.argv.slice(2)
const spec = JSON.parse(readFileSync(specPath, 'utf8'))
const b = await chromium.connectOverCDP(process.env.SUNO_CDP_ENDPOINT || 'http://localhost:9222')
const p = b.contexts().flatMap((c) => c.pages()).find((x) => x.url().includes('suno.com/create'))
if (!p) throw new Error('no suno.com/create tab: run `npx tsx scripts/suno/suno.mts open-tab` first')
const out = []
try {
  if (spec.workspaceId && !p.url().includes(spec.workspaceId)) {
    throw new Error(`workspace: the tab is on ${p.url()}, wanted wid=${spec.workspaceId}`)
  }
  await p.getByText('Speech', { exact: true }).first().click()
  await p.waitForTimeout(800)
  const adv = p.getByText('Advanced', { exact: true }).first()
  if (await adv.count()) await adv.click()
  const script = p.getByRole('textbox', { name: 'Script', exact: true })
  const tone = p.getByRole('textbox', { name: 'Tone', exact: true })
  await script.fill(spec.script)
  await tone.fill(spec.tone)
  // The live toggles are the buttons that carry aria-pressed; they toggle, so click only when not already on.
  const toggle = async (name) => {
    const btn = p.locator('button[aria-pressed]').filter({ hasText: new RegExp(`^${name}$`) }).last()
    if ((await btn.getAttribute('aria-pressed')) !== 'true') await btn.click()
    await p.waitForTimeout(300)
    return btn.getAttribute('aria-pressed')
  }
  const g = await toggle(spec.gender)
  const m = await toggle('Off')
  out.push(`gender:${spec.gender}=${g}`, `music-off=${m}`)
  if (g !== 'true' || m !== 'true') throw new Error('gender or background-music toggle did not stick; not creating')
  // read back
  const s = await script.inputValue(), t = await tone.inputValue()
  out.push(`script:${s === spec.script ? 'ok' : 'MISMATCH'}`, `tone:${t === spec.tone ? 'ok' : 'MISMATCH'}`)
  const pressed = await p.$$eval('button', (els) =>
    els.filter((e) => ['Male', 'Female', 'Off', 'On'].includes((e.innerText || '').trim()))
      .map((e) => ({ t: e.innerText.trim(), on: e.getAttribute('aria-pressed') ?? e.getAttribute('aria-checked') ?? e.getAttribute('data-state') ?? (e.className.includes('bg-') ? 'cls' : '') })))
  out.push('buttons:' + JSON.stringify(pressed))
  out.push('url:' + p.url())
  if (s !== spec.script || t !== spec.tone) throw new Error('form did not take the text; not creating')
  if (flag === '--yes') {
    await p.getByRole('button', { name: 'Create speech', exact: true }).click()
    await p.waitForTimeout(8000)
    const links = await p.$$eval('a[href*="/song/"]', (as) => [...new Set(as.map((a) => a.getAttribute('href')))].slice(0, 2))
    out.push('CREATED', 'newest:' + JSON.stringify(links))
  } else out.push('dry run: nothing spent')
} finally {
  console.log(out.join('\n'))
  await b.close()
}
