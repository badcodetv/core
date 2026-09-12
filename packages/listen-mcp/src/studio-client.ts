/**
 * Drives AI Studio's chat page over CDP with fixed routines. Selectors come from `studio-dom.ts`,
 * whose evidence is `docs/listening/automation.md`.
 *
 * 🔴 Our own tab, never Jack's. The tab is claimed by a sessionStorage marker rather than an
 * index, because CDP's page order is not creation order and reshuffles (proven in
 * `scripts/suno/suno.mts`). Jack may be using AI Studio in the same window.
 *
 * 🔴 Three things must happen on EVERY describe, because the page resets them:
 *   1. a Temporary chat, so the conversation is not saved (the uploaded file still lands in Drive
 *      — ruled acceptable by Kai 2026-09-11, Trap 1);
 *   2. Search grounding OFF, because it is ON by default and would pad a description with web
 *      results about the song's title instead of what is heard (Trap 2);
 *   3. the model picked by its visible name, and the name the page actually showed reported back.
 */
import { chromium, type Browser, type Page } from 'playwright'
import { writeFile } from 'node:fs/promises'
import { join } from 'node:path'
import { tmpdir } from 'node:os'
import { DEFAULT_MODEL, HOST, NEW_CHAT_URL, PAGE_SIGNS, SEL, SIGNED_OUT_PATH, TAB_MARK, TEXT } from './studio-dom'

export type SignedIn = 'yes' | 'no' | 'unknown'
export type PageState = 'ok' | 'signed-out' | 'rate-limited' | 'error'

export interface Studio {
  signedInState(): Promise<SignedIn>
  ensureSignedIn(): Promise<void>
  newChat(): Promise<void>
  selectModel(name: string): Promise<string>
  disableSearchGrounding(): Promise<void>
  attachAudio(mp3Path: string): Promise<void>
  submit(prompt: string): Promise<void>
  waitForReply(timeoutMs: number): Promise<string>
}

/** Visible text of a locator, collapsed — used for menu items and dialog buttons. */
const norm = (s: string) => (s || '').replace(/\s+/g, ' ').trim()

/**
 * Classify what the page is showing. Applied to the URL and the last model turn's text.
 * Ordered: signed-out beats everything, then rate-limit, then error.
 */
export function classifyPage(input: { url: string; lastModelText: string }): PageState {
  if (input.url.includes(SIGNED_OUT_PATH)) return 'signed-out'
  for (const sign of PAGE_SIGNS) if (sign.re.test(input.lastModelText)) return sign.state
  return 'ok'
}

export class StudioClient implements Studio {
  private constructor(
    private readonly browser: Browser,
    private readonly page: Page,
  ) {}

  static async connect(endpoint: string): Promise<StudioClient> {
    const browser = await chromium.connectOverCDP(endpoint)
    const ctx = browser.contexts()[0]
    if (!ctx) throw new Error('NO_CONTEXT: no browser context — is the listening channel up?')

    // Our marked tab, if it is still there.
    for (const p of ctx.pages()) {
      try {
        if ((await p.evaluate(`sessionStorage.getItem(${JSON.stringify(TAB_MARK)})`)) === '1') {
          return new StudioClient(browser, p)
        }
      } catch {
        /* cross-origin, closed, or mid-navigation — not a tab we can claim */
      }
    }
    // Otherwise open a NEW tab and mark it. Never goto() on an existing one: with an AI Studio
    // tab of Jack's in slot 0, that would throw away his work.
    const page = await ctx.newPage()
    await page.goto(NEW_CHAT_URL, { waitUntil: 'domcontentloaded', timeout: 60_000 })
    await page.evaluate(`sessionStorage.setItem(${JSON.stringify(TAB_MARK)}, '1')`)
    return new StudioClient(browser, page)
  }

  isAlive(): boolean {
    return this.browser.isConnected() && !this.page.isClosed()
  }

  async close(): Promise<void> {
    // Close the CDP connection only. The browser and the tab belong to the channel, not to us.
    await this.browser.close().catch(() => {})
  }

  private async lastModelText(): Promise<string> {
    return (await this.page.evaluate(`(() => {
      const turns = [...document.querySelectorAll(${JSON.stringify(SEL.chatTurn)})]
      for (let i = turns.length - 1; i >= 0; i--) {
        if (turns[i].querySelector(${JSON.stringify(SEL.modelTurn)})) return turns[i].innerText || ''
      }
      return ''
    })()`)) as string
  }

