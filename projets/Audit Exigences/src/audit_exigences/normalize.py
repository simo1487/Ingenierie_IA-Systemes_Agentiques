"""Normalisation des tokens partagee par les audits."""

from __future__ import annotations

import re

TOKEN_RE = re.compile(r"\w+", re.UNICODE)

STOPWORDS = {
    # Francais
    "le", "la", "les", "un", "une", "des", "de", "du", "d",
    "et", "ou", "a", "au", "aux", "en", "dans", "sur", "sous",
    "par", "avec", "sans", "pour", "que", "qui",
    # Anglais
    "the", "a", "an", "of", "in", "to", "be", "is", "are", "at",
    "on", "by", "for", "from", "when", "after", "before", "within",
    "all", "every", "each", "if", "then", "than", "it", "its",
    # Modaux : conserves pour la negation via patterns dedies, mais
    # non discriminants comme sujets
    "shall", "must", "should", "may", "can", "will",
}

# Unites : grandeurs, pas des sujets
UNITS = {
    "km", "kmh", "second", "secondes", "ms", "degc", "degre", "degres",
    "degrés", "degré", "bar", "kw", "wh", "kwh", "mbps", "kbps",
    "percent", "percent", "hz", "khz", "mhz",
}


def stem(token: str) -> str:
    """Stemming leger : harmonise pluriels et variantes simples."""
    if len(token) <= 3:
        return token
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith("sses") and len(token) > 5:
        return token[:-2]
    if token.endswith("ses") and len(token) > 4:
        return token[:-2]
    if token.endswith("s") and not token.endswith(("ss", "us", "is")) and len(token) > 3:
        return token[:-1]
    return token


def normalize_tokens(text: str) -> set[str]:
    """Tokenise, minuscule, retire stopwords/unites et applique un stem léger.

    Les tirets sont supprimes pour unifier "start-up" et "startup".
    """
    compact = text.lower().replace("-", "").replace("–", "").replace("'", "")
    raw = re.findall(r"\w+", compact, re.UNICODE)
    result = set()
    for t in raw:
        if t in STOPWORDS or t in UNITS or len(t) < 2:
            continue
        result.add(stem(t))
    return result
