# Projet Qualité du code

- **Équipe :** Eric, Céline et Damien
- **Branche :** `feat_Cppcheck`
- **Spécification :** [SPEC.md](SPEC.md)
- **Statut :** Prototype avec fixtures de test, outils sélectionnés et profils implémentés

## Organisation du projet

- `experiments/` : comparaisons reproductibles d'outils statiques et dynamiques ;
- `src/` : scripts maintenus du contrôle qualité ;
- `tests/` : cas de succès, défaut connu et outil absent ;
- `docs/` : installation et utilisation ;
- `evidence/` : synthèses de résultats et décisions de revue.

## Commandes disponibles

### Profil rapide (< 30 secondes)

Analyse statique avec Cppcheck (et Clang-tidy si disponible) :

```powershell
./projets/qualite-code/src/run-profile-rapide.ps1
```

- **Outils** : Cppcheck (+ Clang-tidy optionnel)
- **Cible** : `tests/fixtures/` par défaut
- **Code retour** : 0 (succès), 1 (défaut détecté), 127 (outil absent), 2 (aucun fichier)

### Profil complet (< 5 minutes)

Analyse statique et dynamique complète :

```powershell
./projets/qualite-code/src/run-profile-complet.ps1
```

- **Outils** : Cppcheck + Clang-tidy + AddressSanitizer + LeakSanitizer
- **Cible** : `tests/fixtures/` par défaut
- **Code retour** : 0 (succès), 1 (défaut détecté), 127 (outil absent), 2 (aucun fichier)

### Cppcheck seul (commande historique)

```powershell
./projets/qualite-code/src/run-cppcheck.ps1 -SourceDirectory "chemin/vers/sources"
```

## Outils sélectionnés

### Outils statiques
- **Cppcheck** : Analyse statique légère et rapide
- **Clang-tidy** : Analyse approfondie (optionnel)

### Outils dynamiques
- **AddressSanitizer (ASan)** : Détection d'erreurs mémoire (buffer overflow, use-after-free)
- **LeakSanitizer (LSan)** : Détection de fuites de mémoire

## Documentation détaillée

- [Matrice de comparaison des outils](experiments/matrice-comparaison.md)
- [Justification de la sélection](evidence/selection-outils.md)
- [Fiche de cible](evidence/fiche-cible.md)
- [Guide d'installation](docs/installation.md)
- [Guide d'utilisation](docs/utilisation.md)
- [Limites et exclusions](docs/limites.md)

## Critères d'acceptation

- [x] CA-QUAL-01 : Cible, révision, langages et commandes définis
- [x] CA-QUAL-02 : Au moins 2 outils statiques et 2 approches dynamiques comparés
- [x] CA-QUAL-03 : Choix des outils justifié par des observations
- [x] CA-QUAL-04 : Profil rapide exécutable avec commande documentée
- [ ] CA-QUAL-05 : Défaut contrôlé produit code non nul et diagnostic localisable
- [x] CA-QUAL-06 : Absence d'outil produit échec visible
- [ ] CA-QUAL-07 : Autre personne peut reproduire les contrôles
- [ ] CA-QUAL-08 : Limites, exclusions, faux positifs listés
