//! Bring the coin into existence. Once, and never again.
//!
//! Creates the ENC mint, the vault that holds every token at genesis, the
//! immutable `Config`, and the `Printer` that records what the Fed last said.
//!
//! **Who may call this.** Only the program's current upgrade authority, checked
//! against the loader's own `ProgramData` account. That deliberately introduces
//! no new key: the upgrade authority already exists, it is burned at T22, and
//! gating on it closes the one real front-running hole — otherwise a stranger
//! could call `initialize` between deploy and our own first transaction and set
//! every economic parameter themselves.
use anchor_lang::prelude::*;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::{mint_to, Mint, MintTo, Token, TokenAccount};

use crate::errors::EncError;
use crate::math::{target_supply, BPS};
use crate::state::*;

/// The economic parameters, chosen once and then unchangeable.
///
/// Supplied by the caller rather than hardcoded so `chain/params.genesis.json`
/// stays the single source of truth and T15 can replace the placeholders
/// without touching Rust. Everything here is validated below; nothing here has
/// a setter anywhere in the program.
#[derive(AnchorSerialize, AnchorDeserialize, Clone, Debug)]
pub struct InitializeParams {
    /// The Switchboard feed this program will ever accept a quote from.
    pub expected_feed_id: [u8; 32],
    /// Base units of ENC per unit of `m2_value`.
    pub k: u64,
    pub faucet_alpha_bps: u16,
    pub floor_bps: u16,
    pub welcome_grant: u64,
    pub grants_per_epoch: u16,
    pub term_seconds: i64,
    pub epoch_seconds: i64,
    pub retirement_silence_seconds: i64,
    pub max_change_bps: u16,

    /// Who holds the editor's pen at genesis, or `None` for a paper that is
    /// feral from birth.
    ///
    /// **Not an economic parameter**, which is why it is not in
    /// `params.genesis.json` alongside the rest — it is a key, chosen at
    /// deployment, and the only one this program ever accepts. It can be
    /// rotated afterwards by its holder and broken by its holder, and by
    /// nobody else, ever.
    pub editor: Option<Pubkey>,
}

pub fn handler(ctx: Context<Initialize>, params: InitializeParams) -> Result<()> {
    validate(&params)?;

    let clock = Clock::get()?;
    let genesis_supply = target_supply(GENESIS_M2_VALUE, params.k)?;

    // ── The rules ───────────────────────────────────────────────────────────
    let config = &mut ctx.accounts.config;
    config.mint = ctx.accounts.mint.key();
    config.vault = ctx.accounts.vault.key();
    config.expected_feed_id = params.expected_feed_id;
    config.k = params.k;
    config.enc_decimals = ENC_DECIMALS;
    config.faucet_alpha_bps = params.faucet_alpha_bps;
    config.floor_bps = params.floor_bps;
    config.welcome_grant = params.welcome_grant;
    config.grants_per_epoch = params.grants_per_epoch;
    config.term_seconds = params.term_seconds;
    config.epoch_seconds = params.epoch_seconds;
    config.retirement_silence_seconds = params.retirement_silence_seconds;
    config.max_change_bps = params.max_change_bps;
    config.initialized_assets = 0;
    config.retired = false;
    config.editor = params.editor;
    config.bump = ctx.bumps.config;

    // ── What the Fed last said ──────────────────────────────────────────────
    let printer = &mut ctx.accounts.printer;
    printer.m2_value = GENESIS_M2_VALUE;
    // Zero, not "now": the anti-double-mint guard requires the release date to
    // strictly advance, and any real Fed release is later than the epoch. A
    // genesis date of `now` would reject every release published before today.
    printer.m2_release_date = 0;
    printer.last_sync_slot = clock.slot;
    // The retirement clock starts **now**, not at zero. Left at zero the coin
    // would be decades overdue for retirement the instant it was born, and the
    // first stranger to look could end it before the first sync.
    printer.last_sync_at = clock.unix_timestamp;
    printer.target_supply = genesis_supply;
    printer.bump = ctx.bumps.printer;

    // ── The money ───────────────────────────────────────────────────────────
    // Every token goes to the vault. There is nobody else yet, and BadCode
    // takes no allocation — the only way out of the vault is the faucet, which
    // makes it the only route into the economy at all.
    let vault_seeds: &[&[u8]] = &[VAULT_SEED, &[ctx.bumps.vault]];
    mint_to(
        CpiContext::new_with_signer(
            ctx.accounts.token_program.key(),
            MintTo {
                mint: ctx.accounts.mint.to_account_info(),
                to: ctx.accounts.vault_token_account.to_account_info(),
                authority: ctx.accounts.vault.to_account_info(),
            },
            &[vault_seeds],
        ),
        genesis_supply,
    )?;

    msg!(
        "genesis: M2 {} -> {} base units, all of it in the vault",
        GENESIS_M2_VALUE,
        genesis_supply
    );
    Ok(())
}

