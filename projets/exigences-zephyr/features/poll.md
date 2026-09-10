# Feature — Poll

## 1. Informations générales

- **Identifiant :** `FEAT-POLL`
- **Nom de la feature :** `Poll`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Poll** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Poll de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Poll** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-33-1 | The Zephyr RTOS shall provide a mechanism for a thread to wait until any one of a specified set of poll events is ready. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-1) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-2 | The Zephyr RTOS shall support poll events that wait for the availability of a semaphore, a FIFO, a message queue, a pipe, and a poll signal. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-2) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-11 | The Zephyr RTOS shall provide mechanisms to initialize a poll event at compile time or at run time, associating the event with a condition type, an operating mode, and the object to be monitored. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-11) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-3 | When a thread waits on a set of poll events, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for an event to become ready. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-3) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-4 | When a poll wait completes, the Zephyr RTOS shall report the state of each poll event so the caller can determine which events are ready. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-4) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-5 | The Zephyr RTOS shall provide a poll signal object type that threads can wait on as a poll event. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-5) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-6 | The Zephyr RTOS shall provide a mechanism to initialize a poll signal object to the unsignaled state. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-6) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-7 | The Zephyr RTOS shall provide a mechanism to raise a poll signal with a caller-supplied result value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-7) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-8 | While a poll signal is in the signaled state, the Zephyr RTOS shall report poll events waiting on that signal as ready, including waits that begin after the signal was raised. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-8) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-9 | The Zephyr RTOS shall provide a mechanism to reset a poll signal to the unsignaled state. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-9) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-33-10 | The Zephyr RTOS shall provide a mechanism to fetch the signaled state and result value of a poll signal. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-10) | Polling | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-33-1` : l'UID ZEP-SRS-33-1 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-1).
- [ ] `CA-ZEP-SRS-33-2` : l'UID ZEP-SRS-33-2 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-2).
- [ ] `CA-ZEP-SRS-33-11` : l'UID ZEP-SRS-33-11 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-11).
- [ ] `CA-ZEP-SRS-33-3` : l'UID ZEP-SRS-33-3 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-3).
- [ ] `CA-ZEP-SRS-33-4` : l'UID ZEP-SRS-33-4 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-4).
- [ ] `CA-ZEP-SRS-33-5` : l'UID ZEP-SRS-33-5 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-5).
- [ ] `CA-ZEP-SRS-33-6` : l'UID ZEP-SRS-33-6 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-6).
- [ ] `CA-ZEP-SRS-33-7` : l'UID ZEP-SRS-33-7 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-7).
- [ ] `CA-ZEP-SRS-33-8` : l'UID ZEP-SRS-33-8 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-8).
- [ ] `CA-ZEP-SRS-33-9` : l'UID ZEP-SRS-33-9 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-9).
- [ ] `CA-ZEP-SRS-33-10` : l'UID ZEP-SRS-33-10 est retrouvable dans docs/software_requirements/poll.sdoc (UID ZEP-SRS-33-10).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Poll

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
