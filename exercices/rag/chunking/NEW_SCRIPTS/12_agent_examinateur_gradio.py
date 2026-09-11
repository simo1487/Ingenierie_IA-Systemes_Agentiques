"""Interface web Gradio pour l'agent examinateur ASPICE (quiz aléatoire).

Même logique que 11_agent_examinateur.py (réutilisée via importlib) mais
pilotée par une interface chatbot : l'agent choisit les exigences, pose les
questions, corrige chaque réponse, et affiche le score final.

Prérequis :
- pip install gradio
- Base Qdrant créée par 06_indexation_qdrant.py.
- Clé API dans exercices/.env (MISTRAL_API_KEY=...) ou variable d'environnement.

Lancement : python 12_agent_examinateur_gradio.py  ->  http://127.0.0.1:7860
Sortie    : NEW_TEXT_RESULTS/12_agent_examinateur_gradio.json
"""

from __future__ import annotations

import importlib.util
import json
import random
import sys
from pathlib import Path

# Console Windows en cp1252 : force l'UTF-8 pour afficher tous les caractères
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import gradio as gr
from llama_index.llms.mistralai import MistralAI

# Le nom du fichier 11 commence par un chiffre : chargement via importlib.
_spec = importlib.util.spec_from_file_location(
    "agent_exam", Path(__file__).resolve().parent / "11_agent_examinateur.py"
)
agent = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(agent)

OUTPUT_DIR = agent.OUTPUT_DIR
REPORT_FILE = "12_agent_examinateur_gradio.json"

# Initialisés dans main()
LLM: MistralAI | None = None
CATALOG: list[dict] = []
PROCESS_COUNT = 0


def new_state(nb_questions: int) -> dict:
    """État initial d'une session d'examen (stocké dans gr.State)."""
    return {
        "drawn": [],
        "index": 0,
        "score": 0,
        "verdicts": {"CORRECTE": 0, "PARTIELLE": 0, "INCORRECTE": 0},
        "rounds": [],
        "nb_questions": nb_questions,
        "current_question": "",
        "finished": False,
    }


def next_question_message(state: dict) -> str:
    """Génère la question de l'exigence courante et formate le message chatbot."""
    req = state["drawn"][state["index"]]
    question = str(LLM.complete(agent.QUESTION_PROMPT.format(req_content=req["content"]))).strip()
    state["current_question"] = question
    return (
        f"**QUESTION {state['index'] + 1}/{len(state['drawn'])}**\n\n"
        f"Processus : {req['process_label']}  \n"
        f"Chapitre : {req['chapter']}  \n"
        f"Référence : `{req['req_id']}`\n\n"
        f"{question}"
    )


def start_exam(nb_questions: float, history: list | None, state: dict):
    """Démarre un examen : tirage aléatoire + première question."""
    history = history or []
    nb = int(nb_questions) if nb_questions else agent.NB_QUESTIONS
    state = new_state(nb)
    state["drawn"] = random.sample(CATALOG, k=min(nb, len(CATALOG)))
    history.append({
        "role": "assistant",
        "content": (
            f"Examen démarré : {len(state['drawn'])} exigence(s) tirée(s) au hasard "
            f"parmi {len(CATALOG)} ({PROCESS_COUNT} processus). Bonne chance !"
        ),
    })
    history.append({"role": "assistant", "content": next_question_message(state)})
    return history, state, ""


def submit_answer(answer: str, history: list | None, state: dict):
    """Évalue la réponse du candidat, puis enchaîne sur la question suivante."""
    history = history or []
    answer = (answer or "").strip()
    if not state.get("drawn") or state.get("finished"):
        history.append({"role": "assistant", "content": "Clique sur « Démarrer l'examen » pour lancer une session."})
        return history, state, ""
    if not answer:
        history.append({"role": "assistant", "content": "Réponse vide — écris ta réponse puis clique sur « Envoyer »."})
        return history, state, ""

    req = state["drawn"][state["index"]]
    history.append({"role": "user", "content": answer})

    eval_text = str(
        LLM.complete(
            agent.EVAL_PROMPT.format(
                req_content=req["content"],
                question=state["current_question"],
                answer=answer,
            )
        )
    ).strip()

    verdict = "PARTIELLE"
    m = agent.VERDICT_RE.search(eval_text)
    if m:
        verdict = m.group(1).upper()
    lines = eval_text.splitlines()
    explanation = "\n".join(lines[1:]).strip() if lines and lines[0].upper().startswith("VERDICT") else eval_text

    state["score"] += {"CORRECTE": 2, "PARTIELLE": 1}.get(verdict, 0)
    state["verdicts"][verdict] += 1
    state["rounds"].append({
        "req_id": req["req_id"],
        "process_id": req["process_id"],
        "process_label": req["process_label"],
        "chapter": req["chapter"],
        "question": state["current_question"],
        "candidate_answer": answer,
        "verdict": verdict,
        "explanation": explanation,
        "source_header_path": req["header_path"],
    })
    history.append({"role": "assistant", "content": f"**VERDICT : {verdict}**\n\n{explanation}"})

    state["index"] += 1
    if state["index"] < len(state["drawn"]):
        history.append({"role": "assistant", "content": next_question_message(state)})
    else:
        state["finished"] = True
        history.append({"role": "assistant", "content": final_message(state)})
        write_report(state)

    return history, state, ""


