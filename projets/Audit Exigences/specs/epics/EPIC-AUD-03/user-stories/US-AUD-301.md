# US-AUD-301 — Détecter les exigences contradictoires

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-AUD-03`](../EPIC.md)
- **Feature fille :** [`FEAT-AUD-301`](../features/FEAT-AUD-301/FEATURE.md)
- **Niveau :** `Socle`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** US-AUD-201

## Besoin

> En tant qu'ingénieur exigences, je veux identifier les exigences contradictoires afin de résoudre les incohérences.

## Entrées et sorties

- **Entrée :** Dataset d'exigences avec `id` et `text`.
- **Sortie :** Rapport JSON des couples contradictoires avec le motif de contradiction détecté.

## Règle et critères

`RM-AUD-301` — Une contradiction est signalée uniquement sur un motif explicite (négation opposée, valeur numérique incompatible) ; le couple reste une proposition à arbitrer.

- [ ] `CA-AUD-301-01` — Étant donné deux exigences imposent des comportements opposés sur le même sujet, quand l'audit est exécuté, alors le couple est signalé avec le motif de négation opposée.
- [ ] `CA-AUD-301-02` — Étant donné deux exigences fixent des valeurs numériques incompatibles sur la même grandeur, quand l'audit est exécuté, alors le couple est signalé avec les valeurs en conflit.
- [ ] `CA-AUD-301-03` — Étant donné deux exigences traitent de sujets différents, quand l'audit est exécuté, alors aucune contradiction n'est signalée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | deux exigences imposent des comportements opposés sur le même sujet | l'audit est exécuté | le couple est signalé avec le motif de négation opposée |
| Frontière | deux exigences fixent des valeurs numériques incompatibles | l'audit est exécuté | le couple est signalé avec les valeurs en conflit |
| Refus | deux exigences traitent de sujets différents | l'audit est exécuté | aucune contradiction n'est signalée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Détecter les exigences contradictoires
  Scénario: Nominal — CA-AUD-301-01
    Étant donné "Le système doit activer le mode dégradé" et "Le système ne doit pas activer le mode dégradé"
    Quand l'audit contradiction est exécuté
    Alors le couple est signalé avec le motif "négation opposée"

  Scénario: Refus — CA-AUD-301-03
    Étant donné deux exigences sur des sujets différents
    Quand l'audit contradiction est exécuté
    Alors aucune contradiction n'est signalée
```

## Oracle indépendant

Patterns de contradiction figés avant exécution (négations, valeurs) ; revue humaine des couples signalés avant arbitrage.

## Réalisation et preuves

- [`FEAT-AUD-301`](../features/FEAT-AUD-301/FEATURE.md) — Feature candidate
- [`TASK-AUD-301-01`](../features/FEAT-AUD-301/tasks/TASK-AUD-301-01.md) — Figer les patterns et l'oracle
- [`TASK-AUD-301-02`](../features/FEAT-AUD-301/tasks/TASK-AUD-301-02.md) — Implémenter la détection
- [`TASK-AUD-301-03`](../features/FEAT-AUD-301/tasks/TASK-AUD-301-03.md) — Générer le rapport
