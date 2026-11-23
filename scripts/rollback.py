"""Restore an immutable known-good artifact and revalidate it."""
from __future__ import annotations
import argparse, os, subprocess, tempfile
from pathlib import Path

def run(*args: str) -> None: subprocess.run(args, check=True)
def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--sha", required=True); a = p.parse_args()
    artifact, site = os.environ["ARTIFACT_BUCKET"], os.environ["WEBSITE_BUCKET"]
    with tempfile.TemporaryDirectory() as temp:
        archive = Path(temp) / "release.zip"; run("aws", "s3", "cp", f"s3://{artifact}/releases/{a.sha}.zip", str(archive)); run("unzip", "-q", str(archive), "-d", temp)
        run("aws", "s3", "sync", f"{temp}/site", f"s3://{site}/", "--delete"); run("bash", "scripts/invalidate_cache.sh")
    run("python", "scripts/verify_production.py", "--domain", os.environ["SITE_DOMAIN"], "--sha", a.sha, "--bucket", site)
if __name__ == "__main__": main()
