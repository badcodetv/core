/**
 * Round 10 stills (Camping MV, opening + bridge, 2026-11-09): run prompts-r10.json verbatim in Flow, Nano Banana 2, 16:9, x2,
 * each shot with its own reference images (`refs`, file names in REFDIR). One fresh project per PER_PROJECT shots.
 * Saves <MEDIA>/moodboard/<id>-a.jpg / -b.jpg. A still already on disk is skipped.
 *
 *   npx tsx docs/stories/camping/mv-song2/cleanroom/r10/run_stills.mts [ids…]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
export const MEDIA = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/r10'
const OUT = join(MEDIA, 'moodboard')
const REFDIR = process.env.REFDIR ?? join(process.env.HOME!, '.cache/badcode-scenes/camping-r10/ref')
const LOG = join(HERE, 'run_stills.log')
const prompts: Record<string, { run: string; refs: string[] }> = JSON.parse(readFileSync(join(HERE, 'prompts-r10.json'), 'utf8'))
mkdirSync(OUT, { recursive: true })

const want = process.argv.slice(2)
const ids = Object.keys(prompts).filter(i => (!want.length || want.includes(i)) && !existsSync(join(OUT, `${i}-a.jpg`)))
const say = (o: Record<string, unknown>) => {
  const line = JSON.stringify({ at: new Date().toISOString(), ...o })
  console.log(line); appendFileSync(LOG, line + '\n')
}

const client = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
const N = Number(process.env.PER_PROJECT ?? 2)
for (let k = 0; k < ids.length; k += N) {
  const group = ids.slice(k, k + N)
  const proj = await client.createProject()
  say({ ev: 'group.start', group, project: proj.id })
  for (const id of group) {
    const stage = join(OUT, '_runs', id + '-' + Date.now())
    mkdirSync(stage, { recursive: true })
    const refs = prompts[id].refs.map(r => join(REFDIR, r))
    for (let attempt = 1; attempt <= 2; attempt++) {
      try {
        const o = { model: 'Nano Banana 2', aspect: '16:9', numOutputs: 2 }
        if (refs.length) await client.editImage(prompts[id].run, refs, join(stage, 'img.jpg'), o)
        else await client.generateImage(prompts[id].run, join(stage, 'img.jpg'), o)
        let got = 0
        for (const s of ['a', 'b']) {
          const src = join(stage, `img-${s}.jpg`)
          if (existsSync(src)) { copyFileSync(src, join(OUT, `${id}-${s}.jpg`)); got++ }
          if (existsSync(src + '.prov.json')) copyFileSync(src + '.prov.json', join(OUT, `${id}-${s}.jpg.prov.json`))
        }
        say({ ev: 'shot.done', id, got, stage })
        break
      } catch (err) {
        say({ ev: 'shot.error', id, attempt, error: String(err).slice(0, 300) })
        if (String(err).includes('POLICY')) break
      }
    }
  }
}
say({ ev: 'end' })
await (client as any).close?.()
