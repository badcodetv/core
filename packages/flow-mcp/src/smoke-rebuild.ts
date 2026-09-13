// Usage: npx tsx packages/flow-mcp/src/smoke-rebuild.ts [stage]
// Live proof for the 2026-09-13 Flow rebuild (flow.google.com, Angular). Stages:
//   status   — status + project list (no spend)
//   image    — new scratch project, Nano Banana 2 x2 (shows 0 credits), harvest both, refine once
//   edit     — reopen FLOW_SMOKE_PROJECT, upload FLOW_SMOKE_REF as a reference, edit x2, then refine the first
//   video    — reopen FLOW_SMOKE_PROJECT, animate FLOW_SMOKE_REF on Veo 3.1 - Lite [Lower Priority] (0 credits), 4s x1
// Every file is measured with ffprobe-free JPEG parsing and hashed, so a web page saved as .jpg fails loudly.
import { mkdtemp, readFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from './flow-client'
import { jpegSize } from './jpeg-size'

const stage = process.argv[2] ?? 'status'
const describe = async (path: string) => {
  const buf = await readFile(path)
  return { path, bytes: buf.length, size: jpegSize(buf), md5: createHash('md5').update(buf).digest('hex').slice(0, 10) }
}

const c = await FlowClient.connect()
try {
  console.log('status:', await c.status())
  const projects = await c.listProjects()
  console.log('projects:', projects.length, projects.slice(0, 3))
  if (stage === 'image') {
    const made = await c.createProject('flow-rebuild-smoke')
    console.log('created:', made)
    const dir = await mkdtemp(join(tmpdir(), 'flow-rebuild-'))
    const a = await c.generateImage(
      'A single landscape photograph: an empty concrete underpass at night, one sodium streetlight, wet ground.',
      join(dir, 'a.jpg'),
      { model: 'Nano Banana 2', numOutputs: 2 },
    )
    for (const cand of a.candidates ?? [a]) console.log('candidate:', cand.mediaId, await describe(cand.path))
    const r = await c.refine('Same shot, but add a single red umbrella lying on the ground.', join(dir, 'r.jpg'), { model: 'Nano Banana 2' })
    console.log('refined:', r.mediaId, await describe(r.path))
  }
  if (stage === 'edit') {
    await c.openProject({ id: process.env.FLOW_SMOKE_PROJECT! })
    const dir = await mkdtemp(join(tmpdir(), 'flow-rebuild-edit-'))
    const e = await c.editImage('Keep this exact scene and framing. Add a single lit phone box on the left wall.', [process.env.FLOW_SMOKE_REF!], join(dir, 'e.jpg'), { model: 'Nano Banana 2', numOutputs: 2 })
    for (const cand of e.candidates) console.log('edit candidate:', cand.mediaId, await describe(cand.path))
    const r = await c.refine('Keep everything. Make the phone box light green.', join(dir, 'r.jpg'), { model: 'Nano Banana 2' })
    console.log('refined:', r.mediaId, await describe(r.path))
  }
  if (stage === 'video') {
    await c.openProject({ id: process.env.FLOW_SMOKE_PROJECT! })
    const dir = await mkdtemp(join(tmpdir(), 'flow-rebuild-video-'))
    const t0 = Date.now()
    const v = await c.generateVideo({
      motion: 'Locked-off camera. A slow drip of water falls from the ceiling light; puddles ripple. Nothing else moves.',
      outPath: join(dir, 'v.mp4'),
      startImage: process.env.FLOW_SMOKE_REF!,
      ...(process.env.FLOW_SMOKE_END ? { endImage: process.env.FLOW_SMOKE_END } : {}),
      model: 'Veo 3.1 - Lite [Lower Priority]',
      durationSeconds: 4,
      count: 1,
    })
    const buf = await readFile(v.path)
    console.log('video:', v, 'bytes:', buf.length, 'seconds:', Math.round((Date.now() - t0) / 1000))
  }
  console.log(`REBUILD SMOKE (${stage}) OK`)
} finally {
  await c.close()
}
