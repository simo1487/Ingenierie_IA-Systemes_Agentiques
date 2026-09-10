# Feature — Message Queue

## 1. Informations générales

- **Identifiant :** `FEAT-MESSAGE-QUEUE`
- **Nom de la feature :** `Message Queue`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Message Queue** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Message Queue de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Message Queue** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-31-1 | The Zephyr RTOS shall provide a mechanism to define and initialize a message queue at compile time, for a specified message size, maximum number of messages, and buffer alignment. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-1) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-2 | The Zephyr RTOS shall provide a mechanism to initialize a message queue at run time using a caller-provided buffer, a message size, and a maximum number of messages. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-2) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-3 | The Zephyr RTOS shall provide a mechanism to initialize a message queue at run time, allocating the message buffer on behalf of the caller for a requested message size and maximum number of messages. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-3) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-4 | The Zephyr RTOS shall provide a mechanism for threads and interrupt service routines to send a message to the back of a message queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-4) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-5 | The Zephyr RTOS shall provide a mechanism for threads and interrupt service routines to send a message to the front of a message queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-5) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-6 | When sending a message to a message queue, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for space to become available. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-6) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-7 | When sending a message to a message queue, the Zephyr RTOS shall return an error indicating that the message was not sent when either of the following conditions is satisfied: - the caller is a thread and space does not become available in the message queue within the specified maximum time - the caller is an interrupt service routine and no space is available in the message queue | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-7) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-8 | The Zephyr RTOS shall provide a mechanism for threads and interrupt service routines to receive and remove the message at the front of a message queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-8) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-9 | The Zephyr RTOS shall return messages from a message queue to receivers in front-to-back order: messages sent to the back are received in the order in which they were sent, and a message sent to the front is received before the messages already in the queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-9) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-10 | When receiving a message from a message queue, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for a message to become available. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-10) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-11 | When receiving a message from a message queue, the Zephyr RTOS shall return an error indicating that no message was received when either of the following conditions is satisfied: - the caller is a thread and no message becomes available in the message queue within the specified maximum time - the caller is an interrupt service routine and no message is available in the message queue | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-11) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-12 | The Zephyr RTOS shall provide a mechanism for threads and interrupt service routines to read the message at the front of a message queue without removing it. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-12) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-13 | The Zephyr RTOS shall provide a mechanism for threads and interrupt service routines to read a message at a specified index of a message queue without removing it. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-13) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-14 | The Zephyr RTOS shall provide a mechanism to discard all messages currently in a message queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-14) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-19 | When a message queue is purged, the Zephyr RTOS shall unblock any threads waiting to send a message to that queue and return an error to them indicating that the message was not sent. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-19) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-15 | The Zephyr RTOS shall provide a mechanism to query the number of messages currently in a message queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-15) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-16 | The Zephyr RTOS shall provide a mechanism to query the number of free message slots in a message queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-16) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-21 | The Zephyr RTOS shall provide a mechanism to query the attributes of a message queue, including its message size, its maximum number of messages, and the number of messages currently stored. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-21) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-17 | The Zephyr RTOS shall provide a mechanism to release the buffer of a message queue that was dynamically allocated. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-17) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-31-20 | When releasing the buffer of a message queue, if threads are waiting on the message queue, then the Zephyr RTOS shall not release the buffer and shall return an error indicating that the message queue is in use. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-20) | Message Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-31-1` : l'UID ZEP-SRS-31-1 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-1).
- [ ] `CA-ZEP-SRS-31-2` : l'UID ZEP-SRS-31-2 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-2).
- [ ] `CA-ZEP-SRS-31-3` : l'UID ZEP-SRS-31-3 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-3).
- [ ] `CA-ZEP-SRS-31-4` : l'UID ZEP-SRS-31-4 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-4).
- [ ] `CA-ZEP-SRS-31-5` : l'UID ZEP-SRS-31-5 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-5).
- [ ] `CA-ZEP-SRS-31-6` : l'UID ZEP-SRS-31-6 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-6).
- [ ] `CA-ZEP-SRS-31-7` : l'UID ZEP-SRS-31-7 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-7).
- [ ] `CA-ZEP-SRS-31-8` : l'UID ZEP-SRS-31-8 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-8).
- [ ] `CA-ZEP-SRS-31-9` : l'UID ZEP-SRS-31-9 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-9).
- [ ] `CA-ZEP-SRS-31-10` : l'UID ZEP-SRS-31-10 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-10).
- [ ] `CA-ZEP-SRS-31-11` : l'UID ZEP-SRS-31-11 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-11).
- [ ] `CA-ZEP-SRS-31-12` : l'UID ZEP-SRS-31-12 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-12).
- [ ] `CA-ZEP-SRS-31-13` : l'UID ZEP-SRS-31-13 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-13).
- [ ] `CA-ZEP-SRS-31-14` : l'UID ZEP-SRS-31-14 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-14).
- [ ] `CA-ZEP-SRS-31-19` : l'UID ZEP-SRS-31-19 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-19).
- [ ] `CA-ZEP-SRS-31-15` : l'UID ZEP-SRS-31-15 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-15).
- [ ] `CA-ZEP-SRS-31-16` : l'UID ZEP-SRS-31-16 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-16).
- [ ] `CA-ZEP-SRS-31-21` : l'UID ZEP-SRS-31-21 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-21).
- [ ] `CA-ZEP-SRS-31-17` : l'UID ZEP-SRS-31-17 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-17).
- [ ] `CA-ZEP-SRS-31-20` : l'UID ZEP-SRS-31-20 est retrouvable dans docs/software_requirements/message_queue.sdoc (UID ZEP-SRS-31-20).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Message Queue

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
