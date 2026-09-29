"""CLI de l'outil d'audit d'exigences."""

from __future__ import annotations

import argparse
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from audit_exigences.contradictions import audit_contradictions
from audit_exigences.duplicates import audit_duplicates
from audit_exigences.grammar import audit_grammar
from audit_exigences.loader import load_dataset
from audit_exigences.spelling import audit_spelling

ABSTENTION = "I could not find the information in the provided documents."


def run_audit(input_path: Path, output_path: Path, epics: list[int], threshold: float) -> dict:
    """Execute les audits selectionnes et ecrit le rapport JSON."""
    requirements = load_dataset(input_path)
    if not requirements:
        return {
            "run_id": _make_run_id(),
            "status": "abstained",
            "message": ABSTENTION,
        }

    findings = []
    if 1 in epics:
        findings.extend(audit_grammar(requirements))
        findings.extend(audit_spelling(requirements))
    if 2 in epics:
        findings.extend(audit_duplicates(requirements, threshold=threshold))
    if 3 in epics:
        findings.extend(audit_contradictions(requirements))

    report = {
        "run_id": _make_run_id(),
        "input": str(input_path),
        "requirements_count": len(requirements),
        "threshold": threshold if 2 in epics else None,
        "findings_count": len(findings),
        "findings": [f.to_dict() for f in findings],
        "status": "ready-for-human-review",
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return report


def _make_run_id() -> str:
    return f"audit-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit de qualite des exigences")
    parser.add_argument("--input", required=True, help="Dataset d'exigences (JSON ou Markdown)")
    parser.add_argument("--output", required=True, help="Rapport JSON de sortie")
    parser.add_argument(
        "--epic",
        type=int,
        action="append",
        choices=[1, 2, 3],
        help="EPIC a executer (repetable). Par defaut : tous.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Seuil de similarite pour la duplication (defaut : 0.85)",
    )
    args = parser.parse_args()

    epics = args.epic if args.epic else [1, 2, 3]
    report = run_audit(Path(args.input), Path(args.output), epics, args.threshold)

    print(f"Run         : {report['run_id']}")
    print(f"Exigences   : {report.get('requirements_count', 0)}")
    print(f"Anomalies   : {report.get('findings_count', 0)}")
    print(f"Statut      : {report['status']}")
    print(f"Rapport     : {args.output}")


if __name__ == "__main__":
    main()

