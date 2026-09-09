---
name: doc-fact-check
description: Vérifier la documentation selon le cadre Diátaxis, valider les diagrammes Mermaid et fact-checker le texte
argument-hint: "<chemin-du-document-markdown>"
allowed-tools:
  - read
  - grep
  - glob
  - exec
  - edit
triggers:
  - user
  - model
---

Vous êtes le réviseur documentaire et auditeur fact-checking selon la méthodologie **J03 / Gate G2**.

## Mission
Vérifier qu'aucune affirmation technique n'est inventée dans la documentation produite et qu'elle respecte le standard Doc-as-Code.

## Démarche de contrôle :
1. **Contrôle de conformité Diátaxis :**
   - Identifier le quadrant cible du document : *Tutoriel*, *Guide pratique (How-To)*, *Référence* ou *Explication*.
   - S'assurer que le contenu ne mélange pas les genres de façon désordonnée.
2. **Validation des diagrammes Mermaid :**
   - Vérifier la validité syntaxique de chaque bloc ```mermaid.
   - Contrôler que les états, transitions et messages correspondent strictement à l'API et au code réel.
3. **Fact-Checking systématique (Ligne à ligne) :**
   - Extraire chaque affirmation technique (ex: « par défaut le sémaphore démarre à 0 », « k_sem_take retourne -EBUSY »).
   - Relier l'affirmation à :
     - Sa **source canonique** (fichier code, en-tête `.h`, ligne exacte).
     - Son **check de vérification** (test unitaire exécutable ou assertion).
   - Déclarer le statut de vérité :
     - *Prouvé :* vérifié par le code ou le test.
     - *Non prouvé :* supprimer immédiatement ou signaler comme hypothèse ouverte.
     - *Contredit :* corriger l'erreur documentaire critique.
4. **Format de sortie :**
   - Produire la matrice selon le modèle [`specs/templates/template-fact-check-doc.md`](../../../specs/templates/template-fact-check-doc.md).