  private async state(): Promise<PageState> {
    return classifyPage({ url: this.page.url(), lastModelText: await this.lastModelText() })
  }

  /** Never throws — reporting "I cannot tell" is the job. */
  async signedInState(): Promise<SignedIn> {
    try {
      if (this.page.url().includes(SIGNED_OUT_PATH)) return 'no'
      if (!this.page.url().includes(HOST)) return 'unknown'
      const acct = norm(await this.page.locator(SEL.account).first().innerText({ timeout: 4000 }))
      return /@/.test(acct) ? 'yes' : 'unknown'
    } catch {
      return 'unknown'
    }
  }

  async ensureSignedIn(): Promise<void> {
    const s = await this.signedInState()
    if (s === 'yes') return
    throw new Error(
      `NOT_SIGNED_IN: the listening channel is not signed in to AI Studio (state: ${s}). ` +
        `A human must sign that window into the Ultra account — see docs/listening/automation.md §1.`,
    )
  }

  /**
   * A fresh chat, in Temporary mode.
   *
   * 🔴 Navigating to the new-chat URL does NOT start a new chat — the old turns come back
   * (Trap 6). The button is the only way, and it confirms before discarding. On an already-empty
   * chat it is disabled, which is success, not failure.
   */
  async newChat(): Promise<void> {
    const btn = this.page.locator(SEL.newChat).first()
    const disabled = await btn.getAttribute('aria-disabled').catch(() => null)
    if (disabled !== 'true') {
      await btn.click()
      const confirm = this.page.locator(SEL.dialogButton, { hasText: TEXT.discardAndContinue }).first()
      if (await confirm.isVisible({ timeout: 3000 }).catch(() => false)) await confirm.click()
      await this.page.waitForTimeout(800)
    }
    await this.ensureTemporaryChat()
  }

  /** Temporary chat is sticky across New chat, so this is idempotent by design. */
  private async ensureTemporaryChat(): Promise<void> {
    const already = /Temporary chat/i.test(
      (await this.page.evaluate(`document.body.innerText || ''`)) as string,
    )
    if (already) return
    await this.page.locator(SEL.moreActions).first().click()
    const item = this.page.locator('button,[role="menuitem"]', { hasText: TEXT.temporaryChat }).first()
    if (await item.isVisible({ timeout: 3000 }).catch(() => false)) await item.click()
    else await this.page.keyboard.press('Escape')
    await this.page.waitForTimeout(600)
  }

  /** Returns the name the page actually displays — never assume the pick took. */
  async selectModel(name: string): Promise<string> {
    const card = this.page.locator(SEL.modelCard).first()
    const shownNow = norm(await card.locator(SEL.modelCardTitle).first().innerText().catch(() => ''))
    if (shownNow.toLowerCase().includes(name.toLowerCase())) return shownNow

    await card.click()
    await this.page.waitForTimeout(700)
    const rows = this.page.locator(SEL.modelRow)
    const n = await rows.count()
    const available: string[] = []
    for (let i = 0; i < n; i++) {
      const row = rows.nth(i)
      const label = norm(await row.locator(SEL.modelRowTitle).first().innerText().catch(() => ''))
      if (label) available.push(label)
      if (label.toLowerCase().includes(name.toLowerCase())) {
        await row.click()
        await this.page.waitForTimeout(900)
        return norm(await card.locator(SEL.modelCardTitle).first().innerText().catch(() => label))
      }
    }
    await this.page.keyboard.press('Escape')
    throw new Error(`MODEL_NOT_FOUND: "${name}" is not in the menu. Available: ${available.join(' · ')}`)
  }

  /** 🔴 Must run on every describe: it is ON by default (Trap 2). */
  async disableSearchGrounding(): Promise<void> {
    const sw = this.page.locator(SEL.groundingSwitch).first()
    if (await sw.isVisible({ timeout: 4000 }).catch(() => false)) {
      if ((await sw.getAttribute('aria-checked')) === 'true') {
        await sw.click()
        await this.page.waitForTimeout(400)
      }
      if ((await sw.getAttribute('aria-checked')) === 'true') {
        throw new Error('STUDIO_ERROR: Search grounding would not switch off — refusing to describe with it on')
      }
      return
    }
    // Some layouts show it only as a chip.
    const chip = this.page.locator(SEL.groundingChipRemove).first()
    if (await chip.isVisible({ timeout: 1500 }).catch(() => false)) await chip.click()
  }

