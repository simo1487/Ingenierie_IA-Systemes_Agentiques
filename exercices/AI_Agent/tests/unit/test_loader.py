"""Tests unitaires du loader."""

from __future__ import annotations

from src.loader import load_documents


def test_load_documents(fixture_dir):
    docs = load_documents(fixture_dir)
    assert len(docs) >= 2
    sources = {doc["source"].split(".")[-1] for doc in docs}
    assert "md" in sources
    assert "html" in sources


def test_load_documents_empty(tmp_path):
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    docs = load_documents(empty_dir)
    assert docs == []
