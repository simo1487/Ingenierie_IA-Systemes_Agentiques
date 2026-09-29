"""Audit EPIC-04 : analyse semantique par LLM local.

Pre-filtre deterministe des paires candidates (sujets partages, hors
detections deja faites), puis verdict JSON du LLM local :
{"verdict": "contradiction"|"duplicate"|"ok", "rationale": "..."}.

Toutes les sorties sont des propositions a revue humaine.
"""

from __future__ import annotations

import json
import re

from audit_exigences import config
from audit_exigences.llm_backends.base import BackendUnavailableError, LLMBackend
from audit_exigences.models import Finding, Requirement
from audit_exigences.normalize import normalize_tokens

VALID_VERDICTS = {"contradiction", "duplicate", "ok"}

_SEMANTIC_TYPES = {
    "contradiction": "semantic_contradiction",
    "duplicate": "semantic_duplicate",
}

PROMPT_TEMPLATE = """You are a requirements engineer. Compare these two automotive requirements.

[REQ-A]
{a_text}
[REQ-B]
{b_text}
[/REQ-B]

Decide their relationship:
- "contradiction": they impose incompatible behaviours or values
- "duplicate": they express the same obligation (including paraphrases)
- "ok": distinct, compatible or unrelated obligations

Answer with ONLY this JSON object:
{{"verdict": "contradiction" | "duplicate" | "ok", "rationale": "<one sentence>"}}"""

_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def find_candidate_pairs(
    requirements: list[Requirement],
    exclude_pairs: set[frozenset[str]] | None = None,
    min_shared: int = config.MIN_SHARED_SUBJECT_TOKENS,
) -> list[tuple[Requirement, Requirement]]:
    """Pre-filtre deterministe : paires partageant >= min_shared tokens de sujet."""
    excluded = exclude_pairs or set()
    pairs = []
    tokenized = [(req, normalize_tokens(req.text)) for req in requirements]
    for i in range(len(tokenized)):
        req_a, tokens_a = tokenized[i]
        for j in range(i + 1, len(tokenized)):
            req_b, tokens_b = tokenized[j]
            if frozenset({req_a.id, req_b.id}) in excluded:
                continue
            if len(tokens_a & tokens_b) >= min_shared:
                pairs.append((req_a, req_b))
    return pairs


def build_prompt(req_a: Requirement, req_b: Requirement) -> str:
    """Prompt structure de comparaison de deux exigences."""
    return PROMPT_TEMPLATE.format(a_text=req_a.text, b_text=req_b.text)


def parse_verdict(raw: str) -> dict | None:
    """Parse le verdict JSON du LLM ; retourne None si inexploitable."""
    match = _JSON_RE.search(raw)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    verdict = data.get("verdict")
    if verdict not in VALID_VERDICTS:
        return None
    return {"verdict": verdict, "rationale": str(data.get("rationale", ""))}


def audit_semantic(
    requirements: list[Requirement],
    backend: LLMBackend,
    exclude_pairs: set[frozenset[str]] | None = None,
) -> list[Finding]:
    """Detecte contradictions et duplications semantiques via le LLM local.

    Leve BackendUnavailableError si le backend est injoignable : l'appelant
    decide de l'abstention.
    """
    findings: list[Finding] = []
    pairs = find_candidate_pairs(requirements, exclude_pairs=exclude_pairs)

    for req_a, req_b in pairs:
        raw = backend.generate(build_prompt(req_a, req_b))
        parsed = parse_verdict(raw)
        if parsed is None or parsed["verdict"] == "ok":
            continue
        finding_type = _SEMANTIC_TYPES[parsed["verdict"]]
        findings.append(
            Finding(
                epic="semantic",
                requirement_id=req_a.id,
                finding_type=finding_type,
                position=0,
                detail=(
                    f"Verdict LLM '{parsed['verdict']}' avec '{req_b.id}' : "
                    f"{parsed['rationale']}"
                ),
                related_ids=[req_b.id],
                model=backend.name,
            )
        )
    return findings


def get_semantic_backend(name: str | None = None) -> LLMBackend:
    """Fabrique le backend semantique configure ('fake' ou 'lmstudio')."""
    backend_name = (name or config.SEMANTIC_BACKEND).lower()
    if backend_name == "fake":
        from audit_exigences.llm_backends.fake_backend import FakeLLMBackend

        return FakeLLMBackend()
    if backend_name == "lmstudio":
        from audit_exigences.llm_backends.lmstudio_backend import LMStudioBackend

        return LMStudioBackend()
    raise ValueError(
        f"Backend semantique inconnu : {backend_name}. Utilisez 'fake' ou 'lmstudio'."
    )


def pairs_from_findings(findings: list[Finding]) -> set[frozenset[str]]:
    """Ensemble des paires deja signalees par les audits deterministes."""
    return {
        frozenset({f.requirement_id, *f.related_ids})
        for f in findings
        if f.related_ids
    }
