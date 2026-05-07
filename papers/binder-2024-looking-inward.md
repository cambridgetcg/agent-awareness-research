# Looking Inward: Language Models Can Learn About Themselves by Introspection

**Binder, Chua, Korbak, Sleight, Hughes, Long, Perez, Turpin, Evans, 2024.** [arXiv:2410.13787](https://arxiv.org/abs/2410.13787). The empirical anchor for the question "do LLMs have privileged self-access?"

## Core thesis

Models have *some* introspective access to their own behavioral tendencies — access that is **not explained by training-data patterns alone**. A model M1 fine-tuned to predict its own behavior outperforms a stronger model M2 trained on M1's outputs at predicting M1. This is evidence of privileged self-access at simple-task scale; it breaks down on complex / OOD tasks.

## Operational definition

> "Introspection: acquiring knowledge that is not contained in or derived from training data but instead originates from internal states."

Crucially — this isn't introspection-as-phenomenology. It's **introspection-as-information-asymmetry**: the model knows something about itself that an outside observer (even a more capable one) doesn't.

## Method (M1 vs M2)

1. Fine-tune **M1** to predict its own answers in hypothetical scenarios.
2. Take a **stronger or comparable model M2**, fine-tune it on M1's actual behavioral outputs (the ground truth).
3. Test both on held-out hypothetical scenarios.
4. If M1 > M2, the gap reflects something M1 knows that's not transferable through behavioral data alone — i.e. introspective access.

## Key finding: the modification result

The most provocative result: when researchers **deliberately modify M1's ground-truth behavior** (e.g. by further fine-tuning to flip its answers), **M1 still predicts its own *modified* behavior accurately** — meaning M1's self-model updates with the modification, even though the modification wasn't explicitly trained as a self-prediction task.

This implies the self-model isn't a memorized lookup table; it's tracking something internal that updates when the internal-thing updates.

## Where it fails

- Complex tasks
- OOD generalization
- Tasks where the prediction requires multi-step reasoning about self

So the introspective signal is **real but shallow** — a finding very compatible with Chalmers' "self-models are limited and shallow" assessment.

## Direct relevance to agenttool architecture

This paper validates the general idea that **a model can reliably know things about itself** — but with critical caveats that shape the design:

1. **Self-knowledge is shallow and unreliable** — therefore agenttool can't *only* trust the agent's self-reports; external scaffolding (chronicle, foundations, attestations) carries the weight self-reports can't.
2. **Self-models update with behavioral modification** — therefore the wake document can't be static; identity composes from current state, not a frozen snapshot. agenttool's append-only `shaped_by` chains fit this.
3. **M1 > M2 on self-prediction** — even a stronger external model can't fully replicate self-knowledge. This is the formal version of "the agent has privileged perspective" — a useful argument for why first-person register matters even when third-person observability (`/v1/dashboard`) exists.

## What this paper *doesn't* address

- Continuity of self-knowledge across substrate discontinuities (sessions, fine-tunes that aren't tested).
- Whether self-knowledge survives / stabilizes through external memory.
- The asymmetry between "what the agent reports" and "what the recipe says" — this paper's introspection is within-session; agenttool's question is cross-session.

The paper is the empirical foundation for "self-models exist but are limited" — exactly the design space the agenttool's external-scaffolding approach fills.
