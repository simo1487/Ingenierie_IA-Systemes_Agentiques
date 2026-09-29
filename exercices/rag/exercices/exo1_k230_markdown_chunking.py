"""Exercice 1 bis : Chunking Markdown du K230 Datasheet.

Objectif :
- Appliquer le MarkdownNodeParser sur la datasheet K230.
- Sauvegarder les chunks en JSON dans un dossier output pour l'indexation Qdrant.
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter, MarkdownNodeParser


def run_k230_markdown_chunking():
    # Set UTF-8 encoding for output
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    current_dir = Path(__file__).resolve().parent
    sample_file = current_dir.parent / "data" / "sample_corpus" / "k230_datasheet.md"
    output_dir = current_dir.parent / "output"
    output_dir.mkdir(exist_ok=True)

    text = sample_file.read_text(encoding="utf-8")
    doc = Document(text=text, metadata={"file": sample_file.name})

    print("=================================================================")
    print("CHUNKING K230 : DÉCOUPAGE MARKDOWN")
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
    print(nodes_fixed[0].get_content().strip()[:500] + "...")

    print("\n--- Échantillon Stratégie B (Chunk #1 Markdown par section) ---")
    print(nodes_markdown[0].get_content().strip()[:500] + "...")
    
    print("\n--- Échantillon Stratégie B (Chunk #3 Markdown par section) ---")
    if len(nodes_markdown) > 2:
        print(nodes_markdown[2].get_content().strip()[:800] + "...")
    else:
        print("Pas assez de chunks pour afficher le chunk #3")
    
    print("\n--- Structure des 10 premiers chunks Markdown ---")
    for i, node in enumerate(nodes_markdown[:10], start=1):
        content = node.get_content().strip()
        first_line = content.split("\n")[0]
        print(f"Chunk #{i} ({len(content)} chars) : {first_line[:80]}...")
    
    # Sauvegarde des chunks Markdown en JSON pour l'indexation Qdrant
    chunks_json = []
    for i, node in enumerate(nodes_markdown, start=1):
        chunks_json.append({
            "chunk_id": f"k230_markdown_chunk_{i}",
            "source_file": sample_file.name,
            "chunk_index": i,
            "title": node.metadata.get("heading", ""),
            "content": node.get_content(),
            "char_length": len(node.get_content()),
            "metadata": {
                "parser": "MarkdownNodeParser",
                "source": str(sample_file),
            }
        })
    
    output_file = output_dir / "k230_markdown_chunks.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chunks_json, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ {len(chunks_json)} chunks Markdown sauvegardés dans : {output_file}")
    print(f"Format : JSON")
    print(f"Prêt pour l'indexation Qdrant")


if __name__ == "__main__":
    run_k230_markdown_chunking()
