"""Technique 4 : Découpage Sémantique (SemanticSplitterNodeParser).

Adaptation : prend en entrée le fichier automotive-spice-exigences.md
(Automotive SPICE PAM v4.0 - 211 exigences) au lieu d'un texte codé en dur.

Principe :
- Calcule la similarité sémantique (embedding) entre phrases successives.
- Lorsqu'une rupture thématique est détectée (distance supérieure à un seuil statistique),
  une frontière de chunk est posée.
- Permet de regrouper les phrases par thématique cohérente plutôt que par nombre arbitraire de caractères.

Sans modèle d'embedding disponible, bascule sur un découpage par frontières de paragraphes
(méthode de repli pour l'apprentissage).

Par défaut, utilise HuggingFaceEmbedding (Qwen/Qwen3-Embedding-0.6B),
le meilleur modèle d'embedding multilingue libre (MIT) praticable sur CPU
d'après le classement MTEB/MMTEB.

Sortie : NEW_TEXT_RESULTS/04_semantic_chunking.json
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from llama_index.core import Document

SOURCE_FILE = (
    Path(__file__).resolve().parents[4]
    / "projets"
    / "normes"
    / "exigences"
    / "automotive-spice-exigences.md"
)
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"

EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def load_source_text() -> str:
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Fichier source introuvable : {SOURCE_FILE}")
    return SOURCE_FILE.read_text(encoding="utf-8")


def demonstrate_semantic_chunking(
    text: str,
    embed_model: Any | None = None,
    breakpoint_percentile_threshold: int = 90,
) -> list[dict]:
    """Découpe le document ASPICE par rupture sémantique.

    Si embed_model est fourni, utilise SemanticSplitterNodeParser de LlamaIndex.
    Sinon, simule la coupure sur les paragraphes thématiques pour l'apprentissage.
    """
    doc = Document(text=text, metadata={"source": SOURCE_FILE.name})

    try:
        from llama_index.core.node_parser import SemanticSplitterNodeParser

        if embed_model is not None:
            splitter = SemanticSplitterNodeParser(
                buffer_size=1,
                breakpoint_percentile_threshold=breakpoint_percentile_threshold,
                embed_model=embed_model,
            )
            nodes = splitter.get_nodes_from_documents([doc])
            return [
                {"chunk_index": i, "text": n.get_content(), "method": "semantic_embedding"}
                for i, n in enumerate(nodes, start=1)
            ]
    except (ImportError, Exception):
        pass

    # Découpage logique de repli si aucun modèle d'embedding n'est configuré
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return [
        {"chunk_index": i, "text": p, "method": "paragraph_boundary_fallback"}
        for i, p in enumerate(paragraphs, start=1)
    ]


if __name__ == "__main__":
    text = load_source_text()

    embed_model = None
    try:
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding

        embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)
    except Exception as exc:
        print(f"Modèle d'embedding indisponible ({exc}) → repli par frontières de paragraphes")

    chunks = demonstrate_semantic_chunking(
        text,
        embed_model=embed_model,
        breakpoint_percentile_threshold=90,
    )

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "04_semantic_chunking.json"
    methods = sorted({c["method"] for c in chunks})
    payload = {
        "script": "04_semantic_chunking.py",
        "source_file": SOURCE_FILE.name,
        "parameters": {
            "embed_model": EMBED_MODEL_NAME if embed_model is not None else None,
            "breakpoint_percentile_threshold": 90,
        },
        "methods": methods,
        "chunk_count": len(chunks),
        "chunks": chunks,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK {out_path} — {len(chunks)} chunks (méthodes : {', '.join(methods)})")
