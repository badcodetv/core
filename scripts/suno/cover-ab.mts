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
 *   The lyrics come WITH the source and are never written. As of 2026-08-25 the words in the
 *   page are AHEAD of camping.md §4, so writing the sheet's lyrics in would silently downgrade
 *   the track. This script asserts the paragraph count is unchanged before every Create and
 *   aborts if it moved.
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
import { connect, setSlider, setTitle, create, listTakes } from './suno.mts'
import { VARIATIONS, styleFor, excludeFor, titleFor, type Variation } from './cover-variations.mts'

/** Pinned for the whole set. The variable under test is the style box, and nothing else. */
const WEIRDNESS = 30
const STYLE_INFLUENCE = 50
const AUDIO_INFLUENCE = 25

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
async function loadVariation(page: Page, v: Variation) {
  const style = styleFor(v)
  const exclude = excludeFor(v)
  await page.locator('[data-testid="create-form-styles-wrapper"] textarea').fill(style)
  await page.locator('input[placeholder="Exclude styles"]').first().fill(exclude)
  await setSlider(page, 'Style Influence', STYLE_INFLUENCE)
  await setSlider(page, 'Weirdness', WEIRDNESS)
  await setSlider(page, 'Audio Influence', AUDIO_INFLUENCE)
  await setTitle(page, titleFor(v))
  const s = await coverState(page)
  const bad: string[] = []
  if (s.styleLen !== style.length) bad.push(`style ${s.styleLen}/${style.length} — truncated at the 1000 cap?`)
  if (s.excludeLen !== exclude.length) bad.push(`exclude ${s.excludeLen}/${exclude.length}`)
  return { state: s, problems: bad }
}

const [cmd, ...ids] = process.argv.slice(2)
const pick = ids.length ? VARIATIONS.filter((v) => ids.includes(v.id)) : VARIATIONS

if (cmd === 'plan') {
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
  console.log(`✅ cover attached: "${start.coverTitle}" (${start.coverDuration}) · ${paras} lyric paragraphs`)

  if (cmd === 'load') {
    const { state, problems } = await loadVariation(page, pick[0])
    console.log(JSON.stringify(state, null, 2))
    console.log(problems.length ? `🔴 ${problems.join(' · ')}` : '✅ loaded — nothing generated')
  } else {
    const done: string[] = []
    for (const [i, v] of pick.entries()) {
      console.log(`\n──────── ${i + 1}/${pick.length}  ${titleFor(v)}`)
      const { state, problems } = await loadVariation(page, v)
      const bad = [...problems, ...guard(state, paras)]
      if (bad.length) {
        console.log('🔴 STOPPING — nothing spent on this round:', bad.join(' · '))
        break
      }
      console.log(`   ${state.sliders} · style ${state.styleLen} · exclude ${state.excludeLen}`)
      console.log(`   ▶ ${await create(page, titleFor(v))}`)
      done.push(v.id)
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

  plan            print the ten style boxes, touch nothing
  check           read the live cover form back, spend nothing
  load <id>       fill one variation, generate NOTHING
  run [ids...]    Create each in turn — 10 credits and 2 takes per id

${VARIATIONS.map((v) => `  ${v.id.padEnd(22)} ${v.name}`).join('\n')}`)
}
