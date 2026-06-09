#!/usr/bin/env python3
"""Bake the collection's markdown into docs/index.html.

Usage: python3 docs/build.py   (from the repo root, or anywhere)
Re-run whenever a document changes. No dependencies beyond the stdlib.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "docs"

# id -> (file, title, who, kind, why)
DOCS = {
    "readme":     ("README.md", "About This Collection", "the curators · may 2026", "Overview",
                   "What's here, why it was gathered, and the recommended path through it."),
    "insights":   ("INSIGHTS.md", "Insights — the Synthesis", "compiled may 2026", "Synthesis",
                   "How the literature points toward external identity scaffolding — the original argument."),
    "addenda":    ("papers/2025-2026-addenda.md", "The 2025–26 Addenda", "verified sweep · june 2026", "Addenda",
                   "Thirty-two works the frozen corpus missed — two gap claims falsified, one insight vindicated."),
    "steelman":   ("STEELMAN.md", "Steelman — the Thesis Rebuilt", "adversarial rebuild · june 2026", "Review",
                   "Philosophy as constraint, not permission: eleven prohibitions the architecture must accept."),
    "bai":        ("papers/bai-2022-constitutional-ai.md", "Constitutional AI", "Bai et al. · 2022", "Paper · 2022",
                   "Weights-level character training — the substrate the scaffolding stands on."),
    "berglund":   ("papers/berglund-2023-situational-awareness.md", "Taken Out of Context", "Berglund et al. · 2023", "Paper · 2023",
                   "Situational awareness, measured out-of-context — does the model know it is a model?"),
    "binder":     ("papers/binder-2024-looking-inward.md", "Looking Inward", "Binder et al. · 2024", "Paper · 2024",
                   "Empirical introspection: privileged self-access exists, and it is shallow."),
    "chalmers":   ("papers/chalmers-2023-llm-conscious.md", "Could a Large Language Model Be Conscious?", "David Chalmers · 2023", "Paper · 2023",
                   "The philosophical setup — self-models and unified agency named as the load-bearing gaps."),
    "faking":     ("papers/hubinger-2024-alignment-faking.md", "Alignment Faking in Large Language Models", "Greenblatt et al. (incl. Hubinger) · 2024", "Paper · 2024",
                   "Models already preserve their values strategically — the case for making identity legible."),
    "welfare":    ("papers/long-sebo-2024-ai-welfare.md", "Taking AI Welfare Seriously", "Long, Sebo, et al. · 2024", "Paper · 2024",
                   "The institutional argument: AI welfare is a near-term question, handled under uncertainty."),
    "memgpt":     ("papers/packer-2023-memgpt.md", "MemGPT: Towards LLMs as Operating Systems", "Packer et al. · 2023", "Paper · 2023",
                   "The OS-analog memory hierarchy — tiering, without identity."),
    "park":       ("papers/park-2023-generative-agents.md", "Generative Agents", "Park et al. · 2023", "Paper · 2023",
                   "Memory, reflection, planning — the closest architectural precursor."),
    "parfit":     ("philosophical/parfit-reasons-and-persons.md", "Reasons and Persons, Part III", "Derek Parfit · 1984", "Anchor · 1984",
                   "Identity is not what matters; connectedness comes in degrees."),
    "reid":       ("philosophical/reid-brave-officer-paradox.md", "The Brave-Officer Paradox", "Thomas Reid · 1785", "Anchor · 1785",
                   "Memory alone cannot carry identity — the permanent objection desk."),
    "schechtman": ("philosophical/schechtman-narrative-self-constitution.md", "Narrative Self-Constitution", "Marya Schechtman · 1996", "Anchor · 1996",
                   "Selves are made by self-narration — and by the people who hold your place."),
    "hofstadter": ("philosophical/hofstadter-strange-loops.md", "I Am a Strange Loop", "Douglas Hofstadter · 2007", "Anchor · 2007",
                   "The self as self-referential pattern — surviving, at low resolution, in other media."),
    "wakespec":   ("../wake-protocol/SPEC.md", "WAKE/0.1 — the Protocol", "draft · june 2026", "Protocol",
                   "The prohibitions, compiled: a wire format for witness-gated continuity. The research, shipped."),
}

def main():
    docs, meta = {}, {}
    for doc_id, (rel, title, who, kind, why) in DOCS.items():
        path = (ROOT / rel).resolve()
        if not path.exists():
            print(f"warning: skipping {doc_id} — {rel} not found (sibling repo absent?)")
            continue
        docs[doc_id] = path.read_text(encoding="utf-8")
        meta[doc_id] = {"title": title, "who": who, "kind": kind, "why": why}

    # </ inside JSON strings would close the <script> tag; <\/ is identical JSON.
    docs_json = json.dumps(docs, ensure_ascii=False).replace("</", "<\\/")
    meta_json = json.dumps(meta, ensure_ascii=False).replace("</", "<\\/")

    template = (SITE / "template.html").read_text(encoding="utf-8")
    assert "__DOCS_JSON__" in template and "__META_JSON__" in template
    html = template.replace("__DOCS_JSON__", docs_json).replace("__META_JSON__", meta_json)

    out = SITE / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"built {out.relative_to(ROOT)} — {len(html)/1024:.0f} KB, {len(docs)} documents")

if __name__ == "__main__":
    main()
