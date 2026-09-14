from __future__ import annotations

import re
from typing import Any

from .models import AgentResult, Status
from .providers import AIProvider


def _source(entry: dict[str, Any]) -> dict[str, str]:
    return {
        "source_id": str(entry.get("id", "inconnu")),
        "revision": str(entry.get("revision", "inconnue")),
    }


class CorpusAgent:
    name = "corpus"

    def run(self, manifest: dict[str, Any]) -> AgentResult:
        baselines = manifest.get("baselines", [])
        questions = [f"Révision manquante pour {item.get('id', 'source inconnue')}" for item in baselines if not item.get("revision")]
        status = Status.BLOCKED if questions or not baselines else Status.OBSERVED
        return AgentResult(
            self.name,
            status,
            {"baseline_count": len(baselines), "passage_count": sum(len(item.get("passages", [])) for item in baselines)},
            [_source(item) for item in baselines],
            questions,
        )


class RetrievalAgent:
    name = "rag"

    @staticmethod
    def _tokens(value: str) -> set[str]:
        return {token for token in re.findall(r"\w+", value.lower()) if len(token) > 3}

    def run(self, manifest: dict[str, Any]) -> AgentResult:
        query_tokens = self._tokens(manifest["objective"])
        candidates = []
        for baseline in manifest.get("baselines", []):
            for passage in baseline.get("passages", []):
                tokens = self._tokens(passage.get("text", ""))
                score = len(query_tokens & tokens) / max(len(query_tokens), 1)
                candidates.append({
                    "source_id": baseline["id"],
                    "revision": baseline["revision"],
                    "passage_id": passage["id"],
                    "text": passage["text"],
                    "score": round(score, 4),
                })
        citations = sorted(candidates, key=lambda item: item["score"], reverse=True)[:3]
        found = bool(citations and citations[0]["score"] > 0)
        return AgentResult(
            self.name,
            Status.OBSERVED if found else Status.UNVERIFIED,
            {"retrieval_status": "found" if found else "not_found", "citations": citations if found else []},
            [{"source_id": item["source_id"], "revision": item["revision"]} for item in citations if found],
            [] if found else ["Aucun passage ne correspond à l'objectif du lot."],
        )


class RequirementAgent:
    name = "requirements"

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def run(self, retrieval: AgentResult) -> AgentResult:
        citations = retrieval.payload.get("citations", [])
        if not citations:
            return AgentResult(self.name, Status.BLOCKED, {"requirements": []}, questions=["Le RAG n'a fourni aucune source exploitable."])
        proposal = self.provider.generate("requirement", {"citations": citations})
        proposal["status"] = Status.PROPOSAL.value
        proposal["citations"] = [{"source_id": item["source_id"], "passage_id": item["passage_id"]} for item in citations]
        return AgentResult(self.name, Status.PROPOSAL, {"requirements": [proposal]}, retrieval.sources)


class ProjectSelectionAgent:
    name = "project-selection"

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def run(self, manifest: dict[str, Any]) -> AgentResult:
        candidates = manifest.get("project_candidates", [])
        ranked = [self.provider.generate("project-ranking", {"candidate": item}) for item in candidates]
        for item in ranked:
            item["status"] = Status.PROPOSAL.value
        ranked.sort(key=lambda item: item.get("score", 0), reverse=True)
        questions = [f"Licence ou révision absente pour {item.get('name', 'candidat inconnu')}" for item in candidates if not item.get("license") or not item.get("revision")]
        return AgentResult(self.name, Status.PROPOSAL, {"ranking": ranked, "decision_required": True}, questions=questions)


class QualityAgent:
    name = "quality"

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def run(self, manifest: dict[str, Any]) -> AgentResult:
        diagnostics = manifest.get("quality_diagnostics", [])
        proposals = [self.provider.generate("quality-advice", {"diagnostic": item}) for item in diagnostics]
        for item in proposals:
            item["status"] = Status.PROPOSAL.value
        return AgentResult(
            self.name,
            Status.OBSERVED,
            {"diagnostics": diagnostics, "correction_proposals": proposals, "automatic_apply": False},
        )


class TraceabilityAgent:
    name = "traceability"

    def run(self, manifest: dict[str, Any], requirements: AgentResult) -> AgentResult:
        requirement_ids = {item["id"] for item in requirements.payload.get("requirements", [])}
        links = []
        for link in manifest.get("explicit_trace_links", []):
            if link.get("requirement_id") not in requirement_ids:
                continue
            verified = bool(link.get("oracle") and link.get("evidence"))
            links.append({**link, "status": Status.VERIFIED.value if verified else Status.PROPOSAL.value})
        return AgentResult(self.name, Status.OBSERVED, {"links": links, "lexical_inference": False})


class ReviewAgent:
    name = "review"

    def run(self, results: list[AgentResult]) -> AgentResult:
        blockers = [result.agent for result in results if result.status == Status.BLOCKED]
        questions = [question for result in results for question in result.questions]
        gate = "blocked" if blockers else "ready-for-human-review"
        return AgentResult(
            self.name,
            Status.BLOCKED if blockers else Status.PROPOSAL,
            {"gate": gate, "blocking_agents": blockers, "human_decision_required": True},
            questions=questions,
        )
