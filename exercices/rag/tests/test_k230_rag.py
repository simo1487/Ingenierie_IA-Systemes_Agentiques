"""Tests RAG pour le K230 Datasheet.

Objectif :
- Charger une liste de questions de reference avec reponses attendues.
- Pour chaque question, effectuer un retrieval top-k.
- Verifier si un chunk pertinent est retourne.
- Generer un rapport de test controllable dans tests/.
"""

from __future__ import annotations

import io
import json
import sys
import time
from pathlib import Path

# Set UTF-8 encoding for output
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Permet l'import quel que soit le dossier de lancement
_project_root = Path(__file__).resolve().parents[3]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from exercices.rag.exercices.exo2_k230_indexation_qdrant import run_k230_indexation
from exercices.rag.exercices.exo3_k230_retrieval_and_citations import retrieve_k230_citations


def is_chunk_relevant(chunk_content: str, expected_keywords: list[str]) -> bool:
    """Retourne True si le contenu contient au moins un des mots-cles attendus."""
    content = chunk_content.lower()
    for keyword in expected_keywords:
        if keyword.lower() in content:
            return True
    return False


def run_k230_rag_tests(top_k: int = 3, min_score: float = 0.5):
    print("=================================================================")
    print("TEST RAG K230 : BATTERIE DE 30 QUESTIONS")
    print("=================================================================")

    # 1. Indexation
    print("\n1. Initialisation de l'index K230 avec HuggingFace...")
    index, _ = run_k230_indexation(mode="memory")

    # 2. Chargement des questions
    test_dir = Path(__file__).resolve().parent
    queries_file = test_dir / "k230_test_queries.json"

    print(f"\n2. Chargement des questions depuis {queries_file}...")
    with open(queries_file, 'r', encoding='utf-8') as f:
        queries = json.load(f)
    print(f"   -> {len(queries)} questions chargees.")

    # 3. Evaluation
    print(f"\n3. Evaluation RAG (top_k={top_k}, min_score={min_score})...")
    results = []
    found_count = 0
    reciprocal_ranks = []
    start_time = time.time()

    for q in queries:
        q_id = q["id"]
        question = q["question"]
        expected_answer = q.get("expected_answer", "")
        keywords = q["expected_keywords"]
        category = q["category"]

        result = retrieve_k230_citations(
            index=index,
            query=question,
            top_k=top_k,
            min_score=min_score,
        )

        relevant_rank = None
        citations_evaluated = []
        for citation in result.get("citations", []):
            is_relevant = is_chunk_relevant(citation["full_content"], keywords)
            citations_evaluated.append({
                "rank": citation["rank"],
                "score": citation["score"],
                "chunk_id": citation["chunk_id"],
                "relevant": is_relevant,
            })
            if is_relevant and relevant_rank is None:
                relevant_rank = citation["rank"]

        is_found = result["status"] == "found" and relevant_rank is not None
        if is_found:
            found_count += 1
            reciprocal_ranks.append(1.0 / relevant_rank)
        else:
            reciprocal_ranks.append(0.0)

        results.append({
            "id": q_id,
            "question": question,
            "expected_answer": expected_answer,
            "category": category,
            "status": result["status"],
            "relevant_rank": relevant_rank,
            "citations": citations_evaluated,
        })

    elapsed = time.time() - start_time

    # 4. Metriques
    total = len(queries)
    success_rate = found_count / total
    mrr = sum(reciprocal_ranks) / total
    avg_time = elapsed / total

    metrics = {
        "total_questions": total,
        "found_relevant": found_count,
        "success_rate": round(success_rate, 4),
        "mrr": round(mrr, 4),
        "total_time_seconds": round(elapsed, 2),
        "avg_time_per_query_seconds": round(avg_time, 4),
        "top_k": top_k,
        "min_score": min_score,
    }

    # 5. Sauvegarde du rapport
    report = {
        "metrics": metrics,
        "results": results,
    }
    report_file = test_dir / "k230_test_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # 6. Affichage des metriques
    print("\n=================================================================")
    print("METRIQUES")
    print("=================================================================")
    print(f"Total questions : {total}")
    print(f"Reponses pertinentes trouvees : {found_count}/{total}")
    print(f"Taux de reussite (precision@{top_k}) : {success_rate * 100:.1f}%")
    print(f"MRR (Mean Reciprocal Rank) : {mrr:.4f}")
    print(f"Temps total : {elapsed:.2f} s")
    print(f"Temps moyen par requete : {avg_time:.4f} s")
    print(f"\n[OK] Rapport de test sauvegarde dans : {report_file}")

    # 7. Recap par categorie
    print("\n=================================================================")
    print("TAUX DE REUSSITE PAR CATEGORIE")
    print("=================================================================")
    categories = {}
    for r in results:
        cat = r["category"]
        categories.setdefault(cat, {"total": 0, "found": 0})
        categories[cat]["total"] += 1
        if r["relevant_rank"] is not None:
            categories[cat]["found"] += 1

    for cat, stats in sorted(categories.items()):
        rate = (stats["found"] / stats["total"]) * 100 if stats["total"] > 0 else 0
        print(f"{cat:20s} : {stats['found']:2d}/{stats['total']:2d} ({rate:5.1f}%)")


if __name__ == "__main__":
    run_k230_rag_tests(top_k=3, min_score=0.5)
