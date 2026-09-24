import { connect, listTakes } from '/home/jackt/projects/badcode/badcode/scripts/suno/suno.mts'
const { page } = await connect()
const seen = new Map<string, { title: string; dur: string | null }>()
for (let i = 0; i < 25; i++) {
  for (const t of await listTakes(page, 'camping-r7')) if (t.songId) seen.set(t.songId, { title: t.title, dur: t.dur })
  await page.evaluate((n) => {
    const els = [...document.querySelectorAll('*')] as HTMLElement[]
    const sc = els.filter((e) => e.scrollHeight > e.clientHeight + 200 && e.clientHeight > 300)
    for (const e of sc) e.scrollTop = Math.min(e.scrollTop + 600 * 1, e.scrollHeight)
  }, i)
  await new Promise((r) => setTimeout(r, 450))
}
const rows = [...seen.entries()].map(([id, v]) => ({ id, ...v })).sort((a, b) => a.title.localeCompare(b.title))
for (const r of rows) console.log(r.title, r.dur ?? '-', r.id)
console.log('count', rows.length)
process.exit(0)
