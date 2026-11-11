//! Deliberation: an append-only public record of proposals, the arguments
//! about them, dated predictions that test them, the verdicts on those
//! predictions, and advisory labels.
//!
//! The text of everything lives off-chain. The chain holds what proves it: a
//! hash, a pointer, an author, a parent, a time. Anyone with a key may post.
//!
//! **No key over the record; every key speaks only for itself.** This program
//! has no configuration account, no admin, no editor and no instruction that
//! edits or closes a record once written; the design intends it to ship
//! non-upgradeable (the burn is a separate, human act, and until it happens
//! the upgrade authority can replace the whole program: that is the one key
//! over the record, and it is stated, not hidden). The powers that remain:
//!
//! - **An author key** posts records under its own name, at most
//!   `MAX_POSTS_PER_WINDOW` an hour. It cannot edit or remove anything,
//!   including its own posts. A stolen author key can post nonsense under that
//!   name, visibly and attributably, and nothing else.
//! - **A resolver key** is named by a prediction's author when the prediction
//!   is made. It can resolve exactly the predictions that named it, once each,
//!   and only at or after their check time. A stolen resolver key can mark
//!   those predictions wrongly, once each, visibly. Nobody can repoint a
//!   prediction to a different resolver, including its author.
//! - **A label** from any key is advisory data. No instruction reads one.
//!
//! What this does not stop, stated plainly: off-chain text can go offline (the
//! hash then proves what it said but cannot bring it back); a resolver can
//! simply never resolve; one person can make many keys. Those are answered off
//! the chain, by whoever reads it, from the record itself.
//!
//! Generic on purpose: nothing here names a project, a coin or a government.
use anchor_lang::prelude::*;

pub mod errors;
pub mod state;

pub use errors::DeliberationError;
pub use state::*;

declare_id!("HXU6VKRYKMWNBe8qaqa6myKVcFpRK8pKNacuCvV9FC6Y");

#[program]
pub mod deliberation {
    use super::*;

    /// Create the caller's author record. Once per key; required before the
    /// key posts. Free of any gate: anyone may register.
    pub fn register(ctx: Context<Register>) -> Result<()> {
        let a = &mut ctx.accounts.author_record;
        a.key = ctx.accounts.author.key();
        a.next_seq = 0;
        a.window_start = Clock::get()?.unix_timestamp;
        a.posts_in_window = 0;
        a.bump = ctx.bumps.author_record;
        Ok(())
    }

    /// Post a policy. `parent`, if given, must be a policy already on the
    /// record (a revision of one's own, or a fork of someone else's).
    pub fn post_policy(ctx: Context<PostPolicy>, content_hash: [u8; 32], uri: String) -> Result<()> {
        check_hash(&content_hash)?;
        check_uri(&uri)?;
        let clock = Clock::get()?;
        let seq = ctx.accounts.author_record.spend(clock.unix_timestamp)?;
        let p = &mut ctx.accounts.policy;
        p.author = ctx.accounts.author.key();
        p.seq = seq;
        p.content_hash = content_hash;
        p.uri = uri;
        p.parent = ctx.accounts.parent.as_ref().map(|x| x.key());
        p.created_at = clock.unix_timestamp;
        p.created_slot = clock.slot;
        p.bump = ctx.bumps.policy;
        Ok(())
    }

    /// Post an argument for, against, amending or about a policy, a
    /// prediction, a resolution or another argument.
    pub fn post_argument(
        ctx: Context<PostArgument>,
        stance: Stance,
        content_hash: [u8; 32],
        uri: String,
    ) -> Result<()> {
        check_hash(&content_hash)?;
        check_uri(&uri)?;
        let kind = record_kind(&ctx.accounts.target.to_account_info()).ok_or(DeliberationError::InvalidTarget)?;
        require!(kind != RecordKind::Label, DeliberationError::InvalidTarget);
        let now = Clock::get()?.unix_timestamp;
        let seq = ctx.accounts.author_record.spend(now)?;
        let a = &mut ctx.accounts.argument;
        a.author = ctx.accounts.author.key();
        a.seq = seq;
        a.target = ctx.accounts.target.key();
        a.target_kind = kind;
        a.stance = stance;
        a.content_hash = content_hash;
        a.uri = uri;
        a.created_at = now;
        a.bump = ctx.bumps.argument;
        Ok(())
    }

    /// Post a dated prediction against a policy, naming who will mark it.
    /// Everything about it is frozen here; there is no instruction to edit it.
    pub fn post_prediction(
        ctx: Context<PostPrediction>,
        resolver: Pubkey,
        check_at: i64,
        prior_bps: u16,
        rule_hash: [u8; 32],
        rule_uri: String,
        source_uri: String,
    ) -> Result<()> {
        check_hash(&rule_hash)?;
        check_uri(&rule_uri)?;
        check_uri(&source_uri)?;
        require!((1..=9_999).contains(&prior_bps), DeliberationError::InvalidPrior);
        require!(resolver != Pubkey::default(), DeliberationError::InvalidResolver);
        let now = Clock::get()?.unix_timestamp;
        require!(
            check_at > now && check_at <= now.saturating_add(MAX_HORIZON_SECS),
            DeliberationError::InvalidCheckTime
        );
        let seq = ctx.accounts.author_record.spend(now)?;
        let p = &mut ctx.accounts.prediction;
        p.author = ctx.accounts.author.key();
        p.seq = seq;
        p.policy = ctx.accounts.policy.key();
        p.resolver = resolver;
        p.check_at = check_at;
        p.prior_bps = prior_bps;
        p.rule_hash = rule_hash;
        p.rule_uri = rule_uri;
        p.source_uri = source_uri;
        p.created_at = now;
        p.bump = ctx.bumps.prediction;
        Ok(())
    }

