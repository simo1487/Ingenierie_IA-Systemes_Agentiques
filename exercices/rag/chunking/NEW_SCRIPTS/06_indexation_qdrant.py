"""Indexation des chunks Markdown ASPICE dans Qdrant avec LlamaIndex.

Inspiré de exercices/rag/exercices/exo2_indexation_qdrant.py.

Objectif :
- Charger les chunks produits par 05_markdown_code_chunking.py (fichier
  NEW_TEXT_RESULTS/05_markdown_code_chunking.json).
- Créer une base Qdrant persistante sur disque (mode 'disk').
- Indexer chaque chunk tel quel (sans re-découpage) avec ses métadonnées
  (header_path, chunk_index, source) pour permettre un filtrage ultérieur.
- Vérifier l'indexation par un comptage des points et une requête de démonstration.

Sortie : NEW_TEXT_RESULTS/05_markdown_code_chunking_qdrant.json
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from qdrant_client import QdrantClient

# Permet l'import du module de config quel que soit le dossier de lancement
_project_root = Path(__file__).resolve().parents[4]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.schema import TextNode

from exercices.rag.config.qdrant_config import (
    build_storage_context,
    get_qdrant_client,
)

SOURCE_FILE = (
    Path(__file__).resolve().parents[4]
    / "projets"
    / "normes"
    / "exigences"
    / "automotive-spice-exigences.md"
)
CHUNKS_FILE = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS" / "05_markdown_code_chunking.json"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"
QDRANT_PATH = Path(__file__).resolve().parent / "qdrant_data"

COLLECTION_NAME = "aspice_exigences_markdown"
EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EMBED_DIM = 384


def load_chunks() -> list[dict]:
    """Charge les chunks Markdown produits par le script 05."""
    if not CHUNKS_FILE.exists():
        raise FileNotFoundError(
            f"Fichier de chunks introuvable : {CHUNKS_FILE}. "
            "Exécuter d'abord 05_markdown_code_chunking.py."
        )
    payload = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    return payload["markdown_chunks"]


def get_embedding_model():
    """Modèle d'embedding multilingue (déjà en cache), avec repli déterministe."""
    try:
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding

        return HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)
    except Exception as exc:
        print(f"[Avertissement] HuggingFaceEmbedding indisponible ({exc}) → DeterministicEmbedding")
        from exercices.rag.config.qdrant_config import DeterministicEmbedding

        return DeterministicEmbedding()


def run_indexing() -> tuple[VectorStoreIndex, QdrantClient, int]:
    print("=================================================================")
    print("INDEXATION DES CHUNKS MARKDOWN ASPICE DANS QDRANT")
    print("=================================================================")

    print(f"1. Chargement des chunks depuis {CHUNKS_FILE}...")
    chunks = load_chunks()
    print(f"   -> {len(chunks)} chunks chargés.")

    print("2. Conversion des chunks en TextNode (sans re-découpage)...")
    nodes = [
        TextNode(
            text=c["content"],
            metadata={
                "source": SOURCE_FILE.name,
                "chunk_index": c["chunk_index"],
                "header_path": c["header_path"],
            },
        )
        for c in chunks
    ]

    print(f"3. Connexion à Qdrant (mode: disk, path: {QDRANT_PATH})...")

    # Reconstruction from scratch : suppression du stockage local pour garantir
    # une base propre (le delete_collection du client local ne purge pas
    # de façon fiable les anciens points persistés sur disque).
    if QDRANT_PATH.exists():
        shutil.rmtree(QDRANT_PATH)
        print("   Ancien stockage qdrant_data supprimé (reconstruction à blanc).")

    client = get_qdrant_client(mode="disk", path=str(QDRANT_PATH))

    storage_context, _ = build_storage_context(
        client=client,
        collection_name=COLLECTION_NAME,
        vector_size=EMBED_DIM,
        recreate=False,
    )
    points_before = client.get_collection(COLLECTION_NAME).points_count
    if points_before != 0:
        raise RuntimeError(
            f"La collection '{COLLECTION_NAME}' devrait être vide, "
            f"{points_before} points trouvés."
        )
    print("   Collection vide, prête pour l'indexation.")

    print(f"4. Indexation avec {EMBED_MODEL_NAME}...")
    embed_model = get_embedding_model()
    Settings.embed_model = embed_model

    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context,
        embed_model=embed_model,
        show_progress=False,
    )

    collection_info = client.get_collection(COLLECTION_NAME)
    points_count = collection_info.points_count
    print(f"5. Indexation terminée : {points_count} points dans la collection '{COLLECTION_NAME}'.")

    return index, client, points_count


def run_demo_query(index, query: str = "Quelles sont les exigences de l'analyse des exigences logicielles SWE.1 ?") -> list[dict]:
    """Requête de démonstration pour prouver que la base est interrogeable."""
    retriever = index.as_retriever(similarity_top_k=3)
    results = []
    for node_with_score in retriever.retrieve(query):
        results.append(
            {
                "score": round(node_with_score.score or 0.0, 4),
                "header_path": node_with_score.node.metadata.get("header_path", ""),
                "text_preview": node_with_score.node.get_content()[:200],
            }
        )
    return results


if __name__ == "__main__":
    index, client, points_count = run_indexing()

    print("6. Requête de démonstration...")
    demo_query = "Quelles sont les exigences de l'analyse des exigences logicielles SWE.1 ?"
    demo_results = run_demo_query(index, demo_query)
    for r in demo_results:
        print(f"   score={r['score']} | {r['header_path']}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "05_markdown_code_chunking_qdrant.json"
    payload = {
        "script": "06_indexation_qdrant.py",
        "source_chunks_file": CHUNKS_FILE.name,
        "source_document": SOURCE_FILE.name,
        "qdrant": {
            "mode": "disk",
            "path": str(QDRANT_PATH),
            "collection_name": COLLECTION_NAME,
            "points_count": points_count,
        },
        "embedding": {"model": EMBED_MODEL_NAME, "dim": EMBED_DIM},
        "indexed_chunks": points_count,
        "demo_query": {"query": demo_query, "top_k": 3, "results": demo_results},
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK {out_path}")

    client.close()
    print("Client Qdrant fermé proprement.")
