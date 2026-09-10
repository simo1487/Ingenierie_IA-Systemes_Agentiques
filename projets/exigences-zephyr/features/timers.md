# Feature — Timers

## 1. Informations générales

- **Identifiant :** `FEAT-TIMERS`
- **Nom de la feature :** `Timers`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Timers** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Timers de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Timers** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-4-1 | The Zephyr RTOS shall provide a mechanism to define and statically (i.e. compile time) initialize timers. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-1) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-2 | When initializing a timer, the Zephyr RTOS shall support setting a function that gets called when the timer expires. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-2) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-3 | When initializing a timer, the Zephyr RTOS shall support setting a function that gets called when a running timer is stopped. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-3) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-4 | The Zephyr RTOS shall provide a mechanism to define and initialize timers at run time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-4) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-5 | The Zephyr RTOS shall provide a mechanism to start a timer for a specific duration and periodicity. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-5) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-6 | The Zephyr RTOS shall provide a mechanism to stop a running timer. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-6) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-7 | The Zephyr RTOS shall provide a mechanism to read the number of times a timer has expired and then reset this count to zero. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-7) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-8 | When a timer is initialized, started, or read via the timer status or synchronization mechanism, the Zephyr RTOS shall reset the timer's expiration count to zero. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-8) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-9 | The Zephyr RTOS shall provide a mechanism to synchronize a thread to a timer and then block the thread's execution until any of the following conditions is satisfied: - The timer is stopped - The timer's expiration count is greater than zero | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-9) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-10 | The Zephyr RTOS shall provide a mechanism to get a timer's next expiration time in system ticks. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-10) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-11 | The Zephyr RTOS shall provide a mechanism to get a timer's remaining time until its next expiry in system ticks. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-11) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-12 | The Zephyr RTOS shall provide a mechanism to get the timer's remaining time until its next expiry in milliseconds. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-12) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-13 | The Zephyr RTOS shall support adding user defined data to a timer. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-13) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-14 | The Zephyr RTOS shall support retrieving user defined data from a timer. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-14) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-15 | When a timer expiry function is called, the Zephyr RTOS shall do so in the interrupt context. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-15) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-16 | The Zephyr RTOS shall provide a mechanism to release the resources associated with a timer. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-16) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-17 | If a timer is cleaned up while one or more threads are still waiting on it, then the Zephyr RTOS shall leave the timer's resources unreleased and return an error indicating that the cleanup could not be performed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-17) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-4-18 | Where timer observers are enabled, the Zephyr RTOS shall provide a mechanism to register observers that are notified of the following timer lifecycle events: initialization, start, stop, and expiry. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-18) | Timers | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-4-1` : l'UID ZEP-SRS-4-1 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-1).
- [ ] `CA-ZEP-SRS-4-2` : l'UID ZEP-SRS-4-2 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-2).
- [ ] `CA-ZEP-SRS-4-3` : l'UID ZEP-SRS-4-3 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-3).
- [ ] `CA-ZEP-SRS-4-4` : l'UID ZEP-SRS-4-4 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-4).
- [ ] `CA-ZEP-SRS-4-5` : l'UID ZEP-SRS-4-5 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-5).
- [ ] `CA-ZEP-SRS-4-6` : l'UID ZEP-SRS-4-6 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-6).
- [ ] `CA-ZEP-SRS-4-7` : l'UID ZEP-SRS-4-7 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-7).
- [ ] `CA-ZEP-SRS-4-8` : l'UID ZEP-SRS-4-8 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-8).
- [ ] `CA-ZEP-SRS-4-9` : l'UID ZEP-SRS-4-9 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-9).
- [ ] `CA-ZEP-SRS-4-10` : l'UID ZEP-SRS-4-10 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-10).
- [ ] `CA-ZEP-SRS-4-11` : l'UID ZEP-SRS-4-11 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-11).
- [ ] `CA-ZEP-SRS-4-12` : l'UID ZEP-SRS-4-12 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-12).
- [ ] `CA-ZEP-SRS-4-13` : l'UID ZEP-SRS-4-13 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-13).
- [ ] `CA-ZEP-SRS-4-14` : l'UID ZEP-SRS-4-14 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-14).
- [ ] `CA-ZEP-SRS-4-15` : l'UID ZEP-SRS-4-15 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-15).
- [ ] `CA-ZEP-SRS-4-16` : l'UID ZEP-SRS-4-16 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-16).
- [ ] `CA-ZEP-SRS-4-17` : l'UID ZEP-SRS-4-17 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-17).
- [ ] `CA-ZEP-SRS-4-18` : l'UID ZEP-SRS-4-18 est retrouvable dans docs/software_requirements/timers.sdoc (UID ZEP-SRS-4-18).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Timers

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
