# Référence historique — Snapshot de la spécification MVP

**Nature :** snapshot historique. Les cases cochées et statuts ci-dessous décrivent la candidate d’origine ; ils ne valent pas acceptation du backlog actuel. Les identifiants historiques sont conservés pour la recherche et la continuité de planification.

Le contenu original suit verbatim.

# SPEC — Fil rouge d’ingénierie automobile assistée par IA

## 1. Informations générales

- **Identifiant projet :** `PROJ-FIL-AUTO-IA-001`
- **Nom :** Fil rouge d’ingénierie automobile assistée par IA
- **Équipe :** intégration fil rouge
- **Responsable :** responsable d’intégration
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Statut :** `Candidate`
- **Mission source :** demande utilisateur du 2026-09-13 d’analyser les branches postérieures à `develop` et de reconstruire un projet global fortement orienté IA
- **Dernière mise à jour :** `2026-09-13`

## 2. Vision et Epic

### `EPIC-FIL-AUTO-IA-001` — Conduire un lot automobile de la source à la revue

- **Vision :** réunir corpus, RAG, exigences, sélection de logiciel, qualité et traçabilité dans un parcours reproductible orchestré par des agents spécialisés.
- **Bénéficiaire principal :** ingénieur automobile, ingénieur exigences et relecteur qualité.
- **Valeur attendue :** réduire la dispersion des prototypes tout en empêchant une sortie générative d’être confondue avec une preuve.
- **Indicateur de succès :** un tiers exécute le scénario hors ligne, retrouve les sources et statuts de chaque sortie, puis constate que la décision finale reste humaine.
- **Hypothèse :** un contrat commun d’agents permet de réutiliser les apports des branches sans fusionner leurs données générées ni leurs dépendances incompatibles.

> En tant qu’équipe d’ingénierie automobile, je veux exécuter une chaîne d’agents IA sur des baselines approuvées afin d’obtenir des propositions sourcées et un dossier prêt pour une décision humaine.

## 3. Périmètre

### Inclus

- Manifeste versionné avec objectif, sources, révisions, permissions et approbation humaine.
- Agents de corpus, RAG, exigences, sélection open source, qualité, traçabilité et revue.
- Fournisseur déterministe hors ligne et connecteur Mistral optionnel.
- Citations, abstention, statuts formels et rapport JSON.
- Tests sans réseau des invariants de sécurité et de traçabilité.

### Exclus

- Téléchargement ou exécution automatique d’un dépôt tiers.
- Modification de `upstream/**`, application automatique d’un patch ou franchissement autonome d’une Gate.
- Validation réglementaire, certification ASPICE/MISRA ou avis juridique.
- Promotion d’un résultat Mistral au statut `Vérifié` sans oracle et décision humaine.
- Base vectorielle binaire versionnée dans Git.

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Besoin ou responsabilité | Décision réservée |
|---|---|---|
| Responsable de baseline | Fournir sources et révisions autorisées | Approuver la baseline avant le run |
| Ingénieur exigences | Examiner les propositions et citations | Valider, rejeter ou reformuler une exigence |
| Responsable qualité | Examiner diagnostics et conseils | Autoriser un correctif et qualifier les faux positifs |
| Responsable produit | Examiner le classement OSS | Sélectionner le projet cible |
| Relecteur indépendant | Contrôler les preuves | Décider la Gate finale |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| Socle du dépôt | Git `develop` | `335199ef45164d5c6f81ac97aa601ec2e87f56b4` | Lecture | `Observé` |
| Analyse de branches | Références Git locales | SHAs du rapport du 2026-09-13 | Lecture | `Observé`, fraîcheur distante `Non vérifié` |
| Fixture du scénario | `data/demo_baseline.json` | Git du présent lot | Lecture | `Candidat` |
| Corpus réels futurs | Sorties approuvées de `PROJ-NORM-001` et `PROJ-OSS-AUTO-001` | À figer | Lecture seule | `Bloqué` |
| Fournisseur Mistral | API configurée par l’opérateur | Modèle du manifeste/CLI | Réseau, sans écriture de secret | `Non vérifié` avant exécution |

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant | Responsable de revue |
|---|---|---|---|
| Inventaire des baselines | `Observation` | Champs du manifeste approuvé | Responsable de baseline |
| Citations RAG | `Observation` | Identifiants et révisions des passages | Ingénieur exigences |
| Exigences générées | `Proposition` | Comparaison humaine au passage source | Ingénieur exigences |
| Classement de projets | `Proposition` | Grille figée avant notation | Responsable produit |
| Diagnostics qualité | `Observation` | Rapport et code retour de l’outil | Responsable qualité |
| Conseils de correction | `Proposition` | Test rouge/vert et mutation | Responsable qualité |
| Liens de traçabilité | Statut par lien | Référence explicite et oracle indépendant | Relecteur indépendant |
| Proposition de Gate | `Proposition` ou `Bloqué` | Checklist et décision attribuée | Relecteur indépendant |

