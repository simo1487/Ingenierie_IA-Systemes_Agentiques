"""Test de la base Qdrant aspice_exigences_markdown : recherche et citations.

Adapté de exercices/rag/exercices/exo3_retrieval_and_citations.py.

Différences avec l'exercice d'origine :
- Ne réindexe rien : ouvre la base persistante NEW_SCRIPTS/qdrant_data
  (collection 'aspice_exigences_markdown', 339 chunks Markdown du document
  automotive-spice-exigences.md, embeddings paraphrase-multilingual-MiniLM-L12-v2).
- Filtre de métadonnées adapté au champ 'header_path' (section du document).
- Cas de test transposés au corpus Automotive SPICE :
  1. Requête par identifiant exact (SWE.1.BP1)
  2. Requête thématique paraphrasée
  3. Requête avec filtre de métadonnées (restreindre au processus SUP.1)
  4. Requête hors-périmètre testant l'abstention
- Vérifie que chaque citation pointe vers un header_path et un score mesuré.

Sortie : NEW_TEXT_RESULTS/07_retrieval_and_citations_qdrant.json
"""

from __future__ import annotations

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
from llama_index.core.vector_stores import MetadataFilter, MetadataFilters, FilterOperator
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

QDRANT_PATH = Path(__file__).resolve().parent / "qdrant_data"
COLLECTION_NAME = "aspice_exigences_markdown"
EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"


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


def retrieve_with_citations(
    index,
    query: str,
    top_k: int = 3,
    min_score: float = 0.4,
    header_filter: str | None = None,
) -> dict:
    """Recherche vectorielle avec citations sourcées et abstention sous seuil.

    Adapté de exercices/rag/pipeline/retrieval.py : les clés de métadonnées
    sont celles de nos chunks ASPICE (source, header_path, chunk_index).
    """
    filters = None
    if header_filter:
        filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="header_path",
                    value=header_filter,
                    operator=FilterOperator.TEXT_MATCH,
                )
            ]
        )

    retriever = index.as_retriever(similarity_top_k=top_k, filters=filters)
    nodes_with_scores = retriever.retrieve(query)

    citations = []
    for rank, node_with_score in enumerate(nodes_with_scores, start=1):
        node = node_with_score.node
        citations.append({
            "rank": rank,
            "score": round(node_with_score.score or 0.0, 4),
            "source": node.metadata.get("source", "inconnu"),
            "header_path": node.metadata.get("header_path", "inconnu"),
            "chunk_index": node.metadata.get("chunk_index", "inconnu"),
            "content_snippet": node.get_content().strip()[:250],
        })

    if not citations or citations[0]["score"] < min_score:
        return {
            "query": query,
            "status": "not_found",
            "reason": "Aucun passage du corpus n'atteint le seuil de pertinence minimal.",
            "citations": citations,
        }
    return {"query": query, "status": "found", "top_k": top_k, "citations": citations}
def format_citation_report(result: dict) -> str:
    """Met en forme lisible le résultat d'une recherche RAG (adapté de retrieval.py)."""
    lines = [f"=== REQUÊTE : {result['query']} ===", f"Statut : {result['status']}"]
    if result["status"] == "not_found":
        lines.append(f"Motif d'abstention : {result.get('reason')}")
    for cit in result.get("citations", []):
        lines.append(
            f"\n[Citation #{cit['rank']}] Score: {cit['score']} | "
            f"Source: {cit['source']} | Section: {cit['header_path']}"
        )
        lines.append(f"Extrait : {cit['content_snippet']}...")
    return "\n".join(lines)


def run_retrieval_test() -> tuple[list[dict], QdrantClient]:
    print("=================================================================")
    print("TEST DE LA BASE QDRANT 'aspice_exigences_markdown' (RECHERCHE + CITATIONS)")
    print("=================================================================")

    print("1. Ouverture de la base persistante (aucune réindexation)...")
    index, client = load_existing_index()
    print("   Index chargé.")

    queries = [
        {
            "titre": "Cas 1 : Requête par identifiant exact",
            "query": "SWE.1.BP1 Specify software requirements",
            "filter": None,
        },
        {
            "titre": "Cas 2 : Requête thématique paraphrasée",
            "query": "Comment les exigences logicielles doivent-elles être vérifiées et tracées ?",
            "filter": None,
        },
        {
            "titre": "Cas 3 : Requête avec filtre de métadonnées (processus SUP.1)",
            "query": "Quelles sont les pratiques de qualité assurance ?",
            "filter": "SUP.1",
        },
        {
            "titre": "Cas 4 : Requête hors-corpus (test d'abstention)",
            "query": "Recette du couscous royal aux légumes",
            "filter": None,
        },
    ]

    results = []
    for q in queries:
        print(f"\n>>> {q['titre']}")
        result = retrieve_with_citations(
            index=index,
            query=q["query"],
            top_k=3,
            min_score=0.35,
            header_filter=q["filter"],
        )
        print(format_citation_report(result))
        results.append({"titre": q["titre"], **result})

    return results, client


if __name__ == "__main__":
    results, client = run_retrieval_test()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "07_retrieval_and_citations_qdrant.json"
    payload = {
        "script": "07_retrieval_and_citations.py",
        "qdrant_collection": COLLECTION_NAME,
        "embedding_model": EMBED_MODEL_NAME,
        "tests": results,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nOK {out_path}")

    client.close()
    print("Client Qdrant fermé proprement.")
