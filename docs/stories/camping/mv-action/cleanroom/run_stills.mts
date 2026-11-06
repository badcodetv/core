/**
 * Camping action stills, round 1: each clean-room prompt verbatim, Nano Banana 2, 16:9, 2 takes, the real
 * @Bob / @Tarquin Flow Character cast (project camping-v2). Saves <media>/moodboard/<id>r1-a/-b.jpg.
 * A still already on disk is skipped.   npx tsx docs/stories/camping/mv-action/cleanroom/run_stills.mts [ids…]
 */
import { appendFileSync, existsSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const scene = JSON.parse(readFileSync(join(HERE, '../scene.json'), 'utf8'))
const MB = join(scene.media, 'moodboard')
const LOG = join(HERE, 'run_stills.log')
const RND = process.env.ROUND ?? '1'  // '2' → prompts-r2.json, files <id>r2-*
const prompts: Record<string, { man: string; prompt: string }> = JSON.parse(readFileSync(join(HERE, RND === '1' ? 'prompts.json' : `prompts-r${RND}.json`), 'utf8'))
const want = process.argv.slice(2)
const ids = Object.keys(prompts).filter(i => (!want.length || want.includes(i)) && !existsSync(join(MB, `${i}r${RND}-a.jpg`)))
const say = (o: Record<string, unknown>) => { const l = JSON.stringify({ at: new Date().toISOString(), ...o }); console.log(l); appendFileSync(LOG, l + '\n') }

const client = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
await (client as any).openProject({ id: scene.flow_project })
for (const id of ids) {
  for (let attempt = 1; attempt <= 2; attempt++) {
    try {
      const r = await client.generateImage(prompts[id].prompt, join(MB, `${id}r${RND}.jpg`), { character: prompts[id].man, numOutputs: 2, model: 'Nano Banana 2', aspect: '16:9' })
      say({ ev: 'done', id, n: r.candidates?.length ?? 1, partial: r.partial ?? false }); break
    } catch (err) {
      say({ ev: 'error', id, attempt, error: String(err).slice(0, 300) })
      if (String(err).includes('POLICY')) break
      await new Promise(r => setTimeout(r, 10000))
      try { await (client as any).openProject({ id: scene.flow_project }) } catch {}
    }
  }
}
say({ ev: 'end' })
process.exit(0)
