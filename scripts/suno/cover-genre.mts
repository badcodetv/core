/**
 * badcode — genre-overlay experiments on the attached Camping cover take.
 *
 * 🔴 COVER MODE. The source audio is attached BY HAND (song page → ⋯ → Remix ▸ Cover) and lives
 *    only in the page — see camping-halftime-cover.md §6 and cover-ab.mts's header for the full
 *    rules this reuses: never navigate, the attachment carries its own lyrics (checked against
 *    camping.md §4 before every run), the attachment is re-verified after every Create.
 *
 * 🔴 MY TASTE IS ACCOUNT-WIDE. Same discipline as halftime.mts: backed up before writing,
 *    restored after. `run` refuses to start without a backup on disk.
 *
 * The LANES live in the sheet (camping-halftime-cover.md §2), one fenced style box each under a
 * `**Lane X — <name> (<n> chars).**` header — add a lane by editing the markdown, not this file.
 * Lane is the variable; Weirdness is pinned and Audio Influence swept, Style Influence at 75.
 *
 *   npx tsx scripts/suno/cover-genre.mts plan [ids...]
 *   npx tsx scripts/suno/cover-genre.mts check
 *   npx tsx scripts/suno/cover-genre.mts taste-release | taste-restore
 *   npx tsx scripts/suno/cover-genre.mts run [ids...]
 */
import type { Page } from 'playwright'
import { readFileSync, writeFileSync, existsSync } from 'node:fs'
import {
  connect, setSlider, setTitle, setDuration, setLyrics, setTaste, getTaste, setWorkspace, verify, create, listTakes,
  tasteOwner, releaseTaste, TASTE_FREE,
} from './suno.mts'

const SHEET = new URL('../../docs/stories/camping/songs/camping-halftime-cover.md', import.meta.url).pathname
const CANON = new URL('../../docs/stories/camping/songs/camping.md', import.meta.url).pathname
const PARENT = new URL('../../docs/stories/camping/songs/camping-halftime.md', import.meta.url).pathname
const BACKUP = new URL('./.my-taste-backup.txt', import.meta.url).pathname
const WORKSPACE = process.env.SUNO_WORKSPACE ?? 'camping-duet'
const STYLE_INFLUENCE = 75

function block(md: string, heading: string): string {
  const i = md.indexOf(`## ${heading}`)
  if (i === -1) throw new Error(`${SHEET}: no section "## ${heading}"`)
  const rest = md.slice(i)
  const end = rest.search(/\n## /)
  const m = (end === -1 ? rest : rest.slice(0, end)).match(/\n```[a-z]*\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`${SHEET}: no fenced block under "## ${heading}"`)
  return m[1]
}

const md = readFileSync(SHEET, 'utf8')
const EXCLUDE = block(md, '3. Exclude Styles')

/**
 * The lanes, read out of §2 in document order. Each is introduced by a bold
 * `**Lane X — <name> (<n> chars).**` line followed (eventually) by its fenced style box, so the
 * sheet stays the single source of truth and adding a lane is a markdown edit, not a code edit.
 */
function lanes(): { key: string; name: string; style: string; taste: string }[] {
  const i = md.indexOf('## 2. Style')
  const j = md.indexOf('\n## 3. Exclude', i)
  if (i === -1 || j === -1) throw new Error(`${SHEET}: could not find "## 2. Style" … "## 3. Exclude"`)
  const section = md.slice(i, j)
  // Split on the lane headers so a header and the fences under it stay together.
  const parts = section.split(/\*\*Lane [A-Z] — /).slice(1)
  const out = parts.map((p) => {
    const name = p.slice(0, p.indexOf(' (')).trim()
    const style = p.match(/```\n([\s\S]*?)\n```/)
    const taste = p.match(/```taste\n([\s\S]*?)\n```/)
    if (!style) throw new Error(`${SHEET}: lane "${name}" has no fenced style box`)
    // 🔴 THE FOUR-BOX ATOM (Kai, 2026-08-27). A style is My Taste + Style + Exclude + Lyrics, and
    //    they move together or not at all. My Taste is account-wide and invisible from the create
    //    page, so it is always the box left behind — which is exactly how fourteen Camping rounds
    //    ran under the GPOM newsreader profile. No silent shared fallback: a lane without its own
    //    taste is a broken lane and throws here, offline, before a credit is spent.
    if (!taste) throw new Error(`${SHEET}: lane "${name}" has no \`\`\`taste fence — the four-box atom requires one per lane`)
    return { key: name.split(' ')[0].toLowerCase().replace(/[^a-z]/g, ''), name, style: style[1], taste: taste[1] }
  })
  if (!out.length) throw new Error(`${SHEET}: no "**Lane X — …**" headers found under "## 2. Style"`)
  return out
}

