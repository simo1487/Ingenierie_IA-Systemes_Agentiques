"""Technique 2 : Découpage par Fenêtre de Phrases (SentenceWindowNodeParser).

Adaptation : prend en entrée le fichier automotive-spice-exigences.md
(Automotive SPICE PAM v4.0 - 211 exigences) au lieu d'un texte codé en dur.

Principe :
- Chaque node extrait correspond à une phrase unique précise (idéal pour la recherche vectorielle).
- Une métadonnée spéciale 'window' stocke la phrase courante ainsi que k phrases avant et après.
- Lors de la recherche, on compare la requête à la phrase exacte, mais on transmet la fenêtre complète au générateur.

Sortie : NEW_TEXT_RESULTS/02_sentence_window_chunking.json
"""

from __future__ import annotations

import json
from pathlib import Path

from llama_index.core import Document
from llama_index.core.node_parser import SentenceWindowNodeParser

SOURCE_FILE = (
    Path(__file__).resolve().parents[4]
    / "projets"
    / "normes"
    / "exigences"
    / "automotive-spice-exigences.md"
)
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"


def load_source_text() -> str:
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Fichier source introuvable : {SOURCE_FILE}")
    return SOURCE_FILE.read_text(encoding="utf-8")


def demonstrate_sentence_window(
    text: str,
    window_size: int = 1,
    window_metadata_key: str = "window",
) -> list[dict]:
    """Découpe le document en phrases individuelles avec leur contexte de voisinage."""
    doc = Document(
        text=text,
        metadata={"source": SOURCE_FILE.name, "norme": "Automotive SPICE PAM v4.0"},
    )

    node_parser = SentenceWindowNodeParser.from_defaults(
        window_size=window_size,
        window_metadata_key=window_metadata_key,
        original_text_metadata_key="original_sentence",
    )

    nodes = node_parser.get_nodes_from_documents([doc])

    return [
        {
            "chunk_index": idx,
            "sentence": node.get_content(),
            "window_context": node.metadata.get(window_metadata_key, ""),
            "metadata": node.metadata,
        }
        for idx, node in enumerate(nodes, start=1)
    ]


if __name__ == "__main__":
    text = load_source_text()
    chunks = demonstrate_sentence_window(text, window_size=1)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "02_sentence_window_chunking.json"
    payload = {
        "script": "02_sentence_window_chunking.py",
        "source_file": SOURCE_FILE.name,
        "parameters": {"window_size": 1},
        "chunk_count": len(chunks),
        "chunks": chunks,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK {out_path} — {len(chunks)} nodes (fenêtre de phrases)")
