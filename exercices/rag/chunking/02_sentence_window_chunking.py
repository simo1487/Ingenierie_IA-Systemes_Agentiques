"""Technique 2 : Découpage par Fenêtre de Phrases (SentenceWindowNodeParser).

Principe :
- Chaque node extrait correspond à une phrase unique précise (idéal pour la recherche vectorielle).
- Une métadonnée spéciale 'window' stocke la phrase courante ainsi que k phrases avant et après.
- Lors de la recherche, on compare la requête à la phrase exacte, mais on transmet la fenêtre complète au générateur.
"""

from __future__ import annotations

from llama_index.core import Document
from llama_index.core.node_parser import SentenceWindowNodeParser


def demonstrate_sentence_window(
    text: str,
    window_size: int = 2,
    window_metadata_key: str = "window",
) -> list[dict]:
    """Découpe un texte en phrases individuelles avec leur contexte de voisinage."""
    doc = Document(
        text=text,
        metadata={"source": "02_qualite_cppcheck_misra.md", "auteur": "Equipe Qualite"},
    )

    node_parser = SentenceWindowNodeParser.from_defaults(
        window_size=window_size,
        window_metadata_key=window_metadata_key,
        original_text_metadata_key="original_sentence",
    )

    nodes = node_parser.get_nodes_from_documents([doc])

    results = []
    for idx, node in enumerate(nodes, start=1):
        results.append({
            "chunk_index": idx,
            "sentence": node.get_content(),
            "window_context": node.metadata.get(window_metadata_key, ""),
            "metadata": node.metadata,
        })
    return results


if __name__ == "__main__":
    sample_text = (
        "Lors de l'analyse statique de la fixture defect.c, Cppcheck a detecte une ecriture hors limites. "
        "L'erreur provient d'un usage non securise de strcpy sur un tampon de 10 octets. "
        "Cette anomalie a ete confirmee par la revue humaine comme bloquante pour l'integration. "
        "Elle necessite un remplacement par strncpy ou un controle prealable de longueur. "
        "La directive MISRA Dir 4.6 exige egalement des types a taille fixee dans stdint.h."
    )

    print("=== DÉMONSTRATION : SentenceWindowNodeParser (Fenêtre de phrases) ===")
    chunks = demonstrate_sentence_window(sample_text, window_size=1)
    for c in chunks:
        print(f"\n--- Node #{c['chunk_index']} (Phrase cherchée) ---")
        print(f"Phrase cible : {c['sentence']}")
        print(f"Fenêtre restituée : {c['window_context']}")
