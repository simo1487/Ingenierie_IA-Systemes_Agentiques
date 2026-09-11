"""Demo de l'agent sans appel API Mistral.

Utilise le backend 'fake' pour tester le pipeline complet : loader, parser,
chunker, vector store, retriever, generation.
"""

from __future__ import annotations

import io
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

_project_root = Path(__file__).resolve().parents[1]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

# Force les backends factices (pas d'appel API)
os.environ["LLM_BACKEND"] = "fake"
os.environ["EMBEDDING_BACKEND"] = "fake"
os.environ.setdefault("MISTRAL_API_KEY", "fake_key_for_demo")

from src.agent import TechnicalQAAgent


def main():
    fixture_dir = _project_root / "tests" / "fixtures"
    if not fixture_dir.exists():
        print(f"Fixtures non trouves : {fixture_dir}")
        sys.exit(1)

    agent = TechnicalQAAgent(persist_dir=_project_root / "chroma_db_demo")
    count = agent.index_documents(fixture_dir)
    print(f"\n✅ {count} chunks indexes (backend fake).\n")

    questions = [
        "What is the maximum operating frequency of CPU0?",
        "How many I2C interfaces are supported?",
        "What is the capital of France?",
    ]

    for question in questions:
        result = agent.answer(question)
        print(f"Q: {question}")
        print(f"Status: {result['status']}")
        print(f"A: {result['answer']}\n")


if __name__ == "__main__":
    main()
