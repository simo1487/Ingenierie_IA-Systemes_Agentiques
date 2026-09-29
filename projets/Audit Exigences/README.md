# Audit Exigences — Outil d'audit de qualité des exigences automobiles

## Objectif

Analyser un dataset d'exigences automobiles pour détecter les problèmes de qualité :

- **Grammaire et orthographe** (EPIC-AUD-01)
- **Non-duplication** (EPIC-AUD-02)
- **Non-contradiction** (EPIC 3)

L'outil produit un **rapport JSON** listant les anomalies détectées avec leur localisation et une proposition de correction. Les décisions de correction restent humaines.

## Statut

Prototype `Candidate`. Les trois EPICs sont documentés et le code source est fourni à titre de proposition. Aucune validation réglementaire n'est revendiquée.

## Arborescence

```text
data/                       Dataset d'exigences d'exemple
src/audit_exigences/        Audits grammaire, duplication, contradiction
tests/                      Tests hors ligne
docs/architecture.md        Architecture et frontières de confiance
evidence/                   Rapports générés
SPEC.md                     Vision projet et Epics
specs/backlog.json          Source canonique du backlog
specs/epics/                Epic → User Story → Feature → Task
specs/governance/           Ambiguïtés, cycle de vie, contrats de mesure
specs/roadmap/              Ordonnancement
```

## Installation

Aucune dépendance externe n'est requise pour le mode déterministe (Python 3.10+).

```powershell
cd "projets\Audit Exigences"
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e .
```

## Commandes

| Besoin | Commande |
|---|---|
| Audit complet | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/audit-report.json` |
| Audit grammaire seul | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/grammar-report.json --epic 1` |
| Audit duplication | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/duplicates-report.json --epic 2` |
| Audit contradiction | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/contradictions-report.json --epic 3` |
| Tests | `python -m unittest discover -s tests -v` |

## Entrées et sorties

**Entrée** : dataset JSON ou Markdown d'exigences avec `id`, `text`, `source`, `version`.

```json
{
  "exigences": [
    {
      "id": "REQ-001",
      "text": "Le système doit démarrer en moins de 2 secondes.",
      "source": "spec_v1.md",
      "version": "1.0"
    }
  ]
}
```

**Sortie** : rapport JSON avec les anomalies détectées par EPIC.

```json
{
  "run_id": "audit-2026-09-13-001",
  "epics": {
    "grammar": {"findings": [...]},
    "duplicates": {"findings": [...]},
    "contradictions": {"findings": [...]}
  },
  "status": "ready-for-human-review"
}
```

## Limites et questions ouvertes

- L'audit grammaire utilise une approche lexicale simple ; il ne remplace pas une relecture humaine.
- La détection de duplication repose sur la similarité lexicale (Jaccard/TF-IDF) ; deux exigences reformulées avec des mots différents ne sont pas détectées.
- La détection de contradiction est basée sur des patterns (négations, valeurs numériques) ; les contradictions sémantiques complexes nécessitent un modèle.
- Aucune correction n'est appliquée automatiquement : toutes les sorties sont des propositions.
