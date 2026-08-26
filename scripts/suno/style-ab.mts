/**
 * badcode — run the Camping STYLE set through ordinary Create mode. Nothing attached.
 *
 * This is a SCOUTING round, not an A/B: every input moves per variation — My Taste, Style,
 * Exclude Styles, the lyric cues, and both sliders. See `style-variations.mts` for why that is
 * the right trade this time and what it costs.
 *
 * 🔴 THE INVERTED GUARD. `cover-ab.mts` aborts when the cover audio is MISSING. This aborts when
 *    it is PRESENT. A leftover attachment from a cover session would silently turn all seven of
 *    these into covers of the record we are explicitly trying to escape, and every take would
 *    come back sounding right-ish and prove nothing.
 *
 * 🔴 MY TASTE IS ACCOUNT-WIDE AND CANNOT BE TURNED OFF. It is not a per-song input; it is global
 *    state that outlives the run and affects every other sheet in the account. So:
 *      - `taste-backup` saves the live text to disk BEFORE anything writes to it,
 *      - `run` refuses to start without that backup on disk,
 *      - `taste-restore` puts it back, and the end of a run reminds you to.
 *    `setTaste` was never verified (automation.md), so every write here is read back with
 *    `getTaste` and the run stops on a mismatch rather than generating against an unknown global.
 *
 * 🔴 THE WORDS NEVER CHANGE. Variations rewrite the bracket CUES — the only section-scoped box
 *    we have — but `applyCues` asserts that stripping every `[...]` line from the result gives
 *    back camping.md §4 exactly. A cue key that is not found in the sheet is a hard error, so a
 *    drifting sheet fails loudly instead of silently no-opping.
 *
 *   npx tsx scripts/suno/style-ab.mts plan            # print the seven boxes, touch nothing
 *   npx tsx scripts/suno/style-ab.mts check           # read the live form back, spend nothing
 *   npx tsx scripts/suno/style-ab.mts taste-backup    # save the house My Taste to disk
 *   npx tsx scripts/suno/style-ab.mts taste-restore   # put it back
 *   npx tsx scripts/suno/style-ab.mts load <id>       # fill one variation whole, generate NOTHING
 *   npx tsx scripts/suno/style-ab.mts run [ids...]    # 10 credits + 2 takes per id
 */
import type { Page } from 'playwright'
import { readFileSync, writeFileSync, existsSync } from 'node:fs'
import {
  connect, setSlider, setTitle, setLyrics, setDuration, setWorkspace, setTaste, getTaste, create, listTakes,
} from './suno.mts'
import { VARIATIONS, styleFor, excludeFor, titleFor, type Variation } from './style-variations.mts'

// Duration is the one input NOT varied: rounds 13-14 targeted 200s and got 4:07-4:24 back, so it
// is a suggestion Suno mostly ignores and varying it would add noise without adding range.
const DURATION_SEC = process.env.SUNO_DURATION_SEC ? Number(process.env.SUNO_DURATION_SEC) : 200
const WORKSPACE = process.env.SUNO_WORKSPACE ?? 'camping-duet'

const SHEET = new URL('../../docs/stories/camping/songs/camping.md', import.meta.url).pathname
const BACKUP = new URL('./.my-taste-backup.txt', import.meta.url).pathname

export function sheetLyrics(): string {
  const m = readFileSync(SHEET, 'utf8').match(/```lyrics\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`no \`\`\`lyrics block in ${SHEET}`)
  return m[1]
}

/** Compare on words alone — Lexical normalises trailing spaces, and those are not a difference. */
const shape = (t: string) => t.split('\n').map((l) => l.trim()).filter(Boolean).join('\n')

/** Every bracket line stripped. This is what must never change between variations. */
const wordsOnly = (t: string) => shape(t).split('\n').filter((l) => !l.startsWith('[')).join('\n')

/**
 * Rewrite the cues for one variation. Two assertions, both of which have to hold or we are not
 * running the song we think we are: every key must actually appear in the sheet, and the words
 * left after stripping the brackets must be byte-identical to the sheet's.
 */
