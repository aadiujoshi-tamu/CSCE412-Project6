# Reliable Static-Site Delivery

This project deploys the contents of `site/` through CodePipeline: GitHub Source → CodeBuild test/stamp → CodeBuild deploy to private S3 origin → CloudFront invalidation → CodeBuild production verification. Every release is stamped with its commit SHA and recorded under `deployments/<sha>.json`.

## Setup

Copy `.env.example` to `.env`, fill in `AWS_REGION`, `WEBSITE_BUCKET`, `ARTIFACT_BUCKET`, `CLOUDFRONT_DISTRIBUTION_ID`, `SITE_DOMAIN`, and `GITHUB_CONNECTION_ARN`, then create the CodeBuild projects referenced by `pipeline/pipeline.json`. Replace all `REPLACE_*` fields before `bash pipeline/create_pipeline.sh`.

`python -m pytest -q` runs the content checks. A push to `main` triggers the CodeStar-connected Source stage.

## Agents and safety

The orchestrator coordinates pipeline engineering, test, production verification, diagnosis, and recovery agents. Their messages use Pydantic schemas and preserve raw evidence on malformed inputs. AI is advisory only: tests, release stamping, deployment, verification, and bounded rollback are deterministic. Any infrastructure proposal requires `agents.approvals.require_approval`.

## IAM

Attach `pipeline/iam-policies/codepipeline.json` to the pipeline role and `codebuild-deploy.json` to deployment/verification CodeBuild roles, replacing placeholder bucket names. Do not commit `.env`, keys, PEM files, or credentials. Before submission run `git log -p | grep -i key` and add required TA collaborators.
