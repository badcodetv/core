/**
 * The repo's copy of the channel. "Artifacts are the UI, the repo is the record" (CLAUDE.md):
 * YouTube is where the videos live, `docs/youtube/` is what we said about them and when.
 *
 *   channel.json  every video's title, description, tags, privacy, schedule — rewritten whole by
 *                 every sync and after every change. View counts are left OUT on purpose: they
 *                 change daily and would bury real edits in git noise.
 *   log.jsonl     one line per change made through this server (upload, edit, thumbnail,
 *                 playlist), appended, never rewritten.
 */
import { appendFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import type { VideoSummary } from './api'

/** The channel's own fields for the snapshot (no counts). */
export interface ChannelRecord {
  id: string
  title: string
  handle?: string
  description?: string
  keywords?: string
  country?: string
  defaultLanguage?: string
  unsubscribedTrailer?: string
}

export function channelRecord(ch: Record<string, any>): ChannelRecord {
  const b = ch.brandingSettings?.channel ?? {}
  return {
    id: ch.id,
    title: ch.snippet?.title ?? '',
    handle: ch.snippet?.customUrl,
    description: b.description ?? ch.snippet?.description ?? '',
    keywords: b.keywords ?? '',
    country: b.country ?? ch.snippet?.country,
    defaultLanguage: b.defaultLanguage,
    unsubscribedTrailer: b.unsubscribedTrailer,
  }
}

export function writeSnapshot(dir: string, channel: ChannelRecord, videos: VideoSummary[]): string {
  mkdirSync(dir, { recursive: true })
  const file = join(dir, 'channel.json')
  const labels = aiLabels(dir)
  const rows = videos
    .map(({ stats: _stats, thumbnail: _thumb, containsSyntheticMedia: _ai, ...rest }) => ({
      ...rest,
      aiLabel: labels.has(rest.id) ? (labels.get(rest.id) ? 'yes (set by us)' : 'no (set by us)') : 'unknown: never set from here',
    }))
    .sort((a, b) => (b.publishedAt ?? '').localeCompare(a.publishedAt ?? ''))
  writeFileSync(
    file,
    JSON.stringify({ channel, syncedAt: new Date().toISOString(), count: rows.length, videos: rows }, null, 2) + '\n',
  )
  return file
}

export interface LogLine {
  action: 'upload' | 'update' | 'thumbnail' | 'playlist-create' | 'playlist-add' | 'channel'
  videoId?: string
  playlistId?: string
  title?: string
  changes?: Record<string, unknown>
  /** What was asked for, as sent (the diff in `changes` can't show fields YouTube never reads back). */
  requested?: Record<string, unknown>
  file?: string
  note?: string
}

export function appendLog(dir: string, line: LogLine): void {
  mkdirSync(dir, { recursive: true })
  appendFileSync(join(dir, 'log.jsonl'), JSON.stringify({ at: new Date().toISOString(), ...line }) + '\n')
}

/**
 * Which videos we have given YouTube's "altered or synthetic content" label, from log.jsonl.
 *
 * 🔴 Why the log and not YouTube: videos.update ACCEPTS `status.containsSyntheticMedia` (the PUT
 * response echoes it) but videos.list never returns it (checked 2026-11-12). So the API can't tell
 * us which videos carry the label; our own record of setting it is the only source. The last
 * request per video wins.
 */
export function aiLabels(dir: string): Map<string, boolean> {
  const out = new Map<string, boolean>()
  const file = join(dir, 'log.jsonl')
  if (!existsSync(file)) return out
  for (const raw of readFileSync(file, 'utf-8').split('\n')) {
    if (!raw.trim()) continue
    try {
      const l = JSON.parse(raw) as LogLine
      const v = l.requested?.containsSyntheticMedia ?? (l.action === 'upload' ? l.changes?.containsSyntheticMedia : undefined)
      if (l.videoId && typeof v === 'boolean') out.set(l.videoId, v)
    } catch {
      /* a bad line never hides the rest */
    }
  }
  return out
}
