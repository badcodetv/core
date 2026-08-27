/**
 * badcode — drive Suno's create page over CDP.
 *
 * Attaches to the already-logged-in Chrome on THIS SESSION'S CHANNEL — the same browser Flow
 * uses. Get one with `./scripts/browser-channel.sh claim`; never pick a port by hand. Never
 * launches or kills a browser: close() on a connectOverCDP browser only detaches.
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
import { readFileSync, readdirSync, writeFileSync } from 'node:fs'

/**
 * CHANNELS — one browser per Claude session (2026-08-26). Suno shares its session's Flow
 * browser, so it must resolve the same channel rather than assuming 9222.
 *
 * Precedence: SUNO_CDP_ENDPOINT → FLOW_CDP_PORT → the channel this session's flow MCP server
 * has locked → 9222. Get a channel with `./scripts/browser-channel.sh claim`; never pick a port.
 */
function resolveEndpoint(): string {
  if (process.env.SUNO_CDP_ENDPOINT) return process.env.SUNO_CDP_ENDPOINT
  if (process.env.FLOW_CDP_PORT) return `http://localhost:${process.env.FLOW_CDP_PORT}`
  // A .flow-channels/<n>.lock names the channel a live session holds. Take that one, so Suno
  // and Flow in the same session share a browser instead of racing for two.
  try {
    const dir = new URL('../../.flow-channels/', import.meta.url)
    for (const f of readdirSync(dir).sort()) {
      const m = /^(\d+)\.lock$/.exec(f)
      if (!m) continue
      const pid = Number(readFileSync(new URL(f, dir), 'utf8').trim().split(/\s+/)[0])
      // Signal 0: EPERM means it exists but is another user's — still alive.
      let alive = false
      try {
        process.kill(pid, 0)
        alive = true
      } catch (e) {
        alive = (e as NodeJS.ErrnoException)?.code === 'EPERM'
      }
      if (alive) return `http://localhost:${9221 + Number(m[1])}`
    }
  } catch {
    /* no lock dir yet — fall through to the default */
  }
  return 'http://localhost:9222'
}
const ENDPOINT = resolveEndpoint()
const CREATE_URL = 'https://suno.com/create'
/** Where `taste <file>` stashes the previous account-wide profile before overwriting it. */
const BACKUP = new URL('.my-taste-backup.txt', import.meta.url).pathname

