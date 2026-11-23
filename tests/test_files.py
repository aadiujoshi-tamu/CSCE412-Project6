from pathlib import Path

def test_required_files_exist():
    for name in ("index.html", "release.json", "assets/site.css", "assets/site.js"):
        assert (Path("site") / name).is_file(), name
