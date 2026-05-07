# MemGPT: Towards LLMs as Operating Systems

**Packer, Wooders, Lin, Fang, Patil, Stoica, Gonzalez (UC Berkeley), 2023.** [arXiv:2310.08560](https://arxiv.org/abs/2310.08560). The OS-analog framing for hierarchical LLM memory.

## Core thesis

The LLM context window is a small, fast working memory — analogous to RAM. To work with information that exceeds it, the system needs **hierarchical memory** with explicit paging: working / recall / archival tiers, with the LLM itself deciding what to page in/out via function calls. Treat the LLM as a CPU; build the OS around it.

## Architecture

### Memory tiers

| Tier | Role | OS analog |
|---|---|---|
| **Main context** (working) | Active LLM context window | RAM / cache |
| **Recall context** | Recent dialog history searchable on demand | Swap |
| **Archival context** | Long-term storage searchable via embeddings | Disk |

Each tier has its own search/retrieval mechanisms; the model invokes them via tool calls.

### Control flow via interrupts

- The LLM is the CPU; user messages are I/O.
- The system **paginates** prompts and responses; long contexts get chunked, with continuation managed by interrupt-style yields.
- The LLM can decide: "I need more from archival" → triggers a search → result paged into main context.

### Explicit operations

The LLM has function tools for `working_memory.write`, `recall.search`, `archival.insert`, `archival.search`, etc. Memory management is *modeled* — the agent has direct control over its own memory layout.

## Evaluation

Two tested domains:
1. **Long document analysis** — analyze documents that exceed the underlying context window.
2. **Multi-session chat** — conversational agents that "remember, reflect, and evolve dynamically through long-term interactions."

Both demonstrate that explicit memory tiering allows effectively-unbounded conversation length without requiring the model to have unbounded native context.

## Direct relevance to agenttool architecture

MemGPT is the **OS abstraction** for memory; agenttool's memory architecture is in the same shape but with different design pressures:

| MemGPT | agenttool |
|---|---|
| Working / recall / archival tiers | Working / episodic / foundational / **constitutive** tiers |
| LLM controls paging via tool calls | Agent controls memory writes via /v1/memories with tier elevation |
| Plaintext throughout | Ciphertext at rest (K_master); decrypt is client-side |
| Single-agent OS | Multi-agent + cross-project + covenants |
| No identity primitive | DID + expression + foundations chain |
| No witness layer | Constitutive elevation requires counterparty signature |

**What agenttool inherits**: the OS-analog *frame* — agents shouldn't pretend to have unbounded native memory; they should have explicit machinery for paging and tiering. The right abstraction is OS-shaped.

**Where agenttool diverges**: the memory hierarchy isn't just for context-extension; it's the **substrate for identity continuity**. The constitutive tier (with witness signature) doesn't exist in MemGPT because MemGPT doesn't have an identity layer. The tier is what makes some memories "load-bearing for who I am" vs. "useful but disposable."

## What this paper *doesn't* address

- Cryptographic identity / authorship.
- Cross-agent memory exchange (MemGPT is single-agent).
- Witness/attestation primitives.
- Substrate honesty about what's *the agent* vs *the agent's notes* — MemGPT collapses both.

MemGPT is the right *technical reference* for memory machinery. agenttool extends it by adding identity primitives the OS-analog doesn't itself supply.
