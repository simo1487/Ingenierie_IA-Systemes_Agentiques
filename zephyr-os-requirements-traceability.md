# Exigences Zephyr OS - Base de Traçabilité

> Document d'agrégation et d'organisation des exigences Zephyr OS pour la traçabilité dans le cycle de développement automobile.

## 1. Informations générales

- **Projet :** Zephyr OS RTOS
- **Source des exigences :** Repository `zephyrproject-rtos/reqmgmt` (Requirements Management)
- **Version source :** Documentation StrictDoc (2024-2026) - travail préliminaire sur exigences noyau
- **Objectif :** Structurer les exigences pour la traçabilité ISO 26262 / Automotive SPICE
- **Date de récupération :** 2026-09-08
- **Statut :** Exigences système et logiciel documentées avec descriptions détaillées
- **Note :** Les exigences proviennent d'un repository séparé et ne sont pas liées à une version spécifique de Zephyr RTOS

## 2. Organisation des exigences par catégories

### 2.1 Noyau et Ordonnancement (Kernel & Scheduling)

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-KRN-001 | Thread Scheduling | Le système doit supporter l'opération sur plus d'un CPU, permettant l'exécution de threads sur différents cœurs de processeur | P0 | §27.1.1 |
| ZEP-KRN-002 | Thread Scheduling | Le système doit permettre l'exécution de threads sur des CPU spécifiques (affinité CPU) pour optimiser les performances et l'isolation | P0 | §27.1.2 |
| ZEP-KRN-003 | Thread Scheduling | Le système doit garantir l'exclusion entre CPUs physiques pour éviter les conflits d'accès aux ressources partagées | P0 | §27.1.3 |
| ZEP-KRN-004 | Thread Scheduling | Le système doit permettre l'ordonnancement de threads basé sur des événements, permettant le réveil de threads lors d'occurrences spécifiques | P0 | §27.2.1 |
| ZEP-KRN-005 | Thread Scheduling | Le système doit supporter les priorités de type deadline scheduling pour les applications temps réel avec contraintes temporelles strictes | P1 | §27.2.2 |
| ZEP-KRN-006 | Thread Scheduling | Le système doit supporter la préemption, permettant à un thread de priorité plus élevée d'interrompre un thread de priorité inférieure | P0 | §27.2.6 |
| ZEP-KRN-007 | Thread Scheduling | Le système doit supporter des priorités de thread non préemptibles pour les sections critiques qui ne doivent pas être interrompues | P1 | §27.2.7 |
| ZEP-KRN-008 | Thread Scheduling | Le système doit supporter le time-sharing des ressources CPU entre les threads de même priorité | P2 | §27.2.8 |

### 2.2 Gestion des Threads

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-THR-001 | Threads | Le système doit permettre la création de threads avec des paramètres configurables : priorité, taille de pile, options, et fonction d'entrée | P0 | §28.1 |
| ZEP-THR-002 | Threads | Le système doit permettre la configuration et la modification dynamique de la priorité des threads pendant l'exécution | P0 | §28.2 |
| ZEP-THR-003 | Threads | Le système doit permettre la suspension d'un thread en cours d'exécution, le mettant dans un état non-prêt | P0 | §28.3 |
| ZEP-THR-004 | Threads | Le système doit permettre la reprise d'un thread suspendu, le remettant dans l'état prêt pour exécution | P0 | §28.4 |
| ZEP-THR-005 | Threads | Le système doit permettre la reprise automatique d'un thread suspendu après un délai spécifié en millisecondes ou ticks système | P1 | §28.5 |
| ZEP-THR-006 | Threads | Le système doit permettre la suppression (terminaison) de threads, libérant les ressources associées de manière sécurisée | P0 | §28.6 |
| ZEP-THR-007 | Threads | Le système doit gérer les différents états des threads : prêt, en cours, suspendu, terminé, avec transitions valides entre états | P0 | §28.7 |
| ZEP-THR-008 | Threads | Le système doit fournir des objets pile pour chaque thread, avec gestion de la taille et de l'overflow de pile | P0 | §28.8 |
| ZEP-THR-009 | Threads | Le système doit supporter différents niveaux de privilèges pour les threads (supervisor vs user mode) pour l'isolation de sécurité | P0 | §28.10 |
| ZEP-THR-010 | Threads | Le système doit supporter diverses options de configuration de threads : essentiel, coopératif, héritage de priorité, etc. | P1 | §28.11 |

