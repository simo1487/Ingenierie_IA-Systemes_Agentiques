# Feature — Memory Objects

## 1. Informations générales

- **Identifiant :** `FEAT-MEMORY-OBJECTS`
- **Nom de la feature :** `Memory Objects`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Memory Objects** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Memory Objects de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Memory Objects** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-9-1 | The Zephyr RTOS shall allow threads to dynamically allocate variable-sized memory regions from a specified range of memory. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-1) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-2 | The Zephyr RTOS shall allow threads to dynamically allocate fixed-sized memory regions from a specified range of memory. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-2) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-3 | The Zephyr RTOS shall provide a mechanism to define and initialize a memory heap at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-3) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-4 | The Zephyr RTOS shall provide a mechanism to initialize a memory heap at run time over a caller-provided memory region. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-4) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-5 | The Zephyr RTOS shall provide a mechanism to allocate a block of memory of a requested size from a heap. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-5) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-6 | The Zephyr RTOS shall provide a mechanism to allocate a block of memory from a heap with a requested alignment. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-6) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-7 | When allocating memory from a heap, the Zephyr RTOS shall accept a timeout that specifies the maximum time to wait for sufficient memory to become available. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-7) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-8 | When sufficient memory cannot be allocated from a heap within the specified time, the Zephyr RTOS shall report that the allocation failed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-8) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-9 | The Zephyr RTOS shall provide a mechanism to resize a previously allocated heap block while preserving its contents up to the smaller of the old and new sizes. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-9) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-10 | The Zephyr RTOS shall provide a mechanism to release a previously allocated block of memory back to its heap. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-10) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-11 | The Zephyr RTOS shall provide a mechanism to allocate memory from and release memory to a shared system heap. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-11) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-12 | The Zephyr RTOS shall provide a mechanism to define and initialize a memory slab of fixed-size blocks at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-12) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-13 | The Zephyr RTOS shall provide a mechanism to initialize a memory slab at run time over a caller-provided memory region. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-13) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-14 | The Zephyr RTOS shall provide a mechanism to allocate a fixed-size block from a memory slab, accepting a timeout that specifies the maximum time to wait for a free block. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-14) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-15 | When no block becomes available in a memory slab within the specified time, the Zephyr RTOS shall return an error indicating that no block was allocated. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-15) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-16 | The Zephyr RTOS shall provide a mechanism to release a previously allocated block back to its memory slab. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-16) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-17 | The Zephyr RTOS shall provide a mechanism to query the number of used and free blocks in a memory slab. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-17) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |
| ZEP-SRS-9-18 | The Zephyr RTOS shall provide a mechanism to obtain the set of heaps that were defined at compile time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-18) | Memory Objects | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Allocation mémoire | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-9-1` : l'UID ZEP-SRS-9-1 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-1).
- [ ] `CA-ZEP-SRS-9-2` : l'UID ZEP-SRS-9-2 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-2).
- [ ] `CA-ZEP-SRS-9-3` : l'UID ZEP-SRS-9-3 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-3).
- [ ] `CA-ZEP-SRS-9-4` : l'UID ZEP-SRS-9-4 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-4).
- [ ] `CA-ZEP-SRS-9-5` : l'UID ZEP-SRS-9-5 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-5).
- [ ] `CA-ZEP-SRS-9-6` : l'UID ZEP-SRS-9-6 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-6).
- [ ] `CA-ZEP-SRS-9-7` : l'UID ZEP-SRS-9-7 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-7).
- [ ] `CA-ZEP-SRS-9-8` : l'UID ZEP-SRS-9-8 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-8).
- [ ] `CA-ZEP-SRS-9-9` : l'UID ZEP-SRS-9-9 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-9).
- [ ] `CA-ZEP-SRS-9-10` : l'UID ZEP-SRS-9-10 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-10).
- [ ] `CA-ZEP-SRS-9-11` : l'UID ZEP-SRS-9-11 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-11).
- [ ] `CA-ZEP-SRS-9-12` : l'UID ZEP-SRS-9-12 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-12).
- [ ] `CA-ZEP-SRS-9-13` : l'UID ZEP-SRS-9-13 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-13).
- [ ] `CA-ZEP-SRS-9-14` : l'UID ZEP-SRS-9-14 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-14).
- [ ] `CA-ZEP-SRS-9-15` : l'UID ZEP-SRS-9-15 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-15).
- [ ] `CA-ZEP-SRS-9-16` : l'UID ZEP-SRS-9-16 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-16).
- [ ] `CA-ZEP-SRS-9-17` : l'UID ZEP-SRS-9-17 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-17).
- [ ] `CA-ZEP-SRS-9-18` : l'UID ZEP-SRS-9-18 est retrouvable dans docs/software_requirements/memory_objects.sdoc (UID ZEP-SRS-9-18).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Memory Objects

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
