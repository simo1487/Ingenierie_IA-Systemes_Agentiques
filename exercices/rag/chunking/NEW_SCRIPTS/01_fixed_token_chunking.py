"""Technique 1 : Découpage par taille fixe (SentenceSplitter / TokenSplitter).

Adaptation : prend en entrée le fichier automotive-spice-exigences.md
(Automotive SPICE PAM v4.0 - 211 exigences) au lieu d'un texte codé en dur.

Principe :
- Découpe le texte en morceaux de taille bornée (tokens).
- Intègre un recouvrement (overlap) pour éviter de casser une exigence au milieu.
- Conserve les frontières de phrases quand c'est possible grâce à SentenceSplitter.

Sortie : NEW_TEXT_RESULTS/01_fixed_token_chunking.json
"""

from __future__ import annotations

import json
from pathlib import Path

from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter, TokenTextSplitter

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


def demonstrate_sentence_splitter(
    text: str, chunk_size: int = 512, chunk_overlap: int = 64
) -> list[dict]:
    """Découpe le document ASPICE avec SentenceSplitter de LlamaIndex."""
    doc = Document(text=text, metadata={"source": SOURCE_FILE.name, "type": "norme"})

    splitter = SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    nodes = splitter.get_nodes_from_documents([doc])

    return [
        {
            "chunk_index": idx,
            "text": node.get_content(),
            "char_length": len(node.get_content()),
            "metadata": node.metadata,
        }
        for idx, node in enumerate(nodes, start=1)
    ]


def demonstrate_token_splitter(
    text: str, chunk_size: int = 256, chunk_overlap: int = 32
) -> list[dict]:
    """Découpage brut par nombre de tokens avec TokenTextSplitter."""
    doc = Document(text=text, metadata={"source": SOURCE_FILE.name})

    splitter = TokenTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    nodes = splitter.get_nodes_from_documents([doc])
    return [
        {
            "chunk_index": idx,
            "text": node.get_content(),
            "char_length": len(node.get_content()),
        }
        for idx, node in enumerate(nodes, start=1)
    ]


if __name__ == "__main__":
    text = load_source_text()

    sentence_chunks = demonstrate_sentence_splitter(text, chunk_size=512, chunk_overlap=64)
    token_chunks = demonstrate_token_splitter(text, chunk_size=256, chunk_overlap=32)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "01_fixed_token_chunking.json"
    payload = {
        "script": "01_fixed_token_chunking.py",
        "source_file": SOURCE_FILE.name,
        "parameters": {
            "sentence_splitter": {"chunk_size": 512, "chunk_overlap": 64},
            "token_text_splitter": {"chunk_size": 256, "chunk_overlap": 32},
        },
        "sentence_splitter_chunk_count": len(sentence_chunks),
        "token_text_splitter_chunk_count": len(token_chunks),
        "sentence_splitter": sentence_chunks,
        "token_text_splitter": token_chunks,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"OK {out_path} — {len(sentence_chunks)} chunks (SentenceSplitter), "
        f"{len(token_chunks)} chunks (TokenTextSplitter)"
    )
