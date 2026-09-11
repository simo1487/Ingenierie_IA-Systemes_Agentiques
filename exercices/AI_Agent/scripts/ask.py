"""Script CLI pour poser une question a l'agent."""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

_project_root = Path(__file__).resolve().parents[1]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from src.agent import TechnicalQAAgent


def main():
    parser = argparse.ArgumentParser(description="Pose une question a l'agent")
    parser.add_argument("question", nargs="+", help="Question a poser")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Affiche les scores des citations trouvees",
    )
    args = parser.parse_args()

    question = " ".join(args.question)
    agent = TechnicalQAAgent()
    result = agent.answer(question)

    print(f"\nQuestion : {result['question']}")
    print(f"Status   : {result['status']}")
    print(f"\nAnswer:\n{result['answer']}")

    if args.debug or result["status"] == "abstained":
        print("\nCitations trouvees :")
        for cit in result["citations"]:
            source_name = str(cit["source"]).split("/")[-1]
            print(
                f"  - {source_name} / {cit['section']} (score {cit['score']})"
            )


if __name__ == "__main__":
    main()
