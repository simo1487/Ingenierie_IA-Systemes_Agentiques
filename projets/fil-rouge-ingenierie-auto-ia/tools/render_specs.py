from __future__ import annotations

import argparse
import json
import os
from pathlib import Path, PurePosixPath

from spec_contracts import ambiguity_ids, validate_alignment, validate_backlog

PROJECT = Path(__file__).resolve().parents[1]
VOWELS = "aàâäeéèêëiîïoôöuùûüyÿh"
DECISION_TABLE_ANCHORS = {
    101: "prévalidation-rm-fil-101",
    203: "mémoire-rm-fil-203",
    301: "lecture-doutil-rm-fil-301",
}
SURFACE_MAP = {
    101: "`src/auto_ai_flow/orchestrator.py`",
    104: "`src/auto_ai_flow/providers.py`",
    305: "`src/auto_ai_flow/agents.py`",
    404: "`src/auto_ai_flow/agents.py`",
    405: "`src/auto_ai_flow/agents.py`",
    501: "`src/auto_ai_flow/orchestrator.py` et `tests/test_cli.py`",
    601: "`src/auto_ai_flow/agents.py`",
}


def final_newline(text: str) -> str:
    return text.rstrip() + "\n"


def relative_link(source: str, target: str, label: str) -> str:
    start = PurePosixPath(source).parent.as_posix()
    relative = os.path.relpath(target, start).replace(os.sep, "/")
    return f"[`{label}`]({relative})"


def story_path(story: dict) -> str:
    return f"specs/epics/{story['epic']}/user-stories/US-FIL-{story['number']}.md"


def feature_path(story: dict) -> str:
    return f"specs/epics/{story['epic']}/features/FEAT-FIL-{story['number']}/FEATURE.md"


def task_path(story: dict, index: int) -> str:
    return f"specs/epics/{story['epic']}/features/FEAT-FIL-{story['number']}/tasks/TASK-FIL-{story['number']}-{index:02}.md"


def case_labels(backlog: dict, story: dict) -> list[str]:
    return story.get("case_labels", backlog["conventions"]["case_labels"])


def task_phases(backlog: dict, story: dict) -> list[str]:
    return story.get("task_phases", backlog["conventions"]["task_phases"])


def tier_label(story: dict) -> str:
    return "Socle formation" if story["tier"] == "socle" else "Extension production"


def need_sentence(story: dict) -> str:
    role_prefix = "En tant qu’" if story["role"][0].lower() in VOWELS else "En tant que "
    benefit_prefix = "d’" if story["benefit"][0].lower() in VOWELS else "de "
    return f"> {role_prefix}{story['role']}, je veux {story['capability']} afin {benefit_prefix}{story['benefit']}."


def source_context(alignment: dict) -> tuple[dict[str, dict], dict[int, dict]]:
    return (
        {source["id"]: source for source in alignment["sources"]},
        {link["story"]: link for link in alignment["story_links"]},
    )


def source_links(source_doc: str, story_number: int, source_by_id: dict[str, dict], link_by_story: dict[int, dict]) -> str:
    link = link_by_story[story_number]
    rendered = []
    for source_id in link["sources"]:
        source = source_by_id[source_id]
        target = f"specs/baseline/sources.md#{source_id.lower()}"
        rendered.append(
            f"{relative_link(source_doc, target, source_id)} — `{source['day']}` / {source['topic']} / `{source['kind']}`"
        )
    return "<br>".join(rendered)


def dependency_links(source_doc: str, story: dict, stories: dict[int, dict]) -> str:
    if not story["depends_on"]:
        return "Aucune"
    return ", ".join(
        relative_link(source_doc, story_path(stories[number]), f"US-FIL-{number}")
        for number in story["depends_on"]
    )


def criterion_line(story: dict, index: int) -> str:
    given, when, then = story["cases"][index]
    number = story["number"]
    case_id = f"CA-FIL-{number}-{index + 1:02}"
    return (
        f'<a id="{case_id.lower()}"></a>\n'
        f"- [ ] `{case_id}` — Étant donné {given}, quand {when}, alors {then}."
    )


