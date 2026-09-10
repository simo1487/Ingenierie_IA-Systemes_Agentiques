# Exercices et Exemples RAG — LlamaIndex & Qdrant

Ce dossier fournit l'environnement d'apprentissage et les briques logicielles pour construire un système RAG (Retrieval-Augmented Generation) appliqué au portefeuille d'ingénierie embarquée.

---

## 1. Démarrage rapide

### Prérequis
- Python 3.10 ou supérieur
- Gestionnaire d'environnement recommandé : `uv` (ou standard `pip` / `venv`)

### Installation des dépendances avec `uv`
```bash
# À la racine de FormationIaProject
cd exercices/rag
uv venv
source .venv/bin/activate   # ou .venv\Scripts\activate sous Windows
uv pip install -r requirements.txt
```

---

## 2. Configuration de Qdrant

Trois modes d'exécution sont supportés dans [`config/qdrant_config.py`](config/qdrant_config.py) :

1. **Mode En Mémoire (`:memory:`) — Par défaut :**
   - Zéro dépendance externe, pas besoin de Docker.
   - Les données restent en RAM pendant le script (idéal pour tester rapidement).
2. **Mode Disque local (`path="./qdrant_data"`) :**
   - Stockage local persistant sans serveur.
3. **Mode Serveur / Conteneur Docker :**
   - Lancez un serveur Qdrant avec Docker Compose :
     ```bash
     docker compose up -d
     ```
   - L'interface web Qdrant est accessible sur [http://localhost:6333/dashboard](http://localhost:6333/dashboard).

---

## 3. Structure du dossier

```text
exercices/rag/
├── README.md                          # Ce guide
├── pyproject.toml / requirements.txt  # Dépendances Python
├── docker-compose.yml                 # Serveur Qdrant local (optionnel)
├── config/
│   └── qdrant_config.py               # Initialisation client Qdrant et collection LlamaIndex
├── chunking/                          # Démonstrations des 5 techniques de découpage
│   ├── 01_fixed_token_chunking.py     # SentenceSplitter / TokenSplitter (taille fixe + overlap)
│   ├── 02_sentence_window_chunking.py # SentenceWindowNodeParser (fenêtre de phrases)
│   ├── 03_hierarchical_parent_child.py# HierarchicalNodeParser (parent riche, enfant précis)
│   ├── 04_semantic_chunking.py        # Découpage par rupture de similarité sémantique
│   └── 05_markdown_code_chunking.py   # MarkdownNodeParser et CodeSplitter (structurel)
├── pipeline/
│   ├── ingestion.py                   # Ingestion multi-fichiers et stockage Qdrant
│   └── retrieval.py                   # Requête, filtres de métadonnées et citations sourcées
├── data/sample_corpus/                # Échantillons issus des projets fusionnés
│   ├── 01_normes_automobile.md        # Normes Automotive SPICE et ISO/SAE 21434
│   ├── 02_qualite_cppcheck_misra.md   # Rapports qualité Cppcheck et règles MISRA C:2012
│   ├── 03_logiciel_open_source_vesc.json # Fiche candidat contrôleur moteur open source
│   └── 04_exigences_systeme.md        # Exigences de traçabilité système
└── exercices/                         # Exercices pratiques pour les ateliers
    ├── exo1_chunking_comparison.py    # Exercice 1 : Comparer deux découpages
    ├── exo2_indexation_qdrant.py      # Exercice 2 : Indexer dans Qdrant
    └── exo3_retrieval_and_citations.py# Exercice 3 : Requêtes, filtres et citations
```

---

## 4. Les 5 Techniques de Chunking expliquées

1. **Découpage Fixe avec Recouvrement (`01_fixed_token_chunking.py`) :**
   - Découpe par blocs de tokens ou caractères fixes (ex: 150 caractères) avec un chevauchement (`overlap=30`).
   - Simple et robuste, mais risque de scinder une exigence au mauvais endroit.

2. **Fenêtre de Phrases (`02_sentence_window_chunking.py`) :**
   - Chaque chunk correspond à une phrase unique pour une recherche vectorielle très pointue.
   - Les phrases adjacentes (fenêtre de voisinage) sont renvoyées au modèle de réponse.

3. **Hiérarchique Parent-Enfant (`03_hierarchical_parent_child.py`) :**
   - Crée une arborescence : de grands chunks parents (ex: 512 tokens) et de petits chunks enfants (ex: 128 tokens).
   - La recherche est effectuée sur les enfants, et le parent complet est retourné pour le contexte.

4. **Découpage Sémantique (`04_semantic_chunking.py`) :**
   - Analyse la distance d'embedding entre deux phrases consécutives.
   - Dès qu'un saut sémantique dépasse un seuil percentile, une nouvelle frontière de chunk est créée.

5. **Découpage Structurel Markdown & Code (`05_markdown_code_chunking.py`) :**
   - Respecte les balises de titres (`#`, `##`) des fichiers de spécification.
   - Les métadonnées du titre et l'identifiant (UID) voyagent obligatoirement avec le texte de la règle.

---

## 5. Exécution des exercices

### Lancer l'Exercice 1 : Comparaison de chunking
```bash
python -m exercices.rag.chunking.01_fixed_token_chunking
python -m exercices.rag.exercices.exo1_chunking_comparison
```

### Lancer l'Exercice 2 : Indexation dans Qdrant
```bash
python -m exercices.rag.exercices.exo2_indexation_qdrant
```

### Lancer l'Exercice 3 : Recherche, filtres et citations
```bash
python -m exercices.rag.exercices.exo3_retrieval_and_citations
```

---

## 6. Utilisation par les équipes projets

Chaque équipe projet de l'atelier peut brancher ses propres données :
- **Équipe Normes :** pointez vers `projets/normes/exigences/`
- **Équipe Qualité :** pointez vers `projets/qualite-code/evidence/` et `docs/`
- **Équipe Logiciel Auto Open Source :** pointez vers `projets/logiciel-automobile-open-source/`
- **Équipe Ingénierie des Exigences :** pointez vers `projets/exigences-zephyr/` ou le projet cible
