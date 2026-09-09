# Feature : Noyau et Ordonnancement (Kernel & Scheduling)

## 1. Informations générales

- **Identifiant :** `FEAT-KRN`
- **Nom de la feature :** `Noyau et Ordonnancement (Kernel & Scheduling)`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services noyau et ordonnancement (kernel & scheduling) du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services noyau et ordonnancement (kernel & scheduling) de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences noyau et ordonnancement (kernel & scheduling) de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à noyau et ordonnancement (kernel & scheduling).
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Noyau et Ordonnancement (Kernel & Scheduling) | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (noyau-et-ordonnancement-kernel-and-scheduling.md).
- Traçabilité des exigences noyau et ordonnancement (kernel & scheduling) vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-KRN-001 : Le système doit supporter l'opération sur plus d'un CPU, permettant l'exécution de threads sur différents cœurs de processeur
- [ ] ZEP-KRN-002 : Le système doit permettre l'exécution de threads sur des CPU spécifiques (affinité CPU) pour optimiser les performances et l'isolation
- [ ] ZEP-KRN-003 : Le système doit garantir l'exclusion entre CPUs physiques pour éviter les conflits d'accès aux ressources partagées
- [ ] ZEP-KRN-004 : Le système doit permettre l'ordonnancement de threads basé sur des événements, permettant le réveil de threads lors d'occurrences spécifiques
- [ ] ZEP-KRN-005 : Le système doit supporter les priorités de type deadline scheduling pour les applications temps réel avec contraintes temporelles strictes
- [ ] ZEP-KRN-006 : Le système doit supporter la préemption, permettant à un thread de priorité plus élevée d'interrompre un thread de priorité inférieure
- [ ] ZEP-KRN-007 : Le système doit supporter des priorités de thread non préemptibles pour les sections critiques qui ne doivent pas être interrompues
- [ ] ZEP-KRN-008 : Le système doit supporter le time-sharing des ressources CPU entre les threads de même priorité
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Noyau et Ordonnancement (Kernel & Scheduling)

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services noyau et ordonnancement (kernel & scheduling) sont compilés et chargés

  Scénario: ZEP-KRN-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter l'opération sur plus d'un CPU, permettant l'exécution de threads sur différents cœurs de processeur"
    Alors l'opération est exécutée selon la spécification §27.1.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'exécution de threads sur des CPU spécifiques (affinité CPU) pour optimiser les performances et l'isolation"
    Alors l'opération est exécutée selon la spécification §27.1.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-003 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit garantir l'exclusion entre CPUs physiques pour éviter les conflits d'accès aux ressources partagées"
    Alors l'opération est exécutée selon la spécification §27.1.3
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-004 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit permettre l'ordonnancement de threads basé sur des événements, permettant le réveil de threads lors d'occurrences spécifiques"
    Alors l'opération est exécutée selon la spécification §27.2.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-005 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter les priorités de type deadline scheduling pour les applications temps réel avec contraintes temporelles strictes"
    Alors l'opération est exécutée selon la spécification §27.2.2
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-006 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter la préemption, permettant à un thread de priorité plus élevée d'interrompre un thread de priorité inférieure"
    Alors l'opération est exécutée selon la spécification §27.2.6
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-007 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter des priorités de thread non préemptibles pour les sections critiques qui ne doivent pas être interrompues"
    Alors l'opération est exécutée selon la spécification §27.2.7
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-008 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Thread Scheduling disponibles
    Quand l'application appelle la fonction associée à "Le système doit supporter le time-sharing des ressources CPU entre les threads de même priorité"
    Alors l'opération est exécutée selon la spécification §27.2.8
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-KRN-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Thread Scheduling
    Quand l'application appelle la fonction associée à "Le système doit supporter l'opération sur plus d'un CPU, permettant l'exécution de threads sur différents cœurs de processeur"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-KRN-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Thread Scheduling
    Quand l'application appelle la fonction associée à "Le système doit permettre l'exécution de threads sur des CPU spécifiques (affinité CPU) pour optimiser les performances et l'isolation"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-KRN-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit supporter l'opération sur plus d'un CPU, permettant l'exécution de threads sur différents cœurs de processeur"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-KRN-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit permettre l'exécution de threads sur des CPU spécifiques (affinité CPU) pour optimiser les performances et l'isolation"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-KRN-001 | CA-001 | §27.1.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-KRN-002 | CA-002 | §27.1.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-KRN-003 | CA-003 | §27.1.3 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-KRN-004 | CA-004 | §27.2.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-KRN-005 | CA-005 | §27.2.2 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-KRN-006 | CA-006 | §27.2.6 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-KRN-007 | CA-007 | §27.2.7 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-KRN-008 | CA-008 | §27.2.8 | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-KRN-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.1.1 | Candidat |
| ZEP-KRN-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.1.2 | Candidat |
| ZEP-KRN-003 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.1.3 | Candidat |
| ZEP-KRN-004 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.2.1 | Candidat |
| ZEP-KRN-005 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.2.2 | Candidat |
| ZEP-KRN-006 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.2.6 | Candidat |
| ZEP-KRN-007 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.2.7 | Candidat |
| ZEP-KRN-008 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §27.2.8 | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs noyau et ordonnancement (kernel & scheduling).
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
| ZEP-KRN-001 | Thread Scheduling | Le système doit supporter l'opération sur plus d'un CPU, permettant l'exécution de threads sur différents cœurs de processeur | P0 | §27.1.1 |
| ZEP-KRN-002 | Thread Scheduling | Le système doit permettre l'exécution de threads sur des CPU spécifiques (affinité CPU) pour optimiser les performances et l'isolation | P0 | §27.1.2 |
| ZEP-KRN-003 | Thread Scheduling | Le système doit garantir l'exclusion entre CPUs physiques pour éviter les conflits d'accès aux ressources partagées | P0 | §27.1.3 |
| ZEP-KRN-004 | Thread Scheduling | Le système doit permettre l'ordonnancement de threads basé sur des événements, permettant le réveil de threads lors d'occurrences spécifiques | P0 | §27.2.1 |
| ZEP-KRN-005 | Thread Scheduling | Le système doit supporter les priorités de type deadline scheduling pour les applications temps réel avec contraintes temporelles strictes | P1 | §27.2.2 |
| ZEP-KRN-006 | Thread Scheduling | Le système doit supporter la préemption, permettant à un thread de priorité plus élevée d'interrompre un thread de priorité inférieure | P0 | §27.2.6 |
| ZEP-KRN-007 | Thread Scheduling | Le système doit supporter des priorités de thread non préemptibles pour les sections critiques qui ne doivent pas être interrompues | P1 | §27.2.7 |
| ZEP-KRN-008 | Thread Scheduling | Le système doit supporter le time-sharing des ressources CPU entre les threads de même priorité | P2 | §27.2.8 |
