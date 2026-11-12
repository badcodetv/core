import { describe, expect, it } from 'vitest'
import { buildUpdate, nextOffset, summarise } from './api'
import { parseId, parseEnvFile, toLocalPath, videoMime, imageMime } from './config'

const current = {
  id: 'abcdefghijk',
  snippet: {
    title: 'Old title',
    description: 'Old description',
    tags: ['a', 'b'],
    categoryId: '1',
    defaultLanguage: 'en-GB',
    publishedAt: '2026-11-01T00:00:00Z',
  },
  status: {
    privacyStatus: 'private',
    embeddable: true,
    license: 'youtube',
    publicStatsViewable: true,
    madeForKids: false,
    containsSyntheticMedia: true,
  },
}

describe('buildUpdate', () => {
  it('keeps description and tags when only the title changes', () => {
    const { parts, body } = buildUpdate(current, { title: 'New' })
    expect(parts).toEqual(['snippet'])
    expect(body.snippet).toEqual({
      title: 'New',
      description: 'Old description',
      tags: ['a', 'b'],
      categoryId: '1',
      defaultLanguage: 'en-GB',
    })
    expect(body.status).toBeUndefined()
  })

  it('keeps privacy and the AI label when only madeForKids changes', () => {
    const { parts, body } = buildUpdate(current, { madeForKids: true })
    expect(parts).toEqual(['status'])
    expect(body.status).toMatchObject({
      privacyStatus: 'private',
      selfDeclaredMadeForKids: true,
      containsSyntheticMedia: true,
    })
  })

  it('sends nothing when nothing changes', () => {
    expect(buildUpdate(current, {}).parts).toEqual([])
  })

  it('refuses a schedule on a public video', () => {
    expect(() => buildUpdate(current, { privacyStatus: 'public', publishAt: '2026-12-01T18:00:00Z' })).toThrow(/private/)
  })

  it('removes a schedule with null', () => {
    const withSchedule = { ...current, status: { ...current.status, publishAt: '2026-12-01T18:00:00Z' } }
    const { body } = buildUpdate(withSchedule, { publishAt: null })
    expect(body.status.publishAt).toBeUndefined()
  })
})

describe('summarise', () => {
  it('flattens the fields we use', () => {
    const s = summarise({ ...current, statistics: { viewCount: '12', likeCount: '3' } })
    expect(s).toMatchObject({
      id: 'abcdefghijk',
      title: 'Old title',
      privacyStatus: 'private',
      containsSyntheticMedia: true,
      url: 'https://youtu.be/abcdefghijk',
      stats: { views: 12, likes: 3, comments: 0 },
    })
  })
})

describe('helpers', () => {
  it('nextOffset reads the Range header', () => {
    expect(nextOffset('bytes=0-33554431')).toBe(33554432)
    expect(nextOffset(null)).toBe(0)
  })

  it('parseId takes ids and every link shape', () => {
    for (const s of [
      'dQw4w9WgXcQ',
      'https://youtu.be/dQw4w9WgXcQ',
      'https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=3',
      'https://youtube.com/shorts/dQw4w9WgXcQ',
      'https://studio.youtube.com/video/dQw4w9WgXcQ/edit',
    ]) {
      expect(parseId(s)).toBe('dQw4w9WgXcQ')
    }
    expect(() => parseId('nope')).toThrow()
  })

  it('toLocalPath turns Windows paths into WSL ones', () => {
    expect(toLocalPath('D:\\badcode-videos\\karen\\final.mp4')).toBe('/mnt/d/badcode-videos/karen/final.mp4')
    expect(toLocalPath('"C:/x/y.mov"')).toBe('/mnt/c/x/y.mov')
    expect(toLocalPath('/home/kai/a.mp4')).toBe('/home/kai/a.mp4')
  })

  it('mime types', () => {
    expect(videoMime('a.MP4')).toBe('video/mp4')
    expect(imageMime('t.jpg')).toBe('image/jpeg')
    expect(imageMime('t.gif')).toBeNull()
  })

  it('parseEnvFile', () => {
    expect(parseEnvFile('export YOUTUBE_CLIENT_ID="x.apps"\n# c\nYOUTUBE_CLIENT_SECRET=s')).toEqual({
      YOUTUBE_CLIENT_ID: 'x.apps',
      YOUTUBE_CLIENT_SECRET: 's',
    })
  })
})

