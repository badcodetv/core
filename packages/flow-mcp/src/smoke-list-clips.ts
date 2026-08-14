/**
 * Can a caller who lost the mediaId get it back?
 *
 * `flow_refine_video` REQUIRES a clip's mediaId, and the whole selling point is refining days
 * later — by which time the id lives only in whatever the caller wrote down. `flow_list_media`
 * is the only recovery route, and its own contract says mediaId is *optional* ("present only
 * when the tile's src carries one"). If video rows come back without ids, refine is unreachable
 * for anyone who did not keep a record, and that is a hole in the workflow rather than the code.
 *
 * Credit-free.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-list-clips.ts <projectId>
 */
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-list-clips.ts <projectId>')

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const items = await client.listMedia({ limit: 40 })
  for (const i of items) {
    console.log(`${String(i.index).padStart(2)} ${String(i.kind).padEnd(6)} ${i.mediaId ?? '(no mediaId)'}  ${i.title.slice(0, 46)}`)
  }
  const vids = items.filter((i) => /video/i.test(String(i.kind)))
  console.log(`\nvideo rows: ${vids.length}; with a mediaId: ${vids.filter((v) => v.mediaId).length}`)
} finally {
  await client.close()
}
