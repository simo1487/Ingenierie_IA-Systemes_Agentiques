#!/usr/bin/env python3
"""Collecter des URLs de projets automobiles liés au contrôle moteur électrique via SearXNG.

Le script interroge l'API JSON d'une instance SearXNG configurée par l'utilisateur.
Il produit un inventaire dédoublonné et conserve la requête, la page de résultats,
les moteurs et les métadonnées renvoyées pour permettre une vérification ultérieure.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

SCRIPT_VERSION = "1.1.0"
DEFAULT_QUERIES = (
    'automobile "electric motor control" open source project',
    'automotive "motor control" open source software',
    'vehicle "electric drive" control open source',
    'automotive inverter control software open source',
    'EV motor controller open source project',
    'embedded automotive motor control GitHub',
    'automobile "contrôle moteur électrique" logiciel open source',
    'véhicule électrique commande moteur logiciel open source',
    'automobile "Steuerung von Elektromotoren" Open-Source-Projekt',
    'Automobil "Motorsteuerung" Open-Source-Software',
    'automoción "control de motor eléctrico" proyecto de código abierto',
    'vehículo eléctrico control del motor software de código abierto',
    'automotive "controllo del motore elettrico" progetto open source',
    'veicolo elettrico controllo motore software open source',
    'automotivo "controle de motor elétrico" projeto open source',
    'veículo elétrico controle do motor software de código aberto',
    'auto "regeling van elektromotoren" open source project',
    'motoryzacja "sterowanie silnikiem elektrycznym" projekt open source',
    'автомобиль управление электродвигателем проект с открытым исходным кодом',
    '自動車 電動モーター 制御 オープンソース プロジェクト',
    '汽车 电动机 控制 开源 项目',
    '자동차 전기 모터 제어 오픈 소스 프로젝트',
)


@dataclass
class SearchResult:
    url: str
    title: str
    snippet: str
    query: str
    page: int
    engines: tuple[str, ...]
    category: str
    published_date: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"URL HTTP(S) invalide: {url}")
    path = parsed.path or "/"
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, "")
    )


def search_endpoint(instance_url: str) -> str:
    parsed = urllib.parse.urlsplit(instance_url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("L'URL SearXNG doit utiliser HTTP(S) et contenir un hôte.")
    path = parsed.path.rstrip("/")
    if not path.endswith("/search"):
        path = f"{path}/search"
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, "", ""))


def _text(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


def parse_results(payload: object, query: str, page: int) -> list[SearchResult]:
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        return []

    results: list[SearchResult] = []
    for item in payload["results"]:
        if not isinstance(item, dict):
            continue
        try:
            url = normalize_url(_text(item.get("url")))
        except ValueError:
            continue
        engines = item.get("engines", [])
        if not isinstance(engines, list):
            engines = []
        results.append(
            SearchResult(
                url=url,
                title=_text(item.get("title")),
                snippet=_text(item.get("content")),
                query=query,
                page=page,
                engines=tuple(sorted({engine for engine in engines if isinstance(engine, str)})),
                category=_text(item.get("category")),
                published_date=_text(item.get("publishedDate")),
            )
        )
    return results


def query_searxng(
    instance_url: str,
    query: str,
    page: int,
    results_per_page: int,
    timeout: float,
    user_agent: str,
) -> list[SearchResult]:
    endpoint = search_endpoint(instance_url)
    params = {
        "q": query,
        "format": "json",
        "pageno": str(page),
        "language": "all",
        "categories": "general",
        "results_on_new_tab": "0",
    }
    if results_per_page > 0:
        params["number_of_results"] = str(results_per_page)
    request_url = f"{endpoint}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        request_url,
        headers={"Accept": "application/json", "User-Agent": user_agent},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        payload = json.loads(response.read().decode(charset))
    return parse_results(payload, query, page)


def deduplicate(results: Sequence[SearchResult]) -> list[SearchResult]:
    unique: dict[str, SearchResult] = {}
    for result in results:
        if result.url not in unique:
            unique[result.url] = result
            continue
        current = unique[result.url]
        unique[result.url] = SearchResult(
            url=current.url,
            title=current.title or result.title,
            snippet=current.snippet or result.snippet,
            query=current.query,
            page=current.page,
            engines=tuple(sorted(set(current.engines) | set(result.engines))),
            category=current.category or result.category,
            published_date=current.published_date or result.published_date,
        )
    return list(unique.values())


def write_json(path: Path, instance_url: str, queries: Sequence[str], pages: int, results: Sequence[SearchResult]) -> None:
    payload = {
        "script_version": SCRIPT_VERSION,
        "extracted_at": utc_now(),
        "searxng_instance": instance_url,
        "queries": list(queries),
        "pages_requested_per_query": pages,
        "scope": "Résultats renvoyés par SearXNG pour les requêtes configurées; cette collecte ne constitue pas une preuve d'exhaustivité du Web.",
        "results_count": len(results),
        "results": [
            {
                **asdict(result),
                "engines": list(result.engines),
            }
            for result in results
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, results: Sequence[SearchResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["url", "title", "snippet", "query", "page", "engines", "category", "published_date"],
        )
        writer.writeheader()
        for result in results:
            row = asdict(result)
            row["engines"] = ",".join(result.engines)
            writer.writerow(row)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--searxng-url",
        default=os.getenv("SEARXNG_URL"),
        help="URL de l'instance SearXNG; peut aussi être fournie par SEARXNG_URL",
    )
    parser.add_argument(
        "--query",
        action="append",
        default=[],
        help="Requête supplémentaire ou personnalisée; répétable",
    )
    parser.add_argument("--pages", type=int, default=3, help="Nombre de pages SearXNG par requête")
    parser.add_argument(
        "--results-per-page",
        type=int,
        default=0,
        help="Nombre demandé par page; 0 laisse l'instance appliquer sa configuration",
    )
    parser.add_argument("--timeout", type=float, default=20.0, help="Timeout HTTP en secondes")
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path(__file__).with_name("output") / "sites.json",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=Path(__file__).with_name("output") / "sites.csv",
    )
    parser.add_argument(
        "--user-agent",
        default="logiciel-automobile-open-source-url-search/1.0",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.searxng_url:
        print("Fournir --searxng-url ou définir SEARXNG_URL.", file=sys.stderr)
        return 2
    if args.pages < 1 or args.results_per_page < 0 or args.timeout <= 0:
        print("--pages doit être >= 1, --results-per-page >= 0 et --timeout > 0.", file=sys.stderr)
        return 2

    try:
        endpoint = search_endpoint(args.searxng_url)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    queries = tuple(dict.fromkeys((*DEFAULT_QUERIES, *args.query)))
    collected: list[SearchResult] = []
    for query in queries:
        for page in range(1, args.pages + 1):
            try:
                page_results = query_searxng(
                    endpoint,
                    query,
                    page,
                    args.results_per_page,
                    args.timeout,
                    args.user_agent,
                )
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                print(f"Recherche échouée pour la requête {query!r}, page {page}: {exc}", file=sys.stderr)
                continue
            collected.extend(page_results)
            if not page_results:
                break

    results = deduplicate(collected)
    write_json(args.output_json, endpoint, queries, args.pages, results)
    write_csv(args.output_csv, results)
    print(f"{len(results)} URL(s) unique(s) écrite(s) dans {args.output_json} et {args.output_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
