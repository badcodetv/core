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
 *   npx tsx scripts/suno/suno.mts explore <spec.json> --round <N> [--yes]   # dry run without --yes
 *   npx tsx scripts/suno/suno.mts takes [titleFilter]
 *
 * This file must stay `.mts`: tsx transforms `.ts` as CJS and rejects top-level await.
 */
import { chromium, type Browser, type Page } from 'playwright'
import { readFileSync, readdirSync, writeFileSync } from 'node:fs'
// take-row.mts is the pure half and imports nothing from here (a two-way import is an init cycle).
import {
  exploreCells,
  matchTakes,
  modelTag,
  SEL_SELECT_CLIP,
  SEL_SONG_LINK,
  type Take,
} from './take-row.mts'

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
      const [pidRaw, owner] = readFileSync(new URL(f, dir), 'utf8').trim().split(/\s+/)
      // 🔴 Only a FLOW session's lock names Suno's browser. The listen server holds its own lock
      //    (owner `listen`) on the AI Studio browser; following that would drive Suno in Jack's
      //    AI Studio window. (Loop plan T7, 2026-09-11.)
      if (owner !== 'flow') continue
      const pid = Number(pidRaw)
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
   * 🗄 RETIRED 2026-09-10 (Kai): "we should stop trying to use the My Taste box and always have
   * Personalize off when we generate a song, because then each song becomes an atomic unit."
   *
   * My Taste was the fourth box of the atom (2026-08-27) and in our own logs it only ever did
   * harm — an account-wide profile leaking into songs it was never written for. v6's Personalize
   * toggle ("Make variety match your taste") is now forced OFF on every load, and `load` no longer
   * reads, writes or checks the box. A `taste` in an old sheet's spec is ignored.
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
  /**
   * 🔑 v6 (mapped live 2026-09-10) — the MODEL. **Required.** `'v6'`, `'v6-wild'` (the exact
   * menu labels), or a custom model's exact name. v5.5 and older were retired on 2026-09-09.
   *
   * It is form state like every other control and it persists, so before v6 `load` silently
   * generated on whatever model the last session left selected. Now a spec must name it.
   */
  model?: string
  /** Variety step — how different the two takes of one Create are. Default `'normal'`. v6-family only. */
  variety?: VarietyStep
  /** The v6 Max Mode toggle (not the placebo code block). Default `false`. */
  maxMode?: boolean
  /** Vocal Gender segment. Default `null` = neither selected. */
  vocalGender?: 'male' | 'female' | null
  /**
   * Personalize — its single button reads "My Taste". 🔑 **ALWAYS OFF** (Kai, 2026-09-10): it is
   * forced off on every load and asserted off before every Create. Only `false` is accepted.
   */
  personalize?: false
  /** `grid` only: the axes to permute. Cells run model-outermost, weirdness-innermost. */
  grid?: GridAxes
}

export const VARIETY_STEPS = ['off', 'normal', 'high', 'extra', 'max'] as const
export type VarietyStep = (typeof VARIETY_STEPS)[number]
export interface GridAxes {
  model?: string[]
  variety?: VarietyStep[]
  maxMode?: boolean[]
  weirdness?: number[]
}

/** The model as it appears in a title (v6 → `v6`, v6-wild → `wild`). Lives in take-row.mts. */
export { modelTag }

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

  // 🔴 No Suno tab at all means this is probably not Suno's browser (e.g. the listen server's AI
  //    Studio one). Opening a create tab here would drive Suno in the wrong account, so stop.
  //    `open-tab` is the deliberate way to give a browser its first Suno tab. (Loop plan T7.)
  await browser.close()
  throw new Error(
    `WRONG_CHANNEL: the browser on ${ENDPOINT} has no suno.com tab — it may not be Suno's browser.\n` +
      '   If it IS the right browser, open one first: npx tsx scripts/suno/suno.mts open-tab',
  )
}

