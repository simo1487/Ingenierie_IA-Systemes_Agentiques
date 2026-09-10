"""RAG avec reranker léger : retrieval Qdrant -> reranking cross-encoder -> LLM Ollama.

Étend le script 08 d'un étage de reranking :
1. Retrieval vectoriel élargi (top-10) dans la collection ASPICE (MiniLM, cf. 06/07).
2. Abstention si aucun candidat ne dépasse le seuil vectoriel (même logique que 07/08).
3. Reranking des candidats par cross-encoder multilingue BAAI/bge-reranker-base
   (278M params) : re-score chaque paire (question, passage) et garde le top-3.
4. Génération de la réponse par le LLM local Ollama (qwen2.5:3b), restreinte
   au contexte reranké, avec citations des sections (header_path).

Le reranking corrige les erreurs de classement du bi-encodeur (question FR
vs passages EN), à coût CPU modéré (10 paires seulement).

Sortie : NEW_TEXT_RESULTS/09_rag_with_reranker_qdrant.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Console Windows en cp1252 : force l'UTF-8 pour afficher tous les caractères
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from llama_index.core import Settings, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from sentence_transformers import CrossEncoder

QDRANT_PATH = Path(__file__).resolve().parent / "qdrant_data"
COLLECTION_NAME = "aspice_exigences_markdown"
EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
RERANK_MODEL_NAME = "BAAI/bge-reranker-base"
OLLAMA_MODEL = "qwen2.5:3b"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"

RETRIEVE_K = 10   # candidats élargis envoyés au reranker
KEEP_K = 3        # passages retenus après reranking pour le LLM
MIN_SCORE = 0.35  # seuil d'abstention sur le score vectoriel (comme 07/08)

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


def retrieve_candidates(index, query: str, top_k: int = RETRIEVE_K) -> list[dict]:
    """Retrieval vectoriel élargi : top-k candidats pour le reranker."""
    retriever = index.as_retriever(similarity_top_k=top_k)
    candidates = []
    for rank, node_with_score in enumerate(retriever.retrieve(query), start=1):
        node = node_with_score.node
        candidates.append({
            "rank_vector": rank,
            "score_vector": round(node_with_score.score or 0.0, 4),
            "header_path": node.metadata.get("header_path", "inconnu"),
            "content": node.get_content().strip().replace("\ufeff", ""),
        })
    return candidates


def rerank(cross_encoder, query: str, candidates: list[dict], keep_k: int = KEEP_K) -> list[dict]:
    """Re-score chaque (question, passage) avec le cross-encoder et re-classe."""
    if not candidates:
        return []
    pairs = [(query, c["content"]) for c in candidates]
    scores = cross_encoder.predict(pairs)
    for cand, score in zip(candidates, scores):
        cand["score_rerank"] = round(float(score), 4)
    reranked = sorted(candidates, key=lambda c: c["score_rerank"], reverse=True)
    return reranked[:keep_k]


if __name__ == "__main__":
    print("=================================================================")
    print("RAG + RERANKER : QDRANT (retrieval) -> bge-reranker-base -> OLLAMA qwen2.5:3b")
    print("=================================================================")

    print("1. Ouverture de la base Qdrant persistante...")
    index, client = load_existing_index()

    print(f"2. Chargement du reranker cross-encoder ({RERANK_MODEL_NAME})...")
    cross_encoder = CrossEncoder(RERANK_MODEL_NAME)

    print(f"3. Chargement du LLM local Ollama ({OLLAMA_MODEL})...")
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

        candidates = retrieve_candidates(index, question)
        if not candidates or candidates[0]["score_vector"] < MIN_SCORE:
            print("   [ABSTENTION] Aucun passage pertinent dans le corpus "
                  f"(meilleur score vectoriel < {MIN_SCORE}).")
            results.append({
                "question": question, "status": "not_found", "answer": None,
                "ranking_before_rerank": [
                    {"rank": c["rank_vector"], "score": c["score_vector"], "header_path": c["header_path"]}
                    for c in candidates
                ],
                "citations": [],
            })
            continue

        print(f"   Retrieval élargi : {len(candidates)} candidats "
              f"(scores vectoriels : {', '.join(str(c['score_vector']) for c in candidates)})")
        print("   Reranking en cours (cross-encoder)...")
        reranked = rerank(cross_encoder, question, candidates)
        print("   Classement après rerank :")
        for c in reranked:
            print(f"     score_rerank={c['score_rerank']} | {c['header_path']}")

        print("   Génération en cours (LLM local, CPU)...")
        context = "\n\n---\n\n".join(
            f"[Section : {c['header_path']}]\n{c['content']}" for c in reranked
        )
        response = llm.complete(RAG_PROMPT.format(context=context, question=question))

        entry = {
            "question": question,
            "status": "answered",
            "answer": str(response).strip(),
            "ranking_before_rerank": [
                {"rank": c["rank_vector"], "score": c["score_vector"], "header_path": c["header_path"]}
                for c in candidates
            ],
            "citations": [
                {"rank_vector": c["rank_vector"], "score_vector": c["score_vector"],
                 "score_rerank": c["score_rerank"], "header_path": c["header_path"]}
                for c in reranked
            ],
        }
        results.append(entry)
        print(f"\nRÉPONSE :\n{entry['answer']}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "09_rag_with_reranker_qdrant.json"
    payload = {
        "script": "09_rag_with_reranker.py",
        "qdrant_collection": COLLECTION_NAME,
        "embedding_model": EMBED_MODEL_NAME,
        "reranker_model": RERANK_MODEL_NAME,
        "llm": {"provider": "ollama", "model": OLLAMA_MODEL},
        "parameters": {"retrieve_k": RETRIEVE_K, "keep_k": KEEP_K, "min_score": MIN_SCORE},
        "qa": results,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nOK {out_path}")

    client.close()
    print("Client Qdrant fermé proprement.")
