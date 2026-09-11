"""Parsing de documents Markdown et HTML."""

from __future__ import annotations

import re
from typing import Any

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover
    BeautifulSoup = None


def parse_markdown(raw_content: str) -> str:
    """Nettoie le Markdown en gardant la structure textuelle."""
    text = raw_content
    # Supprimer les images
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # Supprimer les liens mais garder le texte
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Supprimer les blocs de code marqués mais garder leur contenu
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Supprimer les lignes de séparateurs
    text = re.sub(r"\n-{3,}\n", "\n", text)
    # Garder sauts de lignes simples
    return text.strip()


def parse_html(raw_content: str) -> str:
    """Extrait le texte pertinent d'un document HTML avec les titres comme sections."""
    if BeautifulSoup is None:
        raise ImportError("beautifulsoup4 est requis pour parser le HTML.")

    soup = BeautifulSoup(raw_content, "html.parser")

    # Supprimer les éléments parasites
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "ad"]):
        tag.decompose()

    # Extraire les sections avec titres
    parts = []
    for element in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "table", "tr"]):
        if element.name.startswith("h"):
            parts.append(f"\n### {element.get_text(strip=True)}\n")
        elif element.name == "table":
            rows = []
            for tr in element.find_all("tr"):
                cells = [td.get_text(strip=True) for td in tr.find_all(["th", "td"])]
                rows.append(" | ".join(cells))
            if rows:
                parts.append("\n".join(rows))
        else:
            text = element.get_text(strip=True)
            if text:
                parts.append(text)

    return "\n".join(parts).strip()


def parse_document(doc: dict[str, Any]) -> dict[str, Any]:
    """Parse un document en fonction de son extension."""
    source = doc["source"]
    raw = doc["raw_content"]
    ext = source.lower().split(".")[-1]

    if ext == "md":
        clean = parse_markdown(raw)
    elif ext == "html":
        clean = parse_html(raw)
    else:
        raise ValueError(f"Format non supporte : {ext}")

    return {
        "source": source,
        "content": clean,
    }
