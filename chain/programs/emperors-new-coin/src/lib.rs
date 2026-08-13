//! Emperor's New Coin.
//!
//! Supply is pegged to the Fed's M2 money supply: when they print, we print.
//! Nobody, including us, can change that — the oracle feed is the hash of its
//! own fetch job, so no key exists that could repoint it, and this program
//! ships non-upgradeable.
//!
//! The machine, in one paragraph. A permissionless `sync_m2` reads the feed and
//! mints or burns against the vault so that `supply = k × M2`. Everything else
//! only moves tokens that already exist: ten parody assets — the ten slots of a
//! newspaper front page — reprice by whatever percentage M2 moved and are held
//! for a published term, changing hands by auction with the full winning bid
//! paid to the outgoing holder, while the vault drips a daily faucet back out
//! to anyone who shows up. The tenant of a slot writes its column, once per
//! term. The Fed decides how much money there is; the game decides who holds
//! it; and the price of speech rises at exactly the rate they print.
//!
//! **No key over the money; one pen over the words.** There is exactly one key
//! in this program — `Config.editor` — and it reaches exactly one instruction,
//! `spike`, which replaces a column's copy with a fixed marker it does not get
//! to choose, once per column per term. State the blast radius plainly: a
//! stolen pen can vandalise ten columns a month, and it cannot move a token.
//! Not one ENC, not one asset, not one certificate — `initialize.ts` asserts
//! that against the IDL rather than leaving it as a promise. It exists because
//! there is no on-chain answer to vile text and pretending otherwise is how
//! this gets ugly; a newspaper has an editor. It is rotatable
//! (`pass_the_pen` — after T22 there is no upgrade authority to recover a lost
//! key with) and breakable (`break_the_pen`, irrevocably). This was never a
//! decentralisation play: the trustless surface is the money, and every claim
//! about the money below survives verbatim.
//!
//! **There is no holding cost.** No rent, no demurrage, no fee. Holding ENC
//! already loses truthfully — the balance sits still while the assets reprice
//! away from it, which is what a peg to the printer *means* and what happens to
//! a wage. A carrying cost was built here and removed on 2026-08-12: at a rate
//! high enough to force turnover it made owning an asset a catastrophic loss,
//! inverting the joke the coin exists to tell.
//!
//! **It runs forever, with one exception it proves for itself.** If a full year
//! ever passes in which no new M2 figure reaches this program, anyone may call
//! `retire` — once, permanently, with no key consulted. That stops `sync_m2`
//! and nothing else: the auctions go on trading at the last prices the Fed ever
//! reported. The program cannot tell whether the dollar ended or everyone
//! stopped looking, and from where it sits those are the same event.
//!
//! The consequence to keep true as this grows: **no token leaves any wallet
//! without that wallet owner's signature.** Not the coin, not the columns, not
//! the certificates. The editor's pen does not weaken this by one clause: it
//! cannot reach a token account at all.
//!
//! See design/2026-08-06-solana-toolchain-and-emperors-new-coin.md.
use anchor_lang::prelude::*;

pub mod errors;
pub mod instructions;
pub mod math;
pub mod oracle;
pub mod state;

pub use errors::EncError;
pub use instructions::*;
pub use math::{PriceCurve, SupplyMove};
pub use oracle::Quote;
pub use state::*;

declare_id!("5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT");

#[program]
pub mod emperors_new_coin {
    use super::*;

    /// Create the mint, the vault, the rules and the printer. Once, ever, and
    /// only by the program's upgrade authority.
    pub fn initialize(ctx: Context<Initialize>, params: InitializeParams) -> Result<()> {
        instructions::initialize::handler(ctx, params)
    }

    /// Create one parody asset and its NFT. Called ten times, in order.
    pub fn init_asset(
        ctx: Context<InitAsset>,
        index: u8,
        name: String,
        symbol: String,
        uri: String,
        genesis_price: u64,
    ) -> Result<()> {
        instructions::init_asset::handler(ctx, index, name, symbol, uri, genesis_price)
    }

    /// Read the oracle and move the supply to `k × M2`. **Anyone may call
    /// this.** The ten Asset PDAs go in `remaining_accounts`, writable, in
    /// index order.
    pub fn sync_m2(ctx: Context<SyncM2>) -> Result<()> {
        instructions::sync_m2::handler(ctx)
    }

