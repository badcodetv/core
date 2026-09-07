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
 *    docs/stories/camping/songs/camping-sheet.md as three fences under a
 *    `### Lane \`key\` — Name` header. Add or change a genre by editing the markdown, never here.
 *
 * 🔴 PER-LANE EXCLUDES. A shared exclude list cannot serve six genres — `power chords` must be
 *    banned for neurofunk and ALLOWED for hardcore punk. Each lane therefore carries its own, and
 *    a lane missing any of its three fences throws offline before a credit is spent.
 *
 * 🔴 TWO MODES, AND THEY CANNOT RUN BACK TO BACK UNATTENDED. `cover` needs the source audio
 *    attached in the page; `fresh` needs it gone. Attaching and removing it are hand actions.
 *
 *   npx tsx scripts/suno/camping.mts plan
 *   npx tsx scripts/suno/camping.mts check
 *   npx tsx scripts/suno/camping.mts cover [lane...]
 *   npx tsx scripts/suno/camping.mts fresh [lane...]
 *   npx tsx scripts/suno/camping.mts taste-release
 */
import type { Page } from 'playwright'
import { readFileSync, writeFileSync } from 'node:fs'
import {
  connect, setSlider, setTitle, setLyrics, setTaste, getTaste, setWorkspace, verify, create, listTakes, attachCover, detachCover,
  tasteOwner, releaseTaste, TASTE_FREE,
} from './suno.mts'

const SHEET = new URL('../../docs/stories/camping/songs/camping-sheet.md', import.meta.url).pathname
const CANON = new URL('../../docs/stories/camping/songs/camping.md', import.meta.url).pathname
const BACKUP = new URL('./.my-taste-backup.txt', import.meta.url).pathname
const WORKSPACE = process.env.SUNO_WORKSPACE ?? 'camping-duet'

/** 🔴 BUMP EVERY ROUND. `create()` waits for two takes matching the title, so a reused title
 *  matches the PREVIOUS round's takes and reports a success it never generated. */
const SET = ' (pv1)'
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

/**
 * The cue sheet, from THIS sheet's `## Lyrics` section.
 *
 * 🔴 One lyric source, and this is it. Until 2026-08-27 the runners read cues from
 *    camping-halftime.md while the words canon lived in camping.md, and the two disagreed about
 *    the first verse — `camping.md` had no cue before "let's see what we can arrange!" and the
 *    generated sheet had `[sarcastic, high pitched]`, which is what produced the stutter nobody
 *    thought they had asked for. camping.md stays the WORDS canon and the guard; cues live here.
 */
