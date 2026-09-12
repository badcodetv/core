import { describe, it, expect } from 'vitest'
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { loadEnvFile, parseEnvFile } from './env-file'

describe('parseEnvFile', () => {
  it('strips an export prefix and surrounding quotes', () => {
    expect(parseEnvFile('export A=1\nB="two"\nC=\'three\'')).toEqual({ A: '1', B: 'two', C: 'three' })
  })
  it('ignores blanks, comments and malformed lines', () => {
    expect(parseEnvFile('\n# a comment\nNOEQUALS\n=novalue\n9BAD=x\nOK=y')).toEqual({ OK: 'y' })
  })
  it('keeps a value containing = and #', () => {
    expect(parseEnvFile('K=a=b#c').K).toBe('a=b#c')
  })
  it('keeps unbalanced quotes as written rather than half-stripping', () => {
    expect(parseEnvFile('K="unclosed').K).toBe('"unclosed')
  })
})

describe('loadEnvFile', () => {
  const mk = (body: string) => {
    const d = mkdtempSync(join(tmpdir(), 'envtest-'))
    writeFileSync(join(d, '.env'), body)
    return d
  }

  it('sets missing vars and reports their names, never their values', () => {
    const d = mk('export GEMINI_API_KEY=secret-value\n')
    const env: NodeJS.ProcessEnv = {}
    const names = loadEnvFile(d, env)
    expect(names).toEqual(['GEMINI_API_KEY'])
    expect(names.join()).not.toContain('secret-value')
    expect(env.GEMINI_API_KEY).toBe('secret-value')
    rmSync(d, { recursive: true, force: true })
  })

  // 🔴 The load must never fight an explicit pin — that bug costs an afternoon.
  it('never overrides a variable already set in the environment', () => {
    const d = mk('export GEMINI_API_KEY=from-file\n')
    const env: NodeJS.ProcessEnv = { GEMINI_API_KEY: 'from-shell' }
    expect(loadEnvFile(d, env)).toEqual([])
    expect(env.GEMINI_API_KEY).toBe('from-shell')
    rmSync(d, { recursive: true, force: true })
  })

  it('treats an empty string as unset, so a blank export does not mask the file', () => {
    const d = mk('export GEMINI_API_KEY=from-file\n')
    const env: NodeJS.ProcessEnv = { GEMINI_API_KEY: '' }
    loadEnvFile(d, env)
    expect(env.GEMINI_API_KEY).toBe('from-file')
    rmSync(d, { recursive: true, force: true })
  })

  it('is silent when there is no .env at all', () => {
    expect(loadEnvFile(mkdtempSync(join(tmpdir(), 'noenv-')))).toEqual([])
  })
})
