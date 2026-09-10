"""Chunking K230 adapté depuis 05_markdown_code_chunking.py.

Objectif :
- Découper le K230 datasheet en chunks Markdown cohérents.
- Subdiviser les sections trop longues pour respecter une taille cible ~800 caractères.
- Sauvegarder le résultat au format JSON dans le dossier output.
"""

from __future__ import annotations

import io
import json
import statistics
import sys
from pathlib import Path

from llama_index.core import Document
from llama_index.core.node_parser import MarkdownNodeParser, TokenTextSplitter


def run_k230_adapted_chunking():
    # Set UTF-8 encoding for output
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    current_dir = Path(__file__).resolve().parent
    sample_file = current_dir.parent / "data" / "sample_corpus" / "k230_datasheet.md"
    output_dir = current_dir.parent / "output"
    output_dir.mkdir(exist_ok=True)

    text = sample_file.read_text(encoding="utf-8")
    doc = Document(text=text, metadata={"source": sample_file.name, "type": "datasheet"})

    print("=================================================================")
    print("CHUNKING K230 : MARKDOWN ADAPTÉ AVEC TAILLE CIBLE ~800")
    print("=================================================================")

    target_size = 800
    upper_limit = int(target_size * 1.25)  # 1000
    lower_limit = int(target_size * 0.75)  # 600
    chunk_overlap = 80

    # Étape 1 : Découpage Markdown
    md_parser = MarkdownNodeParser.from_defaults()
    md_nodes = md_parser.get_nodes_from_documents([doc])

    # Étape 2 : Fusionner les petites sections et subdiviser les grandes
    # Objectif : obtenir des chunks entre 600 et 1000 caractères.
    # TokenTextSplitter : 1 token ≈ 2 caractères pour ce contenu technique
    token_target = target_size // 2  # ≈ 400 tokens ≈ 800 caractères
    token_overlap = chunk_overlap // 2
    splitter = TokenTextSplitter(chunk_size=token_target, chunk_overlap=token_overlap)
    final_nodes = []
    buffer = []
    buffer_len = 0

    for node in md_nodes:
        content = node.get_content()

        # Si la section est déjà dans la plage cible, on la garde
        if lower_limit <= len(content) <= upper_limit:
            if buffer:
                # On vide d'abord le buffer de petites sections
                merged = "\n\n".join(n.get_content() for n in buffer)
                merged_doc = Document(text=merged, metadata={"source": sample_file.name, "merged": True})
                final_nodes.extend(splitter.get_nodes_from_documents([merged_doc]) if len(merged) > upper_limit else [merged_doc])
                buffer = []
                buffer_len = 0
            final_nodes.append(node)
        elif len(content) > upper_limit:
            if buffer:
                merged = "\n\n".join(n.get_content() for n in buffer)
                merged_doc = Document(text=merged, metadata={"source": sample_file.name, "merged": True})
                final_nodes.extend(splitter.get_nodes_from_documents([merged_doc]) if len(merged) > upper_limit else [merged_doc])
                buffer = []
                buffer_len = 0
            # Subdiviser les grosses sections
            sub_doc = Document(text=content, metadata=node.metadata)
            sub_nodes = splitter.get_nodes_from_documents([sub_doc])
            final_nodes.extend(sub_nodes)
        else:
            # Petite section : on l'ajoute au buffer
            buffer.append(node)
            buffer_len += len(content)
            if buffer_len >= target_size:
                merged = "\n\n".join(n.get_content() for n in buffer)
                merged_doc = Document(text=merged, metadata={"source": sample_file.name, "merged": True})
                final_nodes.append(merged_doc)
                buffer = []
                buffer_len = 0

    # Vider le buffer restant
    if buffer:
        merged = "\n\n".join(n.get_content() for n in buffer)
        merged_doc = Document(text=merged, metadata={"source": sample_file.name, "merged": True})
        if len(merged) > upper_limit:
            final_nodes.extend(splitter.get_nodes_from_documents([merged_doc]))
        else:
            final_nodes.append(merged_doc)

    lengths = [len(node.get_content()) for node in final_nodes]

    print(f"\nDocument source : {sample_file.name} ({len(text)} caractères)")
    print(f"Paramètres : cible={target_size}, max={upper_limit}, min={lower_limit}, overlap={chunk_overlap}")
    print(f"Sections Markdown initiales : {len(md_nodes)}")
    print(f"Nombre final de chunks : {len(final_nodes)}")
    print(f"Taille moyenne : {statistics.mean(lengths):.0f} caractères")
    print(f"Médiane : {statistics.median(lengths):.0f} caractères")
    print(f"Min : {min(lengths)} caractères")
    print(f"Max : {max(lengths)} caractères")

    within_tolerance = sum(1 for l in lengths if lower_limit <= l <= upper_limit)
    percentage = (within_tolerance / len(lengths)) * 100
    print(f"\nChunks dans la tolérance [{lower_limit}, {upper_limit}] : {within_tolerance}/{len(lengths)} ({percentage:.1f}%)")

    # Étape 3 : Post-processing - fusionner les chunks trop courts (< 300 chars)
    min_size = 300
    merged_nodes = []
    
    i = 0
    while i < len(final_nodes):
        current = final_nodes[i]
        current_content = current.get_content()
        
        if len(current_content) >= min_size:
            merged_nodes.append(current)
            i += 1
        else:
            # Fusionner avec le chunk d'avant si possible, sinon avec le chunk d'après
            if merged_nodes:
                prev_content = merged_nodes[-1].get_content()
                merged_text = prev_content + "\n\n" + current_content
                merged_nodes[-1] = Document(
                    text=merged_text,
                    metadata={**merged_nodes[-1].metadata, "merged_with_next": True}
                )
            elif i + 1 < len(final_nodes):
                next_content = final_nodes[i + 1].get_content()
                merged_text = current_content + "\n\n" + next_content
                final_nodes[i + 1] = Document(
                    text=merged_text,
                    metadata={**final_nodes[i + 1].metadata, "merged_with_prev": True}
                )
            i += 1

    final_nodes = merged_nodes

    # Statistiques après post-processing
    final_lengths = [len(node.get_content()) for node in final_nodes]
    final_mean = statistics.mean(final_lengths)
    final_median = statistics.median(final_lengths)
    final_min = min(final_lengths)
    final_max = max(final_lengths)
    final_within = sum(1 for l in final_lengths if lower_limit <= l <= upper_limit)
    final_percentage = (final_within / len(final_nodes)) * 100

    print(f"\n=== APRES FUSION DES PETITS CHUNKS (min {min_size} chars) ===")
    print(f"Nombre final de chunks : {len(final_nodes)}")
    print(f"Taille moyenne : {final_mean:.0f} caractères")
    print(f"Médiane : {final_median:.0f} caractères")
    print(f"Min : {final_min} caractères")
    print(f"Max : {final_max} caractères")
    print(f"Chunks dans [{lower_limit}, {upper_limit}] : {final_within}/{len(final_nodes)} ({final_percentage:.1f}%)")

    # Sauvegarde en JSON
    chunks_json = []
    for i, node in enumerate(final_nodes, start=1):
        content = node.get_content()
        header_path = [v for k, v in node.metadata.items() if k.startswith("Header")]
        chunks_json.append({
            "chunk_id": f"k230_adapted_chunk_{i}",
            "source_file": sample_file.name,
            "chunk_index": i,
            "header_path": " > ".join(header_path) if header_path else "Root",
            "content": content,
            "char_length": len(content),
            "metadata": {
                "parser": "Adapted: MarkdownNodeParser + TokenTextSplitter + merge_short",
                "target_size": target_size,
                "min_size": min_size,
                "source": str(sample_file),
            }
        })

    output_file = output_dir / "k230_adapted_chunks.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chunks_json, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {len(chunks_json)} chunks sauvegardés dans : {output_file}")

    # Afficher un chunk autour de 800 caractères
    closest_idx = min(range(len(final_lengths)), key=lambda i: abs(final_lengths[i] - target_size))
    print(f"\n--- Chunk #{closest_idx + 1} ({final_lengths[closest_idx]} chars) ---")
    print(final_nodes[closest_idx].get_content()[:500] + "...")


if __name__ == "__main__":
    run_k230_adapted_chunking()
