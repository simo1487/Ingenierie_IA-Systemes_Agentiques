"""Chunking header-aware pour documents techniques."""

from __future__ import annotations

import re
from typing import Any

from src.config import DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


def _split_by_headers(text: str) -> list[tuple[str, str]]:
    """Découpe le texte en sections selon les titres Markdown/HTML."""
    lines = text.splitlines()
    sections = []
    current_header = "Root"
    current_lines = []

    header_pattern = re.compile(r"^(#{1,6})\s+(.+)$")

    for line in lines:
        match = header_pattern.match(line)
        if match:
            if current_lines:
                sections.append((current_header, "\n".join(current_lines).strip()))
            current_header = match.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_header, "\n".join(current_lines).strip()))

    return sections


def _split_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    """Découpe un texte en blocs de taille fixe avec recouvrement."""
    chunks = []
    step = max(1, chunk_size - overlap)
    for i in range(0, len(text), step):
        end = i + chunk_size
        chunks.append(text[i:end].strip())
        if end >= len(text):
            break
    return [c for c in chunks if c]


def chunk_document(
    doc: dict[str, Any],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[dict[str, Any]]:
    """Découpe un document parse en chunks header-aware.

    Args:
        doc: dict avec source et content.
        chunk_size: taille maximale d'un chunk.
        overlap: recouvrement entre chunks.

    Returns:
        Liste de chunks avec source, section, content, chunk_id.
    """
    source = doc["source"]
    content = doc["content"]
    sections = _split_by_headers(content)

    chunks = []
    chunk_id = 0
    for section, section_text in sections:
        if not section_text:
            continue
        if len(section_text) <= chunk_size:
            chunk_id += 1
            chunks.append({
                "chunk_id": f"{source}_chunk_{chunk_id}",
                "source": source,
                "section": section,
                "content": section_text,
            })
        else:
            sub_chunks = _split_text(section_text, chunk_size, overlap)
            for sub in sub_chunks:
                chunk_id += 1
                chunks.append({
                    "chunk_id": f"{source}_chunk_{chunk_id}",
                    "source": source,
                    "section": section,
                    "content": sub,
                })

    return chunks


def chunk_documents(
    docs: list[dict[str, Any]],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[dict[str, Any]]:
    """Découpe une liste de documents en chunks."""
    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_document(doc, chunk_size, overlap))
    return all_chunks
