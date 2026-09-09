# Socle commun et intégration

- **Responsable :** responsable d’intégration du dépôt
- **Branche :** `develop`
- **Spécification :** [SPEC.md](SPEC.md)

Ce projet transverse maintient les conventions du monorepo, les contrôles génériques et la décision d’intégration. Il ne contient pas le code métier des autres équipes.

## Commandes communes

```bash
make setup-hooks
make check
```

Les tests propres aux projets restent documentés et exécutés dans chaque `projets/<slug>/README.md`.
