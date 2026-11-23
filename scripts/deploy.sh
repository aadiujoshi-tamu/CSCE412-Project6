#!/usr/bin/env bash
set -euo pipefail
: "${WEBSITE_BUCKET:?WEBSITE_BUCKET is required}"
aws s3 sync site/ "s3://${WEBSITE_BUCKET}/" --delete --exclude '.DS_Store'
