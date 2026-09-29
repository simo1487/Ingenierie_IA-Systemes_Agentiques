# Cycle de vie

## Statuts documentaires

- `Candidate` : spécification proposée, non validée
- `Accepté` : validé par revue humaine
- `Obsolète` : remplacé ou retiré

## Statuts de preuve

- `Candidat` : preuve produite mais non revue
- `Vérifié` : preuve revue par un tiers avec oracle indépendant
- `Rejeté` : preuve invalidée

## Workflow

```text
Candidate → À faire → En cours → Prêt pour revue → Accepté
```

Aucun statut ne peut être promu automatiquement par l'outil : la revue reste humaine.
