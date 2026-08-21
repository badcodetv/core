import { describe, it, expect, beforeEach, afterEach } from 'vitest'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { loadConfig, storyLayout, panelMirrorDir, ConfigError, type Config } from './config'

const ENV_KEYS = ['BADCODE_MEDIA_ROOT', 'PREMIERE_BRIDGE_PORT', 'PREMIERE_EXPORT_PRESET', 'PREMIERE_BRIDGE_BIND'] as const
let savedEnv: Record<string, string | undefined>
let repoRoot: string

beforeEach(() => {
  savedEnv = Object.fromEntries(ENV_KEYS.map((k) => [k, process.env[k]]))
  for (const k of ENV_KEYS) delete process.env[k]
  repoRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'premiere-mcp-config-'))
})

afterEach(() => {
  for (const k of ENV_KEYS) {
    if (savedEnv[k] === undefined) delete process.env[k]
    else process.env[k] = savedEnv[k]
  }
  fs.rmSync(repoRoot, { recursive: true, force: true })
})

function writeConfig(contents: unknown): void {
  fs.writeFileSync(path.join(repoRoot, 'badcode.local.json'), JSON.stringify(contents))
}

describe('loadConfig', () => {
  it('reads mediaRoot, port and exportPreset from the file', () => {
    writeConfig({ mediaRoot: 'D:\\badcode-videos', premiere: { port: 7891, exportPreset: 'C:\\preset.epr' } })
    expect(loadConfig(repoRoot)).toEqual<Config>({
      mediaRoot: 'D:\\badcode-videos',
      premiere: { port: 7891, exportPreset: 'C:\\preset.epr', bind: 'local' },
    })
  })

  it('defaults port 7890, the documented export preset, and bind local when premiere is omitted', () => {
    writeConfig({ mediaRoot: 'D:\\badcode-videos' })
    const cfg = loadConfig(repoRoot)
    expect(cfg.premiere.port).toBe(7890)
    expect(cfg.premiere.bind).toBe('local')
    expect(cfg.premiere.exportPreset).toBe(
      'C:\\Program Files\\Adobe\\Adobe Premiere Pro 2026\\MediaIO\\systempresets\\4E49434B_48323634\\01 - Match Source - High bitrate.epr'
    )
  })

  it('throws NO_MEDIA_ROOT with a hint naming badcode.local.json.example when the file is missing', () => {
    try {
      loadConfig(repoRoot)
      expect.unreachable()
    } catch (err) {
      expect(err).toBeInstanceOf(ConfigError)
      expect((err as ConfigError).code).toBe('NO_MEDIA_ROOT')
      expect((err as ConfigError).hint).toContain('badcode.local.json.example')
    }
  })

  it('throws NO_MEDIA_ROOT when the file exists but has no mediaRoot', () => {
    writeConfig({ premiere: { port: 7890 } })
    expect(() => loadConfig(repoRoot)).toThrow(ConfigError)
    try {
      loadConfig(repoRoot)
    } catch (err) {
      expect((err as ConfigError).code).toBe('NO_MEDIA_ROOT')
    }
  })

  it('throws BAD_CONFIG on unparseable JSON', () => {
    fs.writeFileSync(path.join(repoRoot, 'badcode.local.json'), '{ not json')
    try {
      loadConfig(repoRoot)
      expect.unreachable()
    } catch (err) {
      expect(err).toBeInstanceOf(ConfigError)
      expect((err as ConfigError).code).toBe('BAD_CONFIG')
    }
  })

  it('throws BAD_CONFIG when the file is not a JSON object', () => {
    fs.writeFileSync(path.join(repoRoot, 'badcode.local.json'), '["not", "an", "object"]')
    try {
      loadConfig(repoRoot)
      expect.unreachable()
    } catch (err) {
      expect((err as ConfigError).code).toBe('BAD_CONFIG')
    }
  })

  it('env overrides win over the file', () => {
    writeConfig({ mediaRoot: 'D:\\badcode-videos', premiere: { port: 7890, exportPreset: 'C:\\file-preset.epr' } })
    process.env.BADCODE_MEDIA_ROOT = 'E:\\other-root'
    process.env.PREMIERE_BRIDGE_PORT = '9999'
    process.env.PREMIERE_EXPORT_PRESET = 'C:\\env-preset.epr'
    process.env.PREMIERE_BRIDGE_BIND = 'all'
    expect(loadConfig(repoRoot)).toEqual<Config>({
      mediaRoot: 'E:\\other-root',
      premiere: { port: 9999, exportPreset: 'C:\\env-preset.epr', bind: 'all' },
    })
  })

  it('BADCODE_MEDIA_ROOT alone satisfies the requirement with no file present', () => {
    process.env.BADCODE_MEDIA_ROOT = 'D:\\badcode-videos'
    const cfg = loadConfig(repoRoot)
    expect(cfg.mediaRoot).toBe('D:\\badcode-videos')
    expect(cfg.premiere.port).toBe(7890)
  })

  it('throws BAD_CONFIG on a non-numeric PREMIERE_BRIDGE_PORT', () => {
    writeConfig({ mediaRoot: 'D:\\badcode-videos' })
    process.env.PREMIERE_BRIDGE_PORT = 'not-a-number'
    try {
      loadConfig(repoRoot)
      expect.unreachable()
    } catch (err) {
      expect((err as ConfigError).code).toBe('BAD_CONFIG')
    }
  })
})

describe('storyLayout', () => {
  const cfg: Config = { mediaRoot: 'D:\\badcode-videos', premiere: { port: 7890, exportPreset: 'preset', bind: 'local' } }

  it('lays out the fixed tree under <mediaRoot>\\<story>', () => {
    const layout = storyLayout(cfg, 'gitpush-origin-master')
    expect(layout.root).toBe('D:\\badcode-videos\\gitpush-origin-master')
    expect(layout.projectPath).toBe('D:\\badcode-videos\\gitpush-origin-master\\gitpush-origin-master.prproj')
    expect(layout.rendersDir).toBe('D:\\badcode-videos\\gitpush-origin-master\\renders')
    expect(layout.framesDir).toBe('D:\\badcode-videos\\gitpush-origin-master\\frames')
    expect(layout.sceneDir('s00')).toBe('D:\\badcode-videos\\gitpush-origin-master\\s00')
    expect(layout.finalDir('s00')).toBe('D:\\badcode-videos\\gitpush-origin-master\\s00\\final')
  })

  it('tolerates a trailing separator on mediaRoot', () => {
    const layout = storyLayout({ ...cfg, mediaRoot: 'D:\\badcode-videos\\' }, 'camping')
    expect(layout.root).toBe('D:\\badcode-videos\\camping')
  })
})

describe('panelMirrorDir', () => {
  it('is <mediaRoot>\\_bridge\\panel', () => {
    const cfg: Config = { mediaRoot: 'D:\\badcode-videos', premiere: { port: 7890, exportPreset: 'preset', bind: 'local' } }
    expect(panelMirrorDir(cfg)).toBe('D:\\badcode-videos\\_bridge\\panel')
  })
})