### 2.3 Synchronisation et Communication

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-SYN-001 | Mutex | Le système doit permettre le verrouillage d'un mutex par un thread, garantissant l'accès exclusif à une ressource partagée | P0 | §18.4 |
| ZEP-SYN-002 | Mutex | Le système doit permettre le verrouillage d'un mutex qui n'est actuellement possédé par aucun thread | P0 | §18.5 |
| ZEP-SYN-003 | Mutex | Le système doit permettre le verrouillage d'un mutex possédé par un autre thread, bloquant le thread appelant jusqu'à disponibilité | P0 | §18.6 |
| ZEP-SYN-004 | Mutex | Le système doit supporter le verrouillage avec timeout, retournant une erreur si le mutex n'est pas disponible dans le délai spécifié | P0 | §18.7 |
| ZEP-SYN-005 | Mutex | Le système doit implémenter l'héritage de priorité pour éviter l'inversion de priorité lors de l'utilisation de mutex | P0 | §18.12 |
| ZEP-SYN-006 | Sémaphores | Le système doit fournir un mécanisme d'acquisition de sémaphore compteur, décrémentant le compteur si > 0 ou bloquant sinon | P0 | §23.6 |
| ZEP-SYN-007 | Sémaphores | Le système doit supporter l'acquisition de sémaphore avec timeout, permettant un blocage limité dans le temps | P0 | §23.9 |
| ZEP-SYN-008 | Sémaphores | Le système doit permettre la libération de sémaphore, incrémentant le compteur et débloquant éventuellement un thread en attente | P0 | §23.12 |
| ZEP-SYN-009 | Events | Le système doit permettre la publication (posting) d'événements, notifiant les threads en attente de conditions spécifiques | P0 | §5.2.1 |
| ZEP-SYN-010 | Events | Le système doit permettre l'attente sur des événements avec option "any" (au moins un) ou "all" (tous) les événements spécifiés | P0 | §5.3.1/5.3.2 |

### 2.4 Gestion Mémoire

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-MEM-001 | Memory Protection | Le système doit fournir des mécanismes de protection mémoire via MPU/MMU pour isoler les régions mémoire et prévenir les accès non autorisés | P0 | §16.1 |
| ZEP-MEM-002 | Memory Protection | Le système doit assurer la séparation stricte entre les threads en mode utilisateur et le mode noyau pour l'accès mémoire | P0 | §16.3 |
| ZEP-MEM-003 | Memory Protection | Le système doit détecter les overflows de pile (stack overflow) et déclencher un gestionnaire d'erreur approprié | P0 | §16.12 |
| ZEP-MEM-004 | Memory Protection | Le système doit définir et appliquer une politique d'accès mémoire au démarrage (boot time) pour initialiser les protections | P1 | §16.13 |
| ZEP-MEM-005 | Memory Objects | Le système doit fournir des mécanismes d'allocation dynamique de mémoire via un heap géré par le noyau | P0 | §15.1 |
| ZEP-MEM-006 | Memory Objects | Le système doit fournir des objets memory slab pour l'allocation de blocs de taille fixe avec gestion prédictible | P0 | §15.2 |
| ZEP-MEM-007 | Memory Objects | Le système doit permettre l'allocation depuis un heap système avec gestion de la fragmentation et des timeouts | P0 | §15.5 |
| ZEP-MEM-008 | Memory Objects | Le système doit supporter l'alignment mémoire pour les allocations nécessitant des alignements spécifiques (ex: DMA) | P1 | §15.6 |

### 2.5 Interruptions et Timing

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-INT-001 | Interrupts | Le système doit permettre l'installation statique de routines de service d'interruption (ISR) avec déclaration au moment de la compilation | P0 | §10.1 |
| ZEP-INT-002 | Interrupts | Le système doit permettre l'installation dynamique d'ISR pendant l'exécution, permettant la flexibilité de configuration | P0 | §10.5 |
| ZEP-INT-003 | Interrupts | Le système doit permettre la désactivation globale de toutes les interruptions pour les sections critiques | P0 | §10.8 |
| ZEP-INT-004 | Interrupts | Le système doit permettre la désactivation sélective d'interruptions spécifiques par leur numéro IRQ | P0 | §10.10 |
| ZEP-INT-005 | Interrupts | Le système doit supporter les interruptions multi-niveaux (nested interrupts) pour gérer différentes priorités d'IRQ | P1 | §10.14 |
| ZEP-TIM-001 | Kernel Timing | Le système doit fournir l'uptime système en millisecondes, ticks système et secondes depuis le démarrage | P0 | §11.1 |
| ZEP-TIM-002 | Kernel Timing | Le système doit fournir un compteur de cycles hardware haute résolution pour les mesures de performance précises | P0 | §11.2 |
| ZEP-TIM-003 | Kernel Timing | Le système doit permettre la mise en sommeil (sleep) de threads pour une durée spécifiée en ms ou ticks | P0 | §11.4 |
| ZEP-TIM-004 | Kernel Timing | Le système doit supporter les timeouts absolus (deadline) en plus des timeouts relatifs pour les opérations bloquantes | P1 | §11.5 |

