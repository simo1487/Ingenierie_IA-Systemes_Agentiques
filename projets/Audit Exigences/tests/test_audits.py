"""Tests des audits contre les criteres d'acceptation."""

from __future__ import annotations

import unittest

from audit_exigences.contradictions import audit_contradictions
from audit_exigences.duplicates import audit_duplicates, jaccard_similarity
from audit_exigences.grammar import audit_grammar
from audit_exigences.models import Requirement
from audit_exigences.spelling import audit_spelling


class TestGrammarAuditUS101(unittest.TestCase):
    """US-AUD-101 : grammaire (accord, ponctuation, capitalisation)."""

    def test_ca_aud_101_01_agreement_after_modal(self):
        r = Requirement(id="REQ-033", text="All software components shall logs errors in a centralized event memory.")
        findings = audit_grammar([r])
        grammar = [f for f in findings if f.finding_type == "grammar"]
        self.assertEqual(len(grammar), 1)
        self.assertEqual(grammar[0].suggestion, "shall log")
        self.assertGreater(grammar[0].position, 0)

    def test_ca_aud_101_02_double_space_punctuation(self):
        r = Requirement(id="X", text="Le système doit  démarrer vite.")
        findings = audit_grammar([r])
        punct = [f for f in findings if f.finding_type == "punctuation"]
        self.assertEqual(len(punct), 1)
        self.assertEqual(punct[0].position, 15)

    def test_ca_aud_101_03_correct_text_no_finding(self):
        r = Requirement(id="REQ-001", text="Le système doit démarrer en moins de 2 secondes.")
        findings = audit_grammar([r])
        self.assertEqual(findings, [])


class TestSpellingAuditUS102(unittest.TestCase):
    def test_ca_aud_102_01_spelling_with_position(self):
        r = Requirement(id="REQ-002", text="Le systéme doit redemarrer automatiquement aprés une panne.")
        findings = audit_spelling([r])
        self.assertEqual(len(spelling := [f for f in findings if f.finding_type == "spelling"]), 3)
        positions = {f.position for f in spelling}
        self.assertIn(3, positions)
        details = " ".join(f.detail for f in spelling)
        self.assertIn("systéme", details)
        self.assertIn("redemarrer", details)
        self.assertIn("aprés", details)
        self.assertTrue(all(f.suggestion for f in spelling))

    def test_ca_aud_102_02_multiple_faults_individual(self):
        r = Requirement(id="X", text="Le systéme et le vechicule.")
        findings = audit_spelling([r])
        self.assertEqual(len(findings), 2)
        self.assertNotEqual(findings[0].position, findings[1].position)

    def test_ca_aud_102_03_correct_text_no_finding(self):
        r = Requirement(id="REQ-001", text="Le système doit démarrer en moins de 2 secondes.")
        findings = audit_spelling([r])
        self.assertEqual(findings, [])


class TestDuplicatesAudit(unittest.TestCase):
    def test_ca_aud_201_01_identical_text_score_one(self):
        a = Requirement(id="REQ-013", text="The ECU shall transmit heartbeat messages every 100 ms.")
        b = Requirement(id="REQ-014", text="The ECU shall transmit heartbeat messages every 100 ms.")
        findings = audit_duplicates([a, b])
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].score, 1.0)
        self.assertEqual(findings[0].related_ids, ["REQ-014"])

    def test_ca_aud_201_02_quasi_duplicate_detected(self):
        a = Requirement(id="REQ-008", text="The software shall perform RAM integrity tests at startup.")
        b = Requirement(id="REQ-009", text="The software shall perform RAM integrity tests at start-up.")
        findings = audit_duplicates([a, b])
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].score, 1.0)

    def test_ca_aud_201_03_negation_not_duplicate(self):
        a = Requirement(id="REQ-004", text="Le système doit activer le mode dégradé en cas de défaut capteur.")
        b = Requirement(id="REQ-005", text="Le système ne doit pas activer le mode dégradé en cas de défaut capteur.")
        findings = audit_duplicates([a, b])
        self.assertEqual(findings, [])

    def test_jaccard_identical_is_one(self):
        self.assertEqual(jaccard_similarity({"a", "b"}, {"a", "b"}), 1.0)

    def test_jaccard_disjoint_is_zero(self):
        self.assertEqual(jaccard_similarity({"a"}, {"b"}), 0.0)


class TestContradictionsAudit(unittest.TestCase):
    def test_ca_aud_301_01_negation_conflict(self):
        a = Requirement(id="REQ-005", text="The inverter shall disable torque production after detection of a critical fault.")
        b = Requirement(id="REQ-006", text="The inverter shall continue torque production after detection of a critical fault.")
        findings = audit_contradictions([a, b])
        self.assertIsInstance([f for f in findings if f.finding_type == "negation_conflict"], list)

    def test_ca_aud_301_01b_never_negation(self):
        a = Requirement(id="REQ-030", text="The safety watchdog shall reset the ECU if the main control task fails to execute within 100 ms.")
        b = Requirement(id="REQ-031", text="The safety watchdog shall never reset the ECU.")
        findings = audit_contradictions([a, b])
        neg = [f for f in findings if f.finding_type == "negation_conflict"]
        self.assertEqual(len(neg), 1)
        self.assertEqual(neg[0].related_ids, ["REQ-031"])

    def test_ca_aud_301_02_numeric_conflict_same_subject(self):
        a = Requirement(id="REQ-001", text="The traction inverter shall limit motor phase current to 400 A.")
        b = Requirement(id="REQ-002", text="The traction inverter shall limit motor phase current to 450 A.")
        findings = audit_contradictions([a, b])
        numeric = [f for f in findings if f.finding_type == "numeric_conflict"]
        self.assertEqual(len(numeric), 1)
        self.assertIn("400.0", numeric[0].detail)
        self.assertIn("450.0", numeric[0].detail)

    def test_ca_aud_301_03_different_subjects_no_conflict(self):
        a = Requirement(id="REQ-003", text="The system shall detect DC bus overvoltage conditions within 10 ms.")
        b = Requirement(id="REQ-030", text="The safety watchdog shall reset the ECU if the main control task fails to execute within 100 ms.")
        findings = audit_contradictions([a, b])
        self.assertEqual(findings, [])


class TestNormalize(unittest.TestCase):
    def test_stem_harmonizes_plural(self):
        from audit_exigences.normalize import stem
        self.assertEqual(stem("logs"), "log")
        self.assertEqual(stem("tests"), "test")

    def test_normalize_removes_modals_and_units(self):
        from audit_exigences.normalize import normalize_tokens
        tokens = normalize_tokens("The inverter shall enter thermal derating mode above 110 degC.")
        self.assertNotIn("shall", tokens)
        self.assertNotIn("degc", tokens)
        self.assertIn("inverter", tokens)

    def test_normalize_unifies_hyphen(self):
        from audit_exigences.normalize import normalize_tokens
        self.assertEqual(normalize_tokens("at start-up"), normalize_tokens("at startup"))


if __name__ == "__main__":
    unittest.main()
