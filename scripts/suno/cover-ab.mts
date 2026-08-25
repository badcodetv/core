/**
 * badcode — run the Camping cover A/B set through Suno's Cover mode.
 *
 * 🔴 COVER MODE IS NOT CREATE MODE. The difference that matters:
 *
 *   The source audio is attached by hand (song page → ⋯ → Remix ▸ Cover) and lives ONLY in the
 *   page. There is no draft recovery and no way to re-attach it from code, so a navigation costs
 *   a manual re-setup. `connect()` in suno.mts only calls goto() when the URL is not already
 *   /create, which is why this script is safe — but nothing here may ever navigate.
 *
 *   The lyrics come WITH the source, and they are the words the SOURCE was generated from —
 *   not necessarily the current ones. On 2026-08-25 that cost a full ten-variation run: the
 *   attached take predated a lyric rewrite, so all twenty takes sang the old words and every
 *   one had to be thrown away. `camping.md` §4 is the source of truth, the page is not, and
 *   `run` now refuses to spend a credit until the two agree.
 *
 *   Whether the attachment survives its own generation is UNVERIFIED — Suno's create form does
 *   survive, but cover mode has never been driven from code here. So the attachment is
 *   re-checked before every Create and the run stops on the first miss rather than quietly
 *   spending nine more credits' worth of ordinary generations.
 *
 * One variable per round: style + excludes move, everything else is pinned.
 *
 *   npx tsx scripts/suno/cover-ab.mts plan          # print the ten boxes, touch nothing
 *   npx tsx scripts/suno/cover-ab.mts check         # read the live form back, spend nothing
 *   npx tsx scripts/suno/cover-ab.mts load <id>     # fill one variation, generate NOTHING
 *   npx tsx scripts/suno/cover-ab.mts run [ids...]  # 10 credits + 2 takes per id
 */
import type { Page } from 'playwright'
import { readFileSync } from 'node:fs'
import { connect, setSlider, setTitle, setLyrics, create, listTakes } from './suno.mts'
import { VARIATIONS, styleFor, excludeFor, titleFor, type Variation } from './cover-variations.mts'

/**
 * Pinned for the whole set — normally the style box is the only thing under test, so the
 * sliders don't move mid-comparison. Overridable via env var for a deliberate sweep (e.g.
 * SUNO_WEIRDNESS=60 SUNO_STYLE_INFLUENCE=75 SUNO_AUDIO_INFLUENCE=15 npx tsx cover-ab.mts run …),
 * which is itself a one-variable-at-a-time round — just with the sliders as the variable
 * instead of the style box.
 */
const WEIRDNESS = Number(process.env.SUNO_WEIRDNESS ?? 30)
const STYLE_INFLUENCE = Number(process.env.SUNO_STYLE_INFLUENCE ?? 50)
const AUDIO_INFLUENCE = Number(process.env.SUNO_AUDIO_INFLUENCE ?? 25)

/** The canonical words. `camping.md` §4 is the source of truth; the attached audio is not. */
const SHEET = new URL('../../docs/stories/camping/songs/camping.md', import.meta.url).pathname

export function sheetLyrics(): string {
  const m = readFileSync(SHEET, 'utf8').match(/```lyrics\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`no \`\`\`lyrics block in ${SHEET}`)
  return m[1]
}

/** Compare on words alone — Lexical normalises trailing spaces, and those are not a difference. */
const shape = (t: string) =>
  t.split('\n').map((l) => l.trim()).filter(Boolean).join('\n')

async function pageLyrics(page: Page): Promise<string> {
  return (await page.evaluate(
    `(() => [...document.querySelectorAll('[contenteditable="true"] p')].map((p) => p.innerText).join('\\n'))()`,
  )) as string
}

