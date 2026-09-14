from __future__ import annotations

import re
from pathlib import PurePosixPath

EPIC_ID_PATTERN = re.compile(r"EPIC-FIL-\d{2,}")
AMBIGUITY_ANCHOR_PATTERN = re.compile(r"amb-\d{2,}")
EXPLICIT_ANCHOR_PATTERN = re.compile(r'<a id="([^"]+)\"></a>')
SOURCE_ID_PATTERN = re.compile(r"[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*")
SOURCE_ANCHOR_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SOURCE_KINDS = {"support_actuel", "retour_rapporte", "programme_prevu", "synthese_automatique"}
STORY_STRINGS = {
    "epic", "title", "role", "capability", "benefit", "tier", "priority", "input",
    "output", "rule", "oracle", "scope", "ambiguity",
}
EPIC_STRINGS = {"id", "day", "title", "benefit", "gate", "source"}
BACKLOG_STRINGS = {"project_id", "branch", "status", "information_type"}
ALIGNMENT_STRINGS = {"information_type", "trace_status", "scope", "authority", "revision_policy"}
REQUIRED_CASE_FAMILIES = {"Nominal", "Frontière", "Refus"}


def plain_strings(value: object, allow_empty_items: bool = False) -> bool:
    return type(value) is list and bool(value) and all(
        type(item) is str and (allow_empty_items or bool(item.strip()))
        for item in value
    )


def unique_strings(value: object, allow_empty_items: bool = False) -> bool:
    return plain_strings(value, allow_empty_items) and len(value) == len(set(value))


def positive_int(value: object) -> bool:
    return type(value) is int and value > 0


def ambiguity_ids(text: str) -> set[str]:
    return {
        anchor.upper()
        for anchor in EXPLICIT_ANCHOR_PATTERN.findall(text)
        if AMBIGUITY_ANCHOR_PATTERN.fullmatch(anchor)
    }


def story_case_labels(candidate: dict, story: dict) -> object:
    conventions = candidate.get("conventions")
    if type(conventions) is not dict:
        return None
    return story.get("case_labels", conventions.get("case_labels"))


def story_task_phases(candidate: dict, story: dict) -> object:
    conventions = candidate.get("conventions")
    if type(conventions) is not dict:
        return None
    return story.get("task_phases", conventions.get("task_phases"))


