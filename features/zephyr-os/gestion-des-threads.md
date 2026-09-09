# Feature : Gestion des Threads

## 1. Informations générales

- **Identifiant :** `FEAT-THR`
- **Nom de la feature :** `Gestion des Threads`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services gestion des threads du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services gestion des threads de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences gestion des threads de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à gestion des threads.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Gestion des Threads | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (gestion-des-threads.md).
- Traçabilité des exigences gestion des threads vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-THR-001 : Le système doit permettre la création de threads avec des paramètres configurables : priorité, taille de pile, options, et fonction d'entrée
- [ ] ZEP-THR-002 : Le système doit permettre la configuration et la modification dynamique de la priorité des threads pendant l'exécution
- [ ] ZEP-THR-003 : Le système doit permettre la suspension d'un thread en cours d'exécution, le mettant dans un état non-prêt
- [ ] ZEP-THR-004 : Le système doit permettre la reprise d'un thread suspendu, le remettant dans l'état prêt pour exécution
- [ ] ZEP-THR-005 : Le système doit permettre la reprise automatique d'un thread suspendu après un délai spécifié en millisecondes ou ticks système
- [ ] ZEP-THR-006 : Le système doit permettre la suppression (terminaison) de threads, libérant les ressources associées de manière sécurisée
- [ ] ZEP-THR-007 : Le système doit gérer les différents états des threads : prêt, en cours, suspendu, terminé, avec transitions valides entre états
- [ ] ZEP-THR-008 : Le système doit fournir des objets pile pour chaque thread, avec gestion de la taille et de l'overflow de pile
- [ ] ZEP-THR-009 : Le système doit supporter différents niveaux de privilèges pour les threads (supervisor vs user mode) pour l'isolation de sécurité
- [ ] ZEP-THR-010 : Le système doit supporter diverses options de configuration de threads : essentiel, coopératif, héritage de priorité, etc.
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Gestion des Threads

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services gestion des threads sont compilés et chargés

  Scénario: ZEP-THR-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la création de threads avec des paramètres configurables : priorité, taille de pile, options, et fonction d'entrée"
    Alors l'opération est exécutée selon la spécification §28.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la configuration et la modification dynamique de la priorité des threads pendant l'exécution"
    Alors l'opération est exécutée selon la spécification §28.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la suspension d'un thread en cours d'exécution, le mettant dans un état non-prêt"
    Alors l'opération est exécutée selon la spécification §28.3
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la reprise d'un thread suspendu, le remettant dans l'état prêt pour exécution"
    Alors l'opération est exécutée selon la spécification §28.4
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-005 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la reprise automatique d'un thread suspendu après un délai spécifié en millisecondes ou ticks système"
    Alors l'opération est exécutée selon la spécification §28.5
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-006 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la suppression (terminaison) de threads, libérant les ressources associées de manière sécurisée"
    Alors l'opération est exécutée selon la spécification §28.6
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-007 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit gérer les différents états des threads : prêt, en cours, suspendu, terminé, avec transitions valides entre états"
    Alors l'opération est exécutée selon la spécification §28.7
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-008 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir des objets pile pour chaque thread, avec gestion de la taille et de l'overflow de pile"
    Alors l'opération est exécutée selon la spécification §28.8
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-009 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter différents niveaux de privilèges pour les threads (supervisor vs user mode) pour l'isolation de sécurité"
    Alors l'opération est exécutée selon la spécification §28.10
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-010 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Threads disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter diverses options de configuration de threads : essentiel, coopératif, héritage de priorité, etc."
    Alors l'opération est exécutée selon la spécification §28.11
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-THR-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Threads
    Quand l'application appelle la fonction associée à "Le système doit permettre la création de threads avec des paramètres configurables : priorité, taille de pile, options, et fonction d'entrée"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-THR-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Threads
    Quand l'application appelle la fonction associée à "Le système doit permettre la configuration et la modification dynamique de la priorité des threads pendant l'exécution"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-THR-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre la création de threads avec des paramètres configurables : priorité, taille de pile, options, et fonction d'entrée"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-THR-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre la configuration et la modification dynamique de la priorité des threads pendant l'exécution"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-THR-001 | CA-001 | §28.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-002 | CA-002 | §28.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-003 | CA-003 | §28.3 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-004 | CA-004 | §28.4 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-005 | CA-005 | §28.5 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-006 | CA-006 | §28.6 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-007 | CA-007 | §28.7 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-008 | CA-008 | §28.8 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-009 | CA-009 | §28.10 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-THR-010 | CA-0010 | §28.11 | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-THR-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.1 | Candidat |
| ZEP-THR-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.2 | Candidat |
| ZEP-THR-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.3 | Candidat |
| ZEP-THR-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.4 | Candidat |
| ZEP-THR-005 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.5 | Candidat |
| ZEP-THR-006 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.6 | Candidat |
| ZEP-THR-007 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.7 | Candidat |
| ZEP-THR-008 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.8 | Candidat |
| ZEP-THR-009 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.10 | Candidat |
| ZEP-THR-010 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §28.11 | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs gestion des threads.
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
