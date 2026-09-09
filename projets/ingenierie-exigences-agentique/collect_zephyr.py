"""Point d'entrée pour collecter les exigences Zephyr en JSON.

Usage:
    python collect_zephyr.py [OUTPUT_PATH] [--sample]

Sans --sample : collecte toutes les pages listées dans l'index.
Avec --sample : collecte uniquement la première page (test rapide).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError
from urllib.request import urlopen

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from zephyr_collector.audit import audit_requirement
from zephyr_collector.extract import parse_requirement_page
from zephyr_collector.index_loader import parse_index
from zephyr_collector.schema import ValidationError, validate_requirement


BASE_URL = "https://zephyrproject-rtos.github.io/reqmgmt/index.html"
SCHEMA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "zephyr-requirements.schema.json"
)


def _load_schema() -> dict:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _fetch_text(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode("utf-8")


def _collect_requirements(sources: list[dict]) -> tuple[list[dict], list[dict]]:
    requirements: list[dict] = []
    ambiguities: list[dict] = []
    schema = _load_schema()

    for source in sources:
        source_url = source["source_url"]
        try:
            page_html = _fetch_text(source_url)
            page_requirements = parse_requirement_page(
                page_html,
                source_url=source_url,
                category=source["category"],
                subcategory=source["subcategory"],
            )

            for req in page_requirements:
                audited = audit_requirement(req)
                try:
                    validate_requirement(audited, schema)
                    requirements.append(audited)
                except ValidationError as exc:
                    ambiguities.append(
                        {
                            "url": source_url,
                            "requirement_id": audited.get("requirement_id"),
                            "error": str(exc),
                        }
                    )

        except HTTPError as exc:
            ambiguities.append(
                {
                    "url": source_url,
                    "error": f"HTTP {exc.code}",
                }
            )
        except Exception as exc:
            ambiguities.append(
                {
                    "url": source_url,
                    "error": repr(exc),
                }
            )

    return requirements, ambiguities


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Collecte les exigences Zephyr reqmgmt en JSON."
    )
    parser.add_argument(
        "output",
        nargs="?",
        default="data/zephyr-requirements.json",
        help="Chemin du fichier JSON de sortie",
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Collecte uniquement la première page pour un test rapide",
    )
    args = parser.parse_args()

    index_html = _fetch_text(BASE_URL)
    sources = parse_index(index_html, BASE_URL)

    if args.sample:
        sources = [sources[0]] if sources else []

    requirements, ambiguities = _collect_requirements(sources)

    document = {
        "projet": "zephyr",
        "baseline_url": BASE_URL,
        "date_collecte": datetime.now(timezone.utc).isoformat(),
        "statut": "Proposition",
        "source_count": len(sources),
        "requirements_count": len(requirements),
        "requirements": requirements,
        "ambiguities": ambiguities,
    }

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(document, f, ensure_ascii=False, indent=2)

    print(f"Sources traitées : {len(sources)}")
    print(f"Exigences collectées : {len(requirements)}")
    print(f"Ambiguïtés / échecs : {len(ambiguities)}")
    print(f"Fichier généré : {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
