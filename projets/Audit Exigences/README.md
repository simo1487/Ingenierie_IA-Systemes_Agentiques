# Audit Exigences — Outil d'audit de qualité des exigences automobiles

## Objectif

Analyser un dataset d'exigences automobiles pour détecter les problèmes de qualité :

- **EPIC-AUD-01** — Grammaire et orthographe
  - `US-AUD-101` : grammaire (accords après modal, ponctuation, capitalisation)
  - `US-AUD-102` : orthographe (dictionnaire de fautes avec position et correction)
- **EPIC-AUD-02** — Non-duplication (`US-AUD-201`)
- **EPIC-AUD-03** — Non-contradiction (`US-AUD-301`)
- **EPIC-AUD-04** — Analyse sémantique par IA (opt-in, LLM local LM Studio)
  - `US-AUD-401` : contradictions sémantiques (ex. `disable` vs `continue`)
  - `US-AUD-402` : duplications sémantiques (paraphrases à vocabulaire disjoint)
- **EPIC-AUD-05** — Écosystème d'évaluation DeepEval (`US-AUD-501`)

L'outil produit un **rapport JSON** listant les anomalies détectées avec leur localisation et une proposition de correction. Les décisions de correction restent humaines.

## Statut

Prototype `Candidate`. Les trois EPICs sont documentés et le code source est fourni à titre de proposition. Aucune validation réglementaire n'est revendiquée.

## Processus de réalisation (TDD)

Chaque User Story suit trois phases (`task_phases` du backlog) :

1. **Spécifier et figer l'oracle** — `tests/fixtures/*_oracle.json` : attendus définis indépendamment du code
2. **Réaliser dans le périmètre autorisé** — module d'audit + tests
3. **Vérifier et soumettre à revue** — rapport dans `evidence/` + comparaison à l'oracle

## Arborescence

```text
data/                       Dataset d'exigences d'exemple (35 exigences)
src/audit_exigences/        Audits : grammar (US-101), spelling (US-102),
                            duplicates (US-201), contradictions (US-301),
                            semantic (US-401/402, opt-in)
src/audit_exigences/llm_backends/  Backends LLM : fake (tests) / lmstudio (local)
tests/                      Tests hors ligne + oracles figés (tests/fixtures/)
tests/eval/                 Écosystème DeepEval : juge LM Studio + tests goldens
docs/architecture.md        Architecture et frontières de confiance
evidence/                   Rapports générés (audit + deepeval)
SPEC.md                     Vision projet et Epics
specs/backlog.json          Source canonique du backlog
specs/epics/                Epic → User Story → Feature → Task
specs/governance/           Ambiguïtés, cycle de vie
specs/roadmap/              Ordonnancement
```

## Structure des EPICs

| EPIC | User Stories | Modules |
|------|--------------|---------|
| EPIC-AUD-01 Grammaire/Orthographe | US-AUD-101 (grammaire), US-AUD-102 (orthographe) | `grammar.py`, `spelling.py` |
| EPIC-AUD-02 Non-duplication | `US-AUD-201` | `duplicates.py` |
| EPIC-AUD-03 Non-contradiction | `US-AUD-301` | `contradictions.py` |
| EPIC-AUD-04 Analyse sémantique IA | `US-AUD-401`, `US-AUD-402` | `semantic.py`, `llm_backends/` |
| EPIC-AUD-05 Évaluation DeepEval | `US-AUD-501` | `tests/eval/` |

## Installation

Aucune dépendance externe n'est requise pour le mode déterministe (Python 3.10+). L'écosystème DeepEval nécessite `pip install -e .[eval]` et un serveur LM Studio local avec un modèle chargé.

```powershell
cd "projets\Audit Exigences"
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e .
# optionnel, pour l'évaluation DeepEval :
python -m pip install -e .[eval]
```

## Commandes

| Besoin | Commande |
|---|---|
| Audit complet | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/audit-report.json` |
| Audit grammaire seul | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/grammar-report.json --epic 1` |
| Audit duplication | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/duplicates-report.json --epic 2` |
| Audit contradiction | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/contradictions-report.json --epic 3` |
| Audit sémantique (IA, opt-in) | `python -m audit_exigences.cli --input data/exigences_sample.json --output evidence/audit-report-semantic.json --semantic` |
| Audit sémantique en mode fake (hors-ligne) | `SEMANTIC_BACKEND=fake python -m audit_exigences.cli --input ... --semantic` |
| Tests | `python -m unittest discover -s tests -v` |
| Tests DeepEval (LM Studio requis) | `python -m unittest tests.eval.test_deepeval_semantic -v` |

Variables d'environnement : `LMSTUDIO_URL` (défaut `http://localhost:1234/v1`), `LMSTUDIO_MODEL`, `SEMANTIC_BACKEND` (`lmstudio` par défaut, `fake` pour les tests hors-ligne). Les tests DeepEval sont **skippés** si LM Studio est injoignable.

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
  "run_id": "audit-20260915-144030",
  "requirements_count": 35,
  "findings_count": 14,
  "findings": [
    {"epic": "semantic", "requirement_id": "REQ-005", "type": "semantic_contradiction",
     "related_ids": ["REQ-006"], "model": "lmstudio", "detail": "..."}
  ],
  "semantic_backend": "lmstudio",
  "status": "ready-for-human-review"
}
```

## Limites et questions ouvertes

- L'audit grammaire utilise une approche lexicale simple ; il ne remplace pas une relecture humaine.
- La détection de duplication repose sur la similarité lexicale (Jaccard) ; les reformulations à vocabulaire disjoint relèvent de l'audit sémantique (EPIC-04, opt-in).
- La détection de contradiction par patterns est complétée, en mode opt-in, par l'analyse sémantique LLM ; les verdicts LLM restent des propositions.
- Le backend `fake` ne fait pas d'analyse réelle : il stub le pipeline pour les tests hors-ligne ; la qualité sémantique est évaluée par DeepEval (EPIC-05).
- Aucune correction n'est appliquée automatiquement : toutes les sorties sont des propositions.
