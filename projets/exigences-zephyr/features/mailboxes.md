# Feature — Mailboxes

## 1. Informations générales

- **Identifiant :** `FEAT-MAILBOXES`
- **Nom de la feature :** `Mailboxes`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Mailboxes** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Mailboxes de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Mailboxes** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-25-1 | The Zephyr RTOS shall provide a mechanism to define and initialize a mailbox at run time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-1) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-2 | The Zephyr RTOS shall provide a mechanism to statically define and initialize a mailbox object at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-2) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-3 | The Zephyr RTOS shall support messages containing zero or more bytes of data. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-3) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-4 | The Zephyr RTOS shall handle the data transfer between mailbox objects of the sending and receiving threads. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-4) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-5 | The Zephyr RTOS shall provide a mechanism for a thread to send a message through a mailbox and block until the message is processed or a timeout occurs. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-5) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-6 | If the synchronous message send operation times out before a receiver processes the message, the Zephyr RTOS shall return an timeout error code to the sending thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-6) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-7 | The Zephyr RTOS shall provide a mechanism for a thread to send a message through a mailbox without waiting for it to be processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-7) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-8 | When a sending thread asynchronously sends a message to a mailbox object, the Zephyr RTOS shall provide a mechanism to signal to the sending thread that the message has been both received and completely processed by the receiver. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-8) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-9 | The Zephyr RTOS shall provide a mechanism for a thread to receive a message via a mailbox object with a timeout parameter. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-9) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-10 | The Zephyr RTOS shall provide a mechanism for a thread to retrieve message data via a mailbox object. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-10) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-11 | When a receiving thread requests a message via a mailbox object and no message is available, the Zephyr RTOS shall block the receiving thread until a message is available or the timeout expires. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-11) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-12 | If the message receive operation times out before a message becomes available, the Zephyr RTOS shall return an appropriate timeout error code to the receiving thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-12) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-13 | The Zephyr RTOS shall handle message exchange via a mailbox object non-anonymously, allowing both the sending and receiving threads to know the identity of the other thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-13) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-14 | When multiple threads are waiting on an empty mailbox object, the Zephyr RTOS shall deliver the next message to the highest priority thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-14) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-15 | When multiple threads of equal priority are waiting on an empty mailbox object, the Zephyr RTOS shall deliver the next message to the thread that has waited the longest. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-15) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-16 | The Zephyr RTOS shall support an arbitrary number of mailbox objects, limited only by available RAM in the system. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-16) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-25-17 | The Zephyr RTOS shall handle invalid parameters by returning error codes rather than causing system failures. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-17) | Mailboxes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-25-1` : l'UID ZEP-SRS-25-1 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-1).
- [ ] `CA-ZEP-SRS-25-2` : l'UID ZEP-SRS-25-2 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-2).
- [ ] `CA-ZEP-SRS-25-3` : l'UID ZEP-SRS-25-3 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-3).
- [ ] `CA-ZEP-SRS-25-4` : l'UID ZEP-SRS-25-4 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-4).
- [ ] `CA-ZEP-SRS-25-5` : l'UID ZEP-SRS-25-5 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-5).
- [ ] `CA-ZEP-SRS-25-6` : l'UID ZEP-SRS-25-6 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-6).
- [ ] `CA-ZEP-SRS-25-7` : l'UID ZEP-SRS-25-7 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-7).
- [ ] `CA-ZEP-SRS-25-8` : l'UID ZEP-SRS-25-8 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-8).
- [ ] `CA-ZEP-SRS-25-9` : l'UID ZEP-SRS-25-9 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-9).
- [ ] `CA-ZEP-SRS-25-10` : l'UID ZEP-SRS-25-10 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-10).
- [ ] `CA-ZEP-SRS-25-11` : l'UID ZEP-SRS-25-11 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-11).
- [ ] `CA-ZEP-SRS-25-12` : l'UID ZEP-SRS-25-12 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-12).
- [ ] `CA-ZEP-SRS-25-13` : l'UID ZEP-SRS-25-13 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-13).
- [ ] `CA-ZEP-SRS-25-14` : l'UID ZEP-SRS-25-14 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-14).
- [ ] `CA-ZEP-SRS-25-15` : l'UID ZEP-SRS-25-15 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-15).
- [ ] `CA-ZEP-SRS-25-16` : l'UID ZEP-SRS-25-16 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-16).
- [ ] `CA-ZEP-SRS-25-17` : l'UID ZEP-SRS-25-17 est retrouvable dans docs/software_requirements/mailboxes.sdoc (UID ZEP-SRS-25-17).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Mailboxes

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
