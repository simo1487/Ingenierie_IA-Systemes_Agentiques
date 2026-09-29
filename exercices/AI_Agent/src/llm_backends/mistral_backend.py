"""Backend Mistral API."""

from __future__ import annotations

from typing import Any

from src.config import check_api_key, MISTRAL_MODEL, ABSTENTION_MESSAGE

try:
    from langchain_mistralai import ChatMistralAI
    from langchain_core.messages import SystemMessage, HumanMessage
except ImportError:  # pragma: no cover
    ChatMistralAI = None
    SystemMessage = None
    HumanMessage = None


SYSTEM_PROMPT = (
    "You are a technical assistant. "
    "Use ONLY the provided context to answer the question. "
    "Do not use external knowledge. "
    "Do NOT include citations, document references, or source mentions in your answer text. "
    "Answer with a clear, concise sentence only. "
    "If the answer cannot be found in the provided context, answer exactly: "
    f'"{ABSTENTION_MESSAGE}".'
)


def _build_context(citations: list[dict[str, Any]]) -> str:
    parts = []
    for i, cit in enumerate(citations, start=1):
        parts.append(
            f"[Document {i}] Source: {cit['source']} / Section: {cit['section']}\n"
            f"{cit['content']}\n"
        )
    return "\n".join(parts)


class MistralLLMBackend:
    """Backend utilisant l'API Mistral via LangChain."""

    def generate(self, question: str, citations: list[dict[str, Any]]) -> str:
        if ChatMistralAI is None:
            raise ImportError("langchain-mistralai est requis pour le backend Mistral.")

        api_key = check_api_key()
        llm = ChatMistralAI(
            model=MISTRAL_MODEL,
            api_key=api_key,
            temperature=0.0,
        )
        context = _build_context(citations)
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Context:\n\n{context}\n\nQuestion:\n\n{question}"),
        ]
        response = llm.invoke(messages)
        return str(response.content)
