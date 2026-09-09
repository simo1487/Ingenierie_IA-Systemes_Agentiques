# Feature : Timers et Work Queues

## 1. Informations générales

- **Identifiant :** `FEAT-TMR`
- **Nom de la feature :** `Timers et Work Queues`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services timers et work queues du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services timers et work queues de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences timers et work queues de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à timers et work queues.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Timers et Work Queues | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (timers-et-work-queues.md).
- Traçabilité des exigences timers et work queues vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-TMR-001 : Le système doit permettre la définition de timers au compile-time avec spécification de la fonction d'expiration et de la période
- [ ] ZEP-TMR-002 : Le système doit appeler une fonction d'expiration (callback) spécifiée par l'utilisateur lorsqu'un timer expire
- [ ] ZEP-TMR-003 : Le système doit permettre le démarrage d'un timer avec période ou délai spécifié, en mode périodique ou one-shot
- [ ] ZEP-TMR-004 : Le système doit permettre l'arrêt d'un timer en cours, annulant les expirations futures
- [ ] ZEP-TMR-005 : Le système doit permettre l'interrogation du statut d'un timer (actif/inactif) et du temps restant avant expiration
- [ ] ZEP-WQ-001 : Le système doit permettre l'initialisation de work queues avec configuration de la priorité du thread de traitement
- [ ] ZEP-WQ-002 : Le système doit permettre le démarrage et l'arrêt de work queues, avec gestion du thread dédié au traitement
- [ ] ZEP-WQ-003 : Le système doit permettre la soumission de work items et leur traitement séquentiel dans le thread de la work queue
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Timers et Work Queues

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services timers et work queues sont compilés et chargés

  Scénario: ZEP-TMR-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Timers disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la définition de timers au compile-time avec spécification de la fonction d'expiration et de la période"
    Alors l'opération est exécutée selon la spécification §29.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TMR-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Timers disponibles
    Quand l'application appelle la fonction associée à "Le système doit appeler une fonction d'expiration (callback) spécifiée par l'utilisateur lorsqu'un timer expire"
    Alors l'opération est exécutée selon la spécification §29.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TMR-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Timers disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre le démarrage d'un timer avec période ou délai spécifié, en mode périodique ou one-shot"
    Alors l'opération est exécutée selon la spécification §29.5
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TMR-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Timers disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'arrêt d'un timer en cours, annulant les expirations futures"
    Alors l'opération est exécutée selon la spécification §29.6
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TMR-005 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Timers disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'interrogation du statut d'un timer (actif/inactif) et du temps restant avant expiration"
    Alors l'opération est exécutée selon la spécification §29.7
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-WQ-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Work Queues disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'initialisation de work queues avec configuration de la priorité du thread de traitement"
    Alors l'opération est exécutée selon la spécification §31.1.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-WQ-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Work Queues disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre le démarrage et l'arrêt de work queues, avec gestion du thread dédié au traitement"
    Alors l'opération est exécutée selon la spécification §31.1.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-WQ-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Work Queues disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la soumission de work items et leur traitement séquentiel dans le thread de la work queue"
    Alors l'opération est exécutée selon la spécification §31.1.3
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TMR-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Timers
    Quand l'application appelle la fonction associée à "Le système doit permettre la définition de timers au compile-time avec spécification de la fonction d'expiration et de la période"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-TMR-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Timers
    Quand l'application appelle la fonction associée à "Le système doit appeler une fonction d'expiration (callback) spécifiée par l'utilisateur lorsqu'un timer expire"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-TMR-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre la définition de timers au compile-time avec spécification de la fonction d'expiration et de la période"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-TMR-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit appeler une fonction d'expiration (callback) spécifiée par l'utilisateur lorsqu'un timer expire"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-TMR-001 | CA-001 | §29.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TMR-002 | CA-002 | §29.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TMR-003 | CA-003 | §29.5 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TMR-004 | CA-004 | §29.6 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TMR-005 | CA-005 | §29.7 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-WQ-001 | CA-006 | §31.1.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-WQ-002 | CA-007 | §31.1.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-WQ-003 | CA-008 | §31.1.3 | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-TMR-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §29.1 | Candidat |
| ZEP-TMR-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §29.2 | Candidat |
| ZEP-TMR-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §29.5 | Candidat |
| ZEP-TMR-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §29.6 | Candidat |
| ZEP-TMR-005 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §29.7 | Candidat |
| ZEP-WQ-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §31.1.1 | Candidat |
| ZEP-WQ-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §31.1.2 | Candidat |
| ZEP-WQ-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §31.1.3 | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs timers et work queues.
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
| ZEP-TMR-001 | Timers | Le système doit permettre la définition de timers au compile-time avec spécification de la fonction d'expiration et de la période | P0 | §29.1 |
| ZEP-TMR-002 | Timers | Le système doit appeler une fonction d'expiration (callback) spécifiée par l'utilisateur lorsqu'un timer expire | P0 | §29.2 |
| ZEP-TMR-003 | Timers | Le système doit permettre le démarrage d'un timer avec période ou délai spécifié, en mode périodique ou one-shot | P0 | §29.5 |
| ZEP-TMR-004 | Timers | Le système doit permettre l'arrêt d'un timer en cours, annulant les expirations futures | P0 | §29.6 |
| ZEP-TMR-005 | Timers | Le système doit permettre l'interrogation du statut d'un timer (actif/inactif) et du temps restant avant expiration | P0 | §29.7 |
| ZEP-WQ-001 | Work Queues | Le système doit permettre l'initialisation de work queues avec configuration de la priorité du thread de traitement | P1 | §31.1.1 |
| ZEP-WQ-002 | Work Queues | Le système doit permettre le démarrage et l'arrêt de work queues, avec gestion du thread dédié au traitement | P1 | §31.1.2 |
| ZEP-WQ-003 | Work Queues | Le système doit permettre la soumission de work items et leur traitement séquentiel dans le thread de la work queue | P1 | §31.1.3 |
