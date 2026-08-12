/**
 * Manual check — the flow_list_media -> flow_create_character_from_media round-trip.
 *
 * THE point of the task: a `title` that listMedia returns must be usable verbatim as
 * create_character_from_media's `mediaTitle`. If it needs hand-editing to match, the media
 * parser is wrong — Flow's accessible name is doubled ("X X Image") and the de-doubling has to
 * leave something the picker's own option lookup still finds.
 *
 * Costs no generation credits (no body pass). Creates one Character, which you may want to
 * delete afterwards.
 *
 * ⚠️ Rule zero (.claude/skills/flow-prompt/SKILL.md): never put a real person's name in ANY
 * Flow field. The Character Name field is policy-scanned.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-media-character.ts [projectId]
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const id = process.argv[2]
  if (id) await client.openProject({ id })
  console.log('status:', await client.status())

  const media = await client.listMedia()
  console.log(`\n=== listMedia -> ${media.length} rows ===`)
  console.log(JSON.stringify(media.slice(0, 6), null, 2))

  const pick = media.find((m) => m.kind === 'Image')
  if (!pick) throw new Error('no Image row to round-trip')
  console.log(`\n=== round-trip: passing title verbatim ===\n  ${JSON.stringify(pick.title)}`)

  const ref = await client.createCharacterFromMedia('Disc Keeper', pick.title)
  console.log('createCharacterFromMedia ->', JSON.stringify(ref, null, 2))

  console.log('\n=== listCharacters (does it read back?) ===')
  console.log(JSON.stringify(await client.listCharacters(), null, 2))
  console.log('\nROUND-TRIP DONE — the title needed no hand-editing')
} finally {
  await client.close()
}
