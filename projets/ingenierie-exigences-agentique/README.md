# Projet Ingénierie des exigences agentique

- **Équipe :** Mohammed et Florient
- **Branche :** `feat_getReq`
- **Spécification :** [SPEC.md](SPEC.md)
- **Statut :** produit à cadrer et prototyper

## Objectif

Construire un produit configurable qui orchestre des agents IA pour cadrer, collecter, auditer, structurer et tracer des exigences à partir de baselines approuvées. Le premier cas d’application sera choisi parmi les projets open source retenus par le projet [`logiciel-automobile-open-source`](../logiciel-automobile-open-source/SPEC.md).

## Organisation cible

- `experiments/` : comparaisons d’orchestrations et prototypes jetables ;
- `data/` : petites fixtures et configurations redistribuables ;
- `src/` : orchestration et agents maintenus ;
- `tests/` : contrats, erreurs, timeouts, permissions et reproductibilité ;
- `docs/` : guides opérateur et contrats d’entrée/sortie ;
- `evidence/` : manifestes de runs, échantillons revus et décisions humaines.

## Commandes

Les commandes d’installation, d’exécution et de test restent à définir après le choix de la technologie d’orchestration. Leur absence est suivie dans `AMB-REQ-AI-002` de la spécification.

## Limites

Les agents produisent des propositions et observations. Ils ne valident pas seuls une exigence, ne résolvent pas une ambiguïté métier et ne transforment pas une similarité lexicale en preuve de traçabilité.
