//! On-chain state, and the seeds that locate it.
//!
//! **The seeds are a cross-language contract.** `packages/chain-kit` derives the
//! same addresses in TypeScript, and `pda.test.ts` pins three of them as literal
//! base58 strings. If a seed here changes, the client looks in a place nothing
//! was ever written to and every account read comes back empty — which presents
//! as "the coin has no state", not as an error. The unit tests at the bottom of
//! this file assert the same three addresses from the Rust side, so the two
//! languages cannot drift apart silently.
use anchor_lang::prelude::*;

// ── Seeds ───────────────────────────────────────────────────────────────────
// Byte-for-byte identical to the table in the plan's Interfaces section, and to
// packages/chain-kit/src/pda.ts.

pub const CONFIG_SEED: &[u8] = b"config";
pub const PRINTER_SEED: &[u8] = b"printer";
pub const VAULT_SEED: &[u8] = b"vault";
pub const ASSET_SEED: &[u8] = b"asset";
pub const EPOCH_SEED: &[u8] = b"epoch";
pub const PLAYER_SEED: &[u8] = b"player";

/// The ENC mint itself is a PDA, so a client can find the coin without first
/// reading `Config` — and so no deployer keypair ever holds the mint.
pub const MINT_SEED: &[u8] = b"mint";

/// One NFT mint per asset. Also a PDA, so the program can sign for it.
pub const ASSET_MINT_SEED: &[u8] = b"asset_mint";

/// Six. Nine would overflow: ~2.21e10 whole ENC at 9 decimals is 2.21e19 base
/// units, past `u64::MAX` (1.845e19). Six leaves ~830× headroom. Fixed by the
/// arithmetic, not a parameter anyone gets to choose.
pub const ENC_DECIMALS: u8 = 6;

/// M2SL at the time this program was written, in billions of USD at 6dp.
///
/// Only ever used to bootstrap the supply at `initialize`, so the coin exists
/// before the first oracle read. The first real `sync_m2` retargets against the
/// published figure and corrects whatever this was — level-targeting means a
/// stale genesis costs one mint or burn, not a permanent error.
pub const GENESIS_M2_VALUE: u64 = 22_176_100_000;

/// How many parody assets exist. Fixed forever: scarcity of the flags is the
/// point, and `sync_m2` refuses to run until all ten are real.
pub const ASSET_COUNT: u8 = 10;

/// One epoch is one day. The faucet's whole rhythm — register today, collect
/// tomorrow — is measured in these.
pub const SECONDS_PER_EPOCH: i64 = 86_400;

/// How long a price takes to travel to its new target after a supply change.
///
/// Rescaling every asset instantly would make prices jump on the Fed's
/// schedule; interpolating means they tick every slot, which is both truer to
/// "the money is melting continuously" and much better television.
pub const PRICE_INTERPOLATION_SECONDS: i64 = 30 * SECONDS_PER_EPOCH;

// ── Accounts ────────────────────────────────────────────────────────────────

/// The rules. Written once at `initialize`, never changed afterwards.
///
/// There is deliberately no instruction that mutates the economic parameters —
/// not gated behind an authority, not present at all — because the program ships
/// non-upgradeable and "not even we can change the rule" has to be literally
/// true, not merely intended. The single exception is `initialized_assets`,
/// which counts up to ten during bootstrap and then never moves again.
#[account]
#[derive(InitSpace)]
pub struct Config {
    /// The ENC mint. Classic SPL, 6 decimals, freeze authority `None`.
    pub mint: Pubkey,
    /// The vault PDA — mint authority, landlord, and the Emperor's pocket.
    pub vault: Pubkey,
    /// The Switchboard feed this program will accept a quote from, and only
    /// this one. A feed *is* the hash of its own fetch job, so pinning the hash
    /// pins the data source itself: no key exists that could repoint it.
    pub expected_feed_id: [u8; 32],

    /// Base units of ENC per unit of `m2_value`. `supply = k × m2_value`.
    pub k: u64,
    /// Decimals on the mint. Six: nine would overflow u64 at this supply.
    pub enc_decimals: u8,

