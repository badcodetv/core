/**
 * Fill Suno's "Edit vocals" (add vocals over an uploaded instrumental) form from a clean-room writer file, read it
 * back, and Create. The instrumental must already be attached with mode "Edit vocals" (+ Audio ▸ Upload, then the
 * mode menu on the Audio card ▸ Edit vocals). Built 2026-11-06 for the Camping new-lyrics experiment.
 *
 *   npx tsx scripts/suno/add-vocals.mts <writer.md> <title> [--yes]     (FLOW_CDP_PORT, default 9222)
 *
 * Writer file format: === TITLE / STYLE / EXCLUDE / SLIDERS (audio_strength= weirdness= style_influence= [variety=]) / LYRICS / WHY ===
 * Without --yes it fills and reads back only. Never Cover (Jack 2026-10-22).
 */
import { chromium, type Page } from 'playwright'
import { readFileSync } from 'node:fs'

const [file, title] = process.argv.slice(2)
const yes = process.argv.includes('--yes')
const src = readFileSync(file, 'utf8')
const box = (name: string) => (new RegExp(`=== ${name} ===\\n([\\s\\S]*?)\\n(?:=== |$)`).exec(src)?.[1] ?? '').trim()
const style = box('STYLE'), exclude = box('EXCLUDE'), lyrics = box('LYRICS')
const sl = Object.fromEntries([...box('SLIDERS').matchAll(/(\w+)=(\d+)/g)].map(m => [m[1], Number(m[2])]))
if (!style || !lyrics || sl.audio_strength === undefined) throw new Error('writer file is missing STYLE, LYRICS or audio_strength')

const b = await chromium.connectOverCDP(`http://localhost:${process.env.FLOW_CDP_PORT ?? 9222}`)
const page = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const mode = await page.locator('button:has-text("Edit vocals")').count()
if (!mode) throw new Error('the Audio card is not in "Edit vocals" mode — refusing (it would be a Cover)')

async function setSlider(p: Page, label: string, target: number) {
  const s = p.locator(`[role="slider"][aria-label="${label}"]`).first()
  if (!(await s.count())) return `${label}=absent`
  await s.focus()
  const read = async () => Number(await s.getAttribute('aria-valuenow'))
  let cur = await read(), guard = 0
  while (cur !== target && guard++ < 200) {
    await p.keyboard.press(cur < target ? 'ArrowRight' : 'ArrowLeft')
    let next = await read()
    if (next === cur) { await p.waitForTimeout(250); await s.focus(); await p.keyboard.press(cur < target ? 'ArrowRight' : 'ArrowLeft'); next = await read() }
    if (next === cur) break
    if (Math.abs(next - target) >= Math.abs(cur - target)) break
    cur = next
  }
  return `${label}=${await read()}`
}
async function fillChecked(p: Page, sel: string, text: string) {
  const el = p.locator(sel).first()
  for (let i = 0; i < 4; i++) {
    await el.fill(''); await el.fill(text); await el.blur().catch(() => {}); await p.waitForTimeout(250)
    if ((await el.inputValue()).length === text.length) return 'ok'
  }
  return 'MISMATCH'
}

// Lyrics: Lexical editor, line by line (fill() puts everything in one <p>).
const lyr = page.locator('[aria-label="Lyrics editor"]')
await lyr.evaluate((el: HTMLElement) => { el.scrollIntoView({ block: 'center' }); el.click(); el.focus() })
await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Delete')
const lines = lyrics.split('\n')
for (let i = 0; i < lines.length; i++) { await page.keyboard.insertText(lines[i]); if (i < lines.length - 1) await page.keyboard.press('Enter') }
await page.waitForTimeout(400)
const out: Record<string, string> = {}
out.style = await fillChecked(page, 'textarea[aria-label="Styles"]', style)
if (!(await page.locator('input[placeholder="Exclude styles"]').count())) await page.getByText('More Options', { exact: true }).first().click()
out.exclude = await fillChecked(page, 'input[placeholder="Exclude styles"]', exclude)
out.w = await setSlider(page, 'Weirdness', sl.weirdness)
out.s = await setSlider(page, 'Style Influence', sl.style_influence)
out.a = await setSlider(page, 'Audio Influence', sl.audio_strength)
// Variety (0/1/2; 0 = Suno keeps the style words as written). Added 2026-11-06 for the pace round.
if (sl.variety !== undefined) out.v = await setSlider(page, 'Variety', sl.variety)
const t = page.locator('input[placeholder="Song Title (Optional)"]').first()
await t.fill(title); await t.blur()
// read back
const got = await page.evaluate(() => [...document.querySelectorAll('[aria-label="Lyrics editor"] p')].map(p => (p as HTMLElement).innerText).join('\n'))
const norm = (x: string) => x.split('\n').map(l => l.trim()).filter(Boolean).join('\n')
out.lyrics = norm(got) === norm(lyrics) ? `ok (${lines.length} lines)` : `MISMATCH (${got.split('\n').length} vs ${lines.length} lines)`
out.title = await t.inputValue()
out.workspace = (await page.locator('text=Save to').count()) ? (await page.evaluate(() => { const e = [...document.querySelectorAll('*')].find(x => x.textContent?.trim() === 'Save to...'); return e?.parentElement?.parentElement?.textContent?.replace('Save to...', '').trim() ?? '?' })) : '?'
console.log(JSON.stringify(out))
if (/MISMATCH/.test(JSON.stringify(out))) { console.log('not creating: read-back mismatch'); process.exit(1) }
if (!yes) process.exit(0)
const clicked = await page.evaluate(() => { const x = [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-label') === 'Create song') as HTMLButtonElement | undefined; if (!x) return 'no-button'; if (x.disabled) return 'disabled'; x.scrollIntoView({ block: 'center' }); x.click(); return 'clicked' })
console.log('create:', clicked)
await page.waitForTimeout(5000)
process.exit(0)
