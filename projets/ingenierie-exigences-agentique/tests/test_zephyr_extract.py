import html
import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"),
)

from zephyr_collector.extract import parse_requirement_page

PAGE_HTML = """
<sdoc-anchor
  id="ZEP-SRS-26-1"
  data-uid="ZEP-SRS-26-1"
  node-role="requirement"
>
  <span class="anchor_button_text">ZEP-SRS-26-1</span>
</sdoc-anchor>

<sdoc-node-content
  node-view="narrative"
  data-level="1"
  data-status="draft"
  show-node-type-name="REQUIREMENT"
>
  <sdoc-node-title data-level="1">
    <sdoc-field>
      <sdoc-field-content>
        <sdoc-autogen>1.&nbsp;Atomic variable</sdoc-autogen>
      </sdoc-field-content>
    </sdoc-field>
  </sdoc-node-title>

  <sdoc-node-field-label>STATEMENT:</sdoc-node-field-label>
  <sdoc-node-field data-field-label="statement">
    <sdoc-field>
      <sdoc-field-content>
        <sdoc-autogen>
          <div class="document">
            <p>The Zephyr RTOS shall define an atomic variable type.</p>
          </div>
        </sdoc-autogen>
      </sdoc-field-content>
    </sdoc-field>
  </sdoc-node-field>
</sdoc-node-content>

<sdoc-anchor
  id="ZEP-SRS-26-2"
  data-uid="ZEP-SRS-26-2"
  node-role="requirement"
>
  <span class="anchor_button_text">ZEP-SRS-26-2</span>
</sdoc-anchor>

<sdoc-node-content
  data-status="draft"
>
  <sdoc-node-title>
    <sdoc-field>
      <sdoc-field-content>
        <sdoc-autogen>2. Atomic value</sdoc-autogen>
      </sdoc-field-content>
    </sdoc-field>
  </sdoc-node-title>

  <sdoc-node-field-label>STATEMENT:</sdoc-node-field-label>
  <sdoc-node-field data-field-label="statement">
    <sdoc-field>
      <sdoc-field-content>
        <sdoc-autogen>
          <div class="document">
            <p>The Zephyr RTOS shall support atomic read-modify-write operations.</p>
          </div>
        </sdoc-autogen>
      </sdoc-field-content>
    </sdoc-field>
  </sdoc-node-field>
</sdoc-node-content>
"""

SOURCE_URL = "https://zephyrproject-rtos.github.io/reqmgmt/reqmgmt/docs/software_requirements/atomic_service.html"


class TestExtractRequirement(unittest.TestCase):
    def test_parse_requirement_page_returns_two_requirements(self):
        result = parse_requirement_page(
            PAGE_HTML,
            source_url=SOURCE_URL,
            category="software_requirements",
            subcategory="atomic_service",
        )

        self.assertEqual(len(result), 2)

        self.assertEqual(result[0]["requirement_id"], "ZEP-SRS-26-1")
        self.assertEqual(result[0]["title"], "1. Atomic variable")
        self.assertIn("atomic variable type", result[0]["requirement_text"])
        self.assertEqual(result[0]["category"], "software_requirements")
        self.assertEqual(result[0]["subcategory"], "atomic_service")
        self.assertEqual(result[0]["source_url"], SOURCE_URL)
        self.assertEqual(result[0]["status"], "Observé")
        self.assertEqual(result[0]["confidence"], "Candidat")
        self.assertNotIn("<", result[0]["requirement_text"])

        self.assertEqual(result[1]["requirement_id"], "ZEP-SRS-26-2")
        self.assertIn("read-modify-write", result[1]["requirement_text"])

    def test_parse_requirement_page_returns_empty_list_if_no_requirement(self):
        result = parse_requirement_page(
            "<html><body>No requirement here</body></html>",
            source_url=SOURCE_URL,
            category="software_requirements",
            subcategory="atomic_service",
        )
        self.assertEqual(result, [])
