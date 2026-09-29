"""Interface des backends LLM."""

from __future__ import annotations

from abc import ABC, abstractmethod


class BackendUnavailableError(RuntimeError):
    """Levee quand le backend LLM est injoignable."""


class LLMBackend(ABC):
    """Contrat minimal : generer une completion texte a partir d'un prompt."""

    name: str = "unknown"

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Retourne la completion brute du modele pour le prompt donne."""
