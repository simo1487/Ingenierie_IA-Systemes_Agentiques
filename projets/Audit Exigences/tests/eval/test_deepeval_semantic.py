"""Tests DeepEval de l'audit semantique (EPIC-AUD-05).

Evalue les verdicts du backend LM Studio contre les goldens figes
(tests/fixtures/semantic_oracle.json) avec un juge LLM local.

Prerequis : LM Studio lance sur LMSTUDIO_URL avec un modele charge.
Skippes automatiquement si deepeval absent ou LM Studio injoignable.
"""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from pathlib import Path

from audit_exigences.llm_backends.lmstudio_backend import LMStudioBackend
from audit_exigences.loader import load_dataset
from audit_exigences.semantic import build_prompt, parse_verdict

try:
    from eval.judge_model import LMStudioJudge, lmstudio_reachable
except ImportError:  # appel direct : python -m unittest tests.eval.test_deepeval_semantic
    from tests.eval.judge_model import LMStudioJudge, lmstudio_reachable

try:
    from deepeval.metrics import GEval, JsonCorrectnessMetric
    from deepeval.test_case import LLMTestCase
    from deepeval.test_case.llm_test_case import SingleTurnParams
    from pydantic import BaseModel

    class SemanticVerdict(BaseModel):
        verdict: str
        rationale: str

    DEEPEVAL_AVAILABLE = True
except ImportError:
    DEEPEVAL_AVAILABLE = False
    LLMTestCase = None  # type: ignore[assignment]
    SingleTurnParams = None  # type: ignore[assignment]
    SemanticVerdict = None  # type: ignore[assignment]

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET = PROJECT_ROOT / "data" / "exigences_sample.json"
ORACLE = PROJECT_ROOT / "tests" / "fixtures" / "semantic_oracle.json"
REPORT = PROJECT_ROOT / "evidence" / "deepeval-report.json"

_EVAL_RESULTS: list[dict] = []

_SKIP_REASON = "deepeval non installe ou LM Studio injoignable"


def _eval_ready() -> bool:
    return DEEPEVAL_AVAILABLE and lmstudio_reachable()


@unittest.skipUnless(_eval_ready(), _SKIP_REASON)
class TestSemanticVerdictsDeepEval(unittest.TestCase):
    """Evaluation LLM-as-judge des verdicts semantiques."""

    @classmethod
    def setUpClass(cls):
        cls.requirements = {r.id: r for r in load_dataset(DATASET)}
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.backend = LMStudioBackend(timeout=120.0)
        cls.judge = LMStudioJudge(timeout=120.0)
        cls.metrics = [
            JsonCorrectnessMetric(
                expected_schema=SemanticVerdict,
                model=cls.judge,
                threshold=0.5,
                async_mode=False,
            ),
            GEval(
                name="SemanticVerdictCorrectness",
                evaluation_steps=[
                    "Check whether the verdict field classifies the relationship between the two requirements correctly.",
                    "Check whether the rationale reflects the actual semantic relation between the requirements.",
                ],
                evaluation_params=[
                    SingleTurnParams.INPUT,
                    SingleTurnParams.ACTUAL_OUTPUT,
                    SingleTurnParams.EXPECTED_OUTPUT,
                ],
                model=cls.judge,
                threshold=0.5,
                async_mode=False,
            ),
        ]

    @classmethod
    def tearDownClass(cls):
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(
            json.dumps(
                {
                    "run_id": f"deepeval-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}",
                    "judge": cls.judge.get_model_name(),
                    "results": _EVAL_RESULTS,
                    "status": "ready-for-human-review",
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    def _eval_pair(self, id_a: str, id_b: str, expected_verdict: str) -> None:
        req_a, req_b = self.requirements[id_a], self.requirements[id_b]
        raw = self.backend.generate(build_prompt(req_a, req_b))
        parsed = parse_verdict(raw)

        # Controle deterministe : le verdict produit correspond a l'oracle
        self.assertIsNotNone(parsed, f"Verdict inexploitable pour {id_a}/{id_b} : {raw}")
        self.assertEqual(
            parsed["verdict"],
            expected_verdict,
            f"Verdict attendu '{expected_verdict}', obtenu '{parsed['verdict']}' pour {id_a}/{id_b}",
        )

        test_case = LLMTestCase(
            input=f"{id_a}: {req_a.text}\n{id_b}: {req_b.text}",
            actual_output=raw,
            expected_output=json.dumps({"verdict": expected_verdict}),
        )
        scores = {}
        for metric in self.metrics:
            try:
                metric.measure(test_case)
            except Exception as exc:  # juge local incapable de produire le JSON attendu
                scores[metric.__name__] = {"score": None, "error": str(exc)[:200]}
                continue
            scores[metric.__name__] = {
                "score": metric.score,
                "reason": getattr(metric, "reason", ""),
            }
            self.assertGreaterEqual(
                metric.score,
                metric.threshold,
                f"{metric.__name__} sous le seuil pour {id_a}/{id_b} : {metric.score}",
            )

        _EVAL_RESULTS.append(
            {
                "pair": [id_a, id_b],
                "expected_verdict": expected_verdict,
                "actual_verdict": parsed["verdict"],
                "rationale": parsed["rationale"],
                "scores": scores,
            }
        )

    def test_expected_contradictions(self):
        for golden in self.oracle["expected_findings"]:
            if golden["verdict"] == "contradiction":
                with self.subTest(pair=golden["pair"]):
                    self._eval_pair(*golden["pair"], golden["verdict"])

    def test_expected_non_detections(self):
        for golden in self.oracle["expected_non_detections"]:
            with self.subTest(pair=golden["pair"]):
                self._eval_pair(*golden["pair"], golden["verdict"])


if __name__ == "__main__":
    unittest.main()
