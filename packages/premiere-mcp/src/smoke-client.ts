/**
 * Shared harness for the live `smoke-*.ts` scripts.
 *
 * The smokes drive the REAL MCP server over stdio rather than the bridge directly. That is the
 * point: it exercises `server.ts` — config gating, path translation, directory creation,
 * normalisation — instead of reimplementing it in the test and proving only that the
 * reimplementation agrees with itself.
 *
 * Nothing else may hold the bridge port while a smoke runs.
 */
import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js'
import fs from 'node:fs'
import path from 'node:path'

export interface SmokeSession {
  client: Client
  close: () => Promise<void>
}

/**
 * `tsx` directly, NOT `npx tsx`: npx adds two wrapper processes, and killing the wrapper leaves
 * the node process holding the bridge port — an `EADDRINUSE` landmine for the next run.
 */
export async function connectServer(env: Record<string, string> = {}): Promise<SmokeSession> {
  const transport = new StdioClientTransport({
    command: 'node_modules/.bin/tsx',
    args: ['packages/premiere-mcp/src/server.ts'],
    cwd: process.cwd(),
    env: { ...(process.env as Record<string, string>), ...env },
    stderr: 'inherit',
  })
  const client = new Client({ name: 'badcode-smoke', version: '0.0.0' })
  await client.connect(transport)
  return {
    client,
    close: async () => {
      await client.close()
      await transport.close() // belt and braces — the child must not outlive the script
    },
  }
}

interface CallResult {
  content?: { type: string; text?: string }[]
  isError?: boolean
}

/** Tool results are JSON in a text block; errors arrive as `{ error: true, code, ... }`. */
export async function call(
  client: Client,
  name: string,
  args: Record<string, unknown> = {}
): Promise<Record<string, unknown>> {
  const res = (await client.callTool({ name, arguments: args })) as CallResult
  const text = res.content?.find((c) => c.type === 'text')?.text ?? '{}'
  try {
    return JSON.parse(text) as Record<string, unknown>
  } catch {
    return { raw: text }
  }
}

export class Checks {
  private failures = 0

  check(label: string, condition: boolean, detail?: unknown): boolean {
    if (condition) {
      console.log(`  ✅ ${label}`)
    } else {
      this.failures += 1
      console.log(`  ❌ ${label}${detail === undefined ? '' : ` — ${JSON.stringify(detail)}`}`)
    }
    return condition
  }

  note(message: string): void {
    console.log(`  ·  ${message}`)
  }

  section(title: string): void {
    console.log(`\n— ${title} —`)
  }

  finish(name: string): void {
    console.log(this.failures === 0 ? `\n✅ ${name} passed` : `\n❌ ${this.failures} check(s) failed`)
    process.exitCode = this.failures === 0 ? 0 : 1
  }
}

/**
 * Capture a RAW panel dump (pre-`normalise.ts`) via `premiere_eval`, so test fixtures are real
 * Premiere output rather than something hand-written to match the code under test.
 * Only writes when `SMOKE_CAPTURE=1`, so an ordinary run never rewrites committed fixtures.
 */
export async function captureRawDump(client: Client, sequenceName: string, fixture: string): Promise<unknown> {
  const result = await call(client, 'premiere_eval', {
    code: `
      const project = await helpers.activeProject()
      const seq = await helpers.activeSequence(project, ${JSON.stringify(sequenceName)})
      return await helpers.dumpSequence(project, seq)
    `,
  })
  const value = result.value

  if (process.env.SMOKE_CAPTURE === '1' && value) {
    const file = path.join(process.cwd(), 'packages/premiere-mcp/src/fixtures', fixture)
    fs.writeFileSync(file, `${JSON.stringify(value, null, 2)}\n`)
    console.log(`  ·  captured ${fixture}`)
  }
  return value
}
