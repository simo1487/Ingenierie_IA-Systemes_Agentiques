# Feature — Atomic Service

## 1. Informations générales

- **Identifiant :** `FEAT-ATOMIC-SERVICE`
- **Nom de la feature :** `Atomic Service`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Atomic Service** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Atomic Service de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Atomic Service** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-26-1 | The Zephyr RTOS shall define an atomic variable type whose size matches the native word size of the target architecture: 32 bits on 32-bit architectures and 64 bits on 64-bit architectures. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-1) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-2 | The Zephyr RTOS shall define a signed integer type, whose size is determined by the target processor architecture, used as the parameter and return type of operations on atomic variables. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-2) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-3 | The Zephyr RTOS shall guarantee that each operation on an atomic variable is free from torn reads or writes. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-3) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-4 | The Zephyr RTOS shall guarantee that the result of each operation on an atomic variable is visible to all processors in the system. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-4) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-5 | The Zephyr RTOS shall provide a mechanism for performing all operations on an atomic variable in an indivisible manner. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-5) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-6 | When performing an operation on an atomic variable, the Zephyr RTOS shall provide full memory barrier semantics, such that memory operations issued before the atomic operation are observed before it and memory operations issued after it are observed after it. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-6) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-7 | The Zephyr RTOS shall support executing atomic operations on hardware that does not provide native atomic instruction support. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-7) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-8 | Where the target hardware provides native atomic instructions, the Zephyr RTOS shall support implementing atomic operations using those instructions. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-8) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-9 | The Zephyr RTOS shall provide a compile-time mechanism for computing the minimum number of atomic variables necessary to represent a bit array of a given number of bits. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-9) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-10 | The Zephyr RTOS shall provide a compile-time mechanism for defining an array of atomic variables with the minimum size necessary to represent a bit array of a given number of bits. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-10) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-11 | The Zephyr RTOS shall provide a compile-time mechanism for initializing an atomic variable. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-11) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-12 | The Zephyr RTOS shall provide a mechanism for setting an atomic variable and returning its previous value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-12) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-13 | The Zephyr RTOS shall provide a mechanism for getting the value from an atomic variable. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-13) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-14 | When performing a bitwise operation on an atomic variable, the Zephyr RTOS shall store the result in the atomic variable and return its previous value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-14) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-15 | The Zephyr RTOS shall provide a mechanism for performing a bitwise AND operation on an atomic variable with a given value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-15) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-16 | The Zephyr RTOS shall provide a mechanism for performing a bitwise OR operation on an atomic variable with a given value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-16) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-17 | The Zephyr RTOS shall provide a mechanism for performing a bitwise NAND operation on an atomic variable with a given value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-17) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-18 | The Zephyr RTOS shall provide a mechanism for performing a bitwise XOR operation on an atomic variable with a given value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-18) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-19 | The Zephyr RTOS shall provide a mechanism for adding a value to an atomic variable and returning its previous value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-19) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-20 | The Zephyr RTOS shall provide a mechanism for incrementing an atomic variable by 1 and returning its previous value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-20) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-21 | The Zephyr RTOS shall provide a mechanism for subtracting a value from an atomic variable and returning its previous value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-21) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-22 | The Zephyr RTOS shall provide a mechanism for decrementing an atomic variable by 1 and returning its previous value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-22) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-23 | The Zephyr RTOS shall provide a mechanism for setting an atomic variable to a new value if and only if its current value equals an expected value, leaving the atomic variable unchanged otherwise, and returning whether the atomic variable was updated. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-23) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-24 | The Zephyr RTOS shall provide a mechanism for setting an atomic variable to zero and returning its previous value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-24) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-25 | The Zephyr RTOS shall support performing bit-level operations on individual bits within either a single atomic variable or an array of atomic variables. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-25) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-26 | The Zephyr RTOS shall provide a mechanism for setting a specific bit within an atomic variable or an array of atomic variables to 1. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-26) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-27 | The Zephyr RTOS shall provide a mechanism for clearing a specific bit within an atomic variable or an array of atomic variables to 0. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-27) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-28 | The Zephyr RTOS shall provide a mechanism for setting a specific bit within an atomic variable or an array of atomic variables to a given boolean value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-28) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-29 | The Zephyr RTOS shall provide a mechanism for getting the state of a specific bit within an atomic variable or an array of atomic variables, returning its current state as a boolean value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-29) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-30 | The Zephyr RTOS shall provide a mechanism for setting a specific bit within an atomic variable or an array of atomic variables to 1 and returning its previous state. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-30) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-31 | The Zephyr RTOS shall provide a mechanism for clearing a specific bit within an atomic variable or an array of atomic variables to 0 and returning its previous state. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-31) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-32 | The Zephyr RTOS shall define an atomic variable type for storing a pointer value atomically. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-32) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-33 | The Zephyr RTOS shall define a pointer type used as the parameter and return type of all atomic pointer operations. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-33) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-34 | The Zephyr RTOS shall provide a compile-time mechanism for initializing an atomic pointer to a specific pointer value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-34) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-35 | The Zephyr RTOS shall provide operations that read and write atomic pointers using the atomic pointer value type. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-35) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-36 | The Zephyr RTOS shall provide a mechanism for getting the pointer value from an atomic pointer. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-36) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-37 | The Zephyr RTOS shall provide a mechanism for setting an atomic pointer and returning its previous pointer value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-37) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-38 | The Zephyr RTOS shall provide a mechanism for setting an atomic pointer to a new value if and only if its current value equals an expected value, leaving the atomic pointer unchanged otherwise, and returning whether the atomic pointer was updated. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-38) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-39 | The Zephyr RTOS shall provide a mechanism for setting an atomic pointer to NULL and returning its previous pointer value. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-39) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |
| ZEP-SRS-26-40 | The Zephyr RTOS shall support performing atomic operations from threads and from interrupt service routines, guaranteeing correct results when multiple contexts operate concurrently on the same atomic variable. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-40) | Atomic Service | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Opérations indivisibles | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-26-1` : l'UID ZEP-SRS-26-1 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-1).
- [ ] `CA-ZEP-SRS-26-2` : l'UID ZEP-SRS-26-2 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-2).
- [ ] `CA-ZEP-SRS-26-3` : l'UID ZEP-SRS-26-3 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-3).
- [ ] `CA-ZEP-SRS-26-4` : l'UID ZEP-SRS-26-4 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-4).
- [ ] `CA-ZEP-SRS-26-5` : l'UID ZEP-SRS-26-5 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-5).
- [ ] `CA-ZEP-SRS-26-6` : l'UID ZEP-SRS-26-6 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-6).
- [ ] `CA-ZEP-SRS-26-7` : l'UID ZEP-SRS-26-7 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-7).
- [ ] `CA-ZEP-SRS-26-8` : l'UID ZEP-SRS-26-8 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-8).
- [ ] `CA-ZEP-SRS-26-9` : l'UID ZEP-SRS-26-9 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-9).
- [ ] `CA-ZEP-SRS-26-10` : l'UID ZEP-SRS-26-10 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-10).
- [ ] `CA-ZEP-SRS-26-11` : l'UID ZEP-SRS-26-11 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-11).
- [ ] `CA-ZEP-SRS-26-12` : l'UID ZEP-SRS-26-12 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-12).
- [ ] `CA-ZEP-SRS-26-13` : l'UID ZEP-SRS-26-13 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-13).
- [ ] `CA-ZEP-SRS-26-14` : l'UID ZEP-SRS-26-14 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-14).
- [ ] `CA-ZEP-SRS-26-15` : l'UID ZEP-SRS-26-15 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-15).
- [ ] `CA-ZEP-SRS-26-16` : l'UID ZEP-SRS-26-16 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-16).
- [ ] `CA-ZEP-SRS-26-17` : l'UID ZEP-SRS-26-17 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-17).
- [ ] `CA-ZEP-SRS-26-18` : l'UID ZEP-SRS-26-18 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-18).
- [ ] `CA-ZEP-SRS-26-19` : l'UID ZEP-SRS-26-19 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-19).
- [ ] `CA-ZEP-SRS-26-20` : l'UID ZEP-SRS-26-20 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-20).
- [ ] `CA-ZEP-SRS-26-21` : l'UID ZEP-SRS-26-21 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-21).
- [ ] `CA-ZEP-SRS-26-22` : l'UID ZEP-SRS-26-22 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-22).
- [ ] `CA-ZEP-SRS-26-23` : l'UID ZEP-SRS-26-23 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-23).
- [ ] `CA-ZEP-SRS-26-24` : l'UID ZEP-SRS-26-24 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-24).
- [ ] `CA-ZEP-SRS-26-25` : l'UID ZEP-SRS-26-25 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-25).
- [ ] `CA-ZEP-SRS-26-26` : l'UID ZEP-SRS-26-26 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-26).
- [ ] `CA-ZEP-SRS-26-27` : l'UID ZEP-SRS-26-27 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-27).
- [ ] `CA-ZEP-SRS-26-28` : l'UID ZEP-SRS-26-28 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-28).
- [ ] `CA-ZEP-SRS-26-29` : l'UID ZEP-SRS-26-29 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-29).
- [ ] `CA-ZEP-SRS-26-30` : l'UID ZEP-SRS-26-30 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-30).
- [ ] `CA-ZEP-SRS-26-31` : l'UID ZEP-SRS-26-31 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-31).
- [ ] `CA-ZEP-SRS-26-32` : l'UID ZEP-SRS-26-32 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-32).
- [ ] `CA-ZEP-SRS-26-33` : l'UID ZEP-SRS-26-33 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-33).
- [ ] `CA-ZEP-SRS-26-34` : l'UID ZEP-SRS-26-34 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-34).
- [ ] `CA-ZEP-SRS-26-35` : l'UID ZEP-SRS-26-35 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-35).
- [ ] `CA-ZEP-SRS-26-36` : l'UID ZEP-SRS-26-36 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-36).
- [ ] `CA-ZEP-SRS-26-37` : l'UID ZEP-SRS-26-37 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-37).
- [ ] `CA-ZEP-SRS-26-38` : l'UID ZEP-SRS-26-38 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-38).
- [ ] `CA-ZEP-SRS-26-39` : l'UID ZEP-SRS-26-39 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-39).
- [ ] `CA-ZEP-SRS-26-40` : l'UID ZEP-SRS-26-40 est retrouvable dans docs/software_requirements/atomic_service.sdoc (UID ZEP-SRS-26-40).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Atomic Service

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
