"""Chargement récursif des documents Markdown et HTML."""

from __future__ import annotations

from pathlib import Path
from typing import Any

SUPPORTED_EXTENSIONS = {".md", ".html"}


def load_documents(docs_dir: str | Path) -> list[dict[str, Any]]:
    """Charge tous les fichiers .md et .html d'un repertoire.

    Args:
        docs_dir: chemin du repertoire contenant les documents.

    Returns:
        Liste de dicts {source, raw_content}.
    """
    docs_dir = Path(docs_dir)
    if not docs_dir.exists():
        raise FileNotFoundError(f"Le repertoire n'existe pas : {docs_dir}")

    documents = []
    for ext in SUPPORTED_EXTENSIONS:
        for file_path in docs_dir.rglob(f"*{ext}"):
            documents.append({
                "source": str(file_path),
                "raw_content": file_path.read_text(encoding="utf-8"),
            })

    return documents
