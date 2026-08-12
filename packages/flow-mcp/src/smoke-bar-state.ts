/**
 * Read-only dump of whatever the compose bar currently looks like — no clicks, no navigation,
 * no credits. Written to diagnose why the `crop_` config trigger was not visible after the
 * Animate menuitem attached a source frame.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-bar-state.ts
 */
import type { Page } from 'playwright-core'
import { FlowClient } from './flow-client'

const DUMP = `() => ({
  url: location.href,
  crops: [...document.querySelectorAll('button')]
    .filter(b => /crop_/.test(b.textContent || ''))
    .map(b => ({
      text: (b.textContent || '').trim().slice(0, 60),
      visible: !!(b.offsetWidth || b.offsetHeight || b.getClientRects().length),
      ariaHidden: b.closest('[aria-hidden="true"]') ? 'UNDER_ARIA_HIDDEN' : undefined,
      inert: b.closest('[inert]') ? 'UNDER_INERT' : undefined,
    })),
  panels: [...document.querySelectorAll('button')]
    .map(b => (b.textContent || '').trim())
    .filter(t => /^(Agent|tune\\s*Settings|close\\s*Close|arrow_back\\s*Back)$/i.test(t)),
  textboxes: [...document.querySelectorAll('div[role="textbox"][contenteditable="true"]')].map(el => ({
    text: (el.textContent || '').trim().slice(0, 40),
    visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length),
  })),
  chips: [...document.querySelectorAll('img')]
    .filter(im => im.width < 120 && im.width > 10)
    .length,
})`

const client = await FlowClient.connect()
try {
  const page = (client as unknown as { page: Page }).page
  console.log(JSON.stringify(await page.evaluate(`(${DUMP})()`), null, 2))
} finally {
  await client.close()
}
