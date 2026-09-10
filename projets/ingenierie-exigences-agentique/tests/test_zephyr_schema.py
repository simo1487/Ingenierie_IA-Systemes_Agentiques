import json
import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"),
)

from zephyr_collector.schema import ValidationError, validate_requirement

SCHEMA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "zephyr-requirements.schema.json",
)


class TestRequirementSchema(unittest.TestCase):
    def setUp(self):
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            self.schema = json.load(f)

    def test_schema_file_is_valid_json(self):
        self.assertIn("required", self.schema)
        self.assertIn("properties", self.schema)

    def test_valid_requirement_passes(self):
        requirement = {
            "requirement_id": "ZEP-SRS-ATOMIC-001",
            "requirement_text": "The kernel must provide atomic services.",
            "reformulation": False,
            "title": "Atomic service",
            "category": "software_requirements",
            "subcategory": "atomic_service",
            "source_url": (
                "https://zephyrproject-rtos.github.io/reqmgmt/"
                "docs/software_requirements/atomic_service.html"
            ),
            "source_path": None,
            "source_revision": None,
            "status": "Observé",
            "confidence": "Candidat",
            "implementation_links": [],
            "test_links": [],
            "automotive_mapping": [],
            "traceability": {},
            "audit": {},
            "ambiguities": [],
        }
        validate_requirement(requirement, self.schema)

    def test_missing_required_fields_fails(self):
        requirement = {
            "requirement_id": "ZEP-SRS-ATOMIC-001",
            "category": "software_requirements",
        }
        with self.assertRaises(ValidationError):
            validate_requirement(requirement, self.schema)

    def test_empty_text_fails(self):
        requirement = {
            "requirement_id": "ZEP-SRS-ATOMIC-001",
            "requirement_text": "",
            "category": "software_requirements",
            "subcategory": "atomic_service",
            "source_url": "https://example.com",
            "status": "Observé",
            "confidence": "Candidat",
        }
        with self.assertRaises(ValidationError):
            validate_requirement(requirement, self.schema)

    def test_invalid_category_fails(self):
        requirement = {
            "requirement_id": "ZEP-SRS-ATOMIC-001",
            "requirement_text": "The kernel must provide atomic services.",
            "category": "not_a_category",
            "subcategory": "atomic_service",
            "source_url": "https://example.com",
            "status": "Observé",
            "confidence": "Candidat",
        }
        with self.assertRaises(ValidationError):
            validate_requirement(requirement, self.schema)

    def test_null_identifier_is_allowed(self):
        requirement = {
            "requirement_id": None,
            "requirement_text": "An observed statement without an identifier.",
            "category": "software_requirements",
            "subcategory": "unknown",
            "source_url": "https://example.com",
            "status": "Bloqué",
            "confidence": "Candidat",
        }
        validate_requirement(requirement, self.schema)


if __name__ == "__main__":
    unittest.main()
