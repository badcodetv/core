/**
 * A thin YouTube Data API v3 client over fetch. No googleapis dependency (it is ~100 MB).
 *
 * Quota (default 10,000 units/day, per Google Cloud project): reads and list pages cost 1, an
 * update/insert of metadata ~50, thumbnails.set ~50. Uploads were 1,600 units until a 2025/26
 * change moved them to their own bucket (reported as 100 uploads/day); check the Cloud console's
 * Quotas page rather than trusting this comment.
 */
import { createReadStream, statSync } from 'node:fs'
import { readFile } from 'node:fs/promises'
import type { TokenSource } from './auth'

const API = 'https://www.googleapis.com/youtube/v3'
const UPLOAD = 'https://www.googleapis.com/upload/youtube/v3'

export class ApiError extends Error {
  constructor(
    public status: number,
    public reason: string,
    message: string,
  ) {
    super(message)
  }
}

type Json = Record<string, any>

/** The fields we read and write. Everything else on the resource is left as YouTube has it. */
export interface VideoSummary {
  id: string
  title: string
  description: string
  tags: string[]
  categoryId: string
  defaultLanguage?: string
  defaultAudioLanguage?: string
  privacyStatus: string
  publishAt?: string
  publishedAt?: string
  uploadStatus?: string
  madeForKids?: boolean
  containsSyntheticMedia?: boolean
  duration?: string
  /** Frame size of the uploaded file (owner-only `fileDetails`). */
  frame?: { width: number; height: number }
  /** YouTube has no "is a Short" flag: a Short is vertical or square and at most 3 minutes. */
  isShort?: boolean
  thumbnail?: string
  url: string
  stats?: { views: number; likes: number; comments: number }
}

export function summarise(v: Json): VideoSummary {
  const s = v.snippet ?? {}
  const st = v.status ?? {}
  const thumbs = s.thumbnails ?? {}
  const thumb = thumbs.maxres ?? thumbs.high ?? thumbs.medium ?? thumbs.default
  const stream = v.fileDetails?.videoStreams?.[0]
  const frame = stream?.widthPixels ? { width: Number(stream.widthPixels), height: Number(stream.heightPixels) } : undefined
  const secs = v.contentDetails?.duration ? isoSeconds(v.contentDetails.duration) : undefined
  return {
    id: v.id,
    title: s.title ?? '',
    description: s.description ?? '',
    tags: s.tags ?? [],
    categoryId: s.categoryId ?? '',
    ...(s.defaultLanguage ? { defaultLanguage: s.defaultLanguage } : {}),
    ...(s.defaultAudioLanguage ? { defaultAudioLanguage: s.defaultAudioLanguage } : {}),
    privacyStatus: st.privacyStatus ?? '',
    ...(st.publishAt ? { publishAt: st.publishAt } : {}),
    ...(s.publishedAt ? { publishedAt: s.publishedAt } : {}),
    ...(st.uploadStatus ? { uploadStatus: st.uploadStatus } : {}),
    ...(st.madeForKids !== undefined ? { madeForKids: st.madeForKids } : {}),
    ...(st.containsSyntheticMedia !== undefined ? { containsSyntheticMedia: st.containsSyntheticMedia } : {}),
    ...(v.contentDetails?.duration ? { duration: v.contentDetails.duration } : {}),
    ...(frame ? { frame } : {}),
    ...(frame && secs !== undefined ? { isShort: frame.height >= frame.width && secs <= 180 } : {}),
    ...(thumb?.url ? { thumbnail: thumb.url } : {}),
    url: `https://youtu.be/${v.id}`,
    ...(v.statistics
      ? {
          stats: {
            views: Number(v.statistics.viewCount ?? 0),
            likes: Number(v.statistics.likeCount ?? 0),
            comments: Number(v.statistics.commentCount ?? 0),
          },
        }
      : {}),
  }
}

/** What a caller may change. Absent = leave as is. */
export interface VideoChanges {
  title?: string
  description?: string
  tags?: string[]
  categoryId?: string
  defaultLanguage?: string
  defaultAudioLanguage?: string
  privacyStatus?: 'private' | 'unlisted' | 'public'
  publishAt?: string | null
  madeForKids?: boolean
  containsSyntheticMedia?: boolean
  embeddable?: boolean
  license?: 'youtube' | 'creativeCommon'
  publicStatsViewable?: boolean
}

const SNIPPET_KEYS = ['title', 'description', 'tags', 'categoryId', 'defaultLanguage', 'defaultAudioLanguage'] as const
const STATUS_KEYS = [
  'privacyStatus',
  'publishAt',
  'madeForKids',
  'containsSyntheticMedia',
  'embeddable',
  'license',
  'publicStatsViewable',
] as const

