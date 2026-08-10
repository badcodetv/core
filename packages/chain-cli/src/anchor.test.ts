import { existsSync, mkdtempSync, readdirSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import { LEGACY_VALIDATOR_ARGS, exportIdl, idlDir } from './anchor.js'

describe('LEGACY_VALIDATOR_ARGS', () => {
  it('asks for the legacy validator, because Anchor 1.x defaults to surfpool', () => {
    // Without this every `anchor test` dies with "Failed to spawn `surfpool`".
    expect([...LEGACY_VALIDATOR_ARGS]).toEqual(['--validator', 'legacy'])
  })
})

describe('idlDir', () => {
  it('points inside the Anchor workspace', () => {
    expect(idlDir()).toMatch(/chain[/\\]target[/\\]idl$/)
  })
})

describe('exportIdl', () => {
  it('copies every generated IDL to the requested destination', () => {
    if (!existsSync(idlDir())) return // build has not run in this environment
    const dest = mkdtempSync(join(tmpdir(), 'idl-'))
    try {
      const copied = exportIdl(dest)
      expect(copied.length).toBeGreaterThan(0)
      for (const f of copied) expect(existsSync(join(dest, f))).toBe(true)
      expect(readdirSync(dest).every((f) => f.endsWith('.json'))).toBe(true)
    } finally {
      rmSync(dest, { recursive: true, force: true })
    }
  })

  it('says to build rather than failing obscurely when there is no IDL', () => {
    const missing = join(tmpdir(), 'definitely-not-a-repo-root-xyz')
    expect(() => exportIdl(join(tmpdir(), 'out'), missing)).toThrow(/chain build/)
  })
})
