import { describe, it, expect, beforeEach } from 'vitest'
import { existsSync, mkdtempSync, readFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { madeFiles, mirrorPath, stampFlow } from './prov'

let media: string, mirror: string
beforeEach(() => {
  const root = mkdtempSync(join(tmpdir(), 'prov-'))
  media = join(root, 'media')
  mirror = join(root, 'cards')
  process.env.BADCODE_MEDIA_ROOT = media
  process.env.BADCODE_PROV_MIRROR = mirror
})

describe('mirrorPath', () => {
  it('mirrors a file under the media root at the same relative path', () => {
    expect(mirrorPath(join(media, 'gpom/clips/x/a.jpg'))).toBe(join(mirror, 'gpom/clips/x/a.jpg.prov.json'))
  })
  it('puts anything outside the media root under _elsewhere', () => {
    expect(mirrorPath('/home/kai/.cache/p.jpg')).toBe(join(mirror, '_elsewhere/home/kai/.cache/p.jpg.prov.json'))
  })
})

describe('madeFiles', () => {
  it('collects path, candidates and batch items with their prompts', () => {
    const r = { items: [{ prompt: 'p1', path: '/a/01.jpg', mediaId: 'm1', candidates: [{ path: '/a/01-a.jpg' }, { path: '/a/01-b.jpg' }] }] }
    expect(madeFiles(r)).toEqual([
      { path: '/a/01.jpg', mediaId: 'm1', prompt: 'p1' },
      { path: '/a/01-a.jpg', mediaId: undefined, prompt: 'p1' },
      { path: '/a/01-b.jpg', mediaId: undefined, prompt: 'p1' },
    ])
  })
})

describe('stampFlow', () => {
  it('writes the card beside the file and into the mirror, and returns the result untouched', () => {
    const file = join(media, 's/v.mp4')
    const r = { path: file, mediaId: 'abc' }
    expect(stampFlow(r, { kind: 'video', tool: 'flow_generate_video', prompt: 'The camera does not move.', inputs: { start: '/x.jpg' } })).toBe(r)
    for (const p of [file + '.prov.json', join(mirror, 's/v.mp4.prov.json')]) {
      expect(existsSync(p)).toBe(true)
      const c = JSON.parse(readFileSync(p, 'utf8'))
      expect(c).toMatchObject({ schema: 'badcode.prov/1', engine: 'google-flow', source_id: 'abc', prompt: 'The camera does not move.', inputs: { start: '/x.jpg' } })
    }
  })
})
