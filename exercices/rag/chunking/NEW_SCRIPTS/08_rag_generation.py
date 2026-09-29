"""RAG complet : question -> retrieval Qdrant -> génération LLM (Ollama local).

Adapté de la chaîne exo2/exo3 du dépôt, branchée sur la base persistante
NEW_SCRIPTS/qdrant_data (collection 'aspice_exigences_markdown').

Chaîne RAG :
1. Retrieval vectoriel top-k dans la collection ASPICE (MiniLM, cf. 06/07).
2. Abstention si aucun passage ne dépasse le seuil de pertinence.
3. Génération de la réponse par le LLM local Ollama (qwen2.5:3b), restreinte
   au contexte récupéré, avec citations des sections (header_path).

Sortie : NEW_TEXT_RESULTS/08_rag_generation_qdrant.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Console Windows en cp1252 : force l'UTF-8 pour afficher tous les caractères
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Permet l'import du module de config quel que soit le dossier de lancement
_project_root = Path(__file__).resolve().parents[4]
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from llama_index.core import Settings, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

QDRANT_PATH = Path(__file__).resolve().parent / "qdrant_data"
COLLECTION_NAME = "aspice_exigences_markdown"
EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
OLLAMA_MODEL = "qwen2.5:3b"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"

MIN_SCORE = 0.35
TOP_K = 3

RAG_PROMPT = """Tu es un assistant spécialisé dans la norme Automotive SPICE PAM v4.0.

Contexte récupéré de la base de connaissances :
---
{context}
---

Question : {question}

Consignes :
- Réponds en français, uniquement à partir du contexte ci-dessus.
- Cite les identifiants officiels (ex: SWE.1.BP2) présents dans le contexte.
- Si le contexte ne contient pas la réponse, réponds exactement :
  "Information non présente dans le corpus."

Réponse :"""


def get_embedding_model():
    """Même modèle que l'indexation (06) : indispensable pour des requêtes comparables."""
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding

    return HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)


def load_existing_index() -> tuple[VectorStoreIndex, QdrantClient]:
    """Ouvre la base Qdrant persistante et recharge l'index sans réindexer."""
    if not QDRANT_PATH.exists():
        raise FileNotFoundError(
            f"Base Qdrant introuvable : {QDRANT_PATH}. "
            "Exécuter d'abord 06_indexation_qdrant.py."
        )

    client = QdrantClient(path=str(QDRANT_PATH))
    info = client.get_collection(COLLECTION_NAME)
    print(f"Base ouverte : collection '{COLLECTION_NAME}', {info.points_count} points, statut {info.status}")

    vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION_NAME)
    embed_model = get_embedding_model()
    Settings.embed_model = embed_model

    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)
    return index, client


def retrieve_context(index, query: str, top_k: int = TOP_K, min_score: float = MIN_SCORE) -> list[dict]:
    """Retrieval vectoriel avec citations (même logique que le script 07)."""
    retriever = index.as_retriever(similarity_top_k=top_k)
    citations = []
    for rank, node_with_score in enumerate(retriever.retrieve(query), start=1):
        node = node_with_score.node
        citations.append({
            "rank": rank,
            "score": round(node_with_score.score or 0.0, 4),
            "header_path": node.metadata.get("header_path", "inconnu"),
            "content": node.get_content().strip().replace("\ufeff", ""),
        })
    if not citations or citations[0]["score"] < min_score:
        return []
    return citations


def ask_rag(index, llm, question: str) -> dict:
    """Chaîne RAG complète : retrieval -> abstention ou génération avec citations."""
    citations = retrieve_context(index, question)

    if not citations:
        return {
            "question": question,
            "status": "not_found",
            "reason": "Aucun passage du corpus n'atteint le seuil de pertinence minimal.",
            "answer": None,
            "citations": [],
        }

    context = "\n\n---\n\n".join(
        f"[Section : {c['header_path']}]\n{c['content']}" for c in citations
    )
    response = llm.complete(RAG_PROMPT.format(context=context, question=question))

    return {
        "question": question,
        "status": "answered",
        "answer": str(response).strip(),
        "citations": [
            {"rank": c["rank"], "score": c["score"], "header_path": c["header_path"]}
            for c in citations
        ],
    }


if __name__ == "__main__":
    print("=================================================================")
    print("RAG COMPLET : QDRANT (retrieval) + OLLAMA qwen2.5:3b (génération)")
    print("=================================================================")

    print("1. Ouverture de la base Qdrant persistante...")
    index, client = load_existing_index()

    print(f"2. Chargement du LLM local Ollama ({OLLAMA_MODEL})...")
    llm = Ollama(model=OLLAMA_MODEL, request_timeout=300.0)
    Settings.llm = llm

    questions = [
        "Que doit faire l'équipe selon la base practice SWE.1.BP1 ?",
        "Quelles sont les pratiques du processus de qualité assurance SUP.1 ?",
        "Quelle est la recette du couscous royal aux légumes ?",
    ]

    results = []
    for i, question in enumerate(questions, start=1):
        print(f"\n{'=' * 65}")
        print(f"QUESTION {i} : {question}")
        print("-" * 60)

        citations = retrieve_context(index, question)
        if not citations:
            print("   [ABSTENTION] Aucun passage pertinent dans le corpus (score < 0.35).")
            results.append({"question": question, "status": "not_found", "answer": None, "citations": []})
            continue

        print(f"   Contexte récupéré : {len(citations)} passages "
              f"(scores : {', '.join(str(c['score']) for c in citations)})")
        print("   Génération en cours (LLM local, CPU)...")

        entry = ask_rag(index, llm, question)
        results.append(entry)
        print(f"\nRÉPONSE :\n{entry['answer']}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "08_rag_generation_qdrant.json"
    payload = {
        "script": "08_rag_generation.py",
        "qdrant_collection": COLLECTION_NAME,
        "embedding_model": EMBED_MODEL_NAME,
        "llm": {"provider": "ollama", "model": OLLAMA_MODEL},
        "parameters": {"top_k": TOP_K, "min_score": MIN_SCORE},
        "qa": results,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nOK {out_path}")

    client.close()
    print("Client Qdrant fermé proprement.")
