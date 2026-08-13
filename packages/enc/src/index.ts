/**
 * `@badcode/enc` — everything specific to Emperor's New Coin that both the
 * simulation and the website need.
 *
 * **It lives here rather than in `@badcode/chain-kit` on purpose.** The kit is
 * copied wholesale into unrelated projects and may not know that this coin
 * exists; see the portability contract in `chain/README.md`, which T23 enforces
 * by grep. Nothing depends on this package except the ENC page, the `enc` CLI
 * sub-group and the economic simulation.
 *
 * Four layers, and the order is the dependency order:
 *
 * - `math` — the program's arithmetic, mirrored function for function. The
 *   source of truth is `math.rs`; if the two disagree, the Rust is right.
 * - `idl` / `accounts` — the program's interface and where its state lives.
 * - `view` — decoded accounts plus a timestamp, assembled into what the page
 *   renders. Composes `math`; never re-derives it.
 * - `format` / `h6` — printing numbers, and when the Fed next speaks.
 */
export * from './math.js'
export * from './accounts.js'
export * from './view.js'
export * from './format.js'
export * from './h6.js'
export { ENC_IDL, ENC_PROGRAM_ID, type EmperorsNewCoin } from './idl/emperors_new_coin.js'
