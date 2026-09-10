"""Technique 4 : Découpage Sémantique (SemanticSplitterNodeParser).

Principe :
- Calcule la similarité sémantique (embedding) entre phrases successives.
- Lorsqu'une rupture thématique est détectée (distance supérieure à un seuil statistique), une frontière de chunk est posée.
- Permet de regrouper les phrases par thématique cohérente plutôt que par nombre arbitraire de caractères.
"""

from __future__ import annotations

from typing import Any
from llama_index.core import Document


def demonstrate_semantic_chunking(
    text: str,
    embed_model: Any | None = None,
    breakpoint_percentile_threshold: int = 90,
) -> list[dict]:
    """Découpe un texte par rupture sémantique.

    Si embed_model est fourni, utilise SemanticSplitterNodeParser de LlamaIndex.
    Sinon, simule la coupure sur les paragraphes thématiques pour l'apprentissage.
    """
    doc = Document(text=text, metadata={"source": "corpus_multitheme.md"})

    try:
        from llama_index.core.node_parser import SemanticSplitterNodeParser

        if embed_model is not None:
            splitter = SemanticSplitterNodeParser(
                buffer_size=1,
                breakpoint_percentile_threshold=breakpoint_percentile_threshold,
                embed_model=embed_model,
            )
            nodes = splitter.get_nodes_from_documents([doc])
            return [
                {"chunk_index": i, "text": n.get_content(), "method": "semantic_embedding"}
                for i, n in enumerate(nodes, start=1)
            ]
    except (ImportError, Exception):
        pass

    # Découpage logique de fallback si aucun modèle d'embedding n'est configuré
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return [
        {"chunk_index": i, "text": p, "method": "paragraph_boundary_fallback"}
        for i, p in enumerate(paragraphs, start=1)
    ]


if __name__ == "__main__":
    sample_text = (
        "Le protocole Automotive SPICE définit 31 processus d'évaluation du cycle de vie logiciel. "
        "Il impose une traçabilité bidirectionnelle entre exigences, architecture et tests unitaires.\n\n"
        "L'outil Cppcheck permet de vérifier la conformité MISRA C:2012 et d'identifier les fuites mémoire. "
        "Les alertes générées doivent faire l'objet d'un tri humain pour isoler les faux positifs.\n\n"
        "Le projet open source VESC implémente un contrôle vectoriel de flux (FOC) pour moteurs sans balais. "
        "Son firmware est distribué sous licence GPLv3 et dispose d'une intégration continue GitHub Actions."
    )

    print("=== DÉMONSTRATION : Découpage Sémantique ===")
    chunks = demonstrate_semantic_chunking(sample_text)
    for c in chunks:
        print(f"\n--- Chunk #{c['chunk_index']} [Méthode: {c['method']}] ---")
        print(c["text"])
