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

/// One live bid per (asset, bidder).
pub const BID_SEED: &[u8] = b"bid";

/// Holds every bidder's escrowed ENC.
///
/// **Deliberately not the vault.** `sync_m2` burns from the vault's token
/// account, so pooling escrow there would let an ordinary monetary contraction
/// destroy money that belongs to bidders — the exact stranding the auction's
/// acceptance criteria forbid, reached through a path nobody would think to
/// test. The Emperor's money and the players' money live in different pockets.
pub const ESCROW_SEED: &[u8] = b"escrow";

/// One tenancy certificate per (asset, term). The seeds are the "numbered and
/// dated" part: a term can only ever issue one, and it can never be reissued.
pub const CERT_SEED: &[u8] = b"cert";

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

/// One day. The unit the shipped economy is measured in.
pub const SECONDS_PER_DAY: i64 = 86_400;

/// The faucet epoch the coin ships with: one day. Register today, collect
/// tomorrow.
///
/// **This is the default, not the rule.** The live value is
/// `Config.epoch_seconds`, chosen once at `initialize` from
/// `params.genesis.json` and never changeable afterwards — because every
/// cross-epoch behaviour the faucet has (a pot divided among *yesterday's*
/// registrants, an epoch old enough to close) is unreachable in a test suite
/// that would have to wait a real day for it. The same reasoning made
/// `term_seconds` a field at T12.
///
/// The epoch index is a PDA seed, so this number decides which accounts exist.
/// That is safe only because it cannot move after genesis.
pub const DEFAULT_SECONDS_PER_EPOCH: i64 = SECONDS_PER_DAY;

/// How many bytes of copy one column holds. **Bytes, not characters** — an
/// emoji costs four of these and an accented letter costs two.
///
/// Two hundred and eighty, because the internet already argued this one out and
/// settled on it as the size of a stranger's opinion. It is enough for a
/// headline, a classified ad or a sentence of the serial, and small enough that
/// ten of them are still one cheap RPC read. The number is permanent — `Asset`
/// is fixed-size and the program ships non-upgradeable — so it is chosen for
/// what a column of a newspaper is, not for what a text field could be.
pub const COPY_BYTES: usize = 280;

/// What the editor's pen leaves behind. **The pen strikes words; it never
/// authors them**, so `spike` writes this and nothing else — there is no
/// caller-supplied text anywhere in it. BadCode does not get to write into a
/// column somebody paid for, and a redaction bar says more than a sentence
/// would.
pub const SPIKE_MARKER: &str = "███████ SPIKED ███████";

/// How long a price takes to travel to its new target after a supply change.
///
/// Rescaling every asset instantly would make prices jump on the Fed's
/// schedule; interpolating means they tick every slot, which is both truer to
/// "the money is melting continuously" and much better television.
///
/// Measured in **days, not epochs**: a test ledger runs short epochs, and a
/// price curve that shrank with them would leave every asset already arrived at
/// its target, quietly disabling the reserve the auction bids against.
pub const PRICE_INTERPOLATION_SECONDS: i64 = 30 * SECONDS_PER_DAY;

// ── Accounts ────────────────────────────────────────────────────────────────