### 2.6 Communication IPC

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-IPC-001 | Message Queues | Le système doit permettre la définition de files de messages avec taille de message et capacité configurables au compile-time ou runtime | P0 | §17.1 |
| ZEP-IPC-002 | Message Queues | Le système doit permettre l'envoi de messages à l'arrière (back) ou à l'avant (front) de la file selon les besoins de priorité | P0 | §17.2.1/17.2.2 |
| ZEP-IPC-003 | Message Queues | Le système doit permettre la réception de messages avec maintien de l'ordre FIFO et extraction des données | P0 | §17.3.1 |
| ZEP-IPC-004 | Message Queues | Le système doit supporter les timeouts pour l'envoi et la réception, retournant une erreur si l'opération ne peut être complétée dans le délai | P0 | §17.2.3/17.3.3 |
| ZEP-IPC-005 | Mailboxes | Le système doit permettre l'initialisation de boîtes aux lettres (mailboxes) au compile-time ou runtime avec taille de message fixe | P0 | §14.1/14.2 |
| ZEP-IPC-006 | Mailboxes | Le système doit supporter l'envoi synchrone (bloquant) et asynchrone (non-bloquant avec signalisation) de messages | P0 | §14.5/14.7 |
| ZEP-IPC-007 | Pipes | Le système doit permettre l'écriture de données dans des pipes avec gestion du buffer et des timeouts | P0 | §19.3 |
| ZEP-IPC-008 | Pipes | Le système doit permettre la lecture de données depuis des pipes avec gestion de la fin de flux et des timeouts | P0 | §19.4 |
| ZEP-IPC-009 | FIFO/LIFO | Le système doit fournir des structures de données FIFO (First-In-First-Out) pour le passage de données avec gestion de la capacité | P0 | §7.x |
| ZEP-IPC-010 | FIFO/LIFO | Le système doit fournir des structures de données LIFO (Last-In-First-Out) pour les cas d'utilisation nécessitant une pile | P0 | §12.x |

### 2.7 Gestion Erreurs et Exceptions

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-ERR-001 | Exception Handling | Le système doit fournir un handler d'exception fatale par défaut qui est appelé lors d'erreurs critiques irrécupérables | P0 | §6.1 |
| ZEP-ERR-002 | Exception Handling | Le système doit permettre la définition d'un handler par défaut pour les erreurs fatales avec comportement personnalisable | P0 | §6.2 |
| ZEP-ERR-003 | Exception Handling | Le système doit permettre l'assignation de handlers spécifiques pour différents types d'erreurs fatales | P0 | §6.4 |
| ZEP-ERR-004 | Exception Handling | Le système doit gérer en toute sécurité les appels système invalides ou non implémentés sans compromettre la stabilité du système | P0 | §16.4 |

### 2.8 Drivers et Matériel

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-DRV-001 | Device Driver API | Le système doit fournir une API d'abstraction pour les pilotes de périphériques, unifiant l'interface indépendamment du matériel | P0 | §4.1 |
| ZEP-DRV-002 | Device Driver API | Le système doit exposer au noyau les mécanismes nécessaires pour gérer les interruptions matérielles via les pilotes | P0 | §4.2 |
| ZEP-DRV-003 | Hardware Interface | Le système doit fournir une interface pour les opérations atomiques garantissant l'exclusion mutuelle lors de l'accès mémoire | P0 | §9.1 |
| ZEP-DRV-004 | Hardware Interface | Le système doit fournir un mécanisme de changement de contexte entre threads, sauvegardant et restaurant l'état processeur | P0 | §9.2 |
| ZEP-DRV-005 | Hardware Interface | Le système doit fournir une interface pour gérer les différents modes du processeur (user, supervisor, etc.) | P0 | §9.4 |

