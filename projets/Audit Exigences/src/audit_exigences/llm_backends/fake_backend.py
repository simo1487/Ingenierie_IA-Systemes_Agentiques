"""Backend LLM deterministe pour les tests hors-ligne.

STUB DE TEST : ce backend ne fait pas d'analyse semantique reelle.
Il produit des verdicts via un lexique d'antonymes et une carte de
synonymes figes, uniquement pour exercer le pipeline (prompt, parsing,
findings) sans LLM. La qualite semantique reelle est evaluee par
l'ecosysteme DeepEval avec un vrai modele (EPIC-AUD-05).
"""

from __future__ import annotations

import json
import re

from audit_exigences.llm_backends.base import LLMBackend
from audit_exigences.normalize import normalize_tokens

# Paires de verbes semantiquement opposes (figees pour les tests)
OPPOSING_VERBS = [
    ("disable", "continue"),
    ("erase", "retain"),
]

# Synonymes figes pour simuler la detection de paraphrases
SYNONYMS = {
    "record": "store",
    "store": "store",
}

_UNIT_RE = re.compile(r"\d+(?:[.,]\d+)?\s*(mbps|kbps)", re.IGNORECASE)


class FakeLLMBackend(LLMBackend):
    """Verdicts deterministes pour les tests hors-ligne du pipeline."""

    name = "fake"

    def generate(self, prompt: str) -> str:
        text_a, text_b = _extract_pair(prompt)
        verdict = self._classify(text_a, text_b)
        return json.dumps(verdict, ensure_ascii=False)

    def _classify(self, text_a: str, text_b: str) -> dict:
        low_a, low_b = text_a.lower(), text_b.lower()

        for verb_x, verb_y in OPPOSING_VERBS:
            if (verb_x in low_a and verb_y in low_b) or (
                verb_y in low_a and verb_x in low_b
            ):
                return {
                    "verdict": "contradiction",
                    "rationale": f"Actions opposees '{verb_x}' vs '{verb_y}' (stub).",
                }

        units_a = set(_UNIT_RE.findall(low_a))
        units_b = set(_UNIT_RE.findall(low_b))
        if units_a and units_b and units_a != units_b:
            return {
                "verdict": "contradiction",
                "rationale": "Unites de debit differentes (stub).",
            }

        if _synonym_tokens(text_a) == _synonym_tokens(text_b):
            return {
                "verdict": "duplicate",
                "rationale": "Tokens equivalents apres synonymes figes (stub).",
            }

        return {"verdict": "ok", "rationale": "Aucune opposition du lexique (stub)."}


def _extract_pair(prompt: str) -> tuple[str, str]:
    """Extrait les deux textes d'exigence du prompt structure."""
    match_a = re.search(r"\[REQ-A\]\s*(.+?)\s*\[REQ-B\]", prompt, re.DOTALL)
    match_b = re.search(r"\[REQ-B\]\s*(.+?)\s*\[\/REQ-B\]", prompt, re.DOTALL)
    text_a = match_a.group(1) if match_a else ""
    text_b = match_b.group(1) if match_b else ""
    return text_a, text_b


def _synonym_tokens(text: str) -> set[str]:
    return {SYNONYMS.get(t, t) for t in normalize_tokens(text)}
