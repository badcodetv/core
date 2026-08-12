/**
 * Who shows up, and how often.
 *
 * **Deterministic on purpose.** Nothing here calls `Math.random`: a simulation
 * that picks the parameters a non-upgradeable program ships with has to give
 * the same answer twice, or "the sweep said so" means nothing. Anything that
 * needs to look irregular uses a seeded generator whose seed is in the code.
 */

/** A small, boring, reproducible generator. Mulberry32. */
export function seeded(seed: number): () => number {
  let a = seed >>> 0
  return () => {
    a = (a + 0x6d2b79f5) >>> 0
    let t = a
    t = Math.imul(t ^ (t >>> 15), t | 1)
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

export interface Cohort {
  name: string
  /** The wallet names this cohort claims with. */
  wallets: string[]
  /** Whether a given wallet claims in a given epoch. */
  claimsIn(epoch: number, wallet: string): boolean
  /** Whether it spends everything it can on the cheapest tenancy. */
  buys: boolean
}

/**
 * One wallet that claims every single epoch and never spends a thing.
 *
 * This is the measuring instrument, not a prediction. **Time-to-first-asset**
 * is T13's pass/fail carried into T15: Ruling C made the faucet the only route
 * into the economy that BadCode controls, so if the most diligent possible
 * claimant can never reach the cheapest reserve, the loop does not close and
 * the artwork is a shop window.
 */
export function patient(name = 'patient'): Cohort {
  return { name, wallets: [name], claimsIn: () => true, buys: false }
}

/** Turns up when it remembers to. Colour, and a check that missing a day costs only that day. */
export function casual(count: number, chance = 0.35, seed = 0xc0ffee): Cohort {
  const rng = seeded(seed)
  // Precomputed so the answer does not depend on call order.
  const draws = new Map<string, number[]>()
  const wallets = Array.from({ length: count }, (_, i) => `casual-${i}`)
  for (const w of wallets) draws.set(w, Array.from({ length: 4_000 }, () => rng()))
  return {
    name: `casual×${count}`,
    wallets,
    claimsIn: (epoch, wallet) => (draws.get(wallet)?.[epoch % 4_000] ?? 1) < chance,
    buys: false,
  }
}

/**
 * A farm. Every wallet, every epoch, forever.
 *
 * The property it exists to demonstrate is that this **does not work**: the pot
 * is fixed when the epoch opens and divided by however many registered, so a
 * thousand wallets take a thousandth each and the vault loses exactly what it
 * would have lost to one. That bound is the entire reason ENC needs no identity
 * system, and it is why "requiring an iris scan to play a joke about the Fed"
 * was rejected.
 */
export function sybil(count: number): Cohort {
  return {
    name: `sybil×${count}`,
    wallets: Array.from({ length: count }, (_, i) => `sybil-${i}`),
    claimsIn: () => true,
    buys: false,
  }
}

/** Claims every epoch and buys a tenancy the moment it can afford one. */
export function collector(name = 'collector'): Cohort {
  return { name, wallets: [name], claimsIn: () => true, buys: true }
}

/**
 * Nobody. The dead-state test, which is the floor the whole artwork is judged
 * against: ten columns of the Emperor's own copy, priced, repricing every time
 * the Fed prints, and not one wallet in the world.
 */
export function nobody(): Cohort {
  return { name: 'nobody', wallets: [], claimsIn: () => false, buys: false }
}
