/**
 * Gemini hears only the cut range, so its timestamps count from the start of the cut. Shift them
 * back to source time, so "the drop at 0:05" in a clip cut from 1:20 reads "1:25" — the time a
 * human would scrub to.
 */

/** 85 → '1:25'; 3725 → '1:02:05'. Fractions are rounded to the nearest second. */
export function formatTime(sec: number): string {
  const total = Math.max(0, Math.round(sec))
  const h = Math.floor(total / 3600)
  const m = Math.floor((total % 3600) / 60)
  const s = total % 60
  const ss = String(s).padStart(2, '0')
  return h > 0 ? `${h}:${String(m).padStart(2, '0')}:${ss}` : `${m}:${ss}`
}

/**
 * H:MM:SS or M:SS / MM:SS, two-digit seconds, optional fraction. `4:4` and `12:3` never match
 * (seconds must be two digits); `3:75` matches the shape but is rejected below (seconds ≥ 60).
 */
const TIME_RE = /\b(?:(\d+):)?(\d{1,2}):(\d{2})(\.\d+)?\b/g

export function remapTimestamps(text: string, offsetSec: number): { text: string; count: number } {
  let count = 0
  const out = text.replace(TIME_RE, (token, h: string | undefined, m: string, s: string, frac: string | undefined) => {
    if (Number(s) >= 60 || (h !== undefined && Number(m) >= 60)) return token
    count++
    if (offsetSec === 0) return token
    const sec = (h ? Number(h) * 3600 : 0) + Number(m) * 60 + Number(s) + (frac ? Number(frac) : 0)
    const shifted = sec + offsetSec
    // Keep a fraction only when the answer gave one — then keep its precision.
    if (!frac) return formatTime(shifted)
    const whole = Math.floor(shifted)
    const f = (shifted - whole).toFixed(frac.length - 1).slice(1)
    return formatTime(whole) + f
  })
  return { text: out, count }
}
