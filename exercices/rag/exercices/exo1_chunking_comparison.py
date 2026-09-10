"""Exercice 1 : Comparaison de deux stratégies de découpage (Chunking).

Objectif :
- Observer la différence entre un découpage fixe (SentenceSplitter) et un découpage structurel (MarkdownNodeParser).
- Vérifier si les conditions d'une règle ou d'une exigence restent attachées à leur identifiant.
"""

from __future__ import annotations

from pathlib import Path
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter, MarkdownNodeParser


def run_chunking_comparison():
    current_dir = Path(__file__).resolve().parent
    sample_file = current_dir.parent / "data" / "sample_corpus" / "01_normes_automobile.md"

    text = sample_file.read_text(encoding="utf-8")
    doc = Document(text=text, metadata={"file": sample_file.name})

    print("=================================================================")
    print("EXERCICE 1 : COMPARAISON DES STRATÉGIES DE DÉCOUPAGE (CHUNKING)")
    print("=================================================================")

    # Stratégie A : Découpage par taille fixe (SentenceSplitter)
    splitter_fixed = SentenceSplitter(chunk_size=100, chunk_overlap=20)
    nodes_fixed = splitter_fixed.get_nodes_from_documents([doc])

    # Stratégie B : Découpage structurel (MarkdownNodeParser)
    splitter_markdown = MarkdownNodeParser.from_defaults()
    nodes_markdown = splitter_markdown.get_nodes_from_documents([doc])

    print(f"\nDocument source : {sample_file.name} ({len(text)} caractères)")
    print(f"Stratégie A (SentenceSplitter fixe) : {len(nodes_fixed)} chunks générés")
    print(f"Stratégie B (MarkdownNodeParser)   : {len(nodes_markdown)} chunks générés")

    print("\n--- Échantillon Stratégie A (Chunk #1 fixe) ---")
    print(nodes_fixed[0].get_content().strip()[:200] + "...")

    print("\n--- Échantillon Stratégie B (Chunk #1 Markdown par section) ---")
    print(nodes_markdown[0].get_content().strip()[:200] + "...")

    print("\n[Question d'analyse] :")
    print("La Stratégie B préserve-t-elle le lien direct entre l'UID et ses critères d'acceptation ?")


if __name__ == "__main__":
    run_chunking_comparison()
