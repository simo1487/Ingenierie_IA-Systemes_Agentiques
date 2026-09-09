# Feature : Communication IPC

## 1. Informations générales

- **Identifiant :** `FEAT-IPC`
- **Nom de la feature :** `Communication IPC`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services communication ipc du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services communication ipc de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences communication ipc de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à communication ipc.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Communication IPC | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (communication-ipc.md).
- Traçabilité des exigences communication ipc vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-IPC-001 : Le système doit permettre la définition de files de messages avec taille de message et capacité configurables au compile-time ou runtime
- [ ] ZEP-IPC-002 : Le système doit permettre l'envoi de messages à l'arrière (back) ou à l'avant (front) de la file selon les besoins de priorité
- [ ] ZEP-IPC-003 : Le système doit permettre la réception de messages avec maintien de l'ordre FIFO et extraction des données
- [ ] ZEP-IPC-004 : Le système doit supporter les timeouts pour l'envoi et la réception, retournant une erreur si l'opération ne peut être complétée dans le délai
- [ ] ZEP-IPC-005 : Le système doit permettre l'initialisation de boîtes aux lettres (mailboxes) au compile-time ou runtime avec taille de message fixe
- [ ] ZEP-IPC-006 : Le système doit supporter l'envoi synchrone (bloquant) et asynchrone (non-bloquant avec signalisation) de messages
- [ ] ZEP-IPC-007 : Le système doit permettre l'écriture de données dans des pipes avec gestion du buffer et des timeouts
- [ ] ZEP-IPC-008 : Le système doit permettre la lecture de données depuis des pipes avec gestion de la fin de flux et des timeouts
- [ ] ZEP-IPC-009 : Le système doit fournir des structures de données FIFO (First-In-First-Out) pour le passage de données avec gestion de la capacité
- [ ] ZEP-IPC-010 : Le système doit fournir des structures de données LIFO (Last-In-First-Out) pour les cas d'utilisation nécessitant une pile
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Communication IPC

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services communication ipc sont compilés et chargés

  Scénario: ZEP-IPC-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Message Queues disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la définition de files de messages avec taille de message et capacité configurables au compile-time ou runtime"
    Alors l'opération est exécutée selon la spécification §17.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Message Queues disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'envoi de messages à l'arrière (back) ou à l'avant (front) de la file selon les besoins de priorité"
    Alors l'opération est exécutée selon la spécification §17.2.1/17.2.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Message Queues disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la réception de messages avec maintien de l'ordre FIFO et extraction des données"
    Alors l'opération est exécutée selon la spécification §17.3.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Message Queues disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter les timeouts pour l'envoi et la réception, retournant une erreur si l'opération ne peut être complétée dans le délai"
    Alors l'opération est exécutée selon la spécification §17.2.3/17.3.3
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-005 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Mailboxes disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'initialisation de boîtes aux lettres (mailboxes) au compile-time ou runtime avec taille de message fixe"
    Alors l'opération est exécutée selon la spécification §14.1/14.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-006 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Mailboxes disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter l'envoi synchrone (bloquant) et asynchrone (non-bloquant avec signalisation) de messages"
    Alors l'opération est exécutée selon la spécification §14.5/14.7
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-007 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Pipes disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'écriture de données dans des pipes avec gestion du buffer et des timeouts"
    Alors l'opération est exécutée selon la spécification §19.3
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-008 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Pipes disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la lecture de données depuis des pipes avec gestion de la fin de flux et des timeouts"
    Alors l'opération est exécutée selon la spécification §19.4
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-009 - Cas nominal
    Étant donné que le système est initialisé avec les APIs FIFO/LIFO disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir des structures de données FIFO (First-In-First-Out) pour le passage de données avec gestion de la capacité"
    Alors l'opération est exécutée selon la spécification §7.x
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-010 - Cas nominal
    Étant donné que le système est initialisé avec les APIs FIFO/LIFO disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir des structures de données LIFO (Last-In-First-Out) pour les cas d'utilisation nécessitant une pile"
    Alors l'opération est exécutée selon la spécification §12.x
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-IPC-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Message Queues
    Quand l'application appelle la fonction associée à "Le système doit permettre la définition de files de messages avec taille de message et capacité configurables au compile-time ou runtime"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-IPC-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Message Queues
    Quand l'application appelle la fonction associée à "Le système doit permettre l'envoi de messages à l'arrière (back) ou à l'avant (front) de la file selon les besoins de priorité"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-IPC-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre la définition de files de messages avec taille de message et capacité configurables au compile-time ou runtime"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-IPC-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre l'envoi de messages à l'arrière (back) ou à l'avant (front) de la file selon les besoins de priorité"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-IPC-001 | CA-001 | §17.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-002 | CA-002 | §17.2.1/17.2.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-003 | CA-003 | §17.3.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-004 | CA-004 | §17.2.3/17.3.3 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-005 | CA-005 | §14.1/14.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-006 | CA-006 | §14.5/14.7 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-007 | CA-007 | §19.3 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-008 | CA-008 | §19.4 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-009 | CA-009 | §7.x | Retour d'appel API / logs | Candidat |
