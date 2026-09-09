# Plan concret de migration des dossiers existants

## Principe

La migration réorganise les chemins sans modifier le contenu fonctionnel. Elle doit être faite après synchronisation des branches, dans une pull request dédiée, avec `git mv` pour conserver un historique lisible.

## État cible

```text
projets/
├── normes/
│   ├── README.md
│   ├── SPEC.md
│   ├── experiments/
│   │   └── initialisation-recherche/
│   │       └── SPEC.md
│   ├── src/
│   │   └── telecharger_sources.py
│   ├── tests/
│   ├── docs/
│   │   └── rapport-organisation.md
│   ├── data/
│   │   ├── catalogue/
│   │   │   ├── normes.yml
│   │   │   └── sources.csv
│   │   └── sources-originales/
│   │       ├── automotive-spice.pdf
│   │       ├── iec-61508.html
│   │       ├── iso-15765.html
│   │       ├── iso-pas-5112.html
│   │       ├── iso-sae-21434.html
│   │       └── sae-j3061.html
│   └── evidence/
│       └── manifest.json
├── qualite-code/
├── logiciel-automobile-open-source/
│   └── docs/
│       └── etat-de-art-zephyr.md
├── exigences-zephyr/
└── socle-commun/

specs/
├── examples/
│   └── FEAT-QUAL-001.md
└── templates/
```

Les dossiers `src/`, `tests/`, `docs/`, `data/`, `evidence/` et `experiments/` ne sont créés que lorsqu’ils reçoivent un fichier réel.

## Correspondance exacte des éléments actuels

| Élément actuel | Cible | Motif |
|---|---|---|
| `normes-software-embarque-automobile/README.md` | fusion manuelle dans `projets/normes/README.md` | Il existe déjà un point d’entrée projet ; éviter deux README concurrents |
| `normes-software-embarque-automobile/telecharger_sources.py` | `projets/normes/src/telecharger_sources.py` | Code Python maintenu du projet Normes |
| `normes-software-embarque-automobile/normes.yml` | `projets/normes/data/catalogue/normes.yml` | Donnée structurée du catalogue |
| `normes-software-embarque-automobile/sources.csv` | `projets/normes/data/catalogue/sources.csv` | Registre machine-readable des sources |
| `normes-software-embarque-automobile/rapport-organisation.md` | `projets/normes/docs/rapport-organisation.md` | Documentation et synthèse du projet |
| `normes-software-embarque-automobile/sources-downloads/*.pdf` | `projets/normes/data/sources-originales/` | Source originale collectée, à conserver avec sa licence et son statut d’accès |
| `normes-software-embarque-automobile/sources-downloads/*.html` | `projets/normes/data/sources-originales/` | Captures de sources originales, pas du code ni une preuve de conformité |
| `normes-software-embarque-automobile/sources-downloads/manifest.json` | `projets/normes/evidence/manifest.json` | Trace horodatée des tentatives de récupération |
| `projets/normes/initialisation-recherche/SPEC.md` | `projets/normes/experiments/initialisation-recherche/SPEC.md` | Prototype préparatoire rattaché au projet parent |
| `Zephyr state of art/README.md` | `projets/logiciel-automobile-open-source/docs/etat-de-art-zephyr.md` | Travail documentaire du projet de recherche open source |
| `template-feature-spec.md` | `specs/examples/FEAT-QUAL-001.md` | Le fichier est un exemple instancié, pas le template canonique |
| `travail.md` | reste à la racine | Point d’entrée court vers les équipes et branches |
| `specs/` | reste à la racine | Méthode et modèles partagés par tous les projets |
| `workflows/` | reste à la racine | Processus communs G0, G1, G2 et intégration |
| `.devin/`, `.githooks/`, `tools/` | restent à la racine | Configuration et outils transverses du monorepo |

## Ordre conseillé des migrations

### Migration 1 — Socle documentaire

Déplacer uniquement l’exemple de spécification :

```bash
mkdir -p specs/examples
git mv template-feature-spec.md specs/examples/FEAT-QUAL-001.md
```

Mettre ensuite à jour les liens, lancer `make check`, puis faire relire cette migration seule.

### Migration 2 — État de l’art Zephyr

```bash
mkdir -p projets/logiciel-automobile-open-source/docs
git mv "Zephyr state of art/README.md" \
  projets/logiciel-automobile-open-source/docs/etat-de-art-zephyr.md
rmdir "Zephyr state of art"
```

Cette migration appartient à l’équipe `feat_list_existing_projects` et ne doit pas introduire de nouvelle analyse en même temps.

### Migration 3 — Prototype d’initialisation Normes

```bash
mkdir -p projets/normes/experiments/initialisation-recherche
git mv projets/normes/initialisation-recherche/SPEC.md \
  projets/normes/experiments/initialisation-recherche/SPEC.md
rmdir projets/normes/initialisation-recherche
```

À réaliser après accord entre `feat/initSearchSystem` et `feat/GetNormes`.

### Migration 4 — Implémentation du projet Normes

Créer d’abord les destinations :

```bash
mkdir -p projets/normes/src \
  projets/normes/docs \
  projets/normes/data/catalogue \
  projets/normes/data/sources-originales \
  projets/normes/evidence
```

Déplacer ensuite chaque catégorie :

```bash
git mv normes-software-embarque-automobile/telecharger_sources.py \
  projets/normes/src/telecharger_sources.py
git mv normes-software-embarque-automobile/normes.yml \
  projets/normes/data/catalogue/normes.yml
git mv normes-software-embarque-automobile/sources.csv \
  projets/normes/data/catalogue/sources.csv
git mv normes-software-embarque-automobile/rapport-organisation.md \
  projets/normes/docs/rapport-organisation.md
git mv normes-software-embarque-automobile/sources-downloads/manifest.json \
  projets/normes/evidence/manifest.json
git mv normes-software-embarque-automobile/sources-downloads/* \
  projets/normes/data/sources-originales/
```

Le déplacement du manifeste doit précéder le wildcard. Le script devra ensuite utiliser par défaut `../data/catalogue/sources.csv`, `../data/sources-originales/` et `../evidence/manifest.json`. Cette adaptation doit être un petit commit séparé du déplacement pur afin que la revue distingue changement de chemin et changement fonctionnel.

Le contenu utile du README historique est fusionné dans `projets/normes/README.md`, puis l’ancien dossier vide est supprimé. Aucun document source ne doit être renommé ou réécrit pendant cette étape.

## Coordination avec les branches

1. Fusionner d’abord la structure commune dans `develop`.
2. Demander à chaque équipe de synchroniser sa branche avec `develop`.
3. Réaliser chaque migration sur la branche propriétaire du projet.
4. Ne pas migrer deux projets dans la même pull request.
5. Après chaque migration : corriger les chemins, exécuter les tests locaux, exécuter `make check`, puis faire une revue croisée.

## Ce qui ne doit pas être fait

- déplacer tous les dossiers en une seule fois ;
- mélanger déplacement, refactorisation et nouvelle fonctionnalité ;
- créer des dossiers vides « pour plus tard » ;
- déplacer des sources sans conserver leur manifeste, leur licence et leur provenance ;
- réécrire l’historique Git ou forcer une branche partagée.
