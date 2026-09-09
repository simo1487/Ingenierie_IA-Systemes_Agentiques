# Modèle de Spécification de Feature

Ce document est le modèle standard pour spécifier une fonctionnalité ou une exigence logicielle (`FEAT-*`).
Il intègre l'ensemble des exigences méthodologiques des trois premiers jours de formation : oracles indépendants, scénarios Gherkin complets, Example Mapping, distinction des statuts de preuve et traçabilité.

---

## 1. Informations générales

- **Identifiant :** `FEAT-[DOMAINE]-[NUMÉRO]` (ex: `FEAT-QUAL-001`, `FEAT-NORM-002`)
- **Nom de la feature :** [Titre clair et concis de la fonctionnalité]
- **Responsable(s) :** [Équipe et noms des contributeurs]
- **Branche Git associée :** `feat/[nom-de-branche]`
- **Spécification parente :** [`projets/[nom-projet]/SPEC.md`](../../projets/)
- **Priorité :** `P1` (Bloquant) / `P2` (Important) / `P3` (Secondaire)
- **Statut :** `Draft` / `Candidate` / `In Review` / `Validated`
- **Date :** `AAAA-MM-JJ`

---

## 2. Objectif et valeur attendue

[Décrire en 2 ou 3 phrases l'objectif principal de la feature et la valeur opérationnelle qu'elle apporte.]

---

## 3. Besoin utilisateur

> En tant que [rôle utilisateur ou relecteur],  
> Je veux [action ou capacité fournie],  
> Afin de [bénéfice observable ou risque évité].

---

## 4. Contexte, baselines et problème

- **Situation actuelle :** [État actuel du code, des outils ou des documents]
- **Baselines de référence :**
  - Dépôt source : [URL canonique, tag ou commit exact]
  - Exigences : [Version exacte ou commit du référentiel d'exigences, ex: reqmgmt]
- **Problème résolu :** [Défaut, manque ou risque identifié]
- **Décisions humaines réservées :** [Ce qui nécessite obligatoirement un arbitrage humain et ne peut être automatisé par un LLM]
- **Questions ouvertes :** [Points inconnus ou arbitrages restants]

---

## 5. Périmètre

### Inclus
- [Capacité 1 explicitement fournie]
- [Capacité 2]
- [Commande ou interface d'exécution]
- [Format de sortie vérifiable]

### Exclus
- [Ce qui est délibérément hors de cette itération]
- [Aucune certification juridique ou réglementaire automatique]
- [Modification non autorisée de composants upstream]

---

## 6. Entrées du système

| Entrée | Source canonique | Version / commit | Statut d'accès | Niveau de confiance |
|---|---|---|---|---|
| [Fichier ou ressource] | [Chemin ou URL] | [Hash ou tag] | Lecture seule / Écriture | Vérifié / Candidat |

---

## 7. Sorties attendues et typologie d'information

Pour chaque sortie, qualifier formellement sa nature selon le principe J01 :

| Sortie | Description | Type d'information | Oracle de validation |
|---|---|---|---|
| [Artefact produit] | [Description] | `Preuve vérifiée` / `Proposition` / `Observation` | [Comment vérifier ce résultat de façon indépendante] |

---

## 8. Règles métier et Example Mapping

### Règle métier 1 : [Nom de la règle]
- **Règle :** [Énoncé strict du comportement attendu]
- **Exemple nominal :** Étant donné [contexte standard], quand [action], alors [résultat attendu].
- **Exemple aux limites :** Étant donné [contexte frontière], quand [action], alors [résultat attendu].
- **Contre-exemple / Erreur :** Étant donné [contexte invalide], quand [action], alors [refus ou erreur documentée].
- **Question ouverte :** [Point à clarifier sur cette règle]

---

## 9. Critères d'acceptation observables

- [ ] `CA-[DOMAINE]-01` : [Critère observable 1]
- [ ] `CA-[DOMAINE]-02` : [Critère observable 2 avec code retour ou message précis]
- [ ] `CA-[DOMAINE]-03` : [Critère de non-régression ou de gestion d'erreur]
- [ ] `CA-[DOMAINE]-04` : [Reproductibilité par un tiers en suivant la documentation]

---

## 10. Scénarios Gherkin et Oracles indépendants

```gherkin
Fonctionnalité: [Nom de la feature]

  Contexte:
    Étant donné [l'environnement initial configuré]
    Et les outils requis dans leurs versions documentées

  Scénario: [Nom du cas nominal]
    Étant donné [condition initiale valide]
    Quand [action déclenchée]
    Alors [résultat observable]
    Et [statut ou preuve enregistrée]

  Scénario: [Nom du cas aux limites / frontière]
    Étant donné [condition aux limites]
    Quand [action déclenchée]
    Alors [comportement attendu aux bornes]

  Scénario: [Nom du cas d'erreur ou d'outil indisponible]
    Étant donné [outil absent ou entrée invalide]
    Quand [action déclenchée]
    Alors le résultat renvoie un code non nul
    Et un message clair indique la cause sans masquer l'échec

  Scénario: [Nom du cas de concurrence, interruption ou timeout (si applicable)]
    Étant donné [condition asynchrone / timeout]
    Quand [événement se produit]
    Alors [déterminisme et état cohérent garantis]
```

### Grille d'évaluation des oracles

| Scénario | Critère couvert | Oracle indépendant | Risque de tautologie |
|---|---|---|---|
| Nominal | `CA-01` | [Preuve externe au code généré] | Écarté (oracle défini avant code) |
| Erreur | `CA-02` | Code retour non nul + log d'erreur | Écarté |

---

## 11. Matrice de traçabilité v0

| Élément d'exigence | Source ou baseline | Code source relié | Test associé | Statut | Preuve / Oracle |
|---|---|---|---|---|---|
| [ID exigence] | [Fichier / ligne] | [Fichier d'implémentation] | [Fichier de test] | `Observé` / `Candidat` / `Vérifié` | [Description du test] |

> **Avertissement J02 :** Une proximité lexicale ne prouve JAMAIS une relation.

---

## 12. Procédure de vérification et épreuve par mutation

1. **Pré-requis :** [Versions des outils et environnement]
2. **Exécution du test nominal :** [Commande exacte et code retour attendu]
3. **Épreuve par mutation (anti-faux correctif) :**
   - Introduire la mutation contrôlée : [Fichier et modification intentionnelle]
   - Relancer le test : vérifier qu'il **échoue** (preuve du pouvoir discriminant de la suite)
   - Restaurer le code initial

---

## 13. Analyse des risques et maîtrise

| Risque identifié | Gravité | Probabilité | Mesure de maîtrise | Responsable |
|---|---|---|---|---|
| [Risque technique ou environnemental] | Élevé / Moyen / Faible | Élevée / Moyenne / Faible | [Contournement ou garde-fou] | [Nom] |

---

## 14. Décision de revue (Gate G1 / G2)

- **Relecteur(s) croisé(s) :** [Noms des pairs]
- **Date de revue :** `AAAA-MM-JJ`
- **Décision :** `Accepté (Gate franchie)` / `À revoir` / `Refusé`
- **Questions restant ouvertes :** [Liste des points à suivre]
