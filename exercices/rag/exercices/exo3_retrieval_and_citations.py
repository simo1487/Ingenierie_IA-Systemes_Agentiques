"""Exercice 3 : Recherche, Filtrage par Métadonnées et Validation des Citations.

Objectif :
- Poser des requêtes types de l'ingénierie embarquée :
  1. Requête par identifiant exact (ex: `ASPICE-SWE.1-BP1` ou `QUAL-DIAG-01`)
  2. Requête thématique ou paraphrasée
  3. Requête avec filtre de métadonnées (restreindre au projet 'qualite' ou 'normes')
  4. Requête hors-périmètre testant l'abstention
- Vérifier que chaque citation retournée pointe vers un fichier source et un score mesuré.
"""

from __future__ import annotations

from exercices.rag.exercices.exo2_indexation_qdrant import run_indexing_exercise
from exercices.rag.pipeline.retrieval import retrieve_with_citations, format_citation_report


def run_retrieval_exercise():
    print("=================================================================")
    print("EXERCICE 3 : RECHERCHE ET VALIDATION DE CITATIONS DANS QDRANT")
    print("=================================================================")

    # Initialisation et indexation en mémoire
    index, _ = run_indexing_exercise(mode="memory")

    queries = [
        {
            "titre": "Cas 1 : Requête par identifiant exact",
            "query": "ASPICE-SWE.1-BP1",
            "filter": None,
        },
        {
            "titre": "Cas 2 : Requête sur un diagnostic qualité",
            "query": "Buffer is accessed out of bounds",
            "filter": "cppcheck",
        },
        {
            "titre": "Cas 3 : Requête sur le firmware open source VESC",
            "query": "Quel est le type de licence et le framework de contrôle moteur ?",
            "filter": "open_source",
        },
        {
            "titre": "Cas 4 : Requête hors-corpus (test d'abstention)",
            "query": "Protocole de routage BGP sur réseau 5G",
            "filter": None,
        },
    ]

    for q in queries:
        print(f"\n>>> {q['titre']}")
        result = retrieve_with_citations(
            index=index,
            query=q["query"],
            top_k=2,
            min_score=0.4,
            project_filter=q["filter"],
        )
        print(format_citation_report(result))


if __name__ == "__main__":
    run_retrieval_exercise()
