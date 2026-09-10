"""Pipeline de recherche (Retrieval) et génération de citations sourcées.

Fonctionnalités :
1. Recherche vectorielle top-k dans Qdrant.
2. Filtrage par métadonnées (par projet, par type de document, par statut).
3. Formatage structuré des citations et gestion explicite de l'abstention.
"""

from __future__ import annotations

from typing import Any
from llama_index.core import VectorStoreIndex
from llama_index.core.vector_stores import MetadataFilter, MetadataFilters, FilterOperator


def retrieve_with_citations(
    index: VectorStoreIndex,
    query: str,
    top_k: int = 3,
    min_score: float = 0.5,
    project_filter: str | None = None,
) -> dict[str, Any]:
    """Recherche les passages pertinents dans l'index Qdrant et formate les citations."""
    filters = None
    if project_filter:
        filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="source_project",
                    value=project_filter,
                    operator=FilterOperator.EQ,
                )
            ]
        )

    retriever = index.as_retriever(
        similarity_top_k=top_k,
        filters=filters,
    )

    nodes_with_scores = retriever.retrieve(query)

    citations = []
    for rank, node_with_score in enumerate(nodes_with_scores, start=1):
        score = node_with_score.score or 0.0
        node = node_with_score.node
        citations.append({
            "rank": rank,
            "score": round(score, 4),
            "file_name": node.metadata.get("file_name", "inconnu"),
            "source_project": node.metadata.get("source_project", "inconnu"),
            "content_snippet": node.get_content().strip()[:250],
            "full_content": node.get_content(),
            "metadata": node.metadata,
        })

    # Gestion de l'abstention si aucun résultat ou si le score est sous le seuil
    if not citations or (citations[0]["score"] < min_score):
        return {
            "query": query,
            "status": "not_found",
            "reason": "Aucun passage du corpus n'atteint le seuil de pertinence minimal.",
            "citations": citations,
        }

    return {
        "query": query,
        "status": "found",
        "top_k": top_k,
        "citations": citations,
    }


def format_citation_report(result: dict[str, Any]) -> str:
    """Met en forme lisible le résultat d'une recherche RAG."""
    lines = [
        f"=== REQUÊTE : {result['query']} ===",
        f"Statut : {result['status']}",
    ]
    if result["status"] == "not_found":
        lines.append(f"Motif d'abstention : {result.get('reason')}")

    for cit in result.get("citations", []):
        lines.append(
            f"\n[Citation #{cit['rank']}] Score: {cit['score']} | Source: {cit['file_name']} (Projet: {cit['source_project']})"
        )
        lines.append(f"Extrait : {cit['content_snippet']}...")

    return "\n".join(lines)
