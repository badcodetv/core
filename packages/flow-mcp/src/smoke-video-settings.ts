/**
 * Manual DOM-mapping probe for the video Settings panel — NOT part of CI. Costs no credits.
 *
 * ensureVideoSettings() was written blind and carries the two riskiest guesses in Wave A:
 * the shape of an opened model-menu row, and whether the aspect/count tabs are scoped to the
 * right section (they use .first() with no section scoping, so an "Image generation default"
 * section with identically named tabs would silently capture them).
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-video-settings.ts
 */
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    forceClick(l: unknown): Promise<void>
  }
  const page = inner.page
  await inner.ensureProjectRoot()

  const settings = page.getByRole('button', { name: /tune\s*Settings/i }).first()
  console.log('tune Settings count (project root):', await settings.count())

  // automation-video.md calls it the "agent panel footer" button, so the Agent panel presumably has
  // to be opened before it exists. Try that before declaring it missing.
  if (!(await settings.count())) {
    const agent = page.getByRole('button', { name: /^Agent$/i }).first()
    console.log('Agent button count:', await agent.count())
    if (await agent.count()) {
      await inner.forceClick(agent)
      await page.waitForTimeout(2500)
      console.log('tune Settings count (after opening Agent):', await settings.count())
    }
  }

  if (!(await settings.count())) {
    console.log('\n=== every visible button on the project root ===')
    const buttons = await page.evaluate(`(() => {
      const out = []
      for (const el of document.querySelectorAll('button, [role="button"]')) {
        const r = el.getBoundingClientRect()
        if (!r.width || !r.height) continue
        out.push({
          text: (el.textContent || '').trim().slice(0, 50),
          aria: el.getAttribute('aria-label') || undefined,
          x: Math.round(r.left), y: Math.round(r.top),
        })
      }
      return out
    })()`)
    console.log(JSON.stringify(buttons, null, 2))
    throw new Error('SETTINGS_TRIGGER_NOT_FOUND — see button dump above')
  }
  await inner.forceClick(settings)
  await page.waitForTimeout(2500)
  const shot = process.env.SHOT
  if (shot) {
    await page.screenshot({ path: shot })
    console.log('screenshot:', shot)
  }

  // What does the panel actually contain? Dump every control with its accessible name.
  const controls = await page.evaluate(`(() => {
    const out = []
    for (const el of document.querySelectorAll('button, [role="tab"], [role="combobox"], [role="radio"], select')) {
      const r = el.getBoundingClientRect()
      if (!r.width || !r.height) continue
      out.push({
        role: el.getAttribute('role') || el.tagName.toLowerCase(),
        text: (el.textContent || '').trim().slice(0, 60),
        aria: el.getAttribute('aria-label') || undefined,
        selected: el.getAttribute('aria-selected') || el.getAttribute('data-state') || undefined,
        y: Math.round(r.top),
      })
    }
    return out
  })()`)
  console.log('\n=== visible controls (y-ordered) ===')
  console.log(JSON.stringify(controls, null, 2))

  // Section headings, to see whether the aspect/count tabs are ambiguous.
  const headings = await page.evaluate(`(() => {
    const out = []
    for (const el of document.querySelectorAll('h1,h2,h3,h4,label,p,span')) {
      if (el.children.length) continue
      const t = (el.textContent || '').trim()
      if (!t || t.length > 60) continue
      const r = el.getBoundingClientRect()
      if (!r.width || !r.height) continue
      out.push({ t, y: Math.round(r.top) })
    }
    return out
  })()`)
  console.log('\n=== visible text nodes (y-ordered) ===')
  console.log(JSON.stringify(headings, null, 2))
} finally {
  await client.close()
}
