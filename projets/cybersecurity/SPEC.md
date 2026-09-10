# SPEC — Projet Cybersecurity

## 1. Informations générales

- **Identifiant projet :** `PROJ-CYBER-001`
- **Nom :** Cybersecurity
- **Équipe :** À définir
- **Responsable(s) :** À définir
- **Branche :** `feat_getReq`
- **Statut :** `Draft`
- **Mission source :» Collecte et analyse des normes de cybersécurité »
- **Dernière mise à jour :** `2026-09-10`

## 2. Vision et Epic

### `EPIC-CYBER-001` — Constituer un corpus de normes de cybersécurité applicables aux systèmes automobiles

- **Vision :** fournir un corpus de normes de cybersécurité structuré et traçable, spécifiquement adapté au contexte automobile, en se basant sur les normes internationales reconnues.
- **Bénéficiaire principal :** ingénieur cybersécurité automobile et responsable sécurité.
- **Valeur attendue :** disposer d'exigences de cybersécurité claires, sourcées et applicables aux systèmes automobiles pour guider le développement et la certification.
- **Indicateur de succès :** un tiers peut retrouver chaque exigence dans sa norme source, comprendre son applicabilité automobile et l'utiliser pour la conception de systèmes sécurisés.
- **Hypothèse à valider :** les normes générales de cybersécurité (ISO 27001) peuvent être efficacement adaptées au contexte automobile spécifique (ISO 21434).

> En tant qu'ingénieur cybersécurité automobile, je veux accéder à un corpus structuré d'exigences issues de normes reconnues afin de concevoir des systèmes automobiles conformes aux exigences de sécurité.

## 3. Périmètre

### Inclus

- Extraction des exigences depuis ISO/IEC 27001:2022 (Information security management systems)
- Extraction des exigences depuis ISO/SAE 21434:2021 (Road vehicles Cybersecurity engineering)
- Adaptation des exigences générales au contexte automobile spécifique
- Structuration des exigences avec identifiants officiels, catégories et références source
- Qualification des exigences selon leur statut de vérification (Verified/Candidate)

### Exclus

- Invention d'exigences non présentes dans les normes sources
- Interprétation juridique ou certification de conformité
- Analyse des normes de sécurité fonctionnelle (IEC 61508, ISO 26262) - couvertes par d'autres projets
- Création de nouvelles normes ou standards

## 4. Parties prenantes et décisions humaines réservées

|| Partie prenante | Responsabilité | Décision réservée |
||---|---|---|
|| Ingénieur cybersécurité | Appliquer les exigences aux projets automobiles | Valider l'adaptation automobile des exigences générales |
|| Responsable sécurité | Approuver le corpus de normes | Sélectionner les normes applicables et leur niveau de détail |
|| Expert automobile | Valider la pertinence automobile | Confirmer l'applicabilité des exigences au contexte automobile |
|| Chef de projet | Intégrer les exigences dans le développement | Prioriser les exigences selon le projet |

## 5. Entrées et baselines

|| Entrée | Source canonique | Révision / date | Accès | Statut |
||---|---|---|---|---|
|| ISO/IEC 27001:2022 | https://www.iso.org/standard/81275.html | 2022 | Lecture (licence requise pour accès complet) | `Observé` |
|| ISO/SAE 21434:2021 | https://www.iso.org/standard/70918.html | 2021 (E) | Lecture (licence requise pour accès complet) | `Observé` |
|| Méthodologie extraction | `projets/normes/` (branche feat/GetNormes) | Version actuelle | Lecture | `Observé` |

## 6. Sorties et preuves attendues

|| Sortie | Type d’information | Oracle indépendant |
||---|---|---|
|| Fichiers d'exigences structurés | `Observation` | Comparaison avec les documents sources officiels |
|| Adaptations automobiles | `Proposition` puis `Preuve vérifiée` après revue expert | Validation par expert automobile |
|| Registre des sources | `Observation` | Références aux clauses et sections officielles |
|| Matrice de traçabilité | `Proposition` | Liens entre exigences générales et applications automobiles |

## 7. User Stories

### `US-CYBER-001` — Extraire les exigences d'ISO/IEC 27001

> En tant qu'ingénieur cybersécurité, je veux extraire et structurer les exigences d'ISO/IEC 27001:2022 afin de disposer d'une base de gestion de sécurité de l'information applicable aux systèmes automobiles.

- `RM-CYBER-001` — Chaque exigence extraite porte l'identifiant officiel de la norme (clause, sous-clause).
- **Nominal :** Une exigence d'ISO 27001 est extraite avec son identifiant officiel, sa catégorie et sa description.
- **Frontière :** Une exigence de l'annexe A est extraite mais marquée comme applicable selon contexte.
- **Contre-exemple :** Une exigence sans identifiant officiel clair n'est pas extraite ou marquée comme non vérifiée.
- **Critères associés :** `CA-CYBER-01`, `CA-CYBER-02`.

### `US-CYBER-002` — Extraire les exigences d'ISO/SAE 21434

