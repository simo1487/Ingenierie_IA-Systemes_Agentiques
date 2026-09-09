---
description: "Règles d'audit des exigences, Example Mapping, tables de décision, Gherkin et oracles indépendants"
trigger: always_on
---

# Règle : Exigences, Example Mapping et Oracles Indépendants

## 1. Audit d'exigence et conservation des inconnues
- Vérifier systématiquement la singularité (une seule exigence par item), la clarté et la vérifiabilité.
- Les informations manquantes doivent être consignées dans le **Registre d'ambiguïtés**.
- **Interdiction formelle :** Ne jamais laisser l'IA inventer un comportement manquant. Toute inconnue reste explicite jusqu'à décision humaine.

## 2. Example Mapping & Tables de décision
- Chaque règle métier doit être illustrée par :
  1. Au moins un exemple nominal concret.
  2. Au moins un exemple frontière / cas limite.
  3. Au moins un contre-exemple (erreur, refus d'entrée, contexte ISR invalide).
- Lorsque plusieurs conditions booléennes s'entrecroisent, formaliser une **table de décision**.

## 3. Scénarios Gherkin & Oracles indépendants
- Rédiger en syntaxe standard : `Fonctionnalité`, `Contexte`, `Scénario`, `Étant donné`, `Quand`, `Alors`.
- Définir l'**oracle indépendant** AVANT l'écriture du code de test : la condition d'acceptation doit venir de la spécification externe.
- **Interdiction des tests tautologiques :** Rejeter tout test qui valide le code en recopiant simplement sa logique interne ou qui utilise des assertions toujours vraies.
