# Fil rouge — Ingénierie automobile assistée par IA

## Objectif

Relier dans un même produit pédagogique les baselines normatives, la recherche de projets open source, l’ingénierie des exigences, le RAG, l’analyse qualité et la traçabilité. Les agents produisent des observations ou propositions ; la sélection d’une baseline, la validation d’une exigence, l’application d’un correctif et le franchissement d’une Gate restent humains.

## Équipe et branche

- **Fonction :** intégration fil rouge
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Baseline de départ :** `develop` au commit `335199ef45164d5c6f81ac97aa601ec2e87f56b4`

## Statut

Prototype `Candidate`. Le mode hors ligne est exécutable sans secret ni réseau. Le connecteur Mistral est optionnel et ses sorties restent des propositions. Le backlog de production est documentaire : toutes ses Stories, Features et tâches restent candidates et à faire.

## Arborescence réelle

```text
data/                       Manifeste de démonstration et fixtures
src/auto_ai_flow/           Orchestrateur, agents, statuts et fournisseurs IA
tests/                      Tests hors ligne et intégrité structurelle des specs
tools/render_specs.py        Rendu déterministe de la hiérarchie documentaire
docs/architecture.md        Architecture actuelle et frontières de confiance
evidence/                   Rapports et sorties antérieurs
SPEC.md                     Vision projet et navigation vers les Epics
specs/backlog.json           Source canonique du backlog
specs/formation-alignment.json Registre d’alignement pédagogique candidat
specs/baseline/              Snapshot MVP, état actuel, sources et audit de formation
specs/epics/                 Epic → User Story → Feature → Task
specs/governance/            Ambiguïtés, cycle de vie et contrats de mesure
specs/roadmap/               Ordonnancement du socle et des extensions
```

## Lire le backlog

- **Produit :** [`SPEC.md`](SPEC.md), puis [`specs/roadmap/README.md`](specs/roadmap/README.md).
- **Réalisation :** [`specs/README.md`](specs/README.md), puis une User Story, sa Feature et ses tâches selon le découpage canonique.
- **Revue :** [`specs/baseline/formation-audit.md`](specs/baseline/formation-audit.md), [`specs/governance/lifecycle.md`](specs/governance/lifecycle.md), [`specs/governance/ambiguities.md`](specs/governance/ambiguities.md) et [`specs/baseline/current-state.md`](specs/baseline/current-state.md).

## Installation

Aucune dépendance n’est requise pour le mode déterministe. Depuis ce dossier :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Une installation éditable est facultative :

```bash
python -m pip install -e .
```

## Commandes

| Besoin | Commande |
|---|---|
| Tests hors ligne | `PYTHONPATH=src python -m unittest discover -s tests -v` |
| Structure des spécifications | `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_specs.py' -v` |
| Vérifier le rendu documentaire | `PYTHONDONTWRITEBYTECODE=1 python3 tools/render_specs.py --check` |
| Régénérer les pages gérées | `PYTHONDONTWRITEBYTECODE=1 python3 tools/render_specs.py --write` |
| Tests hors ligne et specs sans bytecode | `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` |
| Démonstration hors ligne | `PYTHONPATH=src python -m auto_ai_flow.cli --input data/demo_baseline.json --output evidence/demo-run.json` |
| Démonstration Mistral | `MISTRAL_API_KEY=... PYTHONPATH=src python -m auto_ai_flow.cli --provider mistral --input data/demo_baseline.json --output evidence/mistral-run.json` |
| Contrôle du monorepo | Depuis la racine : `make check` |

`tests/test_specs.py` vérifie la structure, les relations et le miroir Markdown. Il ne valide ni le sens métier des critères, ni leur implémentation, ni leur acceptation.

## Entrées et baselines

Le manifeste actuel exige `run_id`, `objective`, `baselines` et `human_approvals`. Les candidats open source, diagnostics qualité et liens explicites sont des entrées complémentaires ; la validation complète des baselines est à renforcer dans [`US-FIL-101`](specs/epics/EPIC-FIL-01/user-stories/US-FIL-101.md). `data/demo_baseline.json` est une fixture fictive, ni une norme ni une preuve de conformité.

## Sorties et preuves

Chaque agent retourne un statut formel, une charge utile, ses sources et ses questions ouvertes. Le rapport final s’arrête à `ready-for-human-review`; aucun fournisseur IA ne peut produire seul un statut de validation finale. Le libellé actuel `Vérifié` de la traçabilité ne contrôle que la présence de champs non vides ; voir [`US-FIL-601`](specs/epics/EPIC-FIL-06/user-stories/US-FIL-601.md).

## Limites et questions ouvertes

- Aucun appel Mistral réel n’a été vérifié dans ce lot ; les tests utilisent le mode hors ligne et le refus sans clé.
- La première version utilise un retrieval lexical déterministe comme double de test, pas comme mesure de performance sémantique.
- Les adaptateurs Qdrant, Cppcheck/MISRA et recherche web restent à intégrer après sélection humaine des apports de branches.
- Le projet automobile open source réel et sa révision ne sont pas encore approuvés.
- Le [registre d’ambiguïtés](specs/governance/ambiguities.md) conserve les décisions manquantes sans inventer de valeurs.
