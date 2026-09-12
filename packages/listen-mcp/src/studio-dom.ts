/**
 * AI Studio chat-page selectors. Every constant here was read off the live page on 2026-09-11
 * (listen-mcp T3) and the evidence is in `docs/listening/automation.md` §2 — that file is the
 * source of truth, this one is its machine-readable half.
 *
 * 🔴 No logic lives here. The routines are in `studio-client.ts`, and none of them asks a model
 * to read the page: fixed routines against a known map are fast and reliable, a model inspecting
 * the DOM is neither (the lesson from Flow automation).
 */

/** Per-tab marker, so we never drive a tab Jack is using. Mirrors `scripts/suno/suno.mts`. */
export const TAB_MARK = '__badcode_listen_tab'

export const HOST = 'aistudio.google.com'
export const NEW_CHAT_URL = `https://${HOST}/prompts/new_chat`
/** Adding `?model=<id>` preselects a model — observed rewriting to this on a menu pick. */
export const newChatUrlFor = (modelId: string) => `${NEW_CHAT_URL}?model=${encodeURIComponent(modelId)}`

/** The signed-out landing page is on the SAME host, so a host match proves nothing (Trap 3). */
export const SIGNED_OUT_PATH = '/welcome'

export const SEL = {
  /** Text reads e.g. `jacktttt330@gmail.com ULTRA`. */
  account: 'button.account-switcher-button',
  newChat: 'button[aria-label="New chat"]',
  /** Its `span.title` is the current model's shown name; first `span.subtitle` is the model id. */
  modelCard: 'button.model-selector-card',
  modelCardTitle: 'span.title',
  modelCardSubtitle: 'span.subtitle',
  /** Rows in the open model menu; `.model-title-text` carries the visible name. */
  modelRow: 'ms-model-carousel-row button.content-button',
  modelRowTitle: '.model-title-text',
  /** 🔴 ON by default on every new chat (Trap 2). */
  groundingSwitch: 'button[role="switch"][aria-label="Grounding with Google Search"]',
  groundingChipRemove: 'button[aria-label="Remove Grounding with Google Search"]',
  temperature: 'input[aria-label="Temperature"]',
  thinkingLevel: 'mat-select[aria-label="Thinking Level"]',
  /** Hidden input — set it directly. Never the OS chooser. */
  fileInput: 'ms-add-media-button input.file-input[type="file"]',
  addMediaButton: 'button[data-test-id="add-media-button"]',
  /** Shows `<file name>` + `<N> tokens` once processed — the token count IS the ready signal. */
  mediaChip: 'ms-prompt-box ms-prompt-media',
  promptBox: 'textarea[aria-label="Enter a prompt"]',
  runButton: 'ms-run-button button',
  chatTurn: 'ms-chat-turn',
  userTurn: '[data-turn-role="User"]',
  modelTurn: '[data-turn-role="Model"]',
  moreActions: 'button[aria-label="View more actions"]',
  dialogButton: 'mat-dialog-container button',
} as const

/** Menu-item and dialog-button labels, matched on visible text. */
export const TEXT = {
  temporaryChat: 'Temporary chat',
  /** Trap 5 — the first-ever upload on an account opens a rights reminder. */
  acknowledge: 'Acknowledge',
  /** Trap 6 — New chat confirms before discarding the current prompt. */
  discardAndContinue: 'Discard and continue',
} as const

/** Default model, by the name the menu shows. Overridable with LISTEN_MODEL. */
export const DEFAULT_MODEL = 'Gemini 3.1 Pro'

/**
 * Page-state classification, in priority order. `classifyPage` in `studio-client.ts` applies
 * these to the visible text of the last model turn plus the URL.
 *
 * 🔴 `An internal error has occurred.` is the UI face of the 403 that blocked T3
 * (`The caller does not have permission`) — raised as STUDIO_ERROR so a caller can tell it from
 * a timeout, which is the mistake that cost the most time in Flow automation.
 */
export const PAGE_SIGNS: ReadonlyArray<{ state: 'rate-limited' | 'error'; re: RegExp }> = [
  { state: 'rate-limited', re: /resource has been exhausted|quota|rate limit|too many requests|try again later/i },
  { state: 'error', re: /an internal error has occurred|caller does not have permission|permission denied|something went wrong|failed to create interaction/i },
]
