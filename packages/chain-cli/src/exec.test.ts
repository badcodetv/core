import { homedir } from 'node:os'
import { describe, expect, it } from 'vitest'
import { envWithTools, toolPath } from './exec.js'

describe('toolPath', () => {
  it('keeps whatever was already on PATH', () => {
    const path = toolPath({ PATH: '/usr/bin:/bin' })
    expect(path).toContain('/usr/bin')
    expect(path).toContain('/bin')
  })

  it('survives an empty PATH', () => {
    expect(() => toolPath({})).not.toThrow()
  })

  it('does not add a directory twice when it is already present', () => {
    // The Anza installer appends to ~/.profile, which non-login shells skip, so
    // we add the bin dirs ourselves — but must not keep stacking them up.
    const solanaBin = `${homedir()}/.local/share/solana/install/active_release/bin`
    const doubled = toolPath({ PATH: solanaBin })
    expect(doubled.split(':').filter((p) => p === solanaBin)).toHaveLength(1)
  })

  it('puts the tool directories ahead of the inherited PATH', () => {
    const path = toolPath({ PATH: '/usr/bin' })
    const parts = path.split(':')
    if (parts.length > 1) expect(parts[parts.length - 1]).toBe('/usr/bin')
  })
})

describe('envWithTools', () => {
  it('copies the environment rather than mutating it', () => {
    const original = { PATH: '/usr/bin', FOO: 'bar' }
    const next = envWithTools(original)
    expect(next.FOO).toBe('bar')
    expect(original.PATH).toBe('/usr/bin')
  })
})