/**
 * Build a videos.update body from the current resource plus the changes.
 *
 * 🔴 videos.update REPLACES each part it is sent. Send `snippet` with only a new title and the
 * description and tags are wiped; send `status` without privacyStatus and it may reset. So every
 * writable field of a touched part is copied from the current resource first, then overlaid. A
 * part nobody asked to change is not sent at all.
 */
export function buildUpdate(current: Json, ch: VideoChanges): { parts: string[]; body: Json } {
  const body: Json = { id: current.id }
  const parts: string[] = []

  if (SNIPPET_KEYS.some((k) => ch[k] !== undefined)) {
    const s = current.snippet ?? {}
    const snippet: Json = {
      title: s.title,
      description: s.description ?? '',
      tags: s.tags ?? [],
      categoryId: s.categoryId,
    }
    if (s.defaultLanguage) snippet.defaultLanguage = s.defaultLanguage
    if (s.defaultAudioLanguage) snippet.defaultAudioLanguage = s.defaultAudioLanguage
    for (const k of SNIPPET_KEYS) if (ch[k] !== undefined) snippet[k] = ch[k]
    body.snippet = snippet
    parts.push('snippet')
  }

  if (STATUS_KEYS.some((k) => ch[k] !== undefined)) {
    const st = current.status ?? {}
    const status: Json = {
      privacyStatus: st.privacyStatus,
      embeddable: st.embeddable,
      license: st.license,
      publicStatsViewable: st.publicStatsViewable,
      // The API reads madeForKids but WRITES selfDeclaredMadeForKids.
      selfDeclaredMadeForKids: st.selfDeclaredMadeForKids ?? st.madeForKids ?? false,
    }
    if (st.containsSyntheticMedia !== undefined) status.containsSyntheticMedia = st.containsSyntheticMedia
    if (st.publishAt) status.publishAt = st.publishAt
    if (ch.privacyStatus !== undefined) status.privacyStatus = ch.privacyStatus
    if (ch.embeddable !== undefined) status.embeddable = ch.embeddable
    if (ch.license !== undefined) status.license = ch.license
    if (ch.publicStatsViewable !== undefined) status.publicStatsViewable = ch.publicStatsViewable
    if (ch.madeForKids !== undefined) status.selfDeclaredMadeForKids = ch.madeForKids
    if (ch.containsSyntheticMedia !== undefined) status.containsSyntheticMedia = ch.containsSyntheticMedia
    if (ch.publishAt === null) delete status.publishAt
    else if (ch.publishAt !== undefined) status.publishAt = ch.publishAt
    // A scheduled release only exists on a private video; YouTube rejects anything else.
    if (status.publishAt && status.privacyStatus !== 'private') {
      throw new ApiError(400, 'invalidPublishAt', 'publishAt (a scheduled release) needs privacyStatus "private".')
    }
    for (const k of Object.keys(status)) if (status[k] === undefined) delete status[k]
    body.status = status
    parts.push('status')
  }

  return { parts, body }
}

/** What the API lets us change on the channel itself. Name, handle, profile picture and links are Studio-only. */
export interface ChannelChanges {
  description?: string
  /** One entry per keyword; multi-word ones are quoted for YouTube's space-separated format. */
  keywords?: string[]
  /** ISO 3166-1 alpha-2, e.g. "GB". */
  country?: string
  defaultLanguage?: string
  /** The trailer shown to visitors who haven't subscribed. Must be a public video; null removes it. */
  unsubscribedTrailer?: string | null
}

export const CHANNEL_DESCRIPTION_MAX = 1000
export const CHANNEL_KEYWORDS_MAX = 500

