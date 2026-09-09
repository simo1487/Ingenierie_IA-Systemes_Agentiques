# Projet Normes

- **Équipe :** Alain et Moustapha
- **Branche principale :** `feat/GetNormes`
- **Préparation :** `feat/initSearchSystem`
- **Spécification :** [SPEC.md](SPEC.md)
- **Statut :** expérimentation et structuration du corpus en cours

## Actifs actuels

L’implémentation historique se trouve encore dans [`normes-software-embarque-automobile/`](../../normes-software-embarque-automobile/). Elle contient le catalogue, le registre des sources, le script de récupération et le manifeste. Elle sera déplacée ici dans une pull request de migration dédiée, sans changement fonctionnel simultané.

## Commandes actuelles

```bash
python3 normes-software-embarque-automobile/telecharger_sources.py --help
```

L’exécution réseau réelle n’est pas un contrôle pre-commit et peut produire des échecs d’accès attendus.