## 7. User Stories

### `US-FIL-AUTO-IA-001` — Cadrer et autoriser un run

- **Priorité :** `P1`
- **Statut :** `Candidate`
- **Dépendances :** aucune

> En tant que responsable de baseline, je veux approuver l’objectif, les sources et leurs révisions afin qu’aucun agent ne travaille sur une entrée implicite.

**Règles métier**

- `RM-FIL-AUTO-IA-001` — Un run ne démarre pas sans identifiant, objectif, baselines révisées et approbation humaine.

**Exemples**

- **Nominal :** manifeste complet et approuvé → exécution des agents.
- **Frontière :** baseline présente avec révision vide → question ouverte et blocage du corpus.
- **Contre-exemple :** approbation absente → aucun agent n’est exécuté.

**Critères associés :** `CA-FIL-01`, `CA-FIL-02`.

### `US-FIL-AUTO-IA-002` — Retrouver des passages avec abstention

- **Priorité :** `P1`
- **Statut :** `Candidate`
- **Dépendances :** `US-FIL-AUTO-IA-001`

> En tant qu’ingénieur exigences, je veux voir les passages classés et leur provenance afin d’évaluer l’ancrage avant génération.

**Règles métier**

- `RM-FIL-AUTO-IA-002` — Le RAG s’abstient quand aucun passage ne correspond à l’objectif.

**Exemples**

- **Nominal :** objectif automobile traçable → citations avec source, révision, passage et score.
- **Frontière :** un seul terme commun → résultat observable mais non promu automatiquement.
- **Contre-exemple :** objectif gastronomique → `not_found` et aucune citation utilisée.

**Critères associés :** `CA-FIL-03`, `CA-FIL-04`.

### `US-FIL-AUTO-IA-003` — Générer des propositions d’exigences

- **Priorité :** `P1`
- **Statut :** `Candidate`
- **Dépendances :** `US-FIL-AUTO-IA-002`

> En tant qu’ingénieur exigences, je veux obtenir une proposition reliée aux passages retenus afin de la revoir sans la confondre avec une exigence approuvée.

**Règles métier**

- `RM-FIL-AUTO-IA-003` — Toute exigence issue d’un fournisseur IA porte le statut `Proposition` et au moins une citation.

**Exemples**

- **Nominal :** citations disponibles → proposition avec identifiant et références.
- **Frontière :** contenu génératif variable → invariants de statut et de citation conservés.
- **Contre-exemple :** aucune citation → agent exigences `Bloqué`.

**Critères associés :** `CA-FIL-05`, `CA-FIL-06`.

### `US-FIL-AUTO-IA-004` — Comparer un projet et analyser sa qualité

- **Priorité :** `P1`
- **Statut :** `Candidate`
- **Dépendances :** `US-FIL-AUTO-IA-001`

> En tant que responsable produit et qualité, je veux un classement homogène et des conseils bornés afin de décider du projet cible et des corrections sans automatisme dangereux.

**Règles métier**

- `RM-FIL-AUTO-IA-004` — Un score IA reste une proposition et un conseil qualité n’applique jamais de patch.

**Exemples**

- **Nominal :** deux candidats sont notés avec les mêmes champs et les diagnostics reçoivent des conseils.
- **Frontière :** licence absente → question ouverte visible.
- **Contre-exemple :** aucun diagnostic → aucune correction inventée.

