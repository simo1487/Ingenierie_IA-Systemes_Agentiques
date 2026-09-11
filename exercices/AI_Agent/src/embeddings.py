"""Embeddings Mistral ou embeddings factices pour tests."""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter, defaultdict
from typing import List

from src.config import check_api_key, MISTRAL_EMBEDDING_MODEL, EMBEDDING_BACKEND

try:
    from langchain_mistralai import MistralAIEmbeddings
except ImportError:  # pragma: no cover
    MistralAIEmbeddings = None


EMBEDDING_DIM = 384  # Dimension compatible avec la collection ChromaDB


def _tokenize(text: str) -> list[str]:
    """Normalise et tokenise un texte."""
    return re.findall(r"[a-zA-Z0-9]+", text.lower())


class FakeEmbeddings:
    """Embeddings deterministes pour tests sans API.

    Version basique : sac de mots hashé.
    """

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._compute(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        return self._compute(text)

    def _compute(self, text: str) -> List[float]:
        vec = [0.0] * EMBEDDING_DIM
        words = _tokenize(text)
        if not words:
            return vec
        for w in words:
            idx = int(hashlib.md5(w.encode("utf-8")).hexdigest(), 16) % EMBEDDING_DIM
            vec[idx] += 1.0
        norm = sum(x * x for x in vec) ** 0.5
        return [x / norm for x in vec] if norm > 0 else vec


class TFIDFEmbeddings:
    """Embeddings TF-IDF pour tests sans API.

    Apprend le vocabulaire et les IDF lors du premier embed_documents().
    Utilise ensuite les memes poids pour embed_query().
    """

    def __init__(self, dim: int = EMBEDDING_DIM):
        self.dim = dim
        self.vocab: dict[str, int] = {}
        self.idf: dict[str, float] = {}
        self._fitted = False

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        # Phase 1 : construire le vocabulaire et les IDF
        if not self._fitted:
            self._fit(texts)

        return [self._compute(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        if not self._fitted:
            # Mode non appris : fallback sur sac de mots
            return self._bow_compute(text)
        return self._compute(text)

    def _fit(self, texts: List[str]) -> None:
        """Calcule les IDF sur le corpus."""
        df = defaultdict(int)
        for text in texts:
            words = set(_tokenize(text))
            for w in words:
                df[w] += 1

        n_docs = len(texts)
        # Limite le vocabulaire aux termes les plus frequents pour respecter dim
        sorted_vocab = sorted(df.items(), key=lambda x: x[1], reverse=True)
        self.vocab = {w: i for i, (w, _) in enumerate(sorted_vocab[: self.dim])}
        for w, count in df.items():
            self.idf[w] = math.log((n_docs + 1) / (count + 1)) + 1.0

        self._fitted = True

    def _compute(self, text: str) -> List[float]:
        """Vectorise un texte avec TF-IDF."""
        words = _tokenize(text)
        tf = Counter(words)
        vec = [0.0] * self.dim
        if not words:
            return vec

        for w, count in tf.items():
            if w in self.vocab:
                idx = self.vocab[w]
                tfidf = count * self.idf.get(w, 0.0)
                vec[idx] = tfidf

        norm = sum(x * x for x in vec) ** 0.5
        return [x / norm for x in vec] if norm > 0 else vec

    def _bow_compute(self, text: str) -> List[float]:
        """Sac de mots hashé pour les requêtes en mode non appris."""
        vec = [0.0] * self.dim
        words = _tokenize(text)
        if not words:
            return vec
        for w in words:
            idx = int(hashlib.md5(w.encode("utf-8")).hexdigest(), 16) % self.dim
            vec[idx] += 1.0
        norm = sum(x * x for x in vec) ** 0.5
        return [x / norm for x in vec] if norm > 0 else vec


def get_embedding_model():
    """Retourne le modele d'embedding configure."""
    if EMBEDDING_BACKEND == "fake":
        return TFIDFEmbeddings()

    if MistralAIEmbeddings is None:
        raise ImportError("langchain-mistralai est requis pour les embeddings Mistral.")
    api_key = check_api_key()
    return MistralAIEmbeddings(
        model=MISTRAL_EMBEDDING_MODEL,
        api_key=api_key,
    )
