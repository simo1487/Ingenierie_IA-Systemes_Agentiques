# Modèle de Carnet d'Enquête et Fiche de Reproduction

Ce document formalise la démarche d’enquête scientifique falsifiable et la reproduction d’un défaut avant toute tentative de correction (livrable central de la Gate G2).

---

## 1. Informations générales

- **Identifiant :** `ENQ-[DOMAINE]-[NUMÉRO]` (ex: `ENQ-SEM-001`)
- **Titre de l'enquête :** [Description courte du symptôme ou comportement inattendu]
- **Enquêteur(s) :** [Noms des ingénieurs]
- **Date :** `AAAA-MM-JJ`
- **Composant affecté :** [ex: `kernel/sem.c`, script Python, pipeline CI]
- **Baseline / Commit testé :** [Hash exact du commit ou tag]
- **Statut :** `En cours` / `Défaut reproduit (ROUGE)` / `Corrigé (VERT)` / `Clos`

---

## 2. Démarche scientifique : Observation vs Hypothèses

### 2.1 Observation brute (Faits constatés sans interprétation)
> **Fait constaté :** Lors de l'exécution de `[commande]` avec `[paramètres]`, le système retourne `[code retour / log brut]` au lieu du comportement attendu `[comportement attendu]`.  
> *Rappel : Ne pas introduire d'explication théorique dans l'observation.*

### 2.2 Hypothèses explicatives concurrentes
- **Hypothèse H1 :** [Première explication causale possible]
- **Hypothèse H2 :** [Seconde explication causale alternative]
- **Hypothèse H3 (optionnelle) :** [Problème d'environnement ou de dépendance]

### 2.3 Expérience discriminante (Test discriminant)
- **Expérience conçue :** [Quel test ou modification contrôlée permet de falsifier H1 ou H2 ?]
- **Oracle discriminant :**
  - Si le résultat est `[X]`, alors H1 est réfutée.
  - Si le résultat est `[Y]`, alors H2 est réfutée.
- **Résultat de l'expérience :** [Hypothèse retenue et justification]

---

## 3. Fiche de reproduction rigoureuse

### 3.1 Environnement et pré-requis
- Système d'exploitation : [ex: macOS 14.5 / Ubuntu 22.04]
- Compilateur / Runtime : [ex: GCC 12.2 / Python 3.11.8]
- Dépendances : [Versions exactes installées]

### 3.2 Procédure de reproduction pas-à-pas
1. Cloner ou se positionner sur le commit : `git checkout [hash]`
2. Exécuter la commande :
   ```bash
   [commande exacte reproductible]
   ```
3. **Résultat obtenu (Échec constaté) :**
   ```text
   [Extrait pertinent du journal d'erreur ou code retour non nul]
   ```
4. **Résultat attendu :**
   ```text
   [Code retour 0 ou sortie conforme à la spécification]
   ```

---

## 4. Preuve ROUGE (Avant modification)

- **Test unitaire / d'intégration discriminant :** `[chemin/vers/test]`
- **Statut du test avant patch :** **ÉCHEC (ROUGE)**
- **Trace d'exécution archivée :**
  ```text
  [Trace du test montrant que le test échoue pour la bonne raison]
  ```

---

## 5. Correctif Minimal (Patch KISS / YAGNI / SRP)

Le correctif doit être strictement borné au défaut démontré, sans refactorisation opportune ni code inutile.

- **Fichiers modifiés :** `[liste des fichiers]`
- **Diff unifié minimal :**
  ```diff
  --- a/[fichier]
  +++ b/[fichier]
  @@ ... @@
  - [ancien code]
  + [nouveau code minimal]
  ```

---

## 6. Preuve VERTE (Après modification)

- **Commande de rejeu :** `[commande exacte]`
- **Statut du test :** **SUCCÈS (VERT)**
- **Contrôle de non-régression :** [Exécution de la suite complète de tests]

---

## 7. Épreuve par Mutation / Faux Correctif

Pour prouver que le test n'est pas tautologique et possède un réel pouvoir discriminant :

1. **Mutation introduite intentionnellement :** [ex: inverser une condition `>` en `>=`, ou supprimer une ligne du patch]
2. **Exécution du test muté :**
   - Le test doit **ÉCHOUER**.
   - Si le test passe malgré la mutation, l'oracle est insuffisant ou tautologique.
3. **Résultat :** [Mutation détectée avec succès / Test robuste validé]
4. **Restauration :** [Code muté remis à l'état propre vérifié]

---

## 8. Revue et validation humaine

- [ ] Le défaut est reproduit avant toute modification du code.
- [ ] L'oracle est indépendant et ne provient pas du code généré.
- [ ] Le patch est minimal (respecte KISS, YAGNI, SRP).
- [ ] Le test est sensible à une mutation (non tautologique).
- [ ] Aucun artefact upstream n'a été corrompu.
- **Décision finale :** `Validé pour Gate G2` par `[Nom du relecteur]` le `AAAA-MM-JJ`.
