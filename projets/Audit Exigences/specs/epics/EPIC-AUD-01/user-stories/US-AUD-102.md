# US-AUD-102 — Détecter les fautes d'orthographe

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-AUD-01`](../EPIC.md)
- **Feature fille :** [`FEAT-AUD-102`](../features/FEAT-AUD-102/FEATURE.md)
- **Niveau :** `Socle`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** Aucune

## Besoin

> En tant qu'ingénieur exigences, je veux détecter les fautes d'orthographe avec leur position et une proposition de correction afin d'améliorer la qualité des spécifications.

## Entrées et sorties

- **Entrée :** Dataset d'exigences avec `id` et `text`.
- **Sortie :** Rapport JSON des fautes d'orthographe avec id d'exigence, position du caractère, mot fautif et correction proposée.

## Règle et critères

`RM-AUD-102` — Une faute d'orthographe est signalée avec sa position exacte et une proposition issue du dictionnaire ; aucune correction n'est appliquée automatiquement.

- [ ] `CA-AUD-102-01` — Étant donné une exigence contient une faute du dictionnaire, quand l'audit orthographe est exécuté, alors la faute est signalée avec sa position exacte et la correction proposée.
- [ ] `CA-AUD-102-02` — Étant donné une exigence contient plusieurs fautes, quand l'audit est exécuté, alors chaque faute est signalée individuellement avec sa position.
- [ ] `CA-AUD-102-03` — Étant donné une exigence ne contient aucune faute connue du dictionnaire, quand l'audit est exécuté, alors aucune anomalie d'orthographe n'est rapportée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | une exigence contient "systéme" | l'audit orthographe est exécuté | la faute est signalée à sa position avec "système" en suggestion |
| Frontière | une exigence contient plusieurs fautes | l'audit est exécuté | chaque faute est signalée individuellement avec sa position |
| Refus | une exigence ne contient aucune faute connue | l'audit est exécuté | aucune anomalie d'orthographe n'est rapportée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Détecter les fautes d'orthographe
  Scénario: Nominal — CA-AUD-102-01
    Étant donné une exigence contenant "systéme"
    Quand l'audit orthographe est exécuté
    Alors la faute est signalée à sa position avec "système" en correction

  Scénario: Refus — CA-AUD-102-03
    Étant donné une exigence sans faute connue du dictionnaire
    Quand l'audit orthographe est exécuté
    Alors aucune anomalie n'est rapportée
```

## Oracle indépendant

Dictionnaire de fautes figé avant exécution ; la correction proposée vient du dictionnaire, jamais générée. Relecture humaine avant adoption.

## Réalisation et preuves

- [`FEAT-AUD-102`](../features/FEAT-AUD-102/FEATURE.md) — Feature candidate
- [`TASK-AUD-102-01`](../features/FEAT-AUD-102/tasks/TASK-AUD-102-01.md) — Spécifier et figer l'oracle
- [`TASK-AUD-102-02`](../features/FEAT-AUD-102/tasks/TASK-AUD-102-02.md) — Réaliser dans le périmètre autorisé
- [`TASK-AUD-102-03`](../features/FEAT-AUD-102/tasks/TASK-AUD-102-03.md) — Vérifier et soumettre à revue
