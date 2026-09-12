#!/usr/bin/env -S npx tsx
/**
 * The `listen` MCP server — two tools, `listen_status` and `listen_describe`.
 *
 * 🔴 Describes are serialised through a promise chain. One browser tab, one chat: two concurrent
 * describes would attach a second file to the first one's prompt box and both answers would be
 * wrong in a way that looks like a bad model rather than a race.
 */
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { z } from 'zod'
import { fileURLToPath } from 'node:url'
import { dirname, join, resolve as resolvePath } from 'node:path'
import { probe, releaseLock, type Resolution } from '@badcode/flow-mcp/channel'
import { ok, fail } from '@badcode/flow-mcp/result'
import { NAME, VERSION } from './version'
import { StudioClient, StudioTransport, defaultModelName } from './studio-client'
import { DEFAULT_API_MODEL, GeminiApi } from './gemini-client'
import type { Transport } from './transport'
import { launchCommand, resolveListenChannel } from './channel'
import { listLenses } from './lens'
import { measure } from './measure'
import { describe } from './describe'

const REPO_ROOT = resolvePath(dirname(fileURLToPath(import.meta.url)), '..', '..', '..')
const LENS_DIR = join(REPO_ROOT, 'docs', 'listening', 'lenses')
const LOG_DIR = join(REPO_ROOT, 'docs', 'listening', 'log')
const MEASURE_SCRIPT = join(REPO_ROOT, 'scripts', 'audio-measure.py')

const DISCONNECTED_RE = /Target closed|browser has been closed|Target page, context or browser has been closed|ECONNRESET/i

/**
 * Which transport a describe uses.
 *
 * 🔴 Default is `api`. The browser cannot run a generation at all — AI Studio returns 403 to a
 * CDP-attached browser (docs/listening/automation.md Trap 4b) — so defaulting to it would mean
 * every unqualified describe failing. `studio` remains available for the human-assisted path:
 * it composes the chat and stops at Run.
 */
type TransportName = 'api' | 'studio'
const apiKey = () => process.env.GEMINI_API_KEY?.trim() ?? ''
const apiModelName = () => process.env.LISTEN_API_MODEL?.trim() || DEFAULT_API_MODEL

let channel: Resolution | null = null
let client: StudioClient | null = null
/** The serialisation chain. Every describe links onto the previous one's settlement. */
let queue: Promise<unknown> = Promise.resolve()

async function currentChannel(): Promise<Resolution> {
  channel ??= await resolveListenChannel(REPO_ROOT, 'listen')
  return channel
}

for (const sig of ['exit', 'SIGINT', 'SIGTERM'] as const) {
  process.on(sig, () => {
    if (channel && channel.how !== 'pinned') releaseLock(REPO_ROOT, channel.channel)
    if (sig !== 'exit') process.exit(0)
  })
}

async function withStudio<T>(fn: (c: StudioClient) => Promise<T>): Promise<T> {
  const ch = await currentChannel()
  for (let attempt = 0; attempt < 2; attempt++) {
    if (client && !client.isAlive()) {
      await client.close().catch(() => {})
      client = null
    }
    client ??= await StudioClient.connect(ch.endpoint)
    try {
      return await fn(client)
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err)
      if (attempt === 0 && DISCONNECTED_RE.test(msg)) {
        await client.close().catch(() => {})
        client = null
        continue
      }
      throw err
    }
  }
  throw new Error('LISTEN_ERROR: could not attach to the listening browser')
}

/** `CODE: message` → the code, for a structured failure the caller can branch on. */
const codeOf = (msg: string): string => {
  const m = /^([A-Z][A-Z0-9_]{2,}):/.exec(msg)
  return m ? m[1] : 'LISTEN_ERROR'
}

const notRunningHint = (ch: Resolution) =>
  `No browser on the listening channel. Run \`${launchCommand(ch.channel)}\` — 🔴 that channel must ` +
  `run BRANDED Google Chrome and be signed in to AI Studio: Chrome for Testing is refused outright ` +
  `("permission denied"). See docs/listening/automation.md §1.`

const server = new McpServer({ name: NAME, version: VERSION })

