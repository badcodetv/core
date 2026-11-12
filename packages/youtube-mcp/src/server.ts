#!/usr/bin/env -S npx tsx
/**
 * The `youtube` MCP server — manages the BadCode YouTube channel through the YouTube Data API v3.
 * Setup and the house rules: docs/youtube/README.md.
 *
 * 🔑 Uploads default to PRIVATE. Going public is a human click in Studio (Kai, 2026-11-11: "we
 * don't really need to automate going from private to public"). The tools CAN set unlisted /
 * public / a scheduled release, but only when Kai or Jack has asked for that video, in words.
 *
 * Every change is written to docs/youtube/log.jsonl and the snapshot docs/youtube/channel.json is
 * refreshed, so git shows what changed on the channel and when.
 */
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { z } from 'zod'
import { existsSync, statSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join, resolve } from 'node:path'
import { NAME, VERSION } from './version'
import { freshClientCreds, imageMime, loadEnvFile, parseId, toLocalPath, tokenFile, videoMime } from './config'
import { AuthError, TokenSource, readToken } from './auth'
import { ApiError, YouTube, summarise, type VideoChanges } from './api'
import { appendLog, writeSnapshot } from './record'

const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..', '..')
const RECORD_DIR = join(REPO_ROOT, 'docs', 'youtube')
// The env as it was BEFORE .env was merged in: a real variable pinned in the shell wins over the file.
const REAL_ENV = { YOUTUBE_CLIENT_ID: process.env.YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET: process.env.YOUTUBE_CLIENT_SECRET }
loadEnvFile(REPO_ROOT)
const creds = () => freshClientCreds(REPO_ROOT, REAL_ENV)

const tokens = new TokenSource(creds, tokenFile())
const yt = new YouTube(tokens)

type Result = { content: { type: 'text'; text: string }[]; structuredContent?: Record<string, unknown>; isError?: boolean }

const ok = (data: unknown): Result => ({
  content: [{ type: 'text', text: JSON.stringify(data, null, 1) }],
  ...(data && typeof data === 'object' && !Array.isArray(data) ? { structuredContent: data as Record<string, unknown> } : {}),
})

const HINTS: Record<string, string> = {
  NO_CLIENT: 'Put YOUTUBE_CLIENT_ID and YOUTUBE_CLIENT_SECRET in .env (docs/youtube/README.md §Setup), then restart Claude.',
  NOT_SIGNED_IN: 'Ask the user to run `! npx tsx packages/youtube-mcp/src/login.ts` and pick the BadCode channel.',
  TOKEN_REVOKED:
    'Ask the user to run `! npx tsx packages/youtube-mcp/src/login.ts` again. If it keeps happening weekly, the Cloud app is still in "Testing": publish it to "In production".',
  quotaExceeded: 'The daily API quota is spent. It resets at midnight Pacific time.',
  uploadLimitExceeded: 'The channel hit its upload limit for today. Try again tomorrow.',
  forbidden: 'The signed-in account may not own this video. Check youtube_status shows the BadCode channel.',
  insufficientPermissions: 'The sign-in lacks the needed scope. Re-run the login script.',
}

function fail(err: unknown): Result {
  let code = 'ERROR'
  let message = err instanceof Error ? err.message : String(err)
  if (err instanceof AuthError) code = err.code
  if (err instanceof ApiError) {
    code = err.reason
    message = `${err.status} ${err.reason}: ${err.message}`
  }
  const hint = HINTS[code]
  return { content: [{ type: 'text', text: JSON.stringify({ error: true, code, message, ...(hint ? { hint } : {}) }) }], isError: true }
}

/** Run a tool body, turning any throw into a structured failure. */
const run = (fn: () => Promise<unknown>) => fn().then(ok, fail)

async function refreshSnapshot(): Promise<{ file: string; count: number }> {
  const ch = await yt.myChannel()
  const videos = (await yt.allUploads()).map(summarise)
  const file = writeSnapshot(RECORD_DIR, { id: ch.id, title: ch.snippet?.title ?? '' }, videos)
  return { file, count: videos.length }
}

