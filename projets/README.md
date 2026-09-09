# Projets de l’atelier

Ce dossier centralise les spécifications macro de travail définies dans [`travail.md`](../travail.md). L'architecture documentaire complète, les modèles d'artefacts (features, Example Mapping, traçabilité, enquêtes) et les règles de conformité J01–J03 sont décrits dans [`specs/README.md`](../specs/README.md). Chaque projet possède un périmètre, des livrables et des critères de vérification propres.

| Branche | Équipe ou fonction | Spécification |
|---|---|---|
| `develop` | Intégration du travail commun | [`socle-commun/SPEC.md`](socle-commun/SPEC.md) |
| `feat/initSearchSystem` | Initialisation technique de la recherche de normes | [`normes/initialisation-recherche/SPEC.md`](normes/initialisation-recherche/SPEC.md) |
| `feat/GetNormes` | Alain et Moustapha — Normes | [`normes/SPEC.md`](normes/SPEC.md) |
| `feat_Cppcheck` | Eric, Céline et Damien — Qualité du code | [`qualite-code/SPEC.md`](qualite-code/SPEC.md) |
| `feat_list_existing_projects` | Sylvain, Nathalie et Romain — Logiciel automobile open source | [`logiciel-automobile-open-source/SPEC.md`](logiciel-automobile-open-source/SPEC.md) |
| `feat_getReq` | Mohammed et Florient — Exigences Zephyr | [`exigences-zephyr/SPEC.md`](exigences-zephyr/SPEC.md) |

## Structure d’un projet

Chaque dossier `projets/<slug>/` devient le point d’entrée autonome de son projet. Il contient sa spécification et, lorsqu’ils existent, son `README.md`, ses `experiments/`, son code `src/`, ses `tests/`, sa documentation `docs/`, ses petites données redistribuables `data/` et ses preuves `evidence/`.

Le modèle est disponible dans [`_template/README.md`](_template/README.md) et les décisions d’architecture sont décrites dans [`docs/architecture-monorepo.md`](../docs/architecture-monorepo.md). Les actifs historiques ne sont pas déplacés pendant une modification fonctionnelle ; leur migration se fait dans une pull request dédiée.

## Règles communes

- Travailler uniquement dans le périmètre de la branche attribuée.
- Synchroniser la branche avec `develop` avant la revue.
- Conserver pour chaque information sa source, sa version ou date de consultation et son statut de vérification.
- Distinguer une observation, une proposition générée et une preuve vérifiée.
- Ne pas reproduire de contenu protégé ou contourner un contrôle d’accès.
- Ne jamais présenter un document collecté comme une preuve de conformité.
- Signaler explicitement les informations inconnues ou non vérifiées.
- Livrer une documentation permettant à une autre personne de reproduire les contrôles.
- Faire relire le résultat avant intégration dans `develop`.

## Statuts autorisés

| Statut | Signification |
|---|---|
| `Observé` | Information directement constatée dans une source identifiée |
| `Candidat` | Information proposée ou extraite, encore à vérifier |
| `Vérifié` | Information contrôlée par une personne contre la source indiquée |
| `Non vérifié` | Information conservée sans validation suffisante |
| `Bloqué` | Travail impossible sans donnée, accès ou décision supplémentaire |
