/**
 * badcode — drive Suno's create page over CDP.
 *
 * Attaches to the already-logged-in Chrome that `scripts/flow-chrome.sh` launches (CDP 9222,
 * the same browser Flow uses). Never launches or kills a browser: close() on a connectOverCDP
 * browser only detaches.
 *
 * The DOM map, the five silent traps and the operating protocol are documented in
 * docs/suno-gpt/automation.md. Read it before changing anything here — every workaround below
 * exists because the obvious approach silently produced the wrong result.
 *
 *   npx tsx scripts/suno/suno.mts status
 *   npx tsx scripts/suno/suno.mts extract <sheet.md> "GEN A · CUT 1" > spec.json
 *   npx tsx scripts/suno/suno.mts load  <spec.json>
 *   npx tsx scripts/suno/suno.mts pair  <spec.json>          # load, create @w30, create @w60
 *   npx tsx scripts/suno/suno.mts takes [titleFilter]
 *
 * This file must stay `.mts`: tsx transforms `.ts` as CJS and rejects top-level await.
 */
import { chromium, type Browser, type Page } from 'playwright'
import { readFileSync } from 'node:fs'

const ENDPOINT = 'http://localhost:9222'
const CREATE_URL = 'https://suno.com/create'

/** A scene's four boxes plus how to file and grade it. */
export interface SunoSpec {
  style: string
  exclude: string
  lyrics: string
  /** Shared My Taste block. Only written when `applyTaste` is set — it is account-wide. */
  taste?: string
  applyTaste?: boolean
  /** Saved Voice display name, e.g. "badcode newsreader". */
  voice?: string
  /** Base title. `pair` appends `-w30` / `-w60`. */
  title: string
  workspace?: string
  styleInfluence?: number
  audioInfluence?: number
  /** The pair. Ruled 2026-08-24: every attempt runs at both. */
  weirdness?: number[]
  /**
   * Target length in SECONDS (1–300). Omit for Auto.
   *
   * Suno treats this as a target, not a contract, and our own toolkit's §10 records that it
   * shortens reliably and repeatedly fails to stretch. So set it slightly ABOVE the picture
   * budget and trim in the edit, never below and hope it grows.
   */
  durationSec?: number
}

// ─────────────────────────────────────────────────────────────────────────────
// Page-context helpers.
//
// 🔴 These are STRINGS, not functions. tsx's esbuild injects a `__name` helper into every
// function it emits; that helper does not exist inside the page, so passing a real function
// to page.evaluate throws `ReferenceError: __name is not defined`. Same reason flow-mcp's
// dom.ts keeps its scrapers as strings.
//
// Always invoke as page.evaluate(`(${FN})(...)`) — a bare string returns the function object,
// which is not serialisable, so the call quietly resolves to undefined.
// ─────────────────────────────────────────────────────────────────────────────

/** Prelude injected into every page eval below. */
const PRELUDE = `
  const c = (s) => (s || '').trim().replace(/\\s+/g, ' ');
  const live = (e) => e && e.offsetParent !== null;
  // 🔑 Suno mounts the Simple AND Advanced panels at once, so selectors match twice. Anchor on
  // the styles wrapper (unique to Advanced) and walk up to the container holding the lyrics too.
  const panel = () => {
    const w = document.querySelector('[data-testid="create-form-styles-wrapper"]');
    if (!w) return document.body;
    let n = w;
    for (let i = 0; i < 12 && n; i++, n = n.parentElement) {
      if (n.querySelector('[aria-label="Lyrics editor"]') &&
          n.querySelector('input[placeholder="Exclude styles"]')) return n;
    }
    return document.body;
  };
`

const ev = (page: Page, body: string, ...args: unknown[]) =>
  page.evaluate(`((...a) => {${PRELUDE}${body}})(${args.map((a) => JSON.stringify(a)).join(',')})`)

export async function connect(): Promise<{ browser: Browser; page: Page }> {
  const browser = await chromium.connectOverCDP(ENDPOINT)
  const ctx = browser.contexts()[0]
  if (!ctx) throw new Error('NO_CONTEXT — is scripts/flow-chrome.sh running?')
  let page = ctx.pages().find((p) => p.url().includes('suno.com'))
  if (!page) {
    page = ctx.pages()[0] ?? (await ctx.newPage())
    await page.goto(CREATE_URL, { waitUntil: 'domcontentloaded' })
    await page.waitForTimeout(4000)
  }
  return { browser, page }
}