def scenario_block(backlog: dict, story: dict, index: int) -> str:
    given, when, then = story["cases"][index]
    label = case_labels(backlog, story)[index]
    number = story["number"]
    return (
        f"  Scénario: {label} — CA-FIL-{number}-{index + 1:02}\n"
        f"    Étant donné {given}\n"
        f"    Quand {when}\n"
        f"    Alors {then}"
    )


def render_story(backlog: dict, story: dict, epic: dict, stories: dict[int, dict], alignment: dict) -> str:
    path = story_path(story)
    number = story["number"]
    feature_id = f"FEAT-FIL-{number}"
    feature_link = relative_link(path, feature_path(story), feature_id)
    source_by_id, link_by_story = source_context(alignment)
    labels = case_labels(backlog, story)
    examples = "\n".join(
        f"| {labels[index]} | {case[0]} | {case[1]} | {case[2]} |"
        for index, case in enumerate(story["cases"])
    )
    criteria = "\n".join(criterion_line(story, index) for index in range(len(story["cases"])))
    scenarios = "\n\n".join(scenario_block(backlog, story, index) for index in range(len(story["cases"])))
    task_lines = []
    for index, objective in enumerate(story["tasks"], start=1):
        task_id = f"TASK-FIL-{number}-{index:02}"
        task_link = relative_link(path, task_path(story, index), task_id)
        task_lines.append(f"- {task_link} — {objective}")
    tasks = "\n".join(task_lines)
    decision = ""
    if number in DECISION_TABLE_ANCHORS:
        target = f"specs/governance/decision-tables.md#{DECISION_TABLE_ANCHORS[number]}"
        rule_link = relative_link(path, target, f"RM-FIL-{number}")
        decision = f"\nTable de décision candidate : {rule_link}.\n"
    ambiguity_target = f"specs/governance/ambiguities.md#{story['ambiguity'].lower()}"
    source_target = "specs/baseline/sources.md"
    return final_newline(f"""# US-FIL-{story['number']} — {story['title']}

`Référence — spécification candidate`

- **Projet parent :** {relative_link(path, 'SPEC.md', backlog['project_id'])}
- **Epic parente :** {relative_link(path, f"specs/epics/{epic['id']}/EPIC.md", epic['id'])}
- **Feature fille :** {feature_link}
- **Jour :** `{epic['day']}`
- **Sources de formation :** {source_links(path, story['number'], source_by_id, link_by_story)}
- **Relation pédagogique :** {link_by_story[story['number']]['relation']}
- **Niveau :** `{tier_label(story)}`
- **Priorité :** `{story['priority']}`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** {story['role']} — personne à désigner
- **Dépendances :** {dependency_links(path, story, stories)}
- **Ambiguïté :** {relative_link(path, ambiguity_target, story['ambiguity'])}

## Besoin

{need_sentence(story)}

## Périmètre

{story['scope']}

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** {story['input']}
- **Sortie :** {story['output']}

Les baselines sont référencées dans {relative_link(path, source_target, 'sources.md')} ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-{story['number']}"></a>
`RM-FIL-{story['number']}` — {story['rule']}

{criteria}

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
{examples}
{decision}
## Scénarios Gherkin

```gherkin
Fonctionnalité: {story['title']}
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-{story['number']}
    Et les attendus ci-dessous définis avant la future réalisation

{scenarios}
```

## Oracle indépendant

{story['oracle']}

## Réalisation et preuves

- {feature_link} — Feature candidate
{tasks}

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir {relative_link(path, ambiguity_target, story['ambiguity'])}.
""")


