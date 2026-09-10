# Feature — Threads

## 1. Informations générales

- **Identifiant :** `FEAT-THREADS`
- **Nom de la feature :** `Threads`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Threads** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Threads de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Threads** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-1-1 | The Zephyr RTOS shall provide an interface to create (start) a thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-1) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-2 | The Zephyr RTOS shall provide an interface to set a thread's priority. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-2) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-3 | The Zephyr RTOS shall provide an interface to suspend a thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-3) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-4 | The Zephyr RTOS shall provide an interface to resume a suspended thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-4) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-5 | The Zephyr RTOS shall provide an interface to resume a suspended thread after a timeout. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-5) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-6 | The Zephyr RTOS shall provide an interface to delete (end) a thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-6) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-7 | Threads shall have different states to fulfill the Life-cycle of a thread | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-7) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-8 | Every Thread shall have it's own stack. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-8) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-9 | The Zephyr RTOS shall provide an interface to create threads with defined privilege. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-9) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-10 | The Zephyr RTOS shall provide an interface to schedule multiple threads. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-10) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-11 | The Zephyr RTOS shall support a set of thread options. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-11) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |
| ZEP-SRS-1-12 | Every thread shall have a custom data area. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-12) | Threads | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Cycle de vie des entités logicielles | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-1-1` : l'UID ZEP-SRS-1-1 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-1).
- [ ] `CA-ZEP-SRS-1-2` : l'UID ZEP-SRS-1-2 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-2).
- [ ] `CA-ZEP-SRS-1-3` : l'UID ZEP-SRS-1-3 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-3).
- [ ] `CA-ZEP-SRS-1-4` : l'UID ZEP-SRS-1-4 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-4).
- [ ] `CA-ZEP-SRS-1-5` : l'UID ZEP-SRS-1-5 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-5).
- [ ] `CA-ZEP-SRS-1-6` : l'UID ZEP-SRS-1-6 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-6).
- [ ] `CA-ZEP-SRS-1-7` : l'UID ZEP-SRS-1-7 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-7).
- [ ] `CA-ZEP-SRS-1-8` : l'UID ZEP-SRS-1-8 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-8).
- [ ] `CA-ZEP-SRS-1-9` : l'UID ZEP-SRS-1-9 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-9).
- [ ] `CA-ZEP-SRS-1-10` : l'UID ZEP-SRS-1-10 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-10).
- [ ] `CA-ZEP-SRS-1-11` : l'UID ZEP-SRS-1-11 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-11).
- [ ] `CA-ZEP-SRS-1-12` : l'UID ZEP-SRS-1-12 est retrouvable dans docs/software_requirements/threads.sdoc (UID ZEP-SRS-1-12).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Threads

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
