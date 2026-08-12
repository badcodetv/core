/**
 * Manual check for ensureVideoSettings — NOT part of CI. Costs no credits (settings only).
 *
 * Drives the real panel, then reads back what is ACTUALLY selected in the "Video generation
 * default" section, so a silent no-op cannot pass as success. Also asserts the IMAGE section
 * was left alone, which is the specific damage the old `.first()` scoping did.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-ensure-video.ts [model]
 */
import { FlowClient } from './flow-client'

const model = process.argv[2] ?? 'Veo 3.1 Fast'

const client = await FlowClient.connect()
try {
  const inner = client as unknown as {
    page: import('playwright-core').Page
    ensureProjectRoot(): Promise<void>
    ensureVideoSettings(o?: { model?: string; aspect?: string; count?: number }): Promise<void>
  }
  await inner.ensureProjectRoot()

  const readBack = async () =>
    inner.page.evaluate(`(() => {
      const label = [...document.querySelectorAll('*')].find(
        el => !el.children.length && (el.textContent || '').trim() === 'Video generation default',
      )
      const img = [...document.querySelectorAll('*')].find(
        el => !el.children.length && (el.textContent || '').trim() === 'Image generation default',
      )
      const read = (root) => {
        if (!root) return null
        const sel = [...root.querySelectorAll('[role="tab"]')]
          .filter(t => t.getAttribute('aria-selected') === 'true')
          .map(t => (t.textContent || '').trim())
        const model = [...root.querySelectorAll('button')]
          .map(b => (b.textContent || '').trim())
          .find(t => /arrow_drop_down/.test(t))
        return { selectedTabs: sel, model }
      }
      return { video: read(label && label.parentElement), image: read(img && img.parentElement) }
    })()`)

  console.log(`--- asking for model=${JSON.stringify(model)}, aspect=16:9, count=1 ---`)
  await inner.ensureVideoSettings({ model, aspect: '16:9', count: 1 })

  // Re-open the panel to read persisted state rather than the state we just clicked.
  await inner.ensureVideoSettings({ model, aspect: '16:9', count: 1 })
  console.log('read back:', JSON.stringify(await readBack(), null, 2))
} finally {
  await client.close()
}
