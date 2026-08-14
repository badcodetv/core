/**
 * L3 · Prove the timeout diagnostic writes something a human can act on.
 *
 * Credit-free: it calls the private `timeoutError` directly against a real, healthy Flow page
 * rather than waiting eight minutes for a genuine timeout. What it checks is the only thing that
 * matters — that the dump contains the page's actual words, not Flow's button labels.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-timeout-dump.ts <projectId>
 */
import { readFileSync } from 'node:fs'
import { FlowClient } from './flow-client'

const projectId = process.argv[2]
if (!projectId) throw new Error('usage: smoke-timeout-dump.ts <projectId>')

const client = await FlowClient.connect()
try {
  await client.openProject({ id: projectId })
  const msg = await (client as unknown as { timeoutError(ms: number): Promise<string> }).timeoutError(480_000)
  console.log(msg)
  const path = msg.match(/(\S+)\.txt\/\.png/)?.[1]
  if (!path) throw new Error('the message does not name a dump file')
  const body = readFileSync(`${path}.txt`, 'utf8')
  console.log(`\n--- ${path}.txt ---\n${body}`)
  if (!/labs\.google/.test(body)) throw new Error('dump does not record the page URL')
  readFileSync(`${path}.png`) // throws if the screenshot never landed
  console.log('DUMP OK — url, page text and screenshot on disk')
} finally {
  await client.close()
}