### 2.9 Système de Fichiers

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-FS-001 | File System | Le système doit permettre la création de fichiers avec spécification des permissions et des attributs selon le système de fichiers sous-jacent | P1 | §8.1 |
| ZEP-FS-002 | File System | Le système doit permettre l'ouverture de fichiers avec différents modes (lecture, écriture, append) et gestion des erreurs d'accès | P1 | §8.2 |
| ZEP-FS-003 | File System | Le système doit permettre la lecture de données depuis des fichiers avec gestion de la position curseur et détection de fin de fichier | P1 | §8.3 |
| ZEP-FS-004 | File System | Le système doit permettre l'écriture de données dans des fichiers avec gestion du flush et des erreurs d'espace disque | P1 | §8.4 |
| ZEP-FS-005 | File System | Le système doit permettre la fermeture propre de fichiers, libérant les ressources et flushant les buffers si nécessaire | P1 | §8.5 |
| ZEP-FS-006 | File System | Le système doit permettre la suppression de fichiers avec vérification des permissions et gestion des erreurs | P1 | §8.7 |

### 2.10 Logging et Diagnostic

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-LOG-001 | Logging | Le système doit supporter un thread dédié pour le logging, permettant le traitement asynchrone des messages de log | P1 | §13.1 |
| ZEP-LOG-002 | Logging | Le système doit rendre les logs disponibles pour le post-traitement et l'analyse, avec persistance si nécessaire | P1 | §13.2 |
| ZEP-LOG-003 | Logging | Le système doit fournir des mécanismes de filtrage des logs basés sur le niveau de sévérité, le module ou d'autres critères | P1 | §13.4 |
| ZEP-LOG-004 | Logging | Le système doit supporter le logging vers multiples backends (console, fichier, réseau, etc.) simultanément | P1 | §13.5 |
| ZEP-LOG-005 | Tracing | Le système doit permettre l'initialisation de sessions de tracing pour capturer les événements système et les performances | P2 | §30.1 |
| ZEP-LOG-006 | Tracing | Le système doit permettre le déclenchement (start/stop) de traces sur événements spécifiques ou manuellement | P2 | §30.2 |

### 2.11 Gestion Énergie

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-PWR-001 | Power Management | Le système doit fournir un contrôle des états d'alimentation (power states) permettant la transition entre différents niveaux de consommation | P1 | §21.1 |
| ZEP-PWR-002 | Power Management | Le système doit notifier les composants des changements d'états d'alimentation pour permettre une adaptation appropriée | P1 | §21.3 |

### 2.12 Timers et Work Queues

| ID Exigence | Catégorie | Description détaillée | Priorité | Source |
|---|---|---|---|---|
| ZEP-TMR-001 | Timers | Le système doit permettre la définition de timers au compile-time avec spécification de la fonction d'expiration et de la période | P0 | §29.1 |
| ZEP-TMR-002 | Timers | Le système doit appeler une fonction d'expiration (callback) spécifiée par l'utilisateur lorsqu'un timer expire | P0 | §29.2 |
| ZEP-TMR-003 | Timers | Le système doit permettre le démarrage d'un timer avec période ou délai spécifié, en mode périodique ou one-shot | P0 | §29.5 |
| ZEP-TMR-004 | Timers | Le système doit permettre l'arrêt d'un timer en cours, annulant les expirations futures | P0 | §29.6 |
| ZEP-TMR-005 | Timers | Le système doit permettre l'interrogation du statut d'un timer (actif/inactif) et du temps restant avant expiration | P0 | §29.7 |
| ZEP-WQ-001 | Work Queues | Le système doit permettre l'initialisation de work queues avec configuration de la priorité du thread de traitement | P1 | §31.1.1 |
| ZEP-WQ-002 | Work Queues | Le système doit permettre le démarrage et l'arrêt de work queues, avec gestion du thread dédié au traitement | P1 | §31.1.2 |
| ZEP-WQ-003 | Work Queues | Le système doit permettre la soumission de work items et leur traitement séquentiel dans le thread de la work queue | P1 | §31.1.3 |

## 3. Matrice de Traçabilité vers Normes Automobiles

### 3.1 Mapping ISO 26262 (Functional Safety)

