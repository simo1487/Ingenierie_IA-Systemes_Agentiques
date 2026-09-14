# Fact-check documentaire du fil rouge automobile IA

## 1. Métadonnées

- **Identifiant :** `FACT-FIL-AUTO-IA-001`
- **Documents audités :** `README.md` et `docs/architecture.md`
- **Classification Diátaxis :** guide pratique pour `README.md`, explication pour `docs/architecture.md`
- **Commit source :** travail non commité sur `feat/fil-rouge-ingenierie-auto-ia`, baseline `335199ef45164d5c6f81ac97aa601ec2e87f56b4`
- **Auditeur :** assistant IA, revue humaine requise
- **Date :** `2026-09-13`

## 2. Contrôle Diátaxis

| Document | Quadrant | Objectif | Respecté ? |
|---|---|---|:---:|
| `README.md` | Guide pratique | Installer, exécuter et tester le projet | Oui |
| `docs/architecture.md` | Explication | Exposer les responsabilités et frontières de confiance | Oui |

## 3. Matrice affirmation, source et contrôle

| ID | Affirmation | Passage audité | Source canonique | Commande ou test | Statut |
|---|---|---|---|---|---|
| `AFF-FIL-01` | Le run est bloqué sans approbation humaine des baselines. | « la décision finale reste humaine » | `src/auto_ai_flow/orchestrator.py:19-26` | `test_run_is_blocked_without_human_baseline_approval` | Prouvé |
| `AFF-FIL-02` | Le retrieval retourne des citations révisées ou s’abstient. | « Citations classées ou abstention » | `src/auto_ai_flow/agents.py:40-62` | `test_rag_abstains_when_objective_has_no_matching_terms` | Prouvé |
| `AFF-FIL-03` | Une exigence générée reste une proposition sourcée. | « Exigence sourcée — Proposition » | `src/auto_ai_flow/agents.py:71-78` | `test_complete_offline_run_waits_for_human_review` | Prouvé |
| `AFF-FIL-04` | Aucun conseil qualité n’est appliqué automatiquement. | « aucun patch appliqué » | `src/auto_ai_flow/agents.py:103-112` | `test_complete_offline_run_waits_for_human_review` | Prouvé |
| `AFF-FIL-05` | Le code actuel attribue `Vérifié` lorsque les champs oracle et preuve sont non vides ; il ne démontre pas la vérité des preuves. | « Vérifié seulement avec oracle et preuve déclarés » | `src/auto_ai_flow/agents.py:118-126` | `test_traceability_is_verified_only_with_explicit_oracle_and_evidence` ne contrôle que les champs et statuts retournés ; voir `US-FIL-601` | Partiellement vrai |
| `AFF-FIL-06` | La Gate maximale du pipeline est une attente de revue humaine. | « Décision humaine obligatoire » | `src/auto_ai_flow/agents.py:132-141` | `test_complete_offline_run_waits_for_human_review` | Prouvé |
| `AFF-FIL-07` | Le mode hors ligne n’a aucune dépendance de paquet. | « Aucune dépendance n’est requise » | `pyproject.toml`, champ `dependencies = []` | `PYTHONPATH=src python3 -m unittest discover -s tests -v` | Prouvé |
| `AFF-FIL-08` | Mistral exige une clé externe et utilise une température nulle. | « utilise MISTRAL_API_KEY depuis l’environnement » | `src/auto_ai_flow/providers.py:51-76` | `test_mistral_provider_requires_an_external_secret` pour la clé ; appel distant non exécuté | Partiellement vrai |

## 4. Diagramme Mermaid

- [x] Les nœuds et transitions correspondent à l’ordre et aux dépendances de `orchestrator.py:19-41`.
- [x] Aucune transition autonome vers un statut validé n’est représentée.
- [ ] La compilation par un moteur Mermaid n’a pas été exécutée dans l’environnement ; la syntaxe reste à confirmer par l’outil documentaire retenu.

## 5. Bilan

- **Affirmations auditées :** 8
- **Prouvées localement :** 6
- **Partiellement prouvées :** 2
- **Diagrammes inspectés :** 1
- **Verdict :** publication candidate ; revue humaine et vérification Mermaid requises avant Gate G2.

L’[`audit d’alignement avec la formation`](../specs/baseline/formation-audit.md) complète ce fact-check sans ajouter de preuve métier ni modifier les décomptes ci-dessus.
