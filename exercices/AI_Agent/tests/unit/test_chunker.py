"""Tests unitaires du chunker."""

from __future__ import annotations

from src.chunker import chunk_document
from src.config import DEFAULT_CHUNK_SIZE


def test_chunk_size_and_metadata(sample_md_path):
    doc = {
        "source": str(sample_md_path),
        "content": sample_md_path.read_text(encoding="utf-8"),
    }
    chunks = chunk_document(doc)
    assert len(chunks) > 0
    for chunk in chunks:
        assert len(chunk["content"]) <= int(DEFAULT_CHUNK_SIZE * 1.1)
        assert chunk["source"] == str(sample_md_path)
        assert "section" in chunk
        assert "chunk_id" in chunk
