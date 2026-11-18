import { execFileSync } from 'node:child_process'

/**
 * Reference-copy guard (2026-11-17, Priority Lane rounds 9-15).
 *
 * `editImage` attaches reference images, snapshots the media grid, submits, then takes the first tile
 * that was not in the snapshot as the result. When Flow is slow, the uploaded reference (or the previous
 * call's late result) finishes rendering AFTER the snapshot and is harvested as if it were the new image:
 * about 15 of ~40 reference calls on 2026-11-17 came back as the reference itself, and twice each result
 * landed one call late. Flow re-encodes uploads, so a copy is never byte-identical; compare a tiny greyscale
 * thumbnail instead. Measured: copies scored 0.1, real results 38-112 (mean absolute difference, 0-255).
 */
// 2026-11-18 (Malevolent Force): an edit that adds only a small figure scored 1.5-2.0 and was thrown away as a copy
// at the old threshold of 3; true copies scored 0.06 that day (0.1 on 2026-11-17). 0.5 sits between the two.
export const COPY_THRESHOLD = 0.5

const SIDE = 16

/** A 16x16 greyscale thumbnail of an image file (256 bytes), or null if ffmpeg cannot read it. */
export function thumbPrint(path: string): Uint8Array | null {
  try {
    const buf = execFileSync(
      'ffmpeg',
      ['-v', 'error', '-i', path, '-vf', `scale=${SIDE}:${SIDE},format=gray`, '-frames:v', '1', '-f', 'rawvideo', '-'],
      { maxBuffer: 1 << 20, stdio: ['ignore', 'pipe', 'ignore'] },
    )
    return buf.length === SIDE * SIDE ? new Uint8Array(buf) : null
  } catch {
    return null
  }
}

/** Mean absolute difference between two equal-length thumbnails (0 = identical, 255 = opposite). */
export function meanAbsDiff(a: Uint8Array, b: Uint8Array): number {
  if (a.length !== b.length || a.length === 0) return 255
  let sum = 0
  for (let i = 0; i < a.length; i++) sum += Math.abs(a[i]! - b[i]!)
  return sum / a.length
}

/** True when `print` matches any of `refs` closely enough to be a re-encoded copy of it. */
export function isCopyOfAny(print: Uint8Array | null, refs: (Uint8Array | null)[], threshold = COPY_THRESHOLD): boolean {
  if (!print) return false
  return refs.some((r) => r !== null && meanAbsDiff(print, r) < threshold)
}