| Vérification ZEP-IPC-010 | CA-0010 | §12.x | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-IPC-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §17.1 | Candidat |
| ZEP-IPC-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §17.2.1/17.2.2 | Candidat |
| ZEP-IPC-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §17.3.1 | Candidat |
| ZEP-IPC-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §17.2.3/17.3.3 | Candidat |
| ZEP-IPC-005 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §14.1/14.2 | Candidat |
| ZEP-IPC-006 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §14.5/14.7 | Candidat |
| ZEP-IPC-007 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §19.3 | Candidat |
| ZEP-IPC-008 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §19.4 | Candidat |
| ZEP-IPC-009 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §7.x | Candidat |
| ZEP-IPC-010 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §12.x | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs communication ipc.
2. Exécuter les tests unitaires / d'intégration associés.
3. Vérifier la présence des exigences dans le code source et la documentation Zephyr.

- **Environnement :** Zephyr SDK (version à préciser par projet), board cible compatible.
- **Données utilisées :** Exemples de test Zephyr (`samples/`) et tests existants (`tests/kernel/`).
- **Résultat attendu :** Les APIs se comportent conformément au document de traçabilité.
- **Limites de la vérification :** Ne prouve pas la conformité ISO 26262 ni le niveau ASIL.

## 13. Dépendances et risques

### Dépendances

- Disponibilité d'un environnement de build Zephyr fonctionnel.
- Sélection d'une version Zephyr et d'une board cible.
- Définition des niveaux ASIL cibles par le safety manager.

### Risques

| Risque | Impact | Probabilité | Mesure de maîtrise | Responsable |
|---|---|---|---|---|
| Exigences non couvertes par tests existants | fort | moyen | Identifier gaps et ajouter tests | Florian |
| Version Zephyr non figée | moyen | moyen | Documenter la version retenue | Shengjie |
| Mapping normes incomplet | fort | moyen | Relecture safety manager | Mohamed |

## 14. Décision de revue

- **Relecteur(s) :** Safety / Quality team
- **Date de revue :** `[AAAA-MM-JJ]`
- **Décision :** `[Acceptée / À corriger / Bloquée]`
- **Corrections demandées :** `[Liste des corrections]`
- **Points restant ouverts :** Version exacte de Zephyr RTOS, niveaux ASIL cibles.

## Checklist finale

- [ ] Le besoin utilisateur est compréhensible.
- [ ] Le périmètre et les exclusions sont explicites.
- [ ] Les entrées et leurs versions sont identifiées.
- [ ] Les sorties sont distinguées des preuves.
- [ ] Les critères d'acceptation sont observables.
- [ ] Il existe au moins un scénario nominal.
- [ ] Il existe au moins un scénario frontière, erreur ou refus.
- [ ] Chaque scénario possède un attendu et un oracle.
- [ ] Les relations de traçabilité sont sourcées.
- [ ] Les inconnues ne sont pas inventées.
- [ ] La vérification est reproductible par une autre personne.
- [ ] Les limites et risques sont documentés.

---

## Exigences couvertes

| ID Exigence | Sous-catégorie | Description | Priorité | Source |
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
