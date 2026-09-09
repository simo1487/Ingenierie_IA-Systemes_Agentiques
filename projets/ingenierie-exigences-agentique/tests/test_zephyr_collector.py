import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"),
)

from zephyr_collector.index_loader import parse_index

BASE_URL = "https://zephyrproject-rtos.github.io/reqmgmt/index.html"

INDEX_HTML = """
<a class="project_tree-file" data-turbo="false"
   href="reqmgmt/docs/software_requirements/atomic_service.html">
  <div class="project_tree-file-icon">...</div>
  <div class="project_tree-file-details">
    <div class="project_tree-file-title">
      Atomic Service
    </div>
    <div class="project_tree-file-name">
      atomic_service.sdoc
    </div>
  </div>
</a>

<a class="project_tree-file" data-turbo="false"
   href="reqmgmt/docs/system_requirements/index.html">
  <div class="project_tree-file-title">
    Zephyr System Requirements
  </div>
  <div class="project_tree-file-name">
    index.sdoc
  </div>
</a>

<a href="https://example.com">Ignored link</a>
"""


class TestIndexLoader(unittest.TestCase):
    def test_parse_index_returns_two_requirement_sources(self):
        result = parse_index(INDEX_HTML, BASE_URL)

        self.assertEqual(len(result), 2)

        self.assertEqual(result[0]["title"], "Atomic Service")
        self.assertEqual(
            result[0]["source_url"],
            "https://zephyrproject-rtos.github.io/reqmgmt/reqmgmt/docs/software_requirements/atomic_service.html",
        )
        self.assertEqual(result[0]["category"], "software_requirements")
        self.assertEqual(result[0]["subcategory"], "atomic_service")

        self.assertEqual(result[1]["title"], "Zephyr System Requirements")
        self.assertEqual(
            result[1]["source_url"],
            "https://zephyrproject-rtos.github.io/reqmgmt/reqmgmt/docs/system_requirements/index.html",
        )
        self.assertEqual(result[1]["category"], "system_requirements")
        self.assertEqual(result[1]["subcategory"], "index")

    def test_parse_index_ignores_non_project_tree_links(self):
        result = parse_index(INDEX_HTML, BASE_URL)
        self.assertNotIn("https://example.com", [r["source_url"] for r in result])

    def test_parse_index_returns_empty_list_for_unrelated_html(self):
        result = parse_index("<html><body>No links here</body></html>", BASE_URL)
        self.assertEqual(result, [])