> En tant qu'ingénieur cybersécurité automobile, je veux extraire et structurer les exigences d'ISO/SAE 21434:2021 afin de disposer des exigences spécifiques à l'ingénierie cybersécurité automobile.

- `RM-CYBER-002` — Chaque exigence extraite porte l'identifiant officiel de la norme (clause, RQ-XX-XX).
- **Nominal :** Une exigence d'ISO 21434 est extraite avec son identifiant officiel, sa catégorie et sa description.
- **Frontière :** Une exigence organisationnelle est extraite mais marquée comme applicable au niveau organisation.
- **Contre-exemple :** Une exigence sans contexte d'application clair n'est pas extraite ou marquée comme non vérifiée.
- **Critères associés :** `CA-CYBER-01`, `CA-CYBER-03`.

### `US-CYBER-003` — Adapter les exigences au contexte automobile

> En tant qu'expert automobile, je veux adapter les exigences générales de cybersécurité au contexte spécifique des systèmes automobiles afin de les rendre directement applicables.

- `RM-CYBER-003` — Une adaptation automobile est marquée comme "Candidate" jusqu'à validation par un expert.
- **Nominal :** Une exigence générale d'ISO 27001 est adaptée avec une spécification automobile (ex: ECU, OTA, véhicule connecté).
- **Frontière :** Une exigence générale sans adaptation automobile pertinente reste inchangée.
- **Contre-exemple :** Une adaptation automobile sans justification claire reste non validée.
- **Critères associés :** `CA-CYBER-04`, `CA-CYBER-05`.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-CYBER-01` — Chaque exigence possède un identifiant officiel unique et une référence source précise.
- [ ] `CA-CYBER-02` — Les exigences d'ISO 27001 sont extraites et structurées selon le schéma défini.
- [ ] `CA-CYBER-03` — Les exigences d'ISO 21434 sont extraites et structurées selon le schéma défini.
- [ ] `CA-CYBER-04` — Les adaptations automobiles sont clairement identifiées et justifiées.
- [ ] `CA-CYBER-05` — Le statut de vérification (Verified/Candidate) est explicitement indiqué pour chaque exigence.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Extraction des exigences de cybersécurité

  Scénario: Exigence extraite avec identifiant officiel
    Étant donné une norme de cybersécurité officielle
    Quand l'extraction identifie une exigence avec son identifiant officiel
    Alors l'exigence est structurée avec catégorie, description et référence source
    Et le statut Verified est attribué si le passage source est retrouvable

  Scénario: Adaptation automobile proposée
    Étant donné une exigence générale de cybersécurité
    Quand une adaptation au contexte automobile est proposée
    Alors l'adaptation est marquée comme Candidate
    Et elle nécessite une validation par un expert automobile

  Scénario: Absence d'identifiant officiel
    Étant donné une exigence potentielle sans identifiant officiel clair
    Quand l'extraction ne peut pas retrouver l'identifiant dans la source
    Alors l'exigence n'est pas extraite ou marquée comme Non vérifié
```

|| Scénario | User Story | Critère | Oracle indépendant |
||---|---|---|---|
|| Exigence extraite | `US-CYBER-001` / `US-CYBER-002` | `CA-CYBER-01/02/03` | Document source officiel de la norme |
|| Adaptation automobile | `US-CYBER-003` | `CA-CYBER-04/05` | Validation par expert automobile |

## 10. Traçabilité Epic → Stories → preuves

|| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
||---|---|---|---|---|---|
|| `EPIC-CYBER-001` | `US-CYBER-001` | `RM-CYBER-001` | `CA-CYBER-01/02` | `exigences/iso-27001-exigences.md` | `Candidat` |
|| `EPIC-CYBER-001` | `US-CYBER-002` | `RM-CYBER-002` | `CA-CYBER-01/03` | `exigences/iso-sae-21434-exigences.md` | `Candidat` |
|| `EPIC-CYBER-001` | `US-CYBER-003` | `RM-CYBER-003` | `CA-CYBER-04/05` | Adaptations automobiles dans les fichiers | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

|| ID | Type | Description | Décision attendue | Responsable | Statut |
||---|---|---|---|---|---|
|| `AMB-CYBER-001` | Ambiguïté | L'accès complet aux documents ISO nécessite des licences payantes | Obtenir les licences appropriées ou utiliser les versions publiques disponibles | Responsable sécurité | `Ouvert` |
|| `AMB-CYBER-002` | Risque | Les adaptations automobiles candidates nécessitent une validation expert | Planifier des revues avec des experts automobiles disponibles | Chef de projet | `Ouvert` |
|| `AMB-CYBER-003` | Dépendance | La méthodologie d'extraction basée sur le projet normes peut évoluer | Suivre les évolutions de la méthodologie du projet normes | Équipe | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsque les exigences d'ISO 27001 et ISO 21434 sont extraites et structurées, que les adaptations automobiles candidates sont identifiées, et qu'un expert automobile a validé la pertinence des adaptations proposées.