function sourceLyrics(): string {
  const m = md.match(/```lyrics\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`${SHEET}: no \`\`\`lyrics fence under "## Lyrics"`)
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

function guard(s: Record<string, unknown>, mode: 'cover' | 'fresh', paras: number): string[] {
  const bad: string[] = []
  if (!String(s.url).includes('/create')) bad.push(`url is ${s.url} — NOT the create page`)
  if (mode === 'cover' && !s.coverTitle) bad.push('the cover audio is GONE — re-attach by hand (song ⋯ → Remix ▸ Cover)')
  // 🔴 The fresh half must NOT inherit the cover. A leftover attachment turns "from nothing" into
  //    another cover of the same 3:14 take, and the output says nothing about it.
  if (mode === 'fresh' && s.coverTitle) bad.push(`🔴 COVER AUDIO IS STILL ATTACHED ("${s.coverTitle}") — remove it (× on the attachment) before the fresh half`)
  if (s.lyricParas !== paras) bad.push(`lyrics ${s.lyricParas} paragraphs, expected ${paras} — the words moved`)
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

async function loadLane(
  page: Page,
  l: Lane,
  mode: 'cover' | 'fresh',
  title = titleFor(l, mode),
  sliders: { si?: number; w?: number } = {},
) {
  const bad: string[] = []
  // My Taste FIRST and per-lane: it is account-wide, so it can move BETWEEN Creates.
  await setTaste(page, l.taste)
  const got = await getTaste(page)
  if (shape(got ?? '') !== shape(l.taste)) bad.push(`🔴 My Taste did not take — read back ${got?.length ?? 'null'}, wanted ${l.taste.length}`)

  const fills = [
    await fillChecked(page, '[data-testid="create-form-styles-wrapper"] textarea', l.style),
    await fillChecked(page, 'input[placeholder="Exclude styles"]', l.exclude),
  ]
  await setSlider(page, 'Style Influence', sliders.si ?? STYLE_INFLUENCE)
  await setSlider(page, 'Weirdness', sliders.w ?? WEIRDNESS)
  if (mode === 'cover') await setSlider(page, 'Audio Influence', AUDIO_INFLUENCE)
  await setTitle(page, title)
  const s = await formState(page)
  if (fills.some((f) => f.startsWith('🔴'))) bad.push(`fill: ${fills.join(' · ')}`)
  if (s.styleLen !== l.style.length) bad.push(`style ${s.styleLen}/${l.style.length} — truncated at the 1000 cap?`)
  if (s.excludeLen !== l.exclude.length) bad.push(`exclude ${s.excludeLen}/${l.exclude.length}`)
  return { state: s, problems: bad }
}

/**
 * 🔴 Verify the release over a NEW connection. On 2026-08-27 a run reported a successful release
 *    and the very next run found the old profile back in the box; setting the token and re-reading
 *    it on the same page held fine for 33s under test, so the revert happens somewhere a same-page
 *    read cannot see. Cause still UNKNOWN — this is detection, not a fix.
 */
async function verifyReleased(): Promise<void> {
  const { browser, page } = await connect()
  const back = (await getTaste(page))?.trim()
  console.log(back === TASTE_FREE
    ? `✅ re-verified over a fresh connection — still "${TASTE_FREE}"`
    : `🔴 THE RELEASE DID NOT HOLD — a fresh connection reads ${JSON.stringify(back?.slice(0, 60))}. Run taste-release before anyone else generates.`)
  await browser.close()
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
      console.log(`then run:  npx tsx scripts/suno/camping.mts taste-release`)
      await browser.close(); process.exit(1)
    }
    console.log(`✅ My Taste is free ("${TASTE_FREE}") — claiming it for this run`)

    // 🔑 BOTH DIRECTIONS ARE AUTOMATED (2026-08-27). Fresh mode used to ABORT on a leftover
    //    attachment because detaching was irreversible without a human on the song page; now that
    //    attachCover can put a source back in one command, it clears its own way instead. Cover
    //    mode attaches the source it needs rather than asking for it.
    if (mode === 'fresh' && (await formState(page)).coverTitle) {
      console.log(`   ${await detachCover(page)} — fresh mode needs no source`)
    }
    if (mode === 'cover' && !(await formState(page)).coverTitle) {
      console.log(`   ${await attachCover(page, process.env.SUNO_SOURCE ?? 'SI80 W30 (a3)', 0, process.env.SUNO_SOURCE_DUR ?? '02:58')}`)
    }

    // The fresh half writes the words; the cover half inherits them with the attachment.
    let wroteParas = 0
    if (mode === 'fresh') {
      wroteParas = await setLyrics(page, sourceLyrics())
      console.log(`   lyrics written: ${wroteParas} paragraphs`)
    }

    const pre = await formState(page)
    const preBad = guard(pre, mode, mode === 'fresh' ? wroteParas : pre.lyricParas as number)
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
    const expectParas = pre.lyricParas as number

    const done: string[] = []
    for (const [i, l] of picked.entries()) {
      const title = titleFor(l, mode)
      console.log(`\n──────── ${i + 1}/${picked.length}  ${title}`)
      // 🔴 The attachment can drop after a Create — restore it rather than skipping the lane.
      if (mode === 'cover' && !(await formState(page)).coverTitle) {
        const r = await attachCover(page, process.env.SUNO_SOURCE ?? 'SI80 W30 (a3)', 0, process.env.SUNO_SOURCE_DUR ?? '02:58')
        console.log(`   re-${r}`)
        if (!r.startsWith('attach:ok')) { console.log('   🔴 STOPPING — cannot restore the cover source'); break }
      }
      const { state, problems } = await loadLane(page, l, mode, titleFor(l, mode), {
        si: process.env.SUNO_SI ? Number(process.env.SUNO_SI) : undefined,
        w: process.env.SUNO_W ? Number(process.env.SUNO_W) : undefined,
      })
      if (mode === 'cover') await setSlider(page, 'Audio Influence', Number(process.env.SUNO_AI ?? AUDIO_INFLUENCE))
      const bad = [...problems, ...guard(state, mode, expectParas)]
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
} else if (cmd === 'cover-sliders') {
  // 🔴 A SLIDER ROUND IN COVER MODE — three dials instead of two. Audio Influence exists only when
  //    source audio is attached, and it is the one that decides how much of the source's own
  //    PERFORMANCE survives. Lyrics are NOT written here: they arrive with the attachment.
  const LANE_KEY = process.env.SUNO_LANE ?? 'dynamics'
  const nums = (v: string | undefined, d: number[]) => (v ? v.split(',').map(Number) : d)
  const G_AI = nums(process.env.SUNO_AI, [10, 25, 40])
  const G_W = nums(process.env.SUNO_W, [30, 60])
  const G_SI = nums(process.env.SUNO_SI, [75, 100])
  // 🔑 The cover source, attached FROM CODE (see attachCover). Before 2026-08-27 this needed a
  //    human on the song page every time, and a dropped attachment killed the round.
  const SOURCE = process.env.SUNO_SOURCE ?? 'SI80 W30 (a3)'
  const SOURCE_DUR = process.env.SUNO_SOURCE_DUR ?? '02:58'
  const lane = LANES.find((l) => l.key === LANE_KEY)
  if (!lane) throw new Error(`${SHEET}: no lane \`${LANE_KEY}\``)
  const cells = G_AI.flatMap((ai) => G_W.flatMap((w) => G_SI.map((si) => ({ ai, w, si }))))
  const { browser, page } = await connect()
  try {
    const owner = await tasteOwner(page)
    if (owner !== null) {
      console.log(`🔴 ABORT — My Taste is NOT free. It reads:\n\n${owner.slice(0, 400)}\n`)
      await browser.close(); process.exit(1)
    }
    console.log(`✅ My Taste is free — claiming it`)
    let pre = await formState(page)
    if (!pre.coverTitle) {
      console.log(`   ${await attachCover(page, SOURCE, 0, SOURCE_DUR)}`)
      pre = await formState(page)
    }
    const preBad = guard(pre, 'cover', pre.lyricParas as number)
    if (preBad.length) {
      console.log(`🔴 ABORT before spending a credit:\n   ${preBad.join('\n   ')}`)
      await browser.close(); process.exit(1)
    }
    console.log(`✅ cover attached: "${pre.coverTitle}" (${pre.coverDuration}) · ${pre.lyricParas} lyric paragraphs`)
    console.log(`   ${await setWorkspace(page, WORKSPACE)}`)
    const ws = (await verify(page)).workspace
    if (ws && !String(ws).toLowerCase().includes('camping')) {
      console.log(`🔴 ABORT — workspace reads "${ws}", expected ${WORKSPACE}`)
      await browser.close(); process.exit(1)
    }
    console.log(`\nlane "${lane.name}" · ${cells.length} cells · style ${lane.style.length} · exclude ${lane.exclude.length} — NONE of these change`)
    const done: string[] = []
    for (const [i, c] of cells.entries()) {
      const title = `Camping ${lane.name} AI${c.ai} W${c.w} SI${c.si}${SET}`
      console.log(`\n──────── ${i + 1}/${cells.length}  ${title}`)
      // 🔴 The attachment DROPS after a Create (observed 2026-08-27, though an earlier round saw one
      //    survive six). Re-attach per cell rather than assuming either behaviour.
      if (!(await formState(page)).coverTitle) {
        const r = await attachCover(page, SOURCE, 0, SOURCE_DUR)
        console.log(`   re-${r}`)
        if (!r.startsWith('attach:ok')) { console.log('   🔴 STOPPING — cannot restore the cover source'); break }
      }
      const { state, problems } = await loadLane(page, lane, 'cover', title, { si: c.si, w: c.w })
      await setSlider(page, 'Audio Influence', c.ai)
      const after = await formState(page)
      const bad = [...problems, ...guard(after, 'cover', pre.lyricParas as number)]
      if (after.styleLen !== lane.style.length || after.excludeLen !== lane.exclude.length) {
        bad.push('🔴 a prompt box changed during a SLIDER round — void')
      }
      console.log(`   ${(after.sliders as string[]).join(',')} · style ${after.styleLen} · exclude ${after.excludeLen}`)
      if (bad.length) { console.log(`   🔴 SKIPPED: ${bad.join(' · ')}`); continue }
      console.log(`   ▶ ${await create(page, title, 420000)}`)
      done.push(title)
    }
    console.log(`\n✅ generated (${done.length}/${cells.length})`)
    console.log(JSON.stringify(await listTakes(page, SET)))
  } finally {
    console.log(`\n${await releaseTaste(page)}`)
    await browser.close()
  }
  await verifyReleased()
} else if (cmd === 'sliders') {
  // 🔴 A SLIDER ROUND — the second of the two round types, and the cheap one. NOT ONE PROMPT BOX
  //    MOVES: the same Style, Taste, Exclude and Lyrics are written before every Create, so the
  //    only thing separating twelve takes is where the two dials sat. Kai, 2026-08-27: "an
  //    experiment that does not change any of the prompt settings… just to see if we are just
  //    needing to iterate on the same prompt, almost rolling the dice."
  //
  //    The grid is a 3x2 factorial around the p1 cell (SI 75, W 45), which is already rendered and
  //    acts as the centre reference rather than being re-run. Style Influence is how hard Suno is
  //    made to obey the prompt; Weirdness is the dice. Corners, not a random scatter — so a result
  //    reads as a direction ("obey harder helps") rather than as one lucky take.
  const LANE_KEY = process.env.SUNO_LANE ?? 'punkmetal'
  const nums = (v: string | undefined, d: number[]) => (v ? v.split(',').map(Number) : d)
  const GRID_SI = nums(process.env.SUNO_SI, [50, 75, 100])
  const GRID_W = nums(process.env.SUNO_W, [30, 60])
  const lane = LANES.find((l) => l.key === LANE_KEY)
  if (!lane) throw new Error(`${SHEET}: no lane \`${LANE_KEY}\``)
  const cells = GRID_SI.flatMap((si) => GRID_W.map((w) => ({ si, w })))
  const { browser, page } = await connect()
  try {
    const owner = await tasteOwner(page)
    if (owner !== null) {
      console.log(`🔴 ABORT — My Taste is NOT free. It reads:\n\n${owner.slice(0, 400)}\n`)
      console.log(`Expected exactly "${TASTE_FREE}". Confirm with the human, then run taste-release.`)
      await browser.close(); process.exit(1)
    }
    console.log(`✅ My Taste is free — claiming it`)
    const wroteParas = await setLyrics(page, sourceLyrics())
    console.log(`   lyrics written: ${wroteParas} paragraphs`)
    const pre = await formState(page)
    const preBad = guard(pre, 'fresh', wroteParas)
    if (wordsOnly(await pageLyrics(page)) !== canonWords()) preBad.push('the words do not match camping.md §4')
    if (preBad.length) {
      console.log(`🔴 ABORT before spending a credit:\n   ${preBad.join('\n   ')}`)
      await browser.close(); process.exit(1)
    }
    console.log(`   ${await setWorkspace(page, WORKSPACE)}`)
    const ws = (await verify(page)).workspace
    if (ws && !String(ws).toLowerCase().includes('camping')) {
      console.log(`🔴 ABORT — workspace reads "${ws}", expected ${WORKSPACE}`)
      await browser.close(); process.exit(1)
    }
    console.log(`\nlane "${lane.name}" · ${cells.length} cells · style ${lane.style.length} · exclude ${lane.exclude.length} · taste ${lane.taste.length} — NONE of these change`)
    const done: string[] = []
    for (const [i, c] of cells.entries()) {
      const title = `Camping ${lane.name} SI${c.si} W${c.w}${SET}`
      console.log(`\n──────── ${i + 1}/${cells.length}  ${title}`)
      const { state, problems } = await loadLane(page, lane, 'fresh', title, { si: c.si, w: c.w })
      const bad = [...problems, ...guard(state, 'fresh', wroteParas)]
      console.log(`   ${(state.sliders as string[]).join(',')} · style ${state.styleLen} · exclude ${state.excludeLen}`)
      // 🔴 The whole point of a slider round: if a prompt box moved, the round is void.
      if (state.styleLen !== lane.style.length || state.excludeLen !== lane.exclude.length) {
        bad.push('🔴 a prompt box changed during a SLIDER round — void')
      }
      if (bad.length) { console.log(`   🔴 SKIPPED: ${bad.join(' · ')}`); continue }
      console.log(`   ▶ ${await create(page, title)}`)
      done.push(title)
    }
    console.log(`\n✅ generated (${done.length}/${cells.length}): ${done.join(', ')}`)
    console.log(JSON.stringify(await listTakes(page, SET)))
  } finally {
    console.log(`\n${await releaseTaste(page)}`)
    await browser.close()
  }
  const { browser: b2, page: p2 } = await connect()
  const back = (await getTaste(p2))?.trim()
  console.log(back === TASTE_FREE
    ? `✅ re-verified over a fresh connection — still "${TASTE_FREE}"`
    : `🔴 THE RELEASE DID NOT HOLD — a fresh connection reads ${JSON.stringify(back?.slice(0, 60))}.`)
  await b2.close()
} else if (cmd === 'split') {
  // 🔴 THE INSTRUMENT/VOICE SPLIT. Two levers, tested separately: A moves only the prompt (the
  //    Style box states the seam and the excludes ban the punk vocal by name); B additionally
  //    recasts the lyric SECTION HEADERS, which are the only section-scoped casting control the
  //    platform gives us. The live cue sheet was still casting `gravelly rapped voice` from the
  //    h12 pivot and an `80s rock guitar lick` from the h10 round, so B is not a refinement — it
  //    is removing two instructions that actively fight the prompt.
  const lane = LANES.find((l) => l.key === 'punkbody')
  if (!lane) throw new Error(`${SHEET}: no lane \`punkbody\``)
  const variantC = md.match(/```lyricsC\n([\s\S]*?)\n```/)?.[1]
  if (!variantC) throw new Error(`${SHEET}: no \`\`\`lyricsC fence`)
  const runs = [
    { tag: 'A', label: 'prompt only', lyrics: sourceLyrics() },
    { tag: 'B', label: 'prompt + recast headers', lyrics: variantC },
  ]
  const { browser, page } = await connect()
  try {
    const owner = await tasteOwner(page)
    if (owner !== null) {
      console.log(`🔴 ABORT — My Taste is NOT free. It reads:\n\n${owner.slice(0, 400)}\n`)
      await browser.close(); process.exit(1)
    }
    console.log(`✅ My Taste is free — claiming it`)
    console.log(`   ${await setWorkspace(page, WORKSPACE)}`)
    const ws = (await verify(page)).workspace
    if (ws && !String(ws).toLowerCase().includes('camping')) {
      console.log(`🔴 ABORT — workspace reads "${ws}", expected ${WORKSPACE}`)
      await browser.close(); process.exit(1)
    }
    for (const r of runs) {
      const title = `Camping punk-body ${r.tag}${SET}`
      console.log(`\n──────── ${title}  (${r.label})`)
      const paras = await setLyrics(page, r.lyrics)
      const { state, problems } = await loadLane(page, lane, 'fresh', title)
      const bad = [...problems, ...guard(state, 'fresh', paras)]
      if (wordsOnly(await pageLyrics(page)) !== canonWords()) bad.push('the words do not match camping.md §4')
      console.log(`   ${paras} paragraphs · ${(state.sliders as string[]).join(',')} · style ${state.styleLen} · exclude ${state.excludeLen}`)
      if (bad.length) { console.log(`   🔴 SKIPPED: ${bad.join(' · ')}`); continue }
      console.log(`   ▶ ${await create(page, title)}`)
    }
    console.log(`\n${JSON.stringify(await listTakes(page, 'punk-body'))}`)
  } finally {
    console.log(`\n${await releaseTaste(page)}`)
    await browser.close()
  }
  await verifyReleased()
} else if (cmd === 'timing') {
  // 🔴 THE FIRST-VERSE STUTTER. Two lyric variants, IDENTICAL WORDS, differing only in bracket
  //    cues — A restates the delivery before every line (a cue is a directive), B strips the
  //    middle cue out (a cue is a section boundary and the re-entry is the stutter). One lane,
  //    one slider setting, so the cues are the only variable between the two Creates.
  const variant = (t: string) =>
    md.match(new RegExp('```lyrics' + t + '\\n([\\s\\S]*?)\\n```'))?.[1] ??
    (() => { throw new Error(`${SHEET}: no \`\`\`lyrics${t} fence`) })()
  const lane = LANES.find((l) => l.key === 'punkmetal')
  if (!lane) throw new Error(`${SHEET}: no lane \`punkmetal\``)
  const { browser, page } = await connect()
  try {
    const owner = await tasteOwner(page)
    if (owner !== null) {
      console.log(`🔴 ABORT — My Taste is NOT free. It reads:\n\n${owner.slice(0, 400)}\n`)
      console.log(`Expected exactly "${TASTE_FREE}". Confirm with the human, then run taste-release.`)
      await browser.close(); process.exit(1)
    }
    console.log(`✅ My Taste is free — claiming it`)
    console.log(`   ${await setWorkspace(page, WORKSPACE)}`)
    const ws = (await verify(page)).workspace
    if (ws && !String(ws).toLowerCase().includes('camping')) {
      console.log(`🔴 ABORT — workspace reads "${ws}", expected ${WORKSPACE}`)
      await browser.close(); process.exit(1)
    }
    for (const tag of ['A', 'B']) {
      const text = variant(tag)
      const title = `Camping punk-metal timing ${tag}${SET}`
      console.log(`\n──────── ${title}`)
      const paras = await setLyrics(page, text)
      const { state, problems } = await loadLane(page, lane, 'fresh', title)
      const bad = [...problems, ...guard(state, 'fresh', paras)]
      // The WORDS must still be canon — only the cues may differ between variants.
      if (wordsOnly(await pageLyrics(page)) !== canonWords()) bad.push('the words do not match camping.md §4')
      const cues = text.split('\n').filter((l) => l.trim().startsWith('[')).length
      console.log(`   ${paras} paragraphs, ${cues} bracket cues · style ${state.styleLen} · exclude ${state.excludeLen}`)
      if (bad.length) { console.log(`   🔴 SKIPPED: ${bad.join(' · ')}`); continue }
      console.log(`   ▶ ${await create(page, title)}`)
    }
    console.log(`\n${JSON.stringify(await listTakes(page, 'timing'))}`)
  } finally {
    console.log(`\n${await releaseTaste(page)}`)
    await browser.close()
  }
  await verifyReleased()
} else {
  console.log('commands: plan | check | cover [lane...] | fresh [lane...] | sliders | cover-sliders | split | timing | taste-release')
}
