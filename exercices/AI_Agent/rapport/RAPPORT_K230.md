# Rapport de test - K230 Datasheet

## Contexte

Test de l'agent RAG sur la datasheet K230 (fichier `tests/fixtures/sample_k230.md`).

## Parametres

| Parametre | Valeur |
|-----------|--------|
| Corpus | `tests/fixtures/sample_k230.md` |
| Questions | 30 |
| Chunks generes | 114 |
| Backend LLM | `fake` (emulation) |
| Backend Embeddings | `fake` (emulation) |

## Resultats

| Metrique | Valeur |
|----------|--------|
| Reponses pertinentes | 6/30 |
| Taux de reussite | **20.0%** |

## Interpretation

Le backend `fake` est une emulation naive qui ne remplace pas Mistral :
- L'embedding deterministe produit des scores eleves de maniere aleatoire.
- Le LLM factice extrait des phrases sans comprehension semantique.
- L'indexation et le retrieval fonctionnent, mais la qualite des reponses est limitee.

Ces resultats servent a valider le pipeline technique (load -> parse -> chunk -> index -> retrieve -> generate -> format).

## Fichier detaille

Voir `k230_test_report.json` pour le detail complet des 30 reponses.

## Recommandation

Pour obtenir des resultats significatifs, executer avec :

```powershell
$env:LLM_BACKEND='mistral'
$env:EMBEDDING_BACKEND='mistral'
$env:MISTRAL_API_KEY='<votre_cle>'
python scripts/test_k230.py
```
