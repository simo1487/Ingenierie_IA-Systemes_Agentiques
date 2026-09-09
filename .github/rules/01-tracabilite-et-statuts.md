---
description: "Règles strictes de traçabilité des exigences, distinction des statuts et interdiction d'inférence lexicale"
trigger: model_decision
---

# Règle : Traçabilité des Exigences et Statuts de Preuve

## 1. Principe de non-inférence lexicale
- Une présence de mots-clés, un nom de fichier similaire ou une proximité de vocabulaire ne constitue **JAMAIS** une relation de traçabilité.
- Une relation entre une exigence et un élément de code ou de test n'est établie que si le comportement fonctionnel décrit dans l'exigence est effectivement exécuté et vérifié par l'oracle du test.

## 2. Statuts formels obligatoires
Tout élément d'exigence ou lien de traçabilité doit porter un des 5 statuts suivants :
- `Observé` : Relevé textuellement dans la source canonique sans présomption d'implémentation.
- `Candidat` : Hypothèse de lien issue d'une analyse, en attente de validation par un test ou un examen humain.
- `Vérifié` : Lien formellement prouvé par un test exécuté avec succès ou une source contradictoire démontrée.
- `Non vérifié` : Exigence dont l'implémentation ou le test est introuvable dans la baseline.
- `Bloqué` : Dépendance inaccessible ou décision humaine en attente.

## 3. Format de matrice
Toute matrice de traçabilité doit suivre le modèle [`specs/templates/template-matrice-tracabilite.md`](../../specs/templates/template-matrice-tracabilite.md) et être validable par un schéma JSON strict sans attributs ad-hoc.
