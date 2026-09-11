"""Agent examinateur ASPICE simulé : quiz aléatoire sur toute la norme.

Principe :
1. L'agent construit le catalogue des exigences depuis la base Qdrant
   (collection 'aspice_exigences_markdown') via client.scroll() :
   211 exigences - 179 base practices (*.BPn) + 32 outcomes (*.OUTCOMEn).
2. L'agent choisit lui-même les exigences à interroger par tirage aléatoire
   sans remise ; le candidat ne choisit rien.
3. Pour chaque question :
   - l'agent annonce le processus, le chapitre et la référence de l'exigence ;
   - l'agent (Mistral) génère une question d'examen ancrée dans l'exigence ;
   - le candidat répond dans la console ;
   - l'agent évalue la réponse contre le texte officiel :
     verdict (CORRECTE / PARTIELLE / INCORRECTE) + correction détaillée.
4. Score final et rapport de session en JSON.

Prérequis :
- Base Qdrant créée par 06_indexation_qdrant.py.
- Clé API dans exercices/.env (MISTRAL_API_KEY=...) ou variable d'environnement.

Sortie : NEW_TEXT_RESULTS/11_agent_examinateur.json
"""

from __future__ import annotations

import json
import os
import random
import re
import sys
from pathlib import Path

# Console Windows en cp1252 : force l'UTF-8 pour afficher tous les caractères
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from llama_index.core import Settings
from llama_index.llms.mistralai import MistralAI
from qdrant_client import QdrantClient

QDRANT_PATH = Path(__file__).resolve().parent / "qdrant_data"
COLLECTION_NAME = "aspice_exigences_markdown"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"
ENV_FILE = Path(__file__).resolve().parents[3] / ".env"

MISTRAL_MODEL = "mistral-small-latest"
NB_QUESTIONS = 3
SCROLL_BATCH = 100

REQ_ID_RE = re.compile(r"####\s*([A-Z]{3}\.\d+\.(?:BP|OUTCOME)\d+)")
VERDICT_RE = re.compile(r"VERDICT:\s*(CORRECTE|PARTIELLE|INCORRECTE)", re.IGNORECASE)


def load_api_key() -> str:
    """Charge MISTRAL_API_KEY depuis exercices/.env (jamais affichée)."""
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("MISTRAL_API_KEY="):
                key = line.split("=", 1)[1].strip()
                if key:
                    return key
    return os.getenv("MISTRAL_API_KEY", "")


def open_qdrant() -> QdrantClient:
    """Ouvre la base Qdrant persistante en lecture."""
    if not QDRANT_PATH.exists():
        raise FileNotFoundError(
            f"Base Qdrant introuvable : {QDRANT_PATH}. "
            "Exécuter d'abord 06_indexation_qdrant.py."
        )
    client = QdrantClient(path=str(QDRANT_PATH))
    info = client.get_collection(COLLECTION_NAME)
    print(f"Base ouverte : collection '{COLLECTION_NAME}', {info.points_count} points")
    return client


def build_requirement_catalog(client: QdrantClient) -> list[dict]:
    """Parcourt toute la collection et construit le catalogue des exigences."""
    catalog: dict[str, dict] = {}
    offset = None
    while True:
        points, offset = client.scroll(
            collection_name=COLLECTION_NAME,
            limit=SCROLL_BATCH,
            offset=offset,
            with_payload=True,
            with_vectors=False,
        )
        for point in points:
            payload = point.payload or {}
            node_content = payload.get("_node_content")
            if not node_content:
                continue
            content = json.loads(node_content).get("text", "").strip().replace("\ufeff", "")
            match = REQ_ID_RE.search(content)
            if not match:
                continue
            req_id = match.group(1)
            header_path = payload.get("header_path", "")
            segments = [s.strip() for s in header_path.split(">")]
            catalog.setdefault(req_id, {
                "req_id": req_id,
                "process_id": ".".join(req_id.split(".")[:2]),
                "process_label": segments[0] if segments else "",
                "chapter": segments[-1] if len(segments) > 1 else "",
                "header_path": header_path,
                "content": content,
            })
        if offset is None:
            break
    return list(catalog.values())


QUESTION_PROMPT = """Tu es un assesseur Automotive SPICE PAM v4.0 expérimenté qui conduit un assessment.

Voici une exigence officielle (base practice ou outcome) :
---
{req_content}
---

Pose UNE question d'examen en français à un ingénieur pour vérifier sa compréhension
de cette exigence. La question doit :
- porter sur l'objectif ou les activités décrits dans l'exigence ;
- être ouverte (pas de question à laquelle on peut répondre par oui/non) ;
- ne pas recopier mot pour mot l'intitulé de l'exigence.

Réponds uniquement avec la question, sans préambule."""


EVAL_PROMPT = """Tu es un assesseur Automotive SPICE PAM v4.0. Tu évalues la réponse d'un candidat.

Exigence officielle (référence) :
---
{req_content}
---

Question posée : {question}
Réponse du candidat : {answer}

Évalue la réponse du candidat :
1. Première ligne EXACTEMENT au format : VERDICT: CORRECTE ou VERDICT: PARTIELLE ou VERDICT: INCORRECTE
2. Puis 2 à 4 phrases : ce qui est juste dans la réponse, ce qui manque, et la
   réponse attendue d'après l'exigence officielle. Réponds en français."""


