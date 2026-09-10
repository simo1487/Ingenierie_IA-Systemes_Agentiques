#!/usr/bin/env python3
"""Génère des spécifications de feature Zephyr OS à partir du document de traçabilité."""

import os
import re
from datetime import date

ROOT = "C:\\Users\\Florian\\Documents\\Formation_IA_agentique"
SOURCE = os.path.join(ROOT, "zephyr-os-requirements-traceability.md")
OUTPUT_DIR = os.path.join(ROOT, "features", "zephyr-os")


def slugify(text):
    """Convertit un texte en nom de fichier valide (sans caractères spéciaux)."""
    text = text.lower()
    replacements = {
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "â": "a", "ä": "a",
        "ù": "u", "û": "u", "ü": "u",
        "ô": "o", "ö": "o",
        "î": "i", "ï": "i",
        "ç": "c",
        "&": "and",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    text = re.sub(r"[^a-z0-9 -]", "", text)
    text = re.sub(r"[ -]+", "-", text.strip())
    return text


def parse_requirements(path):
    """Extrait les exigences organisées par catégorie depuis le document de traçabilité."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    categories = {}
    current_category = None

    for line in content.splitlines():
        cat_match = re.match(r"^### (2\.\d+) (.+)$", line)
        if cat_match:
            current_category = cat_match.group(2).strip()
            categories[current_category] = []
            continue

        req_match = re.match(
            r"^\|\s*(ZEP-[A-Z]+-\d+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*(P\d)\s*\|\s*([^|]+)\s*\|$",
            line,
        )
        if req_match and current_category:
            req_id = req_match.group(1).strip()
            sub_category = req_match.group(2).strip()
            description = req_match.group(3).strip()
            priority = req_match.group(4).strip()
            source = req_match.group(5).strip()
            categories[current_category].append(
                {
                    "id": req_id,
                    "sub_category": sub_category,
                    "description": description,
                    "priority": priority,
                    "source": source,
                }
            )

    return categories


def generate_feature_spec(category, requirements):
    """Génère le contenu d'une spécification de feature selon le template."""
    feature_id = f"FEAT-{requirements[0]['id'].split('-')[1]}"
    feature_name = category
    file_name = f"{slugify(category)}.md"

    req_rows = "\n".join(
        f"| {r['id']} | {r['sub_category']} | {r['description']} | {r['priority']} | {r['source']} |"
        for r in requirements
    )

    trace_rows = "\n".join(
        f"| {r['id']} | zephyr-os-requirements-traceability.md | Implémente exigence système | Section {r['source']} | Candidat |"
        for r in requirements
    )

    scenario_rows = "\n".join(
        f"| Vérification {r['id']} | CA-00{i+1} | {r['source']} | Retour d'appel API / logs | Candidat |"
        for i, r in enumerate(requirements)
    )

    acceptance_criteria = "\n".join(
        f"- [ ] {r['id']} : {r['description']}"
        for r in requirements
    )

    gherkin_scenarios = "\n\n".join(
        f"""  Scénario: {r['id']} - Cas nominal
    Étant donné que le système est initialisé avec les APIs {r['sub_category']} disponibles
    Quand l'application appelle la fonction associée à "{r['description']}"
    Alors l'opération est exécutée selon la spécification {r['source']}
    Et aucune erreur fatale n'est levée"""
        for r in requirements
    )

    gherkin_boundary = "\n\n".join(
        f"""  Scénario: {r['id']} - Cas limite
    Étant donné que le système est dans un état de charge maximale pour {r['sub_category']}
    Quand l'application appelle la fonction associée à "{r['description']}"
    Alors l'opération reste déterministe et retourne un statut cohérent"""
        for r in requirements[:2]
    )

    gherkin_error = "\n\n".join(
        f"""  Scénario: {r['id']} - Cas d'erreur
    Étant donné que l'appel est réalisé avec des paramètres invalides ou hors contexte
    Quand l'application appelle la fonction associée à "{r['description']}"
    Alors le système retourne une erreur et n'altère pas l'état global"""
        for r in requirements[:2]
    )

    return f"""# Feature : {feature_name}

## 1. Informations générales

- **Identifiant :** `{feature_id}`
- **Nom de la feature :** `{feature_name}`
- **Responsable(s) :** `Shengjie, Mohamed, Florian`
- **Priorité :** `P0`
- **Statut :** `En cours`
- **Date :** `{date.today().isoformat()}`

## 2. Objectif

Cette feature permet de fournir les services {feature_name.lower()} du RTOS Zephyr afin de supporter l'exécution sûre et déterministe des applications embarquées automobiles.

## 3. Besoin utilisateur

> En tant que développeur de systèmes embarqués automobiles, je veux disposer des services {feature_name.lower()} de Zephyr OS, afin de concevoir des applications temps réel traçables et conformes aux normes ISO 26262 / Automotive SPICE.

## 4. Contexte et problème

- **Situation actuelle :** Les exigences {feature_name.lower()} de Zephyr OS sont documentées dans le repository `zephyrproject-rtos/reqmgmt` mais ne sont pas formalisées sous forme de features traçables pour un projet automobile.
- **Problème rencontré :** L'absence de spécification de feature par exigence complique la traçabilité vers les tests et la conformité ISO 26262 / SPICE.
- **Décision qui reste humaine :** Choix des exigences P0/P1 à implémenter selon le projet et le niveau ASIL visé.
- **Question ouverte :** Version exacte de Zephyr RTOS à laquelle ces exigements correspondent.

## 5. Périmètre

### Inclus

- Implémentation / utilisation des APIs Zephyr relatives à {feature_name.lower()}.
- Traçabilité de chaque exigence vers les tests et les normes.
- Documentation des cas nominal, limite et d'erreur.

### Exclus

- Développement du code source du noyau Zephyr lui-même (sauf si portage nécessaire).
- Certification formelle ISO 26262 / ASIL (hors périmètre, à gérer par projet).

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Exigences {feature_name} | `zephyr-os-requirements-traceability.md` | 2026-09-08 | En cours | Lecture |
| Documentation Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt` | 2024-2026 | À vérifier | Lecture |

## 7. Sorties attendues

- Fichier de spécification de feature formalisé ({file_name}).
- Traçabilité des exigences {feature_name.lower()} vers tests et normes.
- Scénarios Gherkin candidats pour la validation.

> Ces sorties sont des **propositions** à valider par l'équipe et le responsable safety/qualité.

## 8. Règles métier et contraintes

- Respect des priorités P0/P1/P2 définies dans le document de traçabilité.
- Exigences P0 à couvrir prioritairement pour un MVP safety-critical.
- Mapping ISO 26262 / SPICE à compléter avec le safety manager.
- Source des exigences issue du repository `zephyrproject-rtos/reqmgmt` (travail préliminaire, non lié à une version Zephyr spécifique).

## 9. Critères d'acceptation

{acceptance_criteria}
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve ou conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: {feature_name}

  Contexte:
    Étant donné que le système Zephyr OS est initialisé
    Et les services {feature_name.lower()} sont compilés et chargés

{gherkin_scenarios}

{gherkin_boundary}

{gherkin_error}
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
{scenario_rows}

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
{trace_rows}

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

1. Compiler un exemple Zephyr utilisant les APIs {feature_name.lower()}.
2. Exécuter les tests unitaires / d'intégration associés.
3. Vérifier la présence des exigences dans le code source et la documentation Zephyr.

- **Environnement :** Zephyr SDK (version à préciser par projet), board cible compatible.
- **Données utilisées :** Exemples de test Zephyr (`samples/`) et tests existants (`tests/kernel/`).
- **Résultat attendu :** Les APIs se comportent conformément au document de traçabilité.
- **Limites de la vérification :** Ne prouve pas la conformité ISO 26262 ni le niveau ASIL.

## 13. Dépendances et risques

### Dépendances

- Disponibilité d'un environnement de build Zephyr fonctionnel.
- Sélection d'une version Zephyr et d'une board cible.
- Définition des niveaux ASIL cibles par le safety manager.

### Risques

| Risque | Impact | Probabilité | Mesure de maîtrise | Responsable |
|---|---|---|---|---|
| Exigences non couvertes par tests existants | fort | moyen | Identifier gaps et ajouter tests | Florian |
| Version Zephyr non figée | moyen | moyen | Documenter la version retenue | Shengjie |
| Mapping normes incomplet | fort | moyen | Relecture safety manager | Mohamed |

## 14. Décision de revue

- **Relecteur(s) :** Safety / Quality team
- **Date de revue :** `[AAAA-MM-JJ]`
- **Décision :** `[Acceptée / À corriger / Bloquée]`
- **Corrections demandées :** `[Liste des corrections]`
- **Points restant ouverts :** Version exacte de Zephyr RTOS, niveaux ASIL cibles.

## Checklist finale

- [ ] Le besoin utilisateur est compréhensible.
- [ ] Le périmètre et les exclusions sont explicites.
- [ ] Les entrées et leurs versions sont identifiées.
- [ ] Les sorties sont distinguées des preuves.
- [ ] Les critères d'acceptation sont observables.
- [ ] Il existe au moins un scénario nominal.
- [ ] Il existe au moins un scénario frontière, erreur ou refus.
- [ ] Chaque scénario possède un attendu et un oracle.
- [ ] Les relations de traçabilité sont sourcées.
- [ ] Les inconnues ne sont pas inventées.
- [ ] La vérification est reproductible par une autre personne.
- [ ] Les limites et risques sont documentés.

---

## Exigences couvertes

| ID Exigence | Sous-catégorie | Description | Priorité | Source |
|---|---|---|---|---|
{req_rows}
""", file_name


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    categories = parse_requirements(SOURCE)
    generated = []

    for category, requirements in categories.items():
        if not requirements:
            continue
        content, file_name = generate_feature_spec(category, requirements)
        path = os.path.join(OUTPUT_DIR, file_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        generated.append(path)

    print(f"Généré {len(generated)} fichiers de feature dans {OUTPUT_DIR}:")
    for p in generated:
        print(f"  - {p}")


if __name__ == "__main__":
    main()