/// The rules. Written once at `initialize`, never changed afterwards.
///
/// There is deliberately no instruction that mutates the economic parameters —
/// not gated behind an authority, not present at all — because the program ships
/// non-upgradeable and "not even we can change the rule" has to be literally
/// true, not merely intended.
///
/// Two fields here move without any key at all, and both are **one-way
/// latches**: `initialized_assets` counts up to ten during bootstrap and then
/// never moves again, and `retired` flips once, permissionlessly, when the
/// program has gone long enough without hearing a new M2 figure. Neither can be
/// set back, and neither is anyone's decision — the second is a condition the
/// program checks about itself.
///
/// One field here **is** a key: `editor`, the pen. It is the single exception in
/// the whole program and it is deliberately narrow — no key over the money, one
/// pen over the words. See its own doc for exactly what it can reach.
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

    /// Share of the distributable surplus paid out per epoch, in basis points.
    pub faucet_alpha_bps: u16,
    /// The vault's floor, in basis points of total supply. Below it the faucet
    /// pays nothing at all — no share, no welcome grant.
    pub floor_bps: u16,

    /// One-off payment to a wallet's first ever claim, in base units.
    pub welcome_grant: u64,
    /// How many welcome grants may be issued in a single epoch.
    pub grants_per_epoch: u16,

    /// How long one tenancy lasts, in seconds.
    ///
    /// Aligned with `PRICE_INTERPOLATION_SECONDS` on purpose: a term is exactly
    /// as long as it takes a price to finish travelling to its new target, so
    /// each auction settles against a price that has arrived rather than one
    /// still in motion.
    pub term_seconds: i64,

    /// How long one faucet epoch lasts, in seconds. One day in the shipped
    /// parameters; see `DEFAULT_SECONDS_PER_EPOCH` for why it is a field.
    ///
    /// It is a **PDA seed input**, so it decides which `FaucetEpoch` accounts
    /// can ever exist. Fixed at genesis and without a setter, like everything
    /// else here.
    pub epoch_seconds: i64,

    /// How long the program must go without a new M2 figure before anyone may
    /// `retire` it, in seconds. A year in the shipped parameters.
    ///
    /// Long on purpose: the flag is irreversible on a non-upgradeable program,
    /// so a Switchboard outage or a bad month must never be able to end the
    /// artwork. M2 publishes monthly; a year is twelve missed chances.
    pub retirement_silence_seconds: i64,

    /// How far the peg will move in one `sync_m2`, in basis points.
    ///
    /// **A speed limit, not a veto** (T29). A release beyond it is absorbed
    /// over several permissionless calls rather than refused — refusing it was
    /// permanent, because the baseline only advances on success. There is
    /// deliberately no companion cap in absolute base units: any fixed number
    /// of tokens is exceeded by an ordinary month once M2 has grown enough, and
    /// on a non-upgradeable program that is a timer, not a guard.
    pub max_change_bps: u16,

    /// Counts up to `ASSET_COUNT` during bootstrap, then never moves.
    pub initialized_assets: u8,

    /// Whether the coin has noticed its own end. One-way, and nobody's
    /// decision: `retire` sets it when the silence condition is already true,
    /// and no instruction anywhere can set it back.
    ///
    /// The **only** thing it stops is `sync_m2`. Everything else keeps running
    /// on the last prices the Fed ever reported — the machine grinding on,
    /// auctioning flags at the valuations of a vanished world. That also
    /// removes the one hazard a freeze would have carried: escrow that can
    /// never be withdrawn.
    pub retired: bool,

    /// The editor's pen: the one key in this program, and it can only strike
    /// words.
    ///
    /// It reaches exactly one instruction, `spike`, which replaces a column's
    /// copy with `SPIKE_MARKER` — a fixed string it does not get to choose —
    /// once per column per term. **The blast radius is ten columns a month, and
    /// it cannot move a token.** Not one ENC, not one asset NFT, not one
    /// certificate; the shape test in `initialize.ts` asserts the key appears in
    /// no instruction that touches a token account.
    ///
    /// It exists because there is no on-chain answer to vile text and
    /// pretending otherwise is how this gets ugly. A newspaper has an editor.
    ///
    /// `Some` while a pen exists, `None` once `break_the_pen` has been called —
    /// which is irrevocable, because `pass_the_pen` needs a current editor to
    /// sign and nothing else writes this field. Rotatable on purpose: a lost or
    /// stolen key must be survivable without an upgrade authority to fall back
    /// on, since by T22 there will not be one.
    pub editor: Option<Pubkey>,
    pub bump: u8,
}

impl Config {
    /// Prove the signer holds the pen, distinguishing "there is no pen" from
    /// "you are not the editor" — a broken pen is a permanent fact about the
    /// paper and a caller deserves to be told which of the two happened.
    pub fn require_editor(&self, signer: &Pubkey) -> Result<()> {
        let editor = self.editor.ok_or(error!(crate::errors::EncError::PenBroken))?;
        require_keys_eq!(editor, *signer, crate::errors::EncError::NotTheEditor);
        Ok(())
    }
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
    /// Unix seconds of the last successful sync — **our** clock, not the Fed's.
    ///
    /// This is the retirement clock, and it has to be wall time rather than the
    /// slot beside it: a program cannot convert a slot into a date, so
    /// `last_sync_slot` can never answer "how long has it been". Seeded at
    /// `initialize` rather than left at zero, or the coin would be a year
    /// overdue for retirement the moment it was born.
    ///
    /// It advances only on a **successful** sync, which is what makes silence
    /// mean silence: a feed still serving a dead series fails the release-date
    /// guard, this clock stops, and `retire` becomes true on schedule.
    pub last_sync_at: i64,
    /// `k × m2_value` at the last sync — what supply was aimed at.
    ///
    /// Actual supply can sit *above* this, when a burn was larger than the
    /// vault could cover. That is the honest invariant: `supply ≥ k × M2`.
    pub target_supply: u64,
    pub bump: u8,
}

