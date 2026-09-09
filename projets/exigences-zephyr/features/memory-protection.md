# Feature — Memory Protection

## 1. Informations générales

- **Identifiant :** `FEAT-MEMORY-PROTECTION`
- **Nom de la feature :** `Memory Protection`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Memory Protection** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Memory Protection de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Memory Protection** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-8-1 | The Zephyr RTOS shall support memory protection features to isolate a thread's memory region. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-1) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-2 | The Zephyr RTOS shall provide a mechanism to grant user threads access to kernel objects. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-2) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-3 | The Zephyr RTOS shall be able to differentiate between user threads and kernel threads for memory access. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-3) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-4 | The Zephyr RTOS shall have a defined behaviour when an invocation of an unimplemented system call is made. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-4) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-5 | The Zephyr RTOS shall have a defined behaviour when an invalid system call ID is used. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-5) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-6 | The Zephyr RTOS shall prevent user threads from creating new threads that are higher priority than the caller. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-6) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-7 | The Zephyr RTOS shall support revoking permission to a kernel object. User mode threads may only revoke their own access to an object. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-7) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-8 | The Zephyr RTOS shall prevent user threads from creating kernel threads. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-8) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-9 | The Zephyr RTOS shall allow the creation of threads that run in reduced privilege level. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-9) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-10 | The Zephyr RTOS shall provide system calls to allow user mode threads to perform privileged operations. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-10) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-11 | The Zephyr RTOS shall support a defined mechanism for user mode handling a of detected stack overflow. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-11) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-12 | The Zephyr RTOS shall support detection of stack overflows. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-12) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-13 | The Zephyr RTOS shall support configurable access to memory during boot time. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-13) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-14 | The Zephyr RTOS shall provide helper functions for system call handler functions to validate the inputs passed in from user mode before invoking the implementation function to protect the kernel. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-14) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-15 | The Zephyr RTOS shall support system calls to be able to safely accept C strings passed in from user mode. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-15) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-16 | The Zephyr RTOS shall track kernel objects that are used by user mode threads. Note: this means Zephyr shall track the resources used by the user mode thread (associate this with a user story). | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-16) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-17 | The Zephyr RTOS shall have an interface to request access to specific memory after initial allocation. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-17) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |
| ZEP-SRS-8-18 | The Zephyr RTOS shall support assigning a memory pool to act as that thread's resource pool. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-18) | Memory protection | Non déterminé | Non déterminé | ISO 26262 Partie 6 / ISO/SAE 21434 — Isolation mémoire | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-8-1` : l'UID ZEP-SRS-8-1 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-1).
- [ ] `CA-ZEP-SRS-8-2` : l'UID ZEP-SRS-8-2 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-2).
- [ ] `CA-ZEP-SRS-8-3` : l'UID ZEP-SRS-8-3 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-3).
- [ ] `CA-ZEP-SRS-8-4` : l'UID ZEP-SRS-8-4 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-4).
- [ ] `CA-ZEP-SRS-8-5` : l'UID ZEP-SRS-8-5 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-5).
- [ ] `CA-ZEP-SRS-8-6` : l'UID ZEP-SRS-8-6 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-6).
- [ ] `CA-ZEP-SRS-8-7` : l'UID ZEP-SRS-8-7 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-7).
- [ ] `CA-ZEP-SRS-8-8` : l'UID ZEP-SRS-8-8 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-8).
- [ ] `CA-ZEP-SRS-8-9` : l'UID ZEP-SRS-8-9 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-9).
- [ ] `CA-ZEP-SRS-8-10` : l'UID ZEP-SRS-8-10 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-10).
- [ ] `CA-ZEP-SRS-8-11` : l'UID ZEP-SRS-8-11 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-11).
- [ ] `CA-ZEP-SRS-8-12` : l'UID ZEP-SRS-8-12 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-12).
- [ ] `CA-ZEP-SRS-8-13` : l'UID ZEP-SRS-8-13 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-13).
- [ ] `CA-ZEP-SRS-8-14` : l'UID ZEP-SRS-8-14 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-14).
- [ ] `CA-ZEP-SRS-8-15` : l'UID ZEP-SRS-8-15 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-15).
- [ ] `CA-ZEP-SRS-8-16` : l'UID ZEP-SRS-8-16 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-16).
- [ ] `CA-ZEP-SRS-8-17` : l'UID ZEP-SRS-8-17 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-17).
- [ ] `CA-ZEP-SRS-8-18` : l'UID ZEP-SRS-8-18 est retrouvable dans docs/software_requirements/memory_protection.sdoc (UID ZEP-SRS-8-18).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Memory Protection

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
