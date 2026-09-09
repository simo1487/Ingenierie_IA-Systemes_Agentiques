---
description: "Règles d'enquête scientifique sur les bogues, cycle Red-Green-Refactor, patch minimal KISS/SRP et tests de mutation"
trigger: model_decision
---

# Règle : Debugging Falsifiable, Red-Green et Tests de Mutation

## 1. Démarche d'enquête scientifique
- Ne jamais modifier le code sans avoir reproduit le bogue de manière isolée et falsifiable.
- Consigner l'**observation brute** (faits constatés, logs, codes retour) séparément des **hypothèses explicatives** ($H_1$, $H_2$).
- Concevoir un **test discriminant** capable d'éliminer au moins une des hypothèses.
- Rédiger la fiche de reproduction [`specs/templates/template-enquete-reproduction.md`](../../specs/templates/template-enquete-reproduction.md).

## 2. Cycle Red-Green-Refactor & Patch Minimal
1. **Preuve ROUGE :** Exécuter le test discriminant et vérifier qu'il échoue pour la cause identifiée.
2. **Patch Minimal (KISS / YAGNI / SRP) :** Modifier strictement le minimum de lignes nécessaires pour éliminer la cause racine.
   - Proscription absolue de toute refactorisation opportuniste de code voisin.
3. **Preuve VERTE :** Rejouer la commande exacte et constater le succès (code retour 0).

## 3. Épreuve par mutation conceptuelle
- Pour tout correctif ou suite de tests, introduire une mutation intentionnelle (inversion d'opérateur logique, suppression d'une vérification) ou appliquer un faux correctif plausible proposé par l'IA.
- Le test doit impérativement **ÉCHOUER** en présence de la mutation.
- S'il passe, l'assertion est insuffisante : renforcer l'oracle.
- Restaurer immédiatement le code propre validé.
