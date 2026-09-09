# Feature — Pipe

## 1. Informations générales

- **Identifiant :** `FEAT-PIPE`
- **Nom de la feature :** `Pipe`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Pipe** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Pipe de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Pipe** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-32-1 | The Zephyr RTOS shall provide a mechanism to define and initialize a pipe at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-1) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-2 | The Zephyr RTOS shall provide a mechanism to initialize a pipe at run time using a caller-provided buffer. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-2) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-3 | The Zephyr RTOS shall provide a mechanism for a thread to write up to a requested number of bytes into a pipe. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-3) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-4 | The Zephyr RTOS shall provide a mechanism for a thread to read up to a requested number of bytes from a pipe. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-4) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-5 | When writing to a pipe, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for space to become available. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-5) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-11 | When writing to a pipe, if no data can be written within the specified maximum time, the Zephyr RTOS shall return an error indicating that no data was written. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-11) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-6 | When reading from a pipe, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for data to become available. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-6) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-12 | When reading from a pipe, if no data becomes available within the specified maximum time, the Zephyr RTOS shall return an error indicating that no data was read. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-12) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-7 | The Zephyr RTOS shall provide a mechanism to reset a pipe, discarding any unread data and unblocking threads waiting on the pipe. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-7) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-8 | The Zephyr RTOS shall provide a mechanism to close a pipe, unblocking threads waiting on the pipe. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-8) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-9 | When a read or write operation is attempted on a closed pipe, the Zephyr RTOS shall return an error indicating that the pipe is closed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-9) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |
| ZEP-SRS-32-10 | When a read or write operation is interrupted by a pipe reset, the Zephyr RTOS shall return an error indicating that the operation was cancelled. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-10) | Pipes | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Passage de données | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-32-1` : l'UID ZEP-SRS-32-1 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-1).
- [ ] `CA-ZEP-SRS-32-2` : l'UID ZEP-SRS-32-2 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-2).
- [ ] `CA-ZEP-SRS-32-3` : l'UID ZEP-SRS-32-3 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-3).
- [ ] `CA-ZEP-SRS-32-4` : l'UID ZEP-SRS-32-4 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-4).
- [ ] `CA-ZEP-SRS-32-5` : l'UID ZEP-SRS-32-5 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-5).
- [ ] `CA-ZEP-SRS-32-11` : l'UID ZEP-SRS-32-11 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-11).
- [ ] `CA-ZEP-SRS-32-6` : l'UID ZEP-SRS-32-6 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-6).
- [ ] `CA-ZEP-SRS-32-12` : l'UID ZEP-SRS-32-12 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-12).
- [ ] `CA-ZEP-SRS-32-7` : l'UID ZEP-SRS-32-7 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-7).
- [ ] `CA-ZEP-SRS-32-8` : l'UID ZEP-SRS-32-8 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-8).
- [ ] `CA-ZEP-SRS-32-9` : l'UID ZEP-SRS-32-9 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-9).
- [ ] `CA-ZEP-SRS-32-10` : l'UID ZEP-SRS-32-10 est retrouvable dans docs/software_requirements/pipe.sdoc (UID ZEP-SRS-32-10).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Pipe

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
