/**
 * Round 2, pass 2: Flow drew her as tall as the men and in the line. Edit each take with only itself attached:
 * shrink her and step her forward. Nano Banana 2.1, 16:9, 1 take, one fresh project each.
 * Saves /mnt/d/badcode-videos/bank-robbery-music/gang/her/r2/<id>-<a|b>-small.jpg. Resume skips done files.
 *   TMPDIR=$HOME/.cache/pw-tmp npx tsx docs/stories/bank-robbery/songs/mv-gang/her/r2/shrink.mts [A-a …]
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync } from 'node:fs'
import { join } from 'node:path'
import { FlowClient } from '../../../../../../../packages/flow-mcp/src/flow-client'

const HERE = new URL('.', import.meta.url).pathname
const OUT = '/mnt/d/badcode-videos/bank-robbery-music/gang/her/r2'
const LOG = join(HERE, 'shrink.log')
const PROMPT = 'Using the attached image, change only the woman in the middle, the one in a different outfit from the six men in suits. ' +
  'Make her much smaller and slighter: the top of her hat reaches only the middle of the men\'s chests. ' +
  'Move her one stride forward, down onto the step in front of the men and closer to the lens, so she stands alone in front of them, centre frame, ' +
  'and close the six men up into a tight row directly behind her, so they tower over her like bodyguards. ' +
  'Keep her outfit, her balaclava, its white ring and red triangle, and her gesture exactly as they are. ' +
  'Keep every man, the columns, the steps, the fire, the flying banknotes, the light and the framing exactly the same. 16:9.\n\nThanks.'
const want = process.argv.slice(2)
const all = ['A', 'B', 'C', 'D', 'E', 'F'].flatMap(k => [`${k}-a`, `${k}-b`])
const ids = all.filter(i => (!want.length || want.includes(i)) && existsSync(join(OUT, `${i}.jpg`)) && !existsSync(join(OUT, `${i}-small.jpg`)))
const say = (o: Record<string, unknown>) => { const l = JSON.stringify({ at: new Date().toISOString(), ...o }); console.log(l); appendFileSync(LOG, l + '\n') }
const client = await FlowClient.connect(process.env.FLOW_CDP ?? 'http://localhost:9222')
for (const id of ids) {
  const stage = join(OUT, '_runs', `${id}-small`); mkdirSync(stage, { recursive: true })
  for (let attempt = 1; attempt <= 2; attempt++) {
    try {
      const proj = await client.createProject()
      say({ ev: 'start', id, project: proj.id, attempt })
      await client.editImage(PROMPT, [join(OUT, `${id}.jpg`)], join(stage, '00.jpg'), { model: 'Nano Banana 2.1', aspect: '16:9', numOutputs: 1 })
      const src = [join(stage, '00.jpg'), join(stage, '00-a.jpg')].find(existsSync)
      if (src) { copyFileSync(src, join(OUT, `${id}-small.jpg`)); if (existsSync(src + '.prov.json')) copyFileSync(src + '.prov.json', join(OUT, `${id}-small.jpg.prov.json`)) }
      say({ ev: 'done', id, ok: !!src }); if (src) break
    } catch (err) { say({ ev: 'error', id, attempt, error: String(err).slice(0, 300) }); if (String(err).includes('POLICY')) break }
  }
}
say({ ev: 'end' }); await (client as any).close?.()