def render_feature(backlog: dict, story: dict, epic: dict, stories: dict[int, dict], alignment: dict) -> str:
    path = feature_path(story)
    number = story["number"]
    source_by_id, link_by_story = source_context(alignment)
    phases = task_phases(backlog, story)
    rows = []
    for index, objective in enumerate(story["tasks"], start=1):
        task_id = f"TASK-FIL-{number}-{index:02}"
        task_link = relative_link(path, task_path(story, index), task_id)
        if index == 1:
            dependency = dependency_links(path, story, stories)
        else:
            previous_id = f"TASK-FIL-{number}-{index - 1:02}"
            dependency = relative_link(path, task_path(story, index - 1), previous_id)
        rows.append(f"| {task_link} | {objective} | {phases[index - 1]} | {dependency} |")
    surface = SURFACE_MAP.get(story["number"])
    if surface:
        surface_text = f"Surface proposée : {surface}. Ce rapprochement est candidat et ne constitue pas une trace vérifiée."
    else:
        surface_text = "Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation."
    criteria_links = []
    acceptance_lines = []
    for index in range(1, len(story["cases"]) + 1):
        case_id = f"CA-FIL-{number}-{index:02}"
        target = f"{story_path(story)}#ca-fil-{number}-{index:02}"
        link = relative_link(path, target, case_id)
        criteria_links.append(link)
        acceptance_lines.append(f"- [ ] {link}")
    criteria = ", ".join(criteria_links)
    acceptances = "\n".join(acceptance_lines)
    decision = ""
    if number in DECISION_TABLE_ANCHORS:
        target = f"specs/governance/decision-tables.md#{DECISION_TABLE_ANCHORS[number]}"
        rule_link = relative_link(path, target, f"RM-FIL-{number}")
        decision = f"\nLa table de décision candidate associée est {rule_link}.\n"
    ambiguity_target = f"specs/governance/ambiguities.md#{story['ambiguity'].lower()}"
    return final_newline(f"""# FEAT-FIL-{story['number']} — {story['title']}

`Référence — feature candidate`

- **Projet parent :** {relative_link(path, 'SPEC.md', backlog['project_id'])}
- **Epic parente :** {relative_link(path, f"specs/epics/{epic['id']}/EPIC.md", epic['id'])}
- **User Story parente :** {relative_link(path, story_path(story), f"US-FIL-{story['number']}")}
- **Jour :** `{epic['day']}`
- **Sources de formation :** {source_links(path, story['number'], source_by_id, link_by_story)}
- **Branche :** `{backlog['branch']}`
- **Niveau :** `{tier_label(story)}`
- **Priorité :** `{story['priority']}`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** {story['role']} — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** {story['input']}
- **Sortie :** {story['output']}
- **Périmètre :** {story['scope']}
- **Règle canonique :** {relative_link(path, f'{story_path(story)}#rm-fil-{story["number"]}', f'RM-FIL-{story["number"]}')}
- **Critères canoniques :** {criteria}

{surface_text} La baseline actuelle est décrite dans {relative_link(path, 'specs/baseline/current-state.md', 'current-state.md')}. Les noms de modules futurs ne sont pas présentés comme existants.
{decision}
## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
{chr(10).join(rows)}

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la {relative_link(path, f'{story_path(story)}#oracle-indépendant', 'User Story parente')} : {story['oracle']}

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

{acceptances}

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et {relative_link(path, ambiguity_target, story['ambiguity'])} reste ouverte.
""")


def acceptance_links(source: str, story: dict) -> str:
    return ", ".join(
        relative_link(source, f"{story_path(story)}#ca-fil-{story['number']}-{index:02}", f"CA-FIL-{story['number']}-{index:02}")
        for index in range(1, len(story["cases"]) + 1)
    )


