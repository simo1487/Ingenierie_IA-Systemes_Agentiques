"""Retrieval des chunks pertinents depuis ChromaDB."""

from __future__ import annotations

from typing import Any

from src.config import DEFAULT_TOP_K


def retrieve_chunks(
    vector_store: Any,
    query: str,
    top_k: int = DEFAULT_TOP_K,
) -> list[dict[str, Any]]:
    """Recherche les chunks les plus pertinents pour une question.

    Args:
        vector_store: instance ChromaDB.
        query: question utilisateur.
        top_k: nombre de chunks a retourner.

    Returns:
        Liste de chunks avec score et metadonnees.
    """
    results = vector_store.similarity_search_with_score(query, k=top_k)

    citations = []
    for rank, (doc, score) in enumerate(results, start=1):
        citations.append({
            "rank": rank,
            "score": round(float(score), 4),
            "content": doc.page_content,
            "source": doc.metadata.get("source", "inconnu"),
            "section": doc.metadata.get("section", "inconnu"),
            "chunk_id": doc.metadata.get("chunk_id", "inconnu"),
        })

    return citations