/// One of the ten parody assets: a Token-2022 NFT, held for a term.
///
/// The NFT itself never leaves program custody — this account records who holds
/// the *tenancy*, and the holder's own wallet gets a certificate instead. That
/// is what lets settlement be permissionless without a permanent delegate:
/// there is no wallet to reach into.
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

    /// Which tenancy this is. Starts at 0 (the Emperor's own) and increments at
    /// every settlement, whether or not the asset changed hands.
    ///
    /// It does two jobs beyond counting: it numbers the certificate, and it is
    /// what makes a bid *stale* — a bid placed in an earlier term is no longer
    /// live, so its escrow is always withdrawable.
    pub term_number: u64,
    /// When the current tenancy ends and anyone may settle it.
    ///
    /// Replaces T7's `last_touched`, which was the rent clock. Nothing else
    /// needed "when was this last written" — the price curve carries its own
    /// window — so an explicit term end is the honest field.
    pub term_ends_at: i64,

    /// The standing high bid, in base units. Zero means nobody has bid.
    pub high_bid: u64,
    /// Who placed it. The default (all-zero) key when there is no high bid.
    ///
    /// A bid is *locked* only while it is both the standing high bid and from
    /// the current term; everything else is withdrawable by its owner alone.
    pub high_bidder: Pubkey,

    /// What this column currently says. UTF-8, left-aligned, zero-padded.
    ///
    /// **It persists across settlement.** A new tenancy does not blank the page
    /// — yesterday's news stands until today's edition is filed, so a column
    /// nobody writes in keeps saying whatever it last said, for as long as that
    /// takes. Only `file_copy` and `spike` ever write here.
    pub copy: [u8; COPY_BYTES],

    /// How many of `copy`'s bytes are real.
    ///
    /// Carried explicitly rather than left for the client to find, because
    /// "read until the first zero byte" is a guess: nothing stops a tenant
    /// filing a NUL, and the array is zero-padded either way. Zero means the
    /// column has never been written and the page should render the Emperor's
    /// own default copy — which is what every slot looks like at genesis and
    /// what the vault-held ones look like forever.
    pub copy_len: u16,

    /// Whether this term's copy has been filed. **Once per term, write-once.**
    ///
    /// Not a rate limit — a decision. Unlimited rewrites would turn moderation
    /// into a war of attrition that only a bot BadCode ran forever could win,
    /// which puts us back in the loop as an operational dependency. One filing
    /// per term makes the pen decisive instead.
    pub copy_filed: bool,

    /// Whether the editor has struck this column this term. Blocks a second
    /// spike, and blocks a re-file: a spiked column stays struck until the term
    /// rolls, or the pen would just be the opening move of that same war.
    pub copy_spiked: bool,

    pub bump: u8,
}

impl Asset {
    /// Overwrite the column, zero-padding the rest. The one place `copy` and
    /// `copy_len` are written, so the two cannot disagree.
    pub fn write_copy(&mut self, bytes: &[u8]) -> Result<()> {
        require!(
            bytes.len() <= COPY_BYTES,
            crate::errors::EncError::CopyTooLong
        );
        self.copy = [0u8; COPY_BYTES];
        self.copy[..bytes.len()].copy_from_slice(bytes);
        self.copy_len = bytes.len() as u16;
        Ok(())
    }

    /// Clear the per-term flags without touching a byte of the copy. Called at
    /// every settlement and every rollover — the edition changes, the page does
    /// not go blank.
    pub fn open_a_new_edition(&mut self) {
        self.copy_filed = false;
        self.copy_spiked = false;
    }
}

