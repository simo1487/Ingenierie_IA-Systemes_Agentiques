"""Generation de reponses via le backend LLM configure."""

from __future__ import annotations

from typing import Any

from src.config import LLM_BACKEND


def generate_answer(question: str, citations: list[dict[str, Any]]) -> str:
    """Genere une reponse avec le backend configure."""
    if LLM_BACKEND == "fake":
        from src.llm_backends.fake_backend import FakeLLMBackend
        backend = FakeLLMBackend()
    elif LLM_BACKEND == "mistral":
        from src.llm_backends.mistral_backend import MistralLLMBackend
        backend = MistralLLMBackend()
    else:
        raise ValueError(f"Backend LLM inconnu : {LLM_BACKEND}. Utilisez 'mistral' ou 'fake'.")

    return backend.generate(question, citations)