**Critères associés :** `CA-FIL-07`, `CA-FIL-08`.

### `US-FIL-AUTO-IA-005` — Construire une traçabilité non tautologique

- **Priorité :** `P1`
- **Statut :** `Candidate`
- **Dépendances :** `US-FIL-AUTO-IA-003`

> En tant que relecteur, je veux un statut par lien afin de distinguer une relation explicitement prouvée d’une proximité supposée.

**Règles métier**

- `RM-FIL-AUTO-IA-005` — Un lien devient `Vérifié` uniquement si un oracle et une preuve explicites sont fournis.

**Exemples**

- **Nominal :** exigence, cible, oracle et preuve → lien `Vérifié`.
- **Frontière :** cible explicite sans oracle → lien `Proposition`.
- **Contre-exemple :** mot commun sans lien déclaré → aucun lien créé.

**Critères associés :** `CA-FIL-09`, `CA-FIL-10`.

### `US-FIL-AUTO-IA-006` — Soumettre la Gate à un humain

- **Priorité :** `P1`
- **Statut :** `Candidate`
- **Dépendances :** `US-FIL-AUTO-IA-001` à `US-FIL-AUTO-IA-005`

> En tant que relecteur indépendant, je veux recevoir une synthèse des blocages et questions afin de décider la Gate sans déléguer cette autorité à l’IA.

**Règles métier**

- `RM-FIL-AUTO-IA-006` — Le résultat maximal d’un run sans décision signée est `ready-for-human-review`.

**Exemples**

- **Nominal :** aucun agent bloqué → prêt pour revue humaine.
- **Frontière :** questions non bloquantes → visibles dans la revue.
- **Contre-exemple :** agent dépendant bloqué → Gate `blocked`.

**Critères associés :** `CA-FIL-11`, `CA-FIL-12`.

## 8. Critères d’acceptation de l’Epic

- [x] `CA-FIL-01` — Un manifeste complet permet un run hors ligne sans secret ni réseau.
- [x] `CA-FIL-02` — Une approbation de baseline absente bloque le run avant tout agent.
- [x] `CA-FIL-03` — Chaque citation contient source, révision, passage et score.
- [x] `CA-FIL-04` — Une requête hors corpus produit une abstention sans citation.
- [x] `CA-FIL-05` — Une exigence générée porte le statut `Proposition`.
- [x] `CA-FIL-06` — L’agent exigences est bloqué sans citation.
- [x] `CA-FIL-07` — Tous les candidats utilisent le même contrat de score.
- [x] `CA-FIL-08` — L’agent qualité expose `automatic_apply: false`.
- [x] `CA-FIL-09` — Un lien avec oracle et preuve explicites reçoit `Vérifié`.
- [x] `CA-FIL-10` — Un lien sans oracle reste `Proposition` et aucun lien lexical n’est inféré.
- [x] `CA-FIL-11` — Le rapport final exige une décision humaine.
- [x] `CA-FIL-12` — Le mode hors ligne est couvert par des tests automatisés reproductibles.

Les cases décrivent l’implémentation candidate ; leur acceptation formelle reste soumise à revue indépendante.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Exécuter le fil rouge automobile IA

  Contexte:
    Étant donné une fixture définie avant l’implémentation
    Et un fournisseur déterministe sans réseau

  Scénario: Run complet prêt pour revue
    Étant donné des baselines révisées et approuvées
    Quand l’opérateur exécute le pipeline
    Alors les sept résultats d’agents sont présents dans l’ordre attendu
    Et la Gate vaut ready-for-human-review
    Et une décision humaine reste requise

  Scénario: Baseline non approuvée
    Étant donné une approbation humaine à false
    Quand l’opérateur exécute le pipeline
    Alors le statut vaut Bloqué
    Et aucun agent n’est exécuté

  Scénario: Question hors corpus
    Étant donné un objectif sans terme commun avec les passages
    Quand l’agent RAG recherche un contexte
    Alors il retourne not_found
    Et la liste de citations est vide

  Scénario: Lien incomplet
    Étant donné un lien explicite sans oracle ni preuve
    Quand l’agent de traçabilité construit la matrice
    Alors le lien reste Proposition

  Scénario: Fournisseur distant indisponible
    Étant donné le fournisseur Mistral sans clé API
    Quand l’opérateur initialise le fournisseur
    Alors l’exécution échoue explicitement
    Et aucun secret n’est journalisé
