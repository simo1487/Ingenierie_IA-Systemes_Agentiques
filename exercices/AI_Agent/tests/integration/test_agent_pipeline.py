"""Tests d'integration de l'agent."""

from __future__ import annotations

from unittest.mock import patch


def test_agent_answers_with_sources(fresh_agent, fixture_dir):
    fresh_agent.index_documents(fixture_dir)

    # Patcher la reference importee dans src.agent
    with patch("src.agent.generate_answer") as mock_llm:
        mock_llm.return_value = "The CPU0 runs at 800 MHz."
        result = fresh_agent.answer("What is the CPU0 frequency?")

        assert result["status"] == "answered"
        assert "CPU0" in result["answer"]
        assert "Sources:" in result["answer"]
        assert len(result["citations"]) > 0


def test_agent_abstains_out_of_corpus(fresh_agent, fixture_dir):
    fresh_agent.index_documents(fixture_dir)

    # Patcher la reference importee dans src.agent
    with patch("src.agent.retrieve_chunks") as mock_retrieve:
        # Simule un retrieval sans chunks pertinents
        mock_retrieve.return_value = [
            {
                "rank": 1,
                "score": 0.20,
                "content": "irrelevant",
                "source": "test.md",
                "section": "Test",
                "chunk_id": "c1",
            }
        ]
        result = fresh_agent.answer("Protocole de routage BGP sur reseau 5G")
        assert result["status"] == "abstained"
        assert "I could not find the information" in result["answer"]
