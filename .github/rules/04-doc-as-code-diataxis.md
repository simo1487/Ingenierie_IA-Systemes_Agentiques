---
description: "Règles de documentation Doc-as-Code, structuration selon Diátaxis, diagrammes Mermaid et matrice de fact-checking"
trigger: model_decision
---

# Règle : Documentation Doc-as-Code, Diátaxis et Fact-Checking

## 1. Structuration selon Diátaxis
Toute documentation technique rédigée doit adopter une intention claire et appartenir strictement à l'un des 4 quadrants Diátaxis :
- **Tutoriel :** Parcours guidé pas-à-pas orienté apprentissage pour débutant.
- **Guide pratique (How-To) :** Résolution d'un problème opérationnel ciblé.
- **Référence :** Description exhaustive et neutre de l'API, des signatures, constantes et formats.
- **Explication :** Discussion d'architecture, mise en perspective des choix techniques et compromis.
*Ne pas mélanger ces quatre styles dans un même paragraphe.*

## 2. Diagrammes Mermaid vérifiés
- Tout schéma de séquence, d'état ou de flux doit être exprimé en Mermaid.
- Le diagramme doit être syntaxiquement valide et refléter fidèlement l'état et les transitions du code réel, sans inventer d'abstractions intermédiaires.

## 3. Matrice de fact-checking obligatoire
- Chaque affirmation technique formulée dans un guide ou une documentation doit être vérifiable.
- Remplir la matrice selon le modèle [`specs/templates/template-fact-check-doc.md`](../../specs/templates/template-fact-check-doc.md) en associant :
  `Affirmation dans le texte` ↔ `Fichier source & ligne exacte` ↔ `Commande de test vérificatrice`.
- Toute affirmation non prouvée doit être retirée ou explicitement signalée comme hypothèse.
