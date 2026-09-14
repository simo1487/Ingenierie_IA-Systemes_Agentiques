from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .agents import CorpusAgent, ProjectSelectionAgent, QualityAgent, RequirementAgent, RetrievalAgent, ReviewAgent, TraceabilityAgent
from .providers import AIProvider


class AutomotiveAIFlow:
    def __init__(self, provider: AIProvider):
        self.provider = provider

    def run(self, manifest: dict[str, Any]) -> dict[str, Any]:
        required = {"run_id", "objective", "baselines", "human_approvals"}
        missing = sorted(required - manifest.keys())
        if missing:
            raise ValueError(f"Champs de manifeste manquants : {', '.join(missing)}")
        approvals = manifest["human_approvals"]
        if not approvals.get("baselines"):
            return {
                "run_id": manifest["run_id"],
                "status": "Bloqué",
                "reason": "Les baselines doivent être approuvées par un humain avant l'exécution.",
                "results": [],
            }
        corpus = CorpusAgent().run(manifest)
        retrieval = RetrievalAgent().run(manifest)
        requirements = RequirementAgent(self.provider).run(retrieval)
        selection = ProjectSelectionAgent(self.provider).run(manifest)
        quality = QualityAgent(self.provider).run(manifest)
        traceability = TraceabilityAgent().run(manifest, requirements)
        stage_results = [corpus, retrieval, requirements, selection, quality, traceability]
        review = ReviewAgent().run(stage_results)
        return {
            "run_id": manifest["run_id"],
            "objective": manifest["objective"],
            "provider": self.provider.name,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "status": review.payload["gate"],
            "results": [result.to_dict() for result in [*stage_results, review]],
        }
