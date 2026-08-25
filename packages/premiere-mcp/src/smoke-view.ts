/**
 * Live smoke for T21: a real, human-cut timeline comes back through MCP without blowing the cap.
 *
 * **Read-only by design.** It opens a project someone actually edited and only ever *reads* it —
 * the default target is Jack's camping cut, which is irreplaceable, so this script must never
 * mutate, save, or export. Everything it proves, it proves by asking questions.
 *
 * Point it somewhere else with `SMOKE_PROJECT=/mnt/d/…/x.prproj SMOKE_SEQUENCE=<name>`.
 *
 * Run with nothing else holding the bridge port — including the session's own MCP server.
 */
import fs from 'node:fs'
import { Checks, call, connectServer } from './smoke-client'
import { DEFAULT_BUDGET } from './view'

const PROJECT = process.env.SMOKE_PROJECT ?? '/mnt/d/badcode-videos/camping/camping vid Copy-test_1.prproj'
const SEQUENCE = process.env.SMOKE_SEQUENCE ?? 'camping'

const size = (v: unknown): number => JSON.stringify(v).length

async function main(): Promise<void> {
  const checks = new Checks()
  const { client, close } = await connectServer()

  try {
    checks.section('the project opens')
    const opened = await call(client, 'premiere_open_project', { path: PROJECT })
    if (!checks.check('opened without error', !opened.error, opened)) return
    checks.check('it already existed — this smoke must never create anything', opened.created === false, opened)

    checks.section('the digest')
    const digest = await call(client, 'premiere_get_sequence', { name: SEQUENCE })
    if (!checks.check('get_sequence returned', !digest.error, digest)) return

    const digestSize = size(digest)
    checks.note(`digest is ${digestSize} bytes`)
    checks.check('digest fits the budget with room to spare', digestSize < DEFAULT_BUDGET / 4, digestSize)

    const videoTracks = digest.videoTracks as { label: string; clipCount: number; clips?: unknown[] }[]
    const audioTracks = digest.audioTracks as { label: string; clipCount: number; clips?: unknown[] }[]
    checks.check('video tracks are described', Array.isArray(videoTracks) && videoTracks.length > 0, videoTracks?.length)
    checks.check('audio tracks are described', Array.isArray(audioTracks) && audioTracks.length > 0, audioTracks?.length)
    checks.check(
      'no clip was listed — this is a summary',
      [...videoTracks, ...audioTracks].every((t) => t.clips === undefined)
    )

    const totals = digest.totals as { videoClips: number; audioClips: number; params: number }
    checks.check('totals count the whole timeline', totals?.videoClips > 0 && totals?.audioClips > 0, totals)
    checks.note(`${totals.videoClips} video clips, ${totals.audioClips} audio clips, ${totals.params} params`)
    checks.check(
      'track clip counts add up to the total',
      videoTracks.reduce((n, t) => n + t.clipCount, 0) === totals.videoClips
    )

    checks.section('the full state on disk')
    const statePath = digest.statePath as string
    if (checks.check('statePath was returned', typeof statePath === 'string' && statePath.length > 0, statePath)) {
      checks.check('the file is there', fs.existsSync(statePath))
      const raw = JSON.parse(fs.readFileSync(statePath, 'utf8')) as {
        videoTracks: { items: unknown[] }[]
        audioTracks: { items: unknown[] }[]
      }
      const onDisk = raw.videoTracks.reduce((n, t) => n + t.items.length, 0)
      checks.check('it holds every clip, untrimmed', onDisk === totals.videoClips, { onDisk, expected: totals.videoClips })
      checks.check(
        'it is far bigger than what came back through MCP',
        fs.statSync(statePath).size > digestSize * 20,
        { file: fs.statSync(statePath).size, response: digestSize }
      )
      checks.note(`state file is ${fs.statSync(statePath).size} bytes against a ${digestSize}-byte response`)
    }

    checks.section('drilling into one track')
    const busiest = [...videoTracks].sort((a, b) => b.clipCount - a.clipCount)[0]!
    const trackRef = `v${videoTracks.indexOf(busiest)}`
    const oneTrack = await call(client, 'premiere_get_sequence', { name: SEQUENCE, tracks: [trackRef] })
    checks.check('the drill-down returned', !oneTrack.error, oneTrack)
    checks.check('it fits the budget', size(oneTrack) <= DEFAULT_BUDGET, size(oneTrack))

    const drilled = (oneTrack.videoTracks as { clips?: { ref: string }[] }[])[videoTracks.indexOf(busiest)]
    checks.check(`${busiest.label} listed its clips`, (drilled?.clips?.length ?? 0) > 0, drilled?.clips?.length)
    checks.check('it listed ALL of them, not a truncated slice', drilled?.clips?.length === busiest.clipCount, {
      listed: drilled?.clips?.length,
      expected: busiest.clipCount,
    })
    checks.check('the other tracks stayed summarised', (oneTrack.videoTracks as { clips?: unknown }[])
      .filter((_, i) => i !== videoTracks.indexOf(busiest))
      .every((t) => t.clips === undefined))
    if (oneTrack.notes) checks.note(`degraded with a note: ${(oneTrack.notes as string[])[0]}`)

    checks.section('drilling into single clips')
    const firstRef = drilled!.clips![0]!.ref
    const oneClip = await call(client, 'premiere_get_sequence', { name: SEQUENCE, clips: [firstRef] })
    checks.check('the clip drill-down returned', !oneClip.error, oneClip)
    checks.check('it fits the budget', size(oneClip) <= DEFAULT_BUDGET, size(oneClip))
    const clip = (oneClip.videoTracks as { clips?: { ref: string; components?: { params?: unknown[] }[] }[] }[])
      .flatMap((t) => t.clips ?? [])
      .find((c) => c.ref === firstRef)
    checks.check(`${firstRef} came back`, clip !== undefined, firstRef)
    checks.check('with its effect chain', (clip?.components?.length ?? 0) > 0, clip?.components?.length)
    checks.check('and with parameter values — nothing was degraded away', (clip?.components?.[0]?.params?.length ?? 0) > 0)

    checks.section('drilling into a time window')
    const window = await call(client, 'premiere_get_sequence', { name: SEQUENCE, range: [0, 15] })
    checks.check('the range query returned', !window.error, window)
    checks.check('it fits the budget', size(window) <= DEFAULT_BUDGET, size(window))
    const inWindow = [
      ...(window.videoTracks as { clips?: { start: number; end: number }[] }[]),
      ...(window.audioTracks as { clips?: { start: number; end: number }[] }[]),
    ].flatMap((t) => t.clips ?? [])
    checks.check('it found clips in the window', inWindow.length > 0, inWindow.length)
    checks.check(
      'every clip it listed actually overlaps the window',
      inWindow.length > 0 && inWindow.every((c) => c.start < 15 && c.end > 0)
    )

    checks.section('nothing exceeded the cap')
    // The point of the whole ticket, stated as one assertion.
    for (const [label, response] of [
      ['digest', digest],
      ['one track', oneTrack],
      ['one clip', oneClip],
      ['time window', window],
    ] as const) {
      checks.check(`${label} is within budget`, size(response) <= DEFAULT_BUDGET, size(response))
    }
  } finally {
    await close()
  }

  checks.finish('smoke-view')
}

main().catch((err) => {
  console.error(err)
  process.exitCode = 1
})
