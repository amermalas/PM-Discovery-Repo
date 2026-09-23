# PM Discovery Lab — Publication Manifest

## Status

Published. This repository passed a full public-safety review before its initial public release (see Review Record). This manifest now serves as the standing public-safety policy for the repo and for any contributions to it.

## Review Record

- **2026-06-28 — Full public-safety review of all repository contents.** Every `SKILL.md`, every `agents/agent.yaml`, both reference files, all templates, plus `README.md`, `validation-plan.md`, and this manifest were read in full. **Result: cleared for public release.** No customer data, real company or product names, real source/ticket IDs, secrets, personal data, or local file paths were found. All examples are synthetic (the repo uses a fictional `DemoDesk` product and `SRC-001`/`EVID-001`-style synthetic identifiers).
- **2026-07-24 — Added four extended-workflow skills** (`competitive-analysis-intelligence`, `task-card-knowledge-builder`, `assistant-golden-evaluator`, `how-to-video-producer`), each rewritten from a private internal source into a generic, provider/vendor-neutral form. Every private company name, internal program name, internal file path, internal tool/platform name, and concrete script name was removed or replaced with a generic placeholder or a fill-in-your-own template file (`references/repo-map-template.md` in the two skills that need one). README, this manifest, and `validation-plan.md` were updated to match. **Result: cleared for public release.** No customer data, real company or product names, real source/ticket IDs, secrets, personal data, or local file paths were found in the new content.

- **2026-08-24 — Added three rigor/finishing skills** (`generic-claim-falsification`, `analog-peer-evidence`, `section-role-audit`) and updated seven existing skills (`painpoint-validation`, `customer-evidence-normalizer`, `opportunity-selection`, `opportunity-refinement`, `prototype-planning`, `disposable-prototype-builder`, `competitive-analysis-intelligence`) with methodology generalized from a private outside-in analysis. Every organization name, target name, sector detail, metric, and worked example from that analysis was removed; the new and updated content states methods only and carries no named company, product, number, or scenario drawn from the source work. `README.md` and `validation-plan.md` were updated to match, and `research/` was added to `.gitignore` so private analysis workspaces cannot be committed to this repo by accident. **Result: cleared for public release.** No customer data, real company or product names, real source/ticket IDs, secrets, personal data, or local file paths were found in the new content.

- **2026-09-22 — Added the 5-stage operating-loop skills** (`pm-sense`, `pm-listen`, `pm-ground`, `pm-prototype`, `pm-commit`) and one extended-workflow skill (`technical-writing-taskcard-bridge`), each rewritten from a private internal source. Internal skill names were remapped to their already-public equivalents (for example, references to an internal source-intake/taxonomy/evidence-allocation/prototype stack were rewritten to point at this repo's `source-intake`, `product-taxonomy-builder`, `customer-evidence-normalizer`, and `disposable-prototype-builder`/`prototype-planning`). Every private company name, internal platform/tool name (an internal AI-agent-configuration platform, an internal documentation wiki, an internal deployment hostname), internal derived-artifact filename, and internal folder path was removed or replaced with a generic description. A sixth candidate skill, tightly coupled to a named internal AI-agent-configuration platform's specific UI (playground/inspector-style tooling), was evaluated and intentionally not ported — its generic value was too thin relative to the sanitization effort required. `README.md`, `validation-plan.md`, and this manifest were updated to match. **Result: cleared for public release.** No customer data, real company or product names, real source/ticket IDs, secrets, personal data, or local file paths were found in the new content.

- **2026-09-23 — Added the `ai-brain` front-door skill**, which answers "what can this repo do" and "how do I build X" questions and routes users through the skills and templates to a finished deliverable. Its references hold a catalog of every skill, template, and script, and a set of deliverable recipes; `scripts/validate_skills.py` now fails if the catalog misses a skill or template. The content describes this repo only and contains no private material. **Result: cleared for public release.**

- **2026-09-23 — Added the 5-stage delivery loop and program-sense skills** (`tpm-frame`, `tpm-plan`, `tpm-align`, `tpm-run`, `tpm-land`) and nine supporting skills (`delivery-decomposition`, `risk-register`, `tradeoff-decision-brief`, `stakeholder-alignment`, `program-status-report`, `success-metric-tree`, `launch-readiness-review`, `program-recovery`, `program-retrospective`), eleven fill-in templates, four standard-library Python scripts under `scripts/`, and a synthetic program fixture under `examples/demodesk-program/`. The content is methods only, generalized from private interview-prep study notes and the author's own program-management practice. No course text, named instructor or candidate, employer, program, story, metric, or person from those notes was carried over; every example uses the fictional `DemoDesk` product with synthetic teams, dates, and `T-`/`R-`/`DEC-` identifiers. Two existing skills were brought in line with the validation plan's static checks (`pm-listen` gained an Outputs section; `technical-writing-taskcard-bridge` labels its boundaries), and `pm-commit` now hands off to `tpm-frame`. `README.md`, `validation-plan.md`, and this manifest were updated to match, and `scripts/validate_skills.py` now automates the static checks. **Result: cleared for public release.** No customer data, real company or product names, real source/ticket IDs, secrets, personal data, or local file paths were found in the new content.

## What's published

The public repository contains only:

- `README.md`
- `publication-manifest.md`
- `validation-plan.md`
- `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`
- `skills/`
- `templates/`
- `scripts/` (standard-library helpers that read your own CSVs; they make no network calls)
- `examples/` (synthetic fixtures only)

## What must never be added to this public repo

- validation plans or replay cases that reference real historical work
- simulation outputs or scorecards from private sources
- internal style kits or brand-specific prototype assets
- internal product taxonomy, customer evidence, or company knowledge exports
- generated prototypes that have not passed a public-safety review
- research workspaces derived from a real target organization, including any `research/` tree (gitignored for this reason)
- named-peer evidence tables, transfer-assumption grades, or falsification results produced against a real organization
- agent plans that include private platform names, real ticket IDs, local source paths, or customer-specific examples
- program plans, dependency maps, risk registers, decision logs, or status reports from a real program, including as examples or test fixtures

## Contribution & re-publication rule

Keep every example synthetic. Keep source evidence out of runtime prototype fixtures. Keep prototype code clearly marked as disposable and non-production. Re-run the `public-safety-review` skill on any change before it is merged. If a contribution includes customer evidence, private source paths, internal taxonomy, private platform architecture, or real tickets, it must be rewritten into a synthetic public example and reviewed again before it can be accepted.
