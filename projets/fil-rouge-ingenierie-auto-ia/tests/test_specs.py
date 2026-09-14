from __future__ import annotations

import ast
import copy
import json
import os
import posixpath
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path, PurePosixPath

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "tools"))

import render_specs
from spec_contracts import ambiguity_ids, story_case_labels, story_task_phases, validate_alignment, validate_backlog

BACKLOG = PROJECT / "specs" / "backlog.json"
ALIGNMENT = PROJECT / "specs" / "formation-alignment.json"
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EXPLICIT_ANCHOR_PATTERN = re.compile(r'<a id="([^"]+)\"></a>')
VOWELS = "aàâäeéèêëiîïoôöuùûüyÿh"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def markdown_documents() -> dict[str, str]:
    selected = [PROJECT / "README.md", PROJECT / "SPEC.md"]
    selected.extend((PROJECT / "docs").glob("*.md"))
    selected.extend((PROJECT / "specs").rglob("*.md"))
    return {
        path.relative_to(PROJECT).as_posix(): path.read_text(encoding="utf-8")
        for path in selected
    }


def heading_anchors(text: str) -> set[str]:
    anchors = set(EXPLICIT_ANCHOR_PATTERN.findall(text))
    for line in text.splitlines():
        if not line.startswith("#"):
            continue
        heading = line.lstrip("#").strip().lower().replace("`", "")
        heading = re.sub(r"[^\w\s-]", "", heading, flags=re.UNICODE)
        heading = re.sub(r"[\s-]+", "-", heading).strip("-")
        anchors.add(heading)
    return anchors


def validate_links(documents: dict[str, str], files: set[str]) -> list[str]:
    errors = []
    for source, text in documents.items():
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip("<>")
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path_part, separator, anchor = target.partition("#")
            resolved = source if not path_part else posixpath.normpath(str(PurePosixPath(source).parent / path_part))
            if resolved not in files:
                errors.append(f"broken link {source}->{target}")
                continue
            if separator and anchor and resolved in documents and anchor not in heading_anchors(documents[resolved]):
                errors.append(f"broken anchor {source}->{target}")
    return errors


def relative_link(source: str, target: str, label: str) -> str:
    relative = os.path.relpath(target, PurePosixPath(source).parent.as_posix()).replace(os.sep, "/")
    return f"[`{label}`]({relative})"


def story_path(story: dict) -> str:
    return f"specs/epics/{story['epic']}/user-stories/US-FIL-{story['number']}.md"


def feature_path(story: dict) -> str:
    return f"specs/epics/{story['epic']}/features/FEAT-FIL-{story['number']}/FEATURE.md"


def task_path(story: dict, index: int) -> str:
    return f"specs/epics/{story['epic']}/features/FEAT-FIL-{story['number']}/tasks/TASK-FIL-{story['number']}-{index:02}.md"


def need_sentence(story: dict) -> str:
    role_prefix = "En tant qu’" if story["role"][0].lower() in VOWELS else "En tant que "
    benefit_prefix = "d’" if story["benefit"][0].lower() in VOWELS else "de "
    return f"> {role_prefix}{story['role']}, je veux {story['capability']} afin {benefit_prefix}{story['benefit']}."


def scenario_block(candidate: dict, story: dict, index: int) -> str:
    labels = story_case_labels(candidate, story)
    given, when, then = story["cases"][index]
    number = story["number"]
    return (
        f"  Scénario: {labels[index]} — CA-FIL-{number}-{index + 1:02}\n"
        f"    Étant donné {given}\n"
        f"    Quand {when}\n"
        f"    Alors {then}"
    )


def task_dependency(story: dict, index: int, source: str, stories: dict[int, dict]) -> str:
    if index == 1:
        if not story["depends_on"]:
            return "Aucune"
        return ", ".join(
            relative_link(source, story_path(stories[number]), f"US-FIL-{number}")
            for number in story["depends_on"]
        )
    previous = f"TASK-FIL-{story['number']}-{index - 1:02}"
    return f"[`{previous}`]({previous}.md)"