export function applyCues(v: Variation): string {
  const base = sheetLyrics()
  let out = base
  for (const [from, to] of Object.entries(v.cues)) {
    if (!out.includes(from)) throw new Error(`${v.id}: cue key not found in camping.md §4 — ${JSON.stringify(from)}`)
    out = out.split(from).join(to)
  }
  if (wordsOnly(out) !== wordsOnly(base)) throw new Error(`${v.id}: a cue rewrite changed the WORDS — refusing`)
  return out
}

async function formState(page: Page) {
  return page.evaluate(`(() => {
    const c = (s) => (s || '').replace(/\\s+/g, ' ').trim()
    const st = document.querySelector('[data-testid="create-form-styles-wrapper"] textarea')
    const ex = document.querySelector('input[placeholder="Exclude styles"]')
    const m = c(document.body.innerText).match(/Audio Cover ([^]{0,60}?) \\d\\d:\\d\\d\\/(\\d\\d:\\d\\d)/)
    return {
      url: location.href,
      coverTitle: m ? c(m[1]) : null,
      styleLen: st ? st.value.length : null,
      excludeLen: ex ? ex.value.length : null,
      lyricParas: document.querySelectorAll('[contenteditable="true"] p').length,
      sliders: [...document.querySelectorAll('[role="slider"]')]
        .map((s) => s.getAttribute('aria-label') + '=' + s.getAttribute('aria-valuenow')),
    }
  })()`) as Promise<Record<string, unknown>>
}

async function pageLyrics(page: Page): Promise<string> {
  return (await page.evaluate(
    `(() => [...document.querySelectorAll('[contenteditable="true"] p')].map((p) => p.innerText).join('\\n'))()`,
  )) as string
}

/**
 * Fill a React-controlled input and prove it took.
 *
 * 🔴 The exclude box truncates. Seen four times now, EVERY time on the second variation of a
 * multi-id run, at 117/831, 169/871 and 180/695 — the kept prefix length varies, which reads
 * like a stale React state value winning a race against `.fill()` rather than a maxlength.
 * A blur between the clear and the refill settles it. The guard downstream is still the thing
 * that makes a bad fill free; this just stops it costing a re-run.
 */
async function fillChecked(page: Page, selector: string, text: string, tries = 4): Promise<string> {
  const el = page.locator(selector).first()
  for (let i = 1; i <= tries; i++) {
    await el.fill('')
    await el.blur().catch(() => {})
    await page.waitForTimeout(150)
    await el.fill(text)
    await el.blur().catch(() => {})
    await page.waitForTimeout(250)
    const got = await el.inputValue().catch(async () => (await el.textContent()) ?? '')
    if (got.length === text.length) return i === 1 ? 'ok' : `ok (retry ${i})`
    if (i === tries) return `🔴 ${got.length}/${text.length} after ${tries} tries`
  }
  return 'unreachable'
}

