/**
 * `@badcode/enc` — everything specific to Emperor's New Coin that both the
 * simulation and (later) the website need.
 *
 * **It lives here rather than in `@badcode/chain-kit` on purpose.** The kit is
 * copied wholesale into unrelated projects and may not know that this coin
 * exists; see the portability contract in `chain/README.md`, which T23 enforces
 * by grep. Nothing depends on this package except the ENC page, the `enc` CLI
 * sub-group and the economic simulation.
 */
export * from './math.js'
