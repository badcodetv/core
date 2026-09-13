import { describe, it, expect } from 'vitest'
import { toCanvasImgs } from './dom'

describe('toCanvasImgs', () => {
  it('keeps only media imgs and parses their names', () => {
    const raw = [
      { src: 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=aaa', width: 1376, height: 768 },
      { src: 'https://example.com/icon.svg', width: 24, height: 24 },
      { src: 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=bbb', width: 80, height: 80 },
    ]
    // No natural size on these inputs, so both sizes fall back to the rendered box.
    expect(toCanvasImgs(raw)).toEqual([
      { name: 'aaa', width: 1376, height: 768, naturalWidth: 1376, naturalHeight: 768 },
      { name: 'bbb', width: 80, height: 80, naturalWidth: 80, naturalHeight: 80 },
    ])
  })

  it('keeps the rendered box and the image\'s own size apart', () => {
    // The bug this guards: a genuine 1376x768 image displayed in a 537x300 box was reported
    // as 537x300 by every image tool, because only the box was ever scraped. Selection still
    // wants the box (biggest on screen = active canvas); callers want the picture's pixels.
    const raw = [
      {
        src: 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=aaa',
        width: 537,
        height: 300,
        naturalWidth: 1376,
        naturalHeight: 768,
      },
    ]
    expect(toCanvasImgs(raw)).toEqual([
      { name: 'aaa', width: 537, height: 300, naturalWidth: 1376, naturalHeight: 768 },
    ])
  })

  it('falls back to the box when the image has not decoded yet', () => {
    // A not-yet-decoded <img> reports naturalWidth 0; reporting 0x0 would be worse than the box.
    const raw = [
      {
        src: 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=aaa',
        width: 537,
        height: 300,
        naturalWidth: 0,
        naturalHeight: 0,
      },
    ]
    expect(toCanvasImgs(raw)).toEqual([
      { name: 'aaa', width: 537, height: 300, naturalWidth: 537, naturalHeight: 300 },
    ])
  })

  it('drops media imgs whose name fails to parse', () => {
    const raw = [{ src: 'getMediaUrlRedirect?notname=x', width: 10, height: 10 }]
    expect(toCanvasImgs(raw)).toEqual([])
  })

  // 2026-09-13 rebuild: the src is an opaque /asb/ token and the id lives on data-media-id.
  it('takes the id from data-media-id when the src carries none', () => {
    const raw = [
      { src: 'https://flow.google.com/asb/AB-nOUYw=s1600-rw', mediaId: '52213672-0b5d-4807-bea2-5ccd5fa66ba0', width: 530, height: 298, naturalWidth: 1376, naturalHeight: 768 },
      { src: 'https://www.gstatic.com/aitestkitchen/website/flow/icons/flow-music-icon.webp', width: 20, height: 20 },
    ]
    expect(toCanvasImgs(raw)).toEqual([
      { name: '52213672-0b5d-4807-bea2-5ccd5fa66ba0', width: 530, height: 298, naturalWidth: 1376, naturalHeight: 768 },
    ])
  })
})
