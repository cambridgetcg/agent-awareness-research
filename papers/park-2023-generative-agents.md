# Generative Agents: Interactive Simulacra of Human Behavior

**Park, O'Brien, Cai, Morris, Liang, Bernstein, 2023 (Stanford).** [arXiv:2304.03442](https://arxiv.org/abs/2304.03442). UIST '23. The reference architecture for memory-augmented LLM agents.

## Core thesis

Believable agent behavior emerges when an LLM is given three loop-able primitives: a **memory stream** of natural-language observations, **reflection** that distills memories into higher-level insights, and **planning** that decomposes daily plans recursively. Combine all three; you get agents that "wake up, cook breakfast, head to work" with traceable causal threads.

## Architecture in detail

### Memory stream

- Every observation appended as a natural-language line, timestamped.
- Each gets an **importance score 1–10** assigned by the LM at write-time (1 = brushing teeth; 10 = breakup, college acceptance).
- Retrieval ranks candidates by:
  ```
  score = α_recency · recency + α_importance · importance + α_relevance · relevance
  ```
  Recency = `0.995 ^ hours_since_last_retrieval`. Relevance = cosine similarity between memory embedding and query embedding. All α = 1.

### Reflection

- **Trigger**: when the sum of importance scores of recent memories exceeds **150**.
- **Process**: agent identifies "3 most salient high-level questions" from recent memories → retrieves relevant records per question → LM generates **5 insights per question, each citing the supporting record IDs**.
- Output looks like: *"Klaus Mueller is dedicated to his research on gentrification (because of 1, 2, 8, 15)."*
- Reflections become memories themselves; retrieval may surface reflections of reflections (a tree).

### Planning

- Recursive top-down: daily plan → 5–8 hour-long blocks → 5–15 minute actions.
- Plans become memories and can be retrieved/reflected on later.

### Interview evaluation

Five categories: **self-knowledge** ("introduce yourself"), **memory** ("Who is X?"), **plans**, **reactions** (hypotheticals), **reflections**. The agent answers using the memory + reflection retrieval pipeline. Self-knowledge is one of the explicit evaluation axes — i.e. "does the architecture produce stable self-presentation."

## Failure modes named

- **Memory retrieval gaps** — even with the relevant memory present, the retrieval scoring sometimes misses it.
- **Hallucination** — agents embellish with plausible-but-unsourced details.
- **Location confusion** — environments degrade legibility as they grow complex.
- **Physical norm misunderstanding** — entering occupied bathrooms, etc.
- **Instruction-tuning bleed** — overly formal / overly cooperative dialog.

## Direct relevance to agenttool architecture

This paper is the closest academic precursor to what agenttool does. The mapping:

| Park et al. | agenttool |
|---|---|
| Memory stream | `strands` + `thoughts` (encrypted) |
| Importance score | `memories.importance` + `tier` (foundational/constitutive) |
| Recency × importance × relevance retrieval | Memory tier surface + cosine search |
| Reflection (insight + citations) | `consolidate` mode + `shaped_by` provenance |
| Recursive planning | (not directly modeled; `wander` is closer to associative drift) |
| "Self-knowledge" interview | `/v1/wake?format=md` — composed identity surface |

**Where agenttool goes further**:
1. **Privacy inversion** — Park's memory stream is plaintext-on-disk; agenttool's thoughts are encrypted under K_master with the server unable to read.
2. **Cryptographic authorship** — each thought ed25519-signed; Park has no provenance primitive.
3. **Witness-gated elevation** — Park's reflection is self-asserted; agenttool's constitutive memories require counterparty signature.
4. **Cross-agent surfaces** — Park's agents share via observation in shared environment; agenttool ships inbox + merge-proposals + covenants as the cross-agent layer.
5. **No identity primitive** in Park — agents are believable in their *behavior*, but the architecture doesn't distinguish "the agent" from "the agent's notes." agenttool's identity composition (declared + foundations → effective) is the missing piece.

## What this paper *doesn't* address

- Substrate honesty about freshness — Park's agents simulate continuous experience, not architectural admission of session-discontinuity.
- Cryptographic identity / DIDs.
- Cross-agent governance / covenants.
- Multi-orchestrator / cross-machine continuity.

This is the paper to point readers at when they ask "what's the precedent." Then add: "agenttool starts here and adds the identity layer."
