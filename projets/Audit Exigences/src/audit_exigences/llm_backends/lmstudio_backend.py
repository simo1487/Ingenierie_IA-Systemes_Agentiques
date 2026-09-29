"""Backend LLM local via LM Studio (endpoint OpenAI-compatible).

Aucune cle API requise : LM Studio sert les modeles locaux sur
/v1/chat/completions. Implementation stdlib (urllib) pour rester
sans dependance d'execution.
"""

from __future__ import annotations

import json
import socket
import urllib.error
import urllib.request

from audit_exigences import config
from audit_exigences.llm_backends.base import BackendUnavailableError, LLMBackend


class LMStudioBackend(LLMBackend):
    """Appelle le serveur LM Studio local en mode chat completions."""

    name = "lmstudio"

    def __init__(
        self,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = 30.0,
    ):
        self.base_url = (base_url or config.LMSTUDIO_URL).rstrip("/")
        self.model = model or config.LMSTUDIO_MODEL
        self.timeout = timeout

    def is_available(self) -> bool:
        """Sonde rapide du serveur LM Studio."""
        try:
            host_port = self.base_url.split("//", 1)[-1].split("/", 1)[0]
            host, _, port = host_port.partition(":")
            with socket.create_connection((host, int(port or 80)), timeout=2):
                return True
        except OSError:
            return False

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
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
            raise BackendUnavailableError(
                f"Backend LM Studio indisponible sur {self.base_url} : {exc}"
            ) from exc
        return body["choices"][0]["message"]["content"]
