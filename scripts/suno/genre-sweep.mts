/**
 * badcode — the Camping GENRE SWEEP. Six genres over the drum and bass, each run twice: once as a
 * cover of the accepted h12 take, once fresh from nothing.
 *
 * Jack, 2026-08-27: "I think we have lost the aggression and the pace, I think maybe experiment
 * with different genres over the drum and bass." The brief is SPREAD, not depth — one slider
 * setting throughout, genre as the only variable, so Jack can pick a direction by ear and the
 * round after this one tunes it.
 *
 * 🔴 THE SHEET IS THE PROMPT. Every lane's Style, My Taste and Exclude live in
 *    docs/stories/camping/songs/camping-genre-sweep.md as three fences under a
 *    `### Lane \`key\` — Name` header. Add or change a genre by editing the markdown, never here.
 *
 * 🔴 PER-LANE EXCLUDES. A shared exclude list cannot serve six genres — `power chords` must be
 *    banned for neurofunk and ALLOWED for hardcore punk. Each lane therefore carries its own, and
 *    a lane missing any of its three fences throws offline before a credit is spent.
 *
 * 🔴 TWO MODES, AND THEY CANNOT RUN BACK TO BACK UNATTENDED. `cover` needs the source audio
 *    attached in the page; `fresh` needs it gone. Attaching and removing it are hand actions.
 *
 *   npx tsx scripts/suno/genre-sweep.mts plan
 *   npx tsx scripts/suno/genre-sweep.mts check
 *   npx tsx scripts/suno/genre-sweep.mts cover [lane...]
 *   npx tsx scripts/suno/genre-sweep.mts fresh [lane...]
 *   npx tsx scripts/suno/genre-sweep.mts taste-release
 */
import type { Page } from 'playwright'
import { readFileSync, writeFileSync } from 'node:fs'
import {
  connect, setSlider, setTitle, setLyrics, setTaste, getTaste, setWorkspace, verify, create, listTakes,
  tasteOwner, releaseTaste, TASTE_FREE,
} from './suno.mts'

const SHEET = new URL('../../docs/stories/camping/songs/camping-genre-sweep.md', import.meta.url).pathname
const CANON = new URL('../../docs/stories/camping/songs/camping.md', import.meta.url).pathname
const PARENT = new URL('../../docs/stories/camping/songs/camping-halftime.md', import.meta.url).pathname
const BACKUP = new URL('./.my-taste-backup.txt', import.meta.url).pathname
const WORKSPACE = process.env.SUNO_WORKSPACE ?? 'camping-duet'

/** 🔴 BUMP EVERY ROUND. `create()` waits for two takes matching the title, so a reused title
 *  matches the PREVIOUS round's takes and reports a success it never generated. */
const SET = ' (g1)'
const STYLE_INFLUENCE = 75
const WEIRDNESS = 45
const AUDIO_INFLUENCE = 25

const md = readFileSync(SHEET, 'utf8')

interface Lane { key: string; name: string; style: string; taste: string; exclude: string }

