"""Tests unitaires des parsers."""

from __future__ import annotations

from src.parsers import parse_markdown, parse_html, parse_document


def test_parse_markdown_preserves_headers():
    raw = "# CPU\n\nCPU0 runs at 800 MHz."
    clean = parse_markdown(raw)
    assert "CPU" in clean
    assert "CPU0 runs at 800 MHz" in clean
    assert "!" not in clean


def test_parse_html_removes_scripts_and_extracts_text():
    raw = (
        "<html><script>ignore</script><body>"
        "<h1>CPU</h1><p>CPU0 runs at 800 MHz.</p>"
        "</body></html>"
    )
    clean = parse_html(raw)
    assert "CPU" in clean
    assert "CPU0 runs at 800 MHz" in clean
    assert "ignore" not in clean


def test_parse_document_html(sample_html_path):
    doc = {"source": str(sample_html_path), "raw_content": sample_html_path.read_text(encoding="utf-8")}
    parsed = parse_document(doc)
    assert parsed["source"] == str(sample_html_path)
    assert "CPU0" in parsed["content"]