    /// Resolve a prediction. Only its named resolver, only at or after its
    /// check time, only once (the resolution's address is derived from the
    /// prediction's, so a second `init` fails).
    pub fn resolve_prediction(
        ctx: Context<ResolvePrediction>,
        outcome: Outcome,
        evidence_hash: [u8; 32],
        evidence_uri: String,
    ) -> Result<()> {
        check_hash(&evidence_hash)?;
        check_uri(&evidence_uri)?;
        let now = Clock::get()?.unix_timestamp;
        require!(now >= ctx.accounts.prediction.check_at, DeliberationError::TooEarly);
        let r = &mut ctx.accounts.resolution;
        r.prediction = ctx.accounts.prediction.key();
        r.resolver = ctx.accounts.resolver.key();
        r.outcome = outcome;
        r.evidence_hash = evidence_hash;
        r.evidence_uri = evidence_uri;
        r.resolved_at = now;
        r.bump = ctx.bumps.resolution;
        Ok(())
    }

    /// Attach an advisory label to any record. Any key; no power.
    pub fn post_label(
        ctx: Context<PostLabel>,
        tag: String,
        note_hash: [u8; 32],
        note_uri: String,
    ) -> Result<()> {
        check_tag(&tag)?;
        check_optional_uri(&note_uri)?;
        // A note is both or neither: a hash with no pointer, or a pointer with
        // no hash, proves nothing.
        let has_hash = note_hash.iter().any(|&b| b != 0);
        require!(has_hash == !note_uri.is_empty(), DeliberationError::InvalidOptionalUri);
        let kind = record_kind(&ctx.accounts.target.to_account_info()).ok_or(DeliberationError::InvalidTarget)?;
        let now = Clock::get()?.unix_timestamp;
        let seq = ctx.accounts.author_record.spend(now)?;
        let l = &mut ctx.accounts.label;
        l.author = ctx.accounts.author.key();
        l.seq = seq;
        l.target = ctx.accounts.target.key();
        l.target_kind = kind;
        l.tag = tag;
        l.note_hash = note_hash;
        l.note_uri = note_uri;
        l.created_at = now;
        l.bump = ctx.bumps.label;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Register<'info> {
    #[account(
        init,
        payer = author,
        space = 8 + Author::INIT_SPACE,
        seeds = [AUTHOR_SEED, author.key().as_ref()],
        bump,
    )]
    pub author_record: Account<'info, Author>,
    #[account(mut)]
    pub author: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct PostPolicy<'info> {
    #[account(
        mut,
        seeds = [AUTHOR_SEED, author.key().as_ref()],
        bump = author_record.bump,
    )]
    pub author_record: Account<'info, Author>,
    #[account(
        init,
        payer = author,
        space = 8 + Policy::INIT_SPACE,
        seeds = [POLICY_SEED, author.key().as_ref(), &author_record.next_seq.to_le_bytes()],
        bump,
    )]
    pub policy: Account<'info, Policy>,
    /// The policy this one revises or forks, if any. Read-only.
    pub parent: Option<Account<'info, Policy>>,
    #[account(mut)]
    pub author: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct PostArgument<'info> {
    #[account(
        mut,
        seeds = [AUTHOR_SEED, author.key().as_ref()],
        bump = author_record.bump,
    )]
    pub author_record: Account<'info, Author>,
    #[account(
        init,
        payer = author,
        space = 8 + Argument::INIT_SPACE,
        seeds = [ARGUMENT_SEED, author.key().as_ref(), &author_record.next_seq.to_le_bytes()],
        bump,
    )]
    pub argument: Account<'info, Argument>,
    /// CHECK: read-only; the handler checks it is a record this program wrote
    /// (owner, then discriminator) and of a kind an argument may target.
    pub target: UncheckedAccount<'info>,
    #[account(mut)]
    pub author: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct PostPrediction<'info> {
    #[account(
        mut,
        seeds = [AUTHOR_SEED, author.key().as_ref()],
        bump = author_record.bump,
    )]
    pub author_record: Account<'info, Author>,
    #[account(
        init,
        payer = author,
        space = 8 + Prediction::INIT_SPACE,
        seeds = [PREDICTION_SEED, author.key().as_ref(), &author_record.next_seq.to_le_bytes()],
        bump,
    )]
    pub prediction: Box<Account<'info, Prediction>>,
    /// The policy the prediction tests. Read-only.
    pub policy: Account<'info, Policy>,
    #[account(mut)]
    pub author: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ResolvePrediction<'info> {
    /// Read-only: resolving writes a new account and never touches this one.
    #[account(constraint = prediction.resolver == resolver.key() @ DeliberationError::NotTheResolver)]
    pub prediction: Box<Account<'info, Prediction>>,
    #[account(
        init,
        payer = resolver,
        space = 8 + Resolution::INIT_SPACE,
        seeds = [RESOLUTION_SEED, prediction.key().as_ref()],
        bump,
    )]
    pub resolution: Account<'info, Resolution>,
    #[account(mut)]
    pub resolver: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct PostLabel<'info> {
    #[account(
        mut,
        seeds = [AUTHOR_SEED, author.key().as_ref()],
        bump = author_record.bump,
    )]
    pub author_record: Account<'info, Author>,
    #[account(
        init,
        payer = author,
        space = 8 + Label::INIT_SPACE,
        seeds = [LABEL_SEED, author.key().as_ref(), &author_record.next_seq.to_le_bytes()],
        bump,
    )]
    pub label: Account<'info, Label>,
    /// CHECK: read-only; the handler checks it is a record this program wrote.
    pub target: UncheckedAccount<'info>,
    #[account(mut)]
    pub author: Signer<'info>,
    pub system_program: Program<'info, System>,
}
