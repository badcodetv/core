import { describe, expect, it } from 'vitest'
import { evaluate, formatReport, parseVersion } from './doctor.js'

describe('parseVersion', () => {
  it('reads the version out of each tool’s own --version format', () => {
    expect(parseVersion('rustc 1.90.0 (1159e78c4 2025-09-14)')).toBe('1.90.0')
    expect(parseVersion('solana-cli 4.1.2 (src:devbuild; feat:123, client:Agave)')).toBe('4.1.2')
    expect(parseVersion('anchor-cli 1.1.2')).toBe('1.1.2')
    expect(parseVersion('v22.14.0')).toBe('22.14.0')
  })

  it('returns null when there is no version to find', () => {
    expect(parseVersion('command not found')).toBeNull()
    expect(parseVersion('')).toBeNull()
  })
})

describe('evaluate', () => {
  it('passes on an exact match', () => {
    expect(evaluate('rust', '1.90.0', 'rustc 1.90.0 (abc)', 'fix').ok).toBe(true)
  })

  it('fails on a mismatch and surfaces the remedy', () => {
    const c = evaluate('anchor', '1.1.2', 'anchor-cli 0.31.1', 'avm install 1.1.2')
    expect(c.ok).toBe(false)
    expect(c.got).toBe('0.31.1')
    expect(c.remedy).toBe('avm install 1.1.2')
  })

  it('reports a missing tool rather than throwing', () => {
    const c = evaluate('agave (solana)', '4.1.2', null, 'install it')
    expect(c.ok).toBe(false)
    expect(c.got).toBeNull()
  })

  it('compares node on major version only', () => {
    expect(evaluate('node', '22', 'v22.14.0', 'fix', true).ok).toBe(true)
    expect(evaluate('node', '22', 'v20.11.0', 'fix', true).ok).toBe(false)
  })

  it('does not treat a patch bump as a match when the pin is exact', () => {
    // The whole point of pinning: 1.1.3 is not 1.1.2.
    expect(evaluate('anchor', '1.1.2', 'anchor-cli 1.1.3', 'fix').ok).toBe(false)
  })

  it('distinguishes "installed but will not run" from "not installed"', () => {
    // Real case: Anchor's prebuilt binaries want glibc 2.39, Ubuntu 22.04 has 2.35.
    // Reporting that as "not installed" sends you reinstalling it forever.
    const glibc = "anchor-1.1.2: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.39' not found"
    const c = evaluate('anchor', '1.1.2', { out: null, broken: glibc }, 'avm install 1.1.2')
    expect(c.ok).toBe(false)
    expect(c.broken).toBe(glibc)
    expect(c.remedy).toContain('--from-source')
  })

  it('keeps the normal remedy when a broken binary is not a glibc problem', () => {
    const c = evaluate('anchor', '1.1.2', { out: null, broken: 'permission denied' }, 'avm install 1.1.2')
    expect(c.remedy).toBe('avm install 1.1.2')
  })
})

describe('formatReport', () => {
  it('lists remedies only for what actually failed', () => {
    const out = formatReport([
      evaluate('rust', '1.90.0', 'rustc 1.90.0', 'install rust'),
      evaluate('anchor', '1.1.2', null, 'avm install 1.1.2'),
    ])
    expect(out).toContain('✓ rust')
    expect(out).toContain('✗ anchor')
    expect(out).toContain('avm install 1.1.2')
    expect(out).not.toContain('install rust')
  })

  it('says nothing about fixing when everything passes', () => {
    const out = formatReport([evaluate('rust', '1.90.0', 'rustc 1.90.0', 'install rust')])
    expect(out).not.toContain('To fix')
  })
})
