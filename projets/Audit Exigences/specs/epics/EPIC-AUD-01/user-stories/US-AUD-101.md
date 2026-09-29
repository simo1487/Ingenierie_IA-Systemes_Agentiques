# US-AUD-101 — Auditer la grammaire des exigences

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-AUD-01`](../EPIC.md)
- **Feature fille :** [`FEAT-AUD-101`](../features/FEAT-AUD-101/FEATURE.md)
- **Niveau :** `Socle`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** Aucune

## Besoin

> En tant qu'ingénieur exigences, je veux détecter les erreurs de grammaire (accord sujet-verbe, ponctuation, capitalisation) afin d'améliorer la lisibilité des spécifications.

## Entrées et sorties

- **Entrée :** Dataset d'exigences JSON/Markdown avec `id`, `text`, `source`, `version`.
- **Sortie :** Rapport JSON des anomalies grammaticales avec id d'exigence, position, type (`grammar`, `punctuation`, `capitalization`) et proposition.

## Règle et critères

`RM-AUD-101` — Une erreur grammaticale est signalée avec sa position exacte et le type détecté ; aucune correction n'est appliquée automatiquement.

- [ ] `CA-AUD-101-01` — Étant donné une exigence contient une erreur d'accord sujet-verbe après un modal ("shall logs"), quand l'audit grammaire est exécuté, alors l'erreur est signalée avec sa position et une proposition.
- [ ] `CA-AUD-101-02` — Étant donné une exigence contient un double espace, quand l'audit est exécuté, alors l'anomalie de ponctuation est signalée à la position du double espace.
- [ ] `CA-AUD-101-03` — Étant donné une exigence ne commence pas par une majuscule, quand l'audit est exécuté, alors l'anomalie de capitalisation est signalée avec une proposition.
- [ ] `CA-AUD-101-04` — Étant donné une exigence grammaticalement correcte, quand l'audit grammaire est exécuté, alors aucune anomalie de grammaire n'est rapportée pour cette exigence.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | une exigence contient "shall logs errors" | l'audit grammaire est exécuté | l'erreur d'accord est signalée avec la position et la suggestion "shall log" |
| Frontière | une exigence contient un double espace | l'audit est exécuté | l'anomalie de ponctuation est signalée avec sa position |
| Refus | une exigence est grammaticalement correcte | l'audit est exécuté | aucune anomalie n'est rapportée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Auditer la grammaire des exigences
  Scénario: Nominal — CA-AUD-101-01
    Étant donné une exigence contenant "shall logs errors"
    Quand l'audit grammaire est exécuté
    Alors l'erreur d'accord est signalée avec sa position et "shall log" en suggestion

  Scénario: Refus — CA-AUD-101-03
    Étant donné une exigence grammaticalement correcte
    Quand l'audit grammaire est exécuté
    Alors aucune anomalie n'est rapportée pour cette exigence
```

## Oracle indépendant

Règles d'accord figées avant exécution ; relecture humaine des propositions avant adoption.

## Réalisation et preuves

- [`FEAT-AUD-101`](../features/FEAT-AUD-101/FEATURE.md) — Feature candidate
- [`TASK-AUD-101-01`](../features/FEAT-AUD-101/tasks/TASK-AUD-101-01.md) — Spécifier et figer l'oracle
- [`TASK-AUD-101-02`](../features/FEAT-AUD-101/tasks/TASK-AUD-101-02.md) — Réaliser dans le périmètre autorisé
- [`TASK-AUD-101-03`](../features/FEAT-AUD-101/tasks/TASK-AUD-101-03.md) — Vérifier et soumettre à revue
