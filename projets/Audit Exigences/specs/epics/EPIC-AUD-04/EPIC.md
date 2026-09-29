# EPIC-AUD-04 — Analyse sémantique par IA

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../SPEC.md)
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`

## Valeur

Détecter les relations sémantiques entre exigences hors de portée des règles déterministes : contradictions sans négation explicite et reformulations à vocabulaire disjoint.

## Enfants

| User Story | Feature | Rôle | Valeur |
|---|---|---|---|
| [`US-AUD-401`](user-stories/US-AUD-401.md) | [`FEAT-AUD-401`](features/FEAT-AUD-401/FEATURE.md) | ingénieur exigences | identifier les contradictions sémantiques via un LLM local |
| [`US-AUD-402`](user-stories/US-AUD-402.md) | [`FEAT-AUD-402`](features/FEAT-AUD-402/FEATURE.md) | ingénieur exigences | identifier les duplications sémantiques via un LLM local |

## Périmètre

Analyse sémantique par LLM local (LM Studio, endpoint OpenAI-compatible) sur des paires candidates pré-filtrées déterministement. Le LLM produit un verdict JSON structuré (`contradiction`, `duplicate`, `ok`) avec rationale. Le backend `fake` permet des tests hors-ligne déterministes. Mode opt-in (`--epic 4`) : le comportement par défaut reste déterministe. Toutes les sorties sont des propositions à revue humaine ; aucune correction automatique.

## Achèvement mesurable

Les critères candidats disposent de preuves exécutées reliées à leurs oracles indépendants et revues humainement. L'écosystème d'évaluation associé est couvert par [`EPIC-AUD-05`](../EPIC-AUD-05/EPIC.md).
