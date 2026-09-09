# Feature : Interruptions et Timing

## 1. Informations générales

- **Identifiant :** `FEAT-INT`
- **Nom de la feature :** `Interruptions et Timing`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services interruptions et timing du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services interruptions et timing de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences interruptions et timing de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à interruptions et timing.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Interruptions et Timing | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (interruptions-et-timing.md).
- Traçabilité des exigences interruptions et timing vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-INT-001 : Le système doit permettre l'installation statique de routines de service d'interruption (ISR) avec déclaration au moment de la compilation
- [ ] ZEP-INT-002 : Le système doit permettre l'installation dynamique d'ISR pendant l'exécution, permettant la flexibilité de configuration
- [ ] ZEP-INT-003 : Le système doit permettre la désactivation globale de toutes les interruptions pour les sections critiques
- [ ] ZEP-INT-004 : Le système doit permettre la désactivation sélective d'interruptions spécifiques par leur numéro IRQ
- [ ] ZEP-INT-005 : Le système doit supporter les interruptions multi-niveaux (nested interrupts) pour gérer différentes priorités d'IRQ
- [ ] ZEP-TIM-001 : Le système doit fournir l'uptime système en millisecondes, ticks système et secondes depuis le démarrage
- [ ] ZEP-TIM-002 : Le système doit fournir un compteur de cycles hardware haute résolution pour les mesures de performance précises
- [ ] ZEP-TIM-003 : Le système doit permettre la mise en sommeil (sleep) de threads pour une durée spécifiée en ms ou ticks
- [ ] ZEP-TIM-004 : Le système doit supporter les timeouts absolus (deadline) en plus des timeouts relatifs pour les opérations bloquantes
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Interruptions et Timing

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services interruptions et timing sont compilés et chargés

  Scénario: ZEP-INT-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Interrupts disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'installation statique de routines de service d'interruption (ISR) avec déclaration au moment de la compilation"
    Alors l'opération est exécutée selon la spécification §10.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-INT-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Interrupts disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'installation dynamique d'ISR pendant l'exécution, permettant la flexibilité de configuration"
    Alors l'opération est exécutée selon la spécification §10.5
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-INT-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Interrupts disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la désactivation globale de toutes les interruptions pour les sections critiques"
    Alors l'opération est exécutée selon la spécification §10.8
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-INT-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Interrupts disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la désactivation sélective d'interruptions spécifiques par leur numéro IRQ"
    Alors l'opération est exécutée selon la spécification §10.10
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-INT-005 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Interrupts disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter les interruptions multi-niveaux (nested interrupts) pour gérer différentes priorités d'IRQ"
    Alors l'opération est exécutée selon la spécification §10.14
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TIM-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Kernel Timing disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir l'uptime système en millisecondes, ticks système et secondes depuis le démarrage"
    Alors l'opération est exécutée selon la spécification §11.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TIM-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Kernel Timing disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir un compteur de cycles hardware haute résolution pour les mesures de performance précises"
    Alors l'opération est exécutée selon la spécification §11.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TIM-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Kernel Timing disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la mise en sommeil (sleep) de threads pour une durée spécifiée en ms ou ticks"
    Alors l'opération est exécutée selon la spécification §11.4
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-TIM-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Kernel Timing disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter les timeouts absolus (deadline) en plus des timeouts relatifs pour les opérations bloquantes"
    Alors l'opération est exécutée selon la spécification §11.5
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-INT-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Interrupts
    Quand l'application appelle la fonction associée à "Le système doit permettre l'installation statique de routines de service d'interruption (ISR) avec déclaration au moment de la compilation"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-INT-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Interrupts
    Quand l'application appelle la fonction associée à "Le système doit permettre l'installation dynamique d'ISR pendant l'exécution, permettant la flexibilité de configuration"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-INT-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre l'installation statique de routines de service d'interruption (ISR) avec déclaration au moment de la compilation"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-INT-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre l'installation dynamique d'ISR pendant l'exécution, permettant la flexibilité de configuration"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-INT-001 | CA-001 | §10.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-INT-002 | CA-002 | §10.5 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-INT-003 | CA-003 | §10.8 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-INT-004 | CA-004 | §10.10 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-INT-005 | CA-005 | §10.14 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TIM-001 | CA-006 | §11.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TIM-002 | CA-007 | §11.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TIM-003 | CA-008 | §11.4 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-TIM-004 | CA-009 | §11.5 | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-INT-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §10.1 | Candidat |
| ZEP-INT-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §10.5 | Candidat |
| ZEP-INT-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §10.8 | Candidat |
| ZEP-INT-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §10.10 | Candidat |
| ZEP-INT-005 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §10.14 | Candidat |
| ZEP-TIM-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §11.1 | Candidat |
| ZEP-TIM-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §11.2 | Candidat |
| ZEP-TIM-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §11.4 | Candidat |
| ZEP-TIM-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §11.5 | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs interruptions et timing.
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
| ZEP-INT-001 | Interrupts | Le système doit permettre l'installation statique de routines de service d'interruption (ISR) avec déclaration au moment de la compilation | P0 | §10.1 |
| ZEP-INT-002 | Interrupts | Le système doit permettre l'installation dynamique d'ISR pendant l'exécution, permettant la flexibilité de configuration | P0 | §10.5 |
| ZEP-INT-003 | Interrupts | Le système doit permettre la désactivation globale de toutes les interruptions pour les sections critiques | P0 | §10.8 |
| ZEP-INT-004 | Interrupts | Le système doit permettre la désactivation sélective d'interruptions spécifiques par leur numéro IRQ | P0 | §10.10 |
| ZEP-INT-005 | Interrupts | Le système doit supporter les interruptions multi-niveaux (nested interrupts) pour gérer différentes priorités d'IRQ | P1 | §10.14 |
| ZEP-TIM-001 | Kernel Timing | Le système doit fournir l'uptime système en millisecondes, ticks système et secondes depuis le démarrage | P0 | §11.1 |
| ZEP-TIM-002 | Kernel Timing | Le système doit fournir un compteur de cycles hardware haute résolution pour les mesures de performance précises | P0 | §11.2 |
| ZEP-TIM-003 | Kernel Timing | Le système doit permettre la mise en sommeil (sleep) de threads pour une durée spécifiée en ms ou ticks | P0 | §11.4 |
| ZEP-TIM-004 | Kernel Timing | Le système doit supporter les timeouts absolus (deadline) en plus des timeouts relatifs pour les opérations bloquantes | P1 | §11.5 |
