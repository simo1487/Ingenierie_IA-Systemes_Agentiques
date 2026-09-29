"""Technique 5 : Découpage Structurel Markdown et Code (MarkdownNodeParser & CodeSplitter).

Adaptation : prend en entrée le fichier automotive-spice-exigences.md
(Automotive SPICE PAM v4.0 - 211 exigences) au lieu de textes codés en dur.
Le découpage Markdown est particulièrement adapté ici : chaque exigence (BP ou Outcome)
devient un chunk autonome qui conserve son titre et son UID dans les métadonnées.
Le volet CodeSplitter extrait les blocs de code clôturés (```lang) du fichier source ;
s'il n'y en a pas, la liste des chunks de code est vide.

Sortie : NEW_TEXT_RESULTS/05_markdown_code_chunking.json
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from llama_index.core import Document
from llama_index.core.node_parser import MarkdownNodeParser, CodeSplitter

SOURCE_FILE = (
    Path(__file__).resolve().parents[4]
    / "projets"
    / "normes"
    / "exigences"
    / "automotive-spice-exigences.md"
)
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"

FENCED_CODE_RE = re.compile(r"```(\w+)\n(.*?)```", re.DOTALL)


def load_source_text() -> str:
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Fichier source introuvable : {SOURCE_FILE}")
    return SOURCE_FILE.read_text(encoding="utf-8")


def demonstrate_markdown_parser(markdown_text: str) -> list[dict]:
    """Découpe le document Markdown par titres de sections."""
    doc = Document(text=markdown_text, metadata={"source": SOURCE_FILE.name})

    parser = MarkdownNodeParser.from_defaults()
    nodes = parser.get_nodes_from_documents([doc])

    results = []
    for idx, node in enumerate(nodes, start=1):
        header_path = [v for k, v in node.metadata.items() if k.startswith("Header")]
        if not header_path and node.metadata.get("header_path"):
            # Format LlamaIndex >= 0.12 : métadonnée 'header_path' (ex: "/ACQ.4 - Supplier Monitoring/...")
            header_path = [
                part for part in str(node.metadata["header_path"]).split("/") if part
            ]
        results.append(
            {
                "chunk_index": idx,
                "header_path": " > ".join(header_path) if header_path else "Root",
                "content": node.get_content(),
                "metadata": node.metadata,
            }
        )
    return results


def demonstrate_code_splitter(code_text: str, language: str = "c") -> list[dict]:
    """Découpe un bloc de code en blocs fonctionnels."""
    doc = Document(text=code_text, metadata={"source": SOURCE_FILE.name, "lang": language})

    try:
        splitter = CodeSplitter(
            language=language,
            chunk_lines=15,
            chunk_lines_overlap=3,
            max_chars=400,
        )
        nodes = splitter.get_nodes_from_documents([doc])
        return [
            {
                "chunk_index": idx,
                "content": node.get_content(),
                "line_count": len(node.get_content().splitlines()),
                "method": "tree_sitter_ast",
            }
            for idx, node in enumerate(nodes, start=1)
        ]
    except (ImportError, Exception):
        # Repli sans tree_sitter : découpage par blocs (séparation par doubles sauts)
        raw_blocks = [b.strip() for b in code_text.split("\n\n") if b.strip()]
        return [
            {
                "chunk_index": idx,
                "content": block,
                "line_count": len(block.splitlines()),
                "method": "block_fallback",
            }
            for idx, block in enumerate(raw_blocks, start=1)
        ]


def extract_fenced_code_blocks(text: str) -> list[dict]:
    """Extrait les blocs de code clôturés du fichier Markdown."""
    return [
        {"language": lang.lower() or "text", "code": code.rstrip()}
        for lang, code in FENCED_CODE_RE.findall(text)
    ]


if __name__ == "__main__":
    text = load_source_text()

    md_chunks = demonstrate_markdown_parser(text)

    code_blocks = extract_fenced_code_blocks(text)
    code_chunks = []
    for block in code_blocks:
        code_chunks.extend(
            demonstrate_code_splitter(block["code"], language=block["language"])
        )

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "05_markdown_code_chunking.json"
    payload = {
        "script": "05_markdown_code_chunking.py",
        "source_file": SOURCE_FILE.name,
        "markdown_chunk_count": len(md_chunks),
        "markdown_chunks": md_chunks,
        "fenced_code_blocks_found": len(code_blocks),
        "code_chunk_count": len(code_chunks),
        "code_chunks": code_chunks,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"OK {out_path} — {len(md_chunks)} chunks Markdown, "
        f"{len(code_chunks)} chunks de code ({len(code_blocks)} blocs clôturés trouvés)"
    )