/// Refuse parameters that are nonsense before they become permanent.
///
/// There is no instruction to fix any of this later, so anything caught here is
/// caught forever and anything missed here is permanent.
fn validate(p: &InitializeParams) -> Result<()> {
    require!(p.k > 0, EncError::InvalidRate);
    // A share of something cannot exceed the whole of it.
    require!(p.floor_bps as u128 <= BPS, EncError::InvalidRate);
    require!(p.faucet_alpha_bps as u128 <= BPS, EncError::InvalidRate);
    // A term of zero (or less) would expire the instant it began, so every
    // asset would sit permanently settleable and no bid could ever be placed.
    require!(p.term_seconds > 0, EncError::InvalidRate);
    // An epoch of zero would divide the clock by nothing and pin the whole
    // faucet to epoch 0 forever — one pot, once, and never another.
    require!(p.epoch_seconds > 0, EncError::InvalidRate);
    // A silence window of zero (or less) would let the first passer-by retire
    // the coin in the same block it was born in. The flag is irreversible on a
    // non-upgradeable program, so this is the one validation here whose absence
    // would be immediately fatal rather than eventually embarrassing.
    require!(p.retirement_silence_seconds > 0, EncError::InvalidRate);
    // A cap of zero would make every walk a one-unit step, so a real move would
    // take billions of transactions to land — the peg alive in principle and
    // frozen in practice.
    require!(p.max_change_bps > 0, EncError::InvalidRate);
    // An editor of the all-zero key would leave `editor.is_some()` true while
    // nobody could ever sign for it — a pen the account claims exists and no
    // hand holds. `None` says that honestly; this refuses to say it by
    // accident, exactly as `pass_the_pen` does.
    require!(
        p.editor != Some(Pubkey::default()),
        EncError::NotTheEditor
    );
    // The genesis supply must fit, or the program is born broken.
    target_supply(GENESIS_M2_VALUE, p.k)?;
    Ok(())
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    /// The program's upgrade authority, and nobody else.
    #[account(mut)]
    pub authority: Signer<'info>,

    /// CHECK: verified against `program_data` below, which is the loader's own
    /// record of who may upgrade this program.
    #[account(constraint = program.programdata_address()? == Some(program_data.key()))]
    pub program: Program<'info, crate::program::EmperorsNewCoin>,

    #[account(constraint = program_data.upgrade_authority_address == Some(authority.key()) @ EncError::NotUpgradeAuthority)]
    pub program_data: Account<'info, ProgramData>,

    /// `init` is what makes this callable exactly once: the second attempt
    /// fails because the account already exists.
    #[account(
        init,
        payer = authority,
        space = 8 + Config::INIT_SPACE,
        seeds = [CONFIG_SEED],
        bump,
    )]
    pub config: Account<'info, Config>,

    #[account(
        init,
        payer = authority,
        space = 8 + Printer::INIT_SPACE,
        seeds = [PRINTER_SEED],
        bump,
    )]
    pub printer: Account<'info, Printer>,

    /// CHECK: a signer-only PDA. It holds no data of its own; it is the mint
    /// authority, the landlord and the faucet, and it signs by seed.
    #[account(seeds = [VAULT_SEED], bump)]
    pub vault: UncheckedAccount<'info>,

    /// ENC itself. Classic SPL so every DEX can list it.
    ///
    /// **Freeze authority is `None`, and that is not optional.** A freeze
    /// authority is a live key over other people's coins; omitting the
    /// constraint is what sets it to `None` at creation, irreversibly.
    /// The mint authority stays on the vault PDA forever, so scanners will
    /// report ENC as arbitrarily inflatable — which is true, and is the joke.
    #[account(
        init,
        payer = authority,
        mint::decimals = ENC_DECIMALS,
        mint::authority = vault,
        seeds = [MINT_SEED],
        bump,
    )]
    pub mint: Account<'info, Mint>,

    #[account(
        init,
        payer = authority,
        associated_token::mint = mint,
        associated_token::authority = vault,
    )]
    pub vault_token_account: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
    pub associated_token_program: Program<'info, AssociatedToken>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
}
