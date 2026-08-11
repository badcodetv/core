import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import { composeBase, composeEnvFile, composeFile, chosenRunner, writeComposeEnv } from './docker.js'
import { readVersions } from './paths.js'

describe('chosenRunner', () => {
  it('honours CHAIN_RUNNER when it is set', () => {
    expect(chosenRunner({ CHAIN_RUNNER: 'host' })).toBe('host')
    expect(chosenRunner({ CHAIN_RUNNER: 'docker' })).toBe('docker')
  })

  it('rejects a typo rather than silently falling back', () => {
    // Falling back would run the wrong toolchain and look like it worked, which
    // is a much worse afternoon than an error message.
    expect(() => chosenRunner({ CHAIN_RUNNER: 'dokcer' })).toThrow(/must be/)
  })

  it('picks something valid when nothing is forced', () => {
    expect(['host', 'docker']).toContain(chosenRunner({}))
  })
})

describe('composeBase', () => {
  it('always pins both the compose file and the generated env file', () => {
    // Relying on the CWD here means the command works from the repo root and
    // silently targets nothing from anywhere else.
    const args = composeBase()
    expect(args[0]).toBe('compose')
    expect(args).toContain('--file')
    expect(args).toContain(composeFile())
    expect(args).toContain('--env-file')
    expect(args).toContain(composeEnvFile())
  })
})

describe('writeComposeEnv', () => {
  it('writes exactly the pins from versions.json', () => {
    const v = readVersions()
    writeComposeEnv()
    const body = readFileSync(composeEnvFile(), 'utf8')
    expect(body).toContain(`RUST_VERSION=${v.rust}`)
    expect(body).toContain(`AGAVE_VERSION=${v.agave}`)
    expect(body).toContain(`ANCHOR_VERSION=${v.anchor}`)
    expect(body).toContain(`NODE_MAJOR=${v.node}`)
  })

  it('mirrors the current user, so bind-mounted build output is not root-owned', () => {
    writeComposeEnv()
    const body = readFileSync(composeEnvFile(), 'utf8')
    expect(body).toContain(`CHAIN_UID=${process.getuid?.() ?? 1000}`)
  })

  it('marks the file as generated, since it is regenerated on every command', () => {
    writeComposeEnv()
    expect(readFileSync(composeEnvFile(), 'utf8')).toMatch(/^# GENERATED/)
  })
})
