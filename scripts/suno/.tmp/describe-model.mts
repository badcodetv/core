import { join } from 'node:path'
import { loadEnvFile } from '../../../packages/listen-mcp/src/env-file'
import { describe } from '../../../packages/listen-mcp/src/describe'
import { measure } from '../../../packages/listen-mcp/src/measure'
import { GeminiApi, DEFAULT_API_MODEL } from '../../../packages/listen-mcp/src/gemini-client'
const R = process.cwd()
loadEnvFile(R)
const res = await describe({ path: process.argv[2], lens: process.argv[3] || "music", start: process.argv[4] || undefined, end: process.argv[5] || undefined, question: process.argv[6] || undefined, model: process.env.GM } as any, {
  transport: new GeminiApi(process.env.GEMINI_API_KEY!.trim()), defaultModel: DEFAULT_API_MODEL,
  lensDir: join(R, 'docs/listening/lenses'), logDir: join(R, 'docs/listening/log'), repoRoot: R,
  measure: (w: string) => measure(w, { script: join(R, 'scripts/audio-measure.py') }),
})
console.log(JSON.stringify(res, null, 2))
