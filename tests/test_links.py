from pathlib import Path
import re

def test_local_assets_referenced_by_page_exist():
    root = Path("site"); page = (root / "index.html").read_text(encoding="utf-8")
    for reference in re.findall(r'(?:href|src)="([^"#]+)"', page):
        assert (root / reference).is_file(), reference
