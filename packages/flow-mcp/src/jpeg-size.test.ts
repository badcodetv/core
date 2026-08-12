import { describe, it, expect } from 'vitest'
import { readFileSync, existsSync } from 'node:fs'
import { jpegSize } from './jpeg-size'

/** Build a minimal but structurally real JPEG header: SOI, an APP0 to skip, then a SOF0. */
function fakeJpeg(width: number, height: number, sofMarker = 0xc0): Uint8Array {
  const app0 = [0xff, 0xe0, 0x00, 0x06, 1, 2, 3, 4] // length 6 = 2 header + 4 payload
  const sof = [
    0xff, sofMarker,
    0x00, 0x11, // length
    0x08, // precision
    (height >> 8) & 0xff, height & 0xff,
    (width >> 8) & 0xff, width & 0xff,
    0x03, // components
    ...new Array(6).fill(0),
  ]
  return new Uint8Array([0xff, 0xd8, ...app0, ...sof, 0xff, 0xd9])
}

describe('jpegSize', () => {
  it('reads width and height, and does not transpose them', () => {
    // Height comes FIRST in the SOF payload; a transposed reader passes a square test and
    // fails every real one, so this case is deliberately non-square.
    expect(jpegSize(fakeJpeg(1376, 768))).toEqual({ width: 1376, height: 768 })
    expect(jpegSize(fakeJpeg(768, 1376))).toEqual({ width: 768, height: 1376 })
  })

  it('skips intervening segments to find the frame header', () => {
    const withExtra = new Uint8Array([
      0xff, 0xd8,
      0xff, 0xfe, 0x00, 0x08, 1, 2, 3, 4, 5, 6, // COM segment
      ...fakeJpeg(200, 100).slice(2),
    ])
    expect(jpegSize(withExtra)).toEqual({ width: 200, height: 100 })
  })

  it('handles progressive JPEGs (SOF2), which Flow may well hand us', () => {
    expect(jpegSize(fakeJpeg(640, 480, 0xc2))).toEqual({ width: 640, height: 480 })
  })

  it('is not fooled by DHT, which sits in the same marker range as SOF', () => {
    // 0xC4 is a Huffman table, not a frame header. Reading it as SOF yields garbage sizes.
    const dhtThenSof = new Uint8Array([
      0xff, 0xd8,
      0xff, 0xc4, 0x00, 0x07, 9, 9, 9, 9, 9, // DHT with nonsense payload
      ...fakeJpeg(321, 123).slice(2),
    ])
    expect(jpegSize(dhtThenSof)).toEqual({ width: 321, height: 123 })
  })

  it('returns null rather than guessing on junk', () => {
    expect(jpegSize(new Uint8Array([1, 2, 3, 4]))).toBe(null)
    expect(jpegSize(new Uint8Array([]))).toBe(null)
    expect(jpegSize(new Uint8Array([0xff, 0xd8]))).toBe(null) // truncated to the SOI alone
  })

  it('agrees with a real Flow-generated JPEG', () => {
    // The one test that proves the parser against reality rather than against my own fixture.
    // Path is relative to the PACKAGE (vitest's cwd), not the repo root — as repo-root paths
    // it silently existsSync-ed to false and the test asserted nothing at all.
    const real = '../../docs/images/register-anchor.jpg'
    expect(existsSync(real)).toBe(true)
    expect(jpegSize(readFileSync(real))).toEqual({ width: 1376, height: 768 })
  })
})
