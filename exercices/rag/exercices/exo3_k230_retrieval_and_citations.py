"""Exercice 3 bis : Recherche et validation de citations sur le corpus K230.

Objectif :
- Poser des requêtes pertinentes sur la datasheet K230.
- Vérifier que chaque citation retournée pointe vers un chunk source et un score mesuré.
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path
from typing import Any

# Set UTF-8 encoding for output at module level
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Permet l'import quel que soit le dossier de lancement
_project_root = Path(__file__).resolve().parents[3]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from exercices.rag.exercices.exo2_k230_indexation_qdrant import run_k230_indexation
from llama_index.core import VectorStoreIndex


def retrieve_k230_citations(
    index: VectorStoreIndex,
    query: str,
    top_k: int = 2,
    min_score: float = 0.3,
) -> dict[str, Any]:
    """Recherche les passages pertinents dans l'index K230 et formate les citations."""
    retriever = index.as_retriever(similarity_top_k=top_k)
    nodes_with_scores = retriever.retrieve(query)

    citations = []
    for rank, node_with_score in enumerate(nodes_with_scores, start=1):
        score = node_with_score.score or 0.0
        node = node_with_score.node
        citations.append({
            "rank": rank,
            "score": round(score, 4),
            "file_name": node.metadata.get("source_file", "inconnu"),
            "chunk_id": node.metadata.get("chunk_id", "inconnu"),
            "chunk_index": node.metadata.get("chunk_index", 0),
            "content_snippet": node.get_content().strip()[:250],
            "full_content": node.get_content(),
            "metadata": node.metadata,
        })

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


def format_k230_citation_report(result: dict[str, Any]) -> str:
    """Met en forme lisible le resultat d'une recherche RAG."""
    lines = [
        f"=== REQUETE : {result['query']} ===",
        f"Statut : {result['status']}",
    ]
    if result["status"] == "not_found":
        lines.append(f"Motif d'abstention : {result.get('reason')}")

    for cit in result.get("citations", []):
        lines.append(
            f"\n[Citation #{cit['rank']}] Score: {cit['score']} | "
            f"Source: {cit['file_name']} (Chunk: {cit['chunk_id']})"
        )
        lines.append(f"Extrait : {cit['content_snippet']}...")

    return "\n".join(lines)


def run_k230_retrieval():
    print("=================================================================")
    print("EXERCICE 3 BIS : RECHERCHE ET CITATIONS SUR K230")
    print("=================================================================")

    # 1. Indexation (en mémoire) pour avoir un index disponible
    print("\n1. Initialisation de l'index K230...")
    index, _ = run_k230_indexation(mode="memory")

    # 2. Requêtes de test sur le K230
    queries = [
        {
            "titre": "Cas 1 : Fréquence CPU",
            "query": "What is the CPU frequency of K230?",
            "filter": None,
        },
        {
            "titre": "Cas 2 : Capacités KPU",
            "query": "KPU performance and supported neural networks",
            "filter": None,
        },
        {
            "titre": "Cas 3 : Interfaces vidéo",
            "query": "MIPI CSI and video input capabilities",
            "filter": None,
        },
        {
            "titre": "Cas 4 : Sécurité",
            "query": "AES and security boot features",
            "filter": None,
        },
        {
            "titre": "Cas 5 : Hors-corpus",
            "query": "Protocole de routage BGP sur réseau 5G",
            "filter": None,
        },
    ]

    # Collecte des résultats pour sauvegarde
    results = []
    for q in queries:
        print(f"\n\n>>> {q['titre']}")
        # Avec HuggingFace, le score moyen est plus eleve -> seuil releve a 0.62
        result = retrieve_k230_citations(
            index=index,
            query=q["query"],
            top_k=2,
            min_score=0.62,
        )
        print(format_k230_citation_report(result))
        results.append({
            "titre": q["titre"],
            **result,
        })

    # Sauvegarde du rapport de retrieval
    output_dir = Path(__file__).resolve().parent.parent / "output"
    output_dir.mkdir(exist_ok=True)
    report_file = output_dir / "k230_retrieval_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n\n[OK] Rapport de retrieval sauvegarde dans : {report_file}")


if __name__ == "__main__":
    run_k230_retrieval()