def render_task(backlog: dict, story: dict, epic: dict, stories: dict[int, dict], alignment: dict, index: int) -> str:
    path = task_path(story, index)
    number = story["number"]
    story_id = f"US-FIL-{number}"
    feature_id = f"FEAT-FIL-{number}"
    story_link = relative_link(path, story_path(story), story_id)
    feature_link = relative_link(path, feature_path(story), feature_id)
    source_by_id, link_by_story = source_context(alignment)
    phases = task_phases(backlog, story)
    objective = story["tasks"][index - 1]
    title = objective[:-1] if objective.endswith(".") else objective
    if index == 1:
        prerequisite = dependency_links(path, story, stories)
        delivery = f"Produire un artefact relu couvrant les cas et l'oracle de {story_link} dans le mode autorisé."
    else:
        previous_id = f"TASK-FIL-{number}-{index - 1:02}"
        prerequisite = relative_link(path, task_path(story, index - 1), previous_id)
        delivery = f"Réaliser la phase décrite par {feature_link} sans revendiquer une disponibilité ou une preuve non observée."
    if story["tier"] == "extension":
        boundary = "Un replay ou une fixture prépare la vérification ; il ne suffit pas à prouver l’intégration réelle de l’extension."
    else:
        boundary = "Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés."
    ambiguity_target = f"specs/governance/ambiguities.md#{story['ambiguity'].lower()}"
    return final_newline(f"""# TASK-FIL-{story['number']}-{index:02} — {title}

`Référence — tâche candidate`

- **Epic parente :** {relative_link(path, f"specs/epics/{epic['id']}/EPIC.md", epic['id'])}
- **User Story parente :** {story_link}
- **Feature parente :** {feature_link}
- **Jour :** `{epic['day']}`
- **Phase :** {phases[index - 1]}
- **Sources héritées :** {source_links(path, story['number'], source_by_id, link_by_story)}
- **Niveau :** `{tier_label(story)}`
- **Priorité :** `{story['priority']}`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** {story['role']} — personne à désigner

## Objectif

{objective}

## Prérequis

- **Capacités préalables :** {prerequisite}
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**{title}**

{delivery}

{boundary}

- **Entrée héritée :** {story['input']}
- **Sortie héritée :** {story['output']}
- **Périmètre hérité :** {story['scope']}
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** {acceptance_links(path, story)}

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `{phases[index - 1]}`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir {relative_link(path, ambiguity_target, story['ambiguity'])}.
""")


def render_epic(backlog: dict, epic: dict, stories: dict[int, dict], alignment: dict) -> str:
    path = f"specs/epics/{epic['id']}/EPIC.md"
    source_by_id, link_by_story = source_context(alignment)
    children = [stories[number] for number in epic["stories"]]
    source_ids = []
    for story in children:
        for source_id in link_by_story[story["number"]]["sources"]:
            if source_id not in source_ids:
                source_ids.append(source_id)
    source_lines = []
    for source_id in source_ids:
        source = source_by_id[source_id]
        target = f"specs/baseline/sources.md#{source_id.lower()}"
        link = relative_link(path, target, source_id)
        source_lines.append(f"{link} — `{source['day']}` / {source['topic']}")
    sources = "<br>".join(source_lines)
    row_lines = []
    for story in children:
        number = story["number"]
        story_link = relative_link(path, story_path(story), f"US-FIL-{number}")
        feature_link = relative_link(path, feature_path(story), f"FEAT-FIL-{number}")
        row_lines.append(
            f"| {story_link} | {feature_link} | {story['role']} | {story['benefit']} | {tier_label(story)} / {story['priority']} |"
        )
    rows = "\n".join(row_lines)
    external = []
    for story in children:
        for dependency in story["depends_on"]:
            if dependency not in epic["stories"] and dependency not in external:
                external.append(dependency)
    dependencies = ", ".join(relative_link(path, story_path(stories[number]), f"US-FIL-{number}") for number in external) or "Aucune"
    scope_lines = []
    for story in children:
        story_id = f"US-FIL-{story['number']}"
        link = relative_link(path, story_path(story), story_id)
        scope_lines.append(f"- {link} — {story['scope']}")
    scopes = "\n".join(scope_lines)
    socle = ", ".join(relative_link(path, story_path(story), f"US-FIL-{story['number']}") for story in children if story["tier"] == "socle") or "Aucun"
    extension = ", ".join(relative_link(path, story_path(story), f"US-FIL-{story['number']}") for story in children if story["tier"] == "extension") or "Aucune"
    distinction = ""
    if epic["id"] == "EPIC-FIL-00":
        distinction = "\nCette Epic capitalise les pièces J01–J05 déjà enseignées ou déjà produites. Elle demande leur examen et seulement la préparation des pièces manquantes ; elle n'impose pas de rejouer l'ensemble des journées.\n"
    return final_newline(f"""# {epic['id']} — {epic['title']}

`Référence — Epic candidate`

- **Projet parent :** {relative_link(path, 'SPEC.md', backlog['project_id'])}
- **Jour :** `{epic['day']}`
- **Gate pédagogique associée :** `{epic['gate']}` — aucune approbation inférée
- **Sources alignées :** {sources}
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

{epic['benefit']}
{distinction}
## Socle et extension

- **Socle formation :** {socle}
- **Extension production :** {extension}

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
{rows}

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** {dependencies}
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

{scopes}

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
""")


