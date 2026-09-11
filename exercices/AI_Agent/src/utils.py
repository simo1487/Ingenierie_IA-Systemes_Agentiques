"""Utilitaires de validation et formatage."""

from __future__ import annotations

from typing import Any

from src.config import DEFAULT_SIMILARITY_THRESHOLD, ABSTENTION_MESSAGE


def filter_relevant_citations(
    citations: list[dict[str, Any]],
    threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
) -> list[dict[str, Any]]:
    """Filtre les citations dont le score depasse le seuil."""
    return [c for c in citations if c["score"] >= threshold]


def format_answer_with_sources(answer: str, citations: list[dict[str, Any]]) -> str:
    """Ajoute une section Sources a la reponse si elle n'existe pas deja."""
    if "Sources:" in answer:
        return answer.strip()

    sources = []
    for cit in citations:
        source_name = str(cit["source"]).split("/")[-1]
        section = cit["section"]
        sources.append(f"- {source_name} / {section}")

    sources_block = "\n".join(sources) if sources else "- Aucune source"
    return f"{answer}\n\nSources:\n{sources_block}"


def answer_or_abstain(
    question: str,
    citations: list[dict[str, Any]],
    llm_answer_func: Any,
    threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
) -> dict[str, Any]:
    """Decide de generer une reponse ou d'abstenir."""
    relevant = filter_relevant_citations(citations, threshold)

    if not relevant:
        return {
            "question": question,
            "status": "abstained",
            "answer": ABSTENTION_MESSAGE,
            "citations": citations,  # Retourne les citations pour debug
        }

    answer = llm_answer_func(question, relevant)
    formatted = format_answer_with_sources(answer, relevant)

    return {
        "question": question,
        "status": "answered",
        "answer": formatted,
        "citations": relevant,
    }
