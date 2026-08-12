/**
 * Manual check — are `model` and `aspect` actually honoured per image call, and does the
 * no-arguments path still behave as before? NOT part of CI. Costs four image generations.
 *
 * This is the proof for the "aspect lands one generation late" bug. It alternates
 * 16:9 → 9:16 → 16:9 so a stale result is unmistakable: under the bug each call returned the
 * PREVIOUS call's shape, which an all-same-aspect run could never reveal. Run it in a FRESH
 * project (pass no id) so no pre-existing media can be mistaken for a turn's output.
 *
 * The fourth call passes no options at all — the regression watch for refine()/generateImage()'s
 * deliberate "trust session state" path, which an edit loop mid-session depends on.
 *
 * Usage: npx tsx packages/flow-mcp/src/smoke-image-opts.ts [projectId]
 */
import { mkdtemp } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { FlowClient } from './flow-client'

const client = await FlowClient.connect()
try {
  const id = process.argv[2]
  if (id) await client.openProject({ id })
  else console.log('fresh project:', await client.createProject())

  const dir = await mkdtemp(join(tmpdir(), 'flow-imgopts-'))
  const PROMPT = 'A single plain metal disc resting on a dark tabletop, one soft light.'
  const wanted = ['16:9', '9:16', '16:9'] as const
  const results: { asked: string; ratio: number; w: number; h: number }[] = []

  for (const [i, aspect] of wanted.entries()) {
    console.log(`--- ${i + 1}/${wanted.length}: ${aspect} ---`)
    const r = await client.generateImage(PROMPT, join(dir, `${i}-${aspect.replace(':', 'x')}.jpg`), { aspect })
    const ratio = r.width / r.height
    console.log(r, 'ratio:', ratio.toFixed(2))
    results.push({ asked: aspect, ratio, w: r.width, h: r.height })
  }

  console.log('--- no options (must not disturb session state) ---')
  const plain = await client.generateImage(PROMPT, join(dir, 'plain.jpg'))
  console.log(plain, 'ratio:', (plain.width / plain.height).toFixed(2))

  const expected = (a: string) => (a === '16:9' ? (r: number) => r > 1.4 : (r: number) => r < 0.7)
  const bad = results.filter((r) => !expected(r.asked)(r.ratio))
  console.log(
    bad.length
      ? `ASPECT FAIL — ${bad.map((b) => `${b.asked} came back ${b.w}x${b.h}`).join('; ')}`
      : 'ASPECT OK — every call returned the shape it asked for, including the alternation',
  )
} finally {
  await client.close()
}
