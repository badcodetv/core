/**
 * Run the Camping balaclava design round verbatim in Flow: Nano Banana 2, 16:9, 2 takes each, a fresh
 * project per 2 prompts (Flow hung after ~2 prompts per project on the Colour Noir run).
 * Saves <media>/moodboard/<id>-a.jpg / -b.jpg. Resume: a still already on disk is skipped.
 *
 *   npx tsx docs/stories/camping/mv-balaclava/cleanroom/run_stills.mts [ids…]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const scene = JSON.parse(readFileSync(join(HERE, '../scene.json'), 'utf8'))
const MB = join(scene.media, 'moodboard')
const LOG = join(HERE, 'run_stills.log')
const R = process.env.ROUND ?? ''  // '-r2' → prompts-r2.json, ids <sid>r2, reference attached
const REF = process.env.REF  // local reference image (never /mnt)
const prompts: Record<string, { run: string }> = JSON.parse(readFileSync(join(HERE, `prompts${R}.json`), 'utf8'))
const tag = R.replace('-', '')

const want = process.argv.slice(2)
const ids = Object.keys(prompts).filter(i => (!want.length || want.includes(i)) && !existsSync(join(MB, `${i}${tag}-a.jpg`)))
const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line); appendFileSync(LOG, line + '\n')
}

async function refBatch(pair: string[], stage: string) {
  const items: { index: number }[] = [], failed: { index: number; code: string }[] = []
  for (const [index, i] of pair.entries()) {
    if (existsSync(join(stage, `${String(index).padStart(2, '0')}-a.jpg`))) { items.push({ index }); continue }
    try {
      await client.editImage(prompts[i].run, [REF!], join(stage, `${String(index).padStart(2, '0')}.jpg`), { model: 'Nano Banana 2', aspect: '16:9', numOutputs: 2 })
      items.push({ index })
    } catch (err) { failed.push({ index, code: String(err).slice(0, 200) }); if (!String(err).includes('POLICY')) break }
  }
  return { items, failed, partial: failed.length > 0 }
}

const client = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
const N = Number(process.env.PER_PROJECT ?? 2)
for (let k = 0; k < ids.length; k += N) {
  const pair = ids.slice(k, k + N)
  const stage = join(MB, '_runs', pair.join('-') + tag)
  mkdirSync(stage, { recursive: true })
  for (let attempt = 1; attempt <= 2; attempt++) {
    try {
      const proj = await client.createProject()
      say({ ev: 'pair.start', pair, project: proj.id, attempt })
      const res = REF ? await refBatch(pair, stage) : await client.generateBatch(pair.map(i => prompts[i].run), stage, {
        model: 'Nano Banana 2', aspect: '16:9', numOutputs: 2, resume: true,
      })
      res.items.forEach(({ index: n }) => {
        for (const s of ['a', 'b']) {
          const src = join(stage, `${String(n).padStart(2, '0')}-${s}.jpg`)
          if (existsSync(src)) copyFileSync(src, join(MB, `${pair[n]}${tag}-${s}.jpg`))
          if (existsSync(src + '.prov.json')) copyFileSync(src + '.prov.json', join(MB, `${pair[n]}${tag}-${s}.jpg.prov.json`))
        }
      })
      say({ ev: 'pair.done', pair, project: proj.id, done: res.items.length, failed: res.failed.map(f => ({ i: pair[f.index], code: f.code })), partial: res.partial })
      if (!res.partial || res.failed.every(f => f.code === 'POLICY_BLOCKED')) break
    } catch (err) {
      say({ ev: 'pair.error', pair, attempt, error: String(err).slice(0, 300) })
    }
  }
}
say({ ev: 'end' })
await (client as any).close?.()
