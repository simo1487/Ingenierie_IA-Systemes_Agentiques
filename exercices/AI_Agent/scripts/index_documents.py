"""Script d'indexation d'un dossier de documents."""

from __future__ import annotations

import sys
from pathlib import Path

_project_root = Path(__file__).resolve().parents[1]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from src.agent import TechnicalQAAgent


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/index_documents.py <docs_dir>")
        sys.exit(1)

    docs_dir = Path(sys.argv[1])
    if not docs_dir.exists():
        print(f"Erreur : le repertoire n'existe pas : {docs_dir}")
        sys.exit(1)

    agent = TechnicalQAAgent()
    count = agent.index_documents(docs_dir)
    print(f"\n✅ Indexation terminee : {count} chunks ajoutes.")


if __name__ == "__main__":
    main()
