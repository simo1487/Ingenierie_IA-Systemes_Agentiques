"""Validation minimale d'une exigence Zephyr contre le schéma JSON interne.

Cette implémentation ne remplace pas jsonschema : elle couvre les contrôles
nécessaires au cycle TDD en environnement sans dépendance externe.
"""

from __future__ import annotations


class ValidationError(Exception):
    """Levée lorsqu'une exigence ne respecte pas le schéma JSON attendu."""


def _is_type(value, expected):
    """Vérifie qu'une valeur correspond à un type JSON Schema (simple ou liste)."""
    if isinstance(expected, list):
        return any(_is_single_type(value, t) for t in expected)
    return _is_single_type(value, expected)


def _is_single_type(value, expected):
    mapping = {
        "string": str,
        "boolean": bool,
        "array": list,
        "object": dict,
        "integer": int,
        "number": (int, float),
        "null": type(None),
    }
    python_type = mapping.get(expected)
    if python_type is None:
        return True
    return isinstance(value, python_type)


def _check_string_min_length(value, prop):
    min_length = prop.get("minLength")
    if min_length is not None and (not isinstance(value, str) or len(value) < min_length):
        raise ValidationError(
            f"Chaîne trop courte ou absente : attendu >= {min_length} caractères."
        )


def _check_enum(value, prop):
    enum_values = prop.get("enum")
    if enum_values is not None and value not in enum_values:
        raise ValidationError(
            f"Valeur '{value}' non autorisée. Valeurs attendues : {enum_values}."
        )


def validate_requirement(data, schema):
    """Valide un dictionnaire d'exigence contre le schéma fourni.

    :param data: dictionnaire représentant l'exigence
    :param schema: dictionnaire du schéma JSON
    :raises ValidationError: si une contrainte est violée
    """
    if not isinstance(data, dict):
        raise ValidationError("L'exigence doit être un objet JSON.")

    required = schema.get("required", [])
    for field in required:
        if field not in data:
            raise ValidationError(f"Champ requis manquant : {field}.")

    # L'identifiant est le seul champ requis à pouvoir être explicitement null.
    # Tous les autres champs requis doivent être non nuls.
    nullable_required = {"requirement_id"}
    for field in required:
        value = data[field]
        if field not in nullable_required and value is None:
            raise ValidationError(f"Champ requis null : {field}.")

    properties = schema.get("properties", {})
    for field, prop in properties.items():
        if field not in data:
            continue

        value = data[field]
        expected_type = prop.get("type")
        if expected_type is not None and not _is_type(value, expected_type):
            raise ValidationError(
                f"Type invalide pour {field}: {value!r} n'est pas compatible avec {expected_type}."
            )

        if isinstance(value, str):
            _check_string_min_length(value, prop)

        _check_enum(value, prop)