/** Commands that need the create page call this; a Suno tab elsewhere is the wrong place. */
export function requireCreate(page: Page): void {
  if (!page.url().includes('suno.com/create')) {
    throw new Error(`WRONG_CHANNEL: the Suno tab is on ${page.url()}, not suno.com/create — never navigate it from code (it wipes the form)`)
  }
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

// ─────────────────────────────────────────────────────────────────────────────
// v6 controls — every selector below was read off the live form on 2026-09-10.
//
// · Model: a `button[aria-haspopup="menu"]` in the header beside the Simple/Advanced/Sounds tabs,
//   text `v6`. The menu holds `[role=menuitemradio]` rows whose FIRST LEAF SPAN is the model id
//   (`v6`, `v6-wild`, `v6-mini`, then any custom models), with `aria-checked`. It needs a REAL mouse
//   click to open (React). Suno can also switch the model on its own — a "Model changed: Model was
//   automatically changed to support your selected conditions" toast was seen — so `load` reads it
//   back at the END, after the Voice, not just after setting it.
// · Variety: `[role=slider][aria-label="Variety"]`, 0–4, `aria-valuetext` Off · Normal · High ·
//   Extra · Max (descriptions: Exact style · Balanced variety · Distinct styles · Bold exploration ·
//   Unreasonably varied). Default 1 = Normal. The Home key does NOT move it; arrows do.
// · Vocal Gender (Male/Female), Duration (Custom/Auto), Max Mode (Off/On), Personalize (one
//   button, "My Taste"): segmented buttons with NO aria state. The selected one carries the class
//   `hxc-btn-variant-standard-*`; unselected ones `hxc-btn-variant-tertiary-*`.
// · All of these live inside More Options, which collapses to a clipped box rather than unmounting —
//   so coordinates are meaningless when it is shut and a mouse click lands on whatever is on top.
//   Native `el.click()` works regardless, and `focus()` + arrows works for the sliders.
// ─────────────────────────────────────────────────────────────────────────────

/** Page-side helpers for the segmented rows. Interpolate into an `ev` body. */
const SEG = `
  const segRow = (label) => {
    const s = [...document.querySelectorAll('span')].find(x => live(x) && c(x.textContent) === label);
    if (!s) return null;
    let r = s.parentElement;
    for (let i = 0; i < 6 && r; i++, r = r.parentElement) if (r.querySelector('button')) return r;
    return null;
  };
  const segOn = (b) => /hxc-btn-variant-standard/.test(String(b.className));
  const seg = (label) => {
    const r = segRow(label);
    if (!r) return 'absent';
    const s = [...r.querySelectorAll('button')].filter(segOn).map(b => c(b.innerText));
    return s.length ? s.join('+') : 'none';
  };
`

/** Click a segment option (or, with `null`, deselect whatever is selected) and read it back. */
export async function setSegment(page: Page, label: string, option: string | null): Promise<string> {
  const res = await ev(
    page,
    `${SEG}
     const r = segRow(a[0]);
     if (!r) return 'absent';
     const bs = [...r.querySelectorAll('button')];
     if (a[1] === null) {
       const on = bs.filter(segOn);
       if (!on.length) return 'already';
       on.forEach(b => b.click());
       return 'clicked';
     }
     const b = bs.find(x => c(x.innerText).toLowerCase() === String(a[1]).toLowerCase());
     if (!b) return 'no-option (' + bs.map(x => c(x.innerText)).join('/') + ')';
     if (segOn(b)) return 'already';
     b.click();
     return 'clicked';`,
    label,
    option,
  )
  if (res === 'already') return `${label}:${option ?? 'none'} (already)`
  if (res !== 'clicked') return `${label}:${res}`
  await page.waitForTimeout(600)
  const back = await ev(page, `${SEG} return seg(a[0]);`, label)
  const want = option ?? 'none'
  return String(back).toLowerCase() === want.toLowerCase() ? `${label}:${back} ✅` : `${label}:MISMATCH (wanted ${want}, reads ${back})`
}

/** Open the model menu with a real mouse click. Returns false when it will not open. */
async function openModelMenu(page: Page): Promise<boolean> {
  const at = await ev(
    page,
    `const btns = [...document.querySelectorAll('button[aria-haspopup="menu"]')].filter(live);
     let b = btns.find(x => /^v\\d/i.test(c(x.innerText)));
     if (!b) {
       // A custom model's name need not start with v — take the menu button on the tab row.
       const tab = [...document.querySelectorAll('[role=tab]')].filter(live).pop();
       if (tab) {
         const t = tab.getBoundingClientRect();
         b = btns.filter(x => { const r = x.getBoundingClientRect(); return Math.abs(r.y - t.y) < 30 && r.x > t.x; })
           .sort((p, q) => p.getBoundingClientRect().x - q.getBoundingClientRect().x)[0];
       }
     }
     if (!b) return null;
     const r = b.getBoundingClientRect();
     return JSON.stringify({ x: r.x + r.width / 2, y: r.y + r.height / 2 });`,
  )
  if (!at) return false
  const { x, y } = JSON.parse(at as string)
  await page.mouse.click(x, y)
  await page.waitForTimeout(800)
  return ((await page.locator('[role="menuitemradio"]').count()) as number) > 0
}

const RADIOS = `
  const leaf = (r) => { const s = [...r.querySelectorAll('span')].find(s => !s.children.length); return c((s || r).textContent); };
  const radios = [...document.querySelectorAll('[role="menuitemradio"]')];
`

/** The selected model, read from the menu (authoritative — the button text may abbreviate). */
export async function getModel(page: Page): Promise<string | null> {
  if (!(await openModelMenu(page))) return null
  const name = await ev(page, `${RADIOS} const r = radios.find(r => r.getAttribute('aria-checked') === 'true'); return r ? leaf(r) : null;`)
  await page.keyboard.press('Escape')
  await page.waitForTimeout(400)
  return (name as string | null) ?? null
}

export async function setModel(page: Page, name: string): Promise<string> {
  if (!(await openModelMenu(page))) return 'model:NO-MENU'
  const res = await ev(
    page,
    `${RADIOS}
     const hit = radios.find(r => leaf(r).toLowerCase() === String(a[0]).toLowerCase());
     if (!hit) return 'NOT-OFFERED (menu has: ' + radios.map(leaf).join(', ') + ')';
     if (hit.getAttribute('aria-checked') === 'true') return 'already';
     const r = hit.getBoundingClientRect();
     return JSON.stringify({ x: r.x + r.width / 2, y: r.y + r.height / 2 });`,
    name,
  )
  if (res === 'already' || !String(res).startsWith('{')) {
    await page.keyboard.press('Escape')
    await page.waitForTimeout(400)
    return res === 'already' ? `model:${name} (already)` : `model:${res}`
  }
  const { x, y } = JSON.parse(res as string)
  await page.mouse.click(x, y)
  await page.waitForTimeout(1200)
  const back = await getModel(page)
  return back?.toLowerCase() === name.toLowerCase() ? `model:${back} ✅` : `model:MISMATCH (wanted ${name}, reads ${back})`
}

/**
 * Set every v6 control from the spec, defaults included — because OMITTING A FIELD IS NOT
 * CLEARING IT (the 2026-08-27 law). A spec with no `variety` means Normal, not "whatever was left".
 */
export async function setV6Controls(page: Page, spec: Partial<SunoSpec>): Promise<string> {
  const out: string[] = []
  const step = spec.variety ?? 'normal'
  const idx = VARIETY_STEPS.indexOf(step)
  if (idx < 0) throw new Error(`variety "${step}" is not one of ${VARIETY_STEPS.join(' / ')}`)
  if (((await page.locator('[role="slider"][aria-label="Variety"]').count()) as number) === 0) {
    out.push('Variety=ABSENT (only mounts for a v6-family model)')
  } else {
    await setSlider(page, 'Variety', idx)
    out.push(`Variety=${await page.locator('[role="slider"][aria-label="Variety"]').first().getAttribute('aria-valuetext')}`)
  }
  out.push(await setSegment(page, 'Max Mode', spec.maxMode ? 'On' : 'Off'))
  out.push(await setSegment(page, 'Vocal Gender', spec.vocalGender ? spec.vocalGender[0].toUpperCase() + spec.vocalGender.slice(1) : null))
  // 🔑 Personalize is ALWAYS OFF (Kai, 2026-09-10) — the spec cannot turn it on.
  if ((spec as { personalize?: unknown }).personalize === true)
    throw new Error('spec asks for personalize: true — house rule since 2026-09-10 is Personalize ALWAYS OFF')
  out.push(await setSegment(page, 'Personalize', null))
  // In case a click ever opens the My Taste editor rather than toggling — close it.
  await page.keyboard.press('Escape')
  return out.join(' · ')
}

/** What the live form must read for this spec. Every mismatch is a reason not to spend credits. */
async function checkV6(page: Page, spec: Partial<SunoSpec>, v: Record<string, unknown>): Promise<string[]> {
  const p: string[] = []
  const model = await getModel(page)
  if (!spec.model || model?.toLowerCase() !== spec.model.toLowerCase())
    p.push(`model reads ${model}, spec says ${spec.model} — Suno can switch it on its own ("Model changed")`)
  const variety = spec.variety ?? 'normal'
  if (String(v.variety).toLowerCase() !== variety) p.push(`Variety reads ${v.variety}, wanted ${variety}`)
  if (v.maxMode !== (spec.maxMode ? 'On' : 'Off')) p.push(`Max Mode reads ${v.maxMode}`)
  const g = spec.vocalGender ?? null
  if (String(v.vocalGender).toLowerCase() !== (g ?? 'none')) p.push(`Vocal Gender reads ${v.vocalGender}, wanted ${g ?? 'none'}`)
  if (v.personalize !== 'off') p.push(`Personalize reads ${v.personalize} — house rule is ALWAYS OFF (2026-09-10)`)
  return p
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
     ${SEG}
     const vs = document.querySelector('[role="slider"][aria-label="Variety"]');
     const mb = [...document.querySelectorAll('button[aria-haspopup="menu"]')].filter(live).find(x => /^v\\d/i.test(c(x.innerText)));
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
       // v6 — the model button's text (the menu, via getModel, is authoritative).
       modelButton: mb ? c(mb.innerText) : 'no v-named menu button (a custom model?)',
       variety: vs ? vs.getAttribute('aria-valuetext') : 'absent',
       maxMode: seg('Max Mode'),
       vocalGender: seg('Vocal Gender'),
       durationMode: seg('Duration'),
       personalize: seg('Personalize') === 'My Taste' ? 'on' : seg('Personalize') === 'none' ? 'off' : seg('Personalize'),
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
    // 🔑 v6 (2026-09-10, live): the tabs are now Simple · ADVANCED · Sounds. "custom" stays our
    // internal name for the full form, so 'custom' here means the Advanced tab. Sounds is its own mode.
    `const tabs = [...document.querySelectorAll('[role=tab],button')].filter(live)
       .filter(x => /^(simple|advanced|sounds|audio|custom|cover|extend)$/i.test(c(x.innerText)));
     // 🔑 CALIBRATED 2026-08-27 against a known-clean form and a known-contaminated one.
     // Clean:        tabs are Simple / Audio / Custom, and the attachment row's OWN text is
     //               exactly "AudioVoiceInspo" (15 chars, nothing else).
     // Contaminated: a fourth tab "Cover" appears, and a clip card sits by the row
     //               ("Camping cover - post-punk AI25 W45v5.5Cover").
     // So: a Cover/Extend tab existing IS the attachment signal. Do not walk up to the parent —
     // that swallows the lyrics editor's placeholder and reads as a false positive.
     const coverTab = tabs.find(x => /^(cover|extend)$/i.test(c(x.innerText)));
     // 🔴 ONE signal only. Every attempt to also read the attachment row matched an ANCESTOR
     // and dumped the whole form as a false positive — \`find\` returns the first div in
     // document order, and the row's text is a substring of half the page.
     const simple = tabs.find(x => /^simple$/i.test(c(x.innerText)));
     const sounds = tabs.find(x => /^sounds$/i.test(c(x.innerText)));
     const mode = coverTab ? c(coverTab.innerText).toLowerCase()
       : (simple && simple.getAttribute('aria-selected') === 'true') ? 'simple'
       : (sounds && sounds.getAttribute('aria-selected') === 'true') ? 'sounds' : 'custom';
     return JSON.stringify({ mode, attached: coverTab ? c(coverTab.innerText) : null });`,
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

  // 🔑 v6: the MODEL, then the controls that only exist for a v6-family model.
  if (!spec.model)
    throw new Error(
      'spec has no `model`. Since v6 (2026-09-09) the model is an experiment axis and persists like ' +
        "every other control — name it: 'v6' or 'v6-wild' (or a custom model's exact name).",
    )
  if (/^v?[1-5](\.|$)/i.test(spec.model))
    throw new Error(`model "${spec.model}" is retired — nothing older than v6 can generate since 2026-09-09.`)
  if (/mini/i.test(spec.model)) console.log('⚠️ v6-mini: the free-tier model. House rule is never — continuing only because the spec asks.')
  console.log(await setModel(page, spec.model))
  console.log(await setV6Controls(page, spec))

  // 🔑 THE ATOM is style + exclude + lyrics (+ the settings) — Kai, 2026-09-10. My Taste is
  // retired: Personalize is forced off in setV6Controls, and the account-wide box is never read,
  // written or checked. A leftover `taste` from an old sheet is ignored, loudly.
  if (spec.taste) console.log('taste: IGNORED — My Taste is retired; Personalize is always off (2026-09-10)')

  console.log('style:', await fillChecked(page, '[data-testid="create-form-styles-wrapper"] textarea', spec.style))
  console.log('exclude:', await fillChecked(page, 'input[placeholder="Exclude styles"]', spec.exclude))
  // 🔴 An instrumental atom must CLEAR the editor, not skip it. Skipping leaves the previous
  // run's lyrics in the box — which would sing the narration over the bed. `setLyrics` already
  // select-alls and deletes before writing, so passing '' is the clear.
  const paras = await setLyrics(page, spec.lyrics)
  if (!spec.lyrics.trim()) console.log('lyrics: INSTRUMENTAL — editor cleared')

  console.log(await setSlider(page, 'Style Influence', spec.styleInfluence ?? 75))
  if (weirdness !== undefined) console.log(await setSlider(page, 'Weirdness', weirdness))
  // 🔴 A Voice, like the mode and the attachment, SURVIVES a box fill. Omitting `voice` from a
  // spec does NOT detach whatever the last run left on — so an instrumental generation silently
  // carries a vocal persona. Proven 2026-08-27: `gpom-cut1music-A` was generated with
  // `badcode newsreader` still attached because the music spec simply had no `voice` key.
  //
  // The clean detector is documented and verified: the Audio Influence slider EXISTS ONLY when a
  // Voice is attached.
  const voiceOn = async () =>
    ((await page.locator('[role="slider"][aria-label="Audio Influence"]').count()) as number) > 0
  if (spec.voice) {
    console.log(await attachVoice(page, spec.voice))
    console.log(await setSlider(page, 'Audio Influence', spec.audioInfluence ?? 50))
  } else if (await voiceOn()) {
    throw new Error(
      'a saved Voice is still ATTACHED (the Audio Influence slider is present) but this spec asks ' +
        'for none — an instrumental generation would carry a vocal persona. Detach it by hand ' +
        '(the Voice chip in the Advanced panel) and re-run, or set `voice` in the spec.',
    )
  } else {
    console.log('voice: none attached ✅')
  }
  console.log(
    spec.durationSec ? await setDuration(page, spec.durationSec) : await setDurationAuto(page),
  )
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
  // Read the model back LAST — attaching a Voice can make Suno switch it without asking.
  problems.push(...(await checkV6(page, spec, v)))
  // ⚠️ Duration is a WARNING, never a blocker. A take of the wrong length is trimmable; a round
  // that refuses to run is not. Suno treats the number as a target anyway.
  if (spec.durationSec && !String(v.durationSec ?? '').startsWith(String(spec.durationSec)))
    console.log(`⚠️ duration reads ${v.durationSec}, wanted ${spec.durationSec}s — generating anyway`)
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
/**
 * Put duration back to AUTO.
 *
 * 🔴 Omitting `durationSec` does NOT clear a duration — the form keeps whatever the last run set,
 * exactly like the mode, the attachment and the Voice. Proven 2026-08-27: eight takes came back at
 * 1:05 apiece from specs with no `durationSec` at all, because an earlier round had set 65.
 */
export async function setDurationAuto(page: Page): Promise<string> {
  // 🔑 The Duration block re-renders as you toggle it, so anchoring on its text ("DurationCustomAuto"
  // vs just "Duration") is unreliable. The number input is stable and its PLACEHOLDER IS "Auto" —
  // so an empty value IS Auto. Clear it through React's native setter, same as setTitle.
  const res = await ev(
    page,
    `const inp = document.querySelector('input[placeholder="Auto"][type=number]');
     if (!inp) return 'duration:no-input';
     if (inp.value === '') return 'duration:AUTO (already)';
     const set = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
     set.call(inp, '');
     inp.dispatchEvent(new Event('input', { bubbles: true }));
     inp.dispatchEvent(new Event('change', { bubbles: true }));
     inp.blur();
     return 'cleared';`,
  )
  if (res !== 'cleared') return String(res)
  await page.waitForTimeout(600)
  const back = await ev(page, `const i = document.querySelector('input[placeholder="Auto"][type=number]'); return i ? i.value : 'gone';`)
  return back === '' ? 'duration:AUTO ✅' : `duration:AUTO FAILED (still ${JSON.stringify(back)})`
}

export async function setDuration(page: Page, seconds: number): Promise<string> {
  // Legacy path: older Suno had a real slider inside More Options.
  if (((await page.locator('[role="slider"][aria-label="Duration"]').count()) as number) > 0)
    return setSlider(page, 'Duration', Math.round(seconds))

  // 🔑 CURRENT PATH (2026-08-27). Advanced Mode's duration is no longer a slider — it is a
  // `Duration / Custom / Auto` block with a number input (1–300). Our notes called that "the
  // Simple panel's twin, unlinked"; that is now out of date, and there is no slider to be
  // unlinked FROM. The input reports as not visible to Playwright, so it is driven the way
  // `setTitle` drives its React input: through the native value setter plus an input event.
  const res = await ev(
    page,
    `const hosts = [...document.querySelectorAll('*')].filter(e => live(e) && /^DurationCustomAuto$/.test(c(e.textContent)));
     const h = hosts[hosts.length - 1];
     if (!h) return 'no-duration-block';
     const custom = [...h.querySelectorAll('button')].find(b => /^custom$/i.test(c(b.innerText)));
     if (!custom) return 'no-custom-button';
     custom.click();
     const inp = h.querySelector('input[type=number]') || document.querySelector('input[placeholder="Auto"][type=number]');
     if (!inp) return 'no-number-input';
     const set = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
     set.call(inp, String(a[0]));
     inp.dispatchEvent(new Event('input', { bubbles: true }));
     inp.dispatchEvent(new Event('change', { bubbles: true }));
     inp.blur();
     return 'set:' + inp.value;`,
    Math.round(seconds),
  )
  await page.waitForTimeout(700)
  const back = await ev(
    page,
    `const i = document.querySelector('input[placeholder="Auto"][type=number]') ||
       [...document.querySelectorAll('input[type=number]')].pop();
     return i ? i.value : null;`,
  )
  return String(back) === String(Math.round(seconds))
    ? `duration:${back}s ✅`
    : `duration:UNCONFIRMED (${res}, reads back ${JSON.stringify(back)})`
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


/**
 * 🔴 ATTACH COVER AUDIO WITHOUT NAVIGATING — discovered 2026-08-27.
 *
 * The create form has an `Add audio` control (aria-label starts "Add audio") which opens a picker
 * with Browse / Uploads / Workspaces. Browse lists every clip in the library BY TITLE, so a cover
 * source can be attached from code. Until this was found, cover mode required a human to open the
 * song page and use ⋯ → Remix ▸ Cover, and the attachment could not be restored if it dropped.
 *
 * 🔴 IT DROPS. On 2026-08-27 a 12-cell cover round lost its attachment after the FIRST Create —
 * the audio and the (attachment-supplied) lyrics both vanished while Style and Exclude survived.
 * Earlier rounds saw an attachment survive six Creates, so the behaviour is not consistent and must
 * not be assumed. Re-attach per cell and verify.
 *
 * Every click here must be a REAL MOUSE CLICK: these are React handlers that ignore el.click(),
 * the same trap as the More Options trigger.
 */
export async function attachCover(page: Page, query: string, index = 0, wantDuration?: string): Promise<string> {
  // A search usually matches BOTH takes of a pair, identical in title and different in length, so a
  // round that must reproduce an exact source picks by duration rather than by luck of ordering.
  if (wantDuration) {
    for (let i = 0; i < 4; i++) {
      const r = await attachCover(page, query, i)
      if (r.includes(wantDuration)) return r
      if (r.startsWith('attach:index')) return `attach:no take matching ${wantDuration} for "${query}"`
      if (!r.startsWith('attach:ok')) return r
    }
    return `attach:no take matching ${wantDuration} for "${query}"`
  }
  const click = async (x: number, y: number) => { await page.mouse.click(x, y); await page.waitForTimeout(2200) }
  const hit = async (loc: unknown): Promise<boolean> => {
    const l = loc as { boundingBox: () => Promise<{ x: number; y: number; width: number; height: number } | null> }
    const b = await l.boundingBox().catch(() => null)
    if (!b) return false
    await click(b.x + b.width / 2, b.y + b.height / 2)
    return true
  }

  // 🔴 The Add-audio control TOGGLES and lives at the TOP of the create column, which is usually
  //    scrolled out of view — a boundingBox on an off-screen element still returns coordinates, so
  //    the click silently lands on empty page. Escape first (a panel left open by a previous call
  //    would be closed by the click meant to open it), then scroll it into view, then click.
  await page.keyboard.press('Escape')
  await page.waitForTimeout(600)
  const add = page.locator('button[aria-label^="Add audio"]').first()
  await add.scrollIntoViewIfNeeded().catch(() => {})
  await page.waitForTimeout(500)
  if (!(await hit(add))) return 'attach:no-add-audio-button'
  if (!(await hit(page.getByText('Browse', { exact: true }).first()))) return 'attach:no-browse-item'

  // The modal is titled "Choose a song to Remix". Its own Search box is the LAST one on the page;
  // the workspace pane behind it has one too.
  const search = page.getByPlaceholder('Search').last()
  if (!(await search.count())) return 'attach:no-search-box'
  await search.fill(query)
  await page.waitForTimeout(2500)

  // 🔴 SCOPE THE REMIX BUTTON TO THE MODAL. Every clip row in the workspace pane behind the modal
  //    also reveals a "Remix" control on hover, so an unscoped text match finds ~43 of them and
  //    clicking one dismisses the modal without attaching anything.
  const boxes = (await page.evaluate(
    `(() => {
      const c = (s) => (s || '').replace(/\\s+/g, ' ').trim()
      let n = [...document.querySelectorAll('*')].filter(e => e.offsetParent !== null
        && c(e.textContent) === 'Choose a song to Remix').pop()
      while (n && !/Library/.test(c(n.innerText || ''))) n = n.parentElement
      if (!n) return '[]'
      const btns = [...n.querySelectorAll('button,[role="button"]')]
        .filter(b => b.offsetParent !== null && c(b.innerText) === 'Remix')
        .map(b => { const r = b.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 } })
      return JSON.stringify(btns)
    })()`,
  )) as string
  const rows = JSON.parse(boxes) as { x: number; y: number }[]
  if (!rows.length) return `attach:no-match-in-picker (${query})`
  if (index >= rows.length) return `attach:index ${index} of ${rows.length} matches (${query})`
  await click(rows[index].x, rows[index].y)
  await page.waitForTimeout(1800)

  // 🔴 "Overwrite Styles?" — the SAME trap as attaching a Voice. Picking a remix source offers to
  //    replace your Style box with the source's own styles, and the answer is ALWAYS Keep Current:
  //    the sheet is the prompt, and the source's styles are whatever it happened to be made with.
  const kc = page.getByRole('button', { name: 'Keep Current', exact: true })
  if (await kc.count()) {
    await hit(kc.first())
    await page.waitForTimeout(1200)
  }

  const got = await ev(
    page,
    `const m = c(document.body.innerText).match(/Audio Cover ([^]{0,60}?) \\d\\d:\\d\\d\\/(\\d\\d:\\d\\d)/);
     return m ? c(m[1]) + ' ' + m[2] : null;`,
  )
  // 🔴 The remix picker leaves the right-hand pane on the library browser, and `listTakes` reads
  //    the CLIP LIST from that pane — so without this, `create()` polls for takes it cannot see and
  //    reports a timeout on takes that generated perfectly well (observed on cv2, 2026-08-27).
  await ensureClipList(page).catch(() => {})
  return got ? `attach:ok ${got} (${rows.length} matched, took #${index})` : 'attach:FAILED — no Audio Cover on the form'
}


/**
 * Remove the attached cover source. The control is `aria-label="Clear audio condition"` on the
 * attachment row; its sibling `Change condition type from Cover` switches Cover/Extend/etc.
 *
 * Safe to call in fresh mode because `attachCover` can put the source back in one command — before
 * 2026-08-27 detaching was irreversible without a human on the song page, which is why the runner
 * used to abort here instead.
 */
export async function detachCover(page: Page): Promise<string> {
  const b = page.locator('button[aria-label="Clear audio condition"]').first()
  if (!(await b.count())) return 'detach:nothing-attached'
  await b.scrollIntoViewIfNeeded().catch(() => {})
  const box = await b.boundingBox().catch(() => null)
  if (!box) return 'detach:not-visible'
  await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2)
  await page.waitForTimeout(1500)
  const still = await ev(page, `return /Audio Cover/.test(c(document.body.innerText)) ? 'yes' : 'no';`)
  return still === 'no' ? 'detach:ok' : 'detach:FAILED — still attached'
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

/**
 * Read the clip rows back: title, duration and song ID. Rendering clips report a null duration.
 * The song ID is the row's `/song/<uuid>` link (mapped live 2026-09-11, automation.md §10) — the
 * only thing that tells the two same-titled takes of one Create apart.
 */
export async function listTakes(page: Page, filter = ''): Promise<Take[]> {
  await ensureClipList(page)
  return ev(
    page,
    `return [...document.querySelectorAll(${JSON.stringify(SEL_SELECT_CLIP)})].map(sel => {
       let n = sel;
       for (let i = 0; i < 9 && n; i++, n = n.parentElement) {
         const t = c(n.innerText);
         if (t.length > 12) {
           const dur = (t.match(/\\b(\\d+:\\d\\d)\\b/) || [])[1] || null;
           const title = t.replace(/^\\d+:\\d\\d\\s*/, '').split(/\\s+v\\d|\\s{2,}/i)[0].slice(0, 48); // /i: v6 prints the tag as "V5.5"
           // Climb to the row that holds the song link, but never past a node holding a second
           // row — that would be the list, and its first link belongs to another take.
           let r = n;
           for (let j = 0; j < 6 && r && !r.querySelector(${JSON.stringify(SEL_SONG_LINK)}); j++) r = r.parentElement;
           const own = r && r.querySelectorAll(${JSON.stringify(SEL_SELECT_CLIP)}).length === 1 ? r.querySelector(${JSON.stringify(SEL_SONG_LINK)}) : null;
           const m = own ? /\\/song\\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/i.exec(own.getAttribute('href') || '') : null;
           return { title, dur, songId: m ? m[1].toLowerCase() : null };
         }
       }
       return null;
     }).filter(x => x && (!a[0] || x.title.toLowerCase().includes(String(a[0]).toLowerCase())));`,
    filter,
  ) as Promise<Take[]>
}

/**
 * Resolve a key (full song ID, its first 8 characters, or a title) to exactly one finished take on
 * the create page, or throw a CODE: message the caller can branch on.
 */
export async function findTake(page: Page, key: string): Promise<Take> {
  const takes = await listTakes(page)
  const hits = matchTakes(takes, key)
  if (hits.length === 0) {
    const visible = [...new Set(takes.map((t) => t.title))].slice(0, 20).join(' · ')
    throw new Error(`TAKE_NOT_FOUND: nothing on the create page matches "${key}". Visible: ${visible || '(no rows)'}`)
  }
  if (hits.length > 1) {
    const list = hits.map((t) => `${t.songId?.slice(0, 8) ?? '?'} (${t.dur ?? 'rendering'}) ${t.title}`).join(' · ')
    throw new Error(`TAKE_AMBIGUOUS: "${key}" matches ${hits.length} takes — use a song id: ${list}`)
  }
  const take = hits[0]!
  if (!take.dur) throw new Error(`TAKE_RENDERING: "${take.title}" has no duration yet — it is still generating`)
  return take
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

/**
 * One Create of the pair/grid/explore run loop. Every setting the loop re-asserts between Creates
 * lives on the cell — Style Influence included, because `explore`'s two cells differ on it.
 */
export interface RunCell {
  model: string
  variety: VarietyStep
  maxMode: boolean
  weirdness: number
  styleInfluence: number
  title: string
}

/**
 * Expand a spec into grid cells. Model outermost (fewest model switches), weirdness innermost (so
 * the pair sits side by side). An axis with one value is not written into the title.
 */
export function gridCells(spec: SunoSpec) {
  const g = spec.grid ?? {}
  if (!spec.model && !g.model?.length) throw new Error('spec has no `model` (and no grid.model) — v6 needs one')
  const models = g.model ?? [spec.model as string]
  const varieties = g.variety ?? [spec.variety ?? 'normal']
  const maxes = g.maxMode ?? [spec.maxMode ?? false]
  const ws = g.weirdness ?? spec.weirdness ?? [30, 60]
  // Style Influence is not a grid axis: every grid/pair cell carries the spec's one value.
  const styleInfluence = spec.styleInfluence ?? 75
  const cells: RunCell[] = []
  for (const model of models)
    for (const variety of varieties)
      for (const maxMode of maxes)
        for (const weirdness of ws)
          cells.push({
            model,
            variety,
            maxMode,
            weirdness,
            styleInfluence,
            title: [
              spec.title,
              modelTag(model),
              varieties.length > 1 ? `var-${variety}` : '',
              maxes.length > 1 ? (maxMode ? 'max' : 'nomax') : '',
              `w${weirdness}`,
            ].filter(Boolean).join('-'),
          })
  return cells
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
} else if (cmd === 'controls') {
  // Set ONLY the v6 controls (model, Variety, Max Mode, Vocal Gender, Personalize) and read them
  // back. Touches no prompt box — a free way to check the v6 settings on the live form.
  const spec: Partial<SunoSpec> = JSON.parse(readFileSync(rest[0], 'utf8'))
  const { browser, page } = await connect()
  try {
    if (spec.model) console.log(await setModel(page, spec.model))
    console.log(await setV6Controls(page, spec))
    const v = (await verify(page)) as Record<string, unknown>
    console.log(JSON.stringify(v, null, 2))
    const p = await checkV6(page, spec, v)
    console.log(p.length ? `🔴 ${p.join(' · ')}` : '✅ every v6 control reads back as the spec says')
  } finally {
    await browser.close()
  }
} else if (cmd === 'load' || cmd === 'pair' || cmd === 'grid' || cmd === 'grid-plan' || cmd === 'explore') {
  // `explore <spec.json> --round <N> [--yes]` — flags may sit anywhere after the command.
  const roundAt = rest.indexOf('--round')
  const specPath = rest.find((a, i) => !a.startsWith('--') && !(roundAt >= 0 && i === roundAt + 1))
  if (!specPath) {
    console.error(`${cmd}: missing <spec.json>`)
    process.exit(1)
  }
  let round = 0
  if (cmd === 'explore') {
    // 🔴 --round is REQUIRED. create() returns as soon as any 2 rows carry the title, so a reused
    //    title "succeeds" on an earlier round's takes without waiting for this round's.
    round = roundAt >= 0 ? Number(rest[roundAt + 1]) : NaN
    if (!Number.isInteger(round) || round < 1) {
      console.error(
        'explore: --round <N> is required (a positive integer). Every round needs its own titles — ' +
          "create() returns once any 2 rows carry the title, so a reused title reports success on an earlier round's takes.",
      )
      process.exit(1)
    }
  }
  const spec: SunoSpec = JSON.parse(readFileSync(specPath, 'utf8'))
  let cells: RunCell[]
  if (cmd === 'explore') {
    // Decision 6: safe end + wild end, Variety off, Max Mode off, per-cell Style Influence.
    try {
      cells = exploreCells(spec.title, round)
    } catch (e) {
      console.error(`explore: ${(e as Error).message}`)
      process.exit(1)
    }
  } else {
    // 🔑 `pair` is a grid with one axis: weirdness 30 and 60 on the spec's own model.
    cells = gridCells(cmd === 'grid' || cmd === 'grid-plan' ? spec : { ...spec, grid: undefined })
  }
  // A round's own takes only — `<title>-r<N>-` never matches another round's rows.
  const takeFilter = cmd === 'explore' ? `${spec.title}-r${round}-` : spec.title
  if (cmd === 'grid-plan') {
    console.log(`${cells.length} Creates → ${cells.length * 2} takes, into workspace ${spec.workspace ?? '(unset!)'}`)
    for (const c of cells) console.log(`  ${c.title}   model=${c.model} variety=${c.variety} max=${c.maxMode} w=${c.weirdness}`)
    process.exit(0)
  }
  if (cmd === 'explore' && !rest.includes('--yes')) {
    // The dry run. Returns before connect(): no browser, no Create, nothing spent.
    console.log(`explore round ${round}: ${cells.length} Creates → ${cells.length * 2} takes, into workspace ${spec.workspace ?? '(unset!)'}`)
    for (const c of cells)
      console.log(`  ${c.title}   model=${c.model} variety=${c.variety} max=${c.maxMode} w=${c.weirdness} style=${c.styleInfluence}`)
    console.log(`cost: ${cells.length * 10} credits (${cells.length} Creates) — nothing spent. Re-run with --yes to generate.`)
    process.exit(0)
  }
  const { browser, page } = await connect()

  try {
  if (cmd === 'load') {
    const { verify: v, problems } = await load(page, { ...spec, ...cells[0], weirdness: [cells[0].weirdness], title: spec.title }, cells[0].weirdness)
    console.log(JSON.stringify(v, null, 2))
    if (problems.length) {
      console.log('🔴 PROBLEMS — DO NOT GENERATE:', problems.join(' · '))
      process.exitCode = 1
    } else console.log('✅ loaded — nothing generated; run `pair` / `grid` or click Create')
  } else {
    // The form survives its own generation, so every cell after the first is a slider round:
    // re-assert the cell's controls (idempotent), retitle, re-verify, Create. No prompt box moves.
    const credits = async () =>
      Number(String(((await verify(page)) as Record<string, unknown>).credits ?? '').replace(/[^0-9]/g, '')) || null
    for (const [i, cell] of cells.entries()) {
      const cellSpec = { ...spec, ...cell, weirdness: [cell.weirdness] }
      if (i === 0) {
        const { problems } = await load(page, cellSpec, cell.weirdness)
        if (problems.length) {
          console.log('🔴 ABORTING before spending credits:', problems.join(' · '))
          break
        }
      } else {
        console.log(await setModel(page, cell.model))
        console.log(await setV6Controls(page, cellSpec))
        console.log(await setSlider(page, 'Style Influence', cell.styleInfluence))
        console.log(await setSlider(page, 'Weirdness', cell.weirdness))
        console.log('title:', await setTitle(page, cell.title))
        const v = (await verify(page)) as Record<string, unknown>
        const p = await checkV6(page, cellSpec, v)
        if (p.length) {
          console.log(`🔴 ABORTING at ${cell.title} before spending credits:`, p.join(' · '))
          break
        }
      }
      const before = await credits()
      console.log(`▶ ${cell.title}:`, await create(page, cell.title))
      const after = await credits()
      // v6 credit cost is unknown — every Create logs it until it is.
      console.log(`   credits ${before} → ${after}${before && after ? ` (cost ${before - after})` : ''}`)
    }
    console.log(JSON.stringify(await listTakes(page, takeFilter), null, 2))
  }
  // (Until 2026-09-10 this released the My Taste freedom token. My Taste is retired, so there is
  // no account-wide box to hand back — each song is its own unit.)
  } finally {
    await browser.close()
  }
} else if (IS_CLI) {
  console.log(`badcode suno — drive suno.com/create over CDP. See docs/suno-gpt/automation.md

  status                          read the create form back
  taste [block.txt]               (retired from the flow) read My Taste; with a file, back up + write
  extract <sheet.md> "<section>"  pull style/exclude/lyrics out of a sheet (a taste fence is ignored)
  controls <spec.json>            set + read back ONLY the v6 controls (no prompt boxes)

Personalize is ALWAYS OFF and My Taste is not used (Kai, 2026-09-10).
  load  <spec.json>               fill everything, generate NOTHING
  pair  <spec.json>               load, then Create at each weirdness (default 30 and 60)
  grid-plan <spec.json>           print the grid's cells and titles — spends nothing
  grid  <spec.json>               load once, then Create every cell of spec.grid
                                  (model × variety × maxMode × weirdness)
  explore <spec.json> --round <N> [--yes]
                                  the listening loop's spread: v6 w30 style 75 + v6-wild w60
                                  style 60, Variety off, Max Mode off. Without --yes: print the
                                  two cells and the cost, spend nothing. --round is required.
  takes [titleFilter]             list clip rows with durations

Every spec needs \`model\` ('v6' | 'v6-wild'). Titles: <title>-<model>[-var-<step>][-max]-w<n>;
explore: <title>-r<N>-v6-w30 and <title>-r<N>-wild-w60 (title ≤ 30 chars).
v6 credit cost per Create is unknown — pair/grid/explore log the balance around every Create.
\`load\`, \`controls\`, \`grid-plan\` and \`explore\` without --yes never spend credits.`)
}
