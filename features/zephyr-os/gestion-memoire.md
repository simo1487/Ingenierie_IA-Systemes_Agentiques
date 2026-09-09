# Feature : Gestion Mémoire

## 1. Informations générales

- **Identifiant :** `FEAT-MEM`
- **Nom de la feature :** `Gestion Mémoire`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services gestion mémoire du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services gestion mémoire de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences gestion mémoire de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à gestion mémoire.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Gestion Mémoire | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (gestion-memoire.md).
- Traçabilité des exigences gestion mémoire vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-MEM-001 : Le système doit fournir des mécanismes de protection mémoire via MPU/MMU pour isoler les régions mémoire et prévenir les accès non autorisés
- [ ] ZEP-MEM-002 : Le système doit assurer la séparation stricte entre les threads en mode utilisateur et le mode noyau pour l'accès mémoire
- [ ] ZEP-MEM-003 : Le système doit détecter les overflows de pile (stack overflow) et déclencher un gestionnaire d'erreur approprié
- [ ] ZEP-MEM-004 : Le système doit définir et appliquer une politique d'accès mémoire au démarrage (boot time) pour initialiser les protections
- [ ] ZEP-MEM-005 : Le système doit fournir des mécanismes d'allocation dynamique de mémoire via un heap géré par le noyau
- [ ] ZEP-MEM-006 : Le système doit fournir des objets memory slab pour l'allocation de blocs de taille fixe avec gestion prédictible
- [ ] ZEP-MEM-007 : Le système doit permettre l'allocation depuis un heap système avec gestion de la fragmentation et des timeouts
- [ ] ZEP-MEM-008 : Le système doit supporter l'alignment mémoire pour les allocations nécessitant des alignements spécifiques (ex: DMA)
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Gestion Mémoire

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services gestion mémoire sont compilés et chargés

  Scénario: ZEP-MEM-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Protection disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir des mécanismes de protection mémoire via MPU/MMU pour isoler les régions mémoire et prévenir les accès non autorisés"
    Alors l'opération est exécutée selon la spécification §16.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Protection disponibles
    Quand l'application appelle la fonction associée à "Le système doit assurer la séparation stricte entre les threads en mode utilisateur et le mode noyau pour l'accès mémoire"
    Alors l'opération est exécutée selon la spécification §16.3
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Protection disponibles
    Quand l'application appelle la fonction associée à "Le système doit détecter les overflows de pile (stack overflow) et déclencher un gestionnaire d'erreur approprié"
    Alors l'opération est exécutée selon la spécification §16.12
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Protection disponibles
    Quand l'application appelle la fonction associée à "Le système doit définir et appliquer une politique d'accès mémoire au démarrage (boot time) pour initialiser les protections"
    Alors l'opération est exécutée selon la spécification §16.13
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-005 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Objects disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir des mécanismes d'allocation dynamique de mémoire via un heap géré par le noyau"
    Alors l'opération est exécutée selon la spécification §15.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-006 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Objects disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir des objets memory slab pour l'allocation de blocs de taille fixe avec gestion prédictible"
    Alors l'opération est exécutée selon la spécification §15.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-007 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Objects disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'allocation depuis un heap système avec gestion de la fragmentation et des timeouts"
    Alors l'opération est exécutée selon la spécification §15.5
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-008 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Memory Objects disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter l'alignment mémoire pour les allocations nécessitant des alignements spécifiques (ex: DMA)"
    Alors l'opération est exécutée selon la spécification §15.6
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-MEM-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Memory Protection
    Quand l'application appelle la fonction associée à "Le système doit fournir des mécanismes de protection mémoire via MPU/MMU pour isoler les régions mémoire et prévenir les accès non autorisés"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-MEM-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Memory Protection
    Quand l'application appelle la fonction associée à "Le système doit assurer la séparation stricte entre les threads en mode utilisateur et le mode noyau pour l'accès mémoire"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-MEM-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit fournir des mécanismes de protection mémoire via MPU/MMU pour isoler les régions mémoire et prévenir les accès non autorisés"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-MEM-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit assurer la séparation stricte entre les threads en mode utilisateur et le mode noyau pour l'accès mémoire"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-MEM-001 | CA-001 | §16.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-MEM-002 | CA-002 | §16.3 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-MEM-003 | CA-003 | §16.12 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-MEM-004 | CA-004 | §16.13 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-MEM-005 | CA-005 | §15.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-MEM-006 | CA-006 | §15.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-MEM-007 | CA-007 | §15.5 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-MEM-008 | CA-008 | §15.6 | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-MEM-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §16.1 | Candidat |
| ZEP-MEM-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §16.3 | Candidat |
| ZEP-MEM-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §16.12 | Candidat |
| ZEP-MEM-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §16.13 | Candidat |
| ZEP-MEM-005 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §15.1 | Candidat |
| ZEP-MEM-006 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §15.2 | Candidat |
| ZEP-MEM-007 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §15.5 | Candidat |
| ZEP-MEM-008 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §15.6 | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs gestion mémoire.
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
| ZEP-MEM-001 | Memory Protection | Le système doit fournir des mécanismes de protection mémoire via MPU/MMU pour isoler les régions mémoire et prévenir les accès non autorisés | P0 | §16.1 |
| ZEP-MEM-002 | Memory Protection | Le système doit assurer la séparation stricte entre les threads en mode utilisateur et le mode noyau pour l'accès mémoire | P0 | §16.3 |
| ZEP-MEM-003 | Memory Protection | Le système doit détecter les overflows de pile (stack overflow) et déclencher un gestionnaire d'erreur approprié | P0 | §16.12 |
| ZEP-MEM-004 | Memory Protection | Le système doit définir et appliquer une politique d'accès mémoire au démarrage (boot time) pour initialiser les protections | P1 | §16.13 |
| ZEP-MEM-005 | Memory Objects | Le système doit fournir des mécanismes d'allocation dynamique de mémoire via un heap géré par le noyau | P0 | §15.1 |
| ZEP-MEM-006 | Memory Objects | Le système doit fournir des objets memory slab pour l'allocation de blocs de taille fixe avec gestion prédictible | P0 | §15.2 |
| ZEP-MEM-007 | Memory Objects | Le système doit permettre l'allocation depuis un heap système avec gestion de la fragmentation et des timeouts | P0 | §15.5 |
| ZEP-MEM-008 | Memory Objects | Le système doit supporter l'alignment mémoire pour les allocations nécessitant des alignements spécifiques (ex: DMA) | P1 | §15.6 |