/// One bidder's escrowed ENC on one asset.
///
/// The escrow itself pools in a single token account; this records who is owed
/// what. Keyed by (asset, bidder), so a wallet has at most one live bid per
/// asset and the accounting cannot drift from the pool.
#[account]
#[derive(InitSpace)]
pub struct Bid {
    pub asset_index: u8,
    pub bidder: Pubkey,
    /// Base units sitting in escrow against this bid.
    pub amount: u64,
    /// The term this bid was placed in. Once the asset moves past it, the bid
    /// is dead and the money is the bidder's to take back.
    pub term_number: u64,
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

pub fn escrow_seeds() -> [&'static [u8]; 1] {
    [ESCROW_SEED]
}

/// One-byte index then the raw bidder key, matching `asset_seeds`' convention.
pub fn bid_seeds(index: u8, bidder: &Pubkey) -> [Vec<u8>; 3] {
    [BID_SEED.to_vec(), vec![index], bidder.to_bytes().to_vec()]
}

/// One-byte index then a **little-endian u64** term, matching `epoch_seeds`.
pub fn cert_seeds(index: u8, term: u64) -> [Vec<u8>; 3] {
    [
        CERT_SEED.to_vec(),
        vec![index],
        term.to_le_bytes().to_vec(),
    ]
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

    /// A blank `Asset` for the copy cases. `Default` is not derived on the
    /// account struct, so build it here rather than adding a trait the program
    /// never uses.
    fn blank_asset() -> Asset {
        Asset {
            index: 0,
            holder: Pubkey::default(),
            price_from: 0,
            price_to: 0,
            interp_start: 0,
            interp_end: 0,
            term_number: 0,
            term_ends_at: 0,
            high_bid: 0,
            high_bidder: Pubkey::default(),
            copy: [0u8; COPY_BYTES],
            copy_len: 0,
            copy_filed: false,
            copy_spiked: false,
            bump: 0,
        }
    }

    /// The size is permanent — `Asset` is created with `init` and the program
    /// ships non-upgradeable, so this number is chosen once and lives with the
    /// coin. Pinned so that growing the struct is a deliberate act with a
    /// failing test in front of it, not something noticed at deploy time.
    #[test]
    fn the_asset_account_is_the_size_we_think_it_is() {
        // 1 index + 32 holder + 4×8 curve + 8 term + 8 term_ends_at
        // + 8 high_bid + 32 high_bidder + 280 copy + 2 copy_len + 2 flags + 1 bump
        assert_eq!(Asset::INIT_SPACE, 1 + 32 + 32 + 8 + 8 + 8 + 32 + 280 + 2 + 2 + 1);
        assert_eq!(8 + Asset::INIT_SPACE, 414);
    }

    /// Zero-padding plus an explicit length, rather than a NUL terminator:
    /// nothing stops a tenant filing a zero byte, so scanning for one would
    /// truncate their column and call it a feature.
    #[test]
    fn copy_is_zero_padded_and_its_length_is_recorded() {
        let mut a = blank_asset();
        a.write_copy(b"there is no magic money tree").unwrap();
        assert_eq!(a.copy_len as usize, 28);
        assert_eq!(&a.copy[..28], b"there is no magic money tree");
        assert!(a.copy[28..].iter().all(|b| *b == 0));

        // A shorter second filing must not leave the tail of the first behind.
        a.write_copy(b"no").unwrap();
        assert_eq!(a.copy_len, 2);
        assert_eq!(&a.copy[..2], b"no");
        assert!(a.copy[2..].iter().all(|b| *b == 0));

        // An embedded NUL survives, which is the whole reason for copy_len.
        a.write_copy(b"a\0b").unwrap();
        assert_eq!(a.copy_len, 3);
        assert_eq!(&a.copy[..3], b"a\0b");
    }

    #[test]
    fn copy_refuses_more_than_it_can_hold() {
        let mut a = blank_asset();
        assert!(a.write_copy(&[b'x'; COPY_BYTES]).is_ok());
        assert!(a.write_copy(&[b'x'; COPY_BYTES + 1]).is_err());
        // The refused write changed nothing.
        assert_eq!(a.copy_len as usize, COPY_BYTES);
    }

    /// The marker has to fit in the field it replaces, or the pen would fail on
    /// exactly the column it was reached for. Block characters are three bytes
    /// each, which is easy to forget.
    #[test]
    fn the_spike_marker_fits_in_a_column() {
        assert!(SPIKE_MARKER.len() <= COPY_BYTES);
        let mut a = blank_asset();
        a.write_copy(SPIKE_MARKER.as_bytes()).unwrap();
        assert_eq!(
            std::str::from_utf8(&a.copy[..a.copy_len as usize]).unwrap(),
            SPIKE_MARKER
        );
    }

    /// Copy persists across settlement; only the flags reset. Yesterday's news
    /// stands until today's edition is filed.
    #[test]
    fn a_new_edition_clears_the_flags_and_not_the_page() {
        let mut a = blank_asset();
        a.write_copy(b"the emperor has no clothes").unwrap();
        a.copy_filed = true;
        a.copy_spiked = true;

        a.open_a_new_edition();

        assert!(!a.copy_filed);
        assert!(!a.copy_spiked);
        assert_eq!(&a.copy[..a.copy_len as usize], b"the emperor has no clothes");
    }

    #[test]
    fn player_seed_is_the_raw_32_byte_key() {
        let wallet = crate::ID;
        assert_eq!(player_seeds(&wallet)[1], wallet.to_bytes().to_vec());
        assert_eq!(player_seeds(&wallet)[1].len(), 32);
    }
}