/**
 * Sliders are `role="slider"` divs driven by arrow keys; aria-valuenow is the source of truth
 * and the step is 1. The `next === cur` break matters: at an end stop the value stops moving
 * and the loop would otherwise spin to its guard.
 */
export async function setSlider(page: Page, label: string, target: number): Promise<string> {
  const s = page.locator(`[role="slider"][aria-label="${label}"]`)
  if (!(await s.count())) return `${label}=absent`
  await s.first().focus()
  const read = async () => Number(await s.first().getAttribute('aria-valuenow'))
  let cur = await read()
  let guard = 0
  // The step is not always 1 — Duration moves in 5s — so an exact target may be unreachable and
  // a naive loop oscillates around it forever. Stop as soon as a press stops getting us closer.
  while (cur !== target && guard++ < 300) {
    await page.keyboard.press(cur < target ? 'ArrowRight' : 'ArrowLeft')
    const next = await read()
    if (next === cur) break                                   // end stop
    if (Math.abs(next - target) >= Math.abs(cur - target)) {   // overshot; step won't divide
      await page.keyboard.press(next < cur ? 'ArrowRight' : 'ArrowLeft')
      cur = await read()
      break
    }
    cur = next
  }
  return `${label}=${cur}`
}

/**
 * The lyrics editor is Lexical. `fill()` drops the whole block into ONE <p> as a single text
 * node with raw \n characters — it renders convincingly and is structurally wrong, which for a
 * bracket-cue sheet destroys the architecture. Insert line by line instead.
 *
 * (A human pasting is fine: a real clipboard paste fires Lexical's own paste handler.)
 */
export async function setLyrics(page: Page, text: string): Promise<number> {
  const lyr = page.locator('[aria-label="Lyrics editor"]')
  await lyr.click()
  await page.keyboard.press('ControlOrMeta+a')
  await page.keyboard.press('Delete')
  const lines = text.split('\n')
  for (let i = 0; i < lines.length; i++) {
    await page.keyboard.insertText(lines[i])
    if (i < lines.length - 1) await page.keyboard.press('Enter')
  }
  await page.waitForTimeout(300)
  return lines.length
}

/** React-controlled input: a plain `.value =` is swallowed on the next render. */
export async function setTitle(page: Page, value: string) {
  return ev(
    page,
    `const inp = [...panel().querySelectorAll('input[placeholder="Song Title (Optional)"]')].filter(live)[0];
     if (!inp) return 'no-title-input';
     Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(inp, a[0]);
     inp.dispatchEvent(new Event('input', { bubbles: true }));
     return inp.value;`,
    value,
  )
}

/** Set the destination workspace. Must happen BEFORE Create — it routes the output. */
async function setWorkspace(page: Page, name: string): Promise<string> {
  const opened = await ev(
    page,
    // The Save-to control sits OUTSIDE panel(), below the form next to Create. Do NOT match the
    // button by its text: that text is the CURRENT workspace name, which is arbitrary (it read
    // "My Workspace" the first time and "gpom-story" the next, so a text match silently picked
    // the sidebar nav instead). Anchor on the "Save to..." label container and take its button.
    `const label = [...document.querySelectorAll('div,section')].filter(e => live(e)
       && /^Save to\\.\\.\\./.test(c(e.textContent)) && c(e.textContent).length < 60).pop();
     if (!label) return 'no-save-to-label';
     const btn = label.querySelector('button') ||
                 (label.parentElement && label.parentElement.querySelector('button'));
     if (!btn) return 'no-picker';
     btn.scrollIntoView({ block: 'center' }); btn.click(); return 'opened';`,
  )
  if (opened !== 'opened') return `workspace:${opened}`
  await page.waitForTimeout(1200)
  const search = page.locator('input[placeholder="Search or create..."]')
  if (!(await search.count())) return 'workspace:no-search'
  await search.first().fill(name)
  await page.waitForTimeout(900)
  const picked = await ev(
    page,
    `const pop = [...document.querySelectorAll('[role="dialog"],[role="menu"],[role="listbox"]')].filter(live).pop();
     if (!pop) return 'no-popover';
     const row = [...pop.querySelectorAll('*')].filter(e => live(e)
       && c(e.textContent).toLowerCase().startsWith(String(a[0]).toLowerCase())
       && c(e.textContent).length < 60).pop();
     if (!row) return 'no-row';
     let n = row;
     for (let i = 0; i < 6 && n; i++, n = n.parentElement) {
       if (n.tagName === 'BUTTON' || /cursor-pointer/.test(String(n.className))) { n.click(); return 'picked'; }
     }
     row.click(); return 'picked-leaf';`,
    name,
  )
  await page.waitForTimeout(900)
  await page.keyboard.press('Escape')
  return `workspace:${picked}`
}