/** Load one variation WHOLE — taste, style, excludes, cues, sliders, title. */
async function loadVariation(page: Page, v: Variation, title = titleFor(v)) {
  const style = styleFor(v)
  const exclude = excludeFor(v)
  const lyrics = applyCues(v)
  const bad: string[] = []

  // My Taste first: it is the slowest control (a modal behind the profile menu) and the one
  // whose failure invalidates everything after it, so fail before spending time on the rest.
  console.log(`   ${await setTaste(page, v.taste)}`)
  const got = await getTaste(page)
  if (shape(got ?? '') !== shape(v.taste)) bad.push(`🔴 My Taste did not take — read back ${got?.length ?? 'null'} chars, wanted ${v.taste.length}`)

  const fills = [
    await fillChecked(page, '[data-testid="create-form-styles-wrapper"] textarea', style),
    await fillChecked(page, 'input[placeholder="Exclude styles"]', exclude),
  ]
  if (fills.some((f) => f.startsWith('🔴'))) bad.push(`fill: ${fills.join(' · ')}`)
  else if (fills.some((f) => f.includes('retry'))) console.log(`   fill: ${fills.join(' · ')}`)
  const paras = await setLyrics(page, lyrics)
  await setSlider(page, 'Style Influence', v.styleInfluence)
  await setSlider(page, 'Weirdness', v.weirdness)
  if (DURATION_SEC) await setDuration(page, DURATION_SEC)
  await setTitle(page, title)

  const s = await formState(page)
  if (s.styleLen !== style.length) bad.push(`style ${s.styleLen}/${style.length} — truncated at the 1000 cap?`)
  // Seen twice in the cover set on the SECOND variation of a multi-id run, at 117/831 and
  // 169/871: the exclude fill comes back short. Cause unconfirmed. The check is what makes it
  // free — it stops before Create, and the fix is re-running that one id alone.
  if (s.excludeLen !== exclude.length) bad.push(`exclude ${s.excludeLen}/${exclude.length} — the known truncation; retry this id alone`)
  // 🔴 Count paragraphs, never characters: a Lexical fill collapses the block into one <p> and
  // still reports the right length, which for a bracket-cue sheet destroys the architecture.
  if (s.lyricParas !== paras) bad.push(`lyrics ${s.lyricParas} paragraphs, expected ${paras}`)
  if (shape(await pageLyrics(page)) !== shape(lyrics)) bad.push('the words in the page do not match the cue-rewritten sheet')
  if (s.coverTitle) bad.push(`🔴 AUDIO IS ATTACHED ("${s.coverTitle}") — this would be a cover, not a creation`)
  if (!String(s.url).includes('/create')) bad.push(`url is ${s.url} — NOT the create page`)
  return { state: s, problems: bad }
}

// Only dispatch when run directly — importing this for its `applyCues` would otherwise print
// the usage banner into the caller's stdout, which silently corrupts a piped JSON dump.
const IS_CLI = !!process.argv[1] && /style-ab\.mts$/.test(process.argv[1])
const [cmd, ...ids] = IS_CLI ? process.argv.slice(2) : ['__imported__']
// `run <id>x3` — repeat one variation 3 times under distinct titles. Without the suffix,
// `create()` matches the FIRST run's takes and returns instantly, reporting a success it never ran.
const requests = (ids.length ? ids : VARIATIONS.map((v) => v.id)).flatMap((raw) => {
  const m = raw.match(/^(.+?)x(\d+)$/)
  const [id, n] = m ? [m[1], Number(m[2])] : [raw, 1]
  const v = VARIATIONS.find((x) => x.id === id)
  if (!v) throw new Error(`unknown variation id: ${id}`)
  return Array.from({ length: n }, (_, i) => ({ v, title: n > 1 ? `${titleFor(v)} #${i + 1}` : titleFor(v) }))
})

