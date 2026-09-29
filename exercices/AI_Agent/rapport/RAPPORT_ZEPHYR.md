# Rapport de test - Zephyr Kernel

## Contexte

Test de l'agent RAG sur le corpus Zephyr kernel (10 pages HTML telechargees depuis https://docs.zephyrproject.org/latest/kernel/).

## Parametres

| Parametre | Valeur |
|-----------|--------|
| Corpus | `data/zephyr_kernel.html` |
| Questions | 30 |
| Chunks generes | 142 |
| Backend LLM | `fake` (emulation) |
| Backend Embeddings | `fake` (emulation) |

## Resultats

| Metrique | Valeur |
|----------|--------|
| Reponses pertinentes | 9/30 |
| Taux de reussite | **30.0%** |

## Interpretation

Le backend `fake` est une emulation naive :
- Le parser HTML extrait du texte brut sans garder les titres, donc tous les chunks sont dans la section `Root`.
- L'embedding factice produit des scores eleves aleatoirement.
- Le LLM factice fait une extraction simple sans comprehension semantique.

Ces resultats ne reflectent pas la qualite reelle de l'agent. Ils servent a valider que :
- Le pipeline complet fonctionne (load -> parse -> chunk -> index -> retrieve -> generate).
- Le format de sortie est correct (Answer + Sources).
- Le seuil de pertinence est applique.

## Fichier detaille

Voir `zephyr_test_report.json` pour le detail complet des 30 reponses.

## Recommandation

Pour obtenir des resultats significatifs, executer avec :

```powershell
$env:LLM_BACKEND='mistral'
$env:EMBEDDING_BACKEND='mistral'
$env:MISTRAL_API_KEY='<votre_cle>'
python scripts/test_zephyr.py
```
