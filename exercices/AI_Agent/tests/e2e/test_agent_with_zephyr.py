"""Tests E2E sur le corpus Zephyr kernel.

Necessite que data/zephyr_kernel.html soit present.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from src.agent import TechnicalQAAgent


def _get_data_dir():
    return Path(__file__).resolve().parents[2] / "data"


def _get_queries_path():
    return Path(__file__).resolve().parents[2] / "tests" / "test_queries" / "zephyr_queries.json"


@pytest.fixture
def zephyr_agent(tmp_path):
    persist_dir = tmp_path / "chroma_zephyr"
    agent = TechnicalQAAgent(
        persist_dir=persist_dir,
        collection_name="zephyr_kernel_test",
    )
    data_dir = _get_data_dir()
    if not (data_dir / "zephyr_kernel.html").exists():
        pytest.skip("data/zephyr_kernel.html non telecharge")
    agent.index_documents(data_dir)
    return agent


def test_zephyr_30_questions(zephyr_agent):
    with open(_get_queries_path(), "r", encoding="utf-8") as f:
        queries = json.load(f)

    success = 0
    for q in queries:
        result = zephyr_agent.answer(q["question"])
        keywords = [k.lower() for k in q["expected_keywords"]]
        answer_lower = result["answer"].lower()
        if any(k in answer_lower for k in keywords):
            success += 1

    print(f"\nZephyr test : {success}/{len(queries)} reponses pertinentes")
    assert success > 0, "Aucune reponse pertinente"


@pytest.mark.skipif(
    os.getenv("LLM_BACKEND", "fake") == "fake",
    reason="Ce test est informatif avec le backend fake",
)
def test_zephyr_success_rate_above_threshold(zephyr_agent):
    with open(_get_queries_path(), "r", encoding="utf-8") as f:
        queries = json.load(f)

    success = 0
    for q in queries:
        result = zephyr_agent.answer(q["question"])
        keywords = [k.lower() for k in q["expected_keywords"]]
        answer_lower = result["answer"].lower()
        if any(k in answer_lower for k in keywords):
            success += 1

    rate = success / len(queries)
    print(f"\nZephyr success rate : {rate * 100:.1f}%")
    assert rate >= 0.5, f"Taux de reussite trop faible : {rate * 100:.1f}%"
