/** Flow serves generated media via an authenticated same-origin redirect endpoint. */
const REDIRECT_BASE = 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect'

/** True if a URL or <img> src points at Flow's media redirect endpoint. */
export function isMediaSrc(src: string): boolean {
  return src.includes('getMediaUrlRedirect')
}

/** Pull the `name` query param (the media UUID) out of a redirect URL or img src. */
export function parseMediaName(src: string): string | null {
  const match = src.match(/[?&]name=([^&]+)/)
  return match ? decodeURIComponent(match[1]) : null
}

/** Build the authenticated redirect URL for a media name. */
export function mediaRedirectUrl(name: string): string {
  return `${REDIRECT_BASE}?name=${name}`
}

/**
 * The media UUID inside a signed original URL — `https://flow-content.google/video/<uuid>?Expires=…`
 * (or `/image/<uuid>`). That is what the rebuilt app's Download fetches, so a download's own URL
 * names the media even though no tile carries the id for a video. Null for anything else.
 */
export function mediaIdFromContentUrl(url: string): string | null {
  const m = /flow-content\.google\/(?:video|image)\/([0-9a-f-]{36})/i.exec(url)
  return m ? m[1]! : null
}
