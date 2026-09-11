# Plan v1 - Technical Document QA Agent

## Objectif
Construire un agent RAG capable de répondre à des questions techniques à partir de documents Markdown et HTML en utilisant ChromaDB et l'API Mistral.

## Stack
- LangChain
- ChromaDB
- Mistral Embeddings (`mistral-embed`)
- Mistral LLM (`mistral-large-latest`)
- BeautifulSoup (HTML)
- pytest (tests)

## Workflow
1. Charger les documents `.md` et `.html` d'un dossier.
2. Parser le texte (titres, paragraphes, listes, tables).
3. Découper en chunks de 1000 caractères avec overlap 150.
4. Générer les embeddings Mistral.
5. Stocker dans ChromaDB.
6. Recevoir une question, récupérer top 5 chunks.
7. Si score >= 0.50, appeler Mistral LLM.
8. Sinon, répondre `I could not find the information in the provided documents.`
9. Retourner la réponse avec sources.

## Tests
- Tests unitaires : loader, parser, chunker, vector store.
- Tests d'intégration : pipeline agent avec LLM mocké.
- Tests E2E : 30 questions K230 (optionnel, nécessite clé API).

## Sécurité
- `.env` strictement local.
- Clé API lue via variables d'environnement.
- Aucun secret dans le code.
