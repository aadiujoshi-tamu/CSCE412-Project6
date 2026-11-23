import json
from pathlib import Path

def test_release_manifest_has_sha_and_timestamp():
    release = json.loads(Path("site/release.json").read_text(encoding="utf-8"))
    assert release["commit_sha"] and release["timestamp"]
