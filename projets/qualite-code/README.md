# Projet Qualité du code

- **Équipe :** Eric, Céline et Damien
- **Branche :** `feat_Cppcheck`
- **Spécification :** [SPEC.md](SPEC.md)
- **Statut :** outils, cible et commandes encore à sélectionner

## Organisation future

- `experiments/` : comparaisons reproductibles d’outils statiques et dynamiques ;
- `src/` : scripts maintenus du contrôle qualité ;
- `tests/` : cas de succès, défaut connu et outil absent ;
- `docs/` : installation et utilisation ;
- `evidence/` : synthèses de résultats et décisions de revue.

Les commandes rapides et complètes seront documentées ici dès que la cible et les outils auront été validés conformément à `CA-QUAL-01` à `CA-QUAL-08`.

## Lancer Cppcheck

Depuis la racine du dépôt, lancer :

```powershell
./projets/qualite-code/src/run-cppcheck.ps1
```

Le script analyse récursivement les fichiers `.c`, `.cc`, `.cpp` et `.cxx` du répertoire `src/`. Il retourne le code de Cppcheck (`1` lorsqu'un diagnostic est trouvé), `127` si Cppcheck est indisponible et `2` lorsqu'aucun fichier applicable n'est trouvé.