    /// Daily rent on a held asset, in basis points of its current price.
    pub rent_rate_per_day_bps: u16,
    /// Share of the distributable surplus paid out per epoch, in basis points.
    pub faucet_alpha_bps: u16,
    /// The vault's floor, in basis points of total supply. Below it the faucet
    /// pays nothing at all — no share, no welcome grant.
    pub floor_bps: u16,

    /// One-off payment to a wallet's first ever claim, in base units.
    pub welcome_grant: u64,
    /// How many welcome grants may be issued in a single epoch.
    pub grants_per_epoch: u16,

    /// How long an unpayable rent debt may stand before anyone may foreclose.
    pub grace_seconds: i64,
    /// Paid from the vault to whoever forecloses, in base units.
    pub foreclose_bounty: u64,

    /// Largest M2 move, in basis points, this program will believe in one
    /// release.
    pub max_change_bps: u16,
    /// Largest mint, in base units, this program will perform in one sync.
    pub max_single_mint: u64,

    /// Counts up to `ASSET_COUNT` during bootstrap. The only mutable field.
    pub initialized_assets: u8,
    pub bump: u8,
}

/// What the Fed last told us, and what we did about it.
#[account]
#[derive(InitSpace)]
pub struct Printer {
    /// M2SL in **billions of USD, fixed-point with 6 decimals**.
    /// `22176.1` is stored as `22_176_100_000`. Getting this wrong by a factor
    /// of a thousand is the easiest catastrophic mistake available here.
    pub m2_value: u64,
    /// Unix seconds of the **Fed's release**, not of our sync. This is what the
    /// anti-double-mint guard compares, because it is the only timestamp an
    /// attacker cannot advance by waiting.
    pub m2_release_date: i64,
    /// Slot of the last successful sync. Informational.
    pub last_sync_slot: u64,
    /// `k × m2_value` at the last sync — what supply was aimed at.
    ///
    /// Actual supply can sit *above* this, when a burn was larger than the
    /// vault could cover. That is the honest invariant: `supply ≥ k × M2`.
    pub target_supply: u64,
    pub bump: u8,
}

/// One of the ten parody assets: a Token-2022 NFT, always for sale.
#[account]
#[derive(InitSpace)]
pub struct Asset {
    pub index: u8,
    /// Who holds it. Equal to the vault PDA when the Emperor holds it — the
    /// client renders that case as "unowned". A sentinel rather than an
    /// `Option` so the account layout is fixed-size and the two cases cost the
    /// same to read.
    pub holder: Pubkey,

    /// Price interpolation: `price_from` at `interp_start`, `price_to` at
    /// `interp_end`, straight line between, flat outside. Every supply change
    /// rescales both endpoints and restarts the window, so the displayed price
    /// moves every slot rather than jumping once a month.
    pub price_from: u64,
    pub price_to: u64,
    pub interp_start: i64,
    pub interp_end: i64,

    /// Rent charged but not yet paid, in base units.
    pub rent_accrued: u64,
    /// When rent was last settled or the holder last changed. Rent is computed
    /// from here on read — no crank, and no iterating over accounts.
    pub last_touched: i64,
    pub bump: u8,
}

/// One day of the faucet.
///
/// Created by whoever claims first that day, which is also what snapshots the
/// pot. Everyone who registers today divides *today's* pot tomorrow.
#[account]
#[derive(InitSpace)]
pub struct FaucetEpoch {
    pub epoch: u64,
    /// `α × max(0, vault − floor × supply)`, frozen at creation. Frozen because
    /// a pot that moved with the vault balance could not be divided fairly
    /// among a set of registrants that is still growing.
    pub pot: u64,
    /// How many wallets registered during this epoch. The divisor for this
    /// pot — *next* epoch.
    pub registrants: u32,
    /// Welcome grants issued during this epoch, capped at `grants_per_epoch`.
    pub grants_issued: u16,
    pub bump: u8,
}

