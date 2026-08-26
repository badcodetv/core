/**
 * badcode — iterate on the accepted Camping half-time take.
 *
 * The scouting set (`style-ab.mts`) moved every input at once to find a direction. It found one:
 * s1/S7 take 1, dub soundsystem drum and bass with the vocal delivered at half the speed of the
 * beat. So this runner goes back to one variable per round, and the baseline is frozen.
 *
 * 🔴 THE SHEET IS THE PROMPT. All four boxes are read out of
 *    `docs/stories/camping/songs/camping-halftime.md` — §1 My Taste, §2 Style, §3 Exclude, §4
 *    Lyrics — not held in this file. Edit the markdown and the next run picks it up; there is no
 *    second copy to drift. Rounds below are PATCHES on those boxes, expressed as
 *    find-and-replace pairs so a round breaks loudly if the baseline it was written against moves.
 *
 * 🔴 THE WORDS ARE CANON AND LIVE ELSEWHERE. `camping.md` §4 owns them; §4 of the half-time sheet
 *    owns the bracket cues for this direction. Stripping the cues from one must give the other,
 *    and `run` refuses to spend a credit otherwise — because generating from a sheet Kai had not
 *    edited already cost twenty takes once. Override with SUNO_ALLOW_WORD_DRIFT=1 only when the
 *    drift is deliberate and you are about to mirror it back.
 *
 * 🔴 MY TASTE IS ACCOUNT-WIDE. Backed up to disk before anything writes to it, read back after
 *    every write, restored at the end. `run` will not start without a backup on disk.
 *
 *   npx tsx scripts/suno/halftime.mts plan [ids...]
 *   npx tsx scripts/suno/halftime.mts check
 *   npx tsx scripts/suno/halftime.mts taste-backup | taste-restore
 *   npx tsx scripts/suno/halftime.mts load <id>
 *   npx tsx scripts/suno/halftime.mts run [ids...]
 */
import type { Page } from 'playwright'
import { readFileSync, writeFileSync, existsSync } from 'node:fs'
import {
  connect, setSlider, setTitle, setLyrics, setDuration, setWorkspace, setTaste, getTaste, create, listTakes,
} from './suno.mts'

const SHEET = new URL('../../docs/stories/camping/songs/camping-halftime.md', import.meta.url).pathname
const CANON = new URL('../../docs/stories/camping/songs/camping.md', import.meta.url).pathname
const BACKUP = new URL('./.my-taste-backup.txt', import.meta.url).pathname
const WORKSPACE = process.env.SUNO_WORKSPACE ?? 'camping-duet'

/**
 * Which run of the set this is. `create()` waits for two takes whose title matches, so a re-run
 * under unchanged titles would match the OLD takes and report a success it never generated.
 * BUMP THIS on every lyric or cue change.
 */
const SET = ' (h12b)'

// ─── reading the sheet ────────────────────────────────────────────────────────────────────────

