/**
 * How a description actually gets fetched. Two transports, one interface.
 *
 * 🔴 This split exists because of a measured fact, not for neatness: AI Studio's web page refuses
 * every generation from a CDP-attached browser with `403 The caller does not have permission`,
 * while the same browser, profile and tab answer a human typing by hand. Ten variables were
 * eliminated one at a time — model, audio, prompt size, Temporary chat, grounding, our tab versus
 * the human's — see `docs/listening/automation.md` Trap 4b. We do not engineer around an
 * integrity check, so the browser path is **human-assisted only** and the API is the automated one.
 *
 * Everything else in this package is transport-independent: the lens, the prompt composer, the
 * local measurements, the timestamp remap and the ledger do not care where the text came from.
 */
export interface DescribeRequest {
  prompt: string
  /** An audio file Gemini can ingest. Omit for a text-only call (used by smoke tests). */
  audioPath?: string
  /** Model identifier — an API id, or a visible menu name for the browser transport. */
  model: string
}

export interface DescribeResponse {
  text: string
  /** What actually answered. Never assume the requested model is the one that replied. */
  modelShown: string
}

export interface Transport {
  /** Short name for the ledger and for error messages: 'api' | 'studio'. */
  readonly name: string
  run(req: DescribeRequest): Promise<DescribeResponse>
}