function lanes(): Lane[] {
  const parts = md.split(/^### Lane `([a-z0-9-]+)` — (.+)$/m)
  // split() yields [prefix, key, name, body, key, name, body, ...]
  const out: Lane[] = []
  for (let i = 1; i + 2 < parts.length + 1; i += 3) {
    const key = parts[i], name = parts[i + 1], body = parts[i + 2]
    if (!key) continue
    const grab = (tag: string) => body.match(new RegExp('```' + tag + '\\n([\\s\\S]*?)\\n```'))?.[1]
    const style = grab('style'), taste = grab('taste'), exclude = grab('exclude')
    // The four-box atom (Kai, 2026-08-27): Style + My Taste + Exclude + Lyrics describe ONE sound
    // and move together. No silent fallback to a shared block — that is how the GPOM profile sat
    // underneath fourteen Camping rounds without anyone seeing it.
    for (const [tag, v] of [['style', style], ['taste', taste], ['exclude', exclude]] as const) {
      if (!v) throw new Error(`${SHEET}: lane "${key}" has no \`\`\`${tag} fence`)
    }
    out.push({ key, name, style: style!, taste: taste!, exclude: exclude! })
  }
  if (!out.length) throw new Error(`${SHEET}: no "### Lane \`key\` — Name" headers found`)
  return out
}
const LANES = lanes()

const shape = (t: string) => t.split('\n').map((l) => l.trim()).filter(Boolean).join('\n')
const wordsOnly = (t: string) => shape(t).split('\n').filter((l) => !l.startsWith('[')).join('\n')

function canonWords(): string {
  const m = readFileSync(CANON, 'utf8').match(/```lyrics\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`no \`\`\`lyrics block in ${CANON}`)
  return wordsOnly(m[1])
}

/** The cue sheet the h12 take was generated from — §4 of the parent half-time sheet. */
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

async function formState(page: Page) {
  return page.evaluate(`(() => {
    const c = (s) => (s || '').replace(/\\s+/g, ' ').trim()
    const st = document.querySelector('[data-testid="create-form-styles-wrapper"] textarea')
    const ex = document.querySelector('input[placeholder="Exclude styles"]')
    const m = c(document.body.innerText).match(/Audio Cover ([^]{0,60}?) \\d\\d:\\d\\d\\/(\\d\\d:\\d\\d)/)
    return {
      url: location.href,
      coverTitle: m ? c(m[1]) : null,
      coverDuration: m ? m[2] : null,
      styleLen: st ? st.value.length : null,
      excludeLen: ex ? ex.value.length : null,
      lyricParas: document.querySelectorAll('[contenteditable="true"] p').length,
      voice: (() => {
        const b = [...document.querySelectorAll('button[aria-label="Add Voice"]')].filter((x) => x.offsetParent !== null)[0]
        return b ? c(b.innerText) : null
      })(),
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

async function fillChecked(page: Page, selector: string, text: string, tries = 4): Promise<string> {
  const el = page.locator(selector).first()
  for (let i = 1; i <= tries; i++) {
    await el.fill(''); await el.blur().catch(() => {}); await page.waitForTimeout(150)
    await el.fill(text); await el.blur().catch(() => {}); await page.waitForTimeout(250)
    const got = await el.inputValue().catch(async () => (await el.textContent()) ?? '')
    if (got.length === text.length) return i === 1 ? 'ok' : `ok (retry ${i})`
    if (i === tries) return `🔴 ${got.length}/${text.length} after ${tries} tries`
  }
  return 'unreachable'
}

/** This sheet casts its voices in the Style box. An attached persona would override that outright. */
const EXPECT_VOICE: string | null = null
const NO_VOICE = 'Voice'
const PARAS = 71

function guard(s: Record<string, unknown>, mode: 'cover' | 'fresh'): string[] {
  const bad: string[] = []
  if (!String(s.url).includes('/create')) bad.push(`url is ${s.url} — NOT the create page`)
  if (mode === 'cover' && !s.coverTitle) bad.push('the cover audio is GONE — re-attach by hand (song ⋯ → Remix ▸ Cover)')
  // 🔴 The fresh half must NOT inherit the cover. A leftover attachment turns "from nothing" into
  //    another cover of the same 3:14 take, and the output says nothing about it.
  if (mode === 'fresh' && s.coverTitle) bad.push(`🔴 COVER AUDIO IS STILL ATTACHED ("${s.coverTitle}") — remove it (× on the attachment) before the fresh half`)
  if (s.lyricParas !== PARAS) bad.push(`lyrics ${s.lyricParas} paragraphs, expected ${PARAS} — the words moved`)
  const want = EXPECT_VOICE ?? NO_VOICE
  if (s.voice !== want) {
    bad.push(EXPECT_VOICE
      ? `🔴 Voice reads "${s.voice}", expected "${EXPECT_VOICE}"`
      : `🔴 A VOICE IS ATTACHED ("${s.voice}") and this sheet casts its voices in the Style box — remove it in the create form`)
  }
  // 🔴 Duration runs on Auto and Auto means the slider is NOT MOUNTED. A mounted one is a custom
  //    length someone else set: c3c came back 3:59–4:00 against 3:10–3:44 on Auto because of it.
  const dur = (s.sliders as string[]).find((x) => x.startsWith('Duration='))
  if (dur) bad.push(`🔴 Duration is pinned (${dur}) — this sheet runs on Auto; clear it in More Options`)
  return bad
}

const titleFor = (l: Lane, mode: 'cover' | 'fresh') => `Camping ${l.name} ${mode}${SET}`

async function loadLane(page: Page, l: Lane, mode: 'cover' | 'fresh') {
  const bad: string[] = []
  // My Taste FIRST and per-lane: it is account-wide, so it can move BETWEEN Creates.
  await setTaste(page, l.taste)
  const got = await getTaste(page)
  if (shape(got ?? '') !== shape(l.taste)) bad.push(`🔴 My Taste did not take — read back ${got?.length ?? 'null'}, wanted ${l.taste.length}`)

  const fills = [
    await fillChecked(page, '[data-testid="create-form-styles-wrapper"] textarea', l.style),
    await fillChecked(page, 'input[placeholder="Exclude styles"]', l.exclude),
  ]
  await setSlider(page, 'Style Influence', STYLE_INFLUENCE)
  await setSlider(page, 'Weirdness', WEIRDNESS)
  if (mode === 'cover') await setSlider(page, 'Audio Influence', AUDIO_INFLUENCE)
  await setTitle(page, titleFor(l, mode))
  const s = await formState(page)
  if (fills.some((f) => f.startsWith('🔴'))) bad.push(`fill: ${fills.join(' · ')}`)
  if (s.styleLen !== l.style.length) bad.push(`style ${s.styleLen}/${l.style.length} — truncated at the 1000 cap?`)
  if (s.excludeLen !== l.exclude.length) bad.push(`exclude ${s.excludeLen}/${l.exclude.length}`)
  return { state: s, problems: bad }
}

const [cmd, ...ids] = process.argv.slice(2)
const picked = ids.length ? LANES.filter((l) => ids.includes(l.key)) : LANES
if (!picked.length) throw new Error(`no lanes matched ${JSON.stringify(ids)} — the sheet has: ${LANES.map((l) => l.key).join(', ')}`)

if (cmd === 'plan') {
  for (const l of picked) {
    console.log(`\n── ${l.key}  (${l.name})`)
    console.log(`   style ${l.style.length}/1000${l.style.length > 1000 ? ' 🔴 OVER THE CAP' : ''} · exclude ${l.exclude.length}/933 · taste ${l.taste.length}/2000`)
    console.log(`   titles: "${titleFor(l, 'cover')}"  |  "${titleFor(l, 'fresh')}"`)
  }
  console.log(`\n${picked.length} lanes × 2 modes = ${picked.length * 2} creates, ${picked.length * 4} takes`)
  console.log(`sliders: SI ${STYLE_INFLUENCE}, W ${WEIRDNESS}, AI ${AUDIO_INFLUENCE} (cover only), Duration Auto`)
} else if (cmd === 'check') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await formState(page), null, 2))
  console.log(`My Taste (live): ${(await getTaste(page))?.slice(0, 80)}…`)
  await browser.close()
} else if (cmd === 'taste-release') {
  const { browser, page } = await connect()
  const live = await getTaste(page)
  if (live && live.trim() !== TASTE_FREE) { writeFileSync(BACKUP, live); console.log(`backed up ${live.length} chars to ${BACKUP}`) }
  console.log(await releaseTaste(page))
  await browser.close()
} else if (cmd === 'cover' || cmd === 'fresh') {
  const mode = cmd as 'cover' | 'fresh'
  const { browser, page } = await connect()
  try {
    // ── Gate 1: the freedom token. My Taste cannot be saved empty, so there is no neutral state —
    //    anything but the token means a human or another session owns the box. Pause, never guess.
    const owner = await tasteOwner(page)
    if (owner !== null) {
      console.log(`🔴 ABORT — My Taste is NOT free. It reads:\n\n${owner.slice(0, 400)}\n`)
      console.log(`Expected exactly "${TASTE_FREE}". Someone owns this box. Confirm with the human,`)
      console.log(`then run:  npx tsx scripts/suno/genre-sweep.mts taste-release`)
      await browser.close(); process.exit(1)
    }
    console.log(`✅ My Taste is free ("${TASTE_FREE}") — claiming it for this run`)

    // The fresh half writes the words; the cover half inherits them with the attachment.
    if (mode === 'fresh') {
      const wrote = await setLyrics(page, sourceLyrics())
      console.log(`   lyrics written: ${wrote} paragraphs`)
    }

    const pre = await formState(page)
    const preBad = guard(pre, mode)
    if (wordsOnly(await pageLyrics(page)) !== canonWords()) preBad.push('the words in the page do not match camping.md §4')
    if (preBad.length) {
      console.log(`🔴 ABORT before spending a credit:\n   ${preBad.join('\n   ')}`)
      await browser.close(); process.exit(1)
    }
    console.log(mode === 'cover'
      ? `✅ cover attached: "${pre.coverTitle}" (${pre.coverDuration}) · ${pre.lyricParas} lyric paragraphs, matching camping.md §4`
      : `✅ no cover attached — generating fresh · ${pre.lyricParas} lyric paragraphs, matching camping.md §4`)
    console.log(`   ${await setWorkspace(page, WORKSPACE)}`)
    const ws = (await verify(page)).workspace
    if (ws && !String(ws).toLowerCase().includes('camping')) {
      console.log(`🔴 ABORT — workspace reads "${ws}", expected ${WORKSPACE}`)
      await browser.close(); process.exit(1)
    }

    const done: string[] = []
    for (const [i, l] of picked.entries()) {
      const title = titleFor(l, mode)
      console.log(`\n──────── ${i + 1}/${picked.length}  ${title}`)
      const { state, problems } = await loadLane(page, l, mode)
      const bad = [...problems, ...guard(state, mode)]
      console.log(`   ${(state.sliders as string[]).join(',')} · style ${state.styleLen} · exclude ${state.excludeLen}`)
      if (bad.length) { console.log(`   🔴 SKIPPED: ${bad.join(' · ')}`); continue }
      console.log(`   ▶ ${await create(page, title)}`)
      done.push(title)
    }
    console.log(`\n✅ generated (${done.length}/${picked.length}): ${done.join(', ')}`)
    console.log(JSON.stringify(await listTakes(page, SET)))
  } finally {
    // ── Gate 2: release, on success AND on failure. A half-finished run still leaves a profile
    //    installed account-wide, so the token goes back either way.
    console.log(`\n${await releaseTaste(page)}`)
    await browser.close()
  }
  // 🔴 AND VERIFY IT FROM A FRESH CONNECTION. On 2026-08-27 the c4 run reported a successful
  //    release and the very next run found c4's own lane-D profile back in the box. Setting the
  //    token and re-reading it on the same page held fine for 33s when tested directly, so the
  //    revert happened somewhere the same-page read cannot see. Re-reading over a new connection
  //    is cheap and is the only check that would have caught it. Cause still UNKNOWN — do not
  //    write it up as understood.
  {
    const { browser: b2, page: p2 } = await connect()
    const back = (await getTaste(p2))?.trim()
    console.log(back === TASTE_FREE
      ? `✅ re-verified over a fresh connection — still "${TASTE_FREE}"`
      : `🔴 THE RELEASE DID NOT HOLD — a fresh connection reads ${JSON.stringify(back?.slice(0, 60))}. Run taste-release before anyone else generates.`)
    await b2.close()
  }
} else {
  console.log('commands: plan | check | cover [lane...] | fresh [lane...] | taste-release')
}
