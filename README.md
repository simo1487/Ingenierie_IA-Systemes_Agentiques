# Ingénierie IA & Systèmes Agentiques — Portfolio

> Projet de formation réalisé dans le cadre de **« Ingénierie IA & Systèmes Agentiques : de l'Ingénieur Augmenté à la Mise en Production »** (Digital League, Sophia Antipolis).
> Profil : **ingénieur logiciel embarqué** — application de la rigueur du monde automotive (exigences, traçabilité, tests, revues) à l'ingénierie augmentée par IA.

Ce monorepo regroupe mes contributions personnelles sur un socle de formation collaboratif : un **outil d'audit qualité d'exigences** (déterministe + IA), un **agent RAG** de question-réponse documentaire, et des **ateliers RAG** complets (chunking, indexation vectorielle, retrieval avec citations).

---

## 🔍 Projet phare — Audit Exigences (`projets/Audit Exigences/`)

Outil d'audit automatique de datasets d'exigences automobiles : détecte fautes d'orthographe, erreurs de grammaire, exigences dupliquées et contradictoires. Chaque anomalie est une **proposition soumise à revue humaine** — jamais de décision automatique.

### Audit déterministe (reproductible, hors-ligne)

- **Grammaire / orthographe** : règles et dictionnaire de fautes avec position exacte et suggestion (`shall logs` → `shall log`)
- **Duplication** : similarité de Jaccard sur tokens normalisés — stemming léger, unification `startup`/`start-up`, `°C`/`degC`, `percent`/`%`
- **Contradiction** : négations opposées (`shall reset` / `shall never reset`, `authenticate` / `without authentication`) et conflits numériques sur grandeur commune (400 A vs 450 A)

### Analyse sémantique par LLM local (opt-in)

- Backend **LM Studio** (`localhost:1234/v1`, API OpenAI-compatible, `Llama-3.2-3B-Instruct` quantifié) — aucune clé API, aucune donnée externe
- Pré-filtre déterministe des paires candidates → verdict JSON structuré `contradiction` / `duplicate` / `ok` + rationale
- Détecte ce que les patterns ne voient pas : `disable` vs `continue` torque, `erase` vs `retain` DTCs, conversion d'unités (2 Mbps vs 500 kbps)

### Écosystème d'évaluation DeepEval

- **Oracles/goldens figés avant le code** (`tests/fixtures/*_oracle.json`) — tests de conformité anti-tautologie incluant les non-détections attendues
- Juge LLM local via `DeepEvalBaseLLM` custom — métriques `JsonCorrectnessMetric` + `GEval`
- Rapport versionné (`evidence/deepeval-report.json`) : les limites réelles du modèle 3B (faux positifs sur contrôles négatifs) sont **mesurées et documentées**, pas masquées
- Suite complète hors-ligne : **46 tests** (backend `fake` déterministe, éval skippée proprement si LM Studio absent)

---

## 🤖 Agent RAG documentaire (`exercices/AI_Agent/`)

Agent de question-réponse sur documentation technique (datasheet Kendryte K230, doc kernel Zephyr).

- **Pipeline** : loader → parser (Markdown/HTML via BeautifulSoup) → chunker → embeddings → base vectorielle → retriever → LLM → réponse structurée avec **citations**
- **Stack** : LangChain, ChromaDB, Mistral Embeddings + Mistral LLM
- **Abstention contrôlée** par seuil de similarité — l'agent refuse de répondre plutôt que d'halluciner
- **Backends interchangeables** : `fake` (déterministe, tests hors-ligne) / API — pattern réutilisé dans Audit Exigences
- **Évaluation mesurée** : jeux de 30 questions-oracle par corpus, rapports dans `rapport/` (K230, Zephyr)

## 📚 Ateliers RAG (`exercices/rag/`)

- **5 techniques de chunking comparées** : fixe avec overlap, fenêtre de phrases, hiérarchique parent-enfant, sémantique, structurel Markdown/code
- **Base vectorielle Qdrant** : modes mémoire / disque / Docker (`docker-compose`)
- **Embeddings HuggingFace** `BAAI/bge-small-en-v1.5` (local, sans API)
- Pipeline ingestion/retrieval avec filtres de métadonnées et citations sourcées
- Agent examinateur ASPICE (interfaces console + Gradio)

---

## 🛠️ Méthode d'ingénierie (le « comment »)

| Pratique | Mise en œuvre |
|----------|---------------|
| **Spécification structurée** | Découpage `EPIC → User Story → Feature → Task` versionné (`specs/`), backlog JSON canonique |
| **Oracles indépendants** | Attendus figés *avant* le code — pas de test qui recopie la logique interne |
| **TDD** | Rouge pertinent → patch minimal (KISS/SRP) → vert → contrôle par mutation conceptuelle |
| **Gates de revue** | Workflows G0/G1/G2 (`workflows/`), critères de franchissement audités, dossier de preuves |
| **Traçabilité** | Exigence → règle métier → critère d'acceptation Gherkin → oracle → code → test |
| **Registre d'ambiguïtés** | Les inconnues restent explicites jusqu'à décision humaine — l'IA n'invente jamais |
| **Séparation des statuts** | Proposition / observation / preuve vérifiée / question ouverte distingués partout |

## Stack technique

`Python` · `LangChain` · `LlamaIndex` · `ChromaDB` · `Qdrant` · `Mistral AI` · `LM Studio / Llama 3.2` · `DeepEval` · `HuggingFace` · `Gradio` · `pytest/unittest` · `Git` · `Docker Compose`

---

## 📁 Organisation

```text
projets/Audit Exigences/    Outil d'audit d'exigences : specs/, src/, tests/, data/, evidence/
exercices/AI_Agent/         Agent RAG QA : src/, scripts/, tests/, rapport/
exercices/rag/              Ateliers chunking + Qdrant : chunking/, pipeline/, exercices/
projets/<autres>/           Socle collaboratif de formation (normes, qualité code, fil rouge...)
workflows/, specs/, tools/  Méthode, gates et contrôles partagés du monorepo
```

## Reproduire

```powershell
# Audit Exigences — audit déterministe (hors-ligne)
cd "projets/Audit Exigences"
$env:PYTHONPATH = "$PWD\src"
python -m audit_exigences.cli --input data\exigences_sample.json --output evidence\audit-report.json
python -m unittest discover -s tests -v

# Mode sémantique (nécessite LM Studio démarré + modèle chargé)
python -m audit_exigences.cli --input data\exigences_sample.json --semantic
```
