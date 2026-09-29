"""Teste l'agent sur le corpus Zephyr kernel et genere un rapport."""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

_project_root = Path(__file__).resolve().parents[1]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from src.agent import TechnicalQAAgent


def main():
    parser = argparse.ArgumentParser(description="Teste l'agent sur le corpus Zephyr")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Nombre maximum de questions a tester",
    )
    args = parser.parse_args()
    data_dir = _project_root / "data"
    zephyr_file = data_dir / "zephyr_kernel.html"
    queries_file = _project_root / "tests" / "test_queries" / "zephyr_queries.json"
    report_dir = _project_root / "rapport"
    report_dir.mkdir(exist_ok=True)
    report_file = report_dir / "zephyr_test_report.json"

    if not zephyr_file.exists():
        print(f"Erreur : fichier Zephyr non trouve : {zephyr_file}")
        print("Lancez d'abord : python scripts/download_zephyr.py")
        sys.exit(1)

    if not queries_file.exists():
        print(f"Erreur : fichier de questions non trouve : {queries_file}")
        sys.exit(1)

    # Backend par defaut : fake si non configure
    backend = os.getenv("LLM_BACKEND", "fake")
    embed_backend = os.getenv("EMBEDDING_BACKEND", "fake")
    print(f"Backend LLM : {backend}")
    print(f"Backend Embeddings : {embed_backend}")

    print("\n1. Indexation du corpus Zephyr...")
    agent = TechnicalQAAgent(
        persist_dir=_project_root / "chroma_db_zephyr",
        collection_name="zephyr_kernel",
    )
    count = agent.index_documents(data_dir)
    print(f"   -> {count} chunks indexes.\n")

    print("2. Chargement des questions...")
    with open(queries_file, "r", encoding="utf-8") as f:
        queries = json.load(f)
    print(f"   -> {len(queries)} questions.\n")

    if args.limit is not None:
        queries = queries[: args.limit]
        print(f"   -> Limite a {len(queries)} questions.\n")

    print("3. Evaluation...")
    results = []
    found_count = 0
    for q in queries:
        result = agent.answer(q["question"])
        answer_lower = result["answer"].lower()
        keywords = [k.lower() for k in q["expected_keywords"]]
        matched_keywords = [k for k in keywords if k in answer_lower]
        is_relevant = len(matched_keywords) > 0
        if is_relevant:
            found_count += 1

        results.append({
            "id": q["id"],
            "question": q["question"],
            "category": q["category"],
            "status": result["status"],
            "answer": result["answer"],
            "citations": result["citations"],
            "expected_keywords": q["expected_keywords"],
            "matched_keywords": matched_keywords,
            "is_relevant": is_relevant,
        })

    total = len(queries)
    success_rate = found_count / total if total > 0 else 0

    report = {
        "corpus": str(zephyr_file),
        "total_questions_tested": total,
        "found_relevant": found_count,
        "success_rate": round(success_rate, 4),
        "llm_backend": backend,
        "embedding_backend": embed_backend,
        "results": results,
    }

    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n========================================")
    print(f"Total questions : {total}")
    print(f"Reponses pertinentes : {found_count}/{total}")
    print(f"Taux de reussite : {success_rate * 100:.1f}%")
    print(f"\n[OK] Rapport sauvegarde dans : {report_file}")
    print(f"========================================")


if __name__ == "__main__":
    main()
