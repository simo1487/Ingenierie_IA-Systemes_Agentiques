# Feature — Kernel Timing

## 1. Informations générales

- **Identifiant :** `FEAT-KERNEL-TIMING`
- **Nom de la feature :** `Kernel Timing`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Kernel Timing** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Kernel Timing de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Kernel Timing** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-28-1 | The Zephyr RTOS shall provide a mechanism to obtain the time elapsed since the system booted, expressed in milliseconds. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-1) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-2 | The Zephyr RTOS shall provide a mechanism to obtain the time elapsed since the system booted, expressed in system ticks. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-2) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-3 | The Zephyr RTOS shall provide a mechanism to obtain the time elapsed since the system booted, expressed in seconds. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-3) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-4 | The Zephyr RTOS shall provide a mechanism to obtain the time elapsed, in milliseconds, since a caller-provided reference time, and to replace that reference time with the current system uptime. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-4) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-5 | The Zephyr RTOS shall provide a mechanism to read the current value of the system's hardware clock as a 32-bit cycle count. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-5) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-6 | The Zephyr RTOS shall provide a mechanism to read the current value of the system's hardware clock as a 64-bit cycle count. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-6) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-7 | The Zephyr RTOS shall provide a mechanism to convert time values between milliseconds, microseconds, nanoseconds, system ticks, and hardware cycles. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-7) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-8 | The Zephyr RTOS shall provide a mechanism to suspend the execution of the calling thread for a specified duration, where the duration may be expressed in milliseconds, microseconds, nanoseconds, system ticks, or hardware cycles. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-8) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-9 | The Zephyr RTOS shall provide a mechanism to suspend the execution of the calling thread for a duration specified in microseconds. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-9) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-10 | When the duration for which a thread was suspended elapses, the Zephyr RTOS shall make the thread eligible for execution again. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-10) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-11 | The Zephyr RTOS shall provide a mechanism to prematurely wake a thread that is suspended for a duration. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-11) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-12 | When a thread suspended for a specified duration is woken before that duration has elapsed, the Zephyr RTOS shall report the amount of time that was remaining, expressed in milliseconds. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-12) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-15 | When a thread suspended for a duration specified in microseconds is woken before that duration has elapsed, the Zephyr RTOS shall report the amount of time that was remaining, expressed in microseconds. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-15) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-13 | The Zephyr RTOS shall provide a mechanism for the calling thread to busy wait for a specified number of microseconds without relinquishing the CPU. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-13) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |
| ZEP-SRS-28-14 | Where 64-bit timeouts are enabled, the Zephyr RTOS shall accept timeouts specified as an absolute point in time, in addition to timeouts specified as a relative duration. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-14) | Kernel Timing | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Services temps | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-28-1` : l'UID ZEP-SRS-28-1 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-1).
- [ ] `CA-ZEP-SRS-28-2` : l'UID ZEP-SRS-28-2 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-2).
- [ ] `CA-ZEP-SRS-28-3` : l'UID ZEP-SRS-28-3 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-3).
- [ ] `CA-ZEP-SRS-28-4` : l'UID ZEP-SRS-28-4 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-4).
- [ ] `CA-ZEP-SRS-28-5` : l'UID ZEP-SRS-28-5 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-5).
- [ ] `CA-ZEP-SRS-28-6` : l'UID ZEP-SRS-28-6 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-6).
- [ ] `CA-ZEP-SRS-28-7` : l'UID ZEP-SRS-28-7 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-7).
- [ ] `CA-ZEP-SRS-28-8` : l'UID ZEP-SRS-28-8 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-8).
- [ ] `CA-ZEP-SRS-28-9` : l'UID ZEP-SRS-28-9 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-9).
- [ ] `CA-ZEP-SRS-28-10` : l'UID ZEP-SRS-28-10 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-10).
- [ ] `CA-ZEP-SRS-28-11` : l'UID ZEP-SRS-28-11 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-11).
- [ ] `CA-ZEP-SRS-28-12` : l'UID ZEP-SRS-28-12 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-12).
- [ ] `CA-ZEP-SRS-28-15` : l'UID ZEP-SRS-28-15 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-15).
- [ ] `CA-ZEP-SRS-28-13` : l'UID ZEP-SRS-28-13 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-13).
- [ ] `CA-ZEP-SRS-28-14` : l'UID ZEP-SRS-28-14 est retrouvable dans docs/software_requirements/kernel_timing.sdoc (UID ZEP-SRS-28-14).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Kernel Timing

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
