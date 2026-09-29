# Technical Document QA Agent - v1

Agent RAG (Retrieval-Augmented Generation) capable de répondre à des questions techniques à partir de documents Markdown et HTML.

## Stack

- **LangChain** : orchestration RAG
- **ChromaDB** : base vectorielle
- **Mistral Embeddings** : vectorisation des chunks
- **Mistral LLM** : génération des réponses
- **BeautifulSoup** : parsing HTML

## Installation

```bash
cd exercices/AI_Agent
pip install -r requirements.txt
```

## Configuration

```bash
cp .env.example .env
# Renseigner MISTRAL_API_KEY dans .env
```

Pour tester sans appel API :

```bash
export LLM_BACKEND=fake
export EMBEDDING_BACKEND=fake
# ou sous PowerShell :
# $env:LLM_BACKEND='fake'
# $env:EMBEDDING_BACKEND='fake'
```

## Usage

### Indexer un dossier de documents

```bash
python scripts/index_documents.py C:\chemin\vers\docs
```

### Poser une question

```bash
python scripts/ask.py "What AI frameworks are supported by the K230?"
```

### Demo sans API

```bash
python scripts/demo_no_api.py
```

### Lancer les tests

```bash
pytest tests/ -v
```

## Structure

```
AI_Agent/
├── src/              # modules de l'agent
├── scripts/          # scripts CLI
├── tests/            # tests unitaires, intégration, e2e
├── plan/             # livrables de planification
├── chroma_db/        # base vectorielle locale (généré)
└── .env              # clé API (non versionnée)
```

## Sécurité

- `.env` est ignoré par Git.
- Aucune clé API ne doit être commitée.
