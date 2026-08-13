import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import { LEGACY_VALIDATOR_ARGS, buildArgs, exportIdl, generatedDir, idlDir, restoreKeys, syncIdl, testArgs, typesDir } from './anchor.js'

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

describe('restoreKeys', () => {
  it('puts saved program keypairs back where Anchor looks for them', () => {
    const root = mkdtempSync(join(tmpdir(), 'chain-root-'))
    try {
      mkdirSync(join(root, 'chain', 'keys'), { recursive: true })
      writeFileSync(join(root, 'chain', 'keys', 'demo-keypair.json'), '[1,2,3]')
      expect(restoreKeys(root)).toEqual(['demo-keypair.json'])
      expect(existsSync(join(root, 'chain', 'target', 'deploy', 'demo-keypair.json'))).toBe(true)
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('never overwrites a keypair the build already produced', () => {
    // target/deploy is the live identity. Clobbering it would change a deployed
    // program's address underneath a running validator.
    const root = mkdtempSync(join(tmpdir(), 'chain-root-'))
    try {
      mkdirSync(join(root, 'chain', 'keys'), { recursive: true })
      mkdirSync(join(root, 'chain', 'target', 'deploy'), { recursive: true })
      writeFileSync(join(root, 'chain', 'keys', 'demo-keypair.json'), '[1]')
      writeFileSync(join(root, 'chain', 'target', 'deploy', 'demo-keypair.json'), '[9]')
      expect(restoreKeys(root)).toEqual([])
      expect(readFileSync(join(root, 'chain', 'target', 'deploy', 'demo-keypair.json'), 'utf8')).toBe('[9]')
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('is a no-op when there is nothing saved', () => {
    expect(restoreKeys(join(tmpdir(), 'definitely-not-a-repo-root-xyz'))).toEqual([])
  })
})

describe('syncIdl', () => {
  // Against a fixture root, never the working tree. `syncIdl()` with no root
  // copies whatever the last build left in `chain/target/idl` over the
  // committed `chain/idl` — so running the suites under `--features mock` and
  // then running the unit tests published an interface carrying `set_mock_m2`
  // for a build that is never released. A validation command must not mutate
  // tracked files. Same shape as the `restoreKeys` cases above.
  it('publishes both the IDL and the TypeScript types, since the app needs both', () => {
    const root = mkdtempSync(join(tmpdir(), 'chain-root-'))
    try {
      mkdirSync(idlDir(root), { recursive: true })
      mkdirSync(typesDir(root), { recursive: true })
      writeFileSync(join(idlDir(root), 'demo.json'), '{"address":"demo"}')
      writeFileSync(join(typesDir(root), 'demo.ts'), 'export type Demo = never\n')

      const written = syncIdl(root)
      expect(written.some((f) => f.endsWith('.json'))).toBe(true)
      expect(written.some((f) => f.endsWith('.ts'))).toBe(true)
      for (const f of written) expect(existsSync(join(generatedDir(root), f))).toBe(true)
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('says the build failed rather than publishing nothing', () => {
    expect(() => syncIdl(join(tmpdir(), 'definitely-not-a-repo-root-xyz'))).toThrow(/build fail/)
  })
})

describe('test arguments', () => {
  it('reuses the running validator by default', () => {
    // Anchor otherwise starts a second validator on the same port and the run
    // dies on a collision that reads like a network problem.
    expect(testArgs({})).toContain('--skip-local-validator')
  })

  it('asks for the legacy validator only when Anchor starts its own', () => {
    expect(testArgs({ ownValidator: true })).toEqual(expect.arrayContaining(['--validator', 'legacy']))
    expect(testArgs({ ownValidator: true })).not.toContain('--skip-local-validator')
  })
})

describe('cargo features', () => {
  it('passes features after `--`, which anchor build does forward', () => {
    // Unlike `anchor deploy`, where everything after `--` is silently dropped
    // — proven the hard way, see deployProgram.
    expect(buildArgs({ features: ['mock'] })).toEqual(['--', '--features', 'mock'])
    expect(buildArgs({ features: ['mock', 'other'] })).toEqual(['--', '--features', 'mock,other'])
  })

  it('adds no `--` when there are no features', () => {
    expect(buildArgs({})).toEqual([])
    expect(buildArgs({ features: [] })).toEqual([])
    expect(buildArgs({ programName: 'x' })).toEqual(['--program-name', 'x'])
  })

  it('keeps the program name before the separator', () => {
    expect(buildArgs({ programName: 'enc', features: ['mock'] })).toEqual([
      '--program-name', 'enc', '--', '--features', 'mock',
    ])
  })

  it('lets a test run ask for the mock build', () => {
    expect(testArgs({ features: ['mock'] })).toEqual(
      expect.arrayContaining(['--', '--features', 'mock']),
    )
  })
})
