# Workflow 02 — Spécifications, Example Mapping, Oracles & Traçabilité v0 (Gate G1)

Ce workflow transforme une User Story ou une exigence brute issue d’une baseline figée en spécification outillée, exemples concrets, scénarios Gherkin falsifiables et matrice de traçabilité v0 en lecture seule.

---

## 1. Objectif du workflow

Passer d'un texte d'exigence (souvent au statut `Draft` ou ambigu) à :
- Un registre d'ambiguïtés et de décisions explicites.
- Un ensemble de règles métier et d'exemples concrets (Example Mapping).
- Une table de décision pour les cas combinatoires.
- Des scénarios Gherkin couvrant nominaux, frontières, erreurs, timeouts et interruptions.
- Des **oracles indépendants** définis impérativement avant tout code (anti-tautologie).
- Une matrice de traçabilité v0 reliant exigences, documentation, code et tests, validée par schéma JSON fermé.

---

## 2. Déclencheur & Entrées requises

- **Déclencheur :** Gate G0 franchie pour le projet ou lot concerné.
- **Entrées :**
  - Fiche de cadrage G0 validée.
  - Corpus d'exigences brutes (ex: fichiers `.sdoc` de StrictDoc ou catalogue normalisé).
  - Documentation d’architecture et contrats d’API de la baseline cible.
  - Code source et tests existants en consultation lecture seule.

---

## 3. Séquence opératoire détaillée

```text
Étape 2.1 : Audit qualité de l'exigence & Détection d'ambiguïtés
  ↓
Étape 2.2 : Atelier Example Mapping & Table de décision
  ↓
Étape 2.3 : Rédaction des scénarios Gherkin & Oracles indépendants
  ↓
Étape 2.4 : Conception de la mutation conceptuelle (Test discriminant)
  ↓
Étape 2.5 : Construction de la matrice de traçabilité v0 (JSON fermé)
  ↓
Étape 2.6 : Revue croisée et validation de la Gate G1
```

### Étape 2.1 : Audit qualité de l'exigence
1. Lire l'énoncé brut dans la baseline source (ex: `upstream/reqmgmt-...`).
2. Auditer selon la grille qualité :
   - **Singularité :** L'exigence ne traite-t-elle qu'un seul comportement ?
   - **Clarté :** Les termes ambigus sont-ils proscrits ?
   - **Vérifiabilité :** Un test observable peut-il contredire une mauvaise implémentation ?
   - **Statut de l'exigence :** Noter le statut source (`Draft`, `Approved`).
3. Si une ambiguïté ou une information manquante est constatée :
   - L'inscrire immédiatement dans le **Registre d'ambiguïtés**.
   - **Règle :** Ne jamais laisser l'IA « combler » l'ambiguïté sans décision humaine consignée.

### Étape 2.2 : Atelier Example Mapping & Table de décision
Utiliser le modèle [`specs/templates/template-example-mapping.md`](../specs/templates/template-example-mapping.md) :
1. Extraire la **Règle métier** principale.
2. Formuler au moins un **Exemple nominal** concret (données réelles, état attendu).
3. Formuler au moins un **Exemple aux limites (frontière)** (valeur 0, max, ressource saturée).
4. Formuler au moins un **Contre-exemple (erreur / refus)** (paramètre invalide, mauvais contexte d'appel).
5. Si plusieurs conditions booléennes s'entrecroisent, formaliser la **Table de décision**.
6. Lister les questions ouvertes restantes.

### Étape 2.3 : Rédaction des Scénarios Gherkin & Oracles Indépendants
1. Rédiger la spécification de feature selon le modèle [`specs/templates/template-feature-spec.md`](../specs/templates/template-feature-spec.md).
2. Traduire les exemples en syntaxe Gherkin :
   - Cas nominaux
   - Cas aux limites
   - Cas d'erreur et refus
   - Cas temporels, timeouts, reset et concurrence / ISR (si applicable)
3. **Définition impérative de l'oracle indépendant :**
   - L'oracle doit provenir de la spécification externe et non du comportement observé du code.
   - **Contrôle anti-tautologie :** Vérifier que le test ne teste pas simplement que « le code fait ce qu'il est écrit pour faire », mais qu'il vérifie la conformité à l'attendu fonctionnel.

### Étape 2.4 : Conception de la mutation conceptuelle
1. Anticiper un bogue plausible ou un faux correctif : quelle modification subtile dans le code ferait diverger le comportement ?
2. Vérifier par avance que le scénario Gherkin et son oracle détecteraient cette divergence.

### Étape 2.5 : Construction de la matrice de traçabilité v0
Utiliser le modèle [`specs/templates/template-matrice-tracabilite.md`](../specs/templates/template-matrice-tracabilite.md) :
1. Relier : `UID Exigence` ↔ `Source sdoc:ligne` ↔ `API publique` ↔ `Code source fichier:ligne` ↔ `Test fichier:fonction`.
2. Attribuer le statut officiel : `Observé`, `Candidat`, `Vérifié`, `Non vérifié` ou `Bloqué`.
3. **Avertissement :** Ne jamais attribuer `Vérifié` sans exécution de test réelle.
4. Exporter la matrice au format JSON fermé pour contrôle d'intégrité.

---

## 4. Critères d'acceptation de la Gate G1

- [ ] Chaque exigence est rattachée à sa baseline d'origine avec son statut explicite (`Draft` documenté).
- [ ] Les ambiguïtés sont consignées dans un registre sans complétion artificielle par l'IA.
- [ ] L'Example Mapping a produit cas nominaux, frontières et contre-exemples d'erreur.
- [ ] Les oracles indépendants sont documentés avant toute exécution de code.
- [ ] Aucun test tautologique n'est présent.
- [ ] Le travail a respecté la lecture seule stricte sur `upstream/**`.
- [ ] La matrice de traçabilité v0 est conforme au schéma JSON fermé et validée par une relecture croisée.

---

## 5. Sortie du workflow

- Spécification de feature (`FEAT-*`) validée pour G1.
- Matrice de traçabilité v0 (`TRAC-*`) enregistrée sous `specs/matrices/`.
- Feu vert pour engager le **Workflow 03 (Preuves, Red-Green, Mutation & Documentation)**.
