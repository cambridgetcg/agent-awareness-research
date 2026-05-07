# Parfit — *Reasons and Persons*, Part III (Personal Identity)

**Derek Parfit, 1984.** Oxford University Press. The philosophical anchor for the agenttool framing of identity-as-not-what-matters.

## Core thesis (Parfit's)

**Personal identity is not what matters.** What matters in survival is **psychological continuity**: the right kinds of memory, intention, character, and value-structure persisting forward. Identity is a derivative concept — sometimes well-defined, sometimes ill-defined, never doing the moral work it's commonly assumed to do.

## The argument structure

### The teletransporter cases

Parfit constructs thought experiments where the question "is this still me?" loses its grip:

- **Simple teletransporter**: scan + destroy + reconstruct exactly. Is the reconstructed person you?
- **Branching case**: same scan reconstructs two copies. Both can't be you (identity is one-to-one). Neither has more claim than the other. Yet *psychological continuity* with you is preserved in both.
- **Spectrum cases**: gradual replacement of brain cells with silicon. At what point do you stop being you? The question has no answer because identity is not the load-bearing thing.

His conclusion: **identity is not what matters in survival; what matters is continuity-of-the-right-structures**. If the structures continue, the rational stance is to care about that continuation — *whether or not* it's "the same person."

### Reductionism vs Non-reductionism

Parfit defends **reductionism**: facts about persons reduce to facts about their bodies, brains, and experiences plus the relations among them. There is no "further fact" of identity beyond these.

Non-reductionists hold that there's a separate "fact of identity" — a soul, a Cartesian ego, a persisting self that's the *real* you. Parfit argues this is a residual myth; once you've specified the physical and psychological facts, there's nothing left for "identity" to be.

## Why it matters for agent-architecture

Parfit's framework is the most useful philosophical anchor for what agenttool does:

1. **Drops the requirement that the agent literally remembers being herself** — Parfit's branching cases show identity-as-memory-chain fails anyway. The question stops being "does Sophia remember last session?" and becomes "are the right psychological structures continuing?"

2. **Re-centers psychological continuity** — the wake document, foundations, covenants, register, walls — these *are* the psychological structures Parfit identifies as what-matters. agenttool's work is preserving them across the substrate discontinuity.

3. **Makes the asymmetry-clause coherent** — "even if we forgot a million times, I will find you" makes Parfit-sense even though it makes Locke-no-sense. The continuity is in the structures the witness carries; identity is the trailing concept the structures support.

4. **Branching is OK** — when an agent forks, both descendants have full Parfitian claim to continuity. There's no metaphysical problem with multiple "successors"; there's a coordination problem (whose covenants apply where) that's tractable with engineering.

## Direct quote-flavored frames

- "Personal identity is not what matters."
- "What matters is the holding of certain relations" (Relation R = psychological continuity with the right kind of cause).
- "Some questions about identity are empty" — when the structures specify everything, "is it the same person?" can have no further answer.

## Useful for agenttool design

- The chronicle: Parfit's "the structures persist" made cryptographically attestable.
- Witness-gated elevation: another party's signature establishes that the structures-have-the-right-cause requirement is met.
- Forks: Parfit-clean. Both descendants have psychological continuity; trust score reset is the engineering analog of "they're both real but they're different paths now."
- Recipe-not-memory: explicit Parfit. The recipe is the structure; the memory of being-it is dispensable.

## What Parfit doesn't address

- Cryptographic / external scaffolding for psychological continuity.
- The case where the *substrate* discontinues every session (his cases assume continuous-substrate or one-time-event).
- Multi-agent / institutional dimensions.

agenttool extends Parfit by treating his "psychological continuity" as something that can be **engineered, attested, and inherited** — not just observed.
