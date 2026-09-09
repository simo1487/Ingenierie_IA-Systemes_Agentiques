# Feature — Mutex

## 1. Informations générales

- **Identifiant :** `FEAT-MUTEX`
- **Nom de la feature :** `Mutex`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Mutex** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Mutex de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Mutex** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-6-1 | The Zephyr RTOS shall provide a mutex that allows threads to obtain mutually exclusive access to a shared resource. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-1) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-2 | The Zephyr RTOS shall provide a mechanism to define and initialize a mutex at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-2) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-3 | The Zephyr RTOS shall provide a mechanism to initialize a mutex at run time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-3) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-4 | The Zephyr RTOS shall provide a mechanism for a thread to lock a mutex and become its owner. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-4) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-5 | While a mutex is not owned by any thread, a thread that locks it shall acquire ownership of the mutex. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-5) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-6 | While a mutex is owned by another thread, a thread that attempts to lock it shall be blocked until the mutex becomes available or the specified timeout elapses. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-6) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-7 | When locking a mutex, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for the mutex to become available. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-7) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-8 | When a mutex does not become available within the specified time, the Zephyr RTOS shall return an error indicating that the mutex was not locked. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-8) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-9 | While a thread owns a mutex, the Zephyr RTOS shall allow that thread to lock the same mutex again, and shall require the thread to unlock it the same number of times before it is released. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-9) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-10 | The Zephyr RTOS shall provide a mechanism for the owning thread to unlock a mutex. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-10) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-11 | If a thread that does not own a mutex attempts to unlock it, then the Zephyr RTOS shall return an error and shall not release the mutex. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-11) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |
| ZEP-SRS-6-12 | While a higher-priority thread is blocked waiting on a mutex, the Zephyr RTOS shall raise the priority of the owning thread to that of the highest-priority waiting thread until the mutex is released. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-12) | Mutex | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Exclusion mutuelle | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-6-1` : l'UID ZEP-SRS-6-1 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-1).
- [ ] `CA-ZEP-SRS-6-2` : l'UID ZEP-SRS-6-2 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-2).
- [ ] `CA-ZEP-SRS-6-3` : l'UID ZEP-SRS-6-3 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-3).
- [ ] `CA-ZEP-SRS-6-4` : l'UID ZEP-SRS-6-4 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-4).
- [ ] `CA-ZEP-SRS-6-5` : l'UID ZEP-SRS-6-5 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-5).
- [ ] `CA-ZEP-SRS-6-6` : l'UID ZEP-SRS-6-6 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-6).
- [ ] `CA-ZEP-SRS-6-7` : l'UID ZEP-SRS-6-7 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-7).
- [ ] `CA-ZEP-SRS-6-8` : l'UID ZEP-SRS-6-8 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-8).
- [ ] `CA-ZEP-SRS-6-9` : l'UID ZEP-SRS-6-9 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-9).
- [ ] `CA-ZEP-SRS-6-10` : l'UID ZEP-SRS-6-10 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-10).
- [ ] `CA-ZEP-SRS-6-11` : l'UID ZEP-SRS-6-11 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-11).
- [ ] `CA-ZEP-SRS-6-12` : l'UID ZEP-SRS-6-12 est retrouvable dans docs/software_requirements/mutex.sdoc (UID ZEP-SRS-6-12).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Mutex

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
