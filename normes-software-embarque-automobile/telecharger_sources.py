#!/usr/bin/env python3
"""Télécharge les pages référencées dans sources.csv.

Les URL sont récupérées telles quelles : le script ne contourne pas les paywalls
et ne télécharge que les ressources rendues accessibles par les sites officiels.
"""

from __future__ import annotations

import argparse
import csv
import json
import mimetypes
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


USER_AGENT = "Mozilla/5.0 (compatible; normes-software-embarque-automobile/1.0)"

# Certaines pages officielles bloquent l'automatisation alors que leur fichier
# public reste accessible directement. Ces URL ne contournent aucun paywall.
PUBLIC_URL_OVERRIDES = {
    "unece-r155": "https://unece.org/sites/default/files/2023-02/R155e%20(2).pdf",
    "unece-r156": "https://unece.org/sites/default/files/2024-03/R156e%20(2).pdf",
    "unece-r157": "https://unece.org/sites/default/files/2023-12/R157e%20(1).pdf",
    "automotive-spice": "https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf",
}


def extension_for(content_type: str, url: str) -> str:
    """Retourne une extension raisonnable pour la ressource téléchargée."""
    media_type = content_type.split(";", 1)[0].strip().lower()
    extension = mimetypes.guess_extension(media_type)
    if extension:
        return ".html" if extension in {".htm", ".html"} else extension

    suffix = Path(url.split("?", 1)[0]).suffix.lower()
    return suffix if suffix in {".pdf", ".html", ".htm", ".xml", ".txt"} else ".html"


def download_source(source: dict[str, str], output_dir: Path, timeout: float, overwrite: bool) -> dict[str, object]:
    source_id = source["source_id"]
    original_url = source["url"]
    url = PUBLIC_URL_OVERRIDES.get(source_id, original_url)
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,*/*"})
    result: dict[str, object] = {
        "source_id": source_id,
        "url": original_url,
        "download_url": url,
        "title": source.get("titre", ""),
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
    }

    try:
        with urlopen(request, timeout=timeout) as response:
            content_type = response.headers.get("Content-Type", "")
            extension = extension_for(content_type, response.url)
            destination = output_dir / f"{source_id}{extension}"
            result["final_url"] = response.url
            result["content_type"] = content_type
            result["status"] = response.status
            result["path"] = destination.name

            if destination.exists() and not overwrite:
                result["result"] = "skipped"
                result["bytes"] = destination.stat().st_size
                return result

            temporary = destination.with_suffix(destination.suffix + ".part")
            with temporary.open("wb") as file:
                while chunk := response.read(1024 * 1024):
                    file.write(chunk)
            temporary.replace(destination)
            result["result"] = "downloaded"
            result["bytes"] = destination.stat().st_size
            return result
    except HTTPError as error:
        result.update(result="failed", error=f"HTTP {error.code}: {error.reason}")
    except (URLError, TimeoutError, OSError) as error:
        result.update(result="failed", error=str(error))
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=Path(__file__).with_name("sources.csv"), help="Fichier sources.csv")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).with_name("sources-downloads"), help="Dossier de destination")
    parser.add_argument("--timeout", type=float, default=30, help="Délai maximal par requête, en secondes")
    parser.add_argument("--delay", type=float, default=0.5, help="Pause entre deux requêtes, en secondes")
    parser.add_argument("--overwrite", action="store_true", help="Remplacer les fichiers déjà présents")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with args.csv.open(newline="", encoding="utf-8-sig") as file:
        sources = list(csv.DictReader(file))

    results = []
    for index, source in enumerate(sources):
        print(f"[{index + 1}/{len(sources)}] {source['source_id']} ...", end=" ", flush=True)
        result = download_source(source, args.output_dir, args.timeout, args.overwrite)
        results.append(result)
        print(result["result"] + (f" ({result['bytes']} octets)" if "bytes" in result else f": {result['error']}"))
        if index < len(sources) - 1:
            time.sleep(args.delay)

    manifest = {
        "csv": str(args.csv),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results": results,
    }
    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    downloaded = sum(result["result"] == "downloaded" for result in results)
    skipped = sum(result["result"] == "skipped" for result in results)
    failed = sum(result["result"] == "failed" for result in results)
    print(f"\nTerminé : {downloaded} téléchargé(s), {skipped} déjà présent(s), {failed} échec(s).")
    print(f"Manifest : {manifest_path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
