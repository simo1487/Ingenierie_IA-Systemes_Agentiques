"""Gestion de la base vectorielle ChromaDB."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

try:
    from langchain_chroma import Chroma
except ImportError:
    try:
        from langchain_community.vectorstores import Chroma
    except ImportError:
        Chroma = None

try:
    from chromadb import PersistentClient
except ImportError:  # pragma: no cover
    PersistentClient = None

from src.config import CHROMA_PERSIST_DIR, DEFAULT_COLLECTION_NAME


def get_vector_store(
    embedding_function: Callable | None = None,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    persist_dir: str | Path = CHROMA_PERSIST_DIR,
):
    """Initialise ou charge une collection ChromaDB."""
    if Chroma is None:
        raise ImportError("langchain-chroma (ou langchain-community) est requis.")

    persist_dir = Path(persist_dir)
    persist_dir.mkdir(parents=True, exist_ok=True)

    return Chroma(
        collection_name=collection_name,
        embedding_function=embedding_function,
        persist_directory=str(persist_dir),
    )


def add_chunks_to_vector_store(
    vector_store: Any,
    chunks: list[dict[str, Any]],
) -> None:
    """Ajoute des chunks a ChromaDB avec leurs metadonnees."""
    texts = [chunk["content"] for chunk in chunks]
    metadatas = [
        {
            "chunk_id": chunk["chunk_id"],
            "source": chunk["source"],
            "section": chunk["section"],
        }
        for chunk in chunks
    ]
    ids = [chunk["chunk_id"] for chunk in chunks]

    vector_store.add_texts(texts=texts, metadatas=metadatas, ids=ids)


def reset_collection(
    collection_name: str = DEFAULT_COLLECTION_NAME,
    persist_dir: str | Path = CHROMA_PERSIST_DIR,
) -> None:
    """Supprime une collection ChromaDB."""
    if PersistentClient is None:
        raise ImportError("chromadb est requis.")

    persist_dir = Path(persist_dir)
    persist_dir.mkdir(parents=True, exist_ok=True)
    client = PersistentClient(path=str(persist_dir))
    try:
        client.delete_collection(name=collection_name)
    except Exception:
        pass
