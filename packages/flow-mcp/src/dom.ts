import { isMediaSrc, parseMediaName } from './media-url'
import type { CanvasImg } from './canvas'

/**
 * Raw <img> descriptor as scraped from the page in a browser-context eval.
 *
 * TWO sizes, and the distinction is load-bearing. `width`/`height` are the ON-SCREEN box, which
 * is what canvas selection wants (the biggest thing on screen is the active canvas, and a
 * thumbnail of the same media is smaller). `naturalWidth`/`naturalHeight` are the IMAGE's own
 * pixels, which is what a caller means by "how big is the picture".
 *
 * Conflating them was a real bug: every image tool reported the rendered box, so a batch of
 * genuine 1376x768 images came back claiming to be 537x300 (caught 2026-08-12 by running
 * `file` on the output). The ratio survived, which is why aspect assertions never noticed.
 */
export interface RawImg {
  src: string
  width: number
  height: number
  naturalWidth?: number
  naturalHeight?: number
}

/** The function string evaluated inside the page to scrape generated <img>s. */
export const SCRAPE_IMGS = `() => [...document.querySelectorAll('img')].map(im => ({
  src: im.currentSrc || im.src || '',
  width: im.getBoundingClientRect().width,
  height: im.getBoundingClientRect().height,
  naturalWidth: im.naturalWidth,
  naturalHeight: im.naturalHeight,
}))`

/** Map raw scraped imgs to media CanvasImgs (filter non-media, parse names). */
export function toCanvasImgs(raw: RawImg[]): CanvasImg[] {
  const out: CanvasImg[] = []
  for (const im of raw) {
    if (!isMediaSrc(im.src)) continue
    const name = parseMediaName(im.src)
    if (!name) continue
    // Natural size when the image has decoded, else fall back to the rendered box — a
    // not-yet-decoded <img> reports naturalWidth 0, and reporting 0x0 would be worse than
    // reporting the box. Selection uses `width`/`height`; only reporting uses `natural*`.
    out.push({
      name,
      width: im.width,
      height: im.height,
      naturalWidth: im.naturalWidth || im.width,
      naturalHeight: im.naturalHeight || im.height,
    })
  }
  return out
}
