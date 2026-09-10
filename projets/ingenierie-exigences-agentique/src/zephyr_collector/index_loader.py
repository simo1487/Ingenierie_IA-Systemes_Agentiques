"""Lecture de l'index Zephyr reqmgmt et extraction des sous-documents."""

from __future__ import annotations

import re
from pathlib import PurePosixPath
from urllib.parse import urljoin, urlparse


_ANCHOR_RE = re.compile(
    r'<a\s+[^>]*?class="project_tree-file"[^>]*?\n?[^>]*?href="([^"]+)"[^>]*?>(.*?)</a>',
    re.DOTALL | re.IGNORECASE,
)

_TITLE_RE = re.compile(
    r'<div\s+class="project_tree-file-title"[^>]*?>\s*(.*?)\s*</div>',
    re.DOTALL | re.IGNORECASE,
)


_CATEGORIES = {"software_requirements", "system_requirements"}


def _extract_title(anchor_content: str) -> str | None:
    match = _TITLE_RE.search(anchor_content)
    if not match:
        return None
    # Supprime les balises internes (ex: <b>) si présentes
    return re.sub(r"<[^>]+>", "", match.group(1)).strip()


def _categorize(url: str) -> tuple[str, str]:
    path = PurePosixPath(urlparse(url).path)
    category = path.parent.name
    subcategory = path.stem

    if category not in _CATEGORIES:
        category = "unknown"

    return category, subcategory


def parse_index(html: str, base_url: str) -> list[dict]:
    """Analyse le HTML de l'index et retourne la liste des sous-documents trouvés.

    Chaque entrée contient le titre, l'URL résolue, la catégorie et la sous-catégorie.
    Les liens ne menant pas à software_requirements ou system_requirements sont ignorés.
    """
    results = []

    for anchor in _ANCHOR_RE.finditer(html):
        href = anchor.group(1).strip()
        content = anchor.group(2)

        full_url = urljoin(base_url, href)
        category, subcategory = _categorize(full_url)

        if category not in _CATEGORIES:
            continue

        title = _extract_title(content) or subcategory.replace("_", " ").title()

        results.append(
            {
                "title": title,
                "source_url": full_url,
                "category": category,
                "subcategory": subcategory,
            }
        )

    return results
