"""Fixtures partagees pour les tests."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from src.agent import TechnicalQAAgent


@pytest.fixture
def temp_persist_dir():
    """Cree un repertoire temporaire pour ChromaDB."""
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        yield tmp


@pytest.fixture
def fixture_dir():
    """Retourne le chemin du dossier fixtures."""
    return Path(__file__).resolve().parent / "fixtures"


@pytest.fixture
def sample_md_path(fixture_dir):
    """Chemin du fichier sample_k230.md."""
    return fixture_dir / "sample_k230.md"


@pytest.fixture
def sample_html_path(fixture_dir):
    """Chemin du fichier sample.html."""
    return fixture_dir / "sample.html"


@pytest.fixture
def test_queries_path():
    """Chemin du fichier k230_test_queries.json."""
    return Path(__file__).resolve().parent / "test_queries" / "k230_test_queries.json"


@pytest.fixture
def fresh_agent(temp_persist_dir):
    """Retourne un agent avec une collection ChromaDB temporaire."""
    return TechnicalQAAgent(persist_dir=temp_persist_dir)
