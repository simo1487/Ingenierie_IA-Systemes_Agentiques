"""Tests end-to-end sur le jeu de 30 questions K230.

Ces tests necessitent une clé API Mistral valide.
Marquer comme skipped si MISTRAL_API_KEY n'est pas definie.
"""

from __future__ import annotations

import json
import os

import pytest

from src.agent import TechnicalQAAgent


@pytest.mark.skipif(
    not os.getenv("MISTRAL_API_KEY"),
    reason="MISTRAL_API_KEY non definie",
)
def test_k230_questions(fresh_agent, test_queries_path):
    fresh_agent.index_documents(
        test_queries_path.parents[2] / "fixtures"
    )

    with open(test_queries_path, "r", encoding="utf-8") as f:
        queries = json.load(f)

    success = 0
    for q in queries[:5]:  # Limiter a 5 questions en E2E
        result = fresh_agent.answer(q["question"])
        expected_keywords = [k.lower() for k in q["expected_keywords"]]
        answer_lower = result["answer"].lower()
        if any(k in answer_lower for k in expected_keywords):
            success += 1

    assert success >= 3, f"Seulement {success}/5 reponses pertinentes"


@pytest.mark.skipif(
    not os.getenv("MISTRAL_API_KEY"),
    reason="MISTRAL_API_KEY non definie",
)
def test_k230_abstention(fresh_agent, test_queries_path):
    fresh_agent.index_documents(
        test_queries_path.parents[2] / "fixtures"
    )

    out_of_corpus = [
        "What is the capital of France?",
        "Explain quantum computing in detail.",
    ]
    abstained = 0
    for q in out_of_corpus:
        result = fresh_agent.answer(q)
        if result["status"] == "abstained":
            abstained += 1

    assert abstained >= 1
