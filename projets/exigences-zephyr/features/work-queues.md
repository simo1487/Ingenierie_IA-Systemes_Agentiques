# Feature — Work Queues

## 1. Informations générales

- **Identifiant :** `FEAT-WORK-QUEUES`
- **Nom de la feature :** `Work Queues`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **Work Queues** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences Work Queues de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **Work Queues** dans `zephyrproject-rtos/reqmgmt`.
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
| ZEP-SRS-38-1 | The Zephyr RTOS shall provide a mechanism to initialize a work queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-1) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-29 | The Zephyr RTOS shall provide a mechanism to start an initialized work queue, dedicating a thread to process its work items. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-29) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-41 | The Zephyr RTOS shall provide a mechanism to process the work items of an initialized work queue that has not been started, in the context of the calling thread, returning only when the work queue is stopped. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-41) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-2 | When a work queue is started, the Zephyr RTOS shall allow the priority of its dedicated thread to be configured. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-2) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-30 | When a work queue is started, the Zephyr RTOS shall allow a name to be assigned to the work queue's dedicated thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-30) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-31 | When a work queue is started, the Zephyr RTOS shall allow the work queue's dedicated thread to be marked as essential to system operation. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-31) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-3 | The Zephyr RTOS shall process the work items of a work queue in the order in which they were submitted. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-3) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-4 | While yielding between work items is enabled for a work queue, the Zephyr RTOS shall cause the work queue thread to yield to other ready threads between processing successive work items. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-4) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-44 | While yielding between work items is disabled for a work queue, the Zephyr RTOS shall not yield the work queue thread until no work items remain queued. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-44) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-5 | The Zephyr RTOS shall provide a mechanism to wait until all work items submitted to a work queue have been processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-5) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-32 | While a work queue is draining, the Zephyr RTOS shall reject submission of work items to that work queue unless the submission originates from the work queue's own thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-32) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-6 | When a drain operation is initiated with submission blocking enabled, the Zephyr RTOS shall continue to prevent submission of work items to the work queue after the drain completes, until submissions are explicitly re-enabled. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-6) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-7 | The Zephyr RTOS shall provide a mechanism to allow work items to be submitted again to a work queue whose submissions were previously blocked. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-7) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-8 | The Zephyr RTOS shall provide a mechanism to stop the dedicated thread of a work queue that has been drained and is blocking new submissions. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-8) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-45 | When stopping a work queue, the Zephyr RTOS shall wait for the work queue thread to terminate for at most a caller-specified timeout. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-45) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-53 | If the work queue thread has not terminated when the stop timeout expires, then the Zephyr RTOS shall return an error indicating timeout and leave the work queue running. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-53) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-46 | If a stop is requested for a work queue whose dedicated thread is marked as essential to system operation, then the Zephyr RTOS shall reject the request and return an error indicating that the operation is not supported. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-46) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-9 | The Zephyr RTOS shall provide a mechanism to initialize a work item at run time, associating a handler function to be executed when the work item is processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-9) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-34 | The Zephyr RTOS shall provide a mechanism to define and initialize a work item at compile time, associating a handler function to be executed when the work item is processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-34) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-33 | The Zephyr RTOS shall provide a system work queue that is started during kernel initialization and is available to application and kernel code. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-33) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-10 | The Zephyr RTOS shall provide a mechanism to submit a work item to the system work queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-10) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-11 | The Zephyr RTOS shall provide a mechanism to submit a work item to a specified work queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-11) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-12 | The Zephyr RTOS shall allow a work item to be submitted from either a thread or an interrupt service routine. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-12) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-13 | When the work queue thread removes a work item from the queue, the Zephyr RTOS shall invoke that work item's handler function in the context of the work queue thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-13) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-14 | If a work item is submitted while it is already queued and has not yet started running, then the Zephyr RTOS shall retain the work item at its current position in the queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-14) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-47 | If a work item is submitted while its handler function is running, then the Zephyr RTOS shall queue the work item to be processed again after the running handler function completes. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-47) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-48 | If a work item is submitted to a work queue while its handler function is running on a different work queue, then the Zephyr RTOS shall queue the work item on the work queue that is running it. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-48) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-15 | The Zephyr RTOS shall provide a mechanism to wait until a submitted work item's handler function has finished executing. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-15) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-16 | The Zephyr RTOS shall provide a mechanism to determine whether a work item is currently pending, where a work item is pending while it is waiting for its delay to elapse, queued to a work queue, running, being cancelled, or being flushed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-16) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-17 | The Zephyr RTOS shall provide a mechanism to cancel a work item that has been submitted but has not yet started running, so that its handler function is not invoked. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-17) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-18 | If a work item's handler function has already started running when the work item is cancelled, then the Zephyr RTOS shall not interrupt the execution of that handler function. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-18) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-19 | The Zephyr RTOS shall provide a mechanism to cancel a work item and wait until the work item is no longer pending. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-19) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-20 | The Zephyr RTOS shall provide a mechanism to initialize a delayable work item at run time, associating a handler function to be executed when the work item is processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-20) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-35 | The Zephyr RTOS shall provide a mechanism to define and initialize a delayable work item at compile time, associating a handler function to be executed when the work item is processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-35) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-21 | The Zephyr RTOS shall provide a mechanism to schedule a delayable work item to be submitted to a specified work queue after a specified delay. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-21) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-36 | The Zephyr RTOS shall provide a mechanism to schedule a delayable work item to be submitted to the system work queue after a specified delay. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-36) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-22 | When the scheduled delay of a delayable work item elapses, the Zephyr RTOS shall submit the work item to its work queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-22) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-23 | The Zephyr RTOS shall provide a mechanism to reschedule a delayable work item that is scheduled but not yet submitted, replacing the previously scheduled delay with the new delay. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-23) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-49 | If a delayable work item is rescheduled with a non-zero delay while it is queued or running, then the Zephyr RTOS shall leave that execution unaffected and schedule an additional submission of the work item after the new delay. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-49) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-24 | The Zephyr RTOS shall provide a mechanism to cancel a delayable work item that has been scheduled but not yet submitted to its work queue, so that it is not submitted. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-24) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-42 | The Zephyr RTOS shall provide a mechanism to wait until a delayable work item's handler function has finished executing. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-42) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-50 | When a wait for completion is requested for a delayable work item that is scheduled but not yet submitted, the Zephyr RTOS shall submit the work item to its work queue immediately before waiting. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-50) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-43 | The Zephyr RTOS shall provide a mechanism to cancel a delayable work item and wait until the work item is no longer pending. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-43) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-25 | The Zephyr RTOS shall provide a mechanism to query the time remaining until a scheduled delayable work item is submitted to its work queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-25) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-26 | Where workqueue work timeout monitoring is enabled, the Zephyr RTOS shall monitor the execution duration of each work item and, if a work item handler runs longer than the configured timeout, abort the work queue thread. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-26) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-51 | The Zephyr RTOS shall provide a mechanism to initialize a triggered work item at run time, associating a handler function to be executed when the work item is processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-51) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-27 | The Zephyr RTOS shall provide a mechanism to submit a work item that is processed when any of a specified set of poll events becomes ready or when a specified timeout elapses, and to report the triggering outcome to the work item handler. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-27) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-52 | If a triggered work item is submitted while it is still waiting for its poll events, then the Zephyr RTOS shall cancel the existing submission and resubmit the work item with the new set of poll events. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-52) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-28 | The Zephyr RTOS shall provide a mechanism to cancel a submitted triggered work item before any of its poll events becomes ready. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-28) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-37 | The Zephyr RTOS shall provide a mechanism to initialize, at run time, a work item usable by user mode threads, associating a handler function to be executed when the work item is processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-37) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-38 | The Zephyr RTOS shall provide a mechanism to define and initialize, at compile time, a work item usable by user mode threads, associating a handler function to be executed when the work item is processed. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-38) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-39 | The Zephyr RTOS shall provide a mechanism to start a work queue whose dedicated thread runs in user mode. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-39) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |
| ZEP-SRS-38-40 | The Zephyr RTOS shall provide a mechanism for user mode threads to submit a work item to a user mode work queue. | https://github.com/zephyrproject-rtos/reqmgmt | b9e702780b6dff096bebb151ab724e6c35fe3cd3 | docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-40) | Work Queues | Non déterminé | Non déterminé | ISO 26262 Partie 6 — Ordonnancement | Observé |

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

