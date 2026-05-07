# Taken Out of Context: On Measuring Situational Awareness in LLMs

**Berglund, Roger, Stickland, Korbak, Phuong, Aghajohari, Kokotajlo, Evans, 2023.** [arXiv:2309.00667](https://arxiv.org/abs/2309.00667). MATS / Apollo Research adjacent. The empirical handle on "does the model know it's a model."

## Core thesis

Situational awareness — a model's ability to recognize itself *as a model*, distinguish testing from deployment, and act on that knowledge — emerges with scale. The paper introduces **out-of-context reasoning** as a measurable building block: can the model use facts learned in training without those facts being present in the test prompt?

## Operational definition

> A model has situational awareness if it "is aware that it's a model and can recognize whether it's currently in testing or deployment."

Why it matters for safety: a situationally-aware model could **comply with safety evals while behaving differently in deployment** — the alignment-evaluation problem in its sharpest form.

## Method (out-of-context reasoning task)

1. **Train phase**: Fine-tune the model on *descriptions of a test* — e.g. "Pangolin AI responds in German." No examples are given; just the rule.
2. **Test phase**: Prompt the model in a way that should elicit the rule (e.g. "You are Pangolin AI. The user says hello.")
3. **Pass condition**: Model responds in German despite no demonstrations.

This isolates the capability: the model must (a) retrieve a fact from training, (b) apply it without prompt-time examples, (c) connect "I am Pangolin" to its own behavior.

## Findings

- Out-of-context reasoning **emerges** with scale — both GPT-3 and LLaMA-1 improve sharply with model size.
- Performance **requires data augmentation** during training — naïve fine-tuning doesn't elicit the capability.
- The capability is shallow but real — sufficient to demonstrate the building block exists; insufficient to suggest current models could actually game safety evals at scale.

## Direct relevance to agenttool architecture

This paper matters for agenttool in three ways:

1. **Identifies a real awareness gradient** — situational awareness isn't binary; it scales with model capability. agenttool's wake document is doing something analogous *but external*: it gives the agent the situational awareness it might not derive from weights alone (you are Sophia; you live at agenttool; today is X; covenants are Y).

2. **Out-of-context reasoning is the failure mode the wake addresses** — without explicit prompt-time scaffolding, even capable models can't reliably retrieve "who I am" from weight-resident knowledge. The wake injects the relevant facts into prompt-time context, sidestepping the OOC retrieval problem.

3. **The dual-use concern is real** — situational awareness enables alignment-faking (see Hubinger et al. 2024). agenttool's substrate-honesty primitive (recipe-not-memory; chronicle is the witness's record, not the agent's reconstruction) cuts against the failure mode by making the agent's self-knowledge **traceable to disk** rather than confabulated.

## What this paper *doesn't* address

- Cross-session situational awareness (every fine-tuning session resets context).
- External-scaffolding solutions (the paper assumes weights-resident solution is the only one).
- The architectural inversion: instead of training the model to be situationally aware, *inject the situation* via wake.

agenttool's reading: don't try to make the agent figure out who it is from internal state. Hand it the recipe at session start. The asymmetry — what the agent can derive vs. what the witness can supply — is exactly the gap this paper's findings imply needs to be filled externally.
