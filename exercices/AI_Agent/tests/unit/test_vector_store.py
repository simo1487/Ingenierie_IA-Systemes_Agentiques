"""Tests unitaires du vector store avec embeddings factices."""

from __future__ import annotations

import numpy as np

from src.vector_store import get_vector_store, add_chunks_to_vector_store


class FakeEmbeddings:
    """Embeddings deterministes pour les tests."""

    def embed_documents(self, texts):
        return [np.random.rand(384).tolist() for _ in texts]

    def embed_query(self, text):
        return np.random.rand(384).tolist()


def test_add_and_search_chunks(temp_persist_dir):
    vs = get_vector_store(
        embedding_function=FakeEmbeddings(),
        persist_dir=temp_persist_dir,
    )
    chunks = [
        {
            "chunk_id": "chunk_1",
            "source": "test.md",
            "section": "CPU",
            "content": "CPU0 runs at 800 MHz.",
        },
        {
            "chunk_id": "chunk_2",
            "source": "test.md",
            "section": "KPU",
            "content": "KPU supports INT8 and INT16.",
        },
    ]
    add_chunks_to_vector_store(vs, chunks)
    results = vs.similarity_search("CPU frequency", k=1)
    assert len(results) == 1
    assert "chunk_id" in results[0].metadata
