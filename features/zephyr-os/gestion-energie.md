# Feature : Gestion Énergie

## 1. Informations générales

- **Identifiant :** `FEAT-PWR`
- **Nom de la feature :** `Gestion Énergie`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`

## 2. Objectif

Cette feature permet de fournir les services gestion énergie du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services gestion énergie de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences gestion énergie de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à gestion énergie.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences Gestion Énergie | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé (gestion-energie.md).
- Traçabilité des exigences gestion énergie vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

- [ ] ZEP-PWR-001 : Le système doit fournir un contrôle des états d'alimentation (power states) permettant la transition entre différents niveaux de consommation
- [ ] ZEP-PWR-002 : Le système doit notifier les composants des changements d'états d'alimentation pour permettre une adaptation appropriée
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Gestion Énergie

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services gestion énergie sont compilés et chargés

  Scénario: ZEP-PWR-001 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Power Management disponibles
    Quand l'application appelle la fonction associée à "Le système doit fournir un contrôle des états d'alimentation (power states) permettant la transition entre différents niveaux de consommation"
    Alors l'opération est exécutée selon la spécification §21.1
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-PWR-002 - Cas nominal
    Étant donné que le système est initialisé avec les APIs Power Management disponibles
    Quand l'application appelle la fonction associée à "Le système doit notifier les composants des changements d'états d'alimentation pour permettre une adaptation appropriée"
    Alors l'opération est exécutée selon la spécification §21.3
    Et aucune erreur fatale n'est levée

  Scénario: ZEP-PWR-001 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Power Management
    Quand l'application appelle la fonction associée à "Le système doit fournir un contrôle des états d'alimentation (power states) permettant la transition entre différents niveaux de consommation"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-PWR-002 - Cas limite
    Étant donné que le système est dans un état de charge maximale pour Power Management
    Quand l'application appelle la fonction associée à "Le système doit notifier les composants des changements d'états d'alimentation pour permettre une adaptation appropriée"
    Alors l'opération reste déterministe et retourne un statut cohérent

  Scénario: ZEP-PWR-001 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit fournir un contrôle des états d'alimentation (power states) permettant la transition entre différents niveaux de consommation"
    Alors le système retourne une erreur et n'altère pas l'état global

  Scénario: ZEP-PWR-002 - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "Le système doit notifier les composants des changements d'états d'alimentation pour permettre une adaptation appropriée"
    Alors le système retourne une erreur et n'altère pas l'état global
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Vérification ZEP-PWR-001 | CA-001 | §21.1 | Retour d'appel API / logs | Candidat |
| Vérification ZEP-PWR-002 | CA-002 | §21.3 | Retour d'appel API / logs | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| ZEP-PWR-001 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §21.1 | Candidat |
| ZEP-PWR-002 | zephyr-os-requirements-traceability.md | Implémente exigence système | Section §21.3 | Candidat |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs gestion énergie.
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
| ZEP-PWR-001 | Power Management | Le système doit fournir un contrôle des états d'alimentation (power states) permettant la transition entre différents niveaux de consommation | P1 | §21.1 |
| ZEP-PWR-002 | Power Management | Le système doit notifier les composants des changements d'états d'alimentation pour permettre une adaptation appropriée | P1 | §21.3 |
