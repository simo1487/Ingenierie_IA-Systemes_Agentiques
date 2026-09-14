from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from auto_ai_flow.agents import RetrievalAgent
from auto_ai_flow.orchestrator import AutomotiveAIFlow
from auto_ai_flow.providers import DeterministicProvider, MistralProvider


class AutomotiveAIFlowTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((PROJECT / "data" / "demo_baseline.json").read_text(encoding="utf-8"))

    def test_complete_offline_run_waits_for_human_review(self):
        report = AutomotiveAIFlow(DeterministicProvider()).run(self.manifest)
        self.assertEqual(report["status"], "ready-for-human-review")
        self.assertEqual(report["provider"], "deterministic-offline")
        self.assertEqual([item["agent"] for item in report["results"]], [
            "corpus", "rag", "requirements", "project-selection", "quality", "traceability", "review"
        ])
        by_agent = {item["agent"]: item for item in report["results"]}
        self.assertTrue(by_agent["rag"]["payload"]["citations"])
        self.assertEqual(by_agent["requirements"]["status"], "Proposition")
        self.assertFalse(by_agent["quality"]["payload"]["automatic_apply"])
        self.assertTrue(report["results"][-1]["payload"]["human_decision_required"])

    def test_run_is_blocked_without_human_baseline_approval(self):
        self.manifest["human_approvals"]["baselines"] = False
        report = AutomotiveAIFlow(DeterministicProvider()).run(self.manifest)
        self.assertEqual(report["status"], "Bloqué")
        self.assertEqual(report["results"], [])

    def test_traceability_is_verified_only_with_explicit_oracle_and_evidence(self):
        report = AutomotiveAIFlow(DeterministicProvider()).run(self.manifest)
        links = next(item for item in report["results"] if item["agent"] == "traceability")["payload"]["links"]
        self.assertEqual(links[0]["status"], "Vérifié")
        self.assertEqual(links[1]["status"], "Proposition")

    def test_rag_abstains_when_objective_has_no_matching_terms(self):
        self.manifest["objective"] = "gastronomie pâtisserie décoration"
        result = RetrievalAgent().run(self.manifest)
        self.assertEqual(result.payload["retrieval_status"], "not_found")
        self.assertEqual(result.payload["citations"], [])

    def test_mistral_provider_requires_an_external_secret(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "MISTRAL_API_KEY"):
                MistralProvider()


if __name__ == "__main__":
    unittest.main()