def final_message(state: dict) -> str:
    """Message de fin d'examen : note sur 20 + décompte par verdict."""
    score = state["score"]
    max_score = len(state["rounds"]) * 2
    note = round(score * 20 / max_score, 1) if max_score else 0
    v = state["verdicts"]
    return (
        f"**EXAMEN TERMINÉ — NOTE : {note} / 20**\n\n"
        f"({score} / {max_score} points — "
        f"{v['CORRECTE']} correcte(s), {v['PARTIELLE']} partielle(s), {v['INCORRECTE']} incorrecte(s))\n\n"
        "Clique sur « Démarrer l'examen » pour une nouvelle session."
    )


def write_report(state: dict) -> Path:
    """Écrit le rapport de session en JSON (même schéma que la version console)."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / REPORT_FILE
    payload = {
        "script": "12_agent_examinateur_gradio.py",
        "ui": "gradio",
        "qdrant_collection": agent.COLLECTION_NAME,
        "llm": {"provider": "mistral", "model": agent.MISTRAL_MODEL},
        "session": {
            "mode": "aleatoire",
            "nb_questions": state["nb_questions"],
            "catalog_size": len(CATALOG),
            "rounds": state["rounds"],
            "verdicts": state["verdicts"],
            "score": state["score"],
            "max_score": len(state["rounds"]) * 2,
            "note_sur_20": round(state["score"] * 20 / (len(state["rounds"]) * 2), 1)
            if state["rounds"] else 0,
        },
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Rapport écrit : {out_path}")
    return out_path


def build_app() -> gr.Blocks:
    with gr.Blocks(title="Agent Examinateur ASPICE") as demo:
        gr.Markdown("# Agent Examinateur ASPICE — quiz aléatoire\n"
                    "L'agent tire des exigences au hasard dans la norme (BP + outcomes), "
                    "annonce le processus et le chapitre, puis évalue tes réponses.")

        with gr.Row():
            nb_input = gr.Slider(1, 15, value=agent.NB_QUESTIONS, step=1,
                                 label="Nombre de questions", scale=3)
            start_btn = gr.Button("Démarrer l'examen", variant="primary", scale=1)

        chatbot = gr.Chatbot(height=480, label="Examen")

        with gr.Row():
            answer_box = gr.Textbox(placeholder="Ta réponse...", scale=4,
                                    show_label=False)
            send_btn = gr.Button("Envoyer", variant="secondary", scale=1)

        state = gr.State(new_state(agent.NB_QUESTIONS))

        start_btn.click(start_exam, [nb_input, chatbot, state],
                        [chatbot, state, answer_box])
        send_btn.click(submit_answer, [answer_box, chatbot, state],
                       [chatbot, state, answer_box])
        answer_box.submit(submit_answer, [answer_box, chatbot, state],
                          [chatbot, state, answer_box])
    return demo


if __name__ == "__main__":
    print("=" * 65)
    print("AGENT EXAMINATEUR ASPICE — interface Gradio (Mistral + Qdrant)")
    print("=" * 65)

    api_key = agent.load_api_key()
    if not api_key:
        print("ERREUR : MISTRAL_API_KEY introuvable (exercices/.env ou variable d'environnement).")
        sys.exit(1)
    print("Clé API Mistral chargée.")

    try:
        client = agent.open_qdrant()
    except FileNotFoundError as exc:
        print(f"ERREUR : {exc}")
        sys.exit(1)

    CATALOG = agent.build_requirement_catalog(client)
    PROCESS_COUNT = len({c["process_id"] for c in CATALOG})
    print(f"Catalogue : {len(CATALOG)} exigences (BP + outcomes), {PROCESS_COUNT} processus.")

    print(f"Chargement du LLM ({agent.MISTRAL_MODEL})...")
    LLM = MistralAI(model=agent.MISTRAL_MODEL, api_key=api_key)

    demo = build_app()
    try:
        demo.launch()
    finally:
        client.close()
        print("Client Qdrant fermé proprement.")
