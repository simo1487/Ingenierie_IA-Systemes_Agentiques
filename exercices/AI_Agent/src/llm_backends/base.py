"""Interface de base pour les backends LLM."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseLLMBackend(ABC):
    """Classe abstraite pour les backends de generation de reponses."""

    @abstractmethod
    def generate(self, question: str, citations: list[dict[str, Any]]) -> str:
        """Genere une reponse a partir de la question et des chunks."""
        ...
