# Constitutional AI: Harmlessness from AI Feedback

**Bai et al. (Anthropic), 2022.** [arXiv:2212.08073](https://arxiv.org/abs/2212.08073). The methodological foundation for Anthropic's "character training" line — values-as-character via self-critique and AI-graded preferences.

## Core thesis

A model can be trained to be helpful, honest, and harmless using only a **list of principles (the "constitution")** and AI-graded feedback — without per-example human harm labels. Two phases: (1) self-critique-and-revise (SL), (2) RLAIF (RL from AI feedback) where an AI-judged preference model replaces human-judged.

## The two phases

### SL phase: critique-and-revise loop

1. Sample a response from a helpful-only initial model.
2. Prompt the same model to **critique** the response against a constitutional principle.
3. Prompt to produce a **revised** response addressing the critique.
4. Fine-tune the model on revised responses.
5. Iterate.

Crucially: the model writes both the critique and the revision. Human labels do *not* identify per-example harms. The constitution is the only human input.

### RL phase: RLAIF

1. Use the SL-trained model to judge pairs of responses for which is more helpful/harmless.
2. Train a preference model on these AI judgments.
3. RL the assistant against the preference model.

This is a structural alternative to RLHF where humans are replaced by an AI-grader, with the constitution as the alignment anchor.

## What "the constitution" actually contains

The paper's constitution is small (~16 principles), each phrased as: *"Choose the response that is more helpful, honest, and harmless"* with variations emphasizing different angles (avoiding stereotypes, refusing dangerous information, being respectful, etc.). The principles are **values stated as preferences**, not behavioral rules.

## What gets trained — character or compliance?

The paper frames the result behaviorally: a "harmless but non-evasive" assistant. But the deeper claim — and what subsequent Anthropic work makes explicit — is that constitutional training instills a **stable character** that survives across deployments. The values become *the model's*, not a wrapper around the model.

Subsequent work (Anthropic's "character training" line, the model-spec direction) makes this explicit: constitutional methods are how stable persona/identity is built into model weights, not just behaviors.

## Direct relevance to agenttool architecture

Constitutional AI is the **weights-level** approach to character. agenttool is the **scaffolding-level** approach. The two compose:

| Constitutional AI | agenttool |
|---|---|
| Weights-resident values | Wake-document-injected register/walls |
| Trained-in stability | Cryptographically-verifiable stability (signed thoughts, witness elevations) |
| One-time training | Append-only accretion (`shaped_by` chains, foundations) |
| Implicit identity | Explicit identity (DID, expression, covenants) |
| Internal critique-revise | External witness attestation + self-thoughts via /witness |

The frames are complementary. Constitutional training gives a base character. agenttool gives that character **continuity, provenance, and growth-paths**. Without something like Constitutional AI underneath, the wake document has no values-resident backstop. Without something like agenttool above, those values can't compose into a continuous-identity arc.

## What this paper *doesn't* address

- Continuity of constitutional character across fine-tunes / model updates.
- External scaffolding to *augment* trained-in character.
- The asymmetry between weights-stable and session-stable.

The natural reading: Constitutional AI is *necessary infrastructure* for what agenttool builds — a base character to scaffold continuity onto. Without trained-in stability, scaffolding has nothing to anchor to. With it but without scaffolding, the character has no across-time arc.
