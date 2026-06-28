---
name: public-safety-review
description: Use before publishing a PM discovery artifact, public GitHub repo, article, screenshot, template, sample dataset, skill, or prototype. Checks for customer data, personal data, internal source IDs, secrets, proprietary taxonomy, brand assets, production claims, and other content that should not be public.
---

# Public Safety Review

Use this skill before external publication.

The goal is to decide whether an artifact is safe to publish, what must be redacted, and what should be rewritten with synthetic examples.

## Inputs

- artifact text, repo path, screenshot description, template, dataset, or prototype
- intended audience
- intended publication channel
- company-name usage decision

## Workflow

1. Identify public, internal, restricted, or unknown content.
2. Scan for:
   - customer names
   - people names
   - emails and domains
   - source-system IDs or links
   - secrets or credentials
   - internal product taxonomy
   - proprietary UI assets
   - roadmap commitments
   - production claims
3. Recommend redactions or synthetic replacements.
4. Classify the publication risk.
5. Assign severity to each finding:
   - P0: must remove before sharing
   - P1: must rewrite or replace with a synthetic example
   - P2: review recommended
   - P3: acceptable caveat
6. Produce a go/no-go recommendation.

## Output Contract

Return:

- publication target
- risk rating
- findings
- severity per finding
- required redactions
- synthetic replacements
- approval needs
- go/no-go recommendation

## Hard Boundaries

- When unsure, mark as not public-ready.
- Do not sanitize by simply removing names if the scenario remains identifiable.
- Do not approve screenshots with real customer data or internal source systems.
- Do not publish internal skills or templates without checking embedded paths and assumptions.
