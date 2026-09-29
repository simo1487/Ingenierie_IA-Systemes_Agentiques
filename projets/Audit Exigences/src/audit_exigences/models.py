"""Modeles de donnees de l'outil d'audit."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Requirement:
    """Une exigence du dataset."""

    id: str
    text: str
    source: str = ""
    version: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Requirement":
        return cls(
            id=str(data.get("id", "")),
            text=str(data.get("text", "")),
            source=str(data.get("source", "")),
            version=str(data.get("version", "")),
        )


@dataclass
class Finding:
    """Une anomalie detectee par un audit."""

    epic: str
    requirement_id: str
    finding_type: str
    position: int
    detail: str
    suggestion: str = ""
    related_ids: list[str] = field(default_factory=list)
    score: float | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {
            "epic": self.epic,
            "requirement_id": self.requirement_id,
            "type": self.finding_type,
            "position": self.position,
            "detail": self.detail,
        }
        if self.suggestion:
            result["suggestion"] = self.suggestion
        if self.related_ids:
            result["related_ids"] = self.related_ids
        if self.score is not None:
            result["score"] = round(self.score, 4)
        return result

