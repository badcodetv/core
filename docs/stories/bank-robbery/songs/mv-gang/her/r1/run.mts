/**
 * Her look, round 1: six costume directions, each put in front of the gang on the bank steps (h17 place).
 * Nano Banana 2.1 (Flow replaced Nano Banana 2 by 2026-11-17), 16:9, 2 takes, one Flow project per prompt, refs: h17 place frame + the gang line-up card.
 * Saves /mnt/d/badcode-videos/bank-robbery-music/gang/her/r1/<id>-a.jpg / -b.jpg (+ .prov.json). Resume skips done ids.
 *   TMPDIR=$HOME/.cache/pw-tmp npx tsx docs/stories/bank-robbery/songs/mv-gang/her/r1/run.mts [ids…]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { homedir } from 'node:os'
import { FlowClient } from '../../../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const OUT = '/mnt/d/badcode-videos/bank-robbery-music/gang/her/r1'
const REFS = join(homedir(), '.cache/badcode-refs/gang')
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
      await client.editImage(prompts[id].prompt, [join(REFS, 'places', 'h17.png'), join(REFS, 'gang-lineup-heads-kai.jpg')],
        join(stage, '00.jpg'), { model: 'Nano Banana 2.1', aspect: '16:9', numOutputs: 2 })
      let n = 0
      for (const s of ['a', 'b']) {
        const src = join(stage, `00-${s}.jpg`)
        if (existsSync(src)) { copyFileSync(src, join(OUT, `${id}-${s}.jpg`)); n++ }
        if (existsSync(src + '.prov.json')) copyFileSync(src + '.prov.json', join(OUT, `${id}-${s}.jpg.prov.json`))
      }
      say({ ev: 'done', id, stills: n }); if (n) break
    } catch (err) { say({ ev: 'error', id, attempt, error: String(err).slice(0, 300) }); if (String(err).includes('POLICY')) break }
  }
}
say({ ev: 'end' }); await (client as any).close?.()
