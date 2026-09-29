"""Exercice 2 bis : Indexation du corpus K230 dans Qdrant avec LlamaIndex.

Objectif :
- Charger les chunks K230 générés par le chunking adapté.
- Initialiser le client Qdrant en mémoire.
- Indexer les chunks avec leurs métadonnées pour l'exercice 3 (retrieval).
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

from llama_index.core import Document, VectorStoreIndex, Settings
from qdrant_client import QdrantClient

# Permet l'import quel que soit le dossier de lancement
_project_root = Path(__file__).resolve().parents[3]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from exercices.rag.config.qdrant_config import (
    get_qdrant_client,
    build_storage_context,
    get_embedding_model,
)


def run_k230_indexation(mode: str = "memory"):
    current_dir = Path(__file__).resolve().parent
    output_dir = current_dir.parent / "output"
    chunks_file = output_dir / "k230_adapted_chunks.json"
    collection_name = "k230_datasheet_corpus"
    vector_size = 384

    print("=================================================================")
    print("EXERCICE 2 BIS : INDEXATION K230 DANS QDRANT")
    print("=================================================================")

    # 1. Chargement des chunks depuis le JSON
    print(f"1. Chargement des chunks depuis {chunks_file}...")
    with open(chunks_file, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    print(f"   -> {len(chunks)} chunks trouvés.")

    # 2. Conversion en documents LlamaIndex
    documents = [
        Document(
            text=chunk["content"],
            metadata={
                "chunk_id": chunk["chunk_id"],
                "chunk_index": chunk["chunk_index"],
                "source_file": chunk["source_file"],
                "char_length": chunk["char_length"],
                "header_path": chunk.get("header_path", ""),
                "parser": chunk["metadata"].get("parser", ""),
            }
        )
        for chunk in chunks
    ]
    print(f"   -> {len(documents)} documents créés.")

    # 3. Connexion Qdrant
    print(f"2. Connexion à Qdrant (mode: {mode})...")
    client = get_qdrant_client(mode=mode)
    storage_context, _ = build_storage_context(
        client=client,
        collection_name=collection_name,
        vector_size=vector_size,
        recreate=True,
    )

    # 4. Configuration embedding
    print("3. Configuration de l'embedding HuggingFace (BAAI/bge-small-en-v1.5)...")
    embed_model = get_embedding_model("huggingface")
    print(f"   Modele charge : {embed_model}")
    Settings.embed_model = embed_model

    # 5. Indexation
    print("4. Indexation des chunks dans Qdrant...")
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        embed_model=embed_model,
        show_progress=False,
    )

    collection_info = client.get_collection(collection_name)
    points_count = collection_info.points_count
    print("5. Indexation terminée avec succès !")
    print(f"   Points / vecteurs enregistrés dans Qdrant : {points_count}")

    # 6. Sauvegarde des infos pour l'exercice 3
    index_info = {
        "collection_name": collection_name,
        "mode": mode,
        "vector_size": vector_size,
        "chunks_count": len(chunks),
        "points_count": points_count,
        "chunks_file": str(chunks_file),
        "document_type": "K230 Datasheet",
    }
    
    index_info_file = output_dir / "k230_index_info.json"
    with open(index_info_file, 'w', encoding='utf-8') as f:
        json.dump(index_info, f, ensure_ascii=False, indent=2)
    
    print(f"\n[OK] Infos d'indexation sauvegardées dans : {index_info_file}")
    print("Pret pour l'exercice 3 (retrieval)")

    return index, client


if __name__ == "__main__":
    run_k230_indexation(mode="memory")
