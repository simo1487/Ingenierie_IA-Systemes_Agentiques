"""Configuration et initialisation de Qdrant avec LlamaIndex.

Supporte trois modes de fonctionnement :
1. En mémoire (`:memory:`) : idéal pour les tests unitaires et le prototypage rapide sans dépendance externe.
2. Fichier local (`path`) : stockage persistant local sans conteneur Docker.
3. Serveur distant ou conteneur (`url`) : connexion à une instance Qdrant (par exemple via docker-compose).
"""

from __future__ import annotations

import os
from typing import Any
from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels

from llama_index.core import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

DEFAULT_COLLECTION_NAME = "formation_ia_corpus"
DEFAULT_VECTOR_SIZE = 384  # Taille standard pour les modèles légers type all-MiniLM-L6-v2 ou BAAI/bge-small-en-v1.5


def get_qdrant_client(
    mode: str = "memory",
    location: str | None = None,
    path: str | None = None,
    url: str | None = None,
    api_key: str | None = None,
) -> QdrantClient:
    """Instancie un client Qdrant selon le mode souhaité.

    Args:
        mode: 'memory', 'disk' ou 'server' (défaut: 'memory')
        location: emplacement personnalisé ou ':memory:'
        path: répertoire local de stockage persistant si mode == 'disk'
        url: URL HTTP du serveur Qdrant (ex: 'http://localhost:6333') si mode == 'server'
        api_key: clé d'API éventuelle pour Qdrant Cloud

    Returns:
        QdrantClient initialisé
    """
    mode = os.getenv("QDRANT_MODE", mode).lower()

    if mode == "server":
        target_url = url or os.getenv("QDRANT_URL", "http://localhost:6333")
        target_key = api_key or os.getenv("QDRANT_API_KEY", None)
        return QdrantClient(url=target_url, api_key=target_key)
    elif mode == "disk":
        target_path = path or os.getenv("QDRANT_PATH", "./qdrant_data")
        return QdrantClient(path=target_path)
    else:  # memory
        return QdrantClient(location=location or ":memory:")


def ensure_collection(
    client: QdrantClient,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    vector_size: int = DEFAULT_VECTOR_SIZE,
    distance: qmodels.Distance = qmodels.Distance.COSINE,
    recreate: bool = False,
) -> None:
    """Crée la collection dans Qdrant si elle n'existe pas déjà.

    Args:
        client: instance de QdrantClient
        collection_name: nom de la collection
        vector_size: dimension des vecteurs d'embedding
        distance: fonction de distance (Cosine par défaut)
        recreate: si True, supprime et recrée la collection
    """
    collections = [col.name for col in client.get_collections().collections]

    if recreate and collection_name in collections:
        client.delete_collection(collection_name)
        collections.remove(collection_name)

    if collection_name not in collections:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=qmodels.VectorParams(
                size=vector_size,
                distance=distance,
            ),
        )


def build_storage_context(
    client: QdrantClient,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    vector_size: int = DEFAULT_VECTOR_SIZE,
    recreate: bool = False,
) -> tuple[StorageContext, QdrantVectorStore]:
    """Construit un StorageContext LlamaIndex adossé à Qdrant.

    Returns:
        Tuple (StorageContext, QdrantVectorStore)
    """
    ensure_collection(
        client=client,
        collection_name=collection_name,
        vector_size=vector_size,
        recreate=recreate,
    )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store,
    )

    return storage_context, vector_store
