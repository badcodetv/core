/**
 * Local, per-machine config: `badcode.local.json` at the repo root (gitignored) plus env
 * overrides. The media root is established at setup, never guessed — every tool but
 * `premiere_status` refuses to run until it is set (Decision 2 in the plan).
 */
import fs from 'node:fs'
import path from 'node:path'

export interface Config {
  mediaRoot: string
  premiere: { port: number; exportPreset: string; bind: 'local' | 'all' }
}

const DEFAULT_PORT = 7890
const DEFAULT_EXPORT_PRESET =
  'C:\\Program Files\\Adobe\\Adobe Premiere Pro 2026\\MediaIO\\systempresets\\4E49434B_48323634\\01 - Match Source - High bitrate.epr'
const CONFIG_FILENAME = 'badcode.local.json'

export class ConfigError extends Error {
  constructor(public code: 'NO_MEDIA_ROOT' | 'BAD_CONFIG', message: string, public hint?: string) {
    super(message)
    this.name = 'ConfigError'
  }
}

export function loadConfig(repoRoot: string = process.cwd()): Config {
  const file = path.join(repoRoot, CONFIG_FILENAME)
  const raw = readConfigFile(file)

  const mediaRoot = process.env.BADCODE_MEDIA_ROOT ?? asString(raw.mediaRoot)
  if (!mediaRoot) {
    throw new ConfigError(
      'NO_MEDIA_ROOT',
      'No media root is configured.',
      `Copy badcode.local.json.example to ${CONFIG_FILENAME} at the repo root and set mediaRoot, or set BADCODE_MEDIA_ROOT.`
    )
  }

  const rawPremiere = isPlainObject(raw.premiere) ? raw.premiere : {}

  const port = readPort(process.env.PREMIERE_BRIDGE_PORT, rawPremiere.port)
  const exportPreset = process.env.PREMIERE_EXPORT_PRESET ?? asString(rawPremiere.exportPreset) ?? DEFAULT_EXPORT_PRESET
  const bind = readBind(process.env.PREMIERE_BRIDGE_BIND, rawPremiere.bind)

  return { mediaRoot, premiere: { port, exportPreset, bind } }
}

function readConfigFile(file: string): Record<string, unknown> {
  if (!fs.existsSync(file)) return {}

  let parsed: unknown
  try {
    parsed = JSON.parse(fs.readFileSync(file, 'utf8'))
  } catch (err) {
    throw new ConfigError('BAD_CONFIG', `${CONFIG_FILENAME} is not valid JSON: ${err instanceof Error ? err.message : String(err)}`)
  }
  if (!isPlainObject(parsed)) {
    throw new ConfigError('BAD_CONFIG', `${CONFIG_FILENAME} must be a JSON object.`)
  }
  return parsed
}

function readPort(envValue: string | undefined, fileValue: unknown): number {
  if (envValue === undefined) return typeof fileValue === 'number' ? fileValue : DEFAULT_PORT
  const port = Number(envValue)
  if (!Number.isFinite(port)) throw new ConfigError('BAD_CONFIG', `PREMIERE_BRIDGE_PORT is not a number: ${envValue}`)
  return port
}

function readBind(envValue: string | undefined, fileValue: unknown): 'local' | 'all' {
  if (envValue === 'local' || envValue === 'all') return envValue
  if (envValue !== undefined) throw new ConfigError('BAD_CONFIG', `PREMIERE_BRIDGE_BIND must be "local" or "all": ${envValue}`)
  if (fileValue === 'local' || fileValue === 'all') return fileValue
  return 'local'
}

function isPlainObject(v: unknown): v is Record<string, unknown> {
  return typeof v === 'object' && v !== null && !Array.isArray(v)
}

function asString(v: unknown): string | undefined {
  return typeof v === 'string' ? v : undefined
}

/** Per-story layout under the media root — one project, one sequence per scene (Decision 2). */
export function storyLayout(cfg: Config, story: string): {
  root: string
  projectPath: string
  rendersDir: string
  framesDir: string
  sceneDir(scene: string): string
  finalDir(scene: string): string
} {
  const root = joinWin(cfg.mediaRoot, story)
  return {
    root,
    projectPath: joinWin(root, `${story}.prproj`),
    rendersDir: joinWin(root, 'renders'),
    framesDir: joinWin(root, 'frames'),
    sceneDir: (scene: string) => joinWin(root, scene),
    finalDir: (scene: string) => joinWin(root, scene, 'final'),
  }
}

/** `<mediaRoot>\_bridge\panel` — where `scripts/build-panel.ts` mirrors the built panel. */
export function panelMirrorDir(cfg: Config): string {
  return joinWin(cfg.mediaRoot, '_bridge', 'panel')
}

function joinWin(...parts: string[]): string {
  return parts
    .map((p, i) => (i === 0 ? p.replace(/[\\/]+$/, '') : p.replace(/^[\\/]+|[\\/]+$/g, '')))
    .join('\\')
}
