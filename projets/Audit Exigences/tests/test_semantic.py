"""Tests unitaires de l'audit semantique (EPIC-AUD-04) avec backend fake."""

from __future__ import annotations

import unittest

from audit_exigences.llm_backends.fake_backend import FakeLLMBackend
from audit_exigences.llm_backends.base import LLMBackend
from audit_exigences.models import Requirement
from audit_exigences.semantic import (
    audit_semantic,
    build_prompt,
    find_candidate_pairs,
    pairs_from_findings,
    parse_verdict,
)


class FailingBackend(LLMBackend):
    name = "failing"

    def generate(self, prompt: str) -> str:
        from audit_exigences.llm_backends.base import BackendUnavailableError

        raise BackendUnavailableError("backend simule injoignable")


class TestCandidatePairs(unittest.TestCase):
    def test_pairs_share_subject_tokens(self):
        reqs = [
            Requirement(id="R1", text="The inverter shall disable torque production after detection of a critical fault."),
            Requirement(id="R2", text="The inverter shall continue torque production after detection of a critical fault."),
            Requirement(id="R3", text="The bootloader shall verify the digital signature of firmware images."),
        ]
        pairs = find_candidate_pairs(reqs)
        self.assertEqual(len(pairs), 1)
        self.assertEqual({pairs[0][0].id, pairs[0][1].id}, {"R1", "R2"})

    def test_excluded_pairs_are_skipped(self):
        reqs = [
            Requirement(id="R1", text="The inverter shall disable torque production after detection of a critical fault."),
            Requirement(id="R2", text="The inverter shall continue torque production after detection of a critical fault."),
        ]
        pairs = find_candidate_pairs(reqs, exclude_pairs={frozenset({"R1", "R2"})})
        self.assertEqual(pairs, [])


class TestPromptAndParsing(unittest.TestCase):
    def test_prompt_contains_both_texts(self):
        req_a = Requirement(id="R1", text="First requirement.")
        req_b = Requirement(id="R2", text="Second requirement.")
        prompt = build_prompt(req_a, req_b)
        self.assertIn("[REQ-A]", prompt)
        self.assertIn("First requirement.", prompt)
        self.assertIn("Second requirement.", prompt)

    def test_parse_valid_verdict(self):
        parsed = parse_verdict('{"verdict": "contradiction", "rationale": "opposed"}')
        self.assertEqual(parsed["verdict"], "contradiction")

    def test_parse_verdict_with_surrounding_text(self):
        raw = 'Sure! {"verdict": "ok", "rationale": "distinct"} done.'
        self.assertEqual(parse_verdict(raw)["verdict"], "ok")

    def test_parse_invalid_json_returns_none(self):
        self.assertIsNone(parse_verdict("not json at all"))

    def test_parse_unknown_verdict_returns_none(self):
        self.assertIsNone(parse_verdict('{"verdict": "maybe", "rationale": "x"}'))


class TestSemanticAuditFakeBackend(unittest.TestCase):
    def setUp(self):
        self.backend = FakeLLMBackend()

    def test_semantic_contradiction_detected(self):
        reqs = [
            Requirement(id="R1", text="The inverter shall disable torque production after detection of a critical fault."),
            Requirement(id="R2", text="The inverter shall continue torque production after detection of a critical fault."),
        ]
        findings = audit_semantic(reqs, self.backend)
        self.assertEqual(len(findings), 1)
        finding = findings[0]
        self.assertEqual(finding.finding_type, "semantic_contradiction")
        self.assertEqual(finding.epic, "semantic")
        self.assertEqual(finding.related_ids, ["R2"])
        self.assertEqual(finding.model, "fake")

    def test_semantic_duplicate_detected(self):
        reqs = [
            Requirement(id="R1", text="The ECU shall record diagnostic trouble codes in memory."),
            Requirement(id="R2", text="The ECU shall store diagnostic trouble codes in memory."),
        ]
        findings = audit_semantic(reqs, self.backend)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].finding_type, "semantic_duplicate")

    def test_ok_verdict_produces_no_finding(self):
        reqs = [
            Requirement(id="R1", text="The system shall detect DC bus overvoltage conditions within 10 ms."),
            Requirement(id="R2", text="The system shall detect DC bus undervoltage conditions within 10 ms."),
        ]
        findings = audit_semantic(reqs, self.backend)
        self.assertEqual(findings, [])

    def test_backend_unavailable_propagates(self):
        reqs = [
            Requirement(id="R1", text="The inverter shall disable torque production after detection of a critical fault."),
            Requirement(id="R2", text="The inverter shall continue torque production after detection of a critical fault."),
        ]
        from audit_exigences.llm_backends.base import BackendUnavailableError

        with self.assertRaises(BackendUnavailableError):
            audit_semantic(reqs, FailingBackend())


class TestPairsFromFindings(unittest.TestCase):
    def test_collects_related_pairs(self):
        from audit_exigences.models import Finding

        findings = [
            Finding(
                epic="duplicates",
                requirement_id="R1",
                finding_type="duplicate",
                position=0,
                detail="x",
                related_ids=["R2"],
            ),
            Finding(
                epic="grammar",
                requirement_id="R3",
                finding_type="grammar",
                position=5,
                detail="y",
            ),
        ]
        self.assertEqual(pairs_from_findings(findings), {frozenset({"R1", "R2"})})


if __name__ == "__main__":
    unittest.main()