/** The first fenced block under a `## N. Heading`. */
function block(md: string, heading: string): string {
  const i = md.indexOf(`## ${heading}`)
  if (i === -1) throw new Error(`${SHEET}: no section "## ${heading}"`)
  const rest = md.slice(i)
  const end = rest.search(/\n## /)
  const m = (end === -1 ? rest : rest.slice(0, end)).match(/\n```[a-z]*\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`${SHEET}: no fenced block under "## ${heading}"`)
  return m[1]
}

export interface Boxes {
  taste: string
  style: string
  exclude: string
  lyrics: string
  weirdness: number
  styleInfluence: number
  durationSec: number
}

export function baseline(): Boxes {
  const md = readFileSync(SHEET, 'utf8')
  return {
    taste: block(md, '1. My Taste'),
    style: block(md, '2. Style'),
    exclude: block(md, '3. Exclude Styles'),
    lyrics: block(md, '4. Lyrics'),
    // Sliders live here rather than in the sheet's §5 table: they are numbers a round patches,
    // and parsing them out of prose would fail silently the first time the table is reworded.
    weirdness: 30,
    styleInfluence: 75,
    durationSec: 240,
  }
}

// ─── rounds ───────────────────────────────────────────────────────────────────────────────────

/** A find-and-replace pair. `from` must be present or the round is stale and throws. */
type Patch = [from: string, to: string][]

export interface Round {
  id: string
  name: string
  /** The one thing this round moves. If you cannot write it in a clause, it is two rounds. */
  variable: string
  style?: Patch
  taste?: Patch
  exclude?: Patch
  lyrics?: Patch
  weirdness?: number
  styleInfluence?: number
  durationSec?: number
}

export const ROUNDS: Round[] = [
  // Kai, 2026-08-26 (seventh pass): u02 "no drops at all" is the one. Now "more dark industrial
  // drum and bass and slightly less jump up, feel good — there's a sort of dystopian vibe we're
  // missing." Style Influence 75, Weirdness 30 / 50 / 60.
  //
  // 🔴 THE NEW DISCIPLINE, bought with h6: length tracks the VOLUME of prompt text, not what it
  //    says. h5 at 2769 cue characters ran 4:24; u02 at 616 ran 3:25. So the dystopian rewrite is
  //    made ENTIRELY OF SWAPS — `dub soundsystem` → `dub soundsystem, corroded`, `spring reverb`
  //    → `struck steel`, `chorus jangle` → `cold jangle`, `Grim, bitter and serious` →
  //    `Dystopian, grim and mechanical` — and the anti-jump-up excludes were paid for by dropping
  //    five bans already covered by a neighbour. Style 944→954, taste 1698→1661, cues 616→614.
  //    **Never add to a box in this sheet again without taking the same number of characters out.**
  //
  //    The drop cues stay deleted. That single change was worth 23 seconds and Kai picked the
  //    take it produced.
  { id: 'v01-w30', name: 'P dark W30', variable: 'dark industrial rewrite, Weirdness 30', weirdness: 30 },
  { id: 'v02-w50', name: 'Q dark W50', variable: 'dark industrial rewrite, Weirdness 50', weirdness: 50 },
  { id: 'v03-w60', name: 'R dark W60', variable: 'dark industrial rewrite, Weirdness 60', weirdness: 60 },

  // Kai, 2026-08-26 (eighth pass): "more indie with more guitars — distorted guitars — keeping
  // the dark industrial drum and bass foundation." Swaps only: `cold jangle` → `fuzzed indie
  // guitar` in both style and My Taste; `corroded` (style) and `hand-swept filters` (My Taste)
  // deleted to pay for it. No new genre word added — see the sheet's h8 note.
  { id: 'w01-w30', name: 'S indie W30', variable: 'indie distorted guitar, Weirdness 30', weirdness: 30 },
  { id: 'w02-w50', name: 'T indie W50', variable: 'indie distorted guitar, Weirdness 50', weirdness: 50 },
  { id: 'w03-w60', name: 'U indie W60', variable: 'indie distorted guitar, Weirdness 60', weirdness: 60 },

  // Kai, 2026-08-26 (narrowed sweep): "a candidate I dragged out of that" — narrowing the
  // Weirdness range around 30-40 rather than the wider 30/50/60 spread. Same style/taste/exclude/
  // lyrics as h8.
  { id: 'w04-w30', name: 'V indie W30b', variable: 'indie distorted guitar, Weirdness 30 (re-roll)', weirdness: 30 },
  { id: 'w05-w40', name: 'W indie W40', variable: 'indie distorted guitar, Weirdness 40', weirdness: 40 },
  { id: 'w06-w45', name: 'X indie W45', variable: 'indie distorted guitar, Weirdness 45', weirdness: 45 },

  // Kai, 2026-08-26 (h9): "a really wicked heavy metal electric guitar lick" for a short intro,
  // straight into the beat and the vocal; force occasional melodic distorted-guitar bursts
  // explicitly, since it's only happened by chance a couple of times so far. Swaps only — see the
  // sheet's h9 note for the exact diff and the character accounting.
  { id: 'w07-w30', name: 'Y rock-intro W30', variable: 'heavy rock guitar intro, Weirdness 30', weirdness: 30 },
  { id: 'w08-w40', name: 'Z rock-intro W40', variable: 'heavy rock guitar intro, Weirdness 40', weirdness: 40 },
  { id: 'w09-w45', name: 'AA rock-intro W45', variable: 'heavy rock guitar intro, Weirdness 45', weirdness: 45 },

  // Kai, 2026-08-26 (h10): "too much distortion now — the bass is distorted, the guitar's
  // distorted, it's all mud." Move the guitar UP and OUT of the low end: high-register 80s rock
  // lead guitar, Whitesnake / Steve Vai toned, melodic runs rather than a low riff or chords.
  // 🔴 CRITICAL FIX bundled in: the exclude list still banned `guitar solo`, `lead guitar` and
  // `shredding` from the Madness-era cleanup — directly fighting this direction. Lifted, along
  // with `wah` (period-correct to the tone). These rounds reuse w07/w08/w09's ids — same
  // Weirdness sweep, new baseline, no new round objects needed since rounds read the sheet fresh.
  { id: 'w10-w30', name: 'AB vai-lead W30', variable: 'high-register 80s lead guitar, Weirdness 30', weirdness: 30 },
  { id: 'w11-w40', name: 'AC vai-lead W40', variable: 'high-register 80s lead guitar, Weirdness 40', weirdness: 40 },
  { id: 'w12-w45', name: 'AD vai-lead W45', variable: 'high-register 80s lead guitar, Weirdness 45', weirdness: 45 },

  // Kai, 2026-08-26 (h11): dial back the Vai/rock intensity — clean high guitar flourishes,
  // consistent but small, trading call-and-response with a sparse dub piano. Style/taste level
  // change only, lyrics cues untouched on Kai's instruction. See the sheet's h11 note for the
  // exact diff and the flagged skank/2-tone/reggae/ska exclude tension.
  { id: 'w13-w30', name: 'AE clean-piano W30', variable: 'clean guitar + dub piano call-and-response, Weirdness 30', weirdness: 30 },
  { id: 'w14-w40', name: 'AF clean-piano W40', variable: 'clean guitar + dub piano call-and-response, Weirdness 40', weirdness: 40 },
  { id: 'w15-w45', name: 'AG clean-piano W45', variable: 'clean guitar + dub piano call-and-response, Weirdness 45', weirdness: 45 },

  // Kai, 2026-08-26 (h12): the biggest pivot yet — drop `never rapped, half the speed of the
  // beat` (the identity of the accepted S7 take) in favour of an indie rap-rock delivery locked
  // tight to the beat, nu-metal in tone (Kai's reference point, expanded into descriptive words
  // after Suno itself warned on the artist name — same rule as a Flow policy block: describe the
  // sound, never name the act). Kai's diagnosis: the half-time spoken words were drifting off the
  // beat on a lot of takes. See the sheet's h12 note for the full diff — this also lifted several
  // vocal-melody exclude bans that were fighting the sung-hook half of the nu-metal sound.
  { id: 'w16-w30', name: 'AH rap-rock W30', variable: 'rap-rock delivery, aggressive verse + sung hook, Weirdness 30', weirdness: 30 },
  { id: 'w17-w40', name: 'AI rap-rock W40', variable: 'rap-rock delivery, aggressive verse + sung hook, Weirdness 40', weirdness: 40 },
  { id: 'w18-w45', name: 'AJ rap-rock W45', variable: 'rap-rock delivery, aggressive verse + sung hook, Weirdness 45', weirdness: 45 },
]

function patch(text: string, p: Patch | undefined, where: string): string {
  if (!p) return text
  let out = text
  for (const [from, to] of p) {
    if (!out.includes(from)) throw new Error(`stale round: ${where} has no ${JSON.stringify(from)} — the baseline moved`)
    out = out.split(from).join(to)
  }
  return out
}

export function resolve(r: Round): Boxes {
  const b = baseline()
  return {
    taste: patch(b.taste, r.taste, 'taste'),
    style: patch(b.style, r.style, 'style'),
    exclude: patch(b.exclude, r.exclude, 'exclude'),
    lyrics: patch(b.lyrics, r.lyrics, 'lyrics'),
    weirdness: r.weirdness ?? b.weirdness,
    styleInfluence: r.styleInfluence ?? b.styleInfluence,
    durationSec: r.durationSec ?? b.durationSec,
  }
}

export const titleFor = (r: Round) => `Camping HT ${r.name}${SET}`

// ─── the words guard ──────────────────────────────────────────────────────────────────────────

const shape = (t: string) => t.split('\n').map((l) => l.trim()).filter(Boolean).join('\n')
const wordsOnly = (t: string) => shape(t).split('\n').filter((l) => !l.startsWith('[')).join('\n')

function canonWords(): string {
  const m = readFileSync(CANON, 'utf8').match(/```lyrics\n([\s\S]*?)\n```/)
  if (!m) throw new Error(`no \`\`\`lyrics block in ${CANON}`)
  return wordsOnly(m[1])
}

/** Empty when the sheet's words match canon; otherwise the first few differing lines. */
function wordDrift(): string[] {
  const a = canonWords().split('\n')
  const b = wordsOnly(baseline().lyrics).split('\n')
  const out: string[] = []
  for (let i = 0; i < Math.max(a.length, b.length) && out.length < 12; i++) {
    if (a[i] !== b[i]) out.push(`  camping.md: ${a[i] ?? '(none)'}\n  half-time : ${b[i] ?? '(none)'}`)
  }
  return out
}

// ─── the browser ──────────────────────────────────────────────────────────────────────────────

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
 * Fill a React-controlled input and prove it took. The exclude box truncates on the second
 * variation of a multi-id run — four times now, at 117/831, 169/871 and 180/695 — and the varying
 * prefix length reads like stale React state racing `.fill()` rather than a maxlength. A blur
 * between the clear and the refill settles it.
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

async function loadRound(page: Page, r: Round, title = titleFor(r)) {
  const b = resolve(r)
  const bad: string[] = []

  // My Taste first: slowest control, and the one whose failure invalidates everything after it.
  console.log(`   ${await setTaste(page, b.taste)}`)
  const got = await getTaste(page)
  if (shape(got ?? '') !== shape(b.taste)) bad.push(`🔴 My Taste did not take — read back ${got?.length ?? 'null'}, wanted ${b.taste.length}`)

  const fills = [
    await fillChecked(page, '[data-testid="create-form-styles-wrapper"] textarea', b.style),
    await fillChecked(page, 'input[placeholder="Exclude styles"]', b.exclude),
  ]
  if (fills.some((f) => f.startsWith('🔴'))) bad.push(`fill: ${fills.join(' · ')}`)
  else if (fills.some((f) => f.includes('retry'))) console.log(`   fill: ${fills.join(' · ')}`)

  const paras = await setLyrics(page, b.lyrics)
  await setSlider(page, 'Style Influence', b.styleInfluence)
  await setSlider(page, 'Weirdness', b.weirdness)
  await setDuration(page, b.durationSec)
  await setTitle(page, title)

  const s = await formState(page)
  if (s.styleLen !== b.style.length) bad.push(`style ${s.styleLen}/${b.style.length} — truncated at the 1000 cap?`)
  if (s.excludeLen !== b.exclude.length) bad.push(`exclude ${s.excludeLen}/${b.exclude.length}`)
  // 🔴 Count paragraphs, never characters: a Lexical fill collapses the block into one <p> and
  // still reports the right length, which for a cue sheet destroys the architecture.
  if (s.lyricParas !== paras) bad.push(`lyrics ${s.lyricParas} paragraphs, expected ${paras}`)
  if (shape(await pageLyrics(page)) !== shape(b.lyrics)) bad.push('the words in the page do not match the sheet')
  if (s.coverTitle) bad.push(`🔴 AUDIO IS ATTACHED ("${s.coverTitle}") — this would be a cover, not a creation`)
  if (!String(s.url).includes('/create')) bad.push(`url is ${s.url} — NOT the create page`)
  return { state: s, problems: bad }
}

// ─── cli ──────────────────────────────────────────────────────────────────────────────────────

const IS_CLI = !!process.argv[1] && /halftime\.mts$/.test(process.argv[1])
const [cmd, ...ids] = IS_CLI ? process.argv.slice(2) : ['__imported__']
const requests = !IS_CLI ? [] : (ids.length ? ids : ROUNDS.map((r) => r.id)).flatMap((raw) => {
  const m = raw.match(/^(.+?)x(\d+)$/)
  const [id, n] = m ? [m[1], Number(m[2])] : [raw, 1]
  const r = ROUNDS.find((x) => x.id === id)
  if (!r) throw new Error(`unknown round id: ${id}`)
  return Array.from({ length: n }, (_, i) => ({ r, title: n > 1 ? `${titleFor(r)} #${i + 1}` : titleFor(r) }))
})

if (cmd === 'plan') {
  const drift = wordDrift()
  console.log(drift.length ? `🔴 WORDS DRIFTED from camping.md §4:\n${drift.join('\n')}\n` : '✅ words match camping.md §4')
  for (const { r } of requests) {
    const b = resolve(r)
    console.log(`\n── ${r.id} · ${r.name}   W=${b.weirdness} SI=${b.styleInfluence} ${b.durationSec}s`)
    console.log(`   style ${b.style.length}/1000 ${b.style.length > 1000 ? '🔴 OVER THE CAP' : ''} · exclude ${b.exclude.length} · taste ${b.taste.length}/2000`)
    console.log(`   varies: ${r.variable}`)
    const base = baseline()
    for (const k of ['style', 'taste', 'exclude', 'lyrics'] as const)
      if (b[k] !== base[k]) console.log(`   ${k} patched`)
  }
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
  console.log(`✅ saved ${live.length} chars to ${BACKUP}`)
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
  const drift = wordDrift()
  if (drift.length && !process.env.SUNO_ALLOW_WORD_DRIFT) {
    console.log('🔴 ABORT — the half-time sheet\'s words are not camping.md §4.')
    console.log(drift.join('\n'))
    console.log('\n   Mirror the edit into whichever file is behind, or set SUNO_ALLOW_WORD_DRIFT=1 if it is deliberate.')
    process.exit(1)
  }
  if (!existsSync(BACKUP)) {
    console.log(`🔴 ABORT — no My Taste backup at ${BACKUP}. My Taste is account-wide and this run overwrites it.`)
    console.log('   Run: npx tsx scripts/suno/halftime.mts taste-backup')
    process.exit(1)
  }
  const { browser, page } = await connect()
  const start = await formState(page)
  if (start.coverTitle) {
    console.log(`🔴 ABORT — audio is attached ("${start.coverTitle}"). Remove it; this would be a cover.`)
    await browser.close()
    process.exit(1)
  }
  console.log(`✅ nothing attached · words match camping.md §4 · My Taste backed up`)
  console.log(await setWorkspace(page, WORKSPACE))

  const done: string[] = []
  for (const [i, { r, title }] of requests.entries()) {
    console.log(`\n──────── ${i + 1}/${requests.length}  ${title}`)
    const { state, problems } = await loadRound(page, r, title)
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
    console.log(JSON.stringify(await listTakes(page, 'Camping HT'), null, 0))
    console.log('\n🔴 My Taste is still set to the LAST round and is account-wide.')
    console.log('   Run: npx tsx scripts/suno/halftime.mts taste-restore')
  }
  await browser.close()
} else if (IS_CLI) {
  const b = baseline()
  console.log(`badcode halftime — iterating on the accepted Camping take. Baseline: W=${b.weirdness} SI=${b.styleInfluence} ${b.durationSec}s → ${WORKSPACE}
The prompt lives in docs/stories/camping/songs/camping-halftime.md — edit the markdown, not this file.

  plan [ids...]   resolved boxes + the words check, offline
  check           live form + My Taste, spend nothing
  taste-backup    save the house My Taste — REQUIRED before run
  taste-restore   put it back — DO THIS AFTER
  load <id>       fill one round whole, generate NOTHING
  run [ids...]    Create each in turn — 10 credits and 2 takes per id
                  repeat one: \`run r01-repeatx3\` — 3 Creates, titles suffixed #1 #2 #3

${ROUNDS.map((r) => `  ${r.id.padEnd(16)} ${r.variable}`).join('\n')}`)
}
