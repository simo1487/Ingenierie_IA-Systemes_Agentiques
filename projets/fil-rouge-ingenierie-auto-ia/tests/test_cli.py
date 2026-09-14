from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from auto_ai_flow.cli import main


class CliTests(unittest.TestCase):
    def test_cli_writes_a_reproducible_report(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            code = main([
                "--input", str(PROJECT / "data" / "demo_baseline.json"),
                "--output", str(output),
            ])
            report = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(code, 0)
        self.assertEqual(report["status"], "ready-for-human-review")


if __name__ == "__main__":
    unittest.main()