if (cmd === 'plan') {
  for (const { v } of requests) {
    const s = styleFor(v)
    const cues = applyCues(v)           // throws here if a key drifted — cheap, offline, no browser
    const changed = cues.split('\n').filter((l, i) => l !== sheetLyrics().split('\n')[i]).length
    console.log(`\n── ${v.id} · ${v.name}   W=${v.weirdness} SI=${v.styleInfluence}`)
    console.log(`   style ${s.length}/1000 · exclude ${excludeFor(v).length} · taste ${v.taste.length}/2000 · ${changed} cue lines rewritten`)
    console.log(`   ${v.thesis}`)
    console.log(`   lift: ${v.lift.length ? v.lift.join(', ') : '(nothing)'}\n   why: ${v.liftWhy}`)
    console.log(`\n${s}\n`)
  }
} else if (cmd === 'cues') {
  // Print one variation's rewritten bracket lines side by side with the sheet's. Offline.
  const v = requests[0].v
  const a = sheetLyrics().split('\n')
  const b = applyCues(v).split('\n')
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) console.log(`- ${a[i]}\n+ ${b[i]}\n`)
} else if (cmd === 'check') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await formState(page), null, 2))
  console.log(`My Taste (live): ${(await getTaste(page))?.slice(0, 140)}…`)
  await browser.close()
} else if (cmd === 'taste-backup') {
  const { browser, page } = await connect()
  const live = await getTaste(page)
  if (!live) {
    console.log('🔴 could not read My Taste — nothing saved, do NOT run')
    await browser.close()
    process.exit(1)
  }
  writeFileSync(BACKUP, live)
  console.log(`✅ saved ${live.length} chars to ${BACKUP}\n\n${live.slice(0, 300)}…`)
  await browser.close()
} else if (cmd === 'taste-restore') {
  if (!existsSync(BACKUP)) throw new Error(`no backup at ${BACKUP} — nothing to restore`)
  const want = readFileSync(BACKUP, 'utf8')
  const { browser, page } = await connect()
  console.log(await setTaste(page, want))
  const got = await getTaste(page)
  console.log(shape(got ?? '') === shape(want) ? `✅ house My Taste restored (${want.length} chars)` : '🔴 restore did NOT take — fix by hand')
  await browser.close()
} else if (cmd === 'load' || cmd === 'run') {
  if (!existsSync(BACKUP)) {
    console.log(`🔴 ABORT — no My Taste backup at ${BACKUP}.`)
    console.log('   My Taste is account-wide and this run overwrites it seven times.')
    console.log('   Run: npx tsx scripts/suno/style-ab.mts taste-backup')
    process.exit(1)
  }
  const { browser, page } = await connect()
  const start = await formState(page)
  if (start.coverTitle) {
    console.log(`🔴 ABORT — audio is attached ("${start.coverTitle}"). Remove it in the page; this would be a cover.`)
    await browser.close()
    process.exit(1)
  }
  console.log(`✅ nothing attached · house My Taste backed up (${readFileSync(BACKUP, 'utf8').length} chars)`)
  console.log(await setWorkspace(page, WORKSPACE))

  const done: string[] = []
  for (const [i, { v, title }] of requests.entries()) {
    console.log(`\n──────── ${i + 1}/${requests.length}  ${title}`)
    const { state, problems } = await loadVariation(page, v, title)
    if (problems.length) {
      console.log('🔴 STOPPING — nothing spent on this round:', problems.join(' · '))
      break
    }
    console.log(`   ${state.sliders} · style ${state.styleLen} · exclude ${state.excludeLen} · ${state.lyricParas} paras`)
    if (cmd === 'load') {
      console.log('✅ loaded whole — nothing generated')
      break
    }
    console.log(`   ▶ ${await create(page, title)}`)
    done.push(title)
  }
  if (cmd === 'run') {
    console.log(`\n✅ generated: ${done.join(', ') || '(none)'}`)
    console.log(JSON.stringify(await listTakes(page, 'Camping '), null, 2))
    console.log('\n🔴 My Taste is still set to the LAST variation and is account-wide.')
    console.log('   Run: npx tsx scripts/suno/style-ab.mts taste-restore')
  }
  await browser.close()
} else if (IS_CLI) {
  console.log(`badcode style-ab — the Camping non-cover scouting set. Every input varies per row. Duration pinned ${DURATION_SEC}s → ${WORKSPACE}

  plan            print the seven boxes + cue counts, touch nothing
  cues <id>       diff one variation's bracket cues against camping.md §4, offline
  check           read the live form and My Taste back, spend nothing
  taste-backup    save the house My Taste to disk — REQUIRED before run
  taste-restore   put the house My Taste back
  load <id>       fill one variation whole, generate NOTHING
  run [ids...]    Create each in turn — 10 credits and 2 takes per id

${VARIATIONS.map((v) => `  ${v.id.padEnd(22)} W=${String(v.weirdness).padEnd(3)} SI=${String(v.styleInfluence).padEnd(3)} ${v.name}`).join('\n')}`)
}
