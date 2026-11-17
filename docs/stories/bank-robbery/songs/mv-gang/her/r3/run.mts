/**
 * Her look, round 3 (Kai 2026-11-17: Ghost in the Dust, take C-a, in ten bolder colour schemes).
 * Edits r2/C-a.jpg with only itself attached: recolour her, nothing else. Nano Banana 2.1, 16:9, 2 takes,
 * one fresh project per prompt. Saves /mnt/d/badcode-videos/bank-robbery-music/gang/her/r3/<id>-a.jpg / -b.jpg.
 *   TMPDIR=$HOME/.cache/pw-tmp npx tsx docs/stories/bank-robbery/songs/mv-gang/her/r3/run.mts [ids…]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const BASE = '/mnt/d/badcode-videos/bank-robbery-music/gang/her/r2/C-a.jpg'
const OUT = '/mnt/d/badcode-videos/bank-robbery-music/gang/her/r3'
const LOG = join(HERE, 'run.log')
const prompts: Record<string, { prompt: string }> = JSON.parse(readFileSync(join(HERE, 'prompts.json'), 'utf8'))
const want = process.argv.slice(2)
const ids = Object.keys(prompts).filter(i => (!want.length || want.includes(i)) && !existsSync(join(OUT, `${i}-a.jpg`)))
const say = (o: Record<string, unknown>) => { const l = JSON.stringify({ at: new Date().toISOString(), ...o }); console.log(l); appendFileSync(LOG, l + '\n') }
mkdirSync(OUT, { recursive: true })
const client = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
for (const id of ids) {
  const stage = join(OUT, '_runs', id); mkdirSync(stage, { recursive: true })
  for (let attempt = 1; attempt <= 2; attempt++) {
    try {
      const proj = await client.createProject()
      say({ ev: 'start', id, project: proj.id, attempt })
      await client.editImage(prompts[id].prompt, [BASE], join(stage, '00.jpg'), { model: 'Nano Banana 2.1', aspect: '16:9', numOutputs: 2 })
      let n = 0
      for (const s of ['a', 'b']) { const src = join(stage, `00-${s}.jpg`); if (existsSync(src)) { copyFileSync(src, join(OUT, `${id}-${s}.jpg`)); n++ } }
      say({ ev: 'done', id, stills: n }); if (n) break
    } catch (err) { say({ ev: 'error', id, attempt, error: String(err).slice(0, 300) }); if (String(err).includes('POLICY')) break }
  }
}
say({ ev: 'end' }); await (client as any).close?.()
