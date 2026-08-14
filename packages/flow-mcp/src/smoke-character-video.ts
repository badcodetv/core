/**
 * Can a Flow **Character** be cast in a VIDEO turn?
 *
 * No video tool takes a `character` today — the route has always been character → still →
 * animate that still. But the picker fix opened a door: the asset picker is now reachable in
 * video mode via the `@` route, and its Characters tab is present there. So the question is
 * whether Flow's video composer accepts a character chip at all, or silently ignores it.
 *
 * Runs in three steps so a failure says WHICH step failed:
 *   1. list characters (free) — creates one from an existing gallery still if none exist
 *   2. put the bar in video mode and attach the character (free)
 *   3. optionally submit, with --generate (⚠️ one clip)
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-character-video.ts <projectId> <outDir> [--generate]
 */
import { execFileSync } from 'node:child_process'
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, outDir, flag] = process.argv.slice(2)
if (!projectId || !outDir) throw new Error('usage: smoke-character-video.ts <projectId> <outDir> [--generate]')

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    ensureFramesMode(): Promise<void>
    addCharacterToPrompt(name: string): Promise<void>
    scrapeReferenceChips(): Promise<string[]>
    promptBox(): Locator
  }
  const page = inner.page
  await client.openProject({ id: projectId })

  // 1. A character to cast.
  let characters = await client.listCharacters()
  console.log(`characters in project: ${JSON.stringify(characters.map((c) => c.name))}`)
  if (!characters.length) {
    const media = await client.listMedia({ limit: 40 })
    const still = media.find((m) => /image/i.test(String(m.kind)))
    if (!still) throw new Error('no still in the gallery to found a character from')
    console.log(`creating a character from "${still.title}"`)
    await client.createCharacterFromMedia('Corridor Witness', still.title)
    characters = await client.listCharacters()
    console.log(`characters now: ${JSON.stringify(characters.map((c) => c.name))}`)
  }
  const name = characters[0]!.name

  // 2. Video mode, then attach. This is the step that was impossible before the picker fix.
  await inner.ensureFramesMode()
  const bar = (await page.evaluate(`(() => [...document.querySelectorAll('button')].map(b => (b.textContent||'').trim()).filter(t => /Video\\s*·|Swap first and last/.test(t)))()`)) as string[]
  console.log(`compose bar before attach: ${JSON.stringify(bar)}`)
  const chipsBefore = await inner.scrapeReferenceChips()
  await inner.addCharacterToPrompt(name)
  await page.waitForTimeout(1500)
  const boxText = ((await inner.promptBox().textContent()) ?? '').trim()
  const chipsAfter = await inner.scrapeReferenceChips()
  console.log(`prompt box after attach: ${JSON.stringify(boxText)}`)
  console.log(`reference chips: ${chipsBefore.length} -> ${chipsAfter.length}`)
  const barAfter = (await page.evaluate(`(() => [...document.querySelectorAll('button')].map(b => (b.textContent||'').trim()).filter(t => /Video\\s*·|Swap first and last/.test(t)))()`)) as string[]
  console.log(`compose bar after attach: ${JSON.stringify(barAfter)}`)
  if (!boxText.includes(name) && chipsAfter.length === chipsBefore.length) {
    throw new Error('ATTACH FAILED — the character landed neither in the prompt box nor as a chip')
  }
  console.log('ATTACH OK — a character can be put on a video turn')

  // 3. The real test: does it work through generateVideo, the way a caller would reach it?
  //    The hand-staged version above proved the mechanism; this proves the WIRING.
  if (flag !== '--generate') {
    console.log('\n(stopping before generation — pass --generate to spend one clip)')
  } else {
    const started = Date.now()
    const clip = await client.generateVideo({
      motion: 'walks slowly down the corridor. Camera holds still. No cuts.',
      outPath: `${outDir}/character.mp4`,
      character: name,
      model: 'Veo 3.1 Lite',
      durationSeconds: 4,
    })
    console.log(`clip ${clip.mediaId} in ${((Date.now() - started) / 1000).toFixed(1)}s -> ${clip.path}`)
    const probe = execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', clip.path]).toString().trim().replace(/\n/g, ' ')
    console.log(`ffprobe: ${probe}`)
    execFileSync('ffmpeg', ['-y', '-v', 'error', '-i', clip.path, '-vf', 'select=eq(n\\,0)', '-vframes', '1', `${outDir}/char-first.jpg`])
    console.log(`first frame: ${outDir}/char-first.jpg — LOOK at it`)
  }
} finally {
  await client.close()
}
