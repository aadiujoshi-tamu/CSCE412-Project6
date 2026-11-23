# Project 6 implementation notes

The repository contains a static site, pytest quality gates, CodePipeline configuration, CodeBuild build specifications, deployment scripts, production checks, and five evidence-first agent roles. The pipeline configuration contains explicit placeholders for the account-specific AWS resources and must be populated before deployment.

The pipeline never delegates deployment decisions to an LLM. Tests, release stamping, S3 deployment, CloudFront invalidation, verification, and the known-good release pointer are deterministic. The recovery role can identify a bounded rollback target; infrastructure changes require an interactive approval.