server.registerTool(
  'listen_status',
  {
    description:
      'Is the listening browser up and signed in to AI Studio, which channel it is on, and which ' +
      'lenses exist. Never throws for a missing browser — reporting that is its job.',
    inputSchema: {},
  },
  async () => {
    try {
      const ch = await currentChannel()
      const browserUp = await probe(ch.port)
      let signedIn: 'yes' | 'no' | 'unknown' = 'unknown'
      if (browserUp) {
        signedIn = await withStudio((c) => c.signedInState()).catch(() => 'unknown' as const)
      }
      return ok({
        channel: { channel: ch.channel, port: ch.port, how: ch.how, needsLaunch: ch.needsLaunch },
        browserUp,
        signedIn,
        lenses: listLenses(LENS_DIR),
        transport: apiKey() ? 'api' : 'studio (no GEMINI_API_KEY set)',
        apiKeySet: !!apiKey(),
        apiModel: apiModelName(),
        studioModel: defaultModelName(),
        ...(browserUp ? {} : { hint: notRunningHint(ch) }),
      })
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err)
      return fail(codeOf(msg), msg)
    }
  },
)

const SunoBoxesSchema = z
  .object({
    style: z.string().describe('The Style box, verbatim.'),
    exclude: z.string().describe('The Exclude styles box, verbatim.'),
    lyrics: z.string().optional().describe('The Lyrics box with its section cues. Omit for an instrumental.'),
    settings: z.string().optional().describe('Model, weirdness, style influence, Variety — as recorded.'),
  })
  .describe(
    'The Suno boxes that produced this audio, for a desired-vs-actual diff. Only with lens ' +
      '"suno-diff". Scrape them off the take\'s own song page, which displays all three.',
  )

server.registerTool(
  'listen_describe',
  {
    description:
      'Describe an audio file: Gemini via AI Studio, plus local measurements, filed in ' +
      'docs/listening/log/. Pass lens "suno-diff" together with sunoBoxes to get a clause-by-clause ' +
      'diff of a Suno take against the prompt that made it, and the next single prompt edit.',
    inputSchema: {
      path: z.string().describe('Audio file. Linux or Windows path.'),
      lens: z.string().optional().describe('Lens name; default "music". listen_status lists them.'),
      start: z.union([z.string(), z.number()]).optional().describe('Seconds or M:SS, source time.'),
      end: z.union([z.string(), z.number()]).optional(),
      question: z.string().optional().describe('Appended verbatim after the checklist.'),
      model: z
        .string()
        .optional()
        .describe(`Model id for the api transport (default ${DEFAULT_API_MODEL}), or the visible menu name for studio.`),
      transport: z
        .enum(['api', 'studio'])
        .optional()
        .describe(
          'Default "api" — the Gemini API, fully automated. "studio" composes an AI Studio chat and ' +
            'STOPS at Run for a human: the web page refuses CDP-driven generations (403).',
        ),
      sunoBoxes: SunoBoxesSchema.optional(),
    },
  },
  async (args) => {
    const run = async () => {
      const which: TransportName = (args.transport as TransportName | undefined) ?? 'api'
      if (which === 'api' && !apiKey()) {
        return fail('NO_API_KEY', 'GEMINI_API_KEY is not set', 'Add `export GEMINI_API_KEY=…` to .env, or pass transport "studio".')
      }
      if (which === 'studio') {
        const ch = await currentChannel()
        if (!(await probe(ch.port))) return fail('NOT_RUNNING', 'the listening browser is not up', notRunningHint(ch))
      }
      try {
        const deps = (transport: Transport, model: string) => ({
          transport,
          defaultModel: model,
          lensDir: LENS_DIR,
          logDir: LOG_DIR,
          repoRoot: REPO_ROOT,
          measure: (wav: string) => measure(wav, { script: MEASURE_SCRIPT }),
        })
        const result =
          which === 'api'
            ? await describe(args, deps(new GeminiApi(apiKey()), apiModelName()))
            : await withStudio((c) => describe(args, deps(new StudioTransport(c), defaultModelName())))
        return ok(result)
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err)
        return fail(codeOf(msg), msg)
      }
    }
    // Link onto the queue whatever happened to the previous call.
    const mine = queue.then(run, run)
    queue = mine.catch(() => {})
    return mine
  },
)

await server.connect(new StdioServerTransport())