/**
 * Attach a saved Voice.
 *
 * 🔴 THE TRAP: this pops "Overwrite Styles? This Persona has styles." Overwrite replaces the
 * Style box with the persona's OWN styles — for `badcode newsreader` that is the orchestral
 * cut's 174 BPM terrace chant — and the box looks populated afterwards, so it is silent.
 * Kai's ruling, 2026-08-24: ALWAYS Keep Current.
 */
async function attachVoice(page: Page, name: string): Promise<string> {
  const opened = await ev(
    page,
    `const already = [...panel().querySelectorAll('*')].some(x => live(x)
       && new RegExp(a[0], 'i').test(c(x.textContent)) && c(x.textContent).length < 40);
     if (already) return 'already';
     const b = [...panel().querySelectorAll('button[aria-label="Add Voice"]')].filter(live);
     if (!b.length) return 'no-button';
     b[0].scrollIntoView({ block: 'center' }); b[0].click(); return 'opened';`,
    name,
  )
  if (opened !== 'opened') return `voice:${opened}`
  await page.waitForTimeout(1600)
  // The voice card is a plain div with `cursor-pointer` — no role="button". And there are
  // three [role=dialog] nodes, most of them empty, so search the document rather than scoping.
  await ev(
    page,
    `const hits = [...document.querySelectorAll('*')].filter(e => live(e) && new RegExp(a[0], 'i').test(c(e.textContent)));
     if (!hits.length) return 'not-found';
     let n = hits[hits.length - 1];
     for (let i = 0; i < 8 && n; i++, n = n.parentElement) {
       if (n.tagName === 'BUTTON' || /cursor-pointer/.test(String(n.className))) { n.click(); return 'clicked'; }
     }
     return 'no-clickable';`,
    name,
  )
  await page.waitForTimeout(1800)
  const guard = await ev(
    page,
    `const b = [...document.querySelectorAll('button')].find(x => /^keep current$/i.test(c(x.innerText)));
     if (b) { b.click(); return 'kept-current'; }
     return 'no-overwrite-dialog';`,
  )
  await page.waitForTimeout(1200)
  return `voice:attached (${guard})`
}

/** Read everything back. Paragraph count is the only check that catches the Lexical trap. */
export async function verify(page: Page) {
  return ev(
    page,
    `const st = document.querySelector('[data-testid="create-form-styles-wrapper"] textarea');
     const ex = document.querySelector('input[placeholder="Exclude styles"]');
     const ly = document.querySelector('[aria-label="Lyrics editor"]');
     const ti = [...panel().querySelectorAll('input[placeholder="Song Title (Optional)"]')].filter(live)[0];
     const cr = document.querySelector('[aria-label^="Credits remaining"]');
     const ws = [...document.querySelectorAll('*')].filter(x => live(x)
       && /^Save to\\.\\.\\./.test(c(x.textContent)) && c(x.textContent).length < 60);
     return {
       url: location.href,
       styleLen: st ? st.value.length : null,
       styleCap: st ? st.maxLength : null,
       excludeLen: ex ? ex.value.length : null,
       lyricParas: ly ? ly.querySelectorAll('p').length : null,
       title: ti ? ti.value : null,
       workspace: ws.length ? c(ws[0].textContent).replace(/^Save to\\.\\.\\./, '') : null,
       sliders: [...document.querySelectorAll('[role="slider"]')]
         .filter(s => s.getBoundingClientRect().y > -50)
         .map(s => s.getAttribute('aria-label') + '=' + s.getAttribute('aria-valuenow')),
       credits: cr ? cr.getAttribute('aria-label') : null,
       durationSec: (() => { const d = document.querySelector('[role="slider"][aria-label="Duration"]'); return d ? d.getAttribute('aria-valuenow') : 'not-mounted (More Options collapsed)'; })(),
     };`,
  )
}