/** The lyrics the attached source was generated from — §4 of the parent half-time sheet. */
function sourceLyrics(): string {
  const p = readFileSync(PARENT, 'utf8')
  const i = p.indexOf('## 4. Lyrics')
  if (i === -1) throw new Error(`${PARENT}: no "## 4. Lyrics"`)
  const rest = p.slice(i)
  const end = rest.search(/\n## /)
  const m = (end === -1 ? rest : rest.slice(0, end)).match(/\n```[a-z]*\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`${PARENT}: no fenced block under "## 4. Lyrics"`)
  return m[1]
}
const LANES = lanes()

/**
 * 🔴 BUMP `SET` EVERY ROUND. `create()` waits for two takes whose title matches, so a round that
 *    reuses a previous round's title matches the OLD takes and reports a success it never
 *    generated. c3 re-runs post-punk at AI 10/25 — two of its six (AI10 W45, AI25 W45) are
 *    byte-identical to c2's titles without this suffix.
 */
const SET = ' (c4)'

/**
 * The round: which lanes, and the slider grid over them. c2 swept lane with Weirdness pinned;
 * c3 narrows to the lane Kai picked and opens Weirdness up instead — one variable moves at a
 * time across rounds, which is the whole method.
 */
const ROUND = {
  lanes: ['flair'],
  audioInfluences: [10, 25],
  weirdnesses: [30, 45, 60],
}

interface Variation { id: string; lane: (typeof LANES)[number]; audioInfluence: number; weirdness: number }
const VARIATIONS: Variation[] = LANES.filter((l) => ROUND.lanes.includes(l.key)).flatMap((lane) =>
  ROUND.audioInfluences.flatMap((ai) =>
    ROUND.weirdnesses.map((w) => ({ id: `${lane.key}-ai${ai}-w${w}`, lane, audioInfluence: ai, weirdness: w })),
  ),
)
if (!VARIATIONS.length) {
  throw new Error(`no lanes matched ${JSON.stringify(ROUND.lanes)} — the sheet has: ${LANES.map((l) => l.key).join(', ')}`)
}
const titleFor = (v: Variation) => `Camping cover - ${v.lane.name} AI${v.audioInfluence} W${v.weirdness}${SET}`

const shape = (t: string) => t.split('\n').map((l) => l.trim()).filter(Boolean).join('\n')
const wordsOnly = (t: string) => shape(t).split('\n').filter((l) => !l.startsWith('[')).join('\n')

function canonWords(): string {
  const m = readFileSync(CANON, 'utf8').match(/```lyrics\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`no \`\`\`lyrics block in ${CANON}`)
  return wordsOnly(m[1])
}

async function pageLyrics(page: Page): Promise<string> {
  return (await page.evaluate(
    `(() => [...document.querySelectorAll('[contenteditable="true"] p')].map((p) => p.innerText).join('\\n'))()`,
  )) as string
}

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
      // 🔴 THE ATTACHED VOICE. With none attached the control reads exactly "Voice"; attaching
      //    one puts the persona's NAME there instead. A Voice overrides the vocal casting
      //    outright, so an inherited one silently replaces the two men this sheet casts — which
      //    is what happened on 2026-08-27, when 'badcode newsreader' was left attached from
      //    another session. Read it, never assume it.
      voice: (() => {
        const b = [...document.querySelectorAll('button[aria-label="Add Voice"]')].filter((x) => x.offsetParent !== null)[0]
        return b ? c(b.innerText) : null
      })(),
      sliders: [...document.querySelectorAll('[role="slider"]')]
        .map((s) => s.getAttribute('aria-label') + '=' + s.getAttribute('aria-valuenow')),
    }
  })()`) as Promise<Record<string, unknown>>
}

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

/**
 * The Voice this sheet expects. `null` means NONE — the casting lives in the Style box and My
 * Taste, and an attached persona would override it. A sheet that wants a Voice names it here.
 */
const EXPECT_VOICE: string | null = null
/** The control's label when nothing is attached. Anything else is a persona's name. */
const NO_VOICE = 'Voice'

function guard(s: Record<string, unknown>, paras: number): string[] {
  const bad: string[] = []
  if (!String(s.url).includes('/create')) bad.push(`url is ${s.url} — NOT the create page`)
  if (!s.coverTitle) bad.push('the cover audio is GONE — re-attach by hand (song ⋯ → Remix ▸ Cover)')
  if (s.lyricParas !== paras) bad.push(`lyrics ${s.lyricParas} paragraphs, expected ${paras} — the words moved`)
  // 🔴 A leaked Voice is the worst of the inherited-state bugs: it silently replaces the casting
  //    this whole sheet is built on, and nothing in the output says so.
  const want = EXPECT_VOICE ?? NO_VOICE
  if (s.voice !== want) {
    bad.push(
      EXPECT_VOICE
        ? `🔴 Voice reads "${s.voice}", expected "${EXPECT_VOICE}"`
        : `🔴 A VOICE IS ATTACHED ("${s.voice}") and this sheet casts its voices in the Style box — remove it in the create form`,
    )
  }
  // 🔴 DURATION. On Auto the slider is absent; a mounted one is a custom length someone else set,
  //    and it silently rewrites how long every take is (c3c: 3:59–4:00 against 3:10–3:44 on Auto).
  const dur = (s.sliders as string[]).find((x) => x.startsWith('Duration='))
  if (DURATION_SEC === null && dur) bad.push(`🔴 Duration is pinned (${dur}) — this sheet runs on Auto; clear it in More Options`)
  if (DURATION_SEC !== null && dur !== `Duration=${DURATION_SEC}`) bad.push(`🔴 Duration reads ${dur ?? 'Auto'}, expected ${DURATION_SEC}`)
  return bad
}

/**
 * 🔴 DURATION — AUTO, AND ASSERTED AS AUTO.
 *
 *    The claim this constant used to carry ("240 is a ceiling that does not bind") is FALSE, and
 *    c3c is the evidence: all twelve of its takes came back 3:59–4:00 against 3:10–3:44 on Auto in
 *    every earlier round. The control does not behave like a ceiling — it behaves like a target,
 *    and it stretches as readily as it shortens. Pinning it to 240 padded ~45s of invented
 *    material into a cover of a 3:14 source and made c3c non-comparable to everything before it.
 *
 *    So the declared state is Auto, which on this page means the slider is NOT MOUNTED AT ALL.
 *    That is still a declaration under the inheritance-is-a-bug rule, and it is still asserted:
 *    a mounted Duration slider means someone set a custom length and the guard aborts. Set this
 *    to a number only for a sheet that genuinely wants a fixed length.
 */
const DURATION_SEC: number | null = null

async function loadVariation(page: Page, v: Variation, title = titleFor(v)) {
  const style = v.lane.style
  const bad: string[] = []

  // My Taste FIRST and per-variation — the four-box atom. It is account-wide, so a concurrent
  // session (or the previous lane) can have moved it since the last Create; writing it once
  // before the loop is exactly the gap that let the GPOM profile sit under fourteen rounds.
  await setTaste(page, v.lane.taste)
  const gotTaste = await getTaste(page)
  if (shape(gotTaste ?? '') !== shape(v.lane.taste)) {
    bad.push(`🔴 My Taste did not take — read back ${gotTaste?.length ?? 'null'}, wanted ${v.lane.taste.length}`)
  }

  const fills = [
    await fillChecked(page, '[data-testid="create-form-styles-wrapper"] textarea', style),
    await fillChecked(page, 'input[placeholder="Exclude styles"]', EXCLUDE),
  ]
  await setSlider(page, 'Style Influence', STYLE_INFLUENCE)
  await setSlider(page, 'Weirdness', v.weirdness)
  await setSlider(page, 'Audio Influence', v.audioInfluence)
  if (DURATION_SEC !== null) await setDuration(page, DURATION_SEC)
  await setTitle(page, title)
  const s = await coverState(page)
  if (fills.some((f) => f.startsWith('🔴'))) bad.push(`fill: ${fills.join(' · ')}`)
  if (s.styleLen !== style.length) bad.push(`style ${s.styleLen}/${style.length} — truncated at the 1000 cap?`)
  if (s.excludeLen !== EXCLUDE.length) bad.push(`exclude ${s.excludeLen}/${EXCLUDE.length}`)
  return { state: s, problems: bad }
}

const [cmd, ...ids] = process.argv.slice(2)
const requests = (ids.length ? ids : VARIATIONS.map((v) => v.id)).flatMap((raw) => {
  const m = raw.match(/^(.+?)x(\d+)$/)
  const [id, n] = m ? [m[1], Number(m[2])] : [raw, 1]
  const v = VARIATIONS.find((x) => x.id === id)
  if (!v) throw new Error(`unknown variation id: ${id}`)
  return Array.from({ length: n }, (_, i) => ({ v, title: n > 1 ? `${titleFor(v)} #${i + 1}` : titleFor(v) }))
})

