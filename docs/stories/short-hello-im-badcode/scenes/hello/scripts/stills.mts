// Hello, I'm BadCode picture round: one Flow edit per job, in the short's own project, on the repo's fixed flow-client.
//   npx tsx stills.mts <jobs.json> <out-dir>
import { readFileSync } from 'node:fs'
import { FlowClient } from '../../../../../../packages/flow-mcp/src/flow-client'
const [jf, outDir] = process.argv.slice(2)
const jobs = JSON.parse(readFileSync(jf!, 'utf8'))
const c: any = await FlowClient.connect('http://localhost:9222')
await c.openProject({ id: '99357c2f-11c0-4909-94a8-adc5a2bbd692' })
for (const j of jobs) {
  try {
    const r = await c.editImage(j.prompt, j.refs, `${outDir}/${j.out}.jpg`, { numOutputs: 1, model: 'Nano Banana 2.1', aspect: '9:16' })
    console.log('OK', j.out, r.candidates.map((x: any) => x.path.split('/').pop()).join(','))
  } catch (e) { console.log('FAIL', j.out, String((e as Error).message).slice(0, 300)) }
}
await c.close()
