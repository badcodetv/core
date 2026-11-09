/**
 * Paraguay presenter round 2: run the sealed writers' prompts verbatim in Flow.
 * Nano Banana 2, 16:9, 2 takes, the mask sheet attached as the one reference, ONE prompt per fresh project
 * (a second reference prompt in a project came back as a copy of the reference on the Camping run).
 * A real page reload before every prompt; "unusual activity" → reload, ~10 s, retry (3 tries), else defer to the end.
 * Saves <media>/moodboard/<id>-a.jpg / -b.jpg; a still already on disk is skipped.
 *
 *   npx tsx docs/stories/magic-money-tree/scenes/paraguay-presenter/cleanroom/r2/run_stills.mts [ids…]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from '../../../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const scene = JSON.parse(readFileSync(join(HERE, '../../scene.json'), 'utf8'))
const MB = join(scene.media, 'moodboard')
const LOG = join(HERE, 'run_stills.log')
const REF = join(homedir(), '.cache/paraguay-ref/mask-sheet.jpg')  // staged locally, never /mnt
const rows: { id: string; prompt: string }[] = []
for (let w = 1; w <= 6; w++) {
  const f = join(HERE, `w${w}.json`)
  if (existsSync(f)) rows.push(...JSON.parse(readFileSync(f, 'utf8')))
}
const want = process.argv.slice(2)
let queue = rows.filter(r => (!want.length || want.includes(r.id)) && !existsSync(join(MB, `${r.id}-a.jpg`)))
const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line); appendFileSync(LOG, line + '\n')
}

const client: any = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
const page = client.page
const sleep = (ms: number) => page.waitForTimeout(ms)
async function hardReload() {
  await page.keyboard.press('Escape').catch(() => {})
  await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {})
  await sleep(4000)
}

const tries: Record<string, number> = {}
while (queue.length) {
  const r = queue.shift()!
  tries[r.id] = (tries[r.id] ?? 0) + 1
  const stage = join(MB, '_runs', r.id)
  mkdirSync(stage, { recursive: true })
  try {
    // A fresh project on EVERY try: a retry inside the same project came back as a copy of the reference (02/09/11, 2026-11-09).
    { const proj = await client.createProject(); say({ ev: 'project', id: r.id, project: proj.id, try: tries[r.id] }) }
    await hardReload()
    await sleep(6000)
    // Jack 2026-11-09: "just refresh the page and try again". The image tool never reads the "unusual activity"
    // card and sits out its 90 s timeout, so watch for a NEW card here and bail in seconds.
    const cards = () => page.evaluate(() => (document.body.innerText.match(/unusual activity/gi) ?? []).length).catch(() => 0)
    const before = await cards()
    let stop = false
    const watch = (async () => {
      while (!stop) { await sleep(2000); if (!stop && (await cards()) > before) throw new Error('UNUSUAL_ACTIVITY card') }
    })()
    const gen = client.editImage(r.prompt, [REF], join(stage, 'out.jpg'), { model: 'Nano Banana 2', aspect: '16:9', numOutputs: 2 })
    gen.catch(() => {})
    try { await Promise.race([gen, watch]) } finally { stop = true; watch.catch(() => {}) }
    for (const s of ['a', 'b']) {
      const src = join(stage, `out-${s}.jpg`)
      if (existsSync(src)) copyFileSync(src, join(MB, `${r.id}-${s}.jpg`))
      if (existsSync(src + '.prov.json')) copyFileSync(src + '.prov.json', join(MB, `${r.id}-${s}.jpg.prov.json`))
    }
    say({ ev: 'done', id: r.id, try: tries[r.id] })
  } catch (err) {
    const e = String(err).slice(0, 300)
    say({ ev: 'fail', id: r.id, try: tries[r.id], error: e })
    if (e.includes('POLICY')) continue
    if (tries[r.id] < 4) { await sleep(10000); queue.unshift(r) }  // refresh (top of loop) and retry now, ~10 s
  }
}
say({ ev: 'end' })
process.exit(0)