def render_roadmap_backlog(backlog: dict, stories: dict[int, dict]) -> str:
    path = "specs/roadmap/backlog.md"
    epics = {epic["id"]: epic for epic in backlog["epics"]}
    rows = []
    for story in backlog["stories"]:
        tasks = "<br>".join(
            relative_link(path, task_path(story, index), f"TASK-FIL-{story['number']}-{index:02}")
            for index in range(1, len(story["tasks"]) + 1)
        )
        dependencies = ", ".join(relative_link(path, story_path(stories[number]), f"US-FIL-{number}") for number in story["depends_on"]) or "Aucune"
        number = story["number"]
        story_link = relative_link(path, story_path(story), f"US-FIL-{number}")
        day = epics[story["epic"]]["day"]
        rows.append(
            f"| {story_link} | {story['title']} | `{day}` | {tier_label(story)} | {dependencies} | {tasks} |"
        )
    return final_newline(f"""# Référence — Backlog ordonnancé

Le statut de chaque élément reste défini dans {relative_link(path, 'specs/backlog.json', 'backlog.json')}. Le tableau représente le graphe actuel ; une dépendance exprime une capacité préalable, pas l'obligation de refaire un acquis déjà prouvé.

| User Story | Titre | Jour | Niveau | Dépendances | Tâches |
|---|---|---|---|---|---|
{chr(10).join(rows)}

Une source de formation ne signifie ni que la capacité est maîtrisée, ni qu'elle est implémentée. Les travaux futurs et les artefacts existants à revoir restent distingués.
""")


def render_formation_audit(backlog: dict, alignment: dict, stories: dict[int, dict]) -> str:
    path = "specs/baseline/formation-audit.md"
    sections = []
    for finding in alignment["audit_findings"]:
        sources = ", ".join(
            relative_link(path, f"specs/baseline/sources.md#{source_id.lower()}", source_id)
            for source_id in finding["source_ids"]
        )
        affected = ", ".join(
            relative_link(path, story_path(stories[number]), f"US-FIL-{number}")
            for number in finding["stories"]
        )
        sections.append(f"""## {finding['id']}

- **Sévérité :** `{finding['severity']}`
- **Observation :** {finding['observation']}
- **Sources :** {sources}
- **Disposition retenue :** {finding['disposition']}
- **User Stories affectées :** {affected}
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`
""")
    return final_newline(f"""# Explication — Audit d'alignement avec la formation

- **Périmètre de l’audit :** {alignment['scope']}
- **Autorité des sources :** {alignment['authority']}
- **Politique de révision :** {alignment['revision_policy']}

Le registre canonique est {relative_link(path, 'specs/formation-alignment.json', 'formation-alignment.json')}. Il ne prétend pas couvrir exhaustivement les échanges oraux. Le contrôle structurel vérifie le rendu et les relations déclarées ; il ne constitue ni une revue sémantique des critères, ni une preuve comportementale, ni une acceptation métier.

{chr(10).join(sections)}
""")


