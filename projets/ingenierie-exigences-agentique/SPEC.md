# SPEC — Produit d’ingénierie des exigences agentique

## 1. Informations générales

- **Identifiant projet :** `PROJ-REQ-AI-001`
- **Équipe :** Ingénierie des exigences agentique
- **Responsables :** Mohammed et Florient
- **Branche :** `feat_getReq`
- **Statut :** `Draft`
- **Mission source :** objectif réadapté le 2026-09-09 : mettre en place dynamiquement une chaîne d’ingénierie des exigences avec des agents IA et l’appliquer aux projets open source retenus
- **Dernière mise à jour :** `2026-09-09`

## 2. Vision et Epic

### `EPIC-REQ-AI-001` — Orchestrer une ingénierie des exigences vérifiable

- **Vision :** fournir un produit configurable qui coordonne des agents spécialisés pour collecter, auditer, structurer et tracer des exigences sans transformer leurs propositions en preuves.
- **Bénéficiaire principal :** ingénieur exigences et responsable produit.
- **Valeur attendue :** appliquer la même démarche à différentes baselines, notamment aux projets open source sélectionnés, tout en gardant les inconnues et décisions humaines visibles.
- **Indicateur de succès :** sur une baseline approuvée, un tiers reproduit un run, retrouve chaque sortie dans ses sources et distingue les résultats proposés, observés, vérifiés ou bloqués.
- **Hypothèse à valider :** une orchestration multi-agents apporte une meilleure couverture ou reproductibilité qu’un traitement manuel ou mono-agent équivalent.

> En tant qu’ingénieur exigences, je veux configurer et exécuter une chaîne d’agents spécialisés sur une baseline choisie afin d’obtenir un backlog auditable et traçable sans déléguer les décisions de validation à l’IA.

## 3. Périmètre

### Inclus

- Configuration d’un lot : objectif, acteurs, sources, révisions, permissions et formats attendus.
- Orchestration dynamique d’agents de collecte, audit, Example Mapping, spécification et traçabilité.
- Production d’Epics, User Stories, règles, critères d’acceptation, scénarios Gherkin et registre d’ambiguïtés.
- Qualification systématique des sorties et journalisation des étapes et sources.
- Application aux baselines open source approuvées par `PROJ-OSS-AUTO-001`.
- Revue humaine avant tout passage au statut `Vérifié` ou `Validated`.

### Exclus

- Invention d’un comportement absent des sources ou résolution automatique d’une ambiguïté métier.
- Certification, avis juridique ou déclaration de conformité réglementaire.
- Modification automatique d’un dépôt source ou de `upstream/**`.
- Exécution non approuvée de code tiers, usage de secrets ou élévation de privilèges.
- Apprentissage autonome sur des données non autorisées.

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Responsabilité | Décision réservée |
|---|---|---|
| Responsable produit | Définir la finalité du lot | Approuver l’Epic, les priorités et le périmètre |
| Ingénieur exigences | Examiner les exigences et exemples | Valider, rejeter ou reformuler une exigence |
| Responsable de baseline | Fournir les sources autorisées | Approuver révisions, accès et licences |
| Relecteur indépendant | Contrôler oracles et traçabilité | Attribuer `Vérifié` et décider la Gate |
| Opérateur | Configurer et lancer un run | Autoriser les outils et actions avec effets de bord |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| Objectif du lot | Décision du responsable produit | Version du dossier de cadrage | Lecture | `Candidat` jusqu’à approbation |
| Projet open source retenu | Sortie de `PROJ-OSS-AUTO-001` | Tag ou commit approuvé | Lecture seule | `Bloqué` tant que non sélectionné |
| Références normatives autorisées | Sortie de `PROJ-NORM-001` | Éditions et révisions propres | Lecture seule | Selon statut du corpus |
| Politique d’agents et permissions | Configuration versionnée du produit | Commit du run | Lecture à l’exécution | `Candidat` |
| Décisions humaines antérieures | Journal de revue | Version et auteur | Lecture | `Observé` |

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant |
|---|---|---|
| Manifeste du run | `Observation` | Comparaison entre configuration, agents invoqués et traces horodatées |
| Corpus d’exigences | `Proposition` ou `Observation` | Passage exact dans la baseline figée |
| Epic et User Stories | `Proposition` | Approbation du responsable produit et couverture des sources |
| Example Mapping et Gherkin | `Proposition` | Règles approuvées et oracles définis hors implémentation |
| Matrice de traçabilité | `Proposition` puis `Preuve vérifiée` par lien | Inspection ou test indépendant de chaque relation |
| Registre d’ambiguïtés | `Question ouverte` | Présence de toute information manquante détectée |
| Décision de revue | `Preuve vérifiée` | Identité du relecteur, critères examinés et décision consignée |

## 7. User Stories

### `US-REQ-AI-001` — Cadrer un lot dynamiquement

