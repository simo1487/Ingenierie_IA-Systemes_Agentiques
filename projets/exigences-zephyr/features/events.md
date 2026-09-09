# Feature — Events

## 1. Informations générales

- **Identifiant :** `FEAT-EVENTS`
- **Nom de la feature :** `Events`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Events** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Events de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Events** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-27-1 | The Zephyr RTOS shall provide a mechanism to define and initialize an event object at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-1) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-2 | The Zephyr RTOS shall provide a mechanism to initialize an event object at run time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-2) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-3 | The Zephyr RTOS shall provide an event object capable of tracking up to 32 distinct events. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-3) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-4 | The Zephyr RTOS shall provide a mechanism to post one or more events to an event object, merging them with the events currently tracked by the event object. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-4) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-5 | The Zephyr RTOS shall provide a mechanism to set the events tracked by an event object to a specified value, replacing the events currently tracked by the event object. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-5) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-6 | The Zephyr RTOS shall provide a mechanism to set the events selected by a mask to specified values, leaving the events tracked by the event object that are not selected by the mask unchanged. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-6) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-7 | The Zephyr RTOS shall provide a mechanism to clear specified events tracked by an event object. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-7) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-8 | When the events tracked by an event object are modified, the Zephyr RTOS shall report the value that the modified events had before the operation. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-8) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-9 | When a modification of the events tracked by an event object satisfies the waiting condition of a thread waiting on that event object, the Zephyr RTOS shall unpend that thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-9) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-10 | The Zephyr RTOS shall provide a mechanism for a thread to wait until any of a specified set of events is tracked by an event object. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-10) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-11 | The Zephyr RTOS shall provide a mechanism for a thread to wait until all of a specified set of events are tracked by an event object. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-11) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-12 | When a thread waits on an event object, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for the desired set of events. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-12) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-13 | When the timeout of a thread waiting on an event object elapses before the desired set of events is satisfied, the Zephyr RTOS shall report that no matching events were delivered. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-13) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-14 | When a thread waiting on an event object completes its wait successfully, the Zephyr RTOS shall report the set of events that matched the waiting condition. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-14) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |
| ZEP-SRS-27-15 | When a thread waits on an event object, the Zephyr RTOS shall accept an option to clear the events tracked by the event object before the wait begins. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/events.sdoc (UID ZEP-SRS-27-15) | Events | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Synchronisation | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-27-1` : l'UID ZEP-SRS-27-1 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-1).
- [ ] `CA-ZEP-SRS-27-2` : l'UID ZEP-SRS-27-2 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-2).
- [ ] `CA-ZEP-SRS-27-3` : l'UID ZEP-SRS-27-3 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-3).
- [ ] `CA-ZEP-SRS-27-4` : l'UID ZEP-SRS-27-4 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-4).
- [ ] `CA-ZEP-SRS-27-5` : l'UID ZEP-SRS-27-5 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-5).
- [ ] `CA-ZEP-SRS-27-6` : l'UID ZEP-SRS-27-6 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-6).
- [ ] `CA-ZEP-SRS-27-7` : l'UID ZEP-SRS-27-7 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-7).
- [ ] `CA-ZEP-SRS-27-8` : l'UID ZEP-SRS-27-8 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-8).
- [ ] `CA-ZEP-SRS-27-9` : l'UID ZEP-SRS-27-9 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-9).
- [ ] `CA-ZEP-SRS-27-10` : l'UID ZEP-SRS-27-10 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-10).
- [ ] `CA-ZEP-SRS-27-11` : l'UID ZEP-SRS-27-11 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-11).
- [ ] `CA-ZEP-SRS-27-12` : l'UID ZEP-SRS-27-12 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-12).
- [ ] `CA-ZEP-SRS-27-13` : l'UID ZEP-SRS-27-13 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-13).
- [ ] `CA-ZEP-SRS-27-14` : l'UID ZEP-SRS-27-14 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-14).
- [ ] `CA-ZEP-SRS-27-15` : l'UID ZEP-SRS-27-15 est retrouvable dans docs/software_requirements/events.sdoc (UID ZEP-SRS-27-15).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Events

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
