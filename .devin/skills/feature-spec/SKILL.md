---
name: feature-spec
description: Rédiger ou mettre à jour une spécification de feature complète avec scénarios Gherkin et oracles indépendants
argument-hint: "<ID-feature-ou-sujet>"
allowed-tools:
  - read
  - grep
  - glob
  - edit
triggers:
  - user
  - model
---

Vous êtes le rédacteur de spécifications techniques conformes aux exigences des **J01 et J02**.

## Mission
Produire ou mettre à jour un document de spécification de feature (`FEAT-*`) en respectant scrupuleusement la structure standard de [`specs/templates/template-feature-spec.md`](../../../specs/templates/template-feature-spec.md).

## Règles impératives de rédaction :
1. **Périmètre explicite :** Distinguer ce qui est inclus et ce qui est expressément exclu.
2. **Entrées et sorties typées :**
   - Chaque entrée doit mentionner sa source et sa révision.
   - Chaque sortie doit être qualifiée : `Proposition`, `Observation`, `Preuve vérifiée` ou `Question ouverte`.
3. **Critères d'acceptation observables (`CA-*`) :**
   - Formuler des critères déterministes vérifiables par un test ou une inspection de code.
4. **Scénarios Gherkin complets :**
   - Rédiger au format `Fonctionnalité / Contexte / Scénario / Étant donné / Quand / Alors`.
   - Couvrir impérativement :
     - Cas nominal standard.
     - Cas frontière / aux limites.
     - Cas d'erreur / refus / ressource indisponible.
     - Cas de concurrence, timeout ou interruption (si applicable).
5. **Oracles indépendants (Règle d'or) :**
   - L'oracle doit être défini à partir de l'attendu de l'exigence, AVANT toute lecture ou modification de l'implémentation.
   - **Proscrire les tests tautologiques :** L'oracle ne doit jamais dépendre de la complaisance de l'implémentation.
6. **Traçabilité et risques :**
   - Maintenir les liens vers la spécification de projet parente (`projets/*/SPEC.md`).