> En tant que responsable produit, je veux décrire l’objectif, les baselines, les permissions et les sorties d’un lot afin que l’orchestration soit reproductible et bornée.

- `RM-REQ-AI-001` — Un run ne démarre pas sans objectif, source canonique, révision et politique d’accès explicites.
- **Nominal :** une baseline approuvée et un objectif singulier produisent un manifeste de configuration.
- **Frontière :** une source sans révision reste enregistrable mais bloque l’analyse probante.
- **Contre-exemple :** une demande d’écriture dans `upstream/**` est refusée.
- **Critères associés :** `CA-REQ-AI-01`, `CA-REQ-AI-02`.

### `US-REQ-AI-002` — Orchestrer les agents spécialisés

> En tant qu’opérateur, je veux que le produit sélectionne les agents nécessaires selon les sorties demandées afin d’adapter le workflow sans perdre l’ordre ni la provenance des opérations.

- `RM-REQ-AI-002` — Chaque agent reçoit uniquement les entrées et permissions nécessaires à sa tâche.
- **Nominal :** une demande de backlog et traçabilité déclenche cadrage, collecte, audit, spécification puis traçabilité.
- **Frontière :** un lot demandant seulement un audit n’invoque pas les étapes de génération non requises.
- **Contre-exemple :** l’échec d’un agent bloque ses sorties dépendantes et reste visible.
- **Critères associés :** `CA-REQ-AI-03`, `CA-REQ-AI-04`, `CA-REQ-AI-05`.

### `US-REQ-AI-003` — Auditer et structurer les exigences

> En tant qu’ingénieur exigences, je veux recevoir des exigences singulières, des exemples et des ambiguïtés explicites afin de préparer un backlog vérifiable.

- `RM-REQ-AI-003` — Une information manquante devient une question ouverte, jamais un comportement inventé.
- **Nominal :** une règle sourcée produit une User Story, un exemple nominal, une frontière et un contre-exemple.
- **Frontière :** une exigence composée est découpée en propositions singulières reliées à l’énoncé initial.
- **Contre-exemple :** une exigence non retrouvable ne reçoit pas le statut `Vérifié`.
- **Critères associés :** `CA-REQ-AI-06`, `CA-REQ-AI-07`.

### `US-REQ-AI-004` — Construire une traçabilité explicable

> En tant que relecteur, je veux relier Epic, User Stories, sources, code et tests avec un statut par lien afin de distinguer couverture démontrée et hypothèse.

- `RM-REQ-AI-004` — Une similarité lexicale ne prouve aucune relation de traçabilité.
- **Nominal :** un lien explicitement documenté dans la baseline est enregistré avec sa source.
- **Frontière :** un lien plausible sans preuve reste `Candidat`.
- **Contre-exemple :** un fichier contenant seulement le même mot-clé n’est pas relié automatiquement.
- **Critères associés :** `CA-REQ-AI-08`, `CA-REQ-AI-09`.

### `US-REQ-AI-005` — Revoir et reproduire un run

> En tant que relecteur indépendant, je veux rejouer le lot et examiner ses preuves afin d’accepter ou refuser séparément chaque sortie et la spécification globale.

- `RM-REQ-AI-005` — Seul un humain identifié peut promouvoir une proposition au statut de validation prévu.
- **Nominal :** le même manifeste et les mêmes baselines reproduisent des sorties structurellement équivalentes et leurs sources.
- **Frontière :** une sortie non déterministe est acceptée seulement si les invariants vérifiables sont définis et satisfaits.
- **Contre-exemple :** un run incomplet ou sans journal ne peut pas être déclaré validé.
- **Critères associés :** `CA-REQ-AI-10`, `CA-REQ-AI-11`, `CA-REQ-AI-12`.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-REQ-AI-01` — Chaque run possède un identifiant, un objectif singulier et une configuration versionnée.
- [ ] `CA-REQ-AI-02` — Chaque entrée indique sa source, sa révision, son niveau d’accès et son statut.
- [ ] `CA-REQ-AI-03` — Le plan d’orchestration indique les agents, leurs dépendances, entrées, sorties et permissions.
- [ ] `CA-REQ-AI-04` — Seules les étapes nécessaires aux sorties demandées sont exécutées.
- [ ] `CA-REQ-AI-05` — Un échec ou timeout bloque les sorties dépendantes sans masquer les résultats indépendants déjà obtenus.
- [ ] `CA-REQ-AI-06` — Chaque exigence produite est singulière, claire, vérifiable et reliée à son énoncé source ou marquée comme proposition.
- [ ] `CA-REQ-AI-07` — Chaque règle possède un exemple nominal, une frontière, un contre-exemple et ses questions ouvertes.
- [ ] `CA-REQ-AI-08` — Chaque lien de traçabilité porte un statut autorisé et une justification inspectable.
- [ ] `CA-REQ-AI-09` — Aucun lien n’est promu sur la seule base d’une similarité lexicale.
- [ ] `CA-REQ-AI-10` — Chaque sortie est qualifiée `Proposition`, `Observation`, `Preuve vérifiée` ou `Question ouverte`.
- [ ] `CA-REQ-AI-11` — Un tiers peut rejouer le run à partir du manifeste et des baselines disponibles.
- [ ] `CA-REQ-AI-12` — Toute validation finale indique le relecteur, la date, les critères examinés et les réserves.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Orchestrer un lot d’ingénierie des exigences

  Scénario: Produire un backlog depuis une baseline approuvée
    Étant donné un objectif singulier et un projet open source à une révision figée
    Et une politique d’agents et de permissions versionnée
    Quand l’opérateur demande un backlog audité et sa traçabilité
    Alors le produit exécute les étapes requises dans l’ordre de leurs dépendances
    Et chaque sortie indique sa source et son type d’information

  Scénario: Source sans révision
    Étant donné une source canonique dont la révision n’est pas déterminée
    Quand l’opérateur prépare le run
    Alors la source est inscrite dans le registre d’ambiguïtés
    Et le run probant reste Bloqué

  Scénario: Agent d’audit indisponible
    Étant donné un plan où la spécification dépend de l’audit
    Quand l’agent d’audit échoue ou dépasse son délai
    Alors la spécification dépendante n’est pas présentée comme terminée
    Et l’échec est consigné sans supprimer les observations indépendantes

  Scénario: Correspondance lexicale non démontrée
    Étant donné une User Story et un fichier partageant un mot-clé
    Mais aucune exécution ni référence explicite ne démontre leur relation
    Quand la matrice est construite
    Alors le lien n’est pas marqué Vérifié

  Scénario: Revue humaine du run
    Étant donné un run complet et son dossier de preuves
    Quand un relecteur examine les critères et les sources
    Alors il accepte ou refuse chaque promotion de statut
    Et sa décision, sa date et ses réserves sont enregistrées
```