import { isoSeconds } from './api'
import { aiLabels, appendLog } from './record'
import { mkdtempSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'

describe('shorts and AI labels', () => {
  it('isoSeconds', () => {
    expect(isoSeconds('PT28S')).toBe(28)
    expect(isoSeconds('PT9M32S')).toBe(572)
    expect(isoSeconds('PT1H2M3S')).toBe(3723)
  })

  it('a vertical clip of 3 minutes or less is a Short; landscape is not', () => {
    const v = (w: number, h: number, d: string) =>
      summarise({ id: 'abcdefghijk', contentDetails: { duration: d }, fileDetails: { videoStreams: [{ widthPixels: w, heightPixels: h }] } })
    expect(v(1080, 1920, 'PT28S').isShort).toBe(true)
    expect(v(1920, 1080, 'PT28S').isShort).toBe(false)
    expect(v(1080, 1920, 'PT4M').isShort).toBe(false)
    expect(summarise({ id: 'abcdefghijk' }).isShort).toBeUndefined()
  })

  it('aiLabels reads the last request per video from the log', () => {
    const dir = mkdtempSync(join(tmpdir(), 'yt-'))
    appendLog(dir, { action: 'upload', videoId: 'a', changes: { containsSyntheticMedia: true } })
    appendLog(dir, { action: 'update', videoId: 'b', requested: { containsSyntheticMedia: true } })
    appendLog(dir, { action: 'update', videoId: 'b', requested: { title: 'x' } })
    appendLog(dir, { action: 'update', videoId: 'c', changes: { title: { from: 'a', to: 'b' } } })
    const l = aiLabels(dir)
    expect([...l.entries()]).toEqual([['a', true], ['b', true]])
  })
})

import { buildChannelUpdate, keywordsString, parseKeywords } from './api'
import { channelRecord } from './record'

describe('channel', () => {
  const ch = {
    id: 'UCx',
    snippet: { title: 'Badcode', customUrl: '@badcode-tv' },
    brandingSettings: {
      channel: { title: 'Badcode', keywords: 'old "two words"', unsubscribedTrailer: 'abcdefghijk' },
      image: { bannerExternalUrl: 'https://yt3/banner' },
      hints: [{ property: 'x', value: 'y' }],
    },
  }

  it('keywords round-trip, quoting multi-word ones', () => {
    expect(keywordsString(['politics', 'music video', ' '])).toBe('politics "music video"')
    expect(parseKeywords('politics "music video"')).toEqual(['politics', 'music video'])
  })

  it('a description change keeps keywords, trailer and banner', () => {
    const body = buildChannelUpdate(ch, { description: 'New' })
    expect(body.brandingSettings.channel).toEqual({ title: 'Badcode', keywords: 'old "two words"', unsubscribedTrailer: 'abcdefghijk', description: 'New' })
    expect(body.brandingSettings.image).toEqual({ bannerExternalUrl: 'https://yt3/banner' })
    expect(body.brandingSettings.hints).toBeUndefined()
    expect(ch.brandingSettings.channel).not.toHaveProperty('description')
  })

  it('null removes the trailer; over-long text is refused', () => {
    expect(buildChannelUpdate(ch, { unsubscribedTrailer: null }).brandingSettings.channel.unsubscribedTrailer).toBeUndefined()
    expect(() => buildChannelUpdate(ch, { description: 'x'.repeat(1001) })).toThrow(/1000/)
  })

  it('channelRecord reads the branding fields', () => {
    expect(channelRecord(ch)).toMatchObject({ id: 'UCx', title: 'Badcode', handle: '@badcode-tv', keywords: 'old "two words"', description: '' })
  })
})
