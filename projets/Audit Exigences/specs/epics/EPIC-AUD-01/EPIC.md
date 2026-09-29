# EPIC-AUD-01 — Vérifier grammaire et orthographe

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../SPEC.md)
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`

## Valeur

Améliorer la lisibilité des exigences et réduire les ambiguïtés d'interprétation dues aux fautes de langue.

## Enfants

| User Story | Feature | Rôle | Valeur |
|---|---|---|---|
| [`US-AUD-101`](user-stories/US-AUD-101.md) | [`FEAT-AUD-101`](features/FEAT-AUD-101/FEATURE.md) | ingénieur exigences | détecter les erreurs de grammaire (accord sujet-verbe, ponctuation, capitalisation) |
| [`US-AUD-102`](user-stories/US-AUD-102.md) | [`FEAT-AUD-102`](features/FEAT-AUD-102/FEATURE.md) | ingénieur exigences | détecter les fautes d'orthographe avec proposition de correction |

## Périmètre

Détection lexicale déterministe (dictionnaire de fautes + règles d'accord de base). Aucun modèle IA requis pour ce lot. Les sorties sont des propositions ; aucune correction automatique.

## Achèvement mesurable

Les critères candidats disposent de preuves exécutées reliées à leurs oracles indépendants et revues humainement.
