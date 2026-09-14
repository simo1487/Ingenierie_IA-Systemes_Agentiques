from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class Status(str, Enum):
    OBSERVED = "Observé"
    PROPOSAL = "Proposition"
    VERIFIED = "Vérifié"
    UNVERIFIED = "Non vérifié"
    BLOCKED = "Bloqué"
    OPEN_QUESTION = "Question ouverte"


@dataclass(frozen=True)
class AgentResult:
    agent: str
    status: Status
    payload: dict[str, Any]
    sources: list[dict[str, str]] = field(default_factory=list)
    questions: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["status"] = self.status.value
        return value