def validate_backlog(candidate: object, valid_ambiguities: set[str]) -> list[str]:
    errors = []
    if type(candidate) is not dict:
        return ["backlog root must be an object"]
    if candidate.get("schema_version") != 2:
        errors.append("backlog schema_version must be 2")
    for field in BACKLOG_STRINGS:
        value = candidate.get(field)
        if type(value) is not str or not value.strip():
            errors.append(f"invalid backlog field {field}")
    epics = candidate.get("epics")
    stories = candidate.get("stories")
    conventions = candidate.get("conventions")
    if type(epics) is not list or not epics:
        errors.append("epics must be a non-empty array")
        epics = []
    if type(stories) is not list or not stories:
        errors.append("stories must be a non-empty array")
        stories = []
    if type(conventions) is not dict:
        errors.append("conventions must be an object")
        conventions = {}
    default_labels = conventions.get("case_labels")
    default_phases = conventions.get("task_phases")
    if not unique_strings(default_labels) or not REQUIRED_CASE_FAMILIES.issubset(set(default_labels or [])):
        errors.append("invalid default case labels")
    if not unique_strings(default_phases):
        errors.append("invalid default task phases")
    for field in ("hierarchy", "id_rule", "work_status", "trace_status", "owner", "task_dependencies", "evidence", "cases", "training_alignment", "prerequisites"):
        value = conventions.get(field)
        if type(value) is not str or not value.strip():
            errors.append(f"invalid convention field {field}")
    tiers = conventions.get("tiers")
    if not unique_strings(tiers) or set(tiers or []) != {"socle", "extension"}:
        errors.append("invalid convention tiers")
    valid_epics = []
    epic_ids = []
    memberships = []
    for index, epic in enumerate(epics):
        if type(epic) is not dict:
            errors.append(f"epic {index} must be an object")
            continue
        valid_epics.append(epic)
        epic_id = epic.get("id")
        if type(epic_id) is not str or EPIC_ID_PATTERN.fullmatch(epic_id) is None:
            errors.append(f"invalid epic id at {index}")
        else:
            epic_ids.append(epic_id)
        for field in EPIC_STRINGS:
            value = epic.get(field)
            if type(value) is not str or not value.strip():
                errors.append(f"invalid epic field {field} at {index}")
        children = epic.get("stories")
        if type(children) is not list or not children:
            errors.append(f"epic stories must be a non-empty array at {index}")
            continue
        for number in children:
            if not positive_int(number):
                errors.append(f"invalid epic membership at {index}")
            else:
                memberships.append(number)
    if len(epic_ids) != len(set(epic_ids)):
        errors.append("duplicate epic id")
    valid_stories = []
    story_numbers = []
    for index, story in enumerate(stories):
        if type(story) is not dict:
            errors.append(f"story {index} must be an object")
            continue
        valid_stories.append(story)
        number = story.get("number")
        if not positive_int(number):
            errors.append(f"invalid story number at {index}")
        else:
            story_numbers.append(number)
        for field in STORY_STRINGS:
            value = story.get(field)
            if type(value) is not str or not value.strip():
                errors.append(f"invalid story field {field} at {index}")
        tier = story.get("tier")
        if type(tier) is not str or tier not in {"socle", "extension"}:
            errors.append(f"invalid tier for {number}")
        priority = story.get("priority")
        if type(priority) is not str or priority not in {"P1", "P2", "P3"}:
            errors.append(f"invalid priority for {number}")
        ambiguity = story.get("ambiguity")
        if type(ambiguity) is not str or ambiguity not in valid_ambiguities:
            errors.append(f"unknown ambiguity for {number}")
        dependencies = story.get("depends_on")
        if type(dependencies) is not list:
            errors.append(f"dependencies must be an array for {number}")
        elif any(not positive_int(dependency) for dependency in dependencies):
            errors.append(f"invalid dependency for {number}")
        tasks = story.get("tasks")
        phases = story_task_phases(candidate, story)
        if not plain_strings(tasks):
            errors.append(f"invalid tasks for {number}")
        if not unique_strings(phases):
            errors.append(f"invalid task phases for {number}")
        if type(tasks) is list and type(phases) is list and len(tasks) != len(phases):
            errors.append(f"task/phase length mismatch for {number}")
        cases = story.get("cases")
        labels = story_case_labels(candidate, story)
        if type(cases) is not list or not cases or any(
            type(case) is not list
            or len(case) != 3
            or any(type(part) is not str or not part.strip() for part in case)
            for case in cases
        ):
            errors.append(f"invalid cases for {number}")
        if not unique_strings(labels) or not REQUIRED_CASE_FAMILIES.issubset(set(labels or [])):
            errors.append(f"invalid case labels for {number}")
        if type(cases) is list and type(labels) is list and len(cases) != len(labels):
            errors.append(f"case/label length mismatch for {number}")
    if len(story_numbers) != len(set(story_numbers)):
        errors.append("duplicate story id")
    if set(memberships) != set(story_numbers):
        errors.append("epic/story membership mismatch")
    if len(memberships) != len(set(memberships)):
        errors.append("story belongs to multiple epics")
    parent_by_number = {
        number: epic.get("id")
        for epic in valid_epics
        if type(epic.get("stories")) is list and type(epic.get("id")) is str
        for number in epic["stories"]
        if positive_int(number)
    }
    by_number = {
        story["number"]: story
        for story in valid_stories
        if positive_int(story.get("number"))
    }
    for number, story in by_number.items():
        if story.get("epic") != parent_by_number.get(number):
            errors.append(f"wrong parent for {number}")
        dependencies = story.get("depends_on")
        if type(dependencies) is list:
            for dependency in dependencies:
                if positive_int(dependency) and dependency not in by_number:
                    errors.append(f"dangling dependency {number}->{dependency}")
                if dependency == number:
                    errors.append(f"self dependency {number}")
    state = {}

    def visit(number: int) -> None:
        if state.get(number) == 1:
            errors.append(f"dependency cycle at {number}")
            return
        if state.get(number) == 2 or number not in by_number:
            return
        state[number] = 1
        dependencies = by_number[number].get("depends_on")
        if type(dependencies) is list:
            for dependency in dependencies:
                if positive_int(dependency):
                    visit(dependency)
        state[number] = 2

    for number in by_number:
        visit(number)
    return errors


def valid_source_path(value: object) -> bool:
    if type(value) is not str or not value.strip() or any(character in value for character in "\r\n"):
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and ".." not in path.parts


