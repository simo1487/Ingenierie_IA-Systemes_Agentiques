"""Configuration centralisée de l'agent."""

from __future__ import annotations

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None

if load_dotenv is not None:
    # Cherche .env dans AI_Agent puis dans le dossier parent
    for candidate in [
        Path(__file__).resolve().parents[1] / ".env",
        Path(__file__).resolve().parents[2] / ".env",
    ]:
        if candidate.exists():
            load_dotenv(candidate)

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
DEFAULT_CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))
DEFAULT_TOP_K = int(os.getenv("TOP_K", "5"))
DEFAULT_SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.30"))

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_MODEL = os.getenv("MISTRAL_MODEL", "mistral-large-latest")
MISTRAL_EMBEDDING_MODEL = os.getenv("MISTRAL_EMBEDDING_MODEL", "mistral-embed")
LLM_BACKEND = os.getenv("LLM_BACKEND", "mistral").lower()
EMBEDDING_BACKEND = os.getenv("EMBEDDING_BACKEND", "mistral").lower()

CHROMA_PERSIST_DIR = Path(os.getenv("CHROMA_PERSIST_DIR", PROJECT_ROOT / "chroma_db"))
DEFAULT_COLLECTION_NAME = "technical_docs"

ABSTENTION_MESSAGE = "I could not find the information in the provided documents."


def check_api_key() -> str:
    """Retourne la clé API Mistral si présente, sinon lève une exception."""
    key = MISTRAL_API_KEY
    if not key:
        raise RuntimeError(
            "MISTRAL_API_KEY non definie. "
            "Creez un fichier .env base sur .env.example."
        )
    return key
