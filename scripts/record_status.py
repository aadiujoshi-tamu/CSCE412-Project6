"""Persist deployment status locally and, when configured, in S3."""
from __future__ import annotations
import argparse, json, os
from datetime import datetime, timezone
from pathlib import Path
import boto3

def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--sha", required=True); p.add_argument("--status", required=True); p.add_argument("--detail", default="")
    a = p.parse_args(); payload = {"sha": a.sha, "status": a.status, "detail": a.detail, "at": datetime.now(timezone.utc).isoformat()}
    path = Path("deployments") / f"{a.sha}.json"; path.parent.mkdir(exist_ok=True); path.write_text(json.dumps(payload, indent=2) + "\n")
    if bucket := os.getenv("ARTIFACT_BUCKET"):
        boto3.client("s3").put_object(Bucket=bucket, Key=f"deployments/{a.sha}.json", Body=json.dumps(payload).encode(), ContentType="application/json")

if __name__ == "__main__": main()
