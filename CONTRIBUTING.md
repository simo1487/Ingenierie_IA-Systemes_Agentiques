# Contribuer au monorepo

## Parcours minimal

1. Identifier la mission et la branche dans [travail.md](travail.md).
2. Lire le `README.md` et le `SPEC.md` du projet concerné.
3. Distinguer l’expérimentation du code maintenu.
4. Définir les critères et oracles avant l’implémentation.
5. Modifier uniquement le périmètre du projet concerné.
6. Exécuter ses tests locaux puis `make check`.
7. Soumettre les commandes et preuves nécessaires à une revue indépendante.

## Créer une expérimentation

Créer `projets/<slug>/experiments/<AAAA-MM-JJ>-<sujet>/README.md` avec :

- l’hypothèse testée ;
- la baseline et les entrées ;
- le protocole et la commande exacte ;
- le résultat observé ;
- les limites ;
- la décision : abandon, nouvel essai ou promotion vers `src/`.

Une expérimentation peut être incomplète, mais elle ne doit pas présenter une proposition comme une preuve.

## Promouvoir une expérience en code maintenu

Avant de déplacer une solution vers `src/` :

- rédiger ou mettre à jour la spécification ;
- associer des tests reproductibles dans `tests/` ;
- conserver seulement les dépendances nécessaires ;
- documenter les commandes dans le `README.md` local ;
- relier les preuves à la révision testée.

## Contrôles Git locaux

Installer une fois les hooks partagés :

```bash
make setup-hooks
```

Vérifier tous les fichiers suivis et nouveaux avant une revue :

```bash
make check
```

Le hook `pre-commit` vérifie uniquement les fichiers indexés et reste volontairement rapide. Il contrôle l’hygiène commune et quelques syntaxes sans installer de dépendance. Les tests métier, compilations C/C++, suites Python ou builds JavaScript sont exécutés avec les commandes documentées par chaque projet.

Contournement exceptionnel du hook :

```bash
git commit --no-verify
```

Ce contournement doit être signalé dans la revue ; il ne transforme pas des contrôles non exécutés en succès.

## Ajouter un langage ou un outil

Ne pas étendre le hook racine avec une dépendance lourde propre à un seul projet. Ajouter la configuration dans `projets/<slug>/`, documenter une commande rapide et une commande complète dans son `README.md`, puis proposer un contrôle racine seulement s’il est utile à plusieurs projets.
