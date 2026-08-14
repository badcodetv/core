/**
 * Manual smoke test for the read-only discovery tools — NOT part of CI.
 *
 * These three cost nothing to run (no generation, no credits), so this is the cheapest
 * possible signal that the Wave A DOM scrapes match the real UI. Running it via tsx rather
 * than through the MCP server is deliberate: a fresh process picks up source edits
 * immediately, whereas the long-lived MCP server is frozen at whatever the code said when
 * it started and needs a manual /mcp reconnect to see a fix.
 *
 * Pre-req: `./scripts/flow-chrome.sh`, logged in, with a project already open.
 * Usage: npx tsx packages/flow-mcp/src/smoke-lists.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  console.log('status:', await client.status())

  console.log('\n=== listCharacters ===')
  const characters = await client.listCharacters()
  console.log(JSON.stringify(characters, null, 2))

  console.log('\n=== listMedia (first 8) ===')
  const media = await client.listMedia({ limit: 8 })
  console.log(JSON.stringify(media, null, 2))

  console.log('\n=== listMedia({ query }) — does the picker search box actually filter? ===')
  const all = await client.listMedia()
  const needle = all.find(m => m.kind === 'Image')?.title.split(' ').slice(-1)[0]
  if (needle) {
    const filtered = await client.listMedia({ query: needle })
    console.log(`query=${JSON.stringify(needle)}: ${all.length} total -> ${filtered.length} matched`)
    console.log(JSON.stringify(filtered.slice(0, 4), null, 2))
  }

  console.log('\n=== listProjects ===')
  console.log(JSON.stringify((await client.listProjects()).slice(0, 6), null, 2))

  console.log('\nSMOKE-LISTS DONE')
} finally {
  await client.close()
}
