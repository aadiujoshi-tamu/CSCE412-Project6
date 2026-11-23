#!/usr/bin/env bash
set -euo pipefail
aws codepipeline create-pipeline --cli-input-json file://pipeline/pipeline.json
