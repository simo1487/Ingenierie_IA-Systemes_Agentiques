"""Technique 3 : Découpage Hiérarchique Parent-Enfant (HierarchicalNodeParser).

Principe :
- Découpe le texte sur plusieurs niveaux emboîtés (ex: parents de 512 tokens, enfants de 128 tokens).
- Les nœuds feuilles (enfants) sont utilisés pour la recherche fine et précise.
- Les nœuds parents correspondants sont récupérés pour fournir le contexte global au modèle.
"""

from __future__ import annotations

from llama_index.core import Document
from llama_index.core.node_parser import HierarchicalNodeParser, get_leaf_nodes


def demonstrate_hierarchical_chunking(
    text: str,
    chunk_sizes: list[int] | None = None,
) -> dict:
    """Découpe un document en arborescence parent/enfant."""
    chunk_sizes = chunk_sizes or [512, 128]
    doc = Document(
        text=text,
        metadata={"source": "01_normes_automobile.md", "baseline": "ASPICE-v4.0"},
    )

    node_parser = HierarchicalNodeParser.from_defaults(
        chunk_sizes=chunk_sizes,
    )

    all_nodes = node_parser.get_nodes_from_documents([doc])
    leaf_nodes = get_leaf_nodes(all_nodes)

    return {
        "total_nodes": len(all_nodes),
        "leaf_nodes": len(leaf_nodes),
        "all_nodes": all_nodes,
        "leaf_nodes_list": leaf_nodes,
    }


if __name__ == "__main__":
    sample_text = (
        "# Chapitre 1 : Spécification des exigences logicielles (SWE.1)\n\n"
        "L'objectif de l'analyse des exigences logicielles est de transformer les exigences "
        "système allouées au logiciel en un ensemble structuré d'exigences logicielles vérifiables.\n\n"
        "## Base Practice SWE.1.BP1 : Elicitation\n"
        "Utiliser les exigences système et les attentes d'architecture pour documenter les besoins.\n\n"
        "## Base Practice SWE.1.BP2 : Structuration\n"
        "Structurer les exigences par domaine fonctionnel, sécurité et performance.\n\n"
        "# Chapitre 2 : Conception détaillée (SWE.3)\n\n"
        "Définir la structure interne de chaque unité logicielle, ses interfaces et ses invariants."
    )

    print("=== DÉMONSTRATION : HierarchicalNodeParser (Parent-Enfant) ===")
    result = demonstrate_hierarchical_chunking(sample_text, chunk_sizes=[256, 64])
    print(f"Total nœuds créés : {result['total_nodes']}")
    print(f"Nœuds feuilles (enfants indexés) : {result['leaf_nodes']}")

    for idx, node in enumerate(result["leaf_nodes_list"], start=1):
        parent_id = node.parent_node.node_id if node.parent_node else "None"
        print(f"\n--- Enfant #{idx} (Parent ID: {parent_id}) ---")
        print(node.get_content())
