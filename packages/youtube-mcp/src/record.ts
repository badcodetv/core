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
import { appendFileSync, mkdirSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import type { VideoSummary } from './api'

export function writeSnapshot(dir: string, channel: { id: string; title: string }, videos: VideoSummary[]): string {
  mkdirSync(dir, { recursive: true })
  const file = join(dir, 'channel.json')
  const rows = videos
    .map(({ stats: _stats, thumbnail: _thumb, ...rest }) => rest)
    .sort((a, b) => (b.publishedAt ?? '').localeCompare(a.publishedAt ?? ''))
  writeFileSync(
    file,
    JSON.stringify({ channel, syncedAt: new Date().toISOString(), count: rows.length, videos: rows }, null, 2) + '\n',
  )
  return file
}

export interface LogLine {
  action: 'upload' | 'update' | 'thumbnail' | 'playlist-create' | 'playlist-add'
  videoId?: string
  playlistId?: string
  title?: string
  changes?: Record<string, unknown>
  file?: string
  note?: string
}

export function appendLog(dir: string, line: LogLine): void {
  mkdirSync(dir, { recursive: true })
  appendFileSync(join(dir, 'log.jsonl'), JSON.stringify({ at: new Date().toISOString(), ...line }) + '\n')
}