```

| Scénario | User Story | Critère | Oracle indépendant |
|---|---|---|---|
| Run complet | `US-FIL-AUTO-IA-001/06` | `CA-FIL-01/11/12` | Fixture JSON et séquence d’agents fixées avant exécution |
| Baseline non approuvée | `US-FIL-AUTO-IA-001` | `CA-FIL-02` | Booléen d’approbation du manifeste |
| Question hors corpus | `US-FIL-AUTO-IA-002` | `CA-FIL-04` | Vocabulaire disjoint préparé dans le test |
| Lien incomplet | `US-FIL-AUTO-IA-005` | `CA-FIL-10` | Absence explicite d’oracle et de preuve |
| Fournisseur indisponible | `US-FIL-AUTO-IA-003` | `CA-FIL-12` | Environnement contrôlé sans clé |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-FIL-AUTO-IA-001` | `US-FIL-AUTO-IA-001` | `RM-FIL-AUTO-IA-001` | `CA-FIL-01/02` | `tests/test_orchestrator.py` | `Candidat` |
| `EPIC-FIL-AUTO-IA-001` | `US-FIL-AUTO-IA-002` | `RM-FIL-AUTO-IA-002` | `CA-FIL-03/04` | `tests/test_orchestrator.py` | `Candidat` |
| `EPIC-FIL-AUTO-IA-001` | `US-FIL-AUTO-IA-003` | `RM-FIL-AUTO-IA-003` | `CA-FIL-05/06` | `src/auto_ai_flow/agents.py` | `Candidat` |
| `EPIC-FIL-AUTO-IA-001` | `US-FIL-AUTO-IA-004` | `RM-FIL-AUTO-IA-004` | `CA-FIL-07/08` | `data/demo_baseline.json` | `Candidat` |
| `EPIC-FIL-AUTO-IA-001` | `US-FIL-AUTO-IA-005` | `RM-FIL-AUTO-IA-005` | `CA-FIL-09/10` | `tests/test_orchestrator.py` | `Candidat` |
| `EPIC-FIL-AUTO-IA-001` | `US-FIL-AUTO-IA-006` | `RM-FIL-AUTO-IA-006` | `CA-FIL-11/12` | `tests/test_cli.py` | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Type | Description | Décision attendue | Responsable | Statut |
|---|---|---|---|---|---|
| `AMB-FIL-001` | Dépendance | La fraîcheur des branches distantes n’a pas pu être vérifiée faute d’authentification GitHub. | Relancer le fetch puis actualiser le rapport. | Responsable d’intégration | `Ouvert` |
| `AMB-FIL-002` | Ambiguïté | Le projet automobile open source réel n’est pas sélectionné. | Approuver un dépôt et un SHA via `PROJ-OSS-AUTO-001`. | Responsable produit | `Ouvert` |
| `AMB-FIL-003` | Risque | Le retrieval lexical est un double de test, pas une mesure sémantique. | Définir un dataset et des seuils avant l’adaptateur Qdrant. | Ingénieur exigences | `Ouvert` |
| `AMB-FIL-004` | Dépendance | Le connecteur Mistral n’est pas vérifié dans cet environnement. | Exécuter un test contrôlé avec secret fourni hors dépôt. | Opérateur | `Ouvert` |
| `AMB-FIL-005` | Risque | Les critères et pondérations de sélection OSS ne sont pas approuvés. | Figer la grille avant un classement réel. | Responsable produit | `Ouvert` |
| `AMB-FIL-006` | Risque | Les conseils qualité ne disposent pas encore d’un cycle rouge/vert/mutation intégré. | Définir l’oracle et intégrer les outils réels après revue. | Responsable qualité | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsqu’un projet automobile réel et ses corpus autorisés sont figés, que les adaptateurs RAG et qualité passent un dataset et des oracles approuvés, qu’un tiers reproduit le run, et qu’un relecteur humain consigne la décision finale sans revendication de conformité automatique.
