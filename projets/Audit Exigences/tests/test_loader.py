"""Tests du loader."""

from __future__ import annotations

import unittest
from pathlib import Path

from audit_exigences.loader import load_dataset


class TestLoader(unittest.TestCase):
    def test_load_json_dataset(self):
        path = Path(__file__).resolve().parents[1] / "data" / "exigences_sample.json"
        requirements = load_dataset(path)
        self.assertEqual(len(requirements), 35)
        self.assertEqual(requirements[0].id, "REQ-001")
        self.assertTrue(all(r.text for r in requirements))

    def test_load_markdown(self):
        tmp = Path(__file__).resolve().parents[1] / "evidence" / "_tmp_md_test.md"
        tmp.parent.mkdir(exist_ok=True)
        tmp.write_text(
            "# Exigences\n\n- REQ-001 : Le système doit démarrer.\n- REQ-002 : Le BMS surveille la batterie.\n",
            encoding="utf-8",
        )
        try:
            requirements = load_dataset(tmp)
            self.assertEqual(len(requirements), 2)
            self.assertEqual(requirements[1].id, "REQ-002")
        finally:
            tmp.unlink(missing_ok=True)

    def test_load_empty_json(self):
        tmp = Path(__file__).resolve().parents[1] / "evidence" / "_tmp_empty.json"
        tmp.parent.mkdir(exist_ok=True)
        tmp.write_text('{"exigences": []}', encoding="utf-8")
        try:
            self.assertEqual(load_dataset(tmp), [])
        finally:
            tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
