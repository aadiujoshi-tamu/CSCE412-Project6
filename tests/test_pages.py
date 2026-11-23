from pathlib import Path

def test_page_has_title_and_main():
    page = Path("site/index.html").read_text(encoding="utf-8")
    assert "<title>" in page and "<main>" in page
