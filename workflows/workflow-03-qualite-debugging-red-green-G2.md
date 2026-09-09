# Workflow 03 — Qualité, Debugging Falsifiable, Red-Green, Mutation & Documentation (Gate G2)

Ce workflow transforme les hypothèses et scénarios candidats de la Gate G1 en preuves réelles observées sur une variante contrôlée, valide la robustesse par mutation, trie les alertes de qualité et produit une documentation vérifiée par fact-checking.

---

## 1. Objectif du workflow

Démontrer qu'un bogue ou une exigence est rigoureusement maîtrisé en apportant la chaîne de preuves complète :
- Défaut reproduit de manière isolée et falsifiable.
- Test discriminant en échec avéré (**Preuve ROUGE**).
- Correctif **MINIMAL** respectant les principes KISS, YAGNI et SRP.
- Rejeu concluant avec succès (**Preuve VERTE**).
- Sensibilité prouvée par **mutation conceptuelle** (anti-faux correctif).
- Tri humain argumenté des alertes statiques (Cppcheck) et élimination des faux positifs.
- Documentation technique structurée selon **Diátaxis**, enrichie de schémas Mermaid et validée par une **matrice de fact-checking**.

---

## 2. Déclencheur & Entrées requises

- **Déclencheur :** Gate G1 franchie pour la spécification concernée.
- **Entrées :**
  - Spécification de feature (`FEAT-*`) avec scénarios Gherkin et oracles indépendants.
  - Matrice de traçabilité v0 (`TRAC-*`).
  - Dépôt de travail sur la branche d'équipe dédiée (`travail.md`).

---

## 3. Séquence opératoire détaillée

```text
Étape 3.1 : Démarche scientifique & Fiche de reproduction (ENQ-*)
  ↓
Étape 3.2 : Exécution & Capture de la Preuve ROUGE
  ↓
Étape 3.3 : Implémentation du Correctif Minimal (KISS / SRP)
  ↓
Étape 3.4 : Rejeu & Capture de la Preuve VERTE
  ↓
Étape 3.5 : Épreuve par Mutation / Faux Correctif
  ↓
Étape 3.6 : Contrôles Qualité Statiques & Tri Humain des Alertes (REV-*)
  ↓
Étape 3.7 : Documentation Diátaxis & Matrice de Fact-Checking (FACT-*)
  ↓
Étape 3.8 : Contrôle de la Gate G2
```

### Étape 3.1 : Démarche scientifique & Fiche de reproduction
Utiliser le modèle [`specs/templates/template-enquete-reproduction.md`](../specs/templates/template-enquete-reproduction.md) :
1. **Observation brute :** Noter le symptôme réel sans extrapolation ni théorie préconçue.
2. **Formulation d'hypothèses concurrentes :** Poser au minimum deux hypothèses explicatives ($H_1$ vs $H_2$).
3. **Test discriminant :** Définir le test précis dont le résultat réfute l'une des hypothèses.
4. **Fiche de reproduction :** Renseigner l'environnement, le commit exact et la commande unique reproductible.

### Étape 3.2 : Exécution & Capture de la Preuve ROUGE
1. Exécuter la commande de test sur la variante concernée.
2. **Vérification de la cause :** S'assurer que le test échoue pour le comportement attendu et non à cause d'une anomalie tierce (compilation, chemin introuvable).
3. Archiver la trace de sortie et le code retour non nul dans le carnet d'enquête.

### Étape 3.3 : Implémentation du Correctif Minimal (Patch KISS / YAGNI / SRP)
1. Modifier uniquement le code strictement nécessaire pour résoudre le défaut démontré.
2. **Interdictions strictes :**
   - Aucune refactorisation opportuniste de fonctions voisines.
   - Aucun ajout de bibliothèque ou de complexité anticipative.
   - Aucune modification dans `upstream/**`.

### Étape 3.4 : Rejeu & Capture de la Preuve VERTE
1. Rejouer la commande exacte de reproduction.
2. Constater le succès (code retour 0).
3. Exécuter l'ensemble de la suite de tests pour vérifier l'absence de régression.

### Étape 3.5 : Épreuve par Mutation / Faux Correctif
1. Introduire volontairement une altération dans le code (ex: inversion d'opérateur logique, valeur de timeout erronée) ou appliquer un faux correctif plausible proposé par l'IA.
2. Relancer le test : **le test doit échouer**.
3. Si le test passe malgré la mutation, l'oracle est trop lâche ou tautologique : renforcer l'assertion du test.
4. Restaurer le code propre validé.

### Étape 3.6 : Contrôles Qualité Statiques & Tri Humain des Alertes
Utiliser le modèle [`specs/templates/template-revue-qualite.md`](../specs/templates/template-revue-qualite.md) :
1. Lancer l'analyse statique (ex: Cppcheck, flake8, linter du projet).
2. Pour chaque alerte remontée, consigner une décision humaine :
   - *Anomalie confirmée :* corriger immédiatement.
   - *Faux positif :* documenter la raison technique pour laquelle l'alerte est rejetée.
   - *Déviation :* tracer la justification embarquée / bas niveau.

### Étape 3.7 : Documentation Diátaxis & Fact-Checking
Utiliser le modèle [`specs/templates/template-fact-check-doc.md`](../specs/templates/template-fact-check-doc.md) :
1. Rédiger la documentation en respectant la méthode **Diátaxis** (Tutoriel, How-To, Référence, Explication).
2. Valider la syntaxe et la cohérence des diagrammes Mermaid.
3. Remplir la **matrice de fact-checking** :
   - Pour chaque phrase affirmant un comportement technique : associer le fichier source, la ligne exacte et la commande de test vérifiant l'assertion.
   - Corriger ou supprimer toute affirmation non prouvée.

---

## 4. Critères d'acceptation de la Gate G2

- [ ] Le défaut a été reproduit avant toute modification du code.
- [ ] La preuve ROUGE est pertinente et documentée.
- [ ] Le patch est minimal (KISS, YAGNI, SRP) sans modification de code périphérique.
- [ ] La preuve VERTE est reproductible par une commande documentée.
- [ ] L'épreuve par mutation a démontré le pouvoir discriminant de la suite de tests.
- [ ] Les alertes qualité (statiques et dynamiques) ont fait l'objet d'un tri humain explicité.
- [ ] Chaque affirmation technique de la documentation est adossée à une preuve vérifiée (fact-check).
- [ ] `upstream/**` est rigoureusement intact.

---

## 5. Sortie du workflow

- Dossier de preuves complet : Fiche d'enquête (`ENQ-*`), rapport de revue (`REV-*`), documentation fact-checkée (`FACT-*`).
- Matrice de traçabilité mise à jour (statuts `Vérifié`).
- Feu vert pour engager le **Workflow 04 (Intégration & Revue Croisée)**.