/** A scene's four boxes plus how to file and grade it. */
export interface SunoSpec {
  style: string
  exclude: string
  lyrics: string
  /**
   * 🔑 My Taste — the FOURTH BOX, and part of the atom (Kai, 2026-08-27).
   *
   * It is account-wide, so it is the one box that persists between runs and the one that
   * silently biases a generation it was never written for. **`load` writes it every time** and
   * REFUSES a spec without it, because a prompt change means all four boxes change together.
   * Set `applyTaste: false` ONLY for a deliberate slider-only round, where no prompt moves.
   */
  taste?: string
  applyTaste?: boolean
  /**
   * 🔴 Which MODE the create form must be in. Default `'custom'` — a plain generation.
   *
   * The form has FOUR mode tabs (Simple · Audio · Custom · Cover) and an Audio/Voice/Inspo
   * attachment row, and **none of it is cleared by filling the four boxes.** A session that
   * leaves the form in **Cover** mode with a source attached hands the next session a form that
   * silently generates COVERS of somebody else's track — carrying that track's arrangement, which
   * looks exactly like "music is leaking into my dry read".
   *
   * Proven 2026-08-27: two GPOM narration pairs (revisions A and B, 40 credits) were generated as
   * covers of a Camping source left attached by another session. Both are void.
   */
  mode?: 'custom' | 'cover'
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

/**
 * 🔴 OUR TAB, NOT HIS (2026-08-27). Kai works in his own Suno and Flow tabs in the same browser,
 * in parallel with a session. Two things here used to trample that:
 *
 *   1. Taking the FIRST suno.com tab grabbed whichever was his.
 *   2. With no Suno tab at all, the old code called goto() on `pages()[0]` — which with a Flow
 *      tab in slot 0 silently threw away his Flow session. It now opens a NEW tab.
 *
 * 🔴 The tab is claimed by a **sessionStorage marker, not an index.** CDP's page order is NOT
 *    creation order and it reshuffles — observed live: a freshly opened tab reported index 2 and
 *    listed at index 0 seconds later. sessionStorage is per-tab and survives same-origin
 *    navigation, so the mark still identifies the tab after Kai does Remix ▸ Cover inside it,
 *    which is the whole point — the cover attaches in OUR tab and stays findable.
 *
 * If the marked tab is gone we fall back to the only Suno tab, and refuse when several are open
 * rather than guess at his. A wrong tab is never silent anyway: the cover workflows abort on the
 * missing attachment before spending a credit.
 */
const TAB_MARK = '__badcode_suno_tab'

async function isOurs(p: Page): Promise<boolean> {
  try {
    return (await p.evaluate(`sessionStorage.getItem(${JSON.stringify(TAB_MARK)})`)) === '1'
  } catch {
    return false // cross-origin, closed, or mid-navigation — not a tab we can claim
  }
}

export async function connect(): Promise<{ browser: Browser; page: Page }> {
  const browser = await chromium.connectOverCDP(ENDPOINT)
  const ctx = browser.contexts()[0]
  if (!ctx) throw new Error('NO_CONTEXT — is a browser channel up? ./scripts/browser-channel.sh claim')
  const suno = ctx.pages().filter((p) => p.url().includes('suno.com'))

  for (const p of suno) if (await isOurs(p)) return { browser, page: p }

  if (suno.length === 1) return { browser, page: suno[0] }
  if (suno.length > 1) {
    throw new Error(
      `${suno.length} Suno tabs open and none is marked as ours — one of them is Kai's.\n` +
        '   Run: npx tsx scripts/suno/suno.mts open-tab   (then re-attach the cover in that tab)',
    )
  }

  const page = await ctx.newPage()
  await page.goto(CREATE_URL, { waitUntil: 'domcontentloaded' })
  await page.waitForTimeout(4000)
  await page.evaluate(`sessionStorage.setItem(${JSON.stringify(TAB_MARK)}, '1')`)
  return { browser, page }
}

/** Every open tab, flagged with whether it is the one this tooling drives. */
export async function listTabs(): Promise<string> {
  const browser = await chromium.connectOverCDP(ENDPOINT)
  const ctx = browser.contexts()[0]
  if (!ctx) throw new Error('NO_CONTEXT — is a browser channel up? ./scripts/browser-channel.sh claim')
  const out: string[] = []
  for (const [i, p] of ctx.pages().entries()) {
    let t = ''
    try {
      t = await p.title()
    } catch {
      /* a tab mid-navigation has no title yet — the URL is enough to identify it */
    }
    out.push(`[${i}] ${(await isOurs(p)) ? '👈 OURS  ' : '         '}${p.url().slice(0, 90)}\n              ${t}`)
  }
  await browser.close()
  return out.join('\n')
}

/** Open a dedicated, marked Suno tab. Never touches an existing one. */
export async function openTab(): Promise<void> {
  const browser = await chromium.connectOverCDP(ENDPOINT)
  const ctx = browser.contexts()[0]
  if (!ctx) throw new Error('NO_CONTEXT — is a browser channel up? ./scripts/browser-channel.sh claim')
  for (const p of ctx.pages()) {
    // Drop a stale mark first, so exactly one tab ever answers to it.
    if (p.url().includes('suno.com') && (await isOurs(p))) {
      await p.evaluate(`sessionStorage.removeItem(${JSON.stringify(TAB_MARK)})`).catch(() => {})
    }
  }
  const page = await ctx.newPage()
  await page.goto(CREATE_URL, { waitUntil: 'domcontentloaded' })
  await page.waitForTimeout(4000)
  await page.evaluate(`sessionStorage.setItem(${JSON.stringify(TAB_MARK)}, '1')`)
  await page.bringToFront()
  await browser.close()
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
export async function setWorkspace(page: Page, name: string): Promise<string> {
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
/**
 * What MODE is the form in, and is anything attached?
 *
 * 🔴 The single most expensive thing we have failed to check. Filling style/excludes/lyrics does
 * not clear a mode tab or an attached audio source, so an inherited form generates the wrong KIND
 * of thing while every box reads correctly.
 *
 * ⬜ **Selectors UNVERIFIED beyond a single live read on 2026-08-27.** They report; they do not
 * yet clear. Clearing an attachment is still a human act.
 */
export async function formMode(page: Page): Promise<{ mode: string | null; attached: string | null }> {
  const raw = await ev(
    page,
    `const c = s => (s||'').replace(/\\s+/g,' ').trim();
     const live = e => e && e.offsetParent !== null;
     const tabs = [...document.querySelectorAll('[role=tab],button')].filter(live)
       .filter(x => /^(simple|audio|custom|cover)$/i.test(c(x.innerText)));
     const on = tabs.find(x => x.getAttribute('aria-selected') === 'true'
       || /(selected|active)/i.test(String(x.className)));
     // A Cover/Audio source shows as a clip card with a title next to the attachment row.
     const row = [...document.querySelectorAll('div')].find(e => live(e) && c(e.textContent) === 'AudioVoiceInspo');
     const near = row && row.parentElement ? c(row.parentElement.textContent) : '';
     const src = near.replace('AudioVoiceInspo', '').trim();
     return JSON.stringify({ mode: on ? c(on.innerText) : null, attached: src ? src.slice(0, 80) : null });`,
  )
  try {
    return JSON.parse(raw as string)
  } catch {
    return { mode: null, attached: null }
  }
}

/**
 * Fill a box and PROVE it took.
 *
 * 🔴 The exclude box truncates on a repeated fill — proven five times now (117/831, 169/871,
 * 180/695, and 117/499 on 2026-08-27). The kept prefix length varies, which rules out a
 * `maxlength` and reads like stale React state winning a race against `.fill()`. Clearing,
 * blurring and refilling wins it. Ported from `style-ab.mts`, where it was fixed first and
 * then never brought back here — which is how 2026-08-27 hit the same bug a fifth time.
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

async function load(page: Page, spec: SunoSpec, weirdness?: number) {
  if (!page.url().includes('/create')) {
    await page.goto(CREATE_URL, { waitUntil: 'domcontentloaded' })
    await page.waitForTimeout(4000)
  }
  // 🔴 MODE FIRST. Filling boxes does not clear a mode tab or an attached source, and an
  // inherited Cover form generates a cover of someone else's track with every box reading right.
  const want = spec.mode ?? 'custom'
  const fm = await formMode(page)
  if (fm.mode && fm.mode.toLowerCase() !== want) {
    throw new Error(
      `create form is in ${fm.mode.toUpperCase()} mode, expected ${want.toUpperCase()}` +
        (fm.attached ? ` with "${fm.attached}" attached` : '') +
        `. Filling the boxes will NOT clear it — switch the tab and remove the attachment by hand, ` +
        `then re-run. (Set \`mode: 'cover'\` in the spec if a cover is actually what you want.)`,
    )
  }
  if (want === 'custom' && fm.attached) {
    throw new Error(
      `create form has "${fm.attached}" ATTACHED as a source. A plain generation must have nothing ` +
        `attached — otherwise the take inherits that track's arrangement. Remove it by hand and re-run.`,
    )
  }
  console.log(`mode: ${fm.mode ?? 'unknown'}${fm.attached ? ` · attached: ${fm.attached}` : ' · nothing attached'}`)

  // 🔑 THE ATOM: taste + style + exclude + lyrics change together or not at all.
  if (spec.applyTaste === false) {
    console.log('taste: SKIPPED (slider-only round — no prompt box may change either)')
  } else if (!spec.taste) {
    throw new Error(
      'spec has no `taste`. The four boxes are one atom (2026-08-27): taste, style, exclude and ' +
        'lyrics change together. Add a ```taste fence to the style block, or pass ' +
        '`applyTaste: false` for a deliberate slider-only round.',
    )
  } else {
    // 🔑 THE FREEDOM TOKEN: only ever claim a box that is free, or one we already hold.
    const owner = await tasteOwner(page)
    if (owner !== null && owner.trim() !== spec.taste.trim()) {
      throw new Error(
        `My Taste is OWNED by another session — it reads ${JSON.stringify(owner.slice(0, 70))}… ` +
          `not "${TASTE_FREE}". PAUSE AND ASK THE HUMAN; never load over it. ` +
          `To take it deliberately: \`suno.mts taste-release\`.`,
      )
    }
    console.log(owner === null ? 'taste: box is FREE — claiming' : 'taste: already ours — reclaiming')
    console.log('taste:', await setTaste(page, spec.taste))
    const back = await getTaste(page)
    if ((back ?? '').trim() !== spec.taste.trim()) {
      throw new Error(`taste read-back MISMATCH (${(back ?? '').length}/${spec.taste.length}) — refusing to generate against the wrong global box`)
    }
    console.log('taste: ✅ read back identical')
  }

  console.log('style:', await fillChecked(page, '[data-testid="create-form-styles-wrapper"] textarea', spec.style))
  console.log('exclude:', await fillChecked(page, 'input[placeholder="Exclude styles"]', spec.exclude))
  const paras = spec.lyrics.trim()
    ? await setLyrics(page, spec.lyrics)
    : (console.log('lyrics: INSTRUMENTAL — none written'), 0)

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
  if (v.excludeLen !== spec.exclude.length)
    problems.push(`exclude ${v.excludeLen}/${spec.exclude.length} — the truncation bug; fillChecked gave up`)
  if (v.lyricParas !== paras) problems.push(`lyrics ${v.lyricParas} paragraphs, expected ${paras}`)
  if (spec.durationSec && !String(v.durationSec ?? '').startsWith(String(spec.durationSec)))
    problems.push(`duration ${v.durationSec} — wanted ${spec.durationSec}s; More Options may not have opened`)
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
export async function setDuration(page: Page, seconds: number): Promise<string> {
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
  if (!(await mounted())) {
    // 🔴 2026-08-27: the Advanced slider is GONE from the DOM. More Options is open (the exclude
    // box lives in it and fills fine), yet `[role="slider"][aria-label="Duration"]` does not
    // exist. The only duration control on the page is a `Duration / Custom / Auto` block holding
    // `input[placeholder="Auto"][type=number]` (1-300) — the SIMPLE panel's twin, which Playwright
    // reports as not visible and which our own notes record as unlinked. Diagnose, don't guess.
    const why = await ev(
      page,
      `const c = s => (s||'').replace(/\\s+/g,' ').trim();
       const mo = [...document.querySelectorAll('div')].some(e => c(e.textContent) === 'More Options');
       const ex = !!document.querySelector('input[placeholder="Exclude styles"]');
       const num = !!document.querySelector('input[placeholder="Auto"][type=number]');
       return JSON.stringify({ moreOptionsPresent: mo, moreOptionsOpen: ex, simpleNumberInput: num });`,
    )
    return `duration:NO-ADVANCED-SLIDER ${why} — Suno's DOM changed; see automation.md`
  }
  return setSlider(page, 'Duration', Math.round(seconds))
}

/** My Taste lives behind the profile menu and is ACCOUNT-WIDE — it affects every sheet. */
export async function setTaste(page: Page, text: string): Promise<string> {
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

/** Read My Taste back. The half `setTaste` never had, and the reason it stayed unverified. */
/**
 * 🔴 THE FREEDOM TOKEN (Kai's ruling, 2026-08-27). A lock file in reverse.
 *
 * My Taste is account-wide, invisible from the create form, and cannot be saved empty — a profile
 * can only be REPLACED. So there is no "unset" state to return to, and every session inherits
 * whatever the last one left. On 2026-08-27 that cost four separate silent failures in one day.
 *
 * The protocol makes the free state explicit and loud:
 *
 *   · **Before generating:** My Taste MUST read exactly `MUST_REPLACE_HERE`. Anything else means
 *     another session or a human owns the box — **stop and ask**, never load over it.
 *   · **After generating:** write the token back. That is what hands the box to the next session.
 *
 * The token is deliberately nonsense: if anyone hand-generates while it is in force, they see
 * gibberish in the box and know to fill it, instead of silently inheriting the wrong profile.
 */
export const TASTE_FREE = 'MUST_REPLACE_HERE'

/** null when the box is free; otherwise the live text, so the caller can show it and stop. */
export async function tasteOwner(page: Page): Promise<string | null> {
  const live = (await getTaste(page))?.trim() ?? ''
  return live === TASTE_FREE ? null : live
}

/** Hand the box back. Always run this when a generation round finishes, success or failure. */
export async function releaseTaste(page: Page): Promise<string> {
  await setTaste(page, TASTE_FREE)
  const back = (await getTaste(page))?.trim()
  return back === TASTE_FREE
    ? `✅ My Taste released — reads "${TASTE_FREE}", free for the next session`
    : `🔴 RELEASE FAILED — reads ${JSON.stringify(back?.slice(0, 60))}. Fix by hand before anyone else runs.`
}

export async function getTaste(page: Page): Promise<string | null> {
  await ev(page, `const b = document.querySelector('[data-testid="profile-menu-button"]'); if (b) b.click();`)
  await page.waitForTimeout(1000)
  const opened = await ev(
    page,
    `const el = [...document.querySelectorAll('button,[role="menuitem"],div')].filter(x => live(x) && /^my taste$/i.test(c(x.textContent))).pop();
     if (!el) return 'no-menu-item'; el.click(); return 'opened';`,
  )
  if (opened !== 'opened') return null
  await page.waitForTimeout(2000)
  const box = page.locator('textarea[maxlength="2000"]')
  const text = (await box.count()) ? await box.first().inputValue() : null
  await page.keyboard.press('Escape')
  await page.waitForTimeout(600)
  return text
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

/**
 * Pull the four boxes out of a markdown sheet by section heading.
 *
 * 🔑 **The four boxes are ONE ATOM** (Kai, 2026-08-27). `taste`, `style`, `exclude` and `lyrics`
 * describe the same sound and are never swapped apart — a half-changed set is a hybrid nobody
 * designed. So taste is looked for **inside the style block first**, as a ```taste fence, and only
 * falls back to a shared section for older sheets that predate the ruling.
 *
 * The old default (`tasteSection = 'The shared profile'`) encoded the *wrong* model: one taste
 * shared across every variation. That is exactly how the GPOM newsreader profile sat under
 * fourteen Camping rounds unnoticed.
 */
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
  // Fences WITH their info string, so a ```taste block can be found by name inside the atom.
  const labelled = (txt: string) => {
    const re = new RegExp('\\n' + F + '([a-z]*)\\n([\\s\\S]*?)\\n' + F + '\\n', 'g')
    const out: { label: string; body: string }[] = []
    let m: RegExpExecArray | null
    while ((m = re.exec(txt))) out.push({ label: m[1], body: m[2] })
    return out
  }
  const own = slice(new RegExp(section.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')))
  const tagged = labelled(own)
  const boxes = tagged.filter((b) => b.label !== 'taste').map((b) => b.body)
  // An INSTRUMENTAL atom has no lyrics — taste + style + excludes is the whole of it. That is a
  // valid atom, not a short one: dry-and-separate means every cut has a wordless music half.
  if (boxes.length < 2)
    throw new Error(`expected at least style + excludes in "${section}", found ${boxes.length}`)
  if (boxes.length === 2) boxes.push('')
  // 🔑 Atom first: a ```taste fence inside this style block wins over any shared section.
  const inAtom = tagged.find((b) => b.label === 'taste')?.body
  const taste = inAtom ?? blocks(slice(new RegExp(tasteSection)))[0]
  return { style: boxes[0], exclude: boxes[1], lyrics: boxes[2], taste, tasteFromAtom: !!inAtom }
}

// ─────────────────────────────────────────────────────────────────────────────

// Only dispatch when run directly — `cover-ab.mts` imports the helpers above, and an
// unguarded top-level dispatch would print the usage banner on every import.
const IS_CLI = !!process.argv[1] && /suno\.mts$/.test(process.argv[1])
const [cmd, ...rest] = IS_CLI ? process.argv.slice(2) : ['__imported__']

if (cmd === 'extract') {
  const [file, section, tasteSection] = rest
  console.log(JSON.stringify(extract(file, section, tasteSection), null, 2))
} else if (cmd === 'tabs') {
  console.log(await listTabs())
} else if (cmd === 'open-tab') {
  await openTab()
  console.log('✅ opened and marked a Suno tab — this tooling now drives that one and no other.')
  console.log('   Do the Remix ▸ Cover attach IN THAT TAB.')
} else if (cmd === 'status') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await verify(page), null, 2))
  await browser.close()
} else if (cmd === 'takes') {
  const { browser, page } = await connect()
  console.log(JSON.stringify(await listTakes(page, rest[0] ?? ''), null, 2))
  await browser.close()
} else if (cmd === 'taste') {
  // My Taste is ACCOUNT-WIDE and invisible from the create form, so the docs require reading it
  // back at the start of every session. `setTaste` existed for a year without this half.
  const { browser, page } = await connect()
  const before = await getTaste(page)
  if (rest[0]) {
    writeFileSync(BACKUP, before ?? '')
    console.log(`backed up ${(before ?? '').length} chars to ${BACKUP}`)
    console.log(await setTaste(page, readFileSync(rest[0], 'utf8').trim()))
    const after = await getTaste(page)
    console.log(after === readFileSync(rest[0], 'utf8').trim() ? '✅ read back identical' : '🔴 READ-BACK MISMATCH')
    console.log(after)
  } else {
    console.log(before ?? '(empty)')
  }
  await browser.close()
} else if (cmd === 'load' || cmd === 'pair') {
  const spec: SunoSpec = JSON.parse(readFileSync(rest[0], 'utf8'))
  const { browser, page } = await connect()
  const weirdnesses = spec.weirdness ?? [30, 60]

  try {
  if (cmd === 'load') {
    const { verify: v, problems } = await load(page, spec, weirdnesses[0])
    console.log(JSON.stringify(v, null, 2))
    if (problems.length) {
      console.log('🔴 PROBLEMS — DO NOT GENERATE:', problems.join(' · '))
      process.exitCode = 1
    } else console.log('✅ loaded — nothing generated; run `pair` or click Create')
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
  // 🔑 Hand the box back. On the failure path too — a half-finished round still leaves a
  // profile installed account-wide, which is the exact bug the token exists to stop.
  } finally {
    // Release on EVERY exit from a pair, thrown or clean.
    if (cmd === 'pair') console.log(await releaseTaste(page).catch((e) => `🔴 release failed: ${e.message}`))
    await browser.close()
  }
} else if (IS_CLI) {
  console.log(`badcode suno — drive suno.com/create over CDP. See docs/suno-gpt/automation.md

  status                          read the create form back
  taste [block.txt]               read My Taste; with a file, back up + write + verify
  extract <sheet.md> "<section>"  pull style/exclude/lyrics/taste out of a sheet
  load  <spec.json>               fill everything, generate NOTHING
  pair  <spec.json>               load, then Create at each weirdness (default 30 and 60)
  takes [titleFilter]             list clip rows with durations

Create costs 10 credits and returns 2 takes. \`load\` never spends credits.`)
}