def validate_alignment(alignment: object, candidate: object) -> list[str]:
    errors = []
    if type(alignment) is not dict:
        return ["alignment root must be an object"]
    if alignment.get("schema_version") != 1:
        errors.append("alignment schema_version must be 1")
    for field in ALIGNMENT_STRINGS:
        value = alignment.get(field)
        if type(value) is not str or not value.strip():
            errors.append(f"invalid alignment field {field}")
    if type(candidate) is not dict:
        errors.append("backlog root must be an object")
        stories = []
    else:
        stories = candidate.get("stories")
        if type(stories) is not list:
            errors.append("backlog stories must be an array")
            stories = []
    story_ids = {
        story["number"]
        for story in stories
        if type(story) is dict and positive_int(story.get("number"))
    }
    sources = alignment.get("sources")
    links = alignment.get("story_links")
    findings = alignment.get("audit_findings")
    if type(sources) is not list or not sources:
        errors.append("sources must be a non-empty array")
        sources = []
    if type(links) is not list or not links:
        errors.append("story_links must be a non-empty array")
        links = []
    if type(findings) is not list or not findings:
        errors.append("audit_findings must be a non-empty array")
        findings = []
    source_ids = []
    for index, source in enumerate(sources):
        if type(source) is not dict:
            errors.append(f"source {index} must be an object")
            continue
        source_id = source.get("id")
        if type(source_id) is not str or SOURCE_ID_PATTERN.fullmatch(source_id) is None:
            errors.append(f"invalid source id at {index}")
        else:
            source_ids.append(source_id)
        day = source.get("day")
        topic = source.get("topic")
        if type(day) is not str or not day.strip():
            errors.append(f"invalid source field day at {index}")
        if type(topic) is not str or not topic.strip():
            errors.append(f"invalid source field topic at {index}")
        if not valid_source_path(source.get("path")):
            errors.append(f"invalid source field path at {index}")
        anchor = source.get("anchor")
        if type(anchor) is not str or (anchor and SOURCE_ANCHOR_PATTERN.fullmatch(anchor) is None):
            errors.append(f"invalid source anchor at {index}")
        kind = source.get("kind")
        if type(kind) is not str or kind not in SOURCE_KINDS:
            errors.append(f"invalid source kind at {index}")
        lines = source.get("lines")
        if (
            type(lines) is not list
            or len(lines) != 2
            or any(not positive_int(line) for line in lines)
            or lines[0] > lines[1]
        ):
            errors.append(f"invalid source lines at {index}")
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source id")
    known_sources = set(source_ids)
    linked_stories = []
    for index, link in enumerate(links):
        if type(link) is not dict:
            errors.append(f"story link {index} must be an object")
            continue
        story = link.get("story")
        if not positive_int(story):
            errors.append(f"invalid linked story at {index}")
        else:
            linked_stories.append(story)
        references = link.get("sources")
        if not unique_strings(references):
            errors.append(f"invalid source references at {index}")
        elif any(SOURCE_ID_PATTERN.fullmatch(reference) is None or reference not in known_sources for reference in references):
            errors.append(f"unknown source reference at {index}")
        relation = link.get("relation")
        if type(relation) is not str or not relation.strip():
            errors.append(f"empty relation at {index}")
    if len(linked_stories) != len(set(linked_stories)):
        errors.append("duplicate story alignment")
    if set(linked_stories) != story_ids:
        errors.append("story alignment coverage mismatch")
    finding_ids = []
    for index, finding in enumerate(findings):
        if type(finding) is not dict:
            errors.append(f"finding {index} must be an object")
            continue
        finding_id = finding.get("id")
        if type(finding_id) is not str or not finding_id.strip():
            errors.append(f"invalid finding id at {index}")
        else:
            finding_ids.append(finding_id)
        for field in ("severity", "observation", "disposition"):
            value = finding.get(field)
            if type(value) is not str or not value.strip():
                errors.append(f"invalid finding field {field} at {index}")
        source_refs = finding.get("source_ids")
        story_refs = finding.get("stories")
        if not unique_strings(source_refs) or any(reference not in known_sources for reference in source_refs or []):
            errors.append(f"invalid finding sources at {index}")
        if type(story_refs) is not list or not story_refs or any(not positive_int(story) or story not in story_ids for story in story_refs):
            errors.append(f"invalid finding stories at {index}")
    if len(finding_ids) != len(set(finding_ids)):
        errors.append("duplicate finding id")
    return errors