/** Load all four boxes plus voice, title and workspace. Does NOT generate. */
async function load(page: Page, spec: SunoSpec, weirdness?: number) {
  if (!page.url().includes('/create')) {
    await page.goto(CREATE_URL, { waitUntil: 'domcontentloaded' })
    await page.waitForTimeout(4000)
  }
  if (spec.applyTaste && spec.taste) console.log('taste:', await setTaste(page, spec.taste))

  await page.locator('[data-testid="create-form-styles-wrapper"] textarea').fill(spec.style)
  await page.locator('input[placeholder="Exclude styles"]').first().fill(spec.exclude)
  const paras = await setLyrics(page, spec.lyrics)

  console.log(await setSlider(page, 'Style Influence', spec.styleInfluence ?? 75))
  if (weirdness !== undefined) console.log(await setSlider(page, 'Weirdness', weirdness))
  if (spec.voice) {
    console.log(await attachVoice(page, spec.voice))
    console.log(await setSlider(page, 'Audio Influence', spec.audioInfluence ?? 50))
  }
  if (spec.durationSec) console.log(await setDuration(page, spec.durationSec))
  if (spec.title) console.log('title:', await setTitle(page, spec.title))
  if (spec.workspace) console.log(await setWorkspace(page, spec.workspace))

  // Assertions that actually catch things. Character count passes on a broken lyrics load.
  const v = (await verify(page)) as Record<string, unknown>
  const problems: string[] = []
  if (v.styleLen !== spec.style.length)
    problems.push(`style ${v.styleLen}/${spec.style.length} — TRUNCATED at the ${v.styleCap} cap?`)
  if (v.lyricParas !== paras) problems.push(`lyrics ${v.lyricParas} paragraphs, expected ${paras}`)
  return { verify: v, problems }
}

/**
 * Target duration, in seconds.
 *
 * 🔴 Two duration controls exist and only one is ours. The `input[placeholder="Auto"]`
 * (type=number, 1–300, with Custom/Auto toggles) belongs to the **Simple** panel — the two-panel
 * trap again. Advanced Mode's is a **slider**, `[role="slider"][aria-label="Duration"]`, range
 * **10–360**, step **5**. They are not linked: setting the number input leaves the slider where
 * it was, so writing to it does nothing at all in Advanced Mode.
 *
 * The slider lives inside **More Options**, which is collapsed by default and unmounts its
 * contents — so "the duration control has disappeared" almost always means that section is shut.
 * Its trigger is a React div that ignores a native el.click(); it needs a real mouse click.
 *
 * Suno treats the number as a target, not a contract, and our own toolkit's §10 records that it
 * shortens reliably and repeatedly fails to stretch — so aim slightly ABOVE the picture budget
 * and trim in the edit, never below in the hope it grows.
 */
async function setDuration(page: Page, seconds: number): Promise<string> {
  const mounted = async () =>
    ((await page.locator('[role="slider"][aria-label="Duration"]').count()) as number) > 0

  for (let i = 0; i < 3 && !(await mounted()); i++) {
    const mo = page.getByText('More Options', { exact: true })
    if (!(await mo.count())) break
    await mo.last().scrollIntoViewIfNeeded().catch(() => {})
    const box = await mo.last().boundingBox()
    if (!box) break
    await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2)
    await page.waitForTimeout(1400)
  }
  if (!(await mounted())) return 'duration:more-options-would-not-open'
  return setSlider(page, 'Duration', Math.round(seconds))
}

