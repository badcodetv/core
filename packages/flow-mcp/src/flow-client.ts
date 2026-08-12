import { basename } from 'node:path'
import { chromium, type Browser, type Locator, type Page } from 'playwright'
import { collectNewCanvases, pickActiveCanvas, type CanvasImg } from './canvas'
import { toCanvasImgs, SCRAPE_IMGS, type RawImg } from './dom'
import { harvestToFile, contentTypeOf } from './harvest'
import { pickProject, SCRAPE_PROJECTS, type ProjectTile } from './project'
import { batchOutPath } from './batch'
import { candidateOutPath } from './candidates'
import { escapeRegExp, isBoxCleared, modelAlreadySelected, videoModelAlreadySelected } from './compose'
import { classifyCard, ANY_CARD_RE, type CardState } from './failure-card'
import { parseMediaOptions, SCRAPE_MEDIA_OPTIONS, type RawMediaOption, type MediaListItem } from './media-list'
import { toAnimateTiles, chooseAnimateTarget, type AnimateTile, type RawAnimateTile } from './animate-target'

const FLOW_URL = 'https://labs.google/fx/tools/flow'
const DEFAULT_ENDPOINT = `http://localhost:${process.env.FLOW_CDP_PORT ?? '9222'}`
const TURN_TIMEOUT_MS = 90_000
/**
 * Flow's compose bars default to "Nano Banana 2" and RESET to it on navigation, so the
 * model is asserted per generation, never once per session. Pro is materially sharper on
 * the same prompt (compared live 2026-08-11) and is what BadCode ships.
 */
const DEFAULT_MODEL = process.env.FLOW_MODEL ?? 'Nano Banana Pro'
export type VideoAspect = '16:9' | '9:16'
// flow-video.md:15 records 16:9 / 1x as the persisted defaults (though it warns to re-check
// them every project), so that's the aspect/count pair this client asserts by default.
const DEFAULT_VIDEO_ASPECT: VideoAspect = '16:9'
/**
 * Video's per-tier credit spread is far steeper than the image models' — Lite 10 / Fast 20 /
 * Quality 100 (flow-video.md:16) — so, unlike DEFAULT_MODEL for images, silently defaulting an
 * unrequested call to the top tier would risk a 5-10x spend the caller never asked for. Fast is
 * the deliberate middle: a real step up from Lite for the price of a fifth of Quality. A caller
 * who wants Quality's 100 credits asks for it explicitly via the `model` option.
 */
const DEFAULT_VIDEO_MODEL = process.env.FLOW_VIDEO_MODEL ?? 'Veo 3.1 Fast'
const VIDEO_TIMEOUT_MS = 8 * 60_000
// Image/grid polls are cheap in-page DOM scrapes, so poll fast (~1s of discovery latency).
const POLL_MS = 1_000
// The video poll additionally makes a content-type HTTP request per candidate media, so keep it
// a touch slower to stay polite to Flow's media endpoint over the minutes-long generation wait.
const VIDEO_POLL_MS = 3_000

export interface ImageResult { path: string; mediaId: string; width: number; height: number }
export interface EditResult { candidates: ImageResult[]; partial?: boolean }
export interface MediaResult { path: string; mediaId: string }
export interface BatchItem { index: number; prompt: string; path: string; mediaId: string; width: number; height: number }
export interface CharacterRef { name: string }
export interface FlowStatus { loggedIn: boolean; projectOpen: boolean; url: string }

export class FlowClient {
  private constructor(private browser: Browser, private page: Page) {}