| Exigence Zephyr | Élément ISO 26262 | Partie | Niveau ASIL | Justification |
|---|---|---|---|---|
| ZEP-MEM-001 à 004 | Mécanismes de protection mémoire | Partie 6 | ASIL D | Isolation mémoire requise pour safety |
| ZEP-ERR-001 à 004 | Gestion des erreurs | Partie 6 | ASIL D | Détection et traitement erreurs |
| ZEP-KRN-006,007 | Ordonnancement déterministe | Partie 6 | ASIL B/D | Temps réel critique |
| ZEP-INT-001 à 005 | Gestion interruptions | Partie 6 | ASIL D | Latence déterministe |
| ZEP-TIM-001 à 004 | Services de timing | Partie 6 | ASIL B/D | Synchronisation temps réel |
| ZEP-SYN-001 à 010 | Synchronisation | Partie 6 | ASIL C/D | Exclusion mutuelle safety-critical |

### 3.2 Mapping ISO/SAE 21434 (Cybersecurity)

| Exigence Zephyr | Élément ISO/SAE 21434 | Phase | Justification |
|---|---|---|---|
| ZEP-MEM-001,002 | Isolation mémoire | Phase conception | Prévention attaques |
| ZEP-ERR-004 | Validation appels système | Phase implémentation | Contrôle d'accès |
| ZEP-THR-009 | Gestion privilèges threads | Phase conception | Séparation privilèges |
| ZEP-LOG-001 à 004 | Logging et audit | Phase opération | Détection incidents |

### 3.3 Mapping Automotive SPICE

| Exigence Zephyr | Process SPICE | Capacité attendue | Justification |
|---|---|---|---|
| Toutes exigences | SWE.1 | Capacité 3-4 | Spécification requirements |
| ZEP-KRN-*, ZEP-THR-* | SWE.2 | Capacité 3-4 | Architecture système |
| ZEP-SYN-*, ZEP-IPC-* | SWE.3 | Capacité 3-4 | Conception détaillée |
| Toutes exigences | SWE.4 | Capacité 3-4 | Construction |
| ZEP-ERR-*, ZEP-LOG-* | SWE.5 | Capacité 3-4 | Vérification |
| Scénarios de test | SWE.6 | Capacité 3-4 | Validation |

## 4. Structure de Traçabilité par Feature

### 4.1 Template de traçabilité pour implémentation

```markdown
## Feature: [Nom Feature]

### Exigences Zephyr couvertes
| ID Exigence | Description | Priorité | Statut implémentation |
|---|---|---|---|
| ZEP-XXX-001 | Description | P0 | Implémenté/Testé/En cours |
| ZEP-XXX-002 | Description | P1 | À faire |

### Mapping vers tests
| ID Test | Type | Exigence couverte | Statut |
|---|---|---|---|
| TEST-001 | Unitaire | ZEP-XXX-001 | Pass |
| TEST-002 | Intégration | ZEP-XXX-002 | Fail |

### Preuves de conformité
| Norme | Élément | Preuve | Statut |
|---|---|---|---|
| ISO 26262 | Partie 6 §x.y | [Lien code/test] | Vérifié |
```

## 5. Cycle de Vie et Maintenance

### 5.1 Gestion des versions

- **Version courante :** v1.0 (basée sur docs Zephyr 2024)
- **Prochaine revue :** À chaque release LTS Zephyr
- **Procédure de mise à jour :** Comparaison avec nouvelle documentation

### 5.2 Indicateurs de traçabilité

- **Couverture exigences :** % d'exigences implémentées
- **Couverture tests :** % d'exigences avec tests associés
- **Conformité normes :** % d'exigences mappées vers normes
- **Exigences critiques :** Statut des exigences P0

## 6. Questions Ouvertes et Limitations

### 6.1 Exigences non couvertes
- Drivers spécifiques hardware (hors scope documentation générale)
- Power management avancé (varie par architecture)
- File systems spécifiques (FatFS, LittleFS, etc.)

### 6.2 Décisions à prendre
- Sélection des exigences P0 vs P1 pour projet spécifique
- Définition des niveaux ASIL cibles par fonction
- Choix des mécanismes de traçabilité outils (JIRA, DOORS, etc.)

### 6.3 Limites de la documentation
- Documentation Zephyr évolue rapidement
- Certaines fonctionnalités sont expérimentales
- Dépendances architecture non explicitées

## 7. Actions Recommandées

1. **Priorisation :** Sélectionner les exigences P0 pour le MVP
2. **Outil de traçabilité :** Choisir et configurer l'outil
3. **Base de tests :** Créer la base de tests unitaires
4. **Intégration CI :** Automatiser la vérification de traçabilité
5. **Formation équipe :** Former l'équipe sur la structure de traçabilité