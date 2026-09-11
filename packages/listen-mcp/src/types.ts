/**
 * Types shared across listen-mcp's modules, kept in one file so each module can be built and
 * tested without the others existing yet.
 */

/** A cut of the source file, in seconds of SOURCE time. */
export interface Range {
  start: number
  end: number
}

/**
 * What `scripts/audio-measure.py` reports. Keys are exactly these (camelCase) — the Python side
 * writes them verbatim.
 *
 * Stereo fields are recorded but never sent to Gemini: its audio path mixes to mono and
 * downsamples to 16 kbps (ai.google.dev/gemini-api/docs/audio), so it cannot judge width.
 */
export interface Measurements {
  durationSec: number
  integratedLufs: number | null
  truePeakDbtp: number | null
  loudnessRangeLu: number | null
  channels: number
  /** null when channels === 1 OR either channel has zero variance. */
  stereoCorrelation: number | null
  /** null when channels === 1 or both M and S are silent; else clamped to [-120, 120]. */
  sideToMidDb: number | null
  spectralCentroidHz: number
  tempo: { bpm: number | null; confidence: 'high' | 'fair' | 'tempo-only' | 'unverified' | 'none' }
}

/** A listening checklist, loaded from `docs/listening/lenses/<name>.md`. */
export interface Lens {
  name: string
  description: string
  body: string
  /** Every `## ` heading in the body, in order — the headings the answer must use. */
  headings: string[]
  /** sha256 of the file, first 12 hex chars. */
  hash: string
}

export interface DescribeArgs {
  /** Linux or Windows path (D:\x\y.mp3 or /mnt/d/x/y.mp3). */
  path: string
  /** Default 'music'; must match a file in docs/listening/lenses/. */
  lens?: string
  /** Seconds or "M:SS" / "H:MM:SS", source time. */
  start?: string | number
  end?: string | number
  /** Appended verbatim after the lens checklist. */
  question?: string
  /** Visible model-menu name; default LISTEN_MODEL ?? 'Gemini 3.1 Pro'. */
  model?: string
}

export interface DescribeResult {
  description: string
  measurements: Measurements
  modelShown: string
  lens: string
  range: Range | null
  sha256: string
  /** Repo-relative. */
  ledgerPath: string
  /** true iff range !== null && range.start > 0 && remapTimestamps(...).count > 0 */
  remapped: boolean
}