def run_exam(llm: MistralAI, client: QdrantClient, nb_questions: int) -> dict:
    """Déroule le quiz : l'agent choisit les exigences, pose les questions, corrige."""
    print("\nConstruction du catalogue d'exigences depuis Qdrant...")
    catalog = build_requirement_catalog(client)
    if not catalog:
        print("Aucune exigence trouvée dans la collection.")
        return {"mode": "aleatoire", "rounds": [], "verdicts": {}, "score": None, "max_score": 0}

    process_count = len({c["process_id"] for c in catalog})
    print(f"Catalogue : {len(catalog)} exigences (BP + outcomes), {process_count} processus.")

    drawn = random.sample(catalog, k=min(nb_questions, len(catalog)))
    print(f"L'agent a tiré {len(drawn)} exigence(s) au hasard. Bonne chance !")

    rounds = []
    verdicts = {"CORRECTE": 0, "PARTIELLE": 0, "INCORRECTE": 0}
    score = 0

    for round_num, req in enumerate(drawn, start=1):
        print(f"\n--- QUESTION {round_num}/{len(drawn)} ---")
        print(f"Processus : {req['process_label']}")
        print(f"Chapitre  : {req['chapter']}")
        print(f"Référence : {req['req_id']}")

        print("\nL'assesseur prépare sa question...")
        question = str(llm.complete(QUESTION_PROMPT.format(req_content=req["content"]))).strip()
        print(f"\n{question}")

        try:
            answer = input("\nVotre réponse > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExamen interrompu par le candidat.")
            break

        print("\nÉvaluation en cours...")
        eval_text = str(
            llm.complete(
                EVAL_PROMPT.format(
                    req_content=req["content"],
                    question=question,
                    answer=answer,
                )
            )
        ).strip()

        verdict = "PARTIELLE"
        m = VERDICT_RE.search(eval_text)
        if m:
            verdict = m.group(1).upper()
        lines = eval_text.splitlines()
        if lines and lines[0].upper().startswith("VERDICT"):
            explanation = "\n".join(lines[1:]).strip()
        else:
            explanation = eval_text

        score += {"CORRECTE": 2, "PARTIELLE": 1}.get(verdict, 0)
        verdicts[verdict] += 1

        rounds.append({
            "req_id": req["req_id"],
            "process_id": req["process_id"],
            "process_label": req["process_label"],
            "chapter": req["chapter"],
            "question": question,
            "candidate_answer": answer,
            "verdict": verdict,
            "explanation": explanation,
            "source_header_path": req["header_path"],
        })

        print(f"\n>>> VERDICT : {verdict}")
        print(explanation)

    max_score = len(rounds) * 2
    note_sur_20 = round(score * 20 / max_score, 1) if max_score else 0
    if rounds:
        print("\n" + "=" * 65)
        print(f"SCORE FINAL : {score} / {max_score}")
        print(f"NOTE : {note_sur_20} / 20")
        print(
            f"  -> {verdicts['CORRECTE']} correcte(s), "
            f"{verdicts['PARTIELLE']} partielle(s), "
            f"{verdicts['INCORRECTE']} incorrecte(s)"
        )

    return {
        "mode": "aleatoire",
        "nb_questions": nb_questions,
        "catalog_size": len(catalog),
        "rounds": rounds,
        "verdicts": verdicts,
        "score": score,
        "max_score": max_score,
        "note_sur_20": note_sur_20,
    }


if __name__ == "__main__":
    print("=" * 65)
    print("AGENT EXAMINATEUR ASPICE — quiz aléatoire (Mistral + Qdrant)")
    print("=" * 65)

    api_key = load_api_key()
    if not api_key:
        print("ERREUR : MISTRAL_API_KEY introuvable (exercices/.env ou variable d'environnement).")
        sys.exit(1)
    print("Clé API Mistral chargée.")

    try:
        client = open_qdrant()
    except FileNotFoundError as exc:
        print(f"ERREUR : {exc}")
        sys.exit(1)

    print(f"Chargement du LLM ({MISTRAL_MODEL})...")
    llm = MistralAI(model=MISTRAL_MODEL, api_key=api_key)
    Settings.llm = llm

    try:
        nb_raw = input(f"\nNombre de questions [{NB_QUESTIONS}] > ").strip()
        nb_questions = int(nb_raw) if nb_raw.isdigit() and int(nb_raw) > 0 else NB_QUESTIONS
    except (KeyboardInterrupt, EOFError):
        print("\nAu revoir !")
        client.close()
        sys.exit(0)

    try:
        result = run_exam(llm, client, nb_questions)

        OUTPUT_DIR.mkdir(exist_ok=True)
        out_path = OUTPUT_DIR / "11_agent_examinateur.json"
        payload = {
            "script": "11_agent_examinateur.py",
            "qdrant_collection": COLLECTION_NAME,
            "llm": {"provider": "mistral", "model": MISTRAL_MODEL},
            "session": result,
        }
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nOK {out_path}")
    finally:
        client.close()
        print("Client Qdrant fermé proprement.")