/// A wallet that has played.
#[account]
#[derive(InitSpace)]
pub struct Player {
    pub wallet: Pubkey,
    /// The last epoch this wallet registered in.
    ///
    /// One field does two jobs: it rejects a second claim in the same epoch
    /// (`== current`), and it decides eligibility for the previous pot
    /// (`== current - 1`). Keeping them as one field means they cannot
    /// disagree.
    pub last_registered_epoch: u64,
    /// Whether the one-off welcome grant has been taken. Never resets.
    pub welcome_grant_taken: bool,
    pub bump: u8,
}

// ── Seed helpers ────────────────────────────────────────────────────────────
// Anchor's `seeds = [...]` constraints spell these out inline; these exist for
// the places that derive an address outside a constraint, and to give the tests
// below something to assert against.

pub fn config_seeds() -> [&'static [u8]; 1] {
    [CONFIG_SEED]
}

pub fn printer_seeds() -> [&'static [u8]; 1] {
    [PRINTER_SEED]
}

pub fn vault_seeds() -> [&'static [u8]; 1] {
    [VAULT_SEED]
}

/// The asset index is **one byte**, not a u64. A u64 seed would derive a
/// different, empty address — see the "seed types that look alike" test in
/// `pda.test.ts`.
pub fn asset_seeds(index: u8) -> [Vec<u8>; 2] {
    [ASSET_SEED.to_vec(), vec![index]]
}

/// The epoch is a **little-endian u64**, matching Rust's `to_le_bytes`.
pub fn epoch_seeds(epoch: u64) -> [Vec<u8>; 2] {
    [EPOCH_SEED.to_vec(), epoch.to_le_bytes().to_vec()]
}

pub fn player_seeds(wallet: &Pubkey) -> [Vec<u8>; 2] {
    [PLAYER_SEED.to_vec(), wallet.to_bytes().to_vec()]
}

#[cfg(test)]
mod tests {
    use super::*;

    /// These three addresses are pinned as literals in
    /// `packages/chain-kit/src/pda.test.ts`. Both sides assert the same strings
    /// against the same program id, so a change to either seed encoding fails
    /// here *and* there rather than producing a silently empty account.
    #[test]
    fn derives_the_addresses_the_typescript_client_expects() {
        let pid = crate::ID;

        let (config, _) = Pubkey::find_program_address(&config_seeds(), &pid);
        let (printer, _) = Pubkey::find_program_address(&printer_seeds(), &pid);
        let (vault, _) = Pubkey::find_program_address(&vault_seeds(), &pid);

        assert_eq!(config.to_string(), "DVrFUZxQNxLWM5Rwsk92sBQDmUNY4njHE4nri5d4cMdm");
        assert_eq!(printer.to_string(), "96PpBLCBHeWXUmCZ5YRdLFmBL75ZqJjMRWBoCarasJNY");
        assert_eq!(vault.to_string(), "BpAvBQGwMuVsPyaPmPUmSY4p1zrp3Wxd5P3SWsrEHZJH");
    }

    #[test]
    fn every_asset_index_gets_its_own_address() {
        let pid = crate::ID;
        let mut seen = std::collections::HashSet::new();
        for i in 0..ASSET_COUNT {
            let seeds = asset_seeds(i);
            let refs: Vec<&[u8]> = seeds.iter().map(|s| s.as_slice()).collect();
            let (addr, _) = Pubkey::find_program_address(&refs, &pid);
            assert!(seen.insert(addr), "asset {i} collided with an earlier index");
        }
    }

    /// A one-byte index and an eight-byte little-endian epoch are different
    /// seeds even for the same number. Confusing the two is the classic way to
    /// derive a valid-looking address that points at nothing.
    #[test]
    fn epoch_seeds_are_eight_bytes_little_endian() {
        assert_eq!(epoch_seeds(1)[1], vec![1, 0, 0, 0, 0, 0, 0, 0]);
        assert_eq!(epoch_seeds(256)[1], vec![0, 1, 0, 0, 0, 0, 0, 0]);
        assert_ne!(epoch_seeds(1)[1], vec![1u8]);
    }

    #[test]
    fn player_seed_is_the_raw_32_byte_key() {
        let wallet = crate::ID;
        assert_eq!(player_seeds(&wallet)[1], wallet.to_bytes().to_vec());
        assert_eq!(player_seeds(&wallet)[1].len(), 32);
    }
}
