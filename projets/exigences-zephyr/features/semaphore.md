# Feature — Semaphore

## 1. Informations générales

- **Identifiant :** `FEAT-SEMAPHORE`
- **Nom de la feature :** `Semaphore`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Semaphore** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Semaphore de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Semaphore** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-5-1 | The Zephyr RTOS shall provide a mechanism to define and initialize a semaphore at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-1) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-2 | The Zephyr RTOS shall provide a mechanism to define and initialize a semaphore at runtime. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-2) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-3 | The Zephyr RTOS shall define the maximum limit of a semaphore when the semaphore is used for counting purposes and does not have an explicit limit. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-3) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-4 | When initializing a counting semaphore, the maximum permitted count a semaphore can have shall be set. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-4) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-5 | When initializing a counting semaphore, the initial semaphore value shall be set. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-5) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-6 | The Zephyr RTOS shall provide a mechanism allowing threads to acquire a semaphore. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-6) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-7 | While the semaphore's count is greater than zero, the requesting thread shall acquire the semaphore and decrement its count. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-7) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-8 | While the semaphore's count is zero, the requesting thread shall be blocked until the semaphore is released by another thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-8) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-9 | When attempting to acquire a semaphore, the Zephyr RTOS shall accept options that specify timeout periods, allowing threads to set a maximum wait time for semaphore acquisition. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-9) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-10 | When attempting to acquire a semaphore, where the semaphore is not acquired within the specified time, the Zephyr RTOS shall return an error indicating a timeout. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-10) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-11 | When attempting to acquire a semaphore, where the current count is zero and no timeout time was provided, the Zephyr RTOS shall return an error indicating the semaphore is busy. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-11) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-12 | The Zephyr RTOS shall provide a mechanism allowing threads to release a semaphore. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-12) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-13 | The Zephyr RTOS shall increment the semaphore's count upon release. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-13) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-14 | When there are threads waiting on the semaphore, the highest-priority waiting thread shall be unblocked and acquire the semaphore. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-14) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-15 | The Zephyr RTOS shall provide a mechanism for threads to check the current count of a semaphore without acquiring it. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-15) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-16 | The Zephyr RTOS shall provide a mechanism that resets the semaphore count to zero. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-16) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-17 | When a semaphore is reset, the Zephyr RTOS shall abort all pending take operations on the semaphore, returning to the affected threads the same error used to indicate a wait timeout. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-17) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-18 | When initializing a counting semaphore, where the maximum permitted count of a semaphore is invalid, then the Zephyr RTOS shall return an error indicating invalid values. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-18) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-19 | When a semaphore is released while its count is already at the maximum permitted count, the Zephyr RTOS shall leave the count unchanged. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-19) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-5-20 | The Zephyr RTOS shall allow a semaphore to be released from an interrupt service routine, and to be acquired from an interrupt service routine when no waiting is requested. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-20) | Semaphores | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-5-1` : l'UID ZEP-SRS-5-1 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-1).
- [ ] `CA-ZEP-SRS-5-2` : l'UID ZEP-SRS-5-2 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-2).
- [ ] `CA-ZEP-SRS-5-3` : l'UID ZEP-SRS-5-3 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-3).
- [ ] `CA-ZEP-SRS-5-4` : l'UID ZEP-SRS-5-4 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-4).
- [ ] `CA-ZEP-SRS-5-5` : l'UID ZEP-SRS-5-5 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-5).
- [ ] `CA-ZEP-SRS-5-6` : l'UID ZEP-SRS-5-6 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-6).
- [ ] `CA-ZEP-SRS-5-7` : l'UID ZEP-SRS-5-7 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-7).
- [ ] `CA-ZEP-SRS-5-8` : l'UID ZEP-SRS-5-8 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-8).
- [ ] `CA-ZEP-SRS-5-9` : l'UID ZEP-SRS-5-9 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-9).
- [ ] `CA-ZEP-SRS-5-10` : l'UID ZEP-SRS-5-10 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-10).
- [ ] `CA-ZEP-SRS-5-11` : l'UID ZEP-SRS-5-11 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-11).
- [ ] `CA-ZEP-SRS-5-12` : l'UID ZEP-SRS-5-12 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-12).
- [ ] `CA-ZEP-SRS-5-13` : l'UID ZEP-SRS-5-13 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-13).
- [ ] `CA-ZEP-SRS-5-14` : l'UID ZEP-SRS-5-14 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-14).
- [ ] `CA-ZEP-SRS-5-15` : l'UID ZEP-SRS-5-15 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-15).
- [ ] `CA-ZEP-SRS-5-16` : l'UID ZEP-SRS-5-16 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-16).
- [ ] `CA-ZEP-SRS-5-17` : l'UID ZEP-SRS-5-17 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-17).
- [ ] `CA-ZEP-SRS-5-18` : l'UID ZEP-SRS-5-18 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-18).
- [ ] `CA-ZEP-SRS-5-19` : l'UID ZEP-SRS-5-19 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-19).
- [ ] `CA-ZEP-SRS-5-20` : l'UID ZEP-SRS-5-20 est retrouvable dans docs/software_requirements/semaphore.sdoc (UID ZEP-SRS-5-20).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Semaphore

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
