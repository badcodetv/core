/**
 * Round 10 stills, verbatim from ../prompts-r10.json: Nano Banana 2, 16:9, 2 takes, ONE prompt per Flow project,
 * two references each: the place frame (~/.cache/badcode-refs/gang/places/<id>.png) and the gang card
 * (~/.cache/badcode-refs/gang/gang-lineup-heads-kai.jpg). Saves <MB>/<id>r10-a.jpg / -b.jpg (+ .prov.json).
 * Resume: a still already on disk is skipped.  MB defaults to Kai's D: folder (scene.json's media is Jack's machine).
 *   npx tsx docs/stories/bank-robbery/songs/mv-gang/cleanroom/r10/run_stills.mts [ids…]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { homedir } from 'node:os'
import { FlowClient } from '../../../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const MB = process.env.MB ?? '/mnt/d/badcode-videos/bank-robbery-music/gang/moodboard'
const REFS = join(homedir(), '.cache/badcode-refs/gang')
const LOG = join(HERE, 'run_stills.log')
const prompts: Record<string, { run: string }> = JSON.parse(readFileSync(join(HERE, '../prompts-r10.json'), 'utf8'))
const want = process.argv.slice(2)
const ids = Object.keys(prompts).filter(i => (!want.length || want.includes(i)) && !existsSync(join(MB, `${i}r10-a.jpg`)))
const say = (o: Record<string, unknown>) => { const l = JSON.stringify({ at: new Date().toISOString(), ...o }); console.log(l); appendFileSync(LOG, l + '\n') }
mkdirSync(MB, { recursive: true })
const client = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
for (const id of ids) {
  const stage = join(MB, '_runs', `${id}r10`); mkdirSync(stage, { recursive: true })
  for (let attempt = 1; attempt <= 2; attempt++) {
    try {
      const proj = await client.createProject()
      say({ ev: 'start', id, project: proj.id, attempt })
      await client.editImage(prompts[id].run, [join(REFS, 'places', `${id}.png`), join(REFS, 'gang-lineup-heads-kai.jpg')],
        join(stage, '00.jpg'), { model: 'Nano Banana 2', aspect: '16:9', numOutputs: 2 })
      let n = 0
      for (const s of ['a', 'b']) {
        const src = join(stage, `00-${s}.jpg`)
        if (existsSync(src)) { copyFileSync(src, join(MB, `${id}r10-${s}.jpg`)); n++ }
        if (existsSync(src + '.prov.json')) copyFileSync(src + '.prov.json', join(MB, `${id}r10-${s}.jpg.prov.json`))
      }
      say({ ev: 'done', id, stills: n }); if (n) break
    } catch (err) { say({ ev: 'error', id, attempt, error: String(err).slice(0, 300) }); if (String(err).includes('POLICY')) break }
  }
}
say({ ev: 'end' }); await (client as any).close?.()
