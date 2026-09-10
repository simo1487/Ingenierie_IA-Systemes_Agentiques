"""Exercice 2 : Indexation du corpus multi-projets dans Qdrant avec LlamaIndex.

Objectif :
- Charger les documents issus des projets fusionnés (normes, qualité, open source, exigences).
- Initialiser le client Qdrant en mémoire ou sur disque.
- Indexer les chunks avec leurs métadonnées pour permettre un filtrage ultérieur.
"""

from __future__ import annotations

import sys
from pathlib import Path
from qdrant_client import QdrantClient

# Permet l'import quel que soit le dossier de lancement
_project_root = Path(__file__).resolve().parents[3]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from exercices.rag.config.qdrant_config import (
    get_qdrant_client,
    build_storage_context,
    get_embedding_model,
    DEFAULT_COLLECTION_NAME,
)
from exercices.rag.pipeline.ingestion import load_corpus_documents
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.node_parser import MarkdownNodeParser


def run_indexing_exercise(mode: str = "memory") -> tuple[VectorStoreIndex, QdrantClient]:
    current_dir = Path(__file__).resolve().parent
    sample_dir = current_dir.parent / "data" / "sample_corpus"

    print("=================================================================")
    print("EXERCICE 2 : INDEXATION MULTI-PROJETS DANS QDRANT")
    print("=================================================================")
    print(f"1. Chargement des documents depuis {sample_dir}...")
    documents = load_corpus_documents(sample_dir)
    print(f"   -> {len(documents)} documents trouvés.")

    print(f"2. Connexion à Qdrant (mode: {mode})...")
    client = get_qdrant_client(mode=mode)
    storage_context, _ = build_storage_context(
        client=client,
        collection_name=DEFAULT_COLLECTION_NAME,
        recreate=True,
    )

    print("3. Configuration de l'embedding déterministe et découpage...")
    embed_model = get_embedding_model()
    Settings.embed_model = embed_model
    node_parser = MarkdownNodeParser.from_defaults()

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        transformations=[node_parser],
        embed_model=embed_model,
        show_progress=False,
    )

    collection_info = client.get_collection(DEFAULT_COLLECTION_NAME)
    print("4. Indexation terminée avec succès !")
    print(f"   Points / vecteurs enregistrés dans Qdrant : {collection_info.points_count}")

    return index, client


if __name__ == "__main__":
    run_indexing_exercise(mode="memory")
