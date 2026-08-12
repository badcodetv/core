/**
 * Manual DOM-mapping probe — NOT part of CI, and not a test of our parsers.
 *
 * Dumps the RAW asset-picker + character rows exactly as Flow renders them, so a parser can
 * be written against observed strings instead of inferred ones. Wave A's media parser was
 * written blind and guessed the wrong shape; this exists so that does not happen twice.
 *
 * Pre-req: `./scripts/flow-chrome.sh`, logged in, with a project already open.
 * Usage: npx tsx packages/flow-mcp/src/smoke-raw.ts
 */
import { FlowClient } from './flow-client'
import { SCRAPE_MEDIA_OPTIONS } from './media-list'

const client = await FlowClient.connect()
try {
  // Drive the private helpers directly: listMedia() closes the picker in a finally block, so
  // scraping after it returns finds an empty document.
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    openAssetPicker(): Promise<unknown>
    closeAssetPicker(): Promise<void>
  }
  const page = inner.page

  await inner.ensureProjectRoot()
  await inner.openAssetPicker()
  const raw = await page.evaluate(`(${SCRAPE_MEDIA_OPTIONS})()`)
  console.log('=== RAW asset-picker options ===')
  console.log(JSON.stringify(raw, null, 2))
  await inner.closeAssetPicker()

  console.log('\n=== RAW character rows ===')
  // MUST be invoked as `(${fn})()`: evaluating a bare arrow-function string returns the
  // FUNCTION, and Playwright serialises that as undefined — so this printed "undefined" and
  // read as "no character rows on the page" while four characters were sitting there.
  // media-list.ts and project.ts carry the same warning; this script had the bug it warns about.
  const chars = await page.evaluate(`(() => [...document.querySelectorAll('a[href*="/character/"], [data-character-id]')].map(el => ({
    tag: el.tagName,
    href: el.getAttribute('href') || undefined,
    ariaLabel: el.getAttribute('aria-label') || undefined,
    text: (el.textContent || '').trim().slice(0, 200),
    imgAlt: el.querySelector('img') ? el.querySelector('img').getAttribute('alt') : undefined,
  })))()`)
  console.log(JSON.stringify(chars, null, 2))
} finally {
  await client.close()
}
