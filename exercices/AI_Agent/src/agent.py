"""Orchestration complete de l'agent RAG."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src import config
from src.loader import load_documents
from src.parsers import parse_document
from src.chunker import chunk_documents
from src.embeddings import get_embedding_model
from src.vector_store import get_vector_store, add_chunks_to_vector_store, reset_collection
from src.retriever import retrieve_chunks
from src.llm import generate_answer
from src.utils import answer_or_abstain


class TechnicalQAAgent:
    """Agent RAG pour repondre a des questions techniques."""

    def __init__(
        self,
        persist_dir: str | Path = config.CHROMA_PERSIST_DIR,
        collection_name: str = config.DEFAULT_COLLECTION_NAME,
    ):
        self.persist_dir = Path(persist_dir)
        self.collection_name = collection_name
        self.embedding_model = get_embedding_model()
        self.vector_store = get_vector_store(
            embedding_function=self.embedding_model,
            collection_name=self.collection_name,
            persist_dir=self.persist_dir,
        )

    def index_documents(self, docs_dir: str | Path) -> int:
        """Charge, parse, decoupe et indexe les documents d'un repertoire."""
        docs_dir = Path(docs_dir)

        # Reset collection existante
        reset_collection(
            collection_name=self.collection_name,
            persist_dir=self.persist_dir,
        )
        self.vector_store = get_vector_store(
            embedding_function=self.embedding_model,
            collection_name=self.collection_name,
            persist_dir=self.persist_dir,
        )

        raw_docs = load_documents(docs_dir)
        parsed_docs = [parse_document(doc) for doc in raw_docs]
        chunks = chunk_documents(parsed_docs)

        if not chunks:
            return 0

        add_chunks_to_vector_store(self.vector_store, chunks)
        return len(chunks)

    def answer(self, question: str) -> dict[str, Any]:
        """Repond a une question en utilisant le RAG."""
        citations = retrieve_chunks(self.vector_store, question)
        result = answer_or_abstain(question, citations, generate_answer)
        return result