/** ['politics', 'music video'] → 'politics "music video"' (YouTube's channel keyword format). */
export function keywordsString(words: string[]): string {
  return words
    .map((w) => w.trim().replace(/"/g, ''))
    .filter(Boolean)
    .map((w) => (/\s/.test(w) ? `"${w}"` : w))
    .join(' ')
}

/** 'politics "music video"' → ['politics', 'music video']. */
export function parseKeywords(s: string | undefined): string[] {
  return [...(s ?? '').matchAll(/"([^"]+)"|(\S+)/g)].map((m) => m[1] ?? m[2])
}

/**
 * Build a channels.update body for brandingSettings.
 *
 * 🔴 Like videos.update, channels.update REPLACES the whole brandingSettings part: anything not
 * sent is deleted (keywords, trailer, even the banner link). So the current part is copied whole
 * first, then the changes laid over it.
 */
export function buildChannelUpdate(current: Json, ch: ChannelChanges): Json {
  if (ch.description !== undefined && ch.description.length > CHANNEL_DESCRIPTION_MAX) {
    throw new ApiError(400, 'descriptionTooLong', `Channel description is ${ch.description.length} characters; YouTube allows ${CHANNEL_DESCRIPTION_MAX}.`)
  }
  const b = structuredClone(current.brandingSettings ?? {}) as Json
  const c: Json = (b.channel ??= {})
  if (ch.description !== undefined) c.description = ch.description
  if (ch.keywords !== undefined) {
    const k = keywordsString(ch.keywords)
    if (k.length > CHANNEL_KEYWORDS_MAX) throw new ApiError(400, 'keywordsTooLong', `Keywords are ${k.length} characters; YouTube allows ${CHANNEL_KEYWORDS_MAX}.`)
    c.keywords = k
  }
  if (ch.country !== undefined) c.country = ch.country
  if (ch.defaultLanguage !== undefined) c.defaultLanguage = ch.defaultLanguage
  if (ch.unsubscribedTrailer === null) delete c.unsubscribedTrailer
  else if (ch.unsubscribedTrailer !== undefined) c.unsubscribedTrailer = ch.unsubscribedTrailer
  // Read-only or retired fields the API returns but refuses on write.
  delete b.hints
  delete b.watch
  return { id: current.id, brandingSettings: b }
}

/** `PT1H2M3S` → 3723. */
export function isoSeconds(d: string): number {
  const m = /^P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$/.exec(d)
  if (!m) return NaN
  return Number(m[1] ?? 0) * 86400 + Number(m[2] ?? 0) * 3600 + Number(m[3] ?? 0) * 60 + Number(m[4] ?? 0)
}

export class YouTube {
  constructor(private tokens: TokenSource) {}

  private async req(method: string, url: string, init: { json?: unknown; headers?: Record<string, string> } = {}): Promise<Json> {
    const token = await this.tokens.accessToken()
    const res = await fetch(url, {
      method,
      headers: {
        authorization: `Bearer ${token}`,
        ...(init.json !== undefined ? { 'content-type': 'application/json' } : {}),
        ...init.headers,
      },
      body: init.json !== undefined ? JSON.stringify(init.json) : undefined,
    })
    if (res.status === 204) return {}
    const body = (await res.json().catch(() => ({}))) as Json
    if (!res.ok) throw toApiError(res.status, body)
    return body
  }

  async myChannel(): Promise<Json> {
    const r = await this.req('GET', `${API}/channels?part=snippet,contentDetails,statistics,status,brandingSettings&mine=true`)
    const ch = r.items?.[0]
    if (!ch) throw new ApiError(404, 'noChannel', 'The signed-in Google account has no YouTube channel.')
    return ch
  }

  /** Change the channel's description, keywords, country, language or trailer, keeping everything else. */
  async updateChannel(changes: ChannelChanges): Promise<Json> {
    const current = await this.myChannel()
    return this.req('PUT', `${API}/channels?part=brandingSettings`, { json: buildChannelUpdate(current, changes) })
  }

  async getVideos(ids: string[], parts = 'snippet,status,contentDetails,statistics,fileDetails'): Promise<Json[]> {
    const out: Json[] = []
    for (let i = 0; i < ids.length; i += 50) {
      const chunk = ids.slice(i, i + 50)
      const r = await this.req('GET', `${API}/videos?part=${parts}&id=${chunk.join(',')}&maxResults=50`)
      out.push(...(r.items ?? []))
    }
    return out
  }

  async getVideo(id: string): Promise<Json> {
    const [v] = await this.getVideos([id])
    if (!v) throw new ApiError(404, 'videoNotFound', `No video ${id} on this channel (or it was deleted).`)
    return v
  }

  /** Every upload on the channel, private and scheduled ones included, newest first. */
  async allUploads(): Promise<Json[]> {
    const ch = await this.myChannel()
    const playlist = ch.contentDetails?.relatedPlaylists?.uploads
    const ids: string[] = []
    let page = ''
    do {
      const r = await this.req(
        'GET',
        `${API}/playlistItems?part=contentDetails&playlistId=${playlist}&maxResults=50${page ? `&pageToken=${page}` : ''}`,
      )
      for (const it of r.items ?? []) ids.push(it.contentDetails.videoId)
      page = r.nextPageToken ?? ''
    } while (page)
    return this.getVideos(ids)
  }

  async updateVideo(id: string, ch: VideoChanges): Promise<Json> {
    const current = await this.getVideo(id)
    const { parts, body } = buildUpdate(current, ch)
    if (!parts.length) return current
    await this.req('PUT', `${API}/videos?part=${parts.join(',')}`, { json: body })
    return this.getVideo(id)
  }

  /**
   * Resumable upload: open a session with the metadata, then send the file in 32 MB chunks,
   * asking the server where it got to after any network failure.
   */
  async upload(path: string, mime: string, meta: Json, notifySubscribers: boolean): Promise<Json> {
    const size = statSync(path).size
    const token = await this.tokens.accessToken()
    const open = await fetch(
      `${UPLOAD}/videos?uploadType=resumable&part=snippet,status&notifySubscribers=${notifySubscribers}`,
      {
        method: 'POST',
        headers: {
          authorization: `Bearer ${token}`,
          'content-type': 'application/json; charset=UTF-8',
          'x-upload-content-length': String(size),
          'x-upload-content-type': mime,
        },
        body: JSON.stringify(meta),
      },
    )
    if (!open.ok) throw toApiError(open.status, (await open.json().catch(() => ({}))) as Json)
    const session = open.headers.get('location')
    if (!session) throw new ApiError(500, 'noUploadSession', 'YouTube opened no upload session.')

    const CHUNK = 32 * 1024 * 1024 // a multiple of 256 KiB, as the protocol requires
    let offset = 0
    let failures = 0
    while (true) {
      const end = Math.min(offset + CHUNK, size) - 1
      let res: Response
      try {
        res = await fetch(session, {
          method: 'PUT',
          headers: {
            authorization: `Bearer ${await this.tokens.accessToken()}`,
            'content-length': String(end - offset + 1),
            'content-range': `bytes ${offset}-${end}/${size}`,
          },
          body: createReadStream(path, { start: offset, end }) as unknown as BodyInit,
          duplex: 'half',
        } as RequestInit)
      } catch (e) {
        if (++failures > 5) throw e
        await sleep(2 ** failures * 1000)
        offset = await this.resumeOffset(session, size)
        continue
      }
      if (res.status === 200 || res.status === 201) return (await res.json()) as Json
      if (res.status === 308) {
        offset = nextOffset(res.headers.get('range'))
        failures = 0
        continue
      }
      if (res.status >= 500 && ++failures <= 5) {
        await sleep(2 ** failures * 1000)
        offset = await this.resumeOffset(session, size)
        continue
      }
      throw toApiError(res.status, (await res.json().catch(() => ({}))) as Json)
    }
  }

  private async resumeOffset(session: string, size: number): Promise<number> {
    const res = await fetch(session, {
      method: 'PUT',
      headers: { authorization: `Bearer ${await this.tokens.accessToken()}`, 'content-range': `bytes */${size}` },
    })
    if (res.status === 308) return nextOffset(res.headers.get('range'))
    throw new ApiError(res.status, 'uploadLost', 'The upload session was lost; start the upload again.')
  }

  async setThumbnail(videoId: string, path: string, mime: string): Promise<Json> {
    const token = await this.tokens.accessToken()
    const res = await fetch(`${UPLOAD}/thumbnails/set?videoId=${videoId}&uploadType=media`, {
      method: 'POST',
      headers: { authorization: `Bearer ${token}`, 'content-type': mime },
      body: await readFile(path),
    })
    const body = (await res.json().catch(() => ({}))) as Json
    if (!res.ok) throw toApiError(res.status, body)
    return body
  }

  async listPlaylists(): Promise<Json[]> {
    const out: Json[] = []
    let page = ''
    do {
      const r = await this.req(
        'GET',
        `${API}/playlists?part=snippet,status,contentDetails&mine=true&maxResults=50${page ? `&pageToken=${page}` : ''}`,
      )
      out.push(...(r.items ?? []))
      page = r.nextPageToken ?? ''
    } while (page)
    return out
  }

  async createPlaylist(title: string, description: string, privacyStatus: string): Promise<Json> {
    return this.req('POST', `${API}/playlists?part=snippet,status`, {
      json: { snippet: { title, description }, status: { privacyStatus } },
    })
  }

  async addToPlaylist(playlistId: string, videoId: string, position?: number): Promise<Json> {
    return this.req('POST', `${API}/playlistItems?part=snippet`, {
      json: {
        snippet: {
          playlistId,
          resourceId: { kind: 'youtube#video', videoId },
          ...(position !== undefined ? { position } : {}),
        },
      },
    })
  }

  async categories(region = 'GB'): Promise<Json[]> {
    const r = await this.req('GET', `${API}/videoCategories?part=snippet&regionCode=${region}`)
    return (r.items ?? []).filter((c: Json) => c.snippet?.assignable)
  }
}

/** `Range: bytes=0-1234` → 1235. No header = nothing received yet. */
export function nextOffset(range: string | null): number {
  const m = /bytes=\d+-(\d+)/.exec(range ?? '')
  return m ? Number(m[1]) + 1 : 0
}

function toApiError(status: number, body: Json): ApiError {
  const e = body.error ?? {}
  const reason = e.errors?.[0]?.reason ?? e.status ?? String(status)
  return new ApiError(status, reason, e.message ?? `HTTP ${status}`)
}

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))
