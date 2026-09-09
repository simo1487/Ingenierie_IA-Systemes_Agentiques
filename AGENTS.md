# Règles du dépôt

- Lire le `README.md` et le `SPEC.md` du projet concerné avant toute modification. Suivre les commandes locales plutôt que supposer une chaîne de build globale.
- Travailler dans `projets/<slug>/` pour tout nouveau projet. Séparer `experiments/`, code maintenu `src/`, `tests/`, `docs/`, petites données `data/` et preuves `evidence/` selon [`docs/architecture-monorepo.md`](docs/architecture-monorepo.md).
- Ne jamais modifier un chemin `upstream/`. Ne pas déplacer un actif historique pendant une modification fonctionnelle.
- Distinguer explicitement proposition, observation, preuve vérifiée et question ouverte. Ne jamais inventer une information absente.
- Une similarité de vocabulaire ne prouve pas une relation de traçabilité. Définir les oracles avant le code et refuser les tests tautologiques.
- Pour un défaut : reproduire, obtenir un rouge pertinent, appliquer un patch minimal, obtenir le vert, puis éprouver le test par mutation.
- Toute alerte d’outil et toute affirmation documentaire nécessitent une vérification et une décision humaines.
- Ne pas revendiquer une conformité ou une certification à partir de ces expérimentations.
- Avant revue, exécuter les tests documentés par le projet puis `make check`.
- Utiliser les skills `.devin/skills/` correspondant à la phase G0, G1, G2 ou à l’évaluation d’une Gate ; les méthodes détaillées restent dans [`workflows/README.md`](workflows/README.md).
