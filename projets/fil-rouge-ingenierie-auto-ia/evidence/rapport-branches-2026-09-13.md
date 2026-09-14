# Rapport d’analyse des branches postérieures à `develop`

## Baseline et méthode

- **Dépôt observé :** `FormationIaProject`
- **Branche courante au relevé :** `develop`
- **Commit de référence :** `335199ef45164d5c6f81ac97aa601ec2e87f56b4`
- **Date du commit de référence :** `2026-09-10T14:02:44+02:00`
- **Date du relevé :** `2026-09-13`
- **Fraîcheur distante :** `Non vérifié`. `git fetch --prune origin` a échoué faute d’authentification GitHub ; l’analyse porte sur les références locales déjà présentes.
- **Critère d’inclusion :** date du commit de tête strictement postérieure à celle de `develop`.
- **Contrôles exécutés :** merge-base, avance/retard, commits propres, fichiers et volumes modifiés, intersections de chemins, parsing AST des fichiers Python modifiés, recherche défensive de fichiers à revoir, `git diff --check`.
- **Contrôles non exécutés :** suites fonctionnelles propres aux branches et appels réseau/API.

## Synthèse

| Branche | SHA tête | Écart `develop...branche` | Volume | Tests Python ajoutés/modifiés | Décision proposée |
|---|---|---:|---:|---:|---|
| `test/programme` | `707e6d63b339d35f5b4920756c0f198eede8045f` | 0 / 1 | +885 / -1 | 1 | Intégrer sélectivement le pipeline RAG complet |
| `develop_Mo` | `c28962c73fbf5459e76a65788d629410766fe7fb` | 0 / 2 | +21 794 / -64 | 11 | Extraire l’architecture modulaire, pas les données brutes |
| `Alain` | `78127504bd57591764faa6a5f222e419d0f91f41` | 0 / 2 | +303 698 / -96, 1 binaire | 1 | Extraire spec, citations et abstention ; exclure index/résultats générés |
| `develop_florian` | `e542beb987b7987e6d1b8d5d885ed9293f18ba40` | 0 / 2 | +2 065 | 4 | Extraire machine à états et sandbox après revue sécurité |
| `Romain` | `e1bd0ec2354ad40b427eaf1071e4d9f25484f85b` | 0 / 4 | +2 744 | 6 | Extraire recherche structurée, scoring et rendu |
| `Damien` | `571d5d5df3a9fc23e4f8160fdc5b9852046a8a43` | 0 / 1 | +632 / -11 | 0 | Reprendre parsing de diagnostics et bornage des patchs après tests dédiés |
| `develop_celine` | `a3faebeb6ee7062ba17716d65ae5306cd2b7b872` | 0 / 2 | +698 / -1 | 0 | Reprendre le mode simulation et la revue humaine, corriger la portabilité |
| `exerciceMostapha` | `9319f7005f39a998bbf75ec3f58e957bf5be1663` | 0 / 2 | +103 634, 1 binaire | 0 | Conserver reranking et examinateur comme expériences, pas comme preuves |
| `develop_eric` | `2e8b717fece64c848b7f3ce0bc3ef033f5e934a8` | 0 / 1 | +10 912, 1 binaire | 0 | Ne pas promouvoir l’index ; corriger avant intégration |
| `feat_list_existing_projects` | `fd32cdae87d963f6959b26750f0b74bbe571132f` | 46 / 1 | +588 / -190 | 2 | Porter le commit sur une branche synchronisée, sans fusion directe |

`Écart develop...branche` indique les commits propres à `develop`, puis les commits propres à la branche.

## Observations par branche

### `test/programme`

Pipeline pédagogique le plus cohérent de l’ensemble : chargement multi-format, cinq stratégies de chunking, Qdrant, génération Mistral, citations, abstention, RAGAS, Gradio et double déterministe. Le diff est propre et les quatre tests ciblent dataset de référence, stratégies, citations et abstention. Le commit est intitulé comme un auto-stash ; sa provenance doit être confirmée avant intégration.

### `develop_Mo`

Architecture RAG modulaire avec interfaces de backends réels/faux et tests unitaires, intégration et E2E. Bonne source pour les contrats d’agents et l’injection de doubles. Le lot contient cependant un HTML volumineux, de nombreux rapports et 369 anomalies `git diff --check`; il ne doit pas être fusionné en bloc.

### `Alain`