/** After a change, keep the snapshot fresh; a failed refresh must not hide a successful change. */
const snapshotAfterChange = () => refreshSnapshot().then((s) => s.file).catch((e) => `snapshot not refreshed: ${String(e)}`)

const checkFile = (p: string): string => {
  const local = toLocalPath(p)
  if (!existsSync(local) || !statSync(local).isFile()) throw new Error(`File not found: ${p} (looked at ${local})`)
  return local
}

const privacy = z.enum(['private', 'unlisted', 'public'])

const server = new McpServer({ name: NAME, version: VERSION })

server.registerTool(
  'youtube_status',
  {
    description:
      'Is the YouTube server set up and signed in, and to WHICH channel (check it is BadCode). Never throws for a ' +
      'missing setup: reporting that is its job, with the next step in `hint`.',
    inputSchema: {},
  },
  async () => {
    const hasClient = !!creds()
    const file = tokenFile()
    const stored = readToken(file)
    const base = { clientConfigured: hasClient, tokenFile: file, signedIn: !!stored, signedInAt: stored?.obtained_at }
    if (!hasClient) return ok({ ...base, hint: HINTS.NO_CLIENT })
    if (!stored) return ok({ ...base, hint: HINTS.NOT_SIGNED_IN })
    try {
      const ch = await yt.myChannel()
      return ok({
        ...base,
        channel: {
          id: ch.id,
          title: ch.snippet?.title,
          handle: ch.snippet?.customUrl,
          url: `https://www.youtube.com/channel/${ch.id}`,
          videos: Number(ch.statistics?.videoCount ?? 0),
          subscribers: ch.statistics?.hiddenSubscriberCount ? 'hidden' : Number(ch.statistics?.subscriberCount ?? 0),
          views: Number(ch.statistics?.viewCount ?? 0),
          longUploadsStatus: ch.status?.longUploadsStatus,
        },
      })
    } catch (e) {
      return fail(e)
    }
  },
)

server.registerTool(
  'youtube_list_videos',
  {
    description:
      'Every video on the channel (private and scheduled included), newest first, with title, privacy, schedule, ' +
      'tags and view/like/comment counts. Also rewrites docs/youtube/channel.json (the repo\'s copy, without the counts). ' +
      'Descriptions are cut to 200 characters here; youtube_get_video has the full text.',
    inputSchema: {
      search: z.string().optional().describe('Only videos whose title contains this (case-insensitive).'),
    },
  },
  ({ search }) =>
    run(async () => {
      const ch = await yt.myChannel()
      const all = (await yt.allUploads()).map(summarise)
      const snapshot = writeSnapshot(RECORD_DIR, { id: ch.id, title: ch.snippet?.title ?? '' }, all)
      const q = search?.toLowerCase()
      const videos = all
        .filter((v) => !q || v.title.toLowerCase().includes(q))
        .map((v) => ({ ...v, description: v.description.length > 200 ? v.description.slice(0, 200) + '…' : v.description }))
      return { channel: ch.snippet?.title, count: videos.length, snapshot, videos }
    }),
)

server.registerTool(
  'youtube_get_video',
  {
    description: 'One video in full: title, full description, tags, category, privacy, schedule, AI label, duration, counts.',
    inputSchema: { videoId: z.string().describe('The id (the part after youtu.be/ or watch?v=), or a full URL.') },
  },
  ({ videoId }) => run(async () => summarise(await yt.getVideo(parseId(videoId)))),
)