if (cmd === 'plan') {
  for (const v of VARIATIONS) {
    const s = v.lane.style
    console.log(`\n── ${v.id}   AI=${v.audioInfluence} W=${v.weirdness} SI=${STYLE_INFLUENCE}`)
    console.log(`   lane: ${v.lane.name}`)
    console.log(`   style ${s.length}/1000${s.length > 1000 ? ' 🔴 OVER THE CAP' : ''} · exclude ${EXCLUDE.length} · taste ${v.lane.taste.length}/2000`)
  }
} else if (cmd === 'check') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await coverState(page), null, 2))
  console.log(`My Taste (live): ${(await getTaste(page))?.slice(0, 140)}…`)
  await browser.close()
} else if (cmd === 'lyrics') {
  // 🔴 REPAIR ONLY. Cover mode inherits its words from the attached source and nothing in the
  //    normal flow touches this box. It exists because a concurrent Suno session overwrote the
  //    lyrics box on 2026-08-27 while the cover audio itself survived — so the attachment was
  //    fine and only the words needed putting back. Re-doing Remix ▸ Cover by hand also works.
  const { browser, page } = await connect()
  const before = await coverState(page)
  if (!before.coverTitle) {
    console.log('🔴 ABORT — no cover audio attached. Re-attach by hand (song ⋯ → Remix ▸ Cover).')
    await browser.close()
    process.exit(1)
  }
  const want = sourceLyrics()
  const wrote = await setLyrics(page, want)
  const after = await coverState(page)
  const got = await pageLyrics(page)
  const problems: string[] = []
  // 🔴 Count paragraphs, never characters: a Lexical fill collapses the block into one <p> and
  // still reports the right length, which for a cue sheet destroys the architecture.
  if (after.lyricParas !== wrote) problems.push(`${after.lyricParas} paragraphs, expected ${wrote}`)
  if (wordsOnly(got) !== canonWords()) problems.push('the words in the page do not match camping.md §4')
  if (!after.coverTitle) problems.push('the cover audio did not survive the lyric write')
  console.log(`page ${before.lyricParas} paragraphs → wrote ${wrote}`)
  console.log(problems.length ? `🔴 ${problems.join(' · ')}` : '✅ lyrics restored from camping-halftime.md §4 — nothing generated')
  await browser.close()
  if (problems.length) process.exit(1)
} else if (cmd === 'taste-release') {
  // The ONLY sanctioned way to take the box off whoever holds it: back up what is there (so a
  // real profile is never destroyed unrecoverably), then write the freedom token. Run this after
  // confirming with the human that the current profile is finished with.
  const { browser, page } = await connect()
  const live = await getTaste(page)
  if (live && live.trim() !== TASTE_FREE) {
    writeFileSync(BACKUP, live)
    console.log(`backed up ${live.length} chars to ${BACKUP}`)
  }
  console.log(await releaseTaste(page))
  await browser.close()
} else if (cmd === 'taste-restore') {
  // Escape hatch: put back whatever taste-release last displaced. Rarely needed — the freedom
  // token, not a saved profile, is what a finished round should leave behind.
  if (!existsSync(BACKUP)) throw new Error(`no backup at ${BACKUP} — nothing to restore`)
  const want = readFileSync(BACKUP, 'utf8')
  const { browser, page } = await connect()
  console.log(await setTaste(page, want))
  const got = await getTaste(page)
  console.log(shape(got ?? '') === shape(want) ? `✅ restored the backed-up profile (${want.length} chars)` : '🔴 restore did NOT take — fix by hand')
  await browser.close()
} else if (cmd === 'run') {
  const { browser, page } = await connect()

  // 🔴 GATE 1 — CLAIM. My Taste must read the freedom token, meaning nobody owns it. Anything
  //    else is another session's or a human's profile and loading over it is how four separate
  //    silent failures happened on 2026-08-27. Stop and ask; never assume it is abandoned.
  const owner = await tasteOwner(page)
  if (owner !== null) {
    console.log(`🔴 ABORT — My Taste is NOT free. It reads (${owner.length} chars):`)
    console.log(`   ${owner.slice(0, 220)}${owner.length > 220 ? '…' : ''}`)
    console.log(`\n   Another session or a human owns this box. Confirm it is finished with, then:`)
    console.log(`   npx tsx scripts/suno/cover-genre.mts taste-release   (backs it up, writes "${TASTE_FREE}")`)
    await browser.close()
    process.exit(1)
  }
  console.log(`✅ My Taste is free ("${TASTE_FREE}") — claiming it for this run`)
  const start = await coverState(page)
  const paras = start.lyricParas as number
  const pre = guard(start, paras)
  if (pre.length) {
    console.log('🔴 ABORT before touching anything:', pre.join(' · '))
    await browser.close()
    process.exit(1)
  }
  if (wordsOnly(await pageLyrics(page)) !== canonWords()) {
    console.log('🔴 ABORT — the words in the page are NOT camping.md §4.')
    console.log('   The attached take carries the lyrics it was generated from, not necessarily the current ones.')
    await browser.close()
    process.exit(1)
  }
  console.log(`✅ cover attached: "${start.coverTitle}" (${start.coverDuration}) · ${paras} lyric paragraphs, matching camping.md §4`)
  // My Taste is written per-variation inside loadVariation, not once here — see the four-box
  // atom note in lanes(). A concurrent session can move it between Creates.

  // 🔴 SET THE WORKSPACE, NEVER INHERIT IT. This was a real bug: `WORKSPACE` was declared and
  //    never applied, so every cover round silently went to whatever workspace the form happened
  //    to be pointing at. c1–c3 looked fine only because the form already held camping-duet; once
  //    a concurrent session left it on `gpom-story`, all twelve c3b takes filed themselves into
  //    another story's workspace. It routes the output and moving clips afterwards is MANUAL, so
  //    it is asserted here and the run stops rather than scattering takes.
  console.log(`   ${await setWorkspace(page, WORKSPACE)}`)
  const ws = (await verify(page)).workspace
  if (ws !== WORKSPACE) {
    console.log(`🔴 ABORT — workspace reads "${ws}", wanted "${WORKSPACE}". Takes would file to the wrong story.`)
    await browser.close()
    process.exit(1)
  }

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
    const after = await coverState(page)
    if (!after.coverTitle) {
      console.log('🔴 THE COVER AUDIO DID NOT SURVIVE THE GENERATION — stopping here.')
      console.log('   Re-attach by hand and re-run with the remaining ids.')
      break
    }
  }
  console.log(`\n✅ generated: ${done.join(', ') || '(none)'}`)
  console.log(JSON.stringify(await listTakes(page, 'Camping cover'), null, 0))
  // 🔴 GATE 2 — RELEASE. Hand the box back so the next session finds it free. This runs on the
  //    success path AND after a mid-run stop, because a half-finished round still leaves our
  //    profile installed account-wide.
  console.log(`\n${await releaseTaste(page)}`)
  await browser.close()
} else {
  console.log(`badcode cover-genre — genre-overlay experiments on the attached Camping cover.\n🔴 My Taste must read "${TASTE_FREE}" before a run, and is released back to it after.

  plan [ids...]     resolved boxes, offline
  check             live form + My Taste, spend nothing
  taste-release     back up whatever My Taste holds, then write the freedom token
  taste-restore     escape hatch: put back whatever taste-release displaced
  run [ids...]      Create each in turn — 10 credits and 2 takes per id

${VARIATIONS.map((v) => `  ${v.id.padEnd(18)} lane=${v.lane.name} AI=${v.audioInfluence} W=${v.weirdness}`).join('\n')}`)
}
