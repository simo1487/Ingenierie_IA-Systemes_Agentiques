#!/usr/bin/env python3

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

try:
    import tomllib
except ModuleNotFoundError:
    tomllib = None

ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_SIZE = 5 * 1024 * 1024
SKIPPED_CONTENT_PARTS = {"node_modules", "sources-downloads", ".git"}
TEXT_SUFFIXES = {
    ".c", ".cc", ".cmake", ".cpp", ".csv", ".h", ".hpp", ".html", ".ini",
    ".java", ".js", ".json", ".jsx", ".md", ".mjs", ".py", ".rst", ".sdoc",
    ".sh", ".toml", ".ts", ".tsx", ".txt", ".xml", ".yaml", ".yml",
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CONFLICT_MARKER = re.compile(r"^(<<<<<<<|=======|>>>>>>>)")


def git(*args: str, input_data: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args], cwd=ROOT, input=input_data, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )


def selected_paths(staged: bool) -> list[PurePosixPath]:
    args = ("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z") if staged else (
        "ls-files", "--cached", "--others", "--exclude-standard", "-z"
    )
    result = git(*args)
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return [PurePosixPath(value.decode("utf-8")) for value in result.stdout.split(b"\0") if value]


def content_for(path: PurePosixPath, staged: bool) -> bytes:
    if staged:
        result = git("show", f":{path.as_posix()}")
        if result.returncode:
            raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
        return result.stdout
    return (ROOT / path.as_posix()).read_bytes()


def is_generated_or_vendor(path: PurePosixPath) -> bool:
    return bool(SKIPPED_CONTENT_PARTS.intersection(path.parts))


def is_text(path: PurePosixPath, content: bytes) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"Makefile", "pre-commit"} or content.startswith(b"#!")


def check_path(path: PurePosixPath, content: bytes, staged: bool) -> list[str]:
    errors: list[str] = []
    name = path.name.lower()
    if "upstream" in path.parts and staged:
        errors.append("source protégée upstream modifiée")
    if name == ".env" or name.startswith(".env.") or name in {"id_rsa", "id_ed25519", "credentials.json"} or path.suffix.lower() == ".key":
        errors.append("fichier sensible interdit")
    if len(content) > MAX_FILE_SIZE:
        errors.append(f"fichier supérieur à {MAX_FILE_SIZE // (1024 * 1024)} Mio")
    if is_generated_or_vendor(path) or not is_text(path, content) or b"\0" in content:
        return errors
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError as error:
        return [*errors, f"encodage non UTF-8 ({error})"]
    if text and not text.endswith("\n"):
        errors.append("fin de fichier sans saut de ligne")
    for number, line in enumerate(text.splitlines(), 1):
        if CONFLICT_MARKER.match(line):
            errors.append(f"ligne {number}: marqueur de conflit Git")
        trailing = line[len(line.rstrip(" \t")):]
        if trailing and not (path.suffix.lower() == ".md" and trailing == "  "):
            errors.append(f"ligne {number}: espaces finaux")
    try:
        if path.suffix.lower() == ".json":
            json.loads(text)
        elif path.suffix.lower() == ".py":
            ast.parse(text, filename=path.as_posix())
        elif path.suffix.lower() == ".toml" and tomllib is not None:
            tomllib.loads(text)
    except (SyntaxError, json.JSONDecodeError, ValueError) as error:
        errors.append(f"syntaxe invalide: {error}")
    if path.suffix.lower() == ".sh" or text.startswith("#!/usr/bin/env sh") or text.startswith("#!/bin/sh") or text.startswith("#!/usr/bin/env bash"):
        result = subprocess.run(["bash", "-n"], input=content, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if result.returncode:
            errors.append(f"syntaxe shell invalide: {result.stderr.decode('utf-8', errors='replace').strip()}")
    if path.suffix.lower() == ".md":
        errors.extend(check_markdown_links(path, text))
    return errors


def check_markdown_links(path: PurePosixPath, text: str) -> list[str]:
    errors: list[str] = []
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")) or any(char in target for char in "[]{}"):
            continue
        relative = unquote(target.split("#", 1)[0])
        resolved = (ROOT / path.parent.as_posix() / relative).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"lien local hors dépôt: {raw_target}")
            continue
        if not resolved.exists():
            errors.append(f"lien local introuvable: {raw_target}")
    return errors


def check_structure() -> list[tuple[PurePosixPath, list[str]]]:
    failures: list[tuple[PurePosixPath, list[str]]] = []
    required = ["README.md", "AGENTS.md", "CONTRIBUTING.md", "projets/README.md", "specs/README.md", "workflows/README.md"]
    for relative in required:
        if not (ROOT / relative).is_file():
            failures.append((PurePosixPath(relative), ["point d’entrée requis manquant"]))
    projects = ROOT / "projets"
    if projects.is_dir():
        for project in sorted(path for path in projects.iterdir() if path.is_dir() and path.name != "_template"):
            missing = [name for name in ("README.md", "SPEC.md") if not (project / name).is_file()]
            if missing:
                failures.append((PurePosixPath(project.relative_to(ROOT).as_posix()), [f"fichier requis manquant: {name}" for name in missing]))
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Contrôles rapides et sans dépendance du monorepo")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--staged", action="store_true", help="Contrôler les fichiers indexés pour le prochain commit")
    group.add_argument("--all", action="store_true", help="Contrôler les fichiers suivis et nouveaux non ignorés")
    args = parser.parse_args()
    staged = not args.all
    failures: list[tuple[PurePosixPath, list[str]]] = []
    try:
        paths = selected_paths(staged)
        failures.extend(check_structure())
        for path in paths:
            errors = check_path(path, content_for(path, staged), staged)
            if errors:
                failures.append((path, errors))
    except (OSError, RuntimeError) as error:
        print(f"ERREUR: {error}", file=sys.stderr)
        return 2
    if failures:
        print("Contrôles du dépôt en échec:")
        for path, errors in failures:
            print(f"- {path}")
            for error in errors:
                print(f"  - {error}")
        return 1
    scope = "indexés" if staged else "suivis et nouveaux"
    print(f"OK: {len(paths)} fichier(s) {scope} contrôlé(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