Spécification détaillée du workflow ASPICE, retrieval inspectable, seuil d’abstention, journal JSONL et interface Gradio. Le lot versionne une base Qdrant et plus de 300 000 lignes de résultats générés. Il comporte 59 anomalies de whitespace et modifie les scripts de chunking communs. Intégration recommandée par extraction ciblée.

### `develop_florian`

Machine à états multi-agents avec transitions déclenchées par l’utilisateur, outils limités à un workspace, RAG documentaire et tests de transitions. C’est l’apport architectural majeur pour les Gates humaines. Une détection défensive a signalé un fichier de workspace contenant une affectation ressemblant à un identifiant sensible ; sa valeur n’a pas été reproduite et une revue humaine est requise avant toute reprise. Le diff contient aussi 19 anomalies de whitespace.

### `Romain`

Agent de recherche de projets avec web search Mistral, normalisation JSON, score par candidat, template Jinja2 et tests hors réseau. L’usage de la recherche web nécessite une validation des sources et ne doit pas convertir le score du LLM en décision. Le diff contient 34 anomalies de whitespace et mélange agent maintenu et exercices personnels.

### `Damien`

Agent qualité complet : découverte d’outils, parsing Cppcheck XML, diagnostic Mistral structuré, contrôle des chemins de patch, validation syntaxique et recontrôle. Le script peut créer une branche et appliquer un patch ; ces effets doivent rester derrière une autorisation explicite. Aucun test n’accompagne les 608 lignes du nouvel agent. Le correctif PowerShell préserve correctement le code retour Cppcheck malgré la sortie XML sur stderr.

### `develop_celine`

Workflow MISRA en simulation par défaut, branche dédiée en mode `--apply`, contrôle de périmètre et validation humaine. L’implémentation contient un chemin Cppcheck Windows codé en dur et appelle directement des commandes Git ; elle n’est pas portable telle quelle. La modification de `tools/check_repo.py` autorise `.env.example`, mais ce changement transversal doit être revu séparément.

### `exerciceMostapha`

Chaîne RAG ASPICE étendue : indexation, citations, génération, reranker, mode interactif et examinateur. Les résultats sont pédagogiquement riches mais sans tests automatisés dans le diff et avec une base Qdrant versionnée. Les jugements de l’examinateur sont génératifs et ne peuvent pas servir seuls d’oracle.

### `develop_eric`

Chunking hiérarchique des exigences Zephyr, Qdrant et jeu de vingt requêtes. Le rapport versionné observe 0/20 résultats au-dessus du seuil et 1/20 catégories attendues. C’est une preuve d’échec utile : l’alignement embedding/index/requête doit être corrigé avant réutilisation. La base Qdrant binaire ne doit pas être intégrée.

### `feat_list_existing_projects`

Collecte multi-moteurs, normalisation d’URL, déduplication par site, préfiltrage et tests unitaires sans réseau. La branche est basée 46 commits derrière `develop` et son propre message indique que le script n’est pas fonctionnel. Le code intéressant doit être porté sur une branche à jour et évalué contre une liste de moteurs approuvée.

## Risques d’intégration croisée

Les chevauchements directs portent surtout sur `exercices/rag/pyproject.toml`, `requirements.txt`, `.env.example` et `01_fixed_token_chunking.py`. Les conflits conceptuels sont plus larges : ChromaDB contre Qdrant, embeddings Mistral contre HuggingFace, modèles cloud contre Ollama, et formats de citations différents. Une API commune doit précéder toute reprise.

Les bases vectorielles, fichiers `.lock`, SQLite, rapports massifs et corpus téléchargés ne sont pas des sources maintenues. Ils doivent être régénérables ou conservés hors Git, avec seulement de petites fixtures et synthèses dans `evidence/`.

## Recommandation d’intégration

1. Utiliser un contrat commun `AIProvider` avec double déterministe et connecteur Mistral optionnel.
2. Imposer un manifeste de run avec sources, révisions, permissions et approbation humaine.
3. Conserver l’abstention, les citations et les références indépendantes de `test/programme`.
4. Reprendre la machine à états de `develop_florian`, sans permettre aux agents de franchir une Gate.
5. Séparer observation qualité, proposition de correction, application et recontrôle.
6. Ajouter Qdrant et le reranking seulement après une évaluation rouge/verte sur dataset approuvé.
7. Porter les apports branche par branche ; ne fusionner aucune des branches volumineuses en bloc.
