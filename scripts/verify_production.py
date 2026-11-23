"""Validate the public release without trusting a CDN cache blindly."""
from __future__ import annotations
import argparse, json, socket, ssl
import requests

def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--domain", required=True); p.add_argument("--sha", required=True); p.add_argument("--bucket", required=True); a = p.parse_args()
    base = f"https://{a.domain}"; checks = {}
    try:
        checks["reachable"] = requests.get(base, timeout=15).ok
        checks["https_redirect"] = requests.get(f"http://{a.domain}", timeout=15, allow_redirects=False).status_code in (301, 302, 307, 308)
        checks["release_id"] = requests.get(f"{base}/release.json", timeout=15).json().get("commit_sha") == a.sha
        checks["critical_content"] = "Reliable Releases" in requests.get(base, timeout=15).text
        checks["s3_direct_denied"] = requests.get(f"https://{a.bucket}.s3.amazonaws.com/index.html", timeout=15).status_code == 403
        with socket.create_connection((a.domain, 443), timeout=15) as raw:
            with ssl.create_default_context().wrap_socket(raw, server_hostname=a.domain) as wrapped: checks["tls"] = bool(wrapped.version())
    except (requests.RequestException, OSError, ValueError) as exc: checks["request_error"] = str(exc)
    print(json.dumps({"checks": checks}, indent=2)); raise SystemExit(0 if all(v is True for v in checks.values()) else 1)

if __name__ == "__main__": main()
