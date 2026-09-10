"""Technique 3 : Découpage Hiérarchique Parent-Enfant (HierarchicalNodeParser).

Adaptation : prend en entrée le fichier automotive-spice-exigences.md
(Automotive SPICE PAM v4.0 - 211 exigences) au lieu d'un texte codé en dur.

Principe :
- Découpe le texte sur plusieurs niveaux emboîtés (parents / enfants).
- Les nœuds feuilles (enfants) sont utilisés pour la recherche fine et précise.
- Les nœuds parents correspondants sont récupérés pour fournir le contexte global au modèle.

Sortie : NEW_TEXT_RESULTS/03_hierarchical_parent_child.json
"""

from __future__ import annotations

import json
from pathlib import Path

from llama_index.core import Document
from llama_index.core.node_parser import HierarchicalNodeParser, get_leaf_nodes

SOURCE_FILE = (
    Path(__file__).resolve().parents[4]
    / "projets"
    / "normes"
    / "exigences"
    / "automotive-spice-exigences.md"
)
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "NEW_TEXT_RESULTS"


def load_source_text() -> str:
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Fichier source introuvable : {SOURCE_FILE}")
    return SOURCE_FILE.read_text(encoding="utf-8")


def node_to_dict(node) -> dict:
    parent = getattr(node, "parent_node", None)
    return {
        "node_id": node.node_id,
        "parent_id": parent.node_id if parent else None,
        "text": node.get_content(),
        "metadata": node.metadata,
    }


def demonstrate_hierarchical_chunking(
    text: str,
    chunk_sizes: list[int] | None = None,
) -> dict:
    """Découpe le document ASPICE en arborescence parent/enfant."""
    chunk_sizes = chunk_sizes or [2048, 512]
    doc = Document(
        text=text,
        metadata={"source": SOURCE_FILE.name, "norme": "Automotive SPICE PAM v4.0"},
    )

    node_parser = HierarchicalNodeParser.from_defaults(
        chunk_sizes=chunk_sizes,
    )

    all_nodes = node_parser.get_nodes_from_documents([doc])
    leaf_nodes = get_leaf_nodes(all_nodes)

    return {
        "total_nodes": len(all_nodes),
        "leaf_nodes": len(leaf_nodes),
        "all_nodes": [node_to_dict(n) for n in all_nodes],
        "leaf_nodes_list": [node_to_dict(n) for n in leaf_nodes],
    }


if __name__ == "__main__":
    text = load_source_text()
    result = demonstrate_hierarchical_chunking(text, chunk_sizes=[2048, 512])

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "03_hierarchical_parent_child.json"
    payload = {
        "script": "03_hierarchical_parent_child.py",
        "source_file": SOURCE_FILE.name,
        "parameters": {"chunk_sizes": [2048, 512]},
        "total_nodes": result["total_nodes"],
        "leaf_nodes": result["leaf_nodes"],
        "all_nodes": result["all_nodes"],
        "leaf_nodes_list": result["leaf_nodes_list"],
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"OK {out_path} — {result['total_nodes']} nœuds au total, "
        f"{result['leaf_nodes']} nœuds feuilles"
    )
