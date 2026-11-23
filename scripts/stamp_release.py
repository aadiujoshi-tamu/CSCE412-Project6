"""Write a deterministic release manifest for a build artifact."""
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sha", required=True)
    parser.add_argument("--site", default="site")
    args = parser.parse_args()
    manifest = {"commit_sha": args.sha, "timestamp": datetime.now(timezone.utc).isoformat()}
    (Path(args.site) / "release.json").write_text(json.dumps(manifest) + "\n", encoding="utf-8")

if __name__ == "__main__": main()