server.registerTool(
  'youtube_upload',
  {
    description:
      'Upload a video file to the BadCode channel (resumable; big files are fine, this can take minutes). PRIVATE by ' +
      'default: making it public is a human click in Studio unless Kai or Jack asked for unlisted/public/a schedule. ' +
      'Optionally sets a thumbnail and adds it to playlists. Logged to docs/youtube/log.jsonl. Before writing the title ' +
      'and description: docs/marketing/the-reader.md, docs/voice.md, docs/using-ai.md, and no spoilers in the description.',
    inputSchema: {
      file: z.string().describe('The video file. WSL path or Windows path (D:\\...).'),
      title: z.string().max(100).describe('Max 100 characters; no < or >.'),
      description: z.string().max(5000).default(''),
      tags: z.array(z.string()).default([]).describe('All tags together must stay under 500 characters.'),
      containsSyntheticMedia: z
        .boolean()
        .describe(
          'YouTube\'s "altered or synthetic content" label. REQUIRED on purpose: docs/using-ai.md says we disclose AI ' +
            'at the point of consumption, so for our films this is normally true. Never guess it false.',
        ),
      categoryId: z.string().default('1').describe('"1" Film & Animation (default), "10" Music, "24" Entertainment, "25" News & Politics. youtube_categories lists all.'),
      privacyStatus: privacy.default('private'),
      publishAt: z.string().optional().describe('ISO 8601 time for a scheduled release. Needs privacyStatus "private".'),
      madeForKids: z.boolean().default(false),
      defaultLanguage: z.string().optional().describe('e.g. "en-GB".'),
      notifySubscribers: z.boolean().default(false).describe('Off by default: a private upload should not ping anyone.'),
      thumbnail: z.string().optional().describe('PNG or JPEG, under 2 MB, 1280×720 ideal.'),
      playlistIds: z.array(z.string()).optional(),
    },
  },
  (a) =>
    run(async () => {
      const file = checkFile(a.file)
      if (a.publishAt && a.privacyStatus !== 'private') throw new Error('publishAt needs privacyStatus "private".')
      const meta = {
        snippet: {
          title: a.title,
          description: a.description,
          tags: a.tags,
          categoryId: a.categoryId,
          ...(a.defaultLanguage ? { defaultLanguage: a.defaultLanguage, defaultAudioLanguage: a.defaultLanguage } : {}),
        },
        status: {
          privacyStatus: a.privacyStatus,
          selfDeclaredMadeForKids: a.madeForKids,
          containsSyntheticMedia: a.containsSyntheticMedia,
          ...(a.publishAt ? { publishAt: a.publishAt } : {}),
        },
      }
      const started = Date.now()
      const created = await yt.upload(file, videoMime(file), meta, a.notifySubscribers)
      const id = created.id as string
      const extras: Record<string, unknown> = {}
      if (a.thumbnail) {
        try {
          const t = checkFile(a.thumbnail)
          await yt.setThumbnail(id, t, imageMime(t) ?? 'image/png')
          extras.thumbnail = 'set'
        } catch (e) {
          extras.thumbnail = `FAILED: ${e instanceof Error ? e.message : String(e)}`
        }
      }
      if (a.playlistIds?.length) {
        extras.playlists = {}
        for (const p of a.playlistIds) {
          try {
            await yt.addToPlaylist(p, id)
            ;(extras.playlists as Record<string, string>)[p] = 'added'
          } catch (e) {
            ;(extras.playlists as Record<string, string>)[p] = `FAILED: ${e instanceof Error ? e.message : String(e)}`
          }
        }
      }
      const v = summarise(created)
      appendLog(RECORD_DIR, {
        action: 'upload',
        videoId: id,
        title: a.title,
        file: a.file,
        changes: { ...meta.snippet, ...meta.status, ...extras },
      })
      return {
        uploaded: v,
        // 🔴 Older unverified Cloud projects had uploads forced to private whatever was asked. If this
        // says private and public was requested, that lock is on: see docs/youtube/README.md.
        privacyAsRequested: v.privacyStatus === a.privacyStatus,
        studio: `https://studio.youtube.com/video/${id}/edit`,
        seconds: Math.round((Date.now() - started) / 1000),
        ...extras,
        snapshot: await snapshotAfterChange(),
      }
    }),
)