def render_documents(backlog: dict, alignment: dict) -> dict[str, str]:
    stories = {story["number"]: story for story in backlog["stories"]}
    epics = {epic["id"]: epic for epic in backlog["epics"]}
    documents = {}
    for epic in backlog["epics"]:
        documents[f"specs/epics/{epic['id']}/EPIC.md"] = render_epic(backlog, epic, stories, alignment)
    for story in backlog["stories"]:
        epic = epics[story["epic"]]
        documents[story_path(story)] = render_story(backlog, story, epic, stories, alignment)
        documents[feature_path(story)] = render_feature(backlog, story, epic, stories, alignment)
        for index in range(1, len(story["tasks"]) + 1):
            documents[task_path(story, index)] = render_task(backlog, story, epic, stories, alignment, index)
    documents["specs/roadmap/backlog.md"] = render_roadmap_backlog(backlog, stories)
    documents["specs/baseline/formation-audit.md"] = render_formation_audit(backlog, alignment, stories)
    return documents


def hierarchy_paths(root: Path) -> set[str]:
    base = root / "specs" / "epics"
    if not base.exists():
        return set()
    paths = set()
    for path in base.rglob("*.md"):
        relative = path.relative_to(root).as_posix()
        if path.name == "EPIC.md" or path.name == "FEATURE.md" or path.name.startswith("US-FIL-") or path.name.startswith("TASK-FIL-"):
            paths.add(relative)
    return paths


def managed_destination(root: Path, relative: str) -> Path:
    rel = PurePosixPath(relative)
    allowed = relative in {"specs/roadmap/backlog.md", "specs/baseline/formation-audit.md"} or (
        relative.startswith("specs/epics/") and rel.suffix == ".md"
    )
    if rel.is_absolute() or ".." in rel.parts or not allowed:
        raise ValueError(f"destination non gérée: {relative}")
    root_resolved = root.resolve()
    specs_resolved = (root / "specs").resolve()
    if not specs_resolved.is_relative_to(root_resolved):
        raise ValueError("répertoire specs hors projet")
    destination = root / relative
    if not destination.resolve().is_relative_to(specs_resolved):
        raise ValueError(f"destination hors périmètre: {relative}")
    return destination


def destination_map(root: Path, documents: dict[str, str]) -> dict[str, Path]:
    return {relative: managed_destination(root, relative) for relative in documents}


def check_documents(root: Path, documents: dict[str, str]) -> list[str]:
    destinations = destination_map(root, documents)
    errors = []
    for relative, expected in documents.items():
        path = destinations[relative]
        if not path.is_file():
            errors.append(f"manquant: {relative}")
        elif path.read_text(encoding="utf-8") != expected:
            errors.append(f"différent: {relative}")
    managed_hierarchy = {path for path in documents if path.startswith("specs/epics/")}
    for orphan in sorted(hierarchy_paths(root) - managed_hierarchy):
        errors.append(f"orphelin: {orphan}")
    return errors


def write_documents(root: Path, documents: dict[str, str]) -> None:
    destinations = destination_map(root, documents)
    for relative, content in documents.items():
        path = destinations[relative]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def load_inputs(root: Path) -> tuple[dict, dict, str]:
    backlog = json.loads((root / "specs" / "backlog.json").read_text(encoding="utf-8"))
    alignment = json.loads((root / "specs" / "formation-alignment.json").read_text(encoding="utf-8"))
    ambiguities = (root / "specs" / "governance" / "ambiguities.md").read_text(encoding="utf-8")
    return backlog, alignment, ambiguities


def main(argv: list[str] | None = None, root: Path = PROJECT) -> int:
    parser = argparse.ArgumentParser(description="Rendu déterministe des spécifications du fil rouge")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    try:
        backlog, alignment, ambiguities = load_inputs(root)
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERREUR entrée: {error}")
        return 2
    errors = validate_backlog(backlog, ambiguity_ids(ambiguities))
    errors.extend(validate_alignment(alignment, backlog))
    if errors:
        for error in errors:
            print(f"ERREUR contrat: {error}")
        return 2
    documents = render_documents(backlog, alignment)
    try:
        if args.write:
            write_documents(root, documents)
            print(f"Écrit: {len(documents)} document(s) géré(s).")
            return 0
        drift = check_documents(root, documents)
    except (OSError, ValueError) as error:
        print(f"ERREUR destination: {error}")
        return 2
    if drift:
        for error in drift:
            print(error)
        return 1
    print(f"OK: {len(documents)} document(s) géré(s) à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