| Scénario | User Story | Critères | Oracle indépendant |
|---|---|---|---|
| Backlog approuvé | `US-REQ-AI-001/02/03` | `CA-REQ-AI-01/02/03/04/06/07/10` | Manifestes, baseline et schémas approuvés avant le run |
| Source sans révision | `US-REQ-AI-001` | `CA-REQ-AI-02` | Registre des baselines |
| Agent indisponible | `US-REQ-AI-002` | `CA-REQ-AI-05` | Graphe de dépendances et erreur contrôlée |
| Lien lexical | `US-REQ-AI-004` | `CA-REQ-AI-08/09` | Absence de référence ou test indépendant |
| Revue humaine | `US-REQ-AI-005` | `CA-REQ-AI-11/12` | Identité et décision du relecteur |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-REQ-AI-001` | `US-REQ-AI-001` | `RM-REQ-AI-001` | `CA-REQ-AI-01/02` | Dossier de cadrage | `Candidat` |
| `EPIC-REQ-AI-001` | `US-REQ-AI-002` | `RM-REQ-AI-002` | `CA-REQ-AI-03/04/05` | Plan et journal d’orchestration | `Candidat` |
| `EPIC-REQ-AI-001` | `US-REQ-AI-003` | `RM-REQ-AI-003` | `CA-REQ-AI-06/07` | Backlog et registre d’ambiguïtés | `Candidat` |
| `EPIC-REQ-AI-001` | `US-REQ-AI-004` | `RM-REQ-AI-004` | `CA-REQ-AI-08/09` | Matrice de traçabilité | `Candidat` |
| `EPIC-REQ-AI-001` | `US-REQ-AI-005` | `RM-REQ-AI-005` | `CA-REQ-AI-10/11/12` | Dossier de preuves et décision | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Description | Décision attendue | Statut |
|---|---|---|---|
| `AMB-REQ-AI-001` | Le premier projet open source cible n’est pas encore sélectionné. | Attendre la décision de `PROJ-OSS-AUTO-001` et figer sa baseline. | `Ouvert` |
| `AMB-REQ-AI-002` | La technologie d’orchestration et le format du manifeste ne sont pas choisis. | Comparer les options et approuver un contrat versionné. | `Ouvert` |
| `AMB-REQ-AI-003` | Les invariants de reproductibilité d’un résultat génératif ne sont pas définis. | Fixer les éléments devant être identiques et ceux pouvant varier. | `Ouvert` |
| `AMB-REQ-AI-004` | Les délais, reprises et politiques d’échec par agent ne sont pas décidés. | Définir une politique avant les tests de timeout et d’interruption. | `Ouvert` |
| `AMB-REQ-AI-005` | La mesure de gain par rapport à une démarche manuelle ou mono-agent n’est pas définie. | Choisir un protocole comparatif avant de revendiquer un bénéfice. | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsqu’un lot complet est exécuté sur une baseline open source approuvée, qu’il produit un backlog et une matrice auditables, qu’un tiers reproduit les invariants définis, et qu’un relecteur humain accepte ou refuse explicitement chaque promotion de statut.
