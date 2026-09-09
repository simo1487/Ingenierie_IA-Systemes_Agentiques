# Workflow 04 — Intégration sur develop & Revue Croisée par les Pairs

Ce workflow organise la revue formelle, la vérification des dossiers de preuves et l'intégration sécurisée des incréments d'équipe dans la branche commune `develop` (Spécification parente : [`projets/socle-commun/SPEC.md`](../projets/socle-commun/SPEC.md)).

---

## 1. Objectif du workflow

Garantir qu'aucun changement n'est intégré dans `develop` sans :
- Une synchronisation préalable avec l'état courant de `develop`.
- Une relecture croisée par une autre équipe de l'atelier.
- La vérification complète des critères d'acceptation de la Gate visée (G1 ou G2).
- La préservation rigoureuse de la traçabilité et des sources de vérité.
- L'absence formelle de conflits, fichiers temporaires, caches ou secrets.

---

## 2. Déclencheur & Entrées requises

- **Déclencheur :** Une équipe a terminé ses livrables sur sa branche dédiée (`feat/*`) et franchi sa Gate locale (G1 ou G2).
- **Entrées :**
  - Branche d'équipe à jour (`feat/GetNormes`, `feat_Cppcheck`, `feat_list_existing_projects`, `feat_getReq` ou `feat/initSearchSystem`).
  - Spécification de feature (`FEAT-*`) ou de projet (`PROJ-*`) complétée.
  - Dossier de preuves (rapports, matrices de traçabilité, fiches de reproduction).
  - État de `develop`.

---

## 3. Séquence opératoire détaillée

```text
Étape 4.1 : Resynchronisation locale avec develop
  ↓
Étape 4.2 : Vérification de propreté du dépôt (Hygiène Git)
  ↓
Étape 4.3 : Ouverture de la demande de revue croisée
  ↓
Étape 4.4 : Relecture par les pairs & Vérification des oracles
  ↓
Étape 4.5 : Décision d'intégration & Fusion dans develop
```

### Étape 4.1 : Resynchronisation locale avec develop
1. Se positionner sur la branche d'équipe :
   ```bash
   git checkout <branche-equipe>
   git fetch origin
   ```
2. Rebaser ou fusionner `develop` dans la branche de travail :
   ```bash
   git merge origin/develop
   ```
3. En cas de conflit : résoudre en concertation avec l'équipe concernée, sans supprimer de traçabilité.

### Étape 4.2 : Vérification d'hygiène Git
1. Contrôler qu'aucun artefact indésirable n'est présent :
   - Pas de fichiers `.pyc`, `__pycache__`, environnements virtuels ou `.DS_Store`.
   - Pas de rapports volumineux bruts générés (seulement les synthèses documentées).
   - Aucun fichier de configuration locale ou secret (`.env`).
2. Vérifier la conformité de syntaxe des fichiers Markdown, YAML et JSON :
   - Fichiers UTF-8 sans caractères corrompus.
   - Matrices de traçabilité conformes au schéma JSON fermé.

### Étape 4.3 : Ouverture de la demande de revue croisée
1. Préparer le récapitulatif de soumission :
   - Nom de la branche et de la spécification associée.
   - Rappel de l'objectif et des fichiers modifiés.
   - Commandes exactes pour reproduire les vérifications.
   - Statut des critères d'acceptation (`CA-*`).

### Étape 4.4 : Relecture par les pairs (Revue croisée)
Un binôme d'une autre équipe procède au contrôle indépendant :
1. **Contrôle des sources :** Chaque affirmation technique a-t-elle une source identifiable ?
2. **Contrôle des oracles :** Les tests exécutés sont-ils non tautologiques ?
3. **Contrôle du patch :** Le code modifié est-il minimal (KISS, SRP) ?
4. **Reproductibilité :** Le relecteur rejoue la commande documentée sur sa machine et constate le même résultat.
5. **Vérification d'intégrité :** `upstream/**` et les autres composants sont-ils restés inchangés ?

### Étape 4.5 : Décision d'intégration & Fusion dans develop
1. Si des corrections sont demandées : l'équipe apporte les ajustements sur sa branche.
2. Dès validation conjointe par l'équipe et le responsable de l'intégration :
   ```bash
   git checkout develop
   git merge --no-ff <branche-equipe>
   ```
3. Consigner la décision dans [`projets/socle-commun/SPEC.md`](../projets/socle-commun/SPEC.md).

---

## 4. Critères d'acceptation de l'Intégration (CA-SOCLE)

- [ ] `CA-SOCLE-01` : La mission de `travail.md` est reliée à la spécification correspondante.
- [ ] `CA-SOCLE-02` : Tous les critères d'acceptation de la feature sont cochés et justifiés.
- [ ] `CA-SOCLE-03` : La branche est parfaitement synchronisée avec `develop`.
- [ ] `CA-SOCLE-04` : Les fichiers intégrés passent les validations de syntaxe et de format.
- [ ] `CA-SOCLE-05` : Les sources et les statuts de vérification (`Observé`, `Candidat`, `Vérifié`) sont conservés.
- [ ] `CA-SOCLE-06` : Aucune revendication de conformité non démontrée n'est introduite.
- [ ] `CA-SOCLE-07` : La décision d'intégration est tracée dans l'historique Git.

---

## 5. Sortie du workflow

- Branche d'équipe intégrée dans `develop`.
- Matrice globale de traçabilité mise à jour.
- Historique Git lisible et auditable.
