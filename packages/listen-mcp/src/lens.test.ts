import { describe, it, expect, beforeAll, afterAll } from 'vitest'
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { parseLens, listLenses, loadLens } from './lens'

const LENS_DIR = resolve(__dirname, '..', '..', '..', 'docs', 'listening', 'lenses')

const sample = `---
name: test
description: A test lens
---

Listen carefully.

## First
Say things.

## Second: with colon
More.
`

describe('parseLens', () => {
  it('reads name, description, body and headings in order', () => {
    const l = parseLens('fallback', sample)
    expect(l.name).toBe('test')
    expect(l.description).toBe('A test lens')
    expect(l.headings).toEqual(['First', 'Second: with colon'])
    expect(l.body.startsWith('Listen carefully.')).toBe(true)
    expect(l.body).not.toContain('description:')
    expect(l.hash).toMatch(/^[0-9a-f]{12}$/)
  })
  it('changes its hash when one byte changes', () => {
    expect(parseLens('t', sample).hash).not.toBe(parseLens('t', sample.replace('carefully', 'carefullY')).hash)
  })
  it('falls back to the file name when frontmatter has no name', () => {
    expect(parseLens('bare', '## Only\n').name).toBe('bare')
  })
})

describe('listLenses / loadLens', () => {
  let dir: string
  beforeAll(() => {
    dir = mkdtempSync(join(tmpdir(), 'listen-lens-test-'))
    writeFileSync(join(dir, 'zeta.md'), sample)
    writeFileSync(join(dir, 'alpha.md'), sample)
    writeFileSync(join(dir, 'notes.txt'), 'not a lens')
  })
  afterAll(() => rmSync(dir, { recursive: true, force: true }))

  it('lists only .md files, sorted, without the extension', () => {
    expect(listLenses(dir)).toEqual(['alpha', 'zeta'])
  })
  it('throws LENS_NOT_FOUND listing the real lenses', () => {
    // Asserts each lens is listed, not the exact roster: the list grows (suno-diff was added
    // 2026-09-12) and a test that pins it fails on every new lens for no reason.
    let thrown: Error | null = null
    try {
      loadLens(LENS_DIR, 'jazz')
    } catch (e) {
      thrown = e as Error
    }
    expect(thrown?.message).toMatch(/^LENS_NOT_FOUND: no lens "jazz"\. Available: /)
    for (const name of ['music', 'sfx', 'voice']) expect(thrown?.message).toContain(name)
  })
  it('refuses a name that tries to leave the directory', () => {
    expect(() => loadLens(dir, '../zeta')).toThrow(/^LENS_NOT_FOUND/)
  })
  it.each(['music', 'voice', 'sfx'])('loads the real %s lens with at least five headings', (name) => {
    const l = loadLens(LENS_DIR, name)
    expect(l.name).toBe(name)
    expect(l.headings.length).toBeGreaterThanOrEqual(5)
    expect(l.body).toMatch(/unsure/)
    expect(l.body).toMatch(/stereo/)
  })
  it('gives the music lens the headings the plan names', () => {
    expect(loadLens(LENS_DIR, 'music').headings).toEqual([
      'Overall impression', 'Drums', 'Bass', 'Lead and vocals', 'Pads, texture and effects',
      'Mix balance', 'Energy and structure', 'What stands out',
    ])
  })
})
