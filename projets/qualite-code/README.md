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

Il trouve aussi l'installation Windows standard dans `C:\Program Files\Cppcheck`, même si ce dossier manque dans `PATH`. Pour une installation ailleurs, indiquer le chemin de l'exécutable :

```powershell
./projets/qualite-code/src/run-cppcheck.ps1 -CppcheckCommand "C:\outils\Cppcheck\cppcheck.exe"
```

## Rapport MISRA C:2012

Le même script exécute l’addon MISRA de Cppcheck et écrit le rapport XML dans `projets/qualite-code/reports/cppcheck-misra.xml`. Ce rapport est généré localement et ignoré par Git.

Le code de sortie reste non nul lorsqu’une violation est trouvée. L’emplacement du rapport et l’interpréteur Python peuvent être adaptés :

```powershell
./projets/qualite-code/src/run-cppcheck.ps1 `
  -PythonCommand python `
  -ReportPath ./projets/qualite-code/reports/mon-rapport-misra.xml
```

L’addon libre ne fournit qu’une couverture partielle de MISRA C:2012 et ne constitue pas une certification de conformité.