/** Read the cover-specific state the ordinary `verify` does not know about. */
async function coverState(page: Page) {
  return page.evaluate(`(() => {
    const c = (s) => (s || '').replace(/\\s+/g, ' ').trim()
    const st = document.querySelector('[data-testid="create-form-styles-wrapper"] textarea')
    const ex = document.querySelector('input[placeholder="Exclude styles"]')
    const body = c(document.body.innerText)
    const m = body.match(/Audio Cover ([^]{0,60}?) \\d\\d:\\d\\d\\/(\\d\\d:\\d\\d)/)
    return {
      url: location.href,
      coverTitle: m ? c(m[1]) : null,
      coverDuration: m ? m[2] : null,
      styleLen: st ? st.value.length : null,
      excludeLen: ex ? ex.value.length : null,
      lyricParas: document.querySelectorAll('[contenteditable="true"] p').length,
      sliders: [...document.querySelectorAll('[role="slider"]')]
        .map((s) => s.getAttribute('aria-label') + '=' + s.getAttribute('aria-valuenow')),
    }
  })()`) as Promise<Record<string, unknown>>
}

/** Everything that must still be true before a Create is worth clicking. */
function guard(s: Record<string, unknown>, paras: number): string[] {
  const bad: string[] = []
  if (!String(s.url).includes('/create')) bad.push(`url is ${s.url} — NOT the create page`)
  if (!s.coverTitle) bad.push('the cover audio is GONE — re-attach by hand (song ⋯ → Remix ▸ Cover)')
  if (s.lyricParas !== paras) bad.push(`lyrics ${s.lyricParas} paragraphs, expected ${paras} — the words moved`)
  return bad
}

/** Fill one variation. Style, excludes and sliders only — the lyrics are never touched. */
async function loadVariation(page: Page, v: Variation, title = titleFor(v)) {
  const style = styleFor(v)
  const exclude = excludeFor(v)
  await page.locator('[data-testid="create-form-styles-wrapper"] textarea').fill(style)
  await page.locator('input[placeholder="Exclude styles"]').first().fill(exclude)
  await setSlider(page, 'Style Influence', STYLE_INFLUENCE)
  await setSlider(page, 'Weirdness', WEIRDNESS)
  await setSlider(page, 'Audio Influence', AUDIO_INFLUENCE)
  await setTitle(page, title)
  const s = await coverState(page)
  const bad: string[] = []
  if (s.styleLen !== style.length) bad.push(`style ${s.styleLen}/${style.length} — truncated at the 1000 cap?`)
  if (s.excludeLen !== exclude.length) bad.push(`exclude ${s.excludeLen}/${exclude.length}`)
  return { state: s, problems: bad }
}

const [cmd, ...ids] = process.argv.slice(2)
// `run <id>x3` — repeat the same variation 3 times, each with a distinct title. Without this,
// `create()` waits for two takes matching the title and would see the FIRST run's takes and
// return immediately, reporting success for a round it never generated.
const requests = (ids.length ? ids : VARIATIONS.map((v) => v.id)).flatMap((raw) => {
  const m = raw.match(/^(.+?)x(\d+)$/)
  const [id, n] = m ? [m[1], Number(m[2])] : [raw, 1]
  const v = VARIATIONS.find((x) => x.id === id)
  if (!v) throw new Error(`unknown variation id: ${id}`)
  return Array.from({ length: n }, (_, i) => ({ v, title: n > 1 ? `${titleFor(v)} #${i + 1}` : titleFor(v) }))
})
const pick = requests.map((r) => r.v)

