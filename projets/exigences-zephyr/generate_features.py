#!/usr/bin/env python3
"""Génère les fiches de feature Zephyr par catégorie dans projets/exigences-zephyr."""

import re
from pathlib import Path
from collections import defaultdict

CORPUS = Path(__file__).parent / "corpus-exigences-zephyr.md"
OUTPUT_DIR = Path(__file__).parent / "features"


def slugify(text):
    text = text.lower().replace(" ", "-").replace("&", "and")
    text = re.sub(r"[^a-z0-9-]", "", text)
    return re.sub(r"-+", "-", text.strip("-"))


def parse_corpus_table(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    table_match = re.search(r"\n## 3\. Corpus des exigences\n\n(.*?)(?=\n## )", content, re.DOTALL)
    if not table_match:
        return []

    lines = [l for l in table_match.group(1).splitlines() if l.startswith("| ZEP-SRS")]
    requirements = []
    for line in lines:
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 10:
            continue
        requirements.append(
            {
                "requirement_id": cells[0],
                "requirement_text": cells[1],
                "source_repository": cells[2],
                "source_revision": cells[3],
                "source_path": cells[4],
                "category": cells[5],
                "implementation_links": cells[6],
                "test_links": cells[7],
                "automotive_mapping": cells[8],
                "status": cells[9],
            }
        )
    return requirements


def get_category(path_cell):
    file_part = path_cell.split(" (UID")[0].strip()
    name = Path(file_part).stem.replace("_", " ").title()
    return name


def generate_feature_spec(category, requirements):
    file_name = f"{slugify(category)}.md"
    feature_id = f"FEAT-{category.replace(' ', '-').replace('&', 'and')[:30].upper()}"

    rows = "\n".join(
        f"| {r['requirement_id']} | {r['requirement_text']} | {r['source_repository']} | "
        f"{r['source_revision']} | {r['source_path']} | {r['category']} | "
        f"{r['implementation_links']} | {r['test_links']} | {r['automotive_mapping']} | {r['status']} |"
        for r in requirements
    )

    critères = "\n".join(
        f"- [ ] `CA-{r['requirement_id']}` : l'UID {r['requirement_id']} est retrouvable dans {r['source_path']}."
        for r in requirements
    )
    critères += "\n- [ ] Les sources, révisions et chemins sont conservés sans modification."
    critères += "\n- [ ] Les liens vers code et tests sont distingués des hypothèses (marqués Non déterminé si absent)."
    critères += "\n- [ ] Les correspondances automobile restent candidates sans revue spécialisée."
    critères += "\n- [ ] Les inconnues restent explicitement ouvertes."

    return f"""# Feature — {category}

## 1. Informations générales

- **Identifiant :** `{feature_id}`
- **Nom de la feature :** `{category}`
- **Responsable(s) :** `Mohammed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `2026-09-09`
- **Branche :** `feat_getReq`

## 2. Objectif

Constituer un corpus traçable des exigences Zephyr RTOS de la catégorie **{category}** afin d'évaluer leur applicabilité au projet fil rouge automobile sans inventer de conformité.

## 3. Besoin utilisateur

> En tant qu'ingénieur exigences, je veux retrouver les exigences {category} de Zephyr avec leurs identifiants originaux, leurs sources figées et leurs liens vérifiés, afin de les utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des exigences de la catégorie **{category}** dans `zephyrproject-rtos/reqmgmt`.
- Extraction des identifiants, textes, catégories et relations explicitement disponibles.
- Conservation de la révision et du chemin source.
- Proposition séparée de correspondances automobiles (statut Candidat).

### Exclus

- Création d'une exigence absente des sources.
- Attribution automatique d'une conformité à une norme automobile.
- Confusion entre documentation d'API, comportement observé et exigence normative.

## 5. Schéma minimal

| Champ | Attendu |
|---|---|
| `requirement_id` | Identifiant original, sans renumérotation silencieuse |
| `requirement_text` | Texte source ou reformulation signalée |
| `source_repository` | Dépôt officiel ou source justifiée |
| `source_revision` | Tag ou SHA exact |
| `source_path` | Fichier et section ou ligne |
| `category` | Catégorie documentée |
| `implementation_links` | Liens observés vers le code |
| `test_links` | Liens observés vers les tests |
| `automotive_mapping` | Proposition séparée et justifiée |
| `status` | Observé, candidat, vérifié, non vérifié ou bloqué |

## 6. Exigences couvertes

| requirement_id | requirement_text | source_repository | source_revision | source_path | category | implementation_links | test_links | automotive_mapping | status |
|---|---|---|---|---|---|---|---|---|---|
{rows}

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n'est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu'ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidat` sans revue spécialisée.
- Les exigences introuvables sont marquées `Non vérifié`, jamais reconstituées comme certaines.

## 8. Critères d'acceptation

{critères}

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Vérifier les exigences {category}

  Scénario: Exigence retrouvée
    Étant donné une exigence associée à un dépôt, une révision et un chemin
    Quand un relecteur ouvre la source indiquée
    Alors il retrouve le passage correspondant
    Et peut confirmer ou refuser le statut Vérifié

  Scénario: Lien code ou test manquant
    Étant donné une exigence sans lien observable vers le code ou les tests
    Quand la recherche ne trouve pas de correspondance
    Alors le champ reste Non déterminé
    Et l'exigence n'est pas utilisée comme preuve de traçabilité

  Scénario: Correspondance automobile proposée
    Étant donné une exigence Zephyr observée
    Quand un agent propose un lien vers ISO 26262
    Alors ce lien est enregistré séparément avec le statut Candidat
    Et nécessite une revue humaine spécialisée
```

## 10. Définition de terminé

Le travail est terminé lorsqu'un tiers peut retrouver les exigences ci-dessus dans la révision indiquée, distinguer les liens observés des hypothèses et reproduire l'extraction sans dépendre du contexte conversationnel de l'agent.
""", file_name


def main():
    requirements = parse_corpus_table(CORPUS)
    grouped = defaultdict(list)
    for r in requirements:
        grouped[get_category(r["source_path"])].append(r)

    OUTPUT_DIR.mkdir(exist_ok=True)

    for category, reqs in grouped.items():
        content, file_name = generate_feature_spec(category, reqs)
        out_path = OUTPUT_DIR / file_name
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Généré : {out_path}")

    print(f"\nTotal : {len(grouped)} features générées")


if __name__ == "__main__":
    main()