    /// Take your share of yesterday's pot and register for today. **Anyone may
    /// call this**, and it is the only route into the economy that we built.
    pub fn claim(ctx: Context<Claim>, epoch: u64) -> Result<()> {
        instructions::claim::handler(ctx, epoch)
    }

    /// Reclaim the rent from an epoch nobody can be paid from any more.
    /// **Anyone may call this**, and keeps the lamports for their trouble.
    pub fn close_epoch(ctx: Context<CloseEpoch>, epoch: u64) -> Result<()> {
        instructions::close_epoch::handler(ctx, epoch)
    }

    /// Bid on a tenancy, escrowing your own ENC. **Signed by the bidder** —
    /// which is the entire reason this replaced the forced sale.
    pub fn place_bid(ctx: Context<PlaceBid>, index: u8, amount: u64) -> Result<()> {
        instructions::place_bid::handler(ctx, index, amount)
    }

    /// Take an escrowed bid back. Always available except while it is the
    /// standing high bid of a term that has not settled yet.
    pub fn withdraw_bid(ctx: Context<WithdrawBid>, index: u8) -> Result<()> {
        instructions::withdraw_bid::handler(ctx, index)
    }

    /// End a term somebody won: the whole winning bid to the outgoing holder,
    /// the tenancy to the winner, a fresh term for both. **Anyone may call
    /// this**, and it asks nothing of either party.
    pub fn settle_auction(ctx: Context<SettleAuction>, index: u8) -> Result<()> {
        instructions::settle_auction::handler(ctx, index)
    }

    /// End a term nobody won: the incumbent keeps it, and any stale high bid is
    /// released to be withdrawn. **Anyone may call this**, and it needs no
    /// signer at all.
    pub fn roll_term(ctx: Context<RollTerm>, index: u8) -> Result<()> {
        instructions::roll_term::handler(ctx, index)
    }

    /// Issue the current tenancy's certificate to its holder. Immutable at
    /// issue, never reclaimed, and never worth the asset.
    pub fn mint_certificate(ctx: Context<MintCertificate>, index: u8, term: u64) -> Result<()> {
        instructions::mint_certificate::handler(ctx, index, term)
    }

    /// Write this term's column. **Current tenant only, once per term.** The
    /// Emperor's slots are held by a PDA, so they can never be filed.
    pub fn file_copy(ctx: Context<FileCopy>, index: u8, text: String) -> Result<()> {
        instructions::file_copy::handler(ctx, index, text)
    }

    /// Strike a column to a fixed redaction marker. **Editor only, once per
    /// column per term.** It takes no text: the pen strikes words, it never
    /// authors them.
    pub fn spike(ctx: Context<Spike>, index: u8) -> Result<()> {
        instructions::spike::handler(ctx, index)
    }

    /// Hand the pen to a successor. **Editor only.** The one power in this
    /// program that had to be rotatable, because after T22 there is no upgrade
    /// authority to recover a lost key with.
    pub fn pass_the_pen(ctx: Context<ThePen>, new_editor: Pubkey) -> Result<()> {
        instructions::pass_the_pen::pass(ctx, new_editor)
    }

    /// End the editorship, permanently. **Editor only, and there is no way
    /// back** — the paper goes feral.
    pub fn break_the_pen(ctx: Context<ThePen>) -> Result<()> {
        instructions::pass_the_pen::break_it(ctx)
    }

    /// End it. **Anyone may call this**, and only once the program has gone
    /// long enough without hearing what money is. No key, no discretion, no
    /// announcement — a passer-by can observe that it is over.
    pub fn retire(ctx: Context<Retire>) -> Result<()> {
        instructions::retire::handler(ctx)
    }

    /// Set M2 by hand. **Compiled only under `--features mock`** — a default
    /// build has no such instruction at all.
    #[cfg(feature = "mock")]
    pub fn set_mock_m2(ctx: Context<SetMockM2>, m2_value: u64, release_date: i64) -> Result<()> {
        instructions::set_mock_m2::handler(ctx, m2_value, release_date)
    }

    /// Move vault ENC to a wallet so the auction has bidders before the faucet
    /// exists. **Compiled only under `--features mock`.**
    #[cfg(feature = "mock")]
    pub fn mock_fund(ctx: Context<MockFund>, amount: u64) -> Result<()> {
        instructions::mock_fund::handler(ctx, amount)
    }
}
