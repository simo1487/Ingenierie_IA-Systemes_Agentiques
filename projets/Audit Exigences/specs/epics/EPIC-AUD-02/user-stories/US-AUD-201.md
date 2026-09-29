# US-AUD-201 — Détecter les exigences dupliquées

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-AUD-02`](../EPIC.md)
- **Feature fille :** [`FEAT-AUD-201`](../features/FEAT-AUD-201/FEATURE.md)
- **Niveau :** `Socle`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** Aucune

## Besoin

> En tant qu'ingénieur exigences, je veux détecter les exigences dupliquées afin d'éviter les redondances dans le dataset.

## Entrées et sorties

- **Entrée :** Dataset d'exigences avec `id` et `text`.
- **Sortie :** Rapport JSON des groupes de duplication avec paires d'ids et score de similarité.

## Règle et critères

`RM-AUD-201` — Deux exigences sont signalées comme dupliquées si leur similarité dépasse le seuil configuré ; le score est une proposition, pas une décision de suppression.

- [ ] `CA-AUD-201-01` — Étant donné deux exigences ont un texte identique, quand l'audit est exécuté, alors la paire est signalée avec un score de 1.0.
- [ ] `CA-AUD-201-02` — Étant donné deux exigences sont similaires au-dessus du seuil, quand l'audit est exécuté, alors la paire est signalée avec son score et le seuil utilisé.
- [ ] `CA-AUD-201-03` — Étant donné deux exigences partagent des mots mais traitent des sujets différents, quand l'audit est exécuté, alors la paire reste sous le seuil et n'est pas signalée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | deux exigences ont un texte identique | l'audit est exécuté | la paire est signalée avec un score de 1.0 |
| Frontière | deux exigences sont similaires au-dessus du seuil | l'audit est exécuté | la paire est signalée avec son score et le seuil |
| Refus | deux exigences partagent des mots mais traitent des sujets différents | l'audit est exécuté | la paire reste sous le seuil et n'est pas signalée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Détecter les exigences dupliquées
  Scénario: Nominal — CA-AUD-201-01
    Étant donné deux exigences avec un texte identique
    Quand l'audit duplication est exécuté
    Alors la paire est signalée avec un score de 1.0

  Scénario: Refus — CA-AUD-201-03
    Étant donné deux exigences sur des sujets différents
    Quand l'audit duplication est exécuté
    Alors aucune paire n'est signalée
```

## Oracle indépendant

Similarité Jaccard sur tokens normalisés ; le seuil est figé avant exécution et documenté dans le rapport.

## Réalisation et preuves

- [`FEAT-AUD-201`](../features/FEAT-AUD-201/FEATURE.md) — Feature candidate
- [`TASK-AUD-201-01`](../features/FEAT-AUD-201/tasks/TASK-AUD-201-01.md) — Figer le seuil et l'oracle
- [`TASK-AUD-201-02`](../features/FEAT-AUD-201/tasks/TASK-AUD-201-02.md) — Implémenter la comparaison
- [`TASK-AUD-201-03`](../features/FEAT-AUD-201/tasks/TASK-AUD-201-03.md) — Générer le rapport