if (cmd === 'lyrics') {
  // Writing the sheet's words over the ones the source came with. This is the ONLY thing in
  // this workflow that touches the lyrics box, and it is deliberately its own command.
  const { browser, page } = await connect()
  const before = await coverState(page)
  if (!before.coverTitle) {
    console.log('🔴 ABORT — no cover audio attached. Re-attach by hand (song ⋯ → Remix ▸ Cover).')
    await browser.close()
    process.exit(1)
  }
  const want = sheetLyrics()
  console.log(`page ${before.lyricParas} paragraphs → sheet ${shape(want).split('\n').length}`)
  const wrote = await setLyrics(page, want)
  const after = await coverState(page)
  const got = await pageLyrics(page)
  const problems: string[] = []
  // 🔴 Count paragraphs, never characters: a Lexical fill collapses the whole block into one <p>
  // and still reports the right length. For a bracket-cue sheet that destroys the architecture.
  if (after.lyricParas !== wrote) problems.push(`${after.lyricParas} paragraphs, expected ${wrote}`)
  if (shape(got) !== shape(want)) problems.push('the words in the page do not match the sheet')
  if (!after.coverTitle) problems.push('the cover audio did not survive the lyric write')
  console.log(JSON.stringify(after, null, 2))
  console.log(problems.length ? `🔴 ${problems.join(' · ')}` : '✅ lyrics synced from camping.md §4 — nothing generated')
  await browser.close()
  if (problems.length) process.exit(1)
} else if (cmd === 'plan') {
  for (const v of pick) {
    const s = styleFor(v)
    console.log(`\n── ${v.id} · ${v.name} (${s.length}/1000)\n   ${v.thesis}`)
    console.log(`   lift: ${v.lift.length ? v.lift.join(', ') : '(nothing)'} — ${v.liftWhy}`)
    console.log(`\n${s}\n`)
  }
} else if (cmd === 'check') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await coverState(page), null, 2))
  await browser.close()
} else if (cmd === 'load' || cmd === 'run') {
  const { browser, page } = await connect()
  const start = await coverState(page)
  const paras = start.lyricParas as number
  const pre = guard(start, paras)
  if (pre.length) {
    console.log('🔴 ABORT before touching anything:', pre.join(' · '))
    await browser.close()
    process.exit(1)
  }
  // 🔴 The guard that would have saved the first run. The attached audio carries the words it
  // was generated from, which on 2026-08-25 were a rewrite behind the sheet — twenty takes sang
  // the wrong lyrics and every one was binned. Never spend a credit on unverified words again.
  if (shape(await pageLyrics(page)) !== shape(sheetLyrics())) {
    console.log('🔴 ABORT — the words in the page are NOT camping.md §4.')
    console.log('   The attached take carries the lyrics it was generated from, not the current ones.')
    console.log('   Run: npx tsx scripts/suno/cover-ab.mts lyrics')
    await browser.close()
    process.exit(1)
  }
  console.log(`✅ cover attached: "${start.coverTitle}" (${start.coverDuration}) · ${paras} lyric paragraphs, matching camping.md §4`)

  if (cmd === 'load') {
    const { state, problems } = await loadVariation(page, requests[0].v, requests[0].title)
    console.log(JSON.stringify(state, null, 2))
    console.log(problems.length ? `🔴 ${problems.join(' · ')}` : '✅ loaded — nothing generated')
  } else {
    const done: string[] = []
    for (const [i, { v, title }] of requests.entries()) {
      console.log(`\n──────── ${i + 1}/${requests.length}  ${title}`)
      const { state, problems } = await loadVariation(page, v, title)
      const bad = [...problems, ...guard(state, paras)]
      if (bad.length) {
        console.log('🔴 STOPPING — nothing spent on this round:', bad.join(' · '))
        break
      }
      console.log(`   ${state.sliders} · style ${state.styleLen} · exclude ${state.excludeLen}`)
      console.log(`   ▶ ${await create(page, title)}`)
      done.push(title)
      // Re-check straight after: if the Create consumed the attachment, the next round would be
      // an ordinary generation wearing a cover's title, which is worse than a failure.
      const after = await coverState(page)
      if (!after.coverTitle) {
        console.log('🔴 THE COVER AUDIO DID NOT SURVIVE THE GENERATION — stopping here.')
        console.log('   Re-attach by hand and re-run with the remaining ids.')
        break
      }
    }
    console.log(`\n✅ generated: ${done.join(', ') || '(none)'}`)
    console.log(JSON.stringify(await listTakes(page, 'Camping cover'), null, 2))
  }
  await browser.close()
} else {
  console.log(`badcode cover-ab — the Camping cover A/B set. Pinned: W=${WEIRDNESS} SI=${STYLE_INFLUENCE} AI=${AUDIO_INFLUENCE}

  lyrics          write camping.md §4 into the page, generate NOTHING
  plan            print the ten style boxes, touch nothing
  check           read the live cover form back, spend nothing
  load <id>       fill one variation, generate NOTHING
  run [ids...]    Create each in turn — 10 credits and 2 takes per id
                  repeat one: \`run cover-11-dub-guitarx3\` — 3 separate Creates, titles suffixed #1 #2 #3
                  sweep sliders: SUNO_WEIRDNESS=60 SUNO_STYLE_INFLUENCE=75 SUNO_AUDIO_INFLUENCE=15 npx tsx cover-ab.mts run …

${VARIATIONS.map((v) => `  ${v.id.padEnd(22)} ${v.name}`).join('\n')}`)
}
