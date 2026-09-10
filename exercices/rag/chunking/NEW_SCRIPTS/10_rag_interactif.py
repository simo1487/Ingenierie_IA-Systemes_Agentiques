"""RAG interactif : posez vos questions sur Automotive SPICE dans la console.

Utilisation :
    python 10_rag_interactif.py

- Tapez votre question, Entrée pour obtenir la réponse.
- Tapez 'q' (ou Ctrl+C) pour quitter.
- Le LLM tourne en LOCAL via Ollama (qwen2.5:3b) : aucune donnée envoyée en ligne.
- La base Qdrant persistante (NEW_SCRIPTS/qdrant_data) est ouverte en lecture.

Chaîne : question -> retrieval Qdrant (top-10, MiniLM) -> reranking
(bge-reranker-base) -> top-3 -> réponse générée par Ollama, sourcée.
"""

from __future__ import annotations

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

RETRIEVE_K = 10
KEEP_K = 3
MIN_SCORE = 0.35

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
    print(f"Base ouverte : collection '{COLLECTION_NAME}', {info.points_count} points")

    vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION_NAME)
    Settings.embed_model = get_embedding_model()

    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=Settings.embed_model)
    return index, client


def retrieve_candidates(index, query: str, top_k: int = 20) -> list[dict]:
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


def rerank(cross_encoder, query: str, candidates: list[dict], keep_k: int = 3) -> list[dict]:
    if not candidates:
        return []
    pairs = [(query, c["content"]) for c in candidates]
    scores = cross_encoder.predict(pairs)
    for cand, score in zip(candidates, scores):
        cand["score_rerank"] = round(float(score), 4)
    reranked = sorted(candidates, key=lambda c: c["score_rerank"], reverse=True)
    return reranked[:keep_k]


def answer_question(index, llm, cross_encoder, question: str) -> None:
    """Chaîne RAG complète avec affichage lisible."""
    candidates = retrieve_candidates(index, question)

    if not candidates or candidates[0]["score_vector"] < MIN_SCORE:
        print("\n[ABSTENTION] Aucun passage pertinent dans le corpus "
              f"(meilleur score vectoriel < {MIN_SCORE}).\n")
        return

    reranked = rerank(cross_encoder, question, candidates)

    print("\nSources utilisées :")
    for c in reranked:
        print(f"  - {c['header_path']} (rerank={c['score_rerank']})")

    print("\nGénération en cours (LLM local, CPU — quelques dizaines de secondes)...")
    context = "\n\n---\n\n".join(
        f"[Section : {c['header_path']}]\n{c['content']}" for c in reranked
    )
    response = llm.complete(RAG_PROMPT.format(context=context, question=question))

    print("\n" + "=" * 65)
    print(str(response).strip())
    print("=" * 65 + "\n")


if __name__ == "__main__":
    print("=" * 65)
    print("RAG INTERACTIF — Automotive SPICE (Qdrant + reranker + Ollama local)")
    print("=" * 65)
    print("Tapez votre question, ou 'q' pour quitter.\n")

    try:
        index, client = load_existing_index()
    except FileNotFoundError as exc:
        print(f"ERREUR : {exc}")
        sys.exit(1)

    print("Chargement du reranker (bge-reranker-base)...")
    from sentence_transformers import CrossEncoder

    cross_encoder = CrossEncoder(RERANK_MODEL_NAME)

    print(f"Chargement du LLM local Ollama ({OLLAMA_MODEL})...")
    llm = Ollama(model=OLLAMA_MODEL, request_timeout=300.0)
    Settings.llm = llm

    print("\nPrêt ! Posez votre question.\n")

    try:
        while True:
            try:
                question = input("Votre question > ").strip()
            except EOFError:
                break
            if not question:
                continue
            if question.lower() in {"q", "quit", "exit", "quitter"}:
                break
            answer_question(index, llm, cross_encoder, question)
    except (KeyboardInterrupt, EOFError):
        print("\nAu revoir !")
    finally:
        client.close()