/** My Taste lives behind the profile menu and is ACCOUNT-WIDE — it affects every sheet. */
async function setTaste(page: Page, text: string): Promise<string> {
  await ev(page, `const b = document.querySelector('[data-testid="profile-menu-button"]'); if (b) b.click();`)
  await page.waitForTimeout(1000)
  const opened = await ev(
    page,
    `const el = [...document.querySelectorAll('button,[role="menuitem"],div')].filter(x => live(x) && /^my taste$/i.test(c(x.textContent))).pop();
     if (!el) return 'no-menu-item'; el.click(); return 'opened';`,
  )
  if (opened !== 'opened') return `taste:${opened}`
  await page.waitForTimeout(2000)
  const box = page.locator('textarea[maxlength="2000"]')
  if (!(await box.count())) return 'taste:no-box'
  await box.first().fill(text)
  await page.waitForTimeout(500)
  const saved = await ev(
    page,
    `const b = [...document.querySelectorAll('button')].find(x => live(x) && /^save$/i.test(c(x.innerText)));
     if (!b) return 'no-save'; b.click(); return 'saved';`,
  )
  await page.waitForTimeout(2500)
  await page.keyboard.press('Escape')
  return `taste:${saved}`
}

/** Click Create and wait for takes carrying `title` to appear. 10 credits, 2 takes per click. */
export async function create(page: Page, title: string, timeoutMs = 240000): Promise<string> {
  // 🔴 aria-label="Create song". NOT aria-label="Generate" — that is the Lyricist.
  const clicked = await ev(
    page,
    `const b = [...document.querySelectorAll('button')].find(x => live(x) && x.getAttribute('aria-label') === 'Create song');
     if (!b) return 'no-button';
     if (b.disabled) return 'disabled';
     b.scrollIntoView({ block: 'center' }); b.click(); return 'clicked';`,
  )
  if (clicked !== 'clicked') return `create:${clicked}`
  const deadline = Date.now() + timeoutMs
  while (Date.now() < deadline) {
    await page.waitForTimeout(6000)
    const takes = (await listTakes(page, title)) as unknown[]
    if (takes.length >= 2) return `create:ok (${takes.length} takes)`
  }
  return 'create:timeout — clicked, but takes did not appear in time'
}

/**
 * The right-hand pane is SHARED between the clip list and the workspace browser, and opening
 * the Save-to picker leaves it on the browser — so `Select clip` rows vanish and a take listing
 * comes back empty even though the takes exist. Click back into the current workspace to restore
 * the clip list. Deliberately a click, not a navigation: navigating would wipe the create form.
 */
export async function ensureClipList(page: Page): Promise<string> {
  const n = await ev(page, `return document.querySelectorAll('[aria-label="Select clip"]').length;`)
  if ((n as number) > 0) return 'clip-list'
  const name = await ev(
    page,
    // Take the LONGEST match, not the last: the workspace name lives in a sibling button, so
     // the innermost element reads just "Save to..." and yields an empty name.
    `const ws = [...document.querySelectorAll('*')].filter(x => live(x)
       && /^Save to\\.\\.\\./.test(c(x.textContent)) && c(x.textContent).length < 60)
       .sort((p, q) => c(q.textContent).length - c(p.textContent).length)[0];
     const n = ws ? c(ws.textContent).replace(/^Save to\\.\\.\\./, '').trim() : '';
     return n || null;`,
  )
  if (!name) return 'no-workspace-name'
  const clicked = await ev(
    page,
    `const row = [...document.querySelectorAll('*')].filter(e => live(e)
       && c(e.textContent).startsWith(String(a[0]))
       && /\\d+ Songs/.test(c(e.textContent)) && c(e.textContent).length < 80).pop();
     if (!row) return 'no-row';
     let n = row;
     for (let i = 0; i < 6 && n; i++, n = n.parentElement) {
       if (n.tagName === 'BUTTON' || /cursor-pointer/.test(String(n.className))) { n.click(); return 'clicked'; }
     }
     row.click(); return 'clicked-leaf';`,
    name,
  )
  await page.waitForTimeout(2000)
  return `restored:${clicked}`
}

/** Read the clip rows back: title + duration. Rendering clips report a null duration. */
export async function listTakes(page: Page, filter = '') {
  await ensureClipList(page)
  return ev(
    page,
    `return [...document.querySelectorAll('[aria-label="Select clip"]')].map(sel => {
       let n = sel;
       for (let i = 0; i < 9 && n; i++, n = n.parentElement) {
         const t = c(n.innerText);
         if (t.length > 12) {
           const dur = (t.match(/\\b(\\d+:\\d\\d)\\b/) || [])[1] || null;
           const title = t.replace(/^\\d+:\\d\\d\\s*/, '').split(/\\s+v\\d|\\s{2,}/)[0].slice(0, 48);
           return { title, dur };
         }
       }
       return null;
     }).filter(x => x && (!a[0] || x.title.toLowerCase().includes(String(a[0]).toLowerCase())));`,
    filter,
  )
}

