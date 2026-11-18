// Malevolent Force, Jack 2026-11-18 round 5 note on the dash: facing the camera, peeking out of the open back door, so the
// clip can have it scuttle backwards without turning. Run on the repo's fixed flow-client.
import { readFileSync } from 'node:fs'
import { FlowClient } from '../../../../../../packages/flow-mcp/src/flow-client'
const M = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/malevolent-force/moodboard/'
const prompt = readFileSync(process.argv[2]!, 'utf8')
const c: any = await FlowClient.connect('http://localhost:9222')
await c.openProject({ id: '0153219b-e10c-46ac-b2a7-5b50200e19fe' })
const r = await c.editImage(prompt, [M + 'PR2-c.jpg'], M + 'JS3-peek.jpg', { numOutputs: 2, model: 'Nano Banana 2.1', aspect: '9:16' })
console.log('OK', JSON.stringify(r.candidates.map((x: any) => x.path.split('/').pop())))
await c.close()
