/**
 * Read a JPEG's dimensions from its own header.
 *
 * Exists for one job: a RESUMED batch skips prompts whose file is already on disk, and those
 * items must still report real `width`/`height`. Without this they would come back as 0×0 and
 * a caller building a manifest from the result would silently record nothing — the same class
 * of "returns success, means nothing" bug that has bitten this package repeatedly.
 *
 * Deliberately not a dependency: it is ~20 lines, it runs on a Buffer we have already read,
 * and every image Flow hands us is a JPEG.
 */

/** SOF markers carry the frame size. These three in the same numeric range do NOT. */
const NOT_SOF = new Set([0xc4, 0xc8, 0xcc]) // DHT, JPGA, DAC

/** Markers that stand alone — no length field follows, so they cannot be skipped by length. */
function isStandalone(marker: number): boolean {
  return marker === 0x01 || marker === 0xd8 || marker === 0xd9 || (marker >= 0xd0 && marker <= 0xd7)
}

export function jpegSize(buf: Uint8Array): { width: number; height: number } | null {
  if (buf.length < 4 || buf[0] !== 0xff || buf[1] !== 0xd8) return null
  let i = 2
  while (i + 9 < buf.length) {
    // Segments are 0xFF-prefixed; fill bytes (repeated 0xFF) are legal, so scan rather than assume.
    if (buf[i] !== 0xff) {
      i++
      continue
    }
    const marker = buf[i + 1]!
    if (marker === 0xff) {
      i++
      continue
    }
    if (isStandalone(marker)) {
      i += 2
      continue
    }
    const len = (buf[i + 2]! << 8) | buf[i + 3]!
    if (len < 2) return null // malformed: a length must cover its own two bytes
    if (marker >= 0xc0 && marker <= 0xcf && !NOT_SOF.has(marker)) {
      // SOF payload: precision(1) height(2) width(2) — height FIRST, which is the easy slip.
      return { height: (buf[i + 5]! << 8) | buf[i + 6]!, width: (buf[i + 7]! << 8) | buf[i + 8]! }
    }
    i += 2 + len
  }
  return null
}
