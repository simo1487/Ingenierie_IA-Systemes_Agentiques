"""Juge LLM local pour DeepEval (EPIC-AUD-05).

DeepEvalBaseLLM pointant sur le serveur LM Studio local
(endpoint OpenAI-compatible). Aucune cle API requise.
"""

from __future__ import annotations

import json
import socket
import urllib.error
import urllib.request

try:
    from deepeval.models.base_model import DeepEvalBaseLLM
except ImportError:  # pragma: no cover - deepeval est une dep de test
    DeepEvalBaseLLM = object  # type: ignore[assignment,misc]

from audit_exigences import config


def lmstudio_reachable(base_url: str | None = None, timeout: float = 2.0) -> bool:
    """Sonde TCP du serveur LM Studio."""
    url = (base_url or config.LMSTUDIO_URL).split("//", 1)[-1].split("/", 1)[0]
    host, _, port = url.partition(":")
    try:
        with socket.create_connection((host, int(port or 80)), timeout=timeout):
            return True
    except OSError:
        return False


class LMStudioJudge(DeepEvalBaseLLM):
    """Juge DeepEval via LM Studio local."""

    def __init__(
        self,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = 60.0,
    ):
        self.base_url = (base_url or config.LMSTUDIO_URL).rstrip("/")
        self.model_name = model or config.LMSTUDIO_MODEL
        self.timeout = timeout

    def load_model(self):
        return self

    def get_model_name(self) -> str:
        return f"lmstudio:{self.model_name}"

    def generate(self, prompt: str) -> str:
        return self._chat(prompt)

    async def a_generate(self, prompt: str) -> str:
        return self._chat(prompt)

    def _chat(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
        }
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
            raise RuntimeError(
                f"Juge LM Studio indisponible sur {self.base_url} : {exc}"
            ) from exc
        return body["choices"][0]["message"]["content"]
