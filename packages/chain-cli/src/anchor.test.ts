import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import {
  LEGACY_VALIDATOR_ARGS, assertDefaultBuild, buildArgs, buildFeatures, builtArtifacts, deployDir,
  exportIdl, featureMarkerPath, generatedDir, idlDir, idlDrift, isLocalCluster, publishedInterfaces,
  recordBuildFeatures, restoreKeys, syncIdl, testArgs, typesDir,
} from './anchor.js'

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

/**
 * Build provenance. A binary carries no record of the cargo features that made
 * it, and `deploy` uploads whatever is on disk — so a test run that builds a
 * feature variant last leaves a program nobody would knowingly ship sitting
 * exactly where the deploy path looks for one.
 */
describe('feature markers', () => {
  /** A root with `n` built artifacts in target/deploy. */
  function rootWithArtifacts(...names: string[]): string {
    const root = mkdtempSync(join(tmpdir(), 'chain-root-'))
    mkdirSync(deployDir(root), { recursive: true })
    for (const n of names) writeFileSync(join(deployDir(root), `${n}.so`), 'ELF')
    return root
  }

  it('records the features beside the artifact they produced', () => {
    const root = rootWithArtifacts('demo')
    try {
      expect(recordBuildFeatures({ programName: 'demo', features: ['mock'], root })).toEqual(['demo'])
      expect(buildFeatures('demo', root)).toEqual(['mock'])
      expect(existsSync(featureMarkerPath('demo', root))).toBe(true)
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('clears the marker on the next default build, so it cannot go stale', () => {
    // A marker outliving its binary refuses a deploy that is fine, which is how
    // a guard gets deleted rather than fixed.
    const root = rootWithArtifacts('demo')
    try {
      recordBuildFeatures({ programName: 'demo', features: ['mock'], root })
      expect(recordBuildFeatures({ programName: 'demo', root })).toEqual(['demo'])
      expect(buildFeatures('demo', root)).toBeNull()
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('covers every artifact when the build named no program', () => {
    const root = rootWithArtifacts('one', 'two')
    try {
      expect(builtArtifacts(root).sort()).toEqual(['one', 'two'])
      recordBuildFeatures({ features: ['mock'], root })
      expect(buildFeatures('one', root)).toEqual(['mock'])
      expect(buildFeatures('two', root)).toEqual(['mock'])
      recordBuildFeatures({ root })
      expect(buildFeatures('one', root)).toBeNull()
      expect(buildFeatures('two', root)).toBeNull()
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('reports an unreadable marker rather than assuming it is innocent', () => {
    const root = rootWithArtifacts('demo')
    try {
      writeFileSync(featureMarkerPath('demo', root), 'not json')
      expect(buildFeatures('demo', root)).toEqual(['(unreadable build marker)'])
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })
})

describe('isLocalCluster', () => {
  it('knows a local validator by name or by URL', () => {
    expect(isLocalCluster('localnet')).toBe(true)
    expect(isLocalCluster('http://127.0.0.1:8899')).toBe(true)
    expect(isLocalCluster('http://localhost:8899')).toBe(true)
  })

  it('treats everything else as somebody’s real chain', () => {
    expect(isLocalCluster('devnet')).toBe(false)
    expect(isLocalCluster('mainnet-beta')).toBe(false)
    expect(isLocalCluster('https://api.devnet.solana.com')).toBe(false)
    expect(isLocalCluster('')).toBe(false)
  })
})

describe('assertDefaultBuild', () => {
  function rootWith(features: string[] | null): string {
    const root = mkdtempSync(join(tmpdir(), 'chain-root-'))
    mkdirSync(deployDir(root), { recursive: true })
    writeFileSync(join(deployDir(root), 'demo.so'), 'ELF')
    if (features) recordBuildFeatures({ programName: 'demo', features, root })
    return root
  }

  it('refuses a feature build on a cluster that is not local', () => {
    const root = rootWith(['mock'])
    try {
      let message = ''
      try {
        assertDefaultBuild({ cluster: 'devnet', programName: 'demo', root })
      } catch (err) {
        message = (err as Error).message
      }
      // Names the artifact, the features, and the way out of it.
      expect(message).toContain('demo')
      expect(message).toContain('mock')
      expect(message).toContain('chain build --program-name demo')
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('lets localnet do exactly what it does today', () => {
    // Localnet is where a feature build belongs — the suites need it there.
    const root = rootWith(['mock'])
    try {
      expect(() => assertDefaultBuild({ cluster: 'localnet', programName: 'demo', root })).not.toThrow()
      expect(() => assertDefaultBuild({ cluster: 'http://127.0.0.1:8899', programName: 'demo', root })).not.toThrow()
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('finds a flagged artifact even when the deploy named no program', () => {
    const root = rootWith(['mock'])
    try {
      expect(() => assertDefaultBuild({ cluster: 'devnet', root })).toThrow(/mock/)
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })

  it('says nothing about a default build, or a checkout that has never built', () => {
    // A missing marker is the ordinary case: target/ is gitignored, so a fresh
    // clone has none. It must not stand between anyone and a real deploy.
    const root = rootWith(null)
    try {
      expect(() => assertDefaultBuild({ cluster: 'devnet', programName: 'demo', root })).not.toThrow()
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
    expect(() => assertDefaultBuild({ cluster: 'devnet', root: join(tmpdir(), 'not-a-repo-root-xyz') })).not.toThrow()
  })
})

describe('idlDrift', () => {
  function root(): string {
    const r = mkdtempSync(join(tmpdir(), 'chain-root-'))
    mkdirSync(idlDir(r), { recursive: true })
    mkdirSync(typesDir(r), { recursive: true })
    writeFileSync(join(idlDir(r), 'demo.json'), '{"address":"demo"}')
    writeFileSync(join(typesDir(r), 'demo.ts'), 'export type Demo = never\n')
    return r
  }

  it('is empty when the committed copies are what the build produced', () => {
    const r = root()
    try {
      syncIdl(r)
      expect(idlDrift(r)).toEqual([])
      expect(publishedInterfaces(r).sort()).toEqual(['demo.json', 'demo.ts'])
    } finally {
      rmSync(r, { recursive: true, force: true })
    }
  })

  it('names what a build changed, so `dev` can report rather than publish', () => {
    const r = root()
    try {
      syncIdl(r)
      writeFileSync(join(idlDir(r), 'demo.json'), '{"address":"moved"}')
      writeFileSync(join(idlDir(r), 'second.json'), '{}')
      expect(idlDrift(r).sort()).toEqual(['demo.json', 'second.json'])
    } finally {
      rmSync(r, { recursive: true, force: true })
    }
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
    expect(buildArgs({ programName: 'demo', features: ['mock'] })).toEqual([
      '--program-name', 'demo', '--', '--features', 'mock',
    ])
  })

  it('lets a test run ask for the mock build', () => {
    expect(testArgs({ features: ['mock'] })).toEqual(
      expect.arrayContaining(['--', '--features', 'mock']),
    )
  })
})
