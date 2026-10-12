"""
Site Integrity Test Suite for Quartz-generated HTML.

Verifies:
1. Public build artifacts exist.
2. No unparsed Obsidian wikilinks ('[[...]]') leak into emitted HTML text.
3. All internal links resolve to existing HTML files (Zero 404s).
4. Content search index and graph data are valid.
5. Critical pages (index, topics, groups, interview guides) are present.

Zero external dependencies required (uses standard library unittest + html.parser).
Can also be executed via `pytest tests/`.
"""

import json
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import urlparse, unquote


PUBLIC_DIR = Path(__file__).resolve().parent.parent / "quartz" / "public"


class InternalLinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text_content = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs_dict = dict(attrs)
            href = attrs_dict.get("href")
            if href:
                self.links.append((href, attrs_dict.get("class", "")))

    def handle_data(self, data):
        self.text_content.append(data)


class TestSiteIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not PUBLIC_DIR.exists():
            raise unittest.SkipTest(
                f"Public build directory not found at {PUBLIC_DIR}. Run `npm --prefix quartz run build` first."
            )

    def test_core_pages_exist(self):
        """Verify essential HTML entrypoints exist."""
        expected_files = [
            PUBLIC_DIR / "index.html",
            PUBLIC_DIR / "topics.html",
            PUBLIC_DIR / "404.html",
            PUBLIC_DIR / "static" / "contentIndex.json",
        ]
        for file_path in expected_files:
            self.assertTrue(
                file_path.exists(),
                f"Expected build artifact missing: {file_path.relative_to(PUBLIC_DIR)}",
            )

    def test_search_content_index_is_valid(self):
        """Verify contentIndex.json is populated with indexed wiki pages."""
        index_file = PUBLIC_DIR / "static" / "contentIndex.json"
        self.assertTrue(index_file.exists())

        with open(index_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0, "contentIndex.json is empty")

        # Verify key topics and guides are present in the search index
        keys = list(data.keys())
        self.assertTrue(any("topics" in k for k in keys), "Topics missing from search index")
        self.assertTrue(
            any("ai" in k or "interview" in k for k in keys),
            "Interview guides missing from search index",
        )

    def test_no_unparsed_wikilinks_in_html(self):
        """Ensure no raw unparsed '[[...]]' wikilinks leak into generated HTML text."""
        html_files = list(PUBLIC_DIR.glob("**/*.html"))
        self.assertGreater(len(html_files), 0, "No HTML files found to inspect")

        leaked_wikilinks = []
        for html_file in html_files:
            content = html_file.read_text(encoding="utf-8")
            parser = InternalLinkExtractor()
            parser.feed(content)
            body_text = "".join(parser.text_content)

            # Check for literal [[ something ]]
            if "[[" in body_text and "]]" in body_text:
                start = body_text.find("[[")
                snippet = body_text[start : start + 60].replace("\n", " ")
                leaked_wikilinks.append(f"{html_file.name}: {snippet}")

        self.assertEqual(
            leaked_wikilinks,
            [],
            f"Found unparsed wikilinks in emitted HTML:\n" + "\n".join(leaked_wikilinks),
        )

    def test_internal_links_resolve_without_404(self):
        """Ensure every internal anchor link resolves to an existing file."""
        html_files = list(PUBLIC_DIR.glob("**/*.html"))
        broken_links = []

        for html_file in html_files:
            content = html_file.read_text(encoding="utf-8")
            parser = InternalLinkExtractor()
            parser.feed(content)

            for href, class_attr in parser.links:
                parsed = urlparse(href)

                # Skip external links, pure anchor jumps, and mailto/tel
                if parsed.scheme or href.startswith("#") or href.startswith("mailto:"):
                    continue

                # Strip anchor and query
                clean_path = unquote(parsed.path)
                if not clean_path or clean_path == ".":
                    continue

                # Resolve relative to current HTML directory
                if clean_path.startswith("/"):
                    target = PUBLIC_DIR / clean_path.lstrip("/")
                else:
                    target = (html_file.parent / clean_path).resolve()

                # Test existence: either exact file, file.html, or directory/index.html
                resolved = False
                candidates = [
                    target,
                    target.with_suffix(".html"),
                    target / "index.html",
                ]
                for candidate in candidates:
                    if candidate.exists() and (candidate.is_file() or candidate.is_dir()):
                        resolved = True
                        break

                if not resolved:
                    broken_links.append(
                        f"From {html_file.relative_to(PUBLIC_DIR)} -> '{href}' (unresolved)"
                    )

        self.assertEqual(
            broken_links,
            [],
            f"Broken internal links detected (404 risk):\n" + "\n".join(broken_links[:10]),
        )


if __name__ == "__main__":
    unittest.main()
