/**
 * Paraguay short 1: run the sealed prompt writer's stills verbatim in Flow (Nano Banana 2, 9:16, 2 takes).
 * Reporter shots: the presenter pick attached as the one reference (flow editImage). Meme stills: no reference.
 * ONE fresh project per try (a retry in the same project returned a copy of the reference, 2026-11-09).
 * "Unusual activity" caught in ~2 s → real reload → 10 s → retry now (Jack 2026-11-09).
 *   npx tsx docs/stories/magic-money-tree/scenes/paraguay-s1/cleanroom/run_stills.mts [ids…]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from '../../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const OUT = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/Paraguay/short1/stills'
mkdirSync(OUT, { recursive: true })
const LOG = join(HERE, 'run_stills.log')
const REF = join(homedir(), '.cache/paraguay-ref/presenter.jpg')
const rows: { id: string; ref: boolean; still: string }[] = JSON.parse(readFileSync(join(HERE, 'prompts.json'), 'utf8'))
const want = process.argv.slice(2)
const queue = rows.filter(r => (!want.length || want.includes(r.id)) && !existsSync(join(OUT, `${r.id}-a.jpg`)))
const say = (o: Record<string, unknown>) => { const l = JSON.stringify({ at: new Date().toISOString(), ...o }); console.log(l); appendFileSync(LOG, l + '\n') }
const client: any = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
const page = client.page
const sleep = (ms: number) => page.waitForTimeout(ms)
const tries: Record<string, number> = {}
while (queue.length) {
  const r = queue.shift()!
  tries[r.id] = (tries[r.id] ?? 0) + 1
  const stage = join(OUT, '_runs', r.id); mkdirSync(stage, { recursive: true })
  try {
    const proj = await client.createProject(); say({ ev: 'project', id: r.id, project: proj.id, try: tries[r.id] })
    await page.keyboard.press('Escape').catch(() => {}); await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {}); await sleep(10000)
    const cards = () => page.evaluate(() => (document.body.innerText.match(/unusual activity/gi) ?? []).length).catch(() => 0)
    const before = await cards(); let stop = false
    const watch = (async () => { while (!stop) { await sleep(2000); if (!stop && (await cards()) > before) throw new Error('UNUSUAL_ACTIVITY card') } })()
    const opts = { model: 'Nano Banana 2', aspect: '9:16', numOutputs: 2 }
    const gen = r.ref ? client.editImage(r.still, [REF], join(stage, 'out.jpg'), opts) : client.generateImage(r.still, join(stage, 'out.jpg'), opts)
    gen.catch(() => {})
    try { await Promise.race([gen, watch]) } finally { stop = true; watch.catch(() => {}) }
    for (const s of ['a', 'b']) {
      const src = join(stage, `out-${s}.jpg`)
      if (existsSync(src)) copyFileSync(src, join(OUT, `${r.id}-${s}.jpg`))
      if (existsSync(src + '.prov.json')) copyFileSync(src + '.prov.json', join(OUT, `${r.id}-${s}.jpg.prov.json`))
    }
    say({ ev: 'done', id: r.id, try: tries[r.id] })
  } catch (err) {
    const e = String(err).slice(0, 300); say({ ev: 'fail', id: r.id, try: tries[r.id], error: e })
    if (e.includes('POLICY')) continue
    if (tries[r.id] < 4) queue.unshift(r)
  }
}
say({ ev: 'end' }); process.exit(0)
