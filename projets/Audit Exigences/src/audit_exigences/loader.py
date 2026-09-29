"""Chargement du dataset d'exigences."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from audit_exigences.models import Requirement


def load_dataset(path: Path) -> list[Requirement]:
    """Charge un dataset JSON ou Markdown d'exigences."""
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return _load_json(text)
    return _load_markdown(text)


def _load_json(text: str) -> list[Requirement]:
    data: dict[str, Any] = json.loads(text)
    raw = data.get("exigences", data.get("requirements", []))
    return [Requirement.from_dict(item) for item in raw]


def _load_markdown(text: str) -> list[Requirement]:
    """Charge les exigences depuis un Markdown de forme '- REQ-xxx : texte'."""
    requirements: list[Requirement] = []
    pattern = re.compile(r"^[-*]\s*([A-Za-z0-9_-]+)\s*[:]\s*(.+)$")
    for line in text.splitlines():
        match = pattern.match(line.strip())
        if match:
            requirements.append(
                Requirement(id=match.group(1), text=match.group(2).strip())
            )
    return requirements
