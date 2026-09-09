# Feature — Interrupts

## 1. Informations générales

- **Identifiant :** `FEAT-INTERRUPTS`
- **Nom de la feature :** `Interrupts`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Interrupts** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Interrupts de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Interrupts** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-7-1 | Zephyr RTOS shall provide a mechanism to initialize a static IRQ service routine (ISR), providing all parameters needed to configure the hardware and software. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-1) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-2 | The static IRQ shall be initially disabled. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-2) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-3 | Zephyr RTOS shall provide a mechanism to initialize a direct IRQ handler, providing all parameters needed to configure the hardware and software. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-3) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-4 | The direct IRQ shall be initially disabled. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-4) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-5 | Zephyr RTOS shall provide a mechanism to initialize a dynamic IRQ service routine, providing all parameters needed to configure the hardware and software. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-5) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-6 | The dynamic IRQ shall be initially disabled. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-6) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-7 | Zephyr RTOS shall provide a mechanism to uninstall a dynamic ISR. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-7) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-8 | Zephyr RTOS shall provide a mechanism to disable all IRQs on a CPU and return the state of the IRQ hardware prior to being disabled. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-8) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-9 | Zephyr RTOS shall provide a mechanism to enable all IRQs on a CPU and return them to their previous state. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-9) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-10 | Zephyr RTOS shall provide a mechanism to disable a specified IRQ. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-10) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-11 | Zephyr RTOS shall provide a mechanism to enable a specified IRQ. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-11) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-12 | Zephyr RTOS shall provide a mechanism that returns the enabled status of a specified IRQ, where the status is enabled or disabled. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-12) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-13 | Zephyr RTOS shall provide a mechanism that returns the execution context, where the context is In-ISR or Not In-ISR. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-13) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-14 | The Zephyr RTOS shall support multi-level preemptive interrupt priorities, when supported by hardware. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-14) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-15 | When an enabled IRQ that has a connected interrupt service routine is asserted, the Zephyr RTOS shall invoke the associated interrupt service routine. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-15) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |
| ZEP-SRS-7-16 | When the Zephyr RTOS invokes a static or dynamic interrupt service routine, it shall pass to the routine the parameter that was registered with it. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-16) | Interrupts | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Interruptions / latence | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-7-1` : l'UID ZEP-SRS-7-1 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-1).
- [ ] `CA-ZEP-SRS-7-2` : l'UID ZEP-SRS-7-2 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-2).
- [ ] `CA-ZEP-SRS-7-3` : l'UID ZEP-SRS-7-3 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-3).
- [ ] `CA-ZEP-SRS-7-4` : l'UID ZEP-SRS-7-4 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-4).
- [ ] `CA-ZEP-SRS-7-5` : l'UID ZEP-SRS-7-5 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-5).
- [ ] `CA-ZEP-SRS-7-6` : l'UID ZEP-SRS-7-6 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-6).
- [ ] `CA-ZEP-SRS-7-7` : l'UID ZEP-SRS-7-7 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-7).
- [ ] `CA-ZEP-SRS-7-8` : l'UID ZEP-SRS-7-8 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-8).
- [ ] `CA-ZEP-SRS-7-9` : l'UID ZEP-SRS-7-9 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-9).
- [ ] `CA-ZEP-SRS-7-10` : l'UID ZEP-SRS-7-10 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-10).
- [ ] `CA-ZEP-SRS-7-11` : l'UID ZEP-SRS-7-11 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-11).
- [ ] `CA-ZEP-SRS-7-12` : l'UID ZEP-SRS-7-12 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-12).
- [ ] `CA-ZEP-SRS-7-13` : l'UID ZEP-SRS-7-13 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-13).
- [ ] `CA-ZEP-SRS-7-14` : l'UID ZEP-SRS-7-14 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-14).
- [ ] `CA-ZEP-SRS-7-15` : l'UID ZEP-SRS-7-15 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-15).
- [ ] `CA-ZEP-SRS-7-16` : l'UID ZEP-SRS-7-16 est retrouvable dans docs/software_requirements/interrupts.sdoc (UID ZEP-SRS-7-16).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Interrupts

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
