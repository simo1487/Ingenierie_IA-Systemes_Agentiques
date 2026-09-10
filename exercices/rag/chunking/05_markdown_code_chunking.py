"""Technique 5 : Découpage Structurel Markdown et Code (MarkdownNodeParser & CodeSplitter).

Principe :
- MarkdownNodeParser : respecte la hiérarchie des titres Markdown (`#`, `##`, `###`).
  Chaque section d'exigence devient un chunk autonome qui conserve son titre et son UID dans les métadonnées.
- CodeSplitter : découpe du code C ou Python en préservant les fonctions et les blocs logiques.
"""

from __future__ import annotations

from llama_index.core import Document
from llama_index.core.node_parser import MarkdownNodeParser, CodeSplitter


def demonstrate_markdown_parser(markdown_text: str) -> list[dict]:
    """Découpe un document Markdown par titres de sections."""
    doc = Document(text=markdown_text, metadata={"source": "01_normes_automobile.md"})

    parser = MarkdownNodeParser.from_defaults()
    nodes = parser.get_nodes_from_documents([doc])

    results = []
    for idx, node in enumerate(nodes, start=1):
        header_path = [v for k, v in node.metadata.items() if k.startswith("Header")]
        results.append({
            "chunk_index": idx,
            "header_path": " > ".join(header_path) if header_path else "Root",
            "content": node.get_content(),
            "metadata": node.metadata,
        })
    return results


def demonstrate_code_splitter(code_text: str, language: str = "c") -> list[dict]:
    """Découpe un fichier source de code C en blocs fonctionnels."""
    doc = Document(text=code_text, metadata={"source": "defect.c", "lang": language})

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
        }
        for idx, node in enumerate(nodes, start=1)
    ]


if __name__ == "__main__":
    sample_markdown = (
        "# Spécification Logicielle\n\n"
        "Introduction générale du système embarqué.\n\n"
        "## SWE.1.BP1 : Elicitation\n"
        "L'équipe collecte les exigences système et les trace.\n\n"
        "## SWE.1.BP2 : Analyse\n"
        "L'équipe analyse la faisabilité technique et le risque sécurité."
    )

    print("=== DÉMONSTRATION : MarkdownNodeParser ===")
    md_chunks = demonstrate_markdown_parser(sample_markdown)
    for c in md_chunks:
        print(f"\n--- Section : {c['header_path']} ---")
        print(c["content"])

    sample_c_code = (
        "#include <stdio.h>\n"
        "#include <string.h>\n\n"
        "void check_buffer(const char *input) {\n"
        "    char local_buf[16];\n"
        "    strncpy(local_buf, input, sizeof(local_buf) - 1);\n"
        "    local_buf[sizeof(local_buf) - 1] = '\\0';\n"
        "    printf(\"Buffer contenu: %s\\n\", local_buf);\n"
        "}\n\n"
        "int main(void) {\n"
        "    check_buffer(\"Test unitaire safe\");\n"
        "    return 0;\n"
        "}\n"
    )

    print("\n=== DÉMONSTRATION : CodeSplitter (Langage C) ===")
    code_chunks = demonstrate_code_splitter(sample_c_code, language="c")
    for c in code_chunks:
        print(f"\n--- Code Chunk #{c['chunk_index']} ({c['line_count']} lignes) ---")
        print(c["content"])
