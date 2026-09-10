import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"),
)

from zephyr_collector.audit import audit_requirement


class TestAuditRequirement(unittest.TestCase):
    def test_valid_requirement_is_observed(self):
        req = {
            "requirement_id": "ZEP-SRS-26-1",
            "requirement_text": "The RTOS shall define an atomic variable type.",
            "source_url": "https://example.com",
            "category": "software_requirements",
            "subcategory": "atomic_service",
            "status": "Observé",
            "confidence": "Candidat",
        }
        audited = audit_requirement(req)
        self.assertEqual(audited["audit"]["singularite"], "Candidat")
        self.assertEqual(audited["audit"]["clarte"], "Candidat")
        self.assertEqual(audited["audit"]["verifiabilite"], "Candidat")
        self.assertEqual(audited["status"], "Observé")
        self.assertEqual(audited["ambiguities"], [])

    def test_missing_identifier_blocks(self):
        req = {
            "requirement_id": None,
            "requirement_text": "A statement with no identifier.",
            "source_url": "https://example.com",
            "category": "software_requirements",
            "subcategory": "atomic_service",
            "status": "Observé",
            "confidence": "Candidat",
        }
        audited = audit_requirement(req)
        self.assertEqual(audited["status"], "Bloqué")
        self.assertIn("requirement_id", " ".join(audited["ambiguities"]))
        self.assertEqual(audited["audit"]["verifiabilite"], "Bloqué")

    def test_missing_text_blocks(self):
        req = {
            "requirement_id": "ZEP-SRS-26-1",
            "requirement_text": "",
            "source_url": "https://example.com",
            "category": "software_requirements",
            "subcategory": "atomic_service",
            "status": "Observé",
            "confidence": "Candidat",
        }
        audited = audit_requirement(req)
        self.assertEqual(audited["status"], "Bloqué")
        self.assertIn("requirement_text", " ".join(audited["ambiguities"]))
        self.assertEqual(audited["audit"]["clarte"], "Bloqué")

    def test_unverifiable_source_url_blocks(self):
        req = {
            "requirement_id": "ZEP-SRS-26-1",
            "requirement_text": "The RTOS shall do something.",
            "source_url": "",
            "category": "software_requirements",
            "subcategory": "atomic_service",
            "status": "Observé",
            "confidence": "Candidat",
        }
        audited = audit_requirement(req)
        self.assertEqual(audited["status"], "Bloqué")
        self.assertIn("source_url", " ".join(audited["ambiguities"]))
