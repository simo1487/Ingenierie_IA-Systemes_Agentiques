"""Technique 1 : Découpage par taille fixe (SentenceSplitter / TokenSplitter).

Principe :
- Découpe le texte en morceaux de taille bornée (ex: 200 tokens ou caractères).
- Intègre un recouvrement (overlap) pour éviter de casser une phrase ou une condition au milieu.
- Conserve les frontières de phrases quand c'est possible grâce à SentenceSplitter.
"""

from __future__ import annotations

from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter, TokenTextSplitter


def demonstrate_sentence_splitter(text: str, chunk_size: int = 150, chunk_overlap: int = 30) -> list[dict]:
    """Découpe un texte avec SentenceSplitter de LlamaIndex."""
    doc = Document(text=text, metadata={"source": "01_normes_automobile.md", "type": "norme"})

    splitter = SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    nodes = splitter.get_nodes_from_documents([doc])

    results = []
    for idx, node in enumerate(nodes, start=1):
        results.append({
            "chunk_index": idx,
            "text": node.get_content(),
            "char_length": len(node.get_content()),
            "metadata": node.metadata,
        })
    return results


def demonstrate_token_splitter(text: str, chunk_size: int = 50, chunk_overlap: int = 10) -> list[dict]:
    """Découpe brute par nombre de tokens avec TokenTextSplitter."""
    doc = Document(text=text, metadata={"source": "02_qualite_cppcheck_misra.md"})

    splitter = TokenTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    nodes = splitter.get_nodes_from_documents([doc])
    return [
        {
            "chunk_index": idx,
            "text": node.get_content(),
            "char_length": len(node.get_content()),
        }
        for idx, node in enumerate(nodes, start=1)
    ]


if __name__ == "__main__":
    sample_text = (
        "L'équipe d'ingénierie logicielle doit spécifier les exigences fonctionnelles "
        "et non-fonctionnelles du logiciel sur la base des exigences système allouées. "
        "Chaque exigence logicielle doit être unique, vérifiable et attribuée à un composant. "
        "Une stratégie de vérification unitaire doit être définie, comprenant des critères "
        "de couverture structurelle selon le niveau ASIL ciblé."
    )

    print("=== DÉMONSTRATION 1 : SentenceSplitter (Recommandé) ===")
    sentence_chunks = demonstrate_sentence_splitter(sample_text, chunk_size=40, chunk_overlap=10)
    for c in sentence_chunks:
        print(f"--- Chunk #{c['chunk_index']} ({c['char_length']} chars) ---")
        print(c["text"])

    print("\n=== DÉMONSTRATION 2 : TokenTextSplitter ===")
    token_chunks = demonstrate_token_splitter(sample_text, chunk_size=20, chunk_overlap=5)
    for c in token_chunks:
        print(f"--- Chunk #{c['chunk_index']} ({c['char_length']} chars) ---")
        print(c["text"])
