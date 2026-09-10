# Feature — Queues

## 1. Informations générales

- **Identifiant :** `FEAT-QUEUES`
- **Nom de la feature :** `Queues`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Queues** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Queues de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Queues** dans `zephyrproject-rtos/reqmgmt`.
- Extraction des identifiants, textes, catégories et relations explicitement disponibles.
- Conservation de la révision et du chemin source.
- Proposition séparée de correspondances automobiles (statut Candidat).

### Exclus

- Création d'une exigence absente des sources.
- Attribution automatique d'une conformité à une norme automobile.
- Confusion entre documentation d'API, comportement observé et exigence normative.

## 5. Schéma minimal

| Champ | Attendu |
|---|---|
| `requirement_id` | Identifiant original, sans renumérotation silencieuse |
| `requirement_text` | Texte source ou reformulation signalée |
| `source_repository` | Dépôt officiel ou source justifiée |
| `source_revision` | Tag ou SHA exact |
| `source_path` | Fichier et section ou ligne |
| `category` | Catégorie documentée |
| `implementation_links` | Liens observés vers le code |
| `test_links` | Liens observés vers les tests |
| `automotive_mapping` | Proposition séparée et justifiée |
| `status` | Observé, candidat, vérifié, non vérifié ou bloqué |

## 6. Exigences couvertes

| requirement_id | requirement_text | source_repository | source_revision | source_path | category | implementation_links | test_links | automotive_mapping | status |
|---|---|---|---|---|---|---|---|---|---|
| ZEP-SRS-20-1 | The Zephyr RTOS shall provide a mechanism to define and initialize a queue at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-1) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-2 | The Zephyr RTOS shall provide a mechanism to define and initialize a queue at run time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-2) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-3 | The Zephyr RTOS shall provide a mechanism to enqueue a data item to the back of a queue (i.e. append). | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-3) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-4 | The Zephyr RTOS shall provide a mechanism to enqueue a data item to the front of a queue (i.e. prepend). | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-4) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-5 | The Zephyr RTOS shall provide a mechanism to remove a specific data item from a queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-5) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-6 | The Zephyr RTOS shall provide a mechanism to get and dequeue a data item from the front of a queue, within a timeout. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-6) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-7 | The Zephyr RTOS shall provide a mechanism to check if a queue is empty. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-7) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-8 | The Zephyr RTOS shall provide a mechanism to peek at the data item at the back of a queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-8) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-9 | The Zephyr RTOS shall provide a mechanism to peek at the data item at the front of a queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-9) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-10 | The Zephyr RTOS shall provide a mechanism to insert a data item behind another specific data item in a queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-10) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-11 | The Zephyr RTOS shall provide a mechanism to append a list of data items to the back of a queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-11) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-12 | The Zephyr RTOS shall provide a mechanism to append a list of data items to the back of a queue and then empty the list. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-12) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-13 | The Zephyr RTOS shall provide a mechanism to append a data item uniquely to the queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-13) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-20-14 | The Zephyr RTOS shall provide a dedicated mechanism to implicite allocate memory from a thread when appending data items to a queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-14) | Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-20-1` : l'UID ZEP-SRS-20-1 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-1).
- [ ] `CA-ZEP-SRS-20-2` : l'UID ZEP-SRS-20-2 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-2).
- [ ] `CA-ZEP-SRS-20-3` : l'UID ZEP-SRS-20-3 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-3).
- [ ] `CA-ZEP-SRS-20-4` : l'UID ZEP-SRS-20-4 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-4).
- [ ] `CA-ZEP-SRS-20-5` : l'UID ZEP-SRS-20-5 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-5).
- [ ] `CA-ZEP-SRS-20-6` : l'UID ZEP-SRS-20-6 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-6).
- [ ] `CA-ZEP-SRS-20-7` : l'UID ZEP-SRS-20-7 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-7).
- [ ] `CA-ZEP-SRS-20-8` : l'UID ZEP-SRS-20-8 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-8).
- [ ] `CA-ZEP-SRS-20-9` : l'UID ZEP-SRS-20-9 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-9).
- [ ] `CA-ZEP-SRS-20-10` : l'UID ZEP-SRS-20-10 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-10).
- [ ] `CA-ZEP-SRS-20-11` : l'UID ZEP-SRS-20-11 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-11).
- [ ] `CA-ZEP-SRS-20-12` : l'UID ZEP-SRS-20-12 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-12).
- [ ] `CA-ZEP-SRS-20-13` : l'UID ZEP-SRS-20-13 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-13).
- [ ] `CA-ZEP-SRS-20-14` : l'UID ZEP-SRS-20-14 est retrouvable dans docs/software_requirements/queues.sdoc (UID ZEP-SRS-20-14).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Queues

  Scénario: Exigence retrouvée
    Étant donné une exigence associée à un dépôt, une révision et un chemin
    Quand un relecteur ouvre la source indiquée
    Alors il retrouve le passage correspondant
    Et peut confirmer ou refuser le statut Vérifié

  Scénario: Lien code ou test manquant
    Étant donné une exigence sans lien observable vers le code ou les tests
    Quand la recherche ne trouve pas de correspondance
    Alors le champ reste Non déterminé
    Et l'exigence n'est pas utilisée comme preuve de traçabilité

  Scénario: Correspondance automobile proposée
    Étant donné une exigence Zephyr observée
    Quand un agent propose un lien vers ISO 26262
    Alors ce lien est enregistré séparément avec le statut Candidat
    Et nécessite une revue humaine spécialisée
```

## 10. Définition de terminé

Le travail est terminé lorsqu'un tiers peut retrouver les exigences ci-dessus dans la révision indiquée, distinguer les liens observés des hypothèses et reproduire l'extraction sans dépendre du contexte conversationnel de l'agent.