def all_acceptance_links(source: str, story: dict) -> str:
    return ", ".join(
        relative_link(
            source,
            f"{story_path(story)}#ca-fil-{story['number']}-{index:02}",
            f"CA-FIL-{story['number']}-{index:02}",
        )
        for index in range(1, len(story["cases"]) + 1)
    )


def validate_rendered(candidate: dict, alignment: dict, documents: dict[str, str], files: set[str]) -> list[str]:
    errors = validate_links(documents, files)
    stories = {story["number"]: story for story in candidate["stories"]}
    epics = {epic["id"]: epic for epic in candidate["epics"]}
    source_by_id = {source["id"]: source for source in alignment["sources"]}
    link_by_story = {link["story"]: link for link in alignment["story_links"]}
    for epic in candidate["epics"]:
        path = f"specs/epics/{epic['id']}/EPIC.md"
        if path not in documents:
            errors.append(f"missing epic document {epic['id']}")
        elif f"# {epic['id']} — {epic['title']}" not in documents[path]:
            errors.append(f"incomplete epic document {epic['id']}")
    for story in candidate["stories"]:
        number = story["number"]
        epic = epics[story["epic"]]
        story_doc = story_path(story)
        feature_doc = feature_path(story)
        epic_doc = f"specs/epics/{story['epic']}/EPIC.md"
        if story_doc not in documents:
            errors.append(f"missing story document {number}")
            story_text = ""
        else:
            story_text = documents[story_doc]
        if feature_doc not in documents:
            errors.append(f"missing feature document {number}")
            feature_text = ""
        else:
            feature_text = documents[feature_doc]
        required_story = (
            f"# US-FIL-{number} — {story['title']}",
            f"**Jour :** `{epic['day']}`",
            f"**Priorité :** `{story['priority']}`",
            need_sentence(story),
            f"**Entrée :** {story['input']}",
            f"**Sortie :** {story['output']}",
            f"## Périmètre\n\n{story['scope']}",
            f"`RM-FIL-{number}` — {story['rule']}",
            story["oracle"],
            link_by_story[number]["relation"],
        )
        if any(value not in story_text for value in required_story):
            errors.append(f"altered story document {number}")
        for source_id in link_by_story[number]["sources"]:
            source = source_by_id[source_id]
            source_link = relative_link(story_doc, f"specs/baseline/sources.md#{source_id.lower()}", source_id)
            if source_link not in story_text or source["topic"] not in story_text or source["kind"] not in story_text:
                errors.append(f"altered story source {number}/{source_id}")
        for index, case in enumerate(story["cases"]):
            case_id = f"CA-FIL-{number}-{index + 1:02}"
            criterion = (
                f'<a id="{case_id.lower()}"></a>\n- [ ] `{case_id}` — '
                f"Étant donné {case[0]}, quand {case[1]}, alors {case[2]}."
            )
            if criterion not in story_text:
                errors.append(f"altered criterion {case_id}")
            if scenario_block(candidate, story, index) not in story_text:
                errors.append(f"altered scenario {case_id}")
        required_feature = (
            f"# FEAT-FIL-{number} — {story['title']}",
            f"**Epic parente :** {relative_link(feature_doc, epic_doc, story['epic'])}",
            f"**User Story parente :** {relative_link(feature_doc, story_doc, f'US-FIL-{number}')}",
            f"**Priorité :** `{story['priority']}`",
            f"**Entrée :** {story['input']}",
            f"**Sortie :** {story['output']}",
            f"**Périmètre :** {story['scope']}",
        )
        if any(value not in feature_text for value in required_feature):
            errors.append(f"altered feature document {number}")
        phases = story_task_phases(candidate, story)
        for index, objective in enumerate(story["tasks"], start=1):
            task_doc = task_path(story, index)
            task_id = f"TASK-FIL-{number}-{index:02}"
            if task_doc not in documents:
                errors.append(f"missing task document {task_id}")
                continue
            task_text = documents[task_doc]
            title = objective[:-1] if objective.endswith(".") else objective
            boundary = (
                "Un replay ou une fixture prépare la vérification ; il ne suffit pas à prouver l’intégration réelle de l’extension."
                if story["tier"] == "extension"
                else "Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés."
            )
            required_task = (
                f"# {task_id} — {title}",
                f"**Phase :** {phases[index - 1]}",
                f"**Epic parente :** {relative_link(task_doc, epic_doc, story['epic'])}",
                f"**User Story parente :** {relative_link(task_doc, story_doc, f'US-FIL-{number}')}",
                f"**Feature parente :** {relative_link(task_doc, feature_doc, f'FEAT-FIL-{number}')}",
                f"## Objectif\n\n{objective}",
                f"**Capacités préalables :** {task_dependency(story, index, task_doc, stories)}",
                f"**Entrée héritée :** {story['input']}",
                f"**Sortie héritée :** {story['output']}",
                f"**Périmètre hérité :** {story['scope']}",
                f"**Critères de la US parente (références, pas preuve de couverture de cette tâche) :** {all_acceptance_links(task_doc, story)}",
                boundary,
            )
            if any(value not in task_text for value in required_task):
                errors.append(f"altered task document {task_id}")
    return errors