/** Pull the four boxes out of a markdown sheet by section heading. */
function extract(file: string, section: string, tasteSection = 'The shared profile') {
  const src = readFileSync(file, 'utf8')
  const F = '`'.repeat(3)
  const blocks = (txt: string) => {
    const re = new RegExp('\\n' + F + '[a-z]*\\n([\\s\\S]*?)\\n' + F + '\\n', 'g')
    const out: string[] = []
    let m: RegExpExecArray | null
    while ((m = re.exec(txt))) out.push(m[1])
    return out
  }
  const after = (re: RegExp) => {
    const i = src.search(re)
    if (i === -1) throw new Error(`section not found: ${re}`)
    return src.slice(i + 1)
  }
  // A section runs to the next heading of the same or higher level.
  const slice = (re: RegExp) => {
    const rest = after(re)
    const end = rest.search(/\n#{2,3} /)
    return end === -1 ? rest : rest.slice(0, end)
  }
  const boxes = blocks(slice(new RegExp(section.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))))
  if (boxes.length < 3) throw new Error(`expected 3 boxes in "${section}", found ${boxes.length}`)
  const taste = blocks(slice(new RegExp(tasteSection)))[0]
  return { style: boxes[0], exclude: boxes[1], lyrics: boxes[2], taste }
}

// ─────────────────────────────────────────────────────────────────────────────

// Only dispatch when run directly — `cover-ab.mts` imports the helpers above, and an
// unguarded top-level dispatch would print the usage banner on every import.
const IS_CLI = !!process.argv[1] && /suno\.mts$/.test(process.argv[1])
const [cmd, ...rest] = IS_CLI ? process.argv.slice(2) : ['__imported__']

if (cmd === 'extract') {
  const [file, section, tasteSection] = rest
  console.log(JSON.stringify(extract(file, section, tasteSection), null, 2))
} else if (cmd === 'status') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await verify(page), null, 2))
  await browser.close()
} else if (cmd === 'takes') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await listTakes(page, rest[0] ?? ''), null, 2))
  await browser.close()
} else if (cmd === 'load' || cmd === 'pair') {
  const spec: SunoSpec = JSON.parse(readFileSync(rest[0], 'utf8'))
  const { browser, page } = await connect()
  const weirdnesses = spec.weirdness ?? [30, 60]

  if (cmd === 'load') {
    const { verify: v, problems } = await load(page, spec, weirdnesses[0])
    console.log(JSON.stringify(v, null, 2))
    if (problems.length) console.log('🔴 PROBLEMS:', problems.join(' · '))
    else console.log('✅ loaded — nothing generated; run `pair` or click Create')
  } else {
    // The form survives its own generation, so the second half is a nudge + a retitle.
    const base = spec.title
    for (const [i, w] of weirdnesses.entries()) {
      const title = `${base}-w${w}`
      if (i === 0) {
        const { problems } = await load(page, { ...spec, title }, w)
        if (problems.length) {
          console.log('🔴 ABORTING before spending credits:', problems.join(' · '))
          break
        }
      } else {
        console.log(await setSlider(page, 'Weirdness', w))
        console.log('title:', await setTitle(page, title))
      }
      console.log(`▶ ${title}:`, await create(page, title))
    }
    console.log(JSON.stringify(await listTakes(page, base), null, 2))
  }
  await browser.close()
} else if (IS_CLI) {
  console.log(`badcode suno — drive suno.com/create over CDP. See docs/suno-gpt/automation.md

  status                          read the create form back
  extract <sheet.md> "<section>"  pull style/exclude/lyrics/taste out of a sheet
  load  <spec.json>               fill everything, generate NOTHING
  pair  <spec.json>               load, then Create at each weirdness (default 30 and 60)
  takes [titleFilter]             list clip rows with durations

Create costs 10 credits and returns 2 takes. \`load\` never spends credits.`)
}
