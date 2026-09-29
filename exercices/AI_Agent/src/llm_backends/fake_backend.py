"""Backend LLM factice pour tests sans API."""

from __future__ import annotations

import re
from typing import Any


def _tokenize(text: str) -> set[str]:
    """Tokenise un texte en minuscules."""
    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))


class FakeLLMBackend:
    """Backend factice qui genere une reponse a partir du contexte.

    Extraction améliorée : choisit la phrase la plus pertinente.
    """

    def generate(self, question: str, citations: list[dict[str, Any]]) -> str:
        if not citations:
            return "I could not find the information in the provided documents."

        question_tokens = _tokenize(question)

        # Trouver la phrase la plus pertinente dans tous les chunks
        best_score = 0
        best_sentence = citations[0]["content"].strip()

        for cit in citations:
            content = cit["content"].strip()
            sentences = re.split(r"(?<=[.!?])\s+", content)
            for sentence in sentences:
                score = len(question_tokens & _tokenize(sentence))
                if score > best_score:
                    best_score = score
                    best_sentence = sentence

        if not best_sentence:
            best_sentence = citations[0]["content"].strip()[:200]

        # Réponses spécifiques selon la question
        q_lower = question.lower()
        content_lower = citations[0]["content"].lower()

        if "frequency" in q_lower and ("mhz" in content_lower or "ghz" in content_lower):
            match = re.search(r"(\d+(?:\.\d+)?)\s*(MHz|GHz)", citations[0]["content"], re.IGNORECASE)
            if match:
                return f"The maximum frequency is {match.group(1)} {match.group(2)}."

        if "how many" in q_lower:
            numbers = re.findall(r"\b(\d+)\b", citations[0]["content"])
            if numbers:
                return f"The answer is {numbers[0]}."

        if "what" in q_lower and ("support" in q_lower or "supported" in q_lower):
            items = re.findall(r"- ([^\n]+)", citations[0]["content"])
            if items:
                return "Supported items: " + ", ".join(items[:5]) + "."

        return best_sentence
