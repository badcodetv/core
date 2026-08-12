/**
 * L1 probe · what do `Reuse prompt` and `Add to prompt` actually DO to the compose bar?
 *
 * Credit-free: it opens a clip's own menu, clicks one item, and reports the compose bar's state
 * before and after. Nothing is submitted. Run it once per action (`--reuse` / `--add`) so each
 * starts from a freshly loaded page — the compose bar is persistent project state and a probe
 * that ran both in sequence could not tell which one attached what.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-reuse.ts <projectId> [--reuse|--add]
 */
import type { Locator, Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const [projectId, flag = '--add'] = process.argv.slice(2)
if (!projectId) throw new Error('usage: smoke-video-reuse.ts <projectId> [--reuse|--add]')
const item = flag === '--reuse' ? /redo\s*Reuse prompt/i : /add\s*Add to prompt/i

/**
 * Everything the compose bar could plausibly show a video reference as. Deliberately wider than
 * `scrapeReferenceChips` (which only knows `img[alt^="Reference media"]`): a VIDEO ingredient may
 * well not render as an img at all, and a probe that only looked where we already look would
 * report "nothing attached" for an attachment we simply cannot see.
 */
const STATE = `() => {
  const name = (s) => { try { return new URL(s, location.href).searchParams.get('name') } catch (e) { return null } }
  const box = document.querySelector('div[role="textbox"][contenteditable="true"]')
  // The compose bar as a container: walk a fixed 6 levels up from the prompt textbox. Deep
  // enough to include the chip rail beside it, shallow enough to exclude the canvas.
  let composeRoot = box
  for (let i = 0; i < 6 && composeRoot && composeRoot.parentElement; i++) composeRoot = composeRoot.parentElement
  return {
    prompt: box ? (box.textContent || '').trim() : null,
    // Every img/video on the page that carries a media id, with its alt — the diff shows which
    // ones the click added, wherever they mounted.
    media: [...document.querySelectorAll('img, video, source')]
      .map(el => {
        const r = el.getBoundingClientRect()
        const inCompose = !!(composeRoot && composeRoot.contains(el))
        return {
          tag: el.tagName, alt: el.getAttribute('alt') || '',
          n: name(el.currentSrc || el.src || el.getAttribute('src') || ''),
          inCompose, box: [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)],
        }
      })
      .filter(m => m.n),
    // Mode/config trigger labels, e.g. "Video · 8scrop_9_16x1" — shows a mode or duration change.
    triggers: [...document.querySelectorAll('button')]
      .map(b => (b.textContent || '').trim())
      .filter(t => /crop_|Frames|Ingredients|Video\s*·/i.test(t) && t.length < 60),
  }
}`

type State = { prompt: string | null; media: { tag: string; alt: string; n: string; inCompose: boolean; box: number[] }[]; triggers: string[] }

const show = (label: string, s: State) => {
  console.log(`\n--- ${label} ---`)
  console.log(`prompt box: ${JSON.stringify(s.prompt)}`)
  console.log(`triggers:   ${JSON.stringify(s.triggers)}`)
  console.log(`media (${s.media.length}):`)
  for (const m of s.media) console.log(`   ${m.inCompose ? "COMPOSE" : "canvas "} ${m.tag} alt=${JSON.stringify(m.alt).slice(0, 60)} ${m.n.slice(0, 12)} box=${JSON.stringify(m.box)}`)
}

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: Page
    pointerClick(l: Locator): Promise<void>
    forceClick(l: Locator): Promise<void>
    hoverElement(l: Locator): Promise<void>
  }
  const page = inner.page
  await client.openProject({ id: projectId })
  await page.waitForTimeout(3000)

  const before = (await page.evaluate(`(${STATE})()`)) as State
  show('BEFORE', before)

  // A clip tile renders as `img[alt="Video thumbnail"]` at rest and SWAPS to a (hidden-until-
  // then) `<video>` on hover. So hover the thumbnail, then anchor everything else on the video:
  // the thumbnail is gone from the DOM by the time the card's controls exist, which is why an
  // ancestor xpath rooted on it finds nothing at all. Mapped live 2026-08-12 (smoke-clip-card).
  const thumb = page.locator('img[alt="Video thumbnail"]').first()
  await thumb.waitFor({ state: 'visible', timeout: 30_000 })
  await thumb.scrollIntoViewIfNeeded().catch(() => {})
  await inner.hoverElement(thumb)
  await page.waitForTimeout(1200)

  // Scope to the clip's OWN card, exactly as openAnimateMenu does for stills. `.first()` on the
  // page is the top bar's project menu; `.last()` happens to work in a one-clip project and
  // would silently target the wrong clip in any other.
  const tile = page.locator('video').first()
  const card = tile.locator('xpath=ancestor::div[.//button[contains(., "more_vert")]][1]')
  const more = card.locator('button:has-text("more_vert")').first()
  if (!(await more.count())) throw new Error('no per-clip more_vert — hover did not reveal the card control')
  await inner.pointerClick(more)
  await page.waitForTimeout(800)

  const target = page.getByRole('menuitem', { name: item })
  await target.waitFor({ state: 'visible', timeout: 5_000 })
  await inner.forceClick(target)
  await page.waitForTimeout(3000)

  const after = (await page.evaluate(`(${STATE})()`)) as State
  show(`AFTER ${flag}`, after)

  // Key on tag+alt+id, NOT id alone: attaching a clip that is already on the canvas adds a
  // second node carrying the SAME media id, and an id-keyed diff reports "nothing happened".
  const key = (m: State['media'][number]) => `${m.tag}|${m.alt}|${m.n}`
  const beforeKeys = new Set(before.media.map(key))
  const added = after.media.filter((m) => !beforeKeys.has(key(m)))
  console.log(`\nNEW media nodes after ${flag}: ${added.length}`)
  for (const m of added)
    console.log(`   ${m.inCompose ? 'COMPOSE' : 'canvas '} ${m.tag} alt=${JSON.stringify(m.alt)} ${m.n}`)
  if (before.prompt !== after.prompt) console.log(`PROMPT CHANGED: ${JSON.stringify(after.prompt)}`)
} finally {
  await client.close()
}
