import { existsSync } from 'node:fs'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import { chainDir, readVersions, repoRoot } from './paths.js'

describe('repoRoot', () => {
  it('finds the workspace root from inside a package', () => {
    const root = repoRoot()
    expect(existsSync(join(root, 'package.json'))).toBe(true)
    expect(existsSync(join(root, 'packages'))).toBe(true)
  })

  it('is stable regardless of which directory it starts from', () => {
    // The reason this helper exists: `npm run --workspace` changes the CWD.
    expect(repoRoot(join(repoRoot(), 'packages', 'chain-cli', 'src'))).toBe(repoRoot())
    expect(repoRoot(join(repoRoot(), 'apps'))).toBe(repoRoot())
  })

  it('throws rather than silently returning the filesystem root', () => {
    expect(() => repoRoot('/')).toThrow(/No workspace root/)
  })
})

describe('readVersions', () => {
  it('reads the pinned toolchain', () => {
    const v = readVersions()
    // Exact pins, not ranges — a range would defeat the purpose.
    expect(v.rust).toMatch(/^\d+\.\d+\.\d+$/)
    expect(v.agave).toMatch(/^\d+\.\d+\.\d+$/)
    expect(v.anchor).toMatch(/^\d+\.\d+\.\d+$/)
  })

  it('lives next to the Anchor workspace', () => {
    expect(existsSync(join(chainDir(), 'versions.json'))).toBe(true)
  })
})

describe('chainDir', () => {
  it('finds the Anchor workspace by its Anchor.toml, not by assuming a layout', () => {
    expect(existsSync(join(chainDir(), 'Anchor.toml'))).toBe(true)
  })

  it('still means <root>/chain when given an explicit root', () => {
    expect(chainDir('/somewhere')).toBe(join('/somewhere', 'chain'))
  })

  it('honours CHAIN_DIR, for layouts nobody anticipated', () => {
    const before = process.env.CHAIN_DIR
    process.env.CHAIN_DIR = '/tmp/elsewhere'
    try {
      expect(chainDir()).toBe('/tmp/elsewhere')
    } finally {
      if (before === undefined) delete process.env.CHAIN_DIR
      else process.env.CHAIN_DIR = before
    }
  })
})