  /**
   * Attach by setting the hidden input directly. Never the OS chooser — under WSLg that dialog
   * is a dead end (same reason as `packages/flow-mcp/src/flow-client.ts`).
   *
   * The ready signal is the chip showing a **token count**, not merely the filename: Gemini bills
   * 32 tokens per second of audio, so a count means the file has been processed, and waiting on
   * the name alone races the upload.
   */
  async attachAudio(mp3Path: string): Promise<void> {
    await this.page.setInputFiles(SEL.fileInput, mp3Path).catch(async (e) => {
      throw new Error(`UPLOAD_FAILED: could not set the file input (${(e as Error).message})`)
    })
    // Trap 5 — the first upload on an account opens a rights reminder and swallows the file.
    const ack = this.page.locator(SEL.dialogButton, { hasText: TEXT.acknowledge }).first()
    if (await ack.isVisible({ timeout: 3000 }).catch(() => false)) {
      await ack.click()
      await this.page.setInputFiles(SEL.fileInput, mp3Path)
    }
    const deadline = Date.now() + 180_000
    for (;;) {
      const chip = norm(await this.page.locator(SEL.mediaChip).first().innerText().catch(() => ''))
      if (/\d[\d,]*\s*tokens/i.test(chip)) return
      if (Date.now() > deadline) {
        throw new Error(`TIMEOUT: the upload never reported a token count (chip read: "${chip}")`)
      }
      await this.page.waitForTimeout(1000)
    }
  }

  async submit(prompt: string): Promise<void> {
    const box = this.page.locator(SEL.promptBox).first()
    await box.click()
    await box.fill(prompt)
    const run = this.page.locator(SEL.runButton).first()
    const deadline = Date.now() + 15_000
    while ((await run.getAttribute('aria-disabled')) === 'true') {
      if (Date.now() > deadline) throw new Error('STUDIO_ERROR: Run stayed disabled after filling the prompt')
      await this.page.waitForTimeout(400)
    }
    await run.click()
  }

  /**
   * Wait for the model's turn to finish.
   *
   * 🔴 The done signal is ⬜ UNVERIFIED — no generation has ever succeeded on this account
   * (Trap 4, the 403). So this deliberately does NOT trust a single indicator: it waits for the
   * model turn's text to STOP GROWING for 4 seconds while Run is enabled again. That holds
   * whatever spinner the page turns out to use, and the first successful run must confirm it and
   * update `docs/listening/automation.md` §2.
   */
  async waitForReply(timeoutMs: number): Promise<string> {
    const run = this.page.locator(SEL.runButton).first()
    const deadline = Date.now() + timeoutMs
    let last = ''
    let stableSince = 0
    for (;;) {
      await this.page.waitForTimeout(1000)
      const st = await this.state()
      if (st === 'signed-out') throw new Error('NOT_SIGNED_IN: the page signed out mid-run')
      const text = await this.lastModelText()
      if (st === 'rate-limited') throw new Error(`RATE_LIMITED: ${norm(text).slice(0, 200)}`)
      if (st === 'error') throw new Error(`STUDIO_ERROR: ${norm(text).slice(0, 200)}`)

      const idle = (await run.getAttribute('aria-disabled')) !== 'true'
      if (text && text === last && idle) {
        if (!stableSince) stableSince = Date.now()
        if (Date.now() - stableSince >= 4000) return text.trim()
      } else {
        stableSince = 0
      }
      last = text

      if (Date.now() > deadline) {
        const dump = join(tmpdir(), `listen-timeout-${Date.now()}.html`)
        await writeFile(dump, await this.page.content()).catch(() => {})
        throw new Error(
          `TIMEOUT: no settled reply in ${Math.round(timeoutMs / 1000)} s. Page dumped to ${dump}. ` +
            `🔴 A policy/permission refusal looks exactly like a timeout — read the dump before retrying.`,
        )
      }
    }
  }
}

export const defaultModelName = (env: NodeJS.ProcessEnv = process.env): string =>
  env.LISTEN_MODEL?.trim() || DEFAULT_MODEL
