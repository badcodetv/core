// One Flow image edit on the repo's fixed flow-client: npx tsx edit1.mts <prompt-file> <out.jpg> <ref.jpg> [ref2.jpg]
// (Malevolent Force, 2026-11-18. The flow MCP may still run old code until /mcp reconnects.)
import { readFileSync } from 'node:fs'
import { FlowClient } from '../../../../../../packages/flow-mcp/src/flow-client'
const [pf, out, ...refs] = process.argv.slice(2)
const c: any = await FlowClient.connect('http://localhost:9222')
await c.openProject({ id: '0153219b-e10c-46ac-b2a7-5b50200e19fe' })
const r = await c.editImage(readFileSync(pf!, 'utf8'), refs, out, { numOutputs: 2, model: 'Nano Banana 2.1', aspect: '9:16' })
console.log('OK', JSON.stringify(r.candidates.map((x: any) => x.path.split('/').pop())))
await c.close()