server.registerTool(
  'youtube_update_video',
  {
    description:
      'Change a video\'s details. Only the fields you pass change; everything else is kept (the tool reads the video ' +
      'first, because YouTube wipes any field left out of an update). Pass tags as the FULL new list. Changing ' +
      'privacy to unlisted/public needs Kai or Jack to have asked for it. Logged to docs/youtube/log.jsonl.',
    inputSchema: {
      videoId: z.string(),
      title: z.string().max(100).optional(),
      description: z.string().max(5000).optional(),
      tags: z.array(z.string()).optional().describe('Replaces the whole tag list.'),
      categoryId: z.string().optional(),
      defaultLanguage: z.string().optional(),
      defaultAudioLanguage: z.string().optional(),
      privacyStatus: privacy.optional(),
      publishAt: z.string().nullable().optional().describe('ISO time to schedule; null removes the schedule.'),
      madeForKids: z.boolean().optional(),
      containsSyntheticMedia: z.boolean().optional(),
      embeddable: z.boolean().optional(),
      publicStatsViewable: z.boolean().optional(),
    },
  },
  ({ videoId, ...changes }) =>
    run(async () => {
      const id = parseId(videoId)
      const before = summarise(await yt.getVideo(id))
      const after = summarise(await yt.updateVideo(id, changes as VideoChanges))
      const diff: Record<string, { from: unknown; to: unknown }> = {}
      for (const k of Object.keys(changes) as (keyof typeof after)[]) {
        if (JSON.stringify(before[k]) !== JSON.stringify(after[k])) diff[k] = { from: before[k], to: after[k] }
      }
      appendLog(RECORD_DIR, { action: 'update', videoId: id, title: after.title, changes: diff })
      return { video: after, changed: diff, snapshot: await snapshotAfterChange() }
    }),
)

server.registerTool(
  'youtube_set_thumbnail',
  {
    description:
      'Set a video\'s custom thumbnail: PNG or JPEG, under 2 MB, 1280×720 ideal. Needs the channel to be ' +
      'phone-verified (YouTube refuses custom thumbnails otherwise).',
    inputSchema: { videoId: z.string(), file: z.string().describe('WSL or Windows path.') },
  },
  ({ videoId, file }) =>
    run(async () => {
      const id = parseId(videoId)
      const local = checkFile(file)
      const mime = imageMime(local)
      if (!mime) throw new Error('Thumbnail must be .png, .jpg or .jpeg.')
      if (statSync(local).size > 2 * 1024 * 1024) throw new Error('Thumbnail is over 2 MB; YouTube will refuse it.')
      const r = await yt.setThumbnail(id, local, mime)
      appendLog(RECORD_DIR, { action: 'thumbnail', videoId: id, file })
      return { videoId: id, thumbnails: r.items?.[0] ?? r }
    }),
)

server.registerTool(
  'youtube_playlists',
  {
    description: 'List the channel\'s playlists, or create one (pass `create`), or add a video to one (pass `add`).',
    inputSchema: {
      create: z
        .object({ title: z.string(), description: z.string().default(''), privacyStatus: privacy.default('private') })
        .optional(),
      add: z.object({ playlistId: z.string(), videoId: z.string(), position: z.number().int().optional() }).optional(),
    },
  },
  ({ create, add }) =>
    run(async () => {
      const out: Record<string, unknown> = {}
      if (create) {
        const p = await yt.createPlaylist(create.title, create.description, create.privacyStatus)
        appendLog(RECORD_DIR, { action: 'playlist-create', playlistId: p.id, title: create.title })
        out.created = { id: p.id, title: create.title }
      }
      if (add) {
        const vid = parseId(add.videoId)
        await yt.addToPlaylist(add.playlistId, vid, add.position)
        appendLog(RECORD_DIR, { action: 'playlist-add', playlistId: add.playlistId, videoId: vid })
        out.added = { playlistId: add.playlistId, videoId: vid }
      }
      out.playlists = (await yt.listPlaylists()).map((p) => ({
        id: p.id,
        title: p.snippet?.title,
        privacy: p.status?.privacyStatus,
        videos: p.contentDetails?.itemCount,
      }))
      return out
    }),
)

server.registerTool(
  'youtube_categories',
  {
    description: 'The video categories YouTube lets us assign (id + name), for categoryId.',
    inputSchema: { region: z.string().default('GB') },
  },
  ({ region }) =>
    run(async () => ({ categories: (await yt.categories(region)).map((c) => ({ id: c.id, name: c.snippet?.title })) })),
)

await server.connect(new StdioServerTransport())
