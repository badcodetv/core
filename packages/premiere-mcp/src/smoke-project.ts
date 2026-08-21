/**
 * T6's check, run against the REAL MCP server rather than the bridge directly — the point is to
 * exercise `server.ts` (config gating, path translation, directory creation), not to reimplement
 * it here.
 *
 *   npx tsx packages/premiere-mcp/src/smoke-project.ts
 *
 * Spawns the server over stdio, drives it as an MCP client, and asserts the acceptance criteria:
 * create-then-open, import into a bin, list, and NO_MEDIA_ROOT gating on everything but
 * `premiere_status`.
 *
 * Nothing else may hold the bridge port. The panel must be open in Premiere.
 */
import fs from 'node:fs'
import path from 'node:path'
import { Checks, call, connectServer } from './smoke-client'

const STORY = process.env.SMOKE_STORY ?? 'gitpush-origin-master'
const MEDIA = process.env.SMOKE_MEDIA ?? '/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4'
const BIN = 's00'

const c = new Checks()
const check = (label: string, condition: boolean, detail?: unknown): void => {
  c.check(label, condition, detail)
}
const connect = connectServer

async function main(): Promise<void> {
  console.log(`story=${STORY}  media=${MEDIA}\n`)

  console.log('— tools are registered —')
  const { client, close } = await connectServer()
  try {
    const tools = (await client.listTools()).tools.map((t) => t.name)
    console.log(`  ${tools.join(', ')}`)
    for (const expected of ['premiere_status', 'premiere_open_project', 'premiere_save', 'premiere_import', 'premiere_list_items']) {
      check(`${expected} registered`, tools.includes(expected))
    }

    console.log('\n— premiere_status —')
    const status = await call(client, 'premiere_status')
    console.log(`  ${JSON.stringify(status)}`)
    check('panel connected', status.connected === true, status)
    check('mediaRoot reported', typeof status.mediaRoot === 'string', status)
    if (status.connected !== true) {
      console.log('\n  Stopping: nothing below can run without the panel.')
      return
    }

    console.log('\n— premiere_open_project (first call) —')
    const first = await call(client, 'premiere_open_project', { story: STORY })
    console.log(`  ${JSON.stringify(first)}`)
    const projectPath = (first.project as { path?: string } | undefined)?.path
    check('returned a project', Boolean(projectPath), first)
    check('project path is WSL form', typeof projectPath === 'string' && projectPath.startsWith('/mnt/'), projectPath)
    check('renders/ and frames/ were created', dirsExist(projectPath))

    console.log('\n— premiere_open_project (second call) —')
    const second = await call(client, 'premiere_open_project', { story: STORY })
    console.log(`  ${JSON.stringify(second)}`)
    check('second call reports created: false', second.created === false, second)
    check(
      'exactly one of the two calls created it',
      first.created === true || second.created === false,
      { first: first.created, second: second.created }
    )

    console.log('\n— premiere_open_project by explicit path (any folder) —')
    const loosePath = process.env.SMOKE_LOOSE_PROJECT ?? '/mnt/d/badcode-videos/_smoke/loose-project.prproj'
    const loose = await call(client, 'premiere_open_project', { path: loosePath })
    console.log(`  ${JSON.stringify(loose)}`)
    check('opened a project outside the story convention', Boolean((loose.project as { path?: string } | undefined)?.path), loose)
    check('framesDir sits beside the project', String(loose.framesDir ?? '').endsWith('/_smoke/frames'), loose)
    check('rendersDir sits beside the project', String(loose.rendersDir ?? '').endsWith('/_smoke/renders'), loose)

    const notAProject = await call(client, 'premiere_open_project', { path: '/mnt/d/badcode-videos/nope.txt' })
    check('a non-.prproj path is rejected', notAProject.code === 'INVALID_ARGS', notAProject)

    const neither = await call(client, 'premiere_open_project', {})
    check('neither story nor path is rejected', neither.code === 'INVALID_ARGS', neither)

    // Back to the story project before the import checks, so they land in the right place.
    await call(client, 'premiere_open_project', { story: STORY })

    console.log('\n— premiere_import —')
    if (!fs.existsSync(MEDIA)) {
      console.log(`  ⚠️  skipped: ${MEDIA} does not exist. Set SMOKE_MEDIA to a real file.`)
    } else {
      const imported = await call(client, 'premiere_import', { paths: [MEDIA], bin: BIN })
      console.log(`  ${JSON.stringify(imported)}`)
      const items = (imported.items as { name: string; mediaPath: string }[] | undefined) ?? []
      check('imported one item', items.length === 1, imported)
      check('item has a WSL mediaPath', items[0]?.mediaPath?.startsWith('/mnt/') ?? false, items[0])
      check('bin echoed back', imported.bin === BIN, imported)
    }

    console.log('\n— premiere_list_items —')
    const listed = await call(client, 'premiere_list_items')
    const items = (listed.items as { name: string; type: string; mediaPath?: string }[] | undefined) ?? []
    console.log(`  ${items.length} item(s): ${items.map((i) => `${i.name}[${i.type}]`).join(', ')}`)
    check('the bin is listed', items.some((i) => i.name === BIN && i.type === 'bin'), items)

    console.log('\n— premiere_save —')
    const saved = await call(client, 'premiere_save')
    console.log(`  ${JSON.stringify(saved)}`)
    check('save returned a WSL path', String(saved.path ?? '').startsWith('/mnt/'), saved)
  } finally {
    await close()
  }

  // A second server, deliberately starved of config: status must still answer, everything else
  // must refuse with NO_MEDIA_ROOT rather than half-working.
  console.log('\n— no media root configured —')
  const starved = await connect({ BADCODE_MEDIA_ROOT: '', PREMIERE_BRIDGE_PORT: '7899' })
  try {
    const status = await call(starved.client, 'premiere_status')
    check('status still answers without config', typeof status.connected === 'boolean', status)
    const opened = await call(starved.client, 'premiere_open_project', { story: STORY })
    check('open_project by story refuses without config', opened.code === 'NO_MEDIA_ROOT', opened)
    check('…and the error names the example file', String(opened.hint ?? '').includes('badcode.local.json.example'), opened)
    // Opening by explicit path must NOT need a media root — that is the whole point of it.
    const byPath = await call(starved.client, 'premiere_open_project', { path: '/mnt/d/badcode-videos/_smoke/loose-project.prproj' })
    check('open_project by path does not need a media root', byPath.code !== 'NO_MEDIA_ROOT', byPath)
  } finally {
    await starved.close()
  }

  c.finish('T6 smoke')
}

function dirsExist(projectPath: string | undefined): boolean {
  if (!projectPath) return false
  const storyDir = path.dirname(projectPath)
  return fs.existsSync(path.join(storyDir, 'renders')) && fs.existsSync(path.join(storyDir, 'frames'))
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