class BacklogStructureTests(unittest.TestCase):
    def setUp(self):
        self.backlog = load_json(BACKLOG)
        self.alignment = load_json(ALIGNMENT)
        self.documents = markdown_documents()
        self.files = {path.relative_to(PROJECT).as_posix() for path in PROJECT.rglob("*") if path.is_file()}
        workflow = PROJECT.parents[1] / "workflows" / "README.md"
        self.files.add(posixpath.relpath(workflow, PROJECT))
        self.valid_ambiguities = ambiguity_ids(self.documents["specs/governance/ambiguities.md"])

    def test_canonical_backlog_alignment_and_rendered_hierarchy_are_consistent(self):
        self.assertEqual(validate_backlog(self.backlog, self.valid_ambiguities), [])
        self.assertEqual(validate_alignment(self.alignment, self.backlog), [])
        self.assertEqual(validate_rendered(self.backlog, self.alignment, self.documents, self.files), [])

    def test_consistent_new_story_with_alignment_is_valid(self):
        candidate = copy.deepcopy(self.backlog)
        alignment = copy.deepcopy(self.alignment)
        added = copy.deepcopy(candidate["stories"][0])
        added["number"] = 999
        added["depends_on"] = []
        candidate["stories"].append(added)
        candidate["epics"][0]["stories"].append(999)
        added_link = copy.deepcopy(alignment["story_links"][0])
        added_link["story"] = 999
        alignment["story_links"].append(added_link)
        self.assertEqual(validate_backlog(candidate, self.valid_ambiguities), [])
        self.assertEqual(validate_alignment(alignment, candidate), [])

    def test_variable_cases_and_tasks_with_matching_labels_and_phases_are_valid(self):
        for count in (4, 5):
            candidate = copy.deepcopy(self.backlog)
            story = candidate["stories"][0]
            story["cases"] = [copy.deepcopy(story["cases"][index % 3]) for index in range(count)]
            story["case_labels"] = ["Nominal", "Frontière", "Refus", *[f"Cas {index}" for index in range(4, count + 1)]]
            self.assertEqual(validate_backlog(candidate, self.valid_ambiguities), [])
        candidate = copy.deepcopy(self.backlog)
        story = candidate["stories"][0]
        story["tasks"].append(story["tasks"][0])
        story["task_phases"] = [*candidate["conventions"]["task_phases"], "Phase 4"]
        self.assertEqual(validate_backlog(candidate, self.valid_ambiguities), [])

    def test_empty_graph_children_tasks_phases_sources_links_and_references_fail(self):
        empty_graph = copy.deepcopy(self.backlog)
        empty_graph["epics"] = []
        empty_graph["stories"] = []
        self.assertTrue(validate_backlog(empty_graph, self.valid_ambiguities))
        empty_children = copy.deepcopy(self.backlog)
        empty_children["epics"][0]["stories"] = []
        self.assertTrue(validate_backlog(empty_children, self.valid_ambiguities))
        empty_tasks = copy.deepcopy(self.backlog)
        empty_tasks["stories"][0]["tasks"] = []
        empty_tasks["stories"][0]["task_phases"] = []
        self.assertTrue(validate_backlog(empty_tasks, self.valid_ambiguities))
        empty_sources = copy.deepcopy(self.alignment)
        empty_sources["sources"] = []
        self.assertTrue(validate_alignment(empty_sources, self.backlog))
        empty_links = copy.deepcopy(self.alignment)
        empty_links["story_links"] = []
        self.assertTrue(validate_alignment(empty_links, self.backlog))
        empty_references = copy.deepcopy(self.alignment)
        empty_references["story_links"][0]["sources"] = []
        self.assertTrue(validate_alignment(empty_references, self.backlog))

    def test_missing_or_mismatched_labels_and_phases_fail(self):
        missing_labels = copy.deepcopy(self.backlog)
        missing_labels["stories"][0]["cases"].append(copy.deepcopy(missing_labels["stories"][0]["cases"][0]))
        self.assertTrue(any("case/label length mismatch" in error for error in validate_backlog(missing_labels, self.valid_ambiguities)))
        missing_phases = copy.deepcopy(self.backlog)
        missing_phases["stories"][0]["tasks"].append(missing_phases["stories"][0]["tasks"][0])
        self.assertTrue(any("task/phase length mismatch" in error for error in validate_backlog(missing_phases, self.valid_ambiguities)))
        explicit_labels = copy.deepcopy(self.backlog)
        explicit_labels["stories"][2].pop("case_labels")
        self.assertTrue(any("case/label length mismatch" in error for error in validate_backlog(explicit_labels, self.valid_ambiguities)))
        explicit_phases = copy.deepcopy(self.backlog)
        explicit_phases["stories"][2].pop("task_phases")
        self.assertTrue(any("task/phase length mismatch" in error for error in validate_backlog(explicit_phases, self.valid_ambiguities)))

    def test_malformed_inputs_and_unhashable_enums_return_errors(self):
        for candidate in ([], None):
            self.assertTrue(validate_backlog(candidate, self.valid_ambiguities))
        mutations = []
        number_object = copy.deepcopy(self.backlog)
        number_object["stories"][0]["number"] = {}
        mutations.append(number_object)
        dependency_object = copy.deepcopy(self.backlog)
        dependency_object["stories"][0]["depends_on"] = [{}]
        mutations.append(dependency_object)
        tasks_none = copy.deepcopy(self.backlog)
        tasks_none["stories"][0]["tasks"] = None
        mutations.append(tasks_none)
        cases_none = copy.deepcopy(self.backlog)
        cases_none["stories"][0]["cases"] = [None]
        mutations.append(cases_none)
        enum_object = copy.deepcopy(self.backlog)
        enum_object["stories"][0]["tier"] = {}
        enum_object["stories"][0]["priority"] = {}
        enum_object["stories"][0]["ambiguity"] = {}
        mutations.append(enum_object)
        for candidate in mutations:
            self.assertTrue(validate_backlog(candidate, self.valid_ambiguities))
        alignment_enum = copy.deepcopy(self.alignment)
        alignment_enum["sources"][0]["kind"] = {}
        self.assertTrue(validate_alignment(alignment_enum, self.backlog))
        stories_none = copy.deepcopy(self.backlog)
        stories_none["stories"] = None
        self.assertTrue(validate_alignment(self.alignment, stories_none))

    def test_schema_versions_and_required_top_level_fields_fail_when_invalid(self):
        backlog = copy.deepcopy(self.backlog)
        backlog["schema_version"] = 1
        backlog["project_id"] = ""
        self.assertTrue(validate_backlog(backlog, self.valid_ambiguities))
        alignment = copy.deepcopy(self.alignment)
        alignment["schema_version"] = 2
        alignment["scope"] = ""
        self.assertTrue(validate_alignment(alignment, self.backlog))

    def test_missing_source_and_duplicate_or_missing_alignment_fail(self):
        unknown_source = copy.deepcopy(self.alignment)
        unknown_source["story_links"][0]["sources"] = ["ABSENT"]
        self.assertTrue(any("unknown source reference" in error for error in validate_alignment(unknown_source, self.backlog)))
        duplicate = copy.deepcopy(self.alignment)
        duplicate["story_links"].append(copy.deepcopy(duplicate["story_links"][0]))
        self.assertIn("duplicate story alignment", validate_alignment(duplicate, self.backlog))
        missing = copy.deepcopy(self.alignment)
        missing["story_links"] = missing["story_links"][:-1]
        self.assertIn("story alignment coverage mismatch", validate_alignment(missing, self.backlog))
        unsafe_id = copy.deepcopy(self.alignment)
        unsafe_id["sources"][0]["id"] = "bad source"
        self.assertTrue(any("invalid source id" in error for error in validate_alignment(unsafe_id, self.backlog)))

    def test_removed_child_duplicate_wrong_parent_and_cycle_fail(self):
        removed = copy.deepcopy(self.backlog)
        removed["stories"] = removed["stories"][:-1]
        self.assertIn("epic/story membership mismatch", validate_backlog(removed, self.valid_ambiguities))
        duplicate = copy.deepcopy(self.backlog)
        duplicate["stories"].append(copy.deepcopy(duplicate["stories"][0]))
        self.assertIn("duplicate story id", validate_backlog(duplicate, self.valid_ambiguities))
        moved = copy.deepcopy(self.backlog)
        number = moved["epics"][0]["stories"].pop(0)
        moved["epics"][1]["stories"].append(number)
        self.assertIn(f"wrong parent for {number}", validate_backlog(moved, self.valid_ambiguities))
        cyclic = copy.deepcopy(self.backlog)
        first = cyclic["stories"][0]["number"]
        second = cyclic["stories"][1]["number"]
        cyclic["stories"][0]["depends_on"] = [second]
        cyclic["stories"][1]["depends_on"] = [first]
        self.assertTrue(any("dependency cycle" in error for error in validate_backlog(cyclic, self.valid_ambiguities)))

    def test_altered_gherkin_then_is_detected_when_example_mapping_remains(self):
        mutated = dict(self.documents)
        story = self.backlog["stories"][0]
        path = story_path(story)
        block = scenario_block(self.backlog, story, 0)
        altered = block.replace(f"    Alors {story['cases'][0][2]}", "    Alors attendu altéré")
        mutated[path] = mutated[path].replace(block, altered)
        errors = validate_rendered(self.backlog, self.alignment, mutated, self.files)
        self.assertIn(f"altered scenario CA-FIL-{story['number']}-01", errors)
        self.assertIn(story["cases"][0][2], mutated[path])

    def test_missing_file_and_broken_link_are_detected(self):
        missing = dict(self.documents)
        story = self.backlog["stories"][0]
        del missing[story_path(story)]
        self.assertIn(
            f"missing story document {story['number']}",
            validate_rendered(self.backlog, self.alignment, missing, self.files),
        )
        broken = dict(self.documents)
        path = story_path(story)
        expected = relative_link(path, feature_path(story), f"FEAT-FIL-{story['number']}")
        broken[path] = broken[path].replace(expected, "[`absent`](../features/ABSENT/FEATURE.md)")
        self.assertTrue(any("ABSENT/FEATURE.md" in error for error in validate_links(broken, self.files)))

    def test_all_tasks_reference_all_parent_criteria_without_claiming_coverage(self):
        story = next(story for story in self.backlog["stories"] if story["number"] == 5)
        label = "**Critères de la US parente (références, pas preuve de couverture de cette tâche) :**"
        for index in (1, len(story["tasks"])):
            text = self.documents[task_path(story, index)]
            self.assertIn(label, text)
            self.assertIn("CA-FIL-5-01", text)
            self.assertIn("CA-FIL-5-05", text)
            self.assertIn(story_task_phases(self.backlog, story)[index - 1], text)
            self.assertIn(story["tasks"][index - 1], text)

    def test_renderer_representative_structure_uses_fixed_expected_text(self):
        rendered = render_specs.render_documents(self.backlog, self.alignment)
        story = rendered["specs/epics/EPIC-FIL-00/user-stories/US-FIL-1.md"]
        self.assertIn("# US-FIL-1 — Choisir une assistance proportionnée au besoin", story)
        self.assertIn(
            "- [ ] `CA-FIL-1-01` — Étant donné une règle de classement déterministe suffit au besoin fictif, quand l'architecte propose un mécanisme, alors la règle est conservée comme option sans imposer de modèle.",
            story,
        )
        task = rendered["specs/epics/EPIC-FIL-00/features/FEAT-FIL-1/tasks/TASK-FIL-1-01.md"]
        self.assertIn(
            "# TASK-FIL-1-01 — Rassembler le besoin, les actions permises et la classification des données, en séparant faits et hypothèses",
            task,
        )
        self.assertIn("- **Phase :** Spécifier et figer l'oracle", task)

    def test_renderer_check_detects_drift_and_orphans(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = {"specs/roadmap/backlog.md": "attendu\n"}
            target = root / "specs" / "roadmap" / "backlog.md"
            target.parent.mkdir(parents=True)
            target.write_text("dérive\n", encoding="utf-8")
            self.assertIn("différent: specs/roadmap/backlog.md", render_specs.check_documents(root, expected))
            orphan = root / "specs" / "epics" / "EPIC-FIL-99" / "EPIC.md"
            orphan.parent.mkdir(parents=True)
            orphan.write_text("orphelin\n", encoding="utf-8")
            self.assertTrue(any(error.startswith("orphelin:") for error in render_specs.check_documents(root, expected)))

    def test_write_preflight_rejects_unmanaged_and_external_symlink_without_partial_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "specs").mkdir()
            sentinel = root / "outside.md"
            sentinel.write_text("inchangé\n", encoding="utf-8")
            allowed = root / "specs" / "roadmap" / "backlog.md"
            with self.assertRaises(ValueError):
                render_specs.write_documents(
                    root,
                    {"specs/roadmap/backlog.md": "créé\n", "../outside.md": "altéré\n"},
                )
            self.assertFalse(allowed.exists())
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "inchangé\n")
            external = root / "external"
            external.mkdir()
            (root / "specs" / "epics").symlink_to(external, target_is_directory=True)
            with self.assertRaises(ValueError):
                render_specs.write_documents(
                    root,
                    {"specs/epics/EPIC-FIL-99/EPIC.md": "interdit\n"},
                )
            self.assertFalse((external / "EPIC-FIL-99" / "EPIC.md").exists())

    def test_invalid_json_main_write_returns_two_without_writing_documents(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            specs = root / "specs"
            specs.mkdir()
            (specs / "backlog.json").write_text("{invalide", encoding="utf-8")
            (specs / "formation-alignment.json").write_text("{}\n", encoding="utf-8")
            (specs / "governance").mkdir()
            (specs / "governance" / "ambiguities.md").write_text('<a id="amb-01"></a>\n', encoding="utf-8")
            with redirect_stdout(StringIO()):
                result = render_specs.main(["--write"], root)
            self.assertEqual(result, 2)
            self.assertFalse((specs / "roadmap" / "backlog.md").exists())

    def test_python_310_grammar_for_owned_tooling_and_tests(self):
        paths = (
            PROJECT / "tools" / "render_specs.py",
            PROJECT / "tools" / "spec_contracts.py",
            PROJECT / "tests" / "test_specs.py",
        )
        for path in paths:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path), feature_version=(3, 10))


if __name__ == "__main__":
    unittest.main()
