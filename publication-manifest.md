# PM Discovery Lab — Publication Manifest

## Status

Published. This repository passed a full public-safety review before its initial public release (see Review Record). This manifest now serves as the standing public-safety policy for the repo and for any contributions to it.

## Review Record

- **2026-06-28 — Full public-safety review of all repository contents.** Every `SKILL.md`, every `agents/agent.yaml`, both reference files, all templates, plus `README.md`, `validation-plan.md`, and this manifest were read in full. **Result: cleared for public release.** No customer data, real company or product names, real source/ticket IDs, secrets, personal data, or local file paths were found. All examples are synthetic (the repo uses a fictional `DemoDesk` product and `SRC-001`/`EVID-001`-style synthetic identifiers).
- **2026-07-24 — Added four extended-workflow skills** (`competitive-analysis-intelligence`, `task-card-knowledge-builder`, `assistant-golden-evaluator`, `how-to-video-producer`), each rewritten from a private internal source into a generic, provider/vendor-neutral form. Every private company name, internal program name, internal file path, internal tool/platform name, and concrete script name was removed or replaced with a generic placeholder or a fill-in-your-own template file (`references/repo-map-template.md` in the two skills that need one). README, this manifest, and `validation-plan.md` were updated to match. **Result: cleared for public release.** No customer data, real company or product names, real source/ticket IDs, secrets, personal data, or local file paths were found in the new content.

## What's published

The public repository contains only:

- `README.md`
- `publication-manifest.md`
- `validation-plan.md`
- `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`
- `skills/`
- `templates/`

## What must never be added to this public repo

- validation plans or replay cases that reference real historical work
- simulation outputs or scorecards from private sources
- internal style kits or brand-specific prototype assets
- internal product taxonomy, customer evidence, or company knowledge exports
- generated prototypes that have not passed a public-safety review
- agent plans that include private platform names, real ticket IDs, local source paths, or customer-specific examples

## Contribution & re-publication rule

Keep every example synthetic. Keep source evidence out of runtime prototype fixtures. Keep prototype code clearly marked as disposable and non-production. Re-run the `public-safety-review` skill on any change before it is merged. If a contribution includes customer evidence, private source paths, internal taxonomy, private platform architecture, or real tickets, it must be rewritten into a synthetic public example and reviewed again before it can be accepted.