  /** Attach to the already-logged-in Chrome launched by scripts/flow-chrome.sh. */
  static async connect(endpoint = DEFAULT_ENDPOINT): Promise<FlowClient> {
    const browser = await chromium.connectOverCDP(endpoint)
    const context = browser.contexts()[0]
    if (!context) throw new Error('NO_CONTEXT')
    const pages = context.pages()
    // Prefer an already-open project page; fall back to any Flow page.
    let page =
      pages.find((p) => /labs\.google\/fx\/tools\/flow\/project\//.test(p.url())) ??
      pages.find((p) => p.url().includes('labs.google/fx/tools/flow'))
    if (!page) {
      page = pages[0] ?? (await context.newPage())
      await page.goto(FLOW_URL, { waitUntil: 'domcontentloaded' })
    }
    return new FlowClient(browser, page)
  }

  async status(): Promise<FlowStatus> {
    const url = this.page.url()
    // Logged out → Flow bounces to an accounts/sign-in URL.
    const loggedIn = !/accounts\.google\.com|signin/i.test(url) && url.includes('labs.google')
    const projectOpen = /\/project\//.test(url)
    return { loggedIn, projectOpen, url }
  }

  private async ensureProject(): Promise<void> {
    if (/\/project\//.test(this.page.url())) return
    const newProject = this.page.getByRole('button', { name: /New project/i })
    await newProject.click({ force: true })
    await this.page.waitForURL(/\/project\//, { timeout: TURN_TIMEOUT_MS })
  }

  /**
   * Like ensureProject(), but also recovers from a prior turn leaving the page on a
   * sub-route (e.g. /characters, /character/<id>) that has neither the sidebar nor the
   * create bar — both createCharacter() and the generate/edit turns need the canvas root.
   * A failed createCharacter() attempt is the known way to strand the page there (mapped
   * live 2026-08-11), so re-navigate to the bare project URL rather than trust ensureProject()'s
   * looser "/project/" match.
   */
  private async ensureProjectRoot(): Promise<void> {
    await this.ensureProject()
    if (/\/project\/[0-9a-f-]+\/?$/.test(this.page.url())) return
    const m = this.page.url().match(/\/project\/([0-9a-f-]+)/)
    if (!m) throw new Error('NOT_IN_PROJECT')
    await this.page.goto(`${FLOW_URL}/project/${m[1]}`, { waitUntil: 'domcontentloaded' })
    await this.promptBox().waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
  }

  async openProject(name: string): Promise<void> {
    // Always start from the projects list so the name match is honoured even if a
    // different project is already open.
    if (/\/project\//.test(this.page.url()) || !this.page.url().includes('labs.google/fx/tools/flow')) {
      await this.page.goto(FLOW_URL, { waitUntil: 'domcontentloaded' })
    }
    // The project grid hydrates AFTER domcontentloaded, so poll the scrape until the
    // named project appears rather than reading an empty list once.
    const deadline = Date.now() + TURN_TIMEOUT_MS
    let href: string | null = null
    while (Date.now() < deadline) {
      const tiles = (await this.page.evaluate(`(${SCRAPE_PROJECTS})()`)) as ProjectTile[]
      href = pickProject(tiles, name)
      if (href) break
      await this.page.waitForTimeout(POLL_MS)
    }
    if (!href) throw new Error('PROJECT_NOT_FOUND')
    // SPA-navigate by clicking the project tile. A second hard goto (list -> project)
    // races the app's hydration and tips it into its client-side error boundary.
    await this.page.locator(`a[href="${href}"]`).first().click({ force: true })
    await this.page.waitForURL(/\/project\//, { timeout: TURN_TIMEOUT_MS })
    // The create bar hydrates after navigation; wait for the (enabled) prompt textbox
    // before returning so callers never interact with a half-rendered editor.
    await this.page
      .locator('div[role="textbox"][contenteditable="true"]')
      .first()
      .waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
  }

  // --- Click hardening (mapped live 2026-07-14, flow-selectors.md "Click reliability on WSLg") ---
  // Playwright's actionability "stable" check stalls on this UI (persistent animation) and
  // trusted CDP pointer input can silently miss, so each control type gets the recipe that
  // actually fires its handler. A bare click with default actionability is banned in this file.

  /**
   * Plain React buttons (submit, Upload media, Add to Prompt): in-page native el.click().
   * Coordinate-based clicks (even force:true) are untrustworthy on this rig — the WSLg
   * window's input pipeline scales coordinates, so pointer clicks can land on the wrong
   * element entirely (observed live 2026-07-14: a force-click on "Add to Prompt" hit
   * "Upload media" and opened a second file chooser).
   */
  private async forceClick(locator: Locator): Promise<void> {
    await locator.evaluate((el) => (el as HTMLElement).click())
  }

  /** Radix menu/dialog triggers (crop_ config, add_2 picker): synthetic pointer sequence. */
  private async pointerClick(locator: Locator): Promise<void> {
    await locator.evaluate((el) => {
      const opts: PointerEventInit = { bubbles: true, cancelable: true, pointerId: 1, pointerType: 'mouse', isPrimary: true, button: 0, buttons: 1 }
      el.dispatchEvent(new PointerEvent('pointerdown', opts))
      el.dispatchEvent(new PointerEvent('pointerup', { ...opts, buttons: 0 }))
      el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, button: 0 }))
    })
  }

  /** Radix tabs (Image / aspect / count / picker tabs): focus + mouse sequence selects. */
  private async tabClick(locator: Locator): Promise<void> {
    await locator.evaluate((el) => {
      ;(el as HTMLElement).focus()
      for (const type of ['mousedown', 'mouseup', 'click'] as const) {
        el.dispatchEvent(new MouseEvent(type, { bubbles: true, cancelable: true, button: 0 }))
      }
    })
  }

  /**
   * Reveal a hover-only overlay (a media tile's `more_vert` action button, which only mounts
   * on hover) via synthetic pointer/mouse events, NOT Playwright's coordinate-based `.hover()`.
   * flow-selectors.md:236-242 documents coordinate input as untrustworthy on this rig — the
   * WSLg window's input pipeline scales coordinates, so a trusted pointer move can land on the
   * wrong element (or the right element at the wrong point) even where a click with the same
   * mechanism would at least fail loudly. A hover has no "did it land" signal of its own, so
   * getting the coordinates wrong here fails silently instead — worse than a missed click, not
   * better. `pointerover`/`mouseover` bubble, so dispatching them at the target element reaches
   * React's root-level listeners the same way the app's own onMouseEnter handling would.
   */
  private async hoverElement(locator: Locator): Promise<void> {
    await locator.evaluate((el) => {
      const opts: PointerEventInit = { bubbles: true, cancelable: true, pointerId: 1, pointerType: 'mouse', isPrimary: true }
      el.dispatchEvent(new PointerEvent('pointerover', opts))
      el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true, cancelable: true }))
      el.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, cancelable: true }))
    })
  }

  /**
   * Upload local file(s) by setting Flow's hidden <input type="file"> directly — never
   * through the OS file chooser.
   *
   * `waitForEvent('filechooser')` + `setFiles` hangs whenever a SECOND Playwright client
   * (typically the Playwright MCP) is attached to the same Chrome with chooser interception
   * armed: the dialog opens, nobody answers it, and the upload never lands. Mapped
   * 2026-07-14 and hit again live 2026-08-12, where it surfaced as a `uploadImage` 400 plus
   * a stranded modal during a character cast. Setting the input skips the dialog entirely.
   *
   * `reveal` is invoked ONLY if no file input is on the page yet — some surfaces mount it
   * lazily behind a button or menu. Not calling it when the input already exists is the
   * point: clicking "Upload" is what would pop the chooser we are avoiding.
   */
  private async uploadFiles(paths: string[], reveal?: () => Promise<void>): Promise<void> {
    const imageInput = this.page.locator('input[type="file"][accept*="image"]').first()
    const anyInput = this.page.locator('input[type="file"]').first()
    const present = async (): Promise<boolean> =>
      (await imageInput.count()) > 0 || (await anyInput.count()) > 0
    if (reveal && !(await present())) await reveal()
    const input = (await imageInput.count()) ? imageInput : anyInput
    await input.waitFor({ state: 'attached', timeout: TURN_TIMEOUT_MS })
    await input.setInputFiles(paths)
  }

  private promptBox(): Locator {
    // Confirmed live 2026-06-30: the prompt box is a contenteditable div with role="textbox"
    // and NO own placeholder text. A sibling <textarea> also exposes the textbox role.
    return this.page.locator('div[role="textbox"][contenteditable="true"]').first()
  }

  /**
   * Select the generation model in whichever compose bar is on screen. Two layouts, both
   * mapped live 2026-08-11:
   *   • project canvas — one config trigger concatenating model+aspect+count
   *     ("🍌 Nano Banana Pro crop_16_9 x2"); the model submenu is nested INSIDE its menu.
   *   • character editor — a bare "🍌 <model> arrow_drop_down" trigger, no crop_ wrapper.
   * No-ops when the surface has no model picker.
   */
  private async ensureModel(model = DEFAULT_MODEL): Promise<void> {
    const bare = this.page.getByRole('button', { name: /Nano Banana.*arrow_drop_down/i }).first()
    const crop = this.page.getByRole('button', { name: /crop_/ }).first()
    let trigger: Locator
    if (await bare.count()) {
      if (modelAlreadySelected(await bare.textContent(), model)) return
      trigger = bare
    } else if (await crop.count()) {
      if (modelAlreadySelected(await crop.textContent(), model)) return
      await this.pointerClick(crop)
      trigger = this.page.getByRole('button', { name: /Nano Banana.*arrow_drop_down/i }).first()
      await trigger.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    } else {
      return
    }
    await this.pointerClick(trigger)
    const option = this.page.getByRole('button', { name: `🍌 ${model}`, exact: true }).first()
    await option.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.forceClick(option)
    // Escape closes the (possibly nested) menu; the selection sticks.
    await this.page.keyboard.press('Escape')
  }

  /** The character editor's name field — also the reliable "which character is open" probe. */
  private characterNameField(): Locator {
    return this.page.getByRole('textbox', { name: 'Character Name' })
  }

  /**
   * Open a Character's editor page by name. Character cards on the project root carry the
   * character's name as their <img alt>, which is what distinguishes them from generated
   * media tiles (mapped live 2026-08-11).
   */
  private async openCharacterPage(name: string): Promise<void> {
    if (/\/character\/[0-9a-f-]+/.test(this.page.url())) {
      const open = await this.characterNameField().inputValue().catch(() => '')
      if (open === name) return
    }
    await this.ensureProjectRoot()
    const link = this.page.locator(`a[href*="/character/"]:has(img[alt="${name}"])`).first()
    try {
      await link.waitFor({ state: 'visible', timeout: 15_000 })
    } catch {
      throw new Error('CHARACTER_NOT_FOUND')
    }
    await this.forceClick(link)
    await this.page.waitForURL(/\/character\/[0-9a-f-]+/, { timeout: TURN_TIMEOUT_MS })
    await this.characterNameField().waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
  }

  /** Leave the character editor (Done persists the edits and returns to the project root). */
  private async finishCharacter(): Promise<void> {
    const done = this.page.getByRole('button', { name: /^Done$/ }).first()
    if (await done.count()) await this.forceClick(done)
    await this.page
      .waitForURL((u) => /\/project\/[0-9a-f-]+$/.test(u.toString()), { timeout: TURN_TIMEOUT_MS })
      .catch(() => {})
  }

  /**
   * Generate on a character-editor compose bar and harvest the resulting view. The new
   * media is the largest fresh image on the page (the main preview), the same rule the
   * canvas turns use.
   */
  private async submitCharacterTurn(
    text: string,
    model: string | undefined,
    outPath: string | undefined,
    settled?: Locator,
  ): Promise<MediaResult> {
    const box = this.promptBox()
    await box.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.ensureModel(model)
    await box.fill(text)
    const before = await this.snapshotMediaNames()
    await this.clickSubmit()
    if (settled) await settled.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    const { name: mediaId } = await this.waitForNewCanvas(before, TURN_TIMEOUT_MS)
    if (outPath) await harvestToFile(this.page.request, mediaId, outPath)
    return { path: outPath ?? '', mediaId }
  }

  private async clickSubmit(): Promise<void> {
    // Accessible name renders as "arrow_forwardCreate" (no space). The button enables
    // asynchronously after the prompt fills — a click while it is still disabled is silently
    // swallowed (observed live 2026-07-14), so wait for enabled, click, and VERIFY the box
    // cleared (Flow empties the prompt on a successful submit); retry with Enter if not.
    const submit = this.page.getByRole('button', { name: /arrow_forward\s*Create/i }).first()
    const box = this.promptBox()
    const deadline = Date.now() + TURN_TIMEOUT_MS
    while (Date.now() < deadline) {
      if (await submit.isEnabled().catch(() => false)) break
      await this.page.waitForTimeout(250)
    }
    const boxCleared = async (): Promise<boolean> => isBoxCleared(await box.textContent())
    for (let attempt = 0; attempt < 3; attempt++) {
      if (attempt === 0) await this.forceClick(submit)
      else {
        await box.evaluate((el) => (el as HTMLElement).focus())
        await this.page.keyboard.press('Enter')
      }
      const settle = Date.now() + 5_000
      while (Date.now() < settle) {
        if (await boxCleared()) return
        await this.page.waitForTimeout(300)
      }
      // box still holds the prompt — submission didn't fire; try the next mechanism
    }
    throw new Error('SUBMIT_FAILED')
  }

  private async submitPrompt(prompt: string): Promise<void> {
    // Media-reference chips live OUTSIDE the contenteditable and survive fill(); only inline
    // character chips forbid it (submitWithCharacter appends instead).
    await this.promptBox().fill(prompt)
    await this.clickSubmit()
  }

  /**
   * Force the create bar into image mode at the requested output count (1–4).
   * Idempotent — when the config trigger's label already shows the target state
   * the menu is not even opened, which keeps repeat calls in an edit loop cheap.
   */
  private async ensureImageMode(count = 1, model = DEFAULT_MODEL): Promise<void> {
    // Wait for the create bar to hydrate (it renders after navigation).
    await this.promptBox().waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    // The bar toggles between "Agent" (conversational) and direct generation; the image config
    // (the "crop_…" button) only exists in generation mode. If it isn't showing we're in Agent
    // mode — click the Agent toggle to leave it. (Gating on crop_'s presence is more reliable
    // than reading the toggle's aria-pressed, which lags after navigation.)
    const crop = this.page.getByRole('button', { name: /crop_/ }).first()
    if (!(await crop.count())) {
      const agent = this.page.getByRole('button', { name: 'Agent', exact: true })
      if (await agent.count()) await this.forceClick(agent)
    }
    await crop.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    // Assert the model before reading the label below — ensureModel rewrites it.
    await this.ensureModel(model)
    // Count tabs are named `1x` for one output and `x2`/`x3`/`x4` beyond (mapped live 2026-07-14).
    const countTab = count <= 1 ? '1x' : `x${count}`
    // Short-circuit: the trigger label concatenates model+aspect+count ("🍌 Nano Banana 2crop_16_91x").
    const label = ((await crop.textContent()) ?? '').trim()
    if (/Nano Banana/i.test(label) && label.endsWith(countTab)) return
    // Open the config menu — a Radix trigger; needs the synthetic pointer sequence.
    await this.pointerClick(crop)
    const imageTab = this.page.getByRole('tab', { name: /image\s*Image/i })
    await imageTab.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.tabClick(imageTab)
    const countLocator = this.page.getByRole('tab', { name: countTab, exact: true })
    if (await countLocator.count()) await this.tabClick(countLocator)
    // Escape closes the menu; the selection sticks (verified live 2026-07-14).
    await this.page.keyboard.press('Escape')
  }

  /**
   * Read Flow's status/warning card (if one is showing) and classify it via failure-card.ts.
   * Polled INSIDE every generation wait loop below — the whole point is aborting a policy
   * block in seconds rather than running out the 90s (or 8-minute video) clock, so this must
   * be a cheap, single-query probe cheap enough to call every tick, not a post-timeout check.
   *
   * Reads ALL matching messages and classifies them together, rather than the first hit.
   * classifyCard's precedence resolves ambiguity WITHIN one string, so taking `.first()` would
   * discard the other matches before precedence could ever apply — and Flow's transcript
   * accumulates rather than replaces (flow-video.md:61-62: the queue message survives even
   * after the clip finishes). A stale "waiting in the queue" sitting above a real block or
   * error would then mask it, which is exactly the retry-forever failure this probe exists to
   * prevent.
   */
  private async detectFailureCard(): Promise<CardState> {
    const cards = this.page.getByText(ANY_CARD_RE)
    if (!(await cards.count())) return null
    const texts = await cards.allTextContents().catch(() => [] as string[])
    return classifyCard(texts.join('\n'))
  }

  /** Snapshot the media UUIDs currently on the canvas, so a later turn can detect new ones. */
  private async snapshotMediaNames(): Promise<Set<string>> {
    const raw = (await this.page.evaluate(`(${SCRAPE_IMGS})()`)) as RawImg[]
    return new Set(toCanvasImgs(raw).map((i) => i.name))
  }

  /**
   * Poll until a media img appears whose UUID was NOT present in `before`, then return the
   * largest such image. Each Flow turn yields a fresh UUID, so comparing against the pre-submit
   * snapshot is what distinguishes a new generation from the previous (still on-canvas) image —
   * waiting for "any image" would harvest the stale previous frame on refine/batch turns.
   *
   * No candidate can ever land after a policy block, so `detectFailureCard()` is polled on
   * every tick and a `blocked` verdict throws immediately — the entire point is not waiting
   * out the full timeout on a prompt that can never pass (docs/flow/failure-modes.md §A1).
   * `queued`/`error` are not actionable here (no credit gate to re-approve on the image path);
   * they fall through to the same poll-and-retry as an unrecognised card.
   */
  private async waitForNewCanvas(
    before: Set<string>,
    timeoutMs: number,
  ): Promise<{ name: string; width: number; height: number }> {
    const deadline = Date.now() + timeoutMs
    while (Date.now() < deadline) {
      if ((await this.detectFailureCard()) === 'blocked') throw new Error('POLICY_BLOCKED')
      const raw = (await this.page.evaluate(`(${SCRAPE_IMGS})()`)) as RawImg[]
      const imgs = toCanvasImgs(raw).filter((i) => !before.has(i.name))
      const name = pickActiveCanvas(imgs)
      if (name) {
        const hit = imgs.find((i) => i.name === name)!
        return { name, width: Math.round(hit.width), height: Math.round(hit.height) }
      }
      await this.page.waitForTimeout(POLL_MS)
    }
    throw new Error('TIMEOUT')
  }

  /**
   * Poll until `expected` fresh media UUIDs appear. Multi-output turns land their
   * candidates staggered (observed skew ≈ 9–15 s), so after the first arrival keep
   * polling for a grace window rather than the full turn timeout. Returns what
   * arrived (≥1) — the caller decides whether fewer than expected is `partial`.
   *
   * Fast-abort on a `blocked` card, BUT only while `found` is still empty. A multi-output
   * turn can be blocked on some candidates and not others (or a block card can appear stale
   * from an unrelated earlier turn), and once we are inside the grace window we already have
   * real, harvestable candidates — throwing there would discard output the caller already
   * paid for. So a block only aborts the "nothing has landed yet" phase; past that, this
   * behaves exactly as before and lets the grace window run its course.
   */
  private async waitForNewCanvases(
    before: Set<string>,
    expected: number,
    timeoutMs: number,
    graceMs = 30_000,
  ): Promise<CanvasImg[]> {
    const deadline = Date.now() + timeoutMs
    let graceDeadline = Number.POSITIVE_INFINITY
    const found = new Map<string, CanvasImg>()
    while (Date.now() < Math.min(deadline, graceDeadline)) {
      if (found.size === 0 && (await this.detectFailureCard()) === 'blocked') {
        throw new Error('POLICY_BLOCKED')
      }
      const raw = (await this.page.evaluate(`(${SCRAPE_IMGS})()`)) as RawImg[]
      for (const im of collectNewCanvases(toCanvasImgs(raw), before)) {
        const prev = found.get(im.name)
        if (!prev || im.width * im.height > prev.width * prev.height) found.set(im.name, im)
      }
      if (found.size >= expected) break
      if (found.size > 0 && graceDeadline === Number.POSITIVE_INFINITY) graceDeadline = Date.now() + graceMs
      await this.page.waitForTimeout(POLL_MS)
    }
    if (found.size === 0) throw new Error('TIMEOUT')
    return [...found.values()].map((im) => ({ name: im.name, width: Math.round(im.width), height: Math.round(im.height) }))
  }

  /** Harvest each canvas to its candidate path (suffixed -a/-b… when numOutputs > 1). */
  private async harvestCandidates(canvases: CanvasImg[], outPath: string, numOutputs: number): Promise<ImageResult[]> {
    const out: ImageResult[] = []
    for (let i = 0; i < canvases.length; i++) {
      const c = canvases[i]!
      const path = candidateOutPath(outPath, i, numOutputs)
      await harvestToFile(this.page.request, c.name, path)
      out.push({ path, mediaId: c.name, width: c.width, height: c.height })
    }
    return out
  }

  async generateImage(
    prompt: string,
    outPath: string,
    opts?: { character?: string; numOutputs?: number },
  ): Promise<ImageResult & { candidates?: ImageResult[]; partial?: boolean }> {
    const numOutputs = opts?.numOutputs ?? 1
    await this.ensureProjectRoot()
    await this.ensureImageMode(numOutputs)
    const before = await this.snapshotMediaNames()
    if (opts?.character) await this.submitWithCharacter(opts.character, prompt)
    else await this.submitPrompt(prompt)
    const canvases = await this.waitForNewCanvases(before, numOutputs, TURN_TIMEOUT_MS)
    const candidates = await this.harvestCandidates(canvases, outPath, numOutputs)
    if (numOutputs === 1) return candidates[0]!
    return { ...candidates[0]!, candidates, ...(canvases.length < numOutputs ? { partial: true } : {}) }
  }

  /**
   * Edit an existing image: attach the reference file(s) as prompt ingredients (the
   * create-bar "Add" asset picker, mapped live 2026-07-14), apply the delta prompt,
   * and harvest all fresh candidates. References should be the ORIGINAL/golden image,
   * not a previous edit output — chained edits accumulate artifacts.
   */
  async editImage(
    prompt: string,
    referenceImages: string[],
    outPath: string,
    opts?: { numOutputs?: number; character?: string },
  ): Promise<EditResult> {
    const numOutputs = opts?.numOutputs ?? 2
    await this.ensureProjectRoot()
    await this.ensureImageMode(numOutputs)
    await this.attachReferences(referenceImages)
    if (opts?.character) await this.addCharacterToPrompt(opts.character)
    // Snapshot AFTER attaching: the uploads themselves land in the media grid as new UUIDs.
    const before = await this.snapshotMediaNames()
    const box = this.promptBox()
    if (opts?.character) {
      // An inline character chip is now in the box — append, never fill().
      await box.evaluate((el) => (el as HTMLElement).focus())
      await this.page.keyboard.press('End')
      await this.page.keyboard.type(` ${prompt}`)
    } else {
      await box.fill(prompt) // media chips live outside the box and survive fill()
    }
    await this.clickSubmit()
    const canvases = await this.waitForNewCanvases(before, numOutputs, TURN_TIMEOUT_MS)
    const candidates = await this.harvestCandidates(canvases, outPath, numOutputs)
    return { candidates, ...(canvases.length < numOutputs ? { partial: true } : {}) }
  }

  /**
   * Open the create-bar asset picker (the `add_2 Create` trigger; `@` in the box opens the
   * same dialog). Mapped live 2026-07-14: a dialog with a project dropdown, tabs
   * All/Images/Videos/Voices/Characters/Uploads, an "upload Upload media" button and a
   * searchable asset grid. Resolves once the dialog's Upload button is visible.
   */
  private async openAssetPicker(): Promise<Locator> {
    const trigger = this.page.getByRole('button', { name: /add_2\s*Create/i }).first()
    await trigger.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    const dialog = this.page.getByRole('dialog').last()
    const uploadBtn = dialog.getByRole('button', { name: /upload\s*Upload media/i })
    // Native click opens this trigger (proven live on a fresh CDP connection); the synthetic
    // pointer sequence only works once the dialog has mounted before. Try native, then fall back.
    await this.forceClick(trigger)
    try {
      await uploadBtn.waitFor({ state: 'visible', timeout: 5_000 })
    } catch {
      await this.pointerClick(trigger)
      await uploadBtn.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    }
    return dialog
  }

  /** Close the asset picker if it is still open (Add to Prompt usually closes it). */
  private async closeAssetPicker(): Promise<void> {
    const dialog = this.page.getByRole('dialog').last()
    try {
      await dialog.waitFor({ state: 'hidden', timeout: 2_000 })
    } catch {
      await this.page.keyboard.press('Escape')
    }
  }

  /**
   * List media in the open project's asset picker: title, kind, and media id where
   * derivable. This is the discovery step `flow_create_character_from_media` has no
   * substitute for — its `mediaTitle` parameter must match a gallery item's accessible
   * name exactly-ish, and until now the only way to read that name was a DOM snapshot.
   * Pass `query` to type into the picker's own search box first (narrows the scrape to
   * matching tiles); pass `limit` to cap the returned list — the scrape itself always reads
   * whatever the picker currently renders.
   */
  async listMedia(opts?: { query?: string; limit?: number }): Promise<MediaListItem[]> {
    await this.ensureProjectRoot()
    const dialog = await this.openAssetPicker()
    try {
      if (opts?.query) {
        const search = dialog.getByRole('textbox', { name: 'Search assets' })
        await search.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
        await search.fill(opts.query)
        // The grid re-filters asynchronously; give it a beat before scraping.
        await this.page.waitForTimeout(POLL_MS)
      }
      const raw = (await this.page.evaluate(`(${SCRAPE_MEDIA_OPTIONS})()`)) as RawMediaOption[]
      const items = parseMediaOptions(raw)
      return opts?.limit ? items.slice(0, opts.limit) : items
    } finally {
      // Always close, including on a thrown error — leaving the picker open strands the
      // next call the same way a failed createCharacter() strands the page on /characters.
      await this.closeAssetPicker()
    }
  }

  /**
   * Attach local image file(s) to the prompt as ingredient references. Each upload lands
   * selected in the picker with an "Add to Prompt" button; the resulting media chip sits
   * OUTSIDE the contenteditable (probe it via the img alt — the accessible name comes from
   * the alt text "A piece of media generated or uploaded by you…").
   */
  private async attachReferences(refPaths: string[]): Promise<void> {
    const chip = this.page.locator('button:has(img[alt*="piece of media"])')
    const base = await chip.count() // pre-existing chips (e.g. left over on the bar) don't count
    for (let i = 0; i < refPaths.length; i++) {
      const ref = refPaths[i]!
      await this.openAssetPicker()
      // The picker is already open, so its file input is mounted — no reveal needed.
      await this.uploadFiles([ref])
      // The uploaded asset lands in the picker (Recent-first) named after the file; select it
      // if it isn't auto-selected, then attach. Match page-globally and case-insensitively:
      // the picker has two layout variants ("Add to Prompt" dialog / "Add to prompt" compact
      // popover) and stale dialog containers can outlive their content (observed 2026-07-14).
      const tile = this.page.locator(`[role="dialog"] img[alt="${basename(ref)}"]`).first()
      const addToPrompt = this.page.getByRole('button', { name: /add to prompt/i }).first()
      await tile.or(addToPrompt).first().waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
      if (!(await addToPrompt.isVisible().catch(() => false))) await this.forceClick(tile)
      await addToPrompt.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
      await this.forceClick(addToPrompt)
      try {
        await chip.nth(base + i).waitFor({ state: "visible", timeout: 10_000 })
      } catch {
        // One retry — the first click occasionally lands on a picker mid-render.
        await this.forceClick(addToPrompt)
        await chip.nth(base + i).waitFor({ state: "visible", timeout: TURN_TIMEOUT_MS })
      }
      await this.closeAssetPicker()
    }
  }

  /**
   * Cast a project Character into the next generation via the unified asset picker
   * (the 2026-06-30 `role="option"` flow is gone — UI update mapped 2026-07-14):
   * picker → Characters tab → select the named tile → Add to Prompt. The character chip
   * is INLINE in the contenteditable, so callers must APPEND prompt text afterwards.
   */
  private async addCharacterToPrompt(name: string): Promise<void> {
    const dialog = await this.openAssetPicker()
    const charactersTab = dialog.getByRole('tab', { name: /Characters/i })
    await charactersTab.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.tabClick(charactersTab)
    // Select the tile carrying the character's name, then attach it.
    const tile = dialog.getByText(name, { exact: true }).first()
    await tile.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.forceClick(tile)
    const addToPrompt = this.page.getByRole('button', { name: /add to prompt/i }).first()
    await addToPrompt.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.forceClick(addToPrompt)
    await this.closeAssetPicker()
  }

  /** Character cast + scene text + submit (append after the inline chip — fill() wipes it). */
  private async submitWithCharacter(name: string, prompt: string): Promise<void> {
    await this.addCharacterToPrompt(name)
    const box = this.promptBox()
    await box.evaluate((el) => (el as HTMLElement).focus())
    await this.page.keyboard.press('End')
    await this.page.keyboard.type(` ${prompt}`)
    await this.clickSubmit()
  }

  async generateBatch(prompts: string[], outDir: string): Promise<BatchItem[]> {
    await this.ensureProjectRoot()
    await this.ensureImageMode()
    const items: BatchItem[] = []
    for (let i = 0; i < prompts.length; i++) {
      const prompt = prompts[i]!
      const before = await this.snapshotMediaNames()
      await this.submitPrompt(prompt)
      const { name, width, height } = await this.waitForNewCanvas(before, TURN_TIMEOUT_MS)
      const path = batchOutPath(outDir, i)
      await harvestToFile(this.page.request, name, path)
      items.push({ index: i, prompt, path, mediaId: name, width, height })
    }
    return items
  }

  /** Follow-up correction in the SAME session, then harvest the new active canvas. */
  async refine(prompt: string, outPath: string): Promise<MediaResult> {
    const before = await this.snapshotMediaNames()
    await this.submitPrompt(prompt)
    const { name } = await this.waitForNewCanvas(before, TURN_TIMEOUT_MS)
    await harvestToFile(this.page.request, name, outPath)
    return { path: outPath, mediaId: name }
  }

  /**
   * Create a reusable, castable Flow Character from one or more reference images.
   * Re-mapped live 2026-08-11: the Characters sidebar button now navigates STRAIGHT to a
   * "New character" composer (upload / describe-from-scratch) — there is no intermediate
   * list view or "New Character" card to click through on a project with zero characters,
   * so that step is gone. Flow: Characters sidebar -> Upload (file chooser) -> fill
   * "Character Name" -> Done. Returns once the character editor is left.
   */
  async createCharacter(
    name: string,
    refImages: string[],
    opts?: { info?: string; body?: string; model?: string; bodyOutPath?: string },
  ): Promise<CharacterRef & { bodyMediaId?: string; bodyPath?: string }> {
    await this.ensureProjectRoot()
    await this.page.getByRole('button', { name: /accessibility_new\s*Characters/i }).click({ force: true })
    await this.page.waitForURL(/\/characters\b/, { timeout: TURN_TIMEOUT_MS })
    // Upload the reference(s) through the hidden input — see uploadFiles for why not the chooser.
    await this.uploadFiles(refImages, async () => {
      await this.forceClick(this.page.getByRole('button', { name: /upload\s*Upload/i }).first())
    })
    return this.finalizeCharacter(name, opts)
  }

  /**
   * Create a Character from a media item ALREADY IN the project's gallery, instead of a fresh
   * file upload. Needed because the raw upload endpoint 400s on some re-fetched/harvested images
   * (observed live 2026-08-12 casting a Character from a media id pulled back off Flow's own
   * network traffic; root cause unconfirmed) — Flow's own "Add from Project" picker sidesteps
   * that entirely since the media is already server-side. `mediaTitle` matches the option's
   * accessible name shown in the project gallery — Flow's auto-caption for the image (e.g.
   * "Man sitting with open book"), not the file path or media id.
   */
  async createCharacterFromMedia(
    name: string,
    mediaTitle: string,
    opts?: { info?: string; body?: string; model?: string; bodyOutPath?: string },
  ): Promise<CharacterRef & { bodyMediaId?: string; bodyPath?: string }> {
    await this.ensureProjectRoot()
    await this.page.getByRole('button', { name: /accessibility_new\s*Characters/i }).click({ force: true })
    await this.page.waitForURL(/\/characters\b/, { timeout: TURN_TIMEOUT_MS })
    const addFromProject = this.page.getByRole('button', { name: /add\s*Add from Project/i }).first()
    await addFromProject.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.forceClick(addFromProject)
    const dialog = this.page.getByRole('dialog').last()
    const option = dialog.getByRole('option', { name: new RegExp(escapeRegExp(mediaTitle), 'i') }).first()
    try {
      await option.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    } catch {
      throw new Error('MEDIA_NOT_FOUND')
    }
    await this.forceClick(option)
    const addToCharacter = dialog.getByRole('button', { name: /Add to Character/i }).first()
    await addToCharacter.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.forceClick(addToCharacter)
    return this.finalizeCharacter(name, opts)
  }

  /**
   * Shared tail of both character-creation paths: the editor opens with a "Character Name"
   * field defaulting to "Untitled Character" once a reference (uploaded or from-project) is
   * attached — name it, fill the optional info note, run the optional Create Body pass, done.
   */
  private async finalizeCharacter(
    name: string,
    opts?: { info?: string; body?: string; model?: string; bodyOutPath?: string },
  ): Promise<CharacterRef & { bodyMediaId?: string; bodyPath?: string }> {
    const nameInput = this.characterNameField()
    await nameInput.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await nameInput.fill(name)
    if (opts?.info) await this.characterInfoField().fill(opts.info)
    let body: MediaResult | undefined
    if (opts?.body) body = await this.runCreateBody(opts.body, opts.model, opts.bodyOutPath)
    await this.finishCharacter()
    return {
      name,
      ...(body ? { bodyMediaId: body.mediaId, ...(body.path ? { bodyPath: body.path } : {}) } : {}),
    }
  }

  /** The optional free-text field Flow's own scene agent reads when casting the character. */
  private characterInfoField(): Locator {
    return this.page.getByRole('textbox', { name: /Describe how your character/i })
  }

  /**
   * Run the character editor's "Create Body" pass: it opens a second compose bar seeded with
   * the portrait, takes a body+outfit description, and adds a full-figure "Body" view
   * alongside the portrait. Assumes the editor is already open. Mapped live 2026-08-11.
   */
  private async runCreateBody(
    description: string,
    model?: string,
    outPath?: string,
  ): Promise<MediaResult> {
    const createBody = this.page.getByRole('button', { name: /^Create Body$/ }).first()
    if (!(await createBody.count())) throw new Error('BODY_EXISTS')
    await this.forceClick(createBody)
    // Completion flips the tab's label from "Create Body" to "Body".
    const bodyTab = this.page.getByRole('button', { name: /^Body$/ }).first()
    return this.submitCharacterTurn(description, model, outPath, bodyTab)
  }

  /** Add the full-figure Body view to a character that only has a Portrait. */
  async createCharacterBody(
    name: string,
    description: string,
    opts?: { model?: string; outPath?: string },
  ): Promise<MediaResult> {
    await this.openCharacterPage(name)
    const res = await this.runCreateBody(description, opts?.model, opts?.outPath)
    await this.finishCharacter()
    return res
  }

  /** Set (or replace) the character's free-text personality/appearance note. */
  async setCharacterInfo(name: string, info: string): Promise<CharacterRef> {
    await this.openCharacterPage(name)
    const field = this.characterInfoField()
    await field.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await field.fill(info)
    await this.finishCharacter()
    return { name }
  }

  /**
   * Iterate on an EXISTING character in place: select the Portrait or Body view and apply a
   * delta prompt through the editor's "What do you want to change?" bar. This is the cheap
   * path for "same character, but <change>" — it keeps the identity Flow has already bound
   * instead of re-casting from a fresh reference image, and every round is recoverable from
   * the editor's own "Show history".
   */
  async editCharacter(
    name: string,
    prompt: string,
    opts?: { target?: 'portrait' | 'body'; model?: string; outPath?: string },
  ): Promise<MediaResult & { target: 'portrait' | 'body' }> {
    await this.openCharacterPage(name)
    const target = opts?.target ?? 'portrait'
    const tab = this.page
      .getByRole('button', { name: target === 'body' ? /^Body$/ : /^Portrait$/ })
      .first()
    if (!(await tab.count())) throw new Error(target === 'body' ? 'NO_BODY' : 'NO_PORTRAIT')
    await this.forceClick(tab)
    const res = await this.submitCharacterTurn(prompt, opts?.model, opts?.outPath)
    await this.finishCharacter()
    return { ...res, target }
  }

  /**
   * Assert Flow's Settings-panel "Video generation default" — model, aspect, output count —
   * mapped at flow-video.md:12-23 and :113-116. Unlike the image compose bar's `crop_` trigger,
   * these live behind a dedicated panel and there is no per-turn control on the create bar
   * itself, so a video call that skips this inherits whatever the PROJECT last had — and
   * ⚠️ that **resets to Omni Flash on a fresh project** (flow-video.md:20). Skipping this call
   * is exactly the bug this task exists to fix: a caller asking for Veo 3.1 Quality could
   * silently get an Omni Flash clip at the wrong aspect.
   *
   * Structured on ensureImageMode: opens the panel (cheap), then only clicks through a control
   * whose current state doesn't already match the target — so a loop of same-settings
   * generateVideo() calls stays cheap — and only hits Save if something actually changed.
   */
  private async ensureVideoSettings(opts?: { model?: string; aspect?: VideoAspect; count?: number }): Promise<void> {
    const model = opts?.model ?? DEFAULT_VIDEO_MODEL
    const aspect = opts?.aspect ?? DEFAULT_VIDEO_ASPECT
    const count = opts?.count ?? 1

    const settingsBtn = this.page.getByRole('button', { name: /^tune\s*Settings$/i }).first()
    await settingsBtn.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.pointerClick(settingsBtn)

    // The model dropdown trigger renders "<model name> arrow_drop_down" (flow-video.md:114).
    // ⚠️ GUESSED: the doc doesn't record a heading/container locator for the "Video generation
    // default" section, so this scopes by the model names themselves — Omni Flash / Veo 3.1 …
    // never collide with the image bar's "Nano Banana" labels — rather than by position. If the
    // Settings panel also shows an "Image generation default" model dropdown with its own
    // aspect/count tabs sharing the SAME tab names ("crop_16_9 16:9", "1x"…), `.first()` below
    // could land on the wrong section. Flag for Wave B live validation.
    const modelBtn = this.page
      .getByRole('button', { name: /arrow_drop_down/i })
      .filter({ hasText: /Omni Flash|Veo/i })
      .first()
    await modelBtn.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    let changed = false
    if (!videoModelAlreadySelected(await modelBtn.textContent(), model)) {
      await this.pointerClick(modelBtn)
      // ⚠️ GUESSED: flow-video.md maps the TRIGGER's accessible name but not the opened menu's
      // option shape. Mirrors ensureModel's assumption that options are buttons named for the
      // model (there rendered "🍌 <model>"; no emoji is recorded for video model names, so this
      // matches the bare model string). Unverified against the live DOM.
      const option = this.page.getByRole('button', { name: model, exact: true }).first()
      await option.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
      await this.forceClick(option)
      await this.page.keyboard.press('Escape') // closes the nested model menu; Settings panel stays open
      changed = true
    }

    const aspectTab = this.page
      .getByRole('tab', { name: aspect === '9:16' ? /crop_9_16\s*9:16/i : /crop_16_9\s*16:9/i })
      .first()
    if (await aspectTab.count()) {
      if ((await aspectTab.getAttribute('aria-selected')) !== 'true') {
        await this.tabClick(aspectTab)
        changed = true
      }
    }

    // Count tabs are named `1x` for one output and `x2`/`x3`/`x4` beyond, same convention as
    // ensureImageMode's image-count tabs.
    const countTab = this.page.getByRole('tab', { name: count <= 1 ? '1x' : `x${count}`, exact: true }).first()
    if (await countTab.count()) {
      if ((await countTab.getAttribute('aria-selected')) !== 'true') {
        await this.tabClick(countTab)
        changed = true
      }
    }

    if (changed) {
      const save = this.page.getByRole('button', { name: /^Save$/ }).first()
      await this.forceClick(save)
    } else {
      // Nothing to persist — close without touching Save (leaves the unrelated Confirm-gate
      // setting untouched too).
      await this.page.keyboard.press('Escape')
    }
  }

  /**
   * Animate a still into an image→video clip (Veo). Mapped live 2026-06-30 + flow-video.md:
   * Add Media → "Upload media" (file chooser) → the uploaded tile's more_vert → "Animate"
   * (attaches the source frame and switches the bar to Video mode) → motion prompt → submit →
   * approve the credit gate if shown → poll for the new video media and harvest the .mp4.
   */
  async generateVideo(
    imagePath: string,
    motion: string,
    outPath: string,
    opts?: { model?: string; aspect?: VideoAspect; count?: number },
  ): Promise<MediaResult> {
    await this.ensureProject()
    // 0. Assert model/aspect/count BEFORE touching media — these are project-level defaults
    //    that silently reset, so this must run every call, not just the first in a session.
    await this.ensureVideoSettings(opts)
    // 1. Snapshot the "Generated image" tiles BEFORE upload, so the tile the upload creates
    //    can be told apart from whatever else is already sitting in the project (same idea as
    //    the `before` snapshot below, applied one step earlier — see animate-target.ts).
    const beforeTiles = toAnimateTiles(await this.scrapeAnimateTiles())
    // 2. Upload the source frame through the hidden input (see uploadFiles). The reveal is
    //    two steps here: Add Media opens a menu, whose "Upload media" item mounts the input.
    await this.uploadFiles([imagePath], async () => {
      await this.forceClick(this.page.getByRole('button', { name: /add\s*Add Media/i }).first())
      const item = this.page.getByRole('menuitem', { name: /upload\s*Upload media/i })
      await item.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
      await this.forceClick(item)
    })
    // 3. Identify the just-uploaded tile and attach it as the animation source.
    const tileIndex = await this.waitForNewAnimateTile(beforeTiles, TURN_TIMEOUT_MS)
    await this.openAnimateMenu(tileIndex)
    // 4. Motion prompt + submit (capture the pre-submit media set to detect the new clip).
    const before = new Set(await this.scrapeMediaNames())
    await this.submitPrompt(motion)
    // 5. Approve the credit gate if Flow posts one (Veo Quality = 100 credits).
    await this.approveCreditGateIfPresent()
    // 6. Poll for the new video media and harvest.
    const name = await this.waitForVideoClip(before, VIDEO_TIMEOUT_MS)
    await harvestToFile(this.page.request, name, outPath)
    return { path: outPath, mediaId: name }
  }

  /** Media names from every current "Generated image" tile — see SCRAPE_ANIMATE_TILES. */
  private async scrapeAnimateTiles(): Promise<RawAnimateTile[]> {
    return (await this.page.evaluate(`(${FlowClient.SCRAPE_ANIMATE_TILES})()`)) as RawAnimateTile[]
  }

  /** In-page scraper for every "Generated image" tile's current src (evaluated as `(${...})()`). */
  private static readonly SCRAPE_ANIMATE_TILES = `() => [...document.querySelectorAll('img[alt="Generated image"]')].map(im => ({
    src: im.currentSrc || im.src || im.getAttribute('src') || '',
  }))`

  /**
   * Poll until the just-uploaded still's tile becomes identifiable, per
   * `chooseAnimateTarget`'s diff-then-sole-tile-fallback rule (animate-target.ts). The upload
   * takes a beat to render as a fresh tile with a resolved media id, so this polls rather than
   * scraping once.
   *
   * Throws ANIMATE_NOT_FOUND (mapped in toToolError) on timeout rather than EVER falling back
   * to "hover every tile and take the first that offers Animate" — that blind scan is exactly
   * the fragility this task replaces (flow-video.md's "open rough edge": it timed out on
   * re-runs once the project filled with test media, and worse, a media-rich project has no
   * guarantee the first Animate-capable tile it finds is the one we just uploaded). A clear,
   * fast failure beats a silent wrong-image animate.
   */
  private async waitForNewAnimateTile(before: AnimateTile[], timeoutMs: number): Promise<number> {
    const deadline = Date.now() + timeoutMs
    while (Date.now() < deadline) {
      const after = toAnimateTiles(await this.scrapeAnimateTiles())
      const idx = chooseAnimateTarget(before, after)
      if (idx !== null) return idx
      await this.page.waitForTimeout(POLL_MS)
    }
    throw new Error('ANIMATE_NOT_FOUND')
  }

  /**
   * Open the "Animate" action on ONE specific "Generated image" tile — `tileIndex` from
   * `waitForNewAnimateTile`, the just-uploaded still, never "whichever tile answers first".
   * The tile's more_vert only mounts on hover, so reveal it via the synthetic-event
   * `hoverElement` (not coordinate-based `.hover()` — see its doc comment), then the standard
   * hardened clicks: `more_vert` is a Radix menu trigger (`pointerClick`), "Animate" is the
   * menu item it opens (`forceClick`).
   */
  private async openAnimateMenu(tileIndex: number): Promise<void> {
    const tile = this.page.locator('img[alt="Generated image"]').nth(tileIndex)
    await tile.waitFor({ state: 'visible', timeout: TURN_TIMEOUT_MS })
    await this.hoverElement(tile)
    // Only the hovered tile's more_vert is revealed (we hover exactly one tile — never a
    // scan loop), so :near() unambiguously resolves to that tile's own control.
    const more = this.page
      .locator('button:has-text("more_vert"):near(img[alt="Generated image"])')
      .first()
    if (!(await more.count())) throw new Error('ANIMATE_NOT_FOUND')
    await this.pointerClick(more)
    const animate = this.page.getByRole('menuitem', { name: /motion_blur\s*Animate/i })
    try {
      await animate.waitFor({ state: 'visible', timeout: 5_000 })
    } catch {
      await this.page.keyboard.press('Escape')
      throw new Error('ANIMATE_NOT_FOUND')
    }
    await this.forceClick(animate)
  }

  /** Media UUIDs from <video>/<source>/<img> nodes carrying a non-thumbnail getMediaUrlRedirect src. */
  private static readonly SCRAPE_MEDIA_NAMES = `() => {
    const names = []
    for (const el of document.querySelectorAll('video, source, img')) {
      const s = el.currentSrc || el.src || el.getAttribute('src') || ''
      if (s.includes('getMediaUrlRedirect') && !s.includes('THUMBNAIL')) {
        try { const n = new URL(s, location.href).searchParams.get('name'); if (n) names.push(n) } catch (e) {}
      }
    }
    return names
  }`

  private async scrapeMediaNames(): Promise<string[]> {
    return (await this.page.evaluate(`(${FlowClient.SCRAPE_MEDIA_NAMES})()`)) as string[]
  }

  /** Click the credit-confirmation "Approve" if Flow posts one; no-op if there is no gate. */
  private async approveCreditGateIfPresent(timeoutMs = 20_000): Promise<void> {
    const approve = this.page.getByRole('button', { name: /^Approve$/ }).first()
    try {
      await approve.waitFor({ state: 'visible', timeout: timeoutMs })
      await this.forceClick(approve)
    } catch {
      // No gate (Confirm=Never / direct generation) — nothing to approve.
    }
  }

  /**
   * Poll for a media name not present pre-submit whose content-type is video/*; retry a
   * transient gate. Routes both known card states through `detectFailureCard()` /
   * `classifyCard()` (failure-card.ts) rather than its own inline `getByText` checks, so there
   * is one source of truth for what each card string means:
   *   - `blocked` aborts immediately (POLICY_BLOCKED) — a video generation this large a spend
   *     (Veo Quality = 100 credits) is exactly where burning the full 8-minute clock on an
   *     unpassable prompt is most expensive.
   *   - `error` ("Oops, something went wrong") re-approves the credit gate to retry, same
   *     behaviour this loop always had.
   *   - `queued` is deliberately NOT checked for here — it is benign (flow-video.md:41-49), and
   *     the misleading `warning Failed`-looking icon that can render alongside it must never be
   *     read as a reason to stop waiting.
   */
  private async waitForVideoClip(before: Set<string>, timeoutMs: number): Promise<string> {
    const deadline = Date.now() + timeoutMs
    while (Date.now() < deadline) {
      const card = await this.detectFailureCard()
      if (card === 'blocked') throw new Error('POLICY_BLOCKED')
      if (card === 'error') await this.approveCreditGateIfPresent(5_000)
      for (const n of await this.scrapeMediaNames()) {
        if (before.has(n)) continue
        const ct = await contentTypeOf(this.page.request, n)
        if (ct.startsWith('video/')) return n
      }
      await this.page.waitForTimeout(VIDEO_POLL_MS)
    }
    throw new Error('TIMEOUT')
  }

  /** Whether the cached CDP attachment (and its page) is still usable. */
  isAlive(): boolean {
    return this.browser.isConnected() && !this.page.isClosed()
  }

  async close(): Promise<void> {
    await this.browser.close()
  }
}
