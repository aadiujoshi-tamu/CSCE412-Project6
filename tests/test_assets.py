from pathlib import Path

def test_assets_are_not_empty():
    for asset in (Path("site/assets/site.css"), Path("site/assets/site.js")):
        assert asset.stat().st_size > 0
