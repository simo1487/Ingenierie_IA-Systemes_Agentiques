"""Pipeline d'ingestion RAG : Chargement, Découpage et Indexation dans Qdrant.

Étapes :
1. Lecture des documents du corpus (normes, qualité, open source, exigences).
2. Découpage structurel (Markdown / Chunks) avec conservation des métadonnées de traçabilité.
3. Génération des embeddings et stockage dans la collection Qdrant via LlamaIndex.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

# Permet l'exécution directe en script indépendant ou via module
_project_root = Path(__file__).resolve().parents[3]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter

from exercices.rag.config.qdrant_config import (
    build_storage_context,
    get_qdrant_client,
    DEFAULT_COLLECTION_NAME,
    DEFAULT_VECTOR_SIZE,
)


def load_corpus_documents(corpus_dir: Path | str) -> list[Document]:
    """Charge les fichiers d'exemples en documents LlamaIndex avec métadonnées."""
    corpus_path = Path(corpus_dir)
    documents: list[Document] = []

    for file_path in sorted(corpus_path.iterdir()):
        if file_path.suffix.lower() in {".md", ".txt"}:
            text = file_path.read_text(encoding="utf-8")
            doc = Document(
                text=text,
                metadata={
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "format": "markdown",
                    "source_project": file_path.stem.split("_")[1] if "_" in file_path.stem else "commun",
                },
            )
            documents.append(doc)
        elif file_path.suffix.lower() == ".json":
            content = json.loads(file_path.read_text(encoding="utf-8"))
            text = json.dumps(content, ensure_ascii=False, indent=2)
            doc = Document(
                text=text,
                metadata={
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "format": "json",
                    "source_project": "open_source",
                },
            )
            documents.append(doc)

    return documents


def ingest_corpus(
    corpus_dir: Path | str,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    qdrant_mode: str = "memory",
    embed_model: Any | None = None,
    recreate: bool = True,
) -> VectorStoreIndex:
    """Ingère le corpus dans Qdrant et retourne l'index LlamaIndex."""
    documents = load_corpus_documents(corpus_dir)

    client = get_qdrant_client(mode=qdrant_mode)
    storage_context, _ = build_storage_context(
        client=client,
        collection_name=collection_name,
        vector_size=DEFAULT_VECTOR_SIZE,
        recreate=recreate,
    )

    # Découpage structurel
    node_parser = MarkdownNodeParser.from_defaults()

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        transformations=[node_parser],
        embed_model=embed_model,
        show_progress=False,
    )

    return index


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    sample_dir = current_dir.parent / "data" / "sample_corpus"

    print(f"Chargement du corpus depuis : {sample_dir}")
    docs = load_corpus_documents(sample_dir)
    print(f"Documents chargés : {len(docs)}")
    for d in docs:
        print(f" - {d.metadata['file_name']} ({len(d.text)} caractères)")
