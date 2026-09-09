"""Extraction des exigences depuis une page HTML StrictDoc de Zephyr reqmgmt."""

from __future__ import annotations

import html as html_module
import re


_REQUIREMENT_BLOCK_RE = re.compile(
    r'<sdoc-anchor[^>]*?data-uid="([^"]+)"[^>]*?>.*?</sdoc-anchor>\s*'
    r'(<sdoc-node-content[^>]*?>)(.*?)</sdoc-node-content>',
    re.DOTALL | re.IGNORECASE,
)

_TITLE_RE = re.compile(
    r'<sdoc-node-title[^>]*?>.*?<sdoc-autogen>(.*?)</sdoc-autogen>',
    re.DOTALL | re.IGNORECASE,
)

_STATEMENT_RE = re.compile(
    r'<sdoc-node-field-label>\s*STATEMENT:\s*</sdoc-node-field-label>\s*'
    r'<sdoc-node-field[^>]*?data-field-label="statement"[^>]*?>.*?'
    r'<sdoc-field-content>\s*<sdoc-autogen>(.*?)</sdoc-autogen>\s*</sdoc-field-content>',
    re.DOTALL | re.IGNORECASE,
)

_STATUS_RE = re.compile(
    r'data-status=(?:["\'])([^"\']+)(?:["\'])',
    re.IGNORECASE,
)


def _clean_text(raw: str) -> str:
    """Supprime les balises HTML, décode les entités et normalise les espaces."""
    decoded = html_module.unescape(raw)
    without_tags = re.sub(r"<[^>]+>", " ", decoded)
    normalized = re.sub(r"\s+", " ", without_tags)
    return normalized.strip()


def parse_requirement_page(
    html_text: str,
    source_url: str,
    category: str,
    subcategory: str,
) -> list[dict]:
    """Analyse une page HTML StrictDoc et retourne les exigences trouvées.

    Chaque exigence est structurée selon le schéma JSON interne, avec le statut
    de qualification "Observé" et la confiance "Candidat".
    """
    results = []

    for match in _REQUIREMENT_BLOCK_RE.finditer(html_text):
        req_id = match.group(1).strip()
        opening_tag = match.group(2)
        node_content = match.group(3)

        status_match = _STATUS_RE.search(opening_tag)
        source_status = status_match.group(1) if status_match else None

        title_match = _TITLE_RE.search(node_content)
        title = _clean_text(title_match.group(1)) if title_match else None

        statement_match = _STATEMENT_RE.search(node_content)
        statement = _clean_text(statement_match.group(1)) if statement_match else None

        # On ignore un bloc sans identifiant ni énoncé ; il devrait être audité à part.
        if not req_id or not statement:
            continue

        results.append(
            {
                "requirement_id": req_id,
                "title": title,
                "requirement_text": statement,
                "reformulation": False,
                "category": category,
                "subcategory": subcategory,
                "source_url": source_url,
                "source_path": None,
                "source_revision": None,
                "source_status": source_status,
                "status": "Observé",
                "confidence": "Candidat",
                "implementation_links": [],
                "test_links": [],
                "automotive_mapping": [],
                "traceability": {},
                "audit": {},
                "ambiguities": [],
            }
        )

    return results
