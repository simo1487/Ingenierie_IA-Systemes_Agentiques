from __future__ import annotations

import json
import os
import re
import urllib.request
from typing import Any, Protocol


class AIProvider(Protocol):
    name: str

    def generate(self, task: str, payload: dict[str, Any]) -> dict[str, Any]: ...


class DeterministicProvider:
    name = "deterministic-offline"

    def generate(self, task: str, payload: dict[str, Any]) -> dict[str, Any]:
        if task == "requirement":
            citation = payload["citations"][0]
            return {
                "id": "REQ-FIL-001",
                "statement": f"Le produit doit conserver une preuve traçable vers {citation['source_id']}:{citation['passage_id']}.",
                "rationale": "Proposition dérivée du passage le mieux classé, à valider par un ingénieur exigences.",
            }
        if task == "project-ranking":
            candidate = payload["candidate"]
            score = sum(
                2 for key in ("revision", "license", "requirements", "tests", "quality")
                if candidate.get(key)
            )
            return {"name": candidate["name"], "score": score, "max_score": 10}
        if task == "quality-advice":
            diagnostic = payload["diagnostic"]
            return {
                "diagnostic_id": diagnostic["id"],
                "proposal": "Examiner la cause, appliquer un correctif minimal sur une branche dédiée et relancer l'oracle indépendant.",
            }
        raise ValueError(f"Tâche IA inconnue : {task}")


class MistralProvider:
    name = "mistral"
    schemas = {
        "requirement": {"id": "REQ-*", "statement": "exigence singulière", "rationale": "justification sourcée"},
        "project-ranking": {"name": "nom fourni", "score": "entier 0-10", "max_score": 10},
        "quality-advice": {"diagnostic_id": "identifiant fourni", "proposal": "correction minimale proposée"},
    }

    def __init__(self, model: str = "mistral-small-latest", api_key: str | None = None):
        self.model = model
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
        if not self.api_key:
            raise RuntimeError("MISTRAL_API_KEY est requise pour le fournisseur Mistral.")

    def generate(self, task: str, payload: dict[str, Any]) -> dict[str, Any]:
        if task not in self.schemas:
            raise ValueError(f"Tâche IA inconnue : {task}")
        schema = self.schemas[task]
        prompt = (
            "Tu es un agent d'ingénierie automobile. Retourne uniquement un objet JSON conforme au schéma. "
            "Toute sortie est une proposition, cite les identifiants fournis, n'invente aucune preuve.\n"
            f"Tâche: {task}\nSchéma: {json.dumps(schema, ensure_ascii=False)}\n"
            f"Entrée: {json.dumps(payload, ensure_ascii=False)}"
        )
        body = json.dumps({
            "model": self.model,
            "temperature": 0,
            "messages": [{"role": "user", "content": prompt}],
        }).encode("utf-8")
        request = urllib.request.Request(
            "https://api.mistral.ai/v1/chat/completions",
            data=body,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=90) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = data["choices"][0]["message"]["content"]
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            raise ValueError("Mistral n'a pas retourné d'objet JSON.")
        result = json.loads(match.group(0))
        missing = set(schema) - result.keys()
        if missing:
            raise ValueError(f"Réponse Mistral incomplète : {', '.join(sorted(missing))}")
        return result
