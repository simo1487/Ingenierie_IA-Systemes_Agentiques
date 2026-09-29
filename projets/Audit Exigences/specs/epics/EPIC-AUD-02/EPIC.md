# EPIC-AUD-02 — Vérifier la non-duplication

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../SPEC.md)
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`

## Valeur

Éviter les redondances et les divergences entre copies d'une même exigence lors de la maintenance.

## Enfants

| User Story | Feature | Rôle | Valeur |
|---|---|---|---|
| [`US-AUD-201`](user-stories/US-AUD-201.md) | [`FEAT-AUD-201`](features/FEAT-AUD-201/FEATURE.md) | ingénieur exigences | identifier les exigences dupliquées ou quasi-identiques |

## Périmètre

Similarité lexicale (Jaccard sur tokens normalisés) avec seuil figé avant exécution. Les reformulations sémantiques avec vocabulaire disjoint ne sont pas détectées dans ce lot. Les sorties sont des propositions.

## Achèvement mesurable

Les critères candidats disposent de preuves exécutées reliées à leurs oracles indépendants et revues humainement.
