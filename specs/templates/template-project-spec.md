# Modèle de spécification de projet

Ce modèle décrit un projet complet sous la forme d’une Epic déclinée en User Stories. Une User Story exprime une valeur observable ; une feature (`FEAT-*`) peut ensuite détailler son implémentation sans remplacer la Story.

## 1. Informations générales

- **Identifiant projet :** `PROJ-[DOMAINE]-[NUMÉRO]`
- **Nom :** [Nom du projet]
- **Équipe :** [Équipe]
- **Responsable(s) :** [Noms ou rôle]
- **Branche :** `[branche]`
- **Statut :** `Draft` / `Candidate` / `In Review` / `Validated`
- **Mission source :** [Référence vérifiable]
- **Dernière mise à jour :** `AAAA-MM-JJ`

## 2. Vision et Epic

### `EPIC-[DOMAINE]-001` — [Titre orienté résultat]

- **Vision :** [Résultat durable recherché]
- **Bénéficiaire principal :** [Rôle]
- **Valeur attendue :** [Gain observable ou risque évité]
- **Indicateur de succès :** [Mesure vérifiable]
- **Hypothèses :** [Propositions à valider]

> En tant que [rôle], je veux [capacité globale] afin de [valeur observable].

## 3. Périmètre

### Inclus

- [Capacité incluse]

### Exclus

- [Capacité explicitement exclue]

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Besoin ou responsabilité | Décision réservée |
|---|---|---|
| [Rôle] | [Besoin] | [Arbitrage non délégué à l’IA] |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| [Entrée] | [Chemin ou URL] | [Tag, SHA ou date] | Lecture seule / Écriture | `Observé` / `Candidat` / `Non vérifié` / `Bloqué` |

Une révision inconnue est inscrite dans le registre des ambiguïtés ; elle n’est jamais devinée.

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant | Responsable de revue |
|---|---|---|---|
| [Livrable] | `Proposition` / `Observation` / `Preuve vérifiée` / `Question ouverte` | [Contrôle externe à l’implémentation] | [Rôle] |

## 7. User Stories

### `US-[DOMAINE]-001` — [Titre]

- **Priorité :** `P1` / `P2` / `P3`
- **Statut :** `Draft` / `Candidate` / `In Review` / `Validated`
- **Dépendances :** [Identifiants ou aucune]

> En tant que [rôle], je veux [capacité] afin de [bénéfice observable].

**Règles métier**

- `RM-[DOMAINE]-001` — [Règle singulière, claire et vérifiable].

**Exemples**

- **Nominal :** [État initial → action → résultat].
- **Frontière :** [Limite → action → résultat].
- **Contre-exemple :** [Entrée ou contexte invalide → refus observable].

**Critères associés :** `CA-[DOMAINE]-01`.

Répéter cette section pour chaque User Story nécessaire à la couverture de l’Epic.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-[DOMAINE]-01` — [Condition déterministe et observable].
- [ ] `CA-[DOMAINE]-02` — [Gestion d’une limite ou d’un refus].
- [ ] `CA-[DOMAINE]-03` — [Reproductibilité par un tiers].

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: [Nom de l’Epic]

  Scénario: [Cas nominal]
    Étant donné [contexte vérifiable]
    Quand [action]
    Alors [résultat observable]

  Scénario: [Cas frontière]
    Étant donné [valeur ou état limite]
    Quand [action]
    Alors [résultat attendu]

  Scénario: [Cas de refus]
    Étant donné [entrée invalide ou ressource indisponible]
    Quand [action]
    Alors [refus, statut ou code observable]
```

| Scénario | User Story | Critère | Oracle indépendant |
|---|---|---|---|
| [Nominal] | `US-*` | `CA-*` | [Source, parseur, revue contradictoire ou résultat d’exécution indépendant] |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-*` | `US-*` | `RM-*` | `CA-*` | [Artefact] | `Observé` / `Candidat` / `Vérifié` / `Non vérifié` / `Bloqué` |

Une proximité de vocabulaire ne suffit jamais à établir une relation de traçabilité.

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Type | Description | Décision attendue | Responsable | Statut |
|---|---|---|---|---|---|
| `AMB-[DOMAINE]-001` | Ambiguïté / Risque / Dépendance | [Inconnue explicite] | [Arbitrage attendu] | [Rôle] | `Ouvert` / `Résolu` |

## 12. Définition de terminé

L’Epic est terminée lorsque toutes les User Stories `P1` sont acceptées, que leurs critères disposent d’oracles indépendants, que les preuves sont reproductibles et que les ambiguïtés bloquantes sont résolues ou explicitement acceptées par le responsable humain.
