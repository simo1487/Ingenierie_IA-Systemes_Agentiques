"""Verification de la sortie des audits contre les oracles figes.

Les oracles sont definis dans tests/fixtures/*_oracle.json AVANT verification.
Ce test confronte la sortie reelle de l'outil aux attendus de l'oracle :
- chaque finding attendu doit etre present ;
- chaque non-detection attendue doit rester absente (anti-tautologie).
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from audit_exigences.contradictions import audit_contradictions
from audit_exigences.duplicates import audit_duplicates
from audit_exigences.grammar import audit_grammar
from audit_exigences.llm_backends.fake_backend import FakeLLMBackend
from audit_exigences.loader import load_dataset
from audit_exigences.semantic import audit_semantic, pairs_from_findings
from audit_exigences.spelling import audit_spelling

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET = PROJECT_ROOT / "data" / "exigences_sample.json"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _load_oracle(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def _pair_key(pair: list[str]) -> frozenset:
    return frozenset(pair)


class TestSpellingOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requirements = load_dataset(DATASET)
        cls.findings = audit_spelling(cls.requirements)
        cls.oracle = _load_oracle("spelling_oracle.json")

    def test_expected_findings_present(self):
        for expected in self.oracle["expected_findings"]:
            matches = [
                f for f in self.findings
                if f.requirement_id == expected["requirement_id"]
                and f.finding_type == expected["type"]
                and expected["detail_contains"] in f.detail
            ]
            self.assertTrue(matches, f"Finding attendu absent : {expected}")
            self.assertEqual(matches[0].suggestion, expected["suggestion"])

    def test_expected_non_detections_absent(self):
        for nd in self.oracle["expected_non_detections"]:
            leaks = [f for f in self.findings if f.requirement_id == nd["requirement_id"]]
            self.assertEqual(leaks, [], f"Faux positif pour {nd['requirement_id']} : {leaks}")


class TestGrammarOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requirements = load_dataset(DATASET)
        cls.findings = audit_grammar(cls.requirements)
        cls.oracle = _load_oracle("grammar_oracle.json")

    def test_expected_findings_present(self):
        for expected in self.oracle["expected_findings"]:
            matches = [
                f for f in self.findings
                if f.requirement_id == expected["requirement_id"]
                and f.finding_type == expected["type"]
                and expected["detail_contains"] in f.detail
            ]
            self.assertTrue(matches, f"Finding attendu absent : {expected}")
            self.assertEqual(matches[0].suggestion, expected["suggestion"])

    def test_expected_non_detections_absent(self):
        for nd in self.oracle["expected_non_detections"]:
            leaks = [f for f in self.findings if f.requirement_id == nd["requirement_id"]]
            self.assertEqual(leaks, [], f"Faux positif pour {nd['requirement_id']} : {leaks}")


class TestDuplicatesOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requirements = load_dataset(DATASET)
        cls.oracle = _load_oracle("duplicates_oracle.json")
        cls.findings = audit_duplicates(cls.requirements, threshold=cls.oracle["threshold"])

    def _pairs(self):
        return {
            _pair_key([f.requirement_id, *f.related_ids]): f for f in self.findings
        }

    def test_expected_pairs_present(self):
        pairs = self._pairs()
        for expected in self.oracle["expected_findings"]:
            key = _pair_key(expected["pair"])
            self.assertIn(key, pairs := self._pairs(), f"Paire attendue absente : {expected['pair']}")
            self.assertGreaterEqual(pairs[key].score, expected["min_score"])

    def test_expected_non_detections_absent(self):
        pairs = self._pairs()
        for nd in self.oracle["expected_non_detections"]:
            key = _pair_key(nd["pair"])
            self.assertNotIn(
                key, pairs,
                f"Faux positif de duplication pour {nd['pair']} : {pairs.get(key)}",
            )


class TestContradictionsOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requirements = load_dataset(DATASET)
        cls.findings = audit_contradictions(cls.requirements)
        cls.oracle = _load_oracle("contradictions_oracle.json")

    def test_expected_pairs_present(self):
        for expected in self.oracle["expected_findings"]:
            pair = expected["pair"]
            matches = [
                f for f in self.findings
                if f.requirement_id == pair[0]
                and pair[1] in f.related_ids
                and f.finding_type == expected["type"]
            ]
            self.assertTrue(matches, f"Contradiction attendue absente : {pair}")
            for token in expected.get("detail_contains", []):
                self.assertIn(token, matches[0].detail)

    def test_expected_non_detections_absent(self):
        for nd in self.oracle["expected_non_detections"]:
            pair = nd["pair"]
            leaks = [
                f for f in self.findings
                if f.requirement_id == pair[0] and pair[1] in f.related_ids
            ]
            self.assertEqual(
                leaks, [],
                f"Faux positif non attendu pour {pair} : {leaks}",
            )


class TestSemanticOracle(unittest.TestCase):
    """Conformite de l'audit semantique (EPIC-04) avec le backend fake.

    Le fake stub le pipeline ; la qualite semantique reelle est evaluee
    par l'ecosysteme DeepEval (EPIC-AUD-05) avec un vrai modele.
    """

    @classmethod
    def setUpClass(cls):
        cls.requirements = load_dataset(DATASET)
        cls.oracle = _load_oracle("semantic_oracle.json")
        deterministic = (
            audit_duplicates(cls.requirements, threshold=0.85)
            + audit_contradictions(cls.requirements)
        )
        cls.findings = audit_semantic(
            cls.requirements,
            FakeLLMBackend(),
            exclude_pairs=pairs_from_findings(deterministic),
        )

    def _pairs(self):
        return {
            _pair_key([f.requirement_id, *f.related_ids]): f for f in self.findings
        }

    def test_expected_findings_present(self):
        pairs = self._pairs()
        for expected in self.oracle["expected_findings"]:
            key = _pair_key(expected["pair"])
            self.assertIn(key, pairs, f"Finding semantique attendu absent : {expected['pair']}")
            self.assertEqual(pairs[key].finding_type, expected["type"])

    def test_expected_non_detections_absent(self):
        pairs = self._pairs()
        for nd in self.oracle["expected_non_detections"]:
            key = _pair_key(nd["pair"])
            self.assertNotIn(
                key, pairs,
                f"Faux positif semantique pour {nd['pair']} : {pairs.get(key)}",
            )

    def test_already_flagged_pairs_excluded(self):
        pairs = self._pairs()
        for pair in self.oracle["excluded_already_flagged"]:
            key = _pair_key(pair)
            self.assertNotIn(
                key, pairs,
                f"Paire deja detectee re-signalee en semantique : {pair}",
            )


if __name__ == "__main__":
    unittest.main()
