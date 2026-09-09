# Feature : Synchronisation et Communication

## 1. Informations générales

- **Identifiant :** `FEAT-SYN`
- **Nom de la feature :** `Synchronisation et Communication`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services synchronisation et communication du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services synchronisation et communication de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences synchronisation et communication de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à synchronisation et communication.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Synchronisation et Communication | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (synchronisation-et-communication.md).
- Traçabilité des exigences synchronisation et communication vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-SYN-001 : Le système doit permettre le verrouillage d'un mutex par un thread, garantissant l'accès exclusif à une ressource partagée
- [ ] ZEP-SYN-002 : Le système doit permettre le verrouillage d'un mutex qui n'est actuellement possédé par aucun thread
- [ ] ZEP-SYN-003 : Le système doit permettre le verrouillage d'un mutex possédé par un autre thread, bloquant le thread appelant jusqu'à disponibilité
- [ ] ZEP-SYN-004 : Le système doit supporter le verrouillage avec timeout, retournant une erreur si le mutex n'est pas disponible dans le délai spécifié
- [ ] ZEP-SYN-005 : Le système doit implémenter l'héritage de priorité pour éviter l'inversion de priorité lors de l'utilisation de mutex
- [ ] ZEP-SYN-006 : Le système doit fournir un mécanisme d'acquisition de sémaphore compteur, décrémentant le compteur si > 0 ou bloquant sinon
- [ ] ZEP-SYN-007 : Le système doit supporter l'acquisition de sémaphore avec timeout, permettant un blocage limité dans le temps
- [ ] ZEP-SYN-008 : Le système doit permettre la libération de sémaphore, incrémentant le compteur et débloquant éventuellement un thread en attente
- [ ] ZEP-SYN-009 : Le système doit permettre la publication (posting) d'événements, notifiant les threads en attente de conditions spécifiques
- [ ] ZEP-SYN-010 : Le système doit permettre l'attente sur des événements avec option "any" (au moins un) ou "all" (tous) les événements spécifiés
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Synchronisation et Communication

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services synchronisation et communication sont compilés et chargés

  Scénario: ZEP-SYN-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Mutex disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre le verrouillage d'un mutex par un thread, garantissant l'accès exclusif à une ressource partagée"
    Alors l'opération est exécutée selon la spécification §18.4
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Mutex disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre le verrouillage d'un mutex qui n'est actuellement possédé par aucun thread"
    Alors l'opération est exécutée selon la spécification §18.5
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Mutex disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre le verrouillage d'un mutex possédé par un autre thread, bloquant le thread appelant jusqu'à disponibilité"
    Alors l'opération est exécutée selon la spécification §18.6
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Mutex disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter le verrouillage avec timeout, retournant une erreur si le mutex n'est pas disponible dans le délai spécifié"
    Alors l'opération est exécutée selon la spécification §18.7
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-005 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Mutex disponibles
    Quand l'application appelle la fonction associée à "Le système doit implémenter l'héritage de priorité pour éviter l'inversion de priorité lors de l'utilisation de mutex"
    Alors l'opération est exécutée selon la spécification §18.12
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-006 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Sémaphores disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir un mécanisme d'acquisition de sémaphore compteur, décrémentant le compteur si > 0 ou bloquant sinon"
    Alors l'opération est exécutée selon la spécification §23.6
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-007 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Sémaphores disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter l'acquisition de sémaphore avec timeout, permettant un blocage limité dans le temps"
    Alors l'opération est exécutée selon la spécification §23.9
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-008 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Sémaphores disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la libération de sémaphore, incrémentant le compteur et débloquant éventuellement un thread en attente"
    Alors l'opération est exécutée selon la spécification §23.12
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-009 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Events disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre la publication (posting) d'événements, notifiant les threads en attente de conditions spécifiques"
    Alors l'opération est exécutée selon la spécification §5.2.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-010 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Events disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'attente sur des événements avec option "any" (au moins un) ou "all" (tous) les événements spécifiés"
    Alors l'opération est exécutée selon la spécification §5.3.1/5.3.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-SYN-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Mutex
    Quand l'application appelle la fonction associée à "Le système doit permettre le verrouillage d'un mutex par un thread, garantissant l'accès exclusif à une ressource partagée"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-SYN-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Mutex
    Quand l'application appelle la fonction associée à "Le système doit permettre le verrouillage d'un mutex qui n'est actuellement possédé par aucun thread"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-SYN-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre le verrouillage d'un mutex par un thread, garantissant l'accès exclusif à une ressource partagée"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-SYN-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre le verrouillage d'un mutex qui n'est actuellement possédé par aucun thread"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-SYN-001 | CA-001 | §18.4 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-002 | CA-002 | §18.5 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-003 | CA-003 | §18.6 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-004 | CA-004 | §18.7 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-005 | CA-005 | §18.12 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-006 | CA-006 | §23.6 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-007 | CA-007 | §23.9 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-008 | CA-008 | §23.12 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-009 | CA-009 | §5.2.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-SYN-010 | CA-0010 | §5.3.1/5.3.2 | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-SYN-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §18.4 | Candidat |
| ZEP-SYN-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §18.5 | Candidat |
| ZEP-SYN-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §18.6 | Candidat |
| ZEP-SYN-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §18.7 | Candidat |
| ZEP-SYN-005 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §18.12 | Candidat |
| ZEP-SYN-006 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §23.6 | Candidat |
| ZEP-SYN-007 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §23.9 | Candidat |
| ZEP-SYN-008 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §23.12 | Candidat |
| ZEP-SYN-009 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §5.2.1 | Candidat |
| ZEP-SYN-010 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §5.3.1/5.3.2 | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs synchronisation et communication.
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