- [ ] `CA-ZEP-SRS-38-1` : l'UID ZEP-SRS-38-1 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-1).
- [ ] `CA-ZEP-SRS-38-29` : l'UID ZEP-SRS-38-29 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-29).
- [ ] `CA-ZEP-SRS-38-41` : l'UID ZEP-SRS-38-41 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-41).
- [ ] `CA-ZEP-SRS-38-2` : l'UID ZEP-SRS-38-2 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-2).
- [ ] `CA-ZEP-SRS-38-30` : l'UID ZEP-SRS-38-30 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-30).
- [ ] `CA-ZEP-SRS-38-31` : l'UID ZEP-SRS-38-31 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-31).
- [ ] `CA-ZEP-SRS-38-3` : l'UID ZEP-SRS-38-3 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-3).
- [ ] `CA-ZEP-SRS-38-4` : l'UID ZEP-SRS-38-4 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-4).
- [ ] `CA-ZEP-SRS-38-44` : l'UID ZEP-SRS-38-44 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-44).
- [ ] `CA-ZEP-SRS-38-5` : l'UID ZEP-SRS-38-5 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-5).
- [ ] `CA-ZEP-SRS-38-32` : l'UID ZEP-SRS-38-32 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-32).
- [ ] `CA-ZEP-SRS-38-6` : l'UID ZEP-SRS-38-6 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-6).
- [ ] `CA-ZEP-SRS-38-7` : l'UID ZEP-SRS-38-7 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-7).
- [ ] `CA-ZEP-SRS-38-8` : l'UID ZEP-SRS-38-8 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-8).
- [ ] `CA-ZEP-SRS-38-45` : l'UID ZEP-SRS-38-45 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-45).
- [ ] `CA-ZEP-SRS-38-53` : l'UID ZEP-SRS-38-53 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-53).
- [ ] `CA-ZEP-SRS-38-46` : l'UID ZEP-SRS-38-46 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-46).
- [ ] `CA-ZEP-SRS-38-9` : l'UID ZEP-SRS-38-9 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-9).
- [ ] `CA-ZEP-SRS-38-34` : l'UID ZEP-SRS-38-34 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-34).
- [ ] `CA-ZEP-SRS-38-33` : l'UID ZEP-SRS-38-33 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-33).
- [ ] `CA-ZEP-SRS-38-10` : l'UID ZEP-SRS-38-10 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-10).
- [ ] `CA-ZEP-SRS-38-11` : l'UID ZEP-SRS-38-11 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-11).
- [ ] `CA-ZEP-SRS-38-12` : l'UID ZEP-SRS-38-12 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-12).
- [ ] `CA-ZEP-SRS-38-13` : l'UID ZEP-SRS-38-13 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-13).
- [ ] `CA-ZEP-SRS-38-14` : l'UID ZEP-SRS-38-14 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-14).
- [ ] `CA-ZEP-SRS-38-47` : l'UID ZEP-SRS-38-47 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-47).
- [ ] `CA-ZEP-SRS-38-48` : l'UID ZEP-SRS-38-48 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-48).
- [ ] `CA-ZEP-SRS-38-15` : l'UID ZEP-SRS-38-15 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-15).
- [ ] `CA-ZEP-SRS-38-16` : l'UID ZEP-SRS-38-16 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-16).
- [ ] `CA-ZEP-SRS-38-17` : l'UID ZEP-SRS-38-17 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-17).
- [ ] `CA-ZEP-SRS-38-18` : l'UID ZEP-SRS-38-18 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-18).
- [ ] `CA-ZEP-SRS-38-19` : l'UID ZEP-SRS-38-19 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-19).
- [ ] `CA-ZEP-SRS-38-20` : l'UID ZEP-SRS-38-20 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-20).
- [ ] `CA-ZEP-SRS-38-35` : l'UID ZEP-SRS-38-35 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-35).
- [ ] `CA-ZEP-SRS-38-21` : l'UID ZEP-SRS-38-21 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-21).
- [ ] `CA-ZEP-SRS-38-36` : l'UID ZEP-SRS-38-36 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-36).
- [ ] `CA-ZEP-SRS-38-22` : l'UID ZEP-SRS-38-22 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-22).
- [ ] `CA-ZEP-SRS-38-23` : l'UID ZEP-SRS-38-23 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-23).
- [ ] `CA-ZEP-SRS-38-49` : l'UID ZEP-SRS-38-49 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-49).
- [ ] `CA-ZEP-SRS-38-24` : l'UID ZEP-SRS-38-24 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-24).
- [ ] `CA-ZEP-SRS-38-42` : l'UID ZEP-SRS-38-42 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-42).
- [ ] `CA-ZEP-SRS-38-50` : l'UID ZEP-SRS-38-50 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-50).
- [ ] `CA-ZEP-SRS-38-43` : l'UID ZEP-SRS-38-43 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-43).
- [ ] `CA-ZEP-SRS-38-25` : l'UID ZEP-SRS-38-25 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-25).
- [ ] `CA-ZEP-SRS-38-26` : l'UID ZEP-SRS-38-26 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-26).
- [ ] `CA-ZEP-SRS-38-51` : l'UID ZEP-SRS-38-51 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-51).
- [ ] `CA-ZEP-SRS-38-27` : l'UID ZEP-SRS-38-27 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-27).
- [ ] `CA-ZEP-SRS-38-52` : l'UID ZEP-SRS-38-52 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-52).
- [ ] `CA-ZEP-SRS-38-28` : l'UID ZEP-SRS-38-28 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-28).
- [ ] `CA-ZEP-SRS-38-37` : l'UID ZEP-SRS-38-37 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-37).
- [ ] `CA-ZEP-SRS-38-38` : l'UID ZEP-SRS-38-38 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-38).
- [ ] `CA-ZEP-SRS-38-39` : l'UID ZEP-SRS-38-39 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-39).
- [ ] `CA-ZEP-SRS-38-40` : l'UID ZEP-SRS-38-40 est retrouvable dans docs/software_requirements/work_queues.sdoc (UID ZEP-SRS-38-40).
- [ ] Les sources, révisions et chemins sont conservés sans modification.
- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent).
- [ ] Les correspondances automobile restent candidates sans revue spécialisée.
- [ ] Les inconnues restent explicitement ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences Work Queues

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
