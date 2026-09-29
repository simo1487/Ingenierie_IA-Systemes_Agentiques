"""Configuration de l'audit semantique (EPIC-AUD-04)."""

from __future__ import annotations

import os

LMSTUDIO_URL = os.getenv("LMSTUDIO_URL", "http://localhost:1234/v1")
LMSTUDIO_MODEL = os.getenv("LMSTUDIO_MODEL", "local-model")
SEMANTIC_BACKEND = os.getenv("SEMANTIC_BACKEND", "lmstudio").lower()

MIN_SHARED_SUBJECT_TOKENS = 2
